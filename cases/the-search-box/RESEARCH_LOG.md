# Research Log — The Search Box

Stage: `case-research`. Run 2026-08-30.

Primary source used for essentially all real, cited figures in this case: **The U.S. Coast Guard
Addendum to the United States National Search and Rescue Supplement (NSS) to the International
Aeronautical and Maritime Search and Rescue Manual (IAMSAR)**, COMDTINST M16130.2F, January 2013
("CGADD"), Appendix H ("Search Planning Guide") and Chapter 5 ("SAR Facilities"). This is the same
leeway-coefficient and set-and-drift/optimal-search-factor methodology behind the Coast Guard's
Computer-Assisted Search Planning (CASP) system and its successor, SAROPS — exactly the source the
concept sheet named. The official `dco.uscg.mil` and `media.defense.gov` hosts both returned
HTTP 403 to automated fetch; a mirror hosted by the U.S. Coast Guard Auxiliary's Response
Directorate (`rdept.cgaux.org`) served the identical document (same COMDTINST number, same January
2013 date, same letterhead, confirmed by inspecting the PDF's own title page) and was used for all
citations. Downloaded, converted to text with `pdftotext -layout`, and searched directly rather
than relying on search-result summaries, per the skill's tier-1 preference.

## Placeholder-by-placeholder

| # | Placeholder (abbreviated) | Searched | Found | Outcome |
|---|---|---|---|---|
| P01 | Elapsed time, report → last radar fix | N/A — this is inherently scenario-specific narrative timing, not a published figure | — | **Modeling Assumption** MA1 (4 min). Real incidents are sensitive/identifying (per concept sheet and FACILITATOR.md); no public figure exists or should exist for "how long after a specific PIW radio call before the radar fix." |
| P02 | Elapsed time, last fix → decision point | Same as above | — | **Modeling Assumption** MA2 (2h 30m). This is the load-bearing `t` for D2's parametric equations. |
| P03 | Helicopter remaining on-scene search endurance | "USCG rotary-wing SAR asset fuel/daylight planning limits"; CGADD Table 5-3 (Coast Guard Aircraft Characteristics); CGADD §H.5.2.2 | CGADD Table 5-3: H-60 MAX Endurance = 6.0 hrs (real, HIGH, S7). CGADD §H.5.2.2: "Search endurance can be assumed to be 85 percent of on scene endurance" (real, HIGH, S6). No public figure exists for *this scenario's specific remaining fuel state* at the decision point (that is inherently incident-specific). | **Combined SOURCED + Modeling Assumption.** MA3 states a 4.5-hr on-scene-endurance-remaining assumption (informed by the real 6.0-hr MAX endurance), then applies the real 85% rule to get 3.8 hrs of search endurance. |
| P04 | Helicopter search speed for PIW pattern | "USCG helicopter search speed person in water knots"; found directly in CGADD Table H-9 | CGADD Table H-9 "Search Aircraft Speed Correction": Person in Water row, Helicopter column — 90 kt carries a correction factor of 1.0 (the reference speed); 60/120/140 kt carry 1.5/0.8/0.7. | **SOURCED** (S1, HIGH). Used 90 kt as the case's stated search speed. |
| P05 | Sweep width for PIW search | "National SAR Supplement sweep width table person in water sea state"; CGADD Table H-15 (helicopters, 300–500 ft) | CGADD Table H-15: Person in Water, 300 ft altitude, 5 NM visibility → 0.1 NM uncorrected; footnote: "values... may be increased by a factor of 4 if it is known that the person is wearing a personal flotation device" → 0.4 NM. | **SOURCED** (S2, HIGH), with a stated visibility assumption (MA4, 5 NM) to select which table column applies — the visibility level itself is scenario-specific, but the table value at that visibility is real. |
| P06 | Track spacing | Derived from S2 at a baseline coverage factor of 1.0 (S = W, per CGADD §H.5.5.4/Figure H-20) | — | **SOURCED/derived** (S2, HIGH). 0.4 NM. |
| P07–P09 | Vessel position, radar bearing, radar range | N/A — inherently scenario-specific; the concept sheet explicitly flags these as expected-invented | — | **Modeling Assumptions** MA5–MA7. Real incidents are sensitive/identifying; no public figure should exist here. |
| P10 | Search-object category (of 63 leeway categories) | "Allen Plourde leeway coefficients Coast Guard person in water"; "USCG SAROPS leeway categories PIW"; found directly in CGADD Table H-7 | CGADD Table H-7 lists 5 PIW sub-categories: Vertical, Sitting, Survival Suit (Horizontal), Scuba Suit (Horizontal), Deceased (Horizontal). "Vertical" is the closest published match to a person kept upright by a flotation device. | **SOURCED** (S3, HIGH). |
| P11 | Leeway speed as % of wind speed | Same table | CGADD Table H-7, PIW/Vertical row: Slope 0.011, Y-intercept 0.07 kt → Leeway (kts) = 0.011×Wind(kts) + 0.07 kts. The placeholder asked for a pure "percent of wind speed," but the real published relationship is linear (slope + intercept), not a pure percentage — noted explicitly in case.md and the source note rather than rounding it into a false simple percentage. | **SOURCED** (S3, HIGH). |
| P12 | Leeway divergence angle | Same table | CGADD Table H-7, PIW/Vertical row: divergence angle ±30°. | **SOURCED** (S3, HIGH). |
| P13–P14 | On-scene wind speed and direction | N/A — inherently scenario-specific | — | **Modeling Assumptions** MA8–MA9 (20 kt, 210°T). Chosen to diverge from the current direction so the two boxes visibly disagree, per the case narrative. |
| P15 | Wind-model search-radius growth rate | CGADD Table H-7's "St Err (kts)" column (leeway-speed standard error); CGADD §H.2.1.1 (total probable error concept) | Table H-7, PIW/Vertical: St Err = 0.35 kt. §H.2.1.1 defines total probable error (E) as the radius of the 50%-containment circle, growing with elapsed time via drift-estimate uncertainty; §H.5.6.3 states search radius R = optimal search factor (fs) × E, with fs = 1.1 illustrated at Figure H-24. | **SOURCED** (S3 + S10, HIGH). E(t) = 0.35×t nm; R(t) = 1.1×E(t). |
| P16–P17 | On-scene current speed and direction | N/A — inherently scenario-specific | — | **Modeling Assumptions** MA10–MA11 (1.3 kt, 120°T). |
| P18 | Current-model search-radius growth rate | "NOAA USCG SAR search planning surface current estimate uncertainty percent set and drift error budget"; searched CGADD text for "drift error," "De," "current error," "uncertainty in... current" | **NOT FOUND.** The CGADD's total-probable-error formula (§H.2.1.1) names a drift-estimate-uncertainty term (De) but does not publish a per-hour standard-error figure for surface-current estimates analogous to Table H-7's per-category leeway standard error. A general WebSearch for a NOAA/USCG current-uncertainty rate returned only unrelated CODAR/SAROPS-data-source papers with no citable percentage or per-hour figure. | **Modeling Assumption** MA12 (0.45 kt/hr), explicitly flagged as NOT FOUND and set to the same order of magnitude as the real wind-model figure (0.35 kt) for comparability. Flagged **flippable** in FACILITATOR.md/case.json. |
| P19 | POC — Windward Datum (Option A) | CGADD Figure H-22 ("Probability of Containment For Single Point and Divergent Datums") | Figure H-22 plots four curves (single-point datum, and three "Divergent Datums" curves at increasing divergence distance) as a graph only — no companion numeric table. Because Option A's real ±30° leeway divergence angle (S3) makes it a genuine divergent-datum case, the qualitative direction (POC below the single-point-datum value) is real and citable (S9, MEDIUM), but no exact digit could be read off the graph to a defensible precision from a text-extracted PDF. | **Modeling Assumption** MA13 (55%), explicitly below the real single-point-datum value of 64.75% (S8) used for Option B, consistent with the graph's shape. Flagged **flippable** — the single largest lever on the recommendation. |
| P20 | POC — Set-and-Drift Datum (Option B) | CGADD §H.5.6.3(a)(1) and Figure H-24 | "As shown in Figure H-24, an optimal search factor of 1.1 produces a POC of 64.75% prior to any searching" — an exact, explicitly stated real figure for the single-point-datum case, which applies to Option B since it carries no stated divergence angle. | **SOURCED** (S8, HIGH). |
| P21 | Coverage-factor-to-POD relationship | CGADD §H.5.5 (Coverage Factor) and §H.5.6.2 (Probability of Detection) | §H.5.5.1–H.5.5.3: C = W/S, and C = (W×V×T)/A. §H.5.6.2(c): for "normal search conditions" and coverage beyond the graphed range (>3.0), POD = 1 − e^(−C) (Figure H-21 gives the same relationship graphically for 0–3.0). | **SOURCED** (S4 + S5, HIGH). |

## Rejected / not used

- A general WebSearch for "50% of wind speed" or round-number leeway-speed percentages for
  persons-in-water surfaced only secondary academic papers restating Allen & Plourde's general
  finding qualitatively ("roughly 3–5% of wind speed... depending on flotation"); this was **not**
  used because the CGADD's own Table H-7 gives an exact, category-specific linear equation
  (0.011×Wind + 0.07 for PIW/Vertical) rather than a single percentage, and Table H-7 is the
  primary, dated, unambiguous source per the skill's Tier-1 preference.
- The official `dco.uscg.mil` and `media.defense.gov` copies of the CGADD both returned HTTP 403 to
  automated fetch (likely a bot-blocking measure, not a takedown — the document is a public
  Commandant Instruction). The `rdept.cgaux.org` mirror was verified to be the identical
  COMDTINST M16130.2F document by its own title page before being used for any citation.
- No numeric table for the "divergent datum" POC curves (Figure H-22) was found anywhere in the
  document or in a follow-up search; this was reported as NOT FOUND rather than estimated from
  pixel positions in a rendered graph, per SPEC §5 (see MA13).
- No published per-hour standard-error figure for surface-current estimates (analogous to Table
  H-7's leeway standard error) was found in the CGADD or in a targeted WebSearch of NOAA/USCG SAR
  literature; reported as NOT FOUND (see MA12) rather than invented as a precise digit.

## Supplemental material gathered

- CBS News, ["Lost at sea: A harrowing story of survival"](https://www.cbsnews.com/news/lost-at-sea-a-harrowing-story-of-survival/)
  — the well-documented, publicly reported July 2013 rescue of Long Island lobsterman John
  Aldridge, in which the Coast Guard used SAROPS (built on the same leeway/drift methodology cited
  throughout this case) to locate and rescue him after roughly 11–12 hours in open water. Added to
  Appendix G as supplemental context establishing that this case's methodology is real and has
  found people, consistent with the FACILITATOR.md framing guidance (successful-rescue methodology,
  not peril). Link verified to resolve (HTTP 200) on 2026-08-30. Not cited as a numeric source for
  any placeholder — this incident's own figures are not used anywhere in the case.

## Verification

Ran the skill's standard verification script against the final `case.md`/`case.json`:
placeholders remaining = 0; citation markers with no source row = none; source rows never cited
in text = none; no source is graded LOW; `needs_source[]` has zero entries still `OPEN`;
`modeling_assumptions[]` has 13 entries. Both external URLs cited (the CGADD mirror and the CBS
News article) were re-checked and resolve with HTTP 200 as of 2026-08-30.

## Margin computation (facilitator-only — not in case.md)

Using the sourced/assumed figures above: elapsed time t = 2.5 hr, search endurance T = 3.8 hr,
sweep width W = 0.4 NM, search speed V = 90 kt, optimal search factor fs = 1.1.

- **Option A (Windward):** leeway speed = 0.011×20 + 0.07 = 0.29 kt; E(t) = 0.35×2.5 = 0.875 NM;
  R = 1.1×0.875 = 0.9625 NM; box area (2R)² = 3.706 sq NM; coverage C = (W×V×T)/Area = 136.8/3.706
  = 36.9; POD = 1−e^(−36.9) ≈ 99.99%; POC = 55% (MA13); POS = 0.55×0.9999 ≈ 0.5499;
  POD-per-flight-hour = 0.5499/3.8 ≈ 0.1447 (14.5%/hr).
- **Option B (Set-and-Drift):** E(t) = 0.45×2.5 = 1.125 NM; R = 1.1×1.125 = 1.2375 NM; box area
  (2R)² = 6.126 sq NM; coverage C = 136.8/6.126 = 22.3; POD ≈ 99.99%; POC = 64.75% (S8);
  POS = 0.6475×0.9999 ≈ 0.6474; POD-per-flight-hour = 0.6474/3.8 ≈ 0.1704 (17.0%/hr).
- **margin_pct** = (0.1704 − 0.1447)/0.1704 ≈ **15.1%**, **Option B (Set-and-Drift Datum) wins.**
  Recorded in `case.json`'s `balance` object and in FACILITATOR.md. Within the ~20% ceiling FACILITATOR.md
  itself sets before flagging a need to retune a constraint — but only just; MA12 and MA13 are both
  flagged flippable, and case-qa should re-check this margin once/if either NOT-FOUND assumption is
  replaced by a real figure.

## Next step

Run `case-qa` on `the-search-box`.
