# Guide Notes: Carpenter

**Case:** Carpenter · **Tier:** T2 · **Band:** MS-core · **Studio:** Adventure
**Standards:** see `case.json.standards[]` for the exact ids (10 skills — area of a rectangle,
unit conversion, percent of a number, currency, ratio, comparison, bar graph, coordinate
graphing, percent conversion)

Legacy conversion, 2026-08-20, built from the original case study docx
(`source/Y3/Session 4/Carpenter/Case Study_ Carpenter.docx`) onto the current 11-anchor ladder.
The protagonist, clients, budget cap, and cross-border delivery arrangement are preserved
verbatim from the source; the material/maintenance cost table was fully re-sourced to real,
cited 2026 figures (the source docx table carried no citations at all). The original
`Guide Notes.docx` did not actually describe this case — it was a mismatched template about an
unrelated family scenario with unrelated stock images — so this Guide Notes document is newly
authored for Carpenter specifically. See `case.json.legacy_conversion_note` for the full account.

## Intro

Frame the format: a real professional dilemma, not a worksheet with a story stapled on.
Name the opener — "One carpenter, one client who said 'we trust you' — and a flooring choice
that has to survive ten years of Airbnb guests, not just look good on install day."

## Launch

Read the Overview aloud, then Background's two sentences about the budget (CD$17,900 soft cap)
and the "comfort and luxury" goal, with no Appendix numbers shown yet. Ask: "Just from what
you've heard — does 'pick the cheaper one' sound like it settles this, or not?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Carpet or hardwood?" Show of hands, no discussion yet. Record the count — Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'cheaper'?"**

Push on what "cheaper" means here. Cheaper to install this month? Cheaper counting the years
this flooring actually has to survive? Cheaper relative to a budget cap that's explicitly
*soft*, not a hard wall? Let the room sit in the ambiguity — "Is anyone courageous enough to
define 'cheaper' before we start adding numbers?" Deliberately let it feel underdetermined:
"Wow, this is a harder question than it sounded."

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has picked a working definition of "cheaper" or "best," ask them to name the
actual steps: total square footage by zone, initial cost per option, how each stacks against the
budget cap, and cost over time including any replacement or refinishing. Re-ask: "Given how we
just defined 'cheaper' — is that still the right process?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix F's four Modeling Assumptions as a group, out loud, before anyone computes
anything. Ask which ones the room thinks matter most. (Facilitator note: MA4 — whether
short-term-rental foot traffic changes the wear-life numbers — is the one that actually matters
most, but let the room guess first; that's what the Twist is for.)

## Data Deep Dive

Now, and only now, the numbers. Walk D1 and D2 together as a room: area takeoff, then cost per
option.

**The trap:** most Heroes will price Option A as the obvious winner and stop there, because its
initial cost is dramatically lower and it's the only one that fits comfortably under the
CD$17,900 cap. They will apply Appendix B's wear-life figures (carpet 8–10 years) exactly as
written — a generic *residential* household figure — without noticing that Background already
told them this flat turns over tenants *at least weekly* with *heavy foot traffic*, which is
nothing like a quiet family home. Cold-call on this specifically: "Whose 8-to-10-year number are
you using — a family's living room, or a place that changes tenants every week?"

## Twist — drop this at roughly the 15-minute mark

Deliver slowly, with pauses:

"Newt makes one more call before he sends the pitch — to his flooring wholesaler, who's fitted
plenty of short-term rentals. The wholesaler tells him something the spec sheet doesn't say:
under nightly-turnover, heavy-traffic use — exactly what the Berisels are running — carpet's
real-world replacement clock runs at roughly *half* the normal residential figure. Not 8 to 10
years. More like 4 to 5. Hardwood, being a hard, dense material, doesn't see nearly the same
effect — it might need a touch more frequent recoating, but it doesn't need replacing on a
different clock."

**Facilitator-only.** Recompute Option A live with the room: instead of one full carpet
replacement at year 10, two full replacements land inside the 15-year window — year 5 and year
10. Recompute the 15-year total cost of ownership with the room using `sensitivity_model.py`'s
`evaluate_twist()`: Option A's 15-year total rises from CD$33,723.93 to CD$39,986.87, while
Option B's CD$34,674.14 doesn't move. The option that looked like the clear winner on both
initial cost *and* long-run cost a few minutes ago is now the *more* expensive one over 15 years,
by 15.3%.

Ask: "You now have 60 seconds. Does this change your recommendation — or not?" Then, the
follow-up that matters more than the vote: **"What just broke in your original model? Were you
wrong about the price of flooring — or were you just missing what kind of building this actually
is?"**

Do not hand over a "correct" answer. A carpenter with a soft budget cap to respect and a client
goal to honor can reasonably land on either option even after the Twist — that tension, not a
trick, is the point.

**Twist soundness check (SPEC §6):** this twist was checked against every stated Background/
Appendix fact and Modeling Assumption, read both sequentially (in the order a Hero encounters
them) and simultaneously (all at once, as a final numeric model) — it introduces no new figure
that contradicts an earlier one, only a second, real lens (heavy short-term-rental traffic,
already named in Background's first paragraph) on wear-life data already in front of the room.
It holds under both readings, and `sensitivity_model.py`'s `evaluate()`/`evaluate_twist()` confirm
the winner genuinely flips (base: A cheaper by 2.8%; twist: B cheaper by 15.3%).

## Immediate recommit

Re-vote immediately. "Did the traffic-adjusted recompute change your hand — or did it just
change *why* you're holding it up?"

## Close

Re-vote once more after full discussion. Ask: "Did we ask the right question at Anchor 2, or did
'cheaper' turn out to mean something different by the end?" And: "What math was new to you
today, and how did you attack it?"

## Lessons Learned

The original case's own launch question — "would you choose differently for a house you're
going to rent out?" — turns out to be the entire case, once the numbers are run honestly. The
transferable lesson: **a wear-life figure is only as good as the traffic pattern it was measured
under**, and a short-term rental is not a family home wearing its floors slowly. Read literally,
Appendix B's numbers make carpet the clear winner on every axis. Read in the context Background
already gave — heavy, weekly-turnover traffic — the same numbers flip the recommendation.

## Five Socratic Questions

Use these across Anchors 2–4 and the Data Deep Dive — each is answerable only with this case's
own numbers, not general opinion.

1. Option A costs about CD$8,164 less to install than Option B — but Option B is the only one that matches what the Berisels actually said they wanted. How many dollars of "comfort and luxury" is that gap worth?
2. Option B alone blows past the CD$17,900 soft cap by CD$4,905. Is a "soft" cap a real constraint or not — and how would you argue that to a client who set the number themselves?
3. Appendix B's carpet wear-life (8–10 years) is a general residential figure. Background says this flat turns over tenants weekly with heavy foot traffic. What number would you use instead, and why?
4. Before the Twist, Option A wins 15-year total cost by only 2.8%. After it, Option B wins by 15.3%. What single number, if it changed, could flip the case back the other way?
5. Newt is being paid to give a professional recommendation, not just show two totals. If the Berisels' real priority is "never having a flooring emergency mid-booking," does that change which option you'd pitch, even if it isn't the cheaper one?

## Standards Touched On

See `case.json.standards[]` (10 ids) and `LEARNING_GOALS.md` for the full deliverable ↔ skill
matrix. In brief: area of a rectangle, unit conversion (meters↔feet, USD↔CAD), percent of a
number, currency, ratio, comparison, bar graphs, coordinate graphing, and percent conversion.

## Cohort Bands

See `case.json.cohort_bands[]`.

- **Full (12–20):** Anchors 2–3 run as written; the room splits into an "up-front budget" faction
  and a "comfort-and-luxury/long-run" faction before the Twist forces everyone to re-price
  carpet's replacement cadence.
- **Compressed (6–11):** Anchors 2–3 combine into one pass; D4's cumulative cost-over-time chart
  is worked as one shared example (one option) instead of every Hero building both independently.
- **1:1 / pair (1–2):** No vote to take — Anchor 1 becomes a stated initial position instead of a
  cold-call show of hands; the guide plays devil's advocate directly, arguing whichever side the
  Hero didn't pick.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote (Anchor 1) — no explanation |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just cheaper" |
| 10:00–15:00 | Pressure-test the models: "Whose wear-life number are you using — and for what kind of building?" |
| **15:00** | **DROP THE TWIST** — the wholesaler's heavy-traffic wear-life call, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00–30:00 | Threaded deep conflict — two named threads: (1) up-front cash cost vs. long-run total cost of ownership as competing definitions of "cheaper"; (2) a soft budget cap vs. an explicit client goal ("comfort and luxury") as competing definitions of "the right pitch" |
| 30:00–45:00 | Close, re-vote, reflection, Lessons Learned |
