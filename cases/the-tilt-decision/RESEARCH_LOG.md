# Research Log — Tilt Decision

One row per `{{NEEDS_SOURCE}}` placeholder originally in `case.md`. Grouped by the appendix row
they filled, since most placeholders in Appendix B and D were one of a small number of research
efforts run once and applied to many table cells.

## Appendix A — Site and Racking Specifications

**Site latitude / longitude.** Searched "Sacramento California city hall latitude longitude
decimal degrees NOAA." No NOAA-specific coordinate page surfaced for a city point (NOAA publishes
station coordinates, not city coordinates). Used a geocoding aggregator's coordinates for
Sacramento City Hall (38.5816, -121.4944) as a representative site point — the case does not claim
a specific verified street address, only "a residential rooftop in Sacramento," so a defensible
representative point was sufficient. Considered pulling from USGS GNIS directly but the search
did not surface a clean per-city coordinate page within a reasonable search budget; the aggregator
figure is standard and undisputed for a city-level location. **Confidence: MEDIUM.** → S1.

**Number of panels.** No public record can exist for a fictional household's array size — this
was never going to be a SOURCED figure. Converted to **Modeling Assumption MA1** (20 panels).
Checked whether this figure is load-bearing first: the case's primary metric (Background,
Dilemma) is stated *per panel*, and panel count is identical across both options, so it cancels
out of the A-vs-B comparison entirely. Zero sensitivity — documented as such in MA1 rather than
treated as a risk.

**Panel rated power, STC.** Searched "Qcells Q.PEAK DUO ML-G11+ 400W spec sheet" (a guessed model
name) — did not exist under that exact designation; Qcells' ML-G11 series actually starts at
480W. Re-searched more openly for a Qcells 400W panel and found the Q.PEAK DUO BLK M-G11 series
(380-400 Wp, 108 cells). Fetched the manufacturer's own datasheet PDF directly (media.qcells.com);
initial WebFetch attempt returned a garbled/binary read, so the PDF was downloaded and run through
`pdftotext -layout`, which cleanly surfaced the power-class table confirming a 400W model exists
in this series (doc `Q.PEAK_DUO_BLK_M-G11_series_380-400_30T_2022-06_Rev01_EN`). **Confidence:
HIGH** (manufacturer's own spec sheet). → S2. Also attempted to cross-check via California's CEC
solar equipment list (solarequipment.energy.ca.gov) since the site is in California; the list's
JS-paginated table would not render its rows through WebFetch (returned "does not contain any
entries matching" even for models a plain web search confirmed were listed on that domain) — not
pursued further since the manufacturer datasheet alone already clears the HIGH bar.

**Racking system min/max tilt.** This was the hardest figure to source. Latitude Lock's angle
(~39°) rules out most named residential tilt-leg products, which commonly cap around 30° (checked
and rejected: IronRidge Fixed Tilt Legs, 4-30°/6-30° — [ironridge.com/component/tilt-legs/];
IronRidge Tilt Mount for flat roofs, up to 30° — [ironridge.com/flat-roofs/tilt-mount/]; SnapNrack
Ultra Rail tilt/standoff combinations, 5-30°). Tried Unirac SolarMount Tilt Legs (low/high
profile) directly — the installation manual PDF downloaded cleanly but its angle values are baked
into vector diagrams, not extractable text (`pdftotext` returned only leg-length and hardware
tables, no degree figures); a forum comment referenced "18 to 55 degrees" for a 104" high-profile
leg but this was a reader's comment, not the manufacturer's own stated spec, so it was not used.
Found Clenergy's PV-ezRack SolarRoof Adjustable Tilt Legs, stated (via search-result summary of
the manufacturer's own product page) to support 10-60°, wide enough to cover both option tilts
comfortably. Attempted to independently fetch clenergy.com and clenergy.com.au directly — both
returned HTTP 403 (Cloudflare bot-challenge pages), so the figure could not be verified with a
full primary-page fetch, only corroborated by an independent ENF Solar directory listing for the
same named product. **Confidence: MEDIUM** — noted as not load-bearing regardless, since it is a
feasibility gate only (both actual option tilts, 39° and 24°, sit well inside 10-60° even with
some uncertainty in the true limits). → S3.

**Latitude Lock tilt angle.** Derived, not separately sourced: site latitude 38.5816° [S1] rounded
to the nearest whole degree (39°) — installers set tilt-leg angle to whole-degree resolution.

**Summer Shift tilt angle.** Searched for a solar-design reference stating the "latitude minus 15
degrees" summer rule of thumb. Multiple SEO/calculator sites repeat the rule without attribution
(rejected as LOW-confidence, no defensible provenance for a load-bearing angle). Found a
peer-reviewed academic source stating the same rule in general form: Lave & Kleissl (2011, Solar
Energy), hosted at UC San Diego. **Confidence: MEDIUM** (a general nationwide study, not a
Sacramento-specific design table, but a real citable primary academic source rather than an
uncredited blog repetition). → S4. 38.5816 - 15 = 23.58, rounded to 24°.

## Appendix B — Modeled Monthly Output by Tilt Angle (all 26 cells)

Ran NREL's PVWatts Calculator via its live v8 API (`developer.nlr.gov/api/pvwatts/v8.json`) with
`api_key=DEMO_KEY`, `lat=38.5816`, `lon=-121.4944`, `system_capacity=0.4` (one 400W panel),
`azimuth=180`, `array_type=1` (fixed roof mount), `module_type=0` (standard), `losses=14` (PVWatts
default), once at `tilt=39` (Option A) and once at `tilt=24` (Option B) — every other input held
identical between runs, per the case's own Appendix B instructions. This is a direct, real-time
call against NREL's production government API, not a remembered or estimated figure.
**Confidence: HIGH.** → S5 (all 26 cells, one source row).

Noted in passing: PVWatts' domain moved from `developer.nrel.gov` to `developer.nlr.gov`
(retired May 29, 2026) — used the current domain.

## Appendix C — Utility Time-of-Use Rate Schedule (all 7 rows)

Searched "SMUD residential time-of-use rate schedule 2026." Sacramento is served by SMUD (a
municipal utility, not PG&E, despite Sacramento's proximity to PG&E territory — confirmed this
before proceeding, since assuming the wrong utility would have poisoned every downstream figure).
Fetched SMUD's own "Time-of-Day (5-8pm) Rate — Rate details" page directly and got clean rendered
text: summer = Jun 1-Sep 30, on-peak = 5-8pm daily, summer on-peak = $0.3765/kWh, non-summer
off-peak = $0.1285/kWh, non-summer on-peak = $0.1776/kWh. **Confidence: HIGH** (utility's own
published page). → S6.

Attempted to also fetch the underlying official tariff PDF (`1-R-TOD.ashx`) and the "2026
Residential Rate Guide" PDF for a second, more formal confirmation — both downloaded but returned
corrupted/font-encoded text unusable for extraction (embedded custom font encoding, not a plain
text layer). Did not block on this since the rate-details page already cleared HIGH.

**Non-summer rate choice.** The rate plan actually has two non-summer rates (on-peak $0.1776,
off-peak $0.1285), not one. The case's Appendix C asks for a single "non-summer (winter) rate."
Chose the off-peak rate as representative, since it is what most non-summer hours are billed at
and matches the case's own simplified month-level (not hour-level) weighting scheme. Tested the
alternative (on-peak $0.1776) explicitly: the weighted-output ranking between Option A and Option
B is unchanged either way (Summer Shift wins both times), only the margin size changes (2.13% vs.
1.37%) — so this interpretive choice is not dilemma-flipping, and is documented as such in S6's
note rather than hidden.

## Appendix D — Solar Position Reference Table (all 16 table cells + 12 monthly samples)

NOAA's interactive Solar Calculator (gml.noaa.gov/grad/solcalc) is not a scriptable data source —
it returns an HTML page, not an API. Instead of scraping it, implemented NOAA's own published
solar-position algorithm (the same declination / equation-of-time / hour-angle equations NOAA's
calculator itself runs, documented at gml.noaa.gov/grad/solcalc/solareqns.PDF) directly in Python,
and ran it for the 2026 solstices/equinoxes and all twelve mid-month dates, at the site's latitude
and longitude, using correct Pacific Daylight/Standard Time offsets for each date.

Verified correctness before trusting the output: solar-noon elevation has a closed-form check,
`elevation = 90° - |latitude - declination|`. The script's summer-solstice solar-noon value (74.9°)
matches `90 - (38.5816 - 23.44) = 74.86°` exactly, and the winter-solstice value (28.0°) matches
`90 - (38.5816 - (-23.44)) = 27.98°` exactly — confirming the implementation reproduces the
standard astronomical identity rather than containing a sign or unit error.
**Confidence: HIGH** (exact published formula, independently cross-checked). → S7.

## What was NOT found / converted

- **Number of panels** — NOT FOUND (cannot be a matter of public record for a fictional
  household) → converted to Modeling Assumption MA1 (see above). Zero sensitivity: it is a
  per-panel metric and the count is identical across options, so it cannot flip the dilemma.
- No other placeholder required a Modeling Assumption or a redesign. All other 57 placeholders
  were sourced.

## Margin (facilitator-only — not written into case.md)

Using S5's PVWatts output and S6's rate multiplier (2.93, off-peak-based): Option A (Latitude
Lock) wins raw annual kWh per panel (659.3 vs. 656.2, a 0.47% edge) — matching the case's own
narrative that a competing installer's bold cover-page number favors A. Option B (Summer Shift)
wins the case's actual primary metric, weighted effective annual kWh per panel (1187.5 vs. 1162.8,
a **2.13% margin for B**). Recorded in `case.json`'s `margin_pct` (2.13) and `balance.margin_pct`,
and in `FACILITATOR.md` — not in `case.md`.

## Next step

Run `case-qa` on `the-tilt-decision`.
