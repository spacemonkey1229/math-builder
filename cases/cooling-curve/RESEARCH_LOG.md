# Research Log — cooling-curve

15 `{{NEEDS_SOURCE}}` placeholders enumerated from `case.md` (2026-08-27). This case compares a
fictional facilities engineer's (Advait Rao) pyramid-vs-cone cold-plate fin decision at a
fictional hyperscale AI data center. Two classes of placeholder resulted: (1) real, publicly
priced/published figures (ASHRAE coolant temperature classes, copper spot price) that a real
publisher does supply, and (2) figures that no public source can supply because either the fin
geometry itself ("pyramid" and "cone" fins) is a math-case invention not sold under those names by
any real cold-plate vendor, or the deployment (Advait's specific site, rack count, deadline) is
fictional. Class 2 items are handled as disclosed Modeling Assumptions per the skill's Exit 1 —
none were dropped or required a redesign, because the pyramid/cone dimensions are the entire
mathematical premise of the case (tied directly to the volume-of-a-pyramid/volume-of-a-cone
standards) and cannot be removed without eliminating the case.

---

## P01 — ASHRAE TC9.9 coolant supply temperature range (Appendix A)

Searched: "ASHRAE TC9.9 2021 liquid cooling W1 W2 W3 W4 W5 supply temperature range facility
water". Direct fetch: `upsite.com/blog/major-changes-to-ashraes-fifth-edition-of-thermal-
guidelines-part-3-liquid-cooling-chapter-updates/` (tier 3, industry blog reporting on a paywalled
ASHRAE standard — the standard itself is not freely published, so a tier-1 fetch is not possible).
Cross-checked against snippets from `alliancechemical.com`, `cky.com.tw`, and `crac.services`
(not directly fetched, used only to corroborate, not cited) — all three independently reported the
same W1–W5 (pre-5th-edition) and W17/W27/W32/W40/W45/W+ (5th-edition, published March 2021) class
ranges: 2°C minimum for every class, upper bounds of 17/27/32/40/45/45+°C by class.

**Found:** 2°C–45°C spanning Classes W17–W45 (and W+ above that). **Confidence: MEDIUM** — the
primary standard is paywalled so this is a secondary report, but three independent industry sources
converge exactly, which is stronger corroboration than a single secondary source would give.
Recorded as **S1**. This figure is scene-setting context in Appendix A and is not load-bearing to
any Challenge (D1–D5) calculation.

## P02 — Heat dissipation rate per unit fin surface area, W/in² (Appendix A)

Searched: "pyramid fin cold plate heat sink surface area heat dissipation W/in2", "heat sink fin
heat transfer coefficient watts per square inch liquid cooled data". No manufacturer or standards
body publishes a flat W/in² dissipation-rate figure for a generic cold-plate fin — this quantity
depends on flow rate, coolant ΔT, and fin geometry specifics that vendors treat as proprietary CFD
outputs, not published constants. **NOT FOUND** as a direct citable fact after two search framings
and no plausible tier-1/2 publisher to fetch directly.

Found instead a publicly reported *convective heat-transfer coefficient* range for water-cooled
fins: 500–10,000 W/(m²·K) (general electronics-cooling literature, multiple corroborating
results). This is a real, citable physical-property range, but converting it into "W per in² for
THIS fin" additionally requires a coolant-to-fin-surface ΔT, which is not published for any real
system either. **Resolved as Modeling Assumption MA1**: h ≈ 2,000 W/(m²·K) (conservative low-mid
of the cited range) × an assumed ΔT = 10°C (plausible within the W17–W32 range found in P01) →
q″ = 20,000 W/m² ≈ 13 W/in². The derivation is shown in case.md; the coefficient range itself is
real and cited in the assumption's basis text (not treated as a separate sources[] entry since the
final applied number still requires an unsourced ΔT choice).

## P03–P06 — Pyramid base edge, cone base diameter, and fin heights (Appendix B)

Searched: "CoolIT Systems cold plate pin fin dimensions datasheet inches", "liquid cold plate fin
height mm base diameter cone pin spec sheet vendor". Direct fetch attempted on CoolIT's
`4000W-coldplate-Technical-Brief-f-1.pdf` — **404, tier-1 attempt genuinely failed**. Search
summaries surfaced real pin-fin dimensions from CoolIT (MicroCool: 4mm height, 50 fins/in, 15:1
aspect ratio), Wakefield Thermal, and academic cold-spray-manufactured pin-fin studies (heights
1–2.5mm, densities 8–30 fins/in). None of these vendors sell or measure a fin shaped like a
four-sided pyramid or a smooth cone under those names — real cold-plate fins are pins, diamonds,
or plate-fins, not the pyramid/cone geometry this case invents specifically to exercise the
volume-of-a-pyramid / volume-of-a-cone standards. **NOT FOUND** for the specific shapes this case
needs; a redesign is not viable because these dimensions ARE the case's mathematical premise.

**Resolved as Modeling Assumptions MA2 (pyramid base edge = 0.08 in), MA3 (cone base diameter =
0.09 in), MA4 (fin height, both = 0.2 in)** — set within the real cited dimension range (0.08–0.2
in / 2–5 mm), at the coarser end to match the Overview's "dozens of tiny points" / "standing in
neat rows" visual language (rather than a dense sub-mm micro-pin field), and chosen so the
pyramid's and cone's base footprints closely match (0.0064 in² vs. 0.00636 in²) per the
Background's own stated premise that the two fins share "the same base footprint and height."

## P07 — Material cost per cubic inch (Appendix C)

Searched: "copper price per pound 2026 COMEX spot". Direct fetch: `kitco.com/price/base-
metals/copper` (tier 1 — Kitco is a live exchange-price publisher). **Found: $6.5378/lb, 2026-08-27,
9:16 NY time.** Also fetched `kg-m3.com/material/copper` for the physical constant (density of
pure copper, 8.96 g/cm³ = 0.3237 lb/in³ — a standard, uncontested engineering constant).
**Derived:** $6.5378/lb × 0.3237 lb/in³ = $2.1166/in³ → **$2.12/in³**. **Confidence: HIGH**
(dated exchange price, direct fetch, standard physical constant). Recorded as **S2**, `derived:
true`. Assumes the fin material is copper (the case's Background text allows copper or aluminum;
copper is the higher-conductivity, more common choice for direct-to-chip cold plates and is
applied to both fin geometries for an apples-to-apples comparison).

## P08–P10 — Mold costs (pyramid, cone) and fins-per-mold amortization basis (Appendix C)

Searched: "injection mold tooling cost simple cavity vs complex cavity USD comparison" (found
plastic injection data — **rejected**, wrong manufacturing process: the case's fins are machined
or cast metal, not injection-molded plastic, so plastic tooling costs are not a defensible proxy).
Re-searched: "copper fin stamping die tooling cost CNC machining cold plate microfin manufacturing
cost per unit" — found that CNC machining (the actual dominant real-world process for copper cold
plates) has **zero tooling cost**, which would eliminate the case's entire cost differential; this
is the case's own narrative premise (a cast/stamped-fin approach with per-geometry mold cost), not
something case-research can silently overrule. Found comparable-process figures instead: metal
stamping dies run ~$5,000 for a simple single-cavity die vs. $6,000–$15,000 for a progressive/
compound (multi-feature) die — a real, if not perfectly matched, process analog (metal tooling,
not plastic). Search for die/mold life: "stamping die life number of shots cycles before
replacement" — found 100,000–500,000 cycles typical for simple, lower-volume tooling.

None of these direct-fetch attempts resolved (uneedpm.com and thefabricator.com both returned
403 on fetch, so per the skill's "never cite a URL you did not fetch" rule they are **not** cited
as sources[] entries — used only as informal prose basis for the Modeling Assumptions, which are
explicitly not sourced facts). **NOT FOUND** as citable figures. **Resolved as MA5 (pyramid mold
= $12,000), MA6 (cone mold = $5,000), MA7 (fins per mold = 300,000)** — all flagged HIGH
sensitivity; these are the figures most likely to flip the case's D5 recommendation (see the
Margin Note in case.md's Modeling Assumptions block).

## P11 — Cost-per-watt cooling benchmark (Appendix D)

Searched: "Uptime Institute cost per kilowatt data center liquid cooling infrastructure
benchmark". No Uptime Institute figure surfaced directly. Two industry-blog figures were found
instead, and they **conflict materially**: `thenetworkinstallers.com` reports liquid-cooling
capex at ~$1,000–$2,000/kW ($1–2/W); `introl.com` (fetched directly) reports "$3-4 million" for
1MW of liquid-cooling infrastructure ($3–4/W). Neither article cites a primary publisher for its
figure — both present it as an unattributed industry rule of thumb. Per the skill's "contested
figures" rule (SPEC §5), this is not used as a cited fact. **NOT FOUND** as a defensible sourced
figure. **Resolved as MA8** ($2.00/W, the midpoint of the lower-reported range), with the conflict
disclosed openly in the assumption's basis text rather than silently picking a side. Sensitivity
is Low: Appendix D is used only as a D4 cross-check, not as an input to D1–D3.

## P12–P15 — Deployment scale and mold-order deadline (Appendix E)

Not searched as literal facts — Advait Rao's specific deployment does not exist, so no source can
report its rack count, cold-plates-per-rack, fins-per-cold-plate, or internal deadline (same
reasoning as the `compute-lease` case's MA1–MA3 for its fictional company Kestrel Compute).
**Resolved as Modeling Assumptions grounded in real analogues where possible:**
- **MA9 (16 GPU racks):** pure scenario magnitude, chosen with MA10/MA11 so total fin count
  (16 × 72 × 48 = 55,296) lands inside the "tens of thousands of fins" the case's own Background
  text already states — an internal-consistency check, not an independent search.
- **MA10 (72 cold plates/rack):** grounded in real, current-generation hardware — NVIDIA's
  published GB200 NVL72 architecture (searched: "NVIDIA GB200 NVL72 rack number of GPUs cold
  plates per rack"; fetched `developer.nvidia.com` blog directly, confirmed 72 Blackwell GPUs/rack,
  published 2024-03-18) houses 72 GPUs per rack; the case's own Background states one cold plate
  per accelerator, so 72 cold plates/rack follows from that real spec. Not treated as a sources[]
  citation because Advait's specific site is not claimed to literally be GB200 NVL72 hardware —
  it is real-world grounding for an otherwise-unknowable fictional quantity.
- **MA11 (48 fins/cold plate):** grounded in the same real 8–30 fins/inch pin-density literature
  used for MA2–MA4, scaled down for the coarser fin size this case's dimensions use, and matched
  to the Overview's "dozens" language.
- **MA12 (45-day mold-order deadline):** purely narrative; not externally sourceable; no
  sensitivity to any D1–D4 calculation (matches the `compute-lease` MA3 precedent for a decorative
  countdown figure).

**Note on NVIDIA source's internal inconsistency:** the NVIDIA developer blog and a secondary
Introl blog post disagreed on GB200 NVL72's number of compute trays (18 vs. 36) — this ambiguity
did not affect the figure actually used (GPU count per rack, 72, was consistent everywhere), so it
did not block MA10, but is noted here in case a future pass wants the tray-level detail.

---

## Summary

- **2 SOURCED** (P01 ASHRAE temp range — MEDIUM; P07 copper cost/in³, derived — HIGH).
- **13 ASSUMPTION** (all other placeholders), all resolved via Exit 1 (stated Modeling Assumption),
  none dropped or redesigned — the pyramid/cone dimensions and their cost/dissipation consequences
  are the case's mathematical premise and cannot be removed.
- **0 remaining OPEN placeholders** in `case.md`/`case.json` (verified via the skill's step-7
  script).
- The load-bearing risk in this case is concentrated in **MA5–MA7** (mold cost gap and mold-life
  amortization) — flagged for `case-qa`/`case-balance` attention in the Margin Note.

Next step: **Run case-qa on cooling-curve.**

---

## Addendum 2026-08-29 — MA5 retune research (SPEC §2 balance retune)

The 2026-08-27 case-readiness run found the case unbalanced (T1-09 FAIL, 51.6% margin, cap ~20%)
because MA5 ($12,000 pyramid mold) vs. MA6 ($5,000 cone mold) — a 2.4x ratio — dominated the
pyramid's ~12.6% surface-area edge. Per the case owner's decision to retune (not accept the
imbalance), searched: "injection mold cost complexity multi-cavity vs single cavity price
difference tooling cost benchmark" and "metal injection mold tooling cost simple vs complex cavity
shape of revolution price". Neither plastic-injection nor metal-die literature publishes a figure
for this case's exact fictional geometry (same limitation as the original P08–P10 search), but both
converged on a consistent finding: **added geometric complexity realistically carries roughly a
30–50% cost premium per added complexity feature**, not a multiple-fold premium — e.g. "each
additional cavity adds 30-50% to the base cost" (tooling-cost guides); simple single-cavity molds
commonly run $3,000–$8,000 while complex multi-feature tooling runs materially higher but scales by
that per-feature percentage, not by 2–3x for a single added face-count step going from a
shape-of-revolution to a 4-face solid.

**Applied:** MA5 revised from $12,000 to **$7,000** — a 40% premium over MA6's unchanged $5,000,
inside the researched 30–50% band, still reflecting genuine added complexity (a 4-face mold really
is harder to tool than a single-cavity shape of revolution) without inflating the gap past what real
tooling-complexity pricing supports. MA6, MA7, and every other figure in the case are unchanged.
New margin: **18.4%**, inside SPEC §2's ~20% cap; winner (Cone Standoffs) unchanged. Full arithmetic
in `case.json.balance.margin_note`; full QA re-run in `QA_REPORT.md`'s 2026-08-29 entry.
