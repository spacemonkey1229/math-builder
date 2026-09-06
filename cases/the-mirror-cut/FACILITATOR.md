# Guide Notes: The Mirror Cut

**Case:** The Mirror Cut · **Tier:** T2 · **Band:** MS-core · **Studio:** Heroes Academy
**Standards:** Geometry / Transformations (13 skills claimed, all already-covered reinforcement —
see `case.json.standards[]` and `reinforcement_note` for why `new_coverage[]` is genuinely empty)

Researched and margin-resolved 2026-09-05 (`margin_pct` = 9.99, see `sensitivity_model.py`). This
file is re-checked for drift at every readiness run (the continuity checks in `case-readiness`).

## Intro

Frame the format before anything else: this is a real production-cost decision with a fixed
quote deadline, not a worksheet. Name the opener — "You are the production lead with a bid due at
9 AM. Whichever file you send to the machine tonight is the number your shop lives with for years."
Let the stakes land before moving to the Launch.

## Launch

Show both nesting files side by side (the same pair described in the Overview) with no numbers
labeled — just the layouts. Ask: "Which one do you think actually costs less per bracket, just from
looking at it?" Do not confirm or correct answers here. Most rooms will guess the tighter, mirrored
layout is the obvious win because it "clearly" uses less steel — that gut read is close to right on
material, but it is worth recording out loud before anyone touches a calculator, because the room
is about to learn that "uses less material" and "costs less per part" are not automatically the
same statement.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Sam on The Straight Run — the plain layout everyone
assumes must lose?" Show of hands, both options, no discussion. Record the count — Close will ask
them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'better'?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which one uses
less steel" or "which one looks more efficient," but the case only grades one specific number: net
cost per finished bracket, material plus machine time combined. Push on it: "Sam's boss doesn't
care which file looks more clever. Sam's boss cares what the shop can promise a customer for three
years." If the room lands on "efficient nesting and cheap-per-bracket are related but not
identical" on its own, the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "looks efficient" from "the graded number," ask them to name the actual
steps before touching the appendices: correctly translate the bracket to build The Straight Run
(D1), reflect and translate to build The Mirror Cut's interlocked pair and verify its symmetry
(D2), confirm the 180° rotation gives the same result a second way (D3), check the block still fits
the laser bed rotated (D4), find and use a dilation scale factor for the QC gauges (D5), and only
then run the full nesting takeoff (D6). Re-ask: "Is our question still the right one, now that we
can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gap honestly: Appendix E's three Modeling Assumptions (MA1 the pierce-count
multiplier, MA2 the cutting-speed penalty, MA3 the reject rates) are stated, not sourced — no
public per-shop study exists for any of them at this exact part and nest. Ask which ones change the
*graded* number if they move. The honest answer: MA1 and MA2 do enter the graded net-cost-per-
bracket metric (they set the machine-time side of it), but flexing either one ±50% does not flip
the winner — material cost dominates the total too heavily. MA3 doesn't touch the graded metric at
all; it only matters once the Twist lands. Let a sharp Hero find this themselves before confirming
it — it is a genuine, useful finding, not a gotcha.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's translated coordinates, D2's reflection and symmetry
check, D3's rotation cross-check, D4's bounding-box rotation, D5's scale-factor/dilation pair, and
D6's takeoff together as a room, cold-calling for D2 and D3 specifically — these are where a Hero
who never actually reflected the coordinates (just eyeballed "it flips") or never actually rotated
them 180° to check the match (just assumed it would match) will visibly struggle, which is useful
information for the facilitator, not a moment to rescue.

**Facilitator-only geometry note.** Reflecting bracket A(0,0) B(6,0) C(4.5,4) D(1.5,4) across the
x-axis gives (0,0),(6,0),(4.5,−4),(1.5,−4); translating that copy down 0.25 in (the kerf margin)
gives the interlocked partner (0,−0.25),(6,−0.25),(4.5,−4.25),(1.5,−4.25). The line of symmetry
between the two is y = −0.125 — every original vertex reflects onto its partner's matching vertex
exactly across that line (D2). Rotating the *original* bracket 180° about the point (3, −0.125)
gives (6,−0.25),(0,−0.25),(1.5,−4.25),(4.5,−4.25) — the same four points as D2's construction, just
listed in reverse winding order (D3): reflection reverses orientation, 180° rotation preserves it,
and for this specific interlocked pair both routes land on the same outline. Rotating the combined
block's bounding box ((0,−4.25) to (6,4)) 90° CCW about the origin swaps its 6 in × 8.25 in
footprint to 8.25 in × 6 in (D4) — same footprint, rotated.

**Facilitator-only cost note.** The Straight Run: 196 brackets/sheet, $1.4688 material + $0.01139
machine time = **$1.48019/bracket**. The Mirror Cut: 219 brackets/sheet (the sourced 12% real-world
mirrored-nesting yield gain applied to 196), $1.31454 material + $0.01770 machine time (MA1's extra
pierce, MA2's slower cut) = **$1.33224/bracket**. Margin: **9.99%**, The Mirror Cut wins. The
machine-time cost is real (55.4% higher per bracket than The Straight Run's) but it is small
next to material cost, so it narrows the win from the 10.5%-material-only figure down to 9.99% net
— it does not come close to erasing it. The single biggest lever on this number, if a Hero wants to
argue with it, is the sourced 10–15% yield range itself (S7) — a Hero who picks 10% instead of the
case's 12% gets a real, slightly smaller margin; a Hero who picks 15% gets a real, slightly larger
one — not either Modeling Assumption in Appendix E.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Sam sends the net-cost-per-bracket numbers to the shop owner. She nods, then hands over something
else: the solar installer's inspection contract, and a note from the shop's own quality tech about
the last time they ran a tightly mirrored nest on a job this size. 'Some of those brackets came back
warped. Read the reject clause before you sign anything.'"

"Does the reject clause change what Sam should actually recommend?"

**Facilitator-only: what the numbers actually do.** Using Appendix E's stated reject-rate
assumptions (MA3: The Straight Run 1%, The Mirror Cut 4%, based on the real, documented
heat-affected-zone distortion risk in tightly nested cuts), the cost of a *good* bracket rises for
both layouts, but rises more for The Mirror Cut: The Straight Run's good-part cost becomes
$1.48019 / 0.99 = **$1.495141**; The Mirror Cut's becomes $1.33224 / 0.96 = **$1.387749**. **The
Mirror Cut still wins — but the margin narrows from 9.99% to 7.18%.** The twist does not flip the
verdict; it erodes it, which is itself the point: the room's naive read of the sourced 10–15%
material-yield number would suggest a similarly large *net* win, and the twist shows the real
margin is smaller than that at every stage — first machine time, now reject risk — without ever
actually reversing the decision. Do not hand this reasoning over unprompted; let a Hero who took
Anchor 4's finding seriously (that MA1/MA2 don't flip the graded metric) reason toward why MA3
might behave differently — it's a genuinely separate assumption, revealed later, not baked into the
graded number at all.

## Immediate recommit

Re-vote immediately. Ask by name: "Does the reject clause change your vote — or does it just tell
you the margin you were quoting on was thinner than it looked?" That distinction is the
transferable skill, not the vote itself.

## Deep conflict — three threads (20-30 min)

1. **Yield percent isn't net-cost percent.** The sourced material-yield improvement is 10–15%, and
   the case's own graded net-cost win is 9.99% — close, but not the same number, and the twist
   narrows it further to 7.18%. Why does a real percentage improvement in one part of a cost model
   not automatically show up as the same percentage in the bottom line?
2. **Three assumptions vs. zero.** The Straight Run's number depends on no stated assumption at
   all; The Mirror Cut's better number depends on three (MA1, MA2, and — once the twist lands — MA3).
   Does "wins by a real margin, but needs more assumptions to defend it" change how confident Sam
   should sound quoting it for three years?
3. **Whose multiplier, whose rate.** MA1's 2× pierce count and MA2's 70% speed factor are the case
   author's own estimates, not timed studies. What would a Hero want to see before trusting either
   number more, or less — and does it matter that neither one, even flexed 50% in either direction,
   changes who wins?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both nesting files, cold-call for a gut read, no formulas yet |
| 3:00–10:00 | Position defense — *"Convince us the graded number is the number that matters"* |
| 10:00–15:00 | Pressure-test the models — *"Whose nesting file is most fragile to a bad assumption?"* |
| **15:00** | **DROP THE TWIST** — the inspection contract and reject clause, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (yield% vs. net-cost%; three assumptions vs. zero; whose multiplier) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes will look at the sourced 10–15% material-yield figure and assume the net-cost-per-
bracket margin must be roughly that large too — treating a real, sourced material statistic as if
it were already the answer to the graded question. Watch for a pitch that quotes "The Mirror Cut
saves about 12% on the contract" without ever actually running D6's full takeoff — it has not
distinguished material savings from net-cost savings, and the real number (9.99%, then 7.18% after
the twist) is smaller both times.

## Socratic questions

1. The sourced material-yield improvement is 10–15%, but the case's own graded net-cost margin is 9.99%. What has to be true about a cost model for a real percentage improvement in one input to not show up as the same percentage in the final number?
2. D2 asks you to verify the interlocked pair is symmetric about a specific line using coordinates, not just by eye. Why does a shop's actual laser program need that fact to be exactly true, not just approximately true?
3. Neither Modeling Assumption in Appendix E (MA1, MA2) can flip the graded winner, even flexed 50% in either direction. Does that make them safe to be wrong about, or does it just mean they were never the real risk in this decision?
4. After the reject-clause twist, The Mirror Cut is still cheaper, but by 7.18% instead of 9.99% — a real margin, but a thinner one. Which of those two numbers would you want in front of you if you were the one signing a three-year fixed-price contract?
5. Sam has one night. What does Sam actually tell the shop owner — and does the reject clause change the answer, or just how confident Sam should sound giving it?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that voted for
The Mirror Cut at Anchor 1 purely on "it looks tighter" and stays with it after the twist for a
*different, numbers-based* reason has genuinely moved, even if the vote count looks unchanged.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Anchor 4's "the Modeling Assumptions don't flip the graded metric" finding landed as a
  discovery or had to be told outright.
- Whether "yield percent isn't net-cost percent" was the actual sticking point, or whether D2/D3's
  reflection-vs-rotation cross-check was the harder gate for most Heroes.
- Whether the twist's erosion (not a full flip) felt earned or felt like the case pulling its
  punch, worth listening for directly.

## Standards Touched On

Translation · Reflection · Rotation · Symmetry · Line Of Symmetry · Dilation · Scale Factor

## Facilitator note — sensitivity

Light touch only (SPEC §6): the stakes here are a small business's livelihood riding on a
multi-year contract bid, which can land as real financial-stress texture for some Heroes even
though nobody in the case faces illness, death, or family hardship. If a Hero seems to be reading
too much personal weight into "the shop could lose everything," it's fine to name that the numbers
in this case are realistic but the shop itself is fictional.
