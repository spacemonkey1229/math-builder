# Guide Notes: Medical Statistician

**Case:** Medical Statistician · **Tier:** T3 · **Band:** MS-stretch / HS-entry · **Studio:** Adventure
**Standards:** see `case.json.standards[]` for the exact ids (21 skills — sampling methods,
population/sample vocabulary, currency and multi-step arithmetic, percent, and one required bar
graph)

Legacy conversion, 2026-08-20, built from the original case study docx
(`source/Y3/Session 2/Medical Statician/Case Study_ Medical Statistician.docx` — no separate Guide
Notes document exists for this case) onto the current 11-anchor ladder. The protagonist, the drug,
the budget, and the canine-diabetes facts are preserved from the source; the binary dilemma was
resolved per the human-approved lock in `cases/_concepts/LEGACY_DILEMMA_LOCKS_2026-08-20.md`. See
`case.json.legacy_conversion_note` for the full account of what changed and why.

**A note on sensitive content (SPEC §6):** this case involves animal testing, including the
disclosed fact that a few pilot-study dogs died. Keep the discussion on the study-design math, not
on animal-welfare debate for its own sake — the case's real tension is statistical/regulatory
rigor vs. cost and speed, not whether animal drug trials should exist.

## Intro

Frame the format: this is a real methodological choice pharmaceutical statisticians actually face,
not a worksheet with a story stapled on. Name the opener — "Two honest ways to build a clinical
trial sample. One is textbook-correct. One is what a company under budget and deadline pressure
actually does. Which one do you run?"

## Launch

Read the Overview aloud, then Background's two sentences about the $600,000 budget and the 1-month
launch / 7-month conclusion window, with no Appendix numbers shown yet. Ask: "Just from what you've
heard — does 'more random' obviously mean 'better' here?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who's building the random national sample? Who's going through the partner clinics?" Show of
hands, no discussion yet. Record the count — Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'better'?"**

Push on what "better" means here. Better *evidence for the FDA*? Better *margin of error for the
same dollar*? Better *odds of actually finishing on budget and on time*? Let the room sit in the
ambiguity — "Is anyone courageous enough to define 'better' before we start computing anything?"
Deliberately let it feel underdetermined: "Wow, this is a harder question than it sounded."

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has picked a working definition of "better," ask them to name the actual steps: cost
per enrolled subject, how many subjects that buys within the shared $493,000, and what margin of
error that sample size produces at 95% confidence. Re-ask: "Given how we just defined 'better' — is
that still the right process, or does it leave out something the FDA appendix already told us?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix G's four Modeling Assumptions as a group, out loud, before anyone computes
anything. Ask which ones the room thinks matter most. (Facilitator note: MA1/MA2 — the
recruitment-cost-per-subject figures — are the ones that actually decide the numeric answer; let
the room guess first, that's what the Data Deep Dive is for.)

## Data Deep Dive

Now, and only now, the numbers. Walk D1 and D5 together as a room: budget ÷ cost-per-subject = max
sample size; sample size → margin of error via Appendix E's formula.

**The trap:** most Heroes will compute both options' margins of error, see that Option B's is
smaller (more precise), and conclude Option B is simply the better study — full stop, cost problem
solved. They will not connect that number back to Appendix F's actual legal language, because
Appendix F reads like background flavor text, not something with a number attached. Cold-call on
this specifically after the margin-of-error numbers are on the board: "You've just shown B gives a
tighter margin of error. Does a tighter margin of error mean the FDA will approve this drug faster?"

**A second, quieter trap sits in D1 itself.** Appendix B states that a pure random draw needs to
contact roughly 300 dogs to find one that already has diabetes — the real, cited reason Option A is
slower and more expensive than B. A Hero doing D1's sample-size arithmetic may try to apply that
300:1 ratio as a literal multiplier on top of MA1's $250/subject figure, which blows the $493,000
budget by roughly two orders of magnitude and produces a sample size near zero. MA1's $250 is
already an *all-in* per-enrolled-subject figure (see Appendix G's note) — the 300:1 ratio explains
*why* $250 is set higher than MA2's $90, it is not a second cost layer to multiply through. Watch
for a Hero who tries to stack both and gets a nonsensical result; redirect them to re-read MA1's
basis note before they conclude Option A is unaffordable at any sample size.

## Twist — drop this at roughly the 15-minute mark

Deliver slowly, with pauses:

"Everyone arguing for Option A has been treating this as settled: 'non-random data just doesn't
count for the FDA.' It's not that settled. In 2021, FDA's Center for Veterinary Medicine finalized
real guidance — GFI #266 — that explicitly describes how the agency *will* evaluate real-world
data, including registry and clinic-record data, when it's submitted to help demonstrate a drug
works."

**Facilitator-only.** For the record, the two options' computed margins of error are Option A 3.53%
and Option B 3.06% at each option's maximum affordable sample size — a 15.5% precision gap on the
case's graded primary metric. This does not flip the case to Option B being regulator-approved automatically
— GFI #266 describes real-world data as something CVM will *evaluate* to help demonstrate
effectiveness, not a replacement for the "adequate and well-controlled" randomized standard in 21
CFR 514.117 that Appendix F already quoted. What it breaks is the *strong-form* anti-B argument some
Heroes will have built ("B can never work for FDA, so the cost savings don't matter") — that
position is now indefensible as stated. It does not make the reverse position ("so B is just as
good") defensible either: 514.117's own randomization language still stands as the base legal
requirement Option A alone actually satisfies. The twist narrows the gap between the two arguments;
it does not close it.

Ask: "You now have 60 seconds. Does this change your recommendation — or not?" Then, the follow-up
that matters more than the vote: **"What just broke in your original model? Were you wrong that
regulators only accept random data — or were you just missing that 'weaker evidence' and
'automatically rejected' are two different things?"**

Do not hand over a "correct" answer. Reasonable statisticians genuinely disagree about how much
weight a regulator's real-world-data pathway should get against the base-case randomization
standard — that's the real, transferable tension, not a trick.

**Twist soundness check (SPEC §6):** checked against every stated Background/Appendix fact and
Modeling Assumption, read both sequentially (in the order a Hero encounters them) and
simultaneously (all at once, as a final model) — it introduces no new figure that contradicts an
earlier one (Appendix F's 514.117 quote is unchanged; GFI #266 is an additional, real, separately
cited regulation, not a correction to the first one), only a second, real, disclosed layer of
regulatory nuance. It holds under both readings, and it does not touch the case's numeric primary
metric (margin of error) at all — it only reframes what that metric is worth to the FDA decision.

## Immediate recommit

Re-vote immediately. "Did the GFI #266 reveal change your hand — or did it just change *how
confident* you are in the hand you already had up?"

## Close

Re-vote once more after full discussion. Ask: "Did we ask the right question at Anchor 2, or did
'better' turn out to mean something different by the end?" And: "What math was new to you today,
and how did you attack it?"

## Lessons Learned

The original case's own Challenges asked students to report a margin of error but gave no
mechanism for connecting that number to anything regulatory — a Hero could compute a perfectly
correct margin of error and never realize it doesn't settle the FDA question by itself. This
conversion adds that mechanism directly: **a smaller margin of error is not the same thing as
stronger evidence**, because margin of error only measures precision *given* the sample is
unbiased — it says nothing about whether the sample actually is. Option B can be numerically more
precise and legally weaker at the same time. That distinction — precision vs. validity — is the
core transferable lesson, and it is exactly the distinction real regulators are paid to make.

## Five Socratic Questions

Use these across Anchors 2–4 and the Data Deep Dive — each is answerable only with this case's own
numbers, not general opinion.

1. Option B's margin of error (3.06%) is smaller than Option A's (3.53%) — what does margin of error actually measure, and what does it *not* measure about a sample?
2. Appendix D shows real recruitment costs ranging from $74 to $797 per patient in the very same study — what would have to be true about Bansky's own partner-clinic relationships for Option B's $90/subject assumption to be too optimistic?
3. Appendix F quotes the FDA's own legal language: a well-controlled study's assignment "is random and minimizes bias." If Option B is not random, what exactly is Bansky betting on when it chooses convenience sampling anyway?
4. Every dog recruited through Option B's partner clinics is already a diagnosed, at-risk-breed dog under a vet's care. How might that make Paxovir look *better* or *worse* than it would in the full general population Bansky ultimately wants to sell to?
5. If Bansky's own recruitment-cost assumption for Option A fell by half, would Option A still cost more per subject than Option B — and why or why not?

## Standards Touched On

See `case.json.standards[]` (21 ids) and `LEARNING_GOALS.md` for the full deliverable ↔ skill
matrix. In brief: sample/population/sample-size vocabulary, all four probability sampling methods
and convenience (non-probability) sampling, randomness, probability, currency and multi-step
arithmetic (all four operations), percent, and one required bar graph.

## Cohort Bands

See `case.json.cohort_bands[]`.

- **Full (12–20):** Anchors 2–3 run as written; the room splits into a "precision" faction and a
  "regulatory validity" faction before the Twist forces everyone to hold both at once.
- **Compressed (6–11):** Anchors 2–3 combine into one pass; only one deep-conflict thread
  (statistics OR regulation, not both) runs in the 20:00–30:00 window.
- **1:1 / pair (1–2):** No vote to take — Anchor 1 becomes a stated initial position instead of a
  cold-call show of hands; the guide plays devil's advocate directly, arguing whichever side the
  Hero didn't pick.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote (Anchor 1) — no explanation |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just more precise" |
| 10:00–15:00 | Pressure-test the models: "Whose plan breaks first if the recruitment-cost assumption moves?" |
| **15:00** | **DROP THE TWIST** — the GFI #266 real-world-data reveal, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00–30:00 | Threaded deep conflict — two named threads: (1) precision (margin of error) vs. validity (randomization) as competing definitions of "good evidence"; (2) cost-effectiveness vs. regulatory risk as competing definitions of "the right business call" |
| 30:00–45:00 | Close, re-vote, reflection, Lessons Learned |
