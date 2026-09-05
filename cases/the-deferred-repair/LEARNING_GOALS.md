# Learning Goals — The Deferred Repair

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 three-year conditional-probability table | statistics-and-probability-probability, statistics-and-probability-event, statistics-and-probability-outcome, statistics-and-probability-dependent-event, statistics-and-probability-conditional-probability, statistics-and-probability-how-to-determine-the-probability-of-a-single-event |
| D2 compound "fails at least once in 3 years" calculation | statistics-and-probability-dependent-event, statistics-and-probability-how-to-determine-the-probability-of-a-compound-event, statistics-and-probability-how-to-determine-the-probability-of-conditional-events |
| D3 expected-annual-cost comparison table | advanced-numbers-how-to-find-the-percent-of-a-number, statistics-and-probability-how-to-determine-the-probability-of-a-single-event, statistics-and-probability-probability |
| D4 filtering decision on the other two flagged services | statistics-and-probability-probability, statistics-and-probability-event, statistics-and-probability-outcome, statistics-and-probability-how-to-determine-the-probability-of-a-single-event |
| D5 original visual display (cost comparison) | advanced-numbers-how-to-find-the-percent-of-a-number |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced without recognizing that Year 2's and Year 3's failure figures in Appendix B are not the same kind of quantity as a plain single-year probability — each is explicitly conditioned on the engine having survived every prior skipped year, which is a genuine dependent/conditional-probability read, not just three unrelated lookups. Filling the table also requires reading each row as a probability applied to a defined event ("the coolant system fails this year") over a defined set of outcomes. Genuinely forces `probability`, `event`, `outcome`, `dependent-event`, `conditional-probability`, and the single-event how-to (each row is still, individually, a single event's probability, read correctly).
- **D2** is impossible without combining three dependent, conditionally-defined probabilities into one "at least once" figure via the complement rule (1 − P(no failure at all)) — a student who instead adds or averages the three Appendix B probabilities produces a materially wrong number. Genuinely forces `dependent-event`, the compound-event how-to, and the conditional-events how-to (Year 2 and Year 3's terms in the product are each conditional probabilities, not marginal ones).
- **D3** requires multiplying each year's probability from D1 against Appendix B's repair cost to get a probability-weighted (expected) dollar figure, then comparing it to a flat percent/no-percent certain cost — genuinely forces the percent-of-a-number how-to (converting and applying the probability as a weight on a dollar figure) and the single-event probability how-to; a student who instead just compares the flush price to the flat repair price skips the entire probability-weighting step and produces the case's own named trap answer.
- **D4** requires pulling Appendix C's own probability and cost figures for two different services and using each one's actual failure probability — not the shop's identical urgent tone or similar sticker price — to decide whether it belongs in the same category as the coolant flush. A student who classifies by price or tone alone, without computing/comparing the probabilities, fails this deliverable even if their prose reads confidently. Genuinely forces `probability`, `event`, `outcome`, and the single-event how-to.
- **D5** requires pulling the D3 expected-cost figures forward and rendering them as a comparable visual (bars, a tree, or equivalent) — the antecedent computation is impossible without the percent/expected-value arithmetic already forced in D3, and the deliverable specifically requires the *display* step (labeled axes/branches, not a pasted table). Genuinely forces `how-to-find-the-percent-of-a-number` as the computation the visual is built from.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 9    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

See `case.json.reinforcement_note` for the full accounting. Every claimed skill was checked against
`readmodel/standards_spine.json` before writing and none is `n == 0` (lowest is `dependent-event`
and `conditional-probability` at n=3, and the compound-event how-to at n=4) — this case reinforces
skills the spine already has some coverage for rather than closing a true zero-coverage gap. This is
a **deviation from the concept sheet**: `CONCEPTS_life-skills-first10_2026-09-03.md` concept #4 lists
`conditional-probability` (n=3) and the compound-event how-to (n=4) as skills the case "would close"
— read as low-coverage at concept-approval time, but neither is `n == 0`, so neither clears the
write-time bar for `new_coverage[]` (SPEC §7: "the reason the case exists"). The full `n == 0` list
in the spine was checked (number-sense-depth, number-sense-digit, geometry-how-to-find-the-volume-of-
a-sphere, calculus's quotient-rule how-to, calculus-taylor-series and its how-to) and nothing fits a
car-maintenance probability/expected-cost case without padding. `new_coverage[]` is `[]`, honestly,
per the reinforcement carve-out (T1-10, `skills/case-readiness/SKILL.md`, 2026-08-17) — the same
pattern used in `cases/a-coachs-dilemma/LEARNING_GOALS.md`. The case still closes the *topic* gap
named in the concept sheet (car-maintenance economics, previously zero coverage in the corpus); it
does not additionally close a *skill* gap, and that distinction is flagged here for the project
owner rather than papered over.
