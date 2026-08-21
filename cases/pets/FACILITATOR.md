# Guide Notes: Pets

**Case:** Pets · **Tier:** T2 · **Band:** MS-core · **Studio:** Adventure
**Standards:** see `case.json.standards[]` for the exact ids (22 skills — decimal/whole-number
arithmetic, percent, rounding, currency, and two required visual displays)

Legacy conversion, 2026-08-20, built from the original case study docx
(`source/Y1/Session 4/Pets/Case Study_ Pets.docx` and `Guide Notes.docx`) onto the current
11-anchor ladder. The Thompson siblings, their summer earnings, Mom's insurance requirement, and
both siblings' named breed preferences are preserved verbatim from the source. The original
dilemma's third option (a bird) was dropped per the human-approved lock in
`cases/_concepts/LEGACY_DILEMMA_LOCKS_2026-08-20.md` — see `case.json.legacy_conversion_note` for
the full account of what changed and why, including the cost model, which had to be sourced fresh
(the original appendices were link-only reading lists, not real data).

**A note on sensitive content (SPEC §6):** this case touches a real, if lower-stakes, family-money
dynamic (kids spending their own earned money, a parent's non-negotiable condition) and, in
Appendix C/the Twist, a real genetic health condition in a companion animal. Keep the discussion on
the disclosed numbers, not on Hero pets' own health histories.

## Intro

Frame the format: this is a real "pitch your parent" negotiation, not a worksheet with a story
stapled on. Name the opener — "You get to pick the family's next pet. You're not choosing which one
you like more — you already know that. You're choosing which one you can defend with numbers."

## Launch

Read the Overview aloud, then Background's two load-bearing facts with no Appendix numbers shown
yet: the $1,620 the siblings earned themselves, and Mom's one non-negotiable condition (insurance,
no matter which pet). Ask: "Just from what you've heard — does this feel like an easy call, or a
close one?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Dog or cat?" Show of hands, no discussion yet. Record the count — Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'costs more'?"**

Push on what "costs more" even means here. More on Day 1? More in Year 1? More total, over the
pet's whole life? Or more *per year* it's actually alive? Let the room sit in the ambiguity — "Is
anyone courageous enough to define 'costs more' before we start adding numbers?" Deliberately let
it feel underdetermined: "Wow, this is a harder question than it sounded."

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has picked a working definition, ask them to name the actual steps: Day-1 cost, Year-1
cost, lifetime cost, and — the step almost nobody proposes unprompted — dividing by how many years
the pet is actually expected to live. Re-ask: "Given how we just defined 'costs more' — is that
still the right process?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix E's ten Modeling Assumptions as a group, out loud, before anyone computes anything.
Ask which ones the room thinks matter most. (Facilitator note: MA5 and MA10 — the two lifespan
figures — are the ones that actually matter most, since the primary metric divides by them
directly, but let the room guess first; that's what the Twist leans on.)

## Data Deep Dive

Now, and only now, the numbers. Walk D1–D4 together as a room, building each pet's Day-1, Year-1,
and lifetime totals before touching the per-year division.

**The trap:** most Heroes will build both pets' *lifetime* totals correctly, compare the two raw
dollar figures, and stop there — Option A's raw lifetime total ($38,163) beats Option B's ($25,150)
by 51.7%, which reads as an overwhelming, not-even-close win for the cat. That comparison is
arithmetically correct and it is still the wrong answer to "which pet costs more" as a *fair*
question, because it never accounts for the fact that a Beagle is expected to be alive three more
years than a Scottish Fold — of course the pet that lives longer costs more in total dollars. Cold-
call on this specifically once someone reaches that raw comparison: "You've just told me the dog
costs 51.7% more. Costs 51.7% more *at what*?"

**A second, more dangerous trap sits in D2, before D4 is ever reached.** D2's Year-1-with-insurance
totals are close and, critically, *reversed* from the true per-year answer: Beagle Year-1 = $4,971
vs. Scottish Fold Year-1 = $5,035 — the dog looks cheaper "per year" on this number, while the
correct cost-per-year-of-lifespan (D4's actual metric) has the Fold cheaper ($2,515.00 vs.
$2,935.62). A Hero who does D3/D4's table correctly but then writes their Challenge 2 persuasive
pitch around the more salient, earlier-computed Year-1 figure ("it only costs $4,971 a year for the
dog vs. $5,035 for the cat") will produce a pitch that silently picks the wrong pet — without ever
making an arithmetic error, and without the room's own trap-check catching it, since nothing above
addresses D2. Cold-call on this specifically at the Data Deep Dive, before moving to the Twist:
"Your Year-1 totals are only $64 apart, and the dog's is actually lower. Does that mean the dog
costs less per year over its life? Why or why not?"

## Twist — drop this at roughly the 15-minute mark

Deliver slowly, with pauses:

"Everyone's been comparing total lifetime dollars. But here's something neither pet's breeder puts
in an ad: a Scottish Fold's folded ears come from a real genetic mutation — the same mutation also
affects cartilage all over its body. It's a documented health condition, not folklore, and it's a
real reason the breed's average lifespan runs shorter than a healthy individual's best case. A
Beagle is expected to live about 13 years. A Scottish Fold, on average, about 10."

**Facilitator-only.** Recompute both pets live with the room, dividing each lifetime total by its
own expected lifespan: $38,163 ÷ 13 = $2,935.62/year for the Beagle; $25,150 ÷ 10 = $2,515.00/year
for the Scottish Fold. The gap that looked enormous a few minutes ago (51.7%, dog costs way more)
shrinks to 16.72% (case.json balance.margin_pct) — the cat is still cheaper per year, but not by nearly as much as the raw totals
suggested, and the *reason* the cat's per-year number is smaller — a genetic condition that shortens
its life — is not exactly a selling point for Chloe's pitch either.

Ask: "You now have 60 seconds. Does this change your recommendation — or not?" Then, the follow-up
that matters more than the vote: **"What just broke in your original model? Were you wrong about the
dollars — or were you just missing a way to think about what 'per pet' actually means when the two
pets don't live the same number of years?"**

Do not hand over a "correct" answer. A reasonable pitch can still argue for the Beagle on the
per-year metric losing by 16.7% but delivering three extra years of a kid's favorite pet — or argue
that a documented health risk is exactly why Mom's insurance requirement matters more for the
Scottish Fold than the sticker price suggests. That tension is the real, transferable lesson, not a
trick.

**Twist soundness check (SPEC §6):** this twist was checked against every stated Background/
Appendix fact and Modeling Assumption, read both sequentially (in the order a Hero encounters them)
and simultaneously (all at once, as a final numeric model) — it introduces no new figure that
contradicts an earlier one, only a second, real, disclosed lens (Appendix C/MA5/MA10) on data
already in front of the room. It holds under both readings and does not flip which option wins the
graded metric (Option B stays cheaper per year both before and after the room "discovers" the raw
lifetime gap) — what it changes is the *size* of the gap the room believes it's looking at.

## Immediate recommit

Re-vote immediately. "Did the per-year recompute change your hand — or did it just change *why*
you're holding it up?"

## Close

Re-vote once more after full discussion. Ask: "Did we ask the right question at Anchor 2, or did
'costs more' turn out to mean something different by the end?" And: "What math was new to you today,
and how did you attack it?"

## Lessons Learned

*(Migrated from the original Guide Notes.)* The original discussion split fairly evenly between the
dog and the bird (a third option this conversion drops — see `case.json.legacy_conversion_note`),
and the original guide noted the room addressed nearly every real-world consideration on its own
even without a hard framework forcing it to. This conversion keeps that spirit — Heroes still have
to name and defend a definition of "costs more" themselves at Anchor 2 — while adding the
mathematical apparatus the original case didn't have: **a per-year cost comparison changes which gap
you're looking at, without changing which pet wins.** Raw lifetime dollars make the choice look like
a landslide (51.7%). The fair per-year comparison shows a real but much narrower gap (16.7%). Both
are true. The skill is knowing which one you actually mean when you say "costs more."

## Five Socratic Questions

Use these across Anchors 2–4 and the Data Deep Dive — each is answerable only with this case's own
numbers, not general opinion.

1. Your chosen pet's Day-1 cost is more than the $1,620 the Thompsons actually have saved — how much more, and where does the rest come from?
2. The Beagle's raw lifetime total beats the Scottish Fold's by 51.7%, but its per-year cost is only 16.7% higher — what's the one fact that explains why those two numbers are so different?
3. Mom's insurance requirement adds a bigger percentage to the Beagle's Year-1 total than to the Scottish Fold's — why, given that the Scottish Fold costs more to buy?
4. If a Scottish Fold's shorter average lifespan is caused by a real, documented joint condition, does that make pet insurance more important for Chloe's pick, or does it make the whole pick riskier regardless of insurance?
5. Every dollar figure in this case is a stated midpoint of a real cited range, not one fixed number — how far would the Beagle's expected lifespan (Appendix A/E) have to shift before it changes which pet wins on cost-per-year?

## Standards Touched On

See `case.json.standards[]` (22 ids) and `LEARNING_GOALS.md` for the full deliverable ↔ skill
matrix. In brief: decimal and whole-number arithmetic (all four operations), currency, percent,
rounding, and two required visual displays (bar graph, pie chart).

## Cohort Bands

See `case.json.cohort_bands[]`.

- **Full (12–20):** Anchors 2–3 run as written; the room splits into a "total lifetime dollars"
  faction and a "cost per year of life" faction before the Twist forces everyone to confront why
  those two framings disagree.
- **Compressed (6–11):** Anchors 2–3 combine into one pass; D5's two visual displays are worked as
  one shared example (one option) instead of every Hero building both independently.
- **1:1 / pair (1–2):** No vote to take — Anchor 1 becomes a stated initial position instead of a
  cold-call show of hands; the guide plays devil's advocate directly, arguing whichever pet the
  Hero didn't pick, and personally raises the raw-total-vs-per-year tension if the Hero doesn't find
  it unprompted.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote (Anchor 1) — no explanation |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just cheaper" |
| 10:00–15:00 | Pressure-test the models: "Whose plan breaks first if the lifespan estimate moves?" |
| **15:00** | **DROP THE TWIST** — the genetic-health/lifespan fact and the per-year recompute, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00–30:00 | Threaded deep conflict — two named threads: (1) "total dollars" vs. "dollars per year alive" as competing definitions of *costs more*; (2) a pet's total years with the family vs. a documented health risk as competing definitions of *better* |
| 30:00–45:00 | Close, re-vote, reflection, Lessons Learned |
