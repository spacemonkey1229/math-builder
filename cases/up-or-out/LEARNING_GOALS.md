# Learning Goals — Up or Out

Bidirectional deliverable ↔ skill matrix (case-write §10, MCS-10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Box plots at both ends of the range | statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data, statistics-and-probability-box-and-whisker-plot, statistics-and-probability-quartiles, statistics-and-probability-outlier, statistics-and-probability-median |
| D2 — The size curve | statistics-and-probability-scatter-plot, statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data, statistics-and-probability-slope, statistics-and-probability-linear, statistics-and-probability-non-linear |
| D3 — All sizes pooled | statistics-and-probability-median, advanced-numbers-how-to-convert-numbers-to-percents, number-sense-how-to-compare-two-or-more-values |
| D4 — The cost memo | measurement-how-to-convert-an-amount-with-compound-units, statistics-and-probability-mean, statistics-and-probability-how-to-find-the-mean-of-a-set-of-data, advanced-numbers-how-to-convert-numbers-to-percents, number-sense-how-to-compare-two-or-more-values |
| D5 — The decision under an unknown size | number-sense-how-to-compare-two-or-more-values |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 15    new_coverage: 0 (reinforcement_note on file)
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none — every claimed skill is forced by at least one deliverable
RESULT: PASS
```

## Why the thin skills are genuinely forced

- **how-to-create-a-box-and-whisker-plot-given-a-set-of-data (n=1):** D1 supplies only raw sorted values (Appendix C) and the median-of-halves convention; the five-number summary, fences and plot must be built from them. No one can answer D1 without constructing the plot.
- **non-linear (n=2):** D2 asks for the slope over two stretches per plan and a linear versus non-linear call "and why". A student cannot justify the call without comparing the slopes (Tall: about -5.3 then +0.14 dollars per sq ft per sq ft; a single straight line cannot describe it).
- Skills at n >= 3 (quartiles, outlier, scatter plot terms) are reinforcement, not thin.

## Reinforcement carve-out

No skill in the spine has n==0 (checked 2026-10-28), so `new_coverage[]` is empty and `case.json.reinforcement_note` records the adjacent statistics skills considered and why the deliverables do not force them.
