# Case Study: The Cooling Curve

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

Advait Rao holds two cold-plate samples under the fluorescent lights of the data center's mechanical mezzanine, one in each palm. The GPU racks arriving next quarter aren't the same profile the site was built for — hotter, denser, closer together — and the liquid cold plates bolted to each accelerator are the only thing standing between them and a thermal throttle. He turns the first sample over: dozens of tiny four-sided points machined into the copper base, catching the light like a bed of nails. Then the second: cleaner, simpler, tapered pins standing in neat rows. Both hum faintly on the demo rig behind him, hooked to a chiller loop cycling through clear tubing.

His manager wants the fin spec locked before the mold order goes out — once the tooling is cut, it doesn't change until the next hardware refresh. Somewhere down the mezzanine a fan array kicks on, loud enough that Advait feels it more than hears it. He sets the two samples side by side on the workbench, next to a laptop open to a blank spec sheet, and reaches for his calipers.

---

## Background

Advait Rao is a Facilities Engineer at a hyperscale AI data center responsible for thermal design sign-off on new compute deployments. Next quarter's GPU racks are rated to draw more power per rack than anything the site has previously cooled, and the liquid cold plates mounted directly on each accelerator carry the last line of defense against throttling: fin geometry machined into the plate's underside, designed to pull heat into the coolant loop as efficiently as possible for the material spent.

Two fin geometries are under consideration for the new cold-plate order, and Advait's recommendation sets the tooling for the entire deployment (SEE APPENDIX E).

**Option A — The Pyramid Array.** Each fin is machined as a four-sided pyramid rising from the cold-plate base. A pyramidal fin exposes more surface area per fin than a simpler shape of the same footprint and height, and the ASHRAE TC9.9 data-center thermal guidelines identify exposed fin surface area as the dominant factor in a fin's heat-dissipation capacity (SEE APPENDIX A). But a pyramidal fin's four flat, angled faces require a more complex mold than a shape of revolution, and at data-center volumes — tens of thousands of fins across a single rack deployment (SEE APPENDIX E) — mold complexity shows up directly in per-fin manufacturing cost (SEE APPENDIX C).

**Option B — The Cone Standoffs.** Each fin is machined as a simple cone, tapering from a circular base to a point. A cone mold is a shape of revolution, tooled by a faster and cheaper process than a multi-face pyramid mold (SEE APPENDIX C), but a cone's curved surface encloses less total surface area than a pyramid of matching base footprint and height, which caps how much heat each fin can dissipate (SEE APPENDIX A, APPENDIX B).

Both fin geometries fit inside the same cold-plate footprint and the same coolant-loop flow budget the site's chiller plant already supports — geometry, not flow capacity, is what is on the table. What the deployment actually needs is not the fin that dissipates the most heat, and not the fin that costs the least to make, but the fin that dissipates the most heat per dollar spent producing it, at the volume this deployment requires (SEE APPENDIX C, APPENDIX D, APPENDIX E). Vendor cold-plate technical datasheets and published cooling-infrastructure cost benchmarks anchor the figures Advait is working from; every hard number in this case is either sourced with a citation or, where no public figure exists, stated openly as a Modeling Assumption once research is complete (SEE APPENDIX F).

The vocabulary and "how to…" skills this case will ask you to research are listed in Appendix G — that is where Challenge 1 sends you.

---

## Dilemma

You are Advait Rao.

Do you:

**A.)** Spec the Pyramid Array — pyramidal fins machined into every cold plate in the deployment **OR**

**B.)** Spec the Cone Standoffs — conical standoff fins machined into every cold plate in the deployment

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A volume-per-fin table.** Using the base and height dimensions in Appendix B, compute the volume of material in one Pyramid Array fin (a pyramid) and one Cone Standoff fin (a cone), showing your arithmetic.
- **D2 — A surface-area-per-fin table.** Using the same Appendix B dimensions, compute the total exposed surface area of one Pyramid Array fin and one Cone Standoff fin — the basis for each design's heat-dissipation rate (Appendix A).
- **D3 — A manufacturing-cost-per-fin table.** Convert each fin's D1 volume into a material cost, then add the mold-amortization cost from Appendix C, to find a fully-loaded cost per fin for each design.
- **D4 — A watts-per-dollar comparison table.** Combine each design's D2 surface area with the Appendix A heat-dissipation rate to find watts dissipated per fin, then divide by the D3 cost per fin, scaled to the full deployment fin count in Appendix E. Cross-check your result against the published cost-per-watt cooling benchmark in Appendix D.
- **D5 — A recommendation** stating which fin geometry the site should tool up for, defended against the deployment's mold-order deadline in Appendix E.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A — ASHRAE TC9.9 Thermal Guidelines: Heat Dissipation and Surface Area

Liquid cold-plate fins pull heat from the accelerator into the coolant loop across their exposed surface — the more surface area a fin presents to the coolant at a given coolant supply temperature, the more heat it can carry away per unit time. ASHRAE TC9.9 publishes recommended coolant supply temperature ranges and cooling-capacity guidance for liquid-cooled data-center hardware.

| Quantity | Value |
|---|---|
| ASHRAE TC9.9 recommended liquid coolant supply temperature range this deployment will operate within, °C | 2°C – 45°C (spans Classes W17–W45) [S1] |
| Heat dissipation rate per unit of exposed fin surface area, for a liquid cold-plate fin operating within that coolant supply temperature range, W per in² | 13 W/in² [MA1] |

Referenced from Background and forces the surface-area math behind Challenges D2 and D4.

---

## Appendix B — Fin Geometry Spec Sheet: Pyramid vs. Cone

Dimensions for the two fin geometries under consideration, drawn from cold-plate vendor technical datasheets.

| Dimension | Option A — Pyramid Array fin | Option B — Cone Standoff fin |
|---|---|---|
| Base shape | Square | Circle |
| Base edge length / base diameter (in) | 0.08 in [MA2] | 0.09 in [MA3] |
| Fin height (in) | 0.2 in [MA4] | 0.2 in [MA4] |

Referenced from Background and Challenges D1 and D2.

---

## Appendix C — Material and Manufacturing Cost Basis

Cold-plate fins of this kind are typically machined or cast from a high-conductivity metal. Manufacturing cost per fin has two components: the material used (a function of the fin's volume) and the mold itself, amortized across the number of fins that mold produces before replacement.

| Quantity | Value |
|---|---|
| Fin material and its cost per cubic inch, USD | $2.12/in³ (copper, derived) [S2] |
| Mold cost for a four-face pyramidal fin cavity, USD | $7,000 [MA5] |
| Mold cost for a conical (single-cavity, shape-of-revolution) fin, USD | $5,000 [MA6] |
| Number of fins a single mold produces before replacement (amortization basis) | 300,000 fins [MA7] |

Referenced from Background and Challenge D3.

---

## Appendix D — Cost-per-Watt Cooling Benchmark

Published cooling-infrastructure cost benchmarks give a cross-check figure: what the industry typically pays, per watt of cooling capacity delivered, across data-center liquid-cooling deployments.

| Quantity | Value |
|---|---|
| Published cost-per-watt benchmark for data-center liquid-cooling infrastructure, USD per watt | $2.00/W [MA8] |

Referenced from Challenge D4, as a cross-check against the case's own computed watts-per-dollar figures.

---

## Appendix E — Deployment Build Spec and Constraints

| Constraint | Value |
|---|---|
| Number of GPU racks in next quarter's deployment | 16 racks [MA9] |
| Liquid cold plates per rack | 72 cold plates [MA10] |
| Fins per cold plate | 48 fins [MA11] |
| Mold order deadline, days from today | 45 days [MA12] |

Referenced from Background and Challenges D4 and D5.

---

## Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, needed because no public literature ties an exact number to the specific fictional
> deployment or to the pyramid/cone fin geometries this case invents for the volume-and-surface-area
> comparison. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Heat dissipation rate per unit of exposed fin surface area | 13 W/in² | Derived, not published: liquid cold-plate convective heat-transfer coefficients for water-cooled fins are reported in electronics-cooling literature at roughly 500–10,000 W/(m²·K). Using a conservative mid-low value of h ≈ 2,000 W/(m²·K) and an assumed 10°C coolant-to-fin-surface temperature differential (a plausible margin within the ASHRAE W17–W32 supply range in Appendix A): q″ = h·ΔT = 20,000 W/m² ≈ 13 W/in². | **Load-bearing — HIGH.** Directly scales every fin's D2 surface area into a D4 watts figure. A different ΔT or h choice moves both designs' wattage proportionally (it does not by itself flip which design wins per dollar, since it multiplies both options equally), but it does set the absolute scale students compare against the Appendix D cross-check. |
| MA2 | Pyramid Array fin base edge length | 0.08 in | No datasheet publishes fin dimensions under the name "pyramid fin" — real liquid cold-plate pin fins run 0.08–0.2 in (2–5 mm) tall at sub-mm to ~2 mm pitch (CoolIT MicroCool, general electronics-cooling literature). Chosen at the coarser end of that real range, consistent with the Overview's description of "dozens" of larger standoff-style points rather than a dense micro-pin field, and sized so its base footprint matches MA3's cone footprint per the Background's own "matching base footprint and height" framing. | Load-bearing — feeds D1 and D2 for the Pyramid Array directly. |
| MA3 | Cone Standoff fin base diameter | 0.09 in | Same real-fin-dimension basis as MA2. Diameter chosen so the cone's base area (π·(0.045)² ≈ 0.00636 in²) closely matches the pyramid's base area (0.08² = 0.0064 in²), per the case's stated premise that the two fins share the same base footprint and height. | Load-bearing — feeds D1 and D2 for the Cone Standoffs directly. |
| MA4 | Fin height, both geometries | 0.2 in | Set at the top of the same real cited fin-height range (0.08–0.2 in / 2–5 mm) used for MA2/MA3, and held equal between the two designs per the Background's explicit "same base footprint and height" comparison. | **Highest load-bearing figure in the case.** Height is the single dimension every one of D1–D4 shares between both geometries — changing it rescales both designs' volume, surface area, and cost together. It does not by itself flip the dilemma (it scales both sides), but a very different height changes how large the mold-cost-per-fin gap looks relative to the material-cost gap. |
| MA5 | Mold cost, four-face pyramidal fin cavity | $7,000 | No public price exists for a metal micro-fin mold at this specific geometry and volume. Industry tooling-cost benchmarking (both metal die and injection-mold literature) consistently reports that added geometric complexity — multiple angled faces vs. a single shape-of-revolution cavity — carries roughly a 30–50% cost premium per added complexity feature, not a multiple-fold premium; a four-face pyramid cavity against a single-cavity cone die (MA6, $5,000) is set at the upper end of that realistic premium band. | **Flippable — HIGH.** This is the core cost differential the whole dilemma turns on. A materially smaller pyramid-mold premium narrows or erases Option B's cost advantage; see margin note below. |
| MA6 | Mold cost, conical (shape-of-revolution) fin | $5,000 | Same industry-reporting basis as MA5: a simple, single-cavity die (a cone is a shape of revolution, the simplest mold geometry) runs around $5,000. | **Flippable — HIGH.** Paired directly with MA5; the *gap* between MA5 and MA6 ($2,000) is what makes Option B's per-fin cost lower once amortized. |
| MA7 | Fins produced per mold before replacement | 300,000 fins | No public figure exists for cold-plate fin mold life specifically. General metal-stamping-die life for simple, lower-volume tooling is reported at roughly 100,000–500,000 cycles before wear-driven replacement; 300,000 sits mid-range. Applied identically to both molds (die life is driven mostly by material and cycle count, not by cavity shape, per that same literature). | **Flippable — HIGH.** This is the amortization denominator for both MA5 and MA6. A smaller fin-per-mold count raises both designs' mold-amortization cost per fin, and by more for the pricier pyramid mold — narrowing Option B's advantage as the assumed mold life shrinks. |
| MA8 | Cost-per-watt benchmark, data-center liquid-cooling infrastructure | $2.00/W | **Contested figure, used only as a cross-check, not as a constraint.** Two industry blog sources were found reporting materially different figures with no attributed primary source: one puts liquid-cooling infrastructure capex at roughly $1,000–$2,000/kW ($1–2/W); another puts complete 1 MW liquid-cooling infrastructure at $3–4 million ($3–4/W). Neither cites a primary publisher (e.g., Uptime Institute itself), so per this case's sourcing rules neither is usable as a cited fact. $2.00/W is stated as a representative mid-point of the lower-reported range, explicitly flagged here as unsourced rather than presented as if it were the Uptime Institute figure the case originally asked for. | Low. Appendix D is used only as a D4 cross-check, not as an input to D1–D3; it does not itself feed the watts-per-dollar comparison that decides the dilemma. |
| MA9 | Number of GPU racks in next quarter's deployment | 16 racks | Purely scenario-specific — this fictional deployment's total rack count cannot be sourced from any real company. Chosen, together with MA10 and MA11, so total fin count (16 × 72 × 48 = 55,296) lands in the "tens of thousands of fins" the Background already states. | Low for D1–D4 (a pure scaling multiplier applied equally to both designs' total cost and total wattage in D4 — it does not change which design wins per fin). Matters for D5's framing of deployment scale. |
| MA10 | Liquid cold plates per rack | 72 cold plates | Grounded in real current-generation hardware: NVIDIA's published GB200 NVL72 architecture houses 72 Blackwell GPUs per rack. The Background states a cold plate is "mounted directly on each accelerator" (1:1), so 72 accelerators/rack implies 72 cold plates/rack. This deployment is fictional, so the exact match to GB200 NVL72 is an assumption, not a claim about Advait's specific site. | Low for D1–D4 (same reasoning as MA9 — a uniform scaling factor). |
| MA11 | Fins per cold plate | 48 fins | Real pin-fin cold plates run roughly 8–30 fins per linear inch in published literature; at the coarser, larger-fin scale set by MA2–MA4 (0.08–0.2 in fins, not sub-mm micro-pins), a modest plate supports a "dozens"-scale field of fins, consistent with the Overview's "dozens of tiny four-sided points." 48 fins (e.g., a 6×8 arrangement) was chosen on that basis. | Low for D1–D4 (uniform scaling factor, same reasoning as MA9). |
| MA12 | Mold order deadline, days from today | 45 days | Purely narrative detail internal to the fictional scenario — not externally sourceable. | None. Decorative only; informs D5's timing argument but does not feed any D1–D4 calculation. |

**Margin note (MA5–MA7):** the mold-cost and mold-life assumptions are the figures most likely to
flip D5's recommendation. If the pyramid-mold premium over the cone mold (MA5 − MA6) is smaller
than assumed, or if the assumed mold life (MA7) is longer than 300,000 fins — spreading the
pyramid mold's higher upfront cost over more fins — the per-fin cost gap narrows and the Pyramid
Array's real surface-area advantage (shown in D2) can outweigh it on watts-per-dollar. Treat
MA5–MA7 as the assumptions worth interrogating in discussion.

---

## Appendix F — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | ASHRAE TC9.9 (5th Edition) liquid-cooling facility water supply temperature classes | 2°C (all classes) up to 17/27/32/40/45/45+°C by class (W17–W45, W+) | ASHRAE TC9.9 5th Edition, as reported by [Upsite Technologies — "What You Need to Know About ASHRAE's Fifth Edition of Thermal Guidelines"](https://www.upsite.com/blog/major-changes-to-ashraes-fifth-edition-of-thermal-guidelines-part-3-liquid-cooling-chapter-updates/) | Published March 2021, accessed 2026-08-27 | MEDIUM |
| S2 | Copper spot price (COMEX) → derived material cost per cubic inch | $6.5378/lb → $2.12/in³ | [Kitco — Live Copper Price](https://www.kitco.com/price/base-metals/copper); density constant 0.3237 lb/in³ from [kg-m3.com — Copper density](https://kg-m3.com/material/copper) | Accessed 2026-08-27 | HIGH |

*S1 is a secondary report of a paywalled primary standard (the ASHRAE TC9.9 document itself is not
freely published); three independent industry sources found in research converged on the same
W-class ranges, which is the basis for the MEDIUM grade rather than LOW. S2's per-cubic-inch figure
is derived: $6.5378/lb (copper spot, 2026-08-27) × 0.3237 lb/in³ (density of pure copper) =
$2.1166/in³, rounded to $2.12/in³ in the case table. Full search log, rejected sources, and every
Modeling Assumption's derivation are in RESEARCH_LOG.md.*

---

## Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Surface Area

**"How to…" questions**

- How to find the volume of a pyramid
- How to find the volume of a cone
