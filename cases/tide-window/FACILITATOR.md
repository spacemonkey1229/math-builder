# Guide Notes: Tide Window

**Case:** Tide Window · **Tier:** T4 · **Band:** HS · **Studio:** Launchpad
**Standards:** Pre-Calculus / Trigonometric Functions — the full group, all `new_coverage` (see
`case.json.standards[]` for the exact ids)

Draft written at `case-write` time. Numbers below are placeholders until `case-research` fills
`case.md`; this file is re-checked for drift at every readiness run.

## Intro

Frame the format before anything else: this is not a worksheet, it's a decision Amara has to
defend out loud. Name the opener — "You are a harbor pilot. Six months licensed. Nobody senior is
next to you tonight." Let that sit for a second before moving to the Launch.

## Launch

Show the two tide curves side by side (the same pair described in Background) — one at the Dawn
Transit hour, one at the Slack Tide hour — with no clearance numbers labeled yet, just the shape
of the curve. Ask: "Which one looks safer to you, just from the shape?" Do not confirm or correct
answers here. The point is to get a gut read on the table before anyone touches a formula.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Amara on the Dawn Transit?" Show of hands, both
options, no discussion. Record the count — Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'safe'?"**

Let confusion grow here — this is deliberate, not a delay to rescue. Heroes will want to jump to
"is there enough clearance," but the real question is sharper: *enough clearance under which
reading of the tide — the predicted curve, or the worst case the barometer could actually do
tonight?* Push on it: "Amara's own safety manual doesn't ask 'will it probably be fine.' What does
it actually ask?" If the room lands on "predicted vs. worst-case" on its own, that's the case
working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has a working definition of "safe," ask them to name the actual steps before
touching Appendix A: convert the key clock times into the model's angle, build the sine/cosine
model from the real harmonic data, evaluate it at the Dawn Transit hour, compare against the
minimum-clearance policy. Re-ask: "Is our question still the right one, now that we can see the
steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the two real gaps honestly: the contract penalty figure (Appendix C) and the exact
storm-surge/barometric adjustment for *this specific night* (Appendix D) are both uncertain by
nature, not because research was lazy. Ask which one actually changes the decision if it moves,
and which one is just flavor.

## Data Deep Dive

Now, and only now, the numbers. Walk the angle table (D1), the fitted model (D2), and the
clearance comparison (D3) together as a room, cold-calling for the reference-angle step and the
sine/cosine/tangent evaluation specifically — this is where a Hero who skipped the unit-circle
work will visibly struggle, which is useful information for the facilitator, not a moment to
rescue.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"It's the middle of the discussion. A new marine forecast comes in. The barometric pressure is
dropping faster than tonight's Appendix D range assumed — the storm that was supposed to stay
offshore is closer than predicted."

"The dispatcher radios: the delivery penalty clock hasn't stopped. But neither has the storm."

"You have sixty seconds. Does your Dawn Transit clearance number still hold — and would you still
authorize it?"

**Facilitator-only: what the numbers actually do (case.json.derived).** Under MA3's stated
28 mb pressure drop, the Dawn Transit's margin over the Pilots' Association's policy shrinks from
1.544 ft to 0.634 ft — a real ~59% erosion (19.33% of the 3.28 ft policy floor, which is this
case's graded `margin_pct`), but the clearance stays positive. **The twist does not flip the
verdict; it erodes confidence in it.** This was computed honestly from a real range, not picked to
force a reversal (see `RESEARCH_LOG.md`). Do not correct a Hero who treats this as "still fine,
barely" — that is a defensible read of the real numbers. The room's actual argument should be
whether a margin that's lost more than half its size, on a threshold your own safety policy sets
for exactly this reason, still deserves the same confidence it had five minutes ago. If a Hero asks
"how much worse would it have to get to actually fail," the honest answer is "about 47.5 mb of
local pressure drop, which is itself within real tropical-storm range" — a good follow-on question
to have ready, not a script to hand over unprompted.

This does not hand anyone a clean answer. It should push some Dawn Transit votes toward doubt
without making Slack Tide free of cost — the penalty is still real, and by the time the room
re-votes, the tide window itself may be narrowing. **The twist targets D4 directly**: a Hero who
did the sensitivity check honestly has language ready ("my worst-case already covered this, and
here's the margin that's left" or "my worst-case didn't go this far, and here's what changes"); a
Hero who treated D4 as a formality does not.

## Immediate recommit

Re-vote immediately. Ask by name: "What just broke in your model? Were you wrong — or just missing
information a minute ago?" That distinction is the transferable skill, not the vote itself.

## Deep conflict — three threads (20-30 min)

1. **Prediction vs. policy.** A model can be right on average and still authorize an unsafe
   individual transit. Where's the line between "trust the math" and "trust the safety margin the
   math can't see"?
2. **Whose risk, whose penalty.** The shipping line bears the delivery penalty; Amara bears the
   grounding risk and the license consequence. Is it fair that one person's name is the one on the
   log?
3. **What "enough" data means.** Amara never gets a second pilot to check her work. Is there a
   point where more data collection is itself the wrong call, given the clock is real?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show the two curve shapes, cold-call for a gut read, no formulas yet |
| 3:00–10:00 | Position defense — *"Convince us why it's safe, not just fast"* |
| 10:00–15:00 | Pressure-test the models — *"Whose clearance number is most fragile?"* |
| **15:00** | **DROP THE TWIST** — the revised storm forecast, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (prediction vs. policy; whose risk; what "enough data" means) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

A Hero computes the *predicted* clearance, finds it positive, and stops — treating a model's
central prediction as a guarantee. The case's real tension is that "positive under the predicted
curve" and "safe under the association's minimum-clearance policy across the real range of
conditions" are two different questions, and the second one is the one Amara is actually
accountable for. Watch for a pitch that reports one clearance number and calls the case closed.

## Socratic questions

1. Your model says the Dawn Transit clears the harbor floor by a real margin — what would the storm-surge adjustment have to be for that margin to reach zero?
2. The Pilots' Association's minimum-clearance policy exists for a reason — whose job is it to decide when a "thin but positive" margin is not thin enough, the model or the pilot?
3. If you were the shipping line's dispatcher instead of the pilot, would you weigh the penalty differently — and why is that not actually Amara's problem to solve?
4. Your D1 table required sine, cosine, *and* tangent of the reference angle — which of the three did you actually use in your final clearance number, and why did the case ask for all three anyway?
5. Suppose the real data shows the barometric adjustment on the actual night was smaller than the worst case you modeled in D4 — was Amara wrong to be cautious, or just unlucky in a good way?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that didn't
move at all after the twist is worth asking about directly: did the twist not land, or did the
room already have the right margin built in?

## Lessons Learned

*(To be filled after research and the first real run — placeholder structure only.)*

- Whether the reference-angle step was the place most Heroes actually got stuck.
- Whether the combined sine/cosine/tangent unit-circle skill (one spine how-to, three ratios) read
  as one task or three to a first-time Hero — worth knowing for how this case's D1 is graded.
- Whether the twist's storm-forecast framing landed as a genuine surprise or felt telegraphed by
  Appendix D's own existence.

## Standards Touched On

Radian · Unit Circle · Sine Function · Cosine Function · Tangent Function · Amplitude · Period (Of
A Function) · Reference Angle · How to convert between degrees and radians · How to find the
sine, cosine, and tangent of an angle using the unit circle · How to find the amplitude and
period of a sine or cosine function

## Facilitator note — sensitivity

None required (SPEC §6) — the stakes here are commercial and professional (schedule penalty, a
pilot's license), not personal loss or hardship.
