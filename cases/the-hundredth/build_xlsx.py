#!/usr/bin/env python3
"""Data workbook for The Hundredth: raw appendix values + empty work areas. No answers, no formulas."""
import os, re, json
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
NAVY = "1A3A5C"
wb = openpyxl.Workbook()
F = lambda **k: Font(name="Arial", size=k.pop("size", 10), **k)
WORK = PatternFill("solid", fgColor="FFF8E1")

def header(ws, row, n):
    for c in range(1, n + 1):
        x = ws.cell(row=row, column=c)
        x.font = Font(name="Arial", bold=True, color="FFFFFF", size=11)
        x.fill = PatternFill("solid", fgColor=NAVY)
        x.alignment = Alignment(vertical="center", wrap_text=True)

def body(ws, r0, r1, n, work_cols=()):
    for r in range(r0, r1 + 1):
        for c in range(1, n + 1):
            x = ws.cell(row=r, column=c)
            x.font = F()
            x.alignment = Alignment(wrap_text=True, vertical="top")
            if c in work_cols:
                x.fill = WORK

def widths(ws, ws_w):
    for i, w in enumerate(ws_w, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

def note(ws, text):
    ws.append([])
    ws.append([text])
    ws.cell(row=ws.max_row, column=1).font = F(italic=True, size=9)

# README
ws = wb.active; ws.title = "README"
ws["A1"] = "The Hundredth - Data Workbook"; ws["A1"].font = F(bold=True, size=14, color=NAVY)
rows = [
    ("", ""),
    ("Case", "The Hundredth (cases/the-hundredth)"),
    ("Purpose", "The cited race figures, the example frame rates, the differential-lag grid and the modeling assumptions the Chief Judge works from, with blank work areas for your own calculations."),
    ("", ""),
    ("Sheet", "Maps to"),
    ("Appendix C - Race Figures", "case.md Appendix C figures table [S1]"),
    ("Appendix D - Frame Rates", "case.md Appendix D (scenario inputs; see MA2). Blank columns for D2."),
    ("Appendix E - Lag Grid", "case.md Appendix E. The grid of lag values and the scenario values for D5. Blank columns for D4."),
    ("Appendix F - Assumptions", "case.md Appendix F (MA1-MA5): stated scenario assumptions, NOT sourced data"),
    ("Appendix G - Sources", "case.md Appendix G (S1-S8, full citations)"),
    ("Work Area", "Blank. For your own D1, D3 and D5 calculations. Nothing here is pre-computed."),
    ("", ""),
    ("Note", "This workbook gives you the DATA, not the ANSWER. Speed and distance (D1), frame periods and travel (D2), the range hiding in the reported times (D3), the first-contact margins (D4) and the reliability probabilities and percent difference (D5) are your own work. Shaded cells are for you to fill. The Appendix F values are scenario assumptions chosen by the case author; challenging them is a legitimate move."),
]
for i, (a, b) in enumerate(rows, start=2):
    ws.cell(row=i, column=1, value=a).font = F(bold=True)
    c = ws.cell(row=i, column=2, value=b); c.font = F(); c.alignment = Alignment(wrap_text=True, vertical="top")
widths(ws, [30, 95])

# Appendix C
ws = wb.create_sheet("Appendix C - Race Figures")
ws.append(["Figure", "Value", "Units", "Source"])
for r in [["Race distance", 100, "m", "S1"], ["Reported winning time (Phelps)", 50.58, "s", "S1"],
          ["Reported second-place time (Cavic)", 50.59, "s", "S1"], ["Reported third-place time", 51.12, "s", "S1"]]:
    ws.append(r)
header(ws, 1, 4); body(ws, 2, 5, 4); widths(ws, [38, 12, 8, 10])
note(ws, "Source S1: Olympedia, Men's 100 metres Butterfly, 2008, https://www.olympedia.org/results/261586 (accessed 2026-10-03). The third digit of each time is not recorded or used (Appendix B, SW 11.2).")

# Appendix D
ws = wb.create_sheet("Appendix D - Frame Rates")
ws.append(["Footage type", "Frames per second", "Time between frames (s)  [D2: yours]", "Hand travel per frame (cm)  [D2: yours]", "Separates a 0.01 s difference?  [D2: yours]"])
for r in [["Ordinary television", 30], ["Faster television / phone slow-motion", 60], ["High-speed camera", 240], ["Very high-speed camera", 1000]]:
    ws.append(r + [None, None, None])
header(ws, 1, 5); body(ws, 2, 5, 5, work_cols=(3, 4, 5)); widths(ws, [38, 18, 24, 24, 26])
note(ws, "Scenario inputs (Appendix F, MA2), not sourced. The frame rate of the footage actually reviewed in 2008 was not found. Use your D1 speed for the travel column.")

# Appendix E
ws = wb.create_sheet("Appendix E - Lag Grid")
ws.append(["Delta (s) = lag of Cavic - lag of Phelps", "c (s) = Delta - d, with d = 0.01 s  [D4: yours]", "Who touched first?  [D4: yours]"])
for d in [-0.010, 0.000, 0.005, 0.010, 0.015, 0.020, 0.030]:
    ws.append([d, None, None])
header(ws, 1, 3); body(ws, 2, 8, 3, work_cols=(2, 3))
for r in range(2, 9): ws.cell(row=r, column=1).number_format = "0.000"
widths(ws, [34, 40, 30])
ws.append([]); ws.append(["Scenario values for D5 (declared, not measured; Appendix F)", "Value", "Units"])
header(ws, ws.max_row, 3)
r0 = ws.max_row + 1
for r in [["Delta (differential pad lag)", 0.010, "s"], ["J (judge's extra reading band)", 0.005, "s"],
          ["Frame rate", 240, "frames per second"], ["W (half-width of a close finish)", 0.05, "s"]]:
    ws.append(r)
body(ws, r0, ws.max_row, 3)
ws.append([])
ws.append(["Reliability rule: P = 1 - b / (2 x W). Option A: b = |Delta|. Option B: b = (time between frames) + J. Percent difference = (larger P - smaller P) / smaller P x 100."])
ws.cell(row=ws.max_row, column=1).font = F(italic=True, size=9)
ws.append(["D5 work (yours): band A, band B, P_A, P_B, percent difference, with scenario values and then with your own range from D4 - use the Work Area sheet."])
ws.cell(row=ws.max_row, column=1).font = F(italic=True, size=9)

# Appendix F
md = open(os.path.join(HERE, "case.md"), encoding="utf-8").read()
def table_rows(section_title):
    m = re.search(r'(?ms)^## ' + section_title + r'.*?\n(.*?)(?=^---\s*$)', md)
    lines = [l for l in m.group(1).splitlines() if l.strip().startswith("|")]
    cells = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines]
    return cells[0], cells[2:]
strip = lambda t: re.sub(r'\*\*|\[([^\]]+)\]\(([^)]+)\)', lambda m: (m.group(1) + " <" + m.group(2) + ">") if m.group(1) else "", t)
ws = wb.create_sheet("Appendix F - Assumptions")
h, rows = table_rows("Appendix F")
ws.append(h)
for r in rows: ws.append([strip(c) for c in r])
header(ws, 1, len(h)); body(ws, 2, len(rows) + 1, len(h)); widths(ws, [6, 34, 34, 60, 34])
note(ws, "These figures are NOT sourced. They are stated scenario assumptions chosen by the case author. The lag range is a plausible range, not measured.")

# Appendix G
ws = wb.create_sheet("Appendix G - Sources")
h, rows = table_rows("Appendix G")
ws.append(h)
for r in rows: ws.append([strip(c) for c in r])
header(ws, 1, len(h)); body(ws, 2, len(rows) + 1, len(h)); widths(ws, [6, 40, 18, 70, 18, 12])

# Work Area
ws = wb.create_sheet("Work Area")
ws.append(["Your work (blank; nothing here is pre-computed)", "Your value"])
header(ws, 1, 2)
labels = ["D1: winner's average speed (m/s) =", "D1: distance a hand travels in 0.01 s (cm) =",
          "D3 (i) dropped third digit: smallest pad-time difference (s) =", "D3 (i) dropped third digit: largest pad-time difference (s) =",
          "D3 (ii) rounded: smallest pad-time difference (s) =", "D3 (ii) rounded: largest pad-time difference (s) =",
          "D4: your plausible range for Delta (s) =", "D4: the single Delta above which pad and first contact disagree (s) =",
          "D5: Option A band (s) =", "D5: Option B band (s) =", "D5: P for Option A =", "D5: P for Option B =",
          "D5: percent difference =", "D5: which option wins (scenario values)? =",
          "D5: which option wins (your own D4 range)? ="]
for l in labels: ws.append([l, None])
body(ws, 2, len(labels) + 1, 2, work_cols=(2,)); widths(ws, [66, 24])

out = os.path.join(HERE, "published", "The Hundredth - Data.xlsx")
os.makedirs(os.path.dirname(out), exist_ok=True)
wb.save(out); print("wrote", out)
