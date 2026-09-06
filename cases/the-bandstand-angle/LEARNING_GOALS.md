# Learning Goals — The Bandstand Angle

Bidirectional deliverable ↔ skill matrix. `case-write`, 2026-09-05.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — labeled plan-view sketch, correctly identified polygon type, every vertex marked | `geometry-octagon`, `geometry-hexagon`, `geometry-regular-polygon`, `geometry-irregular-polygon` |
| D2 — interior angles via the sum theorem (regular shortcut for A, given-five-find-sixth for B), convexity | `geometry-sum-of-the-interior-angles-of-a-polygon-theorem`, `geometry-how-to-find-the-measure-of-an-interior-angle-of-a-polygon-given-the-other-angles`, `geometry-convex` |
| D3 — hip-rafter run/rise/length at every vertex via the Pythagorean theorem | `geometry-pythagorean-theorem` |
| D4 — classify one roof panel's quadrilateral shape in each option | `geometry-quadrilateral`, `geometry-trapezoid` |
| D5 — full cost takeoff, covered sq ft per dollar, winner and margin | `advanced-numbers-how-to-multiply-decimal-numbers`, `advanced-numbers-how-to-divide-decimal-numbers`, `advanced-numbers-how-to-find-the-percent-of-a-number` (all already covered) |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 13    new_coverage: 0 (reinforcement pass — see case.json.reinforcement_note)
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each claimed skill** (*could a competent Hero produce the deliverable
correctly without ever performing this skill?*):

- `geometry-octagon`, `geometry-hexagon` — D1 requires correctly naming each frame's polygon type
  on the sketch; a Hero who cannot tell an 8-sided from a 6-sided polygon cannot complete D1.
- `geometry-regular-polygon`, `geometry-irregular-polygon` — D1 requires identifying WHICH option is
  regular and which is irregular, a distinction D2 and D3 both depend on (it is the entire reason
  Option A's angles/rafters are identical and Option B's are not).
- `geometry-sum-of-the-interior-angles-of-a-polygon-theorem` — D2 requires applying the theorem to
  find each polygon's interior-angle sum (1080° for the octagon, 720° for the hexagon) — not a term
  a Hero can satisfy by naming it, the deliverable requires the arithmetic application to both a
  regular and an irregular case.
- `geometry-how-to-find-the-measure-of-an-interior-angle-of-a-polygon-given-the-other-angles` — D2
  explicitly requires finding Option B's sixth, unsurveyed interior angle from the theorem plus the
  five given angles. This is the one skill the octagon's regular shortcut cannot substitute for —
  the deliverable is designed so a Hero who tries the shortcut on the irregular hexagon gets a
  demonstrably wrong answer (120° instead of the correct 100°).
- `geometry-convex` — D2 requires stating and justifying, from the interior angles just found,
  whether each frame is convex. A Hero cannot satisfy this by eyeballing the sketch; the
  justification must cite the angle values.
- `geometry-pythagorean-theorem` — D3 requires computing every hip rafter's length from its run and
  rise at every vertex (identical for Option A's 8, all different for Option B's 6) — direct,
  repeated application, not a term.
- `geometry-quadrilateral`, `geometry-trapezoid` — D4 requires identifying the four-sided roof-panel
  shape in each option and classifying it as specifically as the evidence allows (a plain
  quadrilateral is not enough; the deliverable asks for justification from congruent/non-congruent
  sides, which only resolves to "trapezoid" — and, for Option A, "isosceles trapezoid" — once D2's
  angle-parallelism reasoning and D3's rafter-length results are both in hand).

D5 intentionally claims no new-to-this-case skill — it is the case's real, load-bearing comparison
(the graded covered-square-feet-per-dollar verdict this case is built around) but exercises only
already-covered arithmetic (multiplication, division, percent), consistent with the
anti-inflation doctrine (same pattern as Roofline Call's D5).

No skill here is claimed on the strength of "the case is about roof frames generally" — each one
traces to a specific requirement in a specific deliverable. `case.json.reinforcement_note` records
that the only currently zero-coverage (n=0) skill in the entire Geometry domain
(`geometry-how-to-find-the-volume-of-a-sphere`) was checked and honestly ruled out — nothing in a
hip-and-flat-deck polygon roof frame forces sphere geometry, so `new_coverage[]` is genuinely empty
rather than padded.
