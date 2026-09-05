# The Bracket Bet — Learning Goal Matrix

Bidirectional check between Challenge 3 deliverables and claimed spine skills (`case-write`
SKILL.md §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — order-of-operations growth snapshot (5/15/30-year single-contribution growth, shown step by step) | `advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order`, `advanced-operations-how-to-evaluate-an-exponential-expression`, `advanced-operations-exponent-also-power`, `advanced-operations-base` (a student cannot show the required step-by-step order-of-operations work — exponent evaluated before the multiplication — without applying both how-to skills, and cannot label the parts of the expression correctly in the shown work without knowing what an exponent and a base are) |
| D2 — the forty-year growth ladder (full compounding table, ≤5-year increments) | `advanced-operations-how-to-evaluate-an-exponential-expression`, `advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order`, `advanced-operations-exponent-also-power`, `advanced-operations-base` (repeats D1's procedure roughly eight times across the horizon rather than once — a student cannot build a correct table without re-applying the same exponent-evaluation and order-of-operations skills at every increment, which is what pushes this thin how-to skill from a single forced use to a genuinely reinforced one) |
| D3 — the two tax bills (after-tax value under both future-rate scenarios, both options) | `advanced-numbers-how-to-find-the-percent-of-a-number`, `advanced-numbers-percent` (a student cannot compute either the up-front Pay Now tax bite or the withdrawal-year Pay Later tax bite without correctly finding a percent of a dollar amount at each of the two assumed rates — four separate percent-of-a-number computations in total) |
| D4 — the crossover chart | `advanced-numbers-percent` (the horizontal axis IS the assumed future tax rate — a percent — and the two required plotted points are D3's percent-of-a-number results; a student cannot correctly place or label either axis, or correctly read where the two lines cross, without treating the plotted quantity as a percent rather than a raw dollar figure) |
| D5 — recommendation memo | `advanced-numbers-how-to-find-the-percent-of-a-number` (D5 requires naming, explicitly, what future tax-rate value would flip the recommendation — finding that break-even point means re-applying the percent-of-a-number procedure to test candidate rates against D3's after-tax values, not just restating D1–D4's conclusion; this mirrors the precedent set in `cases/the-bracket-cliff/LEARNING_GOALS.md` and `cases/cooling-curve/LEARNING_GOALS.md`, where the recommendation-memo deliverable is mapped onto an already-claimed skill rather than left unmapped) |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 6    new_coverage: []  (see coverage note — all 6 sit at n>=2, not n=0)
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forces test applied:** a competent student cannot produce D1 without evaluating an exponential
expression and showing the exponent-before-multiplication order of operations explicitly — a
student who states only the final grown value, with no shown exponent step, has not produced D1 as
specified. D2 is not a redundant repeat of D1: it requires re-running the identical exponent
procedure at every increment across the full horizon and assembling the results into one consistent
table, which is what turns a single instance of the thinnest target skill into genuine, repeated
reinforcement. D3 requires four independent percent-of-a-number computations (two options × two
rate scenarios) and cannot be produced correctly by only running one scenario — a student who skips
Scenario 2 has not completed D3, which is also what forces the case's central trap (see
`FACILITATOR.md`). D4 (the crossover chart) and D5 (the recommendation memo) both build on D1–D3's
outputs, but each is now explicitly mapped rather than left as an unmapped synthesis deliverable:
D4 forces `advanced-numbers-percent` because its horizontal axis and both required plotted points
are percent-valued quantities, and D5 forces `advanced-numbers-how-to-find-the-percent-of-a-number`
because naming the flip-point value requires testing candidate rates with the same percent-of-a-
number procedure D3 used, not merely restating an already-computed conclusion. Neither introduces a
new skill claim outside the six already in `case.json.standards[]`.

## Coverage note

All 6 target skills (`advanced-operations-exponent-also-power` n=5, `advanced-operations-base` n=2,
`advanced-numbers-percent` n=57, `advanced-operations-how-to-evaluate-an-exponential-expression`
n=5, `advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order`
n=2, `advanced-numbers-how-to-find-the-percent-of-a-number` n=63) were checked against
`readmodel/standards_spine.json` at the start of this write pass (2026-09-03) and every one already
carries `n >= 2`. Per SPEC §4, `new_coverage[]` is strictly the subset with `n == 0`; none of these
six qualifies, so `new_coverage` is correctly `[]` here.

**Why this case exists anyway — the reinforcement argument.** The approved concept sheet's own
stated justification for this concept is explicitly a reinforcement one, not a zero-coverage one:
it names `advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order`
(n=2, tied for the thinnest how-to skill in the entire Advanced Operations/Exponents group) as
genuinely worth closing further "if the compounding formula is built up from raw multiplication
rather than a single plugged formula" — and D1/D2 are written to do exactly that, forcing the skill
twice (once per contribution-year snapshot in D1, then roughly eight more times across the full
horizon in D2) rather than treating it as a single incidental step. The other 5 skills round out the
case's exponent-and-percent spine without inflating `new_coverage`.

**`reinforcement_note` (recorded in `case.json`):** "All 6 claimed skills already show n>0 in
`readmodel/standards_spine.json` at write time (Exponent/Base/Percent terms and their three how-to
skills range from n=2 to n=63), so `new_coverage[]` is correctly empty per SPEC §4's literal n==0
rule. This case was approved from the concept sheet specifically to reinforce the thin
`advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order`
skill (n=2) by forcing it twice (D1 and D2), not to close a zero-coverage gap — consistent with the
concept sheet's own framing and the precedent set in `cases/the-bracket-cliff/LEARNING_GOALS.md` and
`cases/prove-it-scales/case.json` for disclosed reinforcement-only cases."
