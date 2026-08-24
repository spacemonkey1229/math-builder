# Guide Notes: The Placement Test

**Case:** The Placement Test · **Tier:** T2 (MS-core) · **Studio:** Adventure
**Standards:** Statistics And Probability/Probability — Permutation / How to determine the number
of outcomes of a permutation; Basic Operations/Division — Division / How to divide decimal
numbers; Advanced Numbers/Percents — Percent / How to find the percent of a number (see
`case.json.standards[]` for exact ids)

Drafted at write time, 2026-08-24. Numbers below are **not yet sourced** — every figure this
document references is `{{NEEDS_SOURCE}}` in `case.md` until `case-research` runs. This document
states the *shape* of both arguments and the *basis* for the margin; it does not and cannot state
a margin percentage yet.

## Argument for A — The Straight Cut

The Straight Cut spends the entire fixed test budget on one variant. Once that variant's spend
clears the ad platform's minimum recommended threshold (Appendix C), its conversion-rate read is
the single most statistically reliable number this campaign can produce this quarter — no other
variant is diluting the sample. The honest weakness: it can only ever confirm or deny one
hypothesis (this placement timing, this call-to-action style). It cannot tell Jaylen whether a
different combination would have converted better, because no other combination is ever run.

## Argument for B — The Full Rotation

The Full Rotation is the only plan that can actually answer the question Jaylen's growth lead is
asking — which lever (placement timing, call-to-action style, or their interaction) actually
drives conversion — because it is the only plan that tests more than one combination. The honest
weakness: splitting one fixed budget six ways means each variant's per-variant spend has to clear
Appendix C's minimum threshold on a sixth of the money. Any variant whose split spend falls short
of that threshold produces a conversion-rate estimate too noisy to act on — and a plan that spreads
itself past the point where its own variants clear the reliability bar has quietly traded real
signal for the appearance of more signal.

## The margin

`margin_basis` (also recorded in `case.json.balance`): once Appendices B, C and D are sourced,
compare statistically attributable conversions per dollar of ad spend for The Straight Cut (1
variant at full budget) against The Full Rotation (6 variants at one-sixth budget each, with any
variant that fails to clear Appendix C's minimum-spend threshold flagged as non-statistically-usable
and excluded from the attributable-conversions total, not silently counted at face value). Until
`case-research` fills Appendices B, C and D, `margin_pct` stays `null` — do not guess a number
here.

## Five Socratic questions

1. The Full Rotation tests six variants instead of one. If every one of those six variants clears
   the platform's minimum-spend threshold, is there still any reason to prefer The Straight Cut?
2. You computed the number of distinct production-order sequences for the three placement-timing
   cuts in D1. Why does that number matter to Jaylen's decision, if the team only ever needs to
   pick *one* order to actually produce?
3. Suppose one of The Full Rotation's six variants comes in just under Appendix C's minimum-spend
   threshold. What should Jaylen do with that variant's conversion numbers — report them anyway,
   throw them out, or something else — and why?
4. The Straight Cut and The Full Rotation draw from the exact same total budget. What would have
   to be true about the six variants' individual conversion rates for The Full Rotation to still
   win on conversions-per-dollar despite splitting that budget six ways?
5. If the finance team doubled the fixed test budget for next quarter without changing anything
   else, would you expect that to change which plan wins — and if so, which one does it help more?

## The trap

A Hero can correctly compute D1's permutation count, correctly build D2's budget split, and still
recommend The Full Rotation on the reasoning "more variants tested is more information, so it must
be the better plan" — without ever checking D3, whether each of those six thinner budgets actually
clears the platform's minimum-spend threshold. Six variants that each individually produce
unusable, noise-level conversion estimates are not six times the information; they can be closer
to *no* usable information at all, while still costing the full budget. Watch for a pitch that
cites "six variants tested" as the win condition without ever reporting D3's clearance percentages.

## Sensitivity note

**SPEC §6: NONE.** This case is routine marketing-analytics math — which paid-placement test plan
a brand strategist runs against a fixed budget. No protected subject matter, no facilitator content
flag needed beyond ordinary classroom awareness.

## Facilitator note — coverage

Both claimed permutation skills (`statistics-and-probability-permutation` and
`statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-permutation`) were
already at `n=1` (covered once, by `Codebreaker`) before this case was written, so
`case.json.new_coverage[]` is an empty array — this case closes no coverage gap. It was written
anyway per the approved concept sheet, which explicitly authorized an empty `new_coverage[]` as
long as it is flagged (see `LEARNING_GOALS.md` for the full flag and `n` values verified against
`readmodel/standards_spine.json`).
