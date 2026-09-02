# Learning Goals — The Dosing Curve

Bidirectional deliverable ↔ skill matrix. Every Challenge-3 deliverable must map to a claimed
spine skill; every claimed skill must be forced by at least one deliverable.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Riemann-sum AUC table (per option, from Appendix B sampled data) | calculus-riemann-sum, calculus-how-to-approximate-area-under-a-curve-using-a-riemann-sum |
| D2 — fitted-curve antiderivative + FTC-evaluated definite integral (per option, cross-checked against D1) | calculus-antiderivative, calculus-indefinite-integral, calculus-definite-integral, calculus-how-to-find-an-antiderivative-using-the-power-rule, calculus-how-to-evaluate-a-definite-integral-using-the-fundamental-theorem-of-calculus |
| D3 — fAUC/MIC pass/fail comparison table (per option, vs. Appendix C target and breakpoint) | calculus-definite-integral |
| D4 — shaded-AUC-region graph + cost/handling comparison annotation | calculus-definite-integral |

**"Forces" test applied to each row:**

- D1: a student cannot build a Riemann-sum table from Appendix B's sampled concentration data
  without knowing what a Riemann sum is (partitioning the time axis into subintervals and summing
  height × width, or trapezoidal-rule area, across each one) and without applying the procedure
  itself to real sampled points — both the term and the how-to are load-bearing to the artifact,
  not decoration. This is also the real-world method (a Riemann/trapezoidal-rule sum is literally
  how published pharmacology tables turn sampled concentration data into an AUC figure), so the
  deliverable is not a math exercise bolted onto the case — it is the case's actual computation.
- D2: producing a *continuous* AUC for either option requires fitting a function to the same data,
  finding its general antiderivative via the power rule (the indefinite integral — the antiderivative
  family, not one specific antiderivative), and then evaluating that antiderivative at the treatment
  window's endpoints via the Fundamental Theorem of Calculus to get the definite integral — a
  student cannot produce this deliverable "showing your work" without performing all three terms
  and both how-tos; skipping straight to a single antiderivative without invoking the FTC produces
  a formula, not the requested cross-checked number.
- D3: the fAUC/MIC ratio that decides pass/fail is built directly from the cumulative exposure
  (the definite integral) computed in D2 divided by the published MIC-derived breakpoint from
  Appendix C — a student who has not computed a definite integral for the treatment window has no
  numerator to check against the threshold, so the deliverable reinforces `calculus-definite-integral`
  from a new angle (as a pass/fail gate rather than a raw number) rather than introducing a new
  spine id.
- D4: the shaded region a student must draw and annotate *is* the definite integral rendered
  visually — a student who has not computed the definite integral for each option has nothing
  principled to shade (guessing at a region is not "an original visual display of the data," it is
  a picture). This deliverable also satisfies Challenge 2(b)'s "at least one original visual
  display" requirement, so it earns its place twice over rather than padding the deliverable count.

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 7    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Flag on `new_coverage[]`:** all 7 claimed skills (`calculus-antiderivative`,
`calculus-definite-integral`, `calculus-indefinite-integral`, `calculus-riemann-sum`,
`calculus-how-to-find-an-antiderivative-using-the-power-rule`,
`calculus-how-to-evaluate-a-definite-integral-using-the-fundamental-theorem-of-calculus`,
`calculus-how-to-approximate-area-under-a-curve-using-a-riemann-sum`) were verified against
`readmodel/standards_spine.json` before writing and confirmed `n=1` each — every one already
covered once, by `Total Flow` — not `n=0`. Per SPEC §7, `new_coverage[]` must be non-empty for a
case to have "a reason to exist" in the coverage-gap sense on a strict reading, and this case
genuinely has none: it is written anyway because the concept sheet's own framing is redundancy,
not first coverage — the entire Calculus/Integrals group sits at `n=1` group-wide, meaning every
one of its 7 skills goes to *zero* coverage at once if `Total Flow` is ever retired or fails QA.
This case exists to give the group a second, independent case so no single point of failure can
zero out the group. `case.json.new_coverage` is left as an empty array rather than a false claim,
and `case.json.reinforcement_note` records this reasoning for the coverage-gap tooling.
