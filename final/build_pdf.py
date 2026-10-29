"""Build final/coalition_statement.pdf from the final/*.md sources.

Usage: python3 final/build_pdf.py <fonts_dir>
First pages: the three television statements (government leaders, Ra'am, Joint List),
each in its original language with the other two versions beside it.
Then: the full framework in each language. Last: one signature page per tier, recording who declined.
"""
import base64
import json
import pathlib
import re
import subprocess
import sys

import markdown

ROOT = pathlib.Path(__file__).resolve().parent
FONTS = pathlib.Path(sys.argv[1])


def font_face(family, file, weight):
    data = base64.b64encode((FONTS / file).read_bytes()).decode()
    return (f"@font-face{{font-family:'{family}';font-weight:{weight};"
            f"src:url(data:font/woff2;base64,{data}) format('woff2');}}")


def md(text):
    text = re.sub(r"</?div[^>]*>", "", text)
    # Python-Markdown needs a blank line before a list that follows a paragraph line.
    text = re.sub(r"(?m)^((?![ \t]*(?:[-*] |\d+\. |\|)).+)\n(?=[ \t]*[-*] )", r"\1\n\n", text)
    return markdown.markdown(text, extensions=["tables"])


def tv_section(statement, lang_heading):
    """Text of one statement ("(a)", "(b)", "(c)") in one language from tv_statement.md."""
    src = (ROOT / "tv_statement.md").read_text()
    part = src.split(f"## {statement}", 1)[1].split("\n## ", 1)[0].split("\n---", 1)[0]
    title = part.split("\n", 1)[0].strip()
    block = part.split(f"### {lang_heading}", 1)[1]
    label = block.split("\n", 1)[0].strip()
    block = block.split("\n", 1)[1].split("\n### ", 1)[0].split("\n**", 1)[0]
    block = "\n".join(l[2:] if l.startswith("> ") else l.lstrip(">") for l in block.splitlines())
    return title, f"{lang_heading} {label}".strip(), md(block)


def tv_page(statement, order):
    cols = []
    for lang in order:
        title, label, body = tv_section(statement, lang)
        cls = {"עברית": "col he", "العربية": "col ar", "English": "col"}[lang]
        cols.append(f'<div class="{cls}"><h3>{label}</h3>{body}</div>')
    return f'<h2>{statement} {title}</h2><div class="cols">{"".join(cols)}</div>'


def framework(file):
    text = (ROOT / file).read_text()
    text = text.split("\n---\n*", 1)[0]  # drop simulation footer; restated once in the PDF
    # Clause numbers are not a Markdown list: render "12." / "6a." as bold paragraph labels so numbering never restarts.
    # Sources indent sub-bullets by 3 or 6 spaces; Python-Markdown nests on 4.
    lines, out = text.splitlines(), []
    for i, line in enumerate(lines):
        indent = len(line) - len(line.lstrip(" "))
        body = line.strip()
        m = re.match(r"^(\d+[a-zא-ת؀-ۿ]?)\. (.*)", body) if indent == 0 else None
        if m:
            out += ["", f"**{m.group(1)}.** {m.group(2)}"]
            continue
        is_item = body.startswith("- ")
        if is_item and out and out[-1].strip() and not out[-1].lstrip().startswith("- "):
            out.append("")
        if not is_item and out and out[-1].lstrip().startswith("- ") and body and indent < 6:
            out.append("")
        out.append(("    " if indent >= 6 else "") + body)
        if body.startswith("**") and i + 1 < len(lines) and lines[i + 1].startswith("**"):
            out[-1] += "  "
    return md("\n".join(out))


STATUS = md((ROOT / "tv_statement.md").read_text().split("## Status", 1)[1].split("\n---", 1)[0])
TIERS = json.loads((ROOT / "signatories.json").read_text())


def sig_block(s):
    return f"""
<div class="sig">
  <div class="sig-name">{" · ".join(f"<bdi>{n}</bdi>" for n in s['name'].split(" · "))}</div>
  <div class="sig-party"><bdi>{s['party_en']}</bdi> · <bdi>{s['party_he']}</bdi> · <bdi>{s['party_ar']}</bdi></div>
  <div class="sig-scope">{s['scope']}</div>
  {'<div class="sig-declined">Declined to sign · סירב לחתום · رفض التوقيع</div>' if s.get('declined') else '<div class="sig-line"></div><div class="sig-labels"><span>Signature · חתימה · التوقيع</span><span>Date · תאריך · التاريخ</span></div>'}
</div>"""


# One page per tier: the government parties will not sign on the same page as the Arab factions' replies.
sig_pages = "".join(f"""
<div class="part">
  <h1>Signatures · חתימות · التوقيعات ({i}/{len(TIERS)})</h1>
  <h2>{t['tier_en']}</h2>
  <p class="he">{t['tier_he']}</p>
  <p class="ar">{t['tier_ar']}</p>
  <div class="sig-grid">{"".join(sig_block(s) for s in t['signers'])}</div>
  <div class="note">This document is a simulation exercise based on the parties' public positions. It does not speak for any party.<br>
  <span class="he">מסמך זה הוא תרגיל סימולציה המבוסס על עמדותיהן הפומביות של המפלגות, ואינו מדבר בשם אף מפלגה.</span><br>
  <span class="ar">هذه الوثيقة تمرين محاكاة يستند إلى المواقف العلنية للأحزاب، ولا تتحدث باسم أي حزب.</span></div>
</div>""" for i, t in enumerate(TIERS, 1))

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
{font_face('NotoSans','noto-sans-latin-400-normal.woff2',400)}
{font_face('NotoSans','noto-sans-latin-700-normal.woff2',700)}
{font_face('NotoHeb','noto-sans-hebrew-hebrew-400-normal.woff2',400)}
{font_face('NotoHeb','noto-sans-hebrew-hebrew-700-normal.woff2',700)}
{font_face('NotoAr','noto-naskh-arabic-arabic-400-normal.woff2',400)}
{font_face('NotoAr','noto-naskh-arabic-arabic-700-normal.woff2',700)}
@page {{ size: A4; margin: 14mm 13mm 16mm; }}
body {{ font-family: 'NotoSans','NotoHeb','NotoAr',sans-serif; color:#1a1a1a; font-size:9.6pt; line-height:1.38; }}
h1 {{ font-size:15pt; margin:0 0 4pt; }} h2, h3 {{ break-after:avoid; }} h2 {{ font-size:11.5pt; margin:10pt 0 3pt; border-bottom:1px solid #bbb; padding-bottom:2pt; }}
p {{ margin:3pt 0; }} ul {{ margin:2pt 0; padding-inline-start:16pt; }} li {{ margin:1pt 0; }}
table {{ border-collapse:collapse; width:100%; font-size:8.6pt; margin:4pt 0; }}
td,th {{ border:1px solid #ccc; padding:3pt 4pt; vertical-align:top; text-align:start; }}
.he {{ direction:rtl; font-family:'NotoHeb','NotoSans',sans-serif; }}
.ar {{ direction:rtl; font-family:'NotoAr','NotoSans',sans-serif; line-height:1.55; }}
.part {{ page-break-before:always; }}
.cover-title {{ text-align:center; margin-bottom:6pt; }}
.cover-title h1 {{ font-size:14pt; }} .cover-title .sub {{ font-size:8.5pt; color:#555; }}
.cols {{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:9pt; }}
.col {{ border:1px solid #d6d6d6; border-radius:4pt; padding:6pt 8pt; font-size:8.1pt; line-height:1.36; }}
.col.ar {{ font-size:8.4pt; line-height:1.45; }}
.col h3 {{ margin:0 0 4pt; font-size:9.5pt; }}
.col ul {{ padding-inline-start:11pt; }}
.sig-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:12pt 18pt; margin-top:8pt; }}
.sig {{ border:1px solid #ccc; border-radius:4pt; padding:7pt 9pt; break-inside:avoid; }}
.sig-name {{ font-weight:700; font-size:10.5pt; }} .sig-party {{ font-size:8.5pt; color:#444; }}
.sig-scope {{ font-size:7.8pt; color:#555; margin-top:3pt; min-height:22pt; }}
.status {{ font-size:8.3pt; border:1px solid #c9a; background:#fbf6f2; padding:5pt 8pt; margin:4pt 0 8pt; }}
.sig-line {{ border-bottom:1px solid #333; height:30pt; }}
.sig-labels {{ display:flex; justify-content:space-between; font-size:7.5pt; color:#666; margin-top:2pt; }}
.sig-declined {{ font-weight:700; color:#8a1c1c; font-size:9pt; padding:12pt 0 6pt; }}
.note {{ font-size:7.6pt; color:#666; text-align:center; margin-top:8pt; }}
</style></head><body>

<div class="cover-title">
  <h1>Four Years of Repair · ארבע שנים של תיקון · أربع سنوات من الإصلاح</h1>
  <div class="sub">Television statements for the evening the government is presented · הצהרות לטלוויזיה · بيانات متلفزة</div>
</div>
<div class="status">{STATUS}</div>
<div class="part">{tv_page("(a)", ["עברית", "English", "العربية"])}</div>
<div class="part">{tv_page("(b)", ["العربية", "English", "עברית"])}</div>
<div class="part">{tv_page("(c)", ["العربية", "English", "עברית"])}</div>

<div class="part">{framework('statement_en.md')}</div>
<div class="part he">{framework('statement_he.md')}</div>
<div class="part ar">{framework('statement_ar.md')}</div>

{sig_pages}
</body></html>"""

out_html = FONTS.parent / "coalition_statement.html"
out_html.write_text(html)
subprocess.run(["node", "-e", f"""
const {{chromium}} = require('playwright');
(async () => {{
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://{out_html}'); await p.waitForTimeout(500);
  await p.pdf({{path: '{ROOT / "coalition_statement.pdf"}', format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:7px;width:100%;text-align:center;color:#888"><span class="pageNumber"></span> / <span class="totalPages"></span></div>'}});
  await b.close();
}})();"""], check=True)
print("wrote", ROOT / "coalition_statement.pdf")
