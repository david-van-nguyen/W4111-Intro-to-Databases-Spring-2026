"""Convert one or more markdown files to styled, link-free HTML.

Usage:
    python _md_to_html.py <file_or_dir> [<file_or_dir> ...]

For each .md file given (directories are searched recursively), writes a
sibling .html file with:
  - all hyperlinks removed (link text preserved)
  - raw URLs stripped
  - MongoDB-green styling tuned for printing to PDF
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import markdown

CSS = """
@page { size: Letter; margin: 0.75in; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif;
  font-size: 11pt;
  line-height: 1.5;
  color: #222;
  max-width: 8.5in;
  margin: 1em auto;
  padding: 0 1em;
}
h1, h2, h3, h4 { color: #00684A; page-break-after: avoid; }
h1 { border-bottom: 2px solid #00684A; padding-bottom: 0.2em; }
h2 { border-bottom: 1px solid #ccc; padding-bottom: 0.15em; margin-top: 1.5em; }
code {
  font-family: "SF Mono", Menlo, Consolas, monospace;
  background: #f4f4f4;
  padding: 1px 4px;
  border-radius: 3px;
  font-size: 0.9em;
}
pre {
  background: #f4f4f4;
  padding: 0.75em;
  border-radius: 4px;
  overflow-x: auto;
  white-space: pre-wrap;
  word-wrap: break-word;
  page-break-inside: avoid;
  font-size: 0.85em;
}
pre code { background: none; padding: 0; white-space: pre-wrap; }
table {
  border-collapse: collapse;
  margin: 1em 0;
  width: 100%;
  page-break-inside: avoid;
}
th, td {
  border: 1px solid #bbb;
  padding: 6px 10px;
  text-align: left;
  vertical-align: top;
}
th { background: #eef5f2; }
blockquote {
  border-left: 4px solid #00684A;
  margin: 1em 0;
  padding: 0.2em 1em;
  color: #555;
  background: #f9f9f9;
}
.codehilite { background: #f4f4f4; }
"""


def strip_markdown_links(md_text: str) -> str:
    """Remove markdown/URL syntax so nothing renders as a hyperlink."""
    md_text = re.sub(r"^Source URL:\s*\S+\s*$", "", md_text, flags=re.MULTILINE)
    md_text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", md_text)
    md_text = re.sub(r"\[([^\]]+)\]\(<[^>]+>\)", r"\1", md_text)
    md_text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", md_text)
    md_text = re.sub(r"\[([^\]]+)\]\[[^\]]*\]", r"\1", md_text)
    md_text = re.sub(r"(?m)^\s*\[[^\]]+\]:\s+\S.*$", "", md_text)
    md_text = re.sub(r"<(https?://[^>]+)>", "", md_text)
    md_text = re.sub(r"https?://\S+", "", md_text)
    return md_text


def strip_html_anchors(html: str) -> str:
    return re.sub(
        r"<a\b[^>]*>(.*?)</a>", r"\1", html, flags=re.IGNORECASE | re.DOTALL
    )


def convert_one(md_path: Path) -> Path:
    md_text = md_path.read_text(encoding="utf-8")
    md_text = strip_markdown_links(md_text)

    body = markdown.markdown(
        md_text,
        extensions=["fenced_code", "tables", "codehilite", "sane_lists"],
        extension_configs={
            "codehilite": {"guess_lang": False, "css_class": "codehilite"},
        },
    )
    body = strip_html_anchors(body)

    html = (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        f"<title>{md_path.stem}</title>\n"
        f"<style>{CSS}</style>\n"
        "</head>\n<body>\n"
        f"{body}\n"
        "</body>\n</html>\n"
    )

    out = md_path.with_suffix(".html")
    out.write_text(html, encoding="utf-8")
    return out


def collect_md(paths: list[str]) -> list[Path]:
    files: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if p.is_dir():
            files.extend(sorted(p.rglob("*.md")))
        elif p.is_file() and p.suffix.lower() == ".md":
            files.append(p)
    return files


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python _md_to_html.py <file_or_dir> [...]", file=sys.stderr)
        sys.exit(2)

    md_files = collect_md(sys.argv[1:])
    if not md_files:
        print("No .md files found.", file=sys.stderr)
        sys.exit(1)

    for md in md_files:
        out = convert_one(md)
        size_kb = out.stat().st_size // 1024
        print(f"  {md.name} -> {out.name} ({size_kb} KB)")


if __name__ == "__main__":
    main()
