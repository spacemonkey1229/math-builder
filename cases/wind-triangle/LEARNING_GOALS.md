# LEARNING GOALS — Wind Triangle

Bidirectional deliverable ↔ skill matrix. Run per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 wind-vector table (magnitude/direction → components) | pre-calculus-vector, pre-calculus-magnitude-of-a-vector, pre-calculus-how-to-find-the-magnitude-and-direction-of-a-vector |
| D2 course unit-vector table | pre-calculus-unit-vector, pre-calculus-how-to-find-the-magnitude-and-direction-of-a-vector, geometry-pythagorean-theorem |
| D3 wind-component table (dot product along course) | pre-calculus-dot-product, pre-calculus-how-to-find-the-dot-product-of-two-vectors, pre-calculus-unit-vector |
| D4 wind-triangle diagram + ground-speed table | pre-calculus-how-to-add-and-subtract-vectors, pre-calculus-vector, pre-calculus-magnitude-of-a-vector, geometry-pythagorean-theorem, geometry-right-triangle |
| D5 trip fuel table + break-even | measurement-how-to-convert-an-amount-with-compound-units, advanced-numbers-how-to-find-the-percent-of-a-number |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 11    new_coverage: 7
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Forces test applied to each mapping** — *could a competent student produce this deliverable
correctly without ever performing this skill?*

- **D1 — no.** A meteorological wind is published only as a magnitude and a direction ("from 270 at
  90"). Producing the east/north component pair requires treating that pair as a *vector* and
  running the direction-and-magnitude → components conversion; there is no way to fill the
  component columns from the published table by copying. `pre-calculus-magnitude-of-a-vector` is
  forced in the reverse direction too: the student has to check that the components they wrote
  recover the published speed.
- **D2 — no.** The deliverable explicitly demands the *unit* vector for each course and the
  calculation showing its magnitude is exactly one. That calculation is
  √(east² + north²) = 1 — the Pythagorean theorem applied to a right triangle of components.
  A student who writes down the course bearing and stops has not produced the artifact.
- **D3 — no.** The along-course wind component is the dot product of the wind vector with the
  course unit vector, and this is the one step in the case that cannot be faked: the raw wind
  speed is *not* the headwind, and the difference between them is exactly the projection the dot
  product computes. The crosswind column forces the student to notice that the wind vector
  decomposes into two pieces relative to the course, which is what makes `pre-calculus-unit-vector`
  load-bearing here rather than decorative.
- **D4 — no.** The ground vector is literally the sum of the air vector and the wind vector; the
  deliverable asks for that sum drawn head to tail *and* its magnitude reported as ground speed.
  A student cannot produce a labeled, to-scale wind triangle without performing vector addition,
  and cannot get the ground speed out of it without the right-triangle relationship
  √(TAS² − crosswind²) that closes the triangle.
- **D5 — no.** Leg time comes from nautical miles ÷ knots and leg fuel from hours × pounds-per-hour;
  the final metric is pounds per nautical mile. Every one of those is a compound-unit conversion,
  and getting the units wrong is the most common way this deliverable fails. The break-even
  question ("by what percentage would the forecast headwind have to be wrong…") is a
  percent-of-a-number computation on a quantity the student derived rather than read.

## Skills deliberately NOT claimed

- **`pre-calculus-how-to-find-the-angle-between-two-vectors`-style trigonometric identity skills**
  are not claimed: this case's dot products are computed from components, not from
  |a||b|cos θ, so the angle-between formulation is never forced.
- **Pre-Calculus / Trigonometric Functions** (the group `tide-window` targets) is *touched* —
  converting a bearing to components uses sine and cosine — but is **not claimed**, in either
  `standards[]` or `new_coverage[]`. The case does not force the unit circle, radian measure,
  amplitude, or period, and claiming that group here would inflate coverage on the strength of two
  calculator keystrokes. That group is closed by `tide-window`, which genuinely forces it.

## Already-covered skills also exercised, not claimed in `new_coverage[]`

`geometry-pythagorean-theorem` (n=3), `geometry-right-triangle` (n=3),
`measurement-how-to-convert-an-amount-with-compound-units` (n=6),
`advanced-numbers-how-to-find-the-percent-of-a-number` (n=22).

## Gap group closed

`Pre-Calculus / Vectors` — **7 of 7 skills, the entire group**, all at `n = 0` in
`readmodel/standards_spine.json` at authoring time (`readmodel/gap_queue.json`: `n_gap: 7`,
`n_total: 7`). No partial claim, no split with a second case.
