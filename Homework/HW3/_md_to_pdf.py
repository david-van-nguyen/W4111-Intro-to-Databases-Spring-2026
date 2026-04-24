"""Render a Markdown file to a print-friendly PDF using markdown-pdf.

Usage: python _md_to_pdf.py <file.md> [<file.md> ...]
"""
from __future__ import annotations

import sys
from pathlib import Path

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
"""


def convert_one(md_path: Path) -> Path:
    text = md_path.read_text(encoding="utf-8")
    pdf = MarkdownPdf(toc_level=0, optimize=True)
    pdf.meta["title"] = md_path.stem.replace("_", " ")
    pdf.meta["author"] = "W4111 study materials"
    pdf.add_section(Section(text, toc=False), user_css=CSS)
    out = md_path.with_suffix(".pdf")
    pdf.save(str(out))
    return out


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python _md_to_pdf.py <file.md> [...]", file=sys.stderr)
        sys.exit(2)
    for raw in sys.argv[1:]:
        p = Path(raw)
        if not p.exists():
            print(f"skip (not found): {p}", file=sys.stderr)
            continue
        out = convert_one(p)
        size_kb = out.stat().st_size // 1024
        print(f"  {p.name} -> {out.name} ({size_kb} KB)")


if __name__ == "__main__":
    main()
