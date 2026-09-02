# Case Study: The Irregular Boundary

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

Renata Suh drags the last vertex into place and the polygon on her screen finally closes — a lopsided shape with a bite taken out of one corner and a notch pushed into another, laid over a satellite photo of dark, tilled soil. Her coffee's gone cold next to the mouse. Two other windows sit minimized along the bottom of the screen: one is the bank's boundary-certification form, blinking a due date at the top in red. The other is an email thread with a neighboring farm's manager, tone gone from friendly to clipped over the last three messages, about whose fence line a certain pivot's outer wheel track actually crosses.

She pulls up a second file — the same 160-acre quarter-section, but drawn as a clean rectangle, corners left blank and unplanted, nowhere near the disputed strip. Two versions of the same field. Two different answers to the same question: where does the planted boundary actually go this year.

Her cursor hovers between the two file names. Outside the window, the same field waits under an overcast sky, corn stubble from last season still flattened in rows. Renata's manager wants the recommendation memo by end of day — the bank meeting is tomorrow morning. She minimizes the email thread, opens both boundary files side by side, and reaches for her tablet to start the write-up.

---

## Background

Renata Suh is a GIS land-use analyst for a farm-management company operating corn and soybean quarter-sections across Nebraska's pivot-irrigation country. She finalizes the planted-boundary map her company files with the landowner and the landowner's lender each growing season — the map that sets how many acres of "certified planted ground" this field counts as, for both the lease and the loan collateral behind it.

This 160-acre quarter-section (the standard unit these Nebraska fields are surveyed and leased on) sits under a center-pivot irrigation system, and its lease is up for renewal this year. The landlord's bank wants a locked planted-acreage figure to set next year's cash rent before it approves the renewal (Renata's firm treats this as a spring deadline, ahead of the traditional Nebraska lease-year turnover — see Modeling Assumption MA2). At the same time, a neighboring farm's center-pivot has, for several seasons, swung its outermost "tail" span across the disputed corner of this property's line (**SEE APPENDIX B**). Under Nebraska law, ten years of open, continuous, adverse use of another's land can ripen into a legal right to keep using it — this is the season Renata's company wants the boundary settled on paper.

Renata is weighing two ways to draw this year's planted boundary.

**Option A — The Squared Block.** A standard convex rectangular planted block, sized to the pivot's basic circle (**SEE APPENDIX A**), ceding the four corners of the quarter-section as unplanted ground. This block never touches the disputed strip the neighbor's pivot tail crosses, so it never puts Renata's company in the position of asserting a property line the neighbor might contest.

**Option B — The Reclaimed Line.** An irregular, partly concave planted boundary that reclaims corner acreage beyond the pivot's basic circle *and* asserts the property line up to the disputed strip, forcing the boundary question with the neighbor this season.

Both boundaries sit on the same parcel, irrigated by the same fixed pivot equipment (**SEE APPENDIX A**); no new hardware is under consideration. What changes is the boundary's shape — which vertices are convex and which are reflex (concave), and its total perimeter — because shape drives two real costs: guidance-line/fencing cost for a longer perimeter (**SEE APPENDIX C AND APPENDIX D**), and turning-margin crop loss a combine eats at every concave notch (**SEE APPENDIX E**). Lease and rental-rate stakes are in **APPENDIX F**.

Every hard number here is sourced with a citation or, absent a public figure, stated as a Modeling Assumption once research is complete (**SEE MODELING ASSUMPTIONS AND APPENDIX G**). One fact is settled now: the neighbor dispute above is fictional, built for this case, not a real property dispute — see Modeling Assumptions for what is and is not real about it.

The vocabulary this case will ask you to research is listed in Appendix H — that is where Challenge 1 sends you.

---

## Dilemma

You are Renata Suh.

Do you:

**A.)** Draw the Squared Block — a convex rectangular planted boundary sized to the pivot's basic circle, ceding the corners **OR**

**B.)** Draw the Reclaimed Line — an irregular, partly concave planted boundary that reclaims the corners and asserts the property line to the disputed strip

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A labeled diagram of the Squared Block (Option A).** A to-scale sketch of the convex rectangular planted boundary using the pivot dimensions in Appendix A, with every vertex marked and every interior angle shown, and the shape explicitly labeled as a quadrilateral.
- **D2 — A labeled diagram of the Reclaimed Line (Option B).** A to-scale sketch of the irregular, partly concave planted boundary from Appendix B, with every vertex marked, each interior angle classified as convex or reflex (concave), and the full shape explicitly labeled as an irregular polygon.
- **D3 — A disputed-strip classification note.** Using the strip dimensions in Appendix B, identify the shape of the neighbor's pivot-tail crossing strip (a parallelogram of consistent width running along the property line), and mark on your D2 diagram exactly where the Reclaimed Line boundary does or does not touch that strip.
- **D4 — A usable-acreage and perimeter comparison table.** Using your D1 and D2 diagrams and the dimensions in Appendix A and Appendix B, compute the total planted acres inside each option's boundary and the total perimeter (in feet) of each boundary.
- **D5 — A cost-and-loss comparison table.** Using your D4 perimeter figures, the guidance-line and fencing cost data in Appendix C and Appendix D, and the reflex vertices you identified in D2, compute the added guidance-line/fencing cost of the Reclaimed Line over the Squared Block, and the harvest turning-margin crop loss (Appendix E) at each concave notch.
- **D6 — A recommendation**, stated in dollars per acre, combining your D4 acreage gain and your D5 added costs into the case's primary metric, and stating which boundary Renata should finalize before tomorrow's bank meeting.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A — Quarter-Section and Pivot Geometry Spec Sheet

The 160-acre quarter-section this case is set on, and the fixed center-pivot irrigation equipment already installed on it. Neither option changes this equipment — only the planted-boundary line drawn around it.

| Quantity | Value |
|---|---|
| Quarter-section total area, acres | 160 [S1] |
| Quarter-section side length, feet | 2,640 [S2] |
| Center-pivot basic circle radius, feet | ≈1,373 [S4] |
| Center-pivot basic circle coverage, acres | 136 (85%) [S5] |
| Corner acreage outside the pivot's basic circle (unwatered under Option A), acres and percent of quarter-section | up to 24 (15%) [S3] |

Referenced from Background and forces the boundary math in Challenges D1 and D4.

*A row on corner-system (swing-arm) reclaimable acreage per corner was researched and dropped: no directly-fetchable, dated source gave a clean per-corner figure, and this case does not add any corner-system hardware (Background: "no new hardware is under consideration") — the row was decorative context only. See RESEARCH_LOG.md P07.*

---

## Appendix B — Boundary Survey Data: Option A vs. Option B, and the Disputed Strip

Vertex-and-dimension data for both candidate planted boundaries, and for the neighbor's disputed pivot-tail crossing strip.

**RETUNED 2026-09-01** — see the note below the table for why.

| Quantity | Value |
|---|---|
| Option A (Squared Block) boundary vertex coordinates (feet, origin at the quarter-section's southwest corner) | (103, 103), (2537, 103), (2537, 2537), (103, 2537) — a 2,434 ft × 2,434 ft square, centered in the section [MA3] |
| Option B (Reclaimed Line) boundary vertex coordinates, including each reflex (concave) vertex (feet, same origin) | The full 2,640 ft × 2,640 ft section square with three inward notches cut into it (each notch goes *in*, *across*, and *back out* — not a corner cut): (0,0), (100,0), (100,400)\*, (380,400)\*, (380,0), (480,0), (480,400)\*, (760,400)\*, (760,0), (2640,0), (2640,2640), (2480,2640), (2480,2240)\*, (2000,2240)\*, (2000,2640), (0,2640) — \*reflex (concave) vertex [MA3] |
| Number of reflex (concave) vertices on the Option B boundary | 6 (two per notch, three notches) [MA3] |
| Disputed pivot-tail crossing strip — length along the property line, feet | 480 [MA3] |
| Disputed pivot-tail crossing strip — notch depth (buffer ceded beyond the strip's own width), feet | 400 [MA3] |
| Additional boundary notches beyond the disputed strip — count, width, depth | 2 notches, 280 ft wide × 400 ft deep each [MA3] |

Grounding note: field-boundary polygon shapes of this kind are documented at scale in the USDA NASS Crop Sequence Boundaries (CSB) dataset — a real, public, satellite-derived dataset of corn/soybean field boundaries — though CSB maps crop boundaries, not legal ownership parcels, so it is used here only to ground the general shape of a real pivot-irrigated field boundary (genuinely irregular, with more than one concave point), not as a source for this fictional property's specific line. Referenced from Background and forces Challenges D2, D3, and D4.

**Retune note:** the pre-2026-09-01 version of this table modeled Option B with a single reflex vertex cut as a plain rectangular corner notch. For a boundary made only of horizontal/vertical segments, cutting a rectangular bite out of a *corner* this way is a geometric dead end — it always adds exactly as much new edge as it removes, so it cannot add any perimeter at all, no matter how it's sized. That is why the case's original margin never reflected a real "shape has a cost" trade-off. The retuned boundary above instead notches *into* the middle of an edge (in–across–out), which genuinely does add perimeter, and widens the buffer around the disputed strip from 60 ft (the strip's bare physical width) to 400 ft (a deliberate buffer, not the wheel-track itself) while adding two more notches elsewhere on the boundary. See Modeling Assumption MA3 and RESEARCH_LOG.md for the full rationale.

---

## Appendix C — Fencing Cost Basis

Per-foot fencing cost data for marking the planted boundary on the ground.

| Quantity | Value |
|---|---|
| Woven-wire fencing cost per foot, materials and labor | $1.51 [S6] |
| High-tensile electrified fencing cost per foot, materials and labor | $0.70 [S7] |
| Labor rate used in the above figures, USD per hour | $13.60 [S8] |

Referenced from Background and forces Challenge D5. Figures are from the October 2005 revision of Ag Decision Maker File B1-75 — the most recent revision (December 2024) exists but returned an access-denied error on every direct-fetch attempt during research; see RESEARCH_LOG.md P13–P15. Costs are in 2005 dollars and likely understate current cost.

**Fencing choice for D5/D6:** use woven-wire fencing ($1.51/ft [S6]) as the case's primary fencing assumption for your D5 cost table and D6 recommendation — it is the pricier of the two real, sourced options, and it is the one this case's numbers are built around. High-tensile electrified fencing ($0.70/ft [S7]) is a real, equally sourced alternative; if you price your D5/D6 using it instead, note in your appendix how much your margin figure changes, since the two fencing choices genuinely move the answer.

---

## Appendix D — GPS Guidance and RTK System Cost Basis

Cost data for the guidance system needed to drive and maintain a longer, more complex planted-boundary line.

| Quantity | Value |
|---|---|
| Visual GPS guidance system cost, USD | $10,000 (low end) [S9] |
| Automatic RTK steering system cost, USD | $40,000 and up (high end) [S10] |
| Annual per-acre savings from GPS guidance adoption, USD per acre | $15 (2.7% of production costs) [S11] |
| Guidance-line marking cost per added foot of irregular perimeter, USD per foot | $0.50 [MA4] (retuned 2026-09-01; was $0.15) |

Referenced from Background and forces Challenge D5.

---

## Appendix E — Harvest Turning-Margin Crop-Loss Basis

Basis for the extra crop loss a combine driver incurs at each concave (reflex) vertex of an irregular field boundary, from peer-reviewed harvester path-planning research.

| Quantity | Value |
|---|---|
| Extra double-cut turning margin required at a concave (reflex) boundary vertex, as a distance or area figure | one extra 30-ft header-width pass along the shorter notch edge at each reflex vertex [MA5] |
| Crop value lost per unit of double-cut turning-margin area, USD per acre | $587.23 [S12] |

Referenced from Background and forces Challenge D5. Rahman et al. (2019) — "Optimum harvesting area of convex and concave polygon field for path planning of robot combine harvester," *Intelligent Service Robotics* 12(2):167–179 — establishes that crop near a field boundary is manually cut twice or thrice for a safe combine turning margin, but does not publish a generalizable distance or area figure per reflex vertex that transfers to this case; see Modeling Assumption MA5.

---

## Appendix F — Nebraska Farmland Value and Lease-Renewal Context

Real, current market context for why the lease-renewal deadline in Background carries financial weight.

| Quantity | Value |
|---|---|
| Center-pivot irrigated cropland value trend, most recent reporting period, percent change | -2% (statewide, 2026 vs. 2025) [S14] |
| Center-pivot irrigated cropland cash rental rate trend, most recent reporting period, percent change | approximately -3.6% (average across Nebraska's eight reporting districts — the report does not give a single statewide figure for this land class) [S15] |

Referenced from Background; grounds the lease-renewal stakes in Renata's decision. Not itself an input to Challenge 3's calculations.

---

## Modeling Assumptions

> These are stated scenario assumptions, disclosed openly rather than presented as documented
> fact. A Hero may challenge them in discussion; that is a legitimate move.

| # | Assumption | Basis | Sensitivity |
|---|---|---|---|
| MA1 | The specific neighbor pivot-tail dispute described in Background — including that it has been ongoing "for several seasons," that it centers on one particular corner of this property, and the exact timing of the bank's deadline — is a **fictional scenario invented for this case**, not a report of any real, identifiable property dispute or real people. It is anchored to real Nebraska law: an action to establish a lost or disputed boundary or corner is governed by Neb. Rev. Stat. §34-301, and Nebraska's prescriptive-easement rule (ten years of open, continuous, adverse use ripening into a legal right to continue that use) is illustrated in *Mueller v. Bohannon* (Neb. Sup. Ct. 1999). The legal mechanism is real and current; the specific dispute, property, and people in this case are not. | Not load-bearing to any Challenge 3 calculation — the legal grounding motivates *why* Renata is settling the boundary this season, it does not supply a number any deliverable computes with. |
| MA2 | The bank's specific boundary-certification deadline window is a **stated scenario detail**, not a documented industry-standard deadline — no public source states a standard "lender boundary-certification deadline" for Nebraska pivot-irrigated cropland. It is anchored to a real, adjacent Nebraska pattern: written farmland leases customarily run March 1 to the last day of February, with six months' notice (by September 1) required to change or terminate a lease for the following year. | Not load-bearing to any Challenge 3 calculation — motivates why the decision is urgent, supplies no number used in D1–D6. |
| MA3 | The specific vertex coordinates of both boundary options (given in Appendix B), the count/location/depth of Option B's reflex vertices, and the disputed strip's footprint are **modeled figures invented for this fictional 160-acre parcel** — no real GIS boundary exists for a fictional property. **Retuned 2026-09-01:** the boundary now has three genuine inward notches (in–across–out, not corner cuts) instead of one corner-cut notch — a 480 ft × 400 ft notch excluding the disputed strip, plus two more 280 ft × 400 ft notches elsewhere on the boundary — built to be geometrically consistent with Appendix A's real, sourced quarter-section dimensions and its derived pivot-circle coverage. The acreage Option B reclaims (14.45 acres, down from 23.3 pre-retune) stays comfortably under the cited ~24-acre corner-waste ceiling. | Directly load-bearing to D4, D5, and D6 — this geometry sets the acreage-gained and perimeter-added figures the primary metric is built from. Deepening or widening any notch now trades off acreage reclaimed against added perimeter/turning-margin cost in *opposing* directions, which is what makes D6's margin genuinely sensitive to this assumption (see balance/sensitivity_note in case.json and sensitivity_model.py). |
| MA4 | The per-foot cost of establishing/marking an RTK guidance line around an irregular field boundary is **assumed at $0.50 per added foot** (retuned 2026-09-01; was $0.15/ft) — no public per-foot price list exists for this specific service (distinct from the physical fencing priced in Appendix C); reframed as the cost of a licensed surveyor/agronomist re-certification visit, plausible given the live boundary dispute, rather than a routine RTK-waypoint re-entry, while staying below Appendix C's full physical-fencing rates. | Load-bearing to D5/D6, and now materially so: combined with the retuned MA3 geometry, choosing high-tensile-electrified vs. woven-wire fencing (Appendix C) alone moves D6's margin between about 45% (high-tensile) and about 15% (woven-wire — the case's canonical scenario, designated 2026-09-01). Both are real, sourced figures; test both in your own D5/D6 to see how much the fencing choice matters once the notch actually has a real cost. |
| MA5 | At each reflex (concave) vertex of the Reclaimed Line, the harvest turning-margin crop loss is modeled as **one extra 30-foot combine-header-width pass** left uncut along the shorter of the two notch edges meeting at that vertex — a stated proxy for Rahman et al. (2019)'s qualitative finding that boundary crop is manually cut twice or thrice for a safe turning margin; that paper does not publish a generalizable per-vertex distance or area figure. | Load-bearing to D5/D6. With MA3's retuned three-notch, six-reflex-vertex boundary, this term is now several hundred dollars rather than ~$24 — still smaller than the fencing/guidance term, but no longer negligible. |

Further entries will be added here only if `case-research` returns NOT FOUND on a specific `{{NEEDS_SOURCE}}` figure above and a human accepts a stated assumption in its place — never invented at write time.

---

## Appendix G — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | PLSS quarter-section area | 160 acres | North Dakota Geological Survey — Manz, "The Public Land Survey System (PLSS) – Part 2," *Geo News* ([link](https://www.dmr.nd.gov/ndgs/documents/newsletter/2014Winter/Winter2014PLSS2.pdf)) | 2014-01 | HIGH |
| S2 | PLSS quarter-section side length | 2,640 ft | same as S1 | 2014-01 | HIGH |
| S3 | Corner acreage left unwatered by a pivot circle on a 160-ac quarter section | up to 24 ac (15%) | Edible Geography, "Squaring the Circle" ([link](https://www.ediblegeography.com/squaring-the-circle/)) | 2013-09 | HIGH |
| S4 | Pivot basic-circle radius, consistent with S3 | ≈1,373 ft | Derived from S3 (see note below) | 2013-09 | MEDIUM (derived) |
| S5 | Pivot basic-circle coverage, consistent with S3 | 136 ac (85%) | Derived from S3: 160 − 24 = 136 | 2013-09 | MEDIUM (derived) |
| S6 | Woven-wire fencing cost per foot | $1.51/ft | Iowa State University Extension, Ag Decision Maker File B1-75, "Estimated Costs for Livestock Fencing" ([link](https://www.extension.iastate.edu/agdm/livestock/pdf/b1-75.pdf)) | 2005-10 | MEDIUM |
| S7 | High-tensile electrified fencing cost per foot | $0.70/ft | same as S6 | 2005-10 | MEDIUM |
| S8 | Labor rate used in File B1-75 | $13.60/hr | same as S6 (document cites its own File A3-10) | 2005-10 | MEDIUM |
| S9 | Entry-level GPS guidance system cost, low end | $10,000–$15,000 | Purdue University News ([link](https://www.purdue.edu/uns/html4ever/2004/040413.Lowenberg.gps.html)) | 2004-04 | MEDIUM |
| S10 | RTK auto-steer system cost, high end | $40,000 and up | same as S9 | 2004-04 | MEDIUM |
| S11 | GPS guidance annual per-acre savings | $15/ac (2.7%) | USDA Economic Research Service — Schimmelpfennig, "Cost Savings From Precision Agriculture Technologies on U.S. Corn Farms," *Amber Waves* ([link](https://www.ers.usda.gov/amber-waves/2016/may/cost-savings-from-precision-agriculture-technologies-on-u-s-corn-farms)) | 2016-05 | HIGH |
| S12 | Corn crop margin per acre (revenue minus operating cost), derived from a 2026 UNL irrigated-corn enterprise budget (275 bu/ac yield, $650.27/ac operating cost) | $587.23/ac | University of Nebraska-Lincoln, Center for Agricultural Profitability, "2026 UNL #033 Corn, Irrigated-Electric Pivot, No Till, after Beans" ([link](https://cap.unl.edu/sites/unl.edu.ianr.agecon.center-for-ag-profitability/files/media/file/%23033%20Corn%2C%20Irrigated-Electric%20Pivot%2C%20No%20Till%2C%20after%20Beans_2026.pdf)) + S13 (price) | 2026 | MEDIUM (derived) |
| S13 | Season-average corn price, 2026/27 marketing year | $4.50/bu | USDA WASDE, August 2026 report ([link](https://www.usda.gov/oce/commodity/wasde/wasde0826.pdf)) | 2026-08 | HIGH |
| S14 | Center-pivot irrigated cropland value, percent change | -2% (statewide) | University of Nebraska-Lincoln, Center for Agricultural Profitability — Jansen, "2026 Nebraska Farmland Values and Cash Rental Rates" (Preliminary), CAP Series 26-0302 ([link](https://cap.unl.edu/sites/unl.edu.ianr.agecon.center-for-ag-profitability/files/media/file/ne-farm-real-estate_2026_prelim.pdf)) | 2026-03 | HIGH |
| S15 | Center-pivot irrigated cropland cash rental rate, percent change | ≈-3.6% (average across 8 districts) | same as S14 | 2026-03 | MEDIUM (derived) |

**Notes on derived figures (S4, S5, S12, S15):** S4 and S5 are computed from S3's stated 24-acre/15% corner-waste figure (160 − 24 = 136 ac coverage; radius from circle-area formula). This runs somewhat larger than the "textbook" 1,320-ft/125.7-ac quarter-mile pivot figure found in several other sources (e.g., NC State Extension, reviewed 2024, states ~132 ac with end gun / ~28 ac corners) — the two published corner-waste figures do not fully agree, likely because they assume different end-gun reach; this case uses the FCSAmerica/Edible Geography figure per its own named sourcing rather than averaging the two. S12 combines a real, dated UNL enterprise budget with a real, dated USDA price to compute a margin using "operating-cost margin" (revenue minus operating costs, not the budget's full economic cost, which bakes in land opportunity cost that a marginal reclaimed strip does not change) — a disclosed methodological choice. S15 is an unweighted average across Nebraska's eight agricultural-statistics districts because the source report gives no single statewide cash-rental figure for this land class (unlike its value-trend table, which does).

See `case.json`'s `sources[]` for full machine-readable entries including exact quotes and access dates, and `RESEARCH_LOG.md` for the complete research trail, including rejected searches and the one dropped figure (corner-system swing-arm reclaimable acreage).

---

## Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Convex
- Concave
- Irregular Polygon
- Quadrilateral
- Parallelogram

**"How to…" questions**

*(none — this case's claimed spine skills are all vocabulary terms; Challenge 1's research task points to whichever of the five terms above the Hero found the least familiar.)*

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
