import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
import os

NAVY = "1A3A5C"
wb = openpyxl.Workbook()

def style_header(ws, row=1, ncols=6):
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = Font(name="Arial", bold=True, color="FFFFFF", size=11)
        cell.fill = PatternFill("solid", fgColor=NAVY)
        cell.alignment = Alignment(vertical="center", wrap_text=True)

def autosize(ws, widths):
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w

def set_font(ws, rows, cols, name="Arial", size=10):
    for r in rows:
        for c in cols:
            ws.cell(row=r, column=c).font = Font(name=name, size=size)
            ws.cell(row=r, column=c).alignment = Alignment(wrap_text=True, vertical="top")

# ---------------- README ----------------
ws = wb.active
ws.title = "README"
ws["A1"] = "The Odd Lot — Data Workbook"
ws["A1"].font = Font(name="Arial", bold=True, size=14, color=NAVY)
readme_rows = [
    ("", ""),
    ("Case", "The Odd Lot (cases/the-odd-lot)"),
    ("Purpose", "Raw, cited zoning/geometry data for Priya Chandrasekaran's Plat-As-Is-vs-"
                "Replat-and-Consolidate recommendation decision."),
    ("", ""),
    ("Sheet", "Maps to"),
    ("Appendix B — Zoning Rules", "case.md Appendix B (R7-2 FAR and required rear yard depth)"),
    ("Appendix C — As-Is Parcels", "case.md Appendix C (three parcels' areas, rear/notch lot-line "
                                    "lengths, interior angles)"),
    ("Appendix D — Consolidated Lot", "case.md Appendix D (Option B's consolidated lot dimensions "
                                       "and the octagon plaza)"),
    ("Appendix E — Timeline & Housing Figures", "case.md Appendix E (unit size, lead times, "
                                                  "planning horizon)"),
    ("Appendix F — Modeling Assumptions", "case.md Appendix F (MA1-MA4)"),
    ("Appendix G — Sources", "case.md Appendix G (S1-S5, with full source links)"),
    ("Work Area", "Blank — for your own D1-D4 calculations. Nothing here is pre-computed."),
    ("", ""),
    ("Note", "This workbook gives you the DATA, not the ANSWER. The classification table, "
             "L1's missing angle, both options' required-yard/buildable-footprint figures, the "
             "octagon plaza area, the dwelling-unit counts, the unit-years totals, and the "
             "percent margin are all your own work — see Challenge 3 (D1-D4) in the case study."),
]
r = 2
for a, b in readme_rows:
    ws.cell(row=r, column=1, value=a).font = Font(name="Arial", bold=True, size=10)
    ws.cell(row=r, column=2, value=b).font = Font(name="Arial", size=10)
    ws.cell(row=r, column=2).alignment = Alignment(wrap_text=True)
    r += 1
autosize(ws, [30, 95])

# ---------------- Appendix B ----------------
ws = wb.create_sheet("Appendix B - Zoning Rules")
ws.append(["Rule", "Value", "Applies to", "Source (case.json sources[].id)"])
rows = [
    ["Maximum residential floor area ratio (FAR), standard, R7-2 district", 3.44,
     "Both options — total buildable floor area = FAR x buildable footprint", "S2"],
    ["Required rear yard depth", "30 feet, at every rear lot line", "Both options", "S3"],
]
for row in rows:
    ws.append(row)
style_header(ws, ncols=4)
set_font(ws, range(2, len(rows) + 2), range(1, 5))
autosize(ws, [46, 26, 40, 18])

# ---------------- Appendix C ----------------
ws = wb.create_sheet("Appendix C - As-Is Parcels")
ws.append(["Parcel", "Shape", "Area (sq ft)", "Front lot line (street, ft)",
           "Rear/notch lot-line length requiring a yard (ft)",
           "Interior angles (deg), in order around the parcel"])
rows = [
    ["L1", "Pentagon (convex)", 11000, 80, 40, "90, 90, 141.3, 128.7, ? (Challenge D1)"],
    ["L2", "Hexagon (concave — two notch corners)", 7900, 60, "80 + 60 + 64 = 204",
     "90, 77.5, 192.5, 90, 51.3, 218.7"],
    ["L3", "Pentagon (convex)", 11100, 60, 80, "102.5, 90, 90, 90, 167.5"],
]
for row in rows:
    ws.append(row)
style_header(ws, ncols=6)
set_font(ws, range(2, len(rows) + 2), range(1, 7))
autosize(ws, [10, 34, 14, 22, 40, 42])
ws["A6"] = ("Reading note: for L1 and L3, the rear/notch length is the single lot line farthest "
            "from the front street. For L2 (concave), this case treats the required yard as "
            "running along three lot lines: the one farthest from the front street, plus the two "
            "lot lines forming the inward notch — see case.md Appendix C and Appendix F (MA2).")
ws["A6"].font = Font(name="Arial", italic=True, size=9)
ws["A6"].alignment = Alignment(wrap_text=True)
ws.merge_cells("A6:F8")

# ---------------- Appendix D ----------------
ws = wb.create_sheet("Appendix D - Consolidated Lot")
ws.append(["Figure", "Value", "Source"])
rows = [
    ["Consolidated lot dimensions", "200 ft (front) x 150 ft (depth)", "MA1"],
    ["Consolidated lot area", "30,000 sq ft (same total area as the three as-is parcels combined)", "MA1"],
    ["Rear lot-line length", "200 ft", "MA1"],
    ["Required yard depth", "30 feet", "S3"],
    ["", "", ""],
    ["Plaza — shape", "Regular octagon (8 equal sides)", "constructed scenario"],
    ["Plaza — side length", "30 ft", "constructed scenario"],
    ["Plaza — apothem (center-to-side distance)", "36.2 ft", "constructed scenario"],
    ["Real minimum public plaza area, NYC Zoning Resolution S37-712", "2,000 sq ft", "S4"],
]
for row in rows:
    ws.append(row)
style_header(ws, ncols=3)
set_font(ws, range(2, len(rows) + 2), range(1, 4))
autosize(ws, [52, 56, 20])

# ---------------- Appendix E ----------------
ws = wb.create_sheet("Appendix E - Timeline & Housing")
ws.append(["Figure", "Value", "Applies to", "Source"])
rows = [
    ["Average new-apartment unit size, this region", "714 sq ft/unit", "Both options", "S5"],
    ["Lead time to start of construction, Plat As-Is", "6 months", "Option A", "MA3"],
    ["Lead time to start of construction, Replat & Consolidate", "18 months", "Option B", "MA3"],
    ["City's stated development planning window", "10 years (120 months)", "Both options", "MA4"],
]
for row in rows:
    ws.append(row)
style_header(ws, ncols=4)
set_font(ws, range(2, len(rows) + 2), range(1, 5))
autosize(ws, [48, 22, 16, 12])

# ---------------- Appendix F ----------------
ws = wb.create_sheet("Appendix F - Assumptions")
ws.append(["#", "Assumption", "Value used", "Basis", "Sensitivity"])
rows = [
    ["MA1", "The three as-is parcels' exact dimensions, areas, and shapes",
     "As tabulated in Appendix C (11,000 / 7,900 / 11,100 sq ft; L2 concave)",
     "Constructed to be consistent with the real, cited pattern of irregular parcels formed "
     "where a diagonal road crosses a rectangular grid (Appendix A, S1) — not a specific real "
     "address's surveyed parcel data.",
     "The whole comparison depends on these shapes; a different partition of the same 30,000 "
     "sq ft would change how much area each option loses to required yards."],
    ["MA2", "The simplified yard rule: every non-front lot line requires the yard, and a "
     "concave parcel's notch lot lines are also treated as requiring it",
     "As applied in Appendix C",
     "Real zoning lot-line classification for irregular, multi-frontage parcels is materially "
     "more detailed than this case models — disclosed simplification so the arithmetic is "
     "tractable at this grade band.",
     "Affects both options in the same direction (irregular shapes lose more); not the main "
     "driver of which option wins."],
    ["MA3", "Lead time to start of construction for each option", "6 months (A), 18 months (B)",
     "No public source publishes standard permit-review or lot-merger-filing timelines for a "
     "specific city; set to reflect that a lot-line merger genuinely requires additional real "
     "process (owner agreements, a replat filing) beyond standard permit review.",
     "Highly sensitive."],
    ["MA4", "The city's stated development planning window", "10 years / 120 months",
     "No single universal planning horizon exists across cities; many long-range housing plans "
     "use multi-year horizons in this general range. Set as a disclosed scenario dial.",
     "Highly sensitive — this is also the lever the case's discussion twist pulls."],
]
for row in rows:
    ws.append(row)
style_header(ws, ncols=5)
set_font(ws, range(2, len(rows) + 2), range(1, 6))
autosize(ws, [6, 34, 26, 50, 34])

# ---------------- Appendix G ----------------
ws = wb.create_sheet("Appendix G - Sources")
ws.append(["#", "Claim", "Value", "Org / Title", "URL", "Accessed", "Confidence"])
rows = [
    ["S1", "A pre-grid diagonal road (Broadway) crossing Manhattan's 1811 street grid created "
     "triangular and irregular parcels/plazas at its crossings, including Union Square, Madison "
     "Square, Herald Square, Times Square, and Columbus Circle", "as described",
     "Museum of the City of New York — Broadway and Its Bowties, The Greatest Grid",
     "https://thegreatestgrid.mcny.org/greatest-grid/broadway-and-its-bowties",
     "2026-09-18", "HIGH"],
    ["S2", "Maximum residential floor area ratio for an R7-2 district (standard)", "3.44",
     "NYC Department of City Planning — Zoning Resolution S23-22",
     "https://zr.planning.nyc.gov/article-ii/chapter-3/23-22", "2026-09-18", "HIGH"],
    ["S3", "Required rear yard depth in R7 and R8 residence districts", "not less than 30 feet",
     "NYC Department of City Planning — Zoning Resolution S24-36",
     "https://zoningresolution.planning.nyc.gov/article-ii/chapter-4/24-36", "2026-09-18", "HIGH"],
    ["S4", "Minimum area of a public plaza that earns a zoning floor-area bonus",
     "not less than 2,000 sq ft", "NYC Department of City Planning — Zoning Resolution S37-712",
     "https://zoningresolution.planning.nyc.gov/article-iii/chapter-7/37-712", "2026-09-18", "HIGH"],
    ["S5", "Average size of a new apartment unit, a real U.S. city (used as this case's regional "
     "unit-size figure)", "714 sq ft/unit (Brooklyn, NY)",
     "RentCafe, citing Yardi Matrix — National Average Apartment Size report",
     "https://www.rentcafe.com/blog/rental-market/market-snapshots/national-average-apartment-size/",
     "2026-09-18", "HIGH"],
]
for row in rows:
    ws.append(row)
style_header(ws, ncols=7)
set_font(ws, range(2, len(rows) + 2), range(1, 8))
autosize(ws, [6, 42, 22, 40, 46, 14, 14])

# ---------------- Work Area ----------------
ws = wb.create_sheet("Work Area")
ws["A1"] = "Work Area — your own calculations (nothing pre-filled)"
ws["A1"].font = Font(name="Arial", bold=True, size=12, color=NAVY)
labels = [
    "D1: L1 classification (Polygon / Irregular Polygon / Convex / Concave) =",
    "D1: L2 classification (Polygon / Irregular Polygon / Convex / Concave) =",
    "D1: L3 classification (Polygon / Irregular Polygon / Convex / Concave) =",
    "D1: Which parcel is concave, and at which listed vertex/vertices is the notch? =",
    "D1: L1's missing interior angle = 540 - (90+90+141.3+128.7) =",
    "D2: L1 required-yard area = 40 x 30 =",
    "D2: L1 buildable footprint = 11,000 - required yard =",
    "D2: L2 required-yard area = 204 x 30 =",
    "D2: L2 buildable footprint = 7,900 - required yard =",
    "D2: L3 required-yard area = 80 x 30 =",
    "D2: L3 buildable footprint = 11,100 - required yard =",
    "D2: Combined buildable footprint (A) =",
    "D2: Combined buildable-footprint percentage (A) =",
    "D3: Consolidated lot required-yard area = 200 x 30 =",
    "D3: Consolidated lot buildable footprint (B) =",
    "D3: Buildable-footprint percentage (B) =",
    "D3: Octagon plaza perimeter = 8 x side length =",
    "D3: Octagon plaza area = 1/2 x perimeter x apothem =",
    "D3: Does the plaza clear the 2,000 sq ft minimum? =",
    "D4: Dwelling units, Option A = buildable A x FAR / unit size =",
    "D4: Dwelling units, Option B = buildable B x FAR / unit size =",
    "D4: Unit-years, Option A = units A x (horizon - lead A) / 12 =",
    "D4: Unit-years, Option B = units B x (horizon - lead B) / 12 =",
    "D4: Percent margin between the two unit-year totals =",
    "D4: Which option wins on these numbers? =",
    "D5: Written reflection (see case study Challenge 3, D5) =",
]
r = 3
for lab in labels:
    ws.cell(row=r, column=1, value=lab).font = Font(name="Arial", size=10)
    ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True)
    ws.cell(row=r, column=2).font = Font(name="Arial", size=10)
    ws.cell(row=r, column=2).fill = PatternFill("solid", fgColor="FFF8E1")
    r += 1
autosize(ws, [62, 26])

out_path = os.path.join(os.path.dirname(__file__), "published", "The Odd Lot - Data.xlsx")
wb.save(out_path)
print("wrote xlsx", out_path)
