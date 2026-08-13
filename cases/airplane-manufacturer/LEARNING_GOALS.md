# Learning Goals — Airplane Manufacturer

Bidirectional deliverable <-> skill matrix (case-write §10 LEARNING GOAL CHECK).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 dimensioned nets | geometry-net, geometry-2-dimensional, geometry-3-dimensional, geometry-radius, geometry-diameter, geometry-triangle, geometry-equilateral-triangle, geometry-square, geometry-rectangle, geometry-polygon, geometry-vertex, geometry-concave, geometry-irregular-polygon, geometry-quadrilateral |
| D2 cut-path length | geometry-perimeter, geometry-circumference, geometry-how-to-find-the-measure-of-the-perimeter-of-a-polygon, geometry-how-to-find-the-measure-of-the-circumference-of-a-circle, geometry-pi |
| D3 cut time | measurement-time, measurement-how-to-find-elapsed-time, measurement-how-to-add-and-subtract-time, advanced-numbers-how-to-divide-decimal-numbers |
| D4 net material area / % of sheet | geometry-area, geometry-how-to-find-the-area-of-a-circle, geometry-how-to-find-the-area-of-a-triangle, geometry-how-to-find-the-area-of-a-rectangle, advanced-numbers-percent, advanced-numbers-how-to-convert-numbers-to-percents, advanced-numbers-how-to-find-the-percent-of-a-number |
| D5 max weekly production | advanced-numbers-how-to-multiply-decimal-numbers, advanced-numbers-how-to-divide-decimal-numbers |
| D6 cost / profit / margin / breakeven | advanced-numbers-decimal, advanced-numbers-how-to-add-decimal-numbers, advanced-numbers-how-to-subtract-decimal-numbers, advanced-numbers-how-to-multiply-decimal-numbers, advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number, measurement-time, measurement-how-to-add-and-subtract-time |
| D7 recommendation | number-sense-how-to-compare-two-or-more-values |
| D8 cutting efficiency (min/m^2) | advanced-numbers-how-to-divide-decimal-numbers, advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number, number-sense-how-to-compare-two-or-more-values |

## LEARNING GOAL CHECK

```
deliverables: 8    claimed skills: 35    new_coverage: 4
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each mapping** ("could a competent student produce this deliverable
without ever performing this skill?"):

- D1 cannot be produced without drawing a labeled net (`geometry-net`), correctly identifying
  which shape is `2-dimensional`/`3-dimensional`, and naming/measuring a circle's `radius`/
  `diameter` and the turbine disk's `triangle`/`equilateral-triangle`/`square`/`rectangle`/
  `polygon` parts — the deliverable literally is that labeling.
- D2 cannot be produced without computing a circle's `circumference` (O-ring, twice) and a
  polygon's `perimeter` (turbine disk teeth), both of which require `pi` for the circular parts.
- D3 cannot be produced without converting a distance and a rate into an elapsed time
  (`measurement-time`, `elapsed-time`, `add-and-subtract-time`) via decimal division.
- D4 cannot be produced without `area` of a circle (annulus), a triangle (each tooth), and a
  rectangle/square (disk core), then expressing the part's share of the sheet as a `percent`.
- D5 cannot be produced without multiplying parts-per-sheet by sheets-per-week (itself a division
  of weekly minutes by cycle time) — pure decimal multiplication/division at real stakes.
- D6 cannot be produced without the full decimal arithmetic chain (add material + labor + bending,
  subtract from sell price, convert profit to a `percent` margin) and dividing machine cost by
  weekly profit to get an elapsed `time` (weeks) to break even.
- D7 cannot be produced without literally setting the two options' numbers side by side and
  judging which is larger on 3+ axes — `number-sense-how-to-compare-two-or-more-values`.
- D8 cannot be produced without dividing D3's time by D4's area (division of decimals) and
  expressing the two components' gap as a percent — the deliverable is a division-then-percent
  calculation by construction.

No skill in `standards[]` is unreached: every one of the 35 ids appears in at least one row above,
and none was added "because it sounds related" — each was checked against a specific line in a
specific deliverable before being kept. Skills present in the legacy tag set but **not** kept
(e.g. `basic-operations-*` single/multi-digit arithmetic, `number-sense-shape`/`triangle`/
`rectangle`/`square`/`circle` as bare vocabulary, `statistics-and-probability-histogram`/
`pie-chart`, `measurement-rounding`/`estimating`, `measurement-currency`, `measurement-unit`) were
cut because no Challenge-3 deliverable forces them specifically — they are either subsumed by a
more advanced skill this case does force (e.g. multi-digit multiplication is subsumed by decimal
multiplication) or genuinely untouched by any deliverable (no histogram or pie chart is required
anywhere in Challenge 3).

`new_coverage[]` has 4 entries: `geometry-vertex`, `geometry-concave`, `geometry-irregular-polygon`,
`geometry-quadrilateral`. All four had `n == 0` in the spine before this conversion (verified
directly against `readmodel/standards_spine.json`) and are genuinely forced by D1's labeling
requirement on the turbine disk's real, given shape (Appendix C) — not padding. The other 31 ids
were already tagged `n > 0` (Airplane Manufacturer already appeared in each one's `covered_by[]`
before this conversion) and are reported as such, not claimed as new.
