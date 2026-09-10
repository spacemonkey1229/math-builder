# Facilitator Guide — The Trailer Return

**Case:** The Trailer Return · **Tier:** T3 · **Band:** MS-stretch/HS-entry · **Studio:** MS Adventure
**Standards:** see `case.json.standards[]` (8 ids — Graph (Vertices and Edges), Vertex, Edge, Path,
Cycle, Weighted Graph, How to determine whether a graph has an Euler path or circuit, How to find
the shortest path between two vertices in a weighted graph)

**Sensitivity flag (SPEC §6):** None beyond ordinary care. This case touches a small town's fuel
budget and a contracted-service line item — no illness, death, acute money stress, or family
hardship. No facilitator flag required beyond ordinary care with real municipal budget framing.

## Intro

Frame the case as a real routing decision a small town's public-works department makes every
single collection day. Name the opener: Denise Okafor standing in the Public Works yard, breath
fogging over Truck 4's exhaust, a flatbed hauler's quote open on her phone, a one-page
recommendation due to her supervisor before Thursday's budget meeting. She has not put the truck
in gear yet — that pause is the whole case.

## Launch

Put a small piece of Appendix B's Practice Block on the board — just the six vertices A, B, E, F,
J, K from Appendix B's table, with their real degrees (3, 3, 3, 3, 3, 3) and the streets they sit
on. Ask Heroes to trace a route through just those six corners that never repeats a block segment.
Most will get stuck. Ask why. That stuck feeling — not a lecture on Euler circuits — is the launch.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with The Closed Loop? With The Trailer Return?" Record the
count on the board — Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this actually a question about which option is cheaper, or about something else?"**

Push on what "wasted mileage" means before anyone opens Appendix D. "Denise's supervisor cares
about the diesel line item — is that automatically the right lens?" Let the room sit in the
ambiguity: "This grid has 68 corners and you can't even agree yet on what we're minimizing."

## Anchor 3 — What is the process?

**"If we count every corner's degree, what does that actually tell us?"**

Work one small, fully tractable example on the board before touching the full grid: give the
room the Practice Block's odd-vertex pair O and R from Appendix C. Their shortest-path distance is
0.0000 miles — they are effectively the same intersection — so pairing them costs nothing. Compare
that to pairing O with M (0.1761 mi, the most expensive pair either vertex appears in). Ask: "If
you had to pair up all 14 odd vertices in the Practice Block cheaply, which pairs would you grab
first, and why?" This is the exact logic Appendix D's official 34-vertex matching used at full
scale — the room has now done it by hand on a problem small enough to check. Re-ask: "Now that
you've felt what 'pairing' costs, is 'cheapest tomorrow' still the only question worth asking?"

## Anchor 4 — What don't we know?

**"Do we know exactly what the flatbed hauler would really charge to move a loaded collection
truck, not a sedan?"**

Surface Appendix F's four Modeling Assumptions as a group before anyone computes a dollar figure.
Ask which one the room thinks matters most. (Facilitator note: MA4 — the $115/day hauling fee — is
the one that actually matters most for the dollar comparison, but let the room guess first; that
is what the Twist is for.)

## Data Deep Dive

Now work Appendices B–E directly, in order: D1's full 26-vertex Practice Block degree table
(EVEN/ODD for every corner), D2's full-grid Euler determination (34 odd vertices means neither a
circuit nor — importantly — an Euler path by itself; relaxing to *any two* endpoints is what makes
Option B's open path valid), D3's closed-circuit Practice Block pairing using Appendix C, D4's
open-path Practice Block pairing (leave exactly one pair unmatched, minimizing the rest), and D5's
full-grid dollar table from Appendix D's official ratios and Appendix E's cost data.

**The trap:** most Heroes will build D5, see Option A win by roughly 12x ($10.07/day versus
$9.70/day plus the $115/day hauling fee), and stop there — concluding the case is lopsided in
Option A's favor and never seriously engaging with Option B's actual argument. The trap is
treating "cheaper today" as the only lens available, when the case's own primary metric — the
deadhead ratio, not raw dollars — is what `balance.margin_pct` is computed from: Option A's
1.2069 deadhead ratio versus Option B's 1.1622, a real 3.70% reduction in wasted mileage. A strong
pitch for A still has to name that finding and explain why dollars should override it for this
decision; a strong pitch for B has to admit the dollar gap honestly rather than quietly leaving
Appendix E out of the visual.

## Twist — drop this at roughly the 15-minute mark

Deliver slowly, with pauses, reading directly from Appendix G's own source note on S6:

"The $115/day hauling fee in MA4 is not a quote for hauling Truck 4. It is based on a published
2026 rate range for towing a *standard passenger vehicle* — a flatbed picking up a sedan, not a
loaded municipal collection truck. A real quote for hauling a truck the size and weight of Truck 4
would almost certainly need a bigger, more specialized tow rig than a sedan needs, at a real
premium over that consumer rate."

Ask: "Does this change your dollar comparison — or just how confident you are in it?" Push
further: "Appendix F's own sensitivity note already told you the case isn't sensitive to MA4's
exact direction — even the fee cut roughly in half still leaves Option B far more expensive than
Option A. So if the real fee is likely *higher*, not lower, than $115, what does that do to
Option A's dollar-side argument — does it get stronger, or does it just get more uncertain?"

Do not hand over a "correct" answer. The Twist does not flip the recommendation the way a
close-margin twist would — it does the opposite job: it shows the room that the side that looked
rock-solid (Option A, 12x cheaper) is actually resting on the single least-sourced number in the
whole case (MA4, confidence not claimed as sourced at all — SEE Appendix F), while the side that
looked shakier (Option B, only a 3.70% ratio win) is resting on an exact, reproducible
minimum-weight matching (Appendix D). The lesson is about which numbers deserve how much
confidence, not about which option is "really" correct.

**Twist soundness check (SPEC §6):** checked against every stated Background/Appendix fact and
Modeling Assumption — it introduces no new figure and contradicts nothing already in Appendix E
or F; it only surfaces a qualitative caveat about MA4 and S6 that case.json's own source note
already discloses (`sources[].S6.note`), read aloud rather than left buried in a citation.

## Immediate recommit

Re-vote immediately. "Did the rotator-premium reveal change your hand — or just change how sure
you are of the hand you already had up?"

## Close

Re-vote once more after full discussion. Ask: "Did we ask the right question at Anchor 2 — cheapest
tomorrow, or most efficient always? And which of today's numbers would you trust the least if you
had to defend this pitch to Denise's supervisor?"

## Lessons Learned

An Euler circuit requires every vertex in the graph to have even degree; an Euler path tolerates
exactly two odd vertices left as start and end. A real street grid — the Bay Fruit Streets grid,
modeled on Cape Charles, Virginia's actual downtown layout — has plenty of odd-degree corners (34
of 68), so relaxing "must return to the start" produces a real but modest improvement (3.70% on
the deadhead ratio), not a dramatic one. And a routing problem's "primary metric" (deadhead ratio)
and its "budget line item" (daily diesel plus hauling cost) can point in opposite directions; a
real decision-maker has to say which one she is actually optimizing for, and how confident she
really is in each number she is using to argue it.

## Standards Touched On

See `case.json.standards[]` (8 ids). In brief: Graph (Vertices and Edges), Vertex, Edge, Path,
Cycle, Weighted Graph, How to determine whether a graph has an Euler path or circuit, and How to
find the shortest path between two vertices in a weighted graph.

## Five Socratic Questions

Use these across Anchors 2–4 and the Data Deep Dive — each is answerable only with this case's own numbers, not general opinion.

1. Appendix D shows Option B's deadhead ratio is 3.70% better than Option A's, but Option B costs about 12x more per day in Appendix E — which number is Denise's supervisor actually going to ask about on Thursday, and does that change which option you would recommend?
2. Appendix F's own sensitivity note says the case is not sensitive to MA4's exact direction, even at half the assumed hauling fee — so why does the Twist matter if it cannot flip the dollar comparison either way?
3. D2 asks you to classify the full grid as circuit, path, or neither using the 34-odd-vertex count from Appendix A — if Averyton later closed one of the grid's 9 dead-end streets, could that number change, and how would you check?
4. In D4, Appendix D says the best open-path pair to leave unmatched is the Monroe Avenue dead end and the north end of Strawberry Street — using Appendix C's distances on the Practice Block's own odd vertices, what made O and R a nearly-free pair to match while O and M was one of the most expensive?
5. Denise's crew is paid the same wage under both options (Appendix E) — if that stopped being true, how would you rebuild your D5 table, and would it change your recommendation?

## What a strong defense sounds like

Not a single "right" answer — a strong pitch names its own metric explicitly (deadhead ratio or
dollars), shows the actual Appendix D/E numbers rather than a vague summary, and directly
addresses the other side's strongest point instead of ignoring it (a pitch for A that never
mentions the 3.70% deadhead-ratio finding, or a pitch for B that hides the 12x dollar gap, is a
weak pitch regardless of which option it argues for).

## Cohort Bands

See `case.json.cohort_bands[]`.

- **Full (12–20):** split into two desks — one builds D1/D3 (closed-circuit Practice Block
  pairing) fully before seeing D4, the other jumps to D4's open-path pairing directly — then trade
  findings before the Data Deep Dive so both groups reconcile the same Appendix D numbers and
  confront Appendix E's dollar-vs-ratio tension together.
- **Compressed (6–11):** work D1's Practice Block vertex-degree table together on the board as a
  warm-up (Appendix B), then split into pairs for D3 (closed pairing) vs. D4 (open pairing) rather
  than four separate desks.
- **1:1 or pair (1–2):** no vote at Anchor 1 — the learner states an initial position (Closed Loop
  or Trailer Return), and the guide argues the other side directly. Spend recovered time on D3/D4's
  odd-vertex pairing using Appendix C's distance table, the step most likely to trip up a solo
  learner.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote (Anchor 1) — no explanation |
| 3:00–10:00 | Position defense: "Convince us why your option is better, not just cheaper" |
| 10:00–15:00 | Pressure-test the models: build the O/R vs. O/M pairing example from Appendix C together |
| **15:00** | **DROP THE TWIST** — the heavy-duty rotator premium on MA4's hauling fee, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses, or just gets less confident? "What just broke?" |
| 20:00–30:00 | Threaded deep conflict: (1) deadhead-ratio efficiency vs. raw daily dollars, (2) how much confidence each side's numbers deserve |
| 30:00–45:00 | Close, re-vote, reflection, Lessons Learned |
