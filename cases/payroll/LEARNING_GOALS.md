# Learning Goals — Payroll

Bidirectional deliverable ↔ skill matrix (case-write §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — bar graph of each employee's remaining pay | `number-sense-bar-graph`, `number-sense-data` |
| D2 — pie chart of each employee's percent share of remaining payroll | `statistics-and-probability-pie-chart`, `statistics-and-probability-how-to-create-a-pie-chart-given-a-set-of-data`, `advanced-numbers-percent`, `advanced-numbers-how-to-convert-numbers-to-percents` |
| D3 — Option A: dollar amount removed vs. $20,000 target, in dollars and percent | `basic-operations-how-to-subtract-multi-digit-numbers`, `advanced-numbers-how-to-convert-numbers-to-percents`, `measurement-currency` |
| D4 — Option B: flat percent cut that removes exactly $20,000, per employee | `advanced-numbers-how-to-convert-numbers-to-percents`, `advanced-numbers-how-to-find-the-percent-of-a-number`, `basic-operations-how-to-add-multi-digit-numbers`, `measurement-rounding`, `measurement-how-to-round-a-number-to-a-specified-place-value` |
| D5 — comparison table, chosen option vs. other | `number-sense-how-to-compare-two-or-more-values` |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 13    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each mapping** ("could a competent student produce this deliverable
correctly without ever performing this skill?"):

- D1 cannot be produced without reading Appendix C's five dollar figures as a data set and
  rendering them as a bar graph — a student who skips this either has no chart or a chart that
  isn't a bar graph.
- D2 cannot be produced without converting each employee's remaining pay into a percent share of
  the $111,500 pool and rendering it as a pie chart — the pie-chart wedges only make sense as
  percents of a whole.
- D3 requires subtracting the chosen employee's exact remaining pay from $20,000 (or vice versa)
  and re-expressing that difference as a percent of $20,000 — a student who never subtracts or
  never converts to percent cannot state "over/under/exact by how much."
- D4 requires finding what percent of $111,500 equals $20,000, then applying that percent to each
  of five different base amounts, then rounding each result to the nearest cent — skipping the
  percent-of-a-number step or the rounding step produces wrong per-employee figures that will not
  sum back to $20,000.
- D5 explicitly asks for a comparison table weighing the two options — this is the
  compare-two-or-more-values skill by definition, not a decorative label.

## Why `new_coverage` is empty (legacy conversion)

All 13 claimed skills already have `n > 0` in `readmodel/standards_spine.json` — this legacy case's
own arithmetic (percent, subtraction/addition of multi-digit dollar amounts, bar/pie charts,
rounding, comparison) sits squarely in numeracy vocabulary that dozens of other cases in the corpus
already exercise. A deliberate search of every `n == 0` skill in the spine (137 candidates) turned
up nothing this case's real math genuinely forces — the zero-coverage skills are concentrated in
geometry (volume of a cone/sphere/pyramid), pre-calculus, and calculus, none of which this T2
payroll-arithmetic case has any honest reason to touch. Per the task's own instruction, this is
reported plainly rather than padded: `new_coverage[] = []` is the correct, honest answer for this
conversion, not a defect to paper over.
