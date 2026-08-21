# Learning Goals — Heist

Bidirectional deliverable ↔ skill matrix (case-write §10). "Forces" test applied strictly: could a
competent student produce this deliverable correctly without ever performing this skill? If yes,
the mapping is fake and was cut.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — segment-by-segment route table, total miles, total drive time | number-sense-distance, measurement-distance, number-sense-measurement, number-sense-data, basic-operations-addition, basic-operations-sum, basic-operations-how-to-add-multi-digit-numbers, advanced-numbers-decimal, advanced-numbers-how-to-add-decimal-numbers, measurement-time, measurement-how-to-add-and-subtract-time, measurement-how-to-find-elapsed-time, measurement-how-to-convert-between-units-of-time |
| D2 — 30-second window check for both options, average speed (mph), "does 94/98% tell the whole story" | measurement-time, measurement-how-to-convert-between-units-of-time, measurement-how-to-add-and-subtract-time, measurement-how-to-find-elapsed-time, basic-operations-subtraction, basic-operations-difference, basic-operations-how-to-subtract-multi-digit-numbers, number-sense-how-to-compare-two-or-more-values, number-sense-greater-than, number-sense-less-than, number-sense-equal, basic-operations-division, basic-operations-quotient, basic-operations-how-to-divide-a-multi-digit-number-by-a-2-digit-number, measurement-how-to-convert-an-amount-with-compound-units, measurement-how-to-convert-an-amount-from-one-unit-to-another-unit, advanced-numbers-decimal, advanced-numbers-how-to-divide-decimal-numbers, measurement-rounding, measurement-how-to-round-a-number-to-a-specified-place-value |
| D3 — full compound-probability calculation for each option, percentage-point gap | advanced-numbers-percent, advanced-numbers-how-to-convert-percents-to-numbers, advanced-numbers-how-to-convert-numbers-to-percents, advanced-numbers-decimal, advanced-numbers-decimal-number, advanced-numbers-how-to-read-decimal-numbers, advanced-numbers-how-to-multiply-decimal-numbers, advanced-numbers-how-to-subtract-decimal-numbers, basic-operations-multiplication, basic-operations-product, basic-operations-how-to-multiply-any-two-numbers, statistics-and-probability-event, statistics-and-probability-outcome, statistics-and-probability-probability, statistics-and-probability-theoretical-probability, statistics-and-probability-independent-event, statistics-and-probability-dependent-event, statistics-and-probability-conditional-probability, statistics-and-probability-how-to-determine-the-probability-of-a-single-event, statistics-and-probability-how-to-determine-the-probability-of-a-compound-event, statistics-and-probability-how-to-determine-the-probability-of-conditional-events, measurement-rounding, measurement-how-to-round-a-number-to-a-specified-place-value |
| D4 — police-proximity check against a real station location | number-sense-distance, measurement-distance, number-sense-how-to-compare-two-or-more-values, number-sense-greater-than, number-sense-less-than, measurement-estimating, number-sense-data |
| D5 — bar graph (A vs B final %) + pie chart/histogram (risk-factor share) | number-sense-bar-graph, statistics-and-probability-pie-chart, statistics-and-probability-histogram, statistics-and-probability-how-to-create-a-pie-chart-given-a-set-of-data, statistics-and-probability-how-to-create-a-histogram-given-a-set-of-data, number-sense-data, statistics-and-probability-experimental-probability, statistics-and-probability-theoretical-probability |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 55    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**new_coverage note:** this is a legacy conversion. All 55 claimed skills were already tagged to
"Heist" in `readmodel/standards_spine.json`'s `covered_by[]` from the prior corpus pass (the
original tag set had 66 candidates; every one already had `n >= 1`). After applying the LEARNING
GOAL CHECK to narrow the 66 candidates down to the 55 a Challenge-3 deliverable actually forces
(dropping the 10 decorative single-digit/2-digit operation variants that are strictly subsumed by
the multi-digit/decimal versions this case's real numbers actually require, plus the bare generic
"Number" term), `new_coverage[]` is genuinely empty. This is reported plainly rather than padded:
this legacy case closes no net-new gap in the standards spine, it reinforces skills the corpus
already covers elsewhere. Per `skills/case-readiness/SKILL.md`'s 2026-08-13 T1-10 legacy-conversion
carve-out, an empty `new_coverage[]` on a case carrying `legacy_conversion_note` downgrades from a
BLOCKER to a recorded GAP, not a defect requiring a fabricated skill claim.

**Dropped from the original 66-skill tag set, with reason:**
- `number-sense-number` (bare "Number" term) — too generic to be forced by any specific deliverable; every deliverable already forces more specific number-sense/operation terms.
- `basic-operations-how-to-add-single-digit-numbers`, `-how-to-add-2-digit-numbers` — subsumed by `-how-to-add-multi-digit-numbers`, which the case's real multi-digit totals (miles, minutes, percentages) actually require.
- `basic-operations-how-to-subtract-with-single-digit-differences`, `-how-to-subtract-2-digit-numbers` — subsumed by `-how-to-subtract-multi-digit-numbers` (D2's window-slack subtraction: 30 − 17, 30 − 29 are single/double digit, but the D3 percentage-point gap and D1 totals are multi-digit; kept the more general skill only).
- `basic-operations-how-to-multiply-single-digit-numbers`, `-how-to-multiply-2-digit-numbers-by-single-digit-numbers`, `-how-to-multiply-multi-digit-numbers-by-single-digit-numbers`, `-how-to-multiply-2-digit-numbers-by-2-digit-numbers` — subsumed by `-how-to-multiply-any-two-numbers`, which is what D3's compound-probability chain (multiplying six-plus decimal survival factors together) actually is.
- `basic-operations-how-to-divide-with-single-digit-quotients`, `-how-to-divide-a-multi-digit-number-by-a-single-digit-number` — subsumed by `-how-to-divide-a-multi-digit-number-by-a-2-digit-number`, which D2's average-speed calculation (8.9 ÷ 0.35) actually requires.
