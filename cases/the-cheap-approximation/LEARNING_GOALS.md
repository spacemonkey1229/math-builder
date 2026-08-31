# The Cheap Approximation — Learning Goal Matrix

Bidirectional check between Challenge 3 deliverables and claimed spine skills (`case-write`
SKILL.md §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Taylor series derivation | `calculus-how-to-find-the-taylor-series-of-a-function-at-a-point`, `calculus-taylor-series` (producing a 2nd-order Taylor expansion at a named center point is the literal object of both the how-to procedure and the vocabulary term — there is no way to derive D1 without performing both) |
| D2 — convergence check | `calculus-how-to-determine-whether-a-series-converges-or-diverges`, `calculus-series` (deciding whether the full, non-truncated Taylor series converges over the rated operating range requires applying a genuine convergence test to a series, and understanding what a series is to interpret the result) |
| D3 — error-at-the-extremes table | `calculus-taylor-series` (the error figure is literally the gap between D1's Taylor approximation and the true response-function value — a student cannot produce D3 without having built a genuine 2nd-order Taylor approximation first) |
| D4 — compute-time table | `calculus-taylor-series` (counting the multiply/add operations the Series Path costs requires knowing exactly which terms D1's 2nd-order Taylor expansion contains — a student who never derived D1 cannot correctly count the operations that expansion requires) |
| D5 — comparison and recommendation | draws on D3–D4; forces no additional skill by itself (precedent: `cases/cooling-curve/LEARNING_GOALS.md` D5, a synthesis/recommendation deliverable) |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 4    new_coverage: 2
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forces test applied:** a competent student cannot produce D1 without performing the Taylor-series
how-to at a named point — that is what D1 *is*. D2 cannot be produced without applying a
convergence test to a series — there is no other way to determine an interval of guaranteed
convergence. D3 and D4 each require D1's Taylor-expansion output as their direct input (D3 needs
the approximation's value to compare against the true curve; D4 needs the expansion's exact term
count to cost out the arithmetic), so they force `calculus-taylor-series` transitively rather than
claiming a new skill. D5 is a synthesis deliverable that combines D3 and D4 into the primary metric
without introducing a fifth skill — consistent with the precedent set in
`cases/cooling-curve/LEARNING_GOALS.md` for a case's final recommendation deliverable.

## Coverage note

`calculus-taylor-series` (term) and `calculus-how-to-find-the-taylor-series-of-a-function-at-a-point`
(how-to) both had `n == 0` in `readmodel/standards_spine.json` as of 2026-08-30 (checked at the
start of this write pass) — this case's reason to exist is closing both. These are two of the five
skills in the entire spine currently sitting at true zero coverage.

`calculus-series` (term, `n == 1`) and `calculus-how-to-determine-whether-a-series-converges-or-diverges`
(how-to, `n == 1`) are both claimed because they are genuinely load-bearing (D2 cannot exist without
them — a Taylor series is meaningless to evaluate at the extremes without first knowing where it
converges), not because they needed opening. They are not in `new_coverage[]`.
