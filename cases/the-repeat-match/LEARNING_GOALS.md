# Learning Goals — The Repeat Match

Bidirectional deliverable ↔ skill matrix. Every Challenge-3 deliverable must map to a claimed
spine skill; every claimed skill must be forced by at least one deliverable.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — front-panel registration-point diagram, both composition orders | geometry-transformation, geometry-rotation, geometry-reflection, geometry-clockwise, geometry-counter-clockwise, geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-counterclockwise, geometry-how-to-reflect-a-figure-across-the-y-axis |
| D2 — back-yoke diagram + 180° check against a third, rotated-only panel | geometry-how-to-reflect-a-figure-across-the-x-axis, geometry-how-to-rotate-a-figure-on-the-coordinate-plane-180-degrees, geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-clockwise |
| D3 — symmetry analysis of the master motif | geometry-symmetry, geometry-line-of-symmetry |
| D4 — repeat-tiling diagram, min and max printer repeat | geometry-translation, geometry-how-to-translate-a-figure-on-the-coordinate-plane |
| D5 — congruent-vs-similar comparison, dilation for a second printer | geometry-congruent, geometry-similar, geometry-dilation, geometry-scale-factor, geometry-how-to-dilate-a-figure-on-the-coordinate-plane-given-a-scale-factor, geometry-how-to-find-the-scale-factor-of-a-dilation |
| D6 — marker-layout cost comparison and final recommendation | geometry-transformation, geometry-rotation, geometry-reflection (restates, correctly, which composition order the recommendation depends on) |

**"Forces" test applied to each row:**

- D1: a student cannot plot the registration point through "rotate, then reflect" and "reflect,
  then rotate" without actually performing a rotation and a reflection, naming the rotation's
  direction (CCW, matching the marker's cutting-angle requirement), and recognizing both as
  transformations of the same starting figure. Reflecting the front panel is across the vertical
  center-front seam — the Y-axis in the panel's local coordinate system — which is exactly the
  How to reflect a figure across the Y-Axis procedure.
- D2: the back-yoke seam is horizontal, so its mirrored build reflects across the X-axis instead
  of the Y-axis — a different procedure a student cannot substitute the Y-axis one for and still
  get a correct diagram. The 180-degree check against a third panel that is "only rotated, never
  reflected" cannot be built without the 90-degrees-clockwise how-to (that third panel's own
  build) and the 180-degrees how-to (the comparison rotation).
- D3: a diagram "testing every candidate axis for a line of symmetry" is the definition of the
  Line Of Symmetry how-to-adjacent term applied directly; the written explanation of why none
  exists requires the student to state what Symmetry means and test the motif against it, not
  assert an answer.
- D4: tiling a motif "at fixed intervals across the printable fabric width" with "every
  translation vector labeled" cannot be produced without applying and labeling translations — this
  is the Translation how-to by definition, not an adjacent skill.
- D5: showing the on-printer copies are congruent to the master and to each other, while a
  resized copy for a second printer is similar rather than congruent, requires the student to
  correctly apply and distinguish Congruent from Similar; computing "that dilation's scale factor"
  cannot be done without both the Dilation how-to and the Scale Factor how-to, and the comparison
  cannot be drawn at all without first performing the dilation itself.
- D6: a student who does not correctly identify which composition order from D1 the
  Mirror-Match recommendation depends on has not actually completed this deliverable — restating
  it correctly requires re-applying the rotation/reflection/transformation vocabulary from D1 in
  the context of the final decision, not just repeating a sentence from earlier.

**"Forces" test applied to each claimed skill:**

- geometry-transformation / geometry-rotation / geometry-reflection: unavoidable in D1 (both
  composition orders are built from exactly these two transformation types) and restated
  correctly in D6's recommendation.
- geometry-clockwise / geometry-counter-clockwise: D1's rotation must be specified as
  counterclockwise (matching the marker's cutting-angle requirement); D2's third panel is rotated
  clockwise instead — a student who does not track the direction cannot correctly build either
  diagram or the how-to-rotate-a-figure-90-degrees-clockwise deliverable component.
- geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-counterclockwise /
  geometry-how-to-reflect-a-figure-across-the-y-axis: the two specific procedures D1's front-panel
  build is made of.
- geometry-how-to-reflect-a-figure-across-the-x-axis: the specific procedure D2's back-yoke build
  is made of (a horizontal seam, not a vertical one).
- geometry-how-to-rotate-a-figure-on-the-coordinate-plane-180-degrees /
  geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-clockwise: both load-bearing
  to D2's orientation check against the third, rotated-only panel.
- geometry-symmetry / geometry-line-of-symmetry: both load-bearing to D3, which exists
  specifically to test and explain the motif's asymmetry.
- geometry-translation / geometry-how-to-translate-a-figure-on-the-coordinate-plane: both
  load-bearing to D4's repeat-tiling diagram, which cannot be built without translating the motif
  across the printable width.
- geometry-congruent / geometry-similar / geometry-dilation / geometry-scale-factor /
  geometry-how-to-dilate-a-figure-on-the-coordinate-plane-given-a-scale-factor /
  geometry-how-to-find-the-scale-factor-of-a-dilation: all six load-bearing to D5, which is built
  specifically around the congruent-copies-vs-dilated-similar-copy contrast and the scale-factor
  computation that contrast depends on.

```
LEARNING GOAL CHECK
  deliverables: 6    claimed skills: 20    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Note on `new_coverage: 0`.** This is a deliberate second-pass/redundancy case, not a gap-closing
case. Every skill in Geometry/Transformations already has `n >= 1` coverage as of 2026-09-01 (14
skills at exactly `n=1`, 6 at `n=2` or `n=3` — see `case.json.reinforcement_note` and the group
table in `cases/_concepts/CONCEPTS_precal-second-pass_2026-08-30.md`, C10). The case exists to
reinforce a group where 14 of 20 skills sit at a single point of failure, closing all 20 skills in
the group in one pass rather than adding a skill that currently sits at `n=0`. This intentionally
does not satisfy the normal `new_coverage[] non-empty` validation check (SPEC §7) and that check is
expected to flag it — the exception is deliberate and directed, not an oversight.
