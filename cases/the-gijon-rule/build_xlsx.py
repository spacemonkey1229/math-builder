#!/usr/bin/env python3
"""Data workbook for The Gijon Rule (SKILL 1b): the tabular appendix data a student computes over
(Appendix B match results, Appendix D final tables, Appendix C grid skeleton) plus a clearly
marked blank Work Area. Raw cited values only: NO standings, points, goal differences, safe-cell
counts, percents, rankings or recommendations are pre-computed anywhere. No formulas are used."""
import os
import re
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "published", "The Gijon Rule - Data.xlsx")
NAVY = "1A3A5C"
WORK = "FFF8E1"
thin = Side(style="thin", color="B8C2CE")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)

md = open(os.path.join(HERE, "case.md"), encoding="utf-8").read()


def table_rows(after_heading_re):
    m = re.search(after_heading_re + r".*?\n((?:\|[^\n]*\n)+)", md, re.S)
    rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in m.group(1).splitlines()]
    return [r for r in rows[2:]], rows[0]


wb = openpyxl.Workbook()


def header(ws, row, ncols, start=1):
    for c in range(start, start + ncols):
        cell = ws.cell(row=row, column=c)
        cell.font = Font(name="Arial", bold=True, color="FFFFFF", size=10)
        cell.fill = PatternFill("solid", fgColor=NAVY)
        cell.alignment = Alignment(vertical="center", horizontal="center", wrap_text=True)
        cell.border = BOX


def body(ws, r0, r1, c0, c1, center=False):
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            cell = ws.cell(row=r, column=c)
            cell.font = Font(name="Arial", size=10)
            cell.alignment = Alignment(wrap_text=True, vertical="top", horizontal="center" if center else "left")
            cell.border = BOX


def widths(ws, ws_widths):
    for i, w in enumerate(ws_widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w


def work(ws, r0, r1, c0, c1):
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            cell = ws.cell(row=r, column=c)
            cell.fill = PatternFill("solid", fgColor=WORK)
            cell.border = BOX
            cell.font = Font(name="Arial", size=10)
            cell.alignment = Alignment(horizontal="center", vertical="center")


# ---------------- README ----------------
ws = wb.active
ws.title = "README"
ws["A1"] = "The Gijon Rule - Data Workbook"
ws["A1"].font = Font(name="Arial", bold=True, size=14, color=NAVY)
rows = [
    ("", ""),
    ("Case", "The Gijon Rule (Math Builder case study, MS | Math | 2026-27)"),
    ("Purpose", "The raw, cited 1982 World Cup data and the empty Algeria-Chile grid skeleton from the case study, so you can "
                "build the Group 2 standings, check the other five groups, and fill in the grids in a spreadsheet instead of by hand."),
    ("", ""),
    ("Sheet", "Maps to"),
    ("Appendix A and C - Rules", "Appendix A (the 1982 tie-break ladder) and Appendix C (the two options' ladders and the safe / not safe / unresolved definitions)"),
    ("Appendix B - Group 2 Matches", "Appendix B: the six Group 2 matches, with goals split into two number columns. Sources S1, S2, S3."),
    ("Appendix D - 1982 Groups", "Appendix D: final W / D / L / GF / GA for every team in all six groups, plus blank work columns. Sources S1, S4-S8."),
    ("Appendix F - Assumptions", "Appendix F: modeling assumptions MA1-MA6 (stated choices, not sourced facts)."),
    ("Appendix G - Sources", "Appendix G: S1-S13 with links."),
    ("Work Area", "Blank. A standings skeleton for D1 and four empty 7 x 7 grids for D3 and D4. Yellow cells are for your own entries."),
    ("", ""),
    ("Note", "This workbook gives you the DATA, not the ANSWER. Points, goal difference, goals scored, who advances, whether a cell is safe, "
             "the counts, the percents, the ceiling and the average are all your own work (Challenge 3, D1-D6). No formula and no "
             "computed result is stored anywhere in this file."),
]
r = 2
for a, b in rows:
    ws.cell(row=r, column=1, value=a).font = Font(name="Arial", bold=True, size=10)
    c = ws.cell(row=r, column=2, value=b)
    c.font = Font(name="Arial", size=10)
    c.alignment = Alignment(wrap_text=True, vertical="top")
    r += 1
widths(ws, [32, 100])

# ---------------- Rules ----------------
ws = wb.create_sheet("Appendix A and C - Rules")
ws.append(["Rule", "1982 ladder (Appendix A) = Option A", "Option B (Appendix C)", "Source"])
ws.append(["Points", "2 for a win, 1 for a draw, 0 for a loss", "2 for a win, 1 for a draw, 0 for a loss", "S1, S9"])
ws.append(["Tie-break 1", "Points in all of the group's matches", "Points in all of the group's matches", "S9"])
ws.append(["Tie-break 2", "Goal difference (goals scored minus goals scored against; can be negative)", "Goals scored in all group matches", "S9; Appendix C"])
ws.append(["Tie-break 3", "Goals scored in all group matches", "Goal difference", "S9; Appendix C"])
ws.append(["Tie-break 4", "Drawing of lots", "Drawing of lots", "S9; Appendix C"])
ws.append(["Last two group matches", "kick off at the same moment", "kick off at the same moment", "Appendix C"])
ws.append([])
ws.append(["Definitions (Appendix C)", "", "", ""])
ws.append(["safe", "West Germany and Austria are the top two teams and the ladder fully separates second place from third", "", ""])
ws.append(["unresolved", "second and third still tied after the last test before the lot (never counted as safe)", "", ""])
ws.append(["not safe", "every other cell", "", ""])
ws.append(["Window", "every match score is 0-6 goals per side; 7 x 7 grid cells; cells are a counting device, not probabilities", "", ""])
header(ws, 1, 4)
body(ws, 2, 7, 1, 4)
ws.cell(row=9, column=1).font = Font(name="Arial", bold=True, size=10, color=NAVY)
body(ws, 10, 13, 1, 2)
widths(ws, [26, 60, 44, 18])

# ---------------- Appendix B ----------------
ws = wb.create_sheet("Appendix B - Group 2 Matches")
ws.append(["#", "Date", "Home", "Away", "Home goals", "Away goals", "Score as printed", "Source"])
brows, _ = table_rows(r"## Appendix B")
for n, date, home, away, score, src in brows:
    hg, ag = (int(x) for x in score.split("-"))
    ws.append([int(n), date, home, away, hg, ag, score, src])
header(ws, 1, 8)
body(ws, 2, 1 + len(brows), 1, 8)
for rr in range(2, 2 + len(brows)):
    for cc in (1, 5, 6):
        ws.cell(row=rr, column=cc).alignment = Alignment(horizontal="center")
ws.append([])
ws.append(["Matches 5 and 6 were the last two of the group, played on consecutive days. Match 6 was played at El Molinon, Gijon [S3]. 'Home' and 'Away' are listing labels only; they do not affect any rule."])
ws.cell(row=ws.max_row, column=1).font = Font(name="Arial", italic=True, size=9)
widths(ws, [5, 16, 16, 16, 12, 12, 18, 12])

# ---------------- Appendix D ----------------
ws = wb.create_sheet("Appendix D - 1982 Groups")
ws.append(["Group", "Team", "W", "D", "L", "GF", "GA", "Advanced?", "Source",
           "Points (yours)", "Goal difference (yours)", "1982 ladder: finish (yours)", "Option B ladder: finish (yours)"])
drows, _ = table_rows(r"## Appendix D")
src_for = {"1": "S4 (S1)", "2": "S2 (S1)", "3": "S5 (S1)", "4": "S6 (S1)", "5": "S7 (S1)", "6": "S8 (S1)"}
for g, team, w, d, l, gf, ga, adv in drows:
    ws.append([int(g), team, int(w), int(d), int(l), int(gf), int(ga), adv, src_for[g]])
n = len(drows)
header(ws, 1, 13)
body(ws, 2, 1 + n, 1, 9, center=True)
for rr in range(2, 2 + n):
    ws.cell(row=rr, column=2).alignment = Alignment(horizontal="left")
work(ws, 2, 1 + n, 10, 13)
for c in (10, 11, 12, 13):
    ws.cell(row=1, column=c).fill = PatternFill("solid", fgColor="8A6D00")
ws.append([])
ws.append(["Columns J-M (yellow, headed 'yours') are blank on purpose: Appendix D lists wins, draws, losses, goals for and goals against only. "
           "Points, goal difference and the rankings are for you to compute (D1, D5)."])
ws.cell(row=ws.max_row, column=1).font = Font(name="Arial", italic=True, size=9)
ws.append(["Data note: RSSSF lists Peru's goals against as 5 where the group page used here lists 6 [S1] [S4]; Peru finished last either way."])
ws.cell(row=ws.max_row, column=1).font = Font(name="Arial", italic=True, size=9)
widths(ws, [7, 18, 5, 5, 5, 6, 6, 11, 10, 12, 14, 16, 16])
ws.freeze_panes = "C2"

# ---------------- Appendix F ----------------
ws = wb.create_sheet("Appendix F - Assumptions")
ws.append(["#", "Assumption", "Value used", "Basis", "Sensitivity"])
frows, _ = table_rows(r"## Appendix F")
for row in frows:
    ws.append(row)
header(ws, 1, 5)
body(ws, 2, 1 + len(frows), 1, 5)
ws.append([])
ws.append(["These are NOT sourced facts. They are stated choices by the case author; a Hero may challenge any of them in discussion."])
ws.cell(row=ws.max_row, column=1).font = Font(name="Arial", italic=True, size=9)
widths(ws, [6, 44, 20, 60, 34])

# ---------------- Appendix G ----------------
ws = wb.create_sheet("Appendix G - Sources")
ws.append(["#", "Claim", "Source", "URL", "Date", "Confidence"])
grows, _ = table_rows(r"## Appendix G")
for sid, claim, src, date, conf in grows:
    m = re.match(r"\[(.*?)\]\((.*?)\)(.*)", src)
    ws.append([sid, claim, m.group(1) + m.group(3), m.group(2), date, conf])
header(ws, 1, 6)
body(ws, 2, 1 + len(grows), 1, 6)
widths(ws, [6, 52, 40, 60, 18, 28])

# ---------------- Work Area ----------------
ws = wb.create_sheet("Work Area")
ws["A1"] = "Work Area - your own calculations (nothing pre-filled)"
ws["A1"].font = Font(name="Arial", bold=True, size=12, color=NAVY)
ws["A3"] = "D1 - Group 2 standings. Block 1: before West Germany-Austria (matches 1-5). Block 2: after the as-played result."
ws["A3"].font = Font(name="Arial", bold=True, size=10)
r = 4
for block in ("Block 1: before West Germany-Austria", "Block 2: after West Germany-Austria as played"):
    ws.cell(row=r, column=1, value=block).font = Font(name="Arial", italic=True, size=10)
    r += 1
    for j, h in enumerate(["Team", "Matches played", "Points", "GF", "GA", "Goal difference (show the subtraction)", "Rank (1982 ladder)"], start=1):
        ws.cell(row=r, column=j, value=h)
    header(ws, r, 7)
    for t in ("", "", "", ""):
        r += 1
    work(ws, r - 3, r, 1, 7)
    r += 2

grid_labels = [("Option A ladder", "West Germany 1-0 Austria"), ("Option A ladder", "West Germany 6-5 Austria"),
               ("Option B ladder", "West Germany 1-0 Austria"), ("Option B ladder", "West Germany 6-5 Austria")]
ws.cell(row=r, column=1, value="D3 / D4 - Algeria-Chile grids. Write S (safe), N (not safe) or U (unresolved) in each cell. Rows: Algeria goals. Columns: Chile goals.").font = Font(name="Arial", bold=True, size=10)
r += 2
for lad, sl in grid_labels:
    ws.cell(row=r, column=1, value="%s | %s" % (lad, sl)).font = Font(name="Arial", bold=True, size=10, color=NAVY)
    r += 1
    ws.cell(row=r, column=1, value="Algeria \\ Chile")
    for c in range(7):
        ws.cell(row=r, column=2 + c, value=c)
    header(ws, r, 8)
    for a in range(7):
        r += 1
        ws.cell(row=r, column=1, value=a)
        ws.cell(row=r, column=1).font = Font(name="Arial", bold=True, size=10)
        ws.cell(row=r, column=1).fill = PatternFill("solid", fgColor="E8EEF5")
        ws.cell(row=r, column=1).alignment = Alignment(horizontal="center")
        ws.cell(row=r, column=1).border = BOX
    work(ws, r - 6, r, 2, 8)
    r += 1
    ws.cell(row=r, column=1, value="Safe cells (count) =").font = Font(name="Arial", size=10)
    work(ws, r, r, 2, 2)
    ws.cell(row=r, column=4, value="as a percent of all the cells =").font = Font(name="Arial", size=10)
    work(ws, r, r, 6, 6)
    r += 3
widths(ws, [30, 16, 10, 10, 10, 34, 18, 10])

wb.save(OUT)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
