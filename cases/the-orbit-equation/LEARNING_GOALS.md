# Learning Goals — The Orbit Equation

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 rectangular-to-polar conversion of Option A's 8 waypoints | pre-calculus-polar-coordinate, pre-calculus-how-to-convert-a-point-between-rectangular-and-polar-coordinates |
| D2 graph both rigs' governing polar equations; check clipping | pre-calculus-how-to-graph-a-polar-equation, pre-calculus-polar-coordinate |
| D3 framing-and-compute-cost comparison, primary metric, margin | pre-calculus-polar-coordinate |
| D4 unit-circle camera-facing check | pre-calculus-unit-circle, pre-calculus-tangent-function, pre-calculus-how-to-find-the-sine-cosine-and-tangent-of-an-angle-using-the-unit-circle |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced without knowing what a **polar coordinate** is (the deliverable's entire output is a table of them) and without actually performing the **rectangular-to-polar conversion how-to** (r = sqrt(x²+y²), θ = atan2(y,x)) on each of the 8 given (x,y) waypoints. A student who eyeballs "yes, it looks like a circle" from the numbers without computing r for each point has not performed the how-to, and the deliverable explicitly requires showing conversion work for at least two waypoints. Genuinely forces `polar-coordinate` and the rect↔polar how-to.
- **D2** cannot be produced without treating r(θ) = 18 and r(θ) = 18 − 6 cos θ as **polar equations to graph** — a student who instead only plugs in the 8 sample angles from D1/D3 without producing an actual r-vs-θ plot over the full 0°–360° sweep has not performed **how to graph a polar equation** (the deliverable explicitly asks for a full-orbit graph, not just the sampled table). Finding the minimum radius and comparing it to Appendix C's clipping radius requires reading that graph (or the underlying polar-coordinate values) correctly. Genuinely forces `how-to-graph-a-polar-equation` and reinforces `polar-coordinate`.
- **D3** cannot be produced without repeatedly using each rig's **polar-coordinate** radius value r at each sampled angle (via Appendix D's framing formula, percent ≈ 300/r) — a student who does not correctly read/compute r at each of the 8 angles for each rig cannot produce a correct framing table, and therefore cannot produce a correct primary-metric ratio or margin. Reinforces `polar-coordinate` in a distinct, non-trivial application (using r as an input to a rate calculation, not just identifying or converting it).
- **D4** cannot be produced without using the **unit circle** to find exact sine, cosine, and tangent values at each of the 8 sampled angles (0°, 45°, 90°, …, 315° — all standard reference angles) — a student who uses a calculator for decimal approximations instead of exact unit-circle values (e.g. √2/2, not 0.7071) has not performed **how to find the sine, cosine, and tangent of an angle using the unit circle** as the deliverable explicitly requires ("not decimal approximations"). Identifying where **tangent** is undefined (90°, 270°, where cosine = 0) and explaining what that means physically for the camera's facing-direction code requires understanding the **tangent function** specifically, not just sine and cosine. Genuinely forces `unit-circle`, `tangent-function`, and the how-to.

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 6    new_coverage: 0 (see case.json.reinforcement_note)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

At case-write time (2026-09-18), a fresh read of `readmodel/standards_spine.json` found all 6 targeted
Pre-Calculus skills (3 from Polar And Parametric, 3 from Trigonometric Functions) already at **n=2**
(`covered_by` length 2), matching the concept sheet's own "remaining thin" framing
(`CONCEPTS_computer-graphics_2026-09-12.md`, C2) rather than a claim that they were at n=0 — the
concept sheet itself never claimed these were uncovered, only thin (per `readmodel/gap_queue.json`'s
`n<=2` threshold). Per the reinforcement carve-out (T1-10, `skills/case-readiness/SKILL.md`, "The
reinforcement carve-out on T1-10," added 2026-08-17), `new_coverage[]` is honestly recorded as
**empty** (per that carve-out's own mechanism) rather than padded with these still-thin (n=2), not
strictly zero, skills or with an unrelated, already-thicker skill. Every adjacent skill in both target groups, and in the related Vectors group this case's D4
also touches (vector, dot-product — already n=3), was checked and found already thicker (n>=3) than
the 6 skills this case actually targets — see `case.json.reinforcement_note` for the full per-skill
accounting. All 6 claimed skills are genuinely forced by the deliverables above (see the forces-test).
This project does not edit `readmodel/standards_spine.json` from `case-write` or `case-readiness`; the
live count should be re-verified at `case-publish` time before promotion.
