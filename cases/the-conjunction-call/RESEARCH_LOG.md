# Research Log — Conjunction Call

One row per placeholder from `case-write`'s draft, per `skills/case-research/SKILL.md` §7.

| # | Placeholder / figure | Searched | Found | Disposition |
|---|---|---|---|---|
| P01 | Real industry collision-probability maneuver threshold | "NASA conjunction assessment collision probability threshold maneuver decision" | NASA CARA FAQ / NPR Handbook (2025), nasa.gov: baseline Pc threshold 1×10⁻⁴ for recommending mitigation; ~1.5 orders of magnitude reduction target (≈3.1×10⁻⁶) after a maneuver. Primary-source NASA program documentation. | **SOURCED — S1**, HIGH confidence. |
| P02 | Total tracked/cataloged objects in Earth orbit (for order-of-magnitude grounding of MA1) | "ESA Space Environment Report 2026 number of tracked objects catalog" | ESA DISCOSweb Space Environment Statistics: 46,875 objects, data as of 2026-07-31. Live database maintained by ESA's Space Debris Office. | **SOURCED — S2**, HIGH confidence. |
| P03 | Number of tracked objects sharing Aurora-7's specific altitude band this season | Checked CelesTrak SOCRATES documentation and ESA DISCOSweb statistics pages directly for a per-satellite or per-shell screening-population figure. | No public catalog publishes a per-satellite or per-shell subset count — SOCRATES screens the entire catalog against itself for every active payload, not a narrower per-shell population. This is expected: Aurora-7 is fictional, so no real per-satellite figure could ever exist to find. | **NOT FOUND → ASSUMPTION (MA1)**, grounded in S2's real catalog scale. 36 objects (including Aurora-7), a realistic order of magnitude for a congested mid-inclination LEO shell. |
| P04 | Small-satellite propulsion system real specifications (thrust, Isp, mass, power) | "Busek BIT-3 ion thruster specific impulse thrust spec sheet" | busek.com/bit3 (manufacturer product page): Isp up to 2,150 s, thrust up to 1.1 mN, dry mass 1.40 kg w/ gimbal, input power 56–75 W, reference platform up to 2.39 km/s delta-v for a 14 kg 6U CubeSat. Cross-checked against satcatalog.com/component/bit-3 (consistent, slightly higher upper-bound figures from a different test configuration — busek.com's own page was used as the primary-source figure). | **SOURCED — S3**, HIGH confidence (primary manufacturer datasheet). |
| P05 | Busek BIT-3 propellant mass / iodine tank capacity | Checked busek.com/bit3, satcatalog.com/component/bit-3, satcatalog.com/component/bit-3-cubesat-system, and attempted to extract the hosted BIT-3 datasheet PDF (satcatalog.s3.amazonaws.com). | Not published on any of the three HTML pages checked. The datasheet PDF could not be extracted as readable text (binary/image-stream content); reasonable further attempts were not pursued since two independent product pages from the same manufacturer/reseller both omit this figure, suggesting it is not publicly disclosed for this system at all. | **NOT FOUND → ASSUMPTION (MA3 wet mass, MA4 reserve propellant)**, both disclosed as stated scenario values for the fictional Aurora-7, consistent with the BIT-3's own published reference-platform mass class (14 kg 6U CubeSat). |
| P06 | CelesTrak SOCRATES Plus screening methodology (screening frequency, propagation window, screening range, reported fields) | "CelesTrak SOCRATES Plus conjunction screening methodology minimum range probability three times daily" | celestrak.org/SOCRATES/ (confirmed live 2026-09-17): screens 3×/day, propagates 7 days forward, reports every predicted approach within 5 km at closest approach with minimum range, time of closest approach, relative speed, and maximum Pc. | **SOURCED — S4**, HIGH confidence (primary, live public service). |
| P07 | Aurora-7's specific 45-day, six-event conjunction log (per-event min range, Pc, required delta-v) | N/A — a specific conjunction history for a specific fictional satellite has no real-world source to search for. | Inherently a scenario construction; styled on S4's real report format/field structure. | **ASSUMPTION (MA2)**, disclosed as a stated scenario dataset, not a live feed record. |
| P08 | Meridian Orbital's disposal-compliance minimum propellant reserve | Checked for a general public figure on minimum propellant reserves required for a controlled small-satellite disposal burn; found general orbital-debris-mitigation guidance describing the *requirement* to retain disposal capability, but no single numeric "kg required" figure that would generalize across different spacecraft/thruster combinations. | General practice confirmed (retain enough propellant to complete disposal), but no universal numeric figure exists — the actual number depends on the specific spacecraft's mass, thruster, and target disposal orbit change, none of which are standardized. | **ASSUMPTION (MA5)**, a stated policy minimum for the fictional Meridian Orbital, applied identically under both options in the case's math. |

## Arithmetic derivations (shown in full; case.md's Appendix D asks students to reproduce this)

- Exhaust velocity: `v_e = Isp × g0 = 2,150 s × 9.80665 m/s² = 21,084.2975 m/s`
- Propellant per m/s of delta-v: `12.0 kg ÷ 21,084.2975 m/s = 5.6912×10⁻⁴ kg per m/s` (rounded to 5.691×10⁻⁴ in case.md)
- Events crossing the real 1×10⁻⁴ threshold (Appendix C): E2 (3.4×10⁻⁴), E4 (1.9×10⁻⁴), E5 (5.2×10⁻⁴), E6 (1.1×10⁻⁴). E1 (2.7×10⁻⁵) and E3 (8.1×10⁻⁵) do not cross.
- Total delta-v for maneuvering events: `3.5 + 6.0 + 7.0 + 4.5 = 21.0 m/s`
- Total propellant required: `21.0 × 5.6912×10⁻⁴ = 0.011951 kg`
- Propellant available for avoidance: `0.024 kg (MA4) − 0.0100 kg (MA5) = 0.0140 kg`
- Margin: `(0.0140 − 0.011951) / 0.0140 × 100 = 14.64%` → **Option B (Fly The Season) wins.**
- D1 combination count: `C(36,2) = 36!/(2!·34!) = (36×35)/2 = 630` total pairs; `35` pairs involve Aurora-7 directly.
- D2 standard-notation forms and absolute-value margins against 1×10⁻⁴ (i.e. 0.0001):

| Event | Pc (scientific) | Pc (standard) | \|Pc − 0.0001\| | Margin (scientific) | Crosses threshold? |
|---|---|---|---|---|---|
| E1 | 2.7×10⁻⁵ | 0.000027 | 0.000073 | 7.3×10⁻⁵ | No |
| E2 | 3.4×10⁻⁴ | 0.00034 | 0.00024 | 2.4×10⁻⁴ | Yes |
| E3 | 8.1×10⁻⁵ | 0.000081 | 0.000019 | 1.9×10⁻⁵ | No |
| E4 | 1.9×10⁻⁴ | 0.00019 | 0.00009 | 9.0×10⁻⁵ | Yes |
| E5 | 5.2×10⁻⁴ | 0.00052 | 0.00042 | 4.2×10⁻⁴ | Yes |
| E6 | 1.1×10⁻⁴ | 0.00011 | 0.00001 | 1.0×10⁻⁵ | Yes (barely) |

## Rejected / not used

- OpenEI/PRIMRE-style derived per-unit figures were not applicable here (that rejection pattern is
  from the unrelated Turbine Channel case).
- A NASA CARA "hard body radius" mandatory-mitigation rule (mitigation is mandated if predicted
  miss distance is smaller than the combined hard-body radius, regardless of Pc) is real and
  mentioned in S1, but this case does not use it as a second decision rule — no combined hard-body
  radius figure for a fictional satellite/debris pair could be sourced, and introducing a second
  stated-assumption threshold alongside the real Pc threshold would dilute the case's one clean,
  real decision rule. Noted here so a future author doesn't re-search this and re-discover the same
  dead end.

## Next step

Run `case-readiness` on `the-conjunction-call`.
