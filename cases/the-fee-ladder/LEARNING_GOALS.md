# LEARNING_GOALS.md — The Fee Ladder

Bidirectional deliverable ↔ skill matrix (SPEC §7 / case-write step 10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — recursive formula for the balance sequence, walked tier by tier | discrete-mathematics-recursive-formula, discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence |
| D2 — explicit (non-recursive) formula, derived by substitution from D1 | discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula |
| D3 — fee-quote error table (Quick-Quote vs. Full Ladder, today's client) | discrete-mathematics-recursive-formula, discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula |
| D4 — sensitivity check across client sizes, explained via D2's formula | discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula |
| D5 — recommendation memo, defended with D3/D4 and Appendix A/F | discrete-mathematics-recursive-formula, discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence, discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula |

**Forcing test applied:** *could a competent student produce this deliverable correctly without
ever performing this skill?* For each mapping above, no — D1 cannot be written without stating an
actual recursive rule (Bₖ in terms of Bₖ₋₁) and applying it four times in sequence; D2 requires
literally substituting the recursive rule into itself until no recursive term remains, which is the
mechanical definition of "converting a recursive formula to an explicit formula," not just restating
D1's answer; D3 requires using both D1's (or D2's) computed total and Appendix B's flat rate side by
side, so a student who never built the recursion has no true total to compare against; D4 requires
re-applying D2's explicit formula (not just D1's step-by-step walk, which would be slow to repeat
three times) to two more AUC values and explaining the size-invariance result algebraically; D5
requires weighing D3/D4's real, computed error against Appendix A's deadline and Appendix F's
precedent — a student who never actually computed the true recursive fee cannot state how large the
error being weighed even is.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 3    new_coverage: 0 (reinforcement — see note below)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**new_coverage note.** All 3 claimed skills (`discrete-mathematics-recursive-formula`,
`discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence`,
`discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula`) already show
`n=2` in `readmodel/standards_spine.json` (covered_by: `["Life Insurance", "Redrawing Lines"]`) as
of this case's authoring — the source concept sheet (`CONCEPTS_pim-sector-gaps_2026-08-24.md`, C4)
was written when these skills were at `n≈1`; the spine has since moved to `n=2` via other
case-authoring work in the pipeline. `new_coverage[]` is therefore correctly `[]` per SPEC §4's
literal rule (a skill already at `n>=1` cannot be claimed as newly-closed), and `case.json` carries
a `reinforcement_note` explaining that this case's actual, honest effect is thickening the Proof
And Recursion group's three recursive-formula skills from `n=2` toward `n=3` via a genuine
recursive-to-explicit conversion (not a contrived one, per the concept sheet's own framing) — not
closing a zero-coverage gap. This is a disclosed deviation, flagged here for `case-qa` to confirm
rather than silently treated as a normal zero-new-coverage case.
