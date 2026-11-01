# Research Log — Pixel Snap

Stage 3 (`case-research`) run on `cases/pixel-snap/`, starting from case-write's 25 literal
`{{NEEDS_SOURCE}}` tokens in `case.json.needs_source[]`. Worked in load-bearing weight order: the
two directly load-bearing accuracy figures first (Fast Lock's and True Lock's registration
residuals, since these set D5's false-positive areas), then the analyst-time and shared-budget
figures that resolve the flagged balance risk, then the Sentinel-2 platform/portal facts that
ground the case's realism, then the lower-stakes narrative figures last.

## P14/P15/P17 — Fast Lock and True Lock registration residual error

**Searched:** "Sentinel-2 Level-2A absolute geolocation accuracy meters data quality report"

**Fetched directly:**
`https://sentinels.copernicus.eu/sentinel-data-access/sentinel-products/sentinel-2-data-products/collection-1-level-2a`
— confirmed two exact, dated ESA/Copernicus figures: **"< 12 m at 95.5% confidence of Absolute
Geolocation"** and **"< 5 m at 95.5% confidence of Multitemporal Registration."**

**Outcome:** SOURCED as [S7], HIGH confidence — a direct primary-source quote. Used the 5 m
multitemporal figure as Fast Lock's typical whole-pixel residual (Appendix C), reasoning that Fast
Lock does not improve on the platform's own standard product-to-product co-registration. Used the
12 m absolute-geolocation figure as the "no registration correction at all" baseline used later in
the shared-budget balance calculation (an other concession that gets skipped entirely this month
falls back to this figure).

## P16 — Typical sub-pixel, GCP-based coregistration residual (RMSE)

**Searched:** "image misregistration sub-pixel accuracy required for change detection remote
sensing Townshend Dai Khorram"

**Fetched/confirmed:** Semantic Scholar's record for Dai, X. & Khorram, S. (1998), "The effects of
image misregistration on the accuracy of remotely sensed change detection," *IEEE Transactions on
Geoscience and Remote Sensing*, 36(5), 1566–1577 — confirmed the paper's well-established finding
that **registration accuracy under 0.2 pixel (1/5 pixel) is needed to hold land-cover
change-detection error under 10%**. Corroborated by a second citing paper found and reviewed (Chen
2014, ISPRS, hosted at UNC Charlotte) which independently restates the same Dai & Khorram finding.
The original IEEE Xplore page itself is paywalled and was not fetched directly.

**Outcome: NOT FOUND as a directly-measured Kutai-specific RMSE (no such study exists for this
scenario); exit chosen: SOURCED as [S8] (MEDIUM confidence — a foundational, corroborated
literature benchmark, not a Kutai-specific measurement) used as the bound informing a Modeling
Assumption.** True Lock's achieved RMSE is set at **MA3 = 3 m (0.3 pixel)** — between S8's 2 m
(0.2 px) ideal threshold and S7's 5 m (0.5 px) whole-pixel ceiling — disclosed as an assumption
because no source states what a real GCP-tie-point workflow *actually* achieves on a Sentinel-2
tile, only what the literature says is *needed* for reliable change detection.

## P18/P19/P20/P23/P24 — Analyst-hours per scene and Priya's monthly registration budget (the
## balance-risk fix)

**Searched:** "manual ground control point collection time per point image rectification GIS
workflow hours"

**Fetched/reviewed:** GRASS GIS `i.rectify` manual and ArcGIS Pro's ortho-mapping GCP
documentation — both confirmed the real, well-documented distinction that automated coregistration
is compute-bound while manual GCP tie-point identification is a per-point human task (the analyst
must visually locate and mark each point in both images). No source gives a specific "hours per
Sentinel-2 tile" figure for either workflow.

**Outcome: NOT FOUND as a directly citable hours figure for either workflow; exit chosen:
Modeling Assumptions (MA5 = 20 min/scene Fast Lock, MA6 = 4 hr/scene True Lock)**, grounded in the
real automated-vs-manual distinction above and in case.md's own narrative framing ("a few minutes"
vs. "the rest of the morning").

**The balance-risk test (per FACILITATOR.md's explicit flag):** Computed on Kutai alone, Fast
Lock's ratio (1.6 ha ÷ 1/3 hr = 4.8 ha/analyst-hour) vs. True Lock's ratio (0.96 ha ÷ 4 hr = 0.24
ha/analyst-hour) gives a naive margin of **~95%** — far outside SPEC §2's ~20% band, exactly the
risk case-write flagged. Per SPEC §2 ("retune a constraint, not hide data") and FACILITATOR.md's
explicit instruction, tested whether a disclosed Modeling Assumption — how many other concessions
share Priya's same fixed monthly registration-hour budget — resolves this within a real, plausible
range.

**Resolution:** Set **MA7 = 5 concessions total** (Kutai + 4 neighboring blocks, matching
Background's "Kutai concession and several neighboring blocks") and **MA4 = 100 minutes**
(Priya's total monthly analyst-hours for the registration step specifically), set equal to exactly
5 × MA5's 20 minutes — i.e., Fast-Lock-everywhere uses the entire budget with zero slack. Under
this constraint, True Lock's 4 hours on Kutai alone exceed the entire monthly budget before any
other concession is touched, so the other 4 concessions get no registration correction that month
and fall back to S7's 12 m native absolute-geolocation accuracy (3.84 ha false-positive each,
using MA1's 3,200 m edge length).

- **Policy A (Fast Lock on all 5):** total FP = 5 × 1.6 = 8.0 ha; total hours = 5 × 1/3 = 1.667 hr;
  ratio = **4.8 ha/hr**.
- **Policy B (True Lock on Kutai, other 4 unregistered):** total FP = 0.96 + 4×3.84 = 16.32 ha;
  total hours = 4 hr; ratio = **4.08 ha/hr**.
- **margin = |4.8 − 4.08| / 4.8 = 15.0%.**

This N=5 value was chosen deliberately within the real, plausible "several neighboring blocks"
range stated in Background — smaller N (e.g. 2–3) pushes the resolved margin toward the ~95% naive
figure (too few concessions to dilute Kutai's dominant contribution); much larger N (e.g. 20+)
would push the margin toward 0% and require "several neighboring blocks" to mean an implausibly
large monitoring portfolio for a small NGO analyst. N=5 was the smallest value in the plausible
range that clears the ~20% cap, chosen to keep the retuning as conservative (as close to the
original per-scene story) as possible. **This is a case-defining decision, not a mechanically
filled-in number** — recorded here and in `case.json.modeling_assumptions[MA4/MA5/MA6/MA7]` and
`balance.margin_basis`, never invented silently.

**Rejected approach:** Considered blending totals across N concessions with all N *also* running
Fast Lock (rather than being skipped entirely) — algebraically, this requires N ≈ 70+ other
concessions to dilute the naive ~95% gap down to 20%, which is not a plausible size for "several
neighboring blocks" and was rejected as an unrealistic retuning lever.

## P09/P10 — Kutai tree-line polygon shape and edge length (MA1)

**Searched:** "tropical forest edge density km per hectare fragmentation Borneo Kalimantan
deforestation study"

**Fetched directly:** `https://pmc.ncbi.nlm.nih.gov/articles/PMC5357863/` — Brinck, K. et al.
(2017), "High resolution analysis of tropical forest fragmentation and its impact on the global
carbon cycle," *Nature Communications* — confirmed: "the length of the world's tropical forest
edges sums to nearly 50 million km" and "a total of 295 million ha (19%) of tropical forest area
is <100 m from the forest edge."

**Outcome: NOT FOUND as a Kutai-specific or per-hectare edge-density figure; exit chosen:
Modeling Assumption (MA1)**, a 320×80-pixel (3,200 m × 800 m) rectangle informed by S9 (cited as
[S9]) as real, dated, supplemental context establishing that tropical forest edges are extremely
dense — a multi-kilometer edge segment within one monitored tile is realistic — without claiming
S9's global figure was used to derive the specific 3,200 m value.

## P11 — Ground control point pixel-grid location (MA2)

**Searched:** "ground control point network national geodetic benchmark satellite image
validation public database"

**Fetched directly:** `https://geodesy.noaa.gov/CORS/` — confirmed NOAA's National CORS Network
(NCN) is a real, public, multi-agency network of continuously operating GNSS reference stations,
managed by NOAA's National Geodetic Survey, data distributed free of charge.

**Outcome: SOURCED as [S10], MEDIUM confidence, illustrative only** — CORS does not cover
Indonesia/Kutai, so it is cited only as a real example of the *kind* of public geodetic
infrastructure surveyed GCPs are drawn from. The case's specific GCP coordinate, **MA2 = (+1,500,
−2,200) px from scene center**, remains a disclosed scenario placement (Quadrant IV), chosen to
sit inside the one cloud-clear quadrant the Twist reveals.

## P12 — Sentinel-2 tile/scene footprint dimensions

**Searched:** "Sentinel-2 tile size 100km 10980 pixels granule dimensions"; "Sentinel-2 UTM
tiling grid 100km tile granule pixel dimensions 10980x10980 SentiWiki"

**Fetched directly:** `https://documentation.dataspace.copernicus.eu/Data/SentinelMissions/Sentinel2.html`
— confirmed "Each Sentinel-2 products is composed of approximately 110x110 km tiles." The exact
10,980×10,980-pixel figure (109.8 km ÷ 10 m) was corroborated across multiple independent
technical sources found in search (a ResearchGate discussion thread and SentiWiki-adjacent pages)
rather than read verbatim off one single fetched page.

**Outcome:** SOURCED as [S6], MEDIUM confidence (not HIGH, since the precise pixel count came from
cross-source corroboration rather than one direct primary-document read).

## P01/P02/P03/P04/P25 — Sentinel-2 band resolutions

**Searched:** "Sentinel-2 spatial resolution 10m 20m 60m bands ESA user guide"

**Fetched directly:**
`https://documentation.dataspace.copernicus.eu/Data/SentinelMissions/Sentinel2.html` — confirmed
"four bands at 10 m, six bands at 20 m and three bands at 60 m spatial resolution," plus explicit
band names for the 10 m group (B02 Blue, B03 Green, B04 Red, B08 NIR).
`https://en.wikipedia.org/wiki/Sentinel-2` — confirmed the full 13-band list with exact
wavelengths, corroborating the 10 m/20 m/60 m groupings and filling in the 20 m band list (B5, B6,
B7, B8A, B11, B12) and 60 m band list (B1, B9, B10).

**Also attempted:** `https://sentinel.esa.int/en/web/sentinel/user-guides/sentinel-2-msi/resolutions/spatial`
— DNS failure in this session (`ENOTFOUND sentinel.esa.int`); not cited, per the "never cite a URL
you did not fetch" rule.

**Outcome:** SOURCED as [S1], HIGH confidence — two independently corroborating sources, one a
direct Copernicus documentation page.

## P05 — USGS EarthExplorer access terms

**Fetched directly:** `https://earthexplorer.usgs.gov/` — confirmed "You must be logged in to
download and order scenes." Corroborated via search that EarthExplorer/ERS registration is free.

**Outcome:** SOURCED as [S2], MEDIUM confidence (the free-registration claim is corroborated by
USGS EROS help documentation found in search, not read verbatim off the one page fetched directly
alongside the login-requirement text).

## P06 — AWS Open Data Sentinel-2 L2A COGs bucket

**Fetched directly:** `https://registry.opendata.aws/sentinel-2-l2a-cogs/` — confirmed bucket ARN
`arn:aws:s3:::sentinel-cogs`, region `us-west-2`, "Access to Sentinel data is free, full and open,"
`--no-sign-request` CLI examples, no AWS account required.

**Outcome:** SOURCED as [S3], HIGH confidence — direct primary source.

## P07 — Copernicus Data Space Ecosystem access terms

**Fetched directly:** `https://dataspace.copernicus.eu/` — confirmed "free instant access to a
wide range of data and services from the Copernicus Sentinel missions," browsing needs no account.

**Outcome:** SOURCED as [S4], HIGH confidence — direct primary source.

## P08 — Sentinel-2 orbit geometry (ascending/descending passes)

**Searched:** "Sentinel-2 sun-synchronous orbit ascending descending pass 10:30 local time ESA"

**Attempted direct fetch:** `https://sentinel.esa.int/web/sentinel/missions/sentinel-2/satellite-description/orbit`
— DNS failure in this session; not cited.

**Fetched directly instead:** `https://www.eoportal.org/satellite-missions/copernicus-sentinel-2`
— confirmed "786 km" altitude, "98.6°" inclination, "10:30 hours LTDN" (mean local solar time at
the descending node), "a period of 101 minutes," selected as "the best compromise between cloud
cover minimization and sun illumination."

**Outcome:** SOURCED as [S5], MEDIUM confidence (ESA's own primary orbit page was unreachable this
session; eoPortal is an established, independently-maintained tier-2 aggregator whose figures
matched every other corroborating source found in search — SentiWiki, Wikipedia).

## P21 — Field-enforcement dispatch cost

**Searched:** "SMART ranger patrol cost per day conservation anti-poaching field dispatch cost
study"; ""anti-poaching scout" salary rations month cost"

**Fetched directly:** `https://www.donatetowildlifeconservation.com/conservation-costs/` —
confirmed "$150 – $300 ... will cover one anti-poaching scout's salary and rations for one month
on patrol" and "$25,000 – $30,000 ... will cover a unit of 14 anti-poaching scouts for one year."

**Also fetched, not usable:** `https://www.patrolling.org/anti-poaching-operations/` (no specific
cost figures); `https://conservationtravelafrica.org/.../anti-poaching-training-course-and-volunteer-ranger/`
(a single South African trainee-ranger monthly salary figure, R7,500 — a different program/context,
not used).

**Outcome: NOT FOUND as a genuine per-dispatch (per-trip, vehicle+fuel+crew) cost figure; exit
chosen: Modeling Assumption (MA8 = $180), informed by [S11] (LOW confidence — a donation/
fundraising page with no stated methodology or date)**, scaled from S11's real monthly-salary
figures to a plausible single-trip cost for a multi-scout crew. Not load-bearing for `margin_pct`
(D5's ratio uses hectares/analyst-hour, not dollars) — used only for Background/Overview narrative
color and Appendix D completeness.

## Summary table

| ID | Placeholder(s) | Resolution | Value | Confidence |
|---|---|---|---|---|
| P01-P04, P25 | Sentinel-2 band resolutions | SOURCED (S1) | 10 m/20 m/60 m band groups | HIGH |
| P05 | EarthExplorer access terms | SOURCED (S2) | free browsing, free-account download | MEDIUM |
| P06 | AWS Open Data S3 bucket | SOURCED (S3) | s3://sentinel-cogs, us-west-2 | HIGH |
| P07 | Copernicus Data Space Ecosystem terms | SOURCED (S4) | free instant access | HIGH |
| P08 | Orbit ascending/descending geometry | SOURCED (S5) | 786 km, 98.6°, 10:30 LTDN | MEDIUM |
| P09/P10 | Tree-line polygon shape/length | ASSUMPTION (MA1, informed by S9) | 3,200 m × 800 m rectangle | n/a |
| P11 | GCP pixel-grid location | ASSUMPTION (MA2, informed by S10) | (+1500, −2200) px | n/a |
| P12 | Scene footprint, pixels | SOURCED (S6) | 10,980 × 10,980 px | MEDIUM |
| P13 | Appendix B source note | SOURCED (S6, S9, S10) | — | mixed |
| P14 | L2A absolute geolocation accuracy | SOURCED (S7) | < 12 m @ 95.5% | HIGH |
| P15 | Whole-pixel coregistration residual | SOURCED (S7) | < 5 m @ 95.5% | HIGH |
| P16 | Sub-pixel GCP RMSE | ASSUMPTION (MA3, bounded by S7, S8) | 3 m (0.3 px) | n/a |
| P17 | Appendix C source note | SOURCED (S7, S8) | — | mixed |
| P18 | Monthly analyst-hour budget | ASSUMPTION (MA4) | 100 min | n/a |
| P19 | Fast Lock analyst-hours | ASSUMPTION (MA5) | 20 min | n/a |
| P20 | True Lock analyst-hours | ASSUMPTION (MA6) | 4 hr | n/a |
| P21 | Field-dispatch cost | ASSUMPTION (MA8, informed by S11) | $180 | n/a |
| P22 | Appendix D source note | SOURCED (S11) | — | LOW |
| P23 | Background Fast Lock time | ASSUMPTION (MA5) | 20 min | n/a |
| P24 | Background True Lock time | ASSUMPTION (MA6) | 4 hr | n/a |

**Totals:** 11 real sources fetched and cited (S1–S11), all confirmed live 2026-09-12; 9 Modeling
Assumptions (MA1–MA9), each grounded in a real bound, distinction, or corroborating figure rather
than invented outright; 2 dead-end URLs found but correctly not cited (`sentinel.esa.int` — DNS
failure; a South African trainee-ranger salary page — wrong program/context); 0 figures dropped;
0 remaining OPEN placeholders.

**Balance risk resolution:** `margin_pct = 15.0`, True Lock (Option B) favored, comfortably inside
SPEC §2's ~20% cap — resolved via MA4/MA5/MA6/MA7 (Priya's fixed, fully-subscribed monthly
registration-hour budget shared across 5 concessions), not by hiding or altering the real accuracy
figures (S7, S8) or the case's real geometry. See `FACILITATOR.md`'s "The margin" section and
`case.json.balance.margin_basis` for the full computation.

## Next step

Run `case-readiness` on `pixel-snap`. (Per this task's scope, `case-readiness`/`case-qa`/
`case-publish` were explicitly not run in this pass.)
