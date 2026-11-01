# Case Study: Pixel Snap

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

The alert map is due in eleven minutes, and Priya Anand still has the cursor parked over two different buttons.

On her second monitor, last month's satellite pass sits stacked under this morning's download, and between them, right along the tree line above the Kutai concession, a thin bright ribbon of "new clearing" pixels blinks red. She has seen this ribbon before. It is never quite in the same place twice.

Her phone buzzes on the desk — Bilal, the field-enforcement lead, already up and reading her draft alerts before his coffee. *Team's fueling the trucks. Confirm the Kutai coordinates?*

Two months ago she sent his rangers four hours down a logging road to a "clearing" that turned out to be the same stand of trees the satellite had always seen — just shifted half a pixel to the left. They came back at dusk, angry, having walked past three real clearings her map never flagged, because she'd told them where the software said to look, not where the forest actually was.

She has two ways to line up today's pixels against last month's. One takes a few minutes and a button click. The other takes the rest of the morning, a stack of surveyed ground points, and Bilal's trucks sitting idle in the yard while she works.

The cursor doesn't move. Behind her, an engine turns over in the lot.

---

## Background

Priya Anand is the remote-sensing analyst for a rainforest-conservation NGO monitoring the Kutai concession and several neighboring blocks. Every month she downloads a fresh satellite scene, lines it up against last month's scene — a step called **image registration** — and differences the two to produce the forest-loss alert map that Bilal's field-enforcement team drives out on. She is accountable for two numbers that follow her every month: how many real clearings her map catches, and how many "clearings" turn out to be nothing but a shifted pixel grid.

Both this month's and last month's scenes come from the Sentinel-2 satellite constellation, whose finest visible-light bands (Blue, Green, Red, and Near-Infrared) have a native ground resolution of 10 meters [S1] — meaning every pixel in the scene represents a square patch of forest floor 10 m on a side. Priya's NGO pulls these scenes free of charge from three live public portals: the **USGS EarthExplorer** archive (`earthexplorer.usgs.gov`), the **Sentinel-2 Level-2A Cloud-Optimized GeoTIFF archive on AWS Open Data** (`registry.opendata.aws/sentinel-2-l2a-cogs`), and the **Copernicus Data Space Ecosystem** (`dataspace.copernicus.eu`) (SEE APPENDIX A). Because the two scenes covering Kutai in a given month are sometimes captured on Sentinel-2's ascending orbital pass and sometimes on its descending pass, the pixel-column order can run in opposite directions between them — a fact Appendix A explains and Appendix B's polygon coordinates depend on.

Priya has exactly two ways to register this month's scene to last month's before the alert map ships:

**Fast Lock** shifts the entire new scene by a whole number of pixels — left/right, up/down — until it lines up with last month's scene as closely as a whole-pixel shift allows. It runs in about 20 minutes of Priya's time, mostly spent launching the automated tool and checking its output (MA5, SEE APPENDIX D) — the computation itself takes only seconds — but because real ground features rarely sit on an exact pixel boundary, it can leave true features misaligned by as much as one full pixel width (SEE APPENDIX C).

**True Lock** resamples the new scene to sub-pixel precision using a set of **surveyed ground control points (GCPs)** — real, fixed features on the ground whose coordinates are known independently of the satellite (SEE APPENDIX B). It removes almost all of that pixel-width smear, but the tie-point work — visually locating and marking each control point by hand in both scenes — takes about 4 hours of Priya's time (MA6, SEE APPENDIX D) — time that also has to cover every other concession she monitors this month (SEE APPENDIX D). Every hour Bilal's trucks sit fueled and idle in the yard costs the program money it does not have twice (SEE APPENDIX D).

The tree line and the one surveyed ground control point Priya will register against are given in **APPENDIX B**. The accuracy standards that define how far a whole-pixel shift can be off are in **APPENDIX C**. Analyst time and field-dispatch costs are in **APPENDIX D**. Any stated scenario assumptions are in **APPENDIX E**. The vocabulary and "how to…" skills this case will ask of you are listed in **APPENDIX F** — that is where Challenge 1 sends you. Every figure in this case is sourced or disclosed as an assumption in **APPENDIX G**.

She has to submit one alert map.

---

## Dilemma

You are Priya Anand.

Do you:

**A.)** Run **Fast Lock** — register this month's scene to last month's with a whole-pixel shift, ready in minutes **OR**

**B.)** Run **True Lock** — register it with sub-pixel resampling against surveyed ground control points, ready by evening

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A coordinate-plane plot of the Kutai tree-line polygon** (Appendix B) as it appears in last month's reference scene and in this month's scene under **Fast Lock's** whole-pixel shift. Label the translation vector you applied, and state — with a written argument, not just a claim — whether the shifted polygon is *congruent* to the original ground shape or only *similar* to it.
  *Why this lens fits:* a whole-pixel shift only ever slides the grid — it never rotates, resizes, or reflects it — so the congruent-vs-similar question here really reduces to whether a pure translation can carry one polygon onto the other. A translation always preserves size and shape, which is exactly why that one written argument is enough to settle D1's question either way.
- **D2 — The same polygon redrawn under True Lock's sub-pixel resampling.** Sub-pixel resampling can very slightly rescale a polygon's grid coordinates as well as shift them; compute that scale factor and show it. State, with your numbers, whether the resampled polygon is congruent or merely similar to the original, and how you can tell the difference.
  *Why this lens fits:* unlike D1's pure shift, True Lock's resampling can introduce a real dilation, so congruence can't be assumed here the way it could for a whole-pixel shift — you have to actually measure whether corresponding side lengths still come out in a 1:1 ratio (congruent) or some other constant ratio (similar) before you can say which term applies.
- **D3 — A reflection step.** Appendix A explains that the archived reference scene and this month's alert scene were captured on opposite Sentinel-2 orbital passes, so the tree-line polygon's pixel-column order runs in opposite directions between the two. Before D1 and D2's overlay can mean anything, reflect one scene's polygon across the y-axis of the shared pixel grid. Show the reflected coordinates next to the originals.
  *Why this comes before D1 and D2's overlay, not after:* translation and dilation reasoning only mean something once both polygons are expressed in the same frame of reference. Comparing two scenes whose pixel columns run in opposite directions without reflecting one of them first would overlay a mirror image of the tree line against the real one — any shift or scale factor computed from that pairing wouldn't describe the actual ground feature at all.
- **D4 — A ground-control-point placement.** Plot Appendix B's surveyed ground control point on the scene's local pixel-coordinate grid, with the scene's center as the origin. State which quadrant it falls in, and explain — using Appendix C — why True Lock's correction differs depending on which quadrant a given ground feature sits in.
  *Why quadrant identification is the step that matters here:* Appendix C's accuracy figures describe how well a registration method performs in general, not at one specific spot. Naming the quadrant is what connects that scene-wide standard to a single, checkable point — the same correction method can behave differently depending on where in the scene a given feature happens to fall.
- **D5 — A results table and recommendation.** For each option, compute hectares of falsely-flagged "new clearing" per analyst-hour spent on registration: the misregistration ribbon's area (from D1's or D2's shift, in pixels converted to hectares) divided by the analyst-hours each method costs (Appendix D). Recommend one option, in writing, using this ratio — not the raw time or the raw area alone.
  *Why a rate, and why it's worth rereading Appendix D and E together before you compute it:* a rate is what lets you compare two options whose errors and time costs are both differently sized, on the same footing. But "the analyst-hours each method costs" isn't just a per-scene number sitting in Appendix D in isolation — Appendix D also frames those hours against Priya's *fixed monthly* registration budget, and Appendix E's sensitivity note spells out exactly why that framing is a judgment call D5 itself asks you to make, not one already made for you. Decide deliberately whether your ratio's denominator is one scene's hours or what those hours actually cost against that shared monthly budget, and say which you chose and why.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A: Satellite Scenes & the Three Free Portals

Sentinel-2 is a two-satellite European Space Agency constellation. Its finest-resolution optical bands (visible and near-infrared) have a native ground sample distance of 10 meters [S1]; its other bands are coarser (SEE table below).

| Sentinel-2 band group | Ground resolution | Bands |
|---|---|---|
| Visible + NIR (finest) | 10 m [S1] | B2 (Blue), B3 (Green), B4 (Red), B8 (NIR) |
| Red-edge / SWIR (mid) | 20 m [S1] | B5, B6, B7, B8A, B11, B12 |
| Atmospheric (coarsest) | 60 m [S1] | B1 (Coastal aerosol), B9 (Water vapor), B10 (Cirrus) |

Priya's NGO pulls scenes free of charge, with no purchase and no subscription, from three live public sources:

- **USGS EarthExplorer** — `https://earthexplorer.usgs.gov/` — free search and browsing needs no account; download requires a free EROS Registration System (ERS) account (no cost) [S2].
- **Sentinel-2 Level-2A Cloud-Optimized GeoTIFFs on AWS Open Data** — `https://registry.opendata.aws/sentinel-2-l2a-cogs/` — free, no AWS account required, `--no-sign-request` public access to the `s3://sentinel-cogs` bucket (`us-west-2`) [S3].
- **Copernicus Data Space Ecosystem** — `https://dataspace.copernicus.eu/` — free instant access to Sentinel data, browsing needs no account [S4].

**Ascending vs. descending passes.** Sentinel-2 flies a sun-synchronous orbit (786 km altitude, 98.6° inclination) crossing the equator at 10:30 local solar time on its descending (northbound-to-southbound) node [S5]. A satellite in this kind of orbit crosses a given point on the ground twice in its repeat cycle: once heading roughly north (an *ascending* pass) and once heading roughly south (a *descending* pass). A scene captured on one pass and a scene captured on the other can have their pixel-column (sample) order running in opposite directions relative to true north — which is why Challenge D3 asks you to reflect one polygon before comparing it to the other.

> *Note: this case does not require you to download or process any actual satellite raster. The portals above are the real places this analysis would start; the specific scene pair, coordinates, and accuracy figures Priya works with are given directly in Appendices B and C so the case does not depend on any one file remaining online.*

---

## Appendix B: The Kutai Tree-Line Polygon & Ground Control Point

Every coordinate below is in the scene's native 10 m pixel grid (MA1, MA2 — SEE APPENDIX E for basis).

| Item | Value |
|---|---|
| Tree-line polygon vertices, last month's reference scene (pixel-grid coordinates) | (400, 600), (720, 600), (720, 680), (400, 680) |
| Tree-line polygon vertices, this month's scene, pre-registration (pixel-grid coordinates) | (403.4, 597.7), (723.4, 597.7), (723.4, 677.7), (403.4, 677.7) |
| Tree-line polygon vertices, this month's scene, after **True Lock** sub-pixel resampling (pixel-grid coordinates) | (407.6, 607.3), (727.2, 607.3), (727.2, 687.0), (407.6, 687.0) |
| One surveyed ground control point, local pixel-grid coordinates (origin at scene center) | (+1,500, −2,200) |
| Scene footprint width and height, pixels (10 m band) | 10,980 × 10,980 pixels (≈ 100 km × 100 km ground footprint) [S6] |

> *Sources: [S6] gives the real Sentinel-2 tile/pixel-grid dimensions. The specific tree-line polygon and ground-control-point coordinates above are a stated scenario (MA1, MA2 — SEE APPENDIX E) built to that real pixel scale, not a literal downloaded scene — consistent with the note above that this case does not require processing an actual raster. [S9] and [S10] describe the real, general kind of data (tropical-forest edge density; public geodetic ground-control networks) this scenario represents.*

---

## Appendix C: Registration Accuracy Standards

| Quantity | Value |
|---|---|
| Sentinel-2 Level-2A absolute geolocation accuracy (published spec) | < 12 m at 95.5% confidence [S7] |
| Typical whole-pixel (nearest-neighbor) coregistration residual error | < 5 m (0.5 pixel) at 95.5% confidence [S7] |
| Typical sub-pixel, GCP-based coregistration residual error (RMSE) | ≈ 3 m (0.3 pixel) (MA3 — SEE APPENDIX E) |

> *Source: [S7] (ESA/Copernicus Sentinel-2 Level-2A product data-quality specification) gives the first two figures directly. [S8] establishes the real, published benchmark (registration accuracy under 0.2 pixel is needed to hold land-cover change-detection error under 10%) that the third figure — a stated Modeling Assumption, MA3 — is bounded against.*

---

## Appendix D: Analyst-Hours & Field-Dispatch Cost

Priya monitors Kutai and 4 neighboring concession blocks — 5 scenes to register every month.

| Quantity | Value |
|---|---|
| Priya's total monthly analyst-hours available for registration work, across all concessions she monitors | 1 hour 40 minutes (100 minutes) (MA4 — SEE APPENDIX E) |
| Analyst-hours per scene, Fast Lock (whole-pixel shift) | 20 minutes (MA5 — SEE APPENDIX E) |
| Analyst-hours per scene, True Lock (sub-pixel GCP resampling) | 4 hours (MA6 — SEE APPENDIX E) |
| Cost per field-enforcement dispatch (fuel, crew time, vehicle) sent to a falsely-flagged clearing | $180 (MA8 — SEE APPENDIX E) |

> *Source: [S11] (a wildlife-conservation cost overview citing $150–$300/scout/month for salary and rations, and $25,000–$30,000/year for a 14-scout patrol unit) informs MA8's basis; it is a general conservation-cost figure, not a Kutai-specific or per-dispatch study, and does not enter the D5 calculation directly (SEE APPENDIX E).*

---

## Appendix E: Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case author. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis |
|---|---|---|---|
| MA1 | Kutai tree-line polygon shape and length | A 320-pixel × 80-pixel (3,200 m × 800 m) rectangle (SEE APPENDIX B) | No single public GPS polygon for this exact tile is fetchable without downloading and processing a real raster, which this case deliberately avoids (SEE APPENDIX A note). Built to the real 10 m pixel scale [S1] and informed by [S9]'s finding that tropical forest edges are extremely dense (nearly 50 million km worldwide; 19% of tropical forest area lies within 100 m of an edge) — a multi-kilometer edge segment within one monitored tile is realistic. |
| MA2 | Ground control point location | (+1,500, −2,200) pixels from scene center | A representative placement inside the one quadrant of this month's scene that is clear enough to survey; no Kutai-specific GCP network could be fetched, but [S10] confirms real public geodetic ground-control networks of exactly this kind exist. |
| MA3 | True Lock's achieved sub-pixel registration RMSE | 3 m (0.3 pixel) | Bounded between [S8]'s published 0.2-pixel (2 m) threshold for reliable change detection and [S7]'s published 0.5-pixel (5 m) whole-pixel residual — a real GCP tie-point workflow reduces error well below whole-pixel level but real GCP-survey and manual-placement error keeps it from hitting the literature's ideal exactly. **Sensitivity: HIGH** — this is one of the two directly load-bearing figures in D5's per-scene ratio. |
| MA4 | Priya's total monthly analyst-hours budgeted for the registration step, across all 5 concessions | 100 minutes (1 h 40 min) | Set equal to exactly 5 scenes × MA5's 20 minutes — i.e., her fixed registration-specific time budget covers Fast Lock everywhere with zero slack. Registration is a small slice of her month; interpretation, QA, and field coordination (Background) consume the rest. **Sensitivity: HIGH.** |
| MA5 | Analyst-hours per scene, Fast Lock | 20 minutes | Automated whole-pixel coregistration is compute-bound (seconds), but a real workflow also requires the analyst to launch the tool and visually QA its output before shipping an alert map. **Sensitivity: HIGH.** |
| MA6 | Analyst-hours per scene, True Lock | 4 hours | Manual GCP tie-point identification is a per-point human task, not a compute-bound one — a real, well-documented distinction in GIS/photogrammetry workflows (e.g., GRASS GIS `i.rectify` and ArcGIS Pro's ortho-mapping GCP tools both require the analyst to visually locate and mark each point). Several GCPs, each requiring cross-identification and QC across both scenes, plausibly total to most of a working morning. **Sensitivity: HIGH.** |
| MA7 | Number of concessions sharing Priya's fixed monthly registration budget | 5 total (Kutai + 4 neighboring blocks) | Matches Background's "Kutai concession and several neighboring blocks." **Sensitivity: HIGH — this is the case-defining assumption; see Sensitivity note below.** |
| MA8 | Cost per field-enforcement dispatch | $180 | Informed by [S11]'s real $150–$300/scout/month figures, scaled up for a multi-scout crew's single round-trip fuel and labor cost (a monthly salary figure is not the same unit as a per-trip cost, so this is a disclosed scaling, not a direct citation). Does not enter the D5 hectares-per-analyst-hour calculation; narrative and Appendix D context only. |
| MA9 | True Lock sub-pixel resampling scale factor (Appendix B) | 0.9985, applied to the reference polygon about the scene center | A representative, realistically small affine scale correction of the kind real sub-pixel resampling introduces away from a tile's processing origin — not itself measured from a real raster (SEE APPENDIX A note). Not load-bearing for D5's ratio, which uses the residual distance in meters directly. |

**Sensitivity note (MA4/MA5/MA6/MA7 together).** MA4's 100-minute monthly registration budget is set exactly equal to 5 scenes × MA5's 20 minutes, with zero slack. Spending MA6's 4 hours on any one scene therefore exceeds that entire monthly budget on its own, before any other concession is touched. How much that matters depends on what you assume happens to the other 4 concessions' scenes that month — and that is exactly the kind of judgment call Challenge D5 asks you to make explicit, not one this appendix makes for you.

---

## Appendix F: "How To…" Math Questions To Research

**Vocabulary**

Congruent · Similar · Quadrant · Transformation · Translation · Dilation · Scale Factor · Coordinate Plane · Origin

**How to…**

- How to reflect a figure across the Y-Axis
- How to translate a figure on the coordinate plane
- How to dilate a figure on the coordinate plane given a scale factor

---

## Appendix G: Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Sentinel-2 finest/mid/coarse band groups and resolutions | 10 m (B2,B3,B4,B8); 20 m (B5,B6,B7,B8A,B11,B12); 60 m (B1,B9,B10) | Copernicus Data Space Ecosystem — [Sentinel-2 documentation](https://documentation.dataspace.copernicus.eu/Data/SentinelMissions/Sentinel2.html); corroborated by [Wikipedia — Sentinel-2](https://en.wikipedia.org/wiki/Sentinel-2) | accessed 2026-09-12 | HIGH |
| S2 | USGS EarthExplorer: free browsing, free-account download | Free (account required only to download) | [USGS EarthExplorer](https://earthexplorer.usgs.gov/) | accessed 2026-09-12 | MEDIUM |
| S3 | Sentinel-2 L2A COGs on AWS Open Data: free public bucket | `s3://sentinel-cogs`, `us-west-2`, `--no-sign-request` | [AWS Open Data Registry — Sentinel-2 L2A COGs](https://registry.opendata.aws/sentinel-2-l2a-cogs/) | accessed 2026-09-12 | HIGH |
| S4 | Copernicus Data Space Ecosystem: free instant access | Free, no account needed to browse | [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/) | accessed 2026-09-12 | HIGH |
| S5 | Sentinel-2 orbit geometry | Sun-synchronous, 786 km altitude, 98.6° inclination, 10:30 LTDN (descending node) | [eoPortal — Copernicus Sentinel-2](https://www.eoportal.org/satellite-missions/copernicus-sentinel-2) | accessed 2026-09-12 | MEDIUM |
| S6 | Sentinel-2 tile/granule size at 10 m resolution | 10,980 × 10,980 pixels (≈100 km × 100 km, 109.8 km × 109.8 km with overlap) | [Copernicus Data Space Ecosystem — Sentinel-2 documentation](https://documentation.dataspace.copernicus.eu/Data/SentinelMissions/Sentinel2.html) | accessed 2026-09-12 | MEDIUM |
| S7 | Sentinel-2 Level-2A absolute geolocation accuracy and multitemporal co-registration accuracy | < 12 m (absolute), < 5 m (multitemporal), both at 95.5% confidence | [Copernicus — Sentinel-2 Collection 1 MSI Level-2A](https://sentinels.copernicus.eu/sentinel-data-access/sentinel-products/sentinel-2-data-products/collection-1-level-2a) | accessed 2026-09-12 | HIGH |
| S8 | Registration accuracy needed for reliable change detection | < 0.2 pixel (1/5 pixel) registration accuracy needed to hold change-detection error under 10% | Dai, X. & Khorram, S. (1998). "The effects of image misregistration on the accuracy of remotely sensed change detection." *IEEE Transactions on Geoscience and Remote Sensing*, 36(5), 1566–1577. Accessed via [Semantic Scholar](https://www.semanticscholar.org/paper/The-effects-of-image-misregistration-on-the-of-Dai-Khorram/72eb9dc9b75176327afb0cfea5617b9f36ec85aa) | accessed 2026-09-12 | MEDIUM |
| S9 | Tropical forest edge density | ~50 million km of tropical forest edge worldwide; 19% (295 million ha) of tropical forest area is within 100 m of an edge | Brinck, K. et al. (2017). "High resolution analysis of tropical forest fragmentation and its impact on the global carbon cycle." *Nature Communications*, via [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5357863/) | accessed 2026-09-12 | MEDIUM |
| S10 | Real public geodetic ground-control-point network (illustrative, not Kutai-specific) | NOAA's National CORS Network (NCN), continuously operating GNSS reference stations | [NOAA National Geodetic Survey — CORS](https://geodesy.noaa.gov/CORS/) | accessed 2026-09-12 | MEDIUM |
| S11 | General conservation-patrol staffing cost (not a per-dispatch figure; informs MA8 only) | $150–$300/scout/month; $25,000–$30,000/year for a 14-scout unit | [Donate to Wildlife Conservation — Conservation Costs](https://www.donatetowildlifeconservation.com/conservation-costs/) | accessed 2026-09-12 | LOW |

All 11 sources above were fetched and confirmed live on 2026-09-12.

---

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
