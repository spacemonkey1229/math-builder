# Learning Goals — Movie Executive

Bidirectional deliverable ↔ skill matrix (SPEC §1.5 item 3 / case-write §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — scatter plot + line of best fit for each film | `statistics-and-probability-scatter-plot`, `statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data`, `statistics-and-probability-line-of-best-fit`, `statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data` |
| D2 — correlation classification, coefficient estimate, line-of-best-fit equation | `statistics-and-probability-correlation`, `statistics-and-probability-how-to-identify-correlation-given-a-scatter-plot-or-set-of-data`, `statistics-and-probability-slope`, `statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data` |
| D3 — population/sample/sampling-method table + generalizability judgment | `statistics-and-probability-sample`, `statistics-and-probability-population`, `statistics-and-probability-sample-size`, `statistics-and-probability-random`, `statistics-and-probability-stratified-sampling`, `statistics-and-probability-convenience-sampling`, `number-sense-how-to-compare-two-or-more-values` |
| D4 — definite-buyer (top-2-box) share and mean price, per film | `statistics-and-probability-mean`, `statistics-and-probability-how-to-find-the-mean-of-a-set-of-data`, `advanced-numbers-percent`, `advanced-numbers-how-to-find-the-percent-of-a-number` |
| D5 — projected opening-weekend box office revenue, per film | `advanced-numbers-decimal`, `advanced-numbers-how-to-multiply-decimal-numbers`, `advanced-numbers-how-to-divide-decimal-numbers` |
| D6 — revenue-per-production-dollar comparison + marketing budget recommendation | `advanced-numbers-percent`, `advanced-numbers-how-to-find-the-percent-of-a-number`, `advanced-numbers-how-to-divide-decimal-numbers`, `number-sense-how-to-compare-two-or-more-values` |

## LEARNING GOAL CHECK

```
deliverables: 6    claimed skills: 22    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forces test applied to every mapping:** could a competent Hero produce this deliverable
correctly without ever performing this skill? For all 22 skills above, no — e.g. D1 cannot be
produced without actually plotting the (score, price) pairs on a coordinate plane and fitting a
line to them; D3 cannot be produced without correctly naming which survey used stratified random
sampling vs. convenience sampling and why that distinction matters for generalizability; D5/D6
cannot be produced without genuine decimal multiplication/division and percent-of-a-number
arithmetic chained across three inputs (fraction × price × assumed audience, then ÷ budget).

**Why `new_coverage[]` is empty (not padding).** Every Statistics-and-Probability sampling,
scatter-plot, correlation, and slope/linear-equation skill this case's deliverables genuinely
force already has `n > 0` in `readmodel/standards_spine.json` — this project's Sampling And
Experiments, Displaying Data, and Algebra groups are already well covered by prior cases (Acton
Survey, Medical Statician, Cardiology, and others). No adjacent uncovered skill in this group is
reachable by this case's actual math. This is the `legacy_conversion_note` carve-out
(`skills/case-readiness/SKILL.md`, "2026-08-13" amendment): T1-10 downgrades the empty-
`new_coverage[]` finding from BLOCKER to a recorded GAP for a legacy conversion specifically,
rather than forcing a fabricated claim to manufacture a PASS.
