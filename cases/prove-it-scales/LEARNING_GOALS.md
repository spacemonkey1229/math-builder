# LEARNING_GOALS.md — Prove It Scales

Bidirectional deliverable ↔ skill matrix (SPEC §7 / case-write step 10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — induction proof (base case, inductive step, closing argument) | discrete-mathematics-mathematical-induction, discrete-mathematics-base-case, discrete-mathematics-inductive-step, discrete-mathematics-how-to-prove-a-statement-using-mathematical-induction |
| D2 — labeled recursion trace on a sample hierarchy | discrete-mathematics-base-case, discrete-mathematics-inductive-step |
| D3 — per-call cost interpretation, tied to the inductive step | discrete-mathematics-inductive-step |
| D4 — runtime comparison table, with inductive-step invocation counts | discrete-mathematics-base-case, discrete-mathematics-inductive-step |
| D5 — recommendation memo, defended with proof status + numbers | discrete-mathematics-mathematical-induction, discrete-mathematics-how-to-prove-a-statement-using-mathematical-induction |

**Forcing test applied:** *could a competent student produce this deliverable correctly without
ever performing this skill?* For each mapping above, no — D1 cannot be written without stating an
actual base case and inductive step and completing the induction argument; D2 requires locating
those same two structural elements inside a concrete trace; D3 explicitly requires reasoning from
the inductive step to interpret why per-call cost scales with depth; D4's added invocation-count
column requires counting inductive-step calls, not just copying benchmark numbers; D5 requires
weighing whether D1's induction guarantee (which holds regardless of runtime) is worth D4's runtime
cost (which does depend on runtime/TCO behavior) — a student who never engaged with what
"proven by induction" actually buys them cannot write this memo.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 4    new_coverage: 0 (reinforcement — see note below)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**new_coverage note.** All 4 claimed skills (`discrete-mathematics-mathematical-induction`,
`discrete-mathematics-base-case`, `discrete-mathematics-inductive-step`,
`discrete-mathematics-how-to-prove-a-statement-using-mathematical-induction`) already show `n=1`
in `readmodel/standards_spine.json`, covered by "Redrawing Lines." This is expected and was called
out explicitly in the write instructions for this case: `new_coverage[]` is set to `[]` per SPEC
§4's literal rule (a skill already at `n>=1` cannot be claimed as newly-closed), and `case.json`
carries a `reinforcement_note` explaining that this case exists to *reinforce* thin coverage (one
prior case) on a four-skill discrete-math group, not to close a zero-coverage gap. This is a
deliberate, disclosed deviation from SPEC §4's "no reason to exist" framing for this one case —
flagged for `case-qa` to confirm rather than silently treated as a normal zero-new-coverage case.
