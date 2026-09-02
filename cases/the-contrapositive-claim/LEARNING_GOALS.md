# Learning Goals — The Contrapositive Claim

Bidirectional deliverable ↔ skill matrix, per SPEC §1.7 and case-write step 10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — logic reference sheet (clause as p → q, plus converse/inverse/contrapositive) | discrete-mathematics-conditional-statement, discrete-mathematics-how-to-determine-the-converse-inverse-and-contrapositive-of-a-conditional-statement |
| D2 — single truth table covering all four candidate rules | discrete-mathematics-truth-table, discrete-mathematics-how-to-construct-a-truth-table-for-a-compound-statement |
| D3 — negation table for the four candidate rules' conclusions | discrete-mathematics-negation, discrete-mathematics-conditional-statement |
| D4 — classification memo (appeal scenarios as conjunction/disjunction compound claims, evaluated against D2) | discrete-mathematics-conjunction, discrete-mathematics-disjunction, discrete-mathematics-truth-table |
| D5 — wrongly-denied-claims-caught count under each candidate rule | discrete-mathematics-conditional-statement, discrete-mathematics-how-to-determine-the-converse-inverse-and-contrapositive-of-a-conditional-statement |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 7    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Reasoning behind "forces," per deliverable:**

- **D1** cannot be produced correctly without applying the how-to for converse/inverse/contrapositive
  directly to the case's own clause, and cannot be written up at all without first casting the
  clause as a labeled conditional statement (p, q).
- **D2** cannot be produced correctly without following the row-generation procedure a truth table
  requires, and the deliverable *is* a truth table — the term is unavoidable.
- **D3** requires negating each rule's conclusion correctly, which a student who has not learned
  negation as its own operation (distinct from just "the opposite-sounding rule") will get wrong on
  the inverse specifically — that confusion is the whole point of the deliverable.
- **D4** requires translating "and"/"or" claim-fact combinations into symbolic conjunctions and
  disjunctions and then reading their truth value off D2's table — a student who has not learned
  conjunction and disjunction as distinct operations cannot produce a correct evaluation, only a
  plausible-sounding guess.
- **D5** requires applying whichever of D1's four rules is under test to classify each of Appendix
  E's rows — this is the how-to skill applied at scale, not just derived once.

## new_coverage note

`new_coverage[]` is set to `[]` for this case. All seven claimed skill ids currently show `n = 1`
in `readmodel/standards_spine.json` (Discrete Mathematics / Formal Logic), not `n = 0` — this case
is deliberately a **reinforcement pass** on a group that is already minimally covered, per explicit
authoring instruction, rather than a first-coverage case. See `reinforcement_note` in `case.json`.
