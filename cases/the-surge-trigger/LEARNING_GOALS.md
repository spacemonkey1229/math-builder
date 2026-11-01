# Learning Goals — The Surge Trigger

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 differentiate I(t) via chain rule; solve for t_A; tangent line at t_A | calculus-how-to-use-the-chain-rule-to-differentiate-a-composite-function, calculus-how-to-find-the-equation-of-a-tangent-line-at-a-point |
| D2 build D(t)=I(t)·c(t); differentiate via product rule; solve for t_B | calculus-how-to-use-the-product-rule-to-differentiate-a-product-of-functions |
| D3 classify D(t)'s critical point as a local maximum; compare to I(t)'s behavior | calculus-local-maximum |
| D4 differentiate R(t)=D(t)/I(t) via quotient rule; verify against c(t); compute lag/gap/cost | calculus-how-to-use-the-quotient-rule-to-differentiate-a-quotient-of-functions |
| D5 written recommendation citing D3's finding | calculus-local-maximum, calculus-how-to-use-the-chain-rule-to-differentiate-a-composite-function, calculus-how-to-use-the-product-rule-to-differentiate-a-product-of-functions |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced without recognizing I(t)=I0·e^(kt) as a composite function (outer e^u, inner u=kt) and correctly applying the chain rule to get I'(t)=I0·k·e^(kt) — a student who guesses I'(t)=I0·e^(kt) (forgetting the inner-derivative factor of k) has not performed the chain rule and will get the wrong t_A. The tangent-line equation at t_A requires the how-to's own point-slope procedure using I(t_A) and I'(t_A) as the point and slope. Genuinely forces `chain-rule` and `tangent-line-at-a-point`.
- **D2** requires recognizing D(t)=I(t)·c(t) as a genuine product of two DIFFERENT functions of t (not a constant times a function) and correctly applying the product rule — a student who treats c(t) as a constant (differentiating only I(t)) produces a structurally wrong D'(t) and a wrong t_B. Genuinely forces `product-rule`.
- **D3** requires actually locating D'(t)'s zero (from D2) and correctly classifying it as a local maximum via a sign argument (D'(t)>0 before, D'(t)<0 after) — a student who cannot correctly reason about the sign of the derivative on either side has not performed this deliverable, and the comparison to I(t)'s lack of a turning point requires understanding what "local maximum" actually means, not just naming the term. Genuinely forces `local-maximum`.
- **D4** requires the actual (D'I − DI')/I² setup of the quotient rule shown before simplification — a student who jumps straight to "R(t)=c(t)" without showing the quotient-rule mechanics has not completed the deliverable as specified, even if the final simplified answer is correct. Genuinely forces `quotient-rule`.
- **D5** requires citing D3's specific local-maximum finding (the reported curve turns over; the true curve does not, in this window) as the reason the "delayed copy" assumption is wrong — a student who writes a recommendation without referencing this specific asymmetry has not met the deliverable's own stated requirement, and the recommendation's underlying numbers depend on D1/D2's chain-rule and product-rule results. Genuinely forces `local-maximum` (as the citation target) plus reinforces `chain-rule`/`product-rule` as the numbers the recommendation must be built on.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 5    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

See `case.json.reinforcement_note` for the full accounting. Every one of the 5 claimed skills
(`calculus-how-to-use-the-chain-rule-to-differentiate-a-composite-function`,
`calculus-how-to-use-the-product-rule-to-differentiate-a-product-of-functions`,
`calculus-how-to-use-the-quotient-rule-to-differentiate-a-quotient-of-functions`,
`calculus-how-to-find-the-equation-of-a-tangent-line-at-a-point`, `calculus-local-maximum`) was
checked against `readmodel/standards_spine.json` before writing and every one sits at `n = 1` or
`n = 2`, not `n = 0` — this case reinforces a genuinely **thin** cluster spanning
Calculus/Derivatives and Calculus/Applications Of Derivatives rather than closing a true
zero-coverage gap. `new_coverage[]` is `[]`, honestly, per the reinforcement carve-out (T1-10,
`skills/case-readiness/SKILL.md`, 2026-08-17) — the same pattern used in
`cases/the-approval-gate/case.json` and `cases/the-two-offers/case.json`. Every one of the 5
skills is genuinely forced by at least one deliverable (see the matrix and check above), so
landing this case takes this thin cluster from n=1-2 to n=2-3 across the board.
