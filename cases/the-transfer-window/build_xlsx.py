#!/usr/bin/env python3
"""Build the Data workbook for The Transfer Window. Raw appendix data only --
never pre-computes D1-D6; students do that work in the work-area sheet."""
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


wb = openpyxl.Workbook()

# ---------- README ----------
ws = wb.active
ws.title = "README"
ws["A1"] = "The Transfer Window — Data Workbook"
style_title(ws, "A1")
ws["A2"] = "MS | Math | Case Study | 2026 | Adventure"
style_sub(ws, "A2")
ws["A5"] = "What this is"
ws["B5"] = ("Raw appendix data from The Transfer Window case study, laid out for you to compute "
            "over. Nothing here has been pre-solved -- the sheets give you the sourced figures "
            "the case cites; the modeling (D1-D6 in the case study) is your work to do.")
ws["A6"] = "Case"
ws["B6"] = ("cases/the-transfer-window/case.md — see the case study docx for the full Overview, "
            "Background, Dilemma, and Challenges.")
ws["A8"] = "Sheet"
ws["B8"] = "Maps to"
ws["A9"] = "Appendix A — Mission Parameters"
ws["B9"] = "Appendix A: contract constraints (delivery window, radiation tolerance) and the two real orbital radii. Source: MA1, case.json.sources[] S2-S5/S10."
ws["A10"] = "Appendix B — Orbital Elements"
ws["B10"] = "Appendix B: each option's transfer-ellipse semi-major axis/eccentricity, delta-v, specific impulse, and modeled transit time. Sources: [S3][S6][S7][S12], MA2/MA3."
ws["A11"] = "Appendix C — Propellant and Payload Mass"
ws["B11"] = "Appendix C: the kick stage's fixed wet/dry mass and each option's propellant mass. Sources: [S2][S13], MA4."
ws["A12"] = "Appendix D — Radiation Dose Reference"
ws["B12"] = "Appendix D: dose rate and belt-crossing fraction for each option. Sources: [S14], MA5."
ws["A13"] = "D1-D6 Work Area"
ws["B13"] = ("A blank area for your own parametric position equations, parameter elimination, "
             "propellant-mass-fraction/payload calculation, the D4 primary-metric comparison, "
             "the D5 radiation-dose check, and the D6 recommendation. This is the assignment -- "
             "it is intentionally empty.")
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
    ("Launch vehicle / kick stage", "Meridian's kick stage, modeled on Firefly Aerospace's Sherpa orbital transfer vehicle line (Sherpa-LTC chemical / Sherpa-LTE electric) [S1]"),
    ("Parking orbit radius, measured from Earth's center (km)", 6878),
    ("Target orbit radius, geostationary, measured from Earth's center (km)", 42164),
    ("Customer's maximum acceptable delivery window (days)", "240 (MA1)"),
    ("Payload's rated cumulative radiation-dose tolerance (rad)", "20,000 (20 krad-Si) [S10]"),
]
for r in rows:
    ws.append(r)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [55, 55])
for r in range(2, ws.max_row + 1):
    ws.cell(row=r, column=2).alignment = Alignment(wrap_text=True, vertical="top")
ws.append([])
ws.append(["Source: MA1 is a stated modeling assumption (case.md Appendix E); see case.json sources[] for every sourced figure elsewhere in this workbook.", None])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)

# ---------- Appendix B ----------
ws = wb.create_sheet("Appendix B — Orbital Elements")
header = ["Element", "Option A — The Direct Burn", "Option B — The Patient Drift"]
data = [
    ("Propulsion type", "Chemical bipropellant, high thrust", "Electric (Hall-effect), low thrust"),
    ("Transfer-ellipse semi-major axis (km)", 24521, "24521 (MA2)"),
    ("Transfer-ellipse eccentricity", 0.7195, "0.7195 (MA2)"),
    ("Delta-v budget for this transfer (km/s)", 3.82, 6.0),
    ("Propulsion specific impulse, Isp (s)", 290, 1400),
    ("Modeled total transit time (days)", 0.221, "180 (MA3)"),
]
ws.append(header)
for row in data:
    ws.append(row)
style_header_row(ws, 1, 3)
set_body_font(ws)
col_widths(ws, [46, 40, 40])
for r in range(2, ws.max_row + 1):
    for c in (1, 2, 3):
        ws.cell(row=r, column=c).alignment = Alignment(wrap_text=True, vertical="top")
ws.append([])
ws.append(["Sources: [S3] Gunter's Space Page (Sherpa-LTE); [S6] Wikipedia (standard gravitational parameter); [S7] Benchmark Space Systems (Ocelot Isp); [S12] derived Hohmann-transfer computation. See case.json sources[] for full citations.", None, None])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)

# ---------- Appendix C ----------
ws = wb.create_sheet("Appendix C — Propellant Mass")
ws.append(["Quantity", "Option A — The Direct Burn", "Option B — The Patient Drift"])
c_rows = [
    ("Kick stage total wet mass (kg)", 180, "(same vehicle)"),
    ("Kick stage dry mass (kg)", "30 (MA4)", "(same vehicle)"),
    ("Propellant mass required for this transfer (kg)", 133.0, 63.7),
]
for r in c_rows:
    ws.append(r)
style_header_row(ws, 1, 3)
set_body_font(ws)
col_widths(ws, [50, 35, 35])
ws.append([])
ws.append(["Note: this sheet gives you only the sourced/stated propellant mass. Each option's deliverable payload mass and propellant-mass-fraction percent (D3) are your calculation -- combine wet mass, dry mass, and propellant mass.", None, None])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)
ws.append(["Sources: [S2] Gunter's Space Page (Sherpa-LTC wet mass); [S13] derived rocket-equation computation; MA4 (case.md Appendix E). See case.json sources[] for full citations.", None, None])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)

# ---------- Appendix D ----------
ws = wb.create_sheet("Appendix D — Radiation Dose")
ws.append(["Quantity", "Value"])
d_rows = [
    ("Average cumulative radiation dose rate while actively crossing the belts (rad/day)", "50 (MA5)"),
    ("Fraction of the Direct Burn's total transit time spent actively crossing the belts", "48% [S14]"),
    ("Fraction of the Patient Drift's total transit time spent actively crossing the belts", "48% [S14]"),
]
for r in d_rows:
    ws.append(r)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [60, 30])
for r in range(2, ws.max_row + 1):
    ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True, vertical="top")
ws.append([])
ws.append(["Sources: [S14] derived from S11's Van Allen belt altitudes against Appendix A's real radii; MA5 (case.md Appendix E). See case.json sources[] for full citations.", None])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)

# ---------- D1-D6 Work Area ----------
ws = wb.create_sheet("D1-D6 Work Area")
ws["A1"] = "Work Area — D1 through D6"
style_title(ws, "A1", size=13)
ws["A2"] = ("This sheet is intentionally blank except for column headers. Pull your raw inputs "
            "from the Appendix A/B/C/D sheets -- do not retype values by hand where you can "
            "reference the cell.")
ws["A2"].font = Font(name=ARIAL, italic=True)
ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells("A2:F2")
ws.row_dimensions[2].height = 40

sections = [
    (4, "D1 — Parametric position equations x(E), y(E)",
     ["Option", "x(E)", "y(E)", "Parameter meaning", "Parameter range for one full transfer"]),
    (9, "D2 — Eliminate the parameter + intercept check",
     ["Option", "Rectangular equation (parameter eliminated)", "Algebra shown", "Apoapsis solved (km)", "Matches Appendix A target radius?"]),
    (15, "D3 — Propellant-mass fraction and deliverable payload",
     ["Option", "Propellant mass (kg)", "Propellant % of wet mass", "Deliverable payload (kg)", "Arithmetic shown"]),
    (21, "D4 — Primary metric (kg of deliverable payload per day)",
     ["Option", "Deliverable payload (kg, from D3)", "Transit time (days, Appendix B)", "kg per day", "Division shown"]),
    (27, "D5 — Cumulative radiation-dose check",
     ["Option", "Dose rate x belt fraction x transit time", "Cumulative dose (rad)", "Vs. 20,000 rad tolerance", "Unit conversion shown"]),
    (33, "D6 — Recommendation",
     ["Recommendation to payload customer", "Defended using D4 and D5", "What would have to change for the recommendation to flip"]),
]
for start_row, title, headers in sections:
    ws.cell(row=start_row, column=1, value=title).font = Font(name=ARIAL, bold=True, size=12)
    for c, h in enumerate(headers, start=1):
        ws.cell(row=start_row + 1, column=c, value=h)
    style_header_row(ws, start_row + 1, len(headers))
    for blank_r in range(start_row + 2, start_row + 4):
        for c in range(1, len(headers) + 1):
            ws.cell(row=blank_r, column=c, value=None)

col_widths(ws, [30, 30, 30, 30, 30, 30])

wb.save("cases/the-transfer-window/published/The Transfer Window - Data.xlsx")
print("wrote The Transfer Window - Data.xlsx")
