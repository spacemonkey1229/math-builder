# Pixel Snap — Learning Goal Matrix

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Fast Lock coordinate-plane plot, translation vector, congruence check | geometry-transformation, geometry-translation, geometry-how-to-translate-a-figure-on-the-coordinate-plane, geometry-congruent |
| D2 — True Lock resampled plot, dilation scale factor, congruent-vs-similar argument | geometry-dilation, geometry-scale-factor, geometry-how-to-dilate-a-figure-on-the-coordinate-plane-given-a-scale-factor, geometry-similar, geometry-congruent |
| D3 — Reflection across the y-axis before overlay | geometry-how-to-reflect-a-figure-across-the-y-axis, geometry-transformation |
| D4 — Ground-control-point quadrant placement | geometry-quadrant, geometry-coordinate-plane, geometry-origin |
| D5 — Hectares-falsely-flagged-per-analyst-hour results table and recommendation | (primary-metric ratio deliverable — arithmetic only; forces no new spine skill beyond the geometry already produced in D1/D2) |

## Bidirectional check

**Claimed skills (standards[]), 12 total:**

geometry-congruent, geometry-similar, geometry-how-to-reflect-a-figure-across-the-y-axis, geometry-quadrant, geometry-transformation, geometry-translation, geometry-dilation, geometry-scale-factor, geometry-how-to-translate-a-figure-on-the-coordinate-plane, geometry-how-to-dilate-a-figure-on-the-coordinate-plane-given-a-scale-factor, geometry-coordinate-plane, geometry-origin

Every one of the 12 appears in at least one deliverable's skill list above (D1–D4). None is claimed decoratively:

- **geometry-congruent / geometry-similar** — D1 and D2 force the actual test (is the transformed polygon congruent or only similar to the original?), not a definition recital.
- **geometry-how-to-reflect-a-figure-across-the-y-axis** — D3 is not solvable without it: the ascending/descending pass mismatch (Appendix A) makes the reflection structurally necessary before D1/D2's overlay means anything.
- **geometry-quadrant / geometry-coordinate-plane / geometry-origin** — D4 requires placing a real point relative to a stated origin and naming its quadrant; a student cannot produce this deliverable by narrating around it.
- **geometry-transformation / geometry-translation / geometry-dilation / geometry-scale-factor** and their two how-to skills — D1 and D2's core arithmetic (the pixel-shift vector, the resampling scale factor) is exactly these skills, not adjacent to them.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 12    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Note on new_coverage: 0.** See `case.json`'s `reinforcement_note` — all 4 skills the originating concept sheet (`CONCEPTS_remote-sensing_2026-09-12.md`, C1) scored as prospective new coverage now show `n=2` on the live spine (each already covered by two other cases), so none pass the strict `n==0` test for `new_coverage[]`. This is not a defect unique to this case — `cases/the-repeat-match/case.json` documents the identical situation for the same spine group and the project's established resolution: ship the case as a **reinforcement** case (a third real data point on the group's remaining thin skills) with `new_coverage[]` correctly empty, rather than force a false claim to satisfy SPEC §7's "must be non-empty" line. Flagged for the human sign-off SPEC §7 implies, not silently resolved.
