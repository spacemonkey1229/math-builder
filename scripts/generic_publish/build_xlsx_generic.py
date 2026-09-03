#!/usr/bin/env python3
"""Generic appendix-table -> .xlsx workbook builder.

Parses every '## Appendix <Letter>: <Title>' section's markdown pipe-tables out
of a case's case.md and writes one sheet per appendix (skipping the Sources
appendix and the final "How To..." standards appendix, which aren't
computable data), plus a README sheet naming the case and mapping each sheet
to its appendix and source citations. Ships raw appendix data only -- this is
the exact same data already in the student docx (case.md IS the source of
truth), not a pre-computed answer key.
"""
import json
import re
import sys

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

ARIAL = "Arial"


def style_title(ws, cell, size=14):
    ws[cell].font = Font(name=ARIAL, size=size, bold=True)


def style_sub(ws, cell):
    ws[cell].font = Font(name=ARIAL, size=11, italic=True)


def style_header_row(ws, row, ncols):
    fill = PatternFill(fill_type="solid", fgColor="DDDDDD")
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = Font(name=ARIAL, bold=True)
        cell.fill = fill
        cell.alignment = Alignment(wrap_text=True, vertical="top")


def set_body_font(ws):
    for row in ws.iter_rows():
        for cell in row:
            if cell.value is not None and (cell.font is None or cell.font.name != ARIAL):
                cell.font = Font(name=ARIAL, size=11)


def col_widths(ws, widths):
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w


def parse_appendices(md_text):
    """Return [{'letter':..,'title':..,'tables':[[header,...rows]], 'prose':[...]}]"""
    # split at each "## Appendix X: title" (levels 2) -- stop before Modeling
    # Assumptions / next top-level section that isn't an appendix.
    parts = re.split(r'(?m)^## (Appendix [A-Z]\s*[:—-].*)$', md_text)
    appendices = []
    for i in range(1, len(parts), 2):
        header = parts[i].strip()
        body = parts[i + 1]
        # cut body at the next '---' or '## ' (non-appendix) or '### Appendix' (final standards appendix, handled separately)
        body = re.split(r'\n---\n', body)[0]
        m = re.match(r'Appendix ([A-Z])\s*[:—-]\s*(.*)', header)
        letter, title = m.group(1), m.group(2).strip()
        tables = extract_tables(body)
        appendices.append({"letter": letter, "title": title, "tables": tables, "body": body})
    return appendices


def extract_tables(body):
    lines = body.split('\n')
    tables = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('|'):
            header = [c.strip() for c in line.strip('|').split('|')]
            if i + 1 < len(lines) and re.match(r'^\s*\|?[\s:|-]+\|?\s*$', lines[i + 1]) and '-' in lines[i + 1]:
                j = i + 2
                rows = []
                while j < len(lines) and lines[j].strip().startswith('|'):
                    rows.append([c.strip() for c in lines[j].strip('|').split('|')])
                    j += 1
                tables.append({"header": header, "rows": rows})
                i = j
                continue
        i += 1
    return tables


def strip_md(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1 (\2)', text)
    text = text.replace('\\|', '|')
    return text.strip()


def build(case_id, root):
    case_dir = f"{root}/cases/{case_id}"
    d = json.load(open(f"{case_dir}/case.json"))
    title = d["title"]
    md = open(f"{case_dir}/case.md", encoding="utf-8").read()
    appendices = parse_appendices(md)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "README"
    style_title(ws, "A1")
    ws["A1"] = f"{title} — Data Workbook"
    ws["A2"] = f"MS | Math | Case Study | 2026-27"
    style_sub(ws, "A2")
    ws["A4"] = "This workbook reproduces the raw appendix data tables from the case study, one sheet per appendix, for computing over. It does not pre-compute any of the Challenges' graded deliverables."
    ws["A4"].alignment = Alignment(wrap_text=True)
    ws.merge_cells("A4:D4")
    row = 6
    ws.cell(row=row, column=1, value="Sheet").font = Font(name=ARIAL, bold=True)
    ws.cell(row=row, column=2, value="Appendix").font = Font(name=ARIAL, bold=True)
    ws.cell(row=row, column=3, value="Title").font = Font(name=ARIAL, bold=True)
    row += 1
    sheet_names = []
    for ap in appendices:
        if ap["title"].lower().startswith("sources") or "how to" in ap["title"].lower():
            continue
        if not ap["tables"]:
            continue
        sheet_name = f"App {ap['letter']}"[:31]
        sheet_names.append(sheet_name)
        ws.cell(row=row, column=1, value=sheet_name)
        ws.cell(row=row, column=2, value=f"Appendix {ap['letter']}")
        ws.cell(row=row, column=3, value=ap["title"])
        row += 1
    col_widths(ws, [12, 14, 60])
    set_body_font(ws)

    for ap in appendices:
        if ap["title"].lower().startswith("sources") or "how to" in ap["title"].lower():
            continue
        if not ap["tables"]:
            continue
        sheet_name = f"App {ap['letter']}"[:31]
        wsx = wb.create_sheet(sheet_name)
        style_title(wsx, "A1", size=13)
        wsx["A1"] = f"Appendix {ap['letter']}: {strip_md(ap['title'])}"
        r = 3
        for tbl in ap["tables"]:
            ncols = len(tbl["header"])
            for ci, h in enumerate(tbl["header"], start=1):
                wsx.cell(row=r, column=ci, value=strip_md(h))
            style_header_row(wsx, r, ncols)
            r += 1
            for row_vals in tbl["rows"]:
                for ci, v in enumerate(row_vals[:ncols], start=1):
                    val = strip_md(v)
                    # try numeric coercion for plain numbers
                    numval = val.replace(",", "").replace("$", "").rstrip("%")
                    try:
                        if re.match(r'^-?\d+(\.\d+)?$', numval) and numval not in ("",):
                            val_out = float(numval) if "." in numval else int(numval)
                        else:
                            val_out = val
                    except Exception:
                        val_out = val
                    wsx.cell(row=r, column=ci, value=val_out)
                r += 1
            r += 2
        col_widths(wsx, [28] * 6)
        set_body_font(wsx)

    out_path = f"{case_dir}/published/{title} - Data.xlsx"
    wb.save(out_path)
    print("wrote", out_path)


if __name__ == "__main__":
    ROOT = "/Users/manan/Documents/Claude/Projects/Math Builder"
    CASES = [
        "the-qubit-budget", "the-attribution-sample", "the-fee-ladder", "the-cold-start",
        "the-rig-split", "the-bot-farm", "the-course-correction", "the-plaza-bid",
    ]
    for c in (sys.argv[1:] or CASES):
        build(c, ROOT)
