# Learning Goals — The Setpoint Call

Bidirectional deliverable <-> skill matrix. Run before `case.json` was emitted.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — build TC(r) = CR(r) × MPU(r) from the two cost-rate/time factors | calculus-how-to-solve-an-optimization-problem-using-derivatives |
| D2 — differentiate via the product rule (+ power rule), set TC'(r)=0, solve for r* | calculus-derivative, calculus-how-to-find-a-derivative-using-the-power-rule, calculus-how-to-use-the-product-rule-to-differentiate-a-product-of-functions, calculus-critical-point, calculus-how-to-find-critical-points-of-a-function, calculus-how-to-solve-an-optimization-problem-using-derivatives |
| D3 — first derivative test AND concavity check to confirm minimum, not maximum | calculus-how-to-use-the-first-derivative-test-to-classify-a-critical-point, calculus-concavity, calculus-critical-point |
| D4 — check r* against the rated safe-speed ceiling; evaluate TC at both | calculus-how-to-solve-an-optimization-problem-using-derivatives |
| D5 — total-cost-per-bottle comparison across the contract volume, in dollars and percent | advanced-numbers-how-to-find-the-percent-of-a-number |
| D6 — original visual: TC(r) vs. r, with r* and the rated ceiling labeled | calculus-critical-point, calculus-concavity |

## LEARNING GOAL CHECK

- deliverables: 6
- claimed skills (standards[]): 9
- new_coverage: 0 (empty — see `case.json.reinforcement_note`; every skill in the Calculus/Derivatives
  spine group already has n>=1 as of 2026-09-09, so no zero-coverage claim is honestly available.
  This case reinforces the two thinnest skills in the neighborhood not already claimed by
  `cases/the-marginal-call` — the product rule (n=1) and concavity (n=2) — rather than padding a
  fake new-coverage claim.)

**UNMAPPED DELIVERABLES:** none — every deliverable (D1–D6) has a non-empty skills column.

**UNREACHABLE SKILLS:** none — every id in `standards[]` appears in at least one deliverable's
skills column:
- calculus-derivative → D2
- calculus-critical-point → D2, D3, D6
- calculus-concavity → D3, D6
- calculus-how-to-find-a-derivative-using-the-power-rule → D2
- calculus-how-to-use-the-product-rule-to-differentiate-a-product-of-functions → D2
- calculus-how-to-find-critical-points-of-a-function → D2
- calculus-how-to-use-the-first-derivative-test-to-classify-a-critical-point → D3
- calculus-how-to-solve-an-optimization-problem-using-derivatives → D1, D2, D4
- advanced-numbers-how-to-find-the-percent-of-a-number → D5

**Reverse check (phantom):** every skill named in a deliverable's `skills[]` column is also in
`standards[]` — no deliverable claims credit for a skill the case doesn't list.

RESULT: **PASS**

Forces-test applied to each mapping: could a competent student produce the deliverable correctly
without ever performing the named skill? D2 cannot be done without the product rule — the two
factors CR(r) and MPU(r) are both genuinely r-dependent, and expanding first only hides the
technique, it doesn't remove the need to differentiate a product correctly. D3 cannot be answered
without concavity — the deliverable explicitly asks for the second-derivative sign and what a local
maximum would look like on this curve, which cannot be answered by naming "local minimum" alone.
