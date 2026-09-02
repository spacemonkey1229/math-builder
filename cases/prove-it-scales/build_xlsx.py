#!/usr/bin/env python3
"""Build the Data workbook for Prove It Scales. Raw appendix data only --
never pre-computes D1-D5; students do that work in the D4 work area."""
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
ws["A1"] = "Prove It Scales — Data Workbook"
style_title(ws, "A1")
ws["A2"] = "MS | Math | Case Study | 2026-27 | Adventure"
style_sub(ws, "A2")
ws["A5"] = "What this is"
ws["B5"] = ("Raw appendix data from the Prove It Scales case study, laid out for you to compute "
            "over. Nothing here has been pre-solved -- the sheets give you the sourced figures "
            "the case cites; D1 through D5 (the induction proof, the recursion trace, the "
            "per-call cost interpretation, the runtime comparison table, and the recommendation "
            "memo) are your own work to do.")
ws["A6"] = "Case"
ws["B6"] = ("cases/prove-it-scales/case.md — see the case study docx for the full Overview, "
            "Background, Dilemma, and Challenges.")
ws["A8"] = "Sheet"
ws["B8"] = "Maps to"
ws["A9"] = "Appendix A — Pipeline Constraints"
ws["B9"] = "Appendix A: Meterworks' release timeline, hierarchy depth, throughput, latency SLA, and target runtime. Sources: MA1, S5, S6, MA2, MA7."
ws["A10"] = "Appendix B — Option A Spec"
ws["B10"] = "Appendix B: the recursive RollUpCharges implementation -- code length, base case, inductive step, and whether the target runtime honors tail-call optimization. Sources: MA3, S4."
ws["A11"] = "Appendix C — Option B Spec"
ws["B11"] = "Appendix C: the iterative RollUpCharges implementation -- code length, approach, and correctness argument on file. Source: MA4."
ws["A12"] = "Appendix D — Measured Runtime"
ws["B12"] = "Appendix D: milliseconds per 10,000 billing rollups, iterative vs. recursive (TCO-honored and TCO-not-honored), at three account-hierarchy depths. Sources: S1, S2, S7, S8, MA5, MA6."
ws["A13"] = "Appendix E — Documented Precedent"
ws["B13"] = "Appendix E: the real RavenDB/Ayende production postmortem and the extreme-case Go recursion benchmark. Sources: S3, S2."
ws["A14"] = "D1-D5 Work Area"
ws["B14"] = ("A blank area for your own induction proof, recursion trace notes, per-call cost "
             "interpretation, six-cell runtime comparison table (with an inductive-step-invocation "
             "count column), and recommendation memo. This is the assignment -- it is "
             "intentionally empty.")
for r in (5, 6, 8, 9, 10, 11, 12, 13, 14):
    ws[f"A{r}"].font = Font(name=ARIAL, bold=(r == 8))
    ws[f"B{r}"].font = Font(name=ARIAL)
    ws[f"B{r}"].alignment = Alignment(wrap_text=True, vertical="top")
col_widths(ws, [30, 100])
ws.row_dimensions[5].height = 55
ws.row_dimensions[6].height = 30
for r in (9, 10, 11, 12, 13):
    ws.row_dimensions[r].height = 30
ws.row_dimensions[14].height = 60

# ---------- Appendix A ----------
ws = wb.create_sheet("Appendix A — Pipeline")
rows = [
    ("Quantity", "Value"),
    ("Days from case launch to the release freeze", "3 days (MA1)"),
    ("Maximum account-hierarchy nesting depth observed among current Meterworks customers",
     "5 levels [S5]"),
    ("Billing rollup calls processed per night across all customer accounts",
     "Billions of usage events processed per day, sustained (real usage-billing-platform proxy figure) [S6]"),
    ("Maximum allowed runtime per batch of 10,000 rollups (latency SLA)", "500 ms (MA2)"),
    ("Target language/runtime for the next billing engine release", "Go (MA7)"),
]
for r in rows:
    ws.append(r)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [55, 55])
for r in range(2, ws.max_row + 1):
    ws.cell(row=r, column=2).alignment = Alignment(wrap_text=True, vertical="top")
ws.append([])
ws.append(["Source: MA1/MA2/MA7 are stated modeling assumptions (case.md Modeling Assumptions "
           "block); S5/S6 are sourced figures -- see case.json sources[] for full citations.", None])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)

# ---------- Appendix B ----------
ws = wb.create_sheet("Appendix B — Option A Spec")
ws.append(["Spec", "Value"])
b_rows = [
    ("Lines of code, recursive implementation", "16 lines (MA3)"),
    ("Base case", "An account with zero child accounts; its total is the sum of its own raw usage events."),
    ("Inductive step", "An account's total equals its own raw usage events plus the sum of its children's already-computed totals."),
    ("Does the target runtime named in Appendix A guarantee or reliably apply tail-call optimization to this function?",
     "No. Go's own compiler team has repeatedly and publicly declined to add general tail-call "
     "optimization to the language, citing the need to keep runtime.Callers and stack backtraces "
     "predictable [S4]."),
]
for r in b_rows:
    ws.append(r)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [40, 75])
for r in range(2, ws.max_row + 1):
    ws.cell(row=r, column=2).alignment = Alignment(wrap_text=True, vertical="top")
ws.append([])
ws.append(["Source: MA3 is a stated modeling assumption (illustrative code length). [S4] golang/go "
           "issue #22624 -- see case.json sources[] for the full citation.", None])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)

# ---------- Appendix C ----------
ws = wb.create_sheet("Appendix C — Option B Spec")
ws.append(["Spec", "Value"])
c_rows = [
    ("Lines of code, iterative implementation", "34 lines (MA4)"),
    ("Implementation approach",
     "Explicit loop over a flattened, depth-ordered list of accounts (children processed before "
     "parents), with an explicit stack replacing the call stack."),
    ("Correctness argument on file",
     "A walkthrough of representative test hierarchies up to a stated depth; no induction proof."),
    ("Does this version's runtime depend on the target runtime's tail-call behavior?",
     "No -- per-call cost is fixed and does not depend on tail-call optimization."),
]
for r in c_rows:
    ws.append(r)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [40, 75])
for r in range(2, ws.max_row + 1):
    ws.cell(row=r, column=2).alignment = Alignment(wrap_text=True, vertical="top")
ws.append([])
ws.append(["Source: MA4 is a stated modeling assumption (illustrative code length).", None])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)

# ---------- Appendix D ----------
ws = wb.create_sheet("Appendix D — Measured Runtime")
ws.append(["Account-hierarchy depth", "Iterative (ms / 10,000 rollups)",
           "Recursive, TCO honored (ms / 10,000 rollups)", "Recursive, TCO not honored (ms / 10,000 rollups)"])
d_rows = [
    ("Shallow", 0.164, 0.333, 3.94),
    ("Medium", 0.259, 0.343, 3508),
    ("Deep", 0.354, 0.354, 3122383),
]
for r in d_rows:
    ws.append(r)
style_header_row(ws, 1, 4)
set_body_font(ws)
col_widths(ws, [26, 30, 34, 34])
ws.append([])
ws.append(["Shallow and Deep are directly measured [S1, S2]; Medium is interpolated between them "
           "-- see Modeling Assumption MA5. The Deep-row Iterative figure is not an independent "
           "measurement -- see MA6 [S7].", None, None, None])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)
ws.append(["Figures in this appendix are scaled from published language-runtime benchmarks of a "
           "canonical recursive function's (Fibonacci's) iterative, tail-recursive, and "
           "non-tail-recursive implementations, not from Meterworks' own (fictional) production "
           "telemetry. Sources: [S1] Felipe Dutra Tine e Silva, Medium, 2017-01-25; [S2] pope/"
           "go_recursive_benchmark, GitHub, 2022-12-31; [S7]/[S8] derived figures -- see case.json "
           "sources[] for full citations.", None, None, None])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)
ws.append(["Unit conversion used throughout: ms per 10,000 rollups = ns/op x 10,000 / 1,000,000 = "
           "ns/op x 0.01.", None, None, None])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)

# ---------- Appendix E ----------
ws = wb.create_sheet("Appendix E — Precedent")
ws.append(["Item", "Value"])
e_rows = [
    ("A publicly documented production postmortem describing a recursive map-reduce billing/"
     "aggregation bug and the divergent totals it produced",
     "Oren Eini (Ayende Rahien), founder of RavenDB -- \"Production postmortem: Your math is "
     "wrong, recursion doesn't work this way\" (2022-07-13). A multi-map-reduce billing-"
     "aggregation index silently violated its own assumption once an already-reduced "
     "intermediate result was fed back into the same reduce function on a different cluster "
     "node, producing two different totals for the same account: -67,343 and +67,329 [S3]."),
    ("A published benchmark showing the extreme end of the non-tail-callable recursion cost gap",
     "pope/go_recursive_benchmark (GitHub) -- a naive, non-tail-callable recursive Fibonacci(40) "
     "runs at 312,238,250 ns/op; the same function restructured to be tail-callable runs at "
     "35.36 ns/op -- roughly an 8.8-million-times gap [S2]."),
]
for r in e_rows:
    ws.append(r)
style_header_row(ws, 1, 2)
set_body_font(ws)
col_widths(ws, [45, 90])
for r in range(2, ws.max_row + 1):
    ws.cell(row=r, column=2).alignment = Alignment(wrap_text=True, vertical="top")
ws.append([])
ws.append(["This appendix documents a real, external precedent of the same failure shape "
           "described in Background -- an already-aggregated intermediate result recursively "
           "re-fed into the same reduce function, violating an assumption that held only at the "
           "top level. It is cited as industry precedent, not as an incident at Meterworks "
           "itself. Sources: [S3] ayende.com, 2022-07-13; [S2] see Appendix D above.", None])
ws.cell(row=ws.max_row, column=1).font = Font(name=ARIAL, italic=True, size=10)

# ---------- D1-D5 Work Area ----------
ws = wb.create_sheet("D1-D5 Work Area")
ws["A1"] = "Work Area — D1 through D5"
style_title(ws, "A1", size=13)
ws["A2"] = ("This sheet is intentionally blank except for column headers. Pull your raw inputs "
            "from the Appendix A/B/C/D/E sheets -- do not retype values by hand where you can "
            "reference the cell.")
ws["A2"].font = Font(name=ARIAL, italic=True)
ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells("A2:E2")
ws.row_dimensions[2].height = 40

sections = [
    (4, "D1 — Induction proof",
     ["Base case (state it)", "Inductive step (state it)", "Closing argument connecting the two", "Work shown"]),
    (9, "D2 — Labeled recursion trace",
     ["Sample hierarchy (describe / sketch reference)", "Base-case call(s) marked", "Inductive-step call(s) marked", "Notes"]),
    (14, "D3 — Per-call cost interpretation",
     ["Inductive step from D1", "Why one combine per hierarchy level", "How this interprets Appendix D's figures"]),
    (19, "D4 — Runtime comparison table",
     ["Depth", "Iterative (ms/10,000)", "Recursive TCO-honored (ms/10,000)", "Recursive TCO-not-honored (ms/10,000)", "# inductive-step invocations"]),
    (25, "D5 — Recommendation memo",
     ["Recommendation", "Defended with D1 (proof status)", "Defended with D4 (numbers)", "Defended with Appendix A (target-runtime fact)"]),
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

wb.save("cases/prove-it-scales/published/Prove It Scales - Data.xlsx")
print("wrote Prove It Scales - Data.xlsx")
