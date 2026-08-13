# Learning Goals — Wildfire

Bidirectional deliverable ↔ skill matrix (case-write §10 / SPEC.md §1.5 item 3).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — anticipated acreage (sector-growth model) | geometry-area, geometry-how-to-find-the-area-of-a-circle, measurement-unit, measurement-distance, measurement-how-to-convert-an-amount-from-one-unit-to-another-unit, advanced-numbers-decimal, advanced-numbers-how-to-multiply-decimal-numbers |
| D2 — people expected to lose homes tonight | measurement-ratio, measurement-proportion, measurement-how-to-find-a-missing-amount-in-a-proportion, advanced-numbers-percent, advanced-numbers-how-to-convert-percents-to-numbers, advanced-numbers-how-to-multiply-decimal-numbers |
| D3 — time to reach San Fernando + defense site | measurement-distance, measurement-how-to-convert-an-amount-with-compound-units, measurement-how-to-convert-an-amount-from-one-unit-to-another-unit, advanced-numbers-how-to-divide-decimal-numbers |
| D4 — time to reach Santa Clarita + defense site | measurement-distance, measurement-how-to-convert-an-amount-with-compound-units, measurement-how-to-convert-an-amount-from-one-unit-to-another-unit, advanced-numbers-how-to-divide-decimal-numbers |
| D5 — final recommendation | number-sense-how-to-compare-two-or-more-values |

## LEARNING GOAL CHECK

- deliverables: 5
- claimed skills: 15
- new_coverage: 0

**Forces test applied:** "Could a competent student produce this deliverable correctly without ever performing this skill?" For each row above the answer is no —

- D1 cannot be produced without converting chains → feet → a linear distance, then computing a circular-sector area, then converting square-chains/square-feet → acres. All seven mapped skills are load-bearing arithmetic, not decoration.
- D2 cannot be produced without treating the census housing-density figure as a ratio, solving a proportion against D1's acreage, and applying a percent (occupancy rate) and decimal multiplication (household size) to get a person count.
- D3/D4 cannot be produced without converting a compound rate (chains/hour) to a usable speed (mph), then dividing a real mileage figure by that speed to solve for time.
- D5 cannot be produced without an explicit, stated comparison of the two competing numeric arguments (lead time vs. population) — the case's whole balance test depends on the student actually doing this, not asserting a preference.

**UNMAPPED DELIVERABLES:** none.
**UNREACHABLE SKILLS:** none — every one of the 15 claimed skills is required by at least one deliverable above; none is present merely because the legacy tagging listed it.

**RESULT: PASS**

## Note on the legacy tag list

The legacy standards spine listed **91** skills against "Wildfire" in `covered_by[]` — effectively the entire basic-operations/number-sense/fractions/geometry/measurement/statistics surface of the spine, spanning skills as basic as single-digit addition and as unrelated to this case's actual deliverables as histograms and conditional probability. None of those are dropped lightly, but the LEARNING GOAL CHECK is explicit: a skill earns a place in `standards[]` only if some deliverable in this case actually forces it, not because the original case *touched on* the topic in its "How To…" Appendix E broad Table 1–6 sweep (which listed nearly every MS-math topic as a generic option, not a specific requirement). The 15 skills retained here are the ones this case's own five deliverables cannot be produced without.

`new_coverage[]` is empty: every one of the 15 retained skills already has spine coverage (`n>0`) from other cases (verified directly against `readmodel/standards_spine.json`, not assumed). This is reported plainly rather than padded — see `case.json.new_coverage_note`.
