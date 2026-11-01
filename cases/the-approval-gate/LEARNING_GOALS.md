# Learning Goals — The Approval Gate

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 truth tables for Option A and Option B's escalation rules, all 8 rows | discrete-mathematics-logical-statement, discrete-mathematics-conjunction, discrete-mathematics-disjunction, discrete-mathematics-negation, discrete-mathematics-truth-table, discrete-mathematics-how-to-construct-a-truth-table-for-a-compound-statement |
| D2 formal conditional + converse/inverse/contrapositive of the shared approval rule | discrete-mathematics-conditional-statement, discrete-mathematics-how-to-determine-the-converse-inverse-and-contrapositive-of-a-conditional-statement |
| D3 De Morgan's-Laws derivation + equivalence verdict citing truth-table rows | discrete-mathematics-negation, discrete-mathematics-conjunction, discrete-mathematics-disjunction, discrete-mathematics-truth-table |
| D4 monthly-volume table + total-expected-cost calculation per design | discrete-mathematics-truth-table, discrete-mathematics-logical-statement |
| D5 written recommendation in correct logical notation, addressing the equivalence trap | discrete-mathematics-conjunction, discrete-mathematics-disjunction, discrete-mathematics-negation, discrete-mathematics-conditional-statement, discrete-mathematics-logical-statement |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced without treating each rule as a genuine compound `logical statement` built from `conjunction` (∧) and `disjunction` (∨) of `negation`s (¬p, ¬q), organized into a real `truth table` via its own how-to procedure — a student who skips a row, mislabels a column, or guesses an output without evaluating the compound expression on that row has not produced this deliverable. Genuinely forces `logical-statement`, `conjunction`, `disjunction`, `negation`, `truth-table`, and the truth-table how-to.
- **D2** is impossible without stating a genuine `conditional statement` (if…then, →) and correctly applying the how-to procedure for converse/inverse/contrapositive — a student who writes the converse and the contrapositive as if they were the same statement, or who states the converse but calls it the contrapositive, has not met this deliverable even if their English interpretation sounds plausible. Genuinely forces `conditional-statement` and its how-to.
- **D3** requires actually applying De Morgan's Laws to `negate` a `conjunction` correctly, producing a `disjunction`, then verifying the result against the actual `truth table` built in D1 — a student who asserts equivalence (or non-equivalence) without pointing to a specific row has not performed this deliverable's own stated requirement. Genuinely forces `negation`, `conjunction`, `disjunction`, and `truth-table` as applied, load-bearing operations, not just vocabulary.
- **D4** requires using the `truth table`'s row-by-row classification (which category counts land in "Approve" vs. "Escalate" for each design) as the actual mechanism for sorting Appendix C's counts — a student who cannot correctly read the truth table cannot correctly split the request volume, and the entire cost comparison depends on getting this split right for each `logical statement` (each design's rule). Genuinely forces `truth-table` and `logical-statement` as the classification tool the arithmetic runs on.
- **D5** requires writing the recommendation in actual logical notation (∧, ∨, ¬, →) and explicitly naming the truth-table-vs-wording gap — a student who writes "they're basically the same rule" in plain English without ever notating p ∧ q ∧ ¬r, ¬p ∨ ¬q ∨ r, or ¬p ∧ ¬q ∧ r has not met this deliverable's own stated requirement, even if the dollar conclusion is right. Genuinely forces `conjunction`, `disjunction`, `negation`, `conditional-statement`, and `logical-statement` as the notation the paragraph must actually use.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 8    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

See `case.json.reinforcement_note` for the full accounting. Every one of the 8 claimed skills
(`discrete-mathematics-logical-statement`, `-conjunction`, `-disjunction`, `-negation`,
`-conditional-statement`, `-truth-table`,
`-how-to-construct-a-truth-table-for-a-compound-statement`,
`-how-to-determine-the-converse-inverse-and-contrapositive-of-a-conditional-statement`) was
checked against `readmodel/standards_spine.json` before writing and every one is `n = 2`, not
`n = 0` — this case reinforces a genuinely **thin** group (the concept sheet's own framing:
"8 of 8 skills thin (full close)") rather than closing a true zero-coverage gap. `new_coverage[]`
is `[]`, honestly, per the reinforcement carve-out (T1-10, `skills/case-readiness/SKILL.md`,
2026-08-17) — the same pattern used in `cases/the-overlap-send/LEARNING_GOALS.md`. Every one of
the 8 skills is genuinely forced by at least one deliverable (see the matrix and check above), so
landing this case takes the whole Discrete Mathematics / Formal Logic group from `n=2` to `n=3`
across the board.
