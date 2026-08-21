# Learning Goals — Driving Age

Bidirectional deliverable ↔ skill matrix. See `case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 scatterplot + LOBF, Appendix B data | statistics-and-probability-scatter-plot, statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data, statistics-and-probability-line-of-best-fit, statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data, statistics-and-probability-correlation, statistics-and-probability-how-to-identify-correlation-given-a-scatter-plot-or-set-of-data, geometry-line, number-sense-data |
| D2 graphed linear equation + predictions | statistics-and-probability-how-to-write-a-linear-equation-given-a-graph-of-a-line-of-a-set-of-d, statistics-and-probability-slope, statistics-and-probability-how-to-identify-the-slope-of-a-line-given-a-set-of-data-or-a-graph-o |
| D3 two-point linear equation, compared to D2 | statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data, statistics-and-probability-slope, statistics-and-probability-how-to-identify-the-slope-of-a-line-given-a-set-of-data-or-a-graph-o, number-sense-how-to-compare-two-or-more-values |
| D4 net two-year cost table + bar graph | measurement-currency, advanced-numbers-decimal, advanced-numbers-how-to-add-decimal-numbers, advanced-numbers-how-to-subtract-decimal-numbers, advanced-numbers-how-to-multiply-decimal-numbers, basic-operations-subtraction, basic-operations-how-to-subtract-multi-digit-numbers, basic-operations-multiplication, basic-operations-how-to-multiply-any-two-numbers, basic-operations-addition, basic-operations-how-to-add-multi-digit-numbers, measurement-unit, measurement-how-to-convert-an-amount-from-one-unit-to-another-unit, measurement-time, number-sense-bar-graph, number-sense-how-to-compare-two-or-more-values |

## LEARNING GOAL CHECK

```
deliverables: 4    claimed skills: 28    new_coverage: 0 (legacy carve-out, see case.json.new_coverage_note)
UNMAPPED DELIVERABLES: none -- D1, D2, D3, D4 each map to >=1 skill
UNREACHABLE SKILLS: none -- every id in standards[] appears in at least one deliverable's skills[] above
RESULT: PASS
```

**Forces test applied to each mapping** ("could a competent student produce this deliverable
correctly without ever performing this skill?"):

- D1 cannot be produced without plotting points (scatter-plot), judging their trend
  (correlation), and drawing a line through them (line-of-best-fit, geometry-line) — a student who
  skips any of these does not have a scatterplot with a line of best fit, they have a doodle.
- D2 cannot be produced without reading a slope and intercept off a drawn line and writing them as
  an equation (linear-equation-from-a-graph, slope) — the deliverable is explicitly "read directly
  off your graph," which is what forces the graph-reading skill rather than the data-reading one.
- D3 is deliberately the mirror of D2 — two data points, not a graph — which is what forces the
  distinct "given a set of data" linear-equation skill instead of re-testing D2's graph-reading
  skill a second time.
- D4 cannot be produced without decimal currency arithmetic across multiple operations
  (multiply miles x rate, multiply years, add/subtract to a net total) and a bar graph comparing
  the two option totals.

## Legacy new_coverage note

All 28 skills claimed in `standards[]` already had `n >= 1` in `readmodel/standards_spine.json`
before this conversion (5 of them — statistics-and-probability-scatter-plot,
statistics-and-probability-line-of-best-fit, geometry-line,
statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data, and
statistics-and-probability-how-to-write-a-linear-equation-given-a-graph-of-a-line-of-a-set-of-d —
were already tagged directly to "Driving Age" in `covered_by[]` by the pre-pipeline corpus scan;
the other 23 are basic-operations/advanced-numbers/measurement/number-sense skills already covered
by many other titled cases). `new_coverage[]` is honestly empty. Per `skills/case-readiness/SKILL.md`'s
2026-08-13 legacy-conversion carve-out on T1-10, this downgrades from a BLOCKER to a recorded GAP
because `case.json.legacy_conversion_note` is present — this case is being formalized, not freshly
authored, and no skill in `standards[]` is padding: every one is genuinely forced by D1-D4 above.
