# Guide Notes: FlowState

MS | Guide Notes | Launchpad | 2026-27
**Tier:** T4 (HS) · **Primary metric:** projected paying subscribers within the fixed $60,000 launch budget · **Margin:** 15.1% (sensitive -- see the sensitivity note before Lessons Learned)

---

## Intro

Heroes, today Priya has one job: turn a fixed pile of money into paying customers before a deadline that isn't moving. Two plans, one budget, one submission. There's no answer key — I don't have the "right" plan either, and neither does Priya's board until they see your math.

## Launch

Show a photo of a smart water bottle with a phone paired to it. Ask: *"If you had $60,000 to launch this and get people to actually pay for a subscription, would you rather be everywhere, or be in front of exactly the right people?"*

Let them argue it cold, no numbers yet. Then: *"Priya has two folders in her car right now. Same $60,000. Completely different bets."*

> **Hero name — which folder do you open first? Open for us.**

---

## Anchor 1 — Take a stand and vote

Plan A (Broadcast Blitz) or Plan B (Precision Funnel). No reasoning yet.

Hands up for A. Hands up for B. Write the split on the board.

*"Is anyone courageous enough to stand with ______?"*

## Anchor 2 — What is the problem we're solving?

Do **not** let them start calculating yet.

- What's the actual question? Say it in one sentence.
- Is it "which plan reaches the most people"? Is it "which plan is cheapest per person reached"? Is it "which plan gets the most people to actually *pay*"? **Those are three different questions with three different answers**, and only one of them is what Priya's board actually cares about.
- Someone will say "go with whichever reaches more people." Push: *"Reached, or paying? Priya's board doesn't see a reach number on the slide."*
- Is that the right question?

> Let the confusion grow. Say it out loud: *"Huh. This is a harder question than it looked."* Do not rescue them.

**The trap to let them walk into:** Plan A reaches dramatically more people — millions of impressions versus a few thousand search clicks and a few hundred thousand magazine readers. Most learners will assume "more reach obviously wins" and stop there. The real trap is the funnel: SEO's conversion rate (6.8%, a real number) is nearly six times higher than every broadcast/print channel's conversion rate (1.17%) at the exact stage where a visitor actually signs up. A learner who compares raw reach numbers without running the whole chain down to *paying subscribers* will misjudge which plan is actually ahead — and it's closer than either raw-reach instinct suggests.

## Anchor 3 — What is the process?

- What's the process we'll go through to answer it?
- If we just count total people exposed, are we done? Is exposure the same thing as a customer?
- If we end up with roughly 330 of one thing and roughly 287 of another, how do we decide it's close enough to be a real discussion, versus one plan just winning? What's our tiebreaker *before* we see the numbers?
- Is our question still the right question?

## Anchor 4 — What don't we know?

- What's missing that we'd need to answer this properly?
- Appendix E gives you the assumptions. Do you believe them? The TV CPM figures (Appendix A) are picked from a real range — **have them actually try the range's low and high ends and see how much the comparison moves.**
- Appendix D doesn't give you an awareness or interest rate for the print/magazine channel. What would you assume, and why? (This is the case's built-in T4 "you must assume this yourself" moment — don't hand them a number.)
- What are we assuming about whether the two segments (student athletes vs. working professionals) are equally valuable to Solstice Labs long-term, beyond just their trial-to-paid rate?

---

## Data Deep Dive

Now the numbers. Work these on the board with them.

**The funnel, per channel, per segment.** Every channel's contribution is reach × segment share × awareness × interest × trial-conversion × adoption, chained. This is where "more reach" quietly loses to "better conversion" for some channels and not others.

| Channel | Plan A $ | Plan A subscribers | Plan B $ | Plan B subscribers |
|---|---|---|---|---|
| TV — Sports/Fitness | $18,000 | 137.24 | $6,000 | 45.75 |
| TV — General | $18,000 | 72.80 | $6,000 | 24.27 |
| Radio | $12,000 | 64.63 | $6,000 | 32.31 |
| SEO / paid search | $8,000 | 48.64 | $26,000 | 158.09 |
| Print / magazine | $4,000 | 6.52 | $16,000 | 26.08 |
| **Total** | **$60,000** | **329.83** | **$60,000** | **286.50** |

*(TV — General uses MA3's revised $30.00 CPM, retuned 2026-09-11 from $24.00 after a tighter, broadcast-specific real source was found — see case.json's `sources[S14]` and Appendix E. Print row above uses the case's own reference assumption of 15% awareness / 12% interest for the print channel — the same order of magnitude as radio — for calibration only; a student's own justified value will differ and that's fine, as long as it's justified.)*

**Plan A wins by 15.1%** — comfortably inside the 20% balance cap. Cost per acquisition: Plan A ≈ **$181.92**/subscriber, Plan B ≈ **$209.42**/subscriber.

**Why does Plan A still win, when SEO converts so much better?** Because SEO and print together are only $12,000 of Plan A's budget but $42,000 of Plan B's — Plan B is betting almost its entire budget on the two channels with the smallest raw reach, and even a 6.8% conversion rate can't fully make up for the sheer volume gap when TV/radio still get 20–30% of Plan B's dollars too. Push the room on this directly: *"If SEO is so much better per dollar, why doesn't Plan B just put everything into SEO?"* (Answer, if nobody gets there: there's presumably a ceiling on how much SEO volume $26,000 in a single category can actually buy before returns fall off — the case doesn't model that ceiling, which is itself worth naming as a limitation.)

**The system of equations (D4).** Group the five channels into a broadcast-leaning bucket (TV×2 + radio) and a precision-leaning bucket (SEO + print). Using Plan A's own broadcast-bucket mix and Plan B's own precision-bucket mix, the per-dollar subscriber yields work out to:

- Broadcast bucket: ≈ **0.005722 subscribers per dollar**
- Precision bucket: ≈ **0.004385 subscribers per dollar**

Set up: *x* + *y* = 60,000 and 0.005722*x* + 0.004385*y* = (Plan B's total, 286.50). Solving: **x ≈ $17,498 broadcast, y ≈ $42,502 precision** — a blended plan at that split would tie Plan B exactly. Plan A's actual split is $48,000 / $12,000, so **moving roughly $30,502 from the broadcast bucket into the precision bucket** would erase Plan A's entire advantage down to a tie with Plan B's fixed total. That is a real, computable number — a facilitator should let a room that gets there confirm it against the table above, not just take the algebra on faith. (Both bucket yields shifted slightly from earlier drafts of this case because MA3's TV-General CPM was retuned from $24.00 to $30.00 on 2026-09-11 after a tighter, broadcast-specific real source was found — see RESEARCH_LOG.md.)

---

## Twist — drop this at ~15 minutes into the discussion

Deliver it slowly. Let each piece land.

> *"It's the week of the trade show."*
>
> (pause)
>
> *"Priya's media buyer calls. Both TV packages — sports and general — just quoted new rates. Turns out trade-show week this year lands right on top of the conference championships. Every network is raising ad rates for the live-sports inventory around it, cable and broadcast both."*
>
> (pause)
>
> *"The new quote: both TV CPMs are roughly 50% higher than what the plan was built on."*

**Facilitator only — read before you drop this, do not read aloud.** At a +50% CPM premium on both TV packages, Plan A's total falls to about 259.82 and Plan B's falls only slightly to about 263.16 — Plan B **pulls ahead**, by about **1.3%**. (This is a change from an earlier draft of this case, where the same +50% premium only narrowed the margin to 1.8% without flipping the winner; MA3's TV-General CPM was retuned from $24.00 to $30.00 on 2026-09-11 after a tighter, broadcast-specific real source was found, which raised Plan A's exposure to exactly this swing — the crossover point itself moved from roughly +57% to roughly +44.8% CPM premium.) Confirm a room that gets there against the numbers above, not just the algebra — this is one of the few twists in the corpus where the disclosed scenario premium (+50%) sits *past* the actual crossover point (+44.8%), so the flip is real, not borderline. Do not let a room believe the twist flipped the result without actually recomputing it, but also do not undersell it — at the disclosed premium, it genuinely does flip.

Now: **"Sixty seconds. Are you changing your plan — or not?"**

## Immediate recommit

- Who is **not** changing? Why?
- Who is reconsidering, even if they're not flipping?
- **What just broke in your original model?**
- **Were you wrong — or were you just missing information?** (Sit on this one.)
- Who built a plan whose entire advantage depended on TV pricing holding steady?

---

## Deep conflict — threads (20–30 min)

**Thread 1 — Reach vs. intent.** Plan A reaches vastly more people and still wins on paying subscribers. Plan B reaches far fewer people but converts a much larger share of who it does reach. *"If SEO converts six times better, why doesn't it win outright?"* Push toward: volume still matters when the gap in raw reach is this large — a high conversion rate on a small audience can still lose to mediocre conversion on a huge one.

**Thread 2 — Fragility to a single number.** Plan A's entire advantage rides on two Modeling Assumptions (MA2, MA3 — the TV CPM point-values) picked from real sourced ranges. A plausible seasonal swing doesn't just erase the whole margin — at the disclosed +50% premium, it flips the winner to Plan B. Plan B barely notices the same swing. *"Which plan would you pick if you had to defend it to a board that might ask 'what if TV pricing moves against us?'"*

**Thread 3 — Who actually is Solstice Labs' customer?** Segment 1 (student athletes) converts trial-to-paid at a real 35.8%; Segment 2 (working professionals) converts at a real 52.0%. Plan A's biggest channel (TV Sports/Fitness) skews 65% toward the *lower*-converting segment. Plan B's biggest channel (SEO) is close to an even split. *"Is Plan A quietly betting on the segment that's structurally less likely to keep paying?"*

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. *"Thirty seconds — Plan A or Plan B?"* Two or three learners, fast. Stand/sit vote, no explanation yet. |
| **3:00–10:00** | Position defense (pre-twist). *"Convince us it's better, not just louder."* · *"How many people does your plan actually reach?"* Then press: *"Say the actual subscriber number, not the reach number."* |
| **10:00–15:00** | Pressure-test the models. *"Which plan is more fragile to one wrong assumption?"* · *"What's the single number your plan depends on most?"* |
| **15:00** | **DROP THE TWIST.** Slowly, with pauses. Finish with: *"Sixty seconds. Are you changing your plan — or not?"* |
| **15:00–20:00** | Immediate recommit. Who reverses? *"What just broke?"* |
| **20:00–30:00** | The three threads: reach vs. intent · fragility to a single number · which segment are we really betting on. |
| **30:00–45:00** | Close, re-vote, reflection, lessons learned. |

---

## Close

- **Vote again.** Compare to the Anchor 1 board. Who moved?
- We asked ______ as our key question. Was it the right one?
- What math was new to you here, and how did you attack it?
- If you got a case like this again, what would you check first?

## Lessons Learned

The arithmetic has a clean structure — chain enough percentages together and a bigger number eventually loses to a smaller, faster-converting one, or it doesn't, and the only way to know which is to actually run the chain all the way to the end. Plan A's win (15.1%) is real and it is not a rounding artifact — but it rests almost entirely on two Modeling Assumptions (the TV CPM point-values, MA2/MA3) picked from real, sourced ranges, and a plausible real-world swing (a seasonal ad-rate premium) doesn't just erode it — at the disclosed +50% premium, it flips the winner outright. That is a **disclosed, not eliminated** sensitivity: `case.json.sensitivity_disclosure[]` carries a Category-B entry for exactly this reason — this is a real, quantifiable exposure to values chosen within sourced ranges, unlike the segment-skew and awareness/interest assumptions (Category F), which are irreducible forecasts for a product and campaign that do not exist yet and cannot be tightened by more research.

The system-of-equations deliverable (D4) is the part of this case that exists to be reused: almost any two-plan, fixed-total-budget decision can be reduced to "x dollars in bucket 1, y dollars in bucket 2, x + y = budget, plus a linear yield-per-dollar for each bucket" — solving that system is a transferable move, not a one-off trick for this case.

A facilitator running this room should say plainly what the case says: Plan A wins on the numbers as modeled, that win is real, and it is also genuinely fragile to one specific, disclosed pair of assumptions — both things are true at once, and naming both is stronger than picking one.

---

## Standards Touched On

**Also exercised (no true new_coverage -- every spine skill already has a covering case, see LEARNING_GOALS.md):** Percent · Ratio · Proportion · Mean · System Of Equations · Slope · X-Intercept · How to find the percent of a number · How to convert numbers to percents · How to find a missing amount in a proportion · How to find the mean of a set of data · How to solve a system of linear equations · How to write a linear equation given a set of data

---

## Facilitator note — sensitivity

No SPEC Section 6 subject-matter sensitivity applies. This is a business/marketing resource-allocation decision with no death, illness, or family-hardship stakes.
