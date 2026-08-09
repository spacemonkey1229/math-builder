# Learning Goals — Tide Window

Bidirectional deliverable ↔ skill matrix. `case-write`, 2026-08-01.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — worked angle table (degrees→radians, reference angle, sin/cos/tan via unit circle, per key clock time) | `pre-calculus-radian`, `pre-calculus-unit-circle`, `pre-calculus-reference-angle`, `pre-calculus-sine-function`, `pre-calculus-cosine-function`, `pre-calculus-tangent-function`, `pre-calculus-how-to-convert-between-degrees-and-radians`, `pre-calculus-how-to-find-the-sine-cosine-and-tangent-of-an-angle-using-the-unit-circle` |
| D2 — stated sine/cosine tide model (amplitude, period, fitted to Appendix A) | `pre-calculus-amplitude`, `pre-calculus-period-of-a-function`, `pre-calculus-how-to-find-the-amplitude-and-period-of-a-sine-or-cosine-function` |
| D3 — under-keel clearance table (D2's model evaluated at D1's times) | `pre-calculus-sine-function`, `pre-calculus-cosine-function` (reused — evaluating the fitted model, not a new skill) |
| D4 — storm-surge sensitivity check (D2's model under the Appendix D adjustment range) | `pre-calculus-amplitude`, `pre-calculus-period-of-a-function` (reused — re-evaluating the model under a shifted parameter) |

## LEARNING GOAL CHECK

```
deliverables: 4    claimed skills: 11    new_coverage: 11
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each skill** (*could a competent Hero produce the deliverable correctly
without ever performing this skill?*):

- `radian` / `how-to-convert-between-degrees-and-radians` — D1's angle table is built directly in
  radians for the sine/cosine model; a Hero who never converts cannot fill the table. Forced.
- `unit-circle` / `how-to-find-the-sine-cosine-and-tangent-...-unit-circle` — this spine skill is
  authored as one combined how-to ("find the sine, cosine, *and* tangent... using the unit
  circle"); D1 explicitly asks for all three ratios at the reference angle in one step, which is
  exactly this skill, not three separate ones bolted together. Forced.
- `reference-angle` — several of the case's key times fall outside the model's first "quadrant"
  of the tide cycle (the hours approaching and past the marginal low), so reducing to a reference
  angle is necessary to read the unit circle correctly, not decorative. Forced.
- `sine-function`, `cosine-function` — D1 requires evaluating both explicitly per time; D2's model
  is stated as one or the other (the Hero's choice, defensible either way — a real modeling
  decision, not a coin flip); D3 evaluates whichever was chosen. Forced by D1 regardless of D2's
  choice.
- `tangent-function` — forced only by D1 (see the combined-how-to note above); not needed
  elsewhere in the case, and not claimed elsewhere. This is the deliberate design choice flagged
  in the concept sheet (`cases/_concepts/CONCEPTS_precalc-calculus-discrete_2026-08-01.md`, C1) —
  tangent travels with sine/cosine in the spine's own how-to skill, so it is genuinely forced by
  the same step, not manufactured with an unrelated bearing/heading sub-task.
- `amplitude`, `period-of-a-function`, `how-to-find-the-amplitude-and-period-...` — D2 explicitly
  requires stating both, sourced from Appendix A's real harmonic data. Forced.

No skill here is claimed on the strength of "the case is about trigonometry generally" — each one
traces to a specific verb in a specific deliverable.
