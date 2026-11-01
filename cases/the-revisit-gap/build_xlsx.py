#!/usr/bin/env python3
"""Build the Data workbook for The Revisit Gap. Raw appendix data only -- never pre-computes
D1-D5 or the hectares-per-dollar comparison; students do that work in the work-area sheet."""
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


def note(ws, text):
    ws.append([text])
    ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)
    ws.cell(row=ws.max_row, column=1).alignment = Alignment(wrap_text=True, vertical="top")


wb = openpyxl.Workbook()

# ---------- README ----------
ws = wb.active
ws.title = "README"
ws["A1"] = "Revisit Gap — Data Workbook"
style_title(ws, "A1")
ws["A2"] = "MS | Math | Case Study | 2026-27 | Adventure"
style_sub(ws, "A2")
ws["A5"] = "What this is"
ws["B5"] = ("Raw appendix data from the Revisit Gap case study, laid out for you to compute over. "
            "Nothing here has been pre-solved -- the sheets give you the sourced figures and "
            "stated modeling assumptions the case cites; the box-and-whisker plots, the "
            "minimum-detectable-area comparison, the line of best fit, the missing-month solve, "
            "and the hectares-per-dollar comparison (D1-D5) are your work to do.")
ws["A6"] = "Case"
ws["B6"] = ("cases/the-revisit-gap/case.md — see the case study docx for the full Overview, "
            "Background, Dilemma, and Challenges.")
ws["A8"] = "Sheet"
ws["B8"] = "Maps to"
mapping = [
    ("Appendix A — Feeds & Detection Lag", "Sentinel-2 and commercial imagery resolution/revisit facts, the minimum-mapping-unit rule, and each feed's 10-value detection-lag data set. Sources: [S1], [S5], [S6], [S7], MA1."),
    ("Appendix B — Cost Inputs", "Reserve area, commercial tasking price, analyst hourly cost, and both feeds' scene counts and review times. Sources: [S5], MA2-MA4."),
    ("Appendix C — Annual Detection", "Total confirmed clearing per year and the share too small for Sentinel Free to detect. Source: MA5, MA6."),
    ("Appendix D — Sample Invoices", "A sister program's past commercial invoices at other reserve sizes, plus this reserve's own monthly invoice table with one month redacted."),
    ("Modeling Assumptions", "Every MA# figure used above, its value, its basis, and its stated sensitivity -- reproduced from case.md so you don't have to cross-reference the docx while you work."),
    ("D1-D5 Work Area", "A blank area for your own box-and-whisker plots, minimum-detectable-area work, line-of-best-fit work, the missing-month solve, and the hectares-per-dollar comparison. This is the assignment -- it is intentionally empty."),
]
r = 9
for label, desc in mapping:
    ws.cell(row=r, column=1, value=label).font = Font(name=ARIAL, bold=True)
    c = ws.cell(row=r, column=2, value=desc)
    c.font = Font(name=ARIAL)
    c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[r].height = 30 if len(desc) < 140 else 45
    r += 1
col_widths(ws, [32, 95])
ws.row_dimensions[5].height = 55
ws.row_dimensions[6].height = 30

# ---------- Appendix A ----------
ws = wb.create_sheet("Appendix A — Feeds & Lag")
ws.append(["Quantity", "Value"])
rows = [
    ("Sentinel-2 finest-band resolution", "10 m [S1]"),
    ("Sentinel-2 revisit time (2 satellites, at equator)", "~5 days [S1]"),
    ("Commercial imagery resolution (this case)", "3 m [S5]"),
    ("Commercial tasking cadence (this case)", "weekly"),
    ("Minimum mapping unit rule", "~3x3 pixels [S6][S7]"),
]
for row in rows:
    ws.append(row)
ws.append([])
ws.append(["Commercial Weekly detection lag (days)", "2, 3, 3, 4, 4, 4, 5, 5, 6, 7 [MA1]"])
ws.append(["Sentinel Free detection lag (days)", "3, 4, 5, 6, 7, 9, 10, 12, 15, 20 [MA1]"])
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [50, 55])
for rr in range(2, ws.max_row + 1):
    ws.cell(row=rr, column=2).alignment = Alignment(wrap_text=True, vertical="top")

# ---------- Appendix B ----------
ws = wb.create_sheet("Appendix B — Cost Inputs")
rows = [
    ("Quantity", "Value"),
    ("Reserve area monitored (km2)", "25"),
    ("Commercial Weekly tasking price ($/km2/scene)", "12.00 [S5]"),
    ("Commercial Weekly scenes/year", "52"),
    ("Analyst hourly cost ($/hr)", "35.00 [MA2]"),
    ("Commercial Weekly review time/scene (hr)", "1.5 [MA3]"),
    ("Sentinel Free scenes/year", "73"),
    ("Sentinel Free review time/scene (hr)", "3.0 [MA4]"),
    ("Sentinel Free subscription cost", "$0"),
]
for row in rows:
    ws.append(row)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [50, 30])

# ---------- Appendix C ----------
ws = wb.create_sheet("Appendix C — Annual Detection")
rows = [
    ("Quantity", "Value"),
    ("Total confirmed illegal clearing/year (ha)", "6.0 [MA5]"),
    ("Share of clearing that is 'small' (sub-Sentinel-detectable)", "50% [MA6]"),
]
for row in rows:
    ws.append(row)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [55, 25])

# ---------- Appendix D ----------
ws = wb.create_sheet("Appendix D — Sample Invoices")
ws["A1"] = "Sister program: reserve area (km2) vs. annual commercial cost ($)"
ws["A1"].font = Font(name=ARIAL, bold=True)
ws.append(["Reserve area (km2)", "Annual cost ($)"])
for row in [(10, 9200), (50, 34500), (75, 48900), (100, 65800)]:
    ws.append(row)
style_header_row(ws, 2, 2)
ws.append([])
ws.append(["This reserve's own monthly invoice (most recent year)"])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, bold=True)
ws.append(["Month", "Amount ($)"])
month_rows = [("Jan", 1250), ("Feb", 1180), ("Mar", 1300), ("Apr", 1350), ("May", 1400),
              ("Jun", 1450), ("Jul", "illegible -- solve for this (D4)"), ("Aug", 1420),
              ("Sep", 1300), ("Oct", 1200), ("Nov", 1150), ("Dec", 1100)]
header_row2 = ws.max_row
for row in month_rows:
    ws.append(row)
style_header_row(ws, header_row2, 2)
set_body_font(ws)
col_widths(ws, [30, 35])
ws.append([])
note(ws, "Mean monthly cost for the year: $1,300.00 -- use this and the 11 known months to solve "
         "for July (Challenge D4).")

# ---------- Modeling Assumptions ----------
ws = wb.create_sheet("Modeling Assumptions")
ws["A1"] = "Modeling Assumptions"
style_title(ws, "A1", size=13)
ws["A2"] = ("These figures are NOT sourced. They are stated scenario assumptions chosen by the "
            "case author. You may challenge them in discussion -- that is a legitimate move.")
ws["A2"].font = Font(name=ARIAL, italic=True)
ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells("A2:C2")
ws.row_dimensions[2].height = 30

header_row = 4
ws.cell(row=header_row, column=1, value="#")
ws.cell(row=header_row, column=2, value="Assumption")
ws.cell(row=header_row, column=3, value="Value used")
ma_rows = [
    ("MA1", "Detection-lag data sets", "10 values per feed, as tabled"),
    ("MA2", "Analyst hourly cost", "$35.00/hour"),
    ("MA3", "Commercial Weekly review time/scene", "1.5 hours"),
    ("MA4", "Sentinel Free review time/scene", "3.0 hours"),
    ("MA5", "Total confirmed clearing/year", "6.0 hectares"),
    ("MA6", "Share of clearing that is 'small' (sub-Sentinel-detectable)", "50% -- HIGH sensitivity"),
]
for row in ma_rows:
    ws.append(row)
style_header_row(ws, header_row, 3)
set_body_font(ws)
col_widths(ws, [7, 55, 45])
for rr in range(header_row + 1, ws.max_row + 1):
    ws.cell(row=rr, column=2).alignment = Alignment(wrap_text=True, vertical="top")

# ---------- D1-D5 Work Area ----------
ws = wb.create_sheet("D1-D5 Work Area")
ws["A1"] = "Work Area — D1 through D5"
style_title(ws, "A1", size=13)
ws["A2"] = ("This sheet is intentionally blank except for column headers. Pull your raw inputs "
            "from the Appendix A-D sheets and the Modeling Assumptions sheet -- do not retype "
            "values by hand where you can reference the cell.")
ws["A2"].font = Font(name=ARIAL, italic=True)
ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells("A2:E2")
ws.row_dimensions[2].height = 40

sections = [
    (4, "D1 — Box-and-whisker plots of detection lag",
     ["Feed", "Min", "Q1", "Median", "Q3", "Max"]),
    (11, "D2 — Minimum-detectable-clearing-size comparison",
     ["Feed", "Pixel size (m)", "Min side (m)", "Min area (m2)", "Min area (ha)"]),
    (18, "D3 — Line of best fit for commercial cost vs. area",
     ["x (km2)", "y (cost $)", "Notes"]),
    (24, "D4 — The missing month",
     ["Known months' total", "Mean x 12", "Missing month amount"]),
    (29, "D5 — Hectares-per-dollar results table and recommendation",
     ["Option", "Total annual cost ($)", "Hectares detected/yr", "Ratio (ha/$)", "Recommendation & why"]),
]
for start_row, title, headers in sections:
    ws.cell(row=start_row, column=1, value=title).font = Font(name=ARIAL, bold=True, size=12)
    for c, h in enumerate(headers, start=1):
        ws.cell(row=start_row + 1, column=c, value=h)
    style_header_row(ws, start_row + 1, len(headers))
    for blank_r in range(start_row + 2, start_row + 5):
        for c in range(1, len(headers) + 1):
            ws.cell(row=blank_r, column=c, value=None)

col_widths(ws, [30, 28, 28, 28, 40])

wb.save("cases/the-revisit-gap/published/Revisit Gap - Data.xlsx")
print("wrote Revisit Gap - Data.xlsx")
