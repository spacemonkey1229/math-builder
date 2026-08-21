# FACILITATOR.md — The Reserve Asymptote

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Reserve Asymptote · **Tier:** T3 (HS-entry/HS) · **Studio:** Heroes Academy
**Standards:** Pre-Calculus/Calculus — Limit, Asymptote, Continuity (Informal), One-Sided Limit,
Continuity, Discontinuity, and five "how to…" skills (see `case.json.standards[]` for exact ids).

Researched and margin-resolved 2026-08-18 (`margin_pct` = 0.97, see arithmetic below).

## Intro

Frame the format before the numbers: this is a one-shot filing decision with a hard deadline —
"You are Harlan Voss. Highline files its statutory reserve basis in eleven days. You can only
file one methodology. You have to recommend one tonight." Let that land before Launch.

## Launch

Put the two methods side by side with only the headline comparison visible: the Smooth Curve
(one formula, every age, never triggered a regulatory objection) vs. the Full Table (the actual
published mortality table, exactly as printed). Ask for a gut read: "Same underlying data, same
long-run destination. Which one do you file?" Do not correct an early answer yet — that instinct
is exactly what the case is built to test.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the Full Table — the one that jumps?" Show of hands,
both options, no discussion. Record the count for the Close re-vote.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What does 'better' mean here?"**

Let confusion grow here. Heroes will want to just ask which method is cheaper or easier to
compute, or note the two methods land close together in aggregate (0.97%) and call it a wash.
Push: "Harlan isn't being asked which formula is more convenient. He's being asked which one a
regulator's own actuary will accept as an honest description of the real table — cohort by
cohort, not just on average." If the room arrives at "we need to check more than the aggregate
number" on its own, the case is working.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has the right question, ask them to name the steps before opening Appendix B and
C: estimate the one-sided limit from the real table near age 100 (D1), find the Smooth Curve's
asymptote and its algebraic limit at age 100 (D2), test both functions for continuity at age 100
(D3), compute the single-cohort dollar gap (D4), then compute the portfolio-wide blended margin
(D5) and graph both functions (D6). Re-ask: "Now that we can see the steps — is our question
still the right one?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix F's three Modeling Assumptions honestly: MA1 (the Smooth Curve's exact formula
is not a real firm's proprietary parameters — it's a worked example in the real, named Kannisto
family, calibrated to the two real published data points at ages 90 and 99), MA2 (Highline's
in-force block size is invented, but its age *shape* is scaled from real CDC survivorship data),
MA3 (the case uses the CDC population table instead of the SOA industry-standard annuity table,
because the SOA table's specific digits could not be independently verified). Ask which one is
actually load-bearing for the *comparison* (MA1 and MA2 both are — a different calibration or a
different block shape changes the exact margin) and which one is a dataset substitution that
doesn't touch which method is continuous at age 100 (MA3).

## Data Deep Dive

Now, and only now, the numbers. Walk D1–D3 as a room (the one-sided table limit, the algebraic
asymptote limit, and the continuity test at age 100 for both functions), then split into two
desks for D4 and D5 — one computes the single-cohort dollar gap, one computes the portfolio-wide
blended margin — before reconvening to compare and for D6's graph.

**Facilitator-only arithmetic note.**

At attained age 100: $C_A(100) = 347.27$ (Smooth Curve, algebraic limit as $x\to100$, which
equals the formula's actual value there — continuous). $C_B(100) = 1000.00$ (Full Table, forced
by the "100 and over" closure convention, $q_{100}=1$ — the one-sided limit from below is
$\lim_{x\to100^-} C_B(x) = 329.65$, which does **not** equal $C_B(100)=1000.00$, so the Full
Table function is discontinuous — a jump discontinuity — at age 100).

**Single-cohort gap (D4).** $1000.00 - 347.27 = \mathbf{652.73}$ dollars per $1,000 of face, a
**188%** relative difference at that one age alone.

**Portfolio-wide margin (D5).** Blended across all 534 contracts / $534,000 of face: Method A
totals **$111,266.67**, Method B totals **$112,356.73**. Blended per-$1,000 rates: **$208.36**
(A) vs. **$210.41** (B). Margin: `margin_pct` = **0.97%**. The age-100 cohort's own dollar gap is
$5,221.84 (8 contracts × $652.73 per $1,000 face) — that figure is *larger* than the $1,090.06 net
gap between the two portfolio totals, because at every other age the two methods land close
together and largely cancel out; the age-100 cohort is where nearly all of the real disagreement
concentrates. The figure Heroes should land on is `age_100_cohort_share_of_total_gap_pct` =
**55.8%**: the share of the *absolute* dollar differences, summed age by age, that the age-100
cohort alone accounts for (see `case.json.balance.computed_values` for the exact reconciliation —
walk it from the per-age table, not by subtracting the two blended totals directly).

## Twist

**The aggregate margin and the single-cohort margin tell two different stories from the same
data.** A Hero who stops at D5's blended 0.97% margin — "these two methods barely disagree" — has
not yet seen that D4's single-cohort comparison shows a 188% relative gap at exactly the one age
where Highline has real survivors on the books this year, and that 55.8% of the *entire*
portfolio's dollar exposure to this choice sits in that one 8-contract cohort. The twist fires the
moment a Hero notices the case's real question is not "which method is bigger on average" but
"which method is honest at the boundary" — because statutory reserve adequacy is generally
checked cohort by cohort, not only in aggregate.

## The trap

Heroes will compute the 0.97% aggregate margin, correctly note it's well under any reasonable
materiality threshold, and conclude the choice "barely matters" — missing that nearly all of that
gap (55.8% of the total absolute dollar difference, summed age by age) is concentrated in a single
8-contract cohort, and that
statutory reserve adequacy is generally assessed cohort by cohort, not only in aggregate. A
company can be technically deficient at one attained age even while its overall block reserve
looks comfortable. The trap is treating "small in aggregate" as the whole answer instead of asking
*where* the smallness comes from.

A second, subtler trap: Heroes may assume the two methods disagree about *where mortality cost is
eventually headed* — that the Smooth Curve underestimates the long-run risk. It doesn't. Both
methods share the same ultimate asymptote ($1,000 per $1,000 face, i.e., eventual certainty of
death). They disagree only about *whether that value is reached smoothly or abruptly*, and *at
what specific age*. A Hero who argues "the Smooth Curve is wrong about the long-run risk" has
misread the math — Socratic Question 5 exists specifically to catch this.

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" A room that voted the same way both times is worth pressing:
did they land on the Full Table for the boundary reason, or did they just guess right?

## Deep conflict — two threads (20:00–30:00)

1. **Cost-efficiency vs. regulatory-defensibility.** The Smooth Curve is cheaper to compute and
   has never triggered a regulatory objection on any other Highline filing. Is "it has always
   worked before" a legitimate reason to keep using it, or is that exactly the reasoning a
   regulator would reject once shown the age-100 jump?
2. **Aggregate-margin vs. per-cohort-adequacy.** The blended margin is under 1%. Is that the
   right level to judge reserve adequacy at, or does a company have an obligation to be adequate
   at *every* attained age, even ones representing a tiny share of the total block?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — headline comparison only, gut-check vote |
| 3:00–6:00 | Anchor 1 vote recorded |
| 6:00–9:00 | Anchor 2 — pressure-tests "better, checked how?" |
| 9:00–12:00 | Anchor 3 — name the six-step process before opening Appendix B/C |
| 12:00–15:00 | Anchor 4 — surface MA1–MA3, ask which is load-bearing for the comparison |
| **~15:00** | **TWIST drops** — aggregate margin (0.97%) vs. single-cohort gap (188%) |
| 15:00–20:00 | Data Deep Dive — D1–D3 worked as a room |
| 20:00–30:00 | Deep conflict — two threads (cost-efficiency vs. regulatory-defensibility; aggregate vs. per-cohort adequacy) |
| 30:00–40:00 | Data Deep Dive continued — D4–D6 in two desks, reconvene for the shared table and graph |
| 40:00–45:00 | Close, re-vote, reflection, lessons learned |

## Socratic questions

1. Your blended margin between the two methods is under 1%. If a regulator only checked the aggregate reserve number, would that settle the question — and if they check reserve adequacy cohort by cohort instead, does your answer change?
2. The Smooth Curve formula was built to match the real table exactly at ages 90 and 99. If it matches so well at both ends, why does it miss so badly at age 100?
3. At what attained age does the Full Table function actually become discontinuous, and what real fact about how the source table was built explains why the discontinuity is there instead of somewhere else?
4. If Highline's Horizon Series block had twice as many contracts issued at exactly age 100 this year instead of 8, what would happen to the 0.97% margin — and would the Smooth Curve still be defensible?
5. The Smooth Curve's own equation has a horizontal asymptote of $1,000 per $1,000 of face value — the same ultimate number the Full Table jumps to. If both methods agree on where the cost is eventually headed, what exactly are they disagreeing about?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes reached for the aggregate-margin comparison first, and how much nudging it took
  to get to the single-cohort gap in D4.
- Whether the "188% at one age vs. 0.97% overall" tension was noticed independently or needed a
  direct hint.
- Whether the continuity test (D3) was treated as a real check or as a box to tick before D4.

## Standards Touched On

Limit · Asymptote · Continuity (Informal) · One-Sided Limit · Continuity · Discontinuity · How to
estimate a limit from a table or graph · How to identify a vertical or horizontal asymptote from a
function's equation · How to evaluate a limit algebraically · How to determine whether a function
is continuous at a point

## Facilitator note — margin stability (Tier 2 P5)

The *blended*-cost comparison (which method is cheaper in aggregate, A or B) is genuinely
sensitive to three stated assumptions: the Smooth Curve's two calibration coefficients (MA1) and
the size of the age-100-and-over cohort (MA2). A ±50% flex on any one of these can flip which
method looks cheaper on the blended number alone — see `case.json.sensitivity_disclosure[]`
(Category X on all three: none is independently sourced; each is a good-faith fit or scaling
choice). This is disclosed, not hidden, and it does **not** touch the case's actual structural
finding: the Full Table's discontinuity at age 100 (D1–D3) and the single-cohort dollar gap (D4)
hold regardless of how the blended aggregate number moves. If a Hero leans on "the blended numbers
are close, so it barely matters," this is the honest complication: even the *direction* of "which
is cheaper on average" is not rock-solid — which is one more reason the case argues that judging
by the aggregate number alone is the wrong move.

## Sensitivity note (SPEC §6)

LOW. This case's math never asks a student to reason about any individual's death — every figure
is an aggregate, population-level mortality statistic from a published national table, used to
price an insurance reserve. Keep classroom framing on the pricing/regulatory decision. See
`case.json.sensitivity_note` for the recorded flag.
