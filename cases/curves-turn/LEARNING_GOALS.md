# LEARNING GOALS — The Curve's Turn (`curves-turn`)

Bidirectional deliverable ↔ spine-skill matrix, per `skills/case-write/SKILL.md` §10.
Every id below was resolved verbatim against `readmodel/standards_spine.json` before this file was
written; all thirteen carried `n == 0` at write time, so all thirteen are `new_coverage[]`.

**Target gap group:** `Calculus / Applications Of Derivatives` — all 7 skills, the complete group.
**Secondary (partial):** `Calculus / Derivatives` — 6 of that group's 9 skills. The chain, product
and quotient rules are deliberately **not** claimed: the case's models of record are polynomials,
so no deliverable forces a composite, product or quotient derivative, and claiming them would mark
three gaps closed that no Hero ever touched.

## The matrix

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 model-and-derivative worksheet | `calculus-how-to-find-a-derivative-using-the-power-rule`, `calculus-derivative`, `calculus-instantaneous-rate-of-change`, `calculus-differentiable` |
| D2 tangent-line projection | `calculus-tangent-line`, `calculus-how-to-find-the-equation-of-a-tangent-line-at-a-point` |
| D3 previous-wave critical-point table | `calculus-how-to-find-critical-points-of-a-function`, `calculus-how-to-use-the-first-derivative-test-to-classify-a-critical-point`, `calculus-critical-point`, `calculus-local-maximum`, `calculus-local-minimum` |
| D4 concavity sign chart | `calculus-concavity` |
| D5 retrospective closure optimisation | `calculus-how-to-solve-an-optimization-problem-using-derivatives` |
| D6 decision table | `calculus-instantaneous-rate-of-change`, `calculus-concavity` |

## Why each mapping survives the "forces" test

The test is strict: *could a competent Hero produce this deliverable correctly without ever
performing this skill?* If yes, the mapping is fake and the row comes out.

- **D1 → power rule / derivative.** D1 asks for the derivative of the fitted cubic written out term
  by term. There is no other route to it at this band.
- **D1 → instantaneous rate of change.** D1 explicitly asks for the derivative's *value at the
  decision week*, in cases per week per week, and for one sentence separating it from the average
  rate of change over the last two reported weeks. A Hero who never distinguishes the two cannot
  write that sentence.
- **D1 → differentiable.** D1's closing note asks why the reported step series is not
  differentiable at its own data points. The term is the answer, not decoration.
- **D2 → tangent line / equation of a tangent line.** D2 asks for the line's equation, drawn, and
  then used to project a crossing week. Nothing else produces it.
- **D3 → critical points / first derivative test / local max / local min.** D3 asks for *every*
  critical point of the previous wave's model inside its window and a classification of each. That
  window contains one local minimum and one local maximum, so both terms are exercised, and the
  classification is what the first derivative test is for.
- **D4 → concavity.** D4 is a second-derivative sign chart and the week the sign changes. This is
  the case's title move and the whole of Option A's argument.
- **D5 → optimisation using derivatives.** D5 requires an objective function, its derivative, the
  critical point, and a first-derivative-test confirmation that the critical point is a maximum.
  It cannot be produced by inspection: the objective is a sum of two shifted cubics.
- **D6 → instantaneous rate of change + concavity.** D6 does not merely total two columns. It
  requires the model's rate of change at the first and last week of each plan's closure window, and
  an explanation of the size of the gap between the two plans in terms of the curve's concavity
  over those windows. A Hero who skips both produces two numbers and no argument.

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 6    claimed skills: 13    new_coverage: 13
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  PHANTOM SKILLS (forced by a deliverable but not claimed in standards[]): none
  RESULT: PASS
```

## Coverage effect if this case publishes

| Group | Skills in group | Claimed here | Group closed? |
|---|---|---|---|
| Calculus / Applications Of Derivatives | 7 | 7 | **yes — full group** |
| Calculus / Derivatives | 9 | 6 | no — chain, product and quotient rule remain open |

The three Derivatives skills left open are a real, deliberate residue and are recorded as such, not
quietly absorbed. A later case that models a quantity as a genuine product or composite of two
functions would close them honestly.
