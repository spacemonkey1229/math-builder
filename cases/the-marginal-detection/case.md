Case Study: The Marginal Detection
MS | Math | Case Study | 2026 | Adventure

## Overview

Ingrid Solberg reloads the pipeline dashboard for the third time before her coffee finishes cooling — a spreadsheet-like table of every candidate her team's telescopes have flagged, one row per star. One row is highlighted in yellow, not green: a candidate that cleared the automated flagging threshold overnight, barely. She clicks the row and a second window opens beside it, a plot of twenty small points scattered across the screen — a night's worth of brightness measurements for one star, one candidate, one dip that might be a planet crossing in front of it and might be nothing at all.

Tomorrow's four-hour telescope slot is the only one her team has this week, and it is already spoken for twice — once by this candidate, which wants a second night of data to firm up the detection, and once by a start-of-survey policy that says an unclaimed slot defaults automatically to whichever fresh target sits at the top of the queue. Ingrid has to actually assign the slot, by typing a target name into a single scheduling field, before she leaves tonight, or the automatic default fills it for her.

She pulls up two ways of reading the same twenty points. One fits a straight line through the quiet stretches of the night and measures the dip against how far the leftover static strays from that line. The other ignores the idea of a trend entirely and just asks how unusual the dip looks against the ordinary spread of a normal night for this star. The two methods do not agree. Ingrid's cursor sits in the scheduling field, blinking, next to the label TOMORROW'S SLOT.

## Background

Ingrid Solberg leads the candidate-vetting team for the Sable Peak Survey, a ground-based exoplanet-transit program that shares its telescope time, night by night, across dozens of active candidates and a queue of never-yet-observed targets. Her job is not to discover planets herself — it is to decide, every single night, which candidates deserve another look and which should be set aside so a fresh target can have its turn.

Every candidate the survey's pipeline flags starts the same way: a star's brightness is measured over and over across one night, producing a light curve — a plot of brightness against time (SEE APPENDIX A). If the brightness drops during a short window and then recovers, that dip might be a planet passing in front of the star (a transit). But real light curves are never flat outside the dip. Every star drifts a little over a night as the telescope tracks it through changing air thickness and temperature — and that drift is often curved, not straight, which matters enormously for how "big" a dip has to be before it counts as a real signal instead of ordinary noise (SEE APPENDIX B).

The survey has a standing internal policy for exactly this situation, agreed on by the vetting team before this case begins: a candidate is worth spending a follow-up slot on only if its dip's significance — how many multiples of the night's own noise spread the dip represents — reaches 3.0 or higher (SEE APPENDIX B). Below that line, the dip is scheduled to be logged and set aside, no slot spent. There are exactly two candidate methods on Ingrid's desk for calculating that significance number from the same twenty data points, and depending on which one she trusts, this candidate lands on opposite sides of the 3.0 line (SEE APPENDIX A, APPENDIX B). Real exoplanet-survey pipelines — including NASA's own Kepler mission — set their own, much higher, formal discovery threshold using exactly this kind of significance ratio, which is why the number itself, not just a gut read of the dip, is what the team's policy is built around (SEE APPENDIX C). Every figure Ingrid is working from tonight, sourced or assumed, is documented in (SEE APPENDIX D), and the math vocabulary and procedures needed to build and check her two significance reads are listed in (SEE APPENDIX E).

## Dilemma

You are Ingrid Solberg.
Do you:
A.) Spend tomorrow's follow-up slot re-observing the marginal candidate to try to firm up the detection OR
B.) Abandon the marginal candidate and spend the slot on a fresh, unexamined target instead

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. An original scatter plot of all twenty flux measurements from Appendix A (time step on
    the horizontal axis, flux in parts per million on the vertical axis), with the four
    in-transit points visibly marked apart from the sixteen out-of-transit points.
    D2. A calculated line of best fit through the sixteen out-of-transit points only — its
    equation shown with your work — plotted on top of your Challenge 3 (D1) scatter plot, plus a
    written judgment of how strong the correlation between time and flux really is and why a
    single straight line is a poor (non-linear) description of the night's actual drift.
    D3. The "naive" significance ratio: the transit dip's depth (measured against your Challenge
    3 (D2) line, extended into the transit window) divided by the standard deviation of the
    out-of-transit points' residuals from that line, shown step by step, compared against
    Appendix B's 3.0 follow-up threshold.
    D4. A box-and-whisker plot of the sixteen out-of-transit flux values, with all five summary
    numbers (minimum, Q1, median, Q3, maximum) labeled and your interquartile range shown, plus
    the "distribution-aware" significance ratio — the dip's depth divided by 0.7413 × your IQR
    (Appendix B explains this constant) — compared against the same 3.0 threshold, and a note on
    whether any out-of-transit point qualifies as a statistical outlier by the 1.5×IQR rule.
    D5. A one-paragraph written recommendation that states both significance numbers from
    Challenges 3 (D3) and (D4), explains in plain language why a curved, non-linear drift makes a
    straight-line read and a distribution-based read disagree, and names which read you trust
    more and why.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — The Marginal Candidate's Overnight Light Curve

Referenced in Background and Challenge 3 (D1, D2, D3, D4). Twenty brightness measurements of the
candidate star, taken every 15 minutes across a 4-hour-45-minute observing window. Flux is
reported as parts-per-million (ppm) deviation from the star's own normalized average brightness —
a negative number means the star looked dimmer than usual at that moment. The four points inside
the suspected transit window are marked.

| Time step (t) | Minutes elapsed | Flux (ppm deviation) | In transit? |
|---|---|---|---|
| 0 | 0 | +127 | |
| 1 | 15 | +128 | |
| 2 | 30 | -12 | |
| 3 | 45 | -40 | |
| 4 | 60 | +9 | |
| 5 | 75 | +68 | |
| 6 | 90 | -17 | |
| 7 | 105 | -112 | |
| 8 | 120 | -257 | TRANSIT |
| 9 | 135 | -221 | TRANSIT |
| 10 | 150 | -167 | TRANSIT |
| 11 | 165 | -215 | TRANSIT |
| 12 | 180 | -68 | |
| 13 | 195 | -51 | |
| 14 | 210 | -17 | |
| 15 | 225 | -50 | |
| 16 | 240 | +9 | |
| 17 | 255 | +46 | |
| 18 | 270 | +146 | |
| 19 | 285 | +83 | |

**This exact night's data is a stated Modeling Assumption (MA1)** — see Modeling Assumptions
below. No survey publishes a specific candidate's raw overnight photometry pipeline output; the
values above are a constructed scenario, bounded by real published photometric-precision figures
for a bright ground-based/space-based target (SEE APPENDIX C, [S1]).

For scale: a real, confirmed transiting planet (HD 189733 b) produces a dip of roughly 24,000 ppm
— about 2.4% of the star's light [S5]. This candidate's dip is nowhere near that size, which is
exactly why the question of how to measure "how significant is a small dip" matters here.

## Appendix B — Two Significance Reads and the Follow-Up Threshold

Referenced in Background and Challenge 3 (D2, D3, D4, D5). Both reads turn the same 16
out-of-transit points and the same 4 in-transit points into one number: how many multiples of the
night's own noise the dip represents. They disagree because they measure "the night's own noise"
two different ways.

**Method 1 — the naive line-of-best-fit read.** Fit a straight line to the 16 out-of-transit
points. Measure how far each of those 16 points actually falls from that line (the residuals),
and take the **sample standard deviation** of those 16 residuals — divide the sum of squared
residuals by (16 − 1) = 15, then take the square root; this is the same "divide by n − 1"
convention your calculator's `stdev` function and most introductory statistics courses use by
default, not the "divide by n" population version and not a regression standard error that
divides by (n − 2) — as "one unit of noise." Extend the line into the transit window and measure
the dip against the line: **the dip depth is the line's predicted value at the midpoint of the
transit window (t = 9.5) minus the average (mean) of the four in-transit flux values.** Then
divide that dip depth by the noise unit above.

**Method 2 — the distribution-aware box-and-whisker read.** Do not fit any trend at all. Take the
16 out-of-transit points exactly as measured, find their five-number summary (minimum, Q1,
median, Q3, maximum) **using the linear-interpolation method for Q1 and Q3 — the same method
spreadsheet software's `PERCENTILE.INC`/`QUARTILE.INC` functions use by default, not the
"split the data in half and take the median of each half" method** — and use the interquartile
range (IQR = Q3 - Q1) to estimate "one unit of noise" as 0.7413 × IQR — a standard statistics
conversion (0.7413 ≈ 1 ÷ 1.349, where 1.349 is how many standard deviations apart Q1 and Q3 sit
for a normal, bell-shaped distribution) that turns the middle 50% spread of a data set into an
estimate directly comparable to a standard deviation, robust to a few extreme points skewing the
result. Measure the dip against the out-of-transit median: **the dip depth is the out-of-transit
median minus the average (mean) of the four in-transit flux values.** Then divide that dip depth
by the noise unit above.

**Why they can disagree.** The night's drift is curved (non-linear), not straight — Challenge 3
(D2) asks you to check this directly. A straight line fit through a curved pattern systematically
misses low in the middle and high at the ends (or the reverse), which can make the leftover
residual noise near the center of the night look artificially large or artificially small
depending on exactly where the transit falls. The box-and-whisker read never tries to model the
shape of the drift at all — it just asks how unusual the dip looks against the plain, honest
spread of a normal night, wherever in that spread the dip happens to land.

**The Sable Peak Survey's follow-up policy (MA2):** a candidate's dip must reach a significance
ratio of **3.0** or higher, by whichever read the vetting team is using, before a follow-up slot
is approved. This is a team policy, not a discovery claim — real large-scale surveys use a much
higher bar for an actual confirmed detection (SEE APPENDIX C, [S2]). A 3.0 threshold is simply the
Sable Peak team's own internal bar for "worth a second look," set below the real discovery
standard on purpose, since a follow-up night only adds more evidence — it does not, by itself,
announce a discovery.

## Appendix C — Why This Distinction Is Real

Referenced in Background and Appendix B. Three real, cited facts ground this case's numbers and
its central tension.

**Real surveys set formal significance bars far above 3.0.** NASA's Kepler mission's own transit-
detection pipeline flagged a "Threshold Crossing Event" only once a candidate's combined
(phase-folded) detection statistic — the same kind of significance ratio this case computes, just
built from many nights of data stacked together instead of one — exceeded **7.1 standard
deviations** — a threshold chosen so that, across the roughly 17 million individual statistical
trials Kepler performed over its mission (each time the pipeline checked one star's data for a
possible signal counts as one trial, and running millions of trials means even pure random noise
will occasionally look like a signal somewhere by chance), the pipeline was expected to produce
only about one false alarm from random noise alone [S2]. Sable Peak's 3.0 follow-up bar (Appendix
B, MA2) sits deliberately far below that — it is a
"look again" threshold for one survey's own limited telescope time, not a discovery claim.

**Real photometric noise, at this brightness range, really is in the same ballpark as this
candidate's numbers.** NASA's TESS mission was designed to reach 200 parts-per-million photometric
precision in a one-hour bin for a star at TESS magnitude 10, with in-flight performance later
found to be even better than that pre-flight design figure for the brightest stars in its field
[S1]. This case's Appendix A noise level (point-to-point scatter on the order of 50-130 ppm per
15-minute measurement) is consistent with a bright target observed from a smaller, ground-based
telescope — noisier than TESS's own best in-orbit numbers, which is realistic for a survey with
Sable Peak's more modest equipment.

**Public data-sharing tools like the ones Ingrid's team would actually use are real and
currently live.** The American Association of Variable Star Observers (AAVSO), founded in 1911,
is the largest organization of variable-star observers in the world and maintains a shared
observation database that amateur and professional astronomers alike contribute to and download
from [S3]. NASA's Exoplanet Archive is the standard public repository for confirmed-planet
parameters and their published light curves, including HD 189733 b's real, well-measured transit
depth cited in Appendix A [S4, S5].

## Modeling Assumptions

> These figures are **not sourced from an external publisher**. They are stated scenario
> assumptions chosen by the case author because a specific candidate's raw overnight pipeline
> output, and one survey's own internal follow-up policy, are not the kind of thing any real
> survey publishes for a still-unconfirmed candidate. A Hero may challenge these numbers in
> discussion — that is a legitimate move, and the Sensitivity column shows exactly where the
> challenge would matter.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | The candidate's full 20-point overnight light curve (Appendix A) | See Appendix A for all 20 values | No survey publishes a specific still-unconfirmed candidate's raw per-point pipeline output — this is exactly the kind of in-progress data that stays internal until a candidate is confirmed or dropped. The noise level and the curved (non-linear) drift shape are both bounded by real published photometric-precision figures for a bright target observed with modest ground-based equipment [S1], and the transit dip size is set well below a real confirmed transit's depth [S5] on purpose, since this is meant to be a genuinely marginal case. | The exact point values are load-bearing for both Challenge 3 (D3) and (D4) — a Hero who constructs a different, still-plausible 20-point night (same noise bound, same curve shape) could get a different pair of significance numbers, and possibly a different answer for one or both methods. Work the comparison yourself with a different plausible dataset before assuming this case's exact numbers are unchallengeable. |
| MA2 | The Sable Peak Survey's own follow-up significance threshold (Appendix B) | 3.0 | No public survey policy document states any specific survey's own internal "worth a follow-up slot" bar — this is an operational, team-level policy choice, not a published standard. Set well below Kepler's real, formal 7.1σ discovery threshold [S2] on purpose, since a follow-up observation is a request for more evidence, not a discovery announcement. | Both this case's computed significance numbers (3.006 and 2.521) sit close to this exact threshold on either side. Moving the threshold up or down by even a few tenths could put both reads, or neither read, on the same side of the line — this is the single most sensitive dial in the case, and it is meant to be. |

## Appendix D — Sources

All sourced (non-assumption) figures and facts in this case are cited here.

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | TESS's designed and in-flight photometric precision for bright stars | Pre-flight design target: 200 ppm in a 1-hour bin at TESS magnitude 10; measured in-flight noise floor approximately 20 ppm for the brightest stars | Photometry of 10 Million Stars from the First Two Years of TESS Full Frame Images: Part II, Research Notes of the AAS ([IOPscience](https://iopscience.iop.org/article/10.3847/2515-5172/abca2d)) | published November 2020 | HIGH |
| S2 | Kepler mission's formal Threshold Crossing Event detection significance cutoff, and the false-alarm reasoning behind it | 7.1 standard deviations (Multiple Event Statistic), chosen to keep expected false alarms from random noise to roughly one across the whole mission | Tenenbaum et al., "Detection of Potential Transit Signals in the First Twelve Quarters of Kepler Mission Data" ([arXiv:1212.2915](https://arxiv.org/abs/1212.2915)) | submitted December 2012 | HIGH |
| S3 | AAVSO's founding, scale, and role as a real, currently operating variable-star data-sharing organization | Founded 1911; the largest organization of variable-star observers in the world; maintains a shared, publicly contributed observation database | Wikipedia — [American Association of Variable Star Observers](https://en.wikipedia.org/wiki/American_Association_of_Variable_Star_Observers) | accessed 2026-09-18 | MEDIUM (secondary encyclopedia source, used only for qualitative organizational context, not a numeric figure this case computes with) |
| S4 | NASA Exoplanet Archive's role as the standard public repository for confirmed-planet parameters and light curves | qualitative — grounds Appendix C's claim that public light-curve data tools are real and currently live | NASA Exoplanet Archive ([exoplanetarchive.ipac.caltech.edu](https://exoplanetarchive.ipac.caltech.edu/)) | accessed 2026-09-18 | HIGH |
| S5 | Transit depth of the confirmed exoplanet HD 189733 b, used for scale comparison in Appendix A | approximately 2.4% (about 24,000 ppm) | NASA Exoplanet Archive — HD 189733 b overview page ([exoplanetarchive.ipac.caltech.edu/overview/HD%20189733%20b](https://exoplanetarchive.ipac.caltech.edu/overview/HD%20189733%20b)) | accessed 2026-09-18 | HIGH |

**Who these sources are:** the TESS and Kepler papers [S1, S2] are peer-reviewed publications
from the missions' own science teams, describing the real instruments' real measured or designed
performance. AAVSO [S3] is a real, 115-year-old nonprofit that coordinates variable-star
observing among professional and amateur astronomers worldwide. The NASA Exoplanet Archive
[S4, S5] is NASA's own public database of confirmed exoplanets and their measured properties,
operated by Caltech/IPAC. See `RESEARCH_LOG.md` for the full search trail, including what was
searched and why the candidate's own raw overnight data (MA1) and the survey's follow-up
threshold (MA2) could not be sourced and were instead recorded as stated assumptions.

## Appendix E — "How To…" Math Questions To Research

**Vocabulary terms**

- Non-linear
- Outlier
- Scatter Plot
- Correlation
- Quartiles

**"How to…" questions**

- How to draw a line of best fit given a set of data
- How to create a box and whisker plot given a set of data
- How to create a scatter plot given a set of data
- How to identify correlation given a scatter plot or set of data

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
