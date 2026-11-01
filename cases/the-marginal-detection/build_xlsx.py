#!/usr/bin/env python3
"""Build the Data workbook for The Marginal Detection. Raw appendix data only --
never pre-computes sig_naive/sig_robust; students do that work in the work-area sheet."""
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
ws["A1"] = "The Marginal Detection — Data Workbook"
style_title(ws, "A1")
ws["A2"] = "MS | Math | Case Study | 2026 | Adventure"
style_sub(ws, "A2")
ws["A5"] = "What this is"
ws["B5"] = ("Raw appendix data from The Marginal Detection case study, laid out for you to "
            "compute over. Nothing here has been pre-solved -- the sheets give you the case's "
            "20-point light curve and stated modeling assumptions; the line of best fit, the "
            "box-and-whisker five-number summary, and both significance ratios (D2-D4) are "
            "your work to do.")
ws["A6"] = "Case"
ws["B6"] = ("cases/the-marginal-detection/case.md — see the case study docx for the full "
            "Overview, Background, Dilemma, and Challenges.")
ws["A8"] = "Sheet"
ws["B8"] = "Maps to"
mapping = [
    ("Appendix A — Light Curve", "All 20 flux measurements (time step, minutes elapsed, flux in ppm, in-transit flag). Source: MA1 (stated modeling assumption, bounded by real TESS precision figures [S1])."),
    ("Appendix B — Threshold", "The Sable Peak Survey's own 3.0-sigma follow-up threshold. Source: MA2."),
    ("Appendix C — Real Anchors", "Kepler's real 7.1-sigma detection threshold and TESS's real photometric precision figures, used to bound this case's numbers. Sources: [S1], [S2]."),
    ("Modeling Assumptions", "MA1 and MA2, their basis, and their stated sensitivity -- reproduced from case.md so you don't have to cross-reference the docx while you work."),
    ("D1-D5 Work Area", "A blank area for your own scatter plot inputs, line-of-best-fit computation, naive significance ratio, box-and-whisker five-number summary, robust significance ratio, and written recommendation. This is the assignment -- it is intentionally empty."),
]
r = 9
for label, desc in mapping:
    ws.cell(row=r, column=1, value=label).font = Font(name=ARIAL, bold=True)
    c = ws.cell(row=r, column=2, value=desc)
    c.font = Font(name=ARIAL)
    c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[r].height = 30 if len(desc) < 140 else 45
    r += 1
col_widths(ws, [30, 95])
ws.row_dimensions[5].height = 45
ws.row_dimensions[6].height = 30

# ---------- Appendix A ----------
ws = wb.create_sheet("Appendix A — Light Curve")
FLUX = [127, 128, -12, -40, 9, 68, -17, -112, -257, -221, -167, -215, -68, -51, -17, -50, 9, 46, 146, 83]
TRANSIT = {8, 9, 10, 11}
ws.append(["Time step (t)", "Minutes elapsed", "Flux (ppm deviation)", "In transit?"])
for i, v in enumerate(FLUX):
    ws.append([i, i * 15, v, "TRANSIT" if i in TRANSIT else ""])
style_header_row(ws, 1, 4)
set_body_font(ws)
col_widths(ws, [14, 18, 20, 14])
ws.append([])
note(ws, "MA1 -- stated Modeling Assumption. No survey publishes a specific still-unconfirmed candidate's raw pipeline output. Noise scale bounded by TESS's own published precision figures [S1]; dip size set ~100x below a real confirmed transit's depth [S5].")

# ---------- Appendix B ----------
ws = wb.create_sheet("Appendix B — Threshold")
rows = [
    ("Quantity", "Value"),
    ("Sable Peak Survey's follow-up significance threshold (worth a second look)", "3.0 sigma [MA2]"),
    ("Distribution-aware noise conversion constant (IQR -> sigma-comparable spread)", "0.7413 (standard statistics conversion)"),
]
for row in rows:
    ws.append(row)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [60, 40])
ws.append([])
note(ws, "MA2 -- stated Modeling Assumption. No public survey policy document states any specific survey's own internal follow-up bar. Set well below Kepler's real, formal 7.1-sigma discovery threshold [S2].")

# ---------- Appendix C ----------
ws = wb.create_sheet("Appendix C — Real Anchors")
rows = [
    ("Quantity", "Value"),
    ("Kepler mission's formal Threshold Crossing Event detection cutoff", "7.1 sigma [S2]"),
    ("TESS pre-flight design photometric precision, 1-hour bin, T=10 mag", "200 ppm [S1]"),
    ("TESS in-flight noise floor, brightest stars", "~20 ppm [S1]"),
    ("HD 189733 b real confirmed transit depth (scale comparison)", "~2.4% / ~24,000 ppm [S5]"),
]
for row in rows:
    ws.append(row)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [65, 30])
ws.append([])
note(ws, "Source [S1]: Research Notes of the AAS, 'Photometry of 10 Million Stars from the First Two Years of TESS Full Frame Images: Part II' (iopscience.iop.org/article/10.3847/2515-5172/abca2d), Nov 2020, HIGH. Source [S2]: Tenenbaum et al., 'Detection of Potential Transit Signals in the First Twelve Quarters of Kepler Mission Data' (arxiv.org/abs/1212.2915), Dec 2012, HIGH. Source [S5]: NASA Exoplanet Archive, HD 189733 b overview page, accessed 2026-09-18, HIGH.")

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
    ("MA1", "The candidate's full 20-point overnight light curve", "See Appendix A", "Load-bearing for both D3 and D4 -- a different, still-plausible 20-point night could change one or both significance numbers."),
    ("MA2", "Sable Peak's own follow-up significance threshold", "3.0", "Both computed significance numbers sit close to this exact value on opposite sides -- the single most sensitive dial in this case."),
]
for row in ma_rows:
    ws.append(row)
style_header_row(ws, header_row, 4)
set_body_font(ws)
col_widths(ws, [7, 45, 20, 60])
for rr in range(header_row + 1, ws.max_row + 1):
    ws.cell(row=rr, column=4).alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(row=rr, column=2).alignment = Alignment(wrap_text=True, vertical="top")

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
    (4, "D1 — Scatter plot data check (plot this in your own chart tool)",
     ["Time step", "Minutes elapsed", "Flux (ppm)", "In transit?"]),
    (10, "D2 — Line of best fit through the 16 out-of-transit points",
     ["Slope (m)", "Intercept (c)", "Correlation strength (weak/moderate/strong)", "Non-linear? (Y/N + why)"]),
    (14, "D3 — Naive significance ratio",
     ["Residual SD (ppm)", "Dip depth vs. line (ppm)", "sig_naive = dip / residual SD", "Clears 3.0? (Y/N)"]),
    (18, "D4 — Box-and-whisker five-number summary + robust ratio",
     ["Min", "Q1", "Median", "Q3", "Max", "IQR", "0.7413xIQR", "Dip depth vs. median (ppm)", "sig_robust", "Clears 3.0? (Y/N)"]),
    (23, "D5 — Written recommendation",
     ["Both ratios stated?", "Disagreement explained?", "Your choice (A/B)", "Why"]),
]
for start_row, title, headers in sections:
    ws.cell(row=start_row, column=1, value=title).font = Font(name=ARIAL, bold=True, size=12)
    for c, h in enumerate(headers, start=1):
        ws.cell(row=start_row + 1, column=c, value=h)
    style_header_row(ws, start_row + 1, len(headers))
    for blank_r in range(start_row + 2, start_row + 4):
        for c in range(1, len(headers) + 1):
            ws.cell(row=blank_r, column=c, value=None)

col_widths(ws, [22, 20, 20, 20, 20, 18, 18, 18, 16, 16])

wb.save("cases/the-marginal-detection/published/The Marginal Detection - Data.xlsx")
print("wrote The Marginal Detection - Data.xlsx")
