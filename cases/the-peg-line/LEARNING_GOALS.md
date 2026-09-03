# LEARNING_GOALS.md — The Peg Line

Bidirectional deliverable ↔ skill matrix (SPEC §7 / case-write step 10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — scientific-notation reserve table (reserve total + both options' annual dollar yield) | advanced-operations-scientific-notation, advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation |
| D2 — absolute-value peg-deviation worksheet (five price snapshots) | advanced-operations-absolute-value, advanced-operations-how-to-evaluate-an-absolute-value-expression |
| D3 — yield-per-risk efficiency table (D1 ÷ Appendix E's duration-scaled risk figures, both options) | advanced-operations-scientific-notation, advanced-operations-absolute-value |
| D4 — sensitivity check (recompute D3 with Appendix E's alternate scaling readings) | advanced-operations-absolute-value, advanced-operations-how-to-evaluate-an-absolute-value-expression |
| D5 — recommendation memo (defended with D1, D3/D4, Appendix A) | advanced-operations-scientific-notation, advanced-operations-absolute-value |

**Forcing test applied:** *could a competent student produce this deliverable correctly without
ever performing this skill?* For each mapping above, no — D1 cannot be written without actually
converting a ten-digit dollar figure into scientific notation, correctly placing the decimal and
counting the exponent; D2 cannot be written without evaluating `|price − $1.00|` as an
absolute-value expression for each of five distinct price points, several of which are below
$1.00 and several above, forcing genuine engagement with the "distance from zero" meaning of
absolute value rather than a same-sign shortcut; D3 requires taking D1's scientific-notation
dollar figures and D2's basis-point figures and actually dividing one by the other for both
options — a student who never correctly built D1 or D2 cannot produce a correct D3 table; D4
requires re-running that same division with a different real input and comparing the two results,
which is impossible without having actually understood what D3's ratio represents, not just
copied a number; D5 requires weighing D1's real dollar gap against D3/D4's real efficiency gap
and Appendix A's legal-ceiling fact together — a student who never engaged with what the
scientific-notation dollar figures and the absolute-value deviation figures actually represent
cannot write a defensible memo.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 4    new_coverage: 0 (thickening — see note below)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**new_coverage note.** All 4 claimed skills (`advanced-operations-scientific-notation`,
`advanced-operations-absolute-value`, `advanced-operations-how-to-evaluate-an-absolute-value-expression`,
`advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation`)
already show `n≥1` in `readmodel/standards_spine.json`. This is expected and was flagged from the
start in the concept sheet (`CONCEPTS_pim-sector-gaps_2026-08-24.md`, C6): coverage score **0.0**,
explicitly logged as "0 new / thickens 8" — this case exists to *thicken* a thin
(Scientific Notation/Factorial/Absolute Value) group from n≈1–2 toward n≈2–3, not to close a
zero-coverage gap. `new_coverage[]` is correctly `[]` per SPEC §4's literal rule (a skill already
at `n≥1` cannot be claimed as newly-closed) — this is not a deviation requiring special disclosure
the way `prove-it-scales`'s reinforcement case was, since the concept sheet itself designated this
case as a thickening pass up front, not as an after-the-fact reclassification.

## Balance-test note for readiness stage

**UPDATED 2026-09-01 (balance-retune redesign pass).** The original version of this case had
`margin_pct` = 97.47% — well past SPEC §2's ~20% cap, produced by mixing a normal-drift reference
figure for Option A against an unrelated historical-crisis figure for Option B. Per explicit
project-owner instruction, the dilemma was redesigned rather than waived: Option B's maturity moved
from 13-week to 6-week Treasury bills, and the risk metric was redefined so both options are
measured on the same kind of risk (interest-rate/duration exposure), with Option B's figure derived
from Option A's own real reference number via a real, citable scaling method (the square-root-of-
time rule, S9). The redesigned case's `margin_pct` = 17.04%, under SPEC §2's ~20% cap.

The case's forcing test still passes cleanly (every deliverable genuinely requires the claimed
skill — see the table above, unchanged in substance by the redesign). What changed is that the
case's Socratic "defensible ambiguity" (SPEC §0) is now carried by a genuinely close quantitative
race *in addition to* a qualitative argument, rather than by the qualitative argument alone: D4's
sensitivity check (Appendix E's alternate risk-scaling readings) shows the recommendation actually
flips under one real, defensible alternate assumption. Full retune history in `RESEARCH_LOG.md`.
