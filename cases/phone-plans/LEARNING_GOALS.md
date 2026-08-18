# Learning Goals — Phone Plans

Bidirectional deliverable <-> skill matrix.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 eligibility comparison | number-sense-how-to-compare-two-or-more-values, measurement-currency |
| D2 today's total monthly bill | basic-operations-multiplication, basic-operations-product, basic-operations-how-to-multiply-2-digit-numbers-by-single-digit-numbers, basic-operations-addition, basic-operations-sum, advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number, advanced-numbers-decimal, measurement-rounding, measurement-how-to-round-a-number-to-a-specified-place-value, measurement-currency |
| D3 growth projection (3rd/4th phone) | basic-operations-multiplication, basic-operations-addition, basic-operations-subtraction, basic-operations-difference, measurement-currency |
| D4 original bar graph | number-sense-bar-graph |
| D5 hotspot capacity comparison | measurement-unit, number-sense-how-to-compare-two-or-more-values |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 16    new_coverage: 0
UNMAPPED DELIVERABLES: none -- every deliverable (D1-D5) has a non-empty skills column.
UNREACHABLE SKILLS: none -- every claimed standards[] id appears in at least one deliverable's
  skills column above (cross-checked against case.json.standards[]).
RESULT: PASS
```

Forces test applied to each mapping ("could a competent student produce this deliverable correctly
without ever performing this skill?"):

- D1: cannot identify which of two named tiers is eligible, or state a dollar figure to justify
  ruling one out, without comparing at least two values and reading currency figures. Forces both.
- D2: cannot get today's total bill without multiplying a per-line rate by a line count, summing
  phone + tablet costs, applying Oregon's percent tax rate to a decimal currency total, and
  rounding the result to the cent. Forces all eleven listed skills; none is decorative.
- D3: cannot extend the table to 3 and 4 lines without more multiplication/addition, and cannot
  state how much MORE the bill grows at each step without a subtraction/difference. Forces all five.
- D4: the boilerplate Challenge 2(b) already requires a visual; D4 makes it a specific graph type
  (bar graph of total cost across carrier x line-count), which is what actually forces the skill
  rather than leaving "a visual" undefined.
- D5: cannot compare 30GB vs. 50GB meaningfully without both a unit concept (GB as a measurement
  unit, not an interchangeable "number") and a two-value comparison.

`new_coverage[]` is empty (case.json.new_coverage_note documents the check against the spine's
current n==0 list) -- protected by case-readiness's T1-10 legacy-conversion carve-out since
`case.json.legacy_conversion_note` is present.
