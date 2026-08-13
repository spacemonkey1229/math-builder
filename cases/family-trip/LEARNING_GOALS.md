# Learning Goals — Family Trip

Bidirectional deliverable ↔ skill matrix (case-write §10). "Forces" test applied strictly: could a
competent student produce this deliverable correctly without ever performing this skill? If yes,
the mapping is fake and was cut.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — full cost breakdown table (fares/fees or fuel/hotel, itemized to the penny) | measurement-currency, advanced-numbers-decimal, advanced-numbers-how-to-add-decimal-numbers, advanced-numbers-how-to-multiply-decimal-numbers, advanced-numbers-how-to-divide-decimal-numbers, basic-operations-addition, basic-operations-how-to-add-multi-digit-numbers, basic-operations-multiplication, basic-operations-how-to-multiply-any-two-numbers, basic-operations-division, basic-operations-how-to-divide-a-multi-digit-number-by-a-2-digit-number, measurement-unit, measurement-how-to-convert-an-amount-from-one-unit-to-another-unit |
| D2 — dated itinerary, elapsed travel time, vacation days used | measurement-time, measurement-how-to-find-elapsed-time, measurement-how-to-add-and-subtract-time, measurement-how-to-convert-between-units-of-time, basic-operations-subtraction, basic-operations-how-to-subtract-multi-digit-numbers |
| D3 — recompute Option B with the IRS mileage rate; compare the two driving totals | advanced-numbers-how-to-multiply-decimal-numbers, advanced-numbers-how-to-subtract-decimal-numbers, number-sense-how-to-compare-two-or-more-values |
| D4 — bar graph (A vs B totals) + pie chart (cost breakdown) | number-sense-bar-graph, statistics-and-probability-pie-chart, number-sense-data |
| D5 — dollars-remaining-for-gifts calculation | basic-operations-subtraction, basic-operations-how-to-subtract-multi-digit-numbers, advanced-numbers-how-to-subtract-decimal-numbers, measurement-rounding, measurement-how-to-round-a-number-to-a-specified-place-value |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 26    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**new_coverage note:** this is a legacy conversion. All 26 claimed skills were already tagged to
"Family Trip" in `readmodel/standards_spine.json`'s `covered_by[]` from the prior corpus pass, and
every one of the 61 originally-tagged candidate skills already has `n >= 1` (range 1–29) — none had
`n == 0`. After applying the LEARNING GOAL CHECK to narrow the 61 candidates down to the 26 a
Challenge-3 deliverable actually forces, `new_coverage[]` is genuinely empty. This is reported
plainly rather than padded: this legacy case closes no net-new gap in the standards spine, it
reinforces skills the corpus already covers elsewhere.
