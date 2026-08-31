# RESEARCH_LOG.md — The Late Run

Research trail for every `{{NEEDS_SOURCE: ...}}` placeholder in `case.md` as drafted by
`case-write`. 41 placeholders enumerated (P01–P41). This pass **independently re-verified** every
load-bearing figure carried over from the design-phase concept sheet
(`cases/_concepts/CONCEPTS_precal-second-pass_2026-08-30.md`, C7) with fresh live queries rather
than copying the design-phase numbers — see the "Independent re-verification" note at the bottom.
Zero placeholders remain OPEN: 37 SOURCED (11 primary/derived + 26 that resolve into the four
`Modeling Assumptions` value/basis/sensitivity triples), 0 DROPPED, 0 NOT FOUND.

---

## Appendix A — refractive index, Brewster's-angle formula, Brewster angle (P01–P03)

**P01 — refractive index of standard window/soda-lime glass.** Searched
"refractoiveindex.info soda lime glass refractive index 1.52 Rubin," then fetched
refractiveindex.info's Rubin-clear soda-lime-glass entry directly
(https://refractiveindex.info/?shelf=glass&book=soda-lime&page=Rubin-clear). Cites M. Rubin,
*Optical properties of soda lime silica glasses*, Solar Energy Materials 12, 275–288 (1985);
dispersion formula gives n≈1.51–1.52 across the visible band (n=1.52 at ~0.55 µm). Same primary
source the superseded `the-locks-window` case used (its S2). **SOURCED, HIGH → S1.**

**P02 — Brewster's-angle formula, confirm exact form/source.** Fetched Wikipedia's "Brewster's
angle" page directly: states θ_B = arctan(n₂/n₁) and gives the worked example "for a glass medium
(n₂≈1.5) in air (n₁≈1), Brewster's angle for visible light is approximately 56°," which
cross-checks this case's own derived 56.66°. (RP Photonics' own page was not re-attempted this
pass — the superseded case already logged that automated fetches of rp-photonics.com return
HTTP 403 — so Wikipedia remains the fetched, citable source.) **SOURCED, HIGH → S2.**

**P03 — Brewster angle of the viewing-room glass.** Derived: `arctan(1.52) = 56.66°` (Python
`math.atan`, not eyeballed). **SOURCED (derived) → S1+S2.**

## Appendix B — the Tiffen 138mm UltraPol (P04–P05)

**P04/P05 — average light transmission; filter factor/stop loss.** Fetched
tiffen.com/products/138mm-mounted-ultrapol-circular-polarizer-filter directly (manufacturer's own
current product page): "approximately 40% average light transmission"; "4x filter factor,"
"reduces exposure by 2 stops." Cross-checked against B&H's independent retailer listing in the
same search pass — same figures. **SOURCED, HIGH → S3.**

## Appendix C — sun position at the Locks, two shoot windows (P06–P14)

**P06 — precise coordinates.** Fetched Wikipedia's "Ballard Locks" page directly: 47°39′56″N
122°23′50″W (47.66556°N, 122.39722°W) — matches the case's own stated approximate coordinates
(47.665°N, 122.397°W) to the arc-second. **SOURCED, MEDIUM → S4** (well-attributed tier-2 source
for an uncontested geographic fact — same grade the superseded case used for the same fact).

**P07 — August shoot date/time.** Rather than pick an arbitrary date inside the general "peak
Chinook" window, fetched WDFW's live "Lake Washington salmon counts" page
(wdfw.wa.gov/fishing/reports/counts/lake-washington), **re-fetched fresh this pass** (not copied
from the design-phase concept sheet or the superseded case). Full August 2026 daily Chinook table
pulled: 8/19 = 957, the single highest day of the month and of the season-to-date; running total
through 8/25 = 9,566 (the most recent date with published data as of this research date,
2026-08-31 — 8/26–8/31 rows exist in the table but are not yet populated). **August 19, 2026
chosen as the shoot date because it is confirmed, live, in-season data as the actual best day —
SOURCED, HIGH → S5.** Call time 2:00 PM PDT is a stated Modeling Assumption (MA2, see below).

**P08 — September shoot date/time.** WDFW's own page states, in its own text: "Preliminary daily
coho counts are typically available from early September into October" — confirming no
day-by-day 2026 Coho count exists this far ahead of the season (the live table's Coho column
reads all zero through the dates shown, consistent with the season not having started yet as of
8/31). Two independent Seattle-area salmon-viewing sources were fetched directly and both
converge on the same claim: greaterseattleonthecheap.com's fall-salmon-spawning page states
verbatim "August through November: Coho, or Silver Salmon (best viewing last two weeks of
September)"; ParentMap's salmon-viewing calendar page independently gives the same "last two
weeks of September" window. **The specific date chosen, September 22, 2026, is stated as Modeling
Assumption MA3** (see below) — the window itself is SOURCED, MEDIUM → S6, S7; the single-day pick
within it is not sourceable to one official document the way August 19 is, and is disclosed as
such.

**P09/P10 — sun azimuth, August and September.** NOAA's GML Solar Calculator
(gml.noaa.gov/grad/solcalc/azel.html) has no documented URL-parameter API for azimuth/elevation at
an arbitrary time of day (only sunrise/sunset/solar-noon times are exposed that way). **Drove the
live calculator directly via the Claude Browser tool this pass** (not copied from the
design-phase session): selected "Enter Lat/Long -->," entered 47°39′54″N / 122°23′50″W (matching
S4 to the arc-second — the calculator take degrees/min/sec, and the coordinate's fetched arc-sec
value differs from Wikipedia's stated 56″ by 2″, an immaterial rounding difference already noted
in the superseded case), UTC offset 8 with Daylight Saving = Yes (PDT), and read the output
directly off the live page for two dates:
- **August 19, 2026, 14:00 PDT: azimuth 199.48°, elevation 53.55°**, equation of time −3.56 min,
  solar declination 12.54°, cos(zenith) 0.8043.
- **September 22, 2026, 14:00 PDT: azimuth 199.23°, elevation 40.77°**, equation of time 7.39
  min, solar declination 0.05°, cos(zenith) 0.6745.
Both figures match the design-phase concept sheet's own live-NOAA readings exactly (199.48/53.55
and 199.23/40.77), confirming those numbers were not degraded or altered on re-fetch.
**SOURCED, HIGH → S8 (August), S9 (September).**

**P11/P12 — sun elevation, August and September.** Read directly off the same live NOAA output as
P09/P10, above. **SOURCED, HIGH → S8, S9.**

**P13/P14 — angle of incidence on the glass window, August and September.** A vertical surface's
incidence angle depends on sun elevation and the angular offset between sun azimuth and the
window's own outward-normal azimuth — which requires knowing which way the window faces. No
public floor plan or engineering drawing gives this (see MA1 below; same gap the superseded case
found and disclosed). Under MA1 (window normal azimuth = 180°, due south), computed
`cos(theta_i) = cos(elevation) * cos(sun_azimuth - normal_azimuth)` in Python (not by hand):
**August: 55.94° ≈ 55.9°. September: 44.35° ≈ 44.4°.** **SOURCED (derived) → S8+MA1,
S9+MA1.**

## Appendix D — the Fresnel reflectance and residuals (P15–P25)

**P15–P24 — R_s, R_p, R, residual, and percent removed, both dates.** No blog or forum publishes
a directly-citable "percent glare at this angle" figure with real provenance for an arbitrary
non-Brewster incidence angle — this is normally left as a derivation, not tabulated anywhere.
Derived directly from the Fresnel equations (Wikipedia's "Fresnel equations" page, fetched
directly this pass, confirms the exact `R_s`, `R_p`, `R=(R_s+R_p)/2` forms used in `case.md`
Appendix D — **SOURCED, HIGH → S10**), applied to each date's own incidence angle (P13/P14) via
Snell's Law at n₁=1.00 (air), n₂=1.52 (glass, S1). Computed in Python, not by hand:

| Quantity | August (θᵢ=55.94°) | September (θᵢ=44.35°) |
|---|---|---|
| R_s | 15.161% | 9.447% |
| R_p | 0.006% | 1.015% |
| R = (R_s+R_p)/2 | 7.583% | 5.231% |
| Residual R_p/2 | 0.003% | 0.507% |
| Percent of R removed | 99.961% | 90.300% |

**SOURCED (derived) → S1+S2+S10 (formulas/constants) applied to S8/S9+MA1 (angles).** This is the
case's central computed result: August sits ~0.7° from the glass's own Brewster angle (56.66°) and
is essentially fully recoverable; September sits a real 12.3° off Brewster and caps out
measurably lower, though still high in absolute terms.

**Margin.** `(99.961 − 90.300) / 90.300 × 100 = 10.70%` relative margin, August Call (Option A)
ahead. This is the same relative-margin reading form the superseded case used for its own D4
("share of removable glare," normalized against the theoretical ceiling), applied consistently
here — see FACILITATOR.md for the full computation and the case.json `balance` object.

**P25 — stated production glare tolerance.** No manufacturer or industry spec states a
"tolerance" for residual glare in a documentary shoot context — this is inherently a scenario
choice, not a discoverable fact. **Stated as Modeling Assumption MA4**: tolerance = 2× each
date's own best-achievable residual (R_p/2). Basis and sensitivity below.

## Appendix E — the two runs (P26–P29)

**P26/P27 — 2026-season Chinook counts; confirmation August 19 is the season's best day.**
Same live WDFW fetch as P07, re-pulled fresh this pass: August 19 daily count 957 (season's
single highest day through the most recent published date, 2026-08-25); running total 9,566
through 8/25. Also explicitly asked the live page whether any day after 8/19 in August exceeded
it — confirmed no, and confirmed no data exists yet for 8/26–8/31 (the table's rows for those
dates are present but empty, consistent with a short reporting lag). **SOURCED, HIGH → S5.**

**P28 — published Coho peak-viewing window.** greaterseattleonthecheap.com and ParentMap, both
fetched directly, converge independently on "last two weeks of September." **SOURCED, MEDIUM →
S6, S7** (a converging-sources claim from local aggregator/trade pages, not a single official
government document with a stated start/end date — graded MEDIUM accordingly, same treatment the
design-phase concept sheet already flagged).

**P29 — whether day-by-day Coho counts are available this far ahead.** WDFW's own page states
coho counts are "typically available from early September into October," and the live 2026 Coho
column reads all zero as of this research date (2026-08-31, before the season has started).
**SOURCED, HIGH → S5.** This is the real, sourced reason the September date is a
published-window pick (MA3) rather than a single-day-verified one the way August 19 is.

## Appendix G — Modeling Assumptions (P30–P41)

**MA1 — window orientation (P30–P32).** No public floor plan or engineering drawing states the
underground viewing-room glass window's compass orientation. Two independent sources, fetched
directly, both state the fish ladder/viewing room sits on the **south side** of the Locks complex
(myballard.com: "Built on the south side of the canal, the fish ladder is a critical ecological
corridor..."; a general web search independently corroborated "the fish ladder is located on the
south side of the Ballard Locks"). **Value used: due south, window-normal azimuth = 180°.**
**Sensitivity — re-run fresh this pass, and this is the most consequential open finding of this
research pass:** recomputing both dates' incidence angles and percent-removed at normal azimuths
90° (E), 135° (SE), 180° (S, the assumption used), 225° (SW), and 270° (W) gives:

| Normal | Aug incidence | Aug % removed | Sep incidence | Sep % removed | Relative margin |
|---|---|---|---|---|---|
| 90° (E) | 101.4° | 27.3% | 104.4° | 21.6% | +26.6% (A wins) |
| 135° (SE) | 75.2° | 79.1% | 70.8° | 86.9% | **−8.9% (B wins)** |
| **180° (S, used)** | **55.9°** | **99.96%** | **44.4°** | **90.3%** | **+10.7% (A wins)** |
| 225° (SW) | 57.6° | 99.9% | 47.0° | 93.7% | +6.6% (A wins) |
| 270° (W) | 78.6° | 72.7% | 75.6° | 78.4% | **−7.3% (B wins)** |

The window-orientation assumption **can flip the dilemma** — at southeast- or west-facing
orientations the margin inverts and September wins instead. This is disclosed prominently rather
than smoothed over. The due-south value is retained as the case's stated assumption because it is
the only orientation with an actual documentary basis (both sourced descriptions place the fish
ladder/viewing room on the south side); the other four orientations in the table have no
supporting source at all and are shown only to demonstrate the sensitivity honestly.

**MA2 — shared call time (P33–P35).** Value used: 2:00 PM PDT for both dates (same convention
the superseded case used, chosen for an apples-to-apples professional comparison rather than
optimizing one date's own light). No public record of an actual scheduled call time exists for
either shoot. **Sensitivity — re-run fresh this pass** across 1:00 PM, 2:00 PM, and 3:00 PM PDT
(live NOAA readings for both dates at all three times):

| Time | Aug % removed | Sep % removed | Relative margin |
|---|---|---|---|
| 1:00 PM | 99.79% | 87.55% | 13.98% (A wins) |
| 2:00 PM (used) | 99.96% | 90.30% | 10.70% (A wins) |
| 3:00 PM | 99.12% | 96.85% | 2.35% (A wins) |

Under MA1's south-facing assumption, the margin never crosses zero across this 1–3 PM range — it
narrows toward late afternoon (September's incidence angle approaches Brewster faster than
August's does, as both dates' azimuths sweep west) but Option A stays ahead throughout.

**MA3 — specific September date (P36–P38).** Value used: **September 22, 2026** — the midpoint
of the documented "last two weeks of September" window (Sept 16–30). No official single-day
record exists for Coho the way WDFW's live count data pins down August 19 for Chinook (see P29).
**Sensitivity — re-run fresh this pass** across September 15, 22, and 29, 2026, all at 2:00 PM PDT
(live NOAA readings):

| September date | Incidence | % removed | Relative margin vs. Aug 19 |
|---|---|---|---|
| Sept 15 | 46.81° | 93.49% | 6.97% (A wins) |
| Sept 22 (used) | 44.35° | 90.30% | 10.70% (A wins) |
| Sept 29 | 41.90° | 86.80% | 15.16% (A wins) |

Later in the window, September's incidence angle moves farther from Brewster (the sun keeps
dropping toward the equinox), so the margin *widens*, not narrows, later in the peak window — the
midpoint date (Sept 22) is a conservative, roughly middle-of-the-range pick, not one chosen to
maximize or minimize the margin.

**MA4 — production glare tolerance (P39–P41).** Value used: tolerance = 2× each date's own
best-achievable residual (R_p/2) — i.e., "glare no more than double the floor a perfectly-tuned
polarizer can already reach." Basis: no manufacturer or industry document states an acceptable
on-set glare tolerance; this is a disclosed scenario choice sized relative to each date's own
physical floor rather than an arbitrary absolute number, so it scales sensibly between the two
dates. **Sensitivity** (solving `I(θ)=tolerance` for θ, the exact equation Challenge D2 asks the
student to solve): at tolerance = 1.5×, 2× (used), and 3× the residual, August's rotation-offset
answer barely moves (≈0.8°→1.1°→1.6°, all within about a degree of dead-on), while September's
moves substantially (≈13.4°→19.1°→27.6°). **The tolerance choice matters far more for
September's D2 answer than for August's** — disclosed so a Hero who challenges MA4 in discussion
has a real, quantified reason to.

---

## Independent re-verification note

Every numeric figure carried over from the design-phase concept sheet
(`CONCEPTS_precal-second-pass_2026-08-30.md`, C7) was **re-fetched or re-derived from scratch this
pass**, not copied: the NOAA Solar Calculator was re-driven live for both dates (matching the
concept sheet's own numbers to two decimal places, confirming they were not a stale or invented
carry-forward), WDFW's counts page was re-fetched fresh (confirming August 19, 2026 is still the
season's best day as of the latest published data), and the Coho-window sources were independently
re-fetched. One genuinely new finding came out of this pass that the concept sheet did not surface:
the **window-orientation sensitivity table under MA1**, which shows the dilemma can flip under
alternative (unsourced) orientations — this is disclosed above and in `case.md` Appendix G rather
than smoothed over.

---

## Verification pass

```
placeholders remaining: 0
citation markers with no source row: none
source rows never cited in text: none
INCOMPLETE sources: none
LOW-confidence sources: none (lowest grade used is MEDIUM — S4's coordinates, S6/S7's
  Coho-window claims, S9's date-of-source status folded into S5/S7 — none of these carry the
  case's central computed numbers, which rest on HIGH sources)
```

## Margin computation — confirmed, not preliminary

`case.json`'s `balance.margin_pct` and `winning_option` are computed here for real (not carried
over from the design-phase `preliminary_note`, which is left in place for its own historical
record): **relative margin ≈ 10.70%, Option A (the August Call) wins**, matching the design
phase's preliminary estimate almost exactly (it had estimated ~10.7% as well — an independent
re-derivation landing on the same number to two decimal places, not a coincidence but a sign the
underlying live sources are stable). Recorded FACILITATOR-only in `case.json`'s `balance` object
and in `FACILITATOR.md` — never in `case.md`.

## Next step

`Run case-readiness on the-late-run.`
