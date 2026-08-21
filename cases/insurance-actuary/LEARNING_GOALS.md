# Learning Goals — Insurance Actuary

Bidirectional deliverable ↔ skill matrix (SPEC §1.7 / case-write §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — 2019 forecast table (Young/Middle/Senior, linear-trend from 12 quarters) | `statistics-and-probability-linear`, `statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data`, `statistics-and-probability-mean`, `statistics-and-probability-how-to-find-the-mean-of-a-set-of-data`, `measurement-ratio` |
| D2 — blended remaining-book comparison, margin as a percent | `statistics-and-probability-mean`, `statistics-and-probability-how-to-find-the-mean-of-a-set-of-data`, `measurement-ratio`, `advanced-numbers-percent`, `advanced-numbers-how-to-find-the-percent-of-a-number`, `advanced-numbers-how-to-convert-numbers-to-percents` |
| D3 — ranked 27-class breakdown + risk-tier composition shares | `measurement-ratio`, `advanced-numbers-percent`, `advanced-numbers-how-to-convert-numbers-to-percents` |
| D4 — trend chart, 12 quarters × 3 age classes | `statistics-and-probability-linear`, `measurement-ratio` |

## LEARNING GOAL CHECK

```
deliverables: 4    claimed skills: 8    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forces test applied to each mapping** (*could a competent student produce this deliverable
correctly without ever performing this skill?*):

- **D1** cannot be produced without fitting a line to a set of data (12 known quarters) and
  extending it — that is literally "how to write a linear equation given a set of data." The
  student also needs the mean/sum of coverages per quarter and a Ĉ/car-year ratio. A student
  who just eyeballs "2018 looks like 2017 plus a bit" has not performed this skill and cannot
  produce a defensible D1.
- **D2** cannot be produced without computing an exposure-weighted mean across two combined age
  classes for each option, and expressing the gap between A and B as a percent — a straight
  dollar-difference is not the deliverable asked for.
- **D3** requires converting each risk-tier's share of an age class's exposure into a percent
  (20.6% / 37.4% / 42.0% for Young, etc.) and comparing per-vehicle ratios across 27 rows to find
  the highest/lowest — cannot be produced by reading the table top to bottom.
- **D4** requires plotting a genuinely linear (or near-linear) 12-point trend per class — the
  same "linear" term and the same rate/ratio the y-axis is built from.

## `new_coverage[]` — why it is empty (legacy carve-out, see `case.json.legacy_conversion_note`)

Every claimed skill already has `n > 0` in `readmodel/standards_spine.json`, and "Insurance
Actuary" was not previously listed in any of their `covered_by[]` arrays (verified 2026-08-20).
This is a case being *formalized* through the pipeline, not freshly authored to close a
coverage gap — per `skills/case-readiness/SKILL.md`'s T1-10 legacy carve-out, this downgrades
from a BLOCKER to a recorded GAP rather than requiring a padded claim. No skill above was added
to `standards[]` that the deliverables don't genuinely force.
