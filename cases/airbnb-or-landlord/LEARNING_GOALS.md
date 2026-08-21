# Learning Goals — AirBnb Or Landlord

Bidirectional deliverable ↔ skill matrix (SPEC §1.7 / case-write §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 Airbnb annual profit breakdown | advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number, advanced-numbers-decimal, advanced-numbers-how-to-multiply-decimal-numbers, advanced-numbers-how-to-add-decimal-numbers, advanced-numbers-how-to-subtract-decimal-numbers, basic-operations-multiplication, basic-operations-how-to-multiply-any-two-numbers, basic-operations-addition, basic-operations-how-to-add-multi-digit-numbers, basic-operations-subtraction, basic-operations-how-to-subtract-multi-digit-numbers, measurement-currency |
| D2 Traditional-rental annual profit breakdown | advanced-numbers-percent, advanced-numbers-how-to-convert-percents-to-numbers, advanced-numbers-how-to-find-the-percent-of-a-number, advanced-numbers-decimal, advanced-numbers-how-to-multiply-decimal-numbers, basic-operations-multiplication, basic-operations-how-to-multiply-any-two-numbers, basic-operations-subtraction, measurement-currency |
| D3 Monthly-equivalent + percent-margin + new-mortgage check | basic-operations-division, basic-operations-how-to-divide-a-multi-digit-number-by-a-2-digit-number, advanced-numbers-how-to-divide-decimal-numbers, advanced-numbers-how-to-convert-numbers-to-percents, advanced-numbers-how-to-find-a-whole-given-the-percent-and-the-part-of-the-whole, number-sense-how-to-compare-two-or-more-values, measurement-rounding, measurement-how-to-round-a-number-to-a-specified-place-value |
| D4 Two visual displays (bar graph + pie chart) | number-sense-bar-graph, statistics-and-probability-pie-chart, number-sense-data |
| D5 Monthly household cash-flow total | basic-operations-addition, basic-operations-how-to-add-multi-digit-numbers, basic-operations-subtraction, basic-operations-how-to-subtract-multi-digit-numbers, measurement-currency, measurement-ratio, measurement-proportion, measurement-how-to-find-a-missing-amount-in-a-proportion |

**Forces test applied to every row:** *could a competent student produce this deliverable
correctly without ever performing this skill?* No, for all 28 mapped skills below.

- D1 forces percent-of-a-number (the 15.5% Airbnb host fee), decimal arithmetic (every dollar
  figure here has cents), and multi-step add/subtract/multiply to reach one net total.
- D2 forces converting a percent premium into a decimal multiplier (15% → ×1.15) and applying it
  to a real market baseline — this is not the same skill as D1's fee-subtraction, it's the
  reverse (percent added to a whole, not subtracted from one).
- D3 forces dividing an annual total by 12 (division by a 2-digit number), converting the
  resulting gap between A and B into a percent (not just a raw dollar difference), and rounding
  to a sensible number of decimal places for a currency comparison. "How to find a whole given
  the percent and the part of the whole" is forced by working the margin calculation in reverse
  (given both totals, express the difference as a percent of the smaller one) — the same
  operation this skill names.
- D4 forces the two required visual forms, each drawing on the same "Data" concept from a
  different angle (categorical comparison vs. whole-broken-into-parts).
- D5 forces multi-step signed addition/subtraction across four real dollar figures ending in one
  labeled total, and ratio/proportion in the sense that the whole exercise is a proportional
  budget check: does a rental-profit stream of a given size fit into a fixed monthly obligation.

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 28    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

`new_coverage[]` is honestly empty — every one of the 28 claimed skills already had `n >= 1` in
`readmodel/standards_spine.json` before this conversion (range 1–36; the lowest, "how to find a
whole given the percent and the part of the whole," was at n=1). This is a legacy conversion of a
real pre-pipeline case study, not a freshly authored one with no reason to exist — see
`case.json.legacy_conversion_note` and the 2026-08-13 T1-10 legacy-conversion carve-out in
`skills/case-readiness/SKILL.md`, which downgrades an honestly-empty `new_coverage[]` on a
`legacy_conversion_note` case from BLOCKER to GAP.
