"""
Build HW3_Exam_Study_Guide.pdf with a printable table of contents.

Pipeline:
  1. Render the MD study guide to an HTML body (via _md_to_html.py).
  2. Use headless Chrome to produce the BODY PDF.
  3. Walk the BODY PDF with PyMuPDF and extract the page number where each
     H1 / H2 / H3 heading first appears (detected by font size + color).
  4. Build a TOC HTML page with those page numbers shifted by the estimated
     TOC length.
  5. Render the TOC HTML to a TOC PDF via headless Chrome.
  6. If the TOC's real page count differs from the estimate, regenerate.
  7. Concatenate TOC PDF + BODY PDF, add bookmarks, save as the final PDF.

The main body's layout is never touched after the first render, so the
heading-to-page mapping extracted in step 3 is stable.
"""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

import pymupdf


HERE = Path(__file__).resolve().parent
MD_PATH = HERE / "HW3_Exam_Study_Guide.md"
HTML_PATH = HERE / "HW3_Exam_Study_Guide.html"
BODY_PDF = HERE / "_body.pdf"
TOC_PDF = HERE / "_toc.pdf"
FINAL_PDF = HERE / "HW3_Exam_Study_Guide.pdf"

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


TOC_CSS = """
@page { size: Letter; margin: 0.75in; }
body {
  font-family: -apple-system, "Helvetica Neue", Arial, sans-serif;
  font-size: 11pt;
  color: #1a1a1a;
  line-height: 1.35;
}
h1.toc-title {
  color: #00684A;
  border-bottom: 2px solid #00684A;
  padding-bottom: 0.25em;
  margin: 0 0 1em 0;
  font-size: 22pt;
}
ul.toc { list-style: none; padding: 0; margin: 0; }
ul.toc li { margin: 0; padding: 0; }
.toc-row {
  display: flex;
  align-items: baseline;
  padding: 2px 0;
}
.toc-row .title { flex: 0 0 auto; padding-right: 0.5em; }
.toc-row .dots  { flex: 1 1 auto;
                  border-bottom: 1px dotted #888;
                  margin: 0 0.4em; transform: translateY(-3px); }
.toc-row .page  { flex: 0 0 auto; padding-left: 0.5em;
                  font-variant-numeric: tabular-nums; color: #444; }
.lvl-1 { margin-top: 0.6em; font-weight: 700; color: #00684A; font-size: 12pt; }
.lvl-2 { padding-left: 1.25em; }
.lvl-3 { padding-left: 2.5em; color: #333; font-size: 10pt; }
code { font-family: "SF Mono", Menlo, Consolas, monospace;
       background: #f4f4f4; padding: 1px 4px; border-radius: 3px;
       font-size: 0.9em; }
"""


def run_chrome_print(html_file: Path, out_pdf: Path) -> None:
    subprocess.run(
        [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            f"--print-to-pdf={out_pdf}",
            f"file://{html_file}",
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def extract_md_headings(md_text: str) -> list[tuple[int, str]]:
    """Parse the source MD for H1/H2/H3 (in order), skipping code fences."""
    headings: list[tuple[int, str]] = []
    in_code = False
    for raw in md_text.splitlines():
        stripped = raw.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^(#{1,3})\s+(.+?)\s*$", raw)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            headings.append((level, title))
    return headings


def strip_md_formatting(title: str) -> str:
    """Turn a markdown heading into its plain-text rendered form."""
    t = title
    t = re.sub(r"`([^`]+)`", r"\1", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"\1", t)
    t = re.sub(r"\*([^*]+)\*", r"\1", t)
    return t


def _search_candidates(plain: str) -> list[str]:
    """Return progressively shorter / looser search strings.

    Useful when PyMuPDF's literal search fails due to line wraps or
    weird punctuation rendering in the PDF."""
    cands = [plain]
    # split on em-dash variants (— – --) -> first chunk
    for sep in (" — ", " – ", " -- ", " - "):
        if sep in plain:
            cands.append(plain.split(sep, 1)[0].strip())
            break
    # take first ~5 words
    words = plain.split()
    if len(words) > 5:
        cands.append(" ".join(words[:5]))
    if len(words) > 3:
        cands.append(" ".join(words[:3]))
    if len(words) > 1:
        cands.append(words[0])
    # dedupe while preserving order
    seen: set[str] = set()
    out: list[str] = []
    for c in cands:
        if c and c not in seen:
            seen.add(c)
            out.append(c)
    return out


def find_heading_pages(
    pdf_path: Path, headings: list[tuple[int, str]]
) -> list[tuple[int, str, int]]:
    """For each heading, locate its first occurrence in the PDF body.

    We scan in document order, only searching forward from the last-found
    page, so duplicate heading texts resolve to the correct occurrence.
    """
    doc = pymupdf.open(pdf_path)
    result: list[tuple[int, str, int]] = []
    cursor = 0
    for level, title in headings:
        plain = strip_md_formatting(title)
        found_page: int | None = None
        for candidate in _search_candidates(plain):
            for page_num in range(cursor, doc.page_count):
                if doc[page_num].search_for(candidate, quads=False):
                    found_page = page_num
                    cursor = page_num
                    break
            if found_page is not None:
                break
        if found_page is None:
            for candidate in _search_candidates(plain):
                for page_num in range(doc.page_count):
                    if doc[page_num].search_for(candidate, quads=False):
                        found_page = page_num
                        break
                if found_page is not None:
                    break
        if found_page is None:
            print(f"  WARN: could not locate heading: {title!r}", file=sys.stderr)
            continue
        result.append((level, title, found_page + 1))  # 1-indexed
    doc.close()
    return result


def build_toc_html(
    entries: list[tuple[int, str, int]], toc_page_offset: int
) -> str:
    """Render a TOC page. `toc_page_offset` is added to each page number to
    account for the TOC pages that will be prepended to the body PDF."""
    rows: list[str] = []
    for level, title, page in entries:
        shifted = page + toc_page_offset
        title_html = re.sub(
            r"`([^`]+)`", r"<code>\1</code>", title
        )
        title_html = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", title_html)
        title_html = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", title_html)
        rows.append(
            f'<li class="toc-row lvl-{level}">'
            f'<span class="title">{title_html}</span>'
            f'<span class="dots"></span>'
            f'<span class="page">{shifted}</span>'
            f"</li>"
        )
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Table of Contents</title>
<style>{TOC_CSS}</style></head>
<body>
<h1 class="toc-title">Table of Contents</h1>
<ul class="toc">
{chr(10).join(rows)}
</ul>
</body></html>
"""


def render_toc_pdf(entries: list[tuple[int, str, int]], offset: int) -> int:
    html = build_toc_html(entries, offset)
    with tempfile.NamedTemporaryFile(
        "w", suffix=".html", delete=False, dir=str(HERE)
    ) as f:
        f.write(html)
        tmp = Path(f.name)
    try:
        run_chrome_print(tmp, TOC_PDF)
    finally:
        tmp.unlink(missing_ok=True)
    doc = pymupdf.open(TOC_PDF)
    n = doc.page_count
    doc.close()
    return n


def add_page_numbers(doc: pymupdf.Document) -> None:
    """Stamp 'Page N of M' centered at the bottom of every page."""
    total = doc.page_count
    for i, page in enumerate(doc, start=1):
        label = f"Page {i} of {total}"
        rect = page.rect
        font_size = 9
        text_width = pymupdf.get_text_length(
            label, fontname="helv", fontsize=font_size
        )
        x = (rect.width - text_width) / 2
        y = rect.height - 28  # ~0.39in from bottom (within 0.75in margin)
        page.insert_text(
            (x, y),
            label,
            fontname="helv",
            fontsize=font_size,
            color=(0.4, 0.4, 0.4),
        )


def merge_with_toc_bookmarks(
    toc_pdf: Path,
    body_pdf: Path,
    out_pdf: Path,
    entries: list[tuple[int, str, int]],
    toc_page_count: int,
) -> None:
    final = pymupdf.open()
    final.insert_pdf(pymupdf.open(toc_pdf))
    final.insert_pdf(pymupdf.open(body_pdf))

    add_page_numbers(final)

    toc_items: list[list] = [[1, "Table of Contents", 1]]
    prev_level = 1
    for level, title, page in entries:
        plain = strip_md_formatting(title)
        safe_level = min(level, prev_level + 1)
        toc_items.append([safe_level, plain, page + toc_page_count])
        prev_level = safe_level
    final.set_toc(toc_items)
    final.save(out_pdf, garbage=3, deflate=True)
    final.close()


def main() -> None:
    print("[1/6] md -> html (body)")
    subprocess.run(
        [sys.executable, str(HERE / "_md_to_html.py"), str(MD_PATH)],
        check=True,
    )

    print("[2/6] html -> body pdf (headless Chrome)")
    run_chrome_print(HTML_PATH, BODY_PDF)

    print("[3/6] extract heading page numbers from body PDF")
    md_text = MD_PATH.read_text(encoding="utf-8")
    headings = extract_md_headings(md_text)
    entries = find_heading_pages(BODY_PDF, headings)
    body_page_count = pymupdf.open(BODY_PDF).page_count
    print(f"      body pages = {body_page_count}; headings found = {len(entries)}")

    print("[4/6] render TOC pdf (iterate until TOC length stabilizes)")
    toc_pages = 2  # first estimate
    for attempt in range(1, 5):
        actual = render_toc_pdf(entries, offset=toc_pages)
        print(f"      attempt {attempt}: estimated {toc_pages}, got {actual}")
        if actual == toc_pages:
            break
        toc_pages = actual
    else:
        print("      WARN: TOC page count didn't stabilize in 4 iterations")

    print(f"[5/6] merge TOC ({toc_pages} pages) + body ({body_page_count} pages)")
    merge_with_toc_bookmarks(TOC_PDF, BODY_PDF, FINAL_PDF, entries, toc_pages)

    print("[6/6] cleanup")
    BODY_PDF.unlink(missing_ok=True)
    TOC_PDF.unlink(missing_ok=True)

    final = pymupdf.open(FINAL_PDF)
    kb = FINAL_PDF.stat().st_size // 1024
    print(f"done: {FINAL_PDF.name} -> {final.page_count} pages, {kb} KB")
    final.close()


if __name__ == "__main__":
    main()
