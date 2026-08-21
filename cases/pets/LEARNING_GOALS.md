# Learning Goals — Pets

Bidirectional deliverable ↔ skill matrix (SPEC §1.7 / case-write §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 Day-1 startup cost table + $1,620-savings comparison | measurement-currency, advanced-numbers-decimal, advanced-numbers-how-to-add-decimal-numbers, advanced-numbers-how-to-subtract-decimal-numbers, basic-operations-addition, basic-operations-how-to-add-multi-digit-numbers, basic-operations-subtraction, basic-operations-how-to-subtract-multi-digit-numbers |
| D2 Year-1 total (with/without insurance) | advanced-numbers-how-to-add-decimal-numbers, advanced-numbers-how-to-multiply-decimal-numbers, basic-operations-addition, basic-operations-multiplication, basic-operations-how-to-multiply-any-two-numbers, number-sense-how-to-compare-two-or-more-values |
| D3 Full-lifetime total (insurance every year) | basic-operations-multiplication, basic-operations-how-to-multiply-any-two-numbers, advanced-numbers-how-to-multiply-decimal-numbers, basic-operations-addition, advanced-numbers-how-to-add-decimal-numbers |
| D4 Cost-per-year-of-lifespan, both pets | basic-operations-division, basic-operations-how-to-divide-a-multi-digit-number-by-a-2-digit-number, advanced-numbers-how-to-divide-decimal-numbers, measurement-rounding, measurement-how-to-round-a-number-to-a-specified-place-value, number-sense-how-to-compare-two-or-more-values |
| D5 Bar graph + pie chart | number-sense-bar-graph, statistics-and-probability-pie-chart, number-sense-data |
| D6 Insurance as % of Year-1 total | advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 6    claimed skills: 22    new_coverage: 0 (legacy-conversion carve-out, see case.json.new_coverage_note)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

Every claimed skill in `case.json.standards[]` traces to at least one deliverable above by the
"forces" test (*could a competent student produce this deliverable correctly without ever
performing this skill?* — no, for every row). Two adjacent skills were considered and rejected as
padding, not silently omitted: `measurement-ratio` and `measurement-proportion` — a student
computing D4's cost-per-year figure performs a single division, not a formal ratio/proportion
method, so neither is genuinely forced and neither is claimed.
