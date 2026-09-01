#!/usr/bin/env python3
"""Build the Data workbook for The Phasing Call. Raw appendix data only --
never pre-computes D1-D8; students do that work in the work-area sheet."""
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
            if cell.font is None or cell.font.name != ARIAL:
                if not (cell.font and cell.font.bold and cell.font.size and cell.font.size >= 13):
                    pass
    # simplest: apply Arial to every used cell that has no explicit font set yet
    for row in ws.iter_rows():
        for cell in row:
            if cell.value is not None and (cell.font is None or cell.font.name != ARIAL):
                cell.font = Font(name=ARIAL, size=11)

def col_widths(ws, widths):
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w


wb = openpyxl.Workbook()

# ---------- README ----------
ws = wb.active
ws.title = "README"
ws["A1"] = "The Phasing Call — Data Workbook"
style_title(ws, "A1")
ws["A2"] = "MS | Math | Case Study | 2026 | Adventure"
style_sub(ws, "A2")
ws["A5"] = "What this is"
ws["B5"] = ("Raw appendix data from The Phasing Call case study, laid out for you to compute "
            "over. Nothing here has been pre-solved -- the sheets give you the sourced figures "
            "the case cites; the modeling (D1-D8 in the case study) is your work to do.")
ws["A6"] = "Case"
ws["B6"] = ("cases/the-phasing-call/case.md — see the case study docx for the full Overview, "
            "Background, Dilemma, and Challenges.")
ws["A8"] = "Sheet"
ws["B8"] = "Maps to"
ws["A9"] = "Appendix A — Mission Parameters"
ws["B9"] = "Appendix A: contract constraints and the client station's tracked bearing/range. Source: MA1/MA2/MA3, case.json.sources[]."
ws["A10"] = "Appendix B — Rendezvous Profile Orbital Elements"
ws["B10"] = "Appendix B: each profile's real operational precedent, parking-orbit elements, angular catch-up rate, and modeled transit time. Sources: [S2], [S4], [S5], [S10]."
ws["A11"] = "Appendix C — Autonomous-Flight Budget"
ws["B11"] = "Appendix C: the vehicle's fixed total autonomous-flight/consumables allowance. Source: [S7], [S10]."
ws["A12"] = "Appendix D — Launch-Window Phase-Angle Reference"
ws["B12"] = "Appendix D: the station's orbital period and each profile's phase-angle tolerance band. Sources: [S8], [S9], [S11]."
ws["A13"] = "D1-D8 Work Area"
ws["B13"] = ("A blank area for your own polar-to-rectangular conversion, parametric equations, "
             "parameter elimination, reserve-percent calculation, polar graph data, launch-window "
             "day count, and the D7 primary-metric comparison. This is the assignment -- it is "
             "intentionally empty.")
for r in (5, 6, 8, 9, 10, 11, 12, 13):
    ws[f"A{r}"].font = Font(name=ARIAL, bold=(r == 8))
    ws[f"B{r}"].font = Font(name=ARIAL)
    ws[f"B{r}"].alignment = Alignment(wrap_text=True, vertical="top")
col_widths(ws, [30, 95])
ws.row_dimensions[5].height = 45
ws.row_dimensions[6].height = 30
ws.row_dimensions[9].height = 30
ws.row_dimensions[10].height = 45
ws.row_dimensions[11].height = 30
ws.row_dimensions[12].height = 30
ws.row_dimensions[13].height = 60

# ---------- Appendix A ----------
ws = wb.create_sheet("Appendix A — Mission Parameters")
rows = [
    ("Quantity", "Value"),
    ("Cargo vehicle / launch provider", "Meridian's cargo vehicle, modeled on Northrop Grumman's Cygnus cargo spacecraft [S5]"),
    ("Client station's orbital altitude (above Earth's surface)", "~400-420 km -- the ISS's own real orbit (413 km perigee / 422 km apogee) [S9]"),
    ("Client station's tracked position at the moment of decision (ground tracking radar)", "Bearing 48°, range 210 km from the tracking site (MA1)"),
    ("Contracted docking deadline", "96 hours (4 days) after launch (MA2)"),
    ("Minimum required autonomous-flight/consumables reserve remaining at docking", "15% of total allowance (MA3)"),
]
for r in rows:
    ws.append(r)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [46, 60])
for r in range(2, ws.max_row + 1):
    ws.cell(row=r, column=2).alignment = Alignment(wrap_text=True, vertical="top")
ws.append([])
ws.append(["Source: MA1/MA2/MA3 are stated modeling assumptions (case.md Appendix E); see case.json sources[] for every sourced figure elsewhere in this workbook.", None])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)

# ---------- Appendix B ----------
ws = wb.create_sheet("Appendix B — Orbital Elements")
header = ["Element", "Option A — The Fast-Track", "Option B — The Phasing Climb"]
data = [
    ("Real operational precedent",
     "Soyuz 4-orbit, ~6-hour rendezvous profile, flown since 2013 [S2]; 2-orbit ~3-hour ultrafast variant since 2020 [S3]",
     "Classic 34-orbit, ~2-day Soyuz rendezvous profile flown before 2013 [S4]; current profile for Northrop Grumman's Cygnus (NG-19, Aug 2023, ~2.4-2.5 days) [S5]"),
    ("Parking-orbit altitude (below the client station), km", 220, 220),
    ("Parking-orbit period (Kepler's third law), min", 88.62, 88.62),
    ("Vehicle's angular catch-up rate relative to the station, deg/min", 0.187, 0.187),
    ("Modeled total transit time, parking orbit to docking, hours", 6.0, 60.0),
]
ws.append(header)
for row in data:
    ws.append(row)
style_header_row(ws, 1, 3)
set_body_font(ws)
col_widths(ws, [46, 46, 46])
for r in range(2, ws.max_row + 1):
    for c in (1, 2, 3):
        ws.cell(row=r, column=c).alignment = Alignment(wrap_text=True, vertical="top")
ws.append([])
ws.append(["Sources: [S2] Universe Today; [S3] NASASpaceFlight.com; [S4] SpaceRef/AmericaSpace; [S5] Space.com/Wikipedia (Cygnus NG-19); [S10] Soyuz Crew Operations Manual, Table 8-1. See case.json sources[] for full citations.", None, None])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)

# ---------- Appendix C ----------
ws = wb.create_sheet("Appendix C — Flight Budget")
ws.append(["Quantity", "Value"])
ws.append(["Vehicle's total autonomous-flight/consumables allowance (hours)", 100.8])
ws.append(["Vehicle's total autonomous-flight/consumables allowance (days)", 4.2])
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [55, 30])
ws.append([])
ws.append(["Note: this sheet gives you only the fixed total allowance. Each profile's reserve remaining at docking (D4) is your calculation -- combine this figure with Appendix B's modeled transit time for each profile.", None])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)
ws.append(["Source: [S7] Space.com; [S10] Soyuz Crew Operations Manual, Section 3 (4.2-day calculated autonomous flight life). See case.json sources[] for full citations.", None])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)

# ---------- Appendix D ----------
ws = wb.create_sheet("Appendix D — Phase-Angle")
ws.append(["Quantity", "Value"])
d_rows = [
    ("Client station's orbital period, minutes", 92.9),
    ("Phase angle at liftoff, full possible range", "0° to 360°"),
    ("Phase-angle tolerance band, Option A — the Fast-Track", "~30°"),
    ("Phase-angle tolerance band, Option B — the Phasing Climb", "~270°"),
    ("Launch calendar length used in D6/D7 (days)", 30),
]
for r in d_rows:
    ws.append(r)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [55, 30])
for r in range(2, ws.max_row + 1):
    ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True, vertical="top")
ws.append([])
ws.append(["Sources: [S8] Soyuz Crew Operations Manual (phase-angle definition); [S9] Wikipedia — ISS orbital period; [S11] NASASpaceFlight.com — 30°/270° tolerance figures (see case.md Appendix D's disclosed S10/S11 discrepancy note). See case.json sources[] for full citations.", None])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)

# ---------- D1-D8 Work Area ----------
ws = wb.create_sheet("D1-D8 Work Area")
ws["A1"] = "Work Area — D1 through D8"
style_title(ws, "A1", size=13)
ws["A2"] = ("This sheet is intentionally blank except for column headers. Pull your raw inputs "
            "from the Appendix A/B/C/D sheets -- do not retype values by hand where you can "
            "reference the cell.")
ws["A2"].font = Font(name=ARIAL, italic=True)
ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells("A2:H2")
ws.row_dimensions[2].height = 40

sections = [
    (4, "D1 — Polar-to-rectangular conversion",
     ["Bearing (°)", "Range (km)", "x = r·sin(bearing)", "y = r·cos(bearing)", "Work shown"]),
    (9, "D2 — Parametric position equations x(t), y(t)",
     ["Profile", "x(t)", "y(t)", "Parameter meaning", "Parameter range for full rendezvous"]),
    (15, "D3 — Eliminate the parameter + elapsed-time check",
     ["Profile", "Rectangular equation (parameter eliminated)", "Algebra shown", "Elapsed time solved", "Check against D1 position"]),
    (21, "D4 — Autonomous-flight/consumables reserve",
     ["Profile", "Hours used to docking", "% of total allowance used", "Hours remaining", "% remaining (reserve)"]),
    (27, "D5 — Graphed polar phase-angle boundary",
     ["Profile", "Polar equation (phase-angle band)", "Notes / graph reference"]),
    (32, "D6 — Launch-window calendar calculation",
     ["Profile", "Tolerance band (°)", "Fraction of 360°", "Workable days per 30-day calendar", "Arithmetic shown"]),
    (38, "D7 — Primary-metric comparison (reserve hours per workable day)",
     ["Profile", "Reserve hours remaining (D4)", "Workable days (D6)", "Reserve hours ÷ workable days", "Division shown"]),
    (44, "D8 — Recommendation",
     ["Recommendation to launch director", "Defended using D7 result", "What would have to change for the recommendation to flip"]),
]
for start_row, title, headers in sections:
    ws.cell(row=start_row, column=1, value=title).font = Font(name=ARIAL, bold=True, size=12)
    for c, h in enumerate(headers, start=1):
        cell = ws.cell(row=start_row + 1, column=c, value=h)
    style_header_row(ws, start_row + 1, len(headers))
    # a few blank rows under each header for the student to fill
    for blank_r in range(start_row + 2, start_row + 4):
        for c in range(1, len(headers) + 1):
            ws.cell(row=blank_r, column=c, value=None)

col_widths(ws, [30, 30, 30, 30, 30, 30, 30, 30])

wb.save("cases/the-phasing-call/published/The Phasing Call - Data.xlsx")
print("wrote The Phasing Call - Data.xlsx")
