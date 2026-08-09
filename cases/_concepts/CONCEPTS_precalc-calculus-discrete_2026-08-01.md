# Concept sheet — Pre-Calculus & Trigonometry, Calculus, Discrete Mathematics

**Run:** `case-brainstorm`, manual run 2026-08-01, **extended same day** on request for more
Calculus / Discrete-Combinatorics / Discrete-Graph-Theory options. **Target:** the three branches
B2 (2026-08-01) gave real standards rows for the first time — all at 0% coverage, 0 pipeline
cases. Twelve concepts total now, each targeting a zero-coverage group per `gap_queue.json`
(regenerated 2026-08-01 — see `DOCTRINE_LEDGER.md`; it was stale since B2 and would have been
blind to all three branches otherwise). **C7–C12 (below) are the second pass** — every one of
them is anchored to a domain's own pre-existing `decision_archetypes[]` in `domains.json` (the
B2-verified real sources), not invented to fit the math, per the user's ask for *better* options,
not just more of them.

**Ranking table — Pre-Calc (unchanged, C1 already confirmed)**

| # | Title | Branch / group | Score | Feasibility |
|---|---|---|---|---|
| C1 | Tide Window | Pre-Calc / Trigonometric Functions | **9.8** | HIGH |
| C2 | Wind Triangle | Pre-Calc / Vectors | 7.4 | HIGH |

**Ranking table — Calculus**

| # | Title | Group | Score | Feasibility | Real archetype it's grounded in |
|---|---|---|---|---|---|
| C3 | The Optimal Can | Applications of Derivatives (+partial Derivatives) | 7.7 | MEDIUM-HIGH | *(invented — no domain archetype behind it)* |
| **C8** | **The Curve's Turn** | Applications of Derivatives (full 7/7) | **7.4** | **HIGH** | `epidemiology`: *"Close schools for two weeks now on a rising curve, or stay open and add testing"* |
| C4 | Total Flow | Integrals (full 7/7) | 7.4 | HIGH | *(invented, but USGS sources are exact-fit)* |
| C7 | The Sunset Ramp | Derivatives (partial 6/9) | 4.4 | HIGH | `energy-grid`: *"Build 200 MW of solar plus 4 hours of battery, or 120 MW of gas peaker, for the same capital"* |

**Ranking table — Discrete / Combinatorics**

| # | Title | Score | Feasibility | Real archetype |
|---|---|---|---|---|
| C6 | The Keyspace Decision | 5.8 | HIGH | `cryptography-security`: *"Force 14-character passwords or 8 characters plus a second factor"* |
| **C9** | **Redrawing the Lines** | **5.8** | **HIGH** | `elections-apportionment`: *"Draw the map for compactness or for keeping a county whole, when you cannot have both"* |
| C10 | Pattern Rights | 3.5 | MEDIUM | `tiling-pattern-art`: *"Design the repeat as a straight grid or a half-drop, given the fabric width and the visible seam"* |

**Ranking table — Discrete / Graph Theory**

| # | Title | Score | Feasibility | Real archetype |
|---|---|---|---|---|
| C5 | Six Degrees of Exposure | 3.4 | HIGH, needs SPEC §6 | *(invented — no domain archetype)* |
| **C12** | **Reroute or Wait** | **3.4** | **HIGH** | `transit-routing`: *"Reroute around the closure with 6 extra minutes for everyone, or split the line and force a transfer"* |
| C11 | The One-Pass Route | 2.8 | HIGH | *(a real, well-known applied-math problem — "route inspection" — not from a specific decision_archetype)* |

**Recommendation, updated.**

- **Pre-Calc: C1 stands, unchanged.** Still the best concept on this whole sheet.
- **Calculus: write C8 (The Curve's Turn), not C3.** They're 0.3 points apart, which is inside the
  noise of a hand-graded feasibility factor — the real difference is that C8's every source is
  HIGH/LIVE with nothing to hedge, while C3's honest weak point (a specific plant's retooling
  cost) is exactly the kind of gap that becomes a `{{NEEDS_SOURCE}}` → `NOT FOUND` → Modeling
  Assumption chain in `case-research`. C8 also comes with its dilemma already sitting in
  `epidemiology`'s own `decision_archetypes[]`, same tell that made C1 strong. Keep C3 and C4 on
  the bench, not killed — C4 (Total Flow) is a genuinely clean second case for this branch later.
- **Discrete/Combinatorics: C9 over C6.** Same score, but C9's Pigeonhole Principle use is a real
  *proof*, not a flavor word — "some district's population must be imbalanced, provably, given
  the seat count" is a stronger, more surprising hook than a keyspace calculation, and it doesn't
  require the reader to already find cybersecurity jargon interesting to get in the door. C6 stays
  a strong second option.
- **Discrete/Graph Theory: run C12 and C11 as a pair, kill C5.** Together they close the *entire*
  8-skill group with zero overlap (C12: vertices/edges/weighted-graph/shortest-path; C11:
  path/cycle/Euler), both are HIGH feasibility with live GTFS/Census data, and neither needs a
  SPEC §6 sensitivity note — a real, meaningful advantage over C5 for a *second* pipeline case,
  where you'd rather prove the shell works before taking on an extra doctrine obligation.

**Standing tension, said plainly:** `ROADMAP.md` Track A is explicit — *"do not author case #2
until Cold Chain is `VERIFIED`."* Cold Chain is not `VERIFIED` (still `TIER1_PASS`; see
`DOCTRINE_LEDGER.md`'s 2026-08-01 entries). Brainstorming is safe against that rule — nothing here
writes to `cases/<id>/`, only to this file, exactly as `case-brainstorm`'s own "Never" list
requires. **Actually running `case-write` on any of these is a different decision** and would mean
consciously setting aside the depth-before-breadth rule, not an oversight. Flagging it here so it's
a decision, not a drift.

---

### C1 — Tide Window · score 9.8 · tier Advanced
**Protagonist.** A harbour pilot at a mid-size container port, personally liable for a grounding
if she clears a loaded ship on a tide that doesn't hold.
**The dilemma.** A.) Sail the loaded ship at 04:00 on the marginal low tide, making the contracted
delivery window OR B.) Hold in port for the spring tide 11 hours later, missing the window and
triggering a late-delivery penalty.
**Primary metric.** Under-keel clearance margin (feet) per hour of schedule risk accepted.
**Why it's close.** Modeling the tide as a sinusoid from the station's real harmonic constituents
shows the 04:00 tide clears the ship's draft by a real but thin margin under normal barometric
conditions — thin enough that a modest storm-surge/pressure adjustment (itself real, sourceable
data) could erase it entirely. Waiting is unambiguously safe but the penalty is real money on a
fixed contract. Neither option is free; the case turns on how much margin is "enough."
**Would close (11 skills, 3 how-to / 8 term):**
| id | kind | label |
|---|---|---|
| pre-calculus-how-to-convert-between-degrees-and-radians | how-to | How to convert between degrees and radians |
| pre-calculus-how-to-find-the-sine-cosine-and-tangent-of-an-angle-using-the-unit-circle | how-to | How to find the sine, cosine, and tangent of an angle using the unit circle |
| pre-calculus-how-to-find-the-amplitude-and-period-of-a-sine-or-cosine-function | how-to | How to find the amplitude and period of a sine or cosine function |
| pre-calculus-radian | term | Radian |
| pre-calculus-unit-circle | term | Unit Circle |
| pre-calculus-sine-function | term | Sine Function |
| pre-calculus-cosine-function | term | Cosine Function |
| pre-calculus-tangent-function | term | Tangent Function |
| pre-calculus-amplitude | term | Amplitude |
| pre-calculus-period-of-a-function | term | Period (Of A Function) |
| pre-calculus-reference-angle | term | Reference Angle |
**Already-covered skills it also exercises.** Likely `measurement-how-to-convert-an-amount-with-compound-units`, `measurement-how-to-find-elapsed-time` (already `n>0` from legacy cases) — the case naturally needs both.
**Data feasibility: HIGH.** Named sources: NOAA Tides & Currents (`tidesandcurrents.noaa.gov`) — published harmonic constituents and 6-minute observed/predicted water levels per station, live, free; NOAA National Data Buoy Center (`ndbc.noaa.gov`) — real-time wave/wind conditions for the storm-surge complication. Both already verified LIVE in `domains.json`'s `oceanography` entry (B2 domain-linking pass, 2026-08-01). Not confident about: a specific vessel's real draft/dimensions for a *named* ship (use a published vessel class spec sheet, or state the draft as a Modeling Assumption) — not confident about the exact contract-penalty dollar figure, which should be a stated assumption too.
**Sensitivity (SPEC §6).** NONE — commercial/logistics stakes only.
**Split risk.** NONE — 11 skills is within the normal 8–15 range for one case, and all 11 are the entire target group.

---

### C2 — Wind Triangle · score 7.4 · tier Advanced
**Protagonist.** An airline dispatcher who signs the fuel release and is accountable if a flight
lands with less reserve than planned.
**The dilemma.** A.) File the shorter, direct great-circle route, which runs into a quartering
headwind OR B.) File a longer dogleg route that rides a known tailwind corridor.
**Primary metric.** Fuel burned per nautical mile of net progress toward the destination (not per
mile flown — the wind vector changes what "progress" costs).
**Why it's close.** Resolving true airspeed and wind into a ground-track vector is the actual
tool dispatchers use, and it produces the classic counterintuitive result: the "shorter" route's
headwind component can cost more net fuel than the "longer" route's tailwind assist. The real
margin depends on the day's actual wind vector, which is public, live data, not invented.
**Would close (7 skills, 3 how-to / 4 term):**
| id | kind | label |
|---|---|---|
| pre-calculus-how-to-find-the-magnitude-and-direction-of-a-vector | how-to | How to find the magnitude and direction of a vector |
| pre-calculus-how-to-add-and-subtract-vectors | how-to | How to add and subtract vectors |
| pre-calculus-how-to-find-the-dot-product-of-two-vectors | how-to | How to find the dot product of two vectors |
| pre-calculus-vector | term | Vector |
| pre-calculus-magnitude-of-a-vector | term | Magnitude (Of A Vector) |
| pre-calculus-unit-vector | term | Unit Vector |
| pre-calculus-dot-product | term | Dot Product |
**Data feasibility: HIGH.** Named sources: Aviation Weather Center (`aviationweather.gov`) — live METARs, TAFs, winds-aloft forecasts, the actual planning inputs dispatchers use; OpenSky Network (`opensky-network.org`) — historical/live ADS-B tracks to source a real route's distance and heading. Both LIVE-verified in `domains.json`'s `aviation` entry. Not confident about: a specific charter operator's actual contracted fuel price (state as an assumption) — published aircraft-type fuel-flow figures exist (manufacturer data / ICAO databank) but assembling the exact burn-rate curve for a named aircraft is MEDIUM effort, not a single document.
**Sensitivity (SPEC §6).** NONE.
**Split risk.** NONE.

---

### C3 — The Optimal Can · score 7.7 · tier Advanced
**Protagonist.** A packaging/process engineer at a beverage canner, who owns the material-cost
line item and would have to justify a retooling request to plant leadership.
**The dilemma.** A.) Keep the industry-standard can proportions — fits the existing filling-line
tooling exactly, zero retooling cost OR B.) Switch to the calculus-derived optimal proportions
that use the least aluminum per fluid ounce, which cuts material cost per can but requires a real
capital retooling spend.
**Primary metric.** Dollars saved per year in material cost, net of retooling cost — i.e. payback
period in months at current annual production volume.
**Why it's close.** The true optimum (found by differentiating surface area as a function of
radius at fixed volume, setting the derivative to zero, and confirming a minimum with the first
derivative test) uses meaningfully less aluminum per unit volume than the real standard can, whose
actual proportions are constrained by ergonomics and shelf-stacking, not pure optimization — so
option B looks obviously better on material cost alone, until the retooling cost and the plant's
real annual volume are weighed against how many months of savings it actually takes to pay that
back.
**Would close (7 skills, 3 how-to / 4 term) — the full Applications Of Derivatives group:**
| id | kind | label |
|---|---|---|
| calculus-how-to-find-critical-points-of-a-function | how-to | How to find critical points of a function |
| calculus-how-to-use-the-first-derivative-test-to-classify-a-critical-point | how-to | How to use the first derivative test to classify a critical point |
| calculus-how-to-solve-an-optimization-problem-using-derivatives | how-to | How to solve an optimization problem using derivatives |
| calculus-critical-point | term | Critical Point |
| calculus-local-maximum | term | Local Maximum |
| calculus-local-minimum | term | Local Minimum |
| calculus-concavity | term | Concavity |
**Partial credit, not claimed as fully closed — flagged, not fabricated.** Differentiating the
surface-area function naturally also forces `calculus-derivative`, `calculus-instantaneous-rate-of-change`,
and `calculus-how-to-find-a-derivative-using-the-power-rule` (3 of 9 Derivatives-group skills) —
these are real and should be listed in `new_coverage[]` if `case-write` confirms the deliverable
actually forces them. The other 6 Derivatives-group skills (chain/product/quotient rule,
tangent-line, differentiable) are NOT forced by a single polynomial optimization and must not be
claimed — they need a case with a genuinely composite or product function, which is a real gap
this concept sheet is not closing and should be a separate future target.
**Data feasibility: MEDIUM-HIGH.** Standard can dimensions and material specifications are
well-published in beverage-packaging industry sources (can manufacturers' public technical
literature); aluminum commodity pricing is real, live public market data (LME/COMEX aluminum
price). Not confident about: a specific plant's actual retooling cost — this is genuinely LOW
confidence and should be a stated Modeling Assumption, explicitly flagged as such, not sourced.
**Sensitivity (SPEC §6).** NONE.
**Split risk.** NONE (7 skills fully claimed + 3 flagged-partial, well inside the normal range).

---

### C4 — Total Flow · score 7.4 · tier Advanced
**Protagonist.** A flood-control engineer at a river district, who signs off on levee capacity
ahead of storm season.
**The dilemma.** A.) Reinforce the levee for the modeled 100-year peak flow *rate* alone OR B.)
Reinforce for the modeled total flood *volume* over the full storm duration — the integral of flow
rate over time — which can matter more for how long the levee actually has to hold.
**Primary metric.** Cubic feet of floodwater safely managed per dollar of reinforcement spent.
**Why it's close.** A storm with a lower peak rate but a much longer duration can deliver more
total volume than a sharper, shorter storm with a higher peak — real historical gauge data shows
both storm shapes occur on the same river. Designing to the peak alone (cheaper, faster to
justify) can under-protect against the slow, high-volume event; designing to total volume
(costlier) may over-build for the sharp, short event. Real hydrographs from the same station make
both arguments concrete, not hypothetical.
**Would close (7 skills, 3 how-to / 4 term) — the full Integrals group:**
| id | kind | label |
|---|---|---|
| calculus-how-to-find-an-antiderivative-using-the-power-rule | how-to | How to find an antiderivative using the power rule |
| calculus-how-to-evaluate-a-definite-integral-using-the-fundamental-theorem-of-calculus | how-to | How to evaluate a definite integral using the Fundamental Theorem of Calculus |
| calculus-how-to-approximate-area-under-a-curve-using-a-riemann-sum | how-to | How to approximate area under a curve using a Riemann sum |
| calculus-antiderivative | term | Antiderivative |
| calculus-definite-integral | term | Definite Integral |
| calculus-indefinite-integral | term | Indefinite Integral |
| calculus-riemann-sum | term | Riemann Sum |
**Data feasibility: HIGH.** Named source: USGS National Water Information System / real-time
streamflow data (`waterdata.usgs.gov`) — actual historical discharge (flow-rate) time series for
named gauge stations, free, public, exactly the shape (rate vs. time) this case needs to integrate.
Not confident about: the specific dollar cost of a given reinforcement spec for a named levee —
state as an assumption grounded in a published unit-cost figure if one exists (e.g. Army Corps of
Engineers cost-estimating guidance), otherwise flag as LOW.
**Sensitivity (SPEC §6).** Borderline — flooding can touch property/safety stakes. Recommend a
one-line facilitator note per SPEC §6 even though the case's own math stays in "protection"
framing (capacity managed, not damage inflicted).
**Split risk.** NONE.

---

### C5 — Six Degrees of Exposure · score 3.4 · tier T3/Advanced
**Protagonist.** A county public-health epidemiologist leading a contact-tracing response.
**The dilemma.** A.) Vaccinate the 50 highest-degree (most-connected) individuals identified from
contact-tracing data OR B.) Vaccinate 500 people chosen at random from the same population, same
total dose budget.
**Primary metric.** Modeled transmission edges eliminated per dose spent.
**Why it's close.** On a real, skewed contact network, targeting hubs removes a disproportionate
share of the graph's total connectivity per dose — a strong case for A. But hub identification
depends on contact-tracing data that is slower and costlier to collect and can miss an emerging
cluster that broad random coverage would still catch — a real case for B. The actual payoff
depends on the real network's degree distribution, not a story.
**Would close (5 of 8 skills, 1 how-to / 4 term — does NOT claim the full group):**
| id | kind | label |
|---|---|---|
| discrete-mathematics-how-to-find-the-shortest-path-between-two-vertices-in-a-weighted-graph | how-to | How to find the shortest path between two vertices in a weighted graph |
| discrete-mathematics-graph-vertices-and-edges | term | Graph (Vertices And Edges) |
| discrete-mathematics-vertex | term | Vertex |
| discrete-mathematics-edge | term | Edge |
| discrete-mathematics-weighted-graph | term | Weighted Graph |
**Data feasibility: HIGH.** Named source: Stanford SNAP datasets (`snap.stanford.edu/data`) — real
social/contact-structure graphs as edge lists, free, built for exactly this kind of classroom use.
**Sensitivity (SPEC §6): YES.** Touches disease and vaccination directly. Needs a facilitator
sensitivity note. The framing is already protection-oriented (doses/immunity, not casualties),
consistent with SPEC §6 guidance, but the note is still required.
**Split risk.** Deliberately partial — `path`, `cycle`, and
`discrete-mathematics-how-to-determine-whether-a-graph-has-an-euler-path-or-circuit` are real,
separate Graph Theory skills better forced by a route-inspection case (e.g. "can this crew cover
every street with no repeats," a genuine Euler-circuit question over real Census TIGER/Line
road-centerline data) — not manufactured into this one to inflate the count.

---

### C6 — The Keyspace Decision · score 5.8 · tier T3/Advanced
**Protagonist.** A security operations analyst setting password policy for a mid-size company,
personally on the hook when the next audit finds a weak default.
**The dilemma.** A.) Mandate 14-character passwords with no second factor OR B.) Allow 8-character
passwords but require a second authentication factor (2FA) for every account.
**Primary metric.** Expected time-to-crack (years) per dollar of implementation and support cost.
**Why it's close.** Pure keyspace math (character-set size raised to the password length, via the
Fundamental Counting Principle) makes a 14-character password brute-force-infeasible on its own —
a strong argument for A. But real breach data shows most account compromises come from credential
theft and phishing, not brute force, and 2FA defeats those regardless of password length — while
2FA carries real, ongoing support cost and adoption friction a security budget has to weigh
honestly against A's near-zero marginal cost.
**Would close (5 skills, 2 how-to / 3 term) — the full Combinatorics group:**
| id | kind | label |
|---|---|---|
| discrete-mathematics-how-to-apply-the-fundamental-counting-principle-to-count-outcomes | how-to | How to apply the Fundamental Counting Principle to count outcomes |
| discrete-mathematics-how-to-compute-a-binomial-coefficient | how-to | How to compute a binomial coefficient |
| discrete-mathematics-fundamental-counting-principle | term | Fundamental Counting Principle |
| discrete-mathematics-binomial-coefficient | term | Binomial Coefficient |
| discrete-mathematics-pigeonhole-principle | term | Pigeonhole Principle |
**Data feasibility: HIGH.** Named sources: Have I Been Pwned (`haveibeenpwned.com`) — real breach
sizes and dates, live; CISA Known Exploited Vulnerabilities catalog and NIST National
Vulnerability Database — real, live severity/exploitability data on how breaches actually happen
(supports the "brute force isn't the real threat" argument). MEDIUM on the exact password-cracking
rate figure (published security-research benchmarks exist but assembling one specific, current,
citable number needs `case-research` to actually run the check, not assumed here).
**Sensitivity (SPEC §6).** NONE.
**Split risk.** NONE.

---

## Threshold — calibrated against Cold Chain, not an abstract number (2026-08-01)

Asked whether scores can go higher: **mostly no, without violating this project's own
anti-inflation rule.** C1 (9.8) is already at its group's ceiling — Trigonometric Functions has
exactly 11 skills, so 9.8 is the maximum any concept touching only that group can score at HIGH
feasibility. C9/C6/C10 (Combinatorics, 5 skills total) and C11/C12 (each half of an 8-skill Graph
Theory) are capped by how many atomic skills exist in those spine groups — a fact about B2's
authoring, not about these concepts. Claiming skills a case doesn't genuinely force to push a
score higher is exactly the "coverage-inflation" `case-brainstorm`'s own doctrine exists to catch
(now written into `skills/case-brainstorm/SKILL.md`'s ranking section as a permanent calibration
note, not just noted here for this run).

**So: a threshold, calibrated against the one real case that's shipped.** Recomputed under this
same formula, **Cold Chain itself scores 4.2** (raw 2.2 + a 2.0 group bonus, `HIGH` feasibility) —
lower than most of this sheet. Using Cold Chain's own score as the bar:

| Clears 4.2 | Falls short | 
|---|---|
| C1 (9.8), C3 (7.7), C2/C4/C8 (7.4), C6/C9 (5.8), C7 (4.4) | C5 (3.4), C12 (3.4), C10 (3.5), C11 (2.8) |

**C11 + C12 as a pair clear it easily (2.8 + 3.4 = 6.2)** — they were deliberately designed as a
non-overlapping split of one 8-skill group specifically so neither over-claims; evaluate them
together, not each alone, same as the calibration note now says. **C5 and C10 do not have that
excuse** — C5 is a genuine partial (5/8, no pairing partner proposed) carrying an extra SPEC §6
obligation for no score benefit, and C10 is a real alternative to C9 at lower feasibility (MEDIUM,
not HIGH) with no size excuse either. **Recommend dropping C5 and C10 from the active list**; keep
C10 noted as a bench option only if a future cohort's interest in the visual/craft angle (SPEC
Track F5) outweighs the feasibility gap.

---

## Second pass — 2026-08-01, more/better options requested

Every concept below is grounded in a `decision_archetypes[]` line already sitting in
`domains.json` (written during B2's domain-linking pass, sources fetched and confirmed then) —
the binary and the tension are the domain's own, not built to order.

### C8 — The Curve's Turn · score 7.4 · tier Advanced
**Protagonist.** A county public-health director deciding whether to close schools during a
rising respiratory-illness season.
**The dilemma.** A.) Close schools for two weeks now, while case counts are still low but climbing
faster each day OR B.) Stay open, add on-site rapid testing, and only close if raw case counts
cross a fixed threshold.
**Primary metric.** School-days lost per case of in-school transmission prevented.
**Why it's close.** Option A reacts to *concavity* — the point where the case-count curve's growth
rate itself starts increasing (an inflection point), which gives the earliest possible warning but
is genuinely hard to read cleanly from noisy real daily data and risks a costly false alarm.
Option B reacts to a raw level, which is unambiguous to read but is structurally always later,
since a threshold-crossing happens strictly after the curve has already turned. Real daily case
series are noisy enough that "has it actually turned yet" is a real, defensible judgment call, not
a formality.
**Would close (7 skills, 3 how-to / 4 term) — the full Applications Of Derivatives group:**
| id | kind | label |
|---|---|---|
| calculus-how-to-find-critical-points-of-a-function | how-to | How to find critical points of a function |
| calculus-how-to-use-the-first-derivative-test-to-classify-a-critical-point | how-to | How to use the first derivative test to classify a critical point |
| calculus-how-to-solve-an-optimization-problem-using-derivatives | how-to | How to solve an optimization problem using derivatives |
| calculus-critical-point | term | Critical Point |
| calculus-local-maximum | term | Local Maximum |
| calculus-local-minimum | term | Local Minimum |
| calculus-concavity | term | Concavity |
**Data feasibility: HIGH.** Named sources, all LIVE per `domains.json`'s `epidemiology` entry:
CDC WONDER (`wonder.cdc.gov`, queryable US disease counts by county/age), Our World in Data
(`ourworldindata.org`, downloadable CSV behind every chart), NYT COVID-19 data archive
(`github.com/nytimes/covid-19-data`, daily US county case series — archived but complete and
exactly the shape this case needs: a real, noisy, close-to-real-time daily count series to test
concavity against). Not confident about: the actual per-school-day economic/instructional cost
figure used to weigh against transmission avoided — state as a Modeling Assumption.
**Sensitivity (SPEC §6).** YES — respiratory illness and school closure. Needs a facilitator
sensitivity note. Framing stays administrative/civic (school-days vs. transmission), not personal
tragedy — closer to Cold Chain's own "protection" framing than to a triage decision.
**Split risk.** NONE.

### C7 — The Sunset Ramp · score 4.4 · tier Advanced
**Protagonist.** A grid operations engineer (Balancing Authority Dispatcher) deciding what to
build for tomorrow evening's demand ramp, not just today's average load.
**The dilemma.** A.) Build 200 MW of solar plus 4 hours of battery storage OR B.) Build 120 MW of
a natural-gas peaker plant — both for the same capital budget.
**Primary metric.** Dollars of capital cost per MW/minute of ramp rate covered (how fast the
resource can respond to the evening drop in solar output as the sun sets).
**Why it's close.** The battery can respond instantly to any ramp rate but only for 4 hours total;
the gas peaker has a real, slower minimum start-up ramp but can run all night. Real hourly
generation-by-fuel data lets a student compute the *actual* measured ramp rate (the derivative of
the generation curve) during a real evening solar decline and check which resource's response
capability actually covers it, rather than assuming either "obviously" wins.
**Would close (6 of 9 skills, 2 how-to / 4 term) — does NOT claim the full Derivatives group:**
| id | kind | label |
|---|---|---|
| calculus-how-to-find-a-derivative-using-the-power-rule | how-to | How to find a derivative using the power rule |
| calculus-how-to-find-the-equation-of-a-tangent-line-at-a-point | how-to | How to find the equation of a tangent line at a point |
| calculus-derivative | term | Derivative |
| calculus-instantaneous-rate-of-change | term | Instantaneous Rate Of Change |
| calculus-tangent-line | term | Tangent Line |
| calculus-differentiable | term | Differentiable |
**Data feasibility: HIGH.** Named sources, all LIVE per `domains.json`'s `energy-grid` entry: EIA
Hourly Electric Grid Monitor (`eia.gov/electricity/gridmonitor`, real hourly demand and
generation-by-fuel per balancing authority — exactly the discrete data points a student would
difference to estimate the derivative), EIA Open Data API (generation/capacity/price series, free,
keyed). Not confident about: a specific battery or peaker unit's real installed cost per MW —
use a published EIA capital-cost outlook figure if one exists, else flag as an assumption.
**Sensitivity (SPEC §6).** NONE.
**Split risk.** Deliberately partial — chain/product/quotient rule (3 skills) are not naturally
forced by this design and are NOT claimed. A version of this case that models demand as a real
product of a baseline-trend function and a separate weather-multiplier function would genuinely
force the product rule and could close the full group — noted here as a real design option for
whoever writes this, not claimed as done.

### C9 — Redrawing the Lines · score 5.8 · tier Advanced
**Protagonist.** A state redistricting commission analyst, publicly accountable for the map she
recommends.
**The dilemma.** A.) Draw district boundaries to maximize compactness (a defensible, formula-based
standard) OR B.) Draw them to keep every county whole (a defensible, community-standard
principle) — for a real state where the two principles are shown to conflict on at least one
county.
**Primary metric.** Number of "acceptable" district maps under each standard, out of the total
maps that satisfy the hard legal constraints (equal population within a tolerance, contiguity).
**Why it's close.** Counting the maps that satisfy each standard (via the Fundamental Counting
Principle applied to how precincts can be grouped, at a simplified/bounded scale a class can
actually enumerate) shows both standards are real, defensible, and — this is the point —
genuinely incompatible for specific real counties. The Pigeonhole Principle gives a second,
sharper argument: given a real state's total population and seat count, it's provable that *some*
district's population must land above or below the average, regardless of which standard is used.
**Would close (5 skills, 2 how-to / 3 term) — the full Combinatorics group:**
| id | kind | label |
|---|---|---|
| discrete-mathematics-how-to-apply-the-fundamental-counting-principle-to-count-outcomes | how-to | How to apply the Fundamental Counting Principle to count outcomes |
| discrete-mathematics-how-to-compute-a-binomial-coefficient | how-to | How to compute a binomial coefficient |
| discrete-mathematics-fundamental-counting-principle | term | Fundamental Counting Principle |
| discrete-mathematics-binomial-coefficient | term | Binomial Coefficient |
| discrete-mathematics-pigeonhole-principle | term | Pigeonhole Principle |
**Data feasibility: HIGH.** Named sources, all LIVE per `domains.json`'s `elections-apportionment`
entry: Census congressional apportionment (`census.gov/topics/public-sector/congressional-apportionment.html`,
official populations and seat allocations, every decade), MIT Election Data & Science Lab
(`electionlab.mit.edu/data`, precinct/county/state returns, cleaned), Dave's Redistricting
(`davesredistricting.org`, draws a map and computes compactness live — a real tool a student could
actually use to test option A). Redistricting Data Hub requires free signup (`LIVE_LOGIN`, not a
blocker but worth knowing going in.
**Sensitivity (SPEC §6).** NONE — this is a real civic-math case, not framed around a specific
election outcome or party.
**Split risk.** NONE.

### C10 — Pattern Rights · score 3.5 · tier Advanced
**Protagonist.** A surface-pattern designer licensing a repeat pattern to a fabric manufacturer.
**The dilemma.** A.) License the pattern as a straight-grid repeat (cheaper to print, more visible
seam) OR B.) License it as a half-drop repeat (better seam concealment, costs more per yard to
set up on the printer).
**Primary metric.** Printed yards producible per dollar of setup cost, at the manufacturer's real
fabric width.
**Why it's close.** The number of *distinct* ways a given motif can validly repeat under each
scheme (counted via the Fundamental Counting Principle over the pattern's rotational/reflective
symmetries — there are only 17 wallpaper groups in total, a genuinely surprising real constraint)
determines how much design flexibility the designer keeps under each option, while the
manufacturer's real fabric width and setup cost determine which is cheaper to print at scale.
**Would close (5 skills, 2 how-to / 3 term) — the full Combinatorics group (alternative to C9):**
| id | kind | label |
|---|---|---|
| discrete-mathematics-how-to-apply-the-fundamental-counting-principle-to-count-outcomes | how-to | How to apply the Fundamental Counting Principle to count outcomes |
| discrete-mathematics-how-to-compute-a-binomial-coefficient | how-to | How to compute a binomial coefficient |
| discrete-mathematics-fundamental-counting-principle | term | Fundamental Counting Principle |
| discrete-mathematics-binomial-coefficient | term | Binomial Coefficient |
| discrete-mathematics-pigeonhole-principle | term | Pigeonhole Principle |
**Data feasibility: MEDIUM.** Matches `domains.json`'s own grade for `tiling-pattern-art`
(MEDIUM, not HIGH), even though it has real named sources: Tiling Search MIT
(`tilingsearch.mit.edu`, searchable, measurable Islamic geometric patterns), Tilings Encyclopedia
Bielefeld, The Met Collection and Rijksstudio (open-access, high-resolution decorative-art images
with dimensions). The honest gap: measuring precise repeat geometry from a museum image is real
extra work compared to a clean queryable API, and no source here publishes real fabric-printing
setup-cost figures — that stays a Modeling Assumption.
**Sensitivity (SPEC §6).** NONE.
**Split risk.** NONE, but scores lower than C9 on feasibility alone — present as the backup, not
the pick, unless the visual/craft angle is judged more engaging for a specific cohort (SPEC
Track F's own F5 explicitly flags "the surprising ones" — tiling is named there directly).

### C11 — The One-Pass Route · score 2.8 · tier Advanced
**Protagonist.** A public-works route supervisor (street sweeping or residential trash
collection) trying to cut fuel cost without dropping a street.
**The dilemma.** A.) Route the crew as a single unbroken pass with no street driven twice — only
possible if the neighborhood's street graph has an Euler circuit OR B.) Accept a route with a
specific, calculated number of repeated street segments, because the real graph doesn't have one.
**Primary metric.** "Deadhead" ratio — miles driven per mile of street actually serviced.
**Why it's close.** This is a genuine yes/no math question with a real, checkable answer: does
every intersection (vertex) in the real neighborhood have even degree? If even one has odd
degree, Euler's theorem says a true single-pass route is mathematically impossible, not just hard
to find — the crew must either accept a specific minimum amount of repeated driving (computable)
or the city must pay to add a road connection that would fix the parity. Real street-network data
makes the vertex-degree count a real exercise, not a toy graph.
**Would close (4 of 8 skills, 1 how-to / 3 term) — pairs with C12 to close the full group:**
| id | kind | label |
|---|---|---|
| discrete-mathematics-how-to-determine-whether-a-graph-has-an-euler-path-or-circuit | how-to | How to determine whether a graph has an Euler path or circuit |
| discrete-mathematics-vertex | term | Vertex |
| discrete-mathematics-path | term | Path |
| discrete-mathematics-cycle | term | Cycle |
**Data feasibility: HIGH.** Named source: Census TIGER/Line road-centerline shapefiles
(`census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html`), already
LIVE-verified elsewhere in `domains.json` (`surveying-geodesy`) — free, real street-network
geometry for any US neighborhood, exactly what's needed to build a real vertex-degree table.
**Sensitivity (SPEC §6).** NONE.
**Split risk.** Deliberately partial by design — see C12; together they close all 8 Graph Theory
skills with no overlap.

### C12 — Reroute or Wait · score 3.4 · tier Advanced
**Protagonist.** A transit service planner deciding how to handle a scheduled multi-week track
closure.
**The dilemma.** A.) Reroute every train around the closure, adding 6 minutes to every rider's
trip, on every run, for the closure's duration OR B.) Split the line at the closure and force
every rider crossing it to transfer, keeping each half's trip time unchanged.
**Primary metric.** Total added rider-minutes across the whole system per day, computed from the
real route graph's shortest paths under each option.
**Why it's close.** Option A is a flat, predictable cost applied to every single rider on the
line. Option B adds a real transfer penalty (wait time at the split point) only to riders whose
shortest path actually crosses the closure — cheaper for riders who don't cross it, more
expensive for the ones who do, and the actual comparison depends on real ridership distribution
across the network's real shortest paths, not a guess.
**Would close (4 of 8 skills, 1 how-to / 3 term) — pairs with C11 to close the full group:**
| id | kind | label |
|---|---|---|
| discrete-mathematics-how-to-find-the-shortest-path-between-two-vertices-in-a-weighted-graph | how-to | How to find the shortest path between two vertices in a weighted graph |
| discrete-mathematics-graph-vertices-and-edges | term | Graph (Vertices And Edges) |
| discrete-mathematics-edge | term | Edge |
| discrete-mathematics-weighted-graph | term | Weighted Graph |
**Data feasibility: HIGH.** Named sources, all LIVE per `domains.json`'s `transit-routing` entry:
Transitland (`transit.land`, real GTFS feeds — stops, times, shapes — for thousands of real
agencies), the GTFS specification itself (`gtfs.org`, makes a raw feed readable by a student),
OpenStreetMap (the real road/rail graph with realistic travel times). This is literally the
domain's own decision archetype, verbatim.
**Sensitivity (SPEC §6).** NONE.
**Split risk.** Deliberately partial by design — see C11.
