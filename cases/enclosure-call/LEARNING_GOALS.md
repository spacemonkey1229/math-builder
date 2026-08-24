# Learning Goals — The Enclosure Call

Bidirectional deliverable ↔ skill matrix. Every Challenge-3 deliverable must map to a claimed
spine skill; every claimed skill must be forced by at least one deliverable.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — dimensioned, labeled diagram of each option | geometry-cone, geometry-sphere, geometry-3-dimensional, geometry-how-to-name-a-3-d-shape, geometry-radius |
| D2 — materials-cost table (surface area → material cost) | geometry-surface-area, geometry-pi, geometry-radius |
| D3 — packing-and-shipping table (packing efficiency → units/container → shipping cost) | advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number, geometry-cone, geometry-sphere |
| D4 — total-cost-per-unit comparison table and recommendation | advanced-numbers-percent, geometry-surface-area |

**"Forces" test applied to each row:**

- D1: a student cannot produce a correctly labeled diagram of Project Horn (a cone frustum) or
  Project Orb (a sphere) without correctly naming each as the specific 3-D shape it is — this is
  the vocabulary (Cone, Sphere, 3-Dimensional) and the procedure (how to name a 3-D shape) at
  once, not decoration. Marking radius on both shapes is load-bearing to every downstream
  calculation, so Radius is forced here too.
- D2: total exterior surface area of a cone frustum and of a sphere cannot be computed without
  using π and the radius measurements from D1 in the actual surface-area formulas — Surface Area,
  Pi, and Radius are all load-bearing to producing this table, not mentioned in passing.
- D3: converting a packing-efficiency figure (a percent, including the sphere's ≈74.05% Kepler
  ceiling) into units-that-actually-fit-per-container requires finding a percent of a number
  (container volume × packing efficiency); the table cannot exist without correctly identifying
  which enclosure is the cone frustum and which is the sphere, since the two packing-efficiency
  figures are shape-dependent.
- D4: rolling materials, tooling, and shipping into one total-cost-per-unit figure, then comparing
  Project Horn to Project Orb, is itself a percent-style comparison (expressing the gap as a share
  of the lower cost) built directly on D2's surface-area figures — a student who skipped D2 has no
  materials-cost line to put in this table.

**"Forces" test applied to each claimed skill:**

- geometry-cone / geometry-sphere: both are unavoidable in D1 (naming each shape) and D3
  (assigning the correct packing-efficiency figure to the correct shape) — a student cannot
  complete either deliverable without correctly identifying which option is which shape.
- geometry-3-dimensional: D1 requires the student to recognize and state that these are 3-D solids
  (not 2-D cross-sections) before a dimensioned diagram makes sense.
- geometry-how-to-name-a-3-d-shape: the specific how-to procedure D1 exercises directly — "cone
  frustum" and "sphere" are not guessable labels, they are named using this skill.
- geometry-surface-area / geometry-pi / geometry-radius: all three are load-bearing to D2's
  surface-area computation, which in turn is required input to D4's total-cost table.
- advanced-numbers-percent / advanced-numbers-how-to-find-the-percent-of-a-number: both are
  load-bearing to D3 (packing efficiency is expressed and used as a percent) and to D4 (the final
  cost comparison is expressed as a percentage margin).

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 9    new_coverage: 2
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```
