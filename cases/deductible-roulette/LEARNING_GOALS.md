# Learning Goals — Deductible Roulette

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 three-year claim-probability table (baseline + conditional-on-prior-claim branches) | statistics-and-probability-probability, statistics-and-probability-event, statistics-and-probability-outcome, statistics-and-probability-dependent-event, statistics-and-probability-conditional-probability, statistics-and-probability-how-to-determine-the-probability-of-a-single-event |
| D2 compound "claim-free through Year 1 and Year 2" calculation | statistics-and-probability-dependent-event, statistics-and-probability-how-to-determine-the-probability-of-a-compound-event, statistics-and-probability-how-to-determine-the-probability-of-conditional-events |
| D3 full three-year branch-weighted expected-cost calculation | advanced-numbers-how-to-find-the-percent-of-a-number, statistics-and-probability-how-to-determine-the-probability-of-a-single-event, statistics-and-probability-conditional-probability, statistics-and-probability-probability |
| D4 written breakdown of premium-vs-risk contribution and MA1 sensitivity | statistics-and-probability-probability, statistics-and-probability-conditional-probability, statistics-and-probability-how-to-determine-the-probability-of-a-single-event |
| D5 original visual display (three-year cost comparison) | advanced-numbers-how-to-find-the-percent-of-a-number |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced without recognizing that Year 2 and Year 3 each split into two genuinely different conditional branches — the probability of a claim that year depends on whether a claim has already happened in this window, which is precisely what makes each row a real dependent/conditional-probability read rather than four unrelated lookups. Filling the table also requires reading each row as a probability applied to a defined event ("Priya files an at-fault collision claim") over a defined outcome space. Genuinely forces `probability`, `event`, `outcome`, `dependent-event`, `conditional-probability`, and the single-event how-to (each individual branch is still, correctly, a single event's probability).
- **D2** is impossible without combining two dependent, sequential probabilities into one "claim-free through both years" figure and then taking the complement to get "at least one claim by Year 3" — a student who instead adds the two yearly baseline probabilities, or ignores that Year 2's baseline branch is itself conditional on Year 1 having gone clean, produces a materially wrong number. Genuinely forces `dependent-event`, the compound-event how-to, and the conditional-events how-to.
- **D3** requires weighting each year's expected deductible payment by which branch (clean vs. already-claimed) Priya is in that year, multiplying by the branch-appropriate probability and by the deductible, and adding that to the fixed premium total — genuinely forces the percent-of-a-number how-to (probability as a weight on a dollar figure), single-event probability, and conditional-probability (the branch-selection itself). A student who instead multiplies the *compound* three-year probability from D2 once against the deductible, or who ignores the already-claimed branch entirely, has skipped the entire conditional-weighting step this deliverable exists to force.
- **D4** requires decomposing D3's own total into "how much is the fixed premium gap" versus "how much is the probability-weighted claim-cost gap," and re-examining the case's one Modeling Assumption's effect on that gap — a student who cannot separate those two components, or who cannot state (even qualitatively) how a higher MA1 value would move the comparison, has not actually understood what D3 computed. Genuinely forces `probability`, `conditional-probability`, and the single-event how-to.
- **D5** requires pulling the D3 totals forward into a real comparative visual (bars, a tree, or equivalent) with labeled totals, not a pasted table — the antecedent computation is impossible without the percent/expected-value arithmetic already forced in D3. Genuinely forces `how-to-find-the-percent-of-a-number` as the computation the visual is built from.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 9    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

See `case.json.reinforcement_note` for the full accounting. Every claimed skill was checked against
`readmodel/standards_spine.json` before writing and none is `n == 0` (lowest are `dependent-event`
and `conditional-probability` at n=3, and the compound-event how-to at n=4) — this case reinforces
skills the spine already has some coverage for rather than closing a true zero-coverage skill gap,
the same honest finding as `cases/the-deferred-repair/LEARNING_GOALS.md` (published in the same
batch). `new_coverage[]` is `[]`, per the reinforcement carve-out (T1-10,
`skills/case-readiness/SKILL.md`, 2026-08-17). The case still closes the *topic* gap named at
concept approval — non-health insurance / deductible-choice economics, previously zero coverage in
the corpus, distinct from the existing healthcare-insurance case — it does not additionally close a
*skill* gap, and that distinction is flagged here for the project owner rather than papered over.
