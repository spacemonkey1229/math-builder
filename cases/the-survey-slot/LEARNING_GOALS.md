# Learning Goals — The Survey Slot

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 compound-probability calculation, at least one of 12 independent fields | statistics-and-probability-independent-event, statistics-and-probability-how-to-determine-the-probability-of-a-compound-event, statistics-and-probability-theoretical-probability |
| D2 single-event probability for The Candidate Watch | statistics-and-probability-theoretical-probability, statistics-and-probability-experimental-probability |
| D3 expected-detections-per-hour comparison and percent margin | statistics-and-probability-how-to-determine-the-probability-of-a-compound-event |
| D4 follow-up combinations-and-permutations plan | statistics-and-probability-permutation, statistics-and-probability-combination, statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination, statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-permutation |
| D5 standard-notation data table + filtering | advanced-operations-standard-notation, advanced-operations-how-to-write-a-number-in-standard-notation-given-its-scientific-notation, advanced-operations-scientific-notation |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced correctly without recognizing each of the twelve fields as an **independent event** (one field's outcome does not affect another's) and without applying the **compound-event** complement rule (`P(at least one) = 1 - P(none)`), which is also where **theoretical probability** is exercised — the student computes the probability from the stated per-field rate, not from an experiment. A student who instead multiplies the per-field probability by 12 and reports that as "the probability" has not performed this skill correctly and will get an answer over 100%, which the deliverable explicitly asks them to notice is impossible. Genuinely forces `independent-event`, `how-to-determine-the-probability-of-a-compound-event`, `theoretical-probability`.
- **D2** requires stating a single-event probability directly from Appendix C's given rate (`theoretical-probability` — reasoning from the stated population rate, not from repeated trials) while also requiring the student to recognize that this stated rate is itself grounded in the *observed*, historical outcomes of a real completed survey (`experimental-probability` — Appendix A's TESS follow-up results are a real record of what actually happened to 2,241 real candidates, not a theoretical model). A student who cannot distinguish "the theoretical probability I am told to use for tonight's candidate" from "the experimental record that number came from" has not engaged with either skill correctly. Genuinely forces `theoretical-probability`, `experimental-probability`.
- **D3** requires correctly combining D1's compound-event probability and D2's single-event probability into comparable per-hour rates — a student who has not correctly performed the compound-event calculation in D1 cannot produce a correct D3 comparison, since D3's Sweep number is D1's answer divided by the slot length. Genuinely forces `how-to-determine-the-probability-of-a-compound-event` (applied, not just computed once).
- **D4** cannot be produced without correctly distinguishing an unordered selection (which fields get chosen for follow-up — a **combination**) from an ordered one (what sequence those chosen fields get observed in — a **permutation**). A student who computes only one of the two counts, or who treats "choose 2 of 5" and "arrange 2 of 5 in order" as the same calculation, has not performed both how-tos. The deliverable's explanation requirement ("why exhaustive follow-up isn't realistic") only works if the student has the actual combination count in hand, not a guess. Genuinely forces `permutation`, `combination`, `how-to-determine-the-number-of-outcomes-of-a-combination`, `how-to-determine-the-number-of-outcomes-of-a-permutation`.
- **D5** cannot be produced without converting a value given in **scientific notation** into **standard notation** — a student who leaves the values in `6.13 × 10⁻⁴` form, or who mis-shifts the decimal point, has not performed `how-to-write-a-number-in-standard-notation-given-its-scientific-notation`. The deliverable's filtering half (identifying unneeded columns in Appendix C, not Appendix E) requires the student to have actually understood which values are load-bearing to D1–D3 versus texture. Genuinely forces `standard-notation`, `how-to-write-a-number-in-standard-notation-given-its-scientific-notation`, `scientific-notation`.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 11    new_coverage: 0 (see case.json.reinforcement_note)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

A fresh, live read of `readmodel/standards_spine.json` at case-write time (2026-09-18) found all six
targeted Statistics And Probability/Probability and Advanced Operations skills — `independent-event`,
`permutation`, `how-to-determine-the-number-of-outcomes-of-a-combination`,
`how-to-determine-the-number-of-outcomes-of-a-permutation`, `standard-notation`, and
`how-to-write-a-number-in-standard-notation-given-its-scientific-notation` — already at **n=2**
(`covered_by` length 2 each), not `n=0`. `new_coverage[]` requires true `n==0` (case-write's own
instruction: "Record which claimed skills currently have n == 0"); `n<=2` is `gap_queue.json`'s
separate "thin" convention, which the concept sheet correctly used to *score* this concept but which
does not by itself make a skill eligible for `new_coverage[]`. This session's own earlier spine-wide
sweep (recorded in `cases/the-manifest-split/case.json`) already found that literally no skill
anywhere in the 437-skill spine currently sits at true `n==0`. Per the reinforcement carve-out
(T1-10, `skills/case-readiness/SKILL.md`, "The reinforcement carve-out on T1-10," added 2026-08-17),
`new_coverage[]` is honestly recorded as empty rather than padded with a false zero-coverage claim.
All 6 claimed thin skills are still genuinely forced by the deliverables above (see the forces-test),
and this case still closes 4/4 of the Probability group's remaining thin (n<=2) set plus 2/2 of the
targeted Advanced Operations thin set, exactly as the concept sheet scored it.
