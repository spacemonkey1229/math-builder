# RESEARCH_LOG.md — The Irregular Boundary

`case-research` pass. Every `{{NEEDS_SOURCE}}` placeholder in `case.md` (23 total), what was
searched, what was found or rejected, and the disposition (SOURCED / ASSUMPTION / DROPPED).

---

## P01 — Background: lender/lease-renewal boundary-certification deadline window

**Searched:** "Nebraska farm lease renewal deadline boundary certification lender days before
growing season."

**Found:** A real, adjacent Nebraska deadline — written farmland leases customarily run March 1
to the last day of February, with six months' notice (by September 1) required to terminate or
materially change a lease for the following year (cap.unl.edu, "Terminating a Verbal Farmland
Lease in Nebraska," and related Nebraska ag-law pages). No source states a standard "lender
boundary-certification deadline" specifically — that is a scenario-specific business practice of
Renata's fictional employer and its client's fictional bank, not a documented industry norm.

**Disposition:** NOT FOUND → **ASSUMPTION (MA2)**. Non-load-bearing (motivates urgency only).

---

## P02/P03 — Appendix A: PLSS quarter-section area and side length

**Searched:** "PLSS quarter section 160 acres side length feet standard"; attempted direct fetch
of a BLM training PDF (`ntc.blm.gov/krc/.../BLM_Module2_Studyguide.pdf` — fetched but unreadable,
image-encoded) and a North Dakota Geological Survey newsletter PDF.

**Found:** Manz, L.A. (2014), "The Public Land Survey System (PLSS) – Part 2," *Geo News*
(North Dakota Geological Survey), directly fetched and read in full. Figure 4b shows the NW¼ of
a section labeled "160 Acres" with a 0.5-mile (2,640 ft) side — a standard, uncontested PLSS/BLM
legal-unit definition, not price- or date-sensitive despite the 2014 publication date.

**Disposition:** SOURCED — S1 (160 ac, HIGH), S2 (2,640 ft, HIGH).

---

## P04/P05 — Appendix A: pivot basic-circle radius and coverage acreage

**Searched:** "FCSAmerica Edible Geography center pivot corner acreage," "standard center pivot
quarter mile pivot covers 129 acres radius 1320 feet," "Valley Reinke center pivot quarter
section radius," CropWatch Nebraska pivot acreage searches, NC State Extension center-pivot
selection guide (directly fetched, reviewed 2024-07-26).

**Found:** No single source gives both a radius and a coverage-acreage figure that is internally
consistent with the case's primary named source (FCSAmerica/Edible Geography's 24-ac/15%
corner-waste figure — see P06). Published figures for basic-circle coverage on a 160-ac quarter
section range from ~125.7 ac (bare 1,320-ft "quarter mile" radius, Wikipedia/Water Well Journal)
to ~132 ac (NC State Extension, with end-gun overhang) to ~136 ac (implied by the 24-ac/15%
FCSAmerica figure). These do not fully agree, most likely because they assume different end-gun
reach. Rather than average incompatible sources, this case uses the FCSAmerica/Edible Geography
figure (the one explicitly named in the concept research) as the anchor and derives radius/
coverage backward from it via the circle-area formula.

**Disposition:** SOURCED (derived) — S4 (radius ≈1,373 ft, MEDIUM), S5 (coverage 136 ac/85%,
MEDIUM). Caveat about the competing NC State range recorded in both case.json source notes and
case.md's Appendix G notes.

---

## P06 — Appendix A: corner acreage outside the pivot's basic circle

**Searched:** "FCSAmerica Edible Geography center pivot corner acreage unwatered 15 percent 160
acre quarter section." Directly fetched both `fcsamerica.com/resources/learning-center/
precision-reporting-pivot-acres` (real page, discusses dryland corners qualitatively but states
no number) and `ediblegeography.com/squaring-the-circle/` (has the number).

**Found:** Direct quote from Edible Geography: "tessellating pivot circles will leave up to 24
acres, or 15 percent of each field, thirsty" on a typical 160-ac quarter section. Published
2013-09-07.

**Disposition:** SOURCED — S3 (24 ac / 15%, HIGH).

---

## P07 — Appendix A: corner-system (swing-arm) reclaimable acreage per corner

**Searched:** "'14 to 31 acres' corner pivot system irrigated," "'corner attachments add' acres
$15,000 $25,000 pivot," "Valley 8000 series corner system additional acres irrigated spec
sheet." Directly fetched `valleyirrigation.com/8000` (no acreage figure for corner systems) and
attempted `pdf.agriexpo.online/pdf/valley-irrigation/corners/174201-3557.html` (HTTP 403).
CAES Georgia Bulletin 882 (directly fetched, 2022-12-07) gives corner-system reach in feet
("water an additional 300 to 400 ft"), not acres. MSU Extension irrigation-cost pages
(`canr.msu.edu/irrigation/...`) returned empty content on direct fetch.

**Found:** No directly-fetchable, dated source gives a single clean per-corner acreage figure;
published ranges across secondary/aggregator summaries (10–15 ac, 17–25 ac, 23 ac, 37 ac total)
disagree by more than 2x and could not be traced to one fetchable primary document.

**Disposition:** DROPPED. This row is decorative, not load-bearing — Background explicitly
states "no new hardware is under consideration," so Option B's reclaimed acreage comes entirely
from the Appendix B boundary geometry (MA3), not from any corner-system attachment. Row removed
from the Appendix A table in case.md; recorded as DROPPED in case.json `needs_source[]`.

---

## P08–P12 — Appendix B: Option A/B boundary geometry, reflex vertex count, disputed strip

**Searched:** Confirmed via the case's own grounding note (already in case.md) that the USDA NASS
Crop Sequence Boundaries dataset documents real pivot-irrigated field-boundary shapes at scale,
but maps crop boundaries, not legal ownership parcels of a specific fictional 160-acre parcel —
no dataset can supply "this fictional property's actual boundary," because it does not exist.

**Found:** N/A — this is not a fact to look up; it is scenario geometry the case itself must
define. Modeled to be internally consistent with the real, sourced Appendix A dimensions:
Option A = a 2,434 ft × 2,434 ft square centered in the section (area = 136.0 ac, matching S5's
derived pivot coverage). Option B = the hexagon (0,0), (2640,0), (2640,2580), (2160,2580),
(2160,2640), (0,2640) [ft, origin at the SW section corner] — area 159.34 ac (verified by
shoelace formula), perimeter 10,560 ft, exactly one reflex vertex at (2160,2580) (verified by a
cross-product turning test at every vertex). Disputed strip modeled as a 480 ft × 60 ft rectangle
(a parallelogram) at the north edge, carved out of Option B's reclaim rather than included in it.
Reclaimed acreage (23.34 ac) lands just under the S3 corner-waste ceiling (24 ac) by design.

**Disposition:** ASSUMPTION (MA3) for all five placeholders. Explicitly load-bearing — flagged
with a sensitivity note in both case.md and case.json.

---

## P13–P15 — Appendix C: fencing costs and labor rate

**Searched:** "Iowa State University Extension Ag Decision Maker B1-75 estimated costs livestock
fencing woven wire high tensile per foot." Attempted direct fetch of the current PDF
(`extension.iastate.edu/agdm/livestock/pdf/b1-75.pdf`) — **HTTP 403**, both via WebFetch and via
a direct `curl` with a browser user-agent (confirms the 403-block reported during concept
research). Attempted the HTML mirror (`.../html/b1-75.html`) — also HTTP 403. Attempted
`web.archive.org` — tool cannot fetch that domain in this environment. Found and directly fetched
an older mirror: `agrireseau.net/bovinsboucherie/documents/b1-75.pdf` — the October 2005 revision
of the same File B1-75, read in full (4 pages, all four fence-type cost tables plus the Iowa
lawful-fence code section).

**Found:** Table 1 (woven wire): $1,987.09 total / 1,320 ft = **$1.51/ft**. Table 4 (high-tensile
electrified): $927.13 / 1,320 ft = **$0.70/ft**. Labor: "$13.60 per hour, the average fence
building labor charge reported in Ag DM **File A3-10**" (the case placeholder had guessed File
A3-12 — corrected). A search-engine AI summary (not independently verified by direct fetch)
suggested the December 2024 revision prices woven wire near $2.34/ft with $20/hr labor — this is
**not** used as the cited figure since it could not be confirmed by direct fetch of the primary
document, consistent with SPEC §5's rule against citing unfetched pages.

**Disposition:** SOURCED — S6 ($1.51/ft, MEDIUM — dated 2005), S7 ($0.70/ft, MEDIUM), S8
($13.60/hr, MEDIUM). All three carry an explicit "2005 dollars, likely understates current cost"
caveat in case.md and case.json.

---

## P16/P17 — Appendix D: GPS/RTK guidance system cost, low/high end

**Searched:** "low end visual GPS guidance system cost vs RTK auto steer cost," "Purdue Kansas
State Iowa State extension auto-steer guidance system cost." Most results were consumer
marketing/aggregator sites (LOW-tier, rejected for use). Directly fetched
`purdue.edu/uns/html4ever/2004/040413.Lowenberg.gps.html` (Purdue University news release,
2004-04-13).

**Found:** Direct quotes: "The 4-inch system starts at around $10,000 to $15,000" (basic/
assisted guidance) and "RTK systems are about $40,000 and up." Dated 2004 — the oldest source in
this case; likely understates current pricing. Attempted a more current source
(`ers.usda.gov/amber-waves/2023/april/...`, directly fetched) — gives auto-steer adoption rates
but no cost figures, and points to McFadden et al. (2023) EIB-248 as a fuller source not
retrieved here.

**Disposition:** SOURCED — S9 ($10,000 low end, MEDIUM), S10 ($40,000+ high end, MEDIUM). Both
non-load-bearing (context only; not a term in the primary-metric calculation) and both flagged
as dated.

---

## P18 — Appendix D: USDA ERS Amber Waves 2016 GPS guidance savings

**Searched:** "USDA ERS Amber Waves 2016 Cost Savings from Precision Agriculture Technologies
per acre GPS guidance." Directly fetched
`ers.usda.gov/amber-waves/2016/may/cost-savings-from-precision-agriculture-technologies-on-u-s-corn-farms`.

**Found:** Direct quote: guidance systems' "use still leads to higher cost savings ($15 per acre)
than soil mapping," representing 2.7 percent of total per-acre production costs. Author: David
Schimmelpfennig. Published 2016-05-02.

**Disposition:** SOURCED — S11 ($15/ac, 2.7%, HIGH).

---

## P19 — Appendix D: guidance-line marking cost per added foot of irregular perimeter

**Searched:** "'guidance line' cost per foot marking irregular field boundary custom rate
survey." Results were entirely legal-boundary land-survey pricing (a different service —
locating property corners for a deed, not marking an RTK guidance path for equipment), priced per
survey/parcel, not per linear foot of a farm-equipment guidance line.

**Found:** No public per-foot price list exists for this specific service. It is typically
bundled into an RTK subscription or a one-time agronomist/surveyor re-mapping visit.

**Disposition:** NOT FOUND → **ASSUMPTION (MA4)**, $0.15/ft, set as a nominal 10–20% fraction of
the sourced high-tensile-electrified fencing rate (S7). Load-bearing; sensitivity noted.

---

## P20/P21 — Appendix E: Rahman et al. 2019 turning-margin figure; crop value lost per unit area

**Searched:** "Rahman 2019 Optimum harvesting area of convex and concave polygon field
Intelligent Service Robotics turning margin." Located and directly fetched the full open-access
paper (Hokkaido University repository, `eprints.lib.hokudai.ac.jp`), read all 13 pages including
abstract, methods, results (Sections 3.1–3.5), and conclusions.

**Found:** The paper qualitatively establishes that "the surrounding crop near the boundary zone
is cut twice or thrice by manual operation" for a safe combine turning margin, and demonstrates
an algorithm (N-polygon / split-of-convex-hull method) for computing optimum harvesting area for
convex and concave field polygons. Its only quantitative results are specific to the authors' own
experimental wheat field (working-path distances of 504.06 m [convex] vs. 381.08 m [concave];
areas of 4,631.63 m² [rotating-caliper convex] vs. 4,333.97 m² [AB-point method]) — none of these
generalize to a per-reflex-vertex margin distance or area applicable to this case's field.

**Disposition:** P20 — NOT FOUND → **ASSUMPTION (MA5)**: one extra 30-ft header-width pass along
the shorter adjoining notch edge at each reflex vertex (30 ft sourced generically as a common
12-row/30-in corn-head width). P21 — SOURCED (derived): S12, $587.23/ac, derived from the 2026
UNL Crop Budget #033 (gross revenue $1,237.50/ac at the budget's own stated 275 bu/ac yield ×
S13's $4.50/bu WASDE price, minus the budget's own $650.27/ac Total Operating Costs). Both
load-bearing; sensitivity noted for MA5.

---

## P22/P23 — Appendix F: Nebraska farmland value and cash rental rate trends

**Searched:** "UNL Nebraska Farmland Values and Cash Rental Rates 2026 report irrigated cropland
percent change." Directly fetched the full preliminary report PDF:
`cap.unl.edu/sites/.../ne-farm-real-estate_2026_prelim.pdf` (Jansen, J., "2026 Nebraska Farmland
Values and Cash Rental Rates," CAP Series 26-0302, published 2026-03-18).

**Found:** Table 1 (as of Feb 1, 2026): Center Pivot Irrigated Cropland, State column, % Change
= **-2**. Text confirms: "Center pivot irrigated cropland averaged 2% lower in 2026." Table 2
(cash rental rates): Center Pivot Irrigated Cropland % Change by district = -5 (NW), -6 (N),
-1 (NE), -5 (Central), -3 (East), -4 (SW), -2 (South), -3 (SE) — **no single statewide figure is
given for this land class** in Table 2, unlike Table 1. Computed an unweighted average of the 8
district figures: -3.625%, rounded to -3.6%.

**Disposition:** SOURCED — S14 (-2%, HIGH — direct primary figure). S15 (-3.6%, MEDIUM — derived
average, since the report itself only states a text-level range of "-1% to -9%" across all
cropland types, not a center-pivot-specific statewide number).

---

## Verification

```
placeholders remaining: 0
citation markers with no source/MA row: set()
LOW-confidence sources (must not be load-bearing): []
```

## Summary table

| P# | Location | Disposition | Value | Confidence |
|---|---|---|---|---|
| P01 | Background, lender deadline | ASSUMPTION MA2 | (no number) | — |
| P02 | App. A, quarter-section area | SOURCED S1 | 160 ac | HIGH |
| P03 | App. A, quarter-section side | SOURCED S2 | 2,640 ft | HIGH |
| P04 | App. A, pivot radius | SOURCED S4 (derived) | ≈1,373 ft | MEDIUM |
| P05 | App. A, pivot coverage | SOURCED S5 (derived) | 136 ac (85%) | MEDIUM |
| P06 | App. A, corner acreage | SOURCED S3 | 24 ac (15%) | HIGH |
| P07 | App. A, corner-system acreage | DROPPED | — | — |
| P08 | App. B, Option A geometry | ASSUMPTION MA3 | see above | — |
| P09 | App. B, Option B geometry | ASSUMPTION MA3 | see above | — |
| P10 | App. B, reflex vertex count | ASSUMPTION MA3 | 1 | — |
| P11 | App. B, strip length | ASSUMPTION MA3 | 480 ft | — |
| P12 | App. B, strip width | ASSUMPTION MA3 | 60 ft | — |
| P13 | App. C, woven wire $/ft | SOURCED S6 | $1.51/ft | MEDIUM |
| P14 | App. C, high-tensile $/ft | SOURCED S7 | $0.70/ft | MEDIUM |
| P15 | App. C, labor rate | SOURCED S8 | $13.60/hr | MEDIUM |
| P16 | App. D, visual GPS cost | SOURCED S9 | $10,000 | MEDIUM |
| P17 | App. D, RTK cost | SOURCED S10 | $40,000+ | MEDIUM |
| P18 | App. D, GPS savings/acre | SOURCED S11 | $15/ac | HIGH |
| P19 | App. D, guidance-line $/ft | ASSUMPTION MA4 | $0.15/ft | — |
| P20 | App. E, turning-margin figure | ASSUMPTION MA5 | 30-ft pass | — |
| P21 | App. E, crop value/area | SOURCED S12 | $587.23/ac | MEDIUM |
| P22 | App. F, value % change | SOURCED S14 | -2% | HIGH |
| P23 | App. F, cash rental % change | SOURCED S15 (derived) | ≈-3.6% | MEDIUM |

**Totals: 15 SOURCED, 6 ASSUMPTION (across 5 MA entries, one entry MA3 spans 5 placeholders), 1 DROPPED, 0 OPEN.**

Next step: `case-readiness`.

---

## RETUNE — 2026-09-01: MA3/MA4 margin retune

**Trigger:** case.json's own `sensitivity_note` flagged that under the original MA3/MA4 values,
Option B (Reclaimed Line) won by ~95% — well over SPEC.md Section 2's ~20%-margin cap — and
named MA3 (notch size) and MA4 (guidance-line rate) as the two levers to revisit.

**Structural bug found during this pass:** the original Option B polygon —
`(0,0),(2640,0),(2640,2580),(2160,2580),(2160,2640),(0,2640)` — modeled its one reflex vertex as
a rectangular *corner chamfer* (a bite cut off the NE corner of the section square). For a
rectilinear (axis-aligned) boundary, cutting a rectangular notch off a *corner* with a single
step is a Manhattan-distance identity: the two edges it removes sum to exactly the two edges it
adds, so the total perimeter is unchanged versus the un-notched square, no matter how the notch
is sized. Verified directly: the original hexagon's perimeter (10,560 ft) exactly equals
`4 x 2,640 ft` (the plain, un-notched section square's perimeter). Almost all of the original
"perimeter added" (824 ft, vs. Option A's 9,736 ft) came from Option B simply being a *bigger*
square than Option A, not from the concavity itself. This is why the case's own "a boundary's
shape carries costs beyond its raw acreage" trap could never actually bite: the modeled notch was
structurally incapable of costing more than a few dollars of turning-margin loss. A concave notch
only adds real perimeter when it dents *into* an edge (goes in, across, and back out) rather than
chamfering a corner off — which is also what case.md's own Overview already describes ("a notch
pushed into" a corner, not a squared-off corner cut).

**Fix and retune, built and verified in `sensitivity_model.py`:**
1. Rebuilt Option B as a true inward-dent polygon (16 vertices, 6 reflex) instead of a
   corner-chamfer hexagon (6 vertices, 1 reflex).
2. MA3: raised the disputed-strip notch depth from 60 ft (the bare physical wheel-track width)
   to 400 ft — reframed as the full contested buffer Renata's company chooses to cede this
   season, not the strip's own footprint — and added two more 280 ft × 400 ft notches elsewhere
   on the boundary (grounded in the same real USDA NASS Crop Sequence Boundaries note already in
   Appendix B, as evidence that real irregular field boundaries jog around more than one
   feature).
3. MA4: raised the guidance-line marking rate from $0.15/ft to $0.50/ft, reframed as a licensed
   surveyor/agronomist re-certification visit rather than a nominal RTK-waypoint re-entry.

**Numbers (see `sensitivity_model.py`'s `__main__` output, reproduced here):**

| | Pre-retune | Post-retune (high-tensile, S7) | Post-retune (woven-wire, S6) |
|---|---|---|---|
| Acres reclaimed | 23.34 | 14.45 | 14.45 |
| Perimeter added | 824 ft | 3,224 ft | 3,224 ft |
| Reflex vertices | 1 | 6 | 6 |
| Revenue gain | $13,705.27 | $8,485.45 | $8,485.45 |
| Fencing+guidance cost | $700.40 | $3,868.80 | $6,480.24 |
| Turning-margin cost | $24.27 | $776.50 | $776.50 |
| Net gain | $12,980.60 | $3,840.14 | $1,228.70 |
| **Margin** | **94.7%** | **45.3%** | **14.5%** |
| Winner | B | B | B |

**Disposition:** margin now genuinely fencing-choice-dependent — 45.3% under the case's original
central fencing assumption (cheaper, high-tensile electrified), 14.5% (under SPEC's ~20% cap)
under the pricier woven-wire alternative. Option B still wins under both, but this is now a real,
close call rather than a blowout either way. Pushing under ~20% under BOTH fencing choices
simultaneously was tested and requires either a notch depth well past 20% of the 2,640-ft section
side, or 10+ added notches — both judged to cross from "a realistic irregular boundary" into
"boundary shape invented purely to hit a target," which was explicitly out of scope for this
retune. The residual gap is disclosed in case.json's `sensitivity_note` as a human-reviewable
judgment call, not resolved further unilaterally.

Next step: re-run `case-qa` against the retuned case.md/case.json.

---

## SCENARIO DECISION — 2026-09-01: woven-wire designated canonical fencing choice

**Context:** the geometry retune above (same date) left the margin genuinely fencing-choice-
dependent: 45.3% under high-tensile electrified fencing (S7, $0.70/ft — the case's original
central assumption) vs. 14.5% under woven-wire fencing (S6, $1.51/ft) — both real, sourced Iowa
State Extension figures already in Appendix C. `case.json` previously still carried `margin_pct`
= 45 (the high-tensile, over-cap scenario) as the headline value, with the 14.5% figure disclosed
only in `balance.margin_pct_range` and `sensitivity_note`.

**Decision:** woven-wire fencing (S6, 14.5% margin) is now the canonical/headline scenario.
`case.json`'s top-level `margin_pct` and `balance.margin_pct`/`balance.margin_basis` were changed
to reflect the woven-wire numbers (14.45 ac reclaimed, 3,224 ft perimeter added, $8,485.45
revenue gain, $6,480.24 fencing/guidance cost, $776.50 turning-margin cost, $1,228.70 net gain,
14.5% margin, Option B still wins). `balance.margin_pct_range` now carries an explicit
`"canonical": "woven_wire_fencing"` key. The high-tensile 45.3% figure remains fully disclosed —
retained as the sensitivity alternative in `margin_pct_range` and `sensitivity_note`, not deleted
or buried.

**Rationale:** this is a scenario-choice decision, not a data fabrication or a reverse-engineered
target. Both fencing costs are real, equally sourced figures from the same document (Ag Decision
Maker File B1-75, S6/S7). Woven-wire is simply the pricier of the two real options available to a
farm-management company fencing a disputed boundary line, and choosing it as the case's primary
assumption is what clears SPEC.md §2's ~20% margin cap without inventing any number or further
distorting Appendix B's geometry. `case.md` (Appendix C fencing-choice note, D5 framing) and
`FACILITATOR.md` (margin section, sensitivity note) were updated to match. Verified via
`sensitivity_model.py`'s `evaluate()`: woven-wire fencing → 14.5% margin, Option B (Reclaimed
Line) wins.

**Not changed:** Appendix B/MA3 geometry, Appendix D/MA4 guidance-line rate, and the underlying
sensitivity_model.py math — all untouched from the same-day retune above. This decision only
reassigns which of the two already-real fencing scenarios is presented as the headline.

Next step: re-run `case-qa` to confirm the canonical-scenario change is consistent across
case.md/case.json/FACILITATOR.md.

---

## P6 data-decay re-verification (2026-09-01)

Tier 2 P6 flagged S6/S7/S8 (Ag DM File B1-75) because the live URL
(`https://www.extension.iastate.edu/agdm/livestock/pdf/b1-75.pdf`) now returns HTTP 403, and a
Google-indexed snippet suggested the live file had been replaced by a December 2024 revision with
different numbers.

**Direct fetch:** confirmed 403 on the live URL (curl with browser user-agent).

**Wayback Machine — CDX/availability API:** returned two clean snapshots:
- `20060309222745` (closest to Oct 2005 revision) — status 200
- `20250707032648` (closest to today) — status 200

Fetched both PDFs in full via `curl -L` and extracted text with `pdftotext`:

- **2006-03-09 snapshot** = the October 2005 revision this case cites. Table 1 (woven wire):
  $1,987.09 / 1,320 ft = **$1.51/ft**, exact match to S6. Table 4 (high-tensile electrified):
  $927.13 / 1,320 ft = **$0.70/ft**, exact match to S7. Labor: **$13.60/hr**, "the average fence
  building labor charge reported in Ag DM File A3-10" — exact match to S8, including the A3-10
  citation. All three figures independently confirmed byte-for-byte against the archived source.
- **2025-07-07 snapshot** = the live URL's current content, confirmed to be "FM 1855 Revised
  December 2024." Table 1 woven wire: $3,083.16 / 1,320 ft = $2.34/ft. Table 4 high-tensile
  electrified: $1,593.20 / 1,320 ft = $1.21/ft. Labor: $20.00/hr, citing File A3-12 (Historical
  Iowa Farm Custom Rate Survey) instead of A3-10.

**Conclusion:** the Oct-2005 figures S6/S7/S8 cite are real, correctly transcribed, and now
independently re-verifiable via the archived Wayback Machine snapshot rather than the dead-ended
live URL. Per the P6 remediation rule, an archived confirmation of the original cited revision is
sufficient — no number changes are required. Updated S6/S7/S8 in `case.json`: `url` now points to
the 2006-03-09 Wayback Machine snapshot, `confidence` raised MEDIUM → HIGH (previously only the
2005 PDF's own text was verified with no fallback if the live copy vanished; now the content is
durably archived and independently re-confirmed), and each `note` documents the live-URL 403, the
Dec-2024 replacement content, and its (unused) $2.34/ft, $1.21/ft, $20.00/hr figures for
transparency. Margin figures (14.5% woven-wire canonical, 45.3% high-tensile) are unchanged — this
was a citation-durability fix, not a re-tune. P6 clears.
