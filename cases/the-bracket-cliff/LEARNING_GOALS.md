# The Bracket Cliff — Learning Goal Matrix

Bidirectional check between Challenge 3 deliverables and claimed spine skills (`case-write`
SKILL.md §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — piecewise net-cost function + one-sided limits, Hold The Cliff | `calculus-limit`, `calculus-one-sided-limit`, `calculus-how-to-evaluate-a-limit-algebraically` (a student cannot state `lim_{x→400%⁻} C(x)` and `lim_{x→400%⁻} C(x)` and evaluate them from the Appendix B household figures without knowing what a limit and a one-sided limit are, and without applying the algebraic evaluation procedure to a piecewise function) |
| D2 — continuity test at the threshold, Hold The Cliff | `calculus-continuity`, `calculus-discontinuity`, `calculus-how-to-determine-whether-a-function-is-continuous-at-a-point` (a student cannot correctly identify which part of the three-part continuity definition fails, or correctly name the result a discontinuity, without applying the continuity-at-a-point procedure to D1's limit values) |
| D3 — same two computations, Build The Bridge | `calculus-limit`, `calculus-one-sided-limit`, `calculus-how-to-evaluate-a-limit-algebraically`, `calculus-continuity`, `calculus-discontinuity`, `calculus-how-to-determine-whether-a-function-is-continuous-at-a-point` (repeats the full D1–D2 procedure on Appendix C's continuous formula; a student cannot show Build The Bridge *passes* where Hold The Cliff failed without correctly applying the same one-sided-limit and continuity-at-a-point machinery a second time on different data — this is the case's designed positive/negative worked-example pair, and it is what pushes each of the 6 target skills from `n=1` to `n=2`, closing the single-point-of-failure risk flagged in the concept sheet) |
| D4 — discontinuity-size-vs-cost table | draws on D1–D3's outputs (the discontinuity size is the D2 jump, in dollars); also exercises `advanced-numbers-percent` and `advanced-numbers-how-to-find-the-percent-of-a-number` (already-covered skills, scaling Appendix D's national share and Appendix E's enrollment into a state-specific affected-household estimate) — not scored toward `new_coverage`, included to round out the case per the concept sheet |
| D5 — recommendation memo | draws on D1–D4; forces no additional skill by itself, consistent with the precedent set in `cases/cooling-curve/LEARNING_GOALS.md` and `cases/fret-board/LEARNING_GOALS.md` for a case's final recommendation deliverable |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 6    new_coverage: []  (see coverage note — all 6 sit at n=1, not n=0)
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forces test applied:** a competent student cannot produce D1 without correctly setting up and
evaluating both one-sided limits of a piecewise function — that is the definition of the skill, not
an incidental step. D2 requires applying the specific three-part continuity-at-a-point test to D1's
output and correctly naming the failure a discontinuity — a student who just states "it's not
continuous" without running the test has not produced D2 as specified. D3 is not redundant with
D1–D2: it requires running the identical procedure on a different (continuous) cost function and
reaching the opposite, correctly-justified conclusion — a student who mechanically copies D1–D2's
structure without re-evaluating the new limits will get D3 wrong, so it genuinely forces the same
six skills a second time rather than merely repeating a label. D4 and D5 are synthesis deliverables
built on D1–D3's outputs; D4 additionally exercises two already-covered skills without inflating
`new_coverage`.

## Coverage note

All 6 target skills (`calculus-limit`, `calculus-one-sided-limit`, `calculus-continuity`,
`calculus-discontinuity`, `calculus-how-to-evaluate-a-limit-algebraically`,
`calculus-how-to-determine-whether-a-function-is-continuous-at-a-point`) were checked against
`readmodel/standards_spine.json` at the start of this write pass and each carries `n == 1` — every
one is already covered by exactly one existing case, not zero. Per SPEC §4, `new_coverage[]` is
strictly the subset with `n == 0`; none of these six qualifies, so `new_coverage` is correctly
`[]` here, per this case's explicit write-time instruction (deviating from the usual "a case with
no `new_coverage` has no reason to exist" default in `case-write` SKILL.md §12's validator).

**Why this case exists anyway — the reinforcement argument.** The entire Calculus/Limits And
Continuity group sits at `n=1` across all 6 skills: a single existing case is the *only* thing
standing between this group and total gap status. That is a structural single-point-of-failure risk
in the coverage matrix, the same priority class the concept sheet (`CONCEPTS_precal-second-pass_
2026-08-30.md`, "Addendum (2026-08-31)") flags for the Precal C9/C10 and Geometry C11 concepts. This
case's D1–D3 deliverately reinforce every one of the 6 skills a second time — not once, but twice
each (Hold The Cliff and Build The Bridge each independently force the full one-sided-limit →
continuity-test chain) — moving the whole group from `n=1` to `n=3` per skill and eliminating the
single-point-of-failure risk, which is this case's actual reason to exist even though it cannot
claim `new_coverage` in the SPEC §4 sense.

**`reinforcement_note` (recorded in `case.json`):** "All 6 claimed skills are already covered
(n=1 each) by one prior case; this case does not open new coverage, it removes the group's
single-point-of-failure risk by giving each skill independent, doubled reinforcement (once via
Hold The Cliff in D1–D2, once via Build The Bridge in D3) — an explicit write-time exception to the
usual non-empty-`new_coverage` requirement, authorized because the entire Calculus/Limits And
Continuity group sits at n=1 across all 6 skills with no other case in the pipeline currently
targeting it."
