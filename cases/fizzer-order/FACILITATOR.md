# FACILITATOR.md — Fizzer Order

**Sensitivity flag (SPEC §6):** none. This case is a business/packaging decision with no health,
death, or financial-hardship stakes. No facilitator content note required.

## Intro

Frame the format: a real professional dilemma, not a worksheet with a story stapled on. Name the
opener — "Odalys Reyes has a mold-shop quote deadline today, two hand-built prototypes on her
bench, and a phone still on hold. Whichever shape she signs off on today is the shape Thistle &
Fern ships for the whole holiday run." Odalys came up through studio pottery before packaging
engineering — she trusts what a box feels like in her hand as much as what its spec sheet says,
and the shelf of failed prototypes behind her desk is there on purpose, not clutter. This is a
packaging-engineering call with a real production consequence, not an abstract geometry worksheet.

## Launch

Read the Overview aloud, then Background's first two paragraphs — the Peak Box and Twist Cone
description, and the loose-fill packing note — with no Appendix numbers shown yet. Ask: "Just from
what you've heard, does 'pick the cheaper box' sound like it settles this, or not?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Peak Box or Twist Cone?" Show of hands, no discussion yet. Record the count — Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'wins'?"**

Push on what "wins" means here. Cheaper as a single box off the mold-shop invoice? Cheaper per
Mini Fizzer actually delivered to the retail buyer? Cheapest to ship, carton by carton? Let the
room sit in the ambiguity — "Is anyone courageous enough to define 'wins' before we start adding
numbers?" Deliberately let it feel underdetermined: "Wow, this is a harder question than it
sounded."

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has picked a working definition of "wins," ask them to name the actual steps: the
surface area of each net (D1), the interior volume each shape holds (D2), how many Mini Fizzers
each shape can actually, physically hold once loose-fill air gaps are accounted for (D3), the cost
per Mini Fizzer delivered (D4), and how densely each shape ships in a standard carton (D5).
Re-ask: "Given how we just defined 'wins' — is D4 alone still the right finish line, or does D5
belong in the answer too?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix E's two Modeling Assumptions as a group, out loud, before anyone computes
anything. Ask which one the room thinks matters most. (Facilitator note: MA1 — whether the real
64% loose-packing figure really applies just as well to a tapering cone as to a boxier pyramid —
is the one that actually matters most for the numbers; let the room guess first.)

## Data Deep Dive

Now, and only now, the numbers. Walk D1 through D4 together as a room: net and surface area, then
interior volume, then usable capacity, then cost per Mini Fizzer delivered.

**The trap:** most Heroes will compare the two boxes' raw material cost from D1 — $0.02350 for the
Peak Box versus $0.02378 for the Twist Cone — and stop there, confidently picking the Peak Box
because it is the cheaper *container*. That comparison is real and correctly computed; it just
answers the wrong question. The case's own primary metric is dollars per Mini Fizzer *delivered*,
not dollars per box, and the Twist Cone's larger interior volume converts its slightly higher box
cost into a lower cost per unit once the real 64% packing figure is applied — one extra whole Mini
Fizzer per box. Cold-call on this specifically: "You just told me the Peak Box is cheaper. Cheaper
per *what*?" Once D4 is run in full, Option B (Twist Cone) wins the primary metric by **8.96%** —
comfortably inside SPEC §2's margin cap, which is exactly why Odalys is still standing at her bench
with a prototype in each hand.

A second-order version of the same trap sits in D5: a Hero who then flips to the Twist Cone on
D4's number alone, without ever computing the shipping-carton footprint, misses that the Peak Box
ships nearly twice as densely — a real freight cost Odalys's company pays even though it never
appears on the mold shop's per-box invoice. A strong pitch has to hold both numbers at once.

## Twist: N/A

Fizzer Order does not carry a scripted, mid-discussion narrative reveal the way some cases do (see
`sensitivity_model.py`'s header comment: "no twist authored for this case"). Two reasons, stated
so a facilitator can defend the choice rather than wonder if something was skipped:

1. The case already carries two real, load-bearing complications inside the data itself — D5's
   shipping-density trap (see Data Deep Dive above) and Modeling Assumption MA1's packing-fraction
   caveat (see Sensitivity note below) — rather than needing a fabricated late-breaking fact to do
   that work. Manufacturing a narrative twist on top of two data-native ones would be padding, not
   pedagogy.
2. MA1 is itself available as a live, in-the-room move if a facilitator wants one: relaxing it —
   letting the Twist Cone's real packing fraction run below the Peak Box's sourced 64%, instead of
   holding both shapes at the same figure — is a legitimate thing to spring on the room mid
   -discussion, and it does change the winner (see Sensitivity note). A facilitator who wants a
   twist-shaped beat has one available without inventing new case facts.

## Close

Re-vote once more after full discussion. Ask: "Did we ask the right question at Anchor 2, or did
'wins' turn out to mean something more than one number?" And: "What math was new to you today, and
how did you attack it?"

## Lessons Learned

The naive comparison — pick the cheaper *box* — is correctly computed and still wrong, because it
optimizes the wrong ratio. The transferable lesson: **when a fixed quantity of "stuff" has to fit
inside a container, the number that matters is cost per unit of stuff delivered, not cost per
container** — and that number can favor the container that costs slightly more to build. A second,
smaller lesson rides along in D5: the metric that wins the primary comparison is not automatically
the metric that governs the company's total cost once freight is added, and the case deliberately
does not resolve that tension for the Hero.

## Standards Touched On

See `case.json.standards[]` (10 ids) and `LEARNING_GOALS.md` for the full deliverable ↔ skill
matrix. In brief: pyramid, cone, and sphere vocabulary; surface area of a pyramid; volume of a
pyramid, a cone, and a sphere; and percent of a number (D3's usable-capacity fraction and D4's
cost comparison).

## Cohort Bands

See `case.json.cohort_bands[]`.

- **Full (12–20):** Anchors 2–3 run as written; the room splits into a "cheaper box" faction and a
  "cheaper per fizzer" faction before Data Deep Dive forces everyone to actually run D3 and D4.
- **Compressed (6–11):** Anchors 2–3 combine into one pass; D1 and D2's diagrams and tables are
  worked as one shared example (one option) instead of every Hero building both independently.
- **1:1 / pair (1–2):** No vote to take — Anchor 1 becomes a stated initial position instead of a
  cold-call show of hands; the guide plays devil's advocate directly, arguing whichever side the
  Hero didn't pick.

## Five Socratic Questions

Use these across Anchors 2–4 and the Data Deep Dive — each is answerable only with this case's own numbers, not general opinion.

1. Your D4 table says the Twist Cone wins by about 9% on cost per Mini Fizzer delivered, but the Peak Box is the cheaper box — which number should Odalys actually be optimizing, and why isn't "cheaper box" automatically "cheaper decision"?
2. D5 says nearly twice as many Peak Boxes fit in one shipping carton layer as Twist Cones — if freight is priced by the carton, how big would that per-carton cost have to get before shipping density outweighs the Twist Cone's win on cost per fizzer?
3. Modeling Assumption MA1 applies the same 64% loose-packing figure to both shapes even though the Twist Cone tapers to a point and the Peak Box doesn't — if the cone's real packing efficiency runs even a little below the Peak Box's, what happens to the D4 winner?
4. A student who compares only the two boxes' raw material cost will confidently pick the Peak Box — what did that comparison leave out, and why does leaving it out produce a wrong-but-confident answer?
5. Appendix A says a full sphere-shaped box was ruled out early because a curved-die mold quote came back more than four times the cost of either finalist — if that number were only twice as expensive instead, would it still make sense to rule the sphere out without computing its own D1 through D5 numbers?

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, show-of-hands vote (Anchor 1) — no explanation |
| 3:00–8:00 | Anchor 2: pin down what "wins" means — box price, cost per fizzer, or shipping density |
| 8:00–12:00 | Anchor 3: name the process (D1–D5) as a group before anyone computes anything |
| 12:00–17:00 | Anchor 4: surface Modeling Assumptions MA1/MA2; guess which one matters most |
| 17:00–30:00 | Data Deep Dive: work D1–D4 as a room; cold-call the raw-material-cost trap directly |
| 30:00–36:00 | Twist-equivalent beat (see "Twist: N/A" above): relax MA1's packing fraction live and recompute D4 — no scripted narrative reveal for this case, this is the live-numbers move instead |
| 36:00–40:00 | D5 second-order trap: shipping-carton footprint, and whether it should change the pitch |
| 40:00–45:00 | Close, re-vote, reflection, Lessons Learned |

## Sensitivity note

Modeling Assumption MA1 (Appendix E) is the one number in this case that can flip the D4 winner:
it applies the real 64% loose-packing figure identically to both the Peak Box and the Twist Cone,
even though the cone's taper plausibly packs somewhat less efficiently in the real world than a
boxier shape does. If the Twist Cone's true packing fraction runs meaningfully below 64% while the
Peak Box's stays near 64%, Option A's D4 result overtakes Option B's. `sensitivity_model.py`'s own
asymmetric check (Peak Box held at 64%, only the Twist Cone's packing fraction lowered) shows the
winner actually flips from Option B to Option A once the cone's real packing fraction drops from
64% into the high 50s — comfortably inside the range a facilitator running Tier 2 probe 5 should
expect to find, and well within the wide perturbation band the probe applies to every `FLEX`
dial.
