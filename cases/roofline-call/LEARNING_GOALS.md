# Learning Goals — Roofline Call

Bidirectional deliverable ↔ skill matrix. `case-write`, 2026-08-19.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — labeled framing sketch: vertex, ray, parallel lines, perpendicular lines | `geometry-vertex`, `geometry-ray`, `geometry-parallel-lines`, `geometry-perpendicular-lines` |
| D2 — birdsmouth plumb/level cut angles; verify complementary | `geometry-complementary-angles` |
| D3 — one acute angle, one obtuse angle, named vertex/rays | `geometry-acute-angle`, `geometry-obtuse-angle`, `geometry-vertex`, `geometry-ray` |
| D4 — hip bisection into adjacent angles, verify also complementary | `geometry-adjacent-angles`, `geometry-complementary-angles` |
| D5 — full framing takeoff, board-feet per sq ft, verdict | `advanced-numbers-how-to-multiply-decimal-numbers`, `advanced-numbers-how-to-divide-decimal-numbers`, `advanced-numbers-how-to-find-the-percent-of-a-number` (all already covered) |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 11    new_coverage: 7
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each new-coverage skill** (*could a competent Hero produce the
deliverable correctly without ever performing this skill?*):

- `geometry-ray` — D1 requires labeling at least one rafter as a ray on the sketch, and D3 requires
  naming the rays that form an acute/obtuse angle; a Hero who cannot identify a ray (a fixed
  starting point extending in one direction, matching a rafter's run from eave or corner toward the
  ridge) cannot complete either deliverable correctly.
- `geometry-vertex` — D1 requires marking the ridge vertex; D3 requires naming the vertex of each
  angle identified. Already partially covered elsewhere (`n=1`), so it is claimed in `standards[]`
  but **not** in `new_coverage[]` — it is still genuinely forced by D1/D3, just not new.
- `geometry-acute-angle`, `geometry-obtuse-angle` — D3 explicitly requires identifying one of each,
  computed from D2's real angle values (26.57° and 126.87°), not asserted from memory.
- `geometry-parallel-lines`, `geometry-perpendicular-lines` — D1 requires marking one real pair of
  each directly from that option's own framing plan (the ridge board runs parallel to the long
  walls; common rafters run perpendicular to the ridge in plan view) — a Hero who cannot tell
  parallel from perpendicular cannot label the sketch correctly.
- `geometry-complementary-angles` — D2 requires computing the plumb-cut and level-cut angles and
  showing they sum to 90°; D4 requires the same verification for the hip's two 45° angles. This is
  not a term a Hero can satisfy by naming it — the deliverable requires the arithmetic check.
- `geometry-adjacent-angles` — D4 explicitly requires showing the hip rafter's plan-view ray is the
  shared side of two angles that together make up the building's 90° corner — the defining property
  of adjacent angles, not just a label.

D5 intentionally claims no new skill — it is the case's real, load-bearing comparison (the actual
board-feet-per-square-foot verdict this case is built around) but exercises only already-covered
arithmetic (multiplication, division, percent), consistent with the anti-inflation doctrine.

No skill here is claimed on the strength of "the case is about roofs generally" — each one traces
to a specific requirement in a specific deliverable.
