# Facilitator Notes — Dice Roll

**Case:** Dice Roll · **Tier:** T4 · **Band:** MS-stretch / HS-entry · **Studio:** Adventure
**Standards:** see `case.json.standards[]` for the exact ids (25 skills — population, sample,
sample size, random, simple/systematic/cluster/multistage/convenience sampling, probability,
percent, proportion, rounding, addition, multiplication, bar graph, pie chart, and their paired
"how to…" skills)

**SPEC §6 flag:** none required. This case is framed around statistical defensibility and
public trust in election administration, not around any real election's outcome, candidate, or
party — no partisan content anywhere in it. **Keep the facilitation strictly factual and
neutral throughout.** Marisol's dilemma is a resource-allocation and sampling-methodology
question about a Division program layered on top of Colorado's mandatory, statutorily required
risk-limiting audit (C.R.S. §1-7-515) — the audit itself is never in dispute in this case, and
nothing here should be read as, or steered toward, a statement about election integrity,
election outcomes, or any party or candidate. If a Hero brings partisan framing into
discussion, redirect to the actual question on the table: given a fixed 5-visit budget, which
sampling design does the Division use to choose where its own compliance monitors stand in
person, and what does that choice cost and represent?

## Intro

Frame the format: a real government-operations dilemma, not a worksheet with a story stapled
on. Name the opener — "Twenty ten-sided dice, rolled on camera, are about to seed the exact
ballots every county in Colorado has to hand-recount. That part isn't up for debate — it's the
law. What Marisol has to decide by end of day is something the dice don't touch at all: which
five counties her own team physically visits to watch it happen."

Worth naming when you introduce her: Marisol was a county poll worker herself, years before she
moved to the compliance side — she's worked a real polling floor, not just reviewed the
paperwork it produces, and that ground-level experience is part of why she stays even-keeled
when a county clerk pushes back hard on a finding. She also keeps a single six-sided die on her
desk, a memento from her first audit-methods training, where an instructor used ordinary dice to
teach random sampling — a small, concrete echo of the math this case actually asks Heroes to do.
Keep this strictly a character/competence detail; it is not political content and should not be
used to editorialize about elections.

## Launch

Read the Overview aloud, then Background's first two paragraphs — the RLA is mandatory
statewide regardless of what Marisol picks; her question is only about the Division's own
supplemental in-person monitoring, capped at 5 visits this cycle. Do not show Appendix C's
dollar figures yet. Ask: "Just from what you've heard — does 'pick the 5 cheapest counties to
reach' sound like it settles this, or not?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"The Statewide Draw or The Front Range Loop?" Show of hands, no discussion yet. Record the
count — Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'representative'?"**

Push on what the compliance-monitoring visit is actually *for*. Is it a spot-check on a handful
of counties, or is it evidence the Division can stand behind that its oversight reaches the
whole state? Does "the 5 counties we can afford to reach easily" answer that, or does it quietly
answer a different, easier question? Let the room sit in the ambiguity — "Is anyone courageous
enough to define what this monitoring program is actually supposed to prove, before we start
comparing dollars?"

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has a working definition of what the visit list needs to accomplish, ask them to
name the actual steps: how many counties are on the roster and how the 12-county roster stands
in for the state (Appendix A), how each option's 5 counties are actually chosen (Appendix B),
what each option costs in total (Appendix C), and what each option's chance of ever reaching a
specific remote county actually is. Re-ask: "Given how we just defined 'representative' — is
that still the right process?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix D's five Modeling Assumptions as a group, out loud, before anyone computes
anything. Ask which ones the room thinks matter most to the cost comparison. (Facilitator note:
MA2 — the $450/day loaded staff-cost figure — is the single most load-bearing assumption in the
whole case, with MA1's 150-mile overnight threshold a distant second; MA3, MA4, and MA5 do not
move the A-vs-B margin at all. Let the room guess first — the Twist and Q1/Q4 below are where
this gets tested directly.)

## Data Deep Dive

Now, and only now, the numbers. Walk D1 (population/sample), D2 (the Statewide Draw's realized
selection and systematic-sampling mechanics), and D5 (total program cost) together as a room.

**The trap:** most Heroes will run the total-cost comparison, see that The Front Range Loop is
cheaper — 19.43% cheaper, just inside SPEC §2's cap — and declare it the clear winner because it
"still hits 5 counties." That reasoning quietly treats *hitting the count* (5 visits) as
equivalent to *representing the state*. It skips D4 entirely: the Front Range Loop's 5 counties
are drawn from a permanently fixed near-Denver subset that structurally can never include the
Eastern Plains, the San Luis Valley, or the Western Slope, no matter how many cycles run or how
the travel budget is spent — that isn't a small probability, it is a hard, structural 0%. Cold-
call on this specifically: "You've got your cost numbers. Now open D4 — what's the chance a San
Luis Valley county gets a Division visit under Option B, this cycle, or ever?"

Show the actual split:

- **Option A (Statewide Draw: Jefferson, Boulder, Pueblo, Kit Carson, Alamosa)** — mileage
  $814.64 + lodging $220.00 (Kit Carson and Alamosa require an overnight stay) + M&IE $340.00 +
  staff time $2,250.00 = **Total A = $3,624.64**
- **Option B (Front Range Loop: Jefferson, Douglas, Larimer, Boulder, El Paso)** — mileage
  $330.48 + lodging $0.00 + M&IE $340.00 + staff time $2,250.00 = **Total B = $2,920.48**
- **Margin: 19.43%** — B is cheaper by about 19.43% on total program cost, just inside the ~20%
  cap. B wins on dollars; A wins overwhelmingly (≈80% vs. a structural 0%, D4) on whether a
  remote region is ever represented at all across three cycles.

## Twist — drop this at roughly the 20-minute mark

**This is the same Twist already live in `published/Dice Roll - Interactive.html`'s gated
"Reveal the Twist" panel — deliver that one, do not invent a competing twist.**

Deliver slowly, with pauses:

"Colorado's own real risk-limiting audit — the one that already happens in all 64 counties
regardless of Marisol's visit plan — sets its random seed at a public meeting where staff roll
20 ten-sided dice on camera while the meeting livestreams, and anyone can verify the resulting
seed and recompute the ballot selection afterward (Appendix B, Appendix E S4). Now a county
clerk pushes back on The Statewide Draw: 'If a county's own audit already uses a fully public,
verifiable random process, why does it matter whether the Division's *observers* get there by
a random draw or by convenience? The audit itself is equally random either way.'"

Ask the room: "Using your D4 probability numbers — what is the flaw in that argument? What,
specifically, is being sampled by Marisol's visit plan that is *not* the same thing the
county-level RLA already randomizes?"

**Facilitator-only — the flaw.** The county-level RLA's random seed picks which *ballots*
inside a county that is already scheduled to audit get hand-recounted; that happens identically
in all 64 counties, every cycle, no matter what Marisol decides. Marisol's decision is a
completely separate, second sampling problem: which *counties* (and, systematically, which of
those counties' scheduled sessions) ever get a Division observer physically standing in the
room. A county can run a flawlessly random RLA every single cycle and still never once host a
Division observer if The Front Range Loop structurally excludes it — the ballot audit's
randomness says nothing about whether the *oversight of that audit* ever reaches that county.
The two random processes are independent and serve different purposes: one protects the count,
the other protects confidence that the count was actually run as designed.

Ask: "Does this change your recommendation — or not?" A Hero who leaned on "the audit's already
random, so the visit plan doesn't need to be" now has to name what, specifically, the visit
plan is actually sampling that the county audit does not.

**Optional, time-permitting extension — a second, quantitative wrinkle:** `sensitivity_model.py`
also ships `evaluate_twist()`, a real-world what-if — a new highway bypass cutting Alamosa's
one-way distance from 235 to 117.5 miles, which crosses MA1's 150-mile overnight threshold and
drops Option A's total from $3,624.64 to $3,354.84 (margin: 19.43% → roughly 12.95%, B still
cheaper both ways). Use this only if the room has time after the conceptual Twist above; it
shows the same lesson — a margin "just inside the cap" is not a stable margin — from the cost
side instead of the sampling-theory side.

Do not hand over a "correct" recommendation either way. A defensible pitch for either option
survives this Twist — the point is forcing a Hero to separate "the process is random" from
"the process is *monitored*," which is the entire reason Marisol's job exists.

**Twist soundness check (SPEC §6):** this twist introduces no new figure and changes no
Appendix value — it is a conceptual challenge built entirely from facts already stated in
Background and Appendix B (the public dice-roll seed process) plus the D4 deliverable's own
probability numbers, so it survives every reading of every stated assumption trivially (it
depends on none of them). It invalidates a real position a room would hold — "the county audit
is already random, so the visit plan's own randomness doesn't matter" — which D4's selection-
probability numbers directly refute. The optional quantitative extension is independently
checked: it changes only Appendix A's Alamosa distance under a real-world event, MA1's 150-mile
threshold is exactly what makes it mechanically matter, and `sensitivity_model.py`'s
`evaluate()`/`evaluate_twist()` confirm the margin moves (19.43% → ~12.95%) without flipping the
winner — the same fragility Appendix D's sensitivity note already flags for MA1/MA2. A's
representativeness argument (D4) does not depend on either twist and is unaffected by both.

## Immediate recommit

Re-vote immediately. "Did the recompute change your hand — or did it just change how confident
you are about *why* you're holding it up?"

## Close

Re-vote once more after full discussion. Ask: "Did we ask the right question at Anchor 2, or
did 'representative' turn out to mean something different by the end?" And: "What math was new
to you today, and how did you attack it?"

## Lessons Learned

The case's own numbers make a point neither option can dodge: a margin that sits "just inside"
a cap (19.43%, against SPEC's ~20%) is not the same thing as a *stable* margin. One real-world
change to a single input — a highway bypass affecting one county's distance — cut the gap
between the two options by a third without changing who won. The transferable lesson: **before
you trust a close margin, ask what it's built on, not just what it says** — a cost comparison
that depends heavily on one or two stated assumptions (here, MA1's overnight threshold and MA2's
staff-day rate) is not wrong for depending on them, but a strong recommendation has to say so
out loud, the way Appendix D and this Twist both do.

## Five Socratic Questions

Use these across Anchors 2–4, the Data Deep Dive, and after the Twist — each is answerable only
with this case's own numbers, not general opinion.

1. The Front Range Loop costs about 19.43% less than The Statewide Draw this cycle — what would Kit Carson and Alamosa's round-trip mileage, or the $450/day staff-cost assumption, have to become before that margin flips?
2. The Statewide Draw gives any one roster county a 5/12 chance of being visited this cycle — does a county's *region* change that county's individual chance of selection, and if not, why does the region matter to the argument for A at all?
3. If the Division ran The Front Range Loop for three straight cycles, what is the probability that Kit Carson, Alamosa, La Plata, or Montezuma is ever visited in person, and what does that number tell you about the difference between a random exclusion and a structural one?
4. Appendix D sets the overnight threshold at 150 miles one-way and the loaded staff-day cost at $450 — which of those two assumptions, if it moved, would flip the margin faster, and how do you know without recomputing both from scratch?
5. A director asks: "Why not just send the compliance team to every scheduled audit session in the 5 Statewide Draw counties, instead of a systematic subsample?" — using your Appendix B numbers, what happens to the review-time cost, and is the plan still meaningfully "multistage" if it does that?

## Standards Touched On

See `case.json.standards[]` (25 ids) and `LEARNING_GOALS.md` for the full deliverable ↔ skill
matrix. In brief: population, sample, sample size, random, simple random sampling, systematic
sampling, cluster sampling, multistage sampling, convenience sampling, probability, percent,
proportion, rounding, addition, multiplication, bar graph, and pie chart, each paired with its
"how to…" skill.

## Cohort Bands

See `case.json.cohort_bands[]`.

- **Full (12–20):** Anchors 2–3 run as written; the room splits into a "representativeness
  first" faction and a "cost first" faction before the Twist forces a live recompute of Option
  A's premium.
- **Compressed (6–11):** Anchors 2–3 combine into one pass; D5's cost-by-category table is
  worked as one shared example instead of every Hero building both options independently.
- **1:1 / pair (1–2):** No vote to take — Anchor 1 becomes a stated initial position instead of
  a cold-call show of hands; the facilitator plays devil's advocate directly, arguing whichever
  option the Hero didn't pick.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote (Anchor 1) — no explanation |
| 3:00–8:00 | Position defense: "Convince us why it's the right visit list, not just the cheaper one" |
| 8:00–13:00 | Define the process (Anchor 3): what data would actually settle this? |
| 13:00–20:00 | Data Deep Dive: cost comparison, then D4's selection-probability comparison — name the trap |
| **20:00** | **DROP THE TWIST** — the Alamosa highway bypass, delivered slowly |
| 20:00–25:00 | Immediate recommit: does any hand move? "What actually broke?" |
| 25:00–35:00 | Threaded deep conflict — two named threads: (1) total dollar cost vs. statewide selection-probability coverage as competing definitions of "the right visit list"; (2) a margin that looked stable (19.43%, just inside the cap) vs. one shown to move by a third on a single real-world change |
| 35:00–45:00 | Close, re-vote, reflection, Lessons Learned |
