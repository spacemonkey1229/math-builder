# Guide Notes: The Draft Line

MS | Guide Notes | Adventure | 2026-27
**Tier:** T3 (MS-stretch / HS-entry) · **Primary metric:** net revenue per TEU actually carried · **Margin:** 0.96% (extremely thin — see the sensitivity note before Lessons Learned)

**Model note (2026-09-18):** a Tier 2 cold-solve run caught a real ambiguity in an earlier draft — whether fuel/operating cost applies to the whole voyage per route, or only to the Cape route's "extra days." The case now states explicitly (case.md D3) that each route pays its own fuel and daily operating cost for its own full transit time; only The Canal Passage additionally pays the toll. The winner (A) and the approximate margin (previously 0.98%, now 0.96%) are unchanged — this was a wording fix, not a rebalancing.

---

## Intro

Heroes, Aisha has one routing call and a six-hour berth window. One route is faster but the ship can't
carry everything through it. The other route carries everything, but costs real days at sea. There is
no move here that's free.

## Launch

Show a world shipping-lane map with the Suez Canal and the Cape of Good Hope both marked, and the
Asia–Europe route drawn both ways. Ask: *"If you were the one deciding, would you rather carry less
cargo on the fast route, or all of it on the slow one?"*

Let them argue cold, no numbers yet. Then: *"Aisha has to commit before the berth window closes. Same
ship, same cargo, completely different bet on what gets left behind — cargo, or time."*

> **Hero name — which route do you run? Commit out loud.**

---

## Anchor 1 — Take a stand and vote

The Canal Passage or The Cape Diversion. No reasoning yet.

Hands up for A (Canal). Hands up for B (Cape). Write the split on the board.

*"Is anyone courageous enough to stand with ______?"*

## Anchor 2 — What is the problem we're solving?

Do **not** let them start calculating yet.

- What's the actual question, in one sentence?
- Is it "which route is faster"? Is it "which route is cheaper in total dollars"? Is it "which route
  makes the most money per container actually delivered"? **Those sound similar and are not the same
  question** — only the last one is what Aisha's voyage actually gets measured on.
- Someone will say "obviously take the canal, it's shorter." Push: *"Shorter costs you what, exactly?
  What has to come off the ship to make it fit?"*
- Is that the right question?

> Let the confusion grow. Say it out loud: *"Huh — 'faster' and 'more profitable' aren't the same
> thing here."* Do not rescue them.

**The trap to let them walk into:** most learners will assume the shorter route (the canal) obviously
wins on cost, since it skips 6.67 days of fuel and operating cost entirely — or, in the other
direction, will assume the canal's toll is "extra" money the Cape Diversion never pays and stop
there. Neither framing survives the real arithmetic: *both* routes pay their own full fuel and
operating cost for their own transit time (a ship burns fuel every day at sea, canal or not); the
canal's real edge is a *shorter* transit (22.08 days vs. 28.75) on top of a smaller total cost, and
that edge is still almost entirely erased once you divide by TEU actually carried — because the 200
TEU left behind cost the Canal Passage nearly as much in lost revenue as its whole cost advantage.
A learner who treats "the canal skips the extra days' cost" as the whole story, without dividing by
TEU, will misjudge how close this really is.

## Anchor 3 — What is the process?

- What's the process we'll go through to answer it?
- If we just compare total dollars spent on each route, are we done? Is that the same as comparing
  what each route actually earns *per container it delivers*?
- If we end up with two net-revenue-per-TEU numbers as close as $1,597 and $1,581, how do we decide
  that's close enough to be a real discussion, versus one route just winning outright? What's our
  tiebreaker before we see the numbers?
- Is our question still the right question?

## Anchor 4 — What don't we know?

- What's missing that we'd need to answer this properly?
- Appendix E gives you the assumptions behind the vessel's specs, the fuel price, and the operating
  cost. Do you believe them? Have them actually try a faster and a slower version of each assumption
  and see how much the comparison moves.
- What are we assuming stays fixed about the toll, the fuel price, or the freight rate between now
  and when the ship actually completes the voyage? (This is the case's built-in opening for the
  twist — don't tip it.)

---

## Data Deep Dive

Now the numbers. Work these on the board with them.

**Step 1 — draft and offload (D1).** Vessel laden draft 20.4 m; Suez charted limit 20.1 m (Appendix
A). Excess = 20.4 − 20.1 = 0.3 m = 30 cm. At 0.15 cm/TEU (Appendix B): 30 ÷ 0.15 = **200 TEU** must
come off. Vessel carries 18,000 − 200 = **17,800 TEU** under The Canal Passage; The Cape Diversion
carries the full **18,000 TEU**.

**Step 2 — transit time (D2).** Distances (Appendix C): Suez 10,600 nm, Cape 13,800 nm. At the
vessel's stated 20-knot service speed (Appendix B):

| Route | Hours | Days |
|---|---|---|
| The Canal Passage | 10,600 ÷ 20 = 530 h | 530 ÷ 24 = **22.08 days** |
| The Cape Diversion | 13,800 ÷ 20 = 690 h | 690 ÷ 24 = **28.75 days** |

Schedule difference: 28.75 − 22.08 = **6.67 extra days** via the Cape.

**Step 3 — net revenue per TEU (D3).** Both routes pay their own fuel and daily operating cost for
their own full transit time (from Step 2) — this is not unique to the longer route. Only The Canal
Passage additionally pays the Suez toll.

| | The Canal Passage (22.08 days) | The Cape Diversion (28.75 days) |
|---|---|---|
| TEU carried | 17,800 | 18,000 |
| Revenue (× $1,813/TEU, Appendix D) | $32,271,400 | $32,634,000 |
| Fuel: 200 t/day × $600/t × own days | $2,650,000 | $3,450,000 |
| Operating cost: $25,000/day × own days | $552,083 | $718,750 |
| Toll | $650,000 | — |
| **Total cost** | **$3,852,083** | **$4,168,750** |
| Net revenue | $28,419,317 | $28,465,250 |
| Net revenue ÷ TEU carried | **$1,596.59/TEU** | **$1,581.40/TEU** |

**The Canal Passage wins by 0.96%** — comfortably inside the 20% balance cap, and about as close a
margin as this corpus gets (SPEC's own gold-standard exemplar, Robotics Engineering, won by 0.09%).

**Push the room directly:** *"The Canal Passage's own transit is nearly 7 days shorter — that should
be a big advantage. Why does it only win by under 1%?"* (Answer, if nobody gets there: the 200 TEU
left behind are worth $1,813 × 200 = $362,600 in lost revenue on their own, while the Canal Passage's
shorter-transit cost saving over the Cape Diversion is only about $316,667 [$4,168,750 − $3,852,083].
The lost cargo very nearly cancels out the whole time-and-toll advantage — which is exactly why the
per-TEU comparison is this close.)

---

## Twist — drop this at ~15 minutes into the discussion

Deliver it slowly. Let each piece land.

> *"Aisha's phone buzzes. It's the customer service desk."*
>
> (pause)
>
> *"The 200 containers coming off at the load port — three of the shippers are invoking the
> missed-sailing clause in their service contract. Under the standard agreement, the line owes an
> expedited-alternate-carriage penalty for any booked cargo that misses its sailing."*
>
> (pause)
>
> *"That penalty is $1,800 per TEU. All 200 containers qualify."*

**Facilitator only — read before you drop this, do not read aloud.** This adds 200 × $1,800 =
$360,000 to The Canal Passage's costs. New Canal total cost = $3,852,083 + $360,000 = $4,212,083.
New Canal net revenue = $32,271,400 − $4,212,083 = $28,059,317. New Canal rate = $28,059,317 ÷ 17,800
= **$1,576.37/TEU** — now *below* The Cape Diversion's unchanged $1,581.40/TEU. **The Cape Diversion
now wins, by 0.32%** — the winner flips, on a real, disclosed contractual mechanism (missed-sailing
compensation is a genuine, common shipping-line practice), applied to the exact 200-TEU offload count
the room already computed in D1. Confirm a room that gets there against these numbers, not just the
logic.

Now: **"Sixty seconds. Are you changing your route — or not?"**

## Immediate recommit

- Who is **not** changing? Why?
- Who is reconsidering, even if they're not flipping?
- **What just broke in your original model?**
- **Were you wrong — or were you just missing information?** (Sit on this one.)
- Who built their case entirely on "the canal avoids the biggest single cost" without ever checking
  what leaving cargo behind actually costs?

---

## Deep conflict — threads (20–30 min)

**Thread 1 — "Shorter" vs. "more profitable."** The Canal Passage is the faster, shorter,
cheaper-tolled route, and still only barely wins — and loses entirely once a real, disclosed
contractual cost applies to its leftover cargo. *"If the canal route is faster and the toll is
smaller than the Cape route's extra costs, why does it only barely win — and then lose?"* Push
toward: total dollars spent is not the graded metric; dollars earned per container actually
delivered is, and lost cargo capacity is a real, disclosed cost that very nearly cancels out the
toll savings on its own.

**Thread 2 — Fragility to a single number.** Every one of the case's eight Modeling Assumptions
(Appendix E) is a disclosed value with no directly-citable per-vessel or per-voyage source behind
it — five of the eight (the vessel's draft, its speed, the toll, the fuel price, and the fuel
consumption rate) individually flip the winner at a plausible ±50% swing (see case.json's
sensitivity_disclosure — do not read this section aloud, but use it to steer questions). *"Which
route would you commit to if you had to defend it to Aisha's terminal ops manager, knowing the fuel
price alone could move 20% next month?"*

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. *"Thirty seconds — Canal or Cape?"* Two or three learners, fast. Stand/sit vote, no explanation yet. |
| **3:00–10:00** | Position defense (pre-twist). *"Convince us it's better, not just shorter."* · *"What's your net revenue per TEU — the actual rate, not a guess."* |
| **10:00–15:00** | Pressure-test the models. *"Which route is more fragile to one wrong assumption?"* · *"What single number does your route depend on most?"* |
| **15:00** | **DROP THE TWIST.** Slowly, with pauses. Finish with: *"Sixty seconds. Are you changing your route — or not?"* |
| **15:00–20:00** | Immediate recommit. Who reverses? *"What just broke?"* |
| **20:00–30:00** | The two threads: "shorter" vs. "more profitable" · fragility to a single assumption. |
| **30:00–45:00** | Close, re-vote, reflection, lessons learned. |

---

## Close

- **Vote again.** Compare to the Anchor 1 board. Who moved?
- We asked ______ as our key question. Was it the right one?
- What math was new to you here, and how did you attack it?
- If you got a case like this again, what would you check first?

## Lessons Learned

The arithmetic has a clean structure: a depth measurement compared against a limit tells you how much
cargo has to come off, and a distance-and-speed comparison tells you exactly how many extra days a
longer route costs. The Canal Passage's win (0.96%) is real on tonight's numbers, and it is also
exceptionally fragile — five of the case's eight timing/cost/scale assumptions flip the winner at a
plausible ±50% swing, and a small, realistic contractual cost (a $1,800/TEU missed-sailing penalty on
just 200 containers) is enough to flip it for real. That is a **disclosed, not eliminated** sensitivity
— `case.json.sensitivity_disclosure[]` carries a Category-F entry for every assumption, because none
of them can be tightened by more research; they are genuine voyage-specific and vessel-specific
commercial unknowns no public source measures for any one real ship or shipping line.

A facilitator running this room should say plainly what the case says: The Canal Passage wins on the
numbers as modeled, that win is real, and it is also about as thin a margin as this corpus produces —
both things are true at once, and naming both is stronger than picking one.

---

## Standards Touched On

**Depth · Currency · Distance · How to find elapsed time · How to convert an amount with compound units.**

See `LEARNING_GOALS.md` for the forces-test.

---

## Facilitator note — sensitivity

No SPEC Section 6 subject-matter sensitivity applies. This is a commercial routing decision with no
death, illness, or family-hardship stakes.
