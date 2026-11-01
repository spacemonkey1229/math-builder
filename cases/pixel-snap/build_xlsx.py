#!/usr/bin/env python3
"""Build the Data workbook for Pixel Snap. Raw appendix data only -- never pre-computes
D1-D5 or the hectares-per-analyst-hour comparison; students do that work in the work-area
sheet."""
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
ws["A1"] = "Pixel Snap — Data Workbook"
style_title(ws, "A1")
ws["A2"] = "MS | Math | Case Study | 2026-27 | Adventure"
style_sub(ws, "A2")
ws["A5"] = "What this is"
ws["B5"] = ("Raw appendix data from the Pixel Snap case study, laid out for you to compute over. "
            "Nothing here has been pre-solved -- the sheets give you the sourced figures and "
            "stated modeling assumptions the case cites; the geometry (D1-D4) and the "
            "hectares-per-analyst-hour comparison (D5) are your work to do.")
ws["A6"] = "Case"
ws["B6"] = ("cases/pixel-snap/case.md — see the case study docx for the full Overview, "
            "Background, Dilemma, and Challenges.")
ws["A8"] = "Sheet"
ws["B8"] = "Maps to"
mapping = [
    ("Appendix B — Tree-Line Polygon & GCP", "The Kutai tree-line polygon's pixel-grid vertices in last month's reference scene, this month's pre-registration scene, and this month's True Lock-resampled scene; the one surveyed ground control point; and the scene footprint size. Sources: MA1, MA2, [S6]."),
    ("Appendix C — Accuracy Standards", "Sentinel-2's published absolute geolocation accuracy, the typical whole-pixel coregistration residual, and True Lock's achieved sub-pixel RMSE. Sources: [S7], [S8], MA3."),
    ("Appendix D — Hours & Cost", "Priya's total monthly analyst-hours for registration across all 5 concessions, Fast Lock's and True Lock's per-scene analyst-hours, and the cost per field-enforcement dispatch. Sources: MA4-MA8."),
    ("Modeling Assumptions", "Every MA# figure used above, its value, its basis, and its stated sensitivity -- reproduced from case.md so you don't have to cross-reference the docx while you work."),
    ("D1-D5 Work Area", "A blank area for your own coordinate-plane translation, dilation, reflection, quadrant-placement, and hectares-per-analyst-hour work. This is the assignment -- it is intentionally empty."),
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

# ---------- Appendix B ----------
ws = wb.create_sheet("Appendix B — Tree-Line & GCP")
rows = [
    ("Quantity", "Value"),
    ("Tree-line polygon vertices, last month's reference scene (pixel-grid)", "(400, 600), (720, 600), (720, 680), (400, 680) [MA1]"),
    ("Tree-line polygon vertices, this month's scene, pre-registration (pixel-grid)", "(403.4, 597.7), (723.4, 597.7), (723.4, 677.7), (403.4, 677.7) [MA1]"),
    ("Tree-line polygon vertices, this month's scene, after True Lock sub-pixel resampling (pixel-grid)", "(407.6, 607.3), (727.2, 607.3), (727.2, 687.0), (407.6, 687.0) [MA1]"),
    ("One surveyed ground control point, local pixel-grid coordinates (origin at scene center)", "(+1,500, −2,200) [MA2]"),
    ("Scene footprint width and height, pixels (10 m band)", "10,980 × 10,980 pixels (≈100 km × 100 km) [S6]"),
]
for row in rows:
    ws.append(row)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [70, 55])
for rr in range(2, ws.max_row + 1):
    ws.cell(row=rr, column=2).alignment = Alignment(wrap_text=True, vertical="top")
ws.append([])
note(ws, "Source [S6]: Copernicus Data Space Ecosystem, Sentinel-2 documentation "
         "(documentation.dataspace.copernicus.eu/Data/SentinelMissions/Sentinel2.html), "
         "accessed 2026-09-12, MEDIUM confidence. MA1/MA2 are stated Modeling Assumptions -- "
         "see the Modeling Assumptions sheet.")

# ---------- Appendix C ----------
ws = wb.create_sheet("Appendix C — Accuracy Standards")
rows = [
    ("Quantity", "Value"),
    ("Sentinel-2 Level-2A absolute geolocation accuracy (published spec)", "< 12 m at 95.5% confidence [S7]"),
    ("Typical whole-pixel (nearest-neighbor) coregistration residual error", "< 5 m (0.5 pixel) at 95.5% confidence [S7]"),
    ("Typical sub-pixel, GCP-based coregistration residual error (RMSE)", "≈ 3 m (0.3 pixel) [MA3]"),
]
for row in rows:
    ws.append(row)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [65, 45])
ws.append([])
note(ws, "Source [S7]: Copernicus, Sentinel-2 Collection 1 MSI Level-2A product page "
         "(sentinels.copernicus.eu/sentinel-data-access/sentinel-products/sentinel-2-data-products/"
         "collection-1-level-2a), accessed 2026-09-12, HIGH confidence. [S8]: Dai, X. & Khorram, S. "
         "(1998), IEEE TGRS 36(5), via Semantic Scholar, accessed 2026-09-12, MEDIUM confidence -- "
         "bounds MA3, a stated Modeling Assumption.")

# ---------- Appendix D ----------
ws = wb.create_sheet("Appendix D — Hours & Cost")
rows = [
    ("Quantity", "Value"),
    ("Number of concessions Priya monitors (Kutai + neighboring blocks)", "5 total [MA7]"),
    ("Priya's total monthly analyst-hours available for registration work, across all concessions", "100 minutes (1 h 40 min) [MA4]"),
    ("Analyst-hours per scene, Fast Lock (whole-pixel shift)", "20 minutes [MA5]"),
    ("Analyst-hours per scene, True Lock (sub-pixel GCP resampling)", "4 hours [MA6]"),
    ("Cost per field-enforcement dispatch (fuel, crew time, vehicle) sent to a falsely-flagged clearing", "$180 [MA8]"),
]
for row in rows:
    ws.append(row)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [80, 40])
ws.append([])
note(ws, "Source [S11] (informs MA8 only, not directly cited): Donate to Wildlife Conservation, "
         "'Conservation Costs' (donatetowildlifeconservation.com/conservation-costs/), accessed "
         "2026-09-12, LOW confidence. MA4-MA8 are stated Modeling Assumptions -- see the Modeling "
         "Assumptions sheet.")

# ---------- Modeling Assumptions ----------
ws = wb.create_sheet("Modeling Assumptions")
ws["A1"] = "Modeling Assumptions"
style_title(ws, "A1", size=13)
ws["A2"] = ("These figures are NOT sourced. They are stated scenario assumptions chosen by the "
            "case author. You may challenge them in discussion -- that is a legitimate move.")
ws["A2"].font = Font(name=ARIAL, italic=True)
ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells("A2:D2")
ws.row_dimensions[2].height = 30

header_row = 4
ws.cell(row=header_row, column=1, value="#")
ws.cell(row=header_row, column=2, value="Assumption")
ws.cell(row=header_row, column=3, value="Value used")
ws.cell(row=header_row, column=4, value="Sensitivity")
ma_rows = [
    ("MA1", "Kutai tree-line polygon shape and length", "320 px × 80 px (3,200 m × 800 m) rectangle", "Scales the false-positive ribbon area linearly for both options equally; does not by itself flip the dilemma."),
    ("MA2", "Ground control point pixel-grid location", "(+1,500, −2,200) px from scene center (Quadrant IV)", "Used only for D4's quadrant-identification task; not an input to D5's ratio."),
    ("MA3", "True Lock's achieved sub-pixel registration RMSE", "3 m (0.3 pixel)", "HIGH -- directly sets True Lock's false-positive area."),
    ("MA4", "Priya's total monthly analyst-hours budgeted for registration, across all 5 concessions", "100 minutes (1 h 40 min)", "HIGH -- the case-defining assumption that resolves the balance test."),
    ("MA5", "Analyst-hours per scene, Fast Lock", "20 minutes (1/3 hour)", "HIGH -- denominator of Fast Lock's ratio and of the shared monthly budget."),
    ("MA6", "Analyst-hours per scene, True Lock", "4 hours", "HIGH -- denominator of True Lock's ratio and driver of the shared-budget overage."),
    ("MA7", "Number of concessions sharing Priya's fixed monthly registration budget", "5 total (Kutai + 4 neighboring blocks)", "HIGH -- this is the case-defining assumption; see the case's Appendix E sensitivity note."),
    ("MA8", "Cost per field-enforcement dispatch", "$180", "None for the D5 ratio -- narrative/Appendix D context only."),
    ("MA9", "True Lock sub-pixel resampling scale factor (Appendix B)", "0.9985, about the scene center", "None for the D5 ratio -- pedagogical device for D2's dilation/scale-factor computation only."),
]
for row in ma_rows:
    ws.append(row)
style_header_row(ws, header_row, 4)
set_body_font(ws)
col_widths(ws, [7, 55, 30, 55])
for rr in range(header_row + 1, ws.max_row + 1):
    ws.cell(row=rr, column=2).alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(row=rr, column=4).alignment = Alignment(wrap_text=True, vertical="top")

# ---------- D1-D5 Work Area ----------
ws = wb.create_sheet("D1-D5 Work Area")
ws["A1"] = "Work Area — D1 through D5"
style_title(ws, "A1", size=13)
ws["A2"] = ("This sheet is intentionally blank except for column headers. Pull your raw inputs "
            "from the Appendix B-D sheets and the Modeling Assumptions sheet -- do not retype "
            "values by hand where you can reference the cell.")
ws["A2"].font = Font(name=ARIAL, italic=True)
ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells("A2:E2")
ws.row_dimensions[2].height = 40

sections = [
    (4, "D1 — Fast Lock translation vector & congruence check",
     ["Vertex (reference)", "Vertex (Fast Lock, shifted)", "Translation vector", "Congruent or similar? Why?"]),
    (10, "D2 — True Lock resampling scale factor & congruence check",
     ["Vertex (reference)", "Vertex (True Lock, resampled)", "Scale factor computed", "Congruent or similar? Why?"]),
    (16, "D3 — Reflection across the y-axis",
     ["Original vertex", "Reflected vertex (x, y) -> (-x, y)", "Notes"]),
    (21, "D4 — Ground control point quadrant placement",
     ["GCP coordinates", "Quadrant", "Why True Lock's correction differs by quadrant"]),
    (26, "D5 — Hectares-per-analyst-hour results table and recommendation",
     ["Option", "Misregistration ribbon area (ha)", "Analyst-hours spent", "Ratio (ha/analyst-hour)", "Recommendation & why"]),
]
for start_row, title, headers in sections:
    ws.cell(row=start_row, column=1, value=title).font = Font(name=ARIAL, bold=True, size=12)
    for c, h in enumerate(headers, start=1):
        ws.cell(row=start_row + 1, column=c, value=h)
    style_header_row(ws, start_row + 1, len(headers))
    for blank_r in range(start_row + 2, start_row + 4):
        for c in range(1, len(headers) + 1):
            ws.cell(row=blank_r, column=c, value=None)

col_widths(ws, [30, 30, 28, 28, 40])

wb.save("cases/pixel-snap/published/Pixel Snap - Data.xlsx")
print("wrote Pixel Snap - Data.xlsx")
