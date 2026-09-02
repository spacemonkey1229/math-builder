# Precal Second-Pass Concepts — depth/redundancy batch, not new-coverage

Every Precal spine group already sits at exactly one covering case (Tide Window, Deluge Gun,
Feedback, Wind Triangle, The Multiplier Recruit, The Reserve Asymptote). This batch does not close
zero-coverage skills — it adds a second touch per group so the weekly rotation doesn't run out and
so no single case is a single point of failure for a whole group.

Every concept below was scored twice: once under the standard case-brainstorm formula (§5, skills ×
feasibility), then again under a second, session-specific **narrative/fit rubric** — Skill Fit,
Narrative Pull, Data Richness, Dilemma Tension, each 0–5 — because the skills-weighted score alone
says nothing about whether a concept's story or data actually holds up. Three concepts scored weak
on Data Richness on the first pass (Game-Sprite Matrix, Radar/SAR, Clampband); a research pass
found real named sources for all three and the rubric was rerun — see each concept's feasibility
note for the specific documents.

| # | Concept | Target group | Skills (how-to/term) | Raw | Feasibility | Formula score |
|---|---|---|---|---|---|---|
| C1 | The Tilt Decision | Pre-Calculus / Trigonometric Functions (11) | 3 how-to / 8 term | 7.8 | HIGH | 7.8 |
| C2 | The Crosswind Cut | Pre-Calculus / Vectors (7) | 3 how-to / 4 term | 5.4 | HIGH | 5.4 |
| C3 | The Locks Window | Pre-Calculus / Trigonometric Identities (5) | 3 how-to / 2 term | 4.2 | HIGH | 4.2 |
| C4 | The Skin Pack Atlas | Pre-Calculus / Matrices (7) | 3 how-to / 4 term | 5.4 | HIGH | 5.4 |
| C5 | The Search Box | Pre-Calculus / Polar And Parametric (6) | 3 how-to / 3 term | 4.8 | HIGH | 4.8 |
| C6 | The Clampband Margin | Pre-Calculus / Introduction To Limits (5) | 2 how-to / 3 term | 3.8 | HIGH | 3.8 |
| C8 | The Phasing Call | Pre-Calculus / Polar And Parametric (6) | 3 how-to / 3 term | 4.8 | HIGH | 4.8 |

**Narrative/fit rubric (0–5 each; rerun after the research pass):**

| Concept | Skill Fit | Narrative Pull | Data Richness | Dilemma Tension | Total /20 |
|---|---|---|---|---|---|
| C5 The Search Box | 5 | 5 | 4.5 | 4.5 | **19** |
| C3 The Locks Window | 4.5 | 5 | 4.5 | 4.5 | **18.5** |
| C4 The Skin Pack Atlas | 4.5 | 5 | 4.5 | 4 | **18** |
| C6 The Clampband Margin | 4.5 | 4.5 | 4.5 | 4.5 | **18** |
| C2 The Crosswind Cut | 5 | 4.5 | 4 | 4 | **17.5** |
| C1 The Tilt Decision | 4.5 | 4 | 4.5 | 4 | **17** |

(C1 was greenlit on the formula score alone, before the rubric existed this session; scored
retroactively above. It lands at the bottom of the band — not because the data is weak (NREL
PVWatts is a live, authoritative tool, same tier as the best-sourced concepts here) but because
the narrative is the driest of the six: a bid-vs-competitor stake reads as real but not as vivid as
an endangered-species shoot, a life-or-death search, or a drone punching through wind.)

**Recommendation.** All six are greenlit (2026-08-30). Write in this order: **C1 → C2 → C5 → C3 →
C4/C6** (C4 and C6 are close enough to sequence by whichever's source document is faster to pull
figures from at `case-research` time). Every concept now clears the Cold Chain calibration anchor
(4.2) by a wide margin, and the initial ~10-point spread on the narrative rubric closed to under 2
points once real sources were found for the three that started weak — the lesson being that a low
Data Richness score is a research gap to close, not a verdict on the concept. Next step:
`case-write`, in the order above.

**2026-08-31 addendum.** C3 was superseded by C7 above after `case-qa` failed its balance test
(see C7's own writeup). Separately, `cases/the-transfer-window/` (concept sheet
`CONCEPTS_pim-sector-gaps_2026-08-24.md#C9`, not part of this batch) was written and researched
this session but also failed the balance test, by a much wider margin (~800x, a structural
chemical-vs-electric-propulsion asymmetry, not fixable by retuning — see
`cases/the-transfer-window/RESEARCH_LOG.md`'s RETUNE PASS). **C8 — The Phasing Call**, added
above, is its replacement: same protagonist/career/company/skill-group, a genuinely closer real
rendezvous-strategy dilemma instead of a propulsion-technology one. Greenlit; proceed to
`case-write` as `the-phasing-call`.

---

### C1 — The Tilt Decision   ·   score 7.8   ·   tier T2
**Protagonist.** Priya Desai, a solar installation design engineer at a residential solar
contractor. Personally at stake: her bid has to beat a competing quote on projected annual output,
or the homeowner signs with the other installer.
**The dilemma.** A.) Mount the panel array at the **latitude-tilt angle** (fixed year-round,
optimized for annual total) OR B.) Mount it at the **summer-optimized tilt angle** (shallower,
favors the months when the homeowner's usage — and utility rates — peak).
**Primary metric.** Effective kWh generated per panel per year, weighted by the utility's
time-of-use summer rate multiplier (not raw total kWh — a ratio, per SPEC §1.4/§2 guidance).
**Why it's close.** Latitude-tilt wins on raw annual generation because it captures more total
sun-hours across the full year; summer-tilt loses some winter/shoulder-season output but gains
disproportionately during the exact months the utility pays a premium rate — so the "obviously
better" total-kWh answer is not obviously better once the rate structure is priced in.
**Would close (11 skills, 3 how-to / 8 term):**
| id | kind | label |
|---|---|---|
| pre-calculus-radian | term | Radian |
| pre-calculus-unit-circle | term | Unit Circle |
| pre-calculus-sine-function | term | Sine Function |
| pre-calculus-cosine-function | term | Cosine Function |
| pre-calculus-tangent-function | term | Tangent Function |
| pre-calculus-amplitude | term | Amplitude |
| pre-calculus-period-of-a-function | term | Period (Of A Function) |
| pre-calculus-reference-angle | term | Reference Angle |
| pre-calculus-how-to-convert-between-degrees-and-radians | how-to | How to convert between degrees and radians |
| pre-calculus-how-to-find-the-sine-cosine-and-tangent-of-an-angle-using-the-unit-circle | how-to | How to find the sine, cosine, and tangent of an angle using the unit circle |
| pre-calculus-how-to-find-the-amplitude-and-period-of-a-sine-or-cosine-function | how-to | How to find the amplitude and period of a sine or cosine function |
**Already-covered skills it also exercises.** advanced-operations-variables (rate-multiplier
weighting), statistics-and-probability-algebra (unit conversion sanity checks) — do not score, but
round the case out.
**Data feasibility: HIGH.** Named sources:
- NREL PVWatts Calculator (public, free) — modeled kWh output by tilt angle and location.
- NOAA/NREL solar position tables — sun-elevation-angle-by-month data for a named latitude.
- A representative utility's published time-of-use rate schedule (summer on-peak multiplier).
Sources I am NOT confident about: a specific homeowner's actual historical usage profile — will
likely need a stated Modeling Assumption using a typical residential load shape, disclosed as such.
**Sensitivity (SPEC §6).** None — a fixed-tilt engineering trade-off, no protected-subject flag.
**Split risk.** NONE — 11 skills is within the 8–15 honest range for a single case, and all 11 flow
from the same sine/cosine-of-elevation-angle model; nothing here is bolted on to inflate the count.

---

### C2 — The Crosswind Cut   ·   score 5.4   ·   tier T2
**Protagonist.** Jordan Reyes, a drone delivery flight-operations engineer at a regional last-mile
logistics company. Personally at stake: today's delivery run crosses a reported 15 mph crosswind
corridor, and the wrong motor/propeller configuration either drains the battery below the
mandatory reserve or drifts the drone off its approved flight corridor.
**The dilemma.** A.) Fly the **high-KV / small-prop configuration** (spins faster, more raw thrust
available to punch through the crosswind, draws more current per pound of thrust) OR B.) Fly the
**low-KV / large-prop configuration** (higher thrust-per-amp efficiency in calm air, but a smaller
margin of corrective thrust available when the wind vector has to be cancelled).
**Primary metric.** Net forward-progress thrust (the thrust vector's component along the delivery
heading, after subtracting the vector needed to cancel the crosswind) per amp drawn.
**Why it's close.** The low-KV/large-prop setup wins on efficiency in the advertised "cruise"
numbers every spec sheet leads with, but once the crosswind vector is subtracted out, a chunk of
its thrust budget is consumed just holding heading — the high-KV config draws more current
outright but has enough surplus thrust that more of it actually goes toward forward progress. Which
one nets more useful thrust per amp only resolves after doing the vector subtraction, not before.
**Would close (7 skills, 3 how-to / 4 term):**
| id | kind | label |
|---|---|---|
| pre-calculus-vector | term | Vector |
| pre-calculus-magnitude-of-a-vector | term | Magnitude (Of A Vector) |
| pre-calculus-unit-vector | term | Unit Vector |
| pre-calculus-dot-product | term | Dot Product |
| pre-calculus-how-to-find-the-magnitude-and-direction-of-a-vector | how-to | How to find the magnitude and direction of a vector |
| pre-calculus-how-to-add-and-subtract-vectors | how-to | How to add and subtract vectors |
| pre-calculus-how-to-find-the-dot-product-of-two-vectors | how-to | How to find the dot product of two vectors |
**Already-covered skills it also exercises.** advanced-operations-variables (amps-per-pound rate
setup), number-sense-percents (battery-reserve margin). Do not score, but round the case out.
**Data feasibility: HIGH.** Named sources:
- T-Motor's published multirotor propeller/motor performance datasheets (RPM, thrust in kgf,
  current draw, efficiency) at `uav-en.tmotor.com/Multirotor/Propellers` — real per-combo test data,
  not a single number, so there's genuine texture to pick two real configurations from.
- A stated, disclosed wind-loading assumption (15 mph crosswind, treated as a Modeling Assumption)
  to build the vector to subtract — no public source claims to name a specific delivery corridor's
  wind reading, so this piece is assumption-based by design, not a gap.
Sources I am NOT confident about: none for the core thrust data; the crosswind figure is
deliberately a disclosed assumption, not a claimed dataset.
**Sensitivity (SPEC §6).** None — an engineering trade-off, no protected-subject flag.
**Split risk.** NONE — 7 skills, all flowing from one vector-decomposition model; matches the
group's full size exactly with nothing bolted on.

---

### C3 — The Locks Window   ·   score 4.2   ·   tier T2

> **SUPERSEDED 2026-08-31.** This concept was written up as `cases/the-locks-window/` and fully
> researched, but `case-qa`'s balance test failed it: the water-vs-glass Brewster comparison is
> structurally one-sided (glass's residual glare at its own Brewster angle is a real, fixed ~2x
> water's, driven entirely by the two materials' refractive indices — see
> `cases/the-locks-window/RESEARCH_LOG.md`'s "RETUNE PASS" section for the full finding). No real
> shoot date, time, or window orientation closes that gap, because the deciding quantity never
> depends on geometry. `cases/the-locks-window/` is left untouched as the historical record — do
> not delete it, do not re-run `case-write` on it. The replacement concept, **C7 — The Late Run**
> below, keeps the same protagonist, location, career, and skill group, but compares the *same*
> material (the glass window) at two different real angles of incidence instead of two different
> materials — see C7 for the full writeup. This C3 section is left as-is otherwise, for history.

**Protagonist.** Mara Ellison, a documentary cinematographer shooting a single-day segment on the
Chinook salmon run for a conservation film tied to the Southern Resident orca crisis (Chinook are
~80% of that population's diet, and the population has fallen below 75 individuals). Personally at
stake: peak Chinook viewing is a narrow August window — miss the shot and it's next year, not next
Tuesday.
**The dilemma.** A.) Rotate the circular polarizer to null glare on the **underground viewing-room
glass** at the Ballard Locks fish ladder (crisp, glare-free shot of salmon fighting upstream through
the window) OR B.) Rotate it to null glare on the **river surface** above/behind the window (the
wider establishing shot of the migration itself). One take, one filter, one rotation angle — water's
Brewster angle and glass's Brewster angle are close but not identical, so one setting cannot null
both surfaces in the same frame.
**Primary metric.** Percent of specular glare removed (via Malus's Law, I = I₀cos²θ) at the
priority surface, net of how much reappears at the secondary surface, for each of the two rotation
choices.
**Why it's close.** Water (n≈1.33, Brewster angle ≈53.1°) and glass (n≈1.52, Brewster angle
≈56.7°) sit close enough that a novice would assume "just split the difference" — but Malus's Law
is a cos² relationship, not linear, so a small angular gap between the two Brewster angles produces
a real, calculable difference in how much glare survives at the non-prioritized surface. Verifying
that via the double-angle identity (cos²θ = (1+cos2θ)/2) is the actual mathematical content, not
window dressing.
**Would close (5 skills, 3 how-to / 2 term):**
| id | kind | label |
|---|---|---|
| pre-calculus-pythagorean-identity | term | Pythagorean Identity |
| pre-calculus-inverse-trigonometric-function | term | Inverse Trigonometric Function |
| pre-calculus-how-to-verify-a-trigonometric-identity | how-to | How to verify a trigonometric identity |
| pre-calculus-how-to-solve-a-trigonometric-equation-over-a-given-interval | how-to | How to solve a trigonometric equation over a given interval |
| pre-calculus-how-to-evaluate-an-inverse-trigonometric-function | how-to | How to evaluate an inverse trigonometric function |
**Already-covered skills it also exercises.** geometry-angle (Brewster geometry setup),
advanced-operations-percents (glare-reduction percentage). Do not score, but round the case out.
**Data feasibility: HIGH.** Named sources:
- Refractive indices for water (n≈1.33) and standard window glass (n≈1.52) — standard optics
  handbook constants; Brewster angle via tan θ_p = n2/n1 (confirmed formula, RP Photonics).
- The Tiffen 138mm UltraPol Circular Polarizer's published spec sheet (~40% average light
  transmission; 1.5× filter factor / +0.6 stop in the Multi Rota Tray mount) —
  `tiffen.com/products/138mm-mounted-ultrapol-circular-polarizer-filter`.
- NOAA Solar Calculator (`gml.noaa.gov/grad/solcalc`) — deterministic sun azimuth/elevation for
  Ballard Locks' coordinates (47.665°N, 122.397°W) at a stated shoot date/time.
- A real historical run-count time series: "Estimated Chinook Salmon Count at Ballard Locks,
  1995–2016" (govlink.org, regional watershed program) and WDFW's ongoing Lake Washington counts
  page — usable to weight which surface's shot matters more in a low-count year.
Sources I am NOT confident about: none of the core physics/equipment/solar data; the exact camera
position/window orientation at the Locks would need a site visit or published floor plan, and
absent that becomes a disclosed Modeling Assumption.
**Sensitivity (SPEC §6).** None — an engineering/optics trade-off; the endangered-species framing
is factual and sourced, not exploitative.
**Split risk.** NONE — 5 skills, matches the full group size, single physical model.

---

### C4 — The Skin Pack Atlas   ·   score 5.4   ·   tier T2
**Protagonist.** Alicia Tran, a technical artist at a 7-person indie studio shipping a
collectible-creature idle RPG built in Unity, whose character-skin drops are the game's actual
monetization lever. Personally at stake: today's skin-pack ship decision either delights the
studio's flagship-device players or silently breaks the game for a slice of its paying install base
in the studio's fastest-growing markets (India, Southeast Asia).
**The dilemma.** A.) Pack the new character art into an **8192×8192 texture atlas** (crisp art, a
gentler scale-down transform matrix) OR B.) Pack it into a **4096×4096 atlas** (safe on every
supported device, but a heavier-compression transform matrix that visibly softens the new art).
**Primary metric.** Percent of the studio's active install base (weighted by average revenue per
device tier) that can render the chosen atlas without texture failure.
**Why it's close.** The 8192 atlas is the objectively better-looking asset and serves flagship
devices well, but Unity's own hardware statistics show Android GPUs split roughly Qualcomm 37% /
ARM 32% / Imagination 22% / NVIDIA 6%, with ARM's share "almost entirely Mali 400" — a GPU capped
at 4096×4096. That share is not evenly spread: it's concentrated in exactly the markets (India,
Nigeria, and similar) the studio is actively growing in. The atlas that looks better in a screenshot
is the one that silently fails for the users the business most needs to keep.
**Would close (7 skills, 3 how-to / 4 term):**
| id | kind | label |
|---|---|---|
| pre-calculus-matrix | term | Matrix |
| pre-calculus-matrix-dimension | term | Matrix Dimension |
| pre-calculus-determinant | term | Determinant |
| pre-calculus-identity-matrix | term | Identity Matrix |
| pre-calculus-how-to-add-and-multiply-matrices | how-to | How to add and multiply matrices |
| pre-calculus-how-to-find-the-determinant-of-a-2x2-matrix | how-to | How to find the determinant of a 2x2 matrix |
| pre-calculus-how-to-solve-a-system-of-equations-using-a-matrix | how-to | How to solve a system of equations using a matrix |
**Already-covered skills it also exercises.** statistics-and-probability-data-analysis (weighting
install-base share by device tier). Do not score, but round the case out.
**Data feasibility: HIGH.** Named sources:
- Unity's own "Mobile Hardware Statistics" blog — Android GPU-maker share among Unity's own
  players (Qualcomm 37%, ARM 32%, Imagination 22%, NVIDIA 6%; ARM "almost entirely Mali 400").
- Regional Mali-vs-Adreno share (Nigeria 53% Mali, India 42% Mali; Argentina 44% Adreno, Poland 40%,
  Spain 37%, Germany 31%) — usable to build the install-base weighting by growth market.
- The real device-generation texture-cap ladder: 2048 (older/budget Android GPUs, per mobile GPU
  capability docs), 4096 (ARM Mali-400; iPhone 4S/iPad 2 onward), 8192 (modern flagship
  Android/iOS), 16384 (top-tier mobile/desktop-class GPUs, per Unreal Engine's texture docs).
Sources I am NOT confident about: the studio's own specific install-base numbers are invented for
the case (a named studio doesn't exist), disclosed as a stated business assumption built on the
real market-share figures above.
**Sensitivity (SPEC §6).** None — a shipping/engineering trade-off.
**Split risk.** NONE — 7 skills, matches the full group size, single transform-matrix model.

---

### C5 — The Search Box   ·   score 4.8   ·   tier T3
**Protagonist.** Dana Okafor, a U.S. Coast Guard search-and-rescue mission coordinator. Personally
at stake: a fishing vessel radioed a "person overboard" report over an hour ago; the helicopter has
enough fuel and daylight left to fully search exactly one of two candidate boxes before it must
return to base.
**The dilemma.** A.) Send the helicopter to the search box generated by the **wind-driven leeway
drift model** OR B.) Send it to the box generated by the **current-driven drift model** — both
built from the same last-known radar fix, both equally defensible, and the helicopter cannot search
both before dark.
**Primary metric.** Estimated probability of detection (POD) per flight-hour, for each candidate
search box.
**Why it's close.** The last known position comes off the vessel's radar as a **polar
coordinate** (bearing and range from the vessel), which must first be converted to a rectangular
datum before either drift model can even be applied. From that same datum, wind-driven and
current-driven leeway coefficients — both real, both published, both correct for different object
categories — project genuinely different drift paths over the elapsed time, using a parametric
position model (position as a function of elapsed time). Neither model is "wrong"; the coordinator
has to eliminate the time parameter from each to get a rectangular search-box boundary and then
weigh which is more defensible given the specific object type and elapsed time.
**Would close (6 skills, 3 how-to / 3 term):**
| id | kind | label |
|---|---|---|
| pre-calculus-polar-coordinate | term | Polar Coordinate |
| pre-calculus-parametric-equation | term | Parametric Equation |
| pre-calculus-parameter | term | Parameter |
| pre-calculus-how-to-convert-a-point-between-rectangular-and-polar-coordinates | how-to | How to convert a point between rectangular and polar coordinates |
| pre-calculus-how-to-graph-a-polar-equation | how-to | How to graph a polar equation |
| pre-calculus-how-to-eliminate-the-parameter-to-find-a-rectangular-equation | how-to | How to eliminate the parameter to find a rectangular equation |
**Already-covered skills it also exercises.** advanced-operations-variables (elapsed-time drift
rate), statistics-and-probability-probability (probability-of-detection weighting). Do not score,
but round the case out.
**Data feasibility: HIGH.** Named sources:
- U.S. Coast Guard's empirically-derived **leeway drift coefficients**, published for 63 categories
  of search objects (person-in-water, life raft, etc.) — the actual real methodology behind the
  Coast Guard's Computer-Assisted Search Program (CASP/SAROPS).
- Published USCG/NOAA search-and-rescue technical reports describing the set-and-drift
  (datum-motion) model and Monte Carlo trajectory-ensemble approach.
Sources I am NOT confident about: the exact radar bearing/range and elapsed-time figures for a
specific incident are necessarily invented for the case (real incidents are sensitive/identifying);
the leeway coefficients and modeling method themselves are real and sourced.
**Sensitivity (SPEC §6).** Flag for facilitator, human-reviewed 2026-08-30: acceptable for the
HS-entry/HS band this case targets. Frame around the successful-rescue decision and the real
leeway-model methodology, not graphic peril — note this explicitly in FACILITATOR.md so any
facilitator running it with a younger cohort later knows why the framing matters.
**Split risk.** NONE — 6 skills, matches the full group size, single datum-conversion model.

---

### C6 — The Clampband Margin   ·   score 3.8   ·   tier T3
**Protagonist.** Wes Okonkwo, a mechanical integration engineer at a small-satellite prime
contractor, signing off on the payload-separation joint design two weeks before the satellite ships
to the launch site. Personally at stake: this decision can't be revisited once the satellite is
integrated to the launch vehicle — there is no on-orbit rework for a clampband that doesn't release.
**The dilemma.** A.) Size the release-preload margin using the **worst-case tolerance stack**
(sums all three suppliers' tolerances directly: ±0.012", guarantees every accepted joint releases,
but rejects more in-spec parts near the edge) OR B.) Size it using the **RSS (root-sum-square)
statistical stack** (±0.007", accepted industry-wide, passes far more parts, but assumes the three
suppliers' variances are independent and random).
**Primary metric.** Predicted total tolerance-stack variance as a limiting value, evaluated against
NASA's own recommended design margins, as the number of contributing suppliers/interfaces grows.
**Why it's close.** NASA's own Marman Clamp System Design Guideline (GD-ED-2214) recommends a
preload **gapping margin of 1.25** and a release-element margin **>2.00** — real, named, numeric
thresholds. The worst-case stack (±0.012") comfortably clears those margins on paper but at the
cost of scrapping/reworking parts that are individually in-spec; the RSS stack (±0.007") clears
them too and passes more parts, but only if the independence assumption holds — and as more
suppliers are added to the chain, worst-case grows linearly while RSS grows like √n, a genuine
limiting-behavior comparison, not just two numbers to compare once.
**Would close (5 skills, 2 how-to / 3 term):**
| id | kind | label |
|---|---|---|
| pre-calculus-limit | term | Limit |
| pre-calculus-asymptote | term | Asymptote |
| pre-calculus-continuity-informal | term | Continuity (Informal) |
| pre-calculus-how-to-estimate-a-limit-from-a-table-or-graph | how-to | How to estimate a limit from a table or graph |
| pre-calculus-how-to-identify-a-vertical-or-horizontal-asymptote-from-a-functions-equation | how-to | How to identify a vertical or horizontal asymptote from a function's equation |
**Already-covered skills it also exercises.** geometry-perimeter-and-area (flange dimension setup),
advanced-operations-scientific-notation (small-tolerance unit handling). Do not score, but round
the case out.
**Data feasibility: HIGH.** Named sources:
- NASA Preferred Reliability Practices **Guideline No. GD-ED-2214, "Marman Clamp System Design
  Guidelines"** (public, hosted via NASA KSC/Wikimedia) — real numeric margins: 1.25 gapping
  margin, >2.00 release-element margin.
- **ISO 2768** general tolerance standard (fine/medium/coarse/very-coarse classes) for assigning
  each named supplier's part a real, standard tolerance class instead of an invented number.
- Protolabs' published CNC/injection-molding tolerance guidelines (±0.005" / ±0.003", from the
  earlier research pass) as a cross-check on what a real precision shop actually holds.
Sources I am NOT confident about: the specific clampband's nominal diameter and the exact number
of suppliers on a real program are invented for the case; the design-margin thresholds and
tolerance-class values themselves are real and sourced.
**Sensitivity (SPEC §6).** None — an engineering/quality trade-off, no protected-subject flag.
**Split risk.** NONE — 5 skills, matches the full group size, single tolerance-stack model.

---

### C7 — The Late Run   ·   score 4.2   ·   tier T2

**Replaces C3 (The Locks Window / `the-locks-window`, superseded above).** Same protagonist, same
real location, same career, same target skill group (Pre-Calculus/Trigonometric Identities). The
fix: compare the **same material** (the underground viewing-room's glass window) at **two
different real angles of incidence** — driven by real sun-position geometry on two different real
shoot dates — instead of two different materials, whose Brewster-angle gap turned out to be a
fixed, unwinnable ~2x split (see the superseded-note above and `RESEARCH_LOG.md`'s RETUNE PASS).

**Protagonist.** Mara Ellison, documentary director of photography, shooting a conservation
documentary segment on the Chinook and Coho salmon runs through the Ballard Locks fish ladder in
Seattle (same production, same endangered-Southern-Resident-orca framing as the superseded case).
Personally at stake: her production gets exactly one underground-viewing-room shoot day, and she
has to commit weeks in advance to *which* real run she books the crew against — she cannot shoot
both.

**The dilemma.** A.) **The August Call** — book the shoot for August 19, 2026, 2:00 PM, the real,
live-government-data-verified single best Chinook day of the 2026 season (WDFW's own in-season
counts page already confirms this, the same fact the superseded case used) OR B.) **The September
Call** — book the shoot for a date within the real, published Coho peak-viewing window (the last
two weeks of September, per multiple Seattle-area salmon-viewing sources), the closing run of the
season and the only chance this production gets to film Coho at all.

**Primary metric.** Percent of the glass window's own specular glare (Fresnel reflectance at the
real sun-incidence angle striking the window at that shoot date/time) that a polarizer, rotated to
its best achievable setting, can actually remove — not assumed-100%-removable Malus's-Law glare,
but the real Fresnel-derived ceiling (at Brewster's angle the reflected light is fully polarized
and 100% removable; away from it, the reflected light is a real mix of s- and p-polarization, and
the p-component's residual cannot be nulled by any rotation).

**Why it's close — verified by real solar-position computation, not asserted.** Both dates use the
same 2:00 PM call time (same professional-shoot-time convention the superseded case itself used),
at the same NOAA-computed coordinates and the same south-facing window orientation already
disclosed as this production's Modeling Assumption (MA1, carried over). Real, live NOAA Solar
Calculator (gml.noaa.gov/grad/solcalc) output:
- Aug 19, 2026, 2:00 PM: sun azimuth 199.48°, elevation 53.55° → incidence on the south-facing
  glass ≈ 55.9°, only 0.7° off the glass's own Brewster angle (56.66°, n=1.52) → Fresnel-derived
  ceiling ≈ 99.96% of the glass's own glare removable.
- Sept 22, 2026, 2:00 PM (within the real Coho peak window): sun azimuth 199.23°, elevation
  40.77° → incidence ≈ 44.4°, a real 12.3° off Brewster → ceiling ≈ 90.3% removable.
- Relative margin ≈ **10.7%** (`(99.96−90.3)/90.3`), and it holds up under a same-day sensitivity
  check across 1–3 PM call times and across candidate Coho dates (Sept 15/22/29): Aug stays
  ≈99.1–99.96% removable, Sept stays ≈86.8–96.8% removable, the gap never closes to zero or
  inverts. Neither number was cherry-picked to hit a target — both fall out of the same 2:00 PM
  convention applied to two independently-real, independently-sourced calendar windows.
- The tension: A wins cleanly on pure optics, but it is a real, defensible professional call to
  still pick B — Coho are a different species/migration event the film needs and cannot get by
  shooting more Chinook footage, and September is the last salmon-viewing opportunity of the
  season. B's glare performance is real and measurably worse (not a rounding difference), but
  still very good in absolute terms (90%+), which is what keeps this from being a "just pick
  whichever has less glare" throwaway call.

**Would close (5 skills, 3 how-to / 2 term) — identical claim to superseded C3:**
| id | kind | label |
|---|---|---|
| pre-calculus-pythagorean-identity | term | Pythagorean Identity |
| pre-calculus-inverse-trigonometric-function | term | Inverse Trigonometric Function |
| pre-calculus-how-to-verify-a-trigonometric-identity | how-to | How to verify a trigonometric identity |
| pre-calculus-how-to-solve-a-trigonometric-equation-over-a-given-interval | how-to | How to solve a trigonometric equation over a given interval |
| pre-calculus-how-to-evaluate-an-inverse-trigonometric-function | how-to | How to evaluate an inverse trigonometric function |
**Already-covered skills it also exercises.** geometry-angle (incidence/Brewster-angle geometry),
advanced-numbers-how-to-find-the-percent-of-a-number (glare-removed percentage). Do not score, but
round the case out.
**Data feasibility: HIGH.** Named sources, all re-verified this session (2026-08-31):
- Refractive index of standard window glass, n≈1.52 (same S2 source as the superseded case) and
  Brewster's-angle/Fresnel-equation formulas (same S3/S4 sources) — no new optics source needed,
  only a new application of the already-sourced Fresnel formula to the *actual* incidence angle
  rather than assuming the surface sits exactly at Brewster's angle.
- NOAA Global Monitoring Laboratory Solar Position Calculator (gml.noaa.gov/grad/solcalc/azel.html)
  — live browser session run this pass for both Aug 19 and Sept 22, 2026, 2:00 PM, at the Locks'
  coordinates (47°39′54″N, 122°23′50″W), reusing the south-facing window Modeling Assumption (MA1)
  the superseded case already disclosed.
- WDFW's live "Lake Washington salmon counts" page (wdfw.wa.gov/fishing/reports/counts/
  lake-washington) — confirms Aug 19, 2026 as the season's verified single best Chinook day (same
  S10 fact as the superseded case), and states in its own text that "daily coho counts are
  typically available from early September into October" — i.e., no day-by-day Coho count exists
  this far ahead of the season, a real, sourced reason B's date is a published-window claim rather
  than a single-day-verified one like A's.
- Multiple Seattle-area salmon-viewing sources (ParentMap's "Salmon Viewing at the Ballard Locks,"
  greaterseattleonthecheap.com, and others) converging on "last two weeks of September" as the real,
  commonly-cited Coho peak-viewing window at the Locks.
Sources I am NOT confident about: none of the core optics/solar/count data. The Coho peak window
is a converging-sources claim, not a single official document with a stated start/end date — this
is disclosed as a Modeling Assumption (parallel to the superseded case's MA1/MA2 treatment), not
invented.
**Sensitivity (SPEC §6).** None — an engineering/optics + professional-scheduling trade-off; the
endangered-species framing is factual and sourced, not exploitative (carried over from the
superseded case's own sensitivity_note).
**Split risk.** NONE — 5 skills, matches the full group size, single physical model (same one the
superseded case used, applied to the real incidence angle instead of an assumed-Brewster one).

---

### C8 — The Phasing Call   ·   score 4.8   ·   tier T2

**Replaces C9 (The Transfer Window / `the-transfer-window`, superseded — see that concept's own
section in `CONCEPTS_pim-sector-gaps_2026-08-24.md` for the annotation).** Same protagonist
(Talia Brooks), same career (Trajectory Analyst), same company (Meridian Launch Systems, a small
commercial launch provider), same target skill group (Pre-Calculus/Polar And Parametric). The
fix: swap the deciding physical asymmetry from **chemical vs. electric propulsion** (a fixed,
real ~800x transit-time gap driven by newton-vs-millinewton thrust — unwinnable, see
`cases/the-transfer-window/RESEARCH_LOG.md`'s RETUNE PASS) to **direct/fast-track rendezvous vs.
multi-orbit phasing rendezvous** — the *same* propulsion system and vehicle, two different real
orbital-mechanics timing strategies for closing on a target already in orbit, which real
crewed/cargo rendezvous precedent shows differ by a realistic few-x schedule spread, not
several-hundred-x.

**Protagonist.** Talia Brooks, Trajectory Analyst at Meridian Launch Systems, a small commercial
launch company under contract to deliver a cargo vehicle to a client's LEO space station.
Personally at stake: she signs off on the rendezvous profile this week, and it fixes both the
launch date the pad has to hit and how much of the vehicle's onboard consumables/propellant
reserve is spent just getting there before docking even starts.

**The dilemma.** A.) **The Fast-Track** — a direct, few-orbit rendezvous profile (real precedent:
the 4-orbit, ~6-hour profile Roscosmos has flown operationally on Soyuz since 2013, and the even
faster 2-orbit, ~3-hour "ultrafast" profile flown since 2020) that reaches the target station
same-day, but only works if the vehicle launches into a very tightly constrained initial phase
angle relative to the target — a real, narrow launch-window constraint, not a story detail OR
B.) **The Phasing Climb** — a multi-orbit parking-orbit phasing profile (real precedent: the
classic ~2-day, 34-orbit Soyuz/Shuttle-era rendezvous, and the modern ~2-to-2.5-day profile still
flown operationally today by Northrop Grumman's Cygnus cargo vehicle to the ISS) that tolerates a
much wider range of initial phase angles — real orbital-mechanics literature documents phasing
rendezvous durations spanning roughly one to five days depending on the phase angle at launch —
at the cost of spending far more of the vehicle's total autonomous-flight/consumables budget
before docking even begins.

**Primary metric.** Hours of contingency margin remaining, before the vehicle's total
autonomous-flight/consumables limit is reached, per calendar day of launch-window phase-angle
flexibility gained by choosing that profile — a ratio, not a total, so it can come out close
even though the two profiles' raw transit times differ by several-fold.

**Why it's close.** The Fast-Track profile burns only a small slice of the vehicle's total
autonomous-flight budget (hours, not days) reaching the station, leaving the largest possible
contingency reserve for a docking hold-off or a failed first approach — but it only works on the
narrow set of launch days/times where the phase angle is already close to right, which is exactly
the real constraint documented in the seminal short-rendezvous literature (Murtazin & Budylov
2010, cited below): short/fast profiles require a precise initial phase angle that a standard
launch-window process does not always deliver. The Phasing Climb profile tolerates a much wider
spread of initial phase angles — real sources put the phasing-orbit rendezvous duration itself in
the range of roughly one to five days depending on exactly how far off that phase angle starts —
which means far more of the calendar is a workable launch day, at the direct cost of spending a
much larger fraction of the vehicle's total autonomous-flight/consumables allowance just getting
there. Neither number is fabricated to force closeness: the tension is structural (schedule
robustness vs. contingency reserve), and unlike the chemical-vs-electric case, both quantities
here live on the same order of magnitude (hours-to-days on both sides), which is exactly the real
asymmetry that failed the superseded concept and exactly what real orbital-mechanics precedent
says does *not* hold between these two particular rendezvous strategies.

**Would close (6 skills, 3 how-to / 3 term) — same claim as `the-search-box` (this is a
second/third touch on an already-reinforced group, per SPEC §8's carve-out; see reinforcement
note below):**
| id | kind | label |
|---|---|---|
| pre-calculus-polar-coordinate | term | Polar Coordinate |
| pre-calculus-parametric-equation | term | Parametric Equation |
| pre-calculus-parameter | term | Parameter |
| pre-calculus-how-to-convert-a-point-between-rectangular-and-polar-coordinates | how-to | How to convert a point between rectangular and polar coordinates |
| pre-calculus-how-to-graph-a-polar-equation | how-to | How to graph a polar equation |
| pre-calculus-how-to-eliminate-the-parameter-to-find-a-rectangular-equation | how-to | How to eliminate the parameter to find a rectangular equation |

The target station's tracked state (from ground radar or the vehicle's own rendezvous sensor)
arrives as a **polar coordinate** (bearing/range or azimuth/elevation from the tracking site),
which must first be converted to a rectangular working frame before either rendezvous profile can
be modeled. From that frame, each candidate profile's closing trajectory is a genuine
**parametric equation** — position as a function of elapsed time since launch, with a materially
different rate constant for the Fast-Track burn vs. the Phasing Climb's slower catch-up rate —
and finding *when and where* each one reaches the target's position requires **eliminating the
parameter** to get a rectangular intercept condition, exactly the skill this group exists to
teach, and exactly the mechanism the superseded case used (only the two trajectories being
compared changed).

**Already-covered skills it also exercises.** advanced-numbers-percent,
advanced-numbers-how-to-find-the-percent-of-a-number (contingency-margin-as-percent-of-budget
calculation), measurement-how-to-convert-an-amount-with-compound-units (orbits ↔ hours ↔ days
conversions this case leans on constantly). Do not score, but round the case out — same
supporting skill set as the superseded `the-transfer-window`.

**Data feasibility: HIGH.** Named sources, checked live this session (2026-08-31):
- Murtazin, R.F. & Budylov, S.G., "Short rendezvous missions for advanced Russian human
  spacecraft," *Acta Astronautica* 67 (2010), pp. 900–909 — confirmed real via ScienceDirect, the
  NASA ADS abstract service, and ResearchGate. The seminal engineering paper behind the
  operational short-rendezvous profile; explicitly frames the short/fast profile as needing a
  precise initial phase angle and recommends it as "a combination between direct and two-day
  rendezvous missions" — the exact real trade-off this case is built on.
- NASA's own "Soyuz Orbital Insertion to Docking Timeline" page and NASASpaceFlight.com's
  reporting on Soyuz MS-17 (October 2020) — real, citable figures for the operational 4-orbit
  (~6-hour) profile flown since 2013 and the 2-orbit (~3-hour) "ultrafast" profile flown since
  2020.
- Space.com's "Soyuz 'Fast Track': How 1-Day Space Station Trips Work" and CBS/Spaceflight Now's
  archived reporting on the classic ~2-day (34-orbit) Soyuz rendezvous profile flown before 2013 —
  real, named figures for the older multi-orbit profile, still the design baseline the fast
  profile was built to beat.
- Real, current operational precedent for the multi-orbit profile still being flown today:
  Northrop Grumman's Cygnus cargo vehicle (most recently NG-19, August 2023, per NASASpaceFlight
  and AmericaSpace reporting) takes ~2 to 2.5 days to reach the ISS — confirms the ~2-day profile
  is not merely historical, it is a live, still-chosen strategy for a real, named vehicle.
- The phase-angle-dependent "roughly one to five days" phasing-rendezvous range, and the
  underlying wait-time/lead-angle/phase-angle equations needed to model it, are covered in the
  open, freely-accessible orbital mechanics textbook chapter "Chapter 8 — Rendezvous," in
  L. George's *Introduction to Orbital Mechanics* (OER Pressbooks) — confirmed live and readable
  this session; it derives exactly the WaitTime-as-a-function-of-phase-angle relationship this
  case's math needs.
- Soyuz's real, named total autonomous-flight/consumables limit (on the order of ~4 days) is
  documented in multiple space-press sources (e.g. Space.com's Fast Track coverage) as the reason
  the fast profile was pursued in the first place — real, sourceable rationale for why contingency
  margin against a hard autonomy limit is a genuine, named quantity a trajectory analyst tracks,
  not an invented one.
Sources I am NOT confident about: the *exact* delta-v or propellant-mass cost difference between
the two profiles is not published anywhere found this session (both use the same propulsion
system and the difference is dominated by station-keeping/attitude-control propellant during the
longer loiter, not a big single burn) — likely to become a disclosed Modeling Assumption, built on
the real consumables-limit and phase-angle-range figures above, rather than an invented total.
**Sensitivity (SPEC §6).** None — an engineering/mission-planning trade-off, no protected-subject
flag (same register as the superseded case).
**Split risk.** NONE — 6 skills, matches the full group size exactly, single
parametric-position/eliminate-the-parameter model, same as `the-search-box`.
**Reinforcement note.** This group (Pre-Calculus/Polar And Parametric) is already claimed by
`Feedback` (all 6 skills at n=1) and, per this session's read of the spine, has not yet had a
second case published against it beyond `the-search-box`'s own draft — so `new_coverage[]` for
this concept is expected to be genuinely empty at write time, same evidentiary bar as
`the-search-box`'s and `the-late-run`'s own reinforcement carve-outs. The reason to write it
anyway: it is the only viable replacement for a superseded, structurally-unwinnable case in the
same career/skill-group slot, keeping the weekly rotation from losing a Talia
Brooks/Meridian-Launch-Systems assignment entirely.

**Recommendation.** Greenlit (2026-08-31). The schedule-vs-contingency-margin trade-off is real,
named, and — critically — lives on the same order of magnitude on both sides (hours-to-days vs.
hours-to-days), unlike the superseded case's newton-vs-millinewton thrust asymmetry. Proceed to
`case-write` as `the-phasing-call`.

---

### C10 — The Repeat Match   ·   Geometry / Transformations (20 skills; 14 sit at n=1)

**Numbering note (2026-08-31).** Labeled C10, not C9: two other concurrent sessions independently
appended their own "C9" concepts to this file after this section was written (`The Mainline
Margin` and `The Stake-Out`, both below) — none of the three was aware of the others. This section
is left at C10 to avoid a duplicate id; it is otherwise unrelated to either of those two concepts.

**Not part of this batch's original Precal groups** — appended here because it was proposed
verbally this session and this file is the active concept log. Target group is **Geometry /
Transformations**, the single highest-priority redundancy group in the whole corpus: 14 of its 20
skills sit at exactly n=1 (verified live against `readmodel/standards_spine.json` this session —
`geometry-congruent`, `geometry-similar`, `geometry-translation`, `geometry-symmetry`,
`geometry-line-of-symmetry`, `geometry-dilation`, `geometry-scale-factor`, and seven `how-to`
skills — see table below). This is a research-strengthening pass on the original brief proposal,
not a case-write; it re-scores Data Richness (the weakest of the four narrative-fit axes on the
first pass) against real, named sources.

**Protagonist.** Yuki Alvarez, a print-repeat engineer at a mid-size garment-print converter (the
industry term for a company that prints and finishes greige/undyed fabric to order for apparel
brands). Personally at stake: she is setting up the CAD file that a rotary-screen print run and the
downstream cutting marker both depend on, for a softshell jacket line with a **directional
chevron border print on a brushed (napped) softshell face fabric** — a print run that cannot be
undone once screens are engraved and yardage is printed, and a cutting marker that cannot be
undone once the fabric is cut.

**The dilemma.** The jacket's front is two mirror-image panels (left/right) that must meet at a
center-front zipper seam with the chevron motif matching exactly, on a print motif that is
**not symmetric under reflection** (it points one way, like an arrow) and printed on a fabric with
real physical nap (brushed softshell — the raised fiber surface runs in one direction, exactly the
`nap` concept the Sewing & Craft Alliance guideline below documents). To generate the CAD
artwork for the mirrored right-front panel from the master left-front motif, Yuki must apply a
**90° rotation** (to align the motif to the marker's cutting angle) and a **reflection** (to
produce the mirror-image panel) — in one of two orders:
A.) **Rotate, then reflect** the motif, OR
B.) **Reflect, then rotate** the motif.

**Why it's close — verified by direct coordinate computation, not asserted.** Model the motif's
registration point (the pixel CAD uses to lock the print to the cut line) at position (1, 0)
relative to the panel's local origin. Let R = 90° CCW rotation, R(x,y) = (−y, x); let F = reflection
across the panel's vertical center-seam axis (the y-axis), F(x,y) = (−x, y). Composing them in the
two orders:
- **Rotate-then-reflect:** F(R(1,0)) = F(0,1) = **(0, 1)** — registration point lands at the *top*
  of the panel.
- **Reflect-then-rotate:** R(F(1,0)) = R(−1,0) = **(0, −1)** — registration point lands at the
  *bottom* of the panel.
These are not approximately different — they are opposite points, related by a 180° rotation
about the origin, because rotation and reflection do not commute in general (a standard, verified
dihedral-group fact, confirmed here by direct substitution rather than taken on authority). One
order places the registration point where the marker's chevron-match line actually is; the other
places it at the mirror-opposite location, which fails the seam match outright. Which order is
correct depends on which axis the marker is built around — a real, checkable geometric fact, not
a coin flip — but a novice CAD operator who assumes "rotation and reflection commute, order
doesn't matter" will get a 50/50 shot at guessing right.
**The real, sourced cost of getting it wrong (or of playing safe).** A second, independent
real-world constraint compounds the dilemma: because the fabric has true nap, reflecting the
motif also **reverses the nap direction** on the mirrored panel — a real defect the Sewing & Craft
Alliance's own napped-fabrics guideline (below) exists specifically to prevent ("it's very
important to lay out pattern pieces so the nap runs in the same direction on each garment piece or
you'll end up with odd color shading"). The only way to guarantee correct nap direction on *both*
panels is to forbid reflection entirely and use a same-direction-only ("with-nap") marker layout —
which costs a real, sourced **15–25% more fabric yardage** than a layout that's free to flip pieces
(sources below). So Yuki's real choice is not just "which order is mathematically correct" but
"pay the real, documented 15–25% yardage premium for a guaranteed-correct-nap layout, or use the
cheaper flip-allowed layout and get the rotate/reflect composition order exactly right with no
margin for error" — a genuine cost-vs-precision trade-off, not a manufactured one.

**Would close (14 skills, 7 how-to / 7 term — every n=1 skill in the group):**
| id | kind | label |
|---|---|---|
| geometry-congruent | term | Congruent |
| geometry-similar | term | Similar |
| geometry-translation | term | Translation |
| geometry-symmetry | term | Symmetry |
| geometry-line-of-symmetry | term | Line Of Symmetry |
| geometry-dilation | term | Dilation |
| geometry-scale-factor | term | Scale Factor |
| geometry-how-to-translate-a-figure-on-the-coordinate-plane | how-to | How to translate a figure on the coordinate plane |
| geometry-how-to-reflect-a-figure-across-the-x-axis | how-to | How to reflect a figure across the X-Axis |
| geometry-how-to-reflect-a-figure-across-the-y-axis | how-to | How to reflect a figure across the Y-Axis |
| geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-counterclockwise | how-to | How to rotate a figure on the coordinate plane 90 degrees counterclockwise |
| geometry-how-to-rotate-a-figure-on-the-coordinate-plane-180-degrees | how-to | How to rotate a figure on the coordinate plane 180 degrees |
| geometry-how-to-dilate-a-figure-on-the-coordinate-plane-given-a-scale-factor | how-to | How to dilate a figure on the coordinate plane given a scale factor |
| geometry-how-to-find-the-scale-factor-of-a-dilation | how-to | How to find the scale factor of a dilation |

The `similar`/`dilation`/`scale-factor` skills fit a real secondary step, not a bolted-on
detour: when the print motif is reused across a print run on a different rotary-screen printer
with a different repeat-length capability (see the Reggiani spec below — repeat is adjustable
25–40 in / 640–1018 mm), the motif is **dilated** by a scale factor to fit an integer number of
repeats into the new machine's range; the dilated copy is **similar** to (not congruent with) the
rotated/reflected/translated copies, which remain congruent to each other and to the original —
a genuine, teachable congruent-vs-similar contrast rather than two unrelated topics forced
together.

**Already-covered skills it also reinforces (do not score, round the case out):**
`geometry-transformation` (n=2), `geometry-reflection` (n=2), `geometry-rotation` (n=3),
`geometry-clockwise` (n=2), `geometry-counter-clockwise` (n=2),
`geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-clockwise` (n=2) — the case
naturally exercises the clockwise/counterclockwise distinction (rotation direction is load-bearing
for which composition order is correct) and both the how-to-rotate-90-CW skill (used for a
different, non-mirrored panel elsewhere in the same jacket's marker) alongside the CCW one scored
above.

**Data feasibility: research pass this session (2026-08-31), real named sources for every
figure used — this raises Data Richness from the preliminary 3.5 (asserted, no sources) to a
grounded score:**
- **EFI Reggiani UNICA rotary screen printer** (real, current commercial equipment; EFI acquired
  Reggiani, a century-old Italian textile-machinery maker) — official brochure
  (efi.com/wp-content/uploads/sites/2/2023/10/EFI-Reggiani-UNICA-Brochure-US.pdf), fetched and
  OCR'd directly this session: **print repeat electronically adjustable from 25 to 40 in
  (640–1018 mm), stepless, no tools needed** — a real, named, numeric repeat-length range, not an
  invented figure.
- **US Patent 5,333,111**, "Garment cutting system having computer assisted pattern alignment"
  (Gerber Garment Technology; confirmed live via Google Patents this session) — real, quoted
  patent language: fabrics "which have a plaid or stripe are troublesome in that the clothing
  designer can specify an alignment of the pattern in several adjacent pieces," historically
  requiring "a skilled worker who would manually align the several patterns," and that a marker
  must "leave relatively large buffers around the garment segment patterns that require matching;
  often as much as half a fabric design repeat" — a real, quantifiable buffer figure (half of the
  Reggiani's real 25–40 in repeat range = a real 12.5–20 in buffer scale, not invented).
- **Sewing & Craft Alliance, Guideline 4.120, "Napped Fabrics"** (sewing.org/files/guidelines/
  4_120_napped_fabrics.pdf; real US home-sewing/craft trade association; fetched and OCR'd this
  session) — confirms, in the association's own words, that napped/directional fabrics require
  "all the pieces run in the same direction" and that "extra fabric is generally required in order
  to lay out the pieces this way," and that inconsistent nap direction causes "odd color shading."
  This guideline does not itself state a percentage; the **15–25% extra-yardage figure** is
  corroborated across multiple independent home-sewing yardage-calculator sources (consistent
  across sources checked this session) as the standard rule of thumb pattern envelopes use for a
  "with-nap" vs. "without-nap" layout, and is used in the case as a disclosed range, not a single
  invented number.
- **UCSB Bren School capstone report, "Examining Cut-and-Sew Textile Waste within the Apparel
  Supply Chain"** (real 2024 graduate client project for Patagonia; PDF fetched and OCR'd in full
  this session) — real, measured marker-efficiency data from actual Vietnam garment factories
  across Patagonia's 2022 Fall/Spring seasons: **82% average material utilization (18% average
  waste), with a measured range of 16–21% waste**; also cites **686 Technical Apparel's own
  publicly disclosed 87% cutting efficiency (13% waste)** — the only one of 50 surveyed apparel
  brands the report found to disclose this figure at all — and the broader literature baseline of
  **10–15% pre-consumer cutting waste** (Rissanen, 2005, "From 15% to 0"). These give the case a
  real, sourced baseline efficiency band to compare the "with-nap"-forced 15–25% penalty against,
  instead of an invented percentage.
Sources checked and explicitly **not** used, disclosed here rather than silently dropped: a
vendor blog (tzstreetwear.com) claimed a "±1.5mm" print-to-seam registration tolerance for
all-over prints; the page returned an HTTP 403 on direct fetch and could not be independently
verified against a primary source, so it is **not** used as a case figure. No AATCC standard or
industry body was found that publishes a numeric tolerance specifically for rotate-vs-reflect
composition order (this appears to be a genuine gap — the geometric fact is verified by direct
computation above, not by an industry standard, and the case should present it that way rather
than attributing it to a standard that doesn't exist).
**Sensitivity (SPEC §6).** None — an engineering/manufacturing trade-off, no protected-subject
flag.
**Split risk.** NONE — 14 "would close" skills is within the honest per-case range and closes
every n=1 skill in a single 20-skill group in one pass, via one physical/geometric model (motif
registration-point transformation under the marker's cutting-angle and mirror requirements); the
6 reinforcement skills round out the same group rather than being bolted on from elsewhere.

**Rubric re-score (0–5 each), before vs. after this research pass:**

| Axis | Before (verbal proposal) | After (this pass) | Why it moved |
|---|---|---|---|
| Skill Fit | 4.5 | **5** | Closes all 14 n=1 skills in the group in one coherent model (motif-registration-point transformation), not a subset; the congruent-vs-similar contrast (rotation/reflection/translation copies vs. a dilated copy) is a genuine curricular fit, not padding. |
| Narrative Pull | 4 | **4.5** | The stakes sharpened from a generic "align a seam pattern" framing to a concrete, irreversible CAD-then-print-then-cut sequence, with a specific real defect (nap-direction mismatch/"odd color shading") a real trade guideline warns against by name. |
| Data Richness | 3.5 | **4.5** | This was the flagged weak axis. Five independent, named, verifiable real sources now ground every figure used: a current commercial printer's spec sheet (Reggiani), a real US patent's quoted engineering language, a real trade association's guideline, and a real 2024 university capstone report with measured factory data plus a real company's disclosed efficiency number. One candidate figure (±1.5mm tolerance) was checked and explicitly rejected for lack of verification, rather than used anyway. |
| Dilemma Tension | 4 | **4.5** | The non-commutativity claim is no longer asserted — it's demonstrated by direct coordinate substitution with a concrete, dramatic result (registration point lands at the literal top vs. bottom of the panel), and the cost side of the tension (15–25% real yardage penalty for the safe/rigid layout) is now a sourced range instead of an implied "more expensive" hand-wave. |
| **Total** | **16 / 20** | **19 / 20** | |

**Recommendation.** Greenlit for `case-write` (2026-08-31) as `the-repeat-match`, targeting
Geometry / Transformations. This clears the batch's own Cold Chain calibration anchor (4.2) by a
wide margin and, at 19/20, would be the highest-scoring concept in this file's rubric — largely
because the Data Richness research pass found real, checkable sources for every load-bearing
number instead of leaving any of them as an invented placeholder.

---

## Addendum (2026-08-31) — one Advanced Operations/Variables concept, not part of the Precal batch

This file's title and every concept above it targets Pre-Calculus. The entry below is a
different-domain, different-band addition appended here on explicit instruction: it targets
**Advanced Operations / Variables** (MS core, T2), where 5 of the group's 11 skills sit at
exactly `n=1` (a real redundancy priority — single point of failure, not a coverage gap). It was
developed from scratch this session (starting premise: a vague "irrigation or HVAC
engineer" idea, not yet a formal concept) through a real research pass, replacing that vague
premise with one specific, real, richly-sourced domain and dilemma. It is scored under the same
§5 formula and narrative rubric as the batch above, for a single consistent record, even though it
does not share the batch's Pre-Calculus target or its "second touch on a fully-covered group"
framing — this one **is** a genuine gap-closing concept for the group's five `n=1` skills, not a
redundancy add-on.

**Domain selection.** Three real candidate domains were researched: (a) HVAC duct sizing via
ASHRAE's Equal Friction method (real, well-documented — ASHRAE friction charts, the
equivalent-diameter formula `Deq = 1.30 × (a×b)^0.625 / (a+b)^0.25`, and real sheet-metal cost-
per-pound estimating data all check out) — but the only real "stakes" layer findable was a
contractor's competitive bid margin, not a hard external pass/fail gate; (b) irrigation pipe
sizing via Hazen-Williams friction loss (real, and richly tabulated — see sources below); (c) a
personal-finance/amortization or Mifflin-St Jeor nutrition domain, not pursued further once (b)
turned up a genuinely stronger stakes layer. **(b) was selected**, specifically narrowed from
generic "irrigation" to **agricultural mainline pipe sizing under USDA NRCS Conservation Practice
Standard 430 (Irrigation Pipeline)**, because unlike the landscape/turf irrigation version of
the same math, the agricultural version carries a real, named, hard external gate: a design that
fails the standard's numeric velocity limit is not just "less efficient," it is disqualified from
USDA EQIP cost-share reimbursement outright.

### C10 — The Mainline Margin   ·   score 8.6   ·   tier T2

**Note on numbering.** Labeled C10, not C9, because this file accumulated two other,
independently-written C9 entries this session (`C9 — The Repeat Match`, Geometry/Transformations,
above; `C9 — The Stake-Out`, Geometry/Fundamentals Of Geometry, below) from concurrent work on the
same file — a numbering collision to flag for whoever reconciles this file, not something this
entry's own content needed to resolve.

**Protagonist.** Denise Okafor, an irrigation systems designer at a small farm-irrigation
contracting firm. Personally at stake: the mainline pipe size she specs this week has to pass
NRCS Conservation Practice Standard 430 certification before her client's USDA EQIP cost-share
contract will pay out at all — and her bid has to beat a competing contractor's quote on the
farmer's total out-of-pocket cost.

**The dilemma.** A.) Spec the **smaller-diameter PVC mainline** (cheaper material cost per foot
and less pipe weight, which matters because EQIP reimburses Practice 430 by the pound installed)
OR B.) Spec the **next-size-up PVC mainline** (costs more per foot and per pound up front, but
keeps flow velocity comfortably under NRCS Code 430's numeric velocity ceiling and cuts the
pipeline's Hazen-Williams friction loss — and therefore the pump's annual energy bill —
substantially).

**Primary metric.** Total annualized cost (amortized material cost, net of the farmer's actual
EQIP cost-share reimbursement, plus annual pump energy cost) per acre-inch of water delivered — a
ratio, not a total, so the two pipe sizes can come out close even though their sticker prices
differ.

**Why it's close.** The smaller pipe is cheaper to buy and, because it weighs less, earns a
smaller per-pound EQIP reimbursement too — cash-flow-wise it looks like the easy win on the
purchase-order line alone. But the Hazen-Williams friction-loss relationship is extremely
diameter-sensitive (friction loss scales with roughly the inverse 4.87 power of diameter and
roughly the 1.85 power of flow rate) — a modest step down in pipe size drives a disproportionate
jump in friction loss, and therefore in the pump's total dynamic head and annual energy cost,
computed from real published water-horsepower-per-unit-energy figures (see sources). If that
same modest step down also pushes velocity past NRCS Code 430's numeric ceiling, the design fails
certification outright and the EQIP payment — a real, named fraction of the total job cost — is
forfeited, not just reduced. Neither side is a free lunch: the larger pipe's higher material cost
and higher farmer co-pay are real out-of-pocket costs regardless of the reimbursement rate, so the
larger pipe does not simply win because "the government pays for the extra weight."

**Would close (11 skills, 5 how-to / 6 term) — the full Advanced Operations/Variables group,
closing all five of its `n=1` skills:**
| id | kind | label |
|---|---|---|
| advanced-operations-variable | term | Variable |
| advanced-operations-constant | term | Constant |
| advanced-operations-coefficient | term | Coefficient |
| advanced-operations-term | term | Term |
| advanced-operations-like-terms | term | Like Terms |
| advanced-operations-distributive-property | term | Distributive property |
| advanced-operations-how-to-evaluate-a-variable-expression-substitution-property | how-to | How to evaluate a variable expression (Substitution Property) |
| advanced-operations-how-to-add-and-subtract-an-expression-with-variables | how-to | How to add and subtract an expression with variables |
| advanced-operations-how-to-solve-a-one-step-equation | how-to | How to solve a one-step equation |
| advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-one-side | how-to | How to solve a multi-step equation with a variable on one side |
| advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-both-sides | how-to | How to solve a multi-step equation with a variable on both sides |

Skill fit is unusually tight for this group: the Hazen-Williams friction-loss formula is a real
**variable expression** the student must **substitute** real GPM/diameter/C-factor values into;
building each option's total-cost expression genuinely exercises **variable/constant/coefficient/
term/like-terms/distributive property** (material cost per foot × length, plus labor, combined
and simplified); isolating pipe diameter from a rearranged friction formula is a genuine
**one-step or multi-step equation**; and finding the flow-rate or run-length at which Option A's
and Option B's total annualized cost expressions are *equal* is a genuine **multi-step equation
with the variable on both sides** — the exact skill this group has the least real-world modeling
precedent for.

**Data feasibility: HIGH.** Named sources, checked live this session (2026-08-31):
- USDA NRCS Conservation Practice Standard, **Irrigation Pipeline (Code 430)**, National Handbook
  of Conservation Practices, 2020 revision (`nrcs.usda.gov`, PDF) — the real, government-published
  numeric design criteria: pipeline velocity must not exceed 7 ft/sec at full capacity (surface/
  subsurface systems) unless surge protection is provided, and friction head loss must be computed
  by the Hazen-Williams equation using named roughness coefficients (C=150 for plastic/PE pipe,
  C=130 for aluminum) — a real, citable, hard numeric design gate, not an invented threshold.
- NRCS Conservation Practice Standard, **Microirrigation (Code 441)**, same series — a second real
  numeric velocity ceiling (≤5.0 ft/sec in mains/submains) for the microirrigation variant, useful
  as a documented cross-check figure.
- Rain Bird's published **Landscape Irrigation Design Manual** and standalone **Friction Loss
  Charts** (`rainbird.com`) — real, richly tabulated friction-loss-per-100-ft tables across
  multiple real pipe classes and schedules (PVC Class 160/200/315, Schedule 40/80, PE SDR tubing,
  Schedule 40 steel, Type K copper), each broken out by pipe size and flow rate in GPM — genuine
  table texture, not a single formula.
- The **Irrigation Association's** own published Friction Loss Charts (2008 edition, PDF) — an
  independent industry cross-check of the same Hazen-Williams-derived figures.
- Kansas State Research and Extension **MF2360, "Comparing Irrigation Energy Costs"**, and the
  companion Nebraska/Mississippi State Extension pumping-plant-performance literature — real,
  named energy-cost conversion figures by fuel type (diesel ≈12.5 water-horsepower-hours per
  gallon, gasoline ≈8.66 whp-hr/gal, electricity ≈0.885 whp-hr/kWh), the real link between a
  friction-loss-driven total dynamic head and an actual annual dollar energy cost.
- Texas A&M AgriLife Extension **EB-6011, "Calculating Horsepower Requirements and Sizing
  Irrigation Systems"** — the real, citable brake-horsepower sizing formula
  (`BHP = Q × H / (3960 × E)`) needed to turn flow rate and total dynamic head into a pump energy
  requirement.
- USDA NRCS **EQIP payment schedules and FY general guidance documents** (`nrcs.usda.gov`) —
  confirm Practice 430 is reimbursed **by the pound of pipe installed**, at a real published
  cost-share rate (75% standard, up to 90% for beginning/underserved producers), and that payment
  is contingent on the installed practice certifying against the Code 430 standard — the real,
  named stakes layer behind "the payment is forfeited, not just reduced."

Sources I am NOT confident about: a single canonical, one-stop published table of PVC pipe
cost-per-foot *and* weight-per-foot together (needed to convert a spec'd diameter into both a
material-cost figure and an EQIP per-pound reimbursement figure) — real distributor price lists
(e.g., Ewing Outdoor Supply, Sprinkler Warehouse) and manufacturer weight tables exist but will
need to be assembled from more than one source, and the specific farm's required flow rate,
run length, and local electricity rate are not published anywhere and will need to be disclosed,
justified Modeling Assumptions built on the real formula structure above — not invented totals.

**Sensitivity (SPEC §6).** None — an agricultural-engineering/cost-share economics trade-off, no
protected-subject flag.

**Split risk.** NONE — 11 skills matches the Advanced Operations/Variables group's full size
exactly, and every skill flows from the same single model (build each option's cost expression
via substitution into the Hazen-Williams formula, then solve for the break-even point); nothing is
bolted on to inflate the count.

**Rubric re-score (0–5 each).** This concept was proposed only as a one-line premise this session
("an irrigation or HVAC engineer... using variable-based formulas to size equipment") and
preliminarily rated before any research: Skill Fit 3.5, Narrative Pull 3, Data Richness 3.5,
Dilemma Tension 3 — **13/20**. After picking the specific NRCS/EQIP-gated agricultural domain and
finding the real sources above:

| | Skill Fit | Narrative Pull | Data Richness | Dilemma Tension | Total /20 |
|---|---|---|---|---|---|
| Before (premise only) | 3.5 | 3 | 3.5 | 3 | **13** |
| After (researched) | 5 | 4 | 5 | 4.5 | **18.5** |

- **Skill Fit 3.5 → 5.** The vague premise gave no reason to believe all 11 Variables-group skills
  would be genuinely forced rather than decorative. The researched version does: the group's two
  weakest-fitting skills in the abstract — the one-step and both-sides multi-step equation
  how-tos — turn out to map directly onto rearranging the Hazen-Williams formula and onto solving
  for the two options' real break-even point, respectively.
- **Narrative Pull 3 → 4.** "Irrigation or HVAC" had no real stakes attached. The researched
  version has a genuine, named, non-decorative stake: a farmer's USDA cost-share payment is
  forfeited outright, not merely reduced, if the design fails a hard government-published velocity
  ceiling. It does not reach 5 because the register is quieter than a life-or-death or
  endangered-species case — money and a farm upgrade, not a person, are on the line.
- **Data Richness 3.5 → 5.** The premise named no actual source. The researched version has six
  independently named, checked, richly-tabulated real sources (a government engineering standard,
  two independent friction-loss chart publishers, and three university extension energy-cost/
  sizing documents), not a single generic formula.
- **Dilemma Tension 3 → 4.5.** The premise's dilemma was generic ("larger vs smaller pipe").
  The researched version is structurally close for a specific, real reason: Hazen-Williams'
  steep diameter exponent (~4.87) means friction loss and energy cost swing hard with a modest
  size change, while the EQIP per-pound reimbursement offsets but never eliminates the larger
  pipe's higher material and co-pay cost — two genuinely competing real cost curves, not one
  obviously dominant option.

**Recommendation.** Greenlit (2026-08-31), pending human approval per this skill's own hand-off
rule. Proceed to `case-write` as `the-mainline-margin` if approved.

---

### C9 — The Stake-Out   ·   score 8.6   ·   tier T2

**Note on scope.** This concept targets **Geometry / Fundamentals Of Geometry**, not a Pre-Calculus
group — it does not belong to this file's original "Precal Second-Pass" batch. It is appended here
per this session's explicit instruction (research/planning pass for a single concept), not as part
of the Precal redundancy sweep above. Fundamentals Of Geometry currently has 13 of its 24 skills
sitting at exactly n=1 (single-case coverage: `Roofline Call`, `Survey Corner`, `Plaza Pavers`, and
`Vent Cap` between them hold every one of those 13 skills at n=1) — a genuine redundancy priority,
and this concept is a deliberate single reinforcement case designed to touch all 13 at once, per
the same reinforcement logic C7/C8 used for their own groups.

**Preliminary score (this session's opening framing, not yet researched):** Skill Fit 4, Narrative
Pull 3, Data Richness 3, Dilemma Tension 3.5 — **13.5/20.**

**Protagonist.** Renata Cruz, a construction layout technician at a site-work subcontractor,
staking footing corners for a six-unit townhome foundation. Personally at stake: her stakes are cut
into the ground today; the concrete crew pours to them tomorrow morning, and a corner that's out of
tolerance isn't caught until the formwork inspector's tape measure finds it — after the crew has
already set the forms.

**The dilemma.** A.) **Angle-based (polar) staking** — occupy a control point with a robotic total
station, sight a backsight ray to a known reference point, turn a computed deflection angle (in
degrees) off that ray, and mark each footing corner along the resulting sightline at its computed
distance OR B.) **Coordinate-based (GNSS/RTK) staking** — walk a GNSS rover to each corner's
preloaded design coordinate and mark it where the rover's live position matches, no sightline or
backsight needed. On this particular site, an existing structure standing on the adjacent lot
blocks the total station's direct line of sight to two of the six corners (forcing a second
instrument setup) — and that same structure sits close enough to those same two corners to be a
real GNSS multipath source. The obstruction is not two separate problems for two separate methods;
it is one physical obstruction that degrades each method through its own real, different failure
mode.

**Primary metric.** Expected total minutes to land one corner stake inside the real ACI 117M-10
plan-location tolerance for this footing size, per corner — base layout time for that method, plus
the expected rework-time cost of a corner that misses tolerance and has to be re-shot, where the
miss probability is driven by each method's own real accuracy spec measured against that real
tolerance band (a ratio-of-margins comparison, not two raw totals, per SPEC §1.4/§2 guidance).

**Why it's close — grounded in real, named specs.**
- **The real tolerance band.** ACI 117M-10's foundation "Location Displacement" tolerance for a
  foundation dimension under 2.4 m is the *greater of* 13 mm or 2% of the specified dimension. A
  townhome footing this size (24 in / ~0.61 m wide) computes to 2% × 610 mm ≈ 12.2 mm — so the
  binding, real tolerance is **13 mm**, each corner, each direction.
- **Total station's real margin.** A typical construction-grade robotic total station's combined
  positional error at ordinary stakeout distances (tens of meters) is dominated by its EDM spec —
  a standard, widely-published ±(2 mm + 2 ppm) — with angular error (1″–5″ options, e.g. Leica
  Viva TS16's published range) contributing well under 1 mm at those distances. Combined error:
  roughly **2–3 mm**, leaving ~10 mm of margin inside the 13 mm band.
- **GNSS/RTK's real margin.** Trimble's own published R12i datasheet spec is **8 mm horizontal**
  RTK precision (with a 1 ppm baseline term, negligible at short range) — inside the 13 mm band,
  but with only ~5 mm of margin, roughly half the total station's. And that 8 mm figure is the
  *open-sky* number: real GNSS/multipath literature (surveyed above) is unanimous that RTK
  accuracy degrades measurably near reflective structures and in "urban-canyon"-type obstruction —
  exactly the real condition this site's adjacent structure creates for the two corners nearest it.
- **The genuine trade-off.** Total station wins on margin (2–3 mm vs. 13 mm tolerance) but loses
  time and flexibility: it needs an unobstructed sightline, and the blocked corners force a second,
  time-costly instrument relocation. GNSS/RTK wins on raw throughput — real, sourced productivity
  data puts single-operator RTK stakeout at up to **500 points/hour** — but its accuracy margin is
  thinner to start with, and the same obstruction that slows the total station down is a real,
  literature-documented risk factor for the rover's accuracy at exactly those two corners. Neither
  method is a free lunch on this particular site; the numbers pull in opposite directions for a
  real, physically-linked reason, not an invented one.
- **Disclosed Modeling Assumptions (data gap, stated plainly, not invented).** No public source
  publishes an authoritative "minutes lost re-setting up a total station after a blocked sightline"
  figure, nor an exact "RTK error at N meters from a specific structure" figure — the industry
  literature confirms the *direction and reality* of both effects (extra setup time; multipath
  degradation near structures) without giving a portable universal number for either. The base
  per-point layout-time figures for each method, and the exact size of the near-structure RTK
  accuracy penalty, would be built as disclosed Modeling Assumptions *anchored to* the real specs
  and real qualitative sourcing above — same treatment C1/C8 gave their own assumption gaps.

**Would close (13 skills, 2 how-to / 11 term) — closes every Fundamentals Of Geometry skill
currently sitting at n=1:**
| id | kind | label |
|---|---|---|
| geometry-ray | term | Ray |
| geometry-degree | term | Degree |
| geometry-acute-angle | term | Acute Angle |
| geometry-obtuse-angle | term | Obtuse Angle |
| geometry-right-angle | term | Right Angle |
| geometry-transversal-line | term | Transversal Line |
| geometry-fundamentals-of-geometry-congruent | term | Congruent |
| geometry-supplementary-angles | term | Supplementary Angles |
| geometry-complementary-angles | term | Complementary Angles |
| geometry-vertical-angles | term | Vertical Angles |
| geometry-adjacent-angles | term | Adjacent Angles |
| geometry-how-to-find-angle-measures-of-intersecting-lines | how-to | How to find angle measures of intersecting lines |
| geometry-how-to-find-angle-measures-given-parallel-lines-a-transversal-line-and-at-least-one-an | how-to | How to find angle measures given parallel lines, a transversal line and at least one angle measure |

The backsight-to-corner sightline is a **ray**; the deflection turned off it is measured in
**degrees** and classified as **acute/obtuse/right**; a second baseline run to reach the blocked
corners crosses the first as a **transversal line**, and the angle pairs it creates at each
crossing — **vertical**, **adjacent**, **supplementary**, **complementary** — are exactly what the
two **how-to** skills (finding angle measures at an intersection; finding them given a transversal
across parallel lines) are used to solve for when checking that the new baseline is truly parallel
or perpendicular to the original. Comparing the polar-staked and GNSS-staked positions for the same
corner is a **congruent**-triangles check within tolerance. Every skill flows from one real
staking model — none is bolted on to inflate the count, and this batch of 13 matches this group's
own count of skills sitting at n=1, exactly.

**Already-covered skills it also exercises.** measurement-how-to-convert-an-amount-from-one-unit-to-another-unit
(mm ↔ inches, a real necessity since ACI 117M is metric and U.S. site tolerances/equipment specs
are usually read in inches), advanced-numbers-how-to-find-the-percent-of-a-number (the 2%-of-
dimension tolerance term). Do not score, but round the case out.

**Data feasibility: HIGH.** Named sources, checked live this session (2026-08-31):
- ACI 117M-10 (Reapproved 2015), *Specification for Tolerances for Concrete Construction and
  Materials* — Section 3 foundation tolerances, "Location Displacement" table: foundation
  dimension ≥2.4 m → ±50 mm; foundation dimension <2.4 m → greater of 13 mm or 2% of specified
  dimension. Confirmed via theconstructor.org's tabulated summary of the standard (concrete.org
  hosts the standard itself but only as a paid/preview PDF that did not yield readable tolerance
  tables this session).
- Leica Viva TS16 robotic total station datasheet (leica-geosystems.com) — published angular
  accuracy options of 1″, 2″, 3″, 5″.
- Trimble S8/comparable total station EDM accuracy spec, ±(2 mm + 2 ppm) with prism — a standard,
  widely-cited industry-standard EDM spec (confirmed via multiple independent surveying-reference
  sources, e.g. the THS Concepts total-station-accuracy explainer and surveyor forum technical
  discussion).
- Trimble R12i GNSS receiver datasheet (geospatial.trimble.com / manufacturer-hosted PDF mirrors)
  — published RTK horizontal precision spec of 8 mm (with a 1 ppm baseline-length term).
  Confirmed via Trimble's own product page copy; the PDF datasheet itself did not parse as
  readable text this session, but the same 8 mm figure is independently corroborated by the
  product-page summary.
- Alphageo's "Robotic, Manual Total Stations & GPS Surveying Equipment Compared" industry article
  — real, quoted productivity figure: "GNSS RTK systems allow a single operator to collect 500 or
  more points per hour," plus qualitative cost tiering (manual total station lowest; robotic total
  station 3–5× a manual unit's price; GNSS medium-to-high) and qualitative accuracy-limitation
  notes (total stations need clear line of sight to the prism; GNSS degrades in confined/
  obstructed spaces).
- GNSS multipath/urban-canyon literature (GPS World's "Research roundup: GNSS in urban canyons";
  Swift Navigation's multipath glossary entry; PolyU's "3D Mapping Database-Aided GNSS RTK"
  paper) — real, peer-reviewed and industry-technical confirmation that RTK accuracy degrades
  specifically near reflective structures/obstructions, the mechanism (not the exact magnitude for
  an unbuilt hypothetical site) behind this concept's dilemma.
- Real published equipment rental rates as a secondary cost signal: KWIPPED marketplace average
  $269/day for a robotic total station; Washington State DES's public equipment-rental schedule
  lists a Topcon robotic total station (GPT-3000 series) at $275/day — both real, named, current
  figures, usable if the case's write-up wants a standing-cost comparison alongside the
  per-stake-point time metric.

Sources I am NOT confident about: the exact base per-point layout-time figure for each method, and
the exact magnitude (not just direction) of near-structure RTK degradation for a specific unbuilt
hypothetical site, are not published anywhere found this session — both would become disclosed
Modeling Assumptions anchored to the real specs/qualitative sourcing above, not invented totals.
The concrete.org-hosted ACI 117 PDF itself did not yield readable tolerance tables via automated
fetch this session; the tolerance figures used here are corroborated through a secondary summary
source (theconstructor.org) rather than a direct read of the primary standard — case-write should
attempt to source or purchase the primary ACI 117M-10 document directly before finalizing the
numeric tolerance claim.
**Sensitivity (SPEC §6).** None — a construction-trades engineering/quality trade-off, no
protected-subject flag.
**Split risk.** NONE — 13 skills is a large but still single-digit-plus-a-bit count, within the
8–15 honest range this file has already used for a single case (see C1's own note), and every skill
flows from one physical staking-and-checking model; nothing here is bolted on to inflate the count.

**Rescored narrative/fit rubric (0–5 each), after the research pass above:**

| Concept | Skill Fit | Narrative Pull | Data Richness | Dilemma Tension | Total /20 |
|---|---|---|---|---|---|
| C9 The Stake-Out — before | 4 | 3 | 3 | 3.5 | **13.5** |
| C9 The Stake-Out — after | 5 | 4 | 4.5 | 4 | **17.5** |

**Justification for the re-score.**
- **Skill Fit 4 → 5.** Every one of this group's 13 n=1 skills — not a curated subset — turns out
  to map onto one real staking-and-verification model with no forcing: bearings are degrees off a
  ray, deflection angles classify as acute/obtuse/right, a second baseline is a real transversal
  crossing the first, and the four angle-pair terms plus both how-to skills are exactly what
  checking that baseline's parallelism/perpendicularity requires. This is as tight a fit as any
  concept in this file.
- **Narrative Pull 3 → 4.** The preliminary score under-rated the stakes: this is not an abstract
  angle-classification exercise, it is a named technician's stakes going into the ground today,
  ahead of tomorrow's pour, with a real, tight, code-specified tolerance and a real, non-obvious,
  structurally-linked reason neither method is simply "the right answer." Not a top-tier drama
  premise (no life-or-death stakes), but a genuine professional-consequence one.
- **Data Richness 3 → 4.5.** The preliminary score was speculative; the research pass found real,
  named manufacturer datasheets (Leica TS16, Trimble R12i), a real published national standard
  (ACI 117M-10) with an actual numeric tolerance table, real industry productivity/cost data, and
  real peer-reviewed/technical multipath literature — a genuinely well-sourced concept, held back
  from a 5 only because two figures (per-point layout time; near-structure RTK degradation
  magnitude) resolve to disclosed assumptions rather than hard published numbers.
- **Dilemma Tension 3.5 → 4.** The tension moved from "plausible but unverified" to "real and
  structurally linked": the same obstruction produces a real accuracy cost for one method and a
  real time cost for the other, which is a stronger and more defensible tension than two
  independently-chosen pros/cons would have been. Held short of 4.5–5 because the actual numeric
  gap between the two methods' expected-minutes metric depends on the disclosed assumptions above,
  not on two fully-independent hard numbers the way, say, C8's hours-vs-days comparison does.

**Recommendation.** Promising, not yet greenlit — this was a research/planning pass, not a
case-write. Before `case-write`: (1) obtain a direct, readable copy of ACI 117M-10 §3 to confirm
the tolerance table first-hand rather than through a secondary summary; (2) decide and disclose the
base per-point layout-time Modeling Assumption for each method, anchored to the qualitative
productivity sourcing above; (3) decide and disclose the near-structure RTK-degradation Modeling
Assumption, anchored to the qualitative multipath-literature direction above. All three are
tractable — none is a structural asymmetry of the kind that sank the superseded C3/C9 (in the other
concept file) cases.

---

## Addendum (2026-08-31) — one Calculus/Limits And Continuity concept, not part of the Precal batch

**Note on scope.** Like the two addenda above, this targets a different domain/band than this
file's Pre-Calculus batch: **Calculus / Limits And Continuity**, where all 6 group skills
(`calculus-limit`, `calculus-one-sided-limit`, `calculus-continuity`, `calculus-discontinuity`,
`calculus-how-to-evaluate-a-limit-algebraically`, `calculus-how-to-determine-whether-a-function-is-
continuous-at-a-point`) sit at exactly `n=1` in `readmodel/standards_spine.json` — a fully
uncovered-if-lost group, the same redundancy/gap-closing priority as C9/C10 above. This is a
research/planning pass only, on explicit instruction — not a case-write.

**Starting premise (unresearched, this session).** "The Bracket Cliff" — a tax policy analyst
comparing a tax-bracket "cliff" (jump discontinuity in effective rate at a threshold) vs. a
smoothed/continuous marginal-rate schedule. Preliminary score, before any research: Skill Fit 4,
Narrative Pull 4, Data Richness 4.5, Dilemma Tension 3.5 — **16/20**.

**What the research found — the premise needed a correction, not just sourcing.** U.S. federal
marginal income-tax brackets are, in fact, designed to avoid a jump discontinuity: only the income
*within* each bracket is taxed at that bracket's rate, so a household's total tax liability
`T(income)` is continuous everywhere, including at every bracket boundary (the "just earned $1 more
and lost thousands" cliff many people fear from ordinary tax brackets is a real, common
misconception, not a real feature of the federal bracket structure). The original premise, taken
literally, does not hold up — exactly the outcome this task told me to watch for and pivot on.

**The real, documented cliff found instead: the ACA premium tax credit's 400%-of-FPL subsidy
cliff.** This is a genuine, heavily-documented jump discontinuity, and — as of this research pass,
2026-08-31 — a live, current-events policy fact: the American Rescue Plan Act (2021) and Inflation
Reduction Act (2022) temporarily removed the income cap on ACA premium subsidies from 2021–2025,
capping premiums at a percentage of income for everyone regardless of income (a continuous,
smoothed structure). Congress did not extend that provision, so for the 2026 plan year the original
400%-of-the-federal-poverty-line hard eligibility cutoff is back in force: a household at exactly
400% FPL receives a subsidy; a household at 400.01% FPL receives $0 — a real, current, textbook
jump discontinuity, not a hypothetical one.

**Real numbers found (KFF, 2026 plan-year figures).**
- 2026 subsidy-eligibility threshold: **$62,600/year for a single filer**, **$128,600/year for a
  family of four** (400% of the applicable federal poverty guideline; one secondary source gave
  $132,000 for family-of-four 400% FPL — the discrepancy likely traces to which HHS poverty-
  guideline vintage/year each source's calculator used, and would need to be pinned down and
  disclosed as a Modeling Assumption at case-write time rather than silently resolved here).
- Worked example (60-year-old enrollee, 2026 projected premiums): at **$62,000/year income (≈396%
  FPL)**, the subsidized premium is **≈$6,175/year** (≈10% of income, the enhanced-credit-era
  affordability cap). At **$64,000/year income (≈409% FPL)** — just $2,000 more — the same person
  pays the **full, unsubsidized benchmark premium, ≈$14,931/year** (≈25% of income). That is a
  **$8,756/year jump** in cost triggered by a **$2,000** difference in income — the literal
  `lim_{x→400%⁻} C(x) ≠ lim_{x→400%⁺} C(x)` this skill group exists to teach, with real dollar
  figures on both sides of the limit, not invented ones.
- A second real example (60-year-old couple at ≈402% FPL, ≈$85,000/year combined income): annual
  premium ≈$22,600 (≈a quarter of income) without the enhanced/continuous subsidy formula, versus
  8.5%-of-income under the enhanced formula that applied 2021–2025.
- People earning over 400% FPL were about **5% of subsidized marketplace plan selections in 2024** —
  a real, sourced sense of how many households this discontinuity actually touches.

**Real cost-of-smoothing number (CBO).** Permanently restoring the continuous, no-hard-cutoff
subsidy formula (i.e., removing the cliff nationwide, the same structure ARP/IRA used 2021–2025)
was scored by the Congressional Budget Office at **≈$350 billion added to the federal deficit over
the FY2026–FY2035 window** (≈$296B in higher direct spending, ≈$54B in lower revenue) — a real,
named, large number for what "just make it continuous" actually costs at the federal level.

**Real, live evidence that some governments have already chosen to bear (part of) that cost
themselves.** Ten states currently fund their own wraparound subsidies on top of the federal
formula: California, Colorado, Connecticut, Maryland, Massachusetts, New Jersey, New Mexico, New
York, Vermont, and Washington (SHVS, "Supporting Insurance Affordability with State Marketplace
Subsidies," 2026). Several increased state funding specifically because the federal enhancement
expired: **New Mexico fully replaced the lost federal enhancement for households under 400% FPL**
in its own state program; **Massachusetts added $250 million** to its ConnectorCare wraparound;
**California allocated $190 million** (for 2026, rising to $300 million for 2027) — real, named,
current dollar figures for what one state alone spends to smooth part of this exact cliff. None of
these state programs has extended smoothing *above* 400% FPL, which is the live policy choice this
concept's protagonist would be modeling.

**The revised concept — The Bracket Cliff, retargeted to the real ACA subsidy cliff.**

**Protagonist.** Priya Nakamura, a health policy analyst in a state's health benefit exchange
policy office (a fictional analyst at a generic but realistic state exchange, modeled on the real,
named programs above — not attributed to any specific real state's internal deliberations).
Personally at stake: her office has a small discretionary line item this budget cycle, and she has
to recommend whether to spend it extending the state's own wraparound subsidy to smooth the federal
400%-FPL cliff for households just above the current state-subsidized band, before the legislature's
budget markup locks the number in.

**The dilemma.** A.) **Do nothing — accept the reinstated federal cliff.** The state's exchange
simply applies the federal formula as published: $0 in additional state cost, no new administrative
rule, but every household that crosses 400% FPL — including by a raise as small as $2,000/year —
falls off a real, calculable financial cliff (the ≈$8,756/year jump found above). OR B.) **Fund a
state-level smoothing subsidy** (the real approach New Mexico, Massachusetts, and California have
each taken, at real, named dollar costs) that extends a continuous, income-scaled premium cap past
400% FPL instead of cutting to $0 — removing the discontinuity, verified using the actual definition
of continuity at a point, but at a real, non-trivial, ongoing state budget cost with no federal
reimbursement.

**Primary metric.** The size of the jump discontinuity in a household's annual net insurance cost
function, `C(income)`, at the 400%-FPL threshold — evaluated as the two one-sided limits,
`lim_{x→400%⁻} C(x)` and `lim_{x→400%⁺} C(x)` — compared across Policy A (reinstated cliff, real
2026 KFF figures) and Policy B (a continuous extension of the income-scaled cap, modeled on the real
2021–2025 enhanced-credit formula), set against Policy B's real, named annual cost (scaled from the
real single-state figures above, e.g. New Mexico's/California's own program cost, disclosed as the
Modeling Assumption bridging "one real state's program cost" to "this state's illustrative figure").

**Why it's close.** Policy A costs the state $0 and requires no new rule — pure administrative
simplicity — but leaves a real, provable, and (per KFF) currently-live jump discontinuity that a
household can fall into with a raise as small as $2,000/year, a fact with real news-cycle salience
in 2026. Policy B is provably continuous at the threshold (the defining `left limit = right limit =
f(400%)` check this skill group exists to teach comes out clean, unlike Policy A's), and real states
have already judged it worth paying for — but "worth paying for" is not "free": the real federal-
scale CBO estimate (~$350B/10yr) and the real single-state costs (New Mexico's full replacement,
Massachusetts's $250M, California's $190–300M) show smoothing is a genuine, named, recurring budget
line, not a costless fix. The analyst's recommendation is not "which is mathematically better" (B
obviously wins that) — it is "is the size of a documented discontinuity, at this state's specific
income distribution near 400% FPL, worth this specific dollar cost," which only resolves once both
sides are actually computed, not assumed.

**Target skills (Calculus / Limits And Continuity — all 6 skills in the group, currently n=1
each):**
| id | kind | label |
|---|---|---|
| calculus-limit | term | Limit |
| calculus-one-sided-limit | term | One-Sided Limit |
| calculus-continuity | term | Continuity |
| calculus-discontinuity | term | Discontinuity |
| calculus-how-to-evaluate-a-limit-algebraically | how-to | How to evaluate a limit algebraically |
| calculus-how-to-determine-whether-a-function-is-continuous-at-a-point | how-to | How to determine whether a function is continuous at a point |

The net-cost function `C(income)` under Policy A is piecewise: the income-scaled premium cap for
`income ≤ 400% FPL`, the full unsubsidized benchmark premium for `income > 400% FPL` — evaluating
`C` as income approaches 400% FPL from each side is a direct **one-sided limit** computation using
real 2026 KFF dollar figures on both sides; showing the two one-sided limits disagree (and finding
the exact size of the gap) is evaluating a **limit algebraically** and then applying the **how to
determine whether a function is continuous at a point** procedure to show `C` fails continuity
there — a genuine, textbook **discontinuity**, not an assumed one. Policy B's `C(income)` — the
continuous extension modeled on the real 2021–2025 enhanced-credit formula — is then checked against
the same three-part continuity definition at the same threshold and passes, giving the class a real
positive and negative worked example of the same **continuity**/**limit** machinery on the same real
policy fact pattern.

**Already-covered skills it also exercises.** advanced-numbers-percent, advanced-numbers-how-to-
find-the-percent-of-a-number (income-as-percent-of-FPL, premium-as-percent-of-income affordability
caps this whole case is built on). Do not score, but round the case out.

**Data feasibility: HIGH.** Named sources, checked live this session (2026-08-31):
- KFF, "A Steep Subsidy Cliff Looms for Older Middle-Income Enrollees if ACA Enhanced Tax Credits
  Expire" (KFF Quick Takes, 2026) — the core worked example: 60-year-old at $62,000/≈396% FPL
  paying ≈$6,175/year vs. $64,000/≈409% FPL paying ≈$14,931/year (full benchmark premium), and the
  60-year-old-couple ≈402% FPL / ≈$85,000 / ≈$22,600-premium example; also the "≈5% of subsidized
  marketplace selections were above 400% FPL in 2024" figure.
- healthinsurance.org, "Marketplace enrollees face return of the 'subsidy cliff' in 2026" and its
  companion FPL/subsidy-calculator glossary pages — confirms the cliff's mechanics and the
  $62,600 single / $128,600 family-of-four 400%-FPL threshold figures for 2026 plan-year coverage.
- CNBC, "ACA subsidy cliff: How to keep premium tax credits" (2025-11-18) and "ACA subsidy cliff
  may mean 'astronomical tax bills' for many, CFP says" (2026-01-06) — confirms the 2021–2025
  ARP/IRA enhanced-credit period removed the income cap, and that it was not extended into 2026,
  restoring the hard 400%-FPL cutoff.
- Congressional Budget Office cost estimate (via American Health Law Association's "CBO Pegs Cost
  of Extending ACA Premium Tax Credit at $350 Billion over Ten Years," and corroborated by the
  Committee for a Responsible Federal Budget's "Offsetting ACA Enhanced Subsidy Extensions") — the
  real ≈$350B/FY2026–FY2035 deficit-cost estimate for a permanent, continuous, cliff-free formula.
- Center on Budget and Policy Priorities' SNAP benefit-cliff research (used to confirm what a real,
  well-documented "benefit cliff" analysis looks like methodologically, and to rule out SNAP itself
  as the primary example here — SNAP's own benefit formula phases out gradually, 24–36 cents per
  additional earned dollar, which is a real disincentive-at-the-margin story but not a jump
  discontinuity the way the ACA cliff is).
- State Health and Value Strategies (SHVS), "Supporting Insurance Affordability with State
  Marketplace Subsidies" (2026 PDF) and healthinsurance.org's "Which states offer their own health
  insurance subsidies?" — the real list of 10 states with wraparound subsidies and the real,
  named per-state dollar figures (New Mexico's full replacement of the federal enhancement,
  Massachusetts's $250M ConnectorCare addition, California's $190M-for-2026/$300M-for-2027 program).

Sources I am NOT confident about: the exact 2026 family-of-four 400%-FPL dollar figure has two
slightly different values across sources found this session ($128,600 vs. $132,000) — needs
reconciling against the actual HHS poverty-guideline vintage ACA subsidy calculations use, and
disclosed as a Modeling Assumption if not fully resolvable at case-write time; no state currently
funds smoothing *above* 400% FPL (all 10 real state programs found smooth the *lower* end, up to
roughly 150–400% FPL), so the specific "extend smoothing above 400%" policy option in this concept's
Option B is itself a Modeling Assumption grounded in real states' *demonstrated willingness to fund
smoothing*, not a real, already-implemented above-400%-FPL program — this should be disclosed
explicitly in FACILITATOR.md/case.md rather than implied as already-existing policy.

**Sensitivity (SPEC §6).** Flag for facilitator review: this concept touches real, current
(2026) health-policy and federal-budget debate. Unlike this file's engineering/optics/agricultural
concepts, this one sits closer to a live partisan policy fight (ACA subsidies, federal deficit
spending) — recommend the case framing stay strictly on the neutral analytical question (the real,
computable size of a discontinuity, and the real, named cost of removing it) rather than on which
policy position is "correct," and that FACILITATOR.md say so explicitly for any facilitator running
this with students.

**Split risk.** NONE — 6 skills matches the group's full size exactly, and every skill flows from
one single model (evaluate the same real net-cost function's one-sided limits and continuity at one
real threshold, under two real policy structures); nothing is bolted on to inflate the count.

**Rubric re-score (0–5 each), before vs. after this research pass:**

| Axis | Before (verbal proposal) | After (this pass) | Why it moved |
|---|---|---|---|
| Skill Fit | 4 | **5** | The original tax-bracket premise, taken literally, does not fit at all — ordinary marginal brackets are continuous, so there is no real discontinuity to evaluate. The replacement (ACA 400%-FPL subsidy cliff) maps onto all 6 group skills with no forcing: a real piecewise cost function, a real jump discontinuity provable via one-sided limits, and a real continuous counter-example (the 2021–2025 enhanced formula) to contrast it against in the same case. |
| Narrative Pull | 4 | **4.5** | Moved up, not down: a real household losing ≈$8,756/year in subsidy from a $2,000 raise, on a policy question that is literally back in the news in 2026 (the cliff's return was not extended into this plan year), is a sharper, more current hook than the original generic "tax bracket" framing — but held below 5 because the register is a policy-memo one (dollars and thresholds), not a life-or-death or endangered-species-tier premise. |
| Data Richness | 4.5 | **5** | The original 4.5 was an estimate with no sources at all. The researched version has real, named, cross-corroborating sources for every load-bearing figure: KFF's worked dollar example, CBO's $350B cost estimate, and SHVS/healthinsurance.org's real per-state program-cost figures — a stronger evidentiary base than the original guess implied. |
| Dilemma Tension | 3.5 | **4.5** | The original premise had no real second side to weigh (a jump discontinuity that doesn't actually exist has no genuine "keep it vs. fix it" tension). The researched version does: Policy A is free but leaves a real, provable discontinuity; Policy B is provably continuous but has a real, named, non-trivial cost (CBO's $350B federal-scale figure; real $190M–$250M single-state costs) — a genuine two-sided trade-off, not a one-sided "just fix it" story. |
| **Total** | **16 / 20** | **19 / 20** | |

**Recommendation.** The originally-proposed premise ("ordinary tax-bracket cliff") does not survive
research and should be dropped — regular marginal tax brackets are continuous by design, not a real
discontinuity. The replacement premise above (the real, current, KFF/CBO/SHVS-sourced ACA
premium-subsidy 400%-FPL cliff) is well-supported and, at 19/20, would sit at the top of this file's
narrative rubric alongside C9/The Repeat Match. This was a research/planning pass only, per this
task's own instruction — not yet greenlit for `case-write`; that decision, and resolution of the
two open items flagged above (the $128,600-vs-$132,000 threshold discrepancy; disclosing Option B's
above-400%-FPL extension as a Modeling Assumption rather than an already-implemented program),
should happen at the normal human-review gate before this becomes a written case.

## Addendum (2026-08-31) — one Geometry/Visual Perceptibility concept, not part of the Precal batch

**Note on scope.** Like the addenda above, this targets a different group than this file's
Pre-Calculus batch: **Geometry / Visual Perceptibility**, where 7 of the group's 11 skills sit at
exactly `n=1` in `readmodel/standards_spine.json` (`geometry-face`, `geometry-edge`,
`geometry-pyramid`, `geometry-cone`, `geometry-cylinder`, `geometry-sphere`,
`geometry-how-to-draw-the-net-of-a-3-d-shape`) — the same single-point-of-failure redundancy
priority as the other addenda in this file. This is a research/planning pass only, on explicit
instruction — not a case-write.

**Starting premise (unresearched, this session): "The Legibility Call"** — a traffic engineer
choosing between two road-sign designs (size/font) under real MUTCD legibility-distance standards.
Preliminary score, before any research: Skill Fit 4.5, Narrative Pull 4, Data Richness 4.5,
Dilemma Tension 4 — **17/20.**

**What the research found — the premise does not survive a skill-fit check.** The MUTCD/FHWA side
of the premise is real: the MUTCD 11th Edition (December 2023), Chapter 2A, sets minimum legend
letter heights by road type and speed (e.g., 6 in minimum for principal legend on conventional
rural major routes; 4 in minimum for low-volume roads and urban streets posted 25 mph), and the
sign industry's own legibility-index convention — divide desired viewing distance in feet by a
font/contrast-specific Legibility Index (a commonly cited value for black Helvetica-family
all-caps on white is 22) to get required letter height in inches — is a real, documented formula
(a distinct, more precise cousin of the informal "1 inch of letter height per 40 feet" rule of
thumb). That math is genuine. **But it is Fundamentals-of-Geometry/proportional-reasoning or
Measurement-domain math (a linear ratio between letter height and viewing distance), and it does
not touch this group's actual skill list at all.** Pulling the real skill list for Visual
Perceptibility (not the plausible-sounding name) shows it is entirely about identifying and naming
3-D solids and their nets: `3-Dimensional`, `Net`, `Face`, `Edge`, `Pyramid`, `Prism`, `Cone`,
`Cylinder`, `Sphere`, `How to draw the net of a 3-D shape`, `How to name a 3-D shape` — this is a
"3-D shapes and nets" group, not a "visual perception / optics / legibility" group despite its
label. A flat road sign and a legibility-index ratio never require identifying a solid, counting
its faces or edges, or drawing its net. This is exactly the kind of premise this task warned about:
a plausible name-based guess (`Visual Perceptibility` reads like it could mean "how perceptible
something is, visually," which is what motivated the sign-legibility idea) that does not survive
checking the group's real, literal skill list.

**Domain search for a real alternative that actually forces this skill list.** Three real
candidates were considered against the group's actual "name/count faces-and-edges/draw-a-net for a
3-D solid" content: (a) optometry/vision-testing chart design — rejected, it is 2-D letter-size
geometry again, the same mismatch as the original premise; (b) aircraft cockpit display
legibility — same 2-D mismatch; (c) a small-batch product manufacturer choosing which solid shape
to cast a new product line in, which genuinely requires naming the candidate solids, counting
faces/edges to reason about how a two-part cavity mold must be split along them, and using each
solid's net to reason about mold-cavity layout. **(c) was pursued**, narrowed to a real, specific,
checkable business: a candle-making business owner choosing a new candle shape for a limited
one-time mold purchase.

### C11 — The Mold Line   ·   score (see rescore below)   ·   tier T3

**Protagonist.** A small-batch candle maker (2–3 employee shop) deciding which single new shape to
add to a holiday product line, given a one-time mold-purchase budget and a fixed per-batch wax
budget.

**The dilemma.** A.) Add a **classic pillar (cylinder)** shape — a smooth, single-axis solid with
no flat faces or edges, castable in a simple, cheap two-part mold that separates along one smooth
seam OR B.) Add a **faceted geometric shape (pyramid or square/rectangular prism)** — a
flat-faced solid meeting at sharp edges and vertices, on-trend in candle retail ("geometric" /
"chakra-pyramid" candles are a real, currently-sold product category) but only castable in a mold
that must be split along its actual edges to demold cleanly, which is a real, standard
mold-making constraint (a solid with flat faces and sharp edges needs its parting line to follow
those edges, or a re-entrant/undercut traps the piece in the mold; a smooth solid like a sphere or
cylinder has no such constraint and can use a simpler mold). Choosing between the two options
requires the maker to correctly **name** each candidate solid, **count its faces and edges** to
reason about how many mold pieces it needs, and reason from its **net** to lay out the mold cavity
— not decoratively, but because the mold-piece-count is exactly what drives the up-front tooling
cost difference between the two options.

**Primary metric.** Total cost to produce and sell one batch of the new shape (mold cost amortized
over the batch, plus wax cost per unit, computed from each solid's real volume formula) compared
against the simpler pillar shape's same total, to decide whether the trendier faceted shape is
worth its higher mold cost for this batch size.

**Why it's close — grounded in real, named sources found this session.**
- **Real wax cost.** Fillmore Container's NatureWax C3 soy wax (Cargill), fetched live this
  session: **$2.16/lb** in a 50 lb case, **$2.22/lb** in a 45 lb case, **$3.90/lb** in a 5 lb
  sample size — a real, named, current wholesale price with genuine bulk-discount structure.
- **Real mold prices, by shape, from one named supplier (Beelite Candles), fetched live this
  session:** smooth pillar/cylinder molds **$18.95–$45.95**; cone/taper molds **$19.95–$28.95**;
  a sphere ("Rose Ball") mold **$18.95**; cubic/block (prism) molds **$28.95–$39.95**. These are
  real, current, named retail prices, not invented figures.
- **The genuine (if imperfect) tension.** The smooth solids (sphere, cylinder, cone) cluster at
  the lower end of this real price range; the flat-faced/faceted shapes (cube/prism) sit at the
  higher end — consistent with, though not a controlled proof of, the mold-parting-line
  face/edge logic above. This is a real, directionally-supported pattern in real catalog data, not
  a single clean formula.

**Would close (7 of 11 group skills, all currently at n=1) — plus 2 already-at-n=2 skills for
reinforcement:**
| id | kind | label |
|---|---|---|
| geometry-face | term | Face |
| geometry-edge | term | Edge |
| geometry-pyramid | term | Pyramid |
| geometry-cone | term | Cone |
| geometry-cylinder | term | Cylinder |
| geometry-sphere | term | Sphere |
| geometry-how-to-draw-the-net-of-a-3-d-shape | how-to | How to draw the net of a 3-D shape |
| geometry-net | term | Net (reinforcement, n=2 → 3) |
| geometry-prism | term | Prism (reinforcement, n=2 → 3) |
| geometry-how-to-name-a-3-d-shape | how-to | How to name a 3-D shape (reinforcement, n=2 → 3) |

Naming each candidate (pillar = **cylinder**; faceted option = **pyramid** or **prism**) is
literally the **how-to-name-a-3-D-shape** skill; counting **faces** and **edges** is what
determines each shape's mold-piece count; sketching each candidate's **net** is how a maker lays
out a mold cavity or a paper/cardstock casting template; **cone** and **sphere** enter naturally as
the other real, commonly-sold candle shapes the maker rules out earlier in the same
decision (both smooth, both cheap to mold, both real retail options at this same supplier) —
rounding out the full smooth-vs-faceted solid taxonomy the group's skill list covers, not bolted
on to inflate the count.

**Already-covered skills it also exercises (different group — Surface Area And Volume; do not
score, but round the case out).** Wax cost requires each shape's real volume formula:
`geometry-how-to-find-the-volume-of-a-cylinder` and `geometry-how-to-find-the-volume-of-a-pyramid`
(both currently at n=1 elsewhere — a nice cross-group reinforcement bonus) and, if a sphere option
is carried into the worked comparison, `geometry-how-to-find-the-volume-of-a-sphere` — which is
currently at **n=0, uncovered by any case** in the spine. If the case-write keeps the sphere option
in the worked math rather than just the narrative, this concept would newly close a skill no
existing case touches at all.

**Data feasibility: MODERATE.** Named, live-checked sources this session (2026-08-31):
- Fillmore Container, NatureWax C3 Soy Wax (Cargill) product page — concrete case pricing as
  quoted above.
- Beelite Candles mold-shape catalog — concrete per-shape retail prices as quoted above.
- MUTCD 11th Edition (December 2023), Chapter 2A (mutcd.fhwa.dot.gov) and general sign-industry
  legibility-index convention — real, but **not usable for this concept**; retained only as a
  record that the original premise's underlying facts were genuine, its skill-group targeting was
  not.

Sources I am NOT confident about: no single authoritative source publishes a controlled,
apples-to-apples "mold cost as a function of face/edge count, holding size and material constant"
table — the pillar-vs-cube price pattern above is a real but noisy retail signal (retail prices
also reflect size, popularity, and tooling amortization the retailer chose, not geometry alone),
and a case-write would need to either disclose the face/edge-driven cost premise as a stated
Modeling Assumption anchored to this directional retail evidence, or find a mold-manufacturing
industry source that speaks to parting-line/cavity-count cost directly (a general plastics/
rotocasting-industry fact, not yet confirmed for candle-specific silicone molds this session).

**Sensitivity (SPEC §6).** None — a small-business product-line decision, no protected-subject
flag.

**Split risk.** LOW — 10 skills across two groups (7 primary + 3 reinforcement), all genuinely
required by one shape-selection decision; not bolted on.

**Rescored narrative/fit rubric (0–5 each):**

| Concept | Skill Fit | Narrative Pull | Data Richness | Dilemma Tension | Total /20 |
|---|---|---|---|---|---|
| "The Legibility Call" — this session's opening estimate | 4.5 | 4 | 4.5 | 4 | **17** |
| "The Legibility Call" — after checking the real skill list | 1 | 4 | 4.5 | 4 | **13.5** |
| C11 The Mold Line — new alternative, after research | 4.5 | 3 | 3 | 3 | **13.5** |

**Justification for the re-score.**
- **Skill Fit 4.5 → 1 (original premise).** This is not a partial-credit miss. Zero of this
  group's 11 real skills — not "3-D shape" vocabulary of any kind — is naturally invoked by
  choosing a flat sign's letter height and font under a viewing-distance ratio. The MUTCD research
  is real and would score well against a *different* target (a ratio/proportion or Measurement
  group), but against Visual Perceptibility as it actually exists in the spine, this is close to
  the floor, not a 4.5. Narrative Pull, Data Richness, and Dilemma Tension are left at their
  original values because the underlying MUTCD/legibility-index facts genuinely do check out —
  the failure here is purely a skill-group mismatch, not a factual one.
- **Skill Fit 4.5 (C11).** Every one of the group's 7 n=1 skills is required by naming, decomposing
  (faces/edges), and net-sketching the candidate solids in one real shape-selection decision, with
  cone and sphere entering as real, same-supplier alternatives the maker also considers rather than
  props. Held at 4.5 rather than 5 only because "prism" is used for a squared-off block shape that
  is a slightly less common real candle-catalog item than the round/faceted shapes that anchor the
  rest of the decision.
- **Narrative Pull 3 (C11).** A real but modest-stakes premise — a small business's product-line
  and budget decision, not a safety, legal, or life-affecting one. Lower than the original
  premise's self-rated 4 because a sign engineer's decision at least implies public-safety framing
  (even though that framing turned out to be geometrically irrelevant to this group); a candle
  shop's holiday SKU choice does not carry comparable narrative weight.
- **Data Richness 3 (C11).** Real, named, live-checked prices exist for both wax and molds, but
  neither is a single authoritative standard or manufacturer datasheet the way MUTCD, ACI 117M, or
  the Leica/Trimble specs were in this file's other researched concepts — it is retail catalog
  pricing from one or two named suppliers, useful and real but noisier and less rigorously
  documented.
- **Dilemma Tension 3 (C11).** The cost-vs-trend tension is genuine and directionally supported by
  real prices, but it rests on a retail price *pattern*, not an independent, controlled
  face/edge-count-to-cost formula — weaker than this file's better-sourced concepts (e.g. C9/The
  Stake-Out's real accuracy-spec-vs-real-tolerance-band comparison), honestly reflected here rather
  than inflated.

**Recommendation.** Do not pursue "The Legibility Call" against Visual Perceptibility — the
premise's math is real but targets the wrong skill group entirely, confirmed by checking the
spine's actual skill list rather than its group name. C11 "The Mold Line" is a genuine, real,
skill-fit-correct alternative for this group, but its data is retail-catalog-grade rather than
standard/datasheet-grade — promising enough to keep, not strong enough to greenlight for
`case-write` without either (1) finding an industry (plastics/rotocasting) source that speaks
directly to face/edge-count-driven mold cost, or (2) explicitly disclosing the face/edge-cost
premise as a stated Modeling Assumption anchored to the real, directional retail evidence above.
This was a research/planning pass only, per this task's own instruction.

---

### C11 — The Trial Size   ·   Statistics And Probability / Algebra (9 skills; 5 sit at n=1)

**Note on scope.** Like C9/C10 above, this concept targets a **Statistics And Probability** group,
not a Pre-Calculus one — appended here per this session's explicit instruction (a single-concept
research/planning pass), not part of the file's original Precal redundancy batch. The Algebra group
under Statistics And Probability currently has 5 of its 9 skills sitting at exactly n=1
(`x-intercept`, `system-of-equations`, `how-to-write-a-linear-equation-given-a-graph-of-a-line`,
`how-to-draw-a-line-given-its-linear-equation`, `how-to-solve-a-system-of-linear-equations` — see
`readmodel/standards_spine.json`, domain "Statistics And Probability" → group "Algebra") — a genuine
redundancy priority.

**Preliminary score (this session's opening framing, before research):** Skill Fit 4.5, Narrative
Pull 4.5, Data Richness 4.5, Dilemma Tension 4 — **17.5/20.** This was a bare estimate: zero real
sources, and — critically, as the research below found — a mechanism (an epidemiologist "solving
the sample-size formula for n") that does not actually belong to this skill group at all.

**What research found before the concept could be trusted.** The standard public-health
sample-size formula is real and confirmed: rearranging the margin-of-error formula for a population
proportion, E = z·√(p(1−p)/n), for n gives **n = z²p(1−p)/E²** — documented in CDC Epi Info's
StatCalc population-survey tool, and in standard introductory-statistics texts (Penn State STAT 200;
eCampusOntario's *Introduction to Statistics*). It is real, and it is genuinely how epidemiologists
size a survey. But it is **not** an Algebra-group skill under this spine: solving it for n requires
squaring both sides of a square-root equation, not isolating a variable in a linear equation — and
the spine has no "solve a formula containing an exponent/radical for one of its variables" skill at
all (checked the neighboring Advanced Operations groups: Order Of Operations, Variables, Exponents,
Scientific Notation/Factorial/Absolute Value — the deepest equation-solving skill there is
multi-step *linear* equations). The Algebra group actually on the spine (`x-intercept`, `y-intercept`,
`slope`, `system-of-equations`, and five slope/linear-equation how-tos) is about **linear
cost/rate functions** — not power-analysis algebra. Forcing the sample-size formula into this group
would have been decorative, not load-bearing. The concept below was rebuilt from scratch around a
mechanism that actually is linear: **the real, published, linear cost structure of a public-health
serosurvey** — and it turns out to fit the group's 9 skills tightly, including a genuine,
non-invented use for `x-intercept` (below).

**Protagonist.** Dr. Amara Kondwani, a field epidemiologist on a Ministry of Health serosurvey team
(modeled on the real study role below), tasked with designing a measles/rubella immunity
(seroprevalence) survey ahead of a supplemental vaccination campaign. Personally at stake: her
survey's precision determines which districts and age cohorts get flagged as under-immunized and
targeted for follow-up doses — a survey that's too small risks missing a real immunity gap; a
survey that's too large burns budget that could have bought more vaccine doses or covered more
ground directly. This is protection-framing throughout (identifying and closing immunity gaps
ahead of an outbreak), not a harm/destruction premise — consistent with SPEC §6/§20.

**The real, cited cost data this is built on.** Carcelen AC, Hayford K, Moss WJ, et al., "How much
does it cost to measure immunity? A costing analysis of a measles and rubella serosurvey in
southern Zambia," *PLOS ONE* (2020) — a real, peer-reviewed, itemized costing study of an actual
nested serosurvey:
- **Total nested serosurvey cost: $68,558**, for **658 participants across 16 clusters**.
- **Cost per average participant (blended): $104** ($68,558 ÷ 658 = $104.19 — checks out exactly).
- **Marginal cost per additional participant within an existing cluster: $30** (real, directly
  quoted — this is the survey's true per-person variable cost: extra dried-blood-spot collection,
  lab testing, incremental field time).
- **Marginal cost per additional cluster: $1,620** (real, directly quoted).
- The paper itself states the nested design's minimum adequate sample size was **192 children
  across the same 16 clusters** — a real, quoted, smaller alternative n from the same source.
- The paper also reports the **savings from nesting** ($43,957) versus running the serosurvey as
  its own **standalone survey** — implying a real standalone total of $68,558 + $43,957 = $112,515
  for the same 658 participants (used below only as a secondary sensitivity note, not the primary
  metric).

A second real source — Brenzel L, Saxenian H, Stahley K, Dansereau E, "Cost of immunization
coverage surveys in low- and middle-income countries," *Frontiers in Public Health* (2026) —
corroborates that this kind of survey cost is genuinely linear-ish in participant count at the
population level: household count and total cost are positively correlated (r = 0.58) across many
real surveys, while cost-per-cluster is negatively correlated with cluster count (r = −0.2),
confirming the real-world pattern of "fixed costs spread over a base, plus a real marginal cost per
added person" that this concept's linear model is built on. It also supplies real comparator
per-respondent costs across other survey designs (MICS $204, PCCS $152, LQAS $86, WHO multi-stage
$105) that could season the case's framing without being load-bearing to the primary metric.

**Building the real linear model (the algebra this case actually asks students to do).** Holding
the cluster count fixed at the real 16 used in the study, cost as a function of participants tested
is linear: **Cost(n) = F + $30·n**, where F is the fixed cost of running the 16-cluster
infrastructure before any participant-level testing. F is not itself a number the paper states
directly — it is **derived algebraically** from the two real figures above (disclosed as a derived
quantity, not invented): solving $68,558 = F + $30(658) gives **F = $48,818**. This derivation is
itself the case's "write a linear equation given a set of data" skill in action — students are
handed the two real data points the paper actually reports (or the marginal cost + one real total)
and solve for the equation the same way.

**The dilemma.** With a real fixed survey budget of **$68,558** (the actual total cost of the real
nested design — used directly, not invented) to spend on this serosurvey:
- **Option A — full design (n = 658, the real design actually run).** Spends the entire budget on
  participants; delivers the tightest confidence interval on seroprevalence, most defensible for
  flagging every age cohort's immunity gap district-by-district.
- **Option B — minimum design (n = 192, the paper's own quoted adequate minimum).** Costs
  Cost(192) = $48,818 + $30(192) = **$54,578**, leaving **$68,558 − $54,578 = $13,980** of the same
  fixed budget unspent — real money that could fund **$13,980 ÷ $1,620/cluster ≈ 8 more
  survey clusters** in a currently-unsurveyed district (using the paper's own real marginal
  per-cluster cost), widening geographic coverage instead of tightening precision in the original
  16 — a genuine, real, two-sided trade-off between statistical certainty and program reach, not an
  invented one.

**Primary metric and why the Algebra skills are genuinely load-bearing, not decorative.**
- **Slope ($30/participant)** is the real, directly-quoted marginal cost — read straight off the
  paper, no invention.
- **Writing a linear equation from a set of data** is exactly the F-derivation above: given the
  real marginal cost and one real total, solve for the fixed-cost intercept.
- **y-intercept (F = $48,818)** is that derived fixed cost — the survey's cost before a single
  participant is tested.
- **x-intercept — a genuinely non-decorative use.** Define the *budget-remaining* line
  R(n) = Budget − Cost(n) = $68,558 − $48,818 − $30n = **$19,740 − $30n**. Its x-intercept — the n
  at which the fixed budget is exactly exhausted — is n = 19,740 ÷ 30 = **658**. That is not a
  coincidence built for the case; it is the *actual* real sample size the real study used, recovered
  exactly by solving for where the real budget-remaining line hits zero. This is the strongest,
  least-forced x-intercept use found in this file's research passes so far.
- **System of two linear equations.** Solving {Cost(n) = 48,818 + 30n ; Cost(n) = 68,558} for their
  intersection is the same computation restated as a 2-equation system — a real, meaningful
  "how much can we afford" question, not a textbook-only setup.
- **Solving a system of linear equations / drawing a line from its equation / writing a linear
  equation from a graph** all apply directly to comparing the Option A "spend it all" line against
  the Option B "leave $13,980 for more clusters" line on the same real cost/budget axes.

**Would close (9 skills, 5 how-to / 4 term) — closes every Statistics And Probability/Algebra
skill currently sitting at n=1, plus this group's remaining 4:**
| id | kind | label | current n |
|---|---|---|---|
| statistics-and-probability-x-intercept | term | X-Intercept | 1 |
| statistics-and-probability-y-intercept | term | Y-Intercept | 2 |
| statistics-and-probability-slope | term | Slope | 5 |
| statistics-and-probability-system-of-equations | term | System Of Equations | 1 |
| statistics-and-probability-how-to-identify-the-slope-of-a-line-given-a-set-of-data-or-a-graph-o | how-to | How to identify the slope of a line given a set of data, or a graph of a line of a set of data, or its linear equation | 2 |
| statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data | how-to | How to write a linear equation given a set of data | 6 |
| statistics-and-probability-how-to-write-a-linear-equation-given-a-graph-of-a-line-of-a-set-of-d | how-to | How to write a linear equation given a graph of a line of a set of data | 1 |
| statistics-and-probability-how-to-draw-a-line-of-a-set-of-data-given-its-linear-equation | how-to | How to draw a line of a set of data given its linear equation | 1 |
| statistics-and-probability-how-to-solve-a-system-of-linear-equations | how-to | How to solve a system of linear equations | 1 |

**Already-covered skills it also exercises (Sampling And Experiments group) — do not score, but
round out the case's real vocabulary.** The real study is literally a **cluster-sampling**
(`statistics-and-probability-cluster-sampling`) design with a real **sample size**
(`statistics-and-probability-sample-size`) of 658 drawn from a **population**
(`statistics-and-probability-population`) via **simple random sampling**
(`statistics-and-probability-simple-random-sampling`) within each cluster — every one of these
terms names something the real source paper actually reports, not invented dressing.

**Data feasibility: HIGH.** Named sources, checked live this session (2026-08-31):
- Carcelen AC, Hayford K, Moss WJ, Book C, Thuma PE, Mwansa FD, et al., "How much does it cost to
  measure immunity? A costing analysis of a measles and rubella serosurvey in southern Zambia,"
  *PLOS ONE* 15(10), 2020 — the primary source for every dollar figure in this concept (total cost
  $68,558; n=658 across 16 clusters; $104/participant blended; $30/participant and $1,620/cluster
  marginal costs; 192-child quoted minimum; $43,957 nesting savings). Confirmed via the live PLOS
  ONE article page and PMC mirror (PMC7561102).
- Brenzel L, Saxenian H, Stahley K, Dansereau E, "Cost of immunization coverage surveys in low- and
  middle-income countries," *Frontiers in Public Health*, 2026 — corroborating cross-survey cost
  correlations (r=0.58 cost-vs-household-count; r=−0.2 cost-per-cluster-vs-cluster-count) and
  comparator per-respondent costs (MICS $204, PCCS $152, LQAS $86, WHO multi-stage sampling $105;
  median total survey cost $300,000). Confirmed via the live Frontiers article page.
- CDC Epi Info StatCalc "Population Survey or Descriptive Study" documentation (cdc.gov/epiinfo) —
  confirms the standard n = z²p(1−p)/E² sample-size formula as CDC-documented methodology, used
  here only as narrative/contextual grounding for *why* sample size drives survey precision, not as
  a skill this concept scores against (see mismatch discussion above).

Sources I am NOT confident about / disclosed gaps: (1) the fixed cost F = $48,818 is *derived*
algebraically from the paper's two real published figures, not itself a number the paper states —
this should be presented to students as a derivation exercise, and disclosed in FACILITATOR.md as a
computed, not directly-quoted, figure; (2) I could not source a real, hard per-dose price for "what
else the freed $13,980 could buy" beyond additional survey clusters — I attempted to pull UNICEF
Supply Division's measles-rubella (MR) vaccine per-dose price data this session and every UNICEF
Supply Division PDF returned HTTP 403 to automated fetch; a case-write pass should retry those PDFs
directly (browser fetch, not automated WebFetch) or fall back to the additional-survey-clusters
framing above, which is fully real-sourced already and does not need the vaccine-dose figure at all.

**Sensitivity (SPEC §6).** Low-risk but flag for facilitator awareness: this concept names a real
disease (measles/rubella) and a real public-health surveillance context. Framing is protective
throughout (finding and closing immunity gaps ahead of a vaccination campaign) with no
disease-outcome, mortality, or outbreak-harm content — closer to C9's construction-tolerance register
than to the ACA-cliff concept above's live-policy-debate register. No special handling beyond the
standard "keep the case on the neutral computational question" note this file already gives other
health/insurance concepts.

**Split risk.** NONE — 9 skills matches the group's full size exactly, and every skill flows from
one real, single linear-cost model (one real paper's marginal costs and one real total), not from
skills bolted on to inflate the count.

**Rubric re-score (0–5 each), before vs. after this research pass:**

| Axis | Before (verbal proposal) | After (this pass) | Why it moved |
|---|---|---|---|
| Skill Fit | 4.5 (unverified) | **4.5** | Same number, entirely different and now-verified reasoning. The original claim — that the sample-size formula (n = z²p(1−p)/E²) *is* this group's Algebra skill — does not hold up: that formula requires solving a square-root equation, not a linear one, and the spine has no skill for it. The concept had to be rebuilt around the group's actual content (linear cost/rate functions), which it now fits tightly and non-decoratively — including a genuine, non-invented x-intercept (recovering the real historical n=658 exactly). Held at 4.5, not 5, because the y-intercept ($48,818 fixed cost) is a derived quantity, not a number either source states directly. |
| Narrative Pull | 4.5 | **4** | Moved down slightly: a real field epidemiologist's budget-vs-precision trade-off is a genuine professional stake, but it is a resource-allocation/spreadsheet-register story, not a top-tier drama premise — closer to C1's bid-vs-competitor register than to a life-or-death premise. |
| Data Richness | 4.5 (unverified) | **4.5** | Same number, now actually earned: two real peer-reviewed costing studies (PLOS ONE 2020, Frontiers 2026) supply every dollar figure used, plus a CDC-documented formula for context. Held short of 5 only because the fixed-cost intercept is derived rather than directly quoted, and the "what else the freed budget buys" secondary figure (vaccine dose price) could not be sourced this session (UNICEF PDFs blocked automated fetch). |
| Dilemma Tension | 4 | **4.5** | Moved up: the tension is not merely plausible but *exactly recoverable* from real numbers — solving where the real budget-remaining line hits zero reproduces the real study's actual sample size (658) with no fudging, and the freed-budget alternative (≈8 more real-cost survey clusters) is a genuine, real, two-sided use of the same money, not an invented pro/con pair. |
| **Total** | **17.5 / 20** | **17.5 / 20** | Same total, for substantially different and now-verified reasons — the original guess happened to land close to right, but the mechanism underneath it had to be replaced entirely before the number could be trusted. |

**Recommendation.** The originally-proposed premise ("epidemiologist solves the sample-size formula
for n, scored against this group's Algebra skills") does not survive research and should be dropped
as stated — the formula is real but belongs to no skill on this spine, and forcing it into this
group would have been decorative. The replacement premise above (the real Carcelen et al. Zambia
serosurvey's linear marginal-cost structure, used to build and solve a real linear cost/budget model)
is well-supported and fits this Algebra group's actual 9 skills with no forcing. This was a
research/planning pass only, per this task's instruction — not yet greenlit for `case-write`; before
that: (1) resolve whether to disclose F = $48,818 as a derived-not-quoted figure directly in
FACILITATOR.md (recommended: yes, the same treatment C9/the ACA-cliff concept gave their own
derived/assumption figures); (2) retry sourcing a real UNICEF/Gavi MR vaccine per-dose price for an
optional secondary framing, or proceed without it using the real additional-survey-clusters framing
already fully sourced above.

---

## Addendum (2026-08-31) — one Calculus/Integrals concept, not part of the Precal batch

This file's title and every concept above it targets Pre-Calculus. The entry below is a
different-domain addition appended here on explicit instruction: it targets **Calculus /
Integrals**, where **all 7** of the group's skills sit at exactly `n=1` — the single most
under-redundant, fully-uncovered-if-lost group in the entire corpus (every one of its 7 skills is
`covered_by: ["Total Flow"]` per `readmodel/standards_spine.json`; if that one case is ever
retired or fails QA, the whole group goes to zero coverage at once). It was proposed this session
as a one-line premise — "The Dosing Curve," a pharmacokinetics analyst comparing two drug dosing
schedules by AUC — preliminarily rated 18/20 with zero research behind it. This addendum is that
research pass.

### C11 — The Dosing Curve   ·   score 5.4   ·   tier T2

**Protagonist.** Dr. Priya Chandrasekaran, a food-animal veterinary pharmacology consultant
retained by a stocker-cattle operation to write the herd's antimicrobial treatment protocol for a
bacterial-respiratory-disease outbreak. Personally at stake: the protocol she signs off on has to
clear a real, published pharmacokinetic/pharmacodynamic efficacy threshold (not just "seem like
enough drug") before it can go into the herd's official, auditable treatment records, and it has
to be defensible on cost and animal-handling grounds to the operation's owner.

**The dilemma.** A.) **A single long-acting intramuscular injection** (one handling event per
animal, meets the real published efficacy threshold with the most margin, but costs more per dose
and — per real published comparative pharmacokinetic literature — causes measurably *more*
injection-site tissue damage per event than option B) OR B.) **repeated conventional-formulation
dosing over several days** (cheaper per dose, real published literature shows *less* per-event
tissue damage, but requires multiple handling events — more labor, more animal stress, more total
injection-site-lesion opportunities — and its shorter per-dose half-life means the vet cannot just
assume the cumulative exposure clears the efficacy bar; she has to actually compute it).

**Primary metric.** Cumulative drug exposure over the treatment course — area under the plasma
concentration-time curve (AUC) — checked against a real, published, numeric PK/PD efficacy cutoff
(a target ratio of free-drug AUC to the pathogen's minimum inhibitory concentration, fAUC/MIC).
This is a genuine pass/fail gate, not a preference: a protocol whose computed AUC/MIC ratio falls
short of the published target is not just "less good," it is not a defensible treatment record.

**Why it's close.** Real published data (Aktaş & Yarsan 2017, see sources) shows a single 20 mg/kg
IM dose of conventional oxytetracycline and a single 20 mg/kg IM dose of the long-acting
formulation land within about 9% of each other on total AUC (80.21 vs. 87.35 μg·h/mL) — so if the
comparison stopped at "which total number is bigger," it would barely matter which option Dr.
Chandrasekaran picks. But the two curves have very different *shapes*: the conventional
formulation's half-life (10.47 h) is less than half the long-acting formulation's (27.96 h), and
its Cmax is higher (13.57 vs. 8.72 μg/mL) — a fast, high, short-lived peak versus a lower, flatter,
long-lived plateau. Whether repeated conventional dosing keeps the herd's cumulative exposure
above the real published fAUC/MIC target for the full treatment window, or lets concentration dip
below the efficacy threshold in the gaps between injections, is exactly the kind of question a
single "which AUC number is bigger" comparison cannot answer and a definite integral (or a Riemann
sum built from the real published sampling data) can.

**Would close (7 skills, 3 how-to / 4 term) — the full Calculus/Integrals group, closing all 7 of
its `n=1` skills:**
| id | kind | label |
|---|---|---|
| calculus-antiderivative | term | Antiderivative |
| calculus-definite-integral | term | Definite Integral |
| calculus-indefinite-integral | term | Indefinite Integral |
| calculus-riemann-sum | term | Riemann Sum |
| calculus-how-to-find-an-antiderivative-using-the-power-rule | how-to | How to find an antiderivative using the power rule |
| calculus-how-to-evaluate-a-definite-integral-using-the-fundamental-theorem-of-calculus | how-to | How to evaluate a definite integral using the Fundamental Theorem of Calculus |
| calculus-how-to-approximate-area-under-a-curve-using-a-riemann-sum | how-to | How to approximate area under a curve using a Riemann sum |

Skill fit is unforced and matches real practice, not just real math: a Riemann sum (trapezoidal
rule) is literally the standard way real pharmacology papers compute AUC from discrete sampled
concentration data (this is not a stretch to make the skill fit — it is how the real Aktaş &
Yarsan-style tables get turned into the AUC figures quoted below); fitting a polynomial model to
that same sampled curve and taking its **antiderivative via the power rule** gives a second,
continuous route to the same quantity; evaluating that antiderivative between the treatment
window's start and end times via the **Fundamental Theorem of Calculus** gives the **definite
integral** — total exposure — while the general antiderivative family is the **indefinite
integral**. All four terms and all three how-tos come from one real computation performed two
ways (discrete Riemann sum vs. continuous FTC) and cross-checked against each other, which is
itself standard pharmacology practice (a fitted-curve AUC and a trapezoidal-rule AUC are routinely
reported side by side to confirm they agree).

**Data feasibility: HIGH.** Named sources, checked live this session (2026-08-31):
- **Aktaş İ, Yarsan E. "Pharmacokinetics of Conventional and Long-Acting Oxytetracycline
  Preparations in Kilis Goat." *Frontiers in Veterinary Science*, 2017 Dec 22;4:229,
  doi:10.3389/fvets.2017.00229.** Real published single-dose IM pharmacokinetic parameters at 20
  mg/kg (n=7 goats/group; blood sampled at 0.25, 0.5, 1, 2, 4, 8, 12, 24, 36, 48, 60, 72, 96 h):
  conventional IM — Cmax 13.57±5.83 μg/mL, Tmax 0.46±0.09 h, half-life 10.47±1.30 h, AUC
  80.21±12.71 μg·h/mL, bioavailability 69.71%; long-acting IM — Cmax 8.72±2.47 μg/mL, Tmax
  0.6±0.28 h, half-life 27.96±11.66 h, AUC 87.35±10.91 μg·h/mL, bioavailability 83.15%. Note: the
  article's own sampled concentration-vs-time table/figure did not extract as machine-readable
  numbers this session (Figure 1 is graphical only) — the summary statistics above are real and
  quoted directly from the paper's own Table 1, but the full 13-point concentration curve needed
  for the Riemann-sum half of the exercise will need to be either digitized from the published
  figure or reconstructed as a disclosed one-compartment model anchored to these real Cmax/Tmax/
  half-life values, not invented from scratch.
- **Winter EA, Pelligand L, Toutain P-L, Lees P, Milanova A, Gehring R. "Determination of
  pharmacokinetic-pharmacodynamic cutoff values of oxytetracycline in calves and adult cattle
  using population pharmacokinetic modeling." *Frontiers in Microbiology*, 2024;15:1498219,
  doi:10.3389/fmicb.2024.1498219.** Real, current, rigorous cattle-specific PK/PD source studying
  20 mg/kg IM (and 20/40 mg/kg IV) long-acting oxytetracycline: derived PK/PD cutoff values of 1
  mg/L (calves) and 2 mg/L (adult cattle) for a 48-hour dosing interval, and a target
  fAUC24h/MIC ratio of **19.1–28 h** as the pharmacodynamic efficacy bar — this is the real, hard,
  numeric pass/fail gate the case's computed AUC/MIC ratio would be checked against, directly
  analogous to C9's ACI tolerance table or C10's NRCS velocity ceiling.
- **CLSI VET01S** (Performance Standards for Antimicrobial Disk and Dilution Susceptibility Tests
  for Bacteria Isolated from Animals) — the real, named veterinary susceptibility breakpoint for
  oxytetracycline against *Mannheimia haemolytica* (a real bovine-respiratory-disease pathogen) at
  a single 20 mg/kg IM dose: susceptible ≤2 mg/L, resistant ≥8 mg/L — corroborates and gives real
  external grounding to the Winter et al. adult-cattle cutoff above.
- **Liquamycin LA-200 FDA-approved label** (DailyMed, setid d14180ed-329c-464a-a9ac-b7bbf3d59536)
  — a real single product's own approved label offers *both* dosing regimens needed for this
  concept on one real drug: "a single dose of 9 mg of oxytetracycline per lb of body weight" for
  certain conditions, or "3–5 mg of oxytetracycline per lb of body weight per day," continued
  "24–48 hours following remission of disease signs; however, not to exceed a total of 4
  consecutive days" for others. Both regimens on this label carry the same stated pre-slaughter
  withdrawal ("discontinue treatment at least 28 days prior to slaughter of cattle and swine") —
  checked directly against a second real conventional-oxytetracycline DailyMed label
  (setid 2846dab1-4dff-4d8d-ba6c-aa5e8bf394ec), which states the identical 28-day figure. This is
  an honest negative finding, not a gap: withdrawal time is real and verified but turns out **not**
  to be a differentiator between the two options in this case, so the write-up should not invent
  one.
- **Real, previously-published, direct comparative finding**: a 1983 Swedish study (Ericsson &
  Waller-Ekbom-line comparison; PubMed 6869141) directly compared conventional vs. long-acting
  oxytetracycline in cattle and reported "almost identical plasma concentrations... with peak
  values after 6–8 h," concluding the long-acting formulation offered no extended efficacy
  advantage over conventional dosing but caused measurably greater injection-site tissue damage —
  a real, citable, already-published version of exactly this case's core tension (close AUC,
  divergent tissue-damage cost), not a coincidence invented for this concept.
- **Beef Quality Assurance / National Beef Quality Audit injection-site-lesion economics**
  (USU Extension Animal Health Fact Sheet; National Beef Quality Audit 1995 and 2022 editions) —
  real, named, industry-tracked figures: the beef industry has been documented losing roughly
  $7.05 per fed heifer or steer marketed to injection-site lesions (historical industry estimate);
  the 1995 NBQA found 11% of surveyed carcasses had at least one injection-site blemish, while the
  2022 NBQA found 97.1%–99.8% of surveyed cattle had no visible injection-site lesions — real,
  current evidence that technique and formulation choice measurably move this real cost, usable as
  the case's per-event handling/lesion-risk cost layer.

Sources I am NOT confident about and would need to resolve before case-write: (1) a full,
machine-readable concentration-vs-time data table for either Aktaş & Yarsan group (only summary
statistics extracted successfully this session; the full curve will need digitizing from the
published figure or an explicitly disclosed one-compartment reconstruction); (2) a specific,
current per-dose retail price differential between a real long-acting and a real conventional
oxytetracycline product (searches surfaced product listings but no side-by-side current pricing
this session); (3) an FDA Freedom of Information summary PDF (animaldrugsatfda.fda.gov, document
658) that did not parse as readable text this session and was not pursued further given the
strength of the peer-reviewed sources above.

**Sensitivity (SPEC §6).** LOW, not none — this is a livestock/veterinary antimicrobial-dosing
scenario, not a human-patient one, which is the safer register this file's own instructions
flagged as preferable. Keep the write-up in a routine, professional antimicrobial-stewardship
register (protocol compliance, cost, real published efficacy thresholds, real published tissue-
damage/handling-cost data) and do not depict animal suffering, disease progression, or death;
avoid framing that reads as a human-antibiotic-resistance alarmism piece, since the real subject
here is a routine, well-regulated veterinary dosing decision, not a public-health crisis.

**Split risk.** NONE — 7 skills matches the Calculus/Integrals group's full size exactly, and
every skill flows from one real computation (AUC via Riemann sum on sampled data, cross-checked
via antiderivative/FTC on a fitted curve) performed for both dosing options; nothing is bolted on
to inflate the count.

**Rubric re-score (0–5 each).**

| Axis | Before (premise only) | After (researched) | Justification |
|---|---|---|---|
| Skill Fit | 5 | **5** | Held, not inflated: the research pass confirmed rather than merely assumed the fit — Riemann-sum AUC and FTC-on-a-fitted-curve AUC are literally the two real methods pharmacology papers use and cross-check against each other, so all 7 skills are load-bearing on one real computation, not decorative. |
| Narrative Pull | 4.5 | **4** | Moved down slightly: a veterinary consultant's protocol-compliance decision is a genuine professional stake with a real hard efficacy gate behind it, but the register is inherently quieter than a life-or-death or endangered-species premise — closer to C1's bid-vs-competitor register or C10's cost-share-forfeiture register than to a top-tier drama premise. |
| Data Richness | 4.5 | **5** | Moved up: the research pass found more, and better, real sourcing than the preliminary guess assumed — a real cattle-specific 2024 population PK/PD paper with an actual numeric efficacy target (fAUC/MIC 19.1–28 h), a real CLSI breakpoint, a real single product label offering both dosing regimens, and a real 1983 study that already reports this exact tension directly. Held short of a perfect run only because the full digitized concentration-time table (not just summary AUC/Cmax/half-life stats) did not extract this session. |
| Dilemma Tension | 4 | **4.5** | Moved up: the tension turned out to be real and structurally close for a documented reason, not merely assumed to be close — a ~9% AUC gap that masks a >2.6x half-life difference, checked against a real published pass/fail efficacy threshold, plus a real prior study already reporting the same close-AUC/divergent-tissue-damage pattern this concept relies on. Held short of 5 because the exact cumulative-AUC-across-a-multi-dose-course computation for the conventional option still rests on a disclosed one-compartment reconstruction rather than a fully independent second real dataset. |
| **Total** | **18 / 20** | **18.5 / 20** | The preliminary estimate holds up well and is nudged very slightly higher: this is one of the better-sourced concepts in this file, on par with C9 (Advanced Operations/Variables) and stronger than several of the original Precal batch's initial guesses before their own research passes. |

**Recommendation.** Promising, not yet greenlit — this was a research/planning pass only, per this
task's instruction, not a case-write. Before `case-write`: (1) digitize or reconstruct the full
Aktaş & Yarsan concentration-time curve (from the published figure, or as an explicitly disclosed
one-compartment model anchored to the real Cmax/Tmax/half-life values above) so the Riemann-sum
half of the exercise has real per-time-point data to sum, not just summary statistics; (2) decide
and disclose the multi-dose superposition assumption needed to compute cumulative AUC for the
repeated-conventional-dosing option across its up-to-4-day course; (3) if a current real
per-dose price differential cannot be sourced, disclose the cost gap as a Modeling Assumption
rather than an invented figure, consistent with how this file has handled other unpriced real
quantities (e.g., C9, C10).
