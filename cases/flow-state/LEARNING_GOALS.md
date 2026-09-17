# Learning Goals — FlowState

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 segmented funnel table (reach × segment share × awareness × interest × trial × adoption, chained) | advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number, advanced-numbers-how-to-convert-numbers-to-percents, measurement-ratio, statistics-and-probability-mean |
| D2 reach-per-dollar and cost-per-acquisition table | measurement-ratio, measurement-proportion, measurement-how-to-find-a-missing-amount-in-a-proportion |
| D3 weighted-total comparison (Plan A vs Plan B, percent margin) | statistics-and-probability-mean, statistics-and-probability-how-to-find-the-mean-of-a-set-of-data, advanced-numbers-percent, advanced-numbers-how-to-convert-numbers-to-percents |
| D4 budget-shift system of two linear equations, solved for the break-even split | statistics-and-probability-system-of-equations, statistics-and-probability-how-to-solve-a-system-of-linear-equations, statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data, statistics-and-probability-slope, statistics-and-probability-x-intercept |
| D5 written recommendation citing D2's per-dollar case and D4's reallocation sensitivity | advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number, statistics-and-probability-system-of-equations |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced without repeatedly finding the percent of a number at each funnel stage (`how-to-find-the-percent-of-a-number`) and converting the chained fractional results back to a percent for reporting (`how-to-convert-numbers-to-percents`) — a student who multiplies straight through without ever naming an intermediate quantity as "22% of reach" or "10% of aware" has not shown the chained percent-of-a-percent-of-a-percent work the deliverable requires. The channel-to-segment split is itself a ratio (`ratio`), and reporting Plan A's or Plan B's blended result across two segments genuinely requires a weighted mean (`mean`) rather than a simple average of the two segments' totals, since the segments are unequal shares of each channel's audience. A student who averages the two segments' subscriber counts 50/50 instead of weighting by each channel's actual segment split gets the wrong number for every channel with an asymmetric split (all five channels in Appendix D). Genuinely forces `advanced-numbers-percent`, `how-to-find-the-percent-of-a-number`, `how-to-convert-numbers-to-percents`, `ratio`, and `mean`.
- **D2** requires computing reach-per-dollar as a genuine ratio (reach : budget) and comparing it across five channels with different units of scale (`ratio`, `proportion`) — a student who cannot set up "if $18,000 buys 1,285,714 people of reach, how many people does $1 buy" as a proportion problem (`how-to-find-a-missing-amount-in-a-proportion`) cannot correctly scale between the channel-level reach figures in Appendix A and the per-dollar figures this deliverable asks for. Genuinely forces `ratio`, `proportion`, and the missing-amount-in-a-proportion how-to.
- **D3** requires summing ten channel-by-segment subscriber figures per plan into one total and reporting the percent difference between the two plans' totals — a student who cannot correctly compute a weighted total across channels of very different size (`mean`, `how-to-find-the-mean-of-a-set-of-data`, applied here as a weighted-sum problem rather than a simple average) will misstate the comparison, and the percent-margin step itself requires `percent` and `how-to-convert-numbers-to-percents` applied to two large, unequal totals rather than two small round numbers. Genuinely forces `mean`, `how-to-find-the-mean-of-a-set-of-data`, `percent`, and `how-to-convert-numbers-to-percents`.
- **D4** is impossible without literally setting up and solving a system of two linear equations (`system-of-equations`, `how-to-solve-a-system-of-linear-equations`) — a student who tries a handful of reallocation guesses and stops when two numbers look close has not produced this deliverable, which explicitly requires algebraic work, not guess-and-check. Building the second equation (subscribers as a function of the broadcast/precision split) requires writing a linear equation from the per-dollar yield data computed in D1–D3 (`how-to-write-a-linear-equation-given-a-set-of-data`), and a student cannot correctly interpret what that equation's coefficients mean, or sanity-check their solution, without understanding slope as a per-dollar rate of change (`slope`) and recognizing what the break-even point represents on a graph of subscribers vs. dollars shifted, which is functionally an x-intercept of a difference line (`x-intercept`). Genuinely forces `system-of-equations`, `how-to-solve-a-system-of-linear-equations`, `how-to-write-a-linear-equation-given-a-set-of-data`, `slope`, and `x-intercept`.
- **D5** requires stating the actual percent case for the chosen plan (`percent`, `how-to-find-the-percent-of-a-number`) and correctly characterizing D4's system-of-equations result in the recommendation (`system-of-equations`) — a student who writes "Plan A gets more subscribers" without citing the cost-per-acquisition percent difference or the actual dollar reallocation threshold has not met this deliverable's own stated requirement, even if their underlying arithmetic elsewhere is correct. Genuinely forces `percent`, `how-to-find-the-percent-of-a-number`, and `system-of-equations` as the vocabulary and quantities the paragraph must actually use.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 13    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

See `case.json.reinforcement_note` for the full accounting. Every one of the 13 claimed skills
was checked against `readmodel/standards_spine.json` before writing. A mechanical scan of the
*entire* spine (`python3` sweep over every domain/group/skill, run 2026-09-11) found **zero**
skills anywhere in the spine currently at `n == 0` — every skill in the corpus has already been
claimed by at least one published case. This is not specific to FlowState's topic area; no case
authored from this point forward can produce a non-empty `new_coverage[]` without either the spine
gaining new skills or an existing skill's `covered_by[]` being invalidated the way
`cases/cold-chain/case.json`'s `new_coverage_correction_2026_08_05` note describes. `new_coverage[]`
is therefore `[]`, honestly, per the reinforcement carve-out (T1-10, `skills/case-readiness/SKILL.md`,
2026-08-17) — the same pattern used in `cases/the-fee-route/LEARNING_GOALS.md`. The case still adds
real value against the concept sheet's own framing: `statistics-and-probability-system-of-equations`
(n=5), `statistics-and-probability-how-to-solve-a-system-of-linear-equations` (n=5), and
`statistics-and-probability-x-intercept` (n=3) are among the thinnest groups in the entire spine,
and every one of the 13 claimed skills is genuinely forced by at least one deliverable (see the
matrix and check above) — landing this case takes six genuinely thin Statistics-and-Probability/
Algebra skills up by one each.
