# FACILITATOR.md — The Transfer Window

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — case.md
carries no marker comment for this by design (see the "Balance argument" guidance in `case-write`
SKILL.md); the balance argument, margin, and sensitivity notes live only here and in `case.json`'s
`balance` object.*

**Case:** The Transfer Window · **Tier:** T2 (MS-core) · **Studio:** MS Adventure
**Standards:** Pre-Calculus/Polar And Parametric — Parametric Equation, Parameter, How to eliminate
the parameter to find a rectangular equation, plus supporting Percent/Decimal/Measurement skills
(see `case.json.standards[]` for exact ids).

**Status:** Researched and computed 2026-08-31 (`RESEARCH_LOG.md`). All appendix figures are closed
and sourced. A dedicated retune pass ("RETUNE PASS — 2026-08-31") checked the margin against the
two most likely explanations for a landslide this large and ruled both out as artifacts — see
below.

**Balance flag, read before you facilitate:** on the primary metric (kilograms of deliverable
payload per day of transit time), the Direct Burn beats the Patient Drift by **15,940.5%** —
roughly 160x. This is far outside SPEC §2's ~20% cap and is **waived under MCS-46**
(`case.json.balance_test_waiver`; see `DOCTRINE_LEDGER.md`). The waiver does not mean "treat this
as close." It means the opposite: this case is not built for a Socratic debate over which side
wins — the Direct Burn wins, decisively, on real, honestly-sourced numbers, and every Hero should
land there. **What this case is actually built to teach is why the margin is this large** — that
chemical and electric propulsion differ by wildly *different* orders of magnitude on two different
axes (~800x on transit time, only ~5x on payload mass), and that a ratio metric lets the larger
asymmetry dominate completely rather than the two partially offsetting. The facilitator's job is to
run an audit of the analysis, not a debate about the winner.

## The real numbers (facilitator reference — never appears in case.md)

- Deliverable payload mass: Direct Burn 180 − 30 − 133.0 = **17.0 kg**; Patient Drift
  180 − 30 − 63.7 = **86.3 kg**. Ratio ≈ **5.1x**, Patient Drift ahead.
- Transit time: Direct Burn **0.221 days** (5.3 hr, the Hohmann-transfer coast time, S12); Patient
  Drift **180 days** (MA3, anchored to real Boeing 702SP-class all-electric GEO transfers, S8/S9).
  Ratio ≈ **815x**, Direct Burn ahead.
- Primary metric = deliverable payload ÷ transit time: Direct Burn 17.0 / 0.221 ≈ **76.9 kg/day**;
  Patient Drift 86.3 / 180 ≈ **0.479 kg/day**. Because the metric is a straight ratio, the ~815x
  term the Direct Burn wins on lands in the *denominator* the same way for both options — it is not
  offset by the ~5.1x term the Patient Drift wins on, it dominates it: 76.9 / 0.479 ≈ 160.5x
  (15,940.5%). See `case.json.balance.margin_basis` for the full arithmetic and
  `sensitivity_model.py` for a runnable reproduction.
- A dedicated retune pass re-verified, independently, that neither term is an authorial exaggeration:
  180 days sits inside real published precedent for a full electric GEO orbit-raise (not at an
  extreme of it), and the ~800x transit-time gap is a structural fact of thrust technology —
  chemical thrust runs newtons-to-kilonewtons and converts nearly all its delta-v in minutes;
  Hall-effect electric thrust runs in millinewtons and can only deliver its (larger) total delta-v
  budget continuously over months. This ratio is a property of the two real propulsion
  technologies, not of this case's specific mass/Isp/delta-v numbers — see
  `RESEARCH_LOG.md`'s "RETUNE PASS" for the full re-verification, including why no alternative real
  metric (cost-per-kg, pass/fail against the 240-day contract window) closes the gap without
  fabricating a number.

## Intro

Frame the format before anything else: this is a real trajectory sign-off that becomes a written
contract term, not a worksheet. Name the opener — "You're Talia Brooks. Whichever design you
recommend gets written into the customer's delivery contract. There's no 'we'll see' — you sign
one." Let the stakes land before moving to the Launch.

## Launch

Show Appendix B's two transfer ellipses side by side (illustrative shapes, not the case's real
numbers) — one steep and fast, one long and gradual — with no numbers beyond the general shape yet.
Ask: "Just from what you know about rocket engines versus ion/electric engines, which one do you
think wins on *payload delivered per day of transit* — and by roughly how much?" Take answers
without correcting anyone. Most rooms will correctly guess the Direct Burn is much faster and the
Patient Drift saves more propellant — that instinct is fine and expected. What almost no room will
guess correctly, without doing the math, is *how lopsided the actual per-day comparison turns out
to be*, because "electric propulsion is way more efficient" sounds like it should bank enough extra
payload to make the extra months worth it. Record the room's gut guess at the *size* of the gap
(most will guess something like "2x," "5x," or "it's close") — Close will come back to this.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the Patient Drift — the option that protects the most
payload mass?" Show of hands, both options, no discussion. Record the count — Close will ask again.

## Anchor 2 — What is the problem we're solving?

**"Is 'which one is faster' the right question?" · "What do you mean by 'saves more payload'?"**

Push the room to state the actual metric before touching an appendix: not "which trajectory is
faster" and not "which trajectory delivers more payload mass," but kilograms of deliverable payload
*per day of transit time* — a ratio of two independently-derived quantities, not either alone. If
the room lands on "we need to divide one real number by another real number, not just compare two
separate advantages," the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Make the room name the steps before opening an appendix: (1) write each option's position as a
function of a parameter using its stated semi-major axis and eccentricity, (2) eliminate that
parameter to get a rectangular equation you can actually check against the target orbit radius, (3)
verify each trajectory really reaches the target orbit at that solved point, (4) work out each
option's propellant-mass fraction via the rocket equation and how much payload survives, (5) divide
deliverable payload by transit time for each option and compare, (6) check the cumulative radiation
dose against the tolerance limit. Re-ask: "Now that we can see the steps, is our question still the
right one?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the honest gaps: Appendix E's MA1 (contract delivery window), MA2 (modeling both options as
the same geometric ellipse), MA4 (dry mass), and MA5 (radiation dose rate) are all stated,
disclosed assumptions for a real vehicle used in a fictional company's mission — none of them
changes which option wins D4's ratio. MA1 never binds either option under the case's own figures;
MA2 only affects the D1/D2 algebra (making both options solve the same curve), not the mass/time
economics; MA4 shrinks both options' payload roughly proportionally without closing the ~160x gap;
MA5 affects only the D5 radiation pass/fail check, a separate constraint from the primary metric.
**MA3 — the Patient Drift's 180-day transit time — is the one figure worth real scrutiny**, because
it is the single largest lever in the whole comparison. Ask: "If MA3 is the load-bearing figure,
should we be suspicious that it was chosen to make the Direct Burn win?" Let the room sit with that
suspicion — then, in the Data Deep Dive, follow the real evidence that it is not: 180 days sits
inside real precedent for a full electric GEO orbit-raise, not at an inflated extreme. A sharp Hero
should be able to name that lengthening MA3 never helps the Patient Drift: pushed toward MA1's
240-day contract ceiling (e.g. 239 days) the Direct Burn's margin actually *widens*, to roughly
21,000%, because a longer transit only shrinks the Patient Drift's own kg/day figure further; pushed
past that ceiling (270+ days) the Patient Drift is disqualified outright on the delivery-window gate
before the kg/day comparison is even reached. Either direction, the Patient Drift never wins — the
margin is not a knife's-edge result riding on one assumption (see `sensitivity_model.py`).

## Data Deep Dive

Now, and only now, open Appendices A–E and work D1–D6. Cold-call for D4 specifically — this is
where a Hero who correctly found the Patient Drift protects more payload (D3) but never divided by
each option's own transit time will not yet see the scale of the result.

**Facilitator-only arithmetic note.** D3: Direct Burn deliverable payload = 180 − 30 − 133.0 =
17.0 kg; Patient Drift = 180 − 30 − 63.7 = 86.3 kg. D4: Direct Burn 17.0 kg ÷ 0.221 days ≈ 76.9
kg/day; Patient Drift 86.3 kg ÷ 180 days ≈ 0.479 kg/day. Percent difference (76.9 − 0.479) / 0.479
× 100 ≈ 15,940.5%. Full derivation in `case.json.balance.margin_basis`; reproduced mechanically in
`sensitivity_model.py`.

## Twist — drop this once D4 is on the board, roughly 15 minutes in

Deliver slowly:

"Someone on the team says: 'Wait — the Patient Drift protects about 5 times more payload mass, and
electric propulsion is famous for being way more efficient than chemical. Shouldn't that count for
more? Why isn't this close?'"

Let the room sit with that. Then: "The primary metric isn't payload mass *plus* some efficiency
credit — it's payload mass *divided by* transit time. The Patient Drift really does win the payload
side of the ledger, by about 5x. But it loses the time side of the ledger by about 815x — because
chemical thrust is measured in newtons to kilonewtons and converts nearly all its delta-v in
minutes, while Hall-effect electric thrust is measured in *millinewtons*, three to four orders of
magnitude weaker, so even though it needs *more* total delta-v for the same transfer (6.0 km/s vs.
3.82 km/s), it can only deliver that thrust gradually, over months. A 5x advantage in the numerator
and an 815x disadvantage in the denominator don't average out or partially cancel — they compound.
Dividing by a denominator roughly 815x smaller has almost the same effect regardless of what sits on
top of the division, so the result lands close to that ~815x figure, not somewhere between 5x and
~815x."

**Facilitator-only: what this actually is, and is not.** This is not a "did you pick the right
side" reveal for the case as actually asked — the Direct Burn is the correct answer to D4's stated
ratio metric, and a Hero who reached it with correct D1–D6 arithmetic has not been tricked. The
twist is that the *size* of the win is not what a reasonable pre-computation intuition would
predict (most rooms guess "2x," "5x," or "close," per the Launch), and the reason is a real
mechanism — a ratio of a modest asymmetry (payload, ~5x) against a huge one (transit time, ~815x) —
not an authorial trick or a tuned number. Ask directly: "Is there a real technology where the mass
and time trade-offs are closer to the same order of magnitude — and if there were, would this case
be a much harder call?" Point back to `RESEARCH_LOG.md`'s retune finding: the ~815x gap is a
structural property of chemical-vs-electric *thrust*, present in essentially any real
chemical-vs-full-electric kick-stage comparison to GEO, not a quirk of this case's specific delta-v
or Isp numbers.

## Immediate recommit

Re-vote immediately. Ask by name: "Does this change your recommendation — or does it just change
how surprised you are by the *size* of the gap you already computed?" Most Heroes who did D1–D6
correctly should not flip; the point is whether they can now explain *why* the gap is this large,
not whether they change their answer.

## Deep conflict — two threads (20–30 min)

1. **Ratio vs. sum: why a huge asymmetry swamps a modest one.** The room already computed a ~5x
   payload advantage for the Patient Drift and a ~815x transit-time advantage for the Direct Burn.
   Why does dividing produce ~160x apart instead of something that averages the two? Walk a Hero
   through what the D4 ratio would look like if the two options' transit times were much closer
   together (say, both within 2x of each other) while keeping the same ~5x payload gap — show that
   the result would then look much more like a genuine trade-off, because neither term would
   dominate the division.
2. **What would actually have to change.** D6 asks what would have to change about either design
   for the recommendation to flip. Push past "the numbers would have to be different" to a specific
   answer: since the Direct Burn wins D4 by roughly 160x, closing the gap to parity would require
   roughly a 160x combined swing in the payload-mass ratio and/or the transit-time ratio — for
   instance, the Patient Drift's transit time would need to shrink from 180 days to roughly
   1.1 days (near-chemical speed) before the two options would even approach a fair fight on this
   metric, at which point it would no longer be describing a real low-thrust electric transfer at
   all. That is a specific, checkable claim a Hero should be able to state, not a vague "if things
   were different."

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both transfer ellipses side by side, cold-call for a gut read on size *and* winner, no numbers yet |
| 3:00–10:00 | Position defense — *"Walk us through your D4 ratio — which option wins, and by roughly how much?"* |
| 10:00–15:00 | Pressure-test the process — *"Which of your D1–D3 steps, if it were wrong, would change who wins — and which ones just change the specific numbers?"* |
| **15:00** | **DROP THE TWIST** — why a ~5x term and an ~815x term compound to ~160x instead of partially canceling |
| 15:00–20:00 | Immediate recommit — does the recommendation change, or just the room's read on the *size* of the gap |
| 20:00–30:00 | Threaded deep conflict (ratio dominance; what a real flip would actually require) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

The trap is not "picking the wrong option" — it is under-estimating the size of the correct answer
before computing it, and specifically assuming the payload-mass term and the transit-time term
should carry roughly comparable weight, the way a Hero's intuition would treat "electric is way
more efficient" as automatically enough to offset "electric takes way longer." A Hero who reasons
"electric propulsion is famous for saving fuel, so it's probably worth the extra months" has made a
real, specific analysis mistake: treating a divided metric as if the numerator's advantage and the
denominator's advantage were on the same scale. The second, related trap is stopping at D3 (payload
mass) or D2 (transit time) alone and never actually computing D4's division — a Hero who reports
"the Patient Drift keeps more payload" and "the Direct Burn gets there faster" as two separate,
competing facts, without dividing one by the other, will never see that the two facts are not
remotely the same order of magnitude, and that this is exactly what decides the case.

## Socratic questions

1. Your D3 mass fractions show the Patient Drift protects roughly 5x more deliverable payload than the Direct Burn. Your D2 transit times show the Direct Burn arrives roughly 815x faster. Why does the D4 ratio end up favoring the Direct Burn by roughly 160x — much closer to the 815x figure than to the 5x figure — instead of landing somewhere in between?
2. The Patient Drift's electric engine needs *more* total delta-v than the Direct Burn's chemical engine (6.0 km/s vs. 3.82 km/s) for the same transfer, yet still uses less propellant mass. What does that tell you about what specific impulse actually measures, and why a higher-Isp engine can need more delta-v and still burn less propellant?
3. Appendix B's specific-impulse figures (290 s chemical, 1,400 s electric) differ by about 4.8x, yet the two options' propellant-mass fractions differ by less than that in D3. Meanwhile the transit times differ by roughly 815x. What does that gap between "how different the engines are" and "how different the transit times are" tell you about what's actually driving the ~160x result — is it mostly the engines' efficiency, or mostly how they deliver their thrust over time?
4. Suppose MA3's 180-day Patient Drift transit time were cut in half, to 90 days, while every other figure in the case stayed the same. Would that fully close the D4 gap, or would the Direct Burn still win by a wide margin — and what does that tell you about how sensitive this case's real result is to its single most-scrutinized assumption?
5. If D4 had instead asked you to build a single score by adding an evenly-weighted payload-based number and a speed-based number, instead of dividing one by the other, do you think the Patient Drift would have a real shot at winning? What would you need to know to check that, and does the answer depend on the real numbers alone or also on how you choose to combine them?

## Close

**VOTE AGAIN.** "Did your recommendation change — or just your sense of how large the real gap
is?" Ask what math was new to each Hero, and specifically whether eliminating the parameter in D2,
the rocket-equation arithmetic in D3, or dividing D3 by D2 in D4 was the step that actually
surprised them.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes correctly predicted, before computing D4, that a ~5x payload advantage and an
  ~815x transit-time advantage would compound into a ~160x gap rather than landing somewhere
  between the two — or whether most rooms expected something much closer to "electric wins because
  efficiency matters more" until the arithmetic forced the surprise.
- Whether Anchor 4's suspicion about MA3 (is 180 days a tuned number?) resolved itself once the
  room worked through the real thrust-technology reasoning in the Twist, or needed to be told
  outright.
- Whether any Hero, prompted by Socratic question 4/D6, could actually name the specific change
  (transit time would need to shrink to near-chemical speed, at which point it would no longer
  describe a real electric transfer) needed to flip or even meaningfully close this case's real
  margin.

## Standards Touched On

Parametric Equation; Parameter; Percent; How to eliminate the parameter to find a rectangular
equation; How to find the percent of a number; How to divide decimal numbers; How to convert an
amount with compound units.

## Facilitator note — sensitivity (SPEC §6)

None required. This case carries no illness, death, financial-hardship, or other protected-subject
stakes — it is a routine mission-design and contract-delivery trade-off between two legitimate,
professionally defensible trajectory choices, comparable in register to Wind Triangle or
Navigation. `case.json.balance_test_waiver` documents the separate, unrelated MCS-46 exception this
case carries for its balance-test margin — a landslide margin driven by real, sourced figures, not
a modeling shortcut, kept because the setup still forces genuine multi-step analysis and the
magnitude itself is the pedagogical payoff (see the Status note above).
