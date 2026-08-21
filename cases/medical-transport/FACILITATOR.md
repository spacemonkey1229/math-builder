# Guide Notes: Medical Transport

**Case:** Medical Transport · **Tier:** T3 · **Band:** MS-stretch/HS-entry · **Studio:** Adventure
**Standards:** see `case.json.standards[]` for the exact ids (34 skills — decimal/currency
arithmetic, rate/elapsed-time, probability, mean, percent, and two required visual displays)

Legacy conversion, 2026-08-20, built from the original case study docx
(`source/Y3/Session 2/Medical Transport/Case Study_ Medical Transport.docx`; no separate Guide
Notes doc exists in the source) onto the current 11-anchor ladder. Inland Transport's fleet, shift
structure, delivery network, and Josie's salary/bonus structure are preserved from the source; the
Oregon-specific real-world claims (speed limits, fine schedule, crash-risk model, fuel economy,
gas price) were independently re-verified — see `case.json.legacy_conversion_note` for the full
account of what changed and why. The dilemma is the human-approved lock from
`cases/_concepts/LEGACY_DILEMMA_LOCKS_2026-08-20.md#medical-transport`.

**A note on sensitive content (SPEC §6):** this case touches organ/tissue transport and real
traffic-fatality data. Per SPEC §6, keep the discussion on the disclosed cost/time/risk numbers,
not on casualty counts as an abstract quantity to optimize — the stake here is *getting a
time-critical, irreplaceable shipment there intact*, not a body count.

## Intro

Frame the format: this is a real logistics company's real policy call, not a worksheet with a
story stapled on. Name the opener — "Five cars, four hospitals, one policy Josie has to defend to
the board on Wednesday: how fast should Inland's drivers actually drive?"

## Launch

Read the Overview aloud, then Mr. Jones's line — "time is money, we do it right, but we do it
fast" — without showing any Appendix numbers yet. Ask: "Just from that line alone, what do you
think Josie is being told to do?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who's pitching 'never exceed the limit'? Who's pitching '10 over, always'?" Show of hands, no
discussion yet. Record the count — Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'better'?"**

Push on what "better" means here. Cheaper for Inland? Faster for the patient waiting on donor
tissue? Safer for the driver? Better for Josie's own bonus? Let the room sit in the ambiguity —
"Is anyone courageous enough to define 'better' before we start adding numbers?" Deliberately let
it feel underdetermined: "Wow, this is a harder question than it sounded."

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has picked a working definition of "better," ask them to name the actual steps: fuel
cost at each speed, expected ticket/insurance cost, trip time saved, and whether either option
actually changes the fleet's shot at Josie's bonus thresholds. Re-ask: "Given how we just defined
'better' — is that still the right process?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix's Modeling Assumptions as a group, out loud, before anyone computes anything. Ask
which ones the room thinks matter most. (Facilitator note: MA1 × MA2 — the pull-over probability
and the annual enforcement-exposure count — are the two that actually drive the whole cost
comparison, but let the room guess first; that's what the Twist is for.)

## Data Deep Dive

Now, and only now, the numbers. Walk D1's cost table together as a room.

**The trap (three parts — a fresh cold-solve probe, 2026-08-20, caught the third one live):**

1. Most Heroes will treat "10 mph over" as one uniform risk and one uniform fine across all three
   road types, and will miss Appendix D's posted-65+-mph exception — pricing the freeway violation
   at the $115 Class D rate instead of the real $165 Class C rate.
2. They will also anchor on "75 mph feels the most dangerous" (the freeway, in raw mph) rather than
   noticing that the *city* segment carries the largest **relative** speed increase (10/35 = 28.6%
   over, versus 15.4% over on the freeway) — which Appendix F's crash-risk model says matters more
   than the raw number. Cold-call on this specifically: "Which road type is actually the riskiest
   under Option B, and by what measure?"
3. **The one that will actually catch the room on D1/D2's headline dollar figures, before anyone
   gets to tickets or risk:** Appendix B's mpg penalty is keyed to *speed over 50 mph*, not to
   legality or "which option is speeding." Heroes will read "10 mph over" and Option A/B's
   city-legal-vs-speeding framing and assume Option A, which never breaks a posted limit, pays no
   fuel penalty at all. It does — Option A's own highway leg (55 mph) is 5 mph over the 50-mph
   threshold (one 7% mpg cut) and its freeway leg (65 mph) is 15 mph over (three compounding 7%
   cuts, ~19.6% mpg loss). Skipping this understates Option A's fuel cost and inflates the apparent
   gap between the two options — it corrupts the case's central number, not a peripheral one. Ask
   directly: "Does Option A get a fuel-economy penalty anywhere? Where, and why?" before the room
   locks in its D1 table.

**D5's capacity check (facilitator-only, mechanical answer):** most Heroes will assume faster driving must mean more deliveries, and be surprised to find it doesn't — fleet drive-time capacity (75 vehicle-hr/day, Appendix C) is only 35–42% utilized under either option, so the 4.5 long-distance/20.5 total averages are demand-bound, not speed-bound, and Josie's bonus is genuinely out of reach either way. The one real exception, and Option B's actual quantitative counter-argument (not just "speed feels valuable"): a single vehicle dedicated only to the Eugene route clears 2 round trips/day under Option A (short of Eugene's own 2.7/day demand — Option A needs a second, partially-dedicated vehicle) versus 4/day under Option B (covers it alone). Push the room to find this themselves before revealing it — it's the same shift-capacity math as D4, just applied per-route instead of fleet-wide.

## Twist — drop this at roughly the 15-minute mark

Deliver slowly, with pauses:

"Your cost table used the *expected* number of tickets per vehicle — 2 per year, on average.
But an insurance-industry data point [S7] shows something else: ticket *severity* barely moves your
premium — its own rate table varies by less than 1.5% across brackets from 'under 5 over' to '21–25
over.' What really moves your premium is the **count** of tickets: one ticket is roughly a 24%
increase, 2 tickets roughly 45%, 3 tickets roughly 60%. And Inland's own
policy only *covers* up to 4 tickets per vehicle per year before other consequences apply. Two per
year is the *average* — which means, by ordinary variance, roughly half the fleet's five vehicles
will draw *more* than two in a given year. One unlucky car could blow straight through Inland's own
4-ticket cap."

**Facilitator-only.** The headline table (`case.json.balance`): **Option A costs $8,319.97 per
vehicle per year. Option B costs $9,756.24 per vehicle per year — a 17.26% margin, Option A
cheaper.** That number used the *expected* (average) outcome. The Twist doesn't change the average
— it changes what the average was hiding: a fleet-wide *policy* recommendation was defended using a
single expected value, when the real quantity the board should care about is the spread across five
independent vehicles, not just their mean.

Ask: "You now have 60 seconds. Does this change your recommendation — or not?" Then, the follow-up
that matters more than the vote: **"What just broke in your original model? Were you wrong about
the expected cost — or were you just missing the difference between an average and a range?"**

Do not hand over a "correct" answer. A reasonable board could still accept Option B's ~17% expected
premium as a budgeted cost of doing business faster — that's the real, transferable tension, not a
trick.

**Twist soundness check (SPEC §6):** this twist introduces no new figure that contradicts an
earlier one — it re-reads the already-disclosed S7 data (Appendix E) and the already-stated 4-ticket
cap (Background/Appendix E) together, a lens the cost table's single expected value doesn't surface
on its own. Checked under both a sequential reading (Hero encounters S7 and the 4-ticket cap in
different appendices, may not have connected them) and a simultaneous reading (both facts sit next
to each other in Appendix E already) — it holds under both.

## Immediate recommit

Re-vote immediately. "Did the variance point change your hand — or did it just change *why* you're
holding it up?"

## Close

Re-vote once more after full discussion. Ask: "Did we ask the right question at Anchor 2, or did
'better' turn out to mean something different by the end?" And: "What math was new to you today,
and how did you attack it?"

## Lessons Learned

The original case posed this as a 3-point spectrum (limit / +5 / +10) with no attached cost model —
students were asked to "pick a speed" with only Josie's bonus thresholds and a stray, unattributed
"recent studies" citation to reason from. This conversion adds the apparatus the original case
didn't have: a real Oregon presumptive-fine schedule (with its own posted-65+-mph exception, genuine
legal texture most Heroes won't expect), a real fuel-economy-vs-speed model, and the real Nilsson/
Elvik crash-risk power model in place of the original's slightly-off paraphrase. The transferable
lesson: **an "average" cost is not the same question as a "policy" decision** — Option B's expected
cost is defensible, but defending a *fleet-wide policy* on an average alone, without asking what the
worst plausible vehicle looks like, is the trap.

## Five Socratic Questions

1. Your cost table shows Option A is 17.26% cheaper. What would MA2's 8-exposures/vehicle/year assumption have to rise to before that margin doubles?
2. Josie's bonus depends on the fleet averaging 5+ long-distance deliveries a day, and the given delivery data puts the average at 4.5 (Appendix A). Checked honestly against the fleet's own shift-capacity math (Appendix C), fleet drive-time capacity is never the binding constraint under either option (only 35–42% utilized) — so that 4.5 average genuinely does not move, and the bonus stays out of reach either way. Does that mean Option B has *no* real advantage here — or does the same capacity math reveal something narrower and still real (hint: look at what a single vehicle dedicated only to the Eugene route can do under each option)?
3. The freeway violation under Option B is a Class C, $165 fine — not the Class D, $115 fine the city and highway violations get. Why does driving 10 over on a 65-mph freeway cost more per ticket than driving 10 over on a 35-mph street, even though it's the same "10 mph over"?
4. Appendix F's crash-risk model uses an exponent, not a straight percentage — a 15.4% speed increase on the freeway does not produce a 15.4% jump in fatal-crash risk. What does it produce, and why does that matter for how you'd defend Option A in the room?
5. If Inland's insurer only ever finds out about a ticket the *year it happens* (MA3), is Option B's real cost understated or overstated? What would change if a ticket's surcharge followed the driver for three years instead of one?

## Standards Touched On

See `case.json.standards[]` (34 ids) and `LEARNING_GOALS.md` for the full deliverable ↔ skill
matrix. In brief: decimal and currency arithmetic (all four operations), percent and probability
(expected-cost calculations), rate/elapsed-time (route trip times), mean (delivery averages), and
two required visual displays (bar graph, pie chart).

## Cohort Bands

See `case.json.cohort_bands[]`.

- **Full (12–20):** Anchors 2–3 run as written; the room typically splits into a "safety/cost"
  faction and a "speed-is-the-business" faction before the Twist forces everyone to hold both the
  cost table and the risk table at once.
- **Compressed (6–11):** Anchors 2–3 combine into one pass; D6's ticket-cost table and D7's
  crash-risk table are worked as one shared example instead of every Hero building both
  independently.
- **1:1 / pair (1–2):** No vote to take — Anchor 1 becomes a stated initial position instead of a
  cold-call show of hands; the guide plays devil's advocate directly, arguing whichever side the
  Hero didn't pick.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote (Anchor 1) — no explanation |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just cheaper" |
| 10:00–15:00 | Pressure-test the models: "Which road type is actually riskiest, and by what measure?" |
| **15:00** | **DROP THE TWIST** — the average-vs-variance point on ticket count, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00–30:00 | Threaded deep conflict — two named threads: (1) expected cost vs. worst-plausible-vehicle risk as competing definitions of "safe policy"; (2) raw mph (felt danger) vs. percent-over-limit (modeled relative risk) as competing definitions of "risky" |
| 30:00–45:00 | Close, re-vote, reflection, Lessons Learned |

## Sensitivity note

The 17.26% margin is a **tuned** number: it is a direct function of MA1 (pull-over probability,
25%) and MA2 (annual enforcement exposures/vehicle, 8) — both disclosed, unsourced, stated Modeling
Assumptions, because no current, attributable public data reports either figure. `case-readiness`
Tier 2 probe 5 sweeps both ±50% and records whether the winner or the 20% cap survives in
`QA_REPORT.md` — treat that as live information for a discussion, not a settled fact.
