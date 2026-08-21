# Learning Goals — Urban Planner

Bidirectional deliverable ↔ skill matrix (case-write §10, LEARNING GOAL CHECK).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 distance-and-access map | geometry-coordinate-plane, geometry-x-axis, geometry-y-axis, geometry-origin, geometry-quadrant, geometry-coordinate-pair-also-ordered-pair, geometry-how-to-graph-a-coordinate-pair-on-the-coordinate-plane, geometry-how-to-find-the-distance-between-two-coordinate-pairs-on-a-coordinate-plane, geometry-pythagorean-theorem, geometry-right-triangle, geometry-hypotenuse, geometry-parallel-lines, geometry-perpendicular-lines, measurement-distance |
| D2 site area & estimated-capacity table + convex/concave classification | geometry-area, geometry-how-to-find-the-area-of-a-rectangle, geometry-convex, measurement-how-to-convert-an-amount-with-compound-units, measurement-ratio, measurement-proportion, measurement-how-to-find-a-missing-amount-in-a-proportion, advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number |
| D3 cost table (build-out + transportation + cost/resident) | advanced-numbers-how-to-multiply-decimal-numbers, measurement-how-to-convert-an-amount-from-one-unit-to-another-unit, measurement-how-to-round-a-number-to-a-specified-place-value, basic-operations-how-to-add-multi-digit-numbers, advanced-numbers-how-to-find-the-percent-of-a-number |
| D4 weighted-criteria decision matrix | advanced-numbers-percent, advanced-numbers-how-to-convert-numbers-to-percents, advanced-numbers-how-to-find-the-percent-of-a-number |
| D5 original visual display | number-sense-bar-graph |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 28    new_coverage: 3 (geometry-parallel-lines, geometry-perpendicular-lines, geometry-convex)
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forces test applied to each new_coverage skill (the strict test: could a competent student
produce this deliverable correctly without ever performing this skill?):**

- `geometry-parallel-lines` / `geometry-perpendicular-lines` — D1's coordinate-distance computation
  models the real straight-line distance from City Hall to each site by decomposing it into an
  east-west leg and a north-south leg that meet at a right angle — case.md's Appendix B explicitly
  points out that this mirrors Portland's own real street grid, where the numbered avenues run
  parallel to each other and meet the east-west streets at right angles (perpendicular). A student
  cannot explain *why* the Pythagorean/distance-formula approach is a valid model of this real city
  without identifying which lines are parallel to which, and which meet at a right angle. No, a
  student cannot skip this and still produce a correct, defensible D1.
- `geometry-convex` — D2 explicitly requires classifying each site's combined boundary as convex or
  concave and explaining how that classification determines whether a single rectangle-area formula
  applies or the shape must be broken into pieces first. This is not decorative: Site A is two
  separately-named adjoining parcels (Westmoreland Park + Eastmoreland Golf Course) whose combined
  outline is not a simple rectangle, so the classification step is what justifies the area method
  the student actually uses. A student who skips this cannot defend their D2 area computation.

**Forces test applied to the other 25 (already-covered) skills:** every one is a load-bearing input
to its listed deliverable's arithmetic — the coordinate-plane vocabulary (x-axis/y-axis/origin/
quadrant/coordinate pair) is what D1's plotted map is made of; area/rectangle-area and the
compound-unit conversion (acres → sq ft) are what D2's density scaling runs on; ratio/proportion
and its how-to are the exact operation D2 uses to translate Reedway's real density onto each
candidate site; percent and its how-tos appear in D2 (developed-footprint percent), D3 (rounding
dollar figures) and D4 (weight percentages, which must sum to 100%); the arithmetic how-tos
(multiply decimals, add multi-digit numbers, round to a place value) are D3's cost arithmetic; and
bar-graph is D5's required visual display.

**`new_coverage[]` is genuinely non-empty and not padded.** `geometry-parallel-lines`,
`geometry-perpendicular-lines` and `geometry-convex` all had `n == 0` in
`readmodel/standards_spine.json` at write time (verified via the case-write §1 spine-lock script),
and all three are forced by an actual deliverable per the forces test above — not added because
they "sound related." Every other claimed skill was already covered elsewhere in the corpus before
this conversion; none of the 28 is claimed without a deliverable that genuinely requires it. The
case-readiness Tier 1 legacy-conversion carve-out on T1-10 is not needed here since `new_coverage[]`
is non-empty on its own merits, but this case also carries `legacy_conversion_note` for the
unrelated reason that its premise, protagonist and site list are a legacy conversion.
