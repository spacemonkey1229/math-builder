# Guide Notes: The Overlap Call

MS | Guide Notes | Adventure | 2026-27
**Tier:** T2 (MS core) · **Primary metric:** confirmed secondary cases found per test kit used · **Margin:** **1.11%**, Widest Net (A) narrowly ahead pre-twist — canonical figures below (D4 outlier dropped from both real sets). This margin is genuinely fragile — see the sensitivity note before Lessons Learned, and `case.json.sensitivity_disclosure[]`.

**Do not distribute to students.** This document, and `case.json`'s `balance_test` object, are the only places the balance argument, the margin, and the wrong-path analysis below may live. `case.md` carries the counting convention (rounding) needed to solve the case at all, but never the verdict.

---

## Intro

Heroes, Priya has 45 test kits and a list of names much longer than that. Some names are on both
index patients' lists. Do you cast the widest possible net, or do you spend every kit on the
group you can argue carries the highest concentration of shared risk? There's no answer key here —
the real margin between these two plans is razor-thin, and it moves depending on exactly how many
kits Priya has this week.

## Launch

Show the two flagged contact lists as two overlapping circles, unlabeled, no numbers yet. Ask:
*"If you had far more names than tests, would you rather test everyone touched by either case, or
only the people touched by both?"*

Let them argue it cold. Then: *"Priya's supervisor is already asking why last week's allocation ran
out early. She has to decide today."*

> **Hero name — Widest Net or Shared Risk? Open for us.**

---

## Anchor 1 — Take a stand and vote

Option A (Widest Net) or Option B (Shared Risk). No reasoning yet.

Hands up for A. Hands up for B. Write the split on the board.

*"Is anyone courageous enough to stand with ______?"*

## Anchor 2 — What is the problem we're solving?

Do **not** let them start calculating yet.

- What's the actual question? Say it in one sentence.
- Is it "which group has more people in it"? Is it "which group finds more raw cases"? Is it
  "which group finds more confirmed cases *per test kit spent*"? **Those are three different
  questions**, and only the third is the one Priya's weekly report actually forces her to answer.
- Is that the right question?

**Socratic Q1.** "You have $|A \cup B|$ = 209 people flagged (208 if you dropped the outlier) and
only 45 kits. Which 45 people does your plan actually call first, and why those?"

**The trap to let them walk into.** A student computes D5's raw counts, sees Widest Net finds more
confirmed cases (7) than Shared Risk (4), and assumes the bigger raw number means the better plan
— without ever computing the per-kit ratio the case's own primary metric actually asks for. This
trap is guaranteed to catch anyone who treats a superset's larger headcount as evidence of
anything: the union of two sets is never smaller than either one, so of course it finds at least as
many cases — that comparison is settled by set size alone and proves nothing about which plan uses
its kits well. A second, subtler version of the same trap: a student who never checks Appendix A's
Data Note assumes the flagged outlier (node 828) is automatically a real dual exposure "because the
data says so," and misses that a real contact-tracing system would investigate an implausible
overlap before trusting it — computing D3/D5 on a set that still includes a likely data artifact.

## Anchor 3 — What is the process?

- What's the process we'll go through to answer it?
- If the union always finds more raw cases, are we done? Or is raw count the wrong unit for a
  decision that's actually about kit efficiency?
- **Socratic Q2.** Your intersection group is only 26 or 27 people, depending on what you decided
  about the outlier. If you fully test all of them, you still have well over a third of your kit
  allotment sitting unused — what do you do with the rest? Does your plan even use every kit?
- Is our question still the right question?

## Anchor 4 — What don't we know?

- What's missing that we'd need to answer this properly?
- Appendix C gives you the Modeling Assumptions. Do you believe them? **Have them actually try
  flexing MA1 (the kit allotment) up and down and watch how much the comparison moves** — it moves
  a lot, and not smoothly.
- **Socratic Q3.** Node 828 appears on both lists but looked like a possible data error in
  Appendix A. If you drop that one contact from the intersection, does your recommendation change?
  (Canonical answer: it doesn't flip the winner, but it does narrow the margin from 5.00% to
  1.11% — close enough that a different kit allotment easily flips it.)
- **Socratic Q4.** The union group is bigger and will always find more total cases in raw count —
  7 vs. 4 here. Why isn't that the number that should decide this?

---

## Data Deep Dive

Now the numbers. Work these on the board with them. Remind the room of case.md's counting
convention before anyone divides: round the expected case count to the nearest whole person, then
divide by kits used.

**Canonical (D4 resolved as "drop the outlier," node 828, from both sets — matching real
contact-tracing practice of investigating an implausible overlap before trusting it):**

| Plan | Pool tested | Kits used | Expected cases (round(kits×16.6%)) | Ratio |
|---|---|---|---|---|
| Widest Net (A) | 208 (union) | 45 (of 208 — partial coverage) | round(45×16.6%)=7 | 7/45 = **15.56%** |
| Shared Risk (B) | 26 (intersection) | 26 (of 26 — full coverage, 19 kits unused) | round(26×16.6%)=4 | 4/26 = **15.38%** |

**Margin = (15.556 − 15.385) / 15.385 ≈ 1.11%, A ahead.** Comfortably inside SPEC §2's ~20% cap —
but this tight *because* both groups share the identical MA2 rate. Say this plainly to a room that
gets this far: when two plans apply the same rate, the true expected-value ratio for each is
mathematically just the rate itself, no matter how many kits are used — the entire 1.11% margin is
a **whole-number-rounding artifact** of testing 45 people vs. 26, not a real difference in risk the
data supports. This is not a defect specific to this pair of ego-networks or this kit count; it is
true of any real network pair paired with a flat shared rate. (Verified during 2026-09-13
remediation: the alternate candidate ego-node pair 414/348, with sizes 159/227 and a 44-person
intersection, produces the identical structural pattern — a ~2% rounding-driven margin, not a
robust one — so retuning the data pairing cannot fix this; only a genuinely different dual-exposure
rate could, and none exists to source honestly. See `case.json.sensitivity_disclosure[]`.)

**Sensitivity — if D4 is instead resolved by keeping node 828** (raw, undropped sets: |A|=66,
|B|=170, |A∩B|=27, |A∪B|=209): Shared Risk becomes 4/27=14.81% (round(27×16.6%)=4, same numerator,
bigger denominator), Widest Net unchanged at 15.56%. **Margin widens to 5.00%**, still A. Either
resolution of D4 keeps the case inside the cap.

**Push the room directly:** *"If your ratio for Widest Net came out lower than Shared Risk's,
would you trust that difference — or would you ask what happens with one fewer kit in the
allotment?"* Nobody should leave this room thinking a 1-point margin from rounding is the same kind
of fact as a real measured difference in risk.

---

## Twist — drop this at roughly the 15-minute mark

Deliver it as breaking news, not as a scripted reversal.

> *"Priya's phone buzzes again. This time it's the county lab."*
>
> (pause)
>
> *"A processing-equipment failure just cut usable test-kit supply for the rest of the week —
> from 45 kits down to 27. Same two lists, same rate. Fewer tests."*

**Facilitator only — read before you drop this, do not read aloud verbatim.** This is a flex of
MA1 (kits_per_week), not a change to either real set. Run through `sensitivity_model.py`'s
`evaluate_twist()`: at 27 kits, Widest Net's ratio becomes round(27×16.6%)/27 = 4/27 = **14.81%**,
while Shared Risk is untouched at 4/26 = **15.38%** (it was already using fewer than 27 kits). **The
winner FLIPS from Widest Net (A) to Shared Risk (B), margin 3.85%.** This is a real flip on the
case's own sourced/assumed numbers, not a hypothetical — confirm a room that gets there against the
model, not just the narrative. The lesson: Widest Net's efficiency edge depends on spreading a
shared, flat rate over as many kits as the allotment allows; when the allotment shrinks, that edge
can vanish or reverse, while a plan that already fully covers a small, fixed group is untouched by
the cut.

Now: **"Sixty seconds. Are you changing your recommendation — or not?"**

## Immediate recommit

- Who is flipping? Why?
- Who is holding their position anyway — on what grounds, if the ratio itself flipped?
- **What just broke in your original model?**
- **Were you wrong — or was your answer just riding on an assumption you didn't know was load-
  bearing?** (Sit on this one.)

---

## Deep conflict — threads (Full band)

**Thread 1 — Rate vs. reach.** Widest Net guarantees no exposure category goes completely
untested; Shared Risk guarantees every kit lands on someone with compounded exposure. Which
failure mode is worse: missing someone who was only ever going to be a single, lower-probability
exposure, or spending kits confirming what you already suspected about the highest-risk group?

**Thread 2 — What the outlier decision actually costs.** If the flagged contact (D4) is dropped as
a data error, does either plan's per-kit ratio change enough to flip the recommendation on its own?
Re-run D5 live with and without that one person.

**Thread 3 — Who Priya is accountable to.** She reports kits used and testing efficiency to a
supervisor who is already asking hard questions. After the twist, which plan is easier to defend in
that report — the one that used every kit even after the cut, or the one whose numbers didn't move
at all?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch. *"Thirty seconds — union or intersection?"* Stand/sit vote, no explanation yet. |
| 3:00–10:00 | Position defense (pre-twist). *"Convince us why it's the better use of two kits, not just the more thorough-sounding one."* |
| 10:00–15:00 | Pressure-test: *"How many kits does your plan actually spend? Does it use all of them?"* · *"Have you resolved the outlier contact yet?"* |
| **15:00** | **DROP THE TWIST** — the lab equipment failure, 45 kits → 27. Finish with: *"Does this change your plan — or not?"* |
| 15:00–20:00 | Immediate recommit. Who reverses? *"What just broke?"* |
| 20:00–30:00 | The three threads: rate vs. reach · the outlier's real cost · who Priya answers to. |
| 30:00–45:00 | Close, re-vote against the Anchor 1 board, reflection, lessons learned. |

---

## Close

- **Vote again.** Compare to the Anchor 1 board. Who moved?
- We asked ______ as our key question. Was it the right one?
- What math was new to you here, and how did you attack it?
- If you got a case like this again, what would you check first?

**Socratic Q5.** If tomorrow's two index patients had contact circles that barely overlapped at all
— say $|A \cap B|$ near zero — would you still recommend the same option? What does that tell you
about how much your answer depends on this week's specific overlap and this week's specific kit
count?

## Lessons Learned

The arithmetic has a clean, teachable structure: when two plans are compared using the *same* rate
applied to different pool sizes, the "true" per-kit yield of each plan is mathematically just that
rate, in expectation — any margin you see between them is a whole-number-rounding artifact of
exactly how many kits each plan uses, not a real difference in underlying risk. That is genuinely
true here (case.json's own `sensitivity_disclosure[]` records it), and it is not a flaw unique to
this case's specific ego-network pair or kit count — a real, thorough remediation check (2026-09-13)
confirmed the same pattern holds for the concept sheet's alternate candidate pair (ego-nodes
414/348). The lesson for students is not "this case is broken" — it's that **a razor-thin margin
built on rounding is fragile in a way a large margin built on a real rate difference is not**, and a
careful solver should be able to tell the difference and say so.

The twist (a real-world kit-supply shock, not a set-membership change) is the part of this case
that exists to be reused: any time two options are compared by a ratio that is mostly a rounding
artifact, a small external shock to the denominator (kits available) can flip the recommendation
outright — which is exactly what happened here, live, from 45 kits to 27.

A facilitator running this room should say plainly what the case says: Widest Net wins on the
canonical numbers, that win is real but tiny (1.11%, mostly rounding noise) and easily reversed by
a small real-world change in kit supply — and the room should leave understanding *why* a thin,
rounding-driven margin is a different kind of fact than a robust one.

---

## Standards Touched On

**Reinforcement case — no new_coverage (see `case.json.reinforcement_note` and
`LEARNING_GOALS.md`):** Set · Subset · Union · Intersection · Empty Set · Venn Diagram · Vertex ·
Edge · Graph (Vertices and Edges) · Outlier · How to find the union and intersection of two sets ·
How to represent a set relationship using a Venn diagram

---

## Cohort bands

See `case.json.cohort_bands` — Full (12–20), Compressed (6–11), and 1:1/pair (1–2), each with the
same three-tier structure used across the corpus.

- **Full (12–20).** The plan above runs as written; all three deep-conflict threads get their own
  pass in the block after the twist recommit.
- **Compressed (6–11).** Anchors 2–3 combine into one pass ("what are we deciding, and how"). Build
  the Venn diagram together as one shared board example rather than each Hero drawing their own
  first. Run only Thread 1 (rate vs. reach) — it needs the least setup and carries the case's real
  teaching point. The twist still drops at 15:00.
- **1:1 / pair (1–2).** No vote to take at Anchor 1 — the learner states an initial position
  instead. The facilitator argues the other side directly. The twist still lands; "who reverses"
  becomes "would you reverse, and why."

## Facilitator note — sensitivity

This case involves disease exposure and limited test-kit capacity. Frame the stake as **contacts
protected**, not cases missed, per SPEC Section 6's protection-over-destruction guidance.
Facilitators should note this explicitly before the discussion. Some learners may connect this to a
real experience (a family member's own contact-tracing call, a school exposure notice); give that
room rather than rushing past it into the arithmetic.
