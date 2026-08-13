# Guide Notes: Family Trip

**Case:** Family Trip · **Tier:** T2 · **Band:** MS-core · **Studio:** Adventure
**Standards:** see `case.json.standards[]` for the exact ids (26 skills — decimal/whole-number
arithmetic, unit conversion, elapsed time, currency, and two required visual displays)

Legacy conversion, 2026-08-13, built from the original case study docx
(`source/Y1/Session 1/Family Trip/Case Study_ Family Trip.docx` and `Guide Notes.docx`) onto the
current 11-anchor ladder. The family, budget, vacation-day constraints, and vehicle are preserved
verbatim from the source; the fare/hotel/gas/mileage figures were re-verified for 2026 currency —
see `case.json.legacy_conversion_note` for the full account of what changed and why.

**A note on sensitive content (SPEC §6):** this case touches money stress within a family — a real
couple weighing a hard budget against a newborn's comfort. Keep the discussion on the math and the
disclosed numbers, not on facilitator or Hero personal family-finance anecdotes.

## Intro

Frame the format: this is a real family's real trip-planning decision, not a worksheet with a
story stapled on. Name the opener — "Two ways to get a family of six from Idaho to Arizona for
Christmas. Both real. One number has to cover both the trip and the gifts."

## Launch

Read the Overview aloud, then Background's two sentences about the budget ($1,300, covers travel
*and* gifts) and the vacation-day limit (5 days), with no Appendix numbers shown yet. Ask: "Just
from what you've heard — does this feel like an easy call, or a close one?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who's flying? Who's driving?" Show of hands, no discussion yet. Record the count — Close asks
again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'cheaper'?"**

Push on what "cheaper" even means here. Cheaper *out of pocket this month*? Cheaper counting what
the minivan actually costs to run? Cheaper per day actually spent with the Youngs? Let the room
sit in the ambiguity — "Is anyone courageous enough to define 'cheaper' before we start adding
numbers?" Deliberately let it feel underdetermined: "Wow, this is a harder question than it
sounded."

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has picked a working definition of "cheaper" (or "best"), ask them to name the
actual steps: total fare cost (who actually needs a paid ticket?), total fuel/hotel cost, elapsed
travel time, and vacation days used. Re-ask: "Given how we just defined 'cheaper' — is that still
the right process?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix H's six Modeling Assumptions as a group, out loud, before anyone computes
anything. Ask which ones the room thinks matter most. (Facilitator note: MA4 — gas price vs. the
IRS mileage rate — is the one that actually matters most, but let the room guess first; that's
what the Twist is for.)

## Data Deep Dive

Now, and only now, the numbers. Walk D1's cost breakdown together as a room.

**The trap:** most Heroes will read "six family members" in Background, skip past Appendix D's
lap-child detail entirely, and multiply the round-trip fare by 6 passengers instead of 4 — students
will quietly assume every family member needs a paid ticket. That produces an Option A total that's
wrong by roughly $948 (2 extra full-fare tickets never actually purchased), and it makes them
conclude flying is even more hopelessly expensive than it actually is, which then makes Option B
look like an even more obvious landslide than the real numbers support. Cold-call on this
specifically: "How many people in this family actually need a plane ticket?"

## Twist — drop this at roughly the 15-minute mark

Deliver slowly, with pauses:

"Everyone's cost-per-mile so far has used the price of gas. But the Odyssey isn't free to run —
it's not free to own, either, but Tom and Patricia already own it. Here's a real number: the IRS
publishes a standard mileage rate every year — the number the federal government itself uses to
estimate what a mile in your own car *actually* costs, once you count not just gas but maintenance,
tires, and the fact that a car with 1,888 more miles on it is worth measurably less than one
without them. That rate, right now, is $0.76 a mile."

**Facilitator-only.** Recompute Option B live with the room: 1,888 miles × $0.76 = $1,434.88, plus
the $320 hotel, for a new Option B total of $1,754.88 — versus Option A's $1,940.80. The gap that
looked enormous a few minutes ago (driving at $602.50 vs. flying at $1,940.80 — more than 3× —
Option A category has never come remotely close) shrinks to 10.6%. Driving is still cheaper on this
fully-loaded metric, but not by much, and Option A now buys something real in return: about 3 more
days in Gilbert (Appendix G) using the exact same 5 vacation days, and dramatically less time
buckled into a car seat with a 20-month-old and a 2-month-old.

Ask: "You now have 60 seconds. Does this change your recommendation — or not?" Then, the follow-up
that matters more than the vote: **"What just broke in your original model? Were you wrong about
the price of gas — or were you just missing a way to think about the cost of the car itself?"**

Do not hand over a "correct" answer. Reasonable families genuinely disagree about whether a
government accounting convention should count against a car they already own — that's the real,
transferable tension, not a trick.

**Twist soundness check (SPEC §6):** this twist was checked against every stated Background/
Appendix fact and Modeling Assumption, read both sequentially (in the order a Hero encounters them)
and simultaneously (all at once, as a final numeric model) — it introduces no new figure that
contradicts an earlier one, only a second, real, disclosed lens (Appendix F/MA4) on a cost already
in front of the room. It holds under both readings.

## Immediate recommit

Re-vote immediately. "Did the mileage-rate recompute change your hand — or did it just change *why*
you're holding it up?"

## Close

Re-vote once more after full discussion. Ask: "Did we ask the right question at Anchor 2, or did
'cheaper' turn out to mean something different by the end?" And: "What math was new to you today,
and how did you attack it?"

## Lessons Learned

*(Migrated from the original Guide Notes.)* The original case's own facilitator materials centered
on a genuinely real family text-message exchange — "it's cheaper to drive = more Christmas
presents" versus "it takes SOOO long + we have a baby = not fun" — and the original guide's
takeaway was that both positions are emotionally and practically legitimate, and that the "right"
answer depends on what the family values, not just what's cheapest. This conversion preserves that
lesson exactly, while adding a second, mathematically real lesson the original case didn't have the
apparatus to teach: **the way you define a cost changes which option wins.** Gas-only, driving wins
by a landslide. Fully-loaded (IRS rate), driving wins by single digits. Per real cash dollars
against the stated $1,300 budget, flying isn't even affordable. Three different, all-real answers
to "which is cheaper" — the skill is knowing which one you're actually answering.

## Five Socratic Questions

Use these across Anchors 2–4 and the Data Deep Dive — each is answerable only with this case's own numbers, not general opinion.

1. Only 4 of your 6 family members need a paid plane ticket — how does the total change if you (wrongly) price all 6?
2. Your fully-loaded Option B total uses the IRS's $0.76/mile rate instead of the pump price of gas — why would a family that already owns the Odyssey care about a rate they don't literally pay?
3. Flying buys the Jacksons roughly 3 more days in Gilbert on the exact same 5 vacation days — how many dollars per extra day in Gilbert is that costing them?
4. If Option A's real cash cost blows past the $1,300 budget by several hundred dollars, what exactly would you cut first — and does that change your recommendation?
5. Appendix C's fare data is two years old — what would have to be true about 2026 fares for your recommendation to flip?

## Standards Touched On

See `case.json.standards[]` (26 ids) and `LEARNING_GOALS.md` for the full deliverable ↔ skill
matrix. In brief: decimal and whole-number arithmetic (all four operations), currency, unit
conversion (miles↔gallons via mpg), elapsed time, rounding, and two required visual displays (bar
graph, pie chart).

## Cohort Bands

See `case.json.cohort_bands[]`.

- **Full (12–20):** Anchors 2–3 run as written; the room splits into a "fully-loaded cost" faction
  and a "real cash budget" faction before the Twist forces everyone to hold both numbers at once.
- **Compressed (6–11):** Anchors 2–3 combine into one pass; D4's two visual displays are worked as
  one shared example (one option) instead of every Hero building both independently.
- **1:1 / pair (1–2):** No vote to take — Anchor 1 becomes a stated initial position instead of a
  cold-call show of hands; the guide plays devil's advocate directly, arguing whichever side the
  Hero didn't pick.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote (Anchor 1) — no explanation |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just cheaper" |
| 10:00–15:00 | Pressure-test the models: "Whose plan breaks first if the fare or the gas price moves?" |
| **15:00** | **DROP THE TWIST** — the IRS mileage rate recompute, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00–30:00 | Threaded deep conflict — two named threads: (1) "true cost" vs. "cash-in-hand cost" as competing definitions of *cheaper*; (2) money saved vs. days-with-family gained as competing definitions of *better* |
| 30:00–45:00 | Close, re-vote, reflection, Lessons Learned |
