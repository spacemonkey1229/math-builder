# LEARNING GOALS — Tilt Decision

Bidirectional deliverable ↔ skill matrix. Run per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 degrees→radians conversion table | pre-calculus-radian, pre-calculus-how-to-convert-between-degrees-and-radians |
| D2 solar-position / unit-circle table | pre-calculus-unit-circle, pre-calculus-sine-function, pre-calculus-cosine-function, pre-calculus-tangent-function, pre-calculus-reference-angle, pre-calculus-how-to-find-the-sine-cosine-and-tangent-of-an-angle-using-the-unit-circle |
| D3 annual sinusoidal elevation graph | pre-calculus-amplitude, pre-calculus-period-of-a-function, pre-calculus-how-to-find-the-amplitude-and-period-of-a-sine-or-cosine-function |
| D4 efficiency table + weighted-annual comparison | pre-calculus-cosine-function |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 11    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Note on `new_coverage: 0`.** This is expected and correct for this case, not a defect. Per the
batch header in `cases/_concepts/CONCEPTS_precal-second-pass_2026-08-30.md`, this is a
**depth/redundancy batch**: every Pre-Calculus spine group, including Trigonometric Functions
(this case's target group), already sits at exactly one covering case (`tide-window`). This case
adds a **second** touch on the group so the weekly rotation has a fallback and no single case is a
single point of failure for the whole group. All 11 claimed skills already have `n >= 1` in
`readmodel/standards_spine.json` at authoring time — the concept sheet's own feasibility note flags
this explicitly, and the case is scored and greenlit on that basis, not on closing a zero-coverage
gap. `new_coverage[]` is therefore correctly left empty in `case.json`.

**Forces test applied to each mapping** — *could a competent student produce this deliverable
correctly without ever performing this skill?*

- **D1 — no.** Every published solar-position source in Appendix D reports elevation angle in
  degrees, and the deliverable explicitly demands both units side by side with the conversion
  arithmetic shown. A student cannot fill the radians column by copying — the conversion is the
  artifact.
- **D2 — no.** A solar azimuth is published as a compass-style bearing (degrees clockwise from
  true north), not as a standard mathematical angle. Turning it into one, finding the reference
  angle for whichever quadrant it lands in, and reading off sine, cosine, and tangent from the
  unit circle is the only way to produce the table — a student who just restates the published
  azimuth and elevation has not performed the deliverable. The reference-angle step is forced
  specifically by the afternoon and morning entries, whose azimuths (well past 180° in the
  afternoon case) do not sit in the first quadrant, so a student cannot get correct signs on
  sine/cosine/tangent without identifying which quadrant they are in and computing off the
  reference angle.
- **D3 — no.** The deliverable requires amplitude and period to be identified *from the data* and
  labeled on the graph, not asserted. A student who plots the twelve monthly elevation values
  without recognizing the curve as a sinusoid, and without extracting how far it swings from its
  midline (amplitude) and how long one full cycle takes (period — one year, but the student has to
  show that from the data, not assume it), has not produced the artifact.
- **D4 — no.** The angle-of-incidence relationship between a fixed tilt angle and a variable solar
  elevation angle is a cosine relationship (the fraction of direct sunlight a tilted plane
  actually intercepts falls off as the cosine of the angle between the panel's normal and the
  sun's ray). A student cannot produce a defensible monthly efficiency table, or reconcile it
  against Appendix B's modeled output, without computing that cosine for each month and each
  tilt option — restating Appendix B's PVWatts numbers without deriving them independently does
  not satisfy "checked for consistency." The weighted-annual half of D4 is arithmetic once the
  monthly figures exist, but it is inseparable from the cosine check that precedes it in the same
  deliverable.

## Skills touched but not claimed

The concept sheet (`CONCEPTS_precal-second-pass_2026-08-30.md`, C1) names two already-covered
skills the case "also exercises" without scoring them: a variable-substitution style skill,
exercised informally wherever a monthly rate multiplier is applied as a coefficient in D4's
weighted sum, and a unit-conversion-style sanity check, exercised wherever a student cross-checks
kWh totals. Neither concept-sheet description resolved to an exact, unambiguous id in
`readmodel/standards_spine.json` (the closest candidates —
`advanced-operations-variable` and the `Statistics And Probability/Algebra` group's
slope/linear-equation skills — do not match what is actually exercised here), so **neither is
added to `standards[]`**. Per `skills/case-write/SKILL.md`'s "Never claim a skill no deliverable
forces," an approximate or unverifiable id is not claimed; this case's `standards[]` is limited to
the 11 ids verified directly against the spine (see the verification run in the case-write
session).

## Gap group touched

`Pre-Calculus / Trigonometric Functions` — all 11 skills in the group, all already at `n >= 1` in
`readmodel/standards_spine.json` at authoring time (verified directly against the spine; see
counts in the case-write session's verification run). `tide-window` is the group's first covering
case (its own `case.json.new_coverage` claims all 11 of the same ids). This case is that group's
**second** touch — redundancy/depth work, not gap closure — per the batch header. Note:
`readmodel/gap_queue.json`'s entry for this group still reads `n_gap: 11, n_total: 11` as of this
writing, which is stale relative to `standards_spine.json`'s actual per-skill `n` counts (it has
not been regenerated since `tide-window` shipped); `standards_spine.json` is the authority this
skill's verification step uses, and it is what was checked here.
