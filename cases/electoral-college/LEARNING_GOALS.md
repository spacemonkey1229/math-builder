# LEARNING_GOALS.md — Electoral College

Bidirectional deliverable ↔ skill matrix (SPEC §1.5 item 3 deliverables against `readmodel/standards_spine.json` skill ids).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 State Visit Budget Table (per-state visit cost, running total against the travel budget — a flat per-state fee plus a per-half-day/full-day cost, summed and compared to a cap) | `advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-without-exponents-or` |
| D2 Vote-Share Projection Table (solve for the minimum half-days needed so `baseline% + swing_rate × x > opponent%`, then apply the percent gain) | `advanced-operations-how-to-solve-a-one-step-equation`, `advanced-numbers-how-to-find-the-percent-of-a-number`, `advanced-numbers-percent` |
| D3 Electoral Vote Verification Table (running EV total vs. 270, and that total expressed as a percent of 538) | `advanced-numbers-how-to-convert-numbers-to-percents` |
| D4 Cost-Efficiency Comparison Table (dollar cost per electoral vote and per percentage point flipped, across all 37 contested states, ranked) | `measurement-ratio`, `measurement-proportion`, `measurement-how-to-find-a-missing-amount-in-a-proportion` |
| D5 Demographic Targeting Plan (which voter group to target per half-day, justified against national demographic percentages) | `advanced-numbers-how-to-find-the-percent-of-a-number`, `advanced-numbers-percent` |

## The "forces" test

*Could a competent student produce this deliverable correctly without ever performing this skill?*

- **D1** cannot be built without evaluating a multi-term expression (flat fee + per-visit cost × count, summed across every visited state) in the correct order — a bare "add some numbers" pass without operation-order discipline produces a wrong running total. Forces `advanced-operations-how-to-evaluate-an-expression-...`.
- **D2** is explicitly required to show "the equation you solved" — a student who eyeballs "about 4 half-days" instead of setting up and solving `baseline + 2x > opponent` for `x` has not produced the deliverable as specified. Forces `advanced-operations-how-to-solve-a-one-step-equation` and, to compute the resulting projected share, `advanced-numbers-how-to-find-the-percent-of-a-number` / `Percent`.
- **D3** requires converting a raw EV count into "what percent of 538" — a count alone does not satisfy the deliverable's explicit ask. Forces `advanced-numbers-how-to-convert-numbers-to-percents`.
- **D4** is a comparison across 37 states on two different rates (cost/EV and cost/point) — this is a proportion/ratio task by construction: finding the missing dollar amount needed to close each state's specific point-gap, then normalizing to a common per-unit rate to rank them. Forces `measurement-ratio`, `measurement-proportion`, `measurement-how-to-find-a-missing-amount-in-a-proportion`.
- **D5** requires reading percentages off Appendix D and using them to justify a targeting choice — forces `advanced-numbers-how-to-find-the-percent-of-a-number` and the `Percent` vocabulary itself (a student must be able to state and compare percentages, not just visitors' raw counts).

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 8    new_coverage: 1
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

`new_coverage[]` = `advanced-operations-how-to-solve-a-one-step-equation` (n=0 in the spine before this case). This is a genuine forced skill, not padding: D2 explicitly requires the student to set up and solve `baseline_% + swing_rate × half_days > opponent_%` for the number of half-days, which is a one-step linear equation in one variable. No other candidate skill in the rate/ratio/percent neighborhood of this case had `n == 0` in the spine — this is the one real gap the case's own deliverables force closed, not a manufactured one.
