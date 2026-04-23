"""Render Exam2_SampleQuestions.md to a PDF with:
  - a real bookmark outline (toc_level=3), and
  - a *printed* table of contents with page numbers, injected into the
    markdown between the <!-- TOC:START --> / <!-- TOC:END --> markers.

The script renders in up to 3 passes to let the page numbers in the TOC
stabilize (adding numbers can shift pagination by one page the first time).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pymupdf
from markdown_pdf import MarkdownPdf, Section

CSS = """
@page { size: Letter; margin: 0.75in; }
body {
  font-family: -apple-system, "Helvetica Neue", Arial, sans-serif;
  font-size: 10.5pt;
  line-height: 1.45;
  color: #1a1a1a;
}
h1 { color: #00684A; border-bottom: 2px solid #00684A;
     padding-bottom: 0.2em; margin-top: 0.6em; }
h2 { color: #00684A; border-bottom: 1px solid #ccc;
     padding-bottom: 0.1em; margin-top: 1.2em; }
h3 { color: #004d37; margin-top: 1em; }
h4 { color: #004d37; }
code { font-family: "SF Mono", Menlo, Consolas, monospace;
       background: #f4f4f4; padding: 1px 4px; border-radius: 3px;
       font-size: 0.88em; }
pre { background: #f4f4f4; padding: 0.6em; border-radius: 4px;
      overflow-x: auto; font-size: 0.85em; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; margin: 0.75em 0; width: 100%; font-size: 0.92em; }
th, td { border: 1px solid #bbb; padding: 5px 8px;
         text-align: left; vertical-align: top; }
th { background: #eef5f2; }
blockquote { border-left: 4px solid #00684A; margin: 1em 0;
             padding: 0.1em 1em; color: #444; background: #f9f9f9; }
hr { border: none; border-top: 1px solid #ccc; margin: 1.2em 0; }
ul, ol { margin-left: 1.2em; }
.toc-part { color: #00684A; font-weight: 600; margin-top: 0.9em; }
"""

# ---- Question → section/focus metadata (same ordering as the MD body) ----

PART_A_SECTIONS: list[tuple[str, str, list[tuple[str, str]]]] = [
    ("A.1", "`$match` — filter-only", [
        ("Q1",  "Simple equality filter on nested field"),
        ("Q2",  "Compound filter with range + `$in`"),
        ("Q3",  "Regex / existence filter"),
    ]),
    ("A.2", "`$project` — reshape & compute", [
        ("Q4",  "Rename, drop `_id`, lift nested fields"),
        ("Q5",  "Computed column (`$cond` / `$switch`)"),
    ]),
    ("A.3", "`$sort` + `$limit` — Top-N", [
        ("Q6",  "Top 10 most expensive line items"),
    ]),
    ("A.4", "`$count` — stage vs. accumulator", [
        ("Q7",  "Count documents matching a filter"),
        ("Q8",  "Per-group counts with `$sum: 1`"),
    ]),
    ("A.5", "`$unwind` — arrays to rows", [
        ("Q9",  "Flatten `orderDetails` into line items"),
        ("Q10", "`preserveNullAndEmptyArrays` (LEFT-JOIN)"),
    ]),
    ("A.6", "`$group` — aggregation", [
        ("Q11", "Revenue per order"),
        ("Q12", "Distinct customer count per status"),
        ("Q13", "Top 3 best-selling products"),
    ]),
    ("A.7", "`$lookup` — joins", [
        ("Q14", "Orders with customer name + country"),
        ("Q15", "Customers without any orders (anti-join)"),
    ]),
    ("A.8", "Kitchen-sink pipelines", [
        ("Q16", "Top 5 customers by revenue (uses all 8)"),
        ("Q17", "Revenue by country (two `$group`s + `$lookup`)"),
        ("Q18", "Argmax per group — biggest order per status"),
    ]),
]

PART_B_ROWS: list[tuple[str, str]] = [
    ("Q19", "Return every actor and their movies"),
    ("Q20", "Directors who also acted in the same movie"),
    ("Q21", "Co-actors of Tom Hanks (triangle pattern)"),
    ("Q22", "Aggregation with `HAVING`-style filter (`WITH`)"),
    ("Q23", "Filter on a relationship property (`roles`)"),
    ("Q24", "`UNWIND` a list property"),
    ("Q25", "Shortest path / Bacon number"),
    ("Q26", "Variable-length relationship (`-[:FOLLOWS*2]->`)"),
    ("Q27", "Aggregating on an edge property (`REVIEWED.rating`)"),
]

PART_C_ROWS: list[tuple[str, str]] = [
    ("Q28", "SQL → MQL translation (`WHERE` / `GROUP BY` / `HAVING`)"),
    ("Q29", "Why `$lookup` is almost always followed by `$unwind`"),
    ("Q30", "`$count` stage vs. `{ $sum: 1 }` inside `$group`"),
    ("Q31", "Cypher arrow direction and when to omit it"),
]

# Q## → heading-text prefix used to search the bookmark outline
# (we match by "Q##." at start of the outline title)


def extract_question_pages(pdf_path: Path) -> dict[str, int]:
    """Return {'Q1': 2, 'Q2': 3, ...} by reading the PDF bookmark outline."""
    doc = pymupdf.open(str(pdf_path))
    mapping: dict[str, int] = {}
    for _lvl, title, page in doc.get_toc():
        m = re.match(r"^(Q\d+)\.", title.strip())
        if m:
            mapping[m.group(1)] = page
    doc.close()
    return mapping


def build_toc_markdown(pages: dict[str, int] | None) -> str:
    """Build the TOC section. If pages is None/empty, page column shows '—'."""
    def pg(q: str) -> str:
        if not pages or q not in pages:
            return "—"
        return str(pages[q])

    lines: list[str] = []
    lines.append("## Table of Contents (with page numbers)")
    lines.append("")
    lines.append("> Tip: the PDF also has a **clickable bookmark outline** "
                 "(open the \"Outline\" / \"Bookmarks\" panel in your reader). "
                 "The page numbers below are for the printed copy.")
    lines.append("")

    lines.append("### Part A — MongoDB (`classicmodels`)")
    lines.append("")
    lines.append("| § | Focus | Q# | Question | Page |")
    lines.append("|---|---|---|---|---:|")
    for sec_num, sec_title, rows in PART_A_SECTIONS:
        for i, (q, title) in enumerate(rows):
            sec_cell = f"**{sec_num}** {sec_title}" if i == 0 else ""
            lines.append(f"| {sec_cell} | | {q} | {title} | {pg(q)} |")
    lines.append("")

    lines.append("### Part B — Neo4j (Movie Database)")
    lines.append("")
    lines.append("| Q# | Focus | Page |")
    lines.append("|---|---|---:|")
    for q, title in PART_B_ROWS:
        lines.append(f"| {q} | {title} | {pg(q)} |")
    lines.append("")

    lines.append("### Part C — Conceptual / Short-Answer")
    lines.append("")
    lines.append("| Q# | Focus | Page |")
    lines.append("|---|---|---:|")
    for q, title in PART_C_ROWS:
        lines.append(f"| {q} | {title} | {pg(q)} |")
    lines.append("")
    return "\n".join(lines)


TOC_START = "<!-- TOC:START -->"
TOC_END = "<!-- TOC:END -->"
TOC_RE = re.compile(
    re.escape(TOC_START) + r".*?" + re.escape(TOC_END), re.DOTALL
)


def inject_toc(md_text: str, toc_md: str) -> str:
    block = f"{TOC_START}\n{toc_md}\n{TOC_END}"
    if TOC_RE.search(md_text):
        return TOC_RE.sub(block, md_text)
    # First run: no markers in file yet — tell the user.
    raise SystemExit(
        "ERROR: markdown file must contain the markers\n"
        f"  {TOC_START}\n  {TOC_END}\n"
        "around the region where the printed TOC should live."
    )


def render(md_path: Path, out_path: Path) -> None:
    text = md_path.read_text(encoding="utf-8")
    pdf = MarkdownPdf(toc_level=3, optimize=True)
    pdf.meta["title"] = "Exam 2 — Sample Questions"
    pdf.meta["author"] = "W4111 study materials"
    pdf.add_section(Section(text, toc=True), user_css=CSS)
    pdf.save(str(out_path))


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python _md_to_pdf_exam2.py <file.md>", file=sys.stderr)
        sys.exit(2)
    md_path = Path(sys.argv[1])
    out_path = md_path.with_suffix(".pdf")

    # Pass 1: render with whatever TOC is currently in the file (may have '—').
    render(md_path, out_path)

    # Iterate so page numbers in the TOC stabilize.
    previous: dict[str, int] = {}
    for attempt in range(8):
        pages = extract_question_pages(out_path)
        if pages == previous and pages:
            stabilized = True
            break
        previous = pages

        new_toc = build_toc_markdown(pages)
        text = md_path.read_text(encoding="utf-8")
        text = inject_toc(text, new_toc)
        md_path.write_text(text, encoding="utf-8")

        render(md_path, out_path)
    else:
        stabilized = False

    size_kb = out_path.stat().st_size // 1024
    status = "stabilized" if stabilized else "did NOT stabilize"
    print(f"  {md_path.name} -> {out_path.name} ({size_kb} KB); "
          f"TOC {status} after {attempt + 1} pass(es)")


if __name__ == "__main__":
    main()
