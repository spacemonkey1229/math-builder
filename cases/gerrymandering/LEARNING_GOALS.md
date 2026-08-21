# Learning Goals — Gerrymandering

Bidirectional deliverable ↔ skill matrix. Run against `readmodel/standards_spine.json` at write
time — see the LEARNING GOAL CHECK result below.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 population-balance table | statistics-and-probability-population, statistics-and-probability-mean, statistics-and-probability-how-to-find-the-mean-of-a-set-of-data, advanced-numbers-percent, advanced-numbers-how-to-convert-numbers-to-percents |
| D2 compactness comparison + map | geometry-perimeter, geometry-area, geometry-how-to-find-the-measure-of-the-perimeter-of-a-polygon, geometry-how-to-find-the-area-of-a-circle, geometry-convex |
| D3 efficiency-gap calculation | advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number, measurement-ratio, measurement-proportion, measurement-how-to-find-a-missing-amount-in-a-proportion |
| D4 demographic representativeness check | advanced-numbers-percent, advanced-numbers-how-to-convert-numbers-to-percents, advanced-numbers-how-to-find-the-percent-of-a-number, statistics-and-probability-population |

**"Forces" test applied:** could a competent student produce each deliverable correctly without
ever performing the listed skill? For each skill above, no — e.g. D1's percent-deviation column
cannot be computed without first finding the mean (the "ideal" district population = statewide
total ÷ 3), and D2's compactness score is defined as district area ÷ area of a circle sharing the
district's perimeter, which requires computing a circle's area from that perimeter directly. D3's
county-split vote apportionment (Plan B) is a live proportion problem, not a percent shortcut —
students must set up "county votes : county population :: split-region votes : split-region
population" and solve for the missing amount.

## LEARNING GOAL CHECK

```
deliverables: 4    claimed skills: 14    new_coverage: 1
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

`new_coverage[]` = `["geometry-convex"]` (n=0 in the spine before this case). "Convex" is a
genuine, forced vocabulary term here, not padding: D2 requires the student to look at their
resulting district shape (the intact Treasure Valley under Plan A, or the extended North Idaho
region under Plan B) and classify it as convex or concave as part of defending its compactness
score — a district that "bites in" on itself to capture a specific population pocket is the
textbook visual signature of cracking/packing, and convexity is the precise vocabulary for that
observation.

No other candidate skill in the claimed set had `n == 0`; percent, population, mean,
perimeter/area, and ratio/proportion skills were all already covered elsewhere in the corpus, so
they are claimed in `standards[]` (they are genuinely forced by this case's deliverables) but not
counted again in `new_coverage[]`.
