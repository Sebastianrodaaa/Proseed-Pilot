#!/usr/bin/env python3
"""Generate Step 2a (market scan) and Step 2b (tech baseline) .docx deliverables
from research JSON files in proseed/research/.

Usage: python3 scripts/generate-step2.py [slug ...]
  With no args, processes every *.json in proseed/research/.
"""
import copy
import glob
import json
import os
import sys
import zipfile

from docx import Document
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL_2A = os.path.join(ROOT, "skills/market-scan/templates/attachment_202610_2a_Market_Scan_Template_.dotx")
TPL_2B = os.path.join(ROOT, "skills/tech-baseline/templates/attachment_202611_2b_Tech_Baseline_Template.dotx")
RESEARCH = os.path.join(ROOT, "proseed/research")
OUT_2A = os.path.join(ROOT, "proseed/02a-market-scan")
OUT_2B = os.path.join(ROOT, "proseed/02b-tech-baseline")

DATE = "2026-10-30"
SIGNER = "Devin (agent draft)"


def dotx_to_docx(src, dst):
    with zipfile.ZipFile(src) as z:
        items = {n: z.read(n) for n in z.namelist()}
    items["[Content_Types].xml"] = items["[Content_Types].xml"].replace(
        b"wordprocessingml.template.main+xml", b"wordprocessingml.document.main+xml")
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as z:
        for n, b in items.items():
            z.writestr(n, b)


def set_title(doc, name):
    for r in doc.paragraphs[0].runs:
        if "[Hypothesis name]" in r.text:
            r.text = r.text.replace("[Hypothesis name]", name)
            return
    raise RuntimeError("title placeholder not found")


def fill_section_text(doc, label, content):
    """Remove guidance paras after `label`; write content into first empty para."""
    lp = next(p for p in doc.paragraphs if p.text.strip() == label)
    el = lp._element
    sib = el.getnext()
    wrote = False
    while sib is not None and sib.tag == qn("w:p"):
        p = Paragraph(sib, lp._parent)
        t = p.text.strip()
        if t.startswith("[Remove when filled]") or t.startswith("Output:"):
            sib.getparent().remove(sib)
        elif t == "" and not wrote:
            p.add_run(content)
            wrote = True
        elif t != "":
            break
        sib = el.getnext()
    if not wrote:
        # no empty slot: insert a new para right after the label
        new_p = copy.deepcopy(el)
        for t in new_p.iter(qn("w:t")):
            t.getparent().getparent().remove(t.getparent())
        el.addnext(new_p)
        Paragraph(new_p, lp._parent).add_run(content)


def sign_and_decide(doc, decision="Go to next step"):
    tbl = doc.tables[-1]
    cells = tbl.rows[1].cells
    filled_name = filled_date = False
    for k, c in enumerate(cells):
        if c.text.strip() == "Name" and not filled_name:
            cells[k + 1].text = SIGNER
            filled_name = True
        elif c.text.strip() == "Date" and not filled_date:
            cells[k + 1].text = DATE
            filled_date = True
    for c in tbl.rows[-1].cells:
        if decision in c.text:
            for cb in c._element.iter(qn("w14:checkbox")):
                for ch in cb.iter(qn("w14:checked")):
                    ch.set(qn("w14:val"), "1")
            for t_el in c._element.iter(qn("w:t")):
                if t_el.text and "☐" in t_el.text:
                    t_el.text = t_el.text.replace("☐", "☒")
            break


def add_row(table):
    tr = copy.deepcopy(table.rows[-1]._element)
    for tc in tr.iter(qn("w:tc")):
        for t in tc.iter(qn("w:t")):
            t.text = ""
    table.rows[-1]._element.addnext(tr)
    return tr


# ---------------- 2a ----------------

def gen_2a(data):
    slug = data["slug"]
    out = os.path.join(OUT_2A, f"{slug}-market-scan.docx")
    dotx_to_docx(TPL_2A, out)
    doc = Document(out)
    set_title(doc, data["title"])

    ms = data["market_scan"]

    fill_section_text(doc, "Market size", ms["market_size_text"])
    reg = ms["regions"]
    t0 = doc.tables[0]
    t0.cell(1, 1).text = str(reg.get("Europe", ""))
    t0.cell(1, 3).text = str(reg.get("Asia", ""))
    t0.cell(2, 1).text = str(reg.get("America", ""))
    t0.cell(2, 3).text = str(reg.get("Africa", ""))

    fill_section_text(doc, "Target customers", ms["target_customers_text"])
    t1 = doc.tables[1]
    for r in range(1, 4):
        label = t1.cell(r, 0).text.strip()
        if label in ms["customers"]:
            num, share = ms["customers"][label]
            t1.cell(r, 1).text = str(num)
            t1.cell(r, 2).text = str(share)

    fill_section_text(doc, "Players offering a solution today", ms["players_text"])
    t2 = doc.tables[2]
    rows = ms["players"]
    while len(t2.rows) - 1 < len(rows):
        add_row(t2)
    for i, (who, sol, share) in enumerate(rows, start=1):
        t2.cell(i, 0).text = str(who)
        t2.cell(i, 1).text = str(sol)
        t2.cell(i, 2).text = str(share)

    # Regulation: guidance paras then table; no free-text slot
    lp = next(p for p in doc.paragraphs if p.text.strip() == "Regulation")
    el = lp._element
    sib = el.getnext()
    while sib is not None and sib.tag == qn("w:p"):
        p = Paragraph(sib, lp._parent)
        t = p.text.strip()
        if t.startswith("[Remove when filled]") or t.startswith("Output:"):
            sib.getparent().remove(sib)
        elif t != "":
            break
        sib = el.getnext()
    t3 = doc.tables[3]
    regs = ms["regulation"]
    while len(t3.rows) - 1 < len(regs):
        add_row(t3)
    for i, (reg_name, jur, meaning) in enumerate(regs, start=1):
        t3.cell(i, 0).text = str(reg_name)
        t3.cell(i, 1).text = str(jur)
        t3.cell(i, 2).text = str(meaning)

    sign_and_decide(doc)
    doc.save(out)
    return out


# ---------------- 2b ----------------

TECH_LABELS = ("How it works:", "How well it performs:", "Limits:")


def fill_tech_block(title_para, name, how, perf, limits):
    """title_para = the 'Technology X' paragraph; next 3 paras are the labels."""
    for r in title_para.runs:
        r.text = ""
    if title_para.runs:
        title_para.runs[0].text = name
    else:
        title_para.add_run(name)
    el = title_para._element
    vals = [how, perf, limits]
    for i, lab in enumerate(TECH_LABELS):
        sib = el.getnext()
        p = Paragraph(sib, title_para._parent)
        # keep the label run, append content as a new run
        done = False
        for r in p.runs:
            if lab.rstrip() in r.text:
                done = True
        if not done and p.runs:
            p.runs[0].text = lab + " "
        p.add_run(vals[i])
        el = sib


def gen_2b(data):
    slug = data["slug"]
    out = os.path.join(OUT_2B, f"{slug}-tech-baseline.docx")
    dotx_to_docx(TPL_2B, out)
    doc = Document(out)
    set_title(doc, data["title"])

    tb = data["tech_baseline"]

    # remove guidance para after 'Technologies used in the market'
    lp = next(p for p in doc.paragraphs if p.text.strip() == "Technologies used in the market")
    el = lp._element
    sib = el.getnext()
    while sib is not None and sib.tag == qn("w:p"):
        t = Paragraph(sib, lp._parent).text.strip()
        if t.startswith("[Remove when filled]"):
            sib.getparent().remove(sib)
        else:
            break
        sib = el.getnext()

    # find the two template tech blocks
    tech_paras = [p for p in doc.paragraphs
                  if p.text.strip() in ("Technology X", "Technology Y")]
    techs = tb["technologies"]
    assert len(techs) >= 1, "need at least one technology"

    # clone blocks if more than 2 technologies
    block_elements = [tech_paras[0]._element] + [
        tech_paras[0]._element.getnext() for _ in range(0)]  # placeholder
    # collect the 4 elements of block X
    def block_elems(tp):
        els = [tp._element]
        e = tp._element.getnext()
        for _ in range(3):
            els.append(e)
            e = e.getnext()
        return els

    x_elems = block_elems(tech_paras[0])
    anchor = next(p for p in doc.paragraphs
                  if p.text.strip() == "Why our solution can be better")._element

    # remove the Y block; we'll rebuild all blocks from X clones before anchor
    y_elems = block_elems(tech_paras[1])
    for e in y_elems:
        e.getparent().remove(e)
    for e in x_elems:
        e.getparent().remove(e)

    for i, tech in enumerate(techs):
        new_els = [copy.deepcopy(e) for e in x_elems]
        for ne in new_els:
            anchor.addprevious(ne)
        tp = Paragraph(new_els[0], tech_paras[0]._parent)
        fill_tech_block(tp, tech["name"], tech["how"], tech["performance"], tech["limits"])

    fill_section_text(doc, "Why our solution can be better", tb["why_better_text"])

    # key assumptions into empty paras after the 'Key assumptions' heading
    ka = next(p for p in doc.paragraphs if p.text.strip() == "Key assumptions")
    el = ka._element
    assumptions = tb["key_assumptions"][:5]
    i = 0
    sib = el.getnext()
    while sib is not None and sib.tag == qn("w:p") and i < len(assumptions):
        p = Paragraph(sib, ka._parent)
        if p.text.strip() == "":
            p.add_run("\u2022 " + assumptions[i])
            i += 1
        else:
            break
        sib = el.getnext()
        el = sib
    while i < len(assumptions):
        # ran out of empty paras: clone last empty para
        new_p = copy.deepcopy(ka._element)
        for r in new_p.iter(qn("w:r")):
            new_p.remove(r)
        el.addnext(new_p)
        Paragraph(new_p, ka._parent).add_run("\u2022 " + assumptions[i])
        el = new_p
        i += 1

    sign_and_decide(doc)
    doc.save(out)
    return out


def main():
    os.makedirs(OUT_2A, exist_ok=True)
    os.makedirs(OUT_2B, exist_ok=True)
    slugs = sys.argv[1:]
    files = sorted(glob.glob(os.path.join(RESEARCH, "*.json")))
    for f in files:
        data = json.load(open(f))
        if slugs and data["slug"] not in slugs:
            continue
        try:
            a = gen_2a(data)
            print("2a:", os.path.relpath(a, ROOT))
        except Exception as e:
            print(f"2a FAIL {data['slug']}: {e}")
        try:
            b = gen_2b(data)
            print("2b:", os.path.relpath(b, ROOT))
        except Exception as e:
            print(f"2b FAIL {data['slug']}: {e}")


if __name__ == "__main__":
    main()
