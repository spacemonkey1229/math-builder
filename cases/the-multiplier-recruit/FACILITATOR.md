# Guide Notes: The Multiplier Recruit

**Case:** The Multiplier Recruit · **Tier:** T2 (MS-core) · **Studio:** Adventure
**Standards:** Pre-Calculus/Matrices — Matrix / Matrix Dimension / Determinant / Identity Matrix /
how to add and multiply matrices / how to find the determinant of a 2x2 matrix / how to solve a
system of equations using a matrix (see `case.json.standards[]` for exact ids; this case closes
the full Pre-Calculus/Matrices spine group, 7 of 7 previously zero-coverage)

Researched and margin-resolved 2026-08-18 (`margin_pct` = 13.3, see arithmetic below).

## Intro

Frame the format before the numbers: this is a one-shot recommendation with a real deadline —
"You are Ben Okafor. The IDA board votes at nine tomorrow morning. There is exactly one incentive
package. You have to recommend one employer tonight." Let that land before Launch.

## Launch

Put the two bids side by side with only the headline numbers visible: Meridian Forgeworks, 140
direct jobs; Cascade Distribution, 310 direct jobs; same $3,000-per-job incentive rate for both.
Ask for a gut read: "Same rate per job. One company hires more than twice as many people. Which
one do you fund?" Do not correct a "obviously Cascade" answer yet — that instinct is exactly what
the case is built to test.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with The Anvil Bid — the smaller headcount?" Show of hands,
both options, no discussion. Record the count for the Close re-vote.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What does 'better' mean here?"**

Let confusion grow here. Heroes will want to just compare 140 vs. 310 direct jobs, or note the
per-job incentive rate is identical for both and call it a wash. Push: "Ben isn't being asked which
company hires more people directly. He's being asked which one does more for the *whole county*
per incentive dollar." If the room arrives at "we need a number that isn't just direct jobs" on its
own, the case is working.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has the right question, ask them to name the steps before opening Appendix B: build
the technical coefficient matrix (D1), form **(I − A)** (D2), check it's invertible (D3), solve for
each employer's total regional jobs (D4), then divide by each employer's incentive cost (D5).
Re-ask: "Now that we can see the steps — is our question still the right one?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix E's three Modeling Assumptions honestly: MA1 (Calder County's own technical
coefficient matrix is not a purchased RIMS II table — it's calibrated to real published examples,
because a real one costs $520 and Calder County isn't real anyway), MA2 (the $3,000/job rate is
borrowed from Florida's real QTI program, not Calder County's own passed law), MA3 (both companies'
headcounts are invented, sized to make the "more direct jobs" trap genuinely tempting). Ask which
one is actually load-bearing for the *comparison* (MA1 is — a different real county's own purchased
multipliers could change the exact margin) and which one nets out of the comparison in relative
terms (MA2 does, because both bids pay the identical flat rate).

## Data Deep Dive

Now, and only now, the numbers. Walk D1–D3 as a room (the matrix, its identity-matrix subtraction,
and its determinant), then split into two desks for D4 — one solves Meridian's system, one solves
Cascade's — before reconvening for D5's shared decision table.

**Facilitator-only arithmetic note.**

$$A = \begin{bmatrix}0.20 & 0.05\\0.08 & 0.10\end{bmatrix},\quad
I-A = \begin{bmatrix}0.80 & -0.05\\-0.08 & 0.90\end{bmatrix},\quad
\det(I-A) = (0.80)(0.90)-(-0.05)(-0.08) = 0.716$$

$$(I-A)^{-1} = \frac{1}{0.716}\begin{bmatrix}0.90 & 0.05\\0.08 & 0.80\end{bmatrix}
= \begin{bmatrix}1.25698 & 0.06983\\0.11173 & 1.11732\end{bmatrix}$$

**Argument for A (Meridian Forgeworks).** d = [140, 0]ᵀ.
x = (I−A)⁻¹d = [175.98, 15.64]ᵀ, total **191.62** regional jobs supported. Incentive owed:
140 × $3,000 = $420,000. Jobs per $10,000 of incentive: 191.62 ÷ 42 = **4.56**.

**Argument for B (Cascade Distribution).** d = [0, 310]ᵀ.
x = (I−A)⁻¹d = [21.65, 346.37]ᵀ, total **368.02** regional jobs supported. Incentive owed:
310 × $3,000 = $930,000. Jobs per $10,000 of incentive: 368.02 ÷ 93 = **3.96**.

**The margin.** `margin_pct` = **13.3**. `margin_basis`: (4.5624 − 3.9572) ÷ 4.5624 ≈ 13.27%.
Meridian Forgeworks (Option A) wins on jobs-supported-per-incentive-dollar despite creating fewer
than half of Cascade's direct jobs, because its higher local-purchasing coefficient compounds
through the regional system. This sits comfortably inside SPEC §2's 20% cap — close enough that a
Hero who only compares raw direct-job counts (310 > 140) will confidently pick the wrong option.

## Twist

**Twist: N/A.** As in the project's other strongest structural cases, the surprise here is
mathematical, not narrative, and it fires the moment a Hero notices something during the Data Deep
Dive: **the flat $3,000-per-job rate is identical for both bids.** A Hero who stops at the headline
numbers reasonably concludes the two bids are financially indistinguishable per direct job, and
that Cascade — with more than double the direct hires — must therefore be the better use of the
county's money. Only D4's matrix solve reveals that the identical *rate* produces a meaningfully
different *regional* return, because the rate is paid per direct job while the payoff is measured
in total regional jobs. See **The trap** below.

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" A room that voted the same way both times is worth pressing:
did they land on Anvil for the multiplier reason, or did they just guess right?

## Deep conflict — two threads (15–20 min)

1. **Direct jobs vs. total regional jobs.** Cascade Distribution creates more than double
   Meridian's direct headcount. Is "total regional jobs per incentive dollar" really the fairest
   number for a county government to optimize, or does raw direct-hire count matter for reasons
   the model doesn't capture (visibility, political credit, a promise to voters)?
2. **How much should Ben trust a hand-built matrix?** Appendix B's technical coefficients are a
   stated Modeling Assumption, not a purchased RIMS II table. If Calder County actually spent the
   $520 to buy a real regional multiplier table for its own county, is there any reason to expect
   the real numbers would land far from what Ben assumed — and if they did, would it flip the
   recommendation?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — headline numbers only, gut-check vote |
| 3:00–8:00 | Anchor 1 vote recorded; Anchor 2 pressure-tests "better, measured how?" |
| 8:00–12:00 | Anchor 3 — name the five-step process before opening Appendix B |
| 12:00–15:00 | Anchor 4 — surface MA1–MA3, ask which is load-bearing for the comparison |
| 15:00–30:00 | Data Deep Dive — D1–D5 worked in two desks, reconvene for the shared table |
| **~25:00** | **NAME THE TRAP** — identical per-job rate, very different regional return |
| 30:00–40:00 | Deep conflict — direct jobs vs. regional jobs; trusting a hand-built matrix |
| 40:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Both bids pay the exact same $3,000 per direct job — a Hero who stops there, or who simply compares
140 direct jobs to 310, will conclude Cascade Distribution is the clearly better use of the same
incentive money, since it buys more than twice the direct jobs at the identical rate. That
comparison never asks what happens to Calder County's economy *after* the hiring — it silently
assumes every job an employer creates has the same regional ripple effect, when the entire point of
Appendix B's matrix is that it does not. Watch for a pitch that reports 310 > 140 and calls that
decisive without ever opening Appendix B.

## Socratic questions

1. Both bids pay exactly $3,000 per direct job. If the rate is identical, why isn't the case a tie?
2. Cascade Distribution creates more than double Meridian's direct jobs. What would Meridian's
   local-purchasing coefficients have to look like for Cascade to win on the case's actual metric
   instead?
3. Appendix B's matrix is a stated assumption, not a purchased RIMS II table. What about the way it
   was built should make you trust it more than a number pulled out of thin air — and what would
   make you trust it less?
4. You computed a determinant of 0.716 for (I − A) before solving anything. What would it have
   meant for Ben's model if that determinant had come out to 0?
5. If Calder County doubled its incentive rate for both bids, would you expect the *margin* between
   Meridian and Cascade to grow, shrink, or stay exactly the same — and why?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes reached for the raw direct-job comparison first, and how much nudging it took to
  get to Appendix B's matrix.
- Whether the "identical per-job rate" detail was noticed independently or needed a direct hint.
- Whether the determinant step (D3) was treated as a real check or as a box to tick before D4.

## Standards Touched On

Matrix · Matrix Dimension · Determinant · Identity Matrix · How to add and multiply matrices · How
to find the determinant of a 2x2 matrix · How to solve a system of equations using a matrix

## Facilitator note — sensitivity (SPEC §6)

This case carries no SPEC §6 sensitivity — it is routine regional economic-development math (which
employer a county recruits with a public incentive), with no protected subject matter. No
facilitator flag is needed beyond normal classroom awareness that some Heroes may have a parent or
neighbor who works in economic development, manufacturing, or logistics.
