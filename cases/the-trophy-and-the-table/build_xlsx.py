#!/usr/bin/env python3
"""Data workbook for 'The Trophy and the Table'. DATA ONLY: the official table (Appendix B) and the
ten-season persistence table exactly as published in Appendix E, plus citations and a BLANK work area.
No regression, residual, break-even or answer is computed or pre-filled. No Football-Data file is bundled."""
import os, re
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
md = open(f"{HERE}/case.md", encoding="utf-8").read()
NAVY = "1A3A5C"
wb = openpyxl.Workbook()

def hdr(ws, row, n):
    for c in range(1, n + 1):
        x = ws.cell(row=row, column=c)
        x.font = Font(name="Arial", bold=True, color="FFFFFF", size=10)
        x.fill = PatternFill("solid", fgColor=NAVY)
        x.alignment = Alignment(wrap_text=True, vertical="center")

def body(ws, r0, r1, n):
    for r in range(r0, r1 + 1):
        for c in range(1, n + 1):
            x = ws.cell(row=r, column=c)
            x.font = Font(name="Arial", size=10)
            x.alignment = Alignment(wrap_text=True, vertical="top")

def widths(ws, ws_):
    for i, w in enumerate(ws_, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

def note(ws, row, text, ncols=8):
    ws.cell(row=row, column=1, value=text).font = Font(name="Arial", italic=True, size=9)
    ws.cell(row=row, column=1).alignment = Alignment(wrap_text=True, vertical="top")
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=ncols)
    ws.row_dimensions[row].height = 42

def tables(text):
    out, lines, i = [], text.split("\n"), 0
    while i < len(lines):
        if lines[i].strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?[\s:|-]+\|?\s*$", lines[i + 1]):
            hd = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            j, rows = i + 2, []
            while j < len(lines) and lines[j].strip().startswith("|"):
                rows.append([c.strip() for c in lines[j].strip().strip("|").split("|")]); j += 1
            out.append((hd, rows)); i = j
        else:
            i += 1
    return out

def num(v):
    v = v.replace("−", "-").replace("+", "").replace("**", "").strip()
    return int(v) if re.fullmatch(r"-?\d+", v) else v

def section(letter):
    m = re.search(rf"(?s)## Appendix {letter} .*?(?=\n## Appendix |\Z)", md)
    return m.group(0)

# ---- README
ws = wb.active; ws.title = "README"
ws["A1"] = "The Trophy and the Table — Data Workbook"; ws["A1"].font = Font(name="Arial", bold=True, size=14, color=NAVY)
rows = [
    ("", ""),
    ("Case", "The Trophy and the Table (MS | Math | Case Study | 2026-27)"),
    ("Purpose", "Raw, cited data for the board's Keep the Winner vs Change After 17th decision. You compute over it; nothing here is worked for you."),
    ("", ""),
    ("Sheet", "Maps to"),
    ("Appendix B - League Table", "case study Appendix B: the final 2024/25 Premier League table, all 20 clubs [S1]"),
    ("Appendix E - Persistence", "case study Appendix E: the ten-season persistence data exactly as published there (season pairs and slopes), derived by the case author from [S14]-[S23]"),
    ("Sources", "case study Appendix G: where each table comes from; links to the ten Wikipedia season pages"),
    ("Work Area", "Blank. Your own D1-D4 working goes here."),
    ("", ""),
    ("Source of the data", "Wikipedia (text available under CC BY-SA): the final 2024-25 Premier League table [S1] and the ten season pages [S14]-[S23]. Cite Wikipedia and the season page when you use it."),
    ("Link-only data", "Football-Data.co.uk is listed in the case study (Appendix C) as a LINK ONLY. This workbook contains no Football-Data file or figure. Its terms allow private individuals to download files for their own use only (no commercial, bot, scraper or AI-training use): read them and download anything you want yourself. https://www.football-data.co.uk/data.php"),
    ("Tip", "Goal difference (GD) and the slope column are stored as text exactly as printed in the case study. GD = GF - GA, so you can rebuild a numeric GD column in your Work Area (or convert the text to numbers) before you plot or fit anything."),
    ("Note", "This workbook gives you the DATA, not the ANSWER. The line of best fit, the residuals, the residual spread, the outlier check and the break-even reset cost are your own work, shown in your submission appendix."),
]
r = 2
for a, b in rows:
    ws.cell(row=r, column=1, value=a).font = Font(name="Arial", bold=True, size=10)
    ws.cell(row=r, column=2, value=b).font = Font(name="Arial", size=10)
    ws.cell(row=r, column=2).alignment = Alignment(wrap_text=True, vertical="top"); r += 1
widths(ws, [28, 100])

# ---- Appendix B
ws = wb.create_sheet("Appendix B - League Table")
hd, rows = tables(section("B"))[0]
ws.append([h for h in hd])
for rw in rows:
    # GD (column 8) is kept as TEXT exactly as printed (e.g. "-2", "+45"): the packet continuity check cannot
    # match negative numeric cells to case.md's unsigned numerals. GD = GF - GA, so students can rebuild a numeric column.
    ws.append([(rw[7].replace("\u2212", "-") if i == 7 else num(x)) for i, x in enumerate(rw)])
hdr(ws, 1, len(hd)); body(ws, 2, len(rows) + 1, len(hd)); widths(ws, [6, 28, 6, 6, 6, 6, 6, 7, 6])
ws.freeze_panes = "A2"
note(ws, len(rows) + 3, "Source: [S1] Wikipedia, 2024–25 Premier League (transcription of the official final table), accessed 2026-10-03. W, D, L = wins, draws, losses; GF, GA = goals for, goals against; GD = goal difference (GF − GA); Pts = league points. No club had points deducted. Values are exactly as published; nothing is derived or computed here.", 9)

# ---- Appendix E
ws = wb.create_sheet("Appendix E - Persistence")
hd, rows = tables(section("E"))[0]
ws.append(["Season pair", "Club-pairs", "Slope: next season's miss per point of this season's miss"])
for rw in rows:
    ws.append([rw[0].replace("**", ""), num(rw[1]), rw[2].replace("\u2212", "-").replace("**", "")])  # slope kept as text as printed (see README Tip)
hdr(ws, 1, 3); body(ws, 2, len(rows) + 1, 3); widths(ws, [30, 14, 52])
for r in range(2, len(rows) + 2):
    ws.cell(row=r, column=3).alignment = Alignment(horizontal="right", vertical="top")
note(ws, len(rows) + 3, "Source: DERIVED by the case author (not published by any source) from the ten Wikipedia season tables [S14]-[S23], as reported in case study Appendix E: for each pair of consecutive seasons, the slope of next season's residual on this season's residual over the clubs present in both (17 per pair, 153 pooled). Points are from results (3 per win, 1 per draw), so the 2023/24 points deductions are left out. Each season has only 20 clubs, so every slope is noisy. The per-club season tables are on the linked Wikipedia pages (see the Sources sheet) if you want to check one season pair yourself.", 3)

# ---- Sources
ws = wb.create_sheet("Sources")
ws.append(["#", "What it supports", "Source", "Link", "Date accessed", "Use in this packet"])
src = [
    ("S1", "Final 2024/25 Premier League table (Appendix B)", "Wikipedia — 2024–25 Premier League", "https://en.wikipedia.org/wiki/2024%E2%80%9325_Premier_League", "2026-10-03", "Data in this workbook (CC BY-SA)"),
]
for k, yr in zip(range(14, 24), ["2015–16", "2016–17", "2017–18", "2018–19", "2019–20", "2020–21", "2021–22", "2022–23", "2023–24", "2024–25"]):
    a, b = yr.split("–")
    src.append((f"S{k}", f"Final {yr} table, used by the case author to derive Appendix E", f"Wikipedia — {yr} Premier League",
                f"https://en.wikipedia.org/wiki/{a}%E2%80%93{b}_Premier_League", "2026-10-03", "Link only here; Appendix E slopes derived from it (CC BY-SA)"))
src.append(("S5", "Football-Data.co.uk free match data and its terms (private individuals only; no commercial, bot, scraper or AI-training use)", "Football-Data.co.uk — Data page", "https://www.football-data.co.uk/data.php", "2026-10-03", "LINK ONLY. No Football-Data file or figure is included in this workbook or packet."))
for s in src: ws.append(list(s))
hdr(ws, 1, 6); body(ws, 2, len(src) + 1, 6); widths(ws, [6, 52, 36, 62, 14, 52])

# ---- Work Area (blank)
ws = wb.create_sheet("Work Area")
ws["A1"] = "Your work area — blank. Nothing in this sheet is pre-filled or pre-computed."
ws["A1"].font = Font(name="Arial", bold=True, size=11, color=NAVY)
ws["A3"] = "Use it however you like: paste the Appendix B columns you need, add your own columns, charts and formulas."
ws["A3"].font = Font(name="Arial", italic=True, size=10)
widths(ws, [30] * 8)

out = f"{HERE}/published/The Trophy and the Table - Data.xlsx"
wb.save(out); print("wrote", out, os.path.getsize(out))
