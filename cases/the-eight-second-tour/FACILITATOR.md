# Guide Notes: The Eight-Second Tour

MS/HS | Guide Notes | Adventure | 2026-27
**Tier:** T3 (MS-stretch / HS-entry) · **Primary metric:** predicted average speed over the 24.5 km under the scenario model (the 50-second bar is a graded follow-on) · **Margin:** 1.50% (fragile — see the sensitivity note before Lessons Learned)

---

## Intro

Heroes, it is the night before the last stage of the 1989 Tour de France. Your rider is behind. Tomorrow is one ride against the clock, and you are the director who has to decide how he sits on the bike. One position cuts the wind and costs power. The other keeps the power and fights the wind. I do not have the answer either. The numbers are what you will defend it with, and they are less settled than they look.

**Say this once, early, in your own words:** this is a *hindsight scenario*. The director would not have known Fignon's time. We borrow the real 27:55 as a stand-in for the time you would expect your rival to ride. What the director could know is how the two riders had matched up in the Tour's three earlier time trials, so that record (not hindsight equality) sets LeMond's baseline against Fignon. We never say how many seconds the bars gained anyone, and nobody in the case speaks a line they did not really say.

## Launch

Show the photo in Appendix A (LeMond at the start of the stage, Benjamin Werner, CC BY 2.0). Ask: *"Look at how he is sitting. What is that posture buying him, and what do you think it is costing him?"* Let them guess. Then: *"Nobody on his team could measure either one that night."*

> **Hero name — Aero Bars, or Full Power? Commit out loud.**

---

## Anchor 1 — Take a stand and vote

Aero Bars (A) or Full Power (B). No reasoning yet. Hands up for A, hands up for B, write the split on the board.

*"Is anyone courageous enough to stand with Full Power?"* (Expect a lonely minority. Keep it that way for now.)

## Anchor 2 — What is the problem we're solving?

Do **not** let them start calculating.

- What is the actual question, in one sentence?
- Is it "which position is faster"? Is it "which position wins the Tour"? **Those are different questions.** The first is a comparison of two positions. The second asks whether the faster position is fast *enough* to cover a 50-second gap.
- Someone will say "aero is obviously faster, the literature says so above 46 km/h." Push: *"Faster than what, and by how much? Does faster mean the Tour is won?"*
- Is that the right question?

> Let the confusion grow. Say it aloud: *"Huh, 'it is faster' does not obviously mean 'it is enough.'"* Do not rescue them.

**The trap to let them walk into.** Two linked errors. (1) Most Heroes will stop at "the aero position is faster" and never test it against the 50-second requirement from D1-D3 (and never notice the baseline supplies only part of the gap), so they commit to A without noticing how much of the sensitivity range falls short of the target. (2) Many will read the earlier time-trial ratios as clean conventional-position evidence (they are not: stage 5 had triathlon bars for LeMond, distances and terrain differ), and many will read the two 14% figures in the literature as a matched pair, a 14% drag cut paying for a 14% power loss, as if both came from one comparison. They come from different studies measuring different things, and neither compares aero bars with a conventional position. A related slip is subtracting percentages (y no more than x) instead of working with the cubed ratio.

## Anchor 3 — What is the process?

- How do we turn "25 km in 27 minutes" into something comparable with a drag cut and a power loss?
- If we compute a break-even table, what does a row of it tell us, and what does it not tell us?
- If our break-even says the position needs a power loss of no more than a few percent, how do we decide whether to believe it, given that nobody measured it?
- Is our question still the right question?

## Anchor 4 — What don't we know?

- What do we not know? List it: the true drag cut, the true power loss, Fignon's actual time, the wind, the real course, whether the model matches the real world at all.
- Appendix D states the assumptions. Do you believe them? **Have them move x and y inside the stated range and watch the verdict.**
- The case says the model does not reproduce LeMond's real speed. What does that mean for how far we can trust any single number out of it? (This is the opening for the model-limits lesson. Do not tip the twist.)

---

## Data Deep Dive

Now the numbers. Work them on the board.

**Step 1 — times, speeds and the baseline (D1).**

| Time trial | Distance | LeMond | Fignon | Speed ratio LeMond/Fignon |
|---|---|---|---|---|
| Prologue | 7.8 km | 600 s (46.80 km/h) | 600 s (46.80 km/h) | 1.0000 |
| Stage 5 | 73 km | 5892 s (44.60 km/h) | 5948 s (44.18 km/h) | 1.0095 |
| Stage 15 (mountain) | 39 km | 4299 s (32.66 km/h) | 4346 s (32.31 km/h) | 1.0109 |
| Stage 21 | 24.5 km | 1617 s (54.55 km/h) | 1675 s (52.66 km/h) | 1.0359 (not a baseline) |

(Prologue: Breukink 9:54, both +6 s, so 600 s each. Stage 5: 1:38:12 = 5892 s, +56 s = 5948 s. Stage 15: Rooks 1:10:42 = 4242 s, LeMond +57 s = 4299 s, Fignon +1:44 = 4346 s.) **Baseline range for b: 1.0000 to 1.0109.** Stage 5 sits inside it at 1.0095, with the caveat that LeMond used triathlon bars there. Needed finish on stage 21: 1675 − 50 = **1625 s**; the break-even speed is 24,500 / 1625 = 15.08 m/s = 54.28 km/h; **total needed ratio over Fignon = 1675 / 1625 = 1.0308** (+3.1%). The stage 21 ratio (1.0359) is hindsight and includes the aero position, so it is not a baseline.

**Step 2 — the ratio the aero position must supply, and the power factor (D2).** At b = 1.0000 the aero position must supply 1.0308, and 1.0308³ = **1.0952** (+9.5% power at fixed drag). At b = 1.0109 it must supply 1.0308 / 1.0109 = 1.0197, and 1.0197³ = **1.0601** (+6.0%). The baseline alone, even at its best, gains only about 18 s of the 50 s needed (1675 − 1675 / 1.0109), so Full Power cannot reach the bar.

**Step 3 — break-even table (D3).** Aero position reaches the bar when y ≤ 1 − k (1 − x), with k the power factor.

| CdA cut x | Aero-only, b = 1.0000 (k = 1.0952) | Aero-only, b = 1.0109 (k = 1.0601) | Full model, b = 1.0000 |
|---|---|---|---|
| 10% | 1.4% | 4.6% | 1.1% |
| 14% | 5.8% | 8.8% | 5.2% |
| 15% | 6.9% | 9.9% | 6.2% |
| 20% | 12.4% | 15.2% | 11.3% |

The full model needs rolling resistance, which does not shrink when drag area does (Crr × m × g ≈ 3.06 N here), so it is slightly less forgiving. The gap between the two models is the model-limits lesson, and it is small beside the uncertainty in x, y and b. The full model's baseline is Fignon's speed (52.66 km/h) times b.

**Step 4 — the chart, the line and the shares (D4).** Cube-law points are exactly collinear: for b = 1.0000, y = 1.0952 x − 0.0952; **slope = 1.0952**, the same number as the b = 1.0000 power factor. Meaning: each extra percentage point of drag cut buys about 1.1 points of tolerable power loss, and the line crosses y = 0 at x ≈ 8.7%. For b = 1.0109 the slope is 1.0601 and the line is shifted up by about 3 points of y. Share of the Appendix D box (x 10-15%, y 3-14%) on the winning side: **about 13% at b = 1.0000 and about 39% at b = 1.0109** under the cube law (about 9% and 33% under the full model); at stage 5's 1.0095 about 35%. These shares are illustrative areas of the box, not probabilities: nobody has put a probability on x or y. Corner checks (model-predicted, scenario terms only, relative to Fignon's 27:55 at b = 1): x 15%, y 3%: about 72 s faster; x 10%, y 3%: about 41 s; x 15%, y 14%: about 6.5 s; x 10%, y 14%: about 26 s *slower* than the conventional position. The aero position is faster than conventional in about 85% of the box.

**Decision rules (D4).** A's outcome relative to B ranges from about 26 s slower to about 72 s faster. *Best expected result* or *minimax regret* (A's worst regret about 26 s, B's about 72 s) favours A; *best worst case* (maximin) favours B. Both are legitimate; the room should name its rule.

**Step 5 — model limits (D5).** Full model at 15.15 m/s: aero 0.5 × 1.225 × 0.32 × 15.15³ ≈ 682 W, rolling ≈ 46 W, **total ≈ 728 W**. Whether a rider could hold that for about 27 minutes is the Hero's judgment to defend with a reference they find and cite; the case supplies none. Either way the model does not reproduce the real speed from believable inputs, which is why the case uses ratios only and never claims LeMond produced those watts.

---

## Twist — drop this at ~15 minutes into the discussion

Deliver it slowly. Let each piece land.

> *"Your team physiologist comes in with a number."*
>
> (pause)
>
> *"A lab estimate for the aero position. Not a measurement from the race. A hypothetical, built for tonight."*
>
> (pause)
>
> *"Drag area down by twelve and a half percent. Sustainable power down by fourteen."*
>
> (pause)
>
> *"Both numbers are inside the ranges in your own Appendix D. Treat them as the only estimate of the aero position you have tonight: they replace your own x and y. Run it again. Sixty seconds. Are you changing your recommendation, or not?"*

Say both numbers aloud and say it is invented for the exercise. Do **not** let a room argue that the 12.5% could be revised: the twist supplies **both** x and y, and, because both are supplied and replace the student's own, no reading of the case's assumptions leaves the verdict unchanged. `sensitivity_model.py`'s `evaluate_twist()` runs it: with x = 12.5% and y = 14%, the aero position is slower than the conventional position (speed ratio about 0.994). **Facilitator only — do not read aloud:** before the twist, at the midpoints x = 12.5% and y = 8.5%, A leads by about 1.50% in speed; after it, B leads by about 0.58% (the baseline b cancels in this comparison). The winner flips, but nobody has been given a measurement of LeMond. Be clear that the twist is not a fact about 1989.

## Immediate recommit

- Who is **not** changing? Why?
- Who is reconsidering? (Probe the student who keeps A: *"B already loses by 50 s. With these numbers, does A have any path to winning?"*)
- **What just broke in your original model?**
- **Were you wrong, or just missing information?** (Sit on this one.)
- Who built their case on "the literature says aero is faster above 46 km/h" without checking what the literature actually compared?

---

## Deep conflict — threads (20–30 min)

**Thread 1 — Faster versus fast enough.** Option A is faster in most of the range, yet only part of the range reaches 50 s, and how much depends on the baseline b. *"If neither position is certain to win the Tour, what is the director actually choosing?"* Push toward risk: A has more upside and a real downside; B is the known quantity, but even at the best observed baseline it gains only about 18 s of the 50 s.

**Thread 2 — How much can you trust a model that gets the speed wrong?** The parameters imply a power that Heroes may doubt. *"Which of our numbers is a ratio that survives that error, and which is a watt count that does not?"* Push toward why the case uses ratios only.

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. *"Thirty seconds: bars or no bars?"* Two or three learners, fast. Stand/sit vote, no explanation yet. |
| **3:00–10:00** | Position defense (pre-twist). *"Convince us it is better, not just faster."* · *"What is your break-even number, not a guess?"* |
| **10:00–15:00** | Pressure-test the models. *"Which of x and y are you least sure of?"* · *"Which side of your own break-even line is your chosen point on?"* |
| **15:00** | **DROP THE TWIST.** Slowly, with pauses. Finish with: *"Sixty seconds. Are you changing your recommendation, or not?"* |
| **15:00–20:00** | Immediate recommit. Who reverses? *"What just broke?"* |
| **20:00–30:00** | The two threads: faster versus fast enough · trusting a model that gets the speed wrong. |
| **30:00–45:00** | Close, re-vote, reflection, lessons learned. |

---

## The balance — both arguments

**Argument for A (Aero Bars).** At race speed the aero position starts ahead: at a 54.5 km/h average the peer-reviewed model says aerodynamic losses outweigh power losses (crossover 46 km/h), and the cube law makes each point of drag cut worth about 1.1 points of power. A is faster than conventional in about 85% of the Appendix D box, about 1.5% faster at its midpoints, and about 1.5% faster averaged over the box. And only A can reach the 50-second bar at all: the earlier-time-trial baseline alone gains at most about 18 s on Fignon.

**Argument for B (Full Power).** It is the known quantity. The aero position's power loss is not measured anywhere in the literature this case cites, it is untested for this rider on the eve of the stage, and the aero position is slower than conventional wherever y exceeds roughly x (about 15% of the box; worst case about 26 s slower). Under a best-worst-case rule B wins. To cover 50 s the aero position must stay within roughly 1-10% power loss for a 10-15% drag cut (depending on b) while the stated range runs to 14%. Neither study compares aero bars with a conventional position, and the two 14% figures are not a matched pair.

**Honest weakness of B (state it to the room).** Even at the best observed baseline B gains only about 18 s of the 50 s. B's case is a risk-and-evidence case (it avoids the downside corner and the unmeasured dial), not a case that B reaches the target. The balance is carried by the choice of decision rule, not by B's arithmetic being competitive in most of the box. A room that sees this should say so.

**The margin.** On the primary metric (predicted speed at x = 12.5%, y = 8.5%, the midpoints of the Appendix D ranges) A leads B by **1.50%** (53.74 vs 52.94 km/h at the midpoint baseline b = 1.0055), comfortably inside the 20% cap. It is genuinely fragile: halving x (to 6.25%) or raising y by half (to 12.75%) flips the winner, as does the twist.

## Five Socratic questions

1. Your break-even table at b = 1.0000 says a 14% drag cut tolerates a power loss of about 5.8%. The literature's drag figure is also 14%. Why is it wrong to conclude the aero position must therefore be good enough?
2. D2 says power must rise about 9.5% at b = 1.0000 and about 6.0% at b = 1.0109. Which of the two baselines would you defend in front of the board, given that stage 5 involved triathlon bars?
3. Your chosen point sits inside the Appendix D box. How far would y have to rise before your chosen drag cut stops paying for it, and which dial would you most want a wind tunnel or a lab to measure?
4. The full model is stricter than the cube law at every x. If you had to commit before the ride, which column's tolerances would you trust, and why does the difference between the columns matter less than the uncertainty in y and in b?
5. Appendix B's parameters imply a power for LeMond's real 26:57 that you evaluated in D5. If that figure is unbelievable, which of your other numbers still stand, and which should you stop trusting?

6. Which decision rule did you use (best expected result, minimax regret, best worst case)? Change the rule: does your choice change?

## Close

- **Vote again.** Compare to the Anchor 1 board. Who moved?
- We asked ______ as our key question. Was it the right one?
- What math was new to you here, and how did you attack it?
- If you faced a call like this again, which single number would you try to measure first?

## Lessons Learned

The arithmetic has a clean structure: a ratio of two times becomes a ratio of speeds, the cube law turns that into a power factor, and a straight line (slope 1.0952) says how much power loss a given drag cut can pay for. That structure is the transferable skill. The deeper lesson is that the two options are close because the key dials are unmeasured, not because the math is vague: the verdict flips inside the stated ranges and under the twist. That is a **disclosed, not eliminated** sensitivity (`case.json.sensitivity_disclosure[]` records each dial). The honest finish is to say both things at once: the literature leans aero at race speed, and how much power loss the position tolerates is exactly what nobody measured.

---

## Real-World Basis

- Stage 21 facts (date, distance, 26:57, 27:55, the 50 s deficit, the 8 s margin, equipment, 54.545 km/h): Wikipedia, *1989 Tour de France* (secondary; ProCyclingStats is not openly licensed).
- Earlier time trials (prologue, stage 5, stage 15; results and the stage 5 triathlon-bars sentence): Wikipedia, *1989 Tour de France, Prologue to Stage 10* and *Stage 11 to Stage 21* (secondary), read from raw wikitext. Revision note: the first draft assumed exactly equal conventional speeds (hindsight), which left Full Power with no route to the bar by construction (Tier 2 P2); the baseline is now this record.
- García-López et al. 2008, J Sports Sci 26(3):277-286 (PubMed 17943597): position changes decreased aerodynamic drag by 14% in five professionals, wind tunnel. Its abstract does report a standard racing bike among the positions tested for drag, but no power loss and no aero-bars-versus-conventional power comparison.
- Fintelman et al. 2014, J Biomech 47(8):1894-8 (PubMed 24726654): aerodynamic losses outweigh power losses above 46 km/h; below 30 km/h a more upright position is better. A "peak power fell about 14%" figure is **not** in the abstract and is not used anywhere in this case; the 14% upper end of y is this case's own assumption.
- Popular "15-25%" drag-reduction figures are not peer reviewed and are not used.
- Fignon's physical condition on the day, and details such as saddle sores, are contested and kept out of the math.

## Standards Touched On

**Time · Percent · Ratio · Exponent (also Power) · Variable · Equation · Scatter Plot · How to convert between units of time · How to add and subtract time · How to convert an amount with compound units · How to evaluate an exponential expression · How to convert numbers to percents · How to convert percents to numbers · How to evaluate a variable expression (Substitution Property) · How to solve a multi-step equation with a variable on one side · How to create a scatter plot given a set of data · How to identify the slope of a line given a set of data, or a graph of a line of a set of data, or its linear equation · How to write a linear equation given a set of data.**

See `LEARNING_GOALS.md` for the forces-test and `case.json.reinforcement_note` for why `new_coverage[]` is honestly empty.

---

## Facilitator note — sensitivity

No SPEC Section 6 subject-matter sensitivity applies (no death, illness or family hardship). One subject-matter care: the real riders are real people, so keep to the sourced record, invent no quotes, and treat any account of Fignon's condition as contested.
