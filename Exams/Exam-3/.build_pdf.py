"""Convert exam-3-sample-questions-with-answers.md -> HTML with print-friendly CSS.

Run this, then use Chrome headless to render the HTML to PDF.
"""
from pathlib import Path
import markdown

HERE = Path(__file__).parent
SRC = HERE / "exam-3-sample-questions-with-answers.md"
OUT_HTML = HERE / ".exam-3-sample-questions-with-answers.html"

CSS = r"""
@page {
  size: Letter;
  margin: 0.75in 0.85in 0.85in 0.85in;
  @bottom-center {
    content: "Page " counter(page) " of " counter(pages);
    font-family: 'Charter', 'Georgia', serif;
    font-size: 9pt;
    color: #555;
  }
}

html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }

body {
  font-family: 'Charter', 'Iowan Old Style', 'Georgia', 'Times New Roman', serif;
  font-size: 11pt;
  line-height: 1.45;
  color: #111;
  max-width: 100%;
  margin: 0;
  padding: 0;
  hyphens: auto;
}

h1 {
  font-size: 22pt;
  font-weight: 700;
  margin: 0 0 0.4em 0;
  color: #111;
  border-bottom: 2px solid #111;
  padding-bottom: 0.2em;
}
h2 {
  font-size: 16pt;
  font-weight: 700;
  margin: 0.2em 0 0.6em 0;
  color: #1a3a6c;
  border-bottom: 1px solid #bbb;
  padding-bottom: 0.18em;
  page-break-after: avoid;
}
h3 {
  font-size: 12.5pt;
  font-weight: 700;
  margin: 1.0em 0 0.4em 0;
  color: #333;
  page-break-after: avoid;
}
h3.answer-heading {
  color: #0a5e2a;
  border-top: 1px dotted #aaa;
  padding-top: 0.4em;
}

p { margin: 0.45em 0; }
ul, ol { margin: 0.4em 0 0.6em 1.4em; padding: 0; }
li { margin: 0.18em 0; }

strong { color: #111; }
em { color: #333; }

code {
  font-family: 'JetBrains Mono', 'SF Mono', 'Menlo', 'Consolas', monospace;
  font-size: 0.92em;
  background: #f3f3f3;
  border: 1px solid #e1e1e1;
  border-radius: 3px;
  padding: 0.05em 0.35em;
}
pre {
  background: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 0.6em 0.8em;
  font-size: 9.5pt;
  line-height: 1.35;
  page-break-inside: avoid;
  overflow-x: auto;
}
pre code { background: transparent; border: 0; padding: 0; }

table {
  border-collapse: collapse;
  margin: 0.7em 0;
  width: 100%;
  font-size: 10pt;
  page-break-inside: avoid;
}
th, td {
  border: 1px solid #999;
  padding: 4px 7px;
  text-align: left;
  vertical-align: top;
}
th { background: #eef0f4; font-weight: 700; }
tr:nth-child(even) td { background: #fafafa; }

blockquote {
  border-left: 3px solid #1a3a6c;
  margin: 0.7em 0;
  padding: 0.1em 0.9em;
  background: #f3f6fb;
  color: #333;
  font-size: 10.5pt;
}

hr {
  border: none;
  border-top: 1px solid #bbb;
  margin: 0.8em 0;
}

/* Cover / TOC */
.toc table { font-size: 10.5pt; }
.toc td:first-child { width: 3.5em; font-weight: 700; }
.toc td:last-child { text-align: right; width: 3.5em; }

/* Each Q section starts a fresh page */
h2 { page-break-before: always; }
h2:first-of-type { page-break-before: auto; } /* allow first H2 on cover (none) */

/* Make sure code/tables don't split awkwardly */
table, pre, blockquote { break-inside: avoid; }
"""

HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
{css}
</style>
</head>
<body>
{body}
</body>
</html>
"""


def main() -> None:
    md_text = SRC.read_text(encoding="utf-8")

    md = markdown.Markdown(
        extensions=[
            "tables",
            "fenced_code",
            "codehilite",
            "sane_lists",
            "attr_list",
            "md_in_html",
        ],
        extension_configs={
            "codehilite": {"guess_lang": False, "noclasses": True},
        },
    )
    body_html = md.convert(md_text)

    # Wrap the TOC table for nicer styling.
    body_html = body_html.replace(
        "<h2>Table of Contents</h2>",
        '<h2 class="toc-heading">Table of Contents</h2><div class="toc">',
        1,
    )
    # Close the toc div before the first page break div after the TOC.
    body_html = body_html.replace(
        '<div style="page-break-after: always;"></div>',
        '</div><div style="page-break-after: always;"></div>',
        1,
    )

    # Tag the "Answer" h3 headings so we can color them green.
    body_html = body_html.replace("<h3>Answer</h3>", '<h3 class="answer-heading">Answer</h3>')

    html = HTML_TEMPLATE.format(
        title="W4111 Spring 2026 — Exam 3 Sample Questions & Answers",
        css=CSS,
        body=body_html,
    )
    OUT_HTML.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT_HTML}")


if __name__ == "__main__":
    main()
