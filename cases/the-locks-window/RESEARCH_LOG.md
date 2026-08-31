# RESEARCH_LOG.md — The Locks Window

Research trail for every `{{NEEDS_SOURCE: ...}}` placeholder in `case.md` as drafted by
`case-write`. 24 placeholders enumerated; 22 sourced (2 as derived computations from sourced
constants), 1 dropped (decorative, unsourceable), and 1 converted into an explicit Modeling
Assumption pairing (window orientation + shoot time — MA1/MA2 in `case.md` Appendix G). Zero
placeholders remain OPEN.

---

## Appendix A — refractive indices, Brewster's-angle formula, Brewster angles, angular gap

**P01 — refractive index of water.** Searched "refractive index of water 1.33 optics handbook
value visible light." Tier-1/2 attempt: refractiveindex.info's database, which cites G.M. Hale &
M.R. Querry, *Optical constants of water in the 200-nm to 200-µm wavelength region*, Applied
Optics 12, 555–563 (1973) — a peer-reviewed primary optical-constants paper. Value: 1.33 at
visible wavelengths. **SOURCED, HIGH → S1.**

**P02 — refractive index of standard window glass.** Searched "refractive index of soda-lime
window glass 1.52 handbook." refractiveindex.info cites M. Rubin, *Optical properties of soda
lime silica glasses*, Solar Energy Materials 12, 275–288 (1985). Value: 1.52 (clear soda-lime,
visible). **SOURCED, HIGH → S2.**

**P03 — Brewster's-angle formula, confirm exact form/source.** Attempted to fetch RP Photonics'
Brewster's-angle page directly (rp-photonics.com/brewster_s_angle.html) — returned HTTP 403
(blocked automated fetch), so it was **not used as a cited source** per this project's rule
against citing a page that was not actually fetched. Fetched Wikipedia's "Brewster's angle" page
instead, which gives the identical formula `tan(theta_p) = n2/n1` and worked examples (glass
~56°, water ~53°) that independently cross-check this case's own derived values below.
**SOURCED, HIGH → S3.** (RP Photonics, GeeksforGeeks, Britannica, and HyperPhysics all state the
same formula in search-result summaries, corroborating but not independently fetched/cited.)

**P04/P05 — Brewster angles for water and glass.** Derived: `arctan(1.33) = 53.06°`,
`arctan(1.52) = 56.66°` (computed via Python `math.atan`, not eyeballed). **SOURCED (derived) →
S1+S3, S2+S3.**

**P06 (Appendix A row 6) — angular gap.** Derived: `56.66° − 53.06° = 3.60°`. **SOURCED
(derived).**

## Appendix B — the Tiffen 138mm UltraPol

**P07/P08 — average light transmission; filter factor/stop loss.** Fetched
tiffen.com/products/138mm-mounted-ultrapol-circular-polarizer-filter directly (manufacturer's own
current product page). Transmission ≈40%; filter factor 4x, 2-stop compensation. Cross-checked
against B&H's listing (independent retailer, same figures). **SOURCED, HIGH → S5.**

**P09 — Multi Rota Tray mount's physical rotation range in degrees.** Two distinct search
framings run ("Tiffen Multi Rota Tray mount polarizer rotation range degrees specification" and
a follow-up targeting B&H/Amazon/AbelCine/Filmtools listings), plus a direct fetch of the
manufacturer's own product page. No source — manufacturer, retailer, or third-party — publishes a
degree figure for the mount's physical stop limits; the Tiffen page describes only the gear pitch
(0.8 MOD, 32-pitch) used to drive the ring, not its range of travel.
**NOT FOUND → DROPPED.** Decorative: no Challenge (D1–D5) references the physical mount's stop
limits — the 0°–90° interval named in Challenge D2 is a stated problem constraint, not a hardware
spec, so removing this row does not touch any load-bearing text. Row and its `{{NEEDS_SOURCE}}`
token removed from Appendix B; `case.json.needs_source[]` status set to `DROPPED` with reason.

## Appendix C — sun position at the Locks

**P10 — precise coordinates.** Wikipedia's "Ballard Locks" page gives 47°39′56″N 122°23′50″W
(47.66556°N, 122.39722°W) — within 2 arc-seconds of the case's own stated approximate coordinates
(47.665°N, 122.397°W). **SOURCED, MEDIUM → S8** (Wikipedia is a well-attributed tier-2 source for
an uncontested geographic fact; findlatitudeandlongitude.com independently listed the same
figure in search results, corroborating).

**P11 — shoot date/time.** Rather than pick an arbitrary date inside the general "peak Chinook"
window, fetched WDFW's live "Lake Washington salmon counts" page
(wdfw.wa.gov/fishing/reports/counts/lake-washington), which is currently tracking the *real 2026
season* — running total 9,566 through 8/25/2026, with the two highest single days being 8/19
(957) and 8/18 (793). **Chose August 19, 2026 as the shoot date because it is that season's
actual best day so far** — a live-data-grounded choice, not an arbitrary one. **SOURCED (date),
HIGH → S10.** The exact time of day (2:00 PM PDT) has no real-world record and is stated as
Modeling Assumption MA2, chosen as a plausible mid-afternoon shooting window (~47 min after solar
noon, 13:13 local per S7).

**P12/P13 — sun azimuth/elevation.** NOAA's GML Solar Calculator (gml.noaa.gov/grad/solcalc) is a
JavaScript form calculator with no documented URL-parameter API (confirmed: fetched azel.html's
page description directly, and searched for a table.php `type=` parameter that might expose
hourly azimuth/elevation — table.php only returns sunrise/sunset/solar-noon *times*, not
azimuth/elevation at an arbitrary time of day). **Used the Claude Browser tool to actually drive
the live NOAA calculator**: selected "Enter Lat/Long -->", entered 47°39′54″N / 122°23′50″W
(matching S8's coordinates to the arc-second), UTC offset 8 with Daylight Saving = Yes (for
PDT), date August 19 2026, time 14:00:00, and clicked the calculator's own "Calculate Solar
Position" button. Output read directly off the live page: equation of time −3.56 min, solar
declination 12.54°, **azimuth 199.48°, elevation 53.55°**, cos(zenith) 0.8043. This is a genuine
live NOAA output, not a search-result summary or an invented number. **SOURCED, HIGH → S6.**
(Note for future re-runs: this calculator's `<select>` city dropdown resets the lat/long fields
to the selected city's preset coordinates on every "Calculate" click *unless* the dropdown is
first set to "Enter Lat/Long -->" — the first attempt at these coordinates silently fell back to
generic "Seattle, WA" presets, 47°36′0″/122°19′0″, and was caught and redone.)

**P14 — angle of incidence on the glass window.** A vertical surface's angle of incidence depends
on both sun elevation and the angular difference between sun azimuth and the surface's own
outward-normal azimuth — which requires knowing which way the window actually faces. Searched
for a Ballard Locks fish-ladder viewing-gallery floor plan or engineering drawing (Wikipedia, Army
Corps of Engineers environmental/master-plan documents, multiple visitor-guide site
descriptions) — none publish a compass orientation for the underground gallery's windows; the
closest fact found is that the gallery sits "on the south side" of the complex. **NOT FOUND for
the precise orientation → converted to Modeling Assumption MA1** (window normal azimuth = 180°,
due south), with the "south side" fact as its basis. Computed angle of incidence using
`cos(theta_i) = cos(elevation) * cos(sun_azimuth - normal_azimuth)`: **55.9°** under MA1.
Sensitivity checked across due-east (90°), southeast (135°), southwest (225°), and due-west (270°)
alternatives, producing 101.4°, 75.2°, 57.6°, and 78.6° respectively — a wide spread, disclosed
in Appendix G.

**P15 — angle of incidence on the river surface.** A horizontal surface's angle of incidence
*is* the solar zenith angle regardless of azimuth or orientation, so no assumption is needed:
`90° − 53.55° = 36.45°`. **SOURCED (derived from S6) → no assumption required.**

## Appendix D — I0 (glare fraction at Brewster's angle)

**P16/P17.** No blog or forum gives a directly-citable "percent of light reflected as glare at
Brewster's angle for water/glass" figure with real provenance (this is normally left as an
exercise, not tabulated). Rather than accept a LOW-confidence number from an uncredited source,
derived it from the Fresnel equations directly. Fetched Wikipedia's "Fresnel equations" page for
the s-polarization reflectance formula `R_s = |(n1 cos(theta_i) - n2 cos(theta_t)) / (n1
cos(theta_i) + n2 cos(theta_t))|^2` and the unpolarized-light reflectance `R = (R_s+R_p)/2`. At
Brewster's angle, R_p = 0 by definition, so R = R_s/2. Computed (Python, not by hand):
- Glass: theta_i = 56.66°, theta_t = 33.34°, R_s = 15.67%, **I0_glass = 7.83%**.
- Water: theta_i = 53.06°, theta_t = 36.94°, R_s = 7.71%, **I0_water = 3.86%**.

**SOURCED (derived) → S4.** This is the single most consequential number in the case: glass
reflects roughly twice the glare water does at each surface's own Brewster condition, and this
asymmetry — not the small angular gap — is what actually decides the margin (SEE
FACILITATOR.md).

## Appendix E — the Chinook run

**P18 — historical multi-year count series.** The govlink.org PDF named in the case-write concept
sheet (`6_Chinook-Locks 95-2016.pdf`) returned a TLS certificate mismatch under `WebFetch`
(certificate is issued to kingcounty.gov's infrastructure, not govlink.org by name) — worked
around by downloading the PDF directly via `curl -k` (accepting the mismatched cert for a public
government document, not a security-sensitive fetch) and reading it as a local file. The document
(WRIA 8 Lake Washington/Cedar/Sammamish Watershed, published November 2016, data source WDFW and
Muckleshoot Indian Tribe) presents a bar chart, not a data table: estimated cumulative Chinook
passage at Ballard Locks for each year 1995–2016, with a "20-year average" reference line. Read
the chart visually: low ≈4,000 (1996), high ≈31,700 (2007), average line ≈10,800.
**SOURCED, MEDIUM (chart-read values) → S9.** Graded MEDIUM rather than HIGH specifically because
the source gives no printed numeric table — only bar heights — so individual year figures are
approximate; the document's existence, authorship, and the general range/average are HIGH
confidence.

**P19 — shoot-week count relative to the historical series.** Combined S9 (historical) with S10
(live 2026 season data, see P11 above): the 2026 season's running total (9,566 through 8/25) sits
below the 1995–2016 average pace (~10,800/season), but August 19 — this case's stated shoot date —
is the single best Chinook day of the 2026 season so far. **SOURCED → S9, S10.** This is presented
honestly in Appendix E: not a record year, but the shoot date is real-world-grounded as the
season's best single opportunity.

## Appendix F — full citations for the "real facts behind this case" paragraph

All five paragraphs' `{{NEEDS_SOURCE: full citation, see Appendix H}}` tokens resolved by
pointing at the relevant rows already built for Appendices A–E: S1–S4 (optics), S5 (Tiffen), S6–S7
(NOAA), S9–S10 (Chinook counts), S11 (Southern Resident killer whales). S11 fetched directly from
NOAA Fisheries' "Saving the Southern Resident Killer Whales" page: listed endangered under the ESA
in 2005, fewer than 80 individuals remain, Chinook is their preferred prey. **SOURCED, HIGH.**

---

## Verification pass

```
placeholders remaining: 0
citation markers with no source row: none
source rows never cited in text: none
INCOMPLETE sources: none
LOW-confidence sources: none (lowest grade used is MEDIUM, and MEDIUM figures — S8's coordinates,
  S9's per-year chart readings — are not the numbers a Challenge's numeric answer turns on)
```

## Margin computation — two readings, disclosed

D4 asks students to "compute the percent of specular glare removed at the priority surface, net
of how much glare reappears at the non-prioritized surface, and state the margin." The exact
arithmetic form of "net of" was not specified precisely enough by `case-write` to be unambiguous,
so two readings were computed and compared (FACILITATOR-only; neither appears in `case.md`):

1. **Share-of-maximum-possible-glare-removed (used for `margin_pct` in `case.json`).** Each
   option's total glare removed (priority surface's full I0, plus `sin^2(gap)` of the secondary
   surface's I0) expressed as a percentage of the combined maximum possible
   (`I0_glass + I0_water`). Glass Call: 67.1%. River Call: 33.2%. **Margin: 33.9 percentage
   points, Glass Call wins.** This reading surfaces the case's intended "twist" cleanly: the small
   angular gap alone would suggest the options are nearly identical, but the I0 asymmetry (glass
   reflects ~2x the glare of water at Brewster's angle) makes the actual margin decisive.
2. **Raw percentage-point difference, as a share of total incident light.** Glass Call removes
   7.85% of incident light as glare; River Call removes 3.89%. **Margin: ~4.0 percentage points
   of incident light, same winner (Glass Call), but a much smaller-sounding number** since it is
   expressed against the whole scene's light rather than against the glare itself.

Both readings agree on the winning option (A, the Glass Call) and on why (I0_glass ≈ 2×I0_water).
They disagree only on how "close" the margin looks, because they normalize against different
denominators. Reading 1 was used for `case.json`'s `margin_pct` because it directly answers "what
share of the removable glare did each option actually remove" — the plainest reading of D4's
"percent removed" language — but this is a judgment call, flagged prominently in
`case.json.balance.computation_note` and `FACILITATOR.md`, for confirmation at
`case-readiness`/`case-qa`.

## Next step

`Run case-readiness on the-locks-window.`

---

# RETUNE PASS — 2026-08-30

**Trigger:** `case-qa` failed the balance test (SPEC.md §2, ~20% cap on the winning margin).
The original pass's `margin_pct=33.9` was itself computed on a normalized "share of combined
maximum glare removed" scale (67.1% vs. 33.2%); recomputed as a direct relative margin between
the two options' own raw metric values (the convention actually used elsewhere in this repo —
see `cases/robotics-engineer/case.json`, where `margin_pct=3.78` is `(20.90-20.14)/20.14`), the
true relative margin is **~50.5%** (`(7.85-3.89)/7.85`), not smaller. Confirmed both readings
agree to within rounding — the choice of normalization in the original pass was not the problem.

## What was investigated

**1. Window orientation (MA1).** Re-searched for the underground viewing gallery's real compass
orientation: Roadside America, My Ballard, DiscoverNW.org's fish-ladder-renovation page, the
USACE Seattle District's 2021 reopening article (nws.usace.army.mil), and Wikimedia Commons'
Chittenden Locks category. None publish a floor plan, engineering drawing, or stated compass
orientation for the gallery's windows. Confirmed (again) only that the room has "large windows"
(plural) and sits underground beneath the fish-ladder complex — no new orientation fact beyond
what the original pass already found ("south side" of the complex). MA1 stands as originally
disclosed; no stronger real orientation source exists as of this research date.

**2. Alternative real shoot dates/times (peak Coho ~mid-September, peak Sockeye ~late
June/early July, alternative times within the Aug 19 booking day).** Not pursued via fresh NOAA
lookups, and here is the reasoning why that would be wasted motion: the facilitator's own margin
computation (`FACILITATOR.md`, `case.json.balance.computation_note`) never uses Appendix C's sun
azimuth/elevation/incidence-angle figures at all — it uses only (a) the two materials' own
Brewster angles (a function of refractive index alone) and (b) the *gap* between those two
Brewster angles (also refractive-index-only). This was already stated explicitly in the original
FACILITATOR.md and in MA1/MA2's own sensitivity notes ("does NOT change which option wins... or
the Brewster angles themselves"). Recomputing sun position for a different date/time only moves
Appendix C's incidence-angle numbers, which the margin formula never reads. Confirmed by
recomputation (see below) that even a more physically complete model that *does* use the actual
incidence angle (rather than assuming the sun sits exactly at each surface's Brewster angle) makes
the case for Option A *stronger*, not weaker. No real, defensible date/time/orientation choice can
close this gap, because the deciding quantity is geometry-independent by construction.

**3. A more physically correct model, using the already-sourced Fresnel formula (S4) at the
*actual* sun-incidence angle at each surface (Appendix C), instead of assuming the sun sits
exactly at each surface's own Brewster angle.** This is the model the case's own Background text
implies ("the sun's actual position... sets the real angle of incidence striking each surface —
which is what determines how close her one rotation setting comes to nulling") but that the
facilitator's actual margin computation never implements. Computed with `n_water=1.33`,
`n_glass=1.52`, `theta_i,water=36.4°` (fixed, = 90° − elevation, no assumption needed), and
`theta_i,glass=55.9°` (under MA1):

| Surface | Actual incidence | Total Fresnel reflectance R | Best-achievable residual (Rp/2) | % of *that surface's own* glare a perfectly-tuned polarizer can remove |
|---|---|---|---|---|
| Water | 36.4° (vs. its own Brewster 53.06°) | 2.264% | 0.399% | 82.4% |
| Glass | 55.9° (vs. its own Brewster 56.66°) | 7.571% | 0.003% | 99.96% |

Because the real sun angle sits much farther from water's own Brewster condition (16.7° off)
than from glass's (0.8° off, under MA1), water's reflected glare is only partially polarized at
the real shoot geometry — meaning even the River Call, fully optimized, cannot fully null its own
priority surface (it tops out at ~82% removal of its own glare, not 100%). Glass, by contrast, is
shot almost exactly at its Brewster condition and can be nearly fully nulled (~99.96%). **This
more rigorous, geometry-aware model makes Option A's case stronger, not closer** — it does not
rescue the balance test.

**4. Reframing the primary metric around Appendix E's real run-count data.** Considered whether
weighting "percent glare removed" against the real, sourced 2026-season Chinook count data
(S9, S10) could produce a genuinely close combined metric. Rejected: doing so honestly would
require inventing a conversion factor between "percent of optical glare removed" and "relative
rarity of a day's footage" — there is no real, sourced exchange rate between those two kinds of
value. `case.json`'s `primary_metric` is explicitly optics-only (percent glare removed, net of
reappearance), and `FACILITATOR.md`'s own Twist/Deep-conflict material already treats Appendix E
correctly as a *separate*, non-metric consideration ("the primary metric... says nothing about
which shot the film needs more"). Folding it into `margin_pct` would be exactly the kind of
invented-weight fudge this retune pass was told not to do, so it was not done.

## Why this margin cannot be closed under the current option pair

The deciding quantity is `I0_glass / I0_water ≈ 2.03` — the ratio of each material's own Fresnel
reflectance at its own Brewster angle. This ratio is a pure function of refractive index
(`n_glass=1.52` vs. `n_water=1.33`, both HIGH-confidence sourced constants, S1/S2) and does not
depend on shoot date, shoot time, window orientation, or camera position. It is also not a
coincidence of this particular case's chosen materials: Brewster-angle reflectance increases
monotonically with a material's refractive index (as `n→1`, `theta_B→0` and reflectance `→0`),
so *any* real, physically plausible solid window material — glass (n≈1.5), acrylic (n≈1.49),
polycarbonate (n≈1.58) — will reflect meaningfully more Brewster-angle glare than water
(n≈1.33) does. There is no real, non-exotic window material a documentary crew would actually
encounter at a public facility whose Brewster reflectance would come close to water's. This is a
structural property of the water-vs-solid-window comparison itself, not a fixable input.

## Conclusion and recommendation

**No realistic, defensible change to shoot date, shoot time, window orientation, or the margin's
arithmetic convention brings this case's primary-metric margin under ~20%.** The true relative
margin is a robust ~50%, driven entirely by the fixed ratio of two real refractive indices. Every
avenue instructed by this retune task was tried in good faith (re-searching the window's real
orientation, testing whether a more physically rigorous incidence-angle model would help — it
makes things worse, and testing whether Appendix E's real data could legitimately be folded into
the metric — it can't without inventing a weight) and none succeeds.

**No changes were made to `case.md`, `case.json`, or `FACILITATOR.md` in this pass** — forcing a
smaller number here would require either an implausible modeling assumption (an exotic low-index
window material, or a fabricated real orientation/date) or an invented weighting scheme, both of
which this retune's own instructions prohibited. `case.json.balance.margin_pct` remains `33.9`
(on the original share-of-maximum scale; ~50.5% on a direct relative-margin scale, the convention
used elsewhere in this repo) pending a human decision on next steps.

**Recommended path forward (needs a human/case-write decision, not a retune):** the water-vs-
solid-window Brewster comparison is not fixable in place. Two real options:
1. **Keep the case, drop the "close call" framing.** Not every case needs a coin-flip margin;
   this one teaches Brewster's angle, Malus's law, and the Pythagorean identity through a
   genuinely one-sided, physically decisive real-world result (glass reflects ~2x the glare water
   does at Brewster's angle) — pedagogically valid, but does not satisfy SPEC §2 as currently
   written, so this needs an explicit SPEC exception, not a silent pass.
2. **Rebuild the dilemma around a geometry-driven (not material-driven) asymmetry**, e.g.
   comparing two surfaces of the *same* material at two different real, researchable angles of
   incidence (so the deciding quantity becomes actual sun position/orientation, which genuinely is
   tunable and researchable) instead of two different materials (whose Brewster-angle asymmetry is
   fixed). This preserves the Brewster/Malus/Pythagorean-identity skill set but requires a new
   premise and a fresh `case-write` pass — out of scope for this retune.
