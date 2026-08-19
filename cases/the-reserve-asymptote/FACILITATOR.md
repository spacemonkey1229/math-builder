# FACILITATOR.md — The Reserve Asymptote

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

## Argument for A (The Smooth Curve)

Cheap, fast, and — outside the age-100 boundary — nearly indistinguishable from the real
published table. Its formula is anchored to the two real data points Highline actually has
experience with (ages 90 and 99), it has never triggered a regulatory objection on any other
Highline filing, and it never needs a special case: one equation, every age, 0 to 120. A
reasonable actuary can point out that regulators evaluate a *filed methodology*, and a smooth,
well-behaved formula is easier to defend in a review meeting than "the number jumps here because
the table says so."

## Argument for B (The Full Table)

It is what the actual, real, published mortality table says — nothing modeled, nothing smoothed,
nothing assumed away. The table's closing convention at "100 and over" is not a quirk; it is how
every published life table has to end, and a regulator's own actuary will recognize it
immediately. Filing a method that quietly smooths past a boundary the source data doesn't smooth
past is a real audit exposure, even if the blended dollar impact looks small. "It matches the
table" is a complete defense. "It's close enough in aggregate" is not, if a regulator checks
cohort by cohort.

## The margin

**Method A:** $208.36 reserve required per $1,000 of face value, blended across Highline's full
in-force block. **Method B:** $210.41. **Margin: 0.97%** — well under SPEC §2's 20% cap, and
close enough that neither side has an obviously dominant case on the aggregate number alone.

What makes this case work is that the aggregate margin (0.97%) and the single-cohort margin (at
attained age 100 alone: $652.73 gap per $1,000 of face, a **188% relative difference**) tell two
completely different stories from the same data. 95.7% of the *entire* portfolio-wide dollar
difference between the two methods comes from just 8 of Highline's 534 in-force contracts — the
ones sitting exactly on the boundary this filing year.

## Five Socratic questions

1. Your blended margin between the two methods is under 1%. If a regulator only checked the
   aggregate reserve number, would that settle the question — and if they check reserve adequacy
   cohort by cohort instead, does your answer change?
2. The Smooth Curve formula was built to match the real table exactly at ages 90 and 99. If it
   matches so well at both ends, why does it miss so badly at age 100?
3. At what attained age does the Full Table function actually become discontinuous, and what
   real fact about how the source table was built explains why the discontinuity is there instead
   of somewhere else?
4. If Highline's Horizon Series block had twice as many contracts issued at exactly age 100 this
   year instead of 8, what would happen to the 0.97% margin — and would the Smooth Curve still be
   defensible?
5. The Smooth Curve's own equation has a horizontal asymptote of $1,000 per $1,000 of face value
   — the same ultimate number the Full Table jumps to. If both methods agree on where the cost is
   eventually headed, what exactly are they disagreeing about?

## The trap

Heroes will compute the 0.97% aggregate margin, correctly note it's well under any reasonable
materiality threshold, and conclude the choice "barely matters" — missing that nearly all of that
0.97% (95.7% of the total dollar gap) is concentrated in a single 8-contract cohort, and that
statutory reserve adequacy is generally assessed cohort by cohort, not only in aggregate. A
company can be technically deficient at one attained age even while its overall block reserve
looks comfortable. The trap is treating "small in aggregate" as the whole answer instead of asking
*where* the smallness comes from.

A second, subtler trap: Heroes may assume the two methods disagree about *where mortality cost is
eventually headed* — that the Smooth Curve underestimates the long-run risk. It doesn't. Both
methods share the same ultimate asymptote ($1,000 per $1,000 face, i.e., eventual certainty of
death). They disagree only about *whether that value is reached smoothly or abruptly*, and *at
what specific age*. A Hero who argues "the Smooth Curve is wrong about the long-run risk" has
misread the math — Discussion Question 5 exists specifically to catch this.

## Sensitivity note (SPEC §6)

LOW. This case's math never asks a student to reason about any individual's death — every figure
is an aggregate, population-level mortality statistic from a published national table, used to
price an insurance reserve. Keep classroom framing on the pricing/regulatory decision. See
`case.json.sensitivity_note` for the recorded flag.
