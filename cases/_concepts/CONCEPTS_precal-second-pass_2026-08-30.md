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
