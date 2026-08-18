# Facilitator Guide — Air Traffic Controller

MS | Heroes Academy | Anchor-ladder format (SPEC.md, Section 7, "The facilitator artifacts")
**Primary metric:** gallons of fuel remaining at touchdown, Option A (OGG) vs. Option B (SFO) ·
**Margin:** 5.6% (933.2 gal vs. 881.4 gal) — see the Sensitivity note before Lessons Learned for
the ±50% flex result on this case's one real modeled assumption.

Legacy source: `source/Y2/Session 2/Air Traffic Controller/Guides Notes.docx`. The original Guide
Notes had no timed plan — an Intro, Anchors 1/2/3/5 (no Anchor 4 in the original numbering), a
Data Deep Dive, a two-part Twist, and a Close. This guide migrates that shape into the current
11-anchor ladder, keeps the original Twist's real stakes (organs in transit needing a same-night
connection), and adds a timed plan and sourced grounding the original did not have.

---

## Intro

Frame the format before naming the math: this is a decision made under a ticking clock, with a
damaged aircraft and no do-overs. Don't open with fuel arithmetic — open with the moment: a green
dot on a radar screen, hours from anywhere, and a controller who has seconds to decide, not hours.

## Launch

Read the Overview aloud (or play the exchange as a two-voice scene: captain and controller). Stop
exactly where the case does — Desirae's hand hovering over the flight strip. Do not hand out
Appendix A's distances yet.

## Anchor 1 — TAKE A STAND AND VOTE

"Is anyone courageous enough to stand with Option A — send them back to OGG?" Cold-call for a
vote, no reasoning allowed yet. Write the split on the board.

## Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

"What are we actually trying to find out here?" Let it get messy on purpose. A room will often
start with "which airport is closer" — push back gently: closer to what end? Fuel safety? Weather
safety? Runway length? Let the room sit in that confusion; naming that there might be *two*
different problems bundled into one dilemma (a fuel question and a weather-risk question) is the
real Anchor 2 win here, not a fast answer.

## Anchor 3 — WHAT IS THE PROCESS?

"If we had the data, how would we actually decide?" Push for a concrete comparison, not a vibe —
"we'd compute how much fuel each route burns and see what's left" is a real process. Re-ask
Anchor 2 once a process is on the board: "given this process, are we even asking the right
question, or just the fuel half of it?"

## Anchor 4 — WHAT DON'T WE KNOW?

"What are we assuming? Which assumptions are load-bearing?" Surface, without confirming or
denying yet: does the leak rate ever change again? Does the plane definitely make it either way?
Is the storm actually dangerous to fly through, or just uncomfortable? Bank these — Appendix F's
Modeling Assumptions (MA1-MA3) answer the fuel-rate questions directly; the storm-risk question is
deliberately *not* answered by any appendix, because it isn't a fuel-math question.

## Data Deep Dive

Now, and only now, hand out Appendices A, C, E, and F. Let Heroes work D1 (the steady-state rate)
and D2/D3 (the two fuel-burn totals) before anyone announces which option "wins."

## Twist

**Drop this at roughly the 15-minute mark**, slowly, with pauses — after the room has a fuel
number on the board for both options but before the discussion has fully settled on one answer.

> "One more piece of information just came in. Flight 862 is carrying five organs for transplant
> — three hearts, a liver, and a kidney — already in transit, already on a clock. If this plane
> lands in San Francisco, there's a real chance a connecting flight can get them to Seattle in
> time for scheduled procedures tonight. If it turns back to OGG, that chance is gone — there is
> no same-night path from Kahului to Seattle. Does this change your recommendation to the pilot?"

**What this invalidates:** the comfortable version of "just compare the fuel numbers and pick the
bigger one." Even a room that correctly worked out Option A's larger fuel margin now has to weigh
that margin against a real, time-critical cost to choosing it. It does not make Option B
"correct" — SFO still has a smaller fuel cushion and the Twist adds urgency, not certainty (a
connection might still be missed, weather in San Francisco or Seattle could still slip, ground
handling takes time). It genuinely raises the cost of choosing A without erasing the real
argument for A.

**The follow-up (the whole point):** *"What just broke in your model? Were you wrong, or just
missing information?"* Push the room to say out loud that D1-D4's fuel numbers haven't changed at
all — the Twist doesn't touch the arithmetic. What changed is what the *numbers are worth*.
A close, defensible fuel margin (5.6%) can be swamped by a consideration the fuel math was never
built to capture. That's the transferable skill: a "winning" number is not the same as a complete
answer.

**Soundness check (SPEC.md §6 / case-write §11):** read sequentially against Appendix F's MA1-MA3
and case.json's MA1-MA4, in order — the Twist introduces no new numeric parameter and changes none
of D1-D5's given data, so it cannot contradict any of them; it is purely an additional,
non-numeric consideration layered on top of an unchanged fuel calculation. Read simultaneously —
holding MA1-MA4 and the Twist at once — the same holds: D1-D5's arithmetic is entirely
distance/rate/weight-based and the Twist supplies none of those, so no reading of the stated
assumptions can make the Twist interact with, contradict, or double-count anything in the base
model. (This is different from a twist that changes a quantity inside `evaluate()` — this one
changes what the room *weighs*, not what anyone computes, which is why `sensitivity_model.py`
does not ship an `evaluate_twist()` for this case; see that file's header comment.)

## Close (10 minutes left)

VOTE AGAIN. "Did we ask the right question? Who's changing their answer, and why?" Ask
specifically who moved *because of the fuel numbers* versus who moved *because of the Twist* —
those are two different kinds of "changed my mind" and worth distinguishing out loud.

## Lessons Learned

*(Preserved from the legacy Guide Notes, lightly edited for the anchor-ladder format.)* You may be
faced with a real dilemma that is equally challenging to weed through. There may not be a single
right answer, because there are many variables and the future is entirely unpredictable — but if
you use good logic and thinking, you can at least tip the scales in your favor. This case's own
math is a clean example: the fuel comparison is close (5.6%) and genuinely favors the shorter
route, and that is still not the whole answer — a damaged aircraft flying back into the storm that
damaged it, and a decision that affects whether transplant organs make their window, are real
considerations the fuel arithmetic was never built to weigh. One layer for a facilitator to sit
with privately: this case's fuel margin is close specifically because the aircraft's position was
tuned to make it close (see case.json's `legacy_conversion_note`) — most of the actual flight, a
Hawaii-mainland engine failure is *not* a close fuel call at all, it heavily favors turning back.
Naming that honestly, if a sharp Hero asks why the position is what it is, is more useful than
pretending the numbers were always going to land this close.

## Standards Touched On

See `case.json.standards[]` and the case.md Appendix H "How To…" list — generated mechanically
from `readmodel/standards_spine.json`, not retyped by hand.

---

## Five Socratic questions

1. Option A leaves 933.2 gallons in the tank at touchdown; Option B leaves 881.4 — Option A wins by 51.8 gallons. Is 51.8 gallons out of a 6,875-gallon tank a large safety margin or a small one? What would you need to know to answer that?
2. You computed a steady-state leak rate from Appendix E's plateaued readings. Why does it make sense to ignore the earlier, lower readings when projecting fuel burn over more than a thousand remaining miles?
3. The distance to SFO (1,214 mi) is only 14 miles farther than the distance back to OGG (1,200 mi) — about a 1% difference in distance. Why does that turn into a real, non-trivial difference in fuel remaining?
4. If Typhoon Ignacio had already moved out of the return path entirely, would that change your recommendation? Which option does the storm's position actually affect — the math, the risk, or both?
5. The Twist tells you organs in transit may only make their transplant window through SFO. Does that change your D1-D4 answer? If not, what exactly *does* it change about how you'd defend your choice to the pilot?

## The trap, named explicitly

Most students will compute only the 14-mile distance difference between the two routes (1,200 vs.
1,214 mi, about 1%) and quietly assume the two options are "basically the same" on fuel — they
never notice that the same leak rate applied consistently over *either* distance compounds a
small distance gap into a real, if modest, fuel-margin gap once D1's rate is actually multiplied
through in D2/D3. A second, related trap: students will default to treating whichever option has
more fuel left over as automatically the safer choice, without weighing that Option A means flying
a damaged aircraft back into the same storm that damaged it.

## Sensitivity note

Aviation-emergency case; the base fuel math does not require modeling a crash or a death outcome
(both options land with positive fuel remaining by construction, per case.json's
`sensitivity_note`). The Twist introduces a medically-weighted stake (organ transplant timing) —
flag this for the discussion lead per SPEC.md Section 6. It is deliberately framed around
*delivering* organs in time (a "doses delivered" framing, not a casualty framing) and around
strangers' medical need, not a personal family-hardship subplot — the legacy docx's original
"your own family member is on the transplant list" sub-plot was dropped in conversion (see
case.json's `legacy_conversion_note`) as unnecessary personalization that added no math.

**Assumption-sensitivity disclosure (required reading before you defend the 5.6% margin):** The
case's one genuine modeled assumption is MA1, the steady-state leak rate (3.7 gal/mi, the rounded
mean of Appendix E's plateaued readings). `sensitivity_model.py`'s Tier 2 probe 5 flexes this rate
±50% (to 1.85 and 5.55 gal/mi). **The winner does not flip in either direction** — the leak rate
scales both options' post-failure burn by the same multiplier, and since Option A's distance
(1,200 mi) is always smaller than Option B's (1,214 mi), a uniform rate change can never flip which
option burns less fuel; it can only change how much fuel is left, and by how much the two differ.
At -50% (1.85 gal/mi) both options land with a large, comfortable margin (3,153.2 gal vs. 3,127.3
gal, a 0.82% gap) — the case is very safe under a lighter leak. **At +50% (5.55 gal/mi), BOTH
options run the tank dry before landing** (-1,286.8 gal and -1,364.5 gal — negative, i.e. neither
route is physically completable on the modeled fuel). Option A is still the "less-bad" of the two
negative numbers, but do not read that as a 20%-cap-relevant margin — a negative baseline makes the
percentage formula meaningless (the same class of artifact as this project's own Seton Hall
zero-baseline finding, `skills/case-readiness/SKILL.md`'s P5 section). The honest takeaway for a
facilitator: this case's fuel comparison is genuinely stable in *which option wins*, but is **not**
stable in whether either option is survivable — if the real leak rate were meaningfully worse than
the modeled 3.7 gal/mi, the correct real-world answer would not be "pick the better option," it
would be "neither option lands with fuel to spare, look for a closer alternative or prepare for a
water landing" — a conversation worth having with a sharp room, not a result to paper over
(DOCTRINE_LEDGER.md MCS-26/MCS-41: disclosure is the requirement, not elimination).

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00-3:00 | Cold-call launch (Overview read/acted aloud), 30-second commitments, stand/sit vote — no explanation (Anchor 1) |
| 3:00-10:00 | Position defense: "Convince us why it's better, not just closer" (Anchors 2-3, define the real question(s) and a process) |
| 10:00-15:00 | Pressure-test the models: hand out Appendices A/C/E/F, let D1-D3 develop |
| **15:00** | **DROP THE TWIST** — delivered slowly, with pauses |
| 15:00-20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00-30:00 | Threaded deep conflict: (1) the distance-gap-vs-fuel-gap trap (D2-D4), (2) fuel safety vs. weather/aircraft-damage risk — two axes, not one, (3) how much weight the Twist's unquantified transplant-window urgency should actually carry against a real fuel-safety margin |
| 30:00-45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands

See `case.json.cohort_bands[]` (Full 12-20 / Compressed 6-11 / 1:1-pair 1-2) — three bands
declared per the cohort-bands floor in SPEC.md's "Cohort bands" subsection of Section 7.
