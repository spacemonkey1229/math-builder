# Learning Goals — The Painted Gallon

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 solved-dimensions sheet (sphere radius, cylinder height) | geometry-sphere, geometry-cylinder, geometry-radius, geometry-volume, geometry-how-to-find-the-volume-of-a-sphere, geometry-how-to-find-the-volume-of-a-cylinder |
| D2 idealized surface-area comparison table | geometry-surface-area, geometry-how-to-find-the-surface-area-of-a-cylinder, geometry-sphere |
| D3 steel-area-per-gallon rate | measurement-how-to-convert-an-amount-with-compound-units, geometry-surface-area, geometry-volume |
| D4 real cost-per-square-foot calculation | advanced-numbers-how-to-find-the-percent-of-a-number, geometry-surface-area |
| D5 lifecycle-cost visual + ballot recommendation | advanced-numbers-how-to-find-the-percent-of-a-number, measurement-how-to-convert-an-amount-with-compound-units |
| D6 fabricator-competition written response (added 2026-09-06, balance fix) | *(none, by design — see below)* |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** is impossible without correctly rearranging the sphere volume formula V = (4/3)·π·r³ to solve for r (the case's true-zero-coverage target skill), and separately rearranging the cylinder volume formula V = π·r²·h to solve for h given the real 60 ft diameter from Appendix C. A student who cannot isolate the cubed or squared radius term cannot produce a defensible dimension for either shape. Genuinely forces `sphere`, `cylinder`, `radius`, `volume`, the sphere volume how-to, and the cylinder volume how-to.
- **D2** requires applying the sphere surface-area formula (4·π·r²) and the cylinder surface-area formula (2·π·r² + 2·π·r·h) to the dimensions D1 produced — a student who instead reports D1's raw radius/height as if it were an area has not performed this deliverable. Genuinely forces `surface-area`, the cylinder surface-area how-to, and `sphere` (applying its area formula, distinct from its volume formula already forced in D1).
- **D3** requires converting a raw square-footage figure into a rate per 1,000 gallons — a compound-unit conversion, not a single-unit lookup — and cannot be produced by simply restating D2's totals. Genuinely forces the compound-units how-to, plus reapplying `surface-area` and `volume` as the two quantities being related.
- **D4** requires dividing Appendix B/C's two *different* sourced dollar figures by their two *different* sourced area figures and comparing the resulting rates — a student who instead compares the two raw capital-cost dollar totals without dividing by area has skipped the deliverable's actual arithmetic and cannot explain the true finding (the Spheroid costs more than twice as much per square foot to build). Genuinely forces the percent/rate-of-a-number how-to and `surface-area`.
- **D5** requires pulling Appendix D's two real per-gallon lifecycle figures forward into a genuine visual comparison and only then stating a single ballot dollar figure — the antecedent computation depends on D3/D4's rate work, and the deliverable specifically requires the *display* step plus a defensible one-number recommendation, not a pasted table. Genuinely forces the percent-of-a-number how-to (computing/comparing the two rates) and the compound-units how-to (the rate itself is a compound unit, USD per gallon).

- **D6** (added 2026-09-06, part of the case-readiness balance fix — see `case.json.readiness_revision_note`) deliberately claims **no** spine skill. It asks a Hero to weigh Appendix G's real, sourced fabricator-competition data against their own D5 dollar recommendation and defend a position — this is the case's non-cost balance axis (SPEC §2's "both options genuinely defensible" test), not a math-skill deliverable. Applying this same file's own "could a competent student produce this deliverable correctly without ever performing this skill?" test to any of standards[]'s math skills answers yes for D6, so claiming one would be exactly the fake mapping this test exists to catch. D6 is intentionally outside the deliverable↔skill matrix `new_coverage[]` accounting below.

```
LEARNING GOAL CHECK
  deliverables: 6    claimed skills: 10    new_coverage: 1
  UNMAPPED DELIVERABLES: D6 (by design -- reasoning/balance deliverable, claims no spine skill; see note above)
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

`geometry-how-to-find-the-volume-of-a-sphere` had `n=0` in `readmodel/standards_spine.json` at
write time (2026-09-05) — the last true zero-coverage skill in Geometry/Surface Area & Volume, per
the approved concept sheet. Every other claimed skill was checked against the spine before writing:
`geometry-how-to-find-the-surface-area-of-a-cylinder` (n=1), `geometry-how-to-find-the-volume-of-a-cylinder`
(n=1), `geometry-surface-area` (n=5), `geometry-volume` (n=2), `geometry-sphere` (n=1),
`geometry-cylinder` (n=1), `geometry-radius` (n=4), `measurement-how-to-convert-an-amount-with-compound-units`
(n=16), `advanced-numbers-how-to-find-the-percent-of-a-number` (n=71) — all reinforcement, correctly
excluded from `new_coverage[]`. No `geometry-how-to-find-the-surface-area-of-a-sphere` skill exists
in the spine at all (checked directly); D2's sphere-area work is instead mapped to the general
`geometry-surface-area` term plus `geometry-sphere`, which is the closest honest join available.
