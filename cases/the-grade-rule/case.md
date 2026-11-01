# Case Study: Grade Rule

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

Devon Okafor has the base-size pattern pinned flat on the light table and a factory deadline in three hours. Somewhere in the building, someone is already pulling fabric for the first cut of the new size run, and the grade rule — the set of instructions that turns one pattern into eight — has to be in their inbox before that fabric touches a blade.

Every size in a run grows from the same base pattern, but bodies don't grow the same way at every point. A bust measurement climbs faster from size to size than a waist does, and a waist climbs faster than a shoulder. Scale the whole pattern up by one tidy percentage per size, and the math is fast, clean, and finished in an afternoon — but the pattern quietly stops matching real bodies the further a size sits from the middle of the run. Grade each point on the pattern by its own real, measured increment, and every size fits the way it should — but each of those separate increments has to be found and applied by hand, size by size, point by point.

Devon's name goes on the tech pack. If a size doesn't fit and that size sells, the return rate lands on this decision.

Devon uncaps a red pen and pulls the size chart closer.

---

## Background

Devon Okafor is a pattern grader at a mid-size apparel company, responsible for turning the company's one approved base-size pattern into the full run of sizes the factory will cut this season. The grade rule Devon signs off on ships to the factory this week, and Devon's name is the one attached to it if a size in the run doesn't fit.

Two grading methods are on the table:

**Uniform Dilation** — scale every point on the base pattern by one single scale factor per size step, the same factor applied everywhere on the pattern, computed once and reused for the whole run. Fast to compute, cheap to produce, and mathematically a true dilation: every graded size is a perfect scaled copy of the base size.

**Point-Specific Grading** — grade each landmark point on the pattern (bust point, waist point, hip point) by its own real, individually-measured increment, matching how an actual body's proportions change from size to size rather than scaling everything by the same amount. More accurate to real bodies, but every point at every size step needs its own calculation instead of one shared multiplication.

A real, published body-measurement standard exists for exactly this purpose — a size chart that reports precisely how much bust, waist, and hip measurements actually change from one size to the next across a graded run (SEE APPENDIX A). Because real bodies do not grow at the same rate everywhere, that real growth rate is not identical at every landmark, and a single dilation factor tuned to fit the whole run reasonably well will still miss some landmarks at some sizes by more than the factory's stated fit tolerance (SEE APPENDIX B). A size Devon ships that misses tolerance at even one landmark is a size that does not reliably fit.

Both methods take real grading-room time, billed at the same hourly rate regardless of which method is used (SEE APPENDIX C). None of the figures in this case are invented outright; every one is either cited to a real, live source or stated openly as a scenario assumption, with the basis for each assumption disclosed in **APPENDIX D**.

The vocabulary and "how to…" skills this case will ask you to research are listed in **APPENDIX E** — that is where Challenge 1 sends you. Every sourced figure and stated assumption in this case is documented in **APPENDIX F**. If any real-world term in this case (not the math vocabulary) is unfamiliar, **APPENDIX G** explains it in plain English.

Devon pulls the size chart closer.

---

## Dilemma

You are Devon Okafor.

Do you:

**A.)** Grade the run by Uniform Dilation — one scale factor per size step, applied everywhere on the pattern **OR**

**B.)** Grade the run by Point-Specific Grading — each landmark point graded by its own real, individually-measured increment

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A point-specific scale-factor table.** Using Appendix A's published size-run data, find the real scale factor (new measurement ÷ old measurement) between each pair of consecutive sizes, separately at each of the three landmarks. This table of individually-derived, point-specific scale factors is exactly what Point-Specific Grading uses — a different scale factor at every landmark, not one shared number.
- **D2 — A dilation scale-factor derivation.** Using Appendix A's base-size and largest/smallest-size measurements across all three landmarks, derive the single per-size-step scale factor Uniform Dilation would use, showing your work.
- **D3 — A dilated-pattern prediction table.** Apply D2's scale factor to the base size's bust, waist, and hip measurements to predict Uniform Dilation's version of every other size in the run. For each predicted point, state whether the dilated pattern is a truly similar, congruent-by-tolerance copy of the real body at that size, or not.
- **D4 — A fit-check table.** Compare D3's predicted measurements against D1's real measurements at every size and landmark, compute the absolute difference, and mark each one within or outside Appendix B's stated fit tolerance. For each size, state whether it fully fits (every landmark within tolerance) or not.
- **D5 — A cost, coverage, and decision memo.** Using Appendix C's labor-time and wage figures, compute each option's total grading labor cost for the run. Using D4 (for Option A) and the fact that Point-Specific Grading always matches the real data exactly (for Option B), compute how many of the run's five sizes each option delivers fully within tolerance. Compute each option's dollars of labor per fully-fitting size, convert the final grade-rule table to centimeters for the overseas factory, state your recommendation, and show the arithmetic.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A — Real Body-Measurement Data by Size

The table below is drawn directly from a real published U.S. standard for adult female body measurements, ASTM D5585-11e1 [S1]. Devon's company's size run covers sizes 8 through 16; the base size this pattern is built from is size 12.

| Size | Bust (in) | Waist (in) | Hip (in) |
|---|---|---|---|
| 8 | 36.25 | 29.5 | 38.5 |
| 10 | 37.25 | 30.5 | 39.5 |
| **12 (base)** | **38.75** | **32.25** | **41.0** |
| 14 | 40.375 | 34.0 | 42.5 |
| 16 | 42.125 | 36.0 | 44.25 |

*Notice that the change from size to size is not the same at every landmark, and is not even constant across the run at a single landmark — the waist, for instance, grows by 1.0 in from size 8 to size 10, but by 2.0 in from size 14 to size 16. Challenge D1 asks you to find the real, point-specific scale factor (new ÷ old) at every landmark and every step directly from this table — a different number at every point, exactly what Point-Specific Grading is. Challenge D2 asks you to derive a single shared scale factor from this same table instead; Challenge D3 and D4 ask you to test whether that one shared factor can actually reproduce every number in this table.*

---

## Appendix B — Fit Tolerance

A graded pattern is considered a reliable fit at a given landmark if it falls within a stated tolerance band of the real body measurement at that size — a standard concept in garment fit engineering, where some ease and rounding is always acceptable but a pattern that misses by too much will visibly not fit.

| Quantity | Value |
|---|---|
| Stated fit tolerance, each landmark | ±0.5 in [MA1] |

*Challenge D4 asks you to apply this tolerance to every predicted measurement in D3.*

---

## Appendix C — Grading Labor

| Quantity | Value |
|---|---|
| Median hourly wage, Fabric and Apparel Patternmakers (U.S.) | $30.05/hr [S2] |
| Uniform Dilation: one-time setup time to compute the single scale factor | 3.0 min [MA2] |
| Uniform Dilation: time to apply the scale factor at one landmark, one size | 0.4 min/point [MA2] |
| Point-Specific Grading: time to derive and apply one landmark's real increment, one size | 1.2 min/point [MA2] |
| Point-grades required per option (4 non-base sizes × 3 landmarks) | 12 |

*No public source publishes a per-point grading time for a specific pattern and company — this is an internal production-floor rate, not something any trade body tracks. Point-Specific Grading's per-point time is set at exactly three times Uniform Dilation's, reflecting that each point's real increment has to be individually derived and verified rather than produced by one shared multiplication (see MA2, Appendix D).*

---

## Appendix D — Modeling Assumptions

> These figures are **not sourced** as direct external citations. They are stated scenario assumptions, each grounded in a real basis described below. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Stated fit tolerance at each landmark | ±0.5 in | No single trade-body figure exists for "acceptable grading fit tolerance" specific to Devon's company or this exact garment — real patternmaking references commonly treat a fraction of an inch as workable ease at a single body point, and this case fixes one stated, disclosed value in that range rather than presenting a specific factory's internal standard as universal. | **This is the single most dilemma-relevant assumption in the case.** It is the exact line Challenge D4's fit check is measured against; a tighter tolerance fails more sizes, a looser one fails fewer. |
| MA2 | Per-point grading time, each method | Uniform Dilation 3.0 min setup + 0.4 min/point; Point-Specific 1.2 min/point | No trade body publishes a per-point grading-floor time; this is an internal production rate. The 3:1 per-point ratio reflects that Point-Specific Grading looks up and verifies each point's own real increment individually, while Uniform Dilation reuses one already-computed factor. | Both options' total labor cost scale directly with these rates; a smaller time gap between the two methods shrinks Option B's labor-cost disadvantage, a larger gap widens it. |

*No other figure in this case required a Modeling Assumption — see `RESEARCH_LOG.md` for the full source-by-source trail.*

---

## Appendix E — "How To…" Math Questions To Research

**Vocabulary terms**

- Dilation
- Scale Factor
- Similar
- Congruent

**"How to…" questions**

- How to dilate a figure on the coordinate plane given a scale factor
- How to find the scale factor of a dilation
- How to convert an amount from one unit to another unit

---

## Appendix F — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Real published U.S. standard body measurements for adult females, by numeric size, bust/waist/hip | See Appendix A table | ASTM International, *Standard Tables of Body Measurements for Adult Female Misses Figure Type* (ASTM D5585-11e1), as reproduced in Wikipedia's ["U.S. standard clothing size"](https://en.wikipedia.org/wiki/U.S._standard_clothing_size) | standard: 2011; accessed 2026-09-18 | HIGH |
| S2 | Median hourly wage, Fabric and Apparel Patternmakers (SOC 51-6092) | $30.05/hr | U.S. Bureau of Labor Statistics, OEWS, ["Fabric and Apparel Patternmakers"](https://www.bls.gov/oes/2023/may/oes516092.htm) | May 2023, accessed 2026-09-18 | HIGH |

*Modeling Assumptions MA1–MA2 are documented in Appendix D, not repeated here. Full search trail, rejected sources, and derivation arithmetic: `RESEARCH_LOG.md`.*

---

## Appendix G — Plain-English Notes on Real-World Terms

This appendix explains real-world (non-math) terms and mechanisms used elsewhere in the case, for anyone unfamiliar with pattern grading. It does not affect any Challenge.

**From a body measurement to a moved point — this case's own stated simplification.** Appendix A gives *body circumference* measurements (bust/waist/hip, all the way around the body). A real pattern piece is flat and only covers half the body (the other half is a mirror image, sewn together at the side seams), so a real patternmaker's first step is always the same: divide the body circumference in half (plus a small fixed ease allowance) to get the flat pattern's width at that landmark. This case treats that halving step as a constant, unstated background conversion applied identically under both options — what genuinely differs between Uniform Dilation and Point-Specific Grading is only the *scale factor* applied to that already-halved pattern width, not the halving itself. So "move this landmark point by X inches" always means "shift it by X inches in the single, already-known direction that widens or narrows the flat pattern at that landmark" — never a two-directional (x-and-y) repositioning. A real production grade rule can specify true two-directional point movement (letting a pattern's shape subtly change, not just its overall width), which this case's math does not attempt; this case is deliberately scoped to the width-only version of the problem.

**Picturing the grade rule, and exactly what Devon ships.** A grade rule is not a machine or a single physical object — it is a table, exactly like the tables you build in Challenges D1–D3: one row per landmark point, one column per size, and each cell holding a distance (in inches or centimeters) telling a cutter or a grading machine exactly how far to move that one point from the base pattern to produce that size's version of the pattern. **The table of numbers is the entire deliverable that goes in the factory's inbox.** Devon does not personally redraw eight full patterns by hand — Devon builds and checks the numeric table, sends that table, and the factory's own graders or grading software do the actual re-plotting downstream: taking the base pattern, moving every landmark point by the distance the table specifies for that size, and redrawing the pattern's outline through the new points — by hand on a light table (an illuminated surface bright enough to see a pattern's lines through paper laid on top, used for tracing) or automatically inside grading software. "Turning one pattern into eight" describes the end-to-end result of that whole process, not a single physical action Devon performs alone.

| Term | Plain-English explanation |
|---|---|
| Grade rule | The written set of instructions — how far to move each point on a pattern for each size step — that turns one base-size pattern into a whole run of sizes. See the "Picturing the grade rule" note above for exactly what this looks like. |
| Light table | An illuminated table (glass or plastic top lit from underneath) bright enough to see a pattern's lines through paper or fabric laid on top, used for tracing a pattern accurately by hand. |
| Grading room / cutting room | The workspace where patterns are graded, marked, and where fabric is laid out and cut — distinct rooms in a large factory, sometimes the same space in a smaller shop. |
| Pulling fabric | Taking a bolt or pre-measured length of fabric from storage and laying it out on a cutting table, the step that happens right before cutting begins. |
| Cutting | Using a blade to cut fabric along a pattern's traced outline — a hand rotary cutter or straight knife for smaller runs, or a die press (a machine that stamps a metal cutting-die shape through many layers of stacked fabric at once, like a giant cookie cutter) for high-volume runs. |
| ASTM International | A real, independent standards organization that publishes thousands of technical standards across many industries, including the body-measurement tables this case's Appendix A draws from — the same kind of organization that sets standards for things like construction materials or safety equipment, applied here to clothing sizes. |
| Fabric and Apparel Patternmaker (occupation) | The official U.S. government job category for someone who does exactly Devon's job — drafting and grading the master patterns a factory cuts from — which is why its published wage (Appendix C) is the real-world rate this case uses for grading labor. |
| Pattern grader | The person responsible for building a grade rule and checking that every graded size actually fits. |
| Tech pack | The complete technical document a factory receives describing exactly how to cut and sew a garment, including its grade rule. |
| Base size | The one size a company's pattern is originally drafted and fitted on; every other size in the run is graded up or down from it. |
| Landmark point | A specific, named location on a pattern (like the bust point or waist point) whose position is tracked and adjusted separately when grading. |
| Ease | The small, deliberate extra room built into a garment beyond a person's exact body measurement, so the garment is wearable and comfortable rather than skin-tight. |
| Marking | Tracing or plotting a pattern's outline onto fabric or paper before cutting. |
| Misses figure type | A standard body-shape/proportion category used in U.S. commercial sizing standards, distinct from other categories like "women's" or "petite," each of which has its own published measurement table. |

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
