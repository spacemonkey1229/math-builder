# LEARNING GOAL CHECK — The Locks Window

Bidirectional deliverable ↔ spine-skill matrix, per `case-write` SKILL.md §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Brewster-angle worksheet | `pre-calculus-inverse-trigonometric-function`, `pre-calculus-how-to-evaluate-an-inverse-trigonometric-function`, `geometry-angle` |
| D2 — rotation-angle solution worksheet | `pre-calculus-how-to-solve-a-trigonometric-equation-over-a-given-interval` |
| D3 — identity-verification worksheet | `pre-calculus-pythagorean-identity`, `pre-calculus-how-to-verify-a-trigonometric-identity` |
| D4 — percent-glare-removed comparison table | `advanced-numbers-how-to-find-the-percent-of-a-number` |
| D5 — original visual (Challenge 2b) | `pre-calculus-inverse-trigonometric-function`, `geometry-angle` |

## Reverse check — every claimed skill traced to a deliverable

| Skill id | Kind | Forced by |
|---|---|---|
| `pre-calculus-pythagorean-identity` | term | D3 |
| `pre-calculus-inverse-trigonometric-function` | term | D1, D5 |
| `pre-calculus-how-to-verify-a-trigonometric-identity` | how-to | D3 |
| `pre-calculus-how-to-solve-a-trigonometric-equation-over-a-given-interval` | how-to | D2 |
| `pre-calculus-how-to-evaluate-an-inverse-trigonometric-function` | how-to | D1 |
| `geometry-angle` | term | D1, D5 |
| `advanced-numbers-how-to-find-the-percent-of-a-number` | how-to | D4 |

## The "forces" test applied

*Could a competent student produce this deliverable correctly without ever performing this
skill?*

- **D1** cannot be done without evaluating an inverse trigonometric function: the Brewster-angle
  relationship $\tan\theta_p = n_2/n_1$ gives the *tangent* of the angle, not the angle itself —
  a student must apply $\arctan$ to isolate $\theta_p$ for each surface. There is no way to name
  "the Brewster angle" as a number without that step, and the worksheet explicitly requires the
  inverse trig function to be shown.
- **D2** cannot be done without solving a trigonometric equation over a restricted interval: the
  rotation angle that nulls each surface comes from inverting Malus's Law-driven geometry over
  $0°$ to $90°$, and a student who does not correctly bound the interval will either miss a valid
  rotation angle or accept an angle outside the polarizer's physical range.
- **D3** cannot be done without the Pythagorean identity: $\cos^2\theta = (1+\cos 2\theta)/2$ is
  derived from $\sin^2\theta+\cos^2\theta=1$ combined with the cosine double-angle formula, and
  the deliverable explicitly asks for an *algebraic* verification, not a numerical spot-check —
  "verify" is the deliverable, not "look up."
- **D4** cannot be done without converting a transmitted-intensity fraction into a percent-removed
  figure and comparing two such percentages — "find the percent of a number" is the arithmetic
  core of stating the margin between the Glass Call and the River Call.
- **D5** cannot be labeled correctly without correctly identifying and marking each surface's
  Brewster angle (which requires the same inverse-trig work as D1) and correctly reading angle
  measures onto a graph axis — a diagram with unlabeled or misplaced angle marks does not satisfy
  the deliverable as written.

## Result

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 7    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

All 5 scored skills (`pre-calculus-pythagorean-identity`, `pre-calculus-inverse-trigonometric-function`,
`pre-calculus-how-to-verify-a-trigonometric-identity`,
`pre-calculus-how-to-solve-a-trigonometric-equation-over-a-given-interval`,
`pre-calculus-how-to-evaluate-an-inverse-trigonometric-function`) already show `n>=1` in
`readmodel/standards_spine.json` as of 2026-08-30 (verified against the full Pre-Calculus/
Trigonometric Identities group in `case.json.spine_check_2026-08-30`) — this is a deliberate
**second-pass/redundancy case** per the approved concept sheet
(`cases/_concepts/CONCEPTS_precal-second-pass_2026-08-30.md`, concept C3), so `new_coverage[]` is
correctly empty and is not an authoring error. The remaining 2 claimed skills
(`geometry-angle`, `advanced-numbers-how-to-find-the-percent-of-a-number`) are already covered
elsewhere in the corpus and are exercised here for thickness, per the concept sheet's
"Already-covered skills it also exercises" note — not scored, not in `new_coverage[]`.
