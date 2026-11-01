#!/usr/bin/env python3
"""Build the Data.xlsx workbook for Constellation Bid.

Ships raw, given values from the case's own appendices, plus a clearly-marked
empty work area for each Challenge -- never a pre-computed answer to what the
Challenges ask the student to derive (D1-D4's own results are NOT included).
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
ws["A1"] = "Constellation Bid — Data Workbook"
ws["A1"].font = TITLE_FONT
ws["A3"] = "This workbook"
ws["B3"] = "Raw data from cases/the-constellation-bid/case.md, one sheet per appendix table, plus an empty work area for each Challenge. It does not contain the answers to D1–D4 — that is the assignment."
ws["A4"] = "Case"
ws["B4"] = "Constellation Bid (the-constellation-bid) — MS Math Case Study, Launchpad"
rows = [
    ("Appendix A", "Solara's Orbit and the Unit Circle — altitude, radius, mu, derived speed/circumference"),
    ("Appendix B", "Solara's Six Target Planes — RAAN offsets and satellite counts per plane"),
    ("Appendix D", "Thruster, Propellant, and the Walk Budget"),
    ("Appendix E", "Launch Costs — rideshare and dedicated-launch pricing"),
    ("Work Area D1-D2", "Empty table for your own unit-circle trig and arc-length work"),
    ("Work Area D3-D4", "Empty table for your own delta-v, propellant, and decision-memo work"),
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
ws = wb.create_sheet("Appendix A - Orbit")
style_sheet(ws, [46, 22, 16])
ws["A1"] = "Appendix A — Solara's Orbit and the Unit Circle"
ws["A1"].font = TITLE_FONT
header_row(ws, 3, ["Quantity", "Value", "Source"])
data = [
    ("Orbital altitude", 550.0, "MA1 (grounded in S1)"),
    ("Earth's mean radius (km)", 6371.0, "standard reference value"),
    ("Orbital radius (km)", 6921.0, "= altitude + Earth radius"),
    ("Earth's standard gravitational parameter, mu (km^3/s^2)", 398600.4418, "standard reference value"),
    ("Orbital speed, v (m/s) -- derived, given for D1-D3 verification", 7589.0, "derived: sqrt(mu/r)*1000"),
    ("Orbital circumference (km) -- derived, given for D2 verification", 43486.5, "derived: 2*pi*r"),
]
for i, row in enumerate(data, start=4):
    body_row(ws, i, list(row))
ws["A11"] = "Note: speed and circumference are GIVEN here (already derived) so you can check your own D1-D2 work -- they are not the assignment."
ws["A11"].font = NOTE_FONT

# ------------------------------------------------------------ Appendix B ---
ws = wb.create_sheet("Appendix B - Target Planes")
style_sheet(ws, [16, 26, 20])
ws["A1"] = "Appendix B — Solara's Six Target Planes"
ws["A1"].font = TITLE_FONT
header_row(ws, 3, ["Target plane", "RAAN offset from seed plane (deg)", "Satellites assigned"])
planes = [
    ("Plane 0 (seed)", 0, 10),
    ("Plane 1", 60, 10),
    ("Plane 2", 120, 10),
    ("Plane 3", 180, 10),
    ("Plane 4", 240, 10),
    ("Plane 5", 300, 10),
]
for i, row in enumerate(planes, start=4):
    body_row(ws, i, list(row))
ws["A11"] = "Reminder: a burn can go the shorter way around. Plane 4/5's minimum angular separation is NOT the same as the RAAN offset printed above -- that conversion is Challenge D1's first step."
ws["A11"].font = NOTE_FONT
ws.merge_cells("A11:C11")
ws["A11"].alignment = Alignment(wrap_text=True)

# ------------------------------------------------------------ Appendix D ---
ws = wb.create_sheet("Appendix D - Thruster")
style_sheet(ws, [46, 20, 16])
ws["A1"] = "Appendix D — Thruster, Propellant, and the Walk Budget"
ws["A1"].font = TITLE_FONT
header_row(ws, 3, ["Quantity", "Value", "Source"])
data = [
    ("Specific impulse (Isp), rated maximum (s)", 2150.0, "S3"),
    ("Standard gravity, g0 (m/s^2)", 9.80665, "standard physical constant"),
    ("Satellite wet mass (kg)", 15.0, "MA3"),
    ("Per-satellite propellant allowance for the walk (kg)", 4.0, "MA4"),
]
for i, row in enumerate(data, start=4):
    body_row(ws, i, list(row))

# ------------------------------------------------------------ Appendix E ---
ws = wb.create_sheet("Appendix E - Launch Costs")
style_sheet(ws, [50, 20, 16])
ws["A1"] = "Appendix E — Launch Costs"
ws["A1"].font = TITLE_FONT
header_row(ws, 3, ["Quantity", "Value", "Source"])
data = [
    ("Satellite wet mass (kg)", 15.0, "Appendix D"),
    ("Total constellation mass, 60 satellites (kg)", 900.0, "derived"),
    ("Consolidated Launch: rideshare base price, first 50 kg (USD)", 350000, "S4"),
    ("Consolidated Launch: rideshare price per kg beyond 50 kg (USD/kg)", 7000, "S4"),
    ("Distributed Launch: list price per dedicated Electron launch, up to 300 kg (USD)", 7500000, "S5"),
    ("Distributed Launch: number of dedicated launches required", 6, "one per target plane"),
]
for i, row in enumerate(data, start=4):
    body_row(ws, i, list(row))

# ------------------------------------------------------- Work Area D1-D2 ---
ws = wb.create_sheet("Work Area D1-D2")
style_sheet(ws, [14, 20, 12, 12, 14, 14, 14, 18])
ws["A1"] = "Your Work — D1 Unit-Circle Trig Table & D2 Arc-Length Table"
ws["A1"].font = TITLE_FONT
header_row(ws, 3, ["Plane", "Min. angular\nseparation (deg)", "Separation\n(radians)",
                    "Half-angle\n(radians)", "sin(half-angle)", "cos(half-angle)",
                    "tan(full angle)", "Arc length (km)\n(D2)"])
for i, plane in enumerate(["Plane 0", "Plane 1", "Plane 2", "Plane 3", "Plane 4", "Plane 5"], start=4):
    ws.cell(row=i, column=1, value=plane).font = BODY_FONT
ws["A11"] = "Fill in every column yourself using Appendix A and Appendix B's data above. Nothing in this sheet is pre-computed."
ws["A11"].font = NOTE_FONT
ws.merge_cells("A11:H11")
ws["A11"].alignment = Alignment(wrap_text=True)

# ------------------------------------------------------- Work Area D3-D4 ---
ws = wb.create_sheet("Work Area D3-D4")
style_sheet(ws, [14, 16, 18, 16, 14, 30])
ws["A1"] = "Your Work — D3 Delta-v/Propellant Feasibility & D4 Decision Memo"
ws["A1"].font = TITLE_FONT
header_row(ws, 3, ["Plane", "Delta-v (m/s)", "Propellant\nrequired (kg)", "Within 4.0 kg\nallowance?",
                    "Satellites\nplaced", "Notes"])
for i, plane in enumerate(["Plane 0", "Plane 1", "Plane 2", "Plane 3", "Plane 4", "Plane 5"], start=4):
    ws.cell(row=i, column=1, value=plane).font = BODY_FONT
ws["A11"] = "Decision memo (D4): compute each option's total cost, correctly-placed count, and satellites-per-dollar below."
ws["A11"].font = NOTE_FONT
ws.merge_cells("A11:F11")
header_row(ws, 13, ["Option", "Correctly placed", "Total cost (USD)", "Satellites per dollar", "", ""])
ws["A14"] = "A — Consolidated Launch"
ws["A15"] = "B — Distributed Launch"
ws["A14"].font = BODY_FONT
ws["A15"].font = BODY_FONT
ws["A17"] = "Fill in every column yourself. Nothing in this sheet is pre-computed — that is Challenges D3 and D4."
ws["A17"].font = NOTE_FONT
ws.merge_cells("A17:F17")
ws["A17"].alignment = Alignment(wrap_text=True)

wb.save("cases/the-constellation-bid/published/Constellation Bid - Data.xlsx")
print("wrote Constellation Bid - Data.xlsx")
