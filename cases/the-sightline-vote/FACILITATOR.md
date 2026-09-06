# Guide Notes: The Sightline Vote

**Case:** The Sightline Vote · **Tier:** T2 · **Band:** MS-core · **Studio:** Heroes Academy
**Standards:** Geometry / Fundamentals Of Geometry — all 18 skills in this exact group, reinforcing
(not newly closing) coverage; see `case.json.reinforcement_note` for why `new_coverage[]` is
honestly empty.

Researched and margin-resolved 2026-09-05 (`margin_pct` = 14.56, see `sensitivity_model.py`). This
file is re-checked for drift at every readiness run (the continuity checks in `case-readiness`).

## Intro

Frame the format before anything else: this is a real public-safety funding decision with a
ten-day clock, not a worksheet. Name the opener — "You are the only traffic engineer this city has.
The council votes in ten days. You've got two options and no time to build a mockup of either."
Let the stakes land before moving to the Launch.

## Launch

Show the plan-view diagram of the current intersection (no angle numbers labeled) next to a real
photo or diagram of a T-boned car at a skewed intersection. Ask: "Just from the shape, which of the
two fixes do you think is actually safer?" Do not confirm or correct here. Most rooms will assume
"safer" and "more expensive" always point the same direction — that assumption is the trap, and
it's worth recording out loud before anyone touches a calculator.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Dana on The Offset Bypass — the cheaper one, the one
some of you will assume is the 'lesser' fix?" Show of hands, both options, no discussion. Record
the count — Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'safer'?"**

Let confusion grow here — deliberate. Heroes will want to jump to "which one looks safer" or "which
one is obviously the real fix," but the case only grades one specific number: sightline safety
score *per dollar of construction cost*. Push on it: "The state has a minimum safety standard.
Both options clear it. So is 'safer' even the graded question anymore, or is it 'safer for what
it costs'?" If the room lands on "the graded metric and the 'which is truly safest' question are
two different things" on its own, the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "truly safest" from "the graded number," ask them to name the actual steps
before touching the appendices: correctly identify point/line segment/ray/vertex on each diagram
(D1), derive all four angles at the current skewed crossing and check supplementary/vertical
relationships (D2), confirm Option A's right angles and the ADA ramp's complementary split (D3),
derive Option B's angle from the parallel lot line via the transversal relationship (D4), and only
then compute the safety-score-per-dollar comparison (D5). Re-ask: "Is our question still the right
one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gap honestly: Appendix D's two Modeling Assumptions (MA1 the shared base
reconstruction cost, MA2 the land acquisition cost) are stated, not sourced — no public cost record
exists for this exact, fictional intersection. Ask which one changes the *graded* number if it
moves. Unlike a case where the assumptions are load-bearing on nothing (roofline-call), here the
honest answer is **both matter to the margin, but neither flips the winner** — Option B wins the
graded metric at every combination of MA1/MA2 tested within +/-50%. Let a sharp Hero find this
themselves before confirming it.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's vocabulary labels, D2's current-intersection angle
derivation, D3's right-angle and complementary-split check, D4's parallel/transversal derivation,
and D5's safety-score-per-dollar comparison together as a room, cold-calling for D2 and D4
specifically — these are where a Hero who never actually applied the intersecting-lines or
parallel-transversal relationship (as opposed to just eyeballing the diagram) will visibly
struggle, which is useful information for the facilitator, not a moment to rescue.

**Facilitator-only geometry note.** Current intersection: 50 deg (acute, x2, vertical pair,
congruent) and 130 deg (obtuse, x2, vertical pair, congruent); each acute/obtuse adjacent pair sums
to 180 deg (supplementary) — D2. Option A: all four angles are exactly 90 deg (right angles) by
construction — D3; the ADA curb ramp splits one 90 deg corner into a given 35 deg angle and a found
55 deg angle, and 35 + 55 = 90 (complementary). Option B: the connector lane is built parallel to
the platted lot line, which meets Kellner Avenue (the transversal) at a given 75 deg angle; by the
Corresponding Angles relationship, the connector lane meets Kellner Avenue at that same 75 deg
angle (co-interior partner: 105 deg) — D4.

**Facilitator-only cost note.** Safety score = sin(angle): Option A = sin(90 deg) = **1.0** (the
maximum possible); Option B = sin(75 deg) = **0.9659**. Total cost: Option A = $400,000 (MA1) +
$80,000 (MA2) + 280 ft x $21/ft = **$485,880**. Option B = $400,000 (MA1) + 460 ft x $21/ft =
**$409,660**. Safety-score-per-dollar: A = 2.0581e-6, B = 2.3579e-6. **Margin: 14.56%, Option B
wins.** The single biggest lever on this margin, if a Hero wants to argue with it, is MA1 (the
shared base cost) and MA2 (the land cost) — not the angle geometry, which is fully determined by
the site's own real, derived values.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Dana takes her numbers to the council's grants administrator, hoping for a state safety-grant
match. The administrator pulls up the actual grant terms: the state's Highway Safety Improvement
Program will reimburse 60 percent of construction cost — but only for a design that reaches at
least 85 degrees. 'The Offset Bypass doesn't qualify. It's still a 75-degree intersection. You'd be
paying the full $409,660 yourself.'"

"Does the grant change what Dana should actually recommend?"

**Facilitator-only: what the numbers actually do.** With the grant applied only where the design
reaches 85 deg or more (`sensitivity_model.py`'s `evaluate_twist`): Option A's NET cost drops to
$485,880 x 0.40 = **$194,352** (it qualifies at 90 deg); Option B's net cost stays the full
**$409,660** (75 deg does not qualify). New safety-score-per-dollar: A = 5.1453e-6, B = 2.3579e-6.
**The twist doesn't just erode B's margin — it fully reverses the verdict: Option A now wins by
118.22%.** Do not hand this reasoning over unprompted; let a Hero who took Anchor 4's finding seriously
(that the graded metric is sensitive to MA1/MA2, even though the winner wasn't) reason toward why a
*grant eligibility threshold* is a different kind of lever entirely — one the case's own appendices
never mentioned, because Dana didn't know about it either until this moment.

## Immediate recommit

Re-vote immediately. Ask by name: "Does the grant change your vote — or does it just tell you that
the number you were graded on was never the only number that mattered?" That distinction is the
transferable skill, not the vote itself.

## Deep conflict — three threads (20-30 min)

1. **The metric you're graded on isn't always the metric that decides the vote.** Safety-score-
   per-dollar is real, and Option B wins it cleanly — until a grant program with its own angle
   threshold changes what "per dollar" actually means. Is that a flaw in the case, or a real lesson
   about reading the fine print before recommending a number?
2. **Diminishing returns, made concrete.** Going from the current 50-degree skew to Option B's
   75 degrees is a 26.09% relative gain in the safety score; going from 75 to Option A's full 90
   degrees is only a 3.53% relative gain. Why does the *last* 15 degrees cost so much more (land,
   title work) for so much less safety-score benefit than the *first* 25 degrees did?
3. **Whose $80,000.** MA2's land-acquisition figure is the case author's own reasoned estimate, not
   an appraisal. Is a stated, reasoned dollar figure trustworthy enough to help decide a real
   public vote — and what would you want to see before you trusted it more, or less?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show the current intersection, cold-call for a gut read, no formulas yet |
| 3:00–10:00 | Position defense — *"Convince us the graded number is the number that matters"* |
| 10:00–15:00 | Pressure-test the models — *"Whose recommendation is most fragile to a bad assumption?"* |
| **15:00** | **DROP THE TWIST** — the grant threshold, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (graded metric vs. grant eligibility; diminishing returns; whose $80,000) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes will assume "more perpendicular" and "safer" and "the better recommendation" all point
the same direction, and that the cheaper option (Offset Bypass) must be settling for less safety to
save money. Watch for a pitch that asserts The Squared Corner is "obviously" the better
recommendation because 90 degrees beats 75 degrees, without ever running D5's actual
safety-score-per-dollar comparison — it has not done the arithmetic, and the arithmetic says the
75-degree option is the better value, right up until the twist changes what "value" means.

## Socratic questions

1. Option B's connector lane ends up at exactly 75 degrees — the real state minimum, not a comfortable margin above it. Why might a Hero be more nervous recommending an option that just barely clears a standard than one that clears it by 15 degrees, even after running the numbers?
2. D4 asks you to derive Option B's angle using the parallel-lines/transversal relationship rather than measuring it directly. What would change about your confidence in that 75-degree number if the platted lot line's own angle to Kellner Avenue turned out to be wrong?
3. Going from the current skew to Option B is a much bigger safety-score gain than going from Option B to Option A. Does that mean Option A's extra safety isn't worth having — or does it mean "worth it" depends on a question this case's numbers alone can't answer?
4. After the grant threshold lands, Option A wins by 118.22 percent instead of losing by 14.56 percent — a full reversal, not just an erosion. Which of those two numbers would you want in front of you if you were the one signing Dana's recommendation?
5. Dana has ten days. What does she actually tell the council — and does the grant threshold change the answer, or just how confident she should sound giving it?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that voted for
B at Anchor 1 purely on cost and stays with B after the twist for a *different, numbers-based*
reason (or genuinely reverses to A once the grant is on the table) has moved, even if the count
looks similar.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Anchor 4's "the winner is stable, the margin isn't" finding landed as a discovery or had
  to be told outright.
- Whether the "cheaper must mean less safe" trap was the actual sticking point, or whether D2/D4's
  angle-pair reasoning was the harder gate for most Heroes.
- Whether the twist's full flip (not just an erosion) felt earned or felt like the case moving the
  goalposts — worth listening for directly, same open question roofline-call's Guide Notes flagged.

## Standards Touched On

Point · Line Segment · Ray · Vertex · Degree · Acute Angle · Obtuse Angle · Right Angle · Parallel
Lines · Perpendicular Lines · Transversal Line · Congruent · Supplementary Angles · Complementary
Angles · Vertical Angles · Adjacent Angles · How to find angle measures of intersecting lines · How
to find angle measures given parallel lines, a transversal line and at least one angle measure

## Facilitator note — sensitivity

**Required (SPEC §6):** this case touches a real public-safety topic (two car crashes, one T-boned
driver per incident) as its inciting event. Frame the Overview's crashes matter-of-factly at the
open — property damage and a scare, not a fatality or injury the case dwells on — and steer
discussion toward the engineering and funding decision, not toward dwelling on the crash itself. No
learner in this cohort should be assumed to have been in a car crash, but the topic is common enough
that a light touch at Launch is warranted.
