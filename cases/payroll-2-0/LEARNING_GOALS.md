# Learning Goals — Payroll 2.0

Bidirectional deliverable ↔ skill matrix (case-write §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — bar graph of each employee's projected remaining 2019 pay | `number-sense-bar-graph` |
| D2 — Option A: which employee, dollar amount removed, why not another | `number-sense-how-to-compare-two-or-more-values`, `basic-operations-subtraction`, `basic-operations-difference` |
| D3 — Option B: flat percent cut that removes exactly $25,000, per employee | `advanced-numbers-percent`, `advanced-numbers-how-to-convert-numbers-to-percents`, `advanced-numbers-how-to-find-the-percent-of-a-number`, `basic-operations-subtraction` |
| D4 — projected end-of-2019 profit table, H1 scaled to a full year | `measurement-ratio`, `measurement-proportion`, `measurement-how-to-find-equivalent-ratios`, `basic-operations-addition`, `basic-operations-subtraction` |
| D5 — 2011-2018 profit trend graph with a drawn linear trend line, extended to project 2020 | `statistics-and-probability-linear`, `statistics-and-probability-slope`, `statistics-and-probability-how-to-identify-the-slope-of-a-line-given-a-set-of-data-or-a-graph-o`, `statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data`, `statistics-and-probability-how-to-draw-a-line-of-a-set-of-data-given-its-linear-equation` |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 16    new_coverage: 1
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each mapping** ("could a competent student produce this deliverable
correctly without ever performing this skill?"):

- **D1** cannot be produced without reading Appendix C's five dollar figures as a data set and
  rendering them as a bar graph — any other chart type, or no chart, fails the deliverable as
  written.
- **D2** requires subtracting the chosen employee's exact remaining pay from $25,000 (or the
  reverse) to state the dollar amount removed, and requires comparing all five employees' figures
  against the $25,000 target to justify "why not someone else" with numbers rather than narrative
  alone — a student who never subtracts, or never compares the five values against the target,
  cannot honestly answer the "why not" half of the deliverable.
- **D3** requires finding what percent of the $112,250 five-employee pool equals $25,000, then
  applying that percent to each of five different base amounts to get each employee's new pay — a
  student who skips the percent-of-a-whole step or the percent-of-a-number step produces
  per-employee figures that will not sum back to $25,000.
- **D4** requires scaling the given first-half revenue and expense actuals to a full year using
  the stated 1:2 half-year-to-full-year ratio (Appendix D, Assumption 3), then adding the chosen
  option's adjusted payroll and subtracting from the scaled revenue and expenses — skipping the
  ratio step produces a profit figure with no defensible basis, and the addition/subtraction steps
  are how "profit = revenue − expenses − payroll" actually gets computed from four separate numbers.
- **D5** explicitly asks for a trend line "you draw from a linear equation you write from that
  data" — a student cannot produce this deliverable by eyeballing a projection; they must identify
  the rate of change (slope) between two years of profit data, write that as a linear equation, and
  then draw the specific line that equation describes, extended past 2018 to 2020. Skipping the
  slope step means there is no defensible line to draw; skipping the draw-from-equation step means
  the graph doesn't actually show what the equation predicts.

## `new_coverage` justification

`statistics-and-probability-how-to-draw-a-line-of-a-set-of-data-given-its-linear-equation` (n=0
in `readmodel/standards_spine.json` at write time, re-checked live immediately before this file
was finalized) is genuinely forced by D5, not padded in: D5 does not stop at writing the linear
equation (that alone would only force `how-to-write-a-linear-equation-given-a-set-of-data`, n=4,
already covered elsewhere) — it explicitly requires the student to then draw the line the equation
describes, extended past the given data to project 2020. That second step is a distinct skill from
deriving the equation itself, and the case's own required deliverable text ("with a trend line you
draw from a linear equation you write") makes it non-optional. The other 15 claimed skills all
already have `n > 0` elsewhere in the spine and are not claimed as `new_coverage`.

Checked adjacent `n == 0` candidates before settling on this one: `statistics-and-probability`'s
own `how-to-identify-the-slope...` and `how-to-write-a-linear-equation-given-a-set-of-data` are
both genuinely forced by D5 too, but both already have `n >= 1`, so neither counts as new
coverage even though both stay in `standards[]`. No other `n == 0` skill in the spine (85
candidates at write time, concentrated in geometry visual-perceptibility terms, pre-calculus,
calculus, and discrete mathematics) has any honest connection to this case's payroll/percent/trend
arithmetic.
