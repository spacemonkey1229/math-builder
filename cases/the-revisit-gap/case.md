# Case Study: Revisit Gap

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

The board meets in nine days, and Marcus Oduya has one line item left to defend: the satellite bill.

Last year's invoice sits open on one monitor — five figures, itemized by week. On the other monitor, a free download queue slowly fills with the same forest, the same tree line, a few days slower and a little blurrier at the edges. Marcus has spent three years watching both feeds catch the same clearings, eventually. The question the board actually wants answered isn't which feed is sharper. It's whether the sharper one is worth what it costs.

His inbox has a reminder from the field-patrol coordinator: a report of a small clearing near the reserve's eastern boundary, confirmed on the ground, that neither feed flagged the same week it happened. Marcus still isn't sure which feed would have caught it sooner, or whether either one would have caught it at all.

He opens a blank slide, types "Recommendation," and stops.

Outside his window, a delivery truck idles at the gate — this month's invoice, printed and signed, waiting for his initials before it goes to the board packet.

---

## Background

Marcus Oduya is a deforestation-monitoring analyst for a rainforest-conservation NGO, responsible for recommending the program's satellite-imagery budget for the coming year to the board before it locks. He is accountable for one recommendation, backed by numbers: which imagery plan to fund for the 25 km² reserve his program monitors.

Both options watch the same reserve for the same purpose — catching illegal forest clearing early enough for the field-patrol team to respond (SEE APPENDIX A). They differ in resolution, revisit cadence, and cost.

**Commercial Weekly** subscribes to 3-meter-resolution satellite imagery, newly tasked over the reserve every week, from a commercial provider (SEE APPENDIX A). Finer resolution means smaller clearings are visible before they grow, but the subscription is billed by the square kilometer and by the week, and someone still has to review every scene (one satellite image covering the reserve) it delivers (SEE APPENDIX B).

**Sentinel Free** relies on the Sentinel-2 satellite constellation's free, public 10-meter-resolution imagery, which revisits the same ground roughly every 5 days (SEE APPENDIX A). It costs nothing to download, but a coarser pixel misses small clearings entirely, and someone still has to review every scene it delivers too (SEE APPENDIX B).

Neither option is free once both are counted the same way: the honest comparison is hectares of confirmed illegal clearing detected per dollar of annual imagery cost — not sticker price, and not resolution alone (SEE APPENDIX C). What each resolution can actually detect, and how detection lag varies between the two feeds, are given in **APPENDIX A**. Analyst review time and the commercial subscription's real per-area price are in **APPENDIX B**. The annual detection-and-cost comparison is worked through in **APPENDIX C**. A sample of past commercial invoices from a sister program, at other reserve sizes, is in **APPENDIX D**. Any stated scenario assumptions are in **APPENDIX E**. The vocabulary and "how to…" skills this case asks of you are listed in **APPENDIX F**. Every figure in this case is sourced or disclosed as an assumption in **APPENDIX G**.

He has to recommend one plan.

---

## Dilemma

You are Marcus Oduya.

Do you recommend:

**A.)** **Commercial Weekly** — 3-meter commercial satellite imagery, newly tasked weekly over the reserve **OR**

**B.)** **Sentinel Free** — free 10-meter Sentinel-2 imagery, revisiting the reserve roughly every 5 days

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A box-and-whisker plot of detection lag.** Using Appendix A's two data sets (days between a real clearing event and its first confirmed satellite alert, for each feed), draw a box-and-whisker plot for Commercial Weekly's lag data and one for Sentinel Free's lag data. State, in writing, which feed's detection lag is more consistent (tighter spread) and which has the longer median lag.
  *Why a box-and-whisker plot, not just an average:* the board doesn't just want to know which feed is faster on a typical week — they want to know how much either feed's timing can be trusted. A single average hides how wide a feed's worst-case delays really run; the plot doesn't.
- **D2 — A minimum-detectable-clearing-size comparison.** Using the "3×3 pixel" minimum-mapping-unit rule in Appendix A, compute the smallest clearing patch each feed can reliably detect, in square meters and in hectares, for both the 3 m and 10 m resolutions. Then compute the *ratio* of the two resolutions (10 m ÷ 3 m) and the *ratio* of the two minimum detectable areas, and explain in writing why the two ratios are not the same number — why finer resolution helps more than its raw pixel-size ratio would suggest.
  *Why this is a non-linear relationship, not a straight scaling:* minimum detectable area is a function of pixel size *squared*, not pixel size itself. A resolution that is about 3.3× finer detects patches that are over 11× smaller — tripling the resolution does not triple the detection floor, it does something disproportionately larger, which is exactly what "non-linear" means here.
- **D3 — A line of best fit for the commercial plan's cost.** Using Appendix D's sample of past commercial invoices at other reserve sizes, plot cost (y) against monitored area (x) and draw a line of best fit. Use your line to estimate what Commercial Weekly would cost at the reserve's actual 25 km² size, and compare that estimate to Appendix B's own stated commercial subscription cost.
  *Why a line of best fit earns its place here, rather than just using Appendix B's number directly:* Appendix B gives you the *planned* cost for this exact reserve; Appendix D gives you what four *other, differently-sized* reserves actually paid. If your fitted line's estimate and Appendix B's planned figure disagree by much, that's worth noticing and saying something about before you trust either one blindly.
- **D4 — The missing month.** Appendix D's own monthly invoice table for Commercial Weekly has one month's dollar amount redacted (illegible on the scanned copy the board received), but the year's mean monthly cost is stated. Using the mean and the other eleven months' values, solve for the missing month's dollar amount. Show your work.
  *Why this is solvable at all:* a mean is just a total divided by a count — if you already know the total (from the mean) and eleven of the twelve pieces that make it up, the twelfth is determined. This is a real gap in the board's own paperwork, not a decorative puzzle.
- **D5 — A results table and recommendation.** For each option, compute hectares of confirmed illegal clearing detected per year (Appendix C) divided by that option's total annual cost (subscription, if any, plus analyst review labor — Appendix B). Recommend one plan, in writing, using this ratio — not detection alone, and not cost alone.
  *Why the ratio, and not either number by itself:* a plan that detects more but costs far more isn't obviously worth it, and a free plan that misses real clearings isn't obviously a bargain either. Dividing lets Marcus compare two plans that differ in both what they catch and what they cost on the same footing.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A: The Two Feeds, Resolution, and Detection Lag

Sentinel-2 is a two-satellite European Space Agency constellation whose finest optical bands have a native ground resolution of 10 meters, and which revisits (automatically re-photographs, on its fixed orbit) a given point on Earth roughly every 5 days at the equator with both satellites operating [S1]. It is downloadable free of charge, with no purchase or subscription, from public portals including the USGS EarthExplorer archive (a US government satellite-image search tool), the Sentinel-2 Level-2A (a processing stage where the raw satellite signal has already been corrected for atmosphere and converted to ready-to-use imagery) Cloud-Optimized GeoTIFF archive on AWS Open Data, and the Copernicus Data Space Ecosystem (the European Space Agency's own free data portal) [S2][S3][S4].

Commercial sub-5-meter imagery (this case uses a 3-meter-resolution product, matching Planet's SkySat constellation (a commercial satellite operator) as resold through SkyFi's Planet Select marketplace (an online storefront for buying satellite images)) can be **newly tasked**: instead of only capturing an area when its orbit happens to fly over it (a "revisit"), a commercial operator can point its satellite's camera at a customer-chosen spot on request, on a set cadence — weekly, in this case — rather than waiting for a fixed orbital revisit [S5].

**Minimum detectable clearing size.** A widely used rule of thumb in remote sensing holds that a feature must span roughly 3×3 pixels to be reliably detected and classified — for example, 30-meter imagery from Landsat (a long-running US government Earth-observation satellite program) is generally treated as reliably resolving features no smaller than about 0.81 hectares (a 90 m × 90 m minimum mapping unit) [S6][S7].

**Detection lag data** (days between a real clearing event and its first confirmed satellite alert, drawn from this program's own past incident log, MA1 — SEE APPENDIX E):

| Commercial Weekly (days) | Sentinel Free (days) |
|---|---|
| 2, 3, 3, 4, 4, 4, 5, 5, 6, 7 | 3, 4, 5, 6, 7, 9, 10, 12, 15, 20 |

---

## Appendix B: Cost Inputs

| Quantity | Value |
|---|---|
| Reserve area monitored | 25 km² |
| Commercial Weekly tasking price | $12.00 per km² per scene (SkySat Flexible Tasking) [S5] |
| Commercial Weekly scenes per year | 52 (weekly) |
| Commercial Weekly planned annual subscription cost | 25 km² × $12.00/km² × 52 = $15,600 (derived) |
| Analyst hourly cost | $35.00 per hour (MA2) |
| Commercial Weekly analyst review time per scene | 1.5 hours (MA3) |
| Commercial Weekly total annual analyst labor | 52 × 1.5 × $35.00 = $2,730 (derived) |
| Sentinel Free scenes per year (365 ÷ 5) | 73 |
| Sentinel Free analyst review time per scene | 3.0 hours (MA4) |
| Sentinel Free total annual analyst labor | 73 × 3.0 × $35.00 = $7,665 (derived) |
| Sentinel Free subscription cost | $0 |

---

## Appendix C: Annual Detection

| Quantity | Value |
|---|---|
| Total confirmed illegal clearing across the reserve, per year | 6.0 hectares (MA5) |
| Share of that total that is "small" clearings — roughly the size of a two-car garage to a basketball court: large enough for a person on the ground to see and report, but below Sentinel Free's minimum detectable patch size (900 m&sup2;) while still above Commercial Weekly's (81 m&sup2;) — see D2 | 50% (MA6) |
| Hectares Commercial Weekly detects per year | All 6.0 ha (its finer resolution resolves both size classes) |
| Hectares Sentinel Free detects per year | Only the clearings at or above its own minimum detectable size — see D2 and MA6 |

---

## Appendix D: Sample Past Invoices (Sister Program, Other Reserve Sizes)

A sister program using the same commercial provider at four other, differently-sized reserves, most recent full year:

| Reserve area (km²) | Annual commercial cost ($) |
|---|---|
| 10 | 9,200 |
| 50 | 34,500 |
| 75 | 48,900 |
| 100 | 65,800 |

**Commercial Weekly's own monthly invoice for this reserve, most recent full year** (mean monthly cost: $1,300.00 — SEE CHALLENGE D4):

| Month | Amount ($) |
|---|---|
| Jan | 1,250 |
| Feb | 1,180 |
| Mar | 1,300 |
| Apr | 1,350 |
| May | 1,400 |
| Jun | 1,450 |
| Jul | *(illegible on the scanned copy the board received)* |
| Aug | 1,420 |
| Sep | 1,300 |
| Oct | 1,200 |
| Nov | 1,150 |
| Dec | 1,100 |

---

## Appendix E: Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case author. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis |
|---|---|---|---|
| MA1 | Detection-lag data sets (Appendix A) | 10 values per feed, as tabled | No public program discloses a real, matched detection-lag data set for two specific commercial-vs-free feeds over the same events. This case constructs a representative data set consistent with each feed's real revisit cadence (weekly tasking vs. ~5-day Sentinel-2 revisit, plus realistic cloud/tasking-gap spread) — not measured from any single real program's incident log. |
| MA2 | Analyst hourly cost | $35.00/hour | A representative conservation-sector analyst wage; no single public wage figure was found for this exact role. |
| MA3 | Commercial Weekly analyst review time per scene | 1.5 hours | Finer, pre-tasked commercial imagery typically needs less manual interpretation per scene than coarser free imagery. |
| MA4 | Sentinel Free analyst review time per scene | 3.0 hours | Coarser 10 m imagery requires more manual interpretation and cloud-masking work per scene. |
| MA5 | Total confirmed illegal clearing across the reserve, per year | 6.0 hectares | A representative annual loss figure for a small, actively monitored protected reserve; no public per-reserve figure was found for this specific site. |
| MA6 | Share of annual clearing that is "small" (sub-Sentinel-detectable, super-commercial-detectable) | 50% | Informed by published remote-sensing findings that a large share of tropical deforestation now occurs in small clearings that moderate-resolution sensors systematically under-detect (SEE APPENDIX G). **Sensitivity: HIGH — this is the single most load-bearing assumption in the case; see the Sensitivity note below.** |

**Sensitivity note (MA6).** D5's ratio for Sentinel Free depends entirely on what share of real clearing activity falls below its detection floor. A higher share makes Commercial Weekly's advantage larger; a lower share erodes it, and could erase it. Challenge D5 asks you to state your recommendation using the case's stated 50% figure — but a strong pitch says out loud that this is the number the whole recommendation rides on.

---

## Appendix F: "How To…" Math Questions To Research

**Vocabulary**

- Non-linear

**How to…**

- How to create a box and whisker plot given a set of data
- How to draw a line of best fit given a set of data
- How to find a missing data element given the mean and the remaining elements of its set
- How to convert an amount from one unit to another unit

---

## Appendix G: Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Sentinel-2 revisit time and finest-band resolution | 10 m resolution (four bands); 5-day revisit at the equator with 2 satellites (2-3 days at mid-latitudes) | [Copernicus Data Space Ecosystem — Sentinel-2 documentation](https://documentation.dataspace.copernicus.eu/Data/SentinelMissions/Sentinel2.html) | accessed 2026-09-18 | HIGH |
| S2 | USGS EarthExplorer: free browsing, free-account download | Free (account required only to download) | [USGS EarthExplorer](https://earthexplorer.usgs.gov/) | accessed 2026-09-18 | MEDIUM |
| S3 | Sentinel-2 L2A COGs on AWS Open Data: free public bucket | `s3://sentinel-cogs`, `us-west-2`, `--no-sign-request` | [AWS Open Data Registry — Sentinel-2 L2A COGs](https://registry.opendata.aws/sentinel-2-l2a-cogs/) | accessed 2026-09-12 (prior session, re-cited) | HIGH |
| S4 | Copernicus Data Space Ecosystem: free instant access | Free, no account needed to browse | [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/) | accessed 2026-09-12 (prior session, re-cited) | HIGH |
| S5 | Commercial SkySat imagery pricing | SkySat Archive from $6/km²; SkySat Flexible Tasking from $12/km² | [SkyFi — Planet Select](https://skyfi.com/en/products/planet-select) | accessed 2026-09-18 | MEDIUM |
| S6 | Minimum mapping unit rule of thumb, tied to pixel size | 30 m Landsat pixels are generally treated as reliably resolving features no smaller than about a 3×3-pixel (0.81 ha) minimum mapping unit | Web search synthesis citing Knight, J.F. & Lunetta, R.S. (2003), "An experimental assessment of minimum mapping unit size," *IEEE Transactions on Geoscience and Remote Sensing*, and corroborating GIS/remote-sensing sources (ArcGIS Pro documentation, Esri GIS Dictionary) | accessed 2026-09-18 | MEDIUM |
| S7 | Minimum mapping unit, general definition | "The smallest size that determines whether a feature is captured from a remotely sensed image" | Sage Reference — Encyclopedia of Geographic Information Science, "Minimum Mapping Unit (MMU)" (title/existence confirmed via search; full text not directly fetched this session) | accessed 2026-09-18 | LOW |

All sources above marked "accessed 2026-09-18" were fetched or searched live this session. S3/S4 reuse URLs independently verified live in a prior session on this same project (`cases/pixel-snap/case.json`, 2026-09-12) for the identical claim, per this project's own established practice of citing a previously-fetched, still-current source rather than re-fetching an unchanged public infrastructure page. S6 could not be confirmed by a direct full-text fetch of the original 2003 IEEE paper (paywalled; a ResearchGate landing page returned 403) — the figure is corroborated by multiple independent secondary sources found in this session's search results, graded MEDIUM rather than HIGH for that reason, and used only to justify D2's minimum-mapping-unit *method*, not as a Reserve-specific measured figure. S7 is LOW confidence (title/existence only, full text not fetched) and is used only as general background context, never as a load-bearing figure.

---

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
