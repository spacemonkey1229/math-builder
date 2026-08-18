# Guide Notes: Six Degrees of Exposure

**Case:** Six Degrees of Exposure · **Tier:** T3 (MS-stretch / HS-entry) · **Studio:** Launchpad
**Standards:** Discrete Mathematics — Graph / Vertex / Edge / Weighted Graph / how to find the
shortest path between two vertices in a weighted graph (see `case.json.standards[]` for the exact
ids; this case closes a genuine, previously-thin spine gap in Discrete Mathematics)

Researched and margin-resolved 2026-08-13 (`margin_pct` = 1.0, see `sensitivity_model.py`). This
file is re-checked for drift at every readiness run (the continuity checks in `case-readiness`).

## Intro

Frame the format before anything else: this is a live operational call with a clock on it, not a
worksheet. Name the opener — "You are Dr. Marsh. The vaccination clinic opens tomorrow morning.
The dose allocation is fixed. You have to send one plan to the printer tonight." Let the stakes
land before moving to the Launch.

## Launch

Put the two plans side by side with no numbers yet — just the two sentences: "vaccinate the 50
most-connected people we can find and confirm" vs. "vaccinate 500 people at random from the same
traced population." Ask for a gut read: "Which one sounds smarter to you, just from hearing it?"
Do not confirm or correct. The point is a first instinct before anyone touches Appendix A.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Hub Sweep — the targeted 50?" Show of hands, both
options, no discussion. Record the count — Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What does 'better' mean here?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which plan
vaccinates the most well-connected people," but the real question is sharper: *which plan removes
more of the network's total transmission-weight for the one fixed dollar budget the county
actually has?* Push on it: "Dr. Marsh isn't asking who looks most important on the graph. She's
asking which plan spends the same money better." If the room lands on "we need a number per
dollar, not per person" on its own, the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has the right question, ask them to name the actual steps before touching the
appendices: draw and weight the sample subgraph (D1), pull the real top-50-degree list (D2),
compute each plan's total weight eliminated and check it against the shared budget (D3), then find
the fastest notification path through the sample subgraph (D4). Re-ask: "Is our question still the
right one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gaps honestly: Appendix E's three Modeling Assumptions (MA1 the network itself is
a real public stand-in, not Calloway County's actual contact-tracing data; MA2 an edge's weight
stands for its number of recorded contact events; MA3 the two headcounts, 50 and 500, are the
county's stated plan, not something derived from Appendix D's national-median dollar figures). Ask
which one actually moves the primary-metric comparison if it changes (MA3 does not — see D3's
first half; MA1 does, and that dependency is the honest core of the case, not a flaw) and which one
is the reason D3 has a second half at all (MA3 — the real, sourced per-dose costs do not split one
shared budget into exactly 50 and 500).

## Data Deep Dive

Now, and only now, the numbers. Walk D1's labeled subgraph, D2's real top-50 list, and D3's two
totals together as a room, cold-calling for D3's counting argument specifically — this is where a
Hero who tries to list out 500 random people by hand, instead of reasoning about the probability
that a single edge survives untouched, will visibly stall, which is useful information for the
facilitator, not a moment to rescue.

**Facilitator-only arithmetic note — Argument for A (Operation Hub Sweep).** The 50 highest-degree
individuals (Appendix B) touch 5,859 distinct edges carrying a combined weight of **27,643** —
46.2% of the network's total 59,835 contact-weight, from just 2.6% of the traced population.

**Facilitator-only arithmetic note — Argument for B (Operation Wide Net).** A random 500-person
selection cannot be listed by hand, so its expected reach is found by a counting argument: the
probability that a specific edge (i, j) survives untouched by a random sample of 500 out of 1,899
people is [(1,899−500)(1,899−500−1)] ÷ [1,899×1,898] = (1,399×1,398) ÷ (1,899×1,898) ≈ 0.54263, the
same for every edge regardless of its weight. So the expected fraction of the network's total
weight touched by Wide Net is 1 − 0.54263 ≈ 0.45737, giving an expected weight eliminated of
59,835 × 0.45737 ≈ **27,366.7**.

**The margin.** `margin_pct` = **1.0**. `margin_basis`: compare total edge-weight eliminated for
Hub Sweep's fixed 50-person set (27,643) against the expected total edge-weight eliminated for Wide
Net's random 500-person set (27,366.7), both drawn from the same 59,835-weight network (Appendix
A), since both operations spend the identical shared budget. Operation Hub Sweep wins by
(27,643 − 27,366.7) ÷ 27,643 ≈ **1.0%** — a near dead heat, in the family of the project's own gold
standard (SPEC §2, the 0.09%-margin Robotics Engineering exemplar).

## Twist

**Twist: N/A.** No new information arrives mid-discussion the way a live twist usually drops. This
case's real pedagogical surprise is structural, not narrative, and it fires during the Data Deep
Dive itself: the per-*head* comparison (which every Hero will compute first, and which favors Hub
Sweep by roughly 10×) and the per-*budget* comparison (the case's actual primary metric, a near
dead heat) point in opposite directions. That reversal does the same job a dropped twist usually
does — it makes a room that already voted have to reckon with new reasoning — without needing a
fictional new event. The trap most Heroes will fall into: they compute weight-eliminated-per-head,
see Hub Sweep ahead by roughly 10×, call that decisive, and never go back to check the answer
against the fixed dollar budget that is the case's actual constraint — see **The trap** below for
the full arithmetic.

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that voted the
same way both times is worth asking about directly: did they get to the per-budget number for the
right reasons, or did they never leave the per-head framing at all?

## Deep conflict — two threads (15–20 min)

1. **Per head vs. per budget.** Hub Sweep wins by roughly 10× per person vaccinated but by only
   about 1% per dollar spent. Which number should Dr. Marsh actually report to her director, and
   why isn't "per person" the honest framing when the real constraint is a fixed budget?
2. **The budget-consistency discrepancy (D3's second half).** Appendix D's real, sourced national
   per-dose costs do not divide one shared budget into exactly 50 and 500 — they imply about 88.8
   Hub Sweep doses, not 50. Calloway County's own real internal rates aren't public. Is fixing the
   headcounts at 50 and 500 anyway (Modeling Assumption MA3) a reasonable way to model a real
   decision, or does it quietly favor one plan?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — read both plans cold, gut-check vote, no numbers yet |
| 3:00–8:00 | Anchor 1 vote recorded; Anchor 2 pressure-tests "better than what, measured how?" |
| 8:00–12:00 | Anchor 3 — name the four-step process before opening the appendices |
| 12:00–15:00 | Anchor 4 — surface MA1–MA3, ask which one is load-bearing |
| 15:00–30:00 | Data Deep Dive — D1–D4 worked as a room; cold-call the counting argument for D3 |
| **~25:00** | **NAME THE TRAP** — per-head vs. per-budget; no separate TWIST reveal (see above) |
| 30:00–40:00 | Deep conflict — per-head vs. per-budget; the budget-consistency discrepancy |
| 40:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Per *head* vaccinated, Hub Sweep looks like a landslide: 27,643 ÷ 50 ≈ 552.9 weight-eliminated per
dose against Wide Net's 27,366.7 ÷ 500 ≈ 54.7 — roughly **10.1×** in Hub Sweep's favor. A Hero who
computes only that number will confidently pick A for the wrong reason. The case's actual primary
metric divides by the *shared budget*, not by headcount, and on that division the race is a near
tie, won by barely one percent. Watch for a pitch that reports the per-head number, calls it
decisive, and never asks what the actual constraint (a fixed dollar budget, not a fixed headcount)
does to that comparison.

## Socratic questions

1. You just computed weight-eliminated-per-person for both operations, and Hub Sweep won by about ten times. Why doesn't that number decide the case?
2. If the county's budget doubled tomorrow, would you expect Hub Sweep's *headcount* advantage over Wide Net to grow, shrink, or stay the same — and does that change which operation you'd pick?
3. Operation Wide Net reaches people spread across the entire traced population; Operation Hub Sweep reaches a fixed list of 50 already-identified people. What kind of new information would make that difference matter more than the raw weight-eliminated number does?
4. Your D3 table used an expected value for Wide Net's 500 random doses, not an exact count. What would have to be true about the traced network for that expected value to be a bad estimate of what actually happens on clinic day?
5. Appendix D prices Hub Sweep's doses higher because of case-investigation fieldwork. If that fieldwork got cheaper, at what price would Hub Sweep clearly become the better operation on the case's own metric — and is that a realistic price?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes reached for the per-head ratio first, and how much nudging it took to get the
  room to the per-budget framing on its own.
- Whether D3's counting argument (rather than trying to enumerate 500 random people) was reached
  independently or needed a direct hint.
- Whether the budget-consistency discrepancy (D3's second half) read as a real finding or as a
  distraction from the primary metric.

## Standards Touched On

Graph (Vertices And Edges) · Vertex · Edge · Weighted Graph · How to find the shortest path between
two vertices in a weighted graph

## Facilitator note — sensitivity (SPEC §6)

This case models a real disease outbreak and a real vaccination-response decision, so the framing
is deliberately protection-oriented throughout: doses delivered, contacts reached, transmission-
weight removed from the network. At no point does the math ask a student to compute or optimize a
casualty count, consistent with SPEC §6's guidance to prefer protection framings over destruction
framings. Even so, some learners will have direct personal experience with contact tracing,
quarantine, or unequal access to a vaccination clinic (COVID-19 and other real outbreaks), and a
case like this one can surface real feelings even when the arithmetic itself stays protective. Give
that room before moving into the tables — the discomfort, if it shows up, is not a sign the case
has gone wrong.
