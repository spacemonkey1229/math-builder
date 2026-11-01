# Learning Goals — The Sample Plan

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 sampling-design table (population/sample/individual/sample size/sampling method + justification) | statistics-and-probability-population, statistics-and-probability-sample, statistics-and-probability-individual, statistics-and-probability-sample-size, statistics-and-probability-systematic-sampling |
| D2 escape-probability calculation (repeated multiplication) | statistics-and-probability-experiment, statistics-and-probability-random, statistics-and-probability-probability, statistics-and-probability-event, statistics-and-probability-outcome, statistics-and-probability-how-to-determine-the-probability-of-a-compound-event |
| D3 full expected-cost calculation (inspection + risk-weighted terms) | advanced-numbers-how-to-find-the-percent-of-a-number, statistics-and-probability-how-to-determine-the-probability-of-a-single-event, statistics-and-probability-probability |
| D4 written cost-decomposition + supplier-deviation-notice (Twist) scenario | statistics-and-probability-variability, statistics-and-probability-probability, statistics-and-probability-how-to-determine-the-probability-of-a-single-event |
| D5 original dot plot (escape probability vs. sample size, 4+ candidates) | statistics-and-probability-dot-plot, advanced-numbers-how-to-find-the-percent-of-a-number |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced without correctly identifying which real-world quantity plays which sampling role: the full lot is the *population*, the units actually pulled are the *sample*, one tested unit is an *individual*, the count of units pulled is the *sample size*, and — the deliverable's real teeth — the student must name and justify the *sampling method* (systematic sampling: pulling, say, every kth unit off the production line, per how ANSI/ASQ Z1.4-style acceptance sampling is actually implemented on a real line) rather than defaulting to convenience sampling (grabbing whichever units are easiest to reach). A student who cannot distinguish population from sample, or who cannot explain why systematic sampling — not convenience — is what the standard's own methodology requires, has not produced this deliverable. Genuinely forces `population`, `sample`, `individual`, `sample-size`, `systematic-sampling`.
- **D2** is impossible without recognizing that "the sample contains zero defective units" is a compound event built from n individual pass/fail outcomes, and that computing its probability requires multiplying single-trial probabilities together (not adding them, not taking one flat percentage) — this is a genuine independent/compound-event probability computation, not a lookup. A student who instead multiplies the escape probability by the sample size, or treats it as a single-event calculation, has skipped the entire mechanism D2 exists to force. Genuinely forces `experiment` (the act of pulling and testing a sample is the experiment), `random` (the sampling method's validity depends on the draw being effectively random/representative), `probability`, `event`, `outcome`, and the compound-event how-to.
- **D3** requires combining a certain, unconditional cost (destructive testing) with a probability-weighted cost (an undetected escape) into one true expected-cost figure per plan — a student who compares only the destructive-testing costs (ignoring risk) or only the escape probabilities (ignoring the guaranteed cost) has not actually answered the dilemma. Genuinely forces the percent-of-a-number how-to (probability as a weight on a dollar figure) and single-event/probability reasoning for the baseline lot-occurrence term.
- **D4** requires decomposing D3's own total into "how much is the fixed inspection-cost gap" versus "how much is the probability-weighted risk-cost gap," and then re-examining the case's real lot-occurrence assumption under a stated, different scenario (a supplier deviation notice) — a student who cannot separate those two components, or who cannot say (even qualitatively, before recomputing) why a flagged lot changes the math, has not understood what D3 actually computed. The deliverable also explicitly requires naming that different lots carry different real risk — not identical risk — which is the case's genuine, forced `variability` concept (lot-to-lot variability in true occurrence probability, not just calculation variability). Genuinely forces `variability`, `probability`, and the single-event how-to.
- **D5** requires computing escape probability for sample sizes beyond just A and B, and displaying the result as a dot plot specifically (not a bar chart or a table) — a student who cannot generate at least two more data points beyond the two graded options, or who substitutes a different visual for a dot plot, has not produced this deliverable. The antecedent computation is impossible without the percent/probability arithmetic already forced in D2/D3. Genuinely forces `dot-plot` and the percent-of-a-number how-to.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 15    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

See `case.json.reinforcement_note` for the full accounting. Every claimed skill was checked against
`readmodel/standards_spine.json` before writing and none is `n == 0` — in fact, a full spine scan on
2026-09-09 found **zero** skills anywhere in the spine at `n == 0`: the corpus reached full coverage
in a recent prior batch. `new_coverage[]` is therefore `[]`, per the reinforcement carve-out (T1-10,
`skills/case-readiness/SKILL.md`, 2026-08-17) — this is not an authoring shortcut, it is the honest
result of the spine's current state, and every future case will face the same structural fact until
the spine's own composition changes. The case still closes the *topic/cluster* gap named at concept
approval: Statistics and Probability / Sampling and Experiments had 5 of its 14 skills sitting thin
(`n<=2`) at concept approval, and this case deliberately targets `systematic-sampling` (`n=2`, one of
the thinnest skills in the group) as a genuinely-forced deliverable (D1), not an incidental mention.
