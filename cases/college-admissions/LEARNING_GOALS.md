# LEARNING_GOALS — College Admissions

Bidirectional deliverable ↔ skill matrix (case-write SKILL.md §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — box-and-whisker plot, SAT range | statistics-and-probability-quartiles, statistics-and-probability-box-and-whisker-plot, statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data, statistics-and-probability-outlier, statistics-and-probability-median, statistics-and-probability-range |
| D2 — scatter plot, two applicants vs. class benchmarks | statistics-and-probability-scatter-plot, statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data |
| D3 — 5-data-point comparison table | number-sense-how-to-compare-two-or-more-values, measurement-ratio |
| D4 — SAT point-gap / percent-of-lower-score computation | advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number, advanced-numbers-how-to-convert-numbers-to-percents, measurement-rounding, measurement-how-to-round-a-number-to-a-specified-place-value |
| D5 — raw-count-above estimate, percentile × school size | advanced-numbers-how-to-find-the-percent-of-a-number, measurement-ratio, measurement-rounding, number-sense-how-to-compare-two-or-more-values |

**Forces test applied to each row:** could a competent student produce this deliverable correctly
without ever performing the listed skill? For all five rows, no — D1 cannot be drawn without
identifying quartiles/median/range and plotting an outlier check; D2 requires an actual scatter
plot construction; D3 requires comparing values and reading a ratio-shaped statistic (e.g.
admit rate, percent submitting a score); D4 is a percent-of-a-number / percent-conversion
calculation with a rounding step; D5 requires computing a percent of a school's enrollment and
comparing the two resulting counts.

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 15    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

`new_coverage` is 0 by design for this legacy conversion — see `case.json.new_coverage_note` and
the permanent 2026-08-13 T1-10 legacy-conversion carve-out in `skills/case-readiness/SKILL.md`.
Every one of the 15 claimed `standards[]` skills already has `n>=3` in `readmodel/standards_spine.json`,
each shared with at least two other published cases (LeBron Vs. Michael and Speed Climbing are the
closest neighbors on the quartile/box-and-whisker pair). None were padded in — each is forced by a
named deliverable above, per the mutual-reachability check.
