# RESEARCH LOG — Wind Triangle

**Stage 3, `case-research`, run 2026-08-12.** Opened with **75** `{{NEEDS_SOURCE}}` tokens in
`case.md` (many of them the same figure repeated across table cells); closed with **0**. Every URL
below was fetched in this session with `WebFetch` and confirmed to carry the figure cited before it
was written into the case (MCS-21). Nothing was filled from memory.

`case.json.needs_source[]` consolidates the 75 raw tokens into 19 figure classes with a status
each. The counts below are of raw tokens.

| Outcome | Raw tokens |
|---|---|
| SOURCED | 68 |
| ASSUMPTION (stated in Appendix E) | 4 |
| DROPPED | 3 |
| Still OPEN | **0** |

---

## What was searched, what was found, and what was rejected

### P01–P37 · Waypoint identities, positions, leg distances and leg courses

**Searched:** a published, primary, fetchable source of airport reference positions.
**Rejected without fetching a figure from it:** the OurAirports bulk CSV (≈10 MB, over the fetch
limit) and Wikipedia airport infoboxes (secondary, and MCS-21 forbids citing what was not fetched).
**Found:** the NWS Aviation Weather Center's own **Airport Data API**, which returns identifier,
name, latitude, longitude and elevation as JSON. Two calls were made and both returned cleanly
(**S1**, **S2**). This is the same agency that publishes the wind product, which keeps the
positions and the winds on one authority.

Leg distances and initial true courses are **derived** from those sourced positions by the
haversine and initial-bearing formulas, at an earth radius of 3,440.065 nm. The derivation is shown
in `sensitivity_model.py` and is the student's own work in D2/D5. No distance figure was taken from
any third party.

### P38–P62 · The wind field — the load-bearing decision of this whole case

**Searched:** a real, published, *permanently addressable* upper-wind data set at a stated date and
hour.

- **Attempt 1 — University of Wyoming radiosonde archive** (`weather.uwyo.edu/cgi-bin/sounding?…`).
  **HTTP 404.** The URL form used is no longer served. Not pursued further once a better option
  appeared.
- **Attempt 2 — Aviation Weather Center live winds/temps API**
  (`aviationweather.gov/api/data/windtemp`). Fetched successfully. `level=high` returns only
  45,000 ft and 53,000 ft; **`level=low` returns the 30,000 / 34,000 / 39,000 ft columns**, which
  is what a transcontinental jet actually plans at. Product identified in its own header as
  **FBUS33 KWNO / FD3US3**, issued 122001Z.
  **Rejected as the citation** — not as the data. This endpoint returns a *new* forecast at every
  issuance, so a Tier 2 P6 re-fetch would never find these values again. That is precisely the
  "URL resolves but no longer carries the figure" failure P6 exists to catch.
- **Attempt 3 — Iowa Environmental Mesonet NWS text-product archive.** First try with
  `pil=FBUS31` returned `ERROR: Could not Find: FBUS31` (wrong identifier — IEM keys on the AWIPS
  id, not the WMO heading). Retried with **`pil=FD3US3&e=202608122100`** and it returned the
  **identical product**, header for header, at a URL keyed to a fixed end-timestamp. **This is what
  is cited (S3).** The live AWC endpoint was kept as a same-session corroboration: both returned
  character-identical coded groups for every station used.

The coded groups are reproduced verbatim in Appendix B rather than only decoded, so the case
survives the link dying and so a Hero can check the decode themselves.

**Deliberately over-complete.** Appendix B carries ten stations; the two filed routings use five of
them. KJFK, KBUF, KDEN, KMEM and KLIT are real published rows from the same product that no filed
leg uses. That is SPEC §1.6's filtering practice, and it is also what makes the Twist computable
in the room without introducing a new number.

### P63–P65 · Aircraft type, cruise altitude, cruise true airspeed

**Found:** the **EUROCONTROL Aircraft Performance Database** entry for B738 — TAS 460 kt, Mach
0.79, ceiling FL410 (**S4**). The original `contentzone.eurocontrol.int` URL 301-redirected to
`learningzone.eurocontrol.int`; the redirect target is what was fetched and what is cited.
FL340 was chosen for the case because it is the level the FD product publishes and is comfortably
below the type's certified ceiling.

### P66 · Cruise fuel flow — the weakest source in the case, and it is labelled as such

**Rejected:** the EUROCONTROL performance page above publishes **no** fuel-flow figure.
**Rejected:** the ICAO Aircraft Engine Emissions Databank. It publishes fuel flow at takeoff,
climb, approach and idle thrust settings for the CFM56-7B, not at cruise. Substituting an
approach-thrust number for a cruise number would be a proxy presented as a measurement.
**Found:** **EUROCONTROL, *Standard Inputs for Economic Analyses*, Release 10.0.1, Table 6.1**,
"Average fuel burn rates (kg/minute)", column "En route": **40.1 kg/min** for the narrow-body
segment, which the source names as including the B738 (**S5**). Stated data source: EUROCONTROL
BADA and PRISME.

Graded **MEDIUM**, not HIGH, for two named reasons: it is a *segment average*, not a type-specific
figure, and its column is labelled "En route" rather than "cruise". Both caveats are printed in
Appendix F where a Hero can see them.

**Why this is acceptable rather than a blocker.** Both routings fly the same type at the same true
airspeed and the same fuel flow, so this figure multiplies both sides of the comparison by the same
constant. It sets how big the answer is; it cannot change which routing wins. That is stated in
`balance.margin_basis`, in Appendix F, and in the Guide Notes.

### P67 · Usable fuel capacity — **DROPPED**

**Rejected:** Boeing's own *737 Airplane Characteristics for Airport Planning* is the primary
source, and both the `737.pdf` and `737NG_REV_C.pdf` editions exceed the 10 MB fetch limit — the
fetch failed with `maxContentLength size of 10485760 exceeded`. Aggregator blogs repeating "6,875
US gallons" were found by search and **not used**: MCS-21 and SPEC §5 both forbid it, and a
remembered figure is exactly what this project treats as fabrication.

**Exit taken: drop the figure, then cut what referenced it** (`case-research` §5, exit 3). The
capacity constraint was also decorative: minimum dispatch fuel comes out around 35,700 lb, which
does not come close to binding against any plausible 737-800 capacity, and SPEC §1.3 forbids a
Background constraint that never enters a calculation and never rules out an option. The Background
sentence was removed and **D5's reserve check was rewritten** to compute the minimum dispatch fuel
required by 14 CFR 121.639 — which needs no capacity figure and is a better deliverable.

### P68 · The reserve rule

**Found:** **14 CFR § 121.639**. The human-readable eCFR page 302-redirected to
`unblock.federalregister.gov` and could not be fetched; the **eCFR API renderer URL** was fetched
successfully and returned the section (**S6**). Independently confirmed by a second, separate fetch
of Cornell LII's copy of the same section, which returned the same three requirements. A GovInfo
PDF of the section was also fetched but its text could not be extracted reliably and it was not
relied on.

### P69 · Filed alternate

KLAX is a standard KSFO alternate. Its position came from **S1**; the 293.3 nm distance and 137.6°
course are derived from the sourced KSFO and KLAX positions, not quoted from anywhere.

### P70 · Jet fuel price

**Rejected:** the **IATA Jet Fuel Price Monitor** (Platts). Fetched; it returned $146.93/bbl but
carried **no explicit date** in the content retrieved — only "last week". SPEC §5 requires a stated
cutoff for a still-changing quantity, so an undated price was rejected.
**Rejected:** the **EIA daily** Gulf Coast spot series (`f=D`). Fetched; the daily view returned
values only through 2022 in the content retrieved, which does not agree with the monthly view of
the same series. Rather than cite a figure whose recency could not be confirmed, the daily view was
abandoned.
**Found:** the **EIA monthly** series, *U.S. Gulf Coast Kerosene-Type Jet Fuel Spot Price FOB*,
release date 12 August 2026 (**S7**).

**"As of" handling, per SPEC §5.** The series shows both July 2026 and August 2026 at $3.403/gal.
**July 2026 is used** — the most recent *complete* month. August 2026 was still in progress on the
release date, and freezing a case's economics at an undisclosed, incomplete partial period is the
exact failure recorded in `cases/lebron-vs-michael/case.json.correction_2026_08_04`. The cutoff is
stated in Appendix D and applies to every dollar figure in the case.

### P71 · Density of Jet A — **stated Modeling Assumption (MA4)**

**Searched:** a primary, fetchable, US-government or standards-body statement of a
pounds-per-US-gallon figure.
**Rejected:** ASTM D1655, the governing specification — paywalled.
**Rejected:** the ICAO Carbon Emissions Calculator methodology PDF (which states a kg/L density) —
**HTTP 404** at the URL tried.
**Rejected:** the EIA Monthly Energy Review appendix PDF — fetched, but its text could not be
extracted and no density figure could be confirmed in it.
**Rejected:** the several aviation blogs that state 6.7 lb/gal — LOW confidence, no provenance, and
SPEC §5 does not allow a LOW figure to carry a quantity in a table.

**Exit taken: stated Modeling Assumption** (`case-research` §5, exit 1). **MA4 = 6.7 lb per US
gallon**, in the visible Modeling Assumptions block, with the basis stated and the honest note that
the primary specification is paywalled. Its sensitivity is written down: it affects only the dollar
figure, identically for both routings, and cannot change which routing wins.

### P72–P74 · The assumption slots the writer left open

- **MA1 (was: block time).** The case never uses block time in the metric. The slot was reused for
  a **frequency** figure (2 departures/day, 365 days) whose only job is to annualise the per-flight
  difference. Stated, not sourced; Meridian Air is fictional.
- **MA2 (was: forecast-error band) — DROPPED as an input, and turned into an output.** No published
  verification statistic for FD upper-wind forecasts was located and fetched. Rather than assume an
  error band and hand the student the answer, **D5 now asks the student to compute the break-even
  error** (it is **20.5%**, a uniform 7.2 kt per leg) and to judge for themselves whether a real
  forecast is ever wrong by that much. That is a better deliverable than the assumption would have
  been. The MA2 slot was reused for the **airway-structure allowance**, a different assumption the
  redesign genuinely needed.
- **MA3.** Kept as written: one wind vector per leg, taken at the downwind-end waypoint. Its
  direction of error is stated.

### P75 · The Sources appendix

Written: seven rows, S1–S7, each with the org, the exact document, the fetched URL, the access date
and a confidence grade with its reason.

---

## The Twist: a fetch that produced a negative result, and the negative result is the point

The obvious twist for this case was "the forecast has been amended". That is available as **real
published data**: the same FD family publishes a 24-hour product, **FBUS35 KWNO / FD5US5**, valid
131800Z, with materially different winds at every station (KDBQ 300/58 instead of 300/78; KSLC
220/62 instead of 200/42; KSFO 340/07 instead of 150/13; KSGF 170/14; KABQ 230/12).

It was fetched and fully recomputed. **Under it, Routing B still wins and the margin widens**
(2.16% → 2.33%, before MA2's allowance). A twist that invalidates no position fails SPEC §7.2 and
Tier 2 probe 4, so it was **rejected**, and a corridor-closure reroute twist was authored instead:
convective weather shuts the KSGF corridor and Routing B must be re-filed via KMEM. That twist uses
**only data already published in Appendices A and B** — no new number enters the case — and it
**flips the verdict** to Routing A by 0.64%.

Recorded here in full because the rejection is the useful part: the next person to look for an
"amended forecast" twist on this case should know it was tried, it is real, and it does not work.

---

## Derived arithmetic, in the open

| Quantity | Value | How |
|---|---|---|
| Cruise fuel flow | 5,304.3 lb/h | 40.1 kg/min × 60 = 2,406 kg/h; × 2.20462 lb/kg [S5] |
| Routing A trip fuel | 28,229.1 lb | Σ(filed leg nm ÷ leg ground speed) × fuel flow |
| Routing B trip fuel | 27,756.3 lb | same |
| Difference | 472.8 lb | A − B |
| `margin_pct` | **1.67** | 472.8 ÷ 28,229.1 × 100 |
| Break-even forecast overstatement | **20.5%** | scale factor 0.7952 on Routing A's along-course components, solved by bisection until the two trip fuels are equal |
| Break-even as a uniform shift | +7.21 kt per leg | same, solved additively instead |
| Minimum dispatch fuel, A / B | 35,685 lb / 35,212 lb | trip + KSFO→KLAX alternate (3,478 lb) + 45 min at cruise flow (3,978 lb) [S6] |
| Per-flight fuel difference in money | 70.6 gal → $240.24 | 472.8 lb ÷ 6.7 lb/gal [MA4] × $3.403/gal [S7] |
| Annualised | 345,290 lb → $175,376 | × 730 departures [MA1] |
| Twist: Routing B via KMEM | 28,410.5 lb, winner A by 0.64% | same method, KMEM position [S2] and KMEM wind [S3] |

## Handed back to `case-readiness`

Zero placeholders remain. `case.json.status` = `researched`. Next step: Tier 1, then author
`sensitivity_model.py` and run Tier 2.
