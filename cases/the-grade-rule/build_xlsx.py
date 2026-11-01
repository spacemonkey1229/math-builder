#!/usr/bin/env python3
"""Build the Data.xlsx workbook for Grade Rule.

Ships raw, given values from the case's own appendices, plus a clearly-marked
empty work area for each Challenge -- never a pre-computed answer to what the
Challenges ask the student to derive (D1-D5's own results are NOT included).
"""
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.utils import get_column_letter

FONT = "Arial"
HEADER_FILL = PatternFill("solid", fgColor="1F3864")
HEADER_FONT = Font(name=FONT, bold=True, color="FFFFFF")
TITLE_FONT = Font(name=FONT, bold=True, size=14)
BODY_FONT = Font(name=FONT, size=11)
NOTE_FONT = Font(name=FONT, italic=True, size=10, color="555555")

wb = openpyxl.Workbook()


def style_sheet(ws, widths):
    ws.sheet_view.showGridLines = False
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w


def header_row(ws, row, values):
    for c, v in enumerate(values, start=1):
        cell = ws.cell(row=row, column=c, value=v)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)


def body_row(ws, row, values):
    for c, v in enumerate(values, start=1):
        cell = ws.cell(row=row, column=c, value=v)
        cell.font = BODY_FONT


# ---------------------------------------------------------------- README ---
ws = wb.active
ws.title = "README"
style_sheet(ws, [34, 90])
ws["A1"] = "Grade Rule — Data Workbook"
ws["A1"].font = TITLE_FONT
ws["A3"] = "This workbook"
ws["B3"] = "Real published ASTM D5585-11e1 body-measurement data and labor-rate data from cases/the-grade-rule/case.md, plus an empty work area for each Challenge. It does not contain the answers to D1–D5 — that is the assignment."
ws["A4"] = "Case"
ws["B4"] = "Grade Rule (the-grade-rule) — MS Math Case Study, Adventure"
rows = [
    ("Appendix A", "Real Body-Measurement Data by Size (ASTM D5585-11e1)"),
    ("Appendix B", "Fit Tolerance"),
    ("Appendix C", "Grading Labor"),
    ("Work Area D1-D2", "Empty table for your point-specific and shared scale-factor work"),
    ("Work Area D3-D4", "Empty table for your dilated-prediction and fit-check work"),
    ("Work Area D5", "Empty table for your cost/coverage/decision-memo work"),
]
ws["A6"] = "Sheet"
ws["B6"] = "Maps to"
ws["A6"].font = HEADER_FONT
ws["B6"].font = HEADER_FONT
ws["A6"].fill = HEADER_FILL
ws["B6"].fill = HEADER_FILL
for i, (a, b) in enumerate(rows, start=7):
    ws[f"A{i}"] = a
    ws[f"B{i}"] = b
    ws[f"A{i}"].font = BODY_FONT
    ws[f"B{i}"].font = BODY_FONT
for row in ws.iter_rows():
    for cell in row:
        cell.alignment = Alignment(wrap_text=True, vertical="top")

# ------------------------------------------------------------ Appendix A ---
ws = wb.create_sheet("Appendix A - Body Data")
style_sheet(ws, [12, 14, 14, 14, 16])
ws["A1"] = "Appendix A — Real Body-Measurement Data by Size (ASTM D5585-11e1) [S1]"
ws["A1"].font = TITLE_FONT
header_row(ws, 3, ["Size", "Bust (in)", "Waist (in)", "Hip (in)", "Notes"])
data = [
    (8, 36.25, 29.5, 38.5, ""),
    (10, 37.25, 30.5, 39.5, ""),
    (12, 38.75, 32.25, 41.0, "BASE SIZE"),
    (14, 40.375, 34.0, 42.5, ""),
    (16, 42.125, 36.0, 44.25, ""),
]
for i, row in enumerate(data, start=4):
    body_row(ws, i, list(row))
ws["A11"] = "Source: ASTM International, Standard Tables of Body Measurements for Adult Female Misses Figure Type (D5585-11e1), as reproduced at en.wikipedia.org/wiki/U.S._standard_clothing_size. Accessed 2026-09-18."
ws["A11"].font = NOTE_FONT
ws.merge_cells("A11:E11")
ws["A11"].alignment = Alignment(wrap_text=True)

# ------------------------------------------------------------ Appendix B ---
ws = wb.create_sheet("Appendix B - Tolerance")
style_sheet(ws, [40, 16])
ws["A1"] = "Appendix B — Fit Tolerance"
ws["A1"].font = TITLE_FONT
header_row(ws, 3, ["Quantity", "Value"])
body_row(ws, 4, ["Stated fit tolerance, each landmark [MA1]", "+/- 0.5 in"])

# ------------------------------------------------------------ Appendix C ---
ws = wb.create_sheet("Appendix C - Labor")
style_sheet(ws, [50, 20, 12])
ws["A1"] = "Appendix C — Grading Labor"
ws["A1"].font = TITLE_FONT
header_row(ws, 3, ["Quantity", "Value", "Source"])
data = [
    ("Median hourly wage, Fabric and Apparel Patternmakers (U.S.)", "$30.05/hr", "S2"),
    ("Uniform Dilation: one-time setup time", "3.0 min", "MA2"),
    ("Uniform Dilation: time per landmark, per size", "0.4 min/point", "MA2"),
    ("Point-Specific: time per landmark, per size", "1.2 min/point", "MA2"),
    ("Point-grades required (4 non-base sizes x 3 landmarks)", 12, ""),
]
for i, row in enumerate(data, start=4):
    body_row(ws, i, list(row))

# ------------------------------------------------------- Work Area D1-D2 ---
ws = wb.create_sheet("Work Area D1-D2")
style_sheet(ws, [10, 14, 14, 14, 16])
ws["A1"] = "Your Work — D1 Point-Specific Scale Factors & D2 Shared (Uniform) Factor"
ws["A1"].font = TITLE_FONT
header_row(ws, 3, ["Step", "Bust scale factor", "Waist scale factor", "Hip scale factor", "Notes"])
for i, step in enumerate(["8 -> 10", "10 -> 12", "12 -> 14", "14 -> 16"], start=4):
    ws.cell(row=i, column=1, value=step).font = BODY_FONT
ws["A9"] = "D2: single shared scale factor (Uniform Dilation) ="
ws["A9"].font = BODY_FONT
ws["A11"] = "Fill in every column yourself using Appendix A's data above. Nothing in this sheet is pre-computed."
ws["A11"].font = NOTE_FONT
ws.merge_cells("A11:E11")
ws["A11"].alignment = Alignment(wrap_text=True)

# ------------------------------------------------------- Work Area D3-D4 ---
ws = wb.create_sheet("Work Area D3-D4")
style_sheet(ws, [10, 14, 14, 14, 12, 12, 12, 12])
ws["A1"] = "Your Work — D3 Dilated Predictions & D4 Fit Check"
ws["A1"].font = TITLE_FONT
header_row(ws, 3, ["Size", "Pred. bust", "Pred. waist", "Pred. hip",
                    "Bust diff", "Waist diff", "Hip diff", "Size fits?"])
for i, size in enumerate([8, 10, 12, 14, 16], start=4):
    ws.cell(row=i, column=1, value=size).font = BODY_FONT
ws["A10"] = "Fill in every column yourself using Appendix A/B's data and your D2 scale factor. Nothing in this sheet is pre-computed."
ws["A10"].font = NOTE_FONT
ws.merge_cells("A10:H10")
ws["A10"].alignment = Alignment(wrap_text=True)

# ------------------------------------------------------- Work Area D5 ------
ws = wb.create_sheet("Work Area D5")
style_sheet(ws, [30, 20, 20])
ws["A1"] = "Your Work — D5 Cost, Coverage, and Decision Memo"
ws["A1"].font = TITLE_FONT
header_row(ws, 3, ["Metric", "Option A (Uniform)", "Option B (Point-Specific)"])
rows = ["Total labor cost ($)", "Sizes fully within tolerance", "Dollars per fitting size ($)"]
for i, r in enumerate(rows, start=4):
    ws.cell(row=i, column=1, value=r).font = BODY_FONT
ws["A8"] = "Fill in every column yourself using Appendix C and your D1-D4 work. Nothing in this sheet is pre-computed — that is the assignment."
ws["A8"].font = NOTE_FONT
ws.merge_cells("A8:C8")
ws["A8"].alignment = Alignment(wrap_text=True)

wb.save("cases/the-grade-rule/published/Grade Rule - Data.xlsx")
print("wrote Grade Rule - Data.xlsx")
