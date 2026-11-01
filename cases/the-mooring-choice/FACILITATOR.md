# Guide Notes: Mooring Choice

MS | Guide Notes | Adventure | 2026-27
**Tier:** T2 · **Primary metric:** net buoyant lift (buoyancy minus hull, sinker, and ballast weight) per dollar of material · **Margin:** 19.3% (sensitive — see the sensitivity note before Lessons Learned)

**Do not distribute to students.** This document, and `case.json`'s `balance` object, are the only
places the balance argument, the margin, and the wrong-path analysis below may live. `case.md`
carries only a one-line pointer comment to this file.

---

## Intro

Heroes, Theo has one order sheet and two hull drawings. One is a tall steel cylinder with a cone on
top — the shape of every buoy he's ever hauled out for maintenance. The other is a plain steel ball.
There's no answer key here — the numbers genuinely come out close, and which one wins depends on an
assumption nobody in the room will think to question at first.

## Launch

Show the two cross-sections side by side (the Spar's cylinder-and-cone silhouette vs. the sphere).
Ask: *"If you had to weld one of these by hand, which one looks easier? Which one looks like it
uses less steel?"* Let them argue it cold — most rooms will split, and most rooms will be wrong
about at least one of those two questions.

> **Hero name — Spar or Sphere? Open for us.**

---

## Anchor 1 — Take a stand and vote

Option A (Spar) or Option B (Sphere). No reasoning yet. Hands up. Write the split on the board.

*"Is anyone courageous enough to stand with ______?"*

## Anchor 2 — What is the problem we're solving?

Do **not** let them start calculating yet.

- What's the actual question? Say it in one sentence.
- Is it "which shape uses less steel"? Is it "which shape floats better"? Is it "which shape gives
  the most usable lift per dollar spent, once everything the shape itself requires is paid for"?
  **Those are three different questions**, and only the third is the one Theo's fabrication order
  actually forces him to answer.
- Someone will say "obviously the sphere, it's more efficient." Push: *"Efficient at what — steel
  per volume, or dollars per pound of lift once you've paid for everything the sphere needs to stay
  upright?"*

> Let the confusion grow. Say it out loud: *"Huh. This is a harder question than it looked."* Do
> not rescue them.

**Socratic Q1.** D5 computes net buoyant lift for both options — the Spar Design's raw lift
(3,703.0 kg) is actually *higher* than the Spherical Design's (3,346.1 kg). Does more lift mean a
better system?

**The trap to let them walk into — confirmed by a live cold-solve run against this exact
packet (2026-09-18):** most students will correctly compute both options' net buoyant lift, see
that the Spar Design's number is bigger (3,703.0 kg vs. 3,346.1 kg), and stop there — assuming
"more lift is safer, more lift is obviously better" and recommending the Spar. Every step of their
arithmetic up to that point is correct. What they miss is D5's own instruction to *divide by total
material cost* before recommending anything: the Spar's extra 356.9 kg of lift costs $1,505.01
more ($5,557.59 vs. $4,052.58), and once both are expressed as a ratio (kg of lift per dollar), the
Spherical Design is ahead, 0.8257 vs. 0.6663. A student who computes correctly but never finishes
the division will confidently recommend the Spar and be unable to say why the case's own ratio
disagrees with them.

A second, related trap (a real but secondary risk): a solver who does divide by cost may still
compute D1/D2's steel-surface-area comparison, see the sphere's ~29% steel-efficiency advantage,
and assume that number *is* the final answer — without ever pricing the stability ballast Appendix
C requires, which eats into (but does not erase) that advantage.

## Anchor 3 — What is the process?

- What's the process we'll go through to answer it?
- If the sphere's steel bill is smaller, are we done? Or is there a cost the sphere carries that the
  Spar simply doesn't?
- **Socratic Q2.** Appendix C says the sphere needs stability ballast because it has no natural
  low center of gravity the way the Spar's shape does. Where does that ballast show up in your
  numbers — and where would a rushed solver forget to put it?
- Is our question still the right question?

## Anchor 4 — What don't we know?

- What's missing that we'd need to answer this properly?
- Appendix E gives you the Modeling Assumptions. Do you believe them? MA4 (steel plate thickness)
  and MA6 (the sphere's ballast fraction) are both flagged HIGH sensitivity — **have them actually
  try flexing MA6 up and down and see how much the comparison moves.**
- **Socratic Q3.** The Spar's flat cylindrical sides are easier for the shop to fabricate than a
  curved spherical shell. Does that show up anywhere in your D4/D5 numbers? Should it?

---

## Data Deep Dive

Now the numbers. Work these on the board with them.

| | Spar (Option A) | Sphere (Option B) |
|---|---|---|
| Volume | 6.4088 m³ | 6.3706 m³ |
| Steel surface area | 23.3734 m² | 16.6190 m² |
| Steel weight | 1,834.8 kg | 1,304.6 kg |
| Steel cost | $5,381.06 | $3,826.05 |
| Stability ballast | — | 848.0 kg, $50.00 |
| Shared sinker cost (both) | $176.52 | $176.52 |
| **Total material cost** | **$5,557.59** | **$4,052.58** |
| Seawater displaced | 6,569.1 kg | 6,529.9 kg |
| Sinker submerged weight (both) | 1,031.2 kg | 1,031.2 kg |
| **Net buoyant lift** | **3,703.0 kg** | **3,346.1 kg** |
| **Ratio (kg lift per $)** | **0.6663** | **0.8257** |

**margin = |0.8257 − 0.6663| / 0.8257 = 19.3%.** The Spherical Design (Option B) wins, but by
19.3% — inside the ~20% cap, but only barely. **This is close enough that the ballast assumption
alone (MA6) can flip it — push the room to find that themselves before you show them.**

**Push the room directly:** *"If the ballast fraction were smaller — say the sphere only needed
half as much stability ballast — would the sphere still win? What if it needed more?"*
(**Socratic Q4**, below.)

---

## Twist — drop this at ~15 minutes into the discussion

Deliver it slowly. Let each piece land.

> *"One more call, before Theo signs the order."*
>
> (pause)
>
> *"The fabrication shop just got back to him. Their rolling equipment can bend flat steel plate
> into a cylinder — that's routine. But a sphere isn't made of flat plate bent one way. It's built
> from compound-curved panels, curved in two directions at once, and this shop can't roll those
> in-house."*
>
> (pause)
>
> *"They'd have to subcontract the spherical hull's curved panels to an outside fabricator — at a
> real cost markup on top of the raw steel."*

**Facilitator only — read before you drop this, do not read aloud.** Run
`sensitivity_model.py`'s `evaluate_twist()`: a 40% subcontracting surcharge on the Spherical
Design's own steel cost (only — the Spar's flat sides need no specialty rolling) drops its ratio
from 0.8257 to 0.5993 kg/$, which is now *below* the Spar's unchanged 0.6663 kg/$ — **the twist
flips the winner outright**, margin 10.05% now favoring the Spar. This is a genuine flip, not a
near-tie the way Pixel Snap's twist was — confirm a room that gets there against the model, not
just the narrative.

Now: **"Sixty seconds. Are you changing your recommendation — or not?"**

## Immediate recommit

- Who is **not** changing? Why?
- Who is reconsidering, even if they're not flipping?
- **What just broke in your original model?**
- **Were you wrong — or were you just missing information?** (Sit on this one.)
- Who built a recommendation that depended entirely on the sphere's steel savings, without ever
  pricing how that steel actually gets shaped?

---

## Deep conflict — threads (20–30 min)

**Thread 1 — Steel-efficient vs. actually cheaper.** The sphere uses 29% less steel surface area.
The sphere is still only 19.3% cheaper per unit of lift, not 29% — and after the twist, it's not
cheaper at all. *"Why doesn't a smaller surface area translate directly into a proportionally
smaller total system cost?"*

**Thread 2 — Fragility to a single fraction.** The whole 19.3% margin rides on MA6 (the ballast
fraction). Push: *"If the naval architects had specified a sturdier, heavier ballast package for
rougher water, would the sphere still be worth it?"*

**Thread 3 — What the case doesn't price.** The Spar's fabrication-ease and instrument-mounting
advantage (Background) is real but never gets a dollar figure — until the twist forces one. *"Is
it fair to compare two options when one's real advantage doesn't show up in the ratio until new
information arrives? What should Theo have asked the shop *before* running the numbers?"*

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. *"Thirty seconds — Spar or Sphere?"* Two or three learners, fast. Stand/sit vote, no explanation yet. |
| **3:00–10:00** | Position defense (pre-twist). *"Convince us it's better, not just simpler."* · *"What's your D5 ratio, exactly?"* |
| **10:00–15:00** | Pressure-test the models. *"What's the single assumption your answer depends on most?"* |
| **15:00** | **DROP THE TWIST.** Slowly, with pauses. Finish with: *"Sixty seconds. Are you changing your recommendation — or not?"* |
| **15:00–20:00** | Immediate recommit. Who reverses? *"What just broke?"* |
| **20:00–30:00** | The three threads: steel-efficient vs. actually cheaper · fragility to the ballast fraction · what the case doesn't price. |
| **30:00–45:00** | Close, re-vote, reflection, lessons learned. |

---

## Close

- **Vote again.** Compare to the Anchor 1 board. Who moved?
- We asked ______ as our key question. Was it the right one?
- What math was new to you here, and how did you attack it?
- If you got a case like this again, what would you check first?

**Socratic Q4.** If the ballast fraction were smaller — say the sphere only needed half as much
stability ballast — would the sphere still win? What if it needed more?

**Socratic Q5.** The sinker is identical for both options. Why does the case bother having you
compute it separately (D3) if it doesn't change the comparison between A and B?

## Lessons Learned

The arithmetic has a clean structure — a shape can be dramatically more material-efficient
(29% less steel surface area) without being anywhere near that much cheaper as a complete system,
once every real cost the shape itself creates gets counted. The Spherical Design's win (19.3%) is
real and it is not a rounding artifact — but it rests almost entirely on MA4 (steel plate thickness)
and MA6 (the stability-ballast fraction), and it is fragile enough that a single new piece of
information (the fabrication surcharge) flips it outright. That is a **disclosed, not eliminated**
sensitivity — see `case.json.sensitivity_note` and `sensitivity_model.py`'s probe-5 sweep for the
exact numbers.

The steel-efficient-vs-actually-cheaper reframing (Anchor 2/3, Data Deep Dive) is the part of this
case that exists to be reused: any time a shape or design's raw material efficiency is compared
without first pricing every downstream cost that efficiency creates (ballast, fabrication method,
labor), the naive comparison and the fully-priced comparison can disagree — and only the second one
is the real decision-relevant number.

A facilitator running this room should say plainly what the case says: the sphere wins on the
numbers as modeled, that win is real but narrow (19.3%, not 29%), and it is also genuinely fragile
to one disclosed assumption (the ballast fraction) and to the twist (the fabrication surcharge) —
all three things are true at once, and naming all three is stronger than picking one.

---

## Standards Touched On

**Reinforcement case — no new_coverage (see `case.json.reinforcement_note` and
`LEARNING_GOALS.md`):** How to find the surface area of a cylinder · How to find the volume of a
cylinder · How to find the volume of a cone · How to find the volume of a sphere · How to find the
surface area of a pyramid · How to find the volume of a pyramid

---

## Cohort bands

- **Full (16–24).** The plan above runs as written; both deep-conflict threads get their own pass
  in the 20:00–30:00 block.
- **Compressed (6–11).** Combine Anchors 2 and 3 into a single "has your number changed your mind"
  pass. Run only the ballast-fraction trap thread (Thread 2) — it needs the least setup and carries
  the case's real teaching point. The twist still drops at 15:00. Total runtime ~30 minutes.
- **1:1 or pair (1–2).** No vote to take — the learner states an initial position instead of a
  show-of-hands split at Anchor 1. The facilitator argues the opposite side directly instead of
  cold-calling. The twist still lands; the Close's "who reverses" becomes "would you reverse, and
  why," addressed straight to the learner.

## Facilitator note — sensitivity

No SPEC Section 6 subject-matter sensitivity applies. This is a technical engineering-design
decision with no death, illness, or family-hardship stakes.
