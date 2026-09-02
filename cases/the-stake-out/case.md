# Case Study: The Stake-Out

MS | Math | Case Study | 2026-27 | MS Adventure

---

## Overview

Renata Cruz crouches at the northeast corner of Lot 4, mud sucking at her boots, a hub stake gripped between two fingers and a mallet in the other hand. Behind her, the total station sits locked on its tripod, its laser dot flickering red against the plywood form board across the yard — except it isn't flickering anymore. It's gone. The two-story frame going up next door has swallowed the sightline whole.

Her phone buzzes against her hip. The GNSS rover is charged and clipped to a range pole leaning against the tailgate of her truck, close enough to grab. She glances at the corner she still needs, the one tucked right up against that same next-door wall.

Tomorrow morning the concrete crew shows up at first light. Whatever stake is in the ground when they arrive is the corner they pour to. If it's out of tolerance, nobody finds out until the formwork inspector's tape measure says so — and by then the forms are already up.

Renata straightens, wipes her palm on her jeans, and looks between the dead sightline behind her and the rover clipped to the tailgate. Her foreman is on the far side of the site, out of earshot, trusting her to make this call herself.

Daylight is running out, the last corner is still unstaked, and it's the one corner where both of her tools are working against the same wall.

---

## Background

Renata Cruz is a construction layout technician employed by a site-work subcontractor building the foundations for a townhome development. Her job is to translate the engineer's foundation plan into physical stakes in the ground, marking every footing corner precisely enough that the concrete crew can set forms directly to her marks. She reports to the project's field superintendent and is accountable for every corner she stakes: a corner that is out of tolerance is not caught until the formwork inspector checks it after the forms are already built, at which point fixing it means tearing out and re-pouring (SEE APPENDIX E).

Two staking methods are standard practice on a site like this. **Option A — Total Station Polar Staking** uses a robotic total station occupying a known control point. The technician sights a backsight ray to a second known reference point, turns a computed deflection angle off that ray with the instrument, and marks each footing corner along the resulting sightline at its computed distance (SEE APPENDIX B). **Option B — GNSS/RTK Coordinate Staking** uses a GNSS rover carrying each corner's preloaded design coordinate. The technician walks the rover to where its live, real-time-corrected position matches the target coordinate and marks the ground there — no backsight or sightline required (SEE APPENDIX C).

Every corner staked, by either method, must land inside the plan-location tolerance foundations are held to under the ACI 117M-10 specification for tolerances in concrete construction (SEE APPENDIX A). A corner that misses that tolerance band is not caught until inspection, and the cost of catching it late is a re-shot corner and delayed forms (SEE APPENDIX E).

This particular lot complicates both methods the same way. An existing structure on the adjacent lot stands close enough to some of the foundation's footing corners to block the total station's direct line of sight to them — forcing Renata to relocate and re-establish a second instrument setup for those corners (SEE APPENDIX D). That same structure, at that same distance from those same corners, is also a documented source of GNSS signal multipath — reflected satellite signals bouncing off a nearby structure that degrade a GNSS rover's positional accuracy (SEE APPENDIX D, APPENDIX C). The obstruction is not two unrelated problems; it is one physical object degrading each method through its own real failure mode, at the same corners.

The site's control-point layout, the footing dimensions, and which corners sit in the structure's shadow are fixed for this job, not choices Renata makes (SEE APPENDIX D). What differs between the two methods is how much of each method's real accuracy margin survives at those affected corners, and how much time each method costs to finish the job, including the tolerance-driven risk of having to re-shoot a corner that misses (SEE APPENDIX E).

Current daily equipment rental rates for both instruments are in **Appendix F**, for reference alongside the time-based primary metric. Every sourced or derived figure in this case is documented, with its source and confidence, in **Appendix G**; the handful of figures with no public source are stated openly as Modeling Assumptions rather than invented.

The vocabulary and the "how to…" skills this case will ask of you are listed in **Appendix H** — that is where Challenge 1 sends you.

---

## Dilemma

You are Renata Cruz.

Do you:

**A.)** Stake every footing corner, including the ones in the adjacent structure's shadow, using Total Station Polar Staking **OR**

**B.)** Stake every footing corner, including the ones in the adjacent structure's shadow, using GNSS/RTK Coordinate Staking

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A labeled angle diagram of one un-obstructed footing corner: the backsight ray, the
    control-point occupation, and the turned deflection angle to the corner's sightline, with
    that deflection angle classified as acute, obtuse, or right.
    D2. A second-setup diagram for one of the obstructed corners: the original backsight
    baseline and the new, relocated baseline drawn as a transversal crossing it, with every
    angle pair the crossing creates — vertical, adjacent, supplementary, and complementary —
    labeled.
    D3. A worked angle-measure calculation showing that the relocated baseline is parallel to
    the original baseline, using the transversal's angle relationships and at least one known
    angle measure to solve for at least two unknown angle measures at the crossing.
    D4. A congruence check comparing the corner position each method marks for the same
    obstructed corner — modeling each method's marked point, the shared reference point, and
    the target design point as a small triangle, and stating whether the two resulting triangles
    are congruent within the tolerance band.
    D5. An accuracy-margin table, in millimeters, comparing each method's real spec-based
    positional accuracy against the ACI 117M-10 tolerance for this footing — including the
    unit conversion needed since the equipment specs are published in inches and the tolerance
    standard is metric, and the percent-of-dimension calculation the tolerance itself requires.
    D6. A total-expected-time recommendation for the obstructed corners specifically, combining
    each method's base layout time, its added time cost at an obstructed corner (a second
    instrument setup for Option A; degraded accuracy and rework risk for Option B), and a stated
    choice of method.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

## Appendix A — ACI 117M-10 Foundation Location Tolerance

The plan-location ("Location Displacement") tolerance every footing corner in this case must land
inside, per the ACI 117M-10 specification for tolerances in concrete construction and materials.

| Foundation dimension | Location displacement tolerance |
|---|---|
| Foundation dimension less than 2.4 m (8 ft) | **Greater of 13 mm or 2% of the specified dimension** [S1][S2] |

**Footing dimension used in this case.** 12 in. (a standard 2-story light-frame townhome strip
footing on 2,000 psf soil, slab-on-grade) [S3] — 12 in. = 304.8 mm. 2% of 304.8 mm = 6.1 mm, which
is less than 13 mm, so the governing tolerance for this footing is **13 mm**.

## Appendix B — Total Station Spec Sheet

Manufacturer-published accuracy specifications for the total station Renata's crew uses.

| Spec | Value |
|---|---|
| Model | Leica Viva TS16 robotic total station (TS16 M, 5" angular-accuracy class — the construction-grade option in the TS16 line) [S4] |
| Angular accuracy | 5 arc-seconds (Hz and V, absolute continuous diametrical; TS16 is also offered in 1", 2", and 3" classes) [S4] |
| EDM (distance) accuracy | ±(1 mm + 1.5 ppm), single measurement to prism [S4] |
| Combined positional error at typical stakeout distance | **≈1.3 mm** at a 100 ft (30.48 m) control-point-to-corner distance [MA7] — derived: angular component = 30.48 m × (5″ in radians) = 0.74 mm; EDM component = 1 mm + (1.5 ppm × 30.48 m) = 1.05 mm; combined (root-sum-square) = √(0.74² + 1.05²) ≈ **1.3 mm** |

## Appendix C — GNSS/RTK Receiver Spec Sheet

Manufacturer-published accuracy specification for the GNSS rover, and what happens to that
accuracy near an obstruction.

| Spec | Value |
|---|---|
| Model | Trimble R12i GNSS System [S5] |
| RTK horizontal precision, open sky | ±(8 mm + 1 ppm), RMS, single baseline under 30 km [S5]. At this job's typical short base-to-rover baseline of 0.5 km, that is 8 mm + (1 ppm × 0.5 km) = **8.5 mm** |
| Near-structure (multipath) degradation | **Modeling Assumption [MA5]: an additional ±17 mm RMS of horizontal error (combined with the open-sky spec by root-sum-square), for a corner within about 3 m [MA6] of the adjacent structure.** No single published figure ties a specific mm degradation to a specific distance/material combination for this scenario — see Modeling Assumptions block. The *direction and general magnitude* are real and documented: peer-reviewed GNSS literature places carrier-phase multipath error from a nearby reflective structure at "several centimeters" [S6][S7]. Combined near-structure accuracy: √(8.5² + 17²) ≈ **19.0 mm RMS**. |

## Appendix D — Site Layout & Corner Data

The fixed geometry of this job: where the control points are, where each footing corner falls,
and which corners sit in the adjacent structure's line-of-sight/multipath shadow. These are fixed
scenario facts for this specific lot — not public data, since no public record exists for a
fictional job site — so every figure in this appendix is a stated **Modeling Assumption**.

| Item | Value |
|---|---|
| Number of footing corners on this foundation | 12 [MA8] |
| Number of corners obstructed by the adjacent structure | 3 [MA8] |
| Distance from control point to a typical corner | 100 ft (30.48 m) [MA7] |
| Distance from the adjacent structure to the affected corners | 10 ft (≈3 m) [MA6] |
| Deflection angle example (unobstructed corner) | 62° (acute) — illustrative value for Challenge D1's diagram only; it carries no cost or tolerance consequence [MA9] |

## Appendix E — Productivity, Setup, and Rework Time Data

| Item | Value |
|---|---|
| Base layout time per corner, Total Station Polar Staking | 6 minutes [MA1] |
| Base layout time per corner, GNSS/RTK Coordinate Staking | 3 minutes [MA2] — informed by, but not equal to, the real published Alphageo figure of up to 500 points/hour (7.2 s/point) [S8] for open-terrain point collection; a footing corner requires walking in, waiting for the position to settle on the target coordinate, and marking the ground, which the raw open-terrain figure does not include |
| Added time cost, second total-station setup | 20 minutes [MA3] |
| Rework time cost, a corner that misses tolerance | 45 minutes [MA4] |
| GNSS miss probability at an obstructed corner | **≈62.6% (derived)** — modeling each method's radial position error as a 2D circular-normal distribution (per-axis σ = combined RMS ÷ √2), P(radial error > 13 mm tolerance) = exp(−13² ÷ 2σ²). For Option B at an obstructed corner (combined accuracy 19.0 mm RMS, σ = 13.4 mm): P ≈ 0.626. For Option A at the same corner (combined accuracy 1.3 mm RMS, σ = 0.9 mm): P ≈ 0 (effectively never misses on accuracy grounds — its risk is entirely the second-setup time cost, not rework). |

## Appendix F — Equipment Rental Rates

Secondary cost context — real, published equipment rental rates for each instrument, for
reference alongside the time-based primary metric.

| Equipment | Daily rental rate |
|---|---|
| Robotic total station | $275/day (Topcon robotic total station w/remote, 8000/9000 series) [S9]; corroborated by a $269/day marketplace average across actual rental quotes [S10] |
| GNSS/RTK rover | $150–$250/day (Trimble R12 GNSS system, two named suppliers' current listed rates) [S11] |

## Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author after a genuine, multi-angle research attempt failed to turn up an exact published
> figure. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Base layout time, Total Station Polar Staking, per corner | 6 min | No published per-corner minutes figure exists; 6 min reflects turning a computed angle with a robotic ATR instrument already on a live sightline, walking the distance, driving the hub stake, and a confirmation shot. | Low — total station's time cost is dominated by MA3 (the second setup), not this term. Would need to roughly triple (to ~18 min) before it alone could flip the case's recommendation. |
| MA2 | Base layout time, GNSS/RTK Coordinate Staking, per corner | 3 min | Alphageo's real, cited 500-points/hour figure [S8] is for open-terrain bulk point collection, not a footing corner requiring convergence verification and marking; 3 min is a slower, more conservative per-corner figure for this more careful task. | Low — GNSS's time advantage is large enough that reasonable changes here don't flip the recommendation on their own. |
| MA3 | Added time, second total-station setup | 20 min | No published figure exists; reflects breaking down and moving the tripod, releveling, and resectioning or re-establishing a backsight to two new known points. | **Moderate.** A longer second-setup time shifts the total-expected-time balance toward Option B; a shorter one shifts it further toward Option A. |
| MA4 | Rework time, a corner that misses tolerance | 45 min | No published figure exists; reflects re-shooting and resetting one stake — distinct from, and smaller than, the full tear-out-and-re-pour cost described in Appendix E's Background reference, which is a separate, larger, non-recurring cost. | **Moderate.** A shorter rework time shifts the total-expected-time balance toward Option B; a longer one shifts it toward Option A. |
| MA5 | Near-structure RTK multipath degradation | +17 mm RMS (added by root-sum-square to the open-sky spec) — retuned 2026-09-01 from an original +25 mm RMS to bring the case's margin under SPEC.md §2's ~20% cap (see RESEARCH_LOG.md) | Peer-reviewed GNSS multipath literature [S6][S7] consistently documents "several centimeters" of carrier-phase error near a reflective structure but does not tie an exact mm figure to this scenario's specific distance and structure type. The original 25 mm sat at the high end of the case's own 10–50 mm literature-anchored range; 17 mm is a low-to-mid point in that same real range and is at least as defensible. | **High — still the single most margin-driving assumption in the case.** A smaller multipath degradation shifts the balance toward Option B; a larger one shifts it toward Option A. The literature-documented range (roughly 10–50 mm) spans both directions from the case's stated value, so this assumption is worth pressure-testing in discussion. |
| MA6 | Distance, adjacent structure to affected corners | 10 ft (≈3 m) | Author-chosen scenario parameter, placed within the distance range most GNSS-multipath field studies actually test (roughly 1–5 m from a reflective wall) [S6][S7]. | Low on its own — it is the justification for MA5's applicability, not an independent cost driver. |
| MA7 | Stakeout distance, control point to typical corner | 100 ft (30.48 m) | Author-chosen scenario parameter; a realistic control-point-to-corner distance on a small residential/townhome lot. | Low — total station accuracy stays well inside tolerance across any plausible residential stakeout distance. |
| MA8 | Total footing corners / obstructed corners | 12 total, 3 obstructed | Author-chosen scenario parameter for a modest multi-unit townhome foundation footprint; the obstructed corners are the ones nearest the shared lot line. | None — the case's primary metric and D6 are both computed **per obstructed corner**, so the total/obstructed count does not change the per-corner margin. It only scales the site-wide total. |
| MA9 | Deflection angle example | 62° (acute) | Illustrative value for Challenge D1's diagram only. | None — carries no cost or tolerance consequence. |

## Appendix G — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | US-customary companion standard's foundation location tolerance rule | "the greater of ±2% of specified dimension or 1/2 in." (<8 ft); ±2 in. (≥8 ft) | ACI Committee 117, *ACI 117-10 (Reapproved 2015)*, Section 3.2.1 "Deviation from location," reproduced in a Pennsylvania Dept. of Labor & Industry ICC code-review public comment PDF ([link](https://www.pa.gov/content/dam/copapwp-pagov/en/dli/documents/ucc/documents/2018-icc-code-review-public-comments/szoke-117-10.pdf), p. 26) | 2018 (filing); accessed 2026-09-01 | HIGH |
| S2 | Metric ACI 117M-10 foundation location tolerance | "greater of 13 mm or 2% of specified dimension," foundation dimension ≤ 2.4 m | theconstructor.org, "Tolerances for Concrete Foundation Construction as per ACI 117M-10" ([link](https://theconstructor.org/geotechnical/tolerances-concrete-foundation-construction-aci-117m/21569/)) | undated; accessed 2026-09-01 | MEDIUM — secondary summary of the primary ACI 117M-10 standard. A direct fetch of concrete.org's own ACI 117M-10 preview PDF was attempted and returned only front matter/table of contents (Section 3, p. 117M-25, is beyond the free preview); a civilenghub-hosted sample PDF was also attempted and returned unreadable/garbled content. This figure is consistent in substance and unit-converted magnitude with S1 (1/2 in. = 12.7 mm, commonly rounded to 13 mm; 8 ft ≈ 2.4 m), which is the strongest available corroboration short of the paywalled primary text. |
| S3 | This townhome foundation's footing width | 12 in. (2-story, light-frame, slab-on-grade, 2,000 psf soil) | Knox County (TN) Code Administration & Inspection, "2018 IRC Residential Footing Information" (Table 1, based on 2018 IRC Table R403.1), Rev. 02/2019 ([link](https://knoxcounty.org/codes/pdfs/construction_info/FootingInstructions.pdf)) | Rev. 2019-02; accessed 2026-09-01 | HIGH |
| S4 | Leica Viva TS16 total station angular and EDM accuracy | 1″/2″/3″/5″ angular accuracy options; EDM ±(1 mm + 1.5 ppm), single/prism | Leica Geosystems AG, *Leica TS16 Data Sheet* ([link](https://leica-geosystems.com/-/media/files/leicageosystems/products/datasheets/leica_viva_ts16_ds.ashx)) | 2020 printing (929657en – 11.20); accessed 2026-09-01 | HIGH |
| S5 | Trimble R12i GNSS System RTK horizontal precision | ±(8 mm + 1 ppm) RMS, single baseline < 30 km | Trimble Inc., *Trimble R12i GNSS System Datasheet* ([link](https://trakkitgps.com/wp-content/uploads/2023/09/Trimble_R12i_Datasheet-English-USL.pdf)) | PN 022516-511C (10/22); accessed 2026-09-01 | HIGH |
| S6 | GNSS/RTK multipath error magnitude near a reflective structure (qualitative basis for MA5) | Multipath is the dominant RTK error source near reflective surfaces; carrier-phase error described in the "several centimeters" range | C. Mekik and O. Can, "An Investigation on Multipath Errors in Real Time Kinematic GPS Method" / "Multipath Effects in RTK GPS and a Case Study," *Scientific Research and Essays*, Vol. 5, No. 16 (2010), pp. 2186–2200 | 2010; accessed 2026-09-01 | MEDIUM — real, peer-reviewed paper confirmed via multiple independent citations/aggregators (Semantic Scholar, ResearchGate, Academia.edu); full-text access to the paper's specific distance-vs-error data table was blocked by publisher bot-protection on every mirror attempted (403 responses), so only the qualitative magnitude, not an exact figure tied to a specific distance, is used here — hence MA5 remains a disclosed assumption, not a cited figure. |
| S7 | Corroborating magnitude for GNSS multipath near buildings | "The influence of the multipath effect on the observed carrier phase can reach several centimeters at most" near reflective structures/curtain walls | Peer-reviewed GNSS deformation-monitoring literature indexed on PubMed Central (NCBI), and M. O'Connor et al., "Low-latency GNSS multipath simulation and building wall detection in urban environments," *[Journal]* (2024) | 2024; accessed 2026-09-01 | MEDIUM — real peer-reviewed sources corroborating S6's magnitude and mechanism; general, not tied to this scenario's exact distance/material. |
| S8 | GNSS/RTK stakeout raw productivity (basis for MA2, not itself the per-corner figure) | "A single operator [can] collect 500 or more points per hour" in open terrain (road construction, agricultural grading, large earthworks) | alphageo-info.com, "Robotic vs Manual Total Stations vs GPS: Construction Surveying Instruments Compared" | 2026-07-27; accessed 2026-09-01 | MEDIUM — real, dated, named-publisher article; the figure is a proxy (open-terrain bulk point collection, not footing-corner stakeout-and-mark), so it informs but does not equal MA2. |
| S9 | Robotic total station daily rental rate | $275/day, $850/week, $2,200/month (w/remote, 8000/9000 series) | Washington State Dept. of Enterprise Services, "Survey Equipment Rental Rates" (Topcon Robotic Total Station line item) ([link](https://apps.des.wa.gov/contracting/PPIRentals.pdf)) | undated rate sheet; accessed 2026-09-01 | MEDIUM — named, real, itemized rate sheet hosted on a state government contracting portal; the sheet itself carries no publish date. |
| S10 | Robotic total station rental rate, market corroboration | $269/day, $960/week, $2,754/month average | KWIPPED marketplace, Robotic Total Stations category page, "based on actual Robotic Total Station quotes submitted by KWIPPED Suppliers in the last 12 months" ([link](https://www.kwipped.com/rentals/surveying/robotic-total-stations/1417)) | rolling 12-month average; accessed 2026-09-01 | MEDIUM |
| S11 | GNSS/RTK rover daily rental rate | $150/day (Supplier #4291, Lafayette, LA) and $250/day (Supplier #13047, Ambridge, PA), Trimble R12 GNSS System | KWIPPED marketplace, Trimble R12 GNSS System rental listing ([link](https://www.kwipped.com/rentals/product/trimble-r12-gnss-system/26611)) | accessed 2026-09-01 | MEDIUM — two real, named suppliers' current listed rates; listed for the R12 (non-"i") system, the same product family and accuracy/price class as the R12i used elsewhere in this case, since no R12i-specific daily rate was found listed. |

## Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Ray
- Degree
- Acute Angle
- Obtuse Angle
- Right Angle
- Transversal Line
- Congruent
- Supplementary Angles
- Complementary Angles
- Vertical Angles
- Adjacent Angles

**"How to…" questions**

- How to find angle measures of intersecting lines
- How to find angle measures given parallel lines, a transversal line and at least one angle measure
- How to convert an amount from one unit to another unit
- How to find the percent of a number
- How to compare two or more values

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
