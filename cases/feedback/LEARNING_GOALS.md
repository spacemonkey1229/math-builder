# LEARNING GOALS — Feedback

Bidirectional deliverable ↔ skill matrix. Run per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 rectangular→polar conversion table (both wedges) | pre-calculus-polar-coordinate, pre-calculus-how-to-convert-a-point-between-rectangular-and-polar-coordinates |
| D2 cardioid polar-equation graph, both wedge angles marked | pre-calculus-how-to-graph-a-polar-equation, pre-calculus-polar-coordinate |
| D3 parametric equations of the cross, eliminate the parameter, sightline crossing | pre-calculus-parametric-equation, pre-calculus-parameter, pre-calculus-how-to-eliminate-the-parameter-to-find-a-rectangular-equation |
| D4 gain-before-feedback table at every checked blocking moment | pre-calculus-how-to-convert-a-point-between-rectangular-and-polar-coordinates, pre-calculus-parametric-equation |
| D5 final decision table: worst-case GBF per wedge and the margin | pre-calculus-polar-coordinate, pre-calculus-parametric-equation |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 6    new_coverage: 6
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Forces test applied to each mapping** — *could a competent student produce this deliverable
correctly without ever performing this skill?*

- **D1 — no.** Appendix A gives each wedge's position only as a rectangular (x, y) pair. There is
  no way to fill the r/θ columns without running the rectangular→polar conversion, and the
  resulting (r, θ) pair *is* a polar coordinate — the deliverable cannot exist without the term
  and the how-to both firing.
- **D2 — no.** The deliverable explicitly demands a graph of Appendix B's polar equation over a
  full revolution, with both wedges' θ values (produced in D1) marked on the curve. A student who
  reports the two pattern-rejection numbers without ever plotting r(θ) has not produced a graph of
  a polar equation — they have evaluated a formula at two points, a different and lesser task.
- **D3 — no.** The deliverable requires the cross written as *x(t)* and *y(t)* — the parametric
  equations, with *t* named as the parameter — and then requires the parameter eliminated to reach
  a single rectangular equation. The follow-spot sightline crossing (y = 2) cannot be found without
  that rectangular equation existing first; a student who only evaluates x(t)/y(t) at the two given
  endpoints (which D4 also needs) has not produced the equation D3 asks for, and cannot answer the
  sightline question.
- **D4 — no.** Every cell of the GBF table needs a distance and an angle relative to the mic's
  fixed on-axis heading, for a mic position that is different at each of the three checked
  moments (verse, cross-start, cross-end) — the cross-start and cross-end positions are read
  directly off D3's parametric equations at t = 0 and t = T, and each one is then converted to
  polar coordinates exactly as in D1. A student cannot fill this table from Appendix A alone; the
  handheld moments require the parametric equations from D3.
- **D5 — no.** The recommendation depends on identifying, for each wedge, the single lowest GBF
  score across three moments that live in two different coordinate systems' worth of underlying
  work (a static polar-coordinate read for the verse, and two more polar-coordinate reads derived
  from D3's parametric path) — reusing both families of results directly, not decorative.

## Skills deliberately NOT claimed

- **Pre-Calculus / Trigonometric Functions** (`pre-calculus-sine-function`,
  `pre-calculus-cosine-function`, the unit-circle how-to, the amplitude/period how-to) is *touched*
  — the cardioid equation and the rectangular↔polar conversions both use cosine and, in a full
  solution, the arctangent relationship for θ — but is **not claimed**, in either `standards[]` or
  `new_coverage[]`. This case never asks a student to find an amplitude, a period, or a value on
  the unit circle in the way that group's own how-to skills describe; claiming it here would
  inflate coverage on the strength of a calculator cosine key. That group is closed by
  `tide-window`, which genuinely forces it.
- No logarithm-specific spine skill exists to claim or avoid — the dB formula
  (`−20·log₁₀(g(θ))`) is supplied and used as a given tool, the same way `wind-triangle` supplies
  the ground-speed formula without claiming a trigonometry-identity skill for deriving it.

## Already-covered skills also exercised, not claimed in `new_coverage[]`

None claimed as load-bearing beyond the six target skills; ordinary arithmetic (decibel formula
evaluation, distance formula) is used throughout but is not itself a distinct spine skill this
case forces in the sense `case-write`'s forces-test requires.

## Gap group closed

`Pre-Calculus / Polar And Parametric` — **6 of 6 skills, the entire group**, all at `n = 0` in
`readmodel/standards_spine.json` at authoring time (`readmodel/gap_queue.json`: `n_gap: 6`,
`n_total: 6`). No partial claim, no split with a second case.
