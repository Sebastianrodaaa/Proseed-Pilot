#!/usr/bin/env python3
"""Convert filled ProSeed .docx deliverables to .pdf.

Reads paragraphs and tables in document order and renders them with
reportlab — section labels bold, tables gridded, decision checkbox row
reproduced. Usage:

  python3 scripts/docx-to-pdf.py [file.docx ...]
  (no args: converts every .docx under proseed/)
"""
import glob
import os
import sys

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph as RLParagraph,
                                Spacer, Table as RLTable, TableStyle)

# font with the checkbox glyphs
for cand in ("/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
             "/System/Library/Fonts/Apple Symbols.ttf"):
    if os.path.exists(cand):
        pdfmetrics.registerFont(TTFont("Body", cand))
        pdfmetrics.registerFont(TTFont("Body-Bold", cand))
        BODY = "Body"
        break
else:
    BODY = "Helvetica"

TITLE = ParagraphStyle("title", fontName=BODY, fontSize=16, leading=20, spaceAfter=4)
SUBTLE = ParagraphStyle("subtle", fontName=BODY, fontSize=9, leading=11,
                        textColor=colors.HexColor("#666666"))
H = ParagraphStyle("h", fontName=BODY, fontSize=11.5, leading=14,
                   spaceBefore=10, spaceAfter=3, textColor=colors.black)
P = ParagraphStyle("p", fontName=BODY, fontSize=10, leading=13, spaceAfter=4)

LABELS = {
    "Target customers", "What they want", "Because",
    "Market size", "Players offering a solution today", "Regulation",
    "Technologies used in the market", "Why our solution can be better",
    "Key assumptions", "Market scan", "Tech baseline", "Problem hypothesis",
}
TECH_LABEL_PREFIXES = ("How it works:", "How well it performs:", "Limits:")


def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def para_style(p, idx):
    t = p.text.strip()
    if idx == 0:
        return TITLE
    if t in LABELS or t.startswith("Technology "):
        return H
    if t.startswith(TECH_LABEL_PREFIXES):
        return H
    if p.style.name.lower().startswith("title") or p.style.name.lower().startswith("heading"):
        return H
    return P


def convert(src):
    doc = Document(src)
    story = []
    pi = 0
    tbl_seen = 0
    for child in doc.element.body.iterchildren():
        if child.tag == qn("w:p"):
            p = Paragraph(child, doc)
            t = p.text.strip()
            if not t:
                story.append(Spacer(1, 4))
            else:
                story.append(RLParagraph(esc(t), para_style(p, pi)))
            pi += 1
        elif child.tag == qn("w:tbl"):
            tbl = Table(child, doc)
            tbl_seen += 1
            data = [[RLParagraph(esc(c.text.strip()), P) for c in row.cells]
                    for row in tbl.rows]
            ncols = max(len(r.cells) for r in tbl.rows)
            t = RLTable(data, colWidths=[16.5 * cm / ncols] * ncols)
            style = [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#999999")),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8e8e8")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ]
            # dedupe merged cells display
            for r_i, row in enumerate(tbl.rows):
                seen = {}
                for c_i, cell in enumerate(row.cells):
                    tc = id(cell._tc)
                    if tc in seen:
                        data[r_i][c_i] = RLParagraph("", P)
                    else:
                        seen[tc] = c_i
            t.setStyle(TableStyle(style))
            story.append(Spacer(1, 4))
            story.append(t)
            story.append(Spacer(1, 6))

    out = os.path.splitext(src)[0] + ".pdf"
    SimpleDocTemplate(out, pagesize=A4,
                      leftMargin=2 * cm, rightMargin=2 * cm,
                      topMargin=1.8 * cm, bottomMargin=1.8 * cm).build(story)
    return out


def main():
    files = sys.argv[1:] or sorted(glob.glob("proseed/**/*.docx", recursive=True))
    for f in files:
        try:
            print("pdf:", convert(f))
        except Exception as e:
            print(f"FAIL {f}: {e}")


if __name__ == "__main__":
    main()
