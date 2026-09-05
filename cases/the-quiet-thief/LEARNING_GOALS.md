# Learning Goals — The Quiet Thief

Bidirectional deliverable ↔ skill matrix. Run at `case-write` time per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — derive the real rate of return (percent-to-number, annual real-rate formula, monthly conversion via a fractional exponent) | `advanced-numbers-how-to-convert-percents-to-numbers`, `advanced-numbers-percent`, `advanced-operations-how-to-evaluate-an-exponential-expression`, `advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order`, `advanced-operations-exponent-also-power`, `advanced-operations-base` |
| D2 — Priya's real retirement balance via the future-value-of-an-annuity formula | `advanced-operations-how-to-evaluate-an-exponential-expression`, `advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order`, `advanced-operations-exponent-also-power`, `advanced-operations-base` |
| D3 — the Bridge Plan's required contribution, plus a percent-increase comparison to Priya's contribution | `advanced-operations-how-to-evaluate-an-exponential-expression`, `advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order`, `advanced-numbers-how-to-find-the-percent-of-a-number`, `advanced-numbers-percent` |
| D4 — the Extended Plan's required contribution, plus the percent margin against D3 | `advanced-operations-how-to-evaluate-an-exponential-expression`, `advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order`, `advanced-numbers-how-to-find-the-percent-of-a-number`, `advanced-numbers-percent` |
| D5 — the nominal-rate trap: recompute D3 with the nominal rate, and the percent understatement | `advanced-operations-how-to-evaluate-an-exponential-expression`, `advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order`, `advanced-numbers-how-to-find-the-percent-of-a-number`, `advanced-numbers-percent` |

**Forcing test applied to each row:** could a competent student produce this deliverable correctly
without ever performing the listed skill(s)? For D1, no — a student cannot derive a real rate of
return without first converting two percents to decimal numbers, cannot combine them with the
stated formula without applying percent arithmetic, and cannot convert the resulting annual real
rate into a monthly rate without evaluating an exponential expression with a fractional exponent
under the correct order of operations (exponent before subtraction). For D2, no — the annuity
future-value formula's defining feature is its `(1+r)^n` term; a student who cannot evaluate that
exponential expression, in the correct order relative to the surrounding subtraction and division,
cannot produce a correct balance. For D3, no — the rearranged formula is itself another exponential
expression to evaluate, and stating the "percent increase over Priya's contribution" requires
percent-of-a-number arithmetic on top of that. For D4, no — same reasoning as D3, applied at a
different `n`, plus a second percent computation (this time a percent *decrease*) comparing D4's
result to D3's. For D5, no — recomputing with the nominal rate is a *third* independent
exponential-expression evaluation (same formula, different rate), and "percent by which it
understates the true amount" is a third distinct percent-of-a-number computation, this time
comparing a wrong answer to a right one — which is also the case's named rubric trap (see
`FACILITATOR.md`).

## Claimed skills → deliverables (reverse direction)

| Claimed skill (spine id) | n (before this case) | Forced by |
|---|---|---|
| `advanced-numbers-how-to-convert-percents-to-numbers` | 18 | D1 |
| `advanced-numbers-percent` | 57 | D1, D3, D4, D5 |
| `advanced-operations-how-to-evaluate-an-exponential-expression` | 5 | D1, D2, D3, D4, D5 |
| `advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order` | 2 | D1, D2, D3, D4, D5 |
| `advanced-operations-exponent-also-power` | 5 | D1, D2 |
| `advanced-operations-base` | 2 | D1, D2 |
| `advanced-numbers-how-to-find-the-percent-of-a-number` | 63 | D3, D4, D5 |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 7    new_coverage: []  (see coverage note — all 7 sit at n>=2, not n=0)
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Note on the two thinnest skills.** This case exists to reinforce
`advanced-operations-how-to-evaluate-an-exponential-expression` (n=5) and, especially,
`advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order`
(n=2, tied for the thinnest how-to skill in the entire Advanced Operations/Exponents group). Both
are forced not once but **five separate times** across D1-D5 — the real-rate derivation's monthly
conversion, Priya's balance, the Bridge Plan's contribution, the Extended Plan's contribution, and
the nominal-rate trap's recomputation each require an independent exponential-expression
evaluation with the exponent sequenced correctly relative to the surrounding operations. This is
what turns a single incidental use of a thin skill into genuine, repeated reinforcement, consistent
with the pattern already established in `cases/the-bracket-bet/LEARNING_GOALS.md`.

## Coverage note

All 7 target skills were checked against `readmodel/standards_spine.json` at the start of this
write pass (2026-09-04) and every one already carries `n >= 2`. Per SPEC §4, `new_coverage[]` is
strictly the subset with `n == 0`; none of these seven qualifies, so `new_coverage` is correctly
`[]` here.

**Why this case exists anyway — the reinforcement and topic-gap arguments.** The approved concept
sheet's own stated justification is two-fold and explicit, neither of which is a zero-coverage
claim: (1) it names the long-horizon growth/inflation topic as having zero existing coverage in the
case library (see `case.json.topic_gap_closed`), and (2) it names
`advanced-operations-how-to-evaluate-an-exponential-expression` and the exponent-with-order-of-
operations skill as worth reinforcing by requiring the real-rate-of-return formula to be *derived*,
not given. D1-D5 are written to do exactly that. The other five skills (percent conversion, percent
term, percent-of-a-number, exponent term, base term) round out the case's exponent-and-percent
spine without inflating `new_coverage`.

**`reinforcement_note` (recorded in `case.json`):** see `case.json.reinforcement_note` for the full
text, confirming all 7 claimed skills already show `n>0` at write time and that only 6 skills in the
entire spine currently have `n==0`, none reachable from this case's deliverables — consistent with
the disclosed-reinforcement precedent in `cases/the-two-offers/case.json` and
`cases/the-bracket-bet/case.json`.
