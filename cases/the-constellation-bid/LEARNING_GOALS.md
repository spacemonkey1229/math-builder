# Learning Goal Check — Constellation Bid

Bidirectional deliverable ↔ skill matrix (SPEC §1.5 item 3 / case-write §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — unit-circle trig table | pre-calculus-unit-circle, pre-calculus-tangent-function, pre-calculus-how-to-find-the-sine-cosine-and-tangent-of-an-angle-using-the-unit-circle, pre-calculus-sine-function, pre-calculus-cosine-function, pre-calculus-radian, pre-calculus-how-to-convert-between-degrees-and-radians |
| D2 — arc-length table | geometry-circumference, geometry-how-to-find-the-measure-of-the-circumference-of-a-circle |
| D3 — delta-v and propellant feasibility table | pre-calculus-how-to-find-the-sine-cosine-and-tangent-of-an-angle-using-the-unit-circle |
| D4 — cost-and-coverage decision memo | measurement-ratio |

## Forces test

*"Could a competent student produce this deliverable correctly without ever performing this skill?"*

- **D1** cannot be produced without literally locating six angles on the unit circle and reading off their sine, cosine, and tangent — that is the how-to skill's exact scope, and the term "unit circle" is what the diagram literally is. "Tangent function" is required because D1 explicitly asks for tangent, not just sine/cosine. "Sine function"/"cosine function" are the vocabulary naming what's being computed. Every angle starts in degrees (Appendix B) and must be converted to radians before any unit-circle computation is meaningful — that forces radian and the degree-to-radian how-to directly.
- **D2** cannot be produced without finding the orbital circumference and using it to convert an angle into a physical arc-length distance — that is the circumference how-to's exact scope, and nothing else in the case computes a distance around the orbit.
- **D3** cannot be produced without the sine values D1 already found — the combined plane-change formula (Appendix C) is literally `2v·sin(Δθ/2)`, so a student who has not found sin(Δθ/2) via the unit circle cannot compute a single group's delta-v. This deliverable is the case's real payoff for D1's trig work, not a separate skill.
- **D4** cannot be produced without computing satellites-correctly-placed ÷ total dollars for each option and comparing the two resulting numbers — that is literally forming and comparing a ratio, and nothing in D4 can be completed by comparing raw totals alone (the whole point of the primary metric is that it is a per-dollar rate, not a total).

## Report

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 10    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**new_coverage[] is empty by design, not by omission** — see `case.json`'s `reinforcement_note`. A live check of `readmodel/standards_spine.json` on 2026-09-18 found zero skills anywhere at true `n==0`; three of the ten claimed skills (`pre-calculus-unit-circle`, `pre-calculus-tangent-function`, and their shared how-to) are still the thinnest skills in their group, at `n=2` each, and this case is exactly the kind of reinforcement the concept sheet (`cases/_concepts/CONCEPTS_spaceflight_2026-09-12.md`) recommended.
