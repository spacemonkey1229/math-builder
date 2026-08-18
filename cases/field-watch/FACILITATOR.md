# Guide Notes: Field Watch

**Case:** Field Watch · **Tier:** T2 · **Band:** MS-core · **Studio:** Heroes Academy
**Standards:** Variables group (partial, Advanced Operations) — all `new_coverage` (see
`case.json.standards[]` for the exact ids)

Researched and margin-resolved 2026-08-12 (`margin_pct` = 14.29, see `sensitivity_model.py`). This
file is re-checked for drift at every readiness run (the continuity checks in `case-readiness`).

## Intro

Frame the format before anything else: this is a real professional deadline decision using real
public satellite data, not a worksheet. Name the opener — "Three satellite passes, one insurance
claim file that closes at five, and two different equations that don't agree." Let the stakes land
before moving to the Launch.

## Launch

Show the three NDVI readings (0.72, 0.62, 0.51) plotted as three dots on a day-vs-NDVI axis, with
no lines drawn through them yet. Ask: "If you had to draw one straight line through these dots to
predict what happens next, which two dots would you use?" Do not confirm or correct answers here.
The point is a gut read before anyone touches the algebra.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Talia on Model B — the one that throws out the field's
oldest data point?" Show of hands, both options, no discussion. Record the count — Close will ask
them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What does 'trust' actually mean here?"**

Let confusion grow here — this is deliberate. Heroes will want to reach for "more data is always
better" as a rule of thumb. Push on it: "Talia isn't just averaging data. She's predicting the
future. Does more OLD data always make a prediction about tomorrow more trustworthy?" If the room
starts to notice the decline is speeding up on its own, the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has the right question, ask them to name the actual steps before touching the
appendices: simplify both raw models (D1-D2), solve each for its crossing day (D3-D4), compare how
the models diverge over time (D5), then convert crossing days into safety buffer against the real
deadline (D6-D7). Re-ask: "Is our question still the right one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gaps honestly: Appendix F's two Modeling Assumptions (MA1 the damage threshold,
MA2 all of the field's specific readings) are stated, not universal — Appendix E itself cites real
evidence that NDVI damage thresholds are never a single fixed number in real practice. Ask which one
actually changes the recommendation if it moves (MA1 — see Data Deep Dive).

## Data Deep Dive

Now, and only now, the numbers. Walk D1-D6's algebra and D7's margin comparison together as a room,
cold-calling for D1/D2 (the simplification step) and D5 (the disagreement expression) specifically —
these are the two places a Hero who tries to shortcut by solving the raw, unsimplified equation
directly (skipping distribute-and-combine) will visibly make a sign error, which is useful
information for the facilitator, not a moment to rescue.

**Facilitator-only algebra note.** D1: `0.72 − 0.02(day − 3)` distributes to
`0.72 − 0.02·day + 0.06`, combines to **`0.78 − 0.02·day`**. D2: `0.62 − 0.022(day − 8)` distributes
to `0.62 − 0.022·day + 0.176`, combines to **`0.796 − 0.022·day`**. D3: solving
`0.40 = 0.78 − 0.02·day` gives **day 19**. D4: solving `0.40 = 0.796 − 0.022·day` gives **day 18**.
D5: `(0.78 − 0.02·day) − (0.796 − 0.022·day) = −0.016 + 0.002·day` — the models' disagreement grows
by 0.002 NDVI-points per day, a genuinely useful fact: the farther out you predict, the more the two
models pull apart.

**Facilitator-only margin note.** Buffer: Model A = 26 − 19 = **7 days**, Model B = 26 − 18 =
**8 days**. Margin: **14.29%**, Model B wins (more buffer). This margin holds Model B as the winner
across a ±50% flex of MA1's calibration allowance (effective threshold 0.385-0.415) — margin ranges
12.02%-17.09%, no flip. This is a genuine two-sided balance, not a paper margin: Model A has real
quantified support too — plugging day 13 into Model A's own equation predicts NDVI **0.52**, only
0.01 off Pass 3's real measured 0.51, a check against data Model A never used to build itself.
Model B's affirmative case (steeper slope, a shorter forward reach past its own last data point) and
Model A's affirmative case (a real, checkable track record; less exposed to a single interval's
noise) are both real — B just wins the specific buffer comparison the case is built to decide.

**Facilitator-only extra observation.** Model A's own residual check (0.52 predicted vs. 0.51
actual) means Model A wasn't *unreasonable* even where it disagrees with a real reading — it was
close. Worth naming if a Hero pushes hard on "why trust B at all": the case doesn't ask which model
is right, only which one wins the specific decision the deadline forces.

**Facilitator-only: the sharpest possible follow-up, for a room that wants it.** The 0.01 residual
looks small as an absolute NDVI gap, but reframe it as a rate: over the Pass 2→Pass 3 window (5
days), the field actually declined 0.62−0.51 = 0.11, while Model A's own slope (−0.02/day) predicts
only 0.02×5 = 0.10 of decline over any 5-day window — a real 9.09% underestimate of that interval's
true decline. Because the case's own data shows the decline accelerating, that underestimate would
plausibly grow, not shrink, over the 6 additional days between day 13 (where the check was made) and
day 19 (Model A's claimed crossing day) — meaning Model A's "close" residual is arguably biased in
exactly the risky direction (predicting a later, safer-looking crossing day than reality). This is a
real, correct, deeper reading of the same numbers — not a flaw in the case, a second layer for a
room that's ready for it. Do not lead with this; it belongs only as a response to a Hero who
pushes past D3/D4's "Model A was pretty close" into "how close, exactly, as a rate."

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"It's the middle of the discussion. The satellite data provider issues a correction notice: Pass
3's sensor had a known calibration drift on that date. The corrected NDVI reading for Pass 3 is
higher than what was originally reported — the field's condition on that day wasn't quite as bad as
first recorded."

"Does Model B still deserve more trust than Model A?"

**Facilitator-only: what the numbers actually do.** The corrected Pass 3 NDVI is **0.54**, not
0.51 — a real, disclosed sensor-calibration scenario. Recomputed: Model B's slope becomes
`(0.54 − 0.62)/5 = −0.016`, its crossing day pushes out to **day 21.75**, and its buffer collapses
to **4.25 days** — now *less* than Model A's unchanged 7-day buffer. **The verdict flips: Model A is
now the safer bet**, by a real **64.71%** margin. Do not hand this reasoning over unprompted; let a
Hero who did D3/D4 carefully re-derive Model B with the corrected value — the real skill being
tested is recognizing that a model built from fewer, more recent data points is also more exposed to
a single bad data point turning out to be wrong.

**Facilitator-only: the twist also quietly reverses Appendix C's own story.** Appendix C explains
the models disagree because "the decline sped up between Pass 2 and Pass 3" (slope B steeper than
slope A). After the correction, slope B becomes **−0.016**, shallower than slope A's −0.02 — the
corrected data shows the decline *decelerating*, not accelerating. Nothing in the case text is
technically wrong (Appendix C is a base-case-only explanation, never re-stated after the twist), but
a sharp Hero who re-reads Appendix C post-twist can notice this on their own — let them. It's a
second, independent reason Model B's original justification doesn't hold up, on top of the raw
buffer numbers. Don't announce it; if nobody catches it, it's fine to leave it as a discovery for a
future run.

## Immediate recommit

Re-vote immediately. Ask by name: "Does the correction change your vote, or just how confident you
are in it?" That distinction is the transferable skill, not the vote itself.

## Deep conflict — three threads (20-30 min)

1. **More data vs. more recent data.** Model A uses the field's longer history; Model B reacts to
   its newest, most alarming stretch. The twist punishes Model B for over-trusting one data point.
   Does that mean "more data" wins in general, or does it just mean this particular twist happened
   to fall on Model B's side?
2. **A disagreement that grows.** D5's expression shows the two models pull apart by 0.002
   NDVI-points every day. Why does that matter for how far out either model should be trusted to
   predict?
3. **A verdict that flips on someone else's correction.** The twist isn't Talia's error — it's the
   data provider's. Is a margin that can flip from a third party's calibration notice ever really
   "safe," or is that just the real, permanent risk of working from someone else's sensor?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show the three dots, cold-call for a gut read, no algebra yet |
| 3:00–10:00 | Position defense — *"Convince us more data doesn't automatically win"* |
| 10:00–15:00 | Pressure-test the models — *"Whose crossing day is most fragile?"* |
| **15:00** | **DROP THE TWIST** — the sensor calibration correction, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (more data vs. recent data; a disagreement that grows; a flip on someone else's correction) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes will assume more data always means a more trustworthy model and pick Model A by
default, without noticing the case's own data shows the decline is accelerating — Model A's longer
history is also its most out-of-date. A second version: Heroes who correctly solve D3/D4 will often
stop there and never actually run D6/D7's buffer comparison, missing that a 1-day difference in
predicted crossing day is exactly what a real professional judgment call like this one lives or dies
on.

## Socratic questions

1. Model A uses more data. Model B uses less data but the most recent trend. Which one would you trust with your own money on the line — and does "more data" always mean "more trustworthy"?
2. D5 gives you a single expression for how much the two models disagree, as a function of day. Does that disagreement grow, shrink, or stay constant the further out you predict? What does that tell you about trusting either model for a day far in the future?
3. MA1's threshold (0.40) is explicitly not a universal number — Appendix E says so directly. What would you want to see before you trusted a specific insurer's specific threshold?
4. Both models predict the field crosses the threshold before the deadline. Does that mean the claim is safe either way — or does the 1-day gap between them still matter?
5. Talia has one model to report before five o'clock. What does she tell her supervisor — and does the twist change the answer?
6. Model A's equation predicts NDVI 0.52 on day 13 — Pass 3's real, measured value that day was 0.51, a reading Model A never used to build itself. Does that close check change how much you trust Model A, even though it still loses the buffer comparison?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that didn't
move at all after the twist is worth asking about directly: did the twist not land, or did the room
already understand how fragile Model B's smaller data set was?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes distrusted the "more data automatically wins" heuristic on their own, or needed the
  twist to actually see the risk of a smaller, more recent data set.
- Whether D5's "growing disagreement" expression landed as a genuine insight about prediction
  distance, or was treated as just another algebra step.
- Whether the twist's "third-party correction, not your own error" framing produced different
  reflection than a self-caused error would have (compare to Apron Order's transcription-error
  twist, which was self-caused).

## Standards Touched On

Like Terms · Distributive property · How to add and subtract an expression with variables · How to
solve a multi-step equation with a variable on one side

## Facilitator note — sensitivity

None required (SPEC §6) — the stakes here are a professional claims deadline and an analytical
judgment call, not personal loss or hardship.
