# Guide Notes: Revisit Gap

MS | Guide Notes | Adventure | 2026-27
**Tier:** T3 · **Primary metric:** hectares of confirmed illegal clearing detected per dollar of annual imagery cost · **Margin:** 16.4% (sensitive — see the sensitivity note before Lessons Learned)

**Do not distribute to students.** This document, and `case.json`'s `balance` object, are the only
places the balance argument, the margin, and the wrong-path analysis below may live. `case.md`
carries only a one-line pointer comment to this file.

---

## Intro

Heroes, Marcus has a nine-day deadline and one line item the board will actually argue about: the
satellite bill. There's no answer key — free isn't automatically the smart choice, and expensive
isn't automatically the safe one, and the numbers genuinely come out close.

## Launch

Show two side-by-side image tiles of the same forest edge — one crisp, one blurrier. Ask:
*"If a $15,600-a-year subscription caught every clearing and a free feed missed half of them,
would the subscription be worth it? What if it only caught a few more?"*

Let them argue it cold, no numbers yet. Then: *"Marcus has watched both feeds work for three
years. He still isn't sure which one is actually worth funding."*

> **Hero name — Commercial Weekly or Sentinel Free? Open for us.**

---

## Anchor 1 — Take a stand and vote

Option A (Commercial Weekly) or Option B (Sentinel Free). No reasoning yet. Hands up. Write the
split on the board.

*"Is anyone courageous enough to stand with ______?"*

## Anchor 2 — What is the problem we're solving?

Do **not** let them start calculating yet.

- What's the actual question? Say it in one sentence.
- Is it "which feed catches more clearings"? Is it "which feed is cheaper"? Is it "which feed
  catches the most clearing per dollar actually spent"? **Those are three different questions**,
  and only the third is the one Marcus's board actually needs answered.
- Someone will say "obviously Commercial Weekly, it catches more." Push: *"More per what — per
  year, or per dollar of the board's budget?"*

> Let the confusion grow. Say it out loud: *"Huh. This is a harder question than it looked."* Do
> not rescue them.

**Socratic Q1.** D5's ratio favors Sentinel Free even though Commercial Weekly detects strictly
more hectares (6.0 vs. 3.0). How can the "worse" detector win the recommendation?

**The trap to let them walk into:** most students will compute D5 using raw hectares detected —
see that Commercial Weekly catches twice as much real clearing — and recommend it without ever
finishing the division by total annual cost. Commercial Weekly's real detection advantage is
genuine and large in absolute terms; it simply doesn't survive being expressed as a cost-adjusted
rate once its $18,330 annual price is counted against Sentinel Free's $7,665.

## Anchor 3 — What is the process?

- What's the process we'll go through to answer it?
- If Commercial Weekly detects twice as much, are we done? Or does "twice as much" mean something
  different once you know what each option costs?
- **Socratic Q2.** Appendix C says Sentinel Free only catches half the reserve's real clearing.
  Where does that missing half go — and does the case ever put a cost on the clearings nobody
  catches?

## Anchor 4 — What don't we know?

- What's missing that we'd need to answer this properly?
- Appendix E gives you the Modeling Assumptions. Do you believe them? MA6 (the share of clearing
  too small for Sentinel Free to catch) is flagged HIGH sensitivity — **have them actually try
  flexing MA6 up and down and see how much the comparison moves.**
- **Socratic Q3.** D3's line of best fit, built from four *other* reserves' actual invoices,
  predicts Commercial Weekly would cost about $18,531 at this reserve's size — Appendix B's own
  planned figure is $15,600. Which number should Marcus trust, and why might they disagree?

---

## Data Deep Dive

Now the numbers. Work these on the board with them.

| | Commercial Weekly (A) | Sentinel Free (B) |
|---|---|---|
| Subscription cost | $15,600 | $0 |
| Analyst labor cost | $2,730 (52 scenes × 1.5 hr × $35) | $7,665 (73 scenes × 3.0 hr × $35) |
| **Total annual cost** | **$18,330** | **$7,665** |
| Hectares detected per year | 6.0 ha (all clearing) | 3.0 ha (half — MA6) |
| **Ratio (ha detected per $)** | **0.0003273** | **0.0003914** |

**margin = |0.0003914 − 0.0003273| / 0.0003914 = 16.4%.** Sentinel Free (Option B) wins, but by
16.4% — comfortably inside the ~20% cap, and **entirely dependent on MA6's 50% figure.** Push the
room: *"If that 50% were actually higher, would the answer change? What about 75%?"* (It flips at
just above 58%.)

**D2's non-linear finding, worth putting on the board too:** Commercial Weekly's 3 m resolution is
only about 3.3× finer than Sentinel Free's 10 m — but its minimum detectable clearing size is
about 11.1× smaller (81 m² vs. 900 m², using the 3×3-pixel minimum-mapping-unit rule). *"Why isn't
'3.3× finer' the same as '3.3× smaller clearings caught'?"* — because minimum detectable area
scales with pixel size *squared*, not pixel size itself.

---

## Twist — drop this at ~15 minutes into the discussion

Deliver it slowly. Let each piece land.

> *"One more report, before the board packet closes."*
>
> (pause)
>
> *"An independent field audit — ground survey teams walking the reserve's boundary by hand —
> just came back. It found that 75% of this year's confirmed clearings were small enough to slip
> under Sentinel Free's detection floor. Not 50%, like the original estimate assumed. The loggers
> doing the smallest, hardest-to-spot cuts favor the cloudiest weeks of the wet season — exactly
> when Sentinel Free's own imagery is most likely to be unusable anyway."*

**Facilitator only — read before you drop this, do not read aloud.** Run
`sensitivity_model.py`'s `evaluate_twist()`: at `f_small=0.75`, Sentinel Free's detected hectares
drop from 3.0 to 1.5, its ratio falls to 0.0001957 ha/$ — **below** Commercial Weekly's unchanged
0.0003273 ha/$. The twist **flips the winner outright** to Commercial Weekly (A), margin 40.22%.
This is a genuine flip, not a near-tie — confirm a room that gets there against the model, not
just the narrative.

Now: **"Sixty seconds. Are you changing your recommendation — or not?"**

## Immediate recommit

- Who is **not** changing? Why?
- Who is reconsidering, even if they're not flipping?
- **What just broke in your original model?**
- **Were you wrong — or were you just missing information?** (Sit on this one.)
- Who built a recommendation that depended entirely on the 50% figure without ever checking how
  firm it was?

---

## Deep conflict — threads (20–30 min)

**Thread 1 — Detects more vs. costs less per hectare.** Commercial Weekly detects twice the
clearing. Sentinel Free still wins the ratio. *"Why doesn't detecting more automatically win?"*

**Thread 2 — Fragility to a single share.** The whole 16.4% margin rides on MA6. Push: *"If the
board asked you how confident you are in that 50% number, what would you say?"*

**Thread 3 — What the invoice sample doesn't quite match.** D3's fitted line predicts $18,531 at
this reserve's size; Appendix B plans for $15,600. *"Is that a red flag, a rounding difference, or
something else — and how would you find out?"*

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. *"Thirty seconds — Commercial Weekly or Sentinel Free?"* Two or three learners, fast. Stand/sit vote, no explanation yet. |
| **3:00–10:00** | Position defense (pre-twist). *"Convince us it's better, not just cheaper (or sharper)."* · *"What's your D5 ratio, exactly?"* |
| **10:00–15:00** | Pressure-test the models. *"What's the single assumption your answer depends on most?"* |
| **15:00** | **DROP THE TWIST.** Slowly, with pauses. Finish with: *"Sixty seconds. Are you changing your recommendation — or not?"* |
| **15:00–20:00** | Immediate recommit. Who reverses? *"What just broke?"* |
| **20:00–30:00** | The three threads: detects-more-vs-cheaper-per-hectare · fragility to the 50% share · the invoice-sample discrepancy. |
| **30:00–45:00** | Close, re-vote, reflection, lessons learned. |

---

## Close

- **Vote again.** Compare to the Anchor 1 board. Who moved?
- We asked ______ as our key question. Was it the right one?
- What math was new to you here, and how did you attack it?
- If you got a case like this again, what would you check first?

**Socratic Q4.** D4 asked you to solve for a redacted month's invoice amount using only the mean
and the other eleven months. Why does that work — what has to be true about a mean for this to be
solvable at all?

**Socratic Q5.** If the board asked Marcus to justify the 50% small-clearing estimate in MA6, what
evidence would actually settle it, and how expensive would gathering that evidence be?

## Lessons Learned

The arithmetic has a clean structure — an option that detects strictly more of the thing you care
about is not automatically the better buy once its cost is counted the same way as its benefit.
Sentinel Free's win (16.4%) is real and it is not a rounding artifact — but it rests almost
entirely on MA6 (the share of clearing too small for Sentinel Free to catch), and it is fragile
enough that a single new piece of field evidence flips it outright, and by a lot (40.2%, not a
near-tie).

The detects-more-vs-costs-less-per-hectare reframing (Anchor 2/3, Data Deep Dive) is the part of
this case that exists to be reused: any time a more-capable, more-expensive option is compared
against a less-capable, cheaper one, the naive "which one catches more" question and the
cost-adjusted "which one catches more per dollar" question can point to different winners — and
only the second one is the real budget-relevant number.

A facilitator running this room should say plainly what the case says: Sentinel Free wins on the
numbers as modeled, that win is real but narrow (16.4%, not the ~2:1 raw-detection gap), and it is
also genuinely fragile to one disclosed assumption (MA6) — all three things are true at once, and
naming all three is stronger than picking one.

---

## Standards Touched On

**Reinforcement case — no new_coverage (see `case.json.reinforcement_note` and
`LEARNING_GOALS.md`):** Non-linear · How to create a box and whisker plot given a set of data ·
How to draw a line of best fit given a set of data · How to find a missing data element given the
mean and the remaining elements of its set · How to convert an amount from one unit to another unit

---

## Cohort bands

- **Full (16–24).** The plan above runs as written; both deep-conflict threads get their own pass
  in the 20:00–30:00 block.
- **Compressed (6–11).** Combine Anchors 2 and 3 into a single "has your number changed your mind"
  pass. Run only the detects-more-vs-costs-less trap thread (Thread 1) — it needs the least setup
  and carries the case's real teaching point. The twist still drops at 15:00. Total runtime
  ~30 minutes.
- **1:1 or pair (1–2).** No vote to take — the learner states an initial position instead of a
  show-of-hands split at Anchor 1. The facilitator argues the opposite side directly instead of
  cold-calling. The twist still lands; the Close's "who reverses" becomes "would you reverse, and
  why," addressed straight to the learner.

## Facilitator note — sensitivity

No SPEC Section 6 subject-matter sensitivity applies. This is a technical budget/resource-
allocation decision with no death, illness, or family-hardship stakes.
