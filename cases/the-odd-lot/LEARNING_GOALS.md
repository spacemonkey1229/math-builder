# Learning Goals — The Odd Lot

Bidirectional deliverable ↔ skill matrix (case-write §10, MCS-10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Parcel classification + missing-angle calculation | geometry-polygon, geometry-irregular-polygon, geometry-convex, geometry-concave, geometry-sum-of-the-interior-angles-of-a-polygon-theorem, geometry-how-to-find-the-measure-of-an-interior-angle-of-a-polygon-given-the-other-angles |
| D2 — Option A buildable-footprint table | geometry-area, geometry-perimeter, measurement-ratio, measurement-proportion |
| D3 — Option B buildable footprint + octagon plaza area | geometry-regular-polygon, geometry-how-to-find-the-area-of-a-regular-polygon, geometry-octagon, geometry-area |
| D4 — Dwelling-unit-years comparison, percent margin | measurement-ratio, measurement-proportion, advanced-numbers-how-to-find-the-percent-of-a-number |
| D5 — Written reflection (Population) | statistics-and-probability-population, geometry-irregular-polygon |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 15    new_coverage: 0 (reinforcement_note on file)
UNMAPPED DELIVERABLES: none — every deliverable (D1-D5) maps to at least one skill.
UNREACHABLE SKILLS: none — every claimed skill in standards[] is forced by at least one deliverable:
  polygon                          -> D1 (classification table)
  irregular-polygon                -> D1, D5 (classification; the reflection is explicitly ABOUT irregular parcels)
  convex                           -> D1 (two of the three parcels are classified convex)
  concave                          -> D1 (identifying L2 and its notch is the deliverable's explicit ask)
  regular-polygon                  -> D3 (the plaza; and Option B's consolidated lot is contrasted as NOT itself a regular polygon)
  sum-of-interior-angles theorem   -> D1 (the missing-angle calculation cannot be done without it)
  how-to-interior-angle-given-others -> D1
  how-to-area-of-a-regular-polygon -> D3 (the octagon plaza's area calculation)
  octagon                          -> D3 (the plaza is explicitly named and shaped as a regular octagon)
  area                             -> D2, D3 (every buildable-footprint and plaza-area calculation)
  perimeter                        -> D2 (rear/notch lot-line length is a perimeter quantity; the octagon's perimeter feeds its area formula in D3)
  ratio                            -> D2, D4 (buildable-footprint percentage; FAR itself is a ratio)
  proportion                       -> D2, D4 (same calculations, proportion framing)
  how-to-percent-of-a-number       -> D4 (the percent margin calculation)
  population                       -> D5 (explicitly required term)
RESULT: PASS
```

"Forces" test applied per case-write §10: could a competent student produce each deliverable
correctly without ever performing the named skill? For every row above, no — D1 cannot classify
the parcels or find L1's missing angle without the polygon vocabulary and the interior-angle
theorem; D3 cannot compute the plaza's area without the regular-polygon area formula and correctly
identifying it as an octagon; D4's margin cannot be stated without the percent-of-a-number
procedure; D5 cannot be written correctly without using Population as required.
