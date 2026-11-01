#!/usr/bin/env python3
"""Build the Data workbook for The Mooring Choice. Raw appendix data only -- never pre-computes
D1-D5 or the net-buoyant-lift-per-dollar comparison; students do that work in the work-area sheet."""
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
ws["A1"] = "Mooring Choice — Data Workbook"
style_title(ws, "A1")
ws["A2"] = "MS | Math | Case Study | 2026-27 | Adventure"
style_sub(ws, "A2")
ws["A5"] = "What this is"
ws["B5"] = ("Raw appendix data from the Mooring Choice case study, laid out for you to compute "
            "over. Nothing here has been pre-solved -- the sheets give you the sourced material "
            "prices/densities and stated modeling assumptions the case cites; the geometry "
            "(D1-D4) and the net-buoyant-lift-per-dollar comparison (D5) are your work to do.")
ws["A6"] = "Case"
ws["B6"] = ("cases/the-mooring-choice/case.md — see the case study docx for the full Overview, "
            "Background, Dilemma, and Challenges.")
ws["A8"] = "Sheet"
ws["B8"] = "Maps to"
mapping = [
    ("Appendix A — Hull Dimensions & Steel", "The Spar Design's and Spherical Design's dimensions, shared steel plate thickness, and real steel price/density and seawater density. Sources: MA1-MA4, [S1], [S2], [S3], [S6]."),
    ("Appendix B — Shared Sinker", "The pyramidal sinker's dimensions and real concrete price/density. Sources: MA5, [S4], [S5]."),
    ("Appendix C — Stability Ballast", "The Spherical Design's stability-ballast fraction and material cost. Sources: MA6, MA7."),
    ("Modeling Assumptions", "Every MA# figure used above, its value, its basis, and its stated sensitivity -- reproduced from case.md so you don't have to cross-reference the docx while you work."),
    ("D1-D5 Work Area", "A blank area for your own volume, surface-area, cost, and net-buoyant-lift-per-dollar work. This is the assignment -- it is intentionally empty."),
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
ws.row_dimensions[5].height = 45
ws.row_dimensions[6].height = 30

# ---------- Appendix A ----------
ws = wb.create_sheet("Appendix A — Hull & Steel")
rows = [
    ("Quantity", "Spar Design (A)", "Spherical Design (B)"),
    ("Shape", "Cylinder + conical nose", "Sphere"),
    ("Cylinder radius / sphere radius (m)", "0.60 [MA2]", "1.15 (diameter 2.30 m) [MA3]"),
    ("Cylindrical body height (m)", "5.40 [MA2]", "—"),
    ("Conical nose height (m)", "0.80 [MA2]", "—"),
    ("Steel hull plate thickness (m)", "0.010 [MA4]", "0.010 [MA4]"),
    ("Minimum required buoyant displacement (m3)", "6.41 [MA1]", "6.41 [MA1]"),
]
for row in rows:
    ws.append(row)
style_header_row(ws, 1, 3)
set_body_font(ws)
col_widths(ws, [45, 35, 35])
ws.append([])
note(ws, "Structural steel price: $2,660.55/short ton [S1, Gordian, July 2026, accessed 2026-09-18]. "
         "Density of steel: 7,850 kg/m3 [S3, The Engineering ToolBox]. Density of seawater: "
         "1,025 kg/m3 [S2, Wikipedia — Seawater]. Hull dimensions (MA1-MA4) are stated Modeling "
         "Assumptions scaled to NDBC's real named hull-size classes [S6] — see the Modeling "
         "Assumptions sheet.")

# ---------- Appendix B ----------
ws = wb.create_sheet("Appendix B — Shared Sinker")
rows = [
    ("Quantity", "Value"),
    ("Sinker shape", "Right square pyramid"),
    ("Base side length (m)", "1.50 [MA5]"),
    ("Height (m)", "1.00 [MA5]"),
    ("Concrete price ($/yd3)", "179.95 [S4]"),
    ("Density of reinforced concrete (kg/m3)", "2,400 [S5]"),
]
for row in rows:
    ws.append(row)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [45, 30])
ws.append([])
note(ws, "Source [S4]: ConcreteNetwork.com, 'Concrete Prices,' national average, accessed 2026-09-18, "
         "MEDIUM confidence. Source [S5]: The Engineering ToolBox, 'Concrete Properties,' HIGH "
         "confidence. MA5 (sinker dimensions) is a stated Modeling Assumption.")

# ---------- Appendix C ----------
ws = wb.create_sheet("Appendix C — Stability Ballast")
rows = [
    ("Quantity", "Value"),
    ("Spherical Design stability ballast, as a fraction of its own hull steel weight", "0.65 [MA6]"),
    ("Ballast material cost ($, fixed)", "50.00 [MA7]"),
]
for row in rows:
    ws.append(row)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [65, 25])
ws.append([])
note(ws, "MA6 and MA7 are stated Modeling Assumptions — no public spec exists for this exact hull's "
         "ballast requirement. MA6 is flagged HIGH sensitivity in case.md Appendix E.")

# ---------- Modeling Assumptions ----------
ws = wb.create_sheet("Modeling Assumptions")
ws["A1"] = "Modeling Assumptions"
style_title(ws, "A1", size=13)
ws["A2"] = ("These figures are NOT sourced. They are stated scenario assumptions chosen by the "
            "case author, built to real NDBC hull-size classes and real material prices/densities. "
            "You may challenge them in discussion -- that is a legitimate move.")
ws["A2"].font = Font(name=ARIAL, italic=True)
ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells("A2:D2")
ws.row_dimensions[2].height = 40

header_row = 4
ws.cell(row=header_row, column=1, value="#")
ws.cell(row=header_row, column=2, value="Assumption")
ws.cell(row=header_row, column=3, value="Value used")
ws.cell(row=header_row, column=4, value="Sensitivity")
ma_rows = [
    ("MA1", "Minimum required hull buoyant displacement", "6.41 m3", "Scales both options' volume, displacement, and steel surface area together."),
    ("MA2", "Spar Design dimensions", "radius 0.60 m, cylinder height 5.40 m, cone height 0.80 m", "Sets Option A's D1 volume/surface-area figures."),
    ("MA3", "Spherical Design radius (diameter)", "1.15 m (2.30 m)", "Sets Option B's D2 volume/surface-area figures."),
    ("MA4", "Steel hull plate thickness", "0.010 m (1 cm)", "HIGH -- scales both options' steel weight and cost together."),
    ("MA5", "Shared sinker dimensions", "base 1.50 m, height 1.00 m", "Affects both options equally; does not change the margin between A and B."),
    ("MA6", "Spherical Design stability ballast, as a fraction of its own hull steel weight", "0.65", "HIGH -- the case-defining assumption."),
    ("MA7", "Spherical Design ballast material cost", "$50.00", "LOW -- does not meaningfully move D5's ratio on its own."),
]
for row in ma_rows:
    ws.append(row)
style_header_row(ws, header_row, 4)
set_body_font(ws)
col_widths(ws, [7, 55, 40, 50])
for rr in range(header_row + 1, ws.max_row + 1):
    ws.cell(row=rr, column=2).alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(row=rr, column=4).alignment = Alignment(wrap_text=True, vertical="top")

# ---------- D1-D5 Work Area ----------
ws = wb.create_sheet("D1-D5 Work Area")
ws["A1"] = "Work Area — D1 through D5"
style_title(ws, "A1", size=13)
ws["A2"] = ("This sheet is intentionally blank except for column headers. Pull your raw inputs "
            "from the Appendix A-C sheets and the Modeling Assumptions sheet -- do not retype "
            "values by hand where you can reference the cell.")
ws["A2"].font = Font(name=ARIAL, italic=True)
ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells("A2:E2")
ws.row_dimensions[2].height = 40

sections = [
    (4, "D1 — Spar Design volume & steel surface area",
     ["Component", "Formula used", "Value", "Units"]),
    (11, "D2 — Spherical Design volume & steel surface area, SA:V comparison",
     ["Component", "Formula used", "Value", "Units"]),
    (17, "D3 — Shared sinker volume, surface area, submerged weight",
     ["Component", "Formula used", "Value", "Units"]),
    (23, "D4 — Materials cost table",
     ["Item", "Option A ($)", "Option B ($)", "Notes"]),
    (30, "D5 — Net-buoyant-lift-per-dollar results & recommendation",
     ["Option", "Net buoyant lift (kg)", "Total material cost ($)", "Ratio (kg/$)", "Recommendation & why"]),
]
for start_row, title, headers in sections:
    ws.cell(row=start_row, column=1, value=title).font = Font(name=ARIAL, bold=True, size=12)
    for c, h in enumerate(headers, start=1):
        ws.cell(row=start_row + 1, column=c, value=h)
    style_header_row(ws, start_row + 1, len(headers))
    for blank_r in range(start_row + 2, start_row + 5):
        for c in range(1, len(headers) + 1):
            ws.cell(row=blank_r, column=c, value=None)

col_widths(ws, [32, 32, 28, 28, 40])

wb.save("cases/the-mooring-choice/published/Mooring Choice - Data.xlsx")
print("wrote Mooring Choice - Data.xlsx")
