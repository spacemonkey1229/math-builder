# Learning Goals — The Late Run

Bidirectional deliverable ↔ skill matrix (`case-write` step 10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 Brewster-angle worksheet | pre-calculus-inverse-trigonometric-function, pre-calculus-how-to-evaluate-an-inverse-trigonometric-function, geometry-angle |
| D2 rotation-tolerance worksheet | pre-calculus-how-to-solve-a-trigonometric-equation-over-a-given-interval |
| D3 identity-verification worksheet | pre-calculus-pythagorean-identity, pre-calculus-how-to-verify-a-trigonometric-identity |
| D4 percent-glare-removed comparison table | advanced-numbers-how-to-find-the-percent-of-a-number |
| D5 original visual (rotation-offset graph) | pre-calculus-inverse-trigonometric-function, geometry-angle |

**"Forces" test applied to each row:**

- **D1** — a student cannot find the glass window's own Brewster angle from its refractive index
  without evaluating an inverse tangent. There is no other route from `n` to `θ_p` in the
  Brewster relationship `tan θ_p = n₂/n₁`.
- **D2** — the rotation-tolerance equation `I(θ) = R_p/2 + (R - R_p/2)sin²θ` set equal to a stated
  tolerance is, algebraically, a trig equation that must be solved for θ over a bounded interval
  (0°–90°); there is no shortcut that skips solving for θ.
- **D3** — verifying `sin²θ = 1 - cos²θ` and using it to re-express D2's equation is a direct,
  unavoidable application of the Pythagorean identity; a student cannot "eyeball" an algebraic
  verification.
- **D4** — computing what percent of a surface's own reflectance a given removed amount
  represents is, by definition, a percent-of-a-number calculation; comparing the two options
  requires computing it twice and stating the margin.
- **D5** — plotting transmitted intensity against a rotation-offset angle and marking the
  Brewster angle on the same axes requires the same inverse-trig/angle vocabulary as D1, applied
  visually rather than algebraically — a distinct, still-forced application, not a repeat of D1's
  arithmetic.

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 7    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

`new_coverage` is deliberately 0 — this is a second-pass/redundancy case for an already-covered
spine group (Pre-Calculus/Trigonometric Identities), per the approved concept sheet
(`CONCEPTS_precal-second-pass_2026-08-30.md`, C7). All 5 scored skills sit at `n ≥ 1` as of
2026-08-31 (verified against `readmodel/standards_spine.json`); `geometry-angle` and
`advanced-numbers-how-to-find-the-percent-of-a-number` are round-out skills, not scored, not in
`new_coverage[]`, same treatment as the superseded `the-locks-window` case.
