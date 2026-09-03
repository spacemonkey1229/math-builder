# FACILITATOR.md — The Peg Line

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Peg Line · **Tier:** T2 (MS-core) · **Studio:** MS Adventure
**Standards:** Scientific Notation, Factorial, Absolute Value group — Scientific Notation, Absolute
Value, How to write a number in scientific notation given its standard notation, How to evaluate
an absolute value expression (see `case.json.standards[]` for exact ids).

**Status:** `case-research` complete (2026-09-01); **balance-retune redesign pass complete
(2026-09-01)** — the original dilemma/metric produced `margin_pct = 97.47`, well past SPEC §2's
~20% cap (mixing a normal-drift reference for Option A against an unrelated historical-crisis
reference for Option B). The dilemma and metric were redesigned per explicit project-owner
instruction (retune, not waive): Option B changed from 13-week to 6-week Treasury bills, and the
risk metric changed to a duration-scaled version of Option A's own real reference figure (the
square-root-of-time rule). New `margin_pct = 17.04`, under the ~20% cap. Full retune history in
`RESEARCH_LOG.md`. `case.json.status` is still `"researched"` — not yet run through `case-qa`.

## Real-world grounding (for the facilitator's own background, not for case.md)

- **The GENIUS Act (P.L. 119-27, 2025)** is a real, current U.S. federal law. It caps the Treasury
  securities a payment-stablecoin issuer may hold as reserves at 93 days' remaining maturity —
  written into the statute itself, not left to a regulator's discretion. Both of this case's live
  options (4-week and 6-week bills) sit well inside that cap; the 93-day ceiling now functions as
  background context and as the reason a 13-week third draft was ruled out early, not as the
  live tension.
- **Circle's USDC and the Circle Reserve Fund (USDXX, managed by BlackRock)** are the real
  dollar-stablecoin and real money-market fund this case's Option A posture is modeled on: a 5-day
  weighted average maturity, 89.6% of assets inside a week of maturity (S2).
- **The square-root-of-time rule** (S9, Daníelsson & Zigrand, LSE, 2003) is a real, standard
  quantitative-finance method — regulators (the Basel Committee) recommend scaling a risk/
  volatility estimate from a short holding period to a longer one by multiplying by the square
  root of the ratio of the two periods. This case uses it to derive Option B's peg-deviation risk
  figure from Option A's real, sourced 30-bps reference, rather than comparing two unrelated real
  figures (a normal-conditions number for one option, a crisis number for the other) the way the
  original draft did. **Important for facilitation:** this is a real, defensible, but not the
  *only* defensible way to scale risk by duration — S9's own paper discusses a linear alternative,
  and notes the square-root rule tends to *underestimate* risk for longer/fatter-tailed
  distributions. The case is honest that this is a modeling choice (MA3), not an unchallengeable
  fact — a sharp Hero pushing on it is engaging with the case exactly as designed, not finding a
  flaw to paper over.
- **March 2023 — Silicon Valley Bank's failure and USDC's real depeg** is retained as real
  historical background (Appendix D snapshot 5, Appendix C's rejected-13-week aside) but is
  **no longer a direct input to the balance metric** — see below for why the original design mixing
  it with a normal-drift figure was unbalanced.

## Intro

Frame the format: this is a real treasury-allocation decision a reserves analyst has to sign her
name to, not an abstract word problem. Name the opener — "You control tens of billions of real
dollars backing a token that has to always be worth exactly one dollar. You've found a way to
earn a little more interest on it. The only question is how much of a chance you're willing to
take that the token stops being worth exactly one dollar, even for a few days." Mention, once,
that this is a real, current regulatory environment — the GENIUS Act is real law, signed in 2025 —
this is not invented compliance framing.

## Launch

Show Appendix B and Appendix C side by side — two Treasury-bill maturities, two yields, no peg
data yet. Ask: "Just from the yield numbers, which one would you pick?" Most rooms will say
Option B, since more yield with no visible downside looks free, though the gap is smaller than it
might expect (six cents on a hundred dollars). Do not correct this yet — Anchor 2 exists to slow
the room down before it discovers what it's not seeing.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the Short Ladder — the *lower*-yield option?" Show of
hands, both options, no discussion yet. Record the count; expect it tilted toward the Extended
Ladder before Appendix D/E are seen, though probably less lopsided than a case where the yield gap
looked bigger.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'safe'?"**

Let confusion grow here on purpose. Push: "Both options are already legal — Appendix A tells you
that up front, and neither is even close to the legal ceiling. So if 'is it legal' isn't the
question, what actually is?" Steer the room toward naming that the real question is a *trade*:
how much extra yield is worth how much extra risk of the price moving off $1.00. If the room lands
on "we can't answer that until we know both how big the extra yield is *and* how the two options'
actual risk compares," the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Name the actual steps before touching the appendices: convert the reserve total and each option's
annual yield into scientific notation (D1); work the absolute-value peg-deviation worksheet on
five real price snapshots (D2); build the dollars-per-basis-point efficiency table using Appendix
E's duration-scaled risk figures (D3); check whether that table's conclusion survives under two
different real, defensible scaling assumptions (D4); and recommend, using all of that plus
Appendix A's legal-ceiling fact (D5). Re-ask: "Is our question still the right one, now that we
can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the honest gap: Northlight itself is fictional, so its own reserve total, its own past
peg behavior, and its own attestation cadence are all stated choices, not independently verifiable
facts about a real company (Appendix A's note; MA1–MA4). What *is* real and independently verified
is the shape of the trade: real Treasury yields (S6), a real legal ceiling (S7), a real reference
peg-drift figure (S5), and a real, citable method for scaling that figure to a longer duration
(S9). Ask which of the open figures is actually load-bearing. The honest answer, per `case.json`'s
`sensitivity_note`: it is MA3 — which real scaling method is used to derive Option B's risk figure
from Option A's real base number. Unlike the original draft (where the load-bearing assumption
barely moved the conclusion across its three readings), **this time it genuinely matters**: one
real, defensible reading keeps Option A ahead by under 20%, another widens that lead, and a third
flips the recommendation outright. That itself is worth surfacing before Data Deep Dive.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's scientific-notation conversions, D2's absolute-value
worksheet, and D3's efficiency table together as a room, cold-calling for D3 specifically — this
is where a Hero who computed D1 and D2 correctly but never divides one by the other to actually
compare the options will visibly struggle to answer "so which one wins, and by how much?"

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses: "Here's something Appendix E didn't spell out for you directly.
Option B's risk figure in Appendix E wasn't measured — it was *derived*, by scaling Option A's real
number using one particular method. There's another real, defensible method for doing that same
scaling — and a third, more conservative reading that assumes no extra risk at all from the longer
duration. **Rerun D3's efficiency numbers using each of Appendix E's alternate readings — does
your recommendation change?**"

**Facilitator-only: what this does and doesn't change.** Unlike the original version of this case
(where all three real historical readings barely moved the number), this twist has real teeth:
the square-root-of-time reading (primary) keeps Option A ahead, 17.04%; the linear-scaling reading
widens that to 32.27%; the "no extra risk" floor case actually flips the recommendation to Option
B, 1.57% in its favor. A Hero who reruns all three honestly should come away saying "it depends
which real assumption you trust" — that is the intended discovery, not a flaw in the case.

## Deep conflict — threads (20–30 min)

1. **A legal ceiling is not a safety ceiling — but this time, neither option is anywhere near it.**
   Push: "Appendix A's 93-day cap isn't really in play here — both options sit far inside it. Does
   that make this an easier decision than the original 4-week-vs-13-week draft would have been, or
   a harder one, now that the risk gap itself is small enough to argue about?"
2. **A derived risk figure is not the same as a measured one.** Push: "Nobody has ever actually
   run Northlight's exact 6-week ladder through a real crisis — Option B's risk number in Appendix
   E is calculated from a formula, not observed. Does that make it less trustworthy than Option
   A's real, directly-sourced 30 bps figure? What would it take to actually measure it instead of
   deriving it?"
3. **The metric doesn't decisively favor either option — does that settle the argument, or open
   it up?** Push: "In the original draft of this decision, the math was so lopsided there wasn't
   much left to argue about. Here, the answer flips depending on which real, defensible risk-
   scaling assumption you pick. Is that a weakness in the case's numbers, or is that actually a
   more honest picture of what a real decision like this looks like?"

## The trap

Heroes will treat Anchor 1's instinct ("more yield, basically no visible downside") as durable
even after seeing Appendix E, without ever actually computing D3's ratio for the primary reading —
missing that the two options are, in fact, fairly close (17.04%), not lopsided. A second, related
trap: computing only the primary (square-root-of-time) reading for D4 and assuming that settles
it, without noticing that the case's own alternate readings actually move the needle enough to
flip the winner — several Socratic questions below exist to catch a Hero who treats D4 as a
formality rather than a real check.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote on the Short Ladder — no explanation yet |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just legal" |
| 10:00–15:00 | Pressure-test the models: "Whose ladder is most fragile if the numbers move?" |
| **15:00** | **DROP THE TWIST** — delivered slowly, with pauses (see Twist section) |
| 15:00–20:00 | Immediate recommit: who reruns D3 under the alternate readings and reverses? "What just broke?" |
| 20:00–30:00 | Threaded deep conflict — the three named threads above (legal ceiling vs. real tension; derived vs. measured risk; does an unstable metric settle or open the argument) |
| 30:00–45:00 | Close, re-vote, reflection, Lessons Learned |

## Socratic questions

1. Your D3 table says Option A earns about $91.8 million per basis point of peg-deviation risk, and Option B earns about $76.1 million per basis point. That's a real gap, but not a huge one. What would you need to believe about *how risk should scale with duration* for that gap to look different — bigger, smaller, or reversed?
2. Appendix A tells you both options are already legal under a real 2025 federal law, and neither is close to the ceiling. Why does the case still bother giving you that fact, if it isn't doing much work in this particular decision?
3. You reran D3 under D4's alternate scaling assumptions, and the recommendation actually changed under one of them. What does that tell you about how confident you should be in a "winner," when the number depends on which real, defensible modeling choice you made?
4. Appendix D's snapshot 5 — the real 2023 crisis low — isn't used anywhere in your D3 or D4 calculations. Why do you think the case still includes it? What is it useful for, if not the efficiency ratio?
5. If Priya's manager told her "the board doesn't care about basis points, they care about millions of dollars" — does that change which option your D1/D3 numbers support, or does it just change how you'd explain the same recommendation?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare to Anchor 1's vote — expect the room to be genuinely
split on the recommendation even after the numbers are on the table, since D4's sensitivity check
gives a real, defensible route to either answer; press Heroes to defend which reading they trust
and why, not just which option they picked.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

## Standards Touched On

Scientific Notation · Absolute Value · How to write a number in scientific notation given its
standard notation · How to evaluate an absolute value expression

## Balance argument (SPEC §2)

**Argument for A (the Short Ladder).** Keeps essentially the entire reserve within about two
weeks of maturity on average — close to the real, disclosed posture of the actual money-market
fund backing a real major dollar stablecoin (Appendix B, S2). Its peg-deviation reference is a
real, directly-sourced figure (30 bps, S5), and D3's efficiency figure (~$91.8 million of annual
yield per basis point of duration-scaled risk) is meaningfully larger than the Extended Ladder's
under the primary, industry-standard square-root-of-time reading — by 17.04%.

**Argument for B (the Extended Ladder).** Still entirely legal and nowhere near the ceiling
(Appendix A, S7), and earns a real, recurring $44.1 million more per year (D1) on a reserve this
size, for only 1.5× the average time-to-maturity of the Short Ladder. Option B's risk figure is
*derived*, not measured — and under a different, also-real, also-defensible scaling assumption
(the "no incremental duration risk" floor case in Appendix E/D4), the recommendation flips to
Option B outright. A Hero can argue the case's own sensitivity range shows this decision genuinely
could go either way on the numbers alone.

**Margin — COMPUTED 2026-09-01 (balance-retune redesign pass).** `margin_pct: 17.04`. **Winner
(primary reading): Option A, The Short Ladder, by 17.04% — under SPEC §2's ~20% cap.** Full
arithmetic trail: `case.json.balance.margin_note` and `RESEARCH_LOG.md`'s redesign section. This
supersedes the original design's `margin_pct = 97.47`, which mixed a normal-drift reference for
Option A against an unrelated historical-crisis reference for Option B (the FEDS Notes/CoinGecko
2023 event) — an apples-to-oranges comparison that produced a structural, non-retunable imbalance
regardless of which real reading of the crisis event was used (see `RESEARCH_LOG.md`'s original
retune-attempt writeup, retained for the full history). The redesign changed two things at once,
per the retune brief: (1) Option B's maturity moved from 13-week to 6-week bills — a closer,
still-meaningfully-different pair; and (2) both options' risk figures are now measured on the SAME
kind of risk (interest-rate/duration exposure), with Option B's figure derived from Option A's own
real reference number via a real, citable scaling method (S9) rather than an unrelated crisis
event.

**What this means for facilitation.** Unlike `prove-it-scales`-style qualitative-balance framing,
this case's real numeric race is now genuinely close (17.04%, under the cap), and D4's own
sensitivity check gives a real route to a different winner. The room's work is not just weighing a
values question against a lopsided ratio — it is genuinely deciding which real, defensible modeling
assumption about risk-scaling to trust, and living with the consequences of that choice on the
actual numeric recommendation.

## Facilitator note — sensitivity (SPEC §6)

**Routine treasury-management register — not a crisis narrative.** This case cites a real,
well-known stablecoin depeg event (March 2023, USDC/SVB) for historical color only (Appendix D
snapshot 5; Appendix C's rejected-13-week aside) — it is no longer a direct input to the balance
metric. Facilitators should keep the discussion framed on Northlight's forward-looking treasury-
allocation decision — never on the real event's harm to real holders, and never by name-checking
the real companies involved as though they were the ones under discussion. Northlight, NLD, and
Priya Nathan are entirely fictional; the real event and the real square-root-of-time methodology
are cited as documented data points and a documented technique, the same way a real published
benchmark or formula would be cited in an engineering case.
