# LEARNING GOAL CHECK — Deluge Gun

Bidirectional deliverable ↔ spine-skill matrix, per `case-write` SKILL.md §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — velocity-component verification worksheet | `pre-calculus-pythagorean-identity`, `pre-calculus-how-to-verify-a-trigonometric-identity`, `pre-calculus-sine-function`, `pre-calculus-cosine-function` |
| D2 — two-angle solution worksheet | `pre-calculus-how-to-solve-a-trigonometric-equation-over-a-given-interval`, `pre-calculus-how-to-evaluate-an-inverse-trigonometric-function`, `pre-calculus-inverse-trigonometric-function`, `pre-calculus-reference-angle` |
| D3 — hang-time and clearance comparison | `pre-calculus-sine-function`, `pre-calculus-cosine-function` (vertical velocity component drives time-of-flight/apex height; the trajectory-height-at-a-distance formula for the parapet check uses both sine and cosine) |
| D4 — effective-flow table | `advanced-numbers-how-to-find-the-percent-of-a-number` |
| D5 — original visual (Challenge 2b) | `pre-calculus-radian`, `pre-calculus-how-to-convert-between-degrees-and-radians` |

## Reverse check — every claimed skill traced to a deliverable

| Skill id | Kind | Forced by |
|---|---|---|
| `pre-calculus-pythagorean-identity` | term | D1 |
| `pre-calculus-inverse-trigonometric-function` | term | D2 |
| `pre-calculus-how-to-verify-a-trigonometric-identity` | how-to | D1 |
| `pre-calculus-how-to-solve-a-trigonometric-equation-over-a-given-interval` | how-to | D2 |
| `pre-calculus-how-to-evaluate-an-inverse-trigonometric-function` | how-to | D2 |
| `pre-calculus-sine-function` | term | D1, D3 |
| `pre-calculus-cosine-function` | term | D1, D3 |
| `pre-calculus-reference-angle` | term | D2 |
| `pre-calculus-radian` | term | D5 |
| `pre-calculus-how-to-convert-between-degrees-and-radians` | how-to | D5 |
| `advanced-numbers-how-to-find-the-percent-of-a-number` | how-to | D4 |

## The "forces" test applied

*Could a competent student produce this deliverable correctly without ever performing this
skill?*

- **D1** cannot be done without the Pythagorean identity: the whole point of the deliverable is
  to take the horizontal and vertical velocity components computed from each solved angle and
  verify, by substitution into $\sin^2\theta+\cos^2\theta=1$ (scaled by $v^2$), that they
  recombine to the nozzle's own rated exit velocity. A student who skips the identity has no way
  to check the components against anything — "verify" is the deliverable, not "compute."
- **D2** cannot be done without solving a trig equation on a restricted interval and evaluating
  an inverse trig function: the case gives $R$, $v$, and $g$, and the student must isolate
  $\sin(2\theta)$, apply $\arcsin$, and — critically — find the **second** solution on
  $(0°,90°)$, which is exactly "solve a trigonometric equation over a given interval," not a
  single plug-into-a-formula step.
- **D3** cannot be done without the sine and cosine functions: apex height and time of flight are
  direct functions of $v\sin\theta$, and the parapet-clearance check uses the trajectory-height
  formula $y(x)=x\tan\theta - gx^2/(2v^2\cos^2\theta)$, which needs both. A student who has not
  correctly separated the components in D1 will carry that error forward here, and a student who
  only checks the apex (not the height at the parapet's actual distance) will get the wrong
  clearance answer for the Low Arc, since its apex occurs well past the parapet's location.
- **D4** cannot be done without converting the wind-drift loss rate and time of flight into a
  percent reduction applied to the rated GPM — "find the percent of a number" is the arithmetic
  core of the deliverable.
- **D5** cannot be labeled correctly in both degrees and radians without performing the
  conversion — a diagram with only degree labels does not satisfy the deliverable as written.

## Result

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 11    new_coverage: 5
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

All 5 skills in `new_coverage[]` currently show `n == 0` in `readmodel/standards_spine.json`
(verified 2026-08-19); the remaining 6 claimed skills (`pre-calculus-sine-function`,
`pre-calculus-cosine-function`, `pre-calculus-reference-angle`, `pre-calculus-radian`,
`pre-calculus-how-to-convert-between-degrees-and-radians`, `advanced-numbers-how-to-find-the-percent-of-a-number`)
are already covered elsewhere in the corpus and are exercised here for thickness, not scored.
