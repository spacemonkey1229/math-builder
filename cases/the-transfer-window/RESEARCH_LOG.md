# Research Log — The Transfer Window

24 `{{NEEDS_SOURCE}}` placeholders were enumerated in `case.md` (Appendices A–D). This log records
what was searched, what was found, what was rejected, and why — including two significant
mid-research findings that changed how the case had to be modeled.

## Key finding #1 — no single real vehicle publishes both a chemical and an electric GEO-transfer
mode with a shared, fixed wet/dry mass

The concept sheet named "a Rocket Lab or similar small-launch-provider product." Rocket Lab's
**Photon** was checked first (Wikipedia, Rocket Lab's own spacecraft-bus-lineup announcement) and
ruled out: Photon is chemical-only (Curie/HyperCurie), has no electric-propulsion variant, and is
not marketed for GEO missions. Momentus **Vigoride** was checked next and ruled out: it uses a
water-fed microwave electrothermal thruster only, no chemical mode.

**Spaceflight Inc.'s Sherpa OTV line** (now owned by Firefly Aerospace, confirmed still active —
SpaceNews, "Firefly Aerospace acquires Spaceflight Inc.," 2023‑06‑08) is the real product family
used: **Sherpa‑LTC** (chemical bipropellant, Benchmark Space Systems' Ocelot engine) and
**Sherpa‑LTE** (electric, Apollo Fusion's ACE Hall thruster). This is the closest real match to
"one product line, one chemical variant, one electric variant" — but they are two separately
massed vehicles (Sherpa‑LTC's own published wet mass is 180 kg; no public dry mass exists for a
hypothetical single bus flying either mode). **Rejected as a literal match** to Appendix C's
premise of "identical wet/dry mass regardless of trajectory flown." Recommended and adopted exit:
a disclosed Modeling Assumption (MA-kick-stage) — Meridian's fictional kick stage borrows Sherpa's
real wet mass and both variants' real Isp figures, but the "one shared bus" framing is stated as a
simplification, not literally true of Sherpa.

A second, related trap: naively pairing Sherpa‑LTC's own flown delta‑v (≈0.5 km/s — real, but only
for a modest LEO orbit-raise, not a LEO→GEO transfer) with Sherpa‑LTE's own flown context would
make the **electric** option need a *higher* propellant mass fraction than chemical, which
inverts the case's premise and contradicts real literature on chemical‑vs‑electric mass ratios
(chemical 3–4:1, Hall‑effect 1.3–1.5:1 per general search results). This was caught before being
written into the case. **Resolution:** the Direct Burn's delta‑v is computed directly from real
orbital radii via the standard Hohmann‑transfer equations (not taken from Sherpa‑LTC's own flown
number), while the Patient Drift's delta‑v uses Sherpa‑LTE's real published "over 6 km/s" figure,
which — checked against the general low‑thrust LEO–GEO literature — is consistent with real
low‑thrust GEO-transfer delta‑v requirements (this is why electric needs *more* delta‑v but a much
smaller propellant mass fraction, matching real mass‑ratio literature).

## Key finding #2 — Appendix B's stated methodology (NASA JPL Trajectory Browser / Horizons) does
not apply

Both tools model heliocentric/interplanetary trajectories among solar-system bodies, not
Earth-centric LEO→GEO transfers. Neither returns a semi-major axis or eccentricity for an Earth
parking-orbit-to-GEO transfer. The case's semi-major axis, eccentricity, delta-v, and transit time
for the Direct Burn are instead **derived directly from real inputs** (parking-orbit radius,
GEO radius, Earth's real gravitational parameter) using the standard two-body Hohmann-transfer
equations — legitimate, citable orbital mechanics, not the tool named in the draft. Appendix B's
intro sentence has been corrected in `case.md` to describe the actual method.

## Placeholder-by-placeholder log

| # | Placeholder (short) | Searched | Found | Outcome |
|---|---|---|---|---|
| P01 | Kick stage name | "Rocket Lab Photon" specs; "Momentus Vigoride" specs; "Spaceflight Sherpa-LTC/LTE" specs | Sherpa OTV line (Firefly/ex-Spaceflight), real, dual chemical+electric variants | SOURCED (S1–S3), with MA disclosing the "one shared bus" simplification |
| P02 | Parking orbit radius | Sherpa-LTC/LTE mission profiles (Gunter's Space Page) | Both variants' first missions flew from 500 km SSO | SOURCED (S2, S3) — radius = 500 km + Earth radius |
| P03 | GEO radius | NASA Earthdata orbits page; Earth radius (WGS-84) | 35,786 km altitude (NASA) + 6,378.137 km Earth radius (WGS-84) | SOURCED (S4, S5), derived sum = 42,164 km |
| P04 | Max delivery window | Real satellite-delivery contracts for a fictional company are not public by construction (Appendix E anticipated this) | Boeing 702SP / SEP GTO–GEO commercial precedent: ~6-month (180-day) transfers are commercially accepted today | NOT FOUND (fictional contract) → MA1, anchored to S8 |
| P05 | Radiation tolerance | "commercial satellite bus total ionizing dose kRad spec" | NanoAvionics M6P bus: 20 krad TID, tested for a worst-case 5-year LEO mission | SOURCED (S10) as a proxy — MEDIUM confidence, noted LEO-context caveat (not a GEO-transfer-specific rating) |
| P06–P07 | Semi-major axis (A, B) | JPL Trajectory Browser/Horizons (ruled inapplicable — see Key Finding #2); Hohmann transfer equations | a = 24,521 km, derived from r1, r2, μ | DERIVED (S4–S6); B shares the same value under MA2 |
| P08–P09 | Eccentricity (A, B) | Same as above | e = 0.7195, derived | DERIVED; B shares the same value under MA2 |
| P10–P11 | Delta-v budget (A, B) | Hohmann equations for A; Sherpa-LTE spec for B | A = 3.82 km/s (derived); B = 6.0 km/s ("over 6 km/s," Sherpa-LTE) | DERIVED (A); SOURCED (B, S3) |
| P12–P13 | Isp (A, B) | Benchmark Space Systems Ocelot engine spec; Sherpa-LTE ACE Hall thruster spec | A = 290 s (Ocelot, HTP+octane bipropellant); B = 1,400 s (ACE Hall thruster) | SOURCED (S7, S3) |
| P14–P15 | Transit time (A, B) | Hohmann half-period calculation for A; Boeing 702SP / Lozinski et al. 2019 for B | A = 0.221 days (5.3 hr, idealized ballistic coast); B = 180 days | DERIVED (A); ASSUMPTION MA3 anchored to S8, S9 (B) |
| P16 | Kick stage wet mass | Sherpa-LTC spec (Gunter's Space Page) | 180 kg | SOURCED (S2) |
| P17 | Kick stage dry mass | No public figure exists for a bus flying both modes at this Δv/Isp combination | NOT FOUND | ASSUMPTION MA4 = 30 kg, sensitivity disclosed |
| P18–P19 | Propellant mass (A, B) | Rocket equation using sourced/derived Δv, Isp, and wet mass | A = 133.0 kg (73.9% of wet mass); B = 63.7 kg (35.4%) | DERIVED |
| P20–P21 | Max payload capacity (A, B) | Sherpa-LTC/LTE payload-to-GEO capacity in kg | Not published for either variant; duplicates the D3 deliverable-payload-mass calculation the case already requires | NOT FOUND → **DROPPED** (redesign: row removed from Appendix C, see below) |
| P22 | Belt dose rate | NASA NTRS SEL2/LRO transfer dose papers; general Van Allen belt dose-rate literature; a non-primary "rad/year at 4mm shielding" calculator page | Real figures found ranged from ~200 rad/yr to ~3,700 rad/yr depending on shielding/location — genuinely contested, shielding-dependent, and none carried a clean "rad/day while actively crossing" framing with a defensible primary citation | NOT FOUND at HIGH/MEDIUM bar → ASSUMPTION MA5 = 50 rad/day, disclosed range and sensitivity |
| P23–P24 | Belt-crossing fraction (A, B) | ESA Cluster mission page — real Van Allen belt altitude ranges | Inner belt 6,000–12,000 km altitude, outer belt 25,000–45,000 km altitude; overlapped against Appendix A's real parking/GEO radii, belt-radius territory covers ≈48% of the radial climb for both options | DERIVED (S11 + geometry), same value for both options, with a disclosed time-vs-radius simplification caveat |

## Rejected sources (kept for the next person's benefit)

- **Rocket Lab Photon** as the named kick stage — real, currently offered, but chemical-only and
  not GEO-marketed. Rejected.
- **Momentus Vigoride** — real, currently offered, but single-mode (water MET) only. Rejected.
- A "~200 Rads/year in GTO" figure that surfaced repeatedly in search summaries — never traced to
  a specific fetched primary document with a stated shielding assumption; treated as
  unverifiable and not cited.
- A "3,700 rad/year at 4 mm Al shielding" figure from a web radiation calculator (WorldCalc) — no
  visible provenance for its own inputs; LOW confidence; not used as a load-bearing figure per
  SPEC §5 / SKILL.md grading rules.
- NASA NTRS/arXiv papers on Van Allen belt total dose for **SEL2 and lunar (LRO) transfer
  trajectories** (~150–160 rad at exit with 5 mm shielding) — real NASA sources, but for a
  different mission geometry (translunar, not LEO–GEO), so not directly citable as this case's
  dose-rate figure; referenced qualitatively only, not as a cited number.

## Structural edits made during research (reported, not hidden)

1. Appendix B's introductory sentence (claiming NASA JPL Trajectory Browser/Horizons as the
   modeling tool) was corrected to describe the actual method used: real orbital radii and Earth's
   real gravitational parameter, run through the standard Hohmann-transfer equations. A footnote
   was added explaining why both options share the same transfer-ellipse geometry.
2. Appendix C's "Maximum published payload capacity" row was removed (Exit 3 — decorative/
   duplicative: no public figure exists, and it duplicates the deliverable-payload-mass figure
   Challenge D3 already requires the student to compute).

## Balance finding — flagged, not forced

Computing the primary metric (kg deliverable payload / day of transit) from the sourced and
derived figures above gives the Direct Burn an overwhelming win — roughly two orders of magnitude
higher kg/day than the Patient Drift (Direct Burn's payload is only ~5x smaller than Patient
Drift's, but its transit time is ~800x shorter). This is far outside the SPEC's ~20% target
margin. Per instructions, this is reported plainly rather than adjusted by picking different
numbers to force closeness — see `case.json`'s `balance` object and `FACILITATOR.md` for the exact
computation and a recommendation.

# RETUNE PASS — 2026-08-31

**Trigger:** balance finding above (margin_pct = 15,940.5%, ~800x outside SPEC §2's ~20% cap).
FACILITATOR.md's own flag recommended checking two things before `case-qa`: (1) whether MA3 (the
Patient Drift's 180-day transit time) is an unrealistically extreme assumption, and (2) whether
"kg of payload per day of transit" is the right primary metric at all. Both were investigated.

## 1. Is MA3 unrealistically extreme? No — it is real-world typical, not a modeling error.

Re-verified both transit-time figures independently against the real physics and real mission
precedent, rather than taking the case's own arithmetic on faith:

- **Direct Burn, 0.221 days (5.3 hr).** This is the textbook Hohmann-transfer half-period between
  a 6,878 km parking orbit and 42,164 km GEO, computed from Earth's real GM (S6) via Kepler's
  third law — a standard, uncontested result (real GEO Hohmann transfers are routinely cited in
  the 5–6 hour range for the coast itself, before accounting for the days of real-world perigee/
  apogee-raise burn sequences most actual chemical missions add on top; the case already discloses
  this as an idealized single-burn coast, see Appendix B's footnote and MA2).
- **Patient Drift, 180 days.** Re-searched beyond the two sources already cited (S8: eoPortal on
  Boeing 702SP all-electric GTO–GEO transfers, ~6 months; S9: Lozinski et al. 2019, up to 200
  days). A fresh search on all-electric GEO satellite transfer times (queried 2026-08-31)
  returned the same real family of missions (Boeing 702SP / ABS-3A, EUTELSAT 115 West B, the
  first all-electric-propulsion GEO satellites, entering service 2015) with the same order-of-
  magnitude transit time — several months, not weeks. **180 days sits squarely inside real,
  published precedent for a full electric GEO orbit-raise, not at an exaggerated extreme of it.**
  MA3 is not the problem.

**Why the real gap is ~800x and not the "hours-to-weeks" gap named in this retune's own framing:**
a single chemical burn converts nearly all its delta-v in minutes, so the Direct Burn's transit
time is bounded below only by orbital mechanics (a fixed transfer-ellipse period). A Hall-effect
thruster's thrust is measured in millinewtons — literally 3–4 orders of magnitude below a chemical
engine's newtons-to-kilonewtons — so even though it needs *more* total delta-v (6.0 km/s vs. 3.82
km/s, S3/S12) for the same transfer, it can only deliver that delta-v continuously over months.
This is not a quirk of this case's chosen numbers; it is the structural reason chemical and
electric propulsion are different technologies with different use cases in real spacecraft design
(chemical: minutes-to-hours, one shot, propellant-hungry; electric: months, continuous, propellant-
sparing) — a `real orbital-mechanics fact`, exactly as this retune's own instructions anticipated,
not an artifact of an extreme assumption.

## 2. Can a different real metric close the gap without inventing numbers? No.

**a. Total mission cost per kg delivered.** Real industry commentary on all-electric GEO
satellites (Boeing 702SP program, eoPortal and Boeing press materials, searched 2026-08-31)
confirms qualitatively that lower propellant mass enables real launch-cost savings (a smaller
launch vehicle, or a dual-manifest/shared launch) — a genuine, sourced real-world economic
trade-off in the same direction this fix needs (favoring the Patient Drift). But no source found
publishes a **specific dollar figure** for that savings, nor a specific dollar figure for the cost
of the ~6 extra months before the satellite reaches revenue-generating GEO service (the real
"cost of delayed time-to-orbit" side of the trade). Building a cost-per-kg metric would require
inventing at least one of those two numbers — prohibited by SPEC §5 ("never fabricate a number").
Rejected.

**b. Pass/fail against the contracted delivery window (Appendix A's 240-day MA1 limit) instead of
a continuous ratio.** Checked whether reframing the dilemma as "does either option make the real
contractual deadline" would produce a decisive, non-fabricated split. It does not: at 180 days,
the Patient Drift is real and sourced to be well inside the 240-day window (MA1's own sensitivity
note already says as much — "above roughly 200 days it never binds either option"). Both options
pass. A pass/fail gate on this specific number cannot be the *primary* metric because it never
discriminates between the two options here — it would need a materially shorter contract window
than the sourced 240-day commercial-precedent figure (S8) to bind, which would mean inventing a
tighter fictional contract term with no anchor. Rejected as the primary metric; it remains valid
and stays in the case as Appendix D's secondary, non-numeric pass/fail radiation-dose gate
(unchanged).

## Why this margin cannot be closed under the current option pair

The deciding structural fact is the ~3–4 order-of-magnitude difference between chemical thrust
(newtons–kilonewtons, minutes) and Hall-effect electric thrust (millinewtons, months). This ratio
is a property of the two real propulsion technologies themselves, not of this case's specific
delta-v, Isp, or mass numbers — any real chemical-vs-full-electric kick-stage comparison to GEO
will show a multi-hundred-x transit-time gap alongside only a ~2–6x mass-fraction gap (chemical
mass ratios run ~3–4:1, Hall-effect ~1.3–1.5:1, per the original pass's own literature check). No
real, non-fabricated choice of delivery-window contract term, dry-mass assumption, or cost figure
changes that structural ratio enough to bring a kg/day-style (or any linear combination of payload
mass and transit time) metric under SPEC's ~20% cap.

## Conclusion and recommendation

**No changes were made to `case.md`, `case.json`, or `FACILITATOR.md` in this pass.** Forcing a
closer number here would require either mislabeling a real 180-day electric transit as an
exaggerated assumption (it is not — see §1 above) or inventing a cost figure or a tighter fictional
contract deadline with no real anchor (both prohibited by SPEC §5). `case.json.balance.margin_pct`
remains `15940.5` pending a human decision on next steps, matching the disposition used for
`the-locks-window` under the same circumstance.

**Recommended path forward (needs a human/case-write decision, not a retune):** keep The Transfer
Window's Sherpa-LTC/Sherpa-LTE research as a valid, one-sided real result (it teaches parametric
equations, rectangular-equation elimination, and percent/rate arithmetic through a genuinely
decisive real trade-off between chemical and electric propulsion), and — separately — write a
**new** case under a new id for a genuinely close Pre-Calculus/Polar-and-Parametric dilemma in the
same career and skill group: **two different real parking-orbit phasing strategies for a launch
window**, not chemical-vs-electric propulsion. Real precedent search (2026-08-31) on ISS/crewed-
vehicle rendezvous profiles confirms this is a substantively different, and far more balanced,
kind of trade-off: real rendezvous missions choose between a **direct-ascent** profile (a
favorable phase angle at launch lets the vehicle reach the target in roughly one day, on the order
of hours after the final burn) and a standard **multi-orbit phasing** profile (launching into a
lower, faster-period parking orbit for several orbits — historically ~3–7 orbits, ~2 days on the
currently-flown ISS profile, up to ~5 days depending on phase angle at launch) — a real ~2–5x
schedule spread, not an ~800x one, while the two profiles' propellant/delta-v trade-off is
plausibly of a comparable order of magnitude (phasing trades schedule flexibility and launch-
window frequency for a longer transit, not a different propulsion technology entirely). This
keeps Talia Brooks, Meridian Launch Systems, and the same parametric/rectangular-equation skill
set, but swaps the *deciding physical asymmetry* from "chemical vs. electric propulsion" (fixed at
~800x by real technology) to "one-orbit vs. multi-orbit phasing geometry" (a real, tunable,
much-closer-scale trade). Sources to start from: rendezvous-profile literature surfaced in this
retune's search (e.g. "Short rendezvous missions for advanced Russian human spacecraft," Acta
Astronautica 67 (2010) 900–908) and standard ISS rendezvous-timeline references. Out of scope for
this retune — this is a fresh `case-write` premise, not a fix to the existing case.
