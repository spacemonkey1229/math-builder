# Learning Goals — The Schedule Explosion

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 factorial table across job counts | advanced-operations-factorial, advanced-operations-how-to-evaluate-a-factorial-expression |
| D2 convert n! into search time, find feasibility crossing | advanced-operations-how-to-evaluate-a-factorial-expression |
| D3 six-job exhaustive search (Full Sweep) + nearest-neighbor (Greedy Queue) + percent margin | advanced-operations-factorial, advanced-operations-how-to-evaluate-a-factorial-expression |
| D4 written "wait for faster computers" explanation, defining factorial | advanced-operations-factorial |
| D5 original visual (log-scale explosion chart) | advanced-operations-how-to-evaluate-a-factorial-expression |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced without actually evaluating n! (a product of consecutive integers) for eight different job counts and showing the method for at least three — a student who instead guesses, estimates, or looks up pre-computed values instead of demonstrating the evaluation method has not produced this deliverable. Forces `factorial` (the vocabulary/definition being applied) and its how-to directly.
- **D2** is impossible without a correct D1 value for each job count — a student who has not correctly evaluated n! cannot correctly convert it into a search-time estimate, and the deliverable's core ask (find the exact job count where the strategy stops fitting the eight-hour window) only resolves once the factorial values are right. Forces the factorial how-to (applying the evaluated values); does not independently force the vocabulary term beyond what D1 already established, so it is mapped to the how-to only.
- **D3** requires the student to first restate 6! and use that specific value to justify why an exhaustive search of the six-job batch is possible at all (Appendix A) — a student who skips this step and just starts listing orderings without connecting the count of orderings to 6! has not completed the deliverable as written, which explicitly requires the restatement and confirmation step. The exhaustive search and nearest-neighbor computation that follow depend on correctly knowing there are exactly 720 orderings to check. Forces `factorial` and its how-to.
- **D4** requires the student to state, in their own words, what a factorial is and why it grows the way it does, and to use specific job-count/search-time pairs from D2 to make the argument — a student who writes a vague "it gets really big" answer without a real definition of factorial has not completed this deliverable, which explicitly requires the definition. Forces `factorial` directly.
- **D5** requires plotting the actual n!/search-time values the student computed in D1/D2 — a chart built from any other numbers, or a chart that does not correctly reflect the shape of factorial growth (which a student who never correctly evaluated the factorials could not produce), is not this deliverable. Forces the factorial how-to.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 2    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

See `case.json.reinforcement_note` for the full accounting. Both claimed skills
(`advanced-operations-factorial`, `advanced-operations-how-to-evaluate-a-factorial-expression`) were
checked against `readmodel/standards_spine.json` before writing and neither is `n == 0` (both sit at
`n=1`) — this case reinforces the Advanced Operations / "Scientific Notation, Factorial, Absolute
Value" group's Factorial half specifically, per the task's explicit instruction to target Factorial
(not Scientific Notation, which is reserved for `cases/the-yield-die`, confirmed not to exist yet in
this corpus as of 2026-09-09 — checked directly before writing `standards[]`). `new_coverage[]` is
`[]`, honestly, per the reinforcement carve-out (T1-10, `skills/case-readiness/SKILL.md`,
2026-08-17) — the same pattern used in `cases/the-minimum-payment-trap/case.json`,
`cases/the-deferred-repair/case.json`, and `cases/the-two-offers/case.json`. The case still closes
the *topic* gap named in the approved concept sheet (Advanced Operations / Factorial); it does not
additionally close a *skill* gap (neither claimed skill was at n=0), and that distinction is flagged
here for the project owner rather than papered over.
