# Learning Goals — Biostatician

Bidirectional deliverable ↔ skill matrix (case-write SKILL.md Section 10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Three histograms of time spent, one per weight group | `statistics-and-probability-histogram`, `statistics-and-probability-how-to-create-a-histogram-given-a-set-of-data` |
| D2 — Three box-and-whisker plots on a shared scale | `statistics-and-probability-box-and-whisker-plot`, `statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data`, `statistics-and-probability-quartiles`, `statistics-and-probability-median` |
| D3 — Percent-above-median table (average vs. overweight/obese medians) | `statistics-and-probability-median`, `advanced-numbers-percent`, `advanced-numbers-how-to-convert-numbers-to-percents` |
| D4 — Mean-and-range comparison by gender and age | `statistics-and-probability-mean`, `statistics-and-probability-how-to-find-the-mean-of-a-set-of-data`, `statistics-and-probability-range`, `number-sense-how-to-compare-two-or-more-values` |
| D5 — Outlier check on the obese group's box plot | `statistics-and-probability-outlier`, `statistics-and-probability-mean`, `statistics-and-probability-median` |

## Skill list (`case.json.standards[]`)

```
advanced-numbers-percent
advanced-numbers-how-to-convert-numbers-to-percents
statistics-and-probability-histogram
statistics-and-probability-how-to-create-a-histogram-given-a-set-of-data
statistics-and-probability-box-and-whisker-plot
statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data
statistics-and-probability-quartiles
statistics-and-probability-median
statistics-and-probability-mean
statistics-and-probability-how-to-find-the-mean-of-a-set-of-data
statistics-and-probability-range
statistics-and-probability-outlier
number-sense-how-to-compare-two-or-more-values
```

13 skills claimed. All 13 are `n >= 1` in `readmodel/standards_spine.json` at the time of this
conversion (each already tagged to at least one other case, several — `histogram`, `median`,
`percent` — tagged to "Biostatician" itself by the pre-pipeline corpus scan). `new_coverage[]` is
therefore empty — see `case.json.legacy_conversion_note` for why that is expected and permitted
under the case-readiness T1-10 legacy-conversion carve-out (2026-08-13), not padding: every skill
above is genuinely forced by a deliverable (see table), and the full spine's `n == 0` list (86
skills, dominated by geometry solids, pre-calculus, calculus, and discrete mathematics) was
checked in full — nothing on it is naturally forced by a statistics-and-probability case built on
histograms, box plots, and percent/mean/median comparisons of a real dataset. Padding one in would
be exactly the fabricated-mapping failure the LEARNING GOAL CHECK exists to catch.

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 13    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

Every deliverable maps to at least one skill; every claimed skill is forced by at least one
deliverable (checked both directions by hand against the table above — a competent Hero cannot
produce D1 without knowing what a histogram is and how to build one from data; cannot produce D2
without quartiles and the median; cannot produce D3 without median and percent conversion; cannot
produce D4 without mean, range, and a comparison method; cannot produce D5 without the outlier
concept applied back to mean vs. median).
