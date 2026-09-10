# Facilitator Notes — Boulderfield

**Case:** Boulderfield · **Tier:** T2 · **Band:** MS-core · **Studio:** Adventure
**Standards:** see `case.json.standards[]` for the exact ids (25 skills — integer, positive
number, negative number, operation, expression, equation, variable, rounding, addition,
subtraction, multiplication, division, percent, bar graph, and their paired "how to…" skills)

**SPEC §6 flag:** this case involves a simulated backcountry search-and-rescue incident with a
real (if unnamed) injured climber. It is framed around *reaching* the patient faster, never around
casualty math — same "protection, not destruction" framing SPEC §6 asks for. Keep the facilitation
focused on the routing/timing decision, not on dwelling on worst-case outcomes for the patient.
Talia Ferro, the injured climber, and this specific incident's timeline are this case's own
scenario data — real, sourced facts are the trail statistics, Naismith's Rule, the NWS wind chill
formula, and Rocky Mountain National Park's real, recurring search-and-rescue operations (Appendix
E, S9); no specific real incident or real injured person is being depicted.

## Intro

Frame the format: a real routing decision under time and terrain pressure, not a worksheet with a
story stapled on. Name the opener — "Two routes reach the same summit. One is a mile and a half
longer. Which one gets a rescue team there faster?" Worth naming about Talia: she personally
stopwatch-times both routes herself, off-duty, every season — she does not trust a guidebook
number she hasn't verified herself, which is exactly the habit this case asks Heroes to build.

## Launch

Read the Overview aloud, then Background's first three paragraphs — both routes share the same
lower trail to the Boulderfield before splitting; the Keyhole is longer but maintained; The Loft
is shorter but unmarked above the split. Do not reveal any of Appendix B's adjustment numbers yet.
Ask: "Just from what you've heard — does 'the shorter route' sound like the faster one, or not?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"The Keyhole Route or The Loft?" Show of hands, no discussion yet. Record the count — Close asks
again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'faster'?"**

Push on what "faster" actually means here. Faster to the Boulderfield? To the summit? To the
patient specifically, wherever the patient actually is? Let the room sit in the ambiguity — "Is
anyone courageous enough to say what we're actually optimizing before we start comparing miles?"

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has a working definition of "faster," ask them to name the actual steps: each
route's one-way distance and elevation gain (Appendix A), the Naismith's Rule formula that turns
those into a raw time estimate (Appendix B), and the two adjustments — a shared night-pace
multiplier and The Loft's own route-finding penalty — that turn the raw estimate into a real
total. Re-ask: "Given how we just defined 'faster' — is that still the right process?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix D's five Modeling Assumptions as a group, out loud, before anyone computes
anything. Ask which ones the room thinks matter most. (Facilitator note: MA1 — the ×1.3 night-pace
multiplier — is the single most load-bearing assumption in the whole case, with MA2's 55-minute
route-finding penalty a close second; MA3, MA4, and MA5 do not move the A-vs-B time margin at all,
only the D4 and D5 side calculations. Let the room guess first — the Twist and Q1/Q4 below are
where this gets tested directly.)

## Data Deep Dive

Now, and only now, the numbers. Walk D1 (one-way breakdown), D2 (raw Naismith estimate), and D3
(adjusted total time) together as a room.

**The trap:** most Heroes will see that The Loft is shorter in both distance (13.0 mi vs. 14.5 mi)
*and* has a faster raw Naismith time (4.8167 hr vs. 4.9667 hr), and declare it the obvious winner
before ever opening Appendix B's adjustments table. That reasoning treats "shorter on the map" as
equivalent to "faster in practice," and skips the fact that The Loft is unmaintained and largely
unmarked above the Boulderfield — Appendix B's +55-minute route-finding penalty is exactly the
cost of that, and it is large enough to flip the outcome. Cold-call on this specifically: "You've
got your raw Naismith numbers. Now open Appendix B's adjustments table — does anything change?"

Show the actual split:

- **Option A (The Keyhole Route)** — raw Naismith 4.9667 hr, adjusted by the night-pace multiplier,
  totals **387.4 minutes (about 6h 27m)**
- **Option B (The Loft)** — raw Naismith 4.8167 hr, adjusted by the night-pace multiplier, **plus
  the 55-minute route-finding penalty**, totals **430.7 minutes (about 7h 11m)**
- **Margin: 10.05%** — A is faster by about 10.05% on total adjusted time, comfortably inside the
  ~20% cap. The route that is shorter, and even faster on the raw hiking-and-climbing formula
  alone, loses once the case's own real terrain conditions are priced in.

## Twist — drop this at roughly the 20-minute mark

**This is the same Twist already live in `published/Boulderfield - Interactive.html`'s gated
"Reveal the Twist" panel — deliver that one, do not invent a competing twist.**

Deliver slowly, with pauses:

"New information from dispatch: the injured climber's party reports he has self-descended, in
pain, back down to the Boulderfield — the point where both routes are still the *same trail*.
He is no longer above the split at all."

Ask the room: "Using Appendix A's shared-segment numbers — does your recommendation still hold?
What, exactly, happens to the 10.05% margin you just computed?"

**Facilitator-only — the flaw.** The entire 10.05% margin came from what happens *above* the
Boulderfield: the Keyhole's longer-but-maintained upper section versus The Loft's
shorter-but-penalized upper section. Below the Boulderfield, on the shared trail, there is no
"Option A" or "Option B" at all — both routes are the identical trail. Recomputing the timing
model on the shared segment alone (5.5 mi / 3,360 ft) gives both routes the exact same total time,
**274.04 minutes — a dead tie.** A Hero who leaned on "The Keyhole wins by about 10%" now has to
recognize that number was never a property of the *routes* in the abstract — it was a property of
*where the patient is on those routes*, and the moment that changes, so does the entire comparison.

Ask: "Does this change your recommendation — or not?" A strong answer names that the case's whole
margin lived entirely in the upper, route-specific segment, and ceases to exist the moment the
patient is on the shared lower trail.

Do not hand over a "correct" recommendation either way. Both options are still defensible before
the Twist and after — the point is forcing a Hero to notice that a real-world number can depend
entirely on an assumption (here, patient location) that was never stated as fixed.

**Twist soundness check (SPEC §6):** this twist introduces no new figure and changes no Appendix
value — it recomputes the *same* Appendix A/B figures on the shared lower segment instead of the
full route, which both routes already state they share (Background, Appendix A). It survives every
reading of every stated assumption because it depends on none of MA1-MA5's values, only on which
segment is being timed. `sensitivity_model.py`'s `evaluate()`/`evaluate_twist()` confirm the margin
collapses from 10.05% to exactly 0% without needing any new data.

## Immediate recommit

Re-vote immediately. "Did the new information change your hand — or did it just change how
confident you are about *why* you're holding it up?"

## Close

Re-vote once more after full discussion. Ask: "Did we ask the right question at Anchor 2, or did
'faster' turn out to mean something more specific by the end?" And: "What math was new to you
today, and how did you attack it?"

## Lessons Learned

The case's own numbers make a point neither option can dodge: a 10.05% margin, built entirely from
one 55-minute assumption and one ×1.3 multiplier, is not the same thing as a *stable* fact about
which route is "really" faster. The Twist shows the margin can vanish entirely — not because any
number was wrong, but because the assumption underneath it (where the patient is) changed. The
transferable lesson: **before you trust a close margin, ask what it's built on, and whether that
foundation is fixed or just assumed to be fixed.**

## Five Socratic Questions

Use these across Anchors 2–4, the Data Deep Dive, and after the Twist — each is answerable only
with this case's own numbers, not general opinion.

1. The Keyhole Route beats The Loft by about 10.05% on total time — what would the route-finding penalty, or the night-pace multiplier, have to become before that margin flips?
2. The Loft is shorter in distance *and* has a faster raw Naismith estimate than the Keyhole — so why does the Keyhole still win once every adjustment is applied, and what does that tell you about trusting a "shorter route" claim on its own?
3. Appendix D sets the night-pace multiplier at ×1.3 and the route-finding penalty at 55 minutes — which of those two assumptions, if it moved, would flip the margin faster, and how do you know without recomputing both from scratch?
4. At the Boulderfield, the air temperature and the wind chill differ by 19°F; at the summit, they differ by 23°F — using only addition and subtraction of signed numbers, why is the summit's gap bigger even though its wind speed assumption (35 mph) is only 10 mph higher than the Boulderfield's (25 mph)?
5. If the patient's position changes from "above the split" to "at the Boulderfield," the margin goes from 10.05% to 0% — what, mathematically, did that change actually remove from the comparison, and could the same kind of change happen to any of this case's other numbers?

## Standards Touched On

See `case.json.standards[]` (25 ids) and `LEARNING_GOALS.md` for the full deliverable ↔ skill
matrix. In brief: integer, positive number, negative number, operation, expression, equation,
variable, rounding, addition, subtraction, multiplication, division, percent, and bar graph, each
paired with its "how to…" skill.

## Cohort Bands

See `case.json.cohort_bands[]`.

- **Full (12–20):** Anchors 2–3 run as written; the room splits into a "shorter route wins"
  faction and a "terrain matters more than distance" faction before the Twist forces a live
  recompute of the whole comparison.
- **Compressed (6–11):** Anchors 2–3 combine into one pass; D3's total-time comparison is worked
  as one shared example instead of every Hero building both routes independently.
- **1:1 / pair (1–2):** No vote to take — Anchor 1 becomes a stated initial position instead of a
  cold-call show of hands; the facilitator plays devil's advocate directly, arguing whichever
  route the Hero didn't pick.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote (Anchor 1) — no explanation |
| 3:00–8:00 | Position defense: "Convince us why it's actually faster, not just shorter" |
| 8:00–13:00 | Define the process (Anchor 3): what data would actually settle this? |
| 13:00–20:00 | Data Deep Dive: raw Naismith estimates, then Appendix B's adjustments — name the trap |
| **20:00** | **DROP THE TWIST** — the patient's self-descent to the Boulderfield, delivered slowly |
| 20:00–25:00 | Immediate recommit: does any hand move? "What actually broke?" |
| 25:00–35:00 | Threaded deep conflict — two named threads: (1) "shorter on the map" vs. "faster once terrain and darkness are priced in" as competing definitions of "the right route"; (2) a margin that looked meaningful (10.05%) collapsing to exactly 0% on a single change in where the patient is |
| 35:00–45:00 | Close, re-vote, reflection, Lessons Learned |
