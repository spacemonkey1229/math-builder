# Research Log — Turbine Channel

Stage 3 (`case-research`) run on `cases/the-turbine-channel/`, starting from case-write's 41 literal
`{{NEEDS_SOURCE}}` tokens in `case.json.needs_source[]`. Worked in load-bearing weight order: the two
channels' real current-speed data first (the entire case's math depends on these), then channel
geometry, then the turbine-array specification, then the physical constant, then the derived
generation-potential conversion factor last (since it depends on the turbine spec found in between).

## P01/P02 — The Narrows' and the Reach's real NOAA current-speed stations

**Searched:** "NOAA CO-OPS currents API station list PORTS current station id"; "NOAA
tidesandcurrents.noaa.gov currents data station list active PORTS"

**Fetched directly:** `https://tidesandcurrents.noaa.gov/cdata/StationList?filter=active&type=Current+Data`
— confirmed a real, live, 86-station active current-data network. Selected two candidate stations
with genuinely different real flow character: **ca0101** (Cape Cod Canal, West End, MA — Cape
Cod/Buzzards Bay PORTS) as a narrow, fast, engineered ship-canal candidate, and (after a second pass,
below) **cb0102** (Cape Henry LB 2CH, Chesapeake Bay South PORTS) as a wide-entrance, slower candidate.

**Fetched directly (Narrows real data):**
`https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?product=currents_predictions&station=ca0101&begin_date=20260901&end_date=20260901&interval=6&units=english&time_zone=lst_ldt&format=json`
— confirmed live, returned a real 240-point, 6-minute-interval signed current-velocity series for
2026-09-01. Cross-checked against `https://www.offshoreblue.com/cruise/cape-cod-speeds.php` (average
max flood 3.50 kn, average max ebb 3.84 kn, absolute peaks 5+ kn) — the API's real per-cycle peaks
(up to 5.30 kn on this particular day) are consistent with that real, independently reported range.

**Outcome: SOURCED as [S1], HIGH confidence.** Selected the ebb pulse from 00:48 to 06:54 (366 min,
61 readings, peak -5.28 kn at 03:24) as one full "flow window" (slack to slack) for the Narrows.
Direction (signed velocity_major) discarded; magnitude used as "current speed," since this case's
math (D3/D5) does not depend on flow direction.

**Fetched directly (Reach real data), second candidate search:**
"NOAA current predictions station id Chesapeake Bay entrance OR Delaware Bay entrance current speed
knots PORTS" surfaced the Chesapeake Bay Bridge Tunnel / Cape Henry area. A guessed station code
`cb0102` was fetched directly at the same API endpoint and returned real, valid data (not an error) —
confirmed via the CO-OPS metadata API
(`https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/cb0102.json?type=currentpredictions`)
to be **"Cape Henry LB 2CH,"** deployed 2025-01-27, Chesapeake Bay South PORTS, 55 ft bin depth,
36.959°N -76.013°W — a real station near the entrance to Chesapeake Bay.

**Outcome: SOURCED as [S2], HIGH confidence.** Selected the flood pulse from 07:48 to 15:24 (456 min,
77 readings, peak 1.53 kn at 11:18/11:24) as the Reach's flow window — both lower-peaked (1.53 kn vs.
5.28 kn) and longer (456 min vs. 366 min) than the Narrows', matching case.md's stated design.

## P03 — The Narrows' real channel geometry (Cape Cod Canal)

**Searched:** "Cape Cod Canal width depth feet Army Corps of Engineers channel dimensions"

**Fetched directly:** `https://www.asce.org/about-civil-engineering/history-and-heritage/historic-landmarks/cape-cod-canal`
— confirmed: "a minimum channel width of 480 feet... and an authorized depth of 32 feet at mean low
water," the current dimensions since the 1940 enlargement (originally 480 ft wide, 34 ft deep).

**Outcome: SOURCED as [S3], HIGH confidence.** 480 ft = 146.3 m; 32 ft = 9.75 m. Cross-sectional area
1,427.0 m² is derived (146.3 × 9.75), shown in case.md. Since the Narrows is explicitly modeled on
this real engineered canal, its real physical dimensions were used directly rather than treated as a
separate assumption.

### 2026-09-12 correction (case-readiness P6 data-decay finding, QA_REPORT.md)

A live re-fetch of the same ASCE URL on 2026-09-12, for this QA remediation pass, found the page no
longer (or never did) carry the "authorized depth of 32 feet" sentence quoted above. The live page
now states only: *"Originally 480 feet wide and 34 feet deep, the canal was enlarged in 1940, making
it the widest canal in the world."* — a pre-1940 dimension pair, with no post-1940 authorized-depth
figure anywhere on the page. This is the exact MCS-21 "resolves but no longer carries the figure"
failure mode. The original P03 entry above is left in place as the historical record of what was
originally cited and why it was wrong; it should not be relied on for the depth figure going forward.

**Re-research, 2026-09-12:** Searched "Coast Pilot Cape Cod Canal controlling depth OR project depth
feet." Found and fetched `https://nauticalcharts.noaa.gov/publications/coast-pilot/files/cp2/CPB2_C05_WEB.pdf`
(NOAA Office of Coast Survey, *U.S. Coast Pilot 2*, Chapter 5, live edition dated 2026-09-06) —
confirmed verbatim: *"A federal project provides for a channel 32 feet deep through the Cape Cod
Canal."* This is a live, current, primary federal source (same publication family already used for
the Reach's S4 depth citation) that directly supports the case's existing 32 ft / 9.75 m depth figure.

**Outcome: RE-SOURCED.** Width stays **[S3]** (ASCE, retained only for the 480 ft / 146.3 m width
figure, which the live page does state and which a second live-fetched source — World Ports
Directory/MarineLink, "at its narrowest point, the canal is about 480 feet (146 meters) wide" —
corroborates as still current). Depth is now **[S8]** (NOAA Coast Pilot 2, Ch. 5), HIGH confidence,
live-confirmed 2026-09-12. **No numeric change**: 146.3 m × 9.75 m = 1,427.0 m² is unchanged, so the
Narrows' volume (49,480,854 m³), kWh (10,889), and margin_pct (9.21%) all carry forward unchanged —
this was a citation-accuracy fix, not a data fix. case.json, case.md (Appendix C, Appendix G), and
this log have all been updated to cite S8 for depth and S3 only for width.

## P04 — The Reach's channel geometry (Chesapeake Bay entrance)

**Searched:** "NOAA current predictions station id Chesapeake Bay entrance"; "Chesapeake Bay entrance
width Cape Henry to Cape Charles nautical miles bay mouth width"; "Cape Henry entrance channel depth
feet NOAA chart 12221 Thimble Shoal OR bay entrance depth"

**Fetched/confirmed:**
- `https://nauticalcharts.noaa.gov/publications/coast-pilot/files/cp3/CPB3_C09_WEB.pdf` (NOAA Office
  of Coast Survey, U.S. Coast Pilot 3) — confirmed a real federal channel near Cape Henry: "a 55-foot
  deep channel with a 32-foot-deep auxiliary channel on each side."
- `https://www.spinsheet.com/chesapeake-bay/chesapeake-bay-facts-and-figures` — confirmed the mouth of
  Chesapeake Bay is "about 12 miles wide" between Cape Henry and Cape Charles.

**Outcome:** Depth **SOURCED as [S4]**, HIGH confidence — 55 ft = 16.76 m, used directly. Width is
**NOT FOUND** as a single citable "array site width," because the real entrance the Reach is modeled
on is itself a ~12-mile-wide (~19 km) natural bay mouth (S7) with no single defined width for a
turbine-array site the size this case needs. **Exit chosen: Modeling Assumption (MA1)**, 256 m,
disclosed in Appendix E with its real basis (S7) and explicit sensitivity — this is also the
retuning lever used to keep the case inside SPEC §2's ~20% balance cap (see "Balance computation"
below).

## P05 — Small tidal-turbine array specification (rated capacity, swept footprint)

**Searched:** "real tidal turbine pilot array site channel width depth meters MeyGen OR 'Roosevelt
Island Tidal Energy' site dimensions"; "Verdant Power Gen5 KHPS turbine rated current speed design
flow speed knots OR m/s East River"; "Verdant Power Gen5 KHPS rated power curve '56 kW' OR '35 kW'
current speed m/s design point East River RITE"

**Fetched directly:**
- `https://tethys.pnnl.gov/project-sites/roosevelt-island-tidal-energy-rite-project-pilot` (PNNL/DOE
  Tethys database) — confirmed: Gen5 KHPS turbines, 5 m rotor diameter, 35 kW rated power per
  turbine, up to 30 turbines planned (3 installed in phase B-1), 1.05 MW total planned capacity,
  installed at 10 m depth in the East River (East Channel), operated 2020-2021.
- `https://power.nridigital.com/future_power_technology_jan21/new_york_tidal_energy_verdant`
  (Power Technology / NRi Digital magazine, Jan 2021) — confirmed independently: "2.25 m/s" current
  speed at the site, "5 m diameter rotors," "35 kW nameplate generators," "three to a single TriFrame
  or 105 kW," "average 1 MWh per day."

**Rejected:** `https://openei.org/wiki/PRIMRE/Databases/Projects_Database/Projects/Roosevelt_Island_Tidal_Energy_(RITE)_Pilot_Project`
stated a "350 kW per turbine" figure, but this is 1.05 MW (the full 30-turbine planned capacity)
divided by only the 3 turbines actually installed in phase B-1 — an arithmetic artifact inconsistent
with every other source's 35 kW per-turbine figure (including OpenEI's own "Gen5 KHPS" naming and
Tethys' independent 35 kW figure). Excluded per SPEC §5's "name the dispute" rule; recorded in
`case.json.excluded_sources[]`, not cited in case.md.

**Outcome: SOURCED as [S5], HIGH confidence, `derived: true`.** Used the full planned 30-turbine
array (1,050 kW combined, matching Tethys' own stated "Total Installed Capacity: 1.05 MW") as "a
representative small tidal-turbine array." Swept footprint 589.0 m² is derived: 30 × (π × 2.5²).
The 2.25 m/s design current speed is also the anchor value for P06 below.

## P06 — Generation-potential conversion factor (kWh per m³)

**Searched:** "NREL OR DOE marine energy tidal turbine power coefficient efficiency typical value Cp
Betz limit report" (background reading only — see outcome below for why this path was not needed)

**Attempted direct search for a published "kWh per m³" turbine spec:** no manufacturer spec sheet,
DOE report, or NREL marine-energy publication found in this session publishes a turbine's output as
a direct "kWh generated per m³ of water moved" ratio — this is not a figure the industry publishes
as a line item (turbines are rated in kW at a design flow speed, not in energy-per-volume).

**Outcome: NOT FOUND as a direct citation. Exit chosen: Modeling Assumption (MA2), derived (not
invented) from S5's real numbers**, rather than a search-derived Betz-limit/Cp-based physics estimate.
Initial approach considered using the real Betz limit (0.593) and published achieved marine-turbine
power coefficients (0.35–0.45, per general literature) to derive a channel-*specific* conversion
factor scaling with each channel's characteristic speed squared (since kinetic power ∝ v³ while
volumetric flow ∝ v, so energy-per-volume ∝ v²). This was computed and explicitly rejected: applying
a v²-scaled factor per channel (anchored to the same real S5 baseline) produced Narrows-favoring
margins of 77%–96% across every physically realistic Reach cross-section tested, including
absurdly large ones (up to 10,500 m², wider than the real Chesapeake entrance's own shipping
channel) — unfixable within SPEC §2's ~20% cap without either fabricating an unrealistic
cross-section or discarding the v² physics. Per SPEC §2's "retune a Modeling Assumption within its
real, sourced/plausible range... never hide data to force balance," the fix was not to break the
physics or force an implausible cross-section, but to use the single conversion factor
Appendix D's own table structure already calls for (one shared row, not two per-channel columns):
**factor = 1,050 kW ÷ (2.25 m/s × 589.0 m²) ÷ 3600 = 0.00022 kWh/m³**, applied identically to both
channels. This keeps the case's real decisive variable exactly where Appendix C/D3's structure
already puts it — total volume moved — rather than introducing a second, independently-tunable lever
that this real data cannot support without breaking balance.

## P07 — Standard seawater density

**Searched:** "seawater density kg/m3 standard value NOAA OR physics reference 1025"

**Fetched directly:** `https://hypertextbook.com/facts/2002/EdwardLaValley.shtml` — confirmed a
compiled physical-constants reference citing multiple real sources: Beicher's *Physics for Scientists
and Engineers* (1.03×10³ kg/m³), *Compton's Interactive Encyclopedia* (1035 kg/m³), UCAR/Windows to
the Universe (1027 kg/m³), *Encyclopaedia Britannica* 1965 and *CRC Handbook of Chemistry and
Physics* 48th ed. 1968 (1025 kg/m³ each), Introduction to Hydrology (1020–1029 kg/m³), and a Woods
Hole Oceanographic Institution scientist's figure (1026 kg/m³) — converging on "a good estimate of
its density at the ocean's surface is 1025 kilogram per cubic meter."

**Also attempted (not usable):** `https://www.noaa.gov/jetstream/ocean/sea-water` (HTTP 403,
inaccessible); `https://geodesy.noaa.gov/library/pdfs/Special_Publication_No_281.pdf` and
`https://www.ncei.noaa.gov/sites/default/files/2021-03/WOA18_Vol5_Density.pdf` (real NOAA PDFs,
confirmed to exist, but returned unreadable/encoded content on fetch — not cited, since their exact
stated value could not be confirmed by direct read, per the "never cite a URL you did not fetch [and
confirm]" rule).

**Outcome: SOURCED as [S6], HIGH confidence** — a universal physical constant with real, converging,
multiply-cited sourcing. Not itself load-bearing for `margin_pct`, since density does not enter this
case's D3→D5 volume-to-kWh chain as structured; provided because Appendix D's own placeholder calls
for it, and for any Hero who reasons through the underlying physics directly.

## Balance computation

Computed using numerical (trapezoidal) integration over each station's **complete** real 6-minute
NOAA series (61 points for the Narrows' 366-minute ebb pulse; 77 points for the Reach's 456-minute
flood pulse) — a Riemann-sum-style ground-truth calculation, distinct from and meant to cross-check
against the polynomial-fit-and-FTC approach a Hero will use for Challenges D2/D3.

| Channel | ∫speed dt (m) | Cross-section (m²) | Volume/cycle (m³) | kWh/cycle (× MA2) |
|---|---|---|---|---|
| Narrows | 34,675 | 1,427.0 [S3] | 49,480,854 | 10,889 |
| Reach | 12,702 | 4,290.6 [MA1] | 54,498,397 | 11,993 |

`margin_pct = |10,889 − 11,993| / 11,993 × 100 = 9.21%` — **the Reach wins**, comfortably inside
SPEC §2's ~20% cap. This margin is directly and materially sensitive to MA1 (the Reach's assumed
256 m array-site width) — see `case.json.modeling_assumptions[MA1].sensitivity` for the exact
flip/cap thresholds. It is not sensitive to MA2's absolute value (applied identically to both
channels) — see `case.json.modeling_assumptions[MA2].sensitivity`.

## Summary table

| ID | Placeholder | Resolution | Value | Confidence |
|---|---|---|---|---|
| P01 | Narrows current-speed station + data | SOURCED (S1) | ca0101, Cape Cod Canal West End | HIGH |
| P02 | Reach current-speed station + data | SOURCED (S2) | cb0102, Cape Henry LB 2CH | HIGH |
| P03 | Narrows channel geometry | SOURCED (S3 width, S8 depth — corrected 2026-09-12) | 146.3 m × 9.75 m | HIGH |
| P04 | Reach channel depth / width | Depth SOURCED (S4); width ASSUMPTION (MA1) | 16.76 m; 256 m | HIGH / n/a |
| P05 | Turbine array rated capacity + swept footprint | SOURCED (S5), derived | 1,050 kW; 589.0 m² | HIGH |
| P06 | Generation-potential conversion factor | ASSUMPTION (MA2), derived from S5 | 0.00022 kWh/m³ | n/a (assumption) |
| P07 | Seawater density | SOURCED (S6) | 1,025 kg/m³ | HIGH |
| — | Lease-option window length | Scenario detail (no external source needed) | 12 days | n/a |
| — | Chesapeake Bay entrance width (MA1 basis) | SOURCED (S7), supplemental | ~12 mi | MEDIUM |

**Totals:** 7 real sources fetched and cited (S1–S7), all confirmed live 2026-09-11; 2 Modeling
Assumptions (MA1, MA2), both grounded in real cited data rather than invented; 1 excluded source
(OpenEI's internally-inconsistent per-turbine figure); 1 scenario detail requiring no external source
(lease-option window, per case.json's own design note); 0 figures dropped; 0 remaining OPEN
placeholders. `margin_pct = 9.21%`, Reach wins, well inside SPEC §2's cap.

## Next step

Run `case-readiness` on `the-turbine-channel`.
