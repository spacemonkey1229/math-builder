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

Both fin geometries fit inside the same cold-plate footprint and the same coolant-loop flow budget the site's chiller plant already supports — geometry, not flow capacity, is what is on the table. What the deployment actually needs is not the fin that dissipates the most heat, and not the fin that costs the least to make, but the fin that dissipates the most heat per dollar spent producing it, at the volume this deployment requires (SEE APPENDIX C, APPENDIX D, APPENDIX E). Vendor cold-plate technical datasheets and published cooling-infrastructure cost benchmarks anchor the figures Advait is working from; every hard number in this case is either sourced with a citation or, where no public figure exists, stated openly as a Modeling Assumption once research is complete.

The vocabulary and "how to…" skills this case will ask you to research are listed in Appendix F — that is where Challenge 1 sends you.

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

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->

---

## Appendix A — ASHRAE TC9.9 Thermal Guidelines: Heat Dissipation and Surface Area

Liquid cold-plate fins pull heat from the accelerator into the coolant loop across their exposed surface — the more surface area a fin presents to the coolant at a given coolant supply temperature, the more heat it can carry away per unit time. ASHRAE TC9.9 publishes recommended coolant supply temperature ranges and cooling-capacity guidance for liquid-cooled data-center hardware.

| Quantity | Value |
|---|---|
| ASHRAE TC9.9 recommended liquid coolant supply temperature range this deployment will operate within, °C | {{NEEDS_SOURCE: ASHRAE TC9.9 recommended liquid-cooling coolant supply temperature range, °C, most recent published guideline}} |
| Heat dissipation rate per unit of exposed fin surface area, for a liquid cold-plate fin operating within that coolant supply temperature range, W per in² | {{NEEDS_SOURCE: heat dissipation rate per unit of exposed fin surface area for a liquid cold-plate fin, W per square inch, from ASHRAE TC9.9 guidance or a closely-derived cold-plate vendor technical datasheet figure}} |

Referenced from Background and forces the surface-area math behind Challenges D2 and D4.

---

## Appendix B — Fin Geometry Spec Sheet: Pyramid vs. Cone

Dimensions for the two fin geometries under consideration, drawn from cold-plate vendor technical datasheets.

| Dimension | Option A — Pyramid Array fin | Option B — Cone Standoff fin |
|---|---|---|
| Base shape | Square | Circle |
| Base edge length / base diameter (in) | {{NEEDS_SOURCE: pyramidal cold-plate fin base edge length, in inches, from a published liquid cold-plate vendor technical datasheet (e.g. CoolIT Systems or Vertiv)}} | {{NEEDS_SOURCE: conical cold-plate standoff fin base diameter, in inches, from a published liquid cold-plate vendor technical datasheet (e.g. CoolIT Systems or Vertiv)}} |
| Fin height (in) | {{NEEDS_SOURCE: pyramidal cold-plate fin height, in inches, from a published liquid cold-plate vendor technical datasheet}} | {{NEEDS_SOURCE: conical cold-plate standoff fin height, in inches, from a published liquid cold-plate vendor technical datasheet}} |

Referenced from Background and Challenges D1 and D2.

---

## Appendix C — Material and Manufacturing Cost Basis

Cold-plate fins of this kind are typically machined or cast from a high-conductivity metal. Manufacturing cost per fin has two components: the material used (a function of the fin's volume) and the mold itself, amortized across the number of fins that mold produces before replacement.

| Quantity | Value |
|---|---|
| Fin material and its cost per cubic inch, USD | {{NEEDS_SOURCE: cost per cubic inch of the metal (e.g. copper or aluminum) used in liquid cold-plate fin manufacturing, USD, current or most recent published price}} |
| Mold cost for a four-face pyramidal fin cavity, USD | {{NEEDS_SOURCE: tooling/mold cost for a multi-face pyramidal fin cavity at the production volume this deployment requires, USD}} |
| Mold cost for a conical (single-cavity, shape-of-revolution) fin, USD | {{NEEDS_SOURCE: tooling/mold cost for a conical fin cavity at the production volume this deployment requires, USD}} |
| Number of fins a single mold produces before replacement (amortization basis) | {{NEEDS_SOURCE: typical fin count a production cold-plate fin mold produces before replacement or re-tooling, both geometries}} |

Referenced from Background and Challenge D3.

---

## Appendix D — Cost-per-Watt Cooling Benchmark

Published cooling-infrastructure cost benchmarks give a cross-check figure: what the industry typically pays, per watt of cooling capacity delivered, across data-center liquid-cooling deployments.

| Quantity | Value |
|---|---|
| Published cost-per-watt benchmark for data-center liquid-cooling infrastructure, USD per watt | {{NEEDS_SOURCE: Uptime Institute (or comparable industry benchmark source) published cost-per-watt figure for data-center liquid-cooling infrastructure, USD per watt, most recent}} |

Referenced from Challenge D4, as a cross-check against the case's own computed watts-per-dollar figures.

---

## Appendix E — Deployment Build Spec and Constraints

| Constraint | Value |
|---|---|
| Number of GPU racks in next quarter's deployment | {{NEEDS_SOURCE: number of GPU racks in the deployment this cold-plate fin order covers}} |
| Liquid cold plates per rack | {{NEEDS_SOURCE: number of liquid cold plates per GPU rack in this deployment}} |
| Fins per cold plate | {{NEEDS_SOURCE: number of fins machined into a single liquid cold plate in this deployment}} |
| Mold order deadline, days from today | {{NEEDS_SOURCE: number of days until the fin mold order must be placed for this deployment, per the site's stated hardware-refresh schedule}} |

Referenced from Background and Challenges D4 and D5.

---

## Appendix F — "How To…" Math Questions To Research

**Vocabulary terms**

- Surface Area

**"How to…" questions**

- How to find the volume of a pyramid
- How to find the volume of a cone
