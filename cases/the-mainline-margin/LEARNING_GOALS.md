# LEARNING_GOALS.md — The Mainline Margin

Bidirectional deliverable ↔ skill matrix. Claimed skills (`case.json.standards[]`): the full
Advanced Operations/Variables group — `advanced-operations-variable`, `advanced-operations-constant`,
`advanced-operations-coefficient`, `advanced-operations-term`, `advanced-operations-like-terms`,
`advanced-operations-distributive-property`,
`advanced-operations-how-to-evaluate-a-variable-expression-substitution-property`,
`advanced-operations-how-to-add-and-subtract-an-expression-with-variables`,
`advanced-operations-how-to-solve-a-one-step-equation`,
`advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-one-side`,
`advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-both-sides`.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — total-annualized-cost expression per option, labeled and expanded via the distributive property | advanced-operations-variable, advanced-operations-constant, advanced-operations-coefficient, advanced-operations-term, advanced-operations-distributive-property |
| D2 — substitution table (Hazen-Williams result + D1's expression evaluated at the farm's real inputs) | advanced-operations-how-to-evaluate-a-variable-expression-substitution-property |
| D3 — simplified annualized-cost expression, combining like terms | advanced-operations-like-terms, advanced-operations-how-to-add-and-subtract-an-expression-with-variables |
| D4 — certification check via a one-step equation (max flow rate before the velocity ceiling) | advanced-operations-how-to-solve-a-one-step-equation |
| D5 — rearranged Hazen-Williams formula, multi-step equation with the variable on one side | advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-one-side |
| D6 — break-even calculation, multi-step equation with the variable on both sides, plus recommendation | advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-both-sides |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 6    claimed skills: 11    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS (bidirectional mapping) / SEE NOTE (new_coverage)
```

**Forces test applied:** could a competent student produce D1 without naming a variable, constant,
coefficient, and term, and without applying the distributive property? No — D1 explicitly requires
labeling each of those and showing the expansion step. Could they produce D2 without substituting
real values into an algebraic expression? No — D2's only content is that substitution. Could they
produce D3 without identifying and combining like terms? No. Could they produce D4, D5, or D6
without actually solving the specific equation type each one names (one-step; multi-step,
variable on one side; multi-step, variable on both sides, respectively)? No — each deliverable's
entire content is that specific solve, using inputs that only resolve once Appendices A–F are
sourced, so there is no shortcut that skips the algebra.

No deliverable was left unmapped, and no claimed skill lacks a deliverable that forces it — the
bidirectional check passes cleanly on its own terms.

**Separate, required note on `new_coverage`:** every one of these 11 skills already has real
coverage elsewhere in the corpus (n ≥ 1; verified live against `readmodel/standards_spine.json`
on 2026-09-01 — see the exact per-skill n values in `case.json.reinforcement_note`). None is at
n=0. The concept sheet's own framing ("closing all five of the group's n=1 skills") is correct on
its own terms — this case does reinforce the five weakest-covered skills in the group
(`advanced-operations-like-terms`, `advanced-operations-distributive-property`,
`advanced-operations-how-to-add-and-subtract-an-expression-with-variables`,
`advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-one-side`,
`advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-both-sides`, each
currently at n=1) from single-case to two-case coverage — but n=1 is not n=0, and SPEC §4/§7's
`new_coverage[]` test is specifically the n==0 test. `new_coverage[]` is therefore correctly empty
in `case.json`, and this case does **not** clear the "case has no reason to exist" bar SPEC §7 sets
for new-coverage cases on its own. This is flagged as a blocker for human review in
`case.json.reinforcement_note`, not silently resolved.
