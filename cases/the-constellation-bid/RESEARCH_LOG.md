# Research Log — Constellation Bid

One row per placeholder identified at case-write time, what was searched, what was found or not, and the resolution. All searches and fetches were run live on 2026-09-18.

| # | Placeholder | Searched | Found | Resolution |
|---|---|---|---|---|
| P01 | Constellation altitude | Direct search for a real Solara Orbital altitude filing (none exists — fictional operator); searched for a real, representative modern LEO smallsat constellation altitude instead | FCC approval of SpaceX's first Starlink shell at 550 km (spaceflightnow.com, 2019-04-30) | ASSUMPTION — MA1, grounded in S1. Also confirmed live that most Starlink satellites have since moved to 450–490 km (a 2026 fleet-wide lowering); the case explicitly anchors on the original, better-documented 550 km figure rather than the current one. |
| P02 | Combined plane-change delta-v formula | Standard astrodynamics reference search for single-burn plane-rotation formulas | Δv = 2v·sin(Δθ/2), the standard combined-maneuver relation | SOURCED — S2 (standard reference relation; real formula, applied here to a RAAN change as a disclosed simplification, MA2). |
| P03 | Thruster specific impulse and reference mass | `busek.com/bit3` direct fetch | Isp up to 2,150 s; reference platform 14 kg 6U CubeSat, up to 2.39 km/s delta-v | SOURCED — S3. Same real thruster used in the sibling case `the-conjunction-call`; re-fetched fresh this session rather than reused from memory. |
| P04 | Satellite wet mass for Solara's fictional bus | No real figure exists (fictional constellation) | — | ASSUMPTION — MA3, grounded in S3's real reference-platform mass class. |
| P05 | Per-satellite propellant allowance for the plane-change walk | Searched for any published per-satellite propellant-budget planning figure for a real smallsat constellation; none found at the individual-satellite level (operators do not publish this) | — | ASSUMPTION — MA4, disclosed as the case's own stated, deliberately aggressive engineering-budget scenario. Flagged as the single most dilemma-relevant assumption in the case. |
| P06 | Rideshare (Consolidated Launch) price per kg | Direct fetch of `spacex.com/rideshare` (failed — JavaScript-rendered, no extractable text); two distinct search framings for "SpaceX Transporter rideshare price per kg 2026" | New Space Economy's dated (2026-02-27) report of SpaceX's own published rate: $350,000 base for 50 kg + $7,000/kg beyond, to SSO | SOURCED — S4, MEDIUM (not the primary page itself, consistent with `cases/_concepts/CONCEPTS_spaceflight_2026-09-12.md`'s own note that this exact primary source failed to load cleanly the same week). Historical rideshare price pattern found in the same search ($5,500/kg 2019 → $6,500/kg 2023 → $7,000/kg 2026) is used directly to ground the Twist. |
| P07 | Distributed Launch (dedicated small-lift) price per launch | Direct fetch of `rocketlabcorp.com/launch/electron/` (failed — HTTP 403); two distinct search framings for "Rocket Lab Electron dedicated launch price 2026" | SpaceNexus's live page reporting Rocket Lab's own published list price: $7.5M per launch, 300 kg to LEO | SOURCED — S5, MEDIUM (same not-the-primary-page reason as S4). |

## Rejected sources / dead ends

- `rocketlabcorp.com/launch/electron/` — HTTP 403 Forbidden on direct fetch, twice.
- `spacex.com/rideshare` — resolves, but the page is JavaScript-rendered; the fetch tool returned no pricing text, only the literal string "SpaceX".
- Considered citing a real published per-satellite propellant-tank capacity for an existing operational smallsat constellation (e.g. a real Walker-constellation operator's own published bus datasheet) to ground MA4 directly rather than as a pure scenario figure — no operator publishes this at the individual-satellite level, and the one manufacturer datasheet available (Busek's BIT-3 page, S3) publishes thruster performance, not tank capacity. Resolved as a disclosed scenario assumption instead of a fabricated citation.

## Derivation arithmetic (supports `case.json.derived` and `balance`)

```
mu = 398,600.4418 km^3/s^2      (standard gravitational parameter, not sourced -- standard physical constant)
altitude = 550 km (MA1)         r = 6,371 + 550 = 6,921 km
v = sqrt(mu / r) = sqrt(398,600.4418 / 6,921) = 7.5890 km/s = 7,589.0 m/s
circumference = 2*pi*r = 43,486.5 km

propellant_per_ms = wet_mass_kg / (Isp_s * g0_ms2) = 15.0 / (2,150 * 9.80665) = 15.0 / 21,084.2975
                   = 7.1143e-4 kg per m/s

Per group (minimum angular separation theta, from Appendix B):
  theta=0deg:    dv = 2*7589.0*sin(0)     = 0.00 m/s       propellant = 0.000 kg   FEASIBLE  (<= 4.0 kg)
  theta=60deg:   dv = 2*7589.0*sin(30deg) = 7,589.00 m/s   propellant = 5.399 kg   NOT FEASIBLE
  theta=120deg:  dv = 2*7589.0*sin(60deg) = 13,144.53 m/s  propellant = 9.351 kg   NOT FEASIBLE
  theta=180deg:  dv = 2*7589.0*sin(90deg) = 15,178.00 m/s  propellant = 10.798 kg  NOT FEASIBLE

Option A correctly placed = 10 (Plane 0 only)
Option A total mass = 60 * 15.0 kg = 900 kg
Option A total cost = 350,000 + 7,000*(900-50) = 350,000 + 5,950,000 = $6,300,000
Option A ratio = 10 / 6,300,000 = 1.5873e-6 sats/$

Option B correctly placed = 60 (all six dedicated launches succeed by construction)
Option B total cost = 6 * 7,500,000 = $45,000,000
Option B ratio = 60 / 45,000,000 = 1.3333e-6 sats/$

margin_pct = (1.5873e-6 - 1.3333e-6) / 1.3333e-6 * 100 = 19.05%   winner = A

Twist: rideshare price -> $9,000/kg
  Option A total cost = 350,000 + 9,000*(850) = 350,000 + 7,650,000 = $8,000,000
  Option A ratio = 10 / 8,000,000 = 1.25e-6 sats/$   (< Option B's 1.3333e-6)
  margin_pct = (1.3333e-6 - 1.25e-6) / 1.25e-6 * 100 = 6.67%   winner flips to B

Breakeven rideshare price p (solve ratio_A(p) = ratio_B):
  10 / (350,000 + p*850) = 1.3333e-6
  350,000 + 850p = 7,500,000
  p = 7,150,000 / 850 = $8,411.76/kg
```

All arithmetic re-verified by `sensitivity_model.py` at the bottom of this case's folder; running it directly reproduces every figure above.
