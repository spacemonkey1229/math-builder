# Concept sheet — Satellite Imagery & Remote Sensing (`remote-sensing`)

**Target and why.** `readmodel/domains.json`'s `remote-sensing` entry is HIGH authoring priority,
HIGH data grade, and **0 existing cases** — the domain's own `n_uncovered_signature_skills` is 0
(its 14 signature skills, e.g. `geometry-transformation`, `geometry-translation`, are all already
covered by other cases at n>2), so no concept here can claim a true zero-coverage hole. Per this
session's confirmed spine-wide sweep (zero skills anywhere at true n==0), I scored against
`gap_queue.json`'s thin (n≤2) convention instead, and cross-checked every candidate skill live
against `standards_spine.json` rather than trusting `gap_queue.json`'s group-level counts. **Cross-check
result: no drift found this time** — the four spine groups below (Geometry/Transformations,
Geometry/Coordinate Plane, Geometry/Visual Perceptibility, Geometry/Perimeter And Area,
Statistics And Probability/Displaying Data, Statistics And Probability/Data Analysis) all matched
`gap_queue.json`'s `n_gap`/`n_total` exactly when I pulled the live per-skill list.

| # | Concept | Score | Tier | Group(s) fully thin-closed |
|---|---|---|---|---|
| C1 | Pixel Snap | **6.8** | T2 | Geometry/Transformations (3/3 remaining); Geometry/Coordinate Plane (1/1) |
| C2 | The Revisit Gap | **4.56** | T3 | Statistics And Probability/Displaying Data (3/3); Statistics And Probability/Data Analysis (1/1) |
| C3 | The Calibration Panel | **2.52** | T2 | Geometry/Visual Perceptibility (3/3) |
| C4 | The Pivot Claim | **2.52** | T2 | Geometry/Perimeter And Area (1/1) |

**Recommendation.** Write **C1, Pixel Snap** first: highest score, HIGH feasibility (all three named
sources confirmed live this session), closes two full spine groups with a dilemma that is
*organically* remote sensing's own signature problem (image registration), not a borrowed one.
Write **C2, The Revisit Gap** second — it matches `domains.json`'s decision archetype #1 verbatim
and closes two more full groups, but I could not confirm a public, concrete commercial-imagery
price figure this session (Planet's and Sentinel Hub's public pricing pages returned no rendered
numbers — JS-gated or 404), so it is graded MEDIUM, not HIGH, and `case-research` should either find
a real number or reframe the "commercial" side as a disclosed Modeling Assumption. Between **C3**
and **C4** (tied at 2.52), prefer **C3** if only one more is written: ground-control calibration
targets are core photogrammetry, not an ag/insurance case wearing a remote-sensing costume. **Kill
C4** for this round unless a insurance/ag data source is found — I did not attempt to source specific
crop-insurance payout data, so its economics would be entirely a stated assumption, thinner than
the other three.

---

### C1 — Pixel Snap   ·   score 6.8   ·   tier T2

**Protagonist.** Priya Anand, a deforestation-monitoring analyst for a rainforest conservation NGO,
who has to sign off on this month's forest-loss alert map before it goes to the field-enforcement
team.

**The dilemma.** A.) Register this month's scene to last month's using a whole-pixel shift (fast —
minutes of compute, but can leave real ground features misaligned by up to a full pixel) OR
B.) register it using sub-pixel resampling against surveyed ground control points (accurate, but
takes hours of manual tie-point work before the alert map can ship).

**Primary metric.** Hectares of falsely-flagged "new clearing" (registration-error false positives)
per analyst-hour spent on registration — a ratio, because a method that takes zero time but floods
the enforcement team with false alerts isn't actually faster in any way that matters.

**Why it's close.** The whole-pixel method is nearly free and catches every large clearing fine —
but a one-pixel misregistration at a 10 m Sentinel resolution smears every field edge and tree-line
into a false "change" ribbon, and enforcement teams that chase enough false alerts stop trusting the
system. Sub-pixel registration removes that ribbon almost entirely, but the tie-point work has a
real, unavoidable labor cost that scales with how many scenes ship per month. Neither option is
obviously right until both are counted in the same units.

**Would close (4 skills, 1 how-to / 3 term, all currently n=2):**

| id | kind | label | n | group closed |
|---|---|---|---|---|
| geometry-congruent | term | Congruent | 2 | Transformations — 1 of 3 remaining thin |
| geometry-similar | term | Similar | 2 | Transformations — 1 of 3 remaining thin |
| geometry-how-to-reflect-a-figure-across-the-y-axis | how-to | How to reflect a figure across the Y-Axis | 2 | Transformations — 1 of 3 remaining thin (closes group 3/3) |
| geometry-quadrant | term | Quadrant | 2 | Coordinate Plane — 1/1 remaining thin (closes group) |

*(`geometry-how-to-reflect-a-figure-across-the-y-axis` is genuinely forced here: an ascending-pass
scene and a descending-pass scene of the same ground track can be mirror-imaged relative to each
other, and a student has to reflect one before the two can even be compared for translation/scale.)*

**Already-covered skills it also exercises.** `geometry-transformation` / `geometry-translation` /
`geometry-dilation` / `geometry-scale-factor` / `geometry-how-to-translate-a-figure-on-the-coordinate-plane`
/ `geometry-how-to-dilate-a-figure-on-the-coordinate-plane-given-a-scale-factor` (all n>2 already —
these are the domain's own signature skills and the heart of the registration math, just not
scored because they're no longer thin) — this is *the* natural home for this case, not a stretch.

**Data feasibility: HIGH.** Named sources confirmed live this session:
- USGS EarthExplorer (`https://earthexplorer.usgs.gov/`) — confirmed live; free Landsat archive
  search/download with scene metadata (login required only for download, not browsing).
- Sentinel-2 on AWS Open Data (`https://registry.opendata.aws/sentinel-2-l2a-cogs/`) — free,
  cloud-optimized GeoTIFFs, no account needed (per `domains.json`, cross-checked, not re-fetched
  independently this session since the AWS Open Data registry entry itself is the source of truth).
- Copernicus Data Space Ecosystem (`https://dataspace.copernicus.eu/`) — confirmed live this
  session; explicitly offers "free instant access" to Sentinel data, browsing needs no account.

Not confident about: a real, named pair of same-ground-track scenes with a known, disclosed
sub-pixel registration error — `case-research` will likely need to pick two real scenes and compute
(or reasonably model) the misregistration itself, disclosed as the case's own analysis rather than
a claimed external figure.

**Sensitivity (SPEC §6).** None required — an operational/technical decision, no personal stakes.

**Split risk.** None — 4 scored skills plus a full signature-skill arc (translate/dilate/scale
already covered), one coherent registration-then-difference deliverable.

---

### C2 — The Revisit Gap   ·   score 4.56   ·   tier T3

**Protagonist.** Marcus Oduya, the same kind of conservation NGO's deforestation-monitoring analyst
(different program), who has to recommend a 12-month imagery subscription to the board before the
budget locks.

**The dilemma.** A.) Subscribe to 3 m commercial imagery on a weekly cadence OR B.) rely on free
10 m Sentinel-2 imagery on its ~5-day revisit — for the same deforestation-alert program.
(`domains.json`'s decision archetype #1, verbatim.)

**Primary metric.** Hectares of confirmed illegal clearing detected per dollar of annual imagery
cost — a ratio, since the free option is not "free" once missed early-warning windows are counted,
and the paid option is not obviously worth it if its finer resolution barely changes what actually
gets caught.

**Why it's close.** A box-and-whisker plot of detection lag (days between an actual clearing event
and its first confirmed alert) across many past events would show the finer, more frequent
commercial feed catching things sooner on average — but with real spread, because clouds and tasking
gaps hit both feeds. The minimum clearing patch size each resolution can reliably detect is a
*non-linear* function of pixel size (detectability falls off faster than linearly as patch size
approaches pixel size), so "3x the resolution" doesn't mean "3x smaller detectable clearing." A line
of best fit through cost vs. cumulative hectares monitored for each plan is what actually settles
which option is cheaper per hectare-year — not the sticker price.

**Would close (4 skills, 3 how-to / 1 term, all currently thin):**

| id | kind | label | n | group closed |
|---|---|---|---|---|
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data | how-to | How to create a box and whisker plot given a set of data | 1 | Displaying Data — closes group 3/3 |
| statistics-and-probability-non-linear | term | Non-linear | 2 | Displaying Data — 1 of 3 |
| statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data | how-to | How to draw a line of best fit given a set of data | 2 | Displaying Data — 1 of 3 |
| statistics-and-probability-how-to-find-a-missing-data-element-given-the-mean-and-the-remaining-elements-of-its-set | how-to | How to find a missing data element given the mean and the remaining elements of its set | 1 | Data Analysis — closes group 1/1 |

*(The missing-element skill is forced by a disclosed data gap: one month's commercial invoice line
is illegible/withheld in the released billing sheet, but the annual mean monthly cost is stated —
the student solves for the redacted month, not a decorative bonus problem.)*

**Already-covered skills it also exercises.** `statistics-and-probability-scatter-plot` /
`how-to-create-a-scatter-plot-given-a-set-of-data` (n=9, plotting raw detection-lag data before
summarizing); `measurement-how-to-convert-an-amount-from-one-unit-to-another-unit` (n high,
converting km² coverage to hectares).

**Data feasibility: MEDIUM.** Confirmed live this session: USGS EarthExplorer and Copernicus Data
Space Ecosystem both offer the *free* side's imagery with no concrete numbers missing. **Could not
confirm the commercial side**: `https://www.planet.com/pricing/` and
`https://apps.sentinel-hub.com/plans/` both returned no rendered pricing figures (JS-gated content
or a redirect stub); a UP42 marketplace pricing page (`https://up42.com/marketplace/data`) 404'd.
This matches `domains.json`'s own note that sub-metre commercial imagery is "paid except for
disaster-activation releases" with no further detail. **Not confident about:** any specific,
citable commercial per-km² or per-scene price — `case-research` must either locate one (a reseller
data-sheet, an SEC filing, a published academic cost comparison) or state the commercial cost as an
explicit, disclosed Modeling Assumption rather than a cited figure.

**Sensitivity (SPEC §6).** None required.

**Split risk.** None — 4 scored skills, one coherent "which subscription" deliverable arc.

---

### C3 — The Calibration Panel   ·   score 2.52   ·   tier T2

**Protagonist.** Devon Marsh, a photogrammetrist contracted by a state agency to lay out ground
control targets before a scheduled high-resolution tasking pass, so the agency's own imagery can be
radiometrically and geometrically calibrated.

**The dilemma.** A.) Fabricate flat, matte tarp targets in a checkerboard pattern — cheap and fast
to deploy across many sites OR B.) fabricate raised pyramidal corner-reflector targets — more
reliably visible in the image and more durable in wind, but slower and costlier to build per site.

**Primary metric.** Dollars of fabrication material per target that meets the minimum
image-contrast requirement — a ratio, since a target that is technically cheaper per unit area but
needs twice as many replacements per season is not actually the cheaper option.

**Why it's close.** A flat tarp has no faces or edges to catch oblique sun angle, so its contrast in
the image depends entirely on paint reflectance and can wash out at low sun elevation; the
pyramidal target's faces reliably catch light from more sun angles because of its 3-D geometry, but
building it requires cutting and assembling a net of triangular faces, which costs real fabrication
time per unit. Devon has to net out the raw faces the tarp option lacks against the cheaper flat
material it uses.

**Would close (3 skills, 1 how-to / 2 term, all currently n=2, closes Visual Perceptibility 3/3):**

| id | kind | label | n |
|---|---|---|---|
| geometry-face | term | Face | 2 |
| geometry-edge | term | Edge | 2 |
| geometry-how-to-draw-the-net-of-a-3-d-shape | how-to | How to draw the net of a 3-D shape | 2 |

**Already-covered skills it also exercises.** `geometry-area` (n high, per-target material area).

**Data feasibility: MEDIUM.** I did not identify and confirm a specific, live, free ground-control-
target specification document this session (e.g., an ASPRS or USGS calibration-panel technical
manual) — the category is plausible (photogrammetric calibration targets are a standard,
often-published technical topic) but unverified. **Not confident about:** exact panel dimensions,
material costs, and the minimum-contrast threshold — these would likely be disclosed Modeling
Assumptions unless a specific spec sheet is found.

**Sensitivity (SPEC §6).** None required.

**Split risk.** None — 3 skills, one coherent fabrication-comparison deliverable.

---

### C4 — The Pivot Claim   ·   score 2.52   ·   tier T2

**Protagonist.** Renee Castillo, an imagery analyst under contract to a crop-insurance underwriter,
verifying a farmer's storm-damage claim against a policy filing deadline using a satellite
vegetation-index image of the field.

**The dilemma.** A.) File the claim now, treating the damaged area as the full circle swept by the
center-pivot irrigation arm (fast — one circumference/area calculation from the arm's published
radius) OR B.) wait for the next 5-day satellite revisit and trace the actual, irregular concave
damaged boundary pixel-by-pixel (accurate, since the pivot's circle doesn't reach the field's
un-irrigated corners) — risking the policy's filing deadline.

**Primary metric.** Dollars of claim payout per acre of *actually* damaged area — a ratio, because
the circle approximation systematically overstates payout per acre wherever the field's real
boundary cuts concave corners out of the pivot's circle.

**Would close (2 skills, 1 how-to / 1 term, both currently thin):**

| id | kind | label | n | group closed |
|---|---|---|---|---|
| geometry-how-to-find-the-measure-of-the-circumference-of-a-circle | how-to | How to find the measure of the circumference of a circle | 2 | Perimeter And Area — closes group 1/1 |
| geometry-concave | term | Concave | 2 | Quadrilaterals And Polygons — 1 of 11 remaining (no group bonus) |

**Already-covered skills it also exercises.** `geometry-area` (n high, area of the circle and of the
traced irregular boundary).

**Data feasibility: MEDIUM.** Confirmed live this session: the underlying satellite revisit-cadence
sources (Sentinel-2/Copernicus) are the same HIGH-confirmed sources as C1/C2. **Not confident
about:** any real, public crop-insurance payout schedule or a real named farm's pivot geometry —
individual claims data is not public. `case-research` would need to build the case around
disclosed, stated policy terms (a common per-acre payout structure) rather than a real claim.

**Sensitivity (SPEC §6).** One-line flag: storm/fire crop-damage stakes touch a farmer's income —
not severe, but the facilitator should note it is a real financial-hardship frame, not purely
technical.

**Split risk.** None — 2 scored skills is light; `case-write` should lean on the already-covered
`geometry-area` work to keep the deliverable arc substantial, or consider merging with a second,
adjacent decision if research turns up more.
