#!/usr/bin/env python3
"""Build the Data workbook for Fizzer Order. Raw appendix data only -- never
pre-computes D1-D5; students do that work in the Work Area sheet."""
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

def col_widths(ws, widths):
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w


wb = openpyxl.Workbook()

# ---------- README ----------
ws = wb.active
ws.title = "README"
ws["A1"] = "Fizzer Order — Data Workbook"
style_title(ws, "A1")
ws["A2"] = "MS | Math | Case Study | 2026-27 | Heroes Academy"
style_sub(ws, "A2")
ws["A5"] = "What this is"
ws["B5"] = ("Raw appendix data from the Fizzer Order case study, laid out for you to compute over. "
            "Nothing here has been pre-solved -- D1 through D5 (surface area, interior volume, "
            "usable capacity, cost per Mini Fizzer delivered, and shipping-carton footprint) are "
            "your own work to do.")
ws["A6"] = "Case"
ws["B6"] = "cases/fizzer-order/case.md — see the case study docx for the full Overview, Background, Dilemma, and Challenges."
ws["A8"] = "Sheet"
ws["B8"] = "Maps to"
rows = [
    ("Appendix B — Mini Fizzer Spec", "Mini Fizzer diameter. Source: S2."),
    ("Appendix C — Box Options Spec", "Peak Box and Twist Cone dimensions; loose-fill packing figure. Source: S3."),
    ("Appendix D — Material Cost", "Cardstock price basis for both options. Source: S1."),
    ("Appendix E — Assumptions", "MA1 (uniform packing figure) and MA2 (tooling lockout)."),
    ("Appendix F — Shipping Carton Reference", "Carton price and interior dimensions. Source: S4."),
    ("Appendix G — Sources", "Full citation table for every figure used, S1-S4."),
    ("D1-D5 Work Area", "A blank area for your own surface-area table, volume table, usable-capacity "
                          "table, cost-per-Mini-Fizzer comparison, and shipping-footprint estimate. "
                          "This is the assignment -- it is intentionally empty."),
]
r = 9
for label, mapping in rows:
    ws[f"A{r}"] = label
    ws[f"B{r}"] = mapping
    r += 1
for rr in (5, 6, 8, *range(9, r)):
    ws[f"A{rr}"].font = Font(name=ARIAL, bold=(rr == 8))
    ws[f"B{rr}"].font = Font(name=ARIAL)
    ws[f"B{rr}"].alignment = Alignment(wrap_text=True, vertical="top")
col_widths(ws, [30, 100])
ws.row_dimensions[5].height = 45
ws.row_dimensions[6].height = 30
for rr in range(9, r):
    ws.row_dimensions[rr].height = 30

# ---------- Appendix B ----------
ws = wb.create_sheet("Appendix B — Mini Fizzer Spec")
ws.append(["Quantity", "Value"])
b_rows = [
    ("Shape", "Sphere"),
    ("Diameter (in)", "1.00 [S2]"),
    ("Radius (in)", "0.50 (derived: diameter / 2)"),
]
for row in b_rows:
    ws.append(row)
style_header_row(ws, 1, 2)
col_widths(ws, [46, 40])

# ---------- Appendix C ----------
ws = wb.create_sheet("Appendix C — Box Options Spec")
ws.append(["Quantity", "Option A — The Peak Box", "Option B — The Twist Cone"])
c_rows = [
    ("Shape", "Square pyramid", "Right circular cone"),
    ("Base", "Square, 2.60 in per side", "Circular, 1.60 in radius (3.20 in diameter)"),
    ("Height (in)", "3.50", "3.30"),
]
for row in c_rows:
    ws.append(row)
ws.append(["Loose-fill packing figure (applies to both options)", "~64% [S3]", ""])
style_header_row(ws, 1, 3)
col_widths(ws, [46, 34, 34])

# ---------- Appendix D ----------
ws = wb.create_sheet("Appendix D — Material Cost")
ws.append(["Quantity", "Value"])
d_rows = [
    ("Material", "110 lb. index cardstock, white [S1]"),
    ("Sheet size priced (in)", "8.5 x 11 (93.5 sq in)"),
    ("Price per 250-sheet pack (USD)", "20.99 [S1]"),
    ("Price per individual sheet (USD, derived)", "0.08396"),
    ("Price per square inch (USD, derived)", "0.00089797"),
]
for row in d_rows:
    ws.append(row)
style_header_row(ws, 1, 2)
col_widths(ws, [46, 40])

# ---------- Appendix E ----------
ws = wb.create_sheet("Appendix E — Assumptions")
ws.append(["#", "Assumption", "Value used", "Basis"])
e_rows = [
    ("MA1", "Whether the 64% random loose-packing figure applies equally to the Peak Box and the tapering Twist Cone",
     "Applied identically to both options",
     "No published figure exists specifically for a tapering cone; this case applies the box/general figure to both shapes as a stated simplification."),
    ("MA2", "Mold-shop tooling lockout: whether a second shape could be tooled mid-season",
     "No -- one shape, one season",
     "Mold-shop lead time measured in weeks against a fixed holiday production window and retail reset date."),
]
for row in e_rows:
    ws.append(row)
style_header_row(ws, 1, 4)
col_widths(ws, [6, 46, 26, 60])
for row in ws.iter_rows(min_row=2):
    for cell in row:
        cell.alignment = Alignment(wrap_text=True, vertical="top")

# ---------- Appendix F ----------
ws = wb.create_sheet("Appendix F — Shipping Ref")
ws.append(["Quantity", "Value"])
f_rows = [
    ("Carton", "12 x 12 x 12 in corrugated shipping carton [S4]"),
    ("Interior floor dimensions, one layer (sq in)", "144 (12 x 12)"),
    ("Price per carton, bundle of 25 (USD)", "1.16 [S4]"),
]
for row in f_rows:
    ws.append(row)
style_header_row(ws, 1, 2)
col_widths(ws, [46, 40])

# ---------- Appendix G ----------
ws = wb.create_sheet("Appendix G — Sources")
ws.append(["id", "Claim", "Value", "Source", "Accessed", "Confidence"])
g_rows = [
    ("S1", "Price of one 250-sheet pack of 110 lb. index cardstock, 8.5 in x 11 in",
     "$20.99 per 250-sheet pack",
     "Quill.com, Neenah Exact Index 110 lb. Cardstock Paper (WAU40411) -- https://www.quill.com/neenah-exact-index-110-lb-cardstock-paper-85-x-11-white-250-sheets-pack-wau40411/cbs/52275455.html",
     "2026-09-09", "HIGH"),
    ("S2", "Diameter of a mini bath bomb made from a commercial mini bath bomb mold",
     "1.00 in",
     "GumballStuff.com, Mini Bath Bomb Molds, Round, Clear, 1-inch in diameter -- https://www.gumballstuff.com/mini-bath-bomb-molds-round-clear-1-inch-in-diameter/",
     "2026-09-09", "HIGH"),
    ("S3", "Volume fraction filled when identical spheres are randomly poured/settled into a container",
     "~64%",
     "Wikipedia, Random close pack -- https://en.wikipedia.org/wiki/Random_close_pack",
     "2026-09-09", "MEDIUM"),
    ("S4", "Price and interior dimensions of a 12x12x12 in corrugated shipping carton, bundle of 25",
     "$1.16/carton; 12x12x12 in interior",
     "Uline, 12 x 12 x 12in Corrugated Boxes (S-4125) -- https://www.uline.com/Product/Detail/S-4125/Corrugated-Boxes-200-Test/12-x-12-x-12-Corrugated-Boxes",
     "2026-09-09", "HIGH"),
]
for row in g_rows:
    ws.append(row)
style_header_row(ws, 1, 6)
col_widths(ws, [6, 40, 22, 70, 12, 12])
for row in ws.iter_rows(min_row=2):
    for cell in row:
        cell.alignment = Alignment(wrap_text=True, vertical="top")

# ---------- Work Area ----------
ws = wb.create_sheet("D1-D5 Work Area")
ws["A1"] = "Work Area -- your own calculations"
style_title(ws, "A1", size=12)
ws["A2"] = ("Blank on purpose. Build your D1 surface-area table, D2 volume table, D3 usable-capacity "
            "table, D4 cost-per-Mini-Fizzer comparison, and D5 shipping-footprint estimate here. "
            "Use Appendices B-D and F above for your inputs.")
ws["A2"].font = Font(name=ARIAL, italic=True)
ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells("A2:F2")
ws.row_dimensions[2].height = 45
headers = ["D#", "Quantity", "Option A (Peak Box)", "Option B (Twist Cone)", "Formula/notes", ""]
ws.append([])
ws.append(headers)
style_header_row(ws, 4, 6)
col_widths(ws, [8, 30, 22, 22, 40, 10])

for ws_ in wb.worksheets:
    for row in ws_.iter_rows():
        for cell in row:
            if cell.value is not None and cell.font.name != ARIAL:
                cell.font = Font(name=ARIAL, size=cell.font.size or 11, bold=cell.font.bold,
                                  italic=cell.font.italic, color=cell.font.color)

out_path = "cases/fizzer-order/published/Fizzer Order - Data.xlsx"
wb.save(out_path)
print("wrote", out_path)
