import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

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
ws["A1"] = "The Cold Hit — Data Workbook"
ws["A1"].font = Font(name="Arial", bold=True, size=14, color=NAVY)
readme_rows = [
    ("", ""),
    ("Case", "The Cold Hit (cases/the-cold-hit)"),
    ("Purpose", "Raw, cited data for Dana Osei's Refer-on-Match-vs-Hold-for-Corroboration cold-hit "
                "DNA referral decision."),
    ("", ""),
    ("Sheet", "Maps to"),
    ("Appendix B — Database Sizes", "case.md Appendix B (state and national search-stage sizes)"),
    ("Appendix C — Match Probability Figures", "case.md Appendix C (per-locus match probability, usable loci, DMP rule)"),
    ("Appendix D — Caseload", "case.md Appendix D (this year's cold-hit caseload figures)"),
    ("Appendix E — Policy Costs", "case.md Appendix E (per-case time costs for each policy)"),
    ("Appendix F — Modeling Assumptions", "case.md Appendix F (MA1-MA5)"),
    ("Appendix G — Sources", "case.md Appendix G (S1-S6, full citations)"),
    ("Work Area", "Blank — for your own D1-D3 calculations. Nothing here is pre-computed."),
    ("", ""),
    ("Note", "This workbook gives you the DATA, not the ANSWER. The random match probability (D1), "
             "the database match probability at each stage (D2), and the cases-closed-per-hour rates "
             "and percent margin (D3) are your own work — see Challenge 3 in the case study. This "
             "workbook does not compute D4 (combination/permutation) or D5 (written explanation) "
             "either; those are worked entirely in your own submission."),
]
r = 2
for a, b in readme_rows:
    ws.cell(row=r, column=1, value=a).font = Font(name="Arial", bold=True, size=10)
    ws.cell(row=r, column=2, value=b).font = Font(name="Arial", size=10)
    ws.cell(row=r, column=2).alignment = Alignment(wrap_text=True)
    r += 1
autosize(ws, [30, 90])

# ---------------- Appendix B ----------------
ws = wb.create_sheet("Appendix B - Database Sizes")
ws.append(["Search stage", "Database", "Profiles searched", "Source", "As of"])
rows = [
    ["Stage 1 (searched first, no hit)", "State DNA Index System — this state's Bureau of Forensic Services data bank", 3368310, "S1", "2024-12-31"],
    ["Stage 2 (searched second — this is where the hit came from)", "National DNA Index System (NDIS) — >14,000,000 offender + >4,000,000 arrestee profiles", 18000000, "S2", "2020-09"],
]
for row in rows:
    ws.append(row)
style_header(ws, ncols=5)
set_font(ws, range(2, len(rows) + 2), range(1, 6))
autosize(ws, [34, 46, 16, 10, 12])
ws.append([])
ws.append(["Note: both real databases have continued to grow since the dates above. This case fixes both counts at the dates in this table and does not update them."])
ws.cell(row=ws.max_row, column=1).font = Font(name="Arial", italic=True, size=9)

# ---------------- Appendix C ----------------
ws = wb.create_sheet("Appendix C - Match Probability")
ws.append(["Figure", "Value", "Notes", "Source"])
rows = [
    ["Representative per-locus match probability", 0.075, "Two unrelated people have roughly this chance of matching by coincidence at any single locus. A representative average across loci, not an exact per-locus figure.", "S3"],
    ["This case's usable loci", 8, "Out of 20 CODIS core loci. A scenario construction chosen to be realistic for a degraded decade-old sample.", "n/a — scenario construction"],
    ["CODIS core loci (full panel size)", 20, "Standard number of loci in a full CODIS profile since Jan 1, 2017.", "S5"],
    ["Database match probability (DMP) rule", "DMP = N x RMP", "N = number of profiles searched, RMP = random match probability for the profile recovered. From the 1996 National Research Council report.", "S6"],
]
for row in rows:
    ws.append(row)
style_header(ws, ncols=4)
set_font(ws, range(2, len(rows) + 2), range(1, 5))
autosize(ws, [34, 14, 60, 26])

# ---------------- Appendix D ----------------
ws = wb.create_sheet("Appendix D - Caseload")
ws.append(["Figure", "Value", "Applies to", "Source"])
rows = [
    ["Cold-hit cases reviewed by the unit this year", 60, "Both policies", "MA1"],
    ["Share of the unit's annual caseload recovered from a partial (fewer than 20-locus) profile like this case's", "60%", "Determines how many of the 60 hits reviewed carry this case's D2 database match probability", "MA2"],
]
for row in rows:
    ws.append(row)
style_header(ws, ncols=4)
set_font(ws, range(2, len(rows) + 2), range(1, 5))
autosize(ws, [56, 12, 46, 10])

# ---------------- Appendix E ----------------
ws = wb.create_sheet("Appendix E - Policy Costs")
ws.append(["Cost", "Value", "When it applies", "Source"])
rows = [
    ["Base investigative file review, per cold-hit case", "6 hours", "Every case, under either policy", "MA3"],
    ["Independent corroboration step, per case", "3 hours", "Every case, only under Policy B (Hold for Corroboration)", "MA4"],
    ["Rework cost when a referral later turns out to have been a coincidental match", "200 hours", "Only under Policy A (Refer on Match), only for cases that turn out to be false — expected count computed from Appendix C's database match probability", "MA5"],
]
for row in rows:
    ws.append(row)
style_header(ws, ncols=4)
set_font(ws, range(2, len(rows) + 2), range(1, 5))
autosize(ws, [56, 12, 50, 10])

# ---------------- Appendix F ----------------
ws = wb.create_sheet("Appendix F - Assumptions")
ws.append(["#", "Assumption", "Value used", "Basis", "Sensitivity"])
rows = [
    ["MA1", "Cold-hit cases reviewed this year", "60", "No public source publishes a specific lab's annual cold-hit volume; set at a scale consistent with a state DNA unit actively working a backlog, informed by the real, published scale of state data-bank hit totals (Appendix G, S1).", "The case's totals scale with this figure, but the ratio between the two policies is not very sensitive to it alone."],
    ["MA2", "Share of the annual caseload from a partial (sub-20-locus) profile", "60%", "No public source publishes this split for any specific lab. Degraded, older cold-case evidence is realistically more likely to yield a partial profile than fresh evidence.", "The case's numbers are sensitive to this figure."],
    ["MA3", "Base investigative file review time, per case", "6 hours/case", "No public source publishes a lab's internal file-review time. Applies equally under both policies.", "Low — affects both policies' totals equally."],
    ["MA4", "Corroboration step time, per case (Policy B only)", "3 hours/case", "No public source publishes a specific corroboration procedure's time cost. Set as a modest fixed add-on representative of a documented alibi/location cross-check.", "Sensitive."],
    ["MA5", "Rework cost per false referral (Policy A only)", "200 hours", "No public source publishes this figure for any lab. Set well above the corroboration cost to reflect that walking back an already-sent referral is a materially larger event.", "Highly sensitive."],
]
for row in rows:
    ws.append(row)
style_header(ws, ncols=5)
set_font(ws, range(2, len(rows) + 2), range(1, 6))
autosize(ws, [6, 40, 18, 60, 40])

# ---------------- Appendix G ----------------
ws = wb.create_sheet("Appendix G - Sources")
ws.append(["#", "Claim", "Value", "Source", "URL", "Date", "Confidence"])
rows = [
    ["S1", "Total DNA data bank profiles uploaded to a state's own CODIS since that state's data-bank law took effect", "3,368,310", "California Department of Justice, Bureau of Forensic Services — Proposition 69 DNA Data Bank Program Report, Fourth Quarter 2024", "https://www.oag.ca.gov/system/files/media/databank-quarterly-rpt-q4-2024.pdf", "as of 2024-12-31", "HIGH"],
    ["S2", "National DNA Index System (NDIS) size", ">14,000,000 offender + >4,000,000 arrestee (used as 18,000,000 combined)", "Combined DNA Index System — Wikipedia, citing FBI-published NDIS statistics", "https://en.wikipedia.org/wiki/Combined_DNA_Index_System", "as of 2020-09", "MEDIUM"],
    ["S3", "Representative per-locus random match probability", "~7.5% (0.075)", "Are the F.B.I.'s Probabilities About DNA Matches Crazy? — Freakonomics", "https://freakonomics.com/2008/08/are-the-fbis-probabilities-about-dna-matches-crazy/", "accessed 2026-09-18", "MEDIUM"],
    ["S4", "CODIS operates as a three-tier hierarchy (LDIS/SDIS/NDIS)", "three levels as described", "National Institute of Justice — CODIS Hierarchy", "https://nij.ojp.gov/nij-hosted-online-training-courses/forensic-dna-education-law-enforcement-decisionmakers/partial-matches/codis-hierarchy", "accessed 2026-09-18", "HIGH"],
    ["S5", "CODIS core loci expanded from 13 to 20 on January 1, 2017", "13 original + 7 added = 20 core loci", "RTI International / SAKI — Switching to 20 Core CODIS Loci and the Impact on SAKI Testing", "https://www.sakitta.org/resources/docs/12104SAKIImpctSAKTstCoreLociv3.pdf", "published 2018", "HIGH"],
    ["S6", "1996 NRC report: database-search match probability = RMP x N", "DMP = N x RMP", "National Academies Press (NRC Committee on DNA Technology in Forensic Science), NCBI Bookshelf", "https://www.ncbi.nlm.nih.gov/books/NBK232615/", "1996 report; accessed 2026-09-18", "HIGH"],
]
for row in rows:
    ws.append(row)
style_header(ws, ncols=7)
set_font(ws, range(2, len(rows) + 2), range(1, 8))
autosize(ws, [6, 40, 30, 40, 40, 16, 12])

# ---------------- Work Area ----------------
ws = wb.create_sheet("Work Area")
ws["A1"] = "Work Area — your own calculations (nothing pre-filled)"
ws["A1"].font = Font(name="Arial", bold=True, size=12, color=NAVY)
labels = [
    "D1: Per-locus match probability (Appendix C) =",
    "D1: Number of usable loci (Appendix C) =",
    "D1: RMP = (per-locus probability) ^ (usable loci) =",
    "D1: Why does multiplying per-locus probabilities require independence? (explain) =",
    "D2: N_state (Appendix B, Stage 1) =",
    "D2: DMP_state = N_state x RMP =",
    "D2: N_national (Appendix B, Stage 2) =",
    "D2: DMP_national = N_national x RMP =",
    "D2: Which stage actually produced this case's hit? =",
    "D3: Cold-hit cases reviewed this year (Appendix D) =",
    "D3: Share from a partial profile (Appendix D) =",
    "D3: Expected false referrals under Policy A = cases x share x DMP_national =",
    "D3: Policy A total hours = (cases x base hours) + (expected false referrals x rework hours) =",
    "D3: Policy B total hours = (cases x base hours) + (cases x corroboration hours) =",
    "D3: Policy A rate = cases / Policy A total hours =",
    "D3: Policy B rate = cases / Policy B total hours =",
    "D3: Percent margin between the two rates =",
    "D3: Which policy wins this year? =",
    "D4: C(20,10) — combination (see case study Challenge 3, D4) =",
    "D4: P(20,10) — permutation (see case study Challenge 3, D4) =",
    "D5: Written explanation using Population, Sample, and Convenience Sampling (see case study Challenge 3, D5) =",
]
r = 3
for lab in labels:
    ws.cell(row=r, column=1, value=lab).font = Font(name="Arial", size=10)
    ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(row=r, column=2).font = Font(name="Arial", size=10)
    ws.cell(row=r, column=2).fill = PatternFill("solid", fgColor="FFF8E1")
    r += 1
autosize(ws, [64, 24])

wb.save("The Cold Hit - Data.xlsx")
print("wrote xlsx")
