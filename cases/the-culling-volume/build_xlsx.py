#!/usr/bin/env python3
"""Build the Data workbook for The Culling Volume. Raw appendix data only --
never pre-computes D1-D5; students do that work in the work-area sheet."""
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
ws["A1"] = "The Culling Volume — Data Workbook"
style_title(ws, "A1")
ws["A2"] = "MS | Math | Case Study | 2026 | Adventure"
style_sub(ws, "A2")
ws["A5"] = "What this is"
ws["B5"] = ("Raw appendix data from The Culling Volume case study, laid out for you to compute "
            "over. Nothing here has been pre-solved -- the sheets give you each prop's component "
            "dimensions and the case's cost inputs; the volume/surface-area decomposition (D1), "
            "the bounding sphere and capsule volumes (D2, D3), and the full per-frame cost "
            "comparison (D4) are your work to do.")
ws["A6"] = "Case"
ws["B6"] = ("cases/the-culling-volume/case.md — see the case study docx for the full Overview, "
            "Background, Dilemma, and Challenges.")
ws["A8"] = "Sheet"
ws["B8"] = "Maps to"
mapping = [
    ("Appendix B — Props", "Each prop's component-solid dimensions (cylinder, cone, or square pyramid). Sources: [S1] (lamppost height range), [S2] (pipe diameter), MA1-MA5 (everything else)."),
    ("Appendix C — Prop Counts", "How many of each prop type are tested for culling per frame. Source: MA6."),
    ("Appendix D — Cost Inputs", "Per-object culling-test cost for each bounding-shape option, and the wasted-volume-to-render-cost conversion. Sources: MA7-MA9."),
    ("Modeling Assumptions", "Every MA# figure used above, its value, its basis, and its stated sensitivity -- reproduced from case.md so you don't have to cross-reference the docx while you work."),
    ("D1-D5 Work Area", "A blank area for your own volume/surface-area decomposition, bounding sphere and capsule volumes, wasted-volume totals, and the full per-frame cost comparison. This is the assignment -- it is intentionally empty."),
]
r = 9
for label, desc in mapping:
    ws.cell(row=r, column=1, value=label).font = Font(name=ARIAL, bold=True)
    c = ws.cell(row=r, column=2, value=desc)
    c.font = Font(name=ARIAL)
    c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[r].height = 30 if len(desc) < 140 else 45
    r += 1
col_widths(ws, [28, 95])
ws.row_dimensions[5].height = 45
ws.row_dimensions[6].height = 30

# ---------- Appendix B ----------
ws = wb.create_sheet("Appendix B — Props")
rows = [
    ("Prop", "Component", "Dimension", "Value"),
    ("Lamppost", "Cylinder pole", "Radius (m)", 0.075),
    ("Lamppost", "Cylinder pole", "Height (m)", 6.1),
    ("Lamppost", "Cone fixture cap", "Radius (m)", 0.15),
    ("Lamppost", "Cone fixture cap", "Height (m)", 0.3),
    ("Industrial pipe", "Cylinder", "Radius (m)", 0.0841375),
    ("Industrial pipe", "Cylinder", "Height (m)", 4.0),
    ("Sign post", "Cylinder post", "Radius (m)", 0.05),
    ("Sign post", "Cylinder post", "Height (m)", 2.5),
    ("Sign post", "Square pyramid cap", "Base side (m)", 0.2),
    ("Sign post", "Square pyramid cap", "Height (m)", 0.15),
]
for row in rows:
    ws.append(row)
style_header_row(ws, 1, 4)
set_body_font(ws)
col_widths(ws, [20, 22, 20, 12])
ws.append([])
note(ws, "Lamppost pole height (MA1) chosen within a real, cited standard street-light pole range of 15-30 ft [S1]. Industrial pipe radius = 6.625in OD / 2, a real ASME B36.10 Schedule 40, 6-inch NPS standard [S2]. Every other dimension (MA2, MA3, MA4, MA5) is a stated Modeling Assumption -- see the Modeling Assumptions sheet.")

# ---------- Appendix C ----------
ws = wb.create_sheet("Appendix C — Prop Counts")
rows = [
    ("Prop", "Count tested per frame"),
    ("Lamppost", 600),
    ("Industrial pipe", 600),
    ("Sign post", 600),
    ("Total", 1800),
]
for row in rows:
    ws.append(row)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [30, 24])
ws.append([])
note(ws, "MA6 -- stated Modeling Assumption. No public source publishes any specific game's actual per-frame prop density.")

# ---------- Appendix D ----------
ws = wb.create_sheet("Appendix D — Cost Inputs")
rows = [
    ("Item", "Value"),
    ("Per-object culling-test cost, bounding sphere (Option A)", "0.0005 ms"),
    ("Per-object culling-test cost, bounding capsule (Option B)", "0.0015 ms"),
    ("Rendering/overdraw cost per liter of wasted bounding volume", "0.00000002 ms/liter"),
]
for row in rows:
    ws.append(row)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [58, 24])
ws.append([])
note(ws, "MA7, MA8, MA9 -- all three stated Modeling Assumptions, and the case's three most sensitive dials (see the Modeling Assumptions sheet's Sensitivity column). No public source publishes any of these three figures at this specificity.")

# ---------- Modeling Assumptions ----------
ws = wb.create_sheet("Modeling Assumptions")
ws["A1"] = "Modeling Assumptions"
style_title(ws, "A1", size=13)
ws["A2"] = "These figures are NOT sourced. They are stated scenario assumptions chosen by the case author. You may challenge them in discussion -- that is a legitimate move."
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
    ("MA1", "Lamppost pole height", "6.1 m (20 ft)", "Affects the lamppost's bounding sphere radius directly."),
    ("MA2", "Lamppost fixture cap dimensions", "r 0.15 m, h 0.3 m", "Minor -- small relative to the pole."),
    ("MA3", "Industrial pipe length", "4.0 m", "Scales both bounding shapes' volume for this prop; does not change the winner alone."),
    ("MA4", "Sign post height", "2.5 m", "Minor relative to the lamppost/pipe's contribution to the scene total."),
    ("MA5", "Sign post pyramidal cap dimensions", "base 0.2 m, h 0.15 m", "Minor -- small relative to the post."),
    ("MA6", "Scene prop counts", "600 of each type/frame", "Scales both options' totals together; does not flip the winner alone."),
    ("MA7", "Per-object culling-test cost, sphere", "0.0005 ms", "Most sensitive dial -- see FACILITATOR.md / QA_REPORT.md for the full +/-50% flip findings."),
    ("MA8", "Per-object culling-test cost, capsule", "0.0015 ms", "Most sensitive dial -- see FACILITATOR.md / QA_REPORT.md."),
    ("MA9", "Render cost per liter of wasted volume", "0.00000002 ms/L", "Single most sensitive dial in the case -- see FACILITATOR.md / QA_REPORT.md."),
]
for row in ma_rows:
    ws.append(row)
style_header_row(ws, header_row, 4)
set_body_font(ws)
col_widths(ws, [7, 40, 22, 55])
for rr in range(header_row + 1, ws.max_row + 1):
    ws.cell(row=rr, column=4).alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(row=rr, column=2).alignment = Alignment(wrap_text=True, vertical="top")

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
    (4, "D1 — Real volume and surface area of each prop",
     ["Prop", "Component 1 vol/SA", "Component 2 vol/SA", "Total real volume (m3)", "Total real SA (m2)"]),
    (10, "D2 — Bounding sphere volume + wasted volume, per prop and scene total",
     ["Prop", "Sphere radius (m)", "Sphere volume (m3)", "Wasted volume (L)", "Scene total wasted (L)"]),
    (16, "D3 — Bounding capsule volume + wasted volume, per prop and scene total",
     ["Prop", "Capsule radius (m)", "Capsule volume (m3)", "Wasted volume (L)", "Scene total wasted (L)"]),
    (22, "D4 — Total per-frame cost, both options",
     ["Option", "CPU cost (ms)", "Render cost (ms)", "Total cost (ms)", "Margin (%)"]),
    (28, "D5 — Written recommendation",
     ["Winner", "Most sensitive dial", "Your choice (A/B)", "Why"]),
]
for start_row, title, headers in sections:
    ws.cell(row=start_row, column=1, value=title).font = Font(name=ARIAL, bold=True, size=12)
    for c, h in enumerate(headers, start=1):
        ws.cell(row=start_row + 1, column=c, value=h)
    style_header_row(ws, start_row + 1, len(headers))
    for blank_r in range(start_row + 2, start_row + 5):
        for c in range(1, len(headers) + 1):
            ws.cell(row=blank_r, column=c, value=None)

col_widths(ws, [22, 22, 22, 22, 22])

wb.save("cases/the-culling-volume/published/The Culling Volume - Data.xlsx")
print("wrote The Culling Volume - Data.xlsx")
