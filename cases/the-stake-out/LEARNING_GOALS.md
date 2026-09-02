# The Stake-Out — Learning Goal Matrix

Bidirectional check between Challenge 3 deliverables and claimed spine skills (`case-write`
SKILL.md §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — angle diagram, unobstructed corner (backsight ray, deflection angle, classification) | `geometry-ray`, `geometry-degree`, `geometry-acute-angle`, `geometry-obtuse-angle`, `geometry-right-angle` (the backsight-to-corner sightline is a ray; the turned deflection angle is measured in degrees and must be classified as acute, obtuse, or right — a student cannot correctly draw and label this diagram without naming what a ray is or classifying the angle) |
| D2 — second-setup diagram, obstructed corner (relocated baseline as a transversal, every angle pair at the crossing) | `geometry-transversal-line`, `geometry-vertical-angles`, `geometry-adjacent-angles`, `geometry-supplementary-angles`, `geometry-complementary-angles`, `geometry-how-to-find-angle-measures-of-intersecting-lines` (the relocated baseline crossing the original is a transversal; labeling every angle pair the crossing produces requires identifying vertical, adjacent, supplementary, and complementary pairs and computing their measures at an intersection) |
| D3 — worked angle-measure calculation proving the relocated baseline is parallel | `geometry-how-to-find-angle-measures-given-parallel-lines-a-transversal-line-and-at-least-one-an` (this is the one skill whose test is literally "given parallel lines, a transversal, and one angle measure, find the others" — D3 is that calculation, applied to verify the new baseline) |
| D4 — congruence check, polar-staked point vs. GNSS-staked point | `geometry-fundamentals-of-geometry-congruent` (the deliverable is explicitly a congruence judgment between two triangles built from each method's marked point, the reference point, and the design point) |
| D5 — accuracy-margin table in mm vs. the ACI tolerance | `measurement-how-to-convert-an-amount-from-one-unit-to-another-unit`, `advanced-numbers-how-to-find-the-percent-of-a-number` (equipment specs are published in inches/arc-seconds while the tolerance standard is metric, forcing a real unit conversion; the tolerance itself is defined as "the greater of a fixed mm value or a percent of the dimension," forcing a percent-of-a-number calculation) |
| D6 — total-expected-time recommendation for the obstructed corners | `number-sense-how-to-compare-two-or-more-values` (recommending a method requires explicitly comparing the two methods' total-expected-time values against each other) |

## LEARNING GOAL CHECK

```
deliverables: 6    claimed skills: 16    new_coverage: 13
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forces test applied:** a competent student cannot produce D1 without naming a ray and
classifying an angle by degree measure; cannot produce D2 without correctly identifying a
transversal and every named angle-pair relationship it creates; cannot produce D3 without
applying the parallel-lines-transversal angle-measure procedure specifically (not just "an angle
fact," but the named parallel/transversal one); cannot produce D4 without making an explicit
congruence judgment; cannot produce D5 without converting units across an inch/mm boundary and
computing a percent of a dimension; cannot produce D6 without an explicit comparison between the
two methods' total-time figures. D6's skill was added at write time (rather than left unmapped)
so every deliverable has an honest forcing skill, consistent with how `cases/fret-board`'s D5
(its own synthesis deliverable) was handled.

## Coverage note

All 13 skills in `new_coverage[]` currently have `n == 1` in `readmodel/standards_spine.json`
(checked at write time, see `case.json`'s standards list) — every skill in the
Geometry/Fundamentals Of Geometry group that was sitting at single-case coverage before this case.
Three additional skills are claimed in `standards[]` but **not** in `new_coverage[]` because they
are already well-covered (round-out skills):
`measurement-how-to-convert-an-amount-from-one-unit-to-another-unit` (n=16) and
`advanced-numbers-how-to-find-the-percent-of-a-number` (n=59), per the concept sheet, plus
`number-sense-how-to-compare-two-or-more-values` (n=49), added at write time to give D6 an honest
skill mapping. 13 new-coverage skills is at the
coverage-inflation guard's ceiling (`skills/case-brainstorm/SKILL.md`: "a single 2–3 hour case
honestly exercises roughly 8–15 skills... more than 15 new skills, flag it") but does not exceed
it, and the concept sheet's own framing — this case exists specifically to close every skill
sitting at n=1 in one spine group in one reinforcement pass, exactly mirroring the C7/C8
precedent for their own groups — is the justification for claiming the full 13 rather than
splitting into two cases.
