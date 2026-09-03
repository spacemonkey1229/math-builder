# LEARNING_GOALS.md — The Course Correction

Bidirectional deliverable ↔ skill matrix (SPEC §7 / case-write step 10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — current-vector table (magnitude + direction, resolved to E/N components) | pre-calculus-vector, pre-calculus-magnitude-of-a-vector, pre-calculus-how-to-find-the-magnitude-and-direction-of-a-vector |
| D2 — course unit-vector table + each option's heading vector | pre-calculus-vector, pre-calculus-unit-vector |
| D3 — resultant-velocity table for The Steady Burn (vector addition + dot-product split) | pre-calculus-dot-product, pre-calculus-how-to-add-and-subtract-vectors, pre-calculus-how-to-find-the-dot-product-of-two-vectors |
| D4 — vector diagram, both options, drawn to scale with angles labeled | pre-calculus-vector, pre-calculus-how-to-add-and-subtract-vectors |
| D5 — fuel-cost table + weather-window statement | pre-calculus-magnitude-of-a-vector, pre-calculus-dot-product |

**Forcing test applied:** *could a competent student produce this deliverable correctly without
ever performing this skill?* For each mapping above, no — D1 cannot be written without actually
converting a magnitude-and-direction reading into east/north components (the magnitude-and-
direction how-to, applied in reverse to build components rather than extract them); D2 requires
constructing a genuine unit vector and showing its magnitude is exactly one, not just naming a
bearing; D3 cannot be completed without adding two vectors component-wise and then computing a
real dot product against the course unit vector to separate along-track from cross-track motion —
a student who skips the dot product cannot explain why The Steady Burn doesn't arrive where it's
pointed; D4 requires actually drawing the head-to-tail vector addition/subtraction that D1-D3
computed numerically, not just labeling a sketch; D5 requires carrying D1-D4's vector magnitudes
into a real cost figure and using the along-track component from D3 to defend a schedule claim — a
student who never separated along-track from cross-track progress cannot correctly state whether
Option B makes the window.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 7    new_coverage: 0 (reinforcement — see note below)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**new_coverage note.** All 7 claimed skills (`pre-calculus-vector`, `pre-calculus-magnitude-of-a-vector`,
`pre-calculus-unit-vector`, `pre-calculus-dot-product`, and their three how-tos) already show `n=2`
in `readmodel/standards_spine.json` (covered_by: `["Wind Triangle", "Crosswind Cut"]`) — not `n=1`
as the concept sheet stated when it was written (a second Vectors case, Crosswind Cut, had already
landed in the corpus by the time this case was authored; see `case.json.reinforcement_note`).
`new_coverage[]` is therefore set to `[]` per SPEC §4's literal rule (a skill already at `n>=1`
cannot be claimed as newly-closed). This case exists to *reinforce* the Vectors group further (from
n=2 to n=3 on all 7 skills), matching the concept sheet's own stated intent ("thickens the entire
Vectors group") even though its count of prior coverage was off by one case. This is a disclosed
deviation, flagged for `case-qa` to confirm rather than silently treated as a normal
zero-new-coverage case.
