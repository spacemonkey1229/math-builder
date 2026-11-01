# The Mooring Choice — Learning Goal Matrix

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Spar Design volume + steel surface area | geometry-how-to-find-the-surface-area-of-a-cylinder, geometry-how-to-find-the-volume-of-a-cylinder, geometry-how-to-find-the-volume-of-a-cone |
| D2 — Spherical Design volume + steel surface area, SA:V comparison | geometry-how-to-find-the-volume-of-a-sphere |
| D3 — Shared sinker volume, surface area, submerged weight | geometry-how-to-find-the-surface-area-of-a-pyramid, geometry-how-to-find-the-volume-of-a-pyramid |
| D4 — Materials cost table (steel, concrete, ballast) | geometry-how-to-find-the-surface-area-of-a-cylinder, geometry-how-to-find-the-surface-area-of-a-pyramid |
| D5 — Net-buoyant-lift-per-dollar results table and recommendation | geometry-how-to-find-the-volume-of-a-cylinder, geometry-how-to-find-the-volume-of-a-cone, geometry-how-to-find-the-volume-of-a-sphere, geometry-how-to-find-the-volume-of-a-pyramid |

## Bidirectional check

**Claimed skills (standards[]), 8 total:**

geometry-how-to-find-the-surface-area-of-a-cylinder, geometry-how-to-find-the-volume-of-a-cylinder, geometry-how-to-find-the-volume-of-a-cone, geometry-how-to-find-the-volume-of-a-sphere, geometry-how-to-find-the-surface-area-of-a-pyramid, geometry-how-to-find-the-volume-of-a-pyramid, geometry-surface-area, geometry-volume

(`geometry-surface-area` and `geometry-volume` are the two vocabulary terms Appendix F lists
alongside the six how-to skills — added to `standards[]` after Tier 1's T1-07 check flagged them
as final-appendix labels with no matching claimed skill. Every deliverable D1-D4 literally computes
a volume and/or a surface area, so both terms are forced exactly as directly as the how-to skills
that compute them.)

Every one of the 6 appears in at least one deliverable's skill list above:

- **Surface area of a cylinder** — D1 forces it directly (the Spar's exposed steel), and D4 re-uses that same figure to compute steel cost — not a decorative repeat, D4's cost table cannot be built without it.
- **Volume of a cylinder / volume of a cone** — D1's Spar volume is a cylinder-plus-cone sum, and D5's net-lift figure re-derives displaced seawater from that same volume — a student cannot reach D5's ratio without having done D1's volume work correctly first.
- **Volume of a sphere** — D2 is not solvable without it: the Spherical Design's entire buoyant-volume and steel-surface-area argument depends on it, and D5 reuses the result.
- **Surface area of a pyramid / volume of a pyramid** — D3 requires both directly (the shared sinker's steel-form/concrete-surface estimate and its concrete volume), and D4's concrete cost line depends on D3's volume result.

A student cannot produce any of D1–D5 correctly by narrating around the geometry — each deliverable's own numeric answer is the geometry.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 8    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Note on new_coverage: 0.** See `case.json`'s `reinforcement_note` — all 6 skills the originating concept sheet (`CONCEPTS_oceanography_2026-09-11.md`, C3) scored as prospective new coverage show `n=2` on the live spine as of this write (each already covered by two other cases), matching the concept sheet's own count exactly — no drift occurred between concept-sheet time and write time. None pass the strict `n==0` test for `new_coverage[]`. Per established project precedent (`cases/pixel-snap/case.json`, `cases/the-repeat-match/case.json`), this ships as a **reinforcement** case — a third real data point on Geometry/Surface Area And Volume's six named skills — with `new_coverage[]` correctly empty rather than a forced false claim. Flagged for the human sign-off SPEC §7 implies, not silently resolved.
