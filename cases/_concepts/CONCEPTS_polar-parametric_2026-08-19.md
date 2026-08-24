# Concepts — Pre-Calculus / Polar And Parametric (2026-08-19)

**STATUS 2026-08-22: CLOSED.** C1 (Feedback) was written and shipped as `cases/feedback/`
(TIER2_PASS). The full 6/6-skill target group is now `n=1` in `standards_spine.json`. The
runner-ups below (C2–C4) are obsolete — the group has zero remaining coverage to close. Kept
only as a historical record; nothing here should be written.

**Target.** `Pre-Calculus / Polar And Parametric` — 6/6 skills at `n == 0` (a total hole, and the
entire group closes with one well-built case): `Polar Coordinate`, `Parametric Equation`,
`Parameter` (terms); `How to convert a point between rectangular and polar coordinates`,
`How to graph a polar equation`, `How to eliminate the parameter to find a rectangular equation`
(how-tos). Pulled from `readmodel/gap_queue.json` and confirmed against `standards_spine.json` —
all six ids resolve, all six sit at `n=0`.

Every concept below claims exactly this same 6-skill set (3 how-to × 1.0 + 3 term × 0.6 = raw
4.8, +2.0 full-group bonus = **6.8 before the availability factor** — the ceiling for this group,
since it only has 6 skills total). The differentiator between concepts is therefore **entirely
data feasibility and how honestly each protagonist is forced to use both halves of the group** —
a polar *equation* (not just a polar *point*) and a parametric *equation of motion* that
genuinely needs the parameter eliminated, not just plugged in.

| # | Title | Score | Feasibility | Tier |
|---|---|---|---|---|
| **C1** | **Feedback** | **6.8 × HIGH = 6.8** | **HIGH** | **T4** |
| C2 | Drift Line | 6.8 × MEDIUM = 4.08 | MEDIUM | T4 |
| C3 | Night Signal | 6.8 × MEDIUM = 4.08 | MEDIUM | T4 |
| C4 | Full Circle | 6.8 × MEDIUM = 4.08 | MEDIUM | T3 |

**Recommendation: C1 — Feedback.** It is the only concept where the load-bearing polar curve is
backed by a named, checkable manufacturer document (a real cardioid microphone's published polar
pattern chart) rather than an idealized textbook shape assumed to represent a messier real
phenomenon (radar antenna gain, AM directional-antenna interference contours, an irrigation
head's spray arc). It is also the only one where the parametric half — a performer's blocking
path — is a plain, defensible constant-velocity motion with no radar/atmospheric modeling baggage,
so "eliminate the parameter" produces a clean, gradable rectangular line every time. C4 was
killed for being mathematically too easy (a Ferris-wheel-style circular parametrization
eliminates to a trivial `x²+y²=r²`, which teaches the mechanics but not genuine two-variable
tension) and for lacking a real binary stake. C2 and C3 are both real, both HS-appropriate, and
both worth a future pass if a source hunt turns up better primary data than what's named below —
but neither clears C1 on feasibility today.

---

### C1 — Feedback   ·   score 6.8   ·   tier T4
**Protagonist.** Priya Nakamura, the front-of-house sound engineer for a 300-seat community
theater's touring production. She owns tonight's mix and answers to the house manager if the
show gets shut down for feedback squeal mid-number.
**The dilemma.** A.) Run the lead vocal on the wedge monitor at House-Left (the position the
house crew has used for years) OR B.) Run it on the wedge monitor at House-Right (open tonight
because a second amp channel just failed, forcing a single-wedge choice for the whole show)
**Primary metric.** Gain-before-feedback (dB) at the worst point of the lead's blocking, per
monitor position — the standard live-sound metric combining the microphone's directional
(polar) pattern attenuation at the monitor's angle with the inverse-square-law effect of
monitor-to-mic distance.
**Why it's close.** House-Left is closer to the mic's rear null (better polar rejection, worse
raw distance); House-Right is farther from the null (worse polar rejection, better raw distance).
Neither factor dominates on its own — that is exactly the point of combining a polar-pattern
gain-loss term with a distance-loss term into one dB metric. The lead also isn't static: a
choreographed cross during the bridge moves her along a known straight-line path at
roughly constant speed, and the worst-case angle/distance to each monitor occurs at different,
non-obvious points along that path for A vs. B — found by writing the path as parametric
equations of *t* and eliminating the parameter to get the line she actually walks, then finding
each monitor's closest approach to that line.
**Would close (6 skills, 3 how-to / 3 term):**
| id | kind | label |
|---|---|---|
| pre-calculus-polar-coordinate | term | Polar Coordinate |
| pre-calculus-parametric-equation | term | Parametric Equation |
| pre-calculus-parameter | term | Parameter |
| pre-calculus-how-to-convert-a-point-between-rectangular-and-polar-coordinates | how-to | How to convert a point between rectangular and polar coordinates |
| pre-calculus-how-to-graph-a-polar-equation | how-to | How to graph a polar equation |
| pre-calculus-how-to-eliminate-the-parameter-to-find-a-rectangular-equation | how-to | How to eliminate the parameter to find a rectangular equation |
**Already-covered skills it also exercises.** Distance formula / Pythagorean theorem (geometry,
already `n>0`), basic trigonometric ratios, logarithms (dB is a log scale — likely stays a stated
formula rather than a claimed new skill; not claimed here).
**Data feasibility: HIGH.** Named sources I expect to exist:
- A real handheld vocal microphone's manufacturer-published polar pattern chart with numeric
  dB-down values at labeled angles (e.g. Shure's published SM58 or Beta 58A polar pattern data
  sheet) — the standard "cardioid" shape, `r = 0.5(1 + cos θ)` (normalized), is the textbook
  idealization of exactly this real, published curve family, and Shure's own literature discusses
  the cardioid pattern in these terms.
- The gain-before-feedback formula itself (distance term via the inverse square law in dB —
  `20·log10(d_ref/d)` — plus a polar-attenuation term) is standard, citable audio-engineering
  material (textbooks / trade publications such as Sound On Sound, Shure's own application notes).
Sources I am NOT confident about: an exact numeric GBF "safe" threshold specific to a 300-seat
room (will likely need a stated Modeling Assumption anchored to a general published rule of
thumb); the venue itself and its stage dimensions are fictional and will be modeling-assumption
scenario numbers, dimensioned to be realistic for a real 300-seat house.
**Sensitivity (SPEC §6).** None — no illness, death, or financial-hardship stakes. Facilitator
note only for ordinary "the show could get shut down" stage-fright-adjacent tension, which is
mild and not flagged.
**Split risk.** None — 6 skills, matches the group exactly, no inflation.

### C2 — Drift Line — OBSOLETE, group closed by "Feedback" (was: score 4.08 · tier T4)
**Protagonist.** A Coast Guard sector watchstander deciding how to respond to a disabled,
drifting vessel reported near a charted shoal.
**The dilemma.** A.) Dispatch the duty tow vessel immediately on a direct interception heading OR
B.) Hold the tow vessel at the station and continue radar/AIS monitoring until the drifting
vessel is confirmed inside a defined safe-water buffer
**Primary metric.** Minutes of buffer time before the drifting vessel's projected track crosses
the charted hazard line, per option, weighted against dispatch fuel cost.
**Why it's close.** The drifting vessel's position is a parametric constant-velocity function of
time (its own reported drift heading and speed from wind/current); eliminating the parameter
gives the rectangular line of its track, which must be checked against the hazard boundary.
Radar detection range/bearing from the station is naturally polar. The tow vessel's response
time vs. the vessel's drift rate is what makes A vs. B close.
**Would close (same 6 skills as C1).**
**Data feasibility: MEDIUM.** Real NOAA chart hazard coordinates and real published
current/drift-rate tables exist (NOAA CO-OPS, NOAA nautical charts), but a real, public, per-hazard
station radar detection pattern is not something a public agency publishes with numeric bearing
data the way a microphone spec sheet does — the polar curve itself would likely end up an
idealized circle (mathematically valid but a visually weaker "graph a polar equation" deliverable
than C1's cardioid) or a Modeling Assumption. Coast Guard dispatch cost figures are not public.
**Sensitivity (SPEC §6).** Flag for discussion lead — this concept touches a vessel-in-distress
scenario. Framed as *protection* (buffer time before hazard) rather than casualty count, per
SPEC §6, but still merits the one-line note.
**Split risk.** None.

### C3 — Night Signal — OBSOLETE, group closed by "Feedback" (was: score 4.08 · tier T4)
**Protagonist.** A broadcast engineer recommending which of two candidate directional AM antenna
configurations a station licenses to extend nighttime coverage to a satellite town without
violating FCC nighttime interference-protection rules.
**The dilemma.** A.) License Configuration 1 (a two-tower array favoring range toward the target
town) OR B.) License Configuration 2 (a three-tower array with a deeper protective null toward
the co-channel station it must protect, at some cost to peak range)
**Primary metric.** Square miles of usable nighttime signal added over the target town per dollar
of antenna/engineering cost.
**Why it's close.** A directional AM antenna's radiation pattern is a real, FCC-filed
`relative field vs. azimuth` table — a genuine, often dramatically lobed polar curve, the richest
of any concept here. The parametric half is weaker: it would need to be manufactured (e.g. a
mobile monitoring van's route) rather than something the actual engineering decision needs.
**Data feasibility: MEDIUM.** FCC's public antenna pattern filings are real and are the single
best-sourced polar curve of any concept considered, but locating one specific station's exact
filed RFP (relative field pattern) table via the FCC's LMS/CDBS system within a research session
is not guaranteed, and the interference-protection contour math is genuinely more technical than
an MS/HS case should require (real FCC nighttime protection analysis is a professional-grade
calculation). The parametric requirement would be bolted on, not load-bearing — a coverage-inflation
risk (SPEC's own warning against a concept that "claims skills the case doesn't genuinely force").
**Sensitivity (SPEC §6).** None.
**Split risk.** Real risk this becomes two weaker half-cases (a strong polar case, a weak,
tacked-on parametric case) rather than one case that forces both — flagged, not fatal.

### C4 — Full Circle — OBSOLETE, group closed by "Feedback" (was: score 4.08 · tier T3)
**Protagonist.** A traveling-carnival ride mechanic choosing between two rotating swing-ride
configurations for a summer route.
**The dilemma.** A.) Configuration 1 — shorter chains, faster rotation OR B.) Configuration 2 —
longer chains, slower rotation
**Primary metric.** Rider throughput (riders/hour) at a fixed maximum outward lean angle safety
limit, per configuration.
**Why it's close.** A rider's position during spin-up is genuinely parametric,
`x(t) = r·cos(ωt), y(t) = r·sin(ωt)`, and eliminating *t* gives the classic `x² + y² = r²` circle
— clean, but mathematically thin: it is the textbook example, not a case-specific discovery, and
it does not force a genuinely separate polar-equation deliverable (the "polar equation" of a
ride's swept path is just `r = constant`, a degenerate case that fails to exercise "graph a polar
equation" meaningfully — that skill needs a curve that is *not* a circle to be worth anything).
**Data feasibility: MEDIUM.** Real ride manufacturer spec sheets (e.g. Chance Rides, Zamperla)
publish chain length, rotation speed, and rated capacity — genuinely sourceable — but the polar
half of the math is too degenerate to be worth the case.
**Sensitivity (SPEC §6).** None.
**Split risk.** None, but killed on math thinness (see Recommendation above).

---

**Next step:** `Approve a concept, then run case-write on it.` Per this run's operating
instructions, no human is available to approve interactively — **C1 (Feedback) is selected** and
`case-write` proceeds on it below.
