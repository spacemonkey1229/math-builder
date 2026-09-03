# LEARNING_GOALS.md — The Bot Farm

Bidirectional deliverable ↔ skill matrix (SPEC §7 / case-write step 10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Ring Alpha's adjacency matrix, dimensions stated | pre-calculus-matrix, pre-calculus-matrix-dimension |
| D2 — Wave Nine's adjacency matrix, dimensions stated | pre-calculus-matrix, pre-calculus-matrix-dimension |
| D3 — degree table (row sums) and connectivity density for both clusters | pre-calculus-how-to-add-and-multiply-matrices |
| D4 — density-interpretation memo against real published benchmarks | pre-calculus-how-to-add-and-multiply-matrices, pre-calculus-matrix |
| D5 — recommendation memo, confirmed-bots-per-false-positive computed for both clusters | pre-calculus-how-to-add-and-multiply-matrices |

**Forcing test applied:** *could a competent student produce this deliverable correctly without
ever performing this skill?* No, for each mapping above. D1/D2 cannot be produced without actually
building a matrix from a stated connection list and correctly stating its row×column dimensions —
skipping straight to "it looks dense" produces no matrix at all. D3 requires computing each
account's degree as a literal row sum (equivalently, the adjacency matrix multiplied by a
ones-vector) — a student who only eyeballs "which grid looks fuller" has not performed the skill.
D4 requires using D3's actual computed density numbers, not a visual impression, to engage with
Appendix D's real published AUC figures. D5 requires carrying the matrix-derived density findings
into the final recommendation, not just restating Appendix E's table.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 3    new_coverage: 0 (reinforcement — see note below)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**new_coverage note.** All 3 claimed skills (`pre-calculus-matrix`, `pre-calculus-matrix-dimension`,
`pre-calculus-how-to-add-and-multiply-matrices`) already show `n=2` in `readmodel/standards_spine.json`,
covered by "The Multiplier Recruit" and "The Skin Pack Atlas". `new_coverage[]` is therefore
correctly `[]` per SPEC §4's literal rule (a skill already at `n>=1` cannot be claimed as
newly-closed), matching the source concept sheet's own explicit "0 new skills — thickens Matrices"
framing for this concept (C8, `CONCEPTS_formal-logic-vectors-matrices-numbertheory_2026-08-23.md`).

**Scoping note (judgment call, disclosed).** The Matrices group has 7 skills total; this case uses
only 3 (matrix, matrix-dimension, how-to-add-and-multiply-matrices), not all 7. Two sibling concepts
in the same sheet (C6, C7) explicitly claim all 7 via a system-of-equations or matrix-arithmetic
application; C8's own write-up scopes itself more narrowly ("representing a small social graph as
an adjacency matrix and computing row/column sums directly from it") and never claims determinant,
identity-matrix, or system-of-equations coverage. This case's author found no honest, non-contrived
way to force those three skills into a bot-cluster-suspension adjacency-matrix dilemma, and chose
not to force-fit them. See `case.json.reinforcement_note` for the full record.
