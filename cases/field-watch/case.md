Case Study: Field Watch
MS | Math | Case Study | 2026-27 | Heroes Academy

## Overview

Talia Brennan has three satellite images of the same wheat field open on two monitors, and a claim
file that closes at five this afternoon. The field's owner says drought stress killed a section of
the crop. The insurer needs a number, not a feeling — and the number has to come from the pictures.

Every few days, a free public satellite passes over the same patch of Nebraska and measures how
green it still is. Healthy wheat reflects light one way. Stressed, dying wheat reflects it another
way. Three passes in, the trend is clearly downward — the only question is how fast, and on exactly
which day the field's condition crosses the line that turns "stressed" into "damage," a line the
insurer's own claim file is waiting on.

Talia has two ways to answer that question, built from the same three pictures. One trusts the
field's whole recent history. The other trusts only its most recent, most alarming stretch. They
don't agree with each other — and by the time the file closes this afternoon, she has to put just
one of them in it.

She opens a blank page, writes down the numbers from all three passes, and starts building the
equation that will actually decide this.

## Background

When a farmer's crop is damaged, the insurance payout isn't automatic — a claim file first has to
be verified: someone has to confirm, with evidence, that real loss actually happened before the
insurer cuts a check. This is a real mechanism, not a plot device. Crop insurance in the U.S. is
heavily backed by the USDA's Federal Crop Insurance Program, administered by the Risk Management
Agency (RMA), and the RMA has genuinely used satellite-based remote sensing — including the same
kind of optical imagery this case relies on — to check claims against what the ground actually
shows ([NASA reports on this directly](https://science.nasa.gov/missions/landsat/saving-millions-in-government-dollars-landsat-helps-fight-crop-insurance-fraud/); SEE APPENDIX G). Both sides have
something real at stake in getting the verification right: the farmer is waiting on money to cover
a genuine loss, and the insurer has to avoid paying out on a claim the evidence doesn't support,
without unfairly stalling or denying one that's real. Talia's satellite analysis is the objective
number both sides are counting on.

Talia Brennan is a remote-sensing analyst for a crop-insurance claims service, verifying a damage
claim on a wheat field in Nebraska using nothing but publicly available satellite imagery. Her
readings come from [Sentinel-2](https://sentinels.copernicus.eu/copernicus/sentinel-2), a real,
free-to-use European Space Agency optical satellite system — ordinary multispectral imagery (a
handful of separately-measured light bands, including red and near-infrared), not the specialized
"hyperspectral" sensors sometimes marketed for agriculture. From just those two ordinary bands,
optical satellites like Sentinel-2 and Landsat compute a real, standard quantity called the
Normalized Difference Vegetation Index (NDVI) — a number between roughly 0 (bare ground) and 1
(dense, healthy vegetation), essentially a ratio comparing how much near-infrared light a surface
reflects to how much red light it reflects ([NASA's own explainer](https://science.nasa.gov/earth/earth-observatory/measuring-vegetation-ndvi-evi/)
walks through the formula; SEE APPENDIX A). As real vegetation comes under real stress — drought,
disease, fire — its NDVI genuinely declines, which is exactly why insurers use it as evidence (SEE
APPENDIX A; for further reading on how NDVI works and how real insurers use it, SEE APPENDIX G).

Three real satellite passes exist for this field, spaced the way Sentinel-2 actually revisits the
same ground — every 5 days at the equator, with two satellites in orbit (SEE APPENDIX A). The
field's NDVI has declined across all three passes, but not at a constant rate: the decline from Pass
1 to Pass 2 is slower than the decline from Pass 2 to Pass 3, a real, common pattern when stress
gets worse over time (SEE APPENDIX B).

That leaves Talia with a real choice about which two passes to trust for her trend line. **Model A**
uses Pass 1 and Pass 2 — the field's longer, more established history. **Model B** uses Pass 2 and
Pass 3 — only the most recent stretch, which captures the accelerating decline but rests on fewer
data points. Both are real, defensible lines through real data; they simply don't agree (SEE
APPENDIX B, C).

The insurer's claim file has a real threshold NDVI value below which the field counts as damaged —
though as APPENDIX E shows, there is no single universal NDVI damage threshold in real use; every
insurer sets its own, calibrated to the crop and region, so this case states its own value as a
modeling assumption (SEE APPENDIX D). Whichever model Talia trusts, she has to solve it — as an
actual equation, not a guess — for the exact day the field's NDVI is predicted to cross that
threshold. Solve both, and a Hero will find something worth noticing: both models predict the field
crosses the threshold with real safety buffer left before the claim file's real filing deadline —
this isn't a race against missing that deadline. The actual dilemma is which prediction Talia can
defend in the file: the model anchored in the field's longer, more established history, or the
model that captures its most recent, most alarming stretch (SEE APPENDIX C, D).

All figures in this case are sourced in APPENDIX E, or stated as explicit modeling assumptions in
APPENDIX F where no public figure exists. The vocabulary and the "how to…" skills this case will ask
of you are listed in APPENDIX H — that is where Challenge 1 sends you.

## Dilemma

You are Talia Brennan.
Do you:
A.) Trust Model A — built from Pass 1 and Pass 2, the field's longer history OR
B.) Trust Model B — built from Pass 2 and Pass 3, the most recent trend

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. Model A, simplified: starting from Appendix B's raw form of Model A, use the distributive
    property and combine like terms to write Model A as a single simplified expression for NDVI in
    terms of day.
    D2. Model B, simplified: do the same for Model B.
    D3. Model A's crossing day: using your simplified Model A (D1) and Appendix D's threshold, solve
    the resulting equation for the day Model A predicts the field crosses the threshold.
    D4. Model B's crossing day: do the same for Model B (D2), solving for its own crossing day.
    D5. Comparing the models: write a single simplified expression for how much Model A's and Model
    B's predicted NDVI differ from each other, on any given day (Model A's simplified expression
    minus Model B's simplified expression, combined into one expression).
    D6. The safety buffer: using D3, D4, and Appendix D's filing deadline, find how many days of
    buffer each model gives before the deadline.
    D7. The verdict: using D6's two buffers, find the percentage margin between them and recommend
    which model to trust.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — Real Satellite Monitoring

| | Value |
|---|---|
| Satellite revisit interval used in this case | 5 days at the equator (Sentinel-2, two-satellite constellation) [S1] |
| Index used | NDVI (Normalized Difference Vegetation Index) — a real, standard remote-sensing measurement, computed from red and near-infrared reflectance [S2] |

This case's three-pass spacing (5 days between passes) matches Sentinel-2's real, published revisit
interval — not an invented number.

## Appendix B — The Three Passes

| Pass | Day | NDVI |
|---|---|---|
| Pass 1 | Day 3 | 0.72 |
| Pass 2 | Day 8 | 0.62 |
| Pass 3 | Day 13 | 0.51 |

**Model A** (Pass 1 → Pass 2): raw form NDVI = 0.72 − 0.02(day − 3)
**Model B** (Pass 2 → Pass 3): raw form NDVI = 0.62 − 0.022(day − 8)

Both slopes come directly from the passes above (change in NDVI ÷ change in day). SEE CHALLENGE
D1, D2.

## Appendix C — Why the Models Disagree

Model A's slope (−0.02 NDVI/day) is shallower than Model B's slope (−0.022 NDVI/day) — the decline
sped up between Pass 2 and Pass 3. Model A, anchored in the field's longer history, predicts a
*later* crossing day than Model B, which is more responsive to the field's most recent, most
alarming stretch. Neither model is simply "wrong" — they are built from different, both-real subsets
of the same three passes. SEE CHALLENGE D3, D4, D5.

## Appendix D — The Threshold and the Deadline

| | Value |
|---|---|
| NDVI damage threshold used in this claim | 0.40 — SEE APPENDIX F, MA1 |
| Claim file filing deadline | Day 26 |

## Appendix E — Sources

| id | Claim | Value | Source | Accessed | Confidence |
|---|---|---|---|---|---|
| S1 | Sentinel-2's revisit interval at the equator, two-satellite constellation | 5 days | European Space Agency, "Sentinel-2 images the globe every 5 days" ([link](https://sentinels.copernicus.eu/web/success-stories/-/sentinel-2-images-the-globe-every-5-days)) | 2026-08-12 | HIGH |
| S2 | NDVI is a real, standard remote-sensing vegetation index; burn/vegetation-stress NDVI thresholds are not a single universal value — they vary by region and vegetation type and must be calibrated, not assumed | n/a (context, establishes this case's own threshold is honestly a modeling assumption, not a fabricated "standard" figure) | USGS Burn Severity Portal, glossary ([link](https://burnseverity.cr.usgs.gov/glossary)) | 2026-08-12 | HIGH |

## Appendix F — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, each with a real basis named below. A Hero may challenge them in discussion — that is a
> legitimate move, and Appendix H names the skill a Hero would need to test one.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | NDVI damage threshold for this claim | **0.40** (0.37 base + a 0.03 calibration allowance) | Real burn/stress NDVI thresholds are not universal — they are regionally and crop-type calibrated (S2). This case states its own calibrated value rather than inventing a fake "standard" one. | Directly load-bearing. The 0.03 calibration allowance is flexed ±50% in Tier 2 probe 5 (effective threshold 0.385-0.415): margin ranges 12.02%-17.09%, Model B stays the winner throughout. |
| MA2 | The three passes' specific NDVI values (Appendix B) and the filing deadline (Appendix D) | See Appendix B/D | This field's own claim data for this specific, authored dispute — no public database of real per-field insurance-claim satellite readings exists (same convention as every prior case's authored domain data). | Not swept in Tier 2 probe 5 (authored field data, not a stated numeric flex-eligible dial). |

## Appendix G — Learn More

These are real, currently-live resources for a Hero who wants to go beyond this case's math and see
how NDVI and satellite remote sensing work in the real world:

- [NASA Earthdata — Normalized Difference Vegetation Index (NDVI)](https://www.earthdata.nasa.gov/topics/land-surface/normalized-difference-vegetation-index-ndvi) — NASA's official explainer of how NDVI is calculated from near-infrared and red reflectance, and what the resulting values mean for vegetation health.
- [NASA Earth Observatory — Measuring Vegetation (NDVI & EVI)](https://science.nasa.gov/earth/earth-observatory/measuring-vegetation-ndvi-evi/) — a plain-language walkthrough of the NDVI formula and how scientists use it (and the related EVI index) to track plant health from space.
- [USGS — Landsat Normalized Difference Vegetation Index](https://www.usgs.gov/landsat-missions/landsat-normalized-difference-vegetation-index) — the U.S. Geological Survey's own reference page on how Landsat data is turned into NDVI maps.
- [NASA Science — Landsat Helps Fight Crop Insurance Fraud](https://science.nasa.gov/missions/landsat/saving-millions-in-government-dollars-landsat-helps-fight-crop-insurance-fraud/) — a real NASA article on how the USDA's Risk Management Agency actually uses Landsat satellite imagery to verify crop-insurance claims, the exact kind of work Talia is doing in this case.
- [ESA — Copernicus Sentinel-2 mission overview](https://sentinels.copernicus.eu/copernicus/sentinel-2) — the European Space Agency's official page on the two-satellite Sentinel-2 constellation that produces the real revisit schedule this case's three passes are based on.

## Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Like Terms
- Distributive property

**"How to…" questions**

- How to add and subtract an expression with variables
- How to solve a multi-step equation with a variable on one side
- How to subtract with negative numbers
- How to find the percent of a number

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
