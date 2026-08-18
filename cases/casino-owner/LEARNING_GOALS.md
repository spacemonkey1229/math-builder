# LEARNING_GOALS.md — Casino Owner

Bidirectional deliverable ↔ skill matrix (case-write §10 / case-readiness T1-11).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Indigo weighted-average rake/game-length table (3 tiers) | advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number, advanced-numbers-decimal, advanced-numbers-how-to-multiply-decimal-numbers, basic-operations-multiplication, basic-operations-how-to-multiply-any-two-numbers, statistics-and-probability-mean, statistics-and-probability-how-to-find-the-mean-of-a-set-of-data |
| D2 — Indigo dollars-per-table-per-hour (3 tiers) | measurement-how-to-convert-between-units-of-time, measurement-how-to-convert-an-amount-with-compound-units, basic-operations-division, basic-operations-how-to-divide-a-multi-digit-number-by-a-2-digit-number, advanced-numbers-how-to-divide-decimal-numbers |
| D3 — Video machine blended profit-per-play | statistics-and-probability-probability, statistics-and-probability-how-to-determine-the-probability-of-a-single-event, statistics-and-probability-mean, statistics-and-probability-how-to-find-the-mean-of-a-set-of-data, advanced-numbers-percent, advanced-numbers-how-to-convert-percents-to-numbers, advanced-numbers-decimal |
| D4 — Weekly profit projection per option | measurement-how-to-convert-an-amount-with-compound-units, advanced-numbers-how-to-convert-percents-to-numbers, basic-operations-multiplication, basic-operations-division, number-sense-how-to-compare-two-or-more-values |
| D5 — Original bar graph + written comparison | number-sense-bar-graph, number-sense-how-to-compare-two-or-more-values |

## Reachability check (every claimed skill has a forcing deliverable)

| Skill id | Forced by |
|---|---|
| advanced-numbers-percent | D1, D3 |
| advanced-numbers-how-to-find-the-percent-of-a-number | D1 |
| advanced-numbers-how-to-convert-percents-to-numbers | D3, D4 |
| advanced-numbers-decimal | D1, D3 |
| advanced-numbers-how-to-multiply-decimal-numbers | D1 |
| advanced-numbers-how-to-divide-decimal-numbers | D2 |
| basic-operations-multiplication | D1, D4 |
| basic-operations-how-to-multiply-any-two-numbers | D1 |
| basic-operations-division | D2, D4 |
| basic-operations-how-to-divide-a-multi-digit-number-by-a-2-digit-number | D2 |
| measurement-how-to-convert-between-units-of-time | D2 |
| measurement-how-to-convert-an-amount-with-compound-units | D2, D4 |
| statistics-and-probability-probability | D3 |
| statistics-and-probability-how-to-determine-the-probability-of-a-single-event | D3 |
| statistics-and-probability-mean | D1, D3 |
| statistics-and-probability-how-to-find-the-mean-of-a-set-of-data | D1, D3 |
| number-sense-how-to-compare-two-or-more-values | D4, D5 |
| number-sense-bar-graph | D5 |

**Forces test applied to each row above:** could a competent student produce the deliverable
correctly without ever performing this skill? For every row the answer is no — e.g. D1 cannot be
computed without finding the percent of a number (rake % of a pot) and averaging six pot-size
bands weighted by their own frequencies (mean of a weighted data set); D3 cannot be computed
without converting an "X to 1" odds figure into a win probability (probability of a single event)
and blending four bet-size outcomes by their frequency (mean, again weighted); D4 cannot be
computed without converting a percentage-of-machines-in-use figure into a count of active units
and a minutes-per-game figure into an hourly rate (compound-unit conversion), then comparing two
final dollar totals (compare two or more values).

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 18    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

`new_coverage` is 0 for this case (see `case.json.new_coverage_note`) — every one of the 18
claimed skills already has `n>=8` elsewhere in the corpus, and the current spine's `n==0` list is
entirely geometry/pre-calculus/calculus/discrete-mathematics content this case's arithmetic does
not reach. The T1-10 legacy-conversion carve-out (`skills/case-readiness/SKILL.md`, added
2026-08-13) applies: `case.json.legacy_conversion_note` is present, so an honest empty
`new_coverage[]` downgrades from BLOCKER to a recorded GAP rather than blocking the case outright.
