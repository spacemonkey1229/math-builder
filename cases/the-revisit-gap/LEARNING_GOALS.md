# The Revisit Gap — Learning Goal Matrix

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Box-and-whisker plots of detection lag for both feeds | statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data |
| D2 — Minimum-detectable-clearing-size comparison, resolution ratio vs. area ratio | statistics-and-probability-non-linear, measurement-how-to-convert-an-amount-from-one-unit-to-another-unit |
| D3 — Line of best fit for commercial cost vs. monitored area | statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data |
| D4 — Solve for the missing month's invoice amount | statistics-and-probability-how-to-find-a-missing-data-element-given-the-mean-and-the-remaining- |
| D5 — Hectares-detected-per-dollar results table and recommendation | measurement-how-to-convert-an-amount-from-one-unit-to-another-unit |

## Bidirectional check

**Claimed skills (standards[]), 5 total:**

statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data,
statistics-and-probability-non-linear,
statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data,
statistics-and-probability-how-to-find-a-missing-data-element-given-the-mean-and-the-remaining-,
measurement-how-to-convert-an-amount-from-one-unit-to-another-unit

Every one of the 5 appears in at least one deliverable's skill list above:

- **How to create a box and whisker plot** — D1 is not solvable without it: the case explicitly
  asks for a plot, not a mean or a list, because the spread (not just the center) is the point.
- **Non-linear** — D2 forces the actual recognition test (why does a 3.3x finer resolution
  produce an 11.1x smaller minimum detectable area, not a 3.3x smaller one?), not a definition
  recital.
- **How to draw a line of best fit** — D3 requires fitting a line through Appendix D's real
  multi-reserve sample and using it to extrapolate, not just reading a number off a table.
- **How to find a missing data element given the mean** — D4 is a real, disclosed gap in the
  board's own paperwork (one month illegible), solvable only by combining the stated mean with
  the other eleven known values — a student cannot produce this deliverable by narrating around
  it.
- **How to convert an amount from one unit to another unit** — D2 requires converting square
  meters (the pixel-based minimum detectable patch size) to hectares before it can be compared to
  Appendix C's hectare-denominated clearing totals; D5's results table requires consolidating a
  per-km²-per-scene subscription rate, a scene count, and an hourly labor rate into one common
  annual dollar total before the ratio can be computed.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 5    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Note on new_coverage: 0.** See `case.json`'s `reinforcement_note` — all four skills the
originating concept sheet (`CONCEPTS_remote-sensing_2026-09-12.md`, C2) scored as prospective new
coverage show `n>=1` on the live spine as of this write, matching the concept sheet's own counts
almost exactly (one skill, the line-of-best-fit how-to, drifted from n=2 to n=3 in the interim as
`Driving Age` published — still nowhere near `n==0` either way). None pass the strict `n==0` test
for `new_coverage[]`. Per established project precedent (`cases/pixel-snap/case.json`,
`cases/the-mooring-choice/case.json`, `cases/the-repeat-match/case.json`), this ships as a
**reinforcement** case — a further real data point on these four still-thin skills — with
`new_coverage[]` correctly empty rather than a forced false claim. Flagged for the human sign-off
SPEC §7 implies, not silently resolved.
