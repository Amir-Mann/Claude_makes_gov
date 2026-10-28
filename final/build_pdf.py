"""Build final/coalition_statement.pdf from the final/*.md sources.

Usage: python3 final/build_pdf.py <fonts_dir>
Page 1: the joint public statement in English, Hebrew and Arabic.
Then: the full framework in each language. Last: signature page.
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
    return markdown.markdown(text, extensions=["tables"])


def tv_section(lang_heading):
    src = (ROOT / "tv_statement.md").read_text()
    block = src.split(f"## {lang_heading}", 1)[1].split("\n---", 1)[0]
    block = "\n".join(l[2:] if l.startswith("> ") else l.lstrip(">") for l in block.splitlines())
    return md(block)


def framework(file):
    text = (ROOT / file).read_text()
    text = text.split("\n---\n*", 1)[0]  # drop simulation footer; restated once in the PDF
    return md(text)


SIGNERS = json.loads((ROOT / "signatories.json").read_text())

sig_blocks = "".join(f"""
<div class="sig">
  <div class="sig-name">{s['name']}</div>
  <div class="sig-party">{s['party_en']} · <span dir="rtl">{s['party_he']}</span> · <span dir="rtl">{s['party_ar']}</span></div>
  <div class="sig-scope">{s['scope']}</div>
  <div class="sig-line"></div>
  <div class="sig-labels"><span>Signature · חתימה · التوقيع</span><span>Date · תאריך · التاريخ</span></div>
</div>""" for s in SIGNERS)

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
{font_face('NotoSans','noto-sans-latin-400-normal.woff2',400)}
{font_face('NotoSans','noto-sans-latin-700-normal.woff2',700)}
{font_face('NotoHeb','noto-sans-hebrew-hebrew-400-normal.woff2',400)}
{font_face('NotoHeb','noto-sans-hebrew-hebrew-700-normal.woff2',700)}
{font_face('NotoAr','noto-naskh-arabic-arabic-400-normal.woff2',400)}
{font_face('NotoAr','noto-naskh-arabic-arabic-700-normal.woff2',700)}
@page {{ size: A4; margin: 14mm 13mm 16mm; }}
body {{ font-family: 'NotoSans','NotoHeb','NotoAr',sans-serif; color:#1a1a1a; font-size:9.6pt; line-height:1.38; }}
h1 {{ font-size:15pt; margin:0 0 4pt; }} h2 {{ font-size:11.5pt; margin:10pt 0 3pt; border-bottom:1px solid #bbb; padding-bottom:2pt; }}
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
.sig-line {{ border-bottom:1px solid #333; height:30pt; }}
.sig-labels {{ display:flex; justify-content:space-between; font-size:7.5pt; color:#666; margin-top:2pt; }}
.note {{ font-size:7.6pt; color:#666; text-align:center; margin-top:8pt; }}
</style></head><body>

<div class="cover-title">
  <h1>Four Years of Repair · ארבע שנים של תיקון · أربع سنوات من الإصلاح</h1>
  <div class="sub">Joint public statement of nine political movements · הצהרה פומבית משותפת · بيان علني مشترك</div>
</div>
<div class="cols">
  <div class="col"><h3>English</h3>{tv_section('English')}</div>
  <div class="col he"><h3>עברית</h3>{tv_section('עברית')}</div>
  <div class="col ar"><h3>العربية</h3>{tv_section('العربية')}</div>
</div>

<div class="part">{framework('statement_en.md')}</div>
<div class="part he">{framework('statement_he.md')}</div>
<div class="part ar">{framework('statement_ar.md')}</div>

<div class="part">
  <h1>Signatures · חתימות · التوقيعات</h1>
  <p>Each leader signs the joint public statement (page 1) and the instrument named under their name. Reservations are recorded in Annex 2.<br>
  <span class="he">כל מנהיג/ה חותם/ת על ההצהרה הפומבית המשותפת (עמוד 1) ועל המסמך המצוין תחת שמו/ה. ההסתייגויות מפורטות בנספח 2.</span><br>
  <span class="ar">يوقّع كل قائد على البيان العلني المشترك (الصفحة 1) وعلى الوثيقة المذكورة تحت اسمه. التحفظات مسجلة في الملحق 2.</span></p>
  <div class="sig-grid">{sig_blocks}</div>
  <div class="note">This document is a simulation exercise based on the parties' public positions. It does not speak for any party.<br>
  <span class="he">מסמך זה הוא תרגיל סימולציה המבוסס על עמדותיהן הפומביות של המפלגות, ואינו מדבר בשם אף מפלגה.</span><br>
  <span class="ar">هذه الوثيقة تمرين محاكاة يستند إلى المواقف العلنية للأحزاب، ولا تتحدث باسم أي حزب.</span></div>
</div>
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
