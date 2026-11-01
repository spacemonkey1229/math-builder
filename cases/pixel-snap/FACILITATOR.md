# Guide Notes: Pixel Snap

MS | Guide Notes | Adventure | 2026-27
**Tier:** T2 · **Primary metric:** hectares of falsely-flagged "new clearing" per analyst-hour spent on registration · **Margin:** 15.0% (sensitive — see the sensitivity note before Lessons Learned)

**Do not distribute to students.** This document, and `case.json`'s `balance` object, are the only
places the balance argument, the margin, and the wrong-path analysis below may live. `case.md`
carries only a one-line pointer comment to this file.

---

## Intro

Heroes, today Priya has eleven minutes and two buttons. One button is fast and a little sloppy.
The other is careful and expensive. There's no answer key — I don't know which one is "right"
either, and neither does Priya until the numbers are actually run.

## Launch

Show two overlaid pixel grids, one shifted slightly against the other. Ask: *"If your job was to
tell a truck full of rangers exactly where to drive this morning, would you rather be fast, or
exact?"*

Let them argue it cold, no numbers yet. Then: *"Two months ago, Priya's map sent Bilal's team four
hours down a logging road to chase a clearing that wasn't there. Today she has the same two
choices again."*

> **Hero name — Fast Lock or True Lock? Open for us.**

---

## Anchor 1 — Take a stand and vote

Option A (Fast Lock) or Option B (True Lock). No reasoning yet.

Hands up for A. Hands up for B. Write the split on the board.

*"Is anyone courageous enough to stand with ______?"*

## Anchor 2 — What is the problem we're solving?

Do **not** let them start calculating yet.

- What's the actual question? Say it in one sentence.
- Is it "which method is more accurate"? Is it "which method is faster"? Is it "which method
  produces the fewest false alarms per hour Priya actually spends"? **Those are three different
  questions**, and only the third is the one Priya's board (and Appendix D's fixed monthly-hour
  budget) actually forces her to answer.
- Someone will say "obviously True Lock, it's more accurate." Push: *"More accurate per what? Per
  scene, or per hour of Priya's month?"*
- Is that the right question?

> Let the confusion grow. Say it out loud: *"Huh. This is a harder question than it looked."* Do
> not rescue them.

**Socratic Q1.** Your D5 ratio for Fast Lock comes out far larger than True Lock's. Does that mean
Fast Lock is the worse choice — or does it mean the ratio, computed for one scene alone, is
measuring the wrong thing?

**The trap to let them walk into:** students compute D5's per-scene ratio, see True Lock's number
come out dramatically smaller, and declare True Lock the unconditional right answer — without
noticing the ratio is *per scene*, while True Lock's real cost is *hours taken from a shared,
fixed monthly budget* that covers every other concession Priya monitors. The "obviously correct"
sub-pixel answer looks obvious only because the opportunity cost sitting in Appendix D never
enters the D5 arithmetic unless a student goes looking for it.

## Anchor 3 — What is the process?

- What's the process we'll go through to answer it?
- If Fast Lock's per-scene ratio is dramatically worse, are we done? Or is a per-scene number the
  wrong unit for a decision Priya only gets to make once a month, across five concessions?
- **Socratic Q2.** Appendix D gives Priya a fixed number of analyst-hours to cover every concession
  this month. If she spends the whole morning on Kutai's True Lock, what happens to the other
  concessions' alert maps?
- Is our question still the right question?

## Anchor 4 — What don't we know?

- What's missing that we'd need to answer this properly?
- Appendix E gives you the Modeling Assumptions. Do you believe them? MA3 (True Lock's achieved
  RMSE) and MA4/MA7 (the shared monthly budget and how many concessions draw on it) are both
  flagged HIGH sensitivity — **have them actually try flexing MA7 up and down and see how much the
  comparison moves.**
- **Socratic Q3.** Bilal's team already lost a day chasing a Fast Lock ghost. Does that lost trust
  show up anywhere in your D5 numbers? Should it — and if it should, in what unit would you even
  put it?
- What are we assuming happens to the four concessions that don't get True Lock this month, if
  Priya spends her whole budget on Kutai?

---

## Data Deep Dive

Now the numbers. Work these on the board with them.

**Per-scene, Kutai alone — the naive ratio a student computes straight from case.md:**

| Option | Ribbon area (Kutai) | Analyst-hours | Ratio (ha/analyst-hr) |
|---|---|---|---|
| Fast Lock | 3,200 m × 5 m = 1.6 ha | 1/3 hr (20 min) | **4.8** |
| True Lock | 3,200 m × 3 m = 0.96 ha | 4 hr | **0.24** |

Naive margin: |4.8 − 0.24| / 4.8 ≈ **95%** — wildly outside the ~20% balance cap. **This is the
trap, not the resolved verdict.**

**Whole-month, shared-budget — the resolution.** True Lock's 4 hours on Kutai alone already exceed
Priya's entire 100-minute monthly registration budget (MA4), before any other concession is
touched. Under that choice the other 4 concessions get no registration correction that month and
fall back to Sentinel-2's native, uncorrected accuracy — 12 m (S7), i.e. 3,200 m × 12 m = 3.84 ha
each.

| Policy | Total false-positive area | Total hours | Ratio (ha/analyst-hr) |
|---|---|---|---|
| A — Fast Lock on all 5 concessions | 5 × 1.6 = 8.0 ha | 5 × 1/3 = 1.667 hr | **4.8** |
| B — True Lock on Kutai, other 4 unregistered | 0.96 + 4×3.84 = 16.32 ha | 4 hr | **4.08** |

**margin = |4.8 − 4.08| / 4.8 = 15.0%.** True Lock (Option B) is still favored, but by 15%, not
95% — comfortably inside the ~20% cap.

**Why does the naive number look so different?** Because the naive ratio only ever charges True
Lock's 4 hours against Kutai's own tiny 0.96 ha benefit. The whole-month framing charges those same
4 hours against what the *entire monitored portfolio* loses that month — and once the other four
concessions' fallback accuracy is priced in the same units (hectares per hour), True Lock's
advantage collapses from a 20-to-1 blowout to a real but modest 15% edge.

**Push the room directly:** *"If Priya ran True Lock on every concession every month, what would
have to be true about her total analyst-hour budget for that to still be possible? Is it?"*
(**Socratic Q5**, below.) Nobody should leave this room thinking a per-scene ratio is automatically
the right unit for a shared-budget decision.

---

## Twist — drop this at ~15 minutes into the discussion

Deliver it slowly. Let each piece land.

> *"One more thing about this month's Kutai scene."*
>
> (pause)
>
> *"There's a cloud bank sitting over three of the tile's four quadrants. Usable ground control
> points survive in exactly one quadrant."*
>
> (pause)
>
> *"True Lock can only sub-pixel-correct the quadrant with surviving GCPs. The other three
> quadrants get Fast Lock's whole-pixel treatment this month no matter how many hours Priya
> spends — and nobody has checked yet which quadrant the flagged ribbon is actually in."*

**Facilitator only — read before you drop this, do not read aloud.** D4 places the one surveyed
GCP at (+1,500, −2,200), Quadrant IV — the one clean quadrant this month. If the flagged ribbon
happens to sit in one of the other three (cloud-covered) quadrants, True Lock's advertised RMSE
(MA3, 3 m) simply is not available there this month — the achieved accuracy on that specific
ribbon collapses to the same native/unregistered figure (12 m, S7) the other unregistered
concessions fall back to. Run through `sensitivity_model.py`'s `evaluate_twist()`: with True Lock's
achieved RMSE on Kutai reset to the native 12 m figure, Policy B's ratio rises to exactly Policy
A's (4.8 = 4.8) — the margin collapses to roughly 0%, not a clean flip to Fast Lock. Confirm a room
that gets there against the model, not just the narrative — this twist's real lesson is that
True Lock's whole 15% edge was *entirely* riding on the RMSE gap being available on Kutai itself;
it evaporates, it doesn't reverse.

Now: **"Sixty seconds. Are you changing your recommendation — or not?"**

## Immediate recommit

- Who is **not** changing? Why?
- Who is reconsidering, even if they're not flipping?
- **What just broke in your original model?**
- **Were you wrong — or were you just missing information?** (Sit on this one.)
- Who built a recommendation whose entire edge depended on the GCP quadrant matching the flagged
  ribbon?

---

## Deep conflict — threads (20–30 min)

**Thread 1 — Per-scene vs. whole-month.** The per-scene ratio says True Lock wins by ~95%. The
whole-month ratio says it wins by 15%. Both are real arithmetic on the case's own numbers. *"Which
one should Priya actually put in her monthly report to her board — and why isn't the other one
just as valid?"*

**Thread 2 — Fragility to a single count.** The whole-month margin depends entirely on MA7 (5
concessions sharing the budget). Push: *"If Priya's NGO grew to cover 8 concessions next year with
the same fixed budget, would True Lock still be worth it on Kutai? What if it shrank to 2?"*

**Thread 3 — Trust is not in the ratio.** Bilal's team already burned a day on a Fast Lock ghost.
*"If that lost trust doesn't show up anywhere in the hectares-per-hour number, is the number
actually measuring what matters to Bilal's team? What would you add, and in what unit?"*

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. *"Thirty seconds — Fast Lock or True Lock?"* Two or three learners, fast. Stand/sit vote, no explanation yet. |
| **3:00–10:00** | Position defense (pre-twist). *"Convince us it's better, not just faster."* · *"What's your D5 ratio, exactly?"* |
| **10:00–15:00** | Pressure-test the models. *"Is your ratio per scene, or per Priya's whole month?"* · *"What's the single assumption your answer depends on most?"* |
| **15:00** | **DROP THE TWIST.** Slowly, with pauses. Finish with: *"Sixty seconds. Are you changing your recommendation — or not?"* |
| **15:00–20:00** | Immediate recommit. Who reverses? *"What just broke?"* |
| **20:00–30:00** | The three threads: per-scene vs. whole-month · fragility to the concession count · where trust lives in the numbers. |
| **30:00–45:00** | Close, re-vote, reflection, lessons learned. |

---

## Close

- **Vote again.** Compare to the Anchor 1 board. Who moved?
- We asked ______ as our key question. Was it the right one?
- What math was new to you here, and how did you attack it?
- If you got a case like this again, what would you check first?

**Socratic Q4.** Appendix C caps exactly how far off a whole-pixel shift can be. If that cap turns
out to be small next to the size of a real clearing, does the registration method actually change
what Bilal's team does this month?

**Socratic Q5.** If Priya ran True Lock on every concession every month, what would have to be true
about her total analyst-hour budget for that to still be possible? Is it?

## Lessons Learned

The arithmetic has a clean structure — a ratio computed for one scene and a ratio computed across
a whole shared budget can point to the same winner by wildly different margins, and the only way
to know which margin is real is to actually price the opportunity cost in the same units as the
benefit. True Lock's win (15.0%) is real and it is not a rounding artifact — but it rests almost
entirely on MA4/MA5/MA6/MA7 (the shared monthly budget and how many concessions draw on it) and on
MA3 (True Lock's achieved RMSE), and a plausible retuning of any of them moves the margin a lot,
in one case (a larger concession count) flipping the winner outright. That is a **disclosed, not
eliminated** sensitivity — see `case.json.sensitivity_note` and `sensitivity_model.py`'s probe-5
sweep for the exact numbers.

The per-scene-vs-whole-month reframing (Anchor 2/3, Data Deep Dive) is the part of this case that
exists to be reused: any time a "cheap now" option and an "expensive now" option are being
compared under a shared, exhausted resource budget, the naive single-instance ratio and the
whole-budget ratio can disagree by an order of magnitude, and only the second one is the real
decision-relevant number.

A facilitator running this room should say plainly what the case says: True Lock wins on the
numbers as modeled, that win is real but modest (15%, not 95%), and it is also genuinely fragile to
one specific, disclosed assumption (how many concessions share the budget) and to the twist (which
quadrant the flagged ribbon actually sits in) — all three things are true at once, and naming all
three is stronger than picking one.

---

## Standards Touched On

**Reinforcement case — no new_coverage (see `case.json.reinforcement_note` and
`LEARNING_GOALS.md`):** Congruent · Similar · Quadrant · Transformation · Translation · Dilation ·
Scale Factor · Coordinate Plane · Origin · How to reflect a figure across the Y-Axis · How to
translate a figure on the coordinate plane · How to dilate a figure on the coordinate plane given a
scale factor

---

## Cohort bands

- **Full (16–24).** The plan above runs as written; both deep-conflict threads (per-scene-ratio
  trap, shared-hour-budget reframing) get their own pass in the 20:00–30:00 block.
- **Compressed (6–11).** Combine Anchors 2 and 3 into a single "has your number changed your mind"
  pass. Run only the per-scene-ratio trap thread (Thread 1) — it needs the least setup and carries
  the case's real teaching point. The twist still drops at 15:00. Total runtime ~30 minutes.
- **1:1 or pair (1–2).** No vote to take — the learner states an initial position instead of a
  show-of-hands split at Anchor 1. The facilitator argues the opposite side directly instead of
  cold-calling. The twist still lands; the Close's "who reverses" becomes "would you reverse, and
  why," addressed straight to the learner.

## Facilitator note — sensitivity

No SPEC Section 6 subject-matter sensitivity applies. This is a technical workflow/resource-
allocation decision with no death, illness, or family-hardship stakes.
