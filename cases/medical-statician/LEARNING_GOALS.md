# Learning Goals — Medical Statistician

Bidirectional deliverable ↔ skill matrix (SPEC §1.5 item 3 / case-write §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 stated total sample size, arithmetic shown | `statistics-and-probability-sample-size`, `statistics-and-probability-sample`, `basic-operations-division`, `basic-operations-how-to-divide-a-multi-digit-number-by-a-2-digit-number`, `basic-operations-addition`, `measurement-currency` |
| D2 sampling-method comparison table | `statistics-and-probability-simple-random-sampling`, `statistics-and-probability-stratified-sampling`, `statistics-and-probability-systematic-sampling`, `statistics-and-probability-cluster-sampling`, `statistics-and-probability-convenience-sampling`, `statistics-and-probability-random`, `statistics-and-probability-probability` |
| D3 specific sample-drawing plan | `statistics-and-probability-population`, `statistics-and-probability-sample`, `statistics-and-probability-random` |
| D4 total cost/time vs. budget, dollars remaining | `measurement-currency`, `basic-operations-multiplication`, `basic-operations-how-to-multiply-any-two-numbers`, `basic-operations-division`, `basic-operations-how-to-divide-a-multi-digit-number-by-a-2-digit-number`, `basic-operations-addition`, `basic-operations-subtraction`, `advanced-numbers-percent`, `advanced-numbers-how-to-find-the-percent-of-a-number` |
| D5 margin of error at 95% confidence | `advanced-numbers-percent`, `advanced-numbers-how-to-convert-numbers-to-percents`, `statistics-and-probability-probability`, `statistics-and-probability-sample-size` |
| D6 two original visual displays (sample size, cost, MOE) | `number-sense-bar-graph` |

## Forces test

*"Could a competent student produce this deliverable correctly without ever performing this skill?"*

- **D1** cannot be produced without knowing what a sample and a sample size are, and without dividing
  the remaining $493,000 budget by a per-subject cost to get an affordable count — division and
  currency are unavoidable.
- **D2** cannot be produced without being able to name and distinguish all four probability methods
  and all four non-probability methods — the deliverable explicitly requires rejecting three
  alternatives in the chosen category, which requires knowing what they are.
- **D3** cannot be produced without the concepts of population (the full set) vs. sample (the subset
  drawn) and, for Option A specifically, what "random" selection actually requires operationally.
- **D4** is pure multi-step currency arithmetic against a hard budget cap, plus a percent-remaining
  statement — all five operations/percent skills listed are each individually exercised (dollars
  spent add; drug cost is per-subject count × per-week rate × weeks, i.e. multiplication; dollars
  remaining is total minus spent, i.e. subtraction; percent of budget used requires percent-of-a-
  number).
- **D5** cannot be produced without correctly using the margin-of-error formula's percent output at
  the stated 95% confidence level, which is fundamentally a probability/statistics-and-percent
  computation.
- **D6** cannot be produced without building at least one comparative bar graph — the deliverable
  names three quantities (sample size, cost, margin of error) to display, the natural chart for a
  side-by-side A-vs-B numeric comparison.

## LEARNING GOAL CHECK

```
deliverables: 6    claimed skills: 21    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

`new_coverage` is honestly 0 — see `case.json.new_coverage_note`. This is a legacy conversion
(`case.json.legacy_conversion_note` present), so per `skills/case-readiness/SKILL.md`'s
2026-08-13 legacy-conversion carve-out on T1-10, an empty `new_coverage[]` here is a recorded GAP,
not a BLOCKER.
