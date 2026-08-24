# Learning Goals — The Placement Test

Bidirectional deliverable ↔ skill matrix. Every Challenge-3 deliverable must map to a claimed
spine skill; every claimed skill must be forced by at least one deliverable.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — production-order permutation calculation | statistics-and-probability-permutation, statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-permutation |
| D2 — budget-per-variant table | basic-operations-division, advanced-numbers-how-to-divide-decimal-numbers |
| D3 — minimum-viable-spend clearance table | advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number |
| D4 — final recommendation table (conversions per dollar) | advanced-numbers-how-to-divide-decimal-numbers |

**"Forces" test applied to each row:**

- D1: a student cannot produce a defensible count of "how many distinct production-order
  sequences are possible" without knowing what a permutation is (order matters, no repeats,
  drawn from a fixed set of three cuts) and without applying the permutation formula to the
  actual number of production weeks available — both the term and the how-to are load-bearing to
  the artifact itself, not decoration. This is the calculation the case explicitly turns on: it
  is what shows Jaylen (and the student) that the space of possible test designs is far larger
  than the fixed budget and fixed production calendar can actually absorb.
- D2: splitting a single fixed dollar budget one way versus six ways cannot be shown "with the
  arithmetic shown" without performing division on a decimal dollar amount — a student who never
  divides has nothing to put in the table.
- D3: "what percent of the threshold does this budget represent" is literally the percent-of-a-number
  operation; a student cannot produce the clearance table without converting a per-variant dollar
  figure into a percent of Appendix C's threshold.
- D4: the conversions-per-dollar figure for each plan is itself a division of a (decimal) dollar
  amount, reinforcing D2's how-to skill from a new angle (a rate rather than a straight split); it
  introduces no new spine skill of its own, matching the reinforcement pattern used elsewhere in
  this project (e.g. The Multiplier Recruit's D5).

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 6    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Flag on `new_coverage[]`:** both `statistics-and-probability-permutation` and
`statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-permutation` were
verified against `readmodel/standards_spine.json` before writing and confirmed `n=1` each
(covered once already, by `Codebreaker`), not `n=0`. The remaining four claimed skills
(`basic-operations-division`, `advanced-numbers-how-to-divide-decimal-numbers`,
`advanced-numbers-percent`, `advanced-numbers-how-to-find-the-percent-of-a-number`) are all
heavily covered elsewhere (n=29, n=29, n=50, n=53 respectively) and were never candidates for
`new_coverage[]`. Per SPEC §7, `new_coverage[]` must be non-empty for a case to have "a reason to
exist" in the coverage-gap sense — this case genuinely has none. It is written anyway because the
concept sheet explicitly authorized this outcome ("new_coverage[] may end up empty, which is
acceptable per SPEC §7 ONLY IF you flag it"), and per the concept sheet the case's real
justification is pedagogical (a genuine, load-bearing permutation application tied to a budget
decision), not coverage-gap closure. This is flagged here, in the final report, and in
`case.json.new_coverage`, which is left as an empty array rather than a false claim.
