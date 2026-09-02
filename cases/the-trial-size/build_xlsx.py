#!/usr/bin/env python3
"""Build the Data workbook for The Trial Size. Raw appendix data only --
never pre-computes D1-D4; students do that work in the Work Area sheet."""
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
ws["A1"] = "The Trial Size — Data Workbook"
style_title(ws, "A1")
ws["A2"] = "MS | Math | Case Study | 2026 | Adventure"
style_sub(ws, "A2")
ws["A5"] = "What this is"
ws["B5"] = ("Raw appendix data from The Trial Size case study, laid out for you to compute over. "
            "Nothing here has been pre-solved -- D1 through D4 (deriving the Cost(n) line, "
            "graphing it, reading the Budget-Remaining line's x-intercept, and solving the "
            "break-even system of equations) are your own work to do.")
ws["A6"] = "Case"
ws["B6"] = "cases/the-trial-size/case.md — see the case study docx for the full Overview, Background, Dilemma, and Challenges."
ws["A8"] = "Sheet"
ws["B8"] = "Maps to"
ws["A9"] = "Appendix A — Serosurvey Cost Data"
ws["B9"] = "Appendix A: Full Precision and Reserve And Expand sample sizes and costs, and the marginal cost per additional participant. The 95% CI half-width column is handed to you pre-computed here (D5 asks you to reproduce it yourself). Sources: S1, S3, S4, S7, S8."
ws["A10"] = "Appendix C — Cluster Expansion Parameters"
ws["B10"] = "Appendix C: existing cluster count, marginal cost per new cluster, total fixed budget, new-district participant density (a disclosed Modeling Assumption), and the resulting new-district CI half-width. Sources: S1, S2, S5, S7, S8."
ws["A11"] = "Appendix D — Precision Formula"
ws["B11"] = "Appendix D: the real, sourced Henderson & Sundaresan (1982) precision formula d = z*sqrt(deff*p(1-p)/n) and its parameters (z, deff, p). D5 asks you to substitute and evaluate it yourself for all three real sample sizes. Sources: S7, S8."
ws["A12"] = "Appendix E — Sources"
ws["B12"] = "Appendix E: full citation table for every figure used, S1-S8."
ws["A13"] = "Modeling Assumptions"
ws["B13"] = "The two disclosed Modeling Assumptions this case uses (p=0.5 maximum-variance convention; new-cluster participant density), matching the case.md Modeling Assumptions section."
ws["A14"] = "D1-D5 Work Area"
ws["B14"] = ("A blank area for your own Cost(n) derivation, graph notes, Budget-Remaining "
             "x-intercept, break-even system-of-equations solution, and CI half-width "
             "substitution/evaluation. This is the assignment -- it is intentionally empty.")
for r in (5, 6, 8, 9, 10, 11, 12, 13, 14):
    ws[f"A{r}"].font = Font(name=ARIAL, bold=(r == 8))
    ws[f"B{r}"].font = Font(name=ARIAL)
    ws[f"B{r}"].alignment = Alignment(wrap_text=True, vertical="top")
col_widths(ws, [30, 100])
ws.row_dimensions[5].height = 55
ws.row_dimensions[6].height = 30
for r in (9, 10, 11, 12, 13):
    ws.row_dimensions[r].height = 30
ws.row_dimensions[14].height = 55

# ---------- Appendix A ----------
ws = wb.create_sheet("Appendix A — Cost Data")
ws.append(["Design", "Sample size tested (n)", "Total cost (USD)", "Resulting 95% CI half-width (Appendix D)"])
rows = [
    ("Full Precision", "658 [S1]", "$68,558 [S1]", "±5.4% [S7, S8]"),
    ("Reserve And Expand (certified-adequate minimum, existing clusters only)", "192 [S3]", "not given -- derive from the Cost(n) line (D1)", "±10.0% [S7, S8]"),
    ("Marginal cost per additional participant (within an existing cluster)", "—", "$30 [S4]", "—"),
]
for r in rows:
    ws.append(r)
style_header_row(ws, 1, 4)
set_body_font(ws)
col_widths(ws, [50, 25, 40, 32])
ws.append([])
ws.append(["Modeling note: the fixed cost of running the existing cluster infrastructure before "
           "any participant is tested is NOT stated directly anywhere. It must be derived "
           "algebraically from the two real data points above (Full Precision's n and total cost, "
           "and the marginal cost per participant) -- that derivation is D1's required "
           "calculation. Reserve And Expand's total cost at n=192 is deliberately left blank in "
           "this sheet for the same reason.", None, None])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)
ws.cell(row=ws.max_row, column=1).alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells(f"A{ws.max_row}:C{ws.max_row}")
ws.row_dimensions[ws.max_row].height = 45

# ---------- Appendix C ----------
ws = wb.create_sheet("Appendix C — Cluster Params")
ws.append(["Parameter", "Value"])
c_rows = [
    ("Existing survey clusters already staffed and permitted", "16 [S2]"),
    ("Marginal cost per additional new cluster opened", "$1,620 [S5]"),
    ("Total fixed survey budget", "$68,558 [S1]"),
    ("Participants tested per newly opened cluster (Modeling Assumption: 192 / 16)", "12/cluster"),
    ("Total new clusters opened by Reserve And Expand's freed budget", "8 (floor of $13,980 / $1,620; $1,020 unspent)"),
    ("Resulting 95% CI half-width for the new, currently unsurveyed district (Appendix D)", "±14.1% [S7, S8]"),
]
for r in c_rows:
    ws.append(r)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [55, 45])
for r in range(2, ws.max_row + 1):
    ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True, vertical="top")

# ---------- Appendix D — Precision Formula ----------
ws = wb.create_sheet("Appendix D — Precision Formula")
ws["A1"] = "Appendix D — The Real Precision-vs-Sample-Size Relationship"
style_title(ws, "A1", size=13)
ws["A3"] = ("The classic reference for this relationship is Henderson RH, Sundaresan T, "
            "\"Cluster sampling to assess immunization coverage...,\" Bulletin of the World Health "
            "Organization 60(2): 253-260 (1982) [S7], the foundational paper behind the "
            "worldwide-standard 30x7 (n=210) design, built to hit a two-sided 95% CI no wider than "
            "+-10 percentage points, assuming a design effect (deff) of 2. A 2026 peer-reviewed "
            "review [S8] quotes the exact numeric derivation: unclustered effective n=96 (at "
            "p=0.5) inflated by deff=2 to actual n=192, rounded up to the classic n=210.")
ws["A3"].font = Font(name=ARIAL, italic=True)
ws["A3"].alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells("A3:D3")
ws.row_dimensions[3].height = 90
ws["A5"] = "The formula:"
ws["A5"].font = Font(name=ARIAL, bold=True)
ws["A6"] = "d = z * SQRT(deff * p*(1-p) / n)"
ws["A6"].font = Font(name=ARIAL, bold=True, size=12)
ws.append([])
ws["A8"] = "Parameter"
ws["B8"] = "Value"
ws["A9"] = "z (95% confidence)"
ws["B9"] = 1.96
ws["A10"] = "deff (design effect)"
ws["B10"] = 2
ws["A11"] = "p (maximum-variance assumption, Modeling Assumption MA1)"
ws["B11"] = 0.5
style_header_row(ws, 8, 2)
set_body_font(ws)
col_widths(ws, [45, 15, 15, 15])

# ---------- Appendix E — Sources ----------
ws = wb.create_sheet("Appendix E — Sources")
ws.append(["#", "Claim", "Value", "Source", "Date", "Confidence"])
d_rows = [
    ("S1", "Total nested measles-rubella serosurvey cost and participant count, Southern Province, Zambia",
     "$68,558 for n=658", "Carcelen AC, Hayford K, Moss WJ, et al., PLOS ONE 2020 (see case.json sources[] for full citation and URL)", "2020-10-15", "HIGH"),
    ("S2", "Number of survey clusters in the nested design", "16 clusters", "Carcelen et al. 2020, PLOS ONE", "2020-10-15", "HIGH"),
    ("S3", "Certified-adequate minimum sample size for the same 16 clusters", "192 children", "Carcelen et al. 2020, PLOS ONE", "2020-10-15", "HIGH"),
    ("S4", "Marginal cost of adding one participant within an existing cluster", "$30/participant", "Carcelen et al. 2020, PLOS ONE", "2020-10-15", "HIGH"),
    ("S5", "Marginal cost of including one additional cluster", "$1,620/cluster", "Carcelen et al. 2020, PLOS ONE", "2020-10-15", "HIGH"),
    ("S6", "Corroborating cost-per-participant order of magnitude (context only, not load-bearing)", "n/a", "Brenzel L, Saxenian H, Stahley K, Dansereau E, Frontiers in Public Health", "2026", "MEDIUM"),
    ("S7", "Classic cluster-survey precision design: 30x7 (n=210) method, +-10% precision target, deff=2",
     "deff=2; target d=+-10%; design n=210", "Henderson RH, Sundaresan T, Bulletin of the World Health Organization 60(2):253-260", "1982", "HIGH"),
    ("S8", "Explicit numeric derivation: effective n=96 -> actual n=192 -> design n=210",
     "effective n=96 -> n=192 -> n=210", "Rhoda DA, Soofi S, Hussain I, et al., Journal of Survey Statistics and Methodology 13(5):587-614", "2026", "HIGH"),
]
for r in d_rows:
    ws.append(r)
style_header_row(ws, 1, 6)
set_body_font(ws)
col_widths(ws, [6, 45, 20, 45, 14, 12])
for r in range(2, ws.max_row + 1):
    ws.cell(row=r, column=2).alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(row=r, column=4).alignment = Alignment(wrap_text=True, vertical="top")

# ---------- Modeling Assumptions ----------
ws = wb.create_sheet("Modeling Assumptions")
ws["A1"] = "Modeling Assumptions"
style_title(ws, "A1", size=13)
ws["A2"] = ("These figures are NOT sourced. They are stated scenario assumptions chosen by the "
            "case author. A Hero may challenge them in discussion -- that is a legitimate move.")
ws["A2"].font = Font(name=ARIAL, italic=True)
ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells("A2:E2")
ws.row_dimensions[2].height = 30
ws.append([])
ws.append(["#", "Assumption", "Value used", "Basis", "Sensitivity"])
ma_rows = [
    ("MA1", "p = 0.5 (maximum-variance assumption) used in the CI half-width formula for both districts",
     "p = 0.5",
     "The true seroprevalence in the new, unsurveyed district is unknown; p=0.5 is the same "
     "conservative convention Henderson & Sundaresan's 1982 design used.",
     "Produces the widest CI half-width for any given n, in both options equally -- does not "
     "favor either design and does not affect margin_pct."),
    ("MA2", "Newly opened clusters tested at the same per-cluster density as the certified-adequate "
     "design (192/16 = 12 participants/cluster)",
     "12 participants/cluster (96 new-district participants total)",
     "Carcelen et al. 2020 never opened new clusters, so no per-new-cluster sample size is "
     "stated; reusing the study's own certified-adequate density is the most conservative, "
     "best-disclosed choice available.",
     "Directly determines the new district's CI half-width (+-14.1%) and therefore the case's "
     "primary_metric and margin_pct -- see case.json balance_test_waiver for the retune analysis."),
]
for r in ma_rows:
    ws.append(r)
style_header_row(ws, 4, 5)
set_body_font(ws)
col_widths(ws, [6, 35, 25, 40, 40])
for r in range(5, ws.max_row + 1):
    for c in (2, 3, 4, 5):
        ws.cell(row=r, column=c).alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[r].height = 60

# ---------- D1-D5 Work Area ----------
ws = wb.create_sheet("D1-D5 Work Area")
ws["A1"] = "Work Area — D1 through D5"
style_title(ws, "A1", size=13)
ws["A2"] = ("This sheet is intentionally blank except for column headers. Pull your raw inputs "
            "from the Appendix A/C/D sheets -- do not retype values by hand where you can "
            "reference the cell.")
ws["A2"].font = Font(name=ARIAL, italic=True)
ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells("A2:E2")
ws.row_dimensions[2].height = 40

sections = [
    (4, "D1 — Cost(n) = fixed + marginal·n, derived step by step",
     ["Two known points (n, cost)", "Marginal cost (given)", "Fixed cost (solve for it)", "Cost(n) equation"]),
    (9, "D2 — Graph of Cost(n)",
     ["n range plotted", "Full Precision point plotted", "Reserve And Expand point plotted", "Notes"]),
    (14, "D3 — Budget-Remaining line R(n)",
     ["R(n) equation", "x-intercept", "What the x-intercept represents"]),
    (19, "D4 — Break-even system of equations",
     ["Equation 1 (Full Precision cost)", "Equation 2 (Reserve And Expand cost)", "Break-even n (solved algebraically)", "Work shown"]),
    (24, "D5 — CI half-width d = z*sqrt(deff*p(1-p)/n), substitution and evaluation",
     ["n = 658 (substitution + d)", "n = 192 (substitution + d)", "n = 96 (substitution + d)", "Which design(s) clear the WHO +-10% target, and where"]),
]
for start_row, title, headers in sections:
    ws.cell(row=start_row, column=1, value=title).font = Font(name=ARIAL, bold=True, size=12)
    for c, h in enumerate(headers, start=1):
        ws.cell(row=start_row + 1, column=c, value=h)
    style_header_row(ws, start_row + 1, len(headers))
    for blank_r in range(start_row + 2, start_row + 4):
        for c in range(1, len(headers) + 1):
            ws.cell(row=blank_r, column=c, value=None)

col_widths(ws, [32, 32, 32, 32, 32])

wb.save("cases/the-trial-size/published/The Trial Size - Data.xlsx")
print("wrote The Trial Size - Data.xlsx")
