# Learning Goals — The Minimum-Payment Trap

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 recursively defined monthly balance model (both strategies) | discrete-mathematics-recursive-formula, discrete-mathematics-base-case, discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence |
| D2 eighteen-month month-by-month table (both strategies) | discrete-mathematics-recursive-formula, discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence |
| D3 eighteen-month totals comparison + percent margin | advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number |
| D4 full payoff (months, years, total interest) + simple-interest-trap explanation | discrete-mathematics-recursive-formula, discrete-mathematics-base-case, discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence |
| D5 percent breakdown of interest vs. principal | advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number |
| D6 original visual display (balance trajectories) | discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced without stating a genuine base case (Month 0 = Appendix A's $7,756) and a genuine recursive step (each month's balance defined in terms of the PREVIOUS month's balance, not a closed-form formula) — a student who instead writes a single non-recursive formula for "balance after n months" has not produced this deliverable, because the whole point (stated in case-write's own framing) is that The Minimum Track's payment changes every month depending on the current balance, which cannot be captured without a genuine recursive definition. Forces `recursive-formula`, `base-case`, and the how-to for writing one.
- **D2** is impossible without actually iterating D1's recursive step eighteen times, each time using the *previous row's* ending balance — a student who instead computes each month's interest from the *original* $7,756 (skipping the recursion) produces a materially wrong table, which is exactly the trap D4 later names explicitly. Forces `recursive-formula` and the how-to for writing/applying one.
- **D3** requires converting two raw dollar totals (interest paid under A vs. under B) into a percent difference — genuinely forces `percent` and the percent-of-a-number how-to; a student who just reports "A paid more in dollars" without computing the percent margin has not completed this deliverable.
- **D4** requires continuing the exact same D1 recursion far past month eighteen (to month 233 for The Minimum Track) rather than restarting with a shortcut formula, and requires the student to reason about why skipping the recursion (charging interest on the original balance for every month) breaks the answer — this is impossible to answer correctly without having built and understood the D1 recursive model in the first place. Forces `recursive-formula`, `base-case`, and the how-to for writing one.
- **D5** requires taking D3's dollar totals and computing what percent of the total money paid went to interest versus principal for each strategy — a second, independent percent-of-a-number calculation from D3's, not a restatement of it. Forces `percent` and the percent-of-a-number how-to.
- **D6** requires plotting the actual month-by-month balances produced by D2's iterative table — a student cannot produce a genuine, correctly-shaped balance-trajectory chart (the Minimum Track's balance declining far more slowly than the Fixed Push's) without having actually run the recursion to generate the data points; a chart built from any other numbers is not this deliverable. Forces the recursive-formula how-to.

```
LEARNING GOAL CHECK
  deliverables: 6    claimed skills: 5    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

See `case.json.reinforcement_note` for the full accounting. Every claimed skill was checked against
`readmodel/standards_spine.json` before writing and none is `n == 0` (lowest are `base-case` at n=2
and `recursive-formula`/the recursive-formula how-to at n=3 each) — this case reinforces the
Discrete Mathematics / Proof And Recursion group, which the approved concept sheet correctly
identified as thin, but "thin" is not "zero," so it does not clear the write-time bar for
`new_coverage[]` (SPEC §7/§8: "the reason the case exists"). The full current `n == 0` list in the
spine was checked (number-sense-depth, number-sense-digit, geometry-how-to-find-the-volume-of-a-
sphere, calculus's quotient-rule how-to, calculus-taylor-series and its how-to) and nothing fits a
recursively-modeled credit-card-debt case without padding. `new_coverage[]` is `[]`, honestly, per
the reinforcement carve-out (T1-10, `skills/case-readiness/SKILL.md`, 2026-08-17) — the same pattern
used in `cases/the-deferred-repair/LEARNING_GOALS.md` and `cases/the-two-offers/case.json`. The case
still closes the *topic* gap named in the concept sheet (debt & credit / credit cards, previously
zero coverage in the corpus); it does not additionally close a *skill* gap, and that distinction is
flagged here for the project owner rather than papered over.
