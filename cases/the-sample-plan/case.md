Case Study: The Sample Plan
MS | Math | Case Study | 2026 | Adventure

## Overview

The dock door is up, and the driver has checked his phone three times in the last two minutes. Renata Ibarra hasn't signed the release yet.

Behind her, stacked on a pallet, sit the sealed cases of single-use tubing manifolds from Lot 4471 — the sterile connective plumbing that a customer's cell-therapy manufacturing line is waiting on, three states away, to start a run tomorrow morning. Her badge still reads "Quality — 2nd Shift." Her signature on the Certificate of Analysis is the only thing standing between this lot and that truck.

The batch-release screen in front of her — software that walks a Quality Engineer through each required test one at a time, records the actual result next to what the specification requires, and only lets her generate and sign a Certificate of Analysis (the document listing every specification, every actual result, and her signature) once every required line shows a pass — shows two saved sampling plans, same lot number at the top of both. One of them is already highlighted, the way the software always defaults to the plan that clears fastest. The other sits one click away, in a smaller font, unselected.

Her supervisor, half in the doorway with his coat already on, says the thing everyone on this shift says by nine o'clock: "It's the same lot either way — just sign the fast one." Renata doesn't say what she's actually thinking, which is that "fast" and "fully covered" are two different questions, and nobody has actually run the numbers on which sampling plan she's about to click tonight.

The countdown on the driver's dispatch app ticks over. Her cursor sits between the two plans, over a button that will decide how many of these units get pulled and destroyed to check the rest.

## Background

Renata Ibarra is a Quality Engineer at Alden Bioprocess Components, a mid-sized manufacturer of single-use tubing and manifold assemblies — a manifold assembly is a branching network of sterile, single-use plastic tubing joined together at multiple ports (an opening on the tubing itself where another line, sensor, or connector attaches), connectors, and clamps, built to route a drug or biologic fluid from one manufacturing step to the next and then be thrown away rather than cleaned and reused — used in biologics (drugs manufactured from living cells, which are grown and held inside a bioreactor: in single-use manufacturing like Alden's, that is typically a large flexible plastic bag holding cells and growth medium (a nutrient-rich liquid that feeds the cells so they can grow and multiply) in liquid suspension (dispersed throughout the liquid, rather than dissolved in it or floating on top), sitting inside a rigid support container rather than a fixed steel tank) and cell-therapy production (a treatment manufactured individually, from one specific patient's own cells, on a fixed clinical timeline — which is why a single-sourced tubing lot with no substitute on hand can stall that one manufacturing run outright, not just delay a shipment) — the same general product category made at far larger scale by named industry players like Sartorius, Thermo Fisher Scientific, and Cytiva, whose single-use systems Alden's assemblies are designed to be compatible with. Every finished production lot must clear a destructive quality-control (QC) sample before Renata can sign its Certificate of Analysis and release it for shipment (SEE APPENDIX A). "Destructive" is the operative word: every unit pulled for testing is cut open, pressure-tested to failure, or otherwise consumed in the process, and cannot be sold afterward — so a bigger sample is not free QC, it is real, disposed inventory. A tested unit "fails" in one of a few concrete ways — it leaks at a seal or port under normal pressure, or it survives to some pressure but bursts below the minimum threshold the standard requires — and either one means that unit did not meet spec. Because every unit in the same lot is molded, welded, and sterilized together from the same raw-material batch and the same production run, a defect found in one destructively tested unit is treated as evidence about how the *whole* lot was made, not just about that one unit — that substitution (a few destroyed units standing in for what could not otherwise be known about the rest without destroying every one of them) is the entire logic behind pulling a sample at all, rather than testing 0 units or all 500.

Tonight's lot, Lot 4471, presents Renata with two named, pre-approved sampling plans loaded into the batch-release software (SEE APPENDIX A): **The Lean Draw**, which pulls the smaller sample size specified by the ANSI/ASQ Z1.4 acceptance-sampling standard's General Inspection Level II for a lot this size, and **The Deep Draw**, which pulls the larger sample size specified by the same standard's General Inspection Level III for the identical lot (SEE APPENDIX B). Both plans use the same acceptance rule: the lot is only released if every single tested unit passes; if even one tested unit fails, the whole lot is held for full inspection. Every other line of the two plans — which lot, which product, which acceptance rule — is identical; only the sample size, and therefore the number of units destroyed and the odds of catching a real problem, changes.

The instinct on the floor — her supervisor's instinct, and the software's own default selection — is that the smaller, faster sample is "close enough," since both plans use the same strict pass/fail rule. But a bigger sample doesn't just cost more units; it also changes, in a real and calculable way, the probability that an out-of-spec lot slips through undetected (SEE APPENDIX C). Renata has to weigh the certain, up-front cost of destroying more units against the real, probability-weighted cost of a defect reaching the customer's manufacturing line uncaught — using Appendix C's real industry contamination-occurrence data and the standard's own math (SEE APPENDIX D for the vocabulary and procedures that math requires, APPENDIX E for every source behind these figures, and APPENDIX F if you want real general background reading on any of this section's manufacturing/QC vocabulary beyond what the challenges require), not a gut feeling about which plan "sounds thorough enough."

There is a further wrinkle worth naming honestly: the industry-wide contamination-occurrence rate in Appendix C describes an average lot, not necessarily *this* lot. A lot flagged by a supplier deviation notice — a formal document a supplier files, on its own, when a raw material or component it shipped doesn't fully meet the agreed specification — is a different situation than an ordinary lot pulled at random (SEE APPENDIX C). Filing that notice is only the first step: the receiving quality team (Renata's own) is then required to evaluate it before the affected material can be used at all, and that evaluation ends in one of three real outcomes — accept the deviation as-is, reject the affected lot outright, or accept it only under extra scrutiny (such as pulling a larger sample) before it can be used. Whichever plan wins the math for an average lot might not win the same way for a lot Quality already has a specific reason to worry about.

## Dilemma

You are Renata Ibarra.
Do you:
A.) Sign off on The Lean Draw — the smaller Level II sample size OR
B.) Sign off on The Deep Draw — the larger Level III sample size

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A sampling-design table for each plan identifying: the **population** (the full production
    lot), the **sample** (the units actually pulled for destructive testing), an **individual**
    (one tested unit and its two possible outcomes), the **sample size**, and the **sampling
    method** used to select which physical units are pulled — with a written justification of why
    that method (not an easier one, like grabbing whichever units are most convenient to reach on
    the pallet) is the one the standard actually calls for.
    D2. An escape-probability calculation for each plan: using Appendix C's assumed fraction of
    defective units inside an out-of-spec lot, compute the probability that a fully out-of-spec
    lot still passes every single tested unit and ships undetected — shown as repeated
    multiplication, step by step, not just a final percentage.
    D3. A full expected-cost calculation for each plan: the certain destructive-testing cost (every
    tested unit, at its per-unit cost from Appendix A) plus the probability-weighted cost of an
    undetected defect reaching the customer (Appendix C's real lot-contamination-occurrence rate,
    times your D2 escape probability, times Appendix C's cost of an undetected escape) — with the
    arithmetic shown for every term, for both plans.
    D4. A written breakdown of D3's result: state how much of the cost difference between the two
    plans comes from the certain destructive-testing cost alone versus the probability-weighted
    risk cost, and then answer this directly — if Lot 4471 had actually been flagged by a supplier
    deviation notice (Appendix C's elevated-risk scenario), would your Challenge 2 recommendation
    still hold? Show the recomputed D3 arithmetic for that scenario before you answer.
    D5. An original dot plot comparing the escape probability produced by at least four different
    candidate sample sizes (including both Lean Draw and Deep Draw), to show whether that
    probability drops at a steady, even rate as the sample size grows, or at some other rate.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — The Two Sampling Plans

Referenced in Background and Challenge 3 (D1, D3, D4). Lot 4471 contains 500 finished units (MA3 — see Appendix C's modeling note below the assumptions table; this is a scenario-setting figure, not a disclosed real Alden lot size). Every destructively tested unit is a real, disposed cost — it cannot be sold once tested.

| | The Lean Draw (Option A) | The Deep Draw (Option B) |
|---|---|---|
| ANSI/ASQ Z1.4 General Inspection Level | II | III |
| Sample size code letter | H [S1] | J [S1] |
| Sample size (units pulled and destroyed) | 50 [S1] | 80 [S1] |
| Acceptance rule | Accept only if 0 of the tested units fail (a "c = 0" plan) [S2] | Accept only if 0 of the tested units fail (a "c = 0" plan) [S2] |
| Cost per unit destructively tested | $250 (MA-cost — see Appendix C) | $250 (MA-cost — see Appendix C) |
| Total destructive-testing cost | 50 x $250 = $12,500.00 | 80 x $250 = $20,000.00 |

## Appendix B — The ANSI/ASQ Z1.4 Standard (Why These Are the Only Two Real Options)

Referenced in Background and Challenge 3 (D1). Renata cannot simply pick any sample size she likes — Alden's quality system requires every lot's sampling plan to come from a real, named acceptance-sampling standard, so the two options above are not arbitrary numbers, they are the standard's own published values.

| Lot size range | General Inspection Level I code letter | General Inspection Level II code letter | General Inspection Level III code letter |
|---|---|---|---|
| 281 to 500 [S1] | F [S1] | H [S1] | J [S1] |

**Modeling note:** General Inspection Level II is the standard's own default level for ordinary lots; Level III is a tightened level a quality system may specify when it wants more assurance for the same lot. Level I (a reduced level, cheaper still) exists in the standard but is not one of tonight's two loaded plans — Alden's own quality system does not permit Level I for this product family, a real internal constraint, not a choice Renata is making tonight.

## Appendix C — Real Contamination Data (Modeling Assumptions Below)

Referenced in Background and Challenge 3 (D2, D3, D4).

**Real, sourced figure — how often an average lot in this industry is actually out-of-spec:**

| | Value |
|---|---|
| Probability that a given production lot at a large-scale (1,000-liter-plus) biologics manufacturing facility is contaminated / out-of-spec in a given run | 2.3% [S3] |
| Estimated real-world cost when an out-of-spec lot is NOT caught before it reaches a customer's manufacturing line | $1,000,000 to $2,000,000 per incident [S3] |

**A note on scale:** a real, single-patient CAR-T (chimeric antigen receptor T-cell — a patient's own immune cells, genetically re-engineered outside the body to attack their disease, then infused back into that same patient) cell-therapy treatment — the same category of cell therapy this case's customer manufacturing line makes — carries a reported list price of roughly $373,000 to $475,000 per patient (for lymphomas -- cancers of the lymphatic system -- or leukemia -- a cancer of blood-forming tissue) [S4], before accounting for the cost of managing serious side effects, which can push the total past $1,000,000. That single-patient figure is several times larger than either sampling plan's entire destructive-testing cost ($12,500 or $20,000, Appendix A) and is itself a meaningful fraction of Appendix C's $1,000,000-$2,000,000 estimated cost of one undetected failed lot — real evidence that the stakes on Renata's screen are not abstract. Alden's own revenue and the customer's exact production volume are not publicly disclosed and are not asserted here.

## Modeling Assumptions

> The figures in this section are **not sourced**. They are stated scenario assumptions chosen by
> the case author because no manufacturer publicly discloses a unit-level defect rate for its own
> single-use consumables, no general figure exists for how much a specific supplier-flagged lot's
> risk should be assumed to rise above the industry-wide average above, and Lot 4471's own size is
> a scenario detail, not a disclosed real production figure. A Hero may challenge any of these
> numbers in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Fraction of individual units that are actually defective, inside a lot that IS out-of-spec | 2.5% | No manufacturer publishes a unit-level defect fraction for its own single-use consumables; this value is set within the range of Acceptable Quality Levels the ANSI/ASQ Z1.4 standard itself is built to test against for major/critical characteristics (the standard's own severity labels for a defect: a "critical" defect could cause harm or make the unit unsafe to use, a "major" defect would likely cause the unit to fail in normal use without necessarily being dangerous, and a "minor" defect — not tested against here — is a cosmetic or non-functional flaw). | Work through Challenge 3 (D3) at a much higher value than the one used here before assuming this is the case's fragile number — the answer may surprise you. |
| MA2 | Probability that Lot 4471 specifically is out-of-spec, GIVEN a supplier deviation notice has already flagged it — used only in Challenge 3's D4 scenario, not in the primary recommendation | 6% | A documented reason to suspect a specific lot (a supplier deviation notice on an incoming raw material) is real information a quality system is required to act on, but no published figure states exactly how much it should raise the odds for that one lot; this value is a deliberately moderate multiple of the industry-wide baseline above. MA1 (the 2.5% unit-level defect fraction) is held constant at its baseline value throughout the D4 elevated-risk scenario — MA2 changes only the probability that the lot itself is out-of-spec, not what fraction of units inside an out-of-spec lot are defective. | This is the assumption Challenge 3 (D4) asks you to test directly — see how far above the baseline it has to rise before your Challenge 2 recommendation would actually change. |
| MA-cost | Cost per unit destructively tested (Appendix A), and the specific dollar figure used within Appendix C's real $1,000,000-$2,000,000 sourced cost-of-escape range | $250 per unit tested; $1,400,000 used as the cost of an undetected escape | Alden does not publicly disclose its internal per-unit QC testing cost, so a representative figure is assumed. The $1,400,000 escape-cost figure is chosen toward the lower-middle of the real, sourced $1,000,000-$2,000,000 range [S3], since this case's undetected-defect scenario (a consumable-level defect reaching one customer's manufacturing run) is not necessarily the same severity as every incident behind that industry-wide range. | Not swept independently in this case's sensitivity check — see `sensitivity_model.py` for how it combines with MA1 and MA2. |

**MA3 — Lot 4471's size (500 units):** also not a disclosed real figure. It is chosen at the top
of the ANSI/ASQ Z1.4 standard's own real "281 to 500" lot-size band (Appendix B) specifically so
this case's two sampling plans are the standard's genuine Level II and Level III values for that
band, not an arbitrary pair of numbers.

## Appendix D — "How To…" Math Questions To Research

**Vocabulary terms**

- Population
- Sample
- Individual
- Sample Size
- Systematic Sampling
- Experiment
- Random
- Variability
- Dot Plot
- Probability
- Event
- Outcome

**"How to…" questions**

- How to determine the probability of a single event
- How to determine the probability of a compound event
- How to find the percent of a number

## Appendix E — Sources

All sourced (non-assumption) figures in this case are cited here.

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | ANSI/ASQ Z1.4-2003 Sample Size Code Letters (by lot size and General Inspection Level) and the Master Table's sample size per code letter | Lot size 281-500: Level I = F, Level II = H, Level III = J. Code letter H = 50 units; code letter J = 80 units. | ANSI/ASQ Standard Z1.4-2003, reproduced in an AQL (Acceptable Quality Level — see Appendix C's Modeling Assumptions) reference chart — Asia Quality Focus, "AQL Chart" (PDF) | standard dated 2003; chart accessed 2026-09-09 | HIGH |
| S2 | Zero acceptance number ("c = 0") sampling plans are a real, standard acceptance-sampling method used in regulated manufacturing, requiring less inspection than the corresponding full ANSI/ASQ Z1.4 plan for the same assurance level (how confident the plan makes a quality team that an accepted lot is actually good) | c = 0 (accept only if zero defective units are found in the sample) | William A. Levinson, "When and How to Use Zero Acceptance Number Sampling," Quality Digest | 2018-04-04 (accessed 2026-09-09) | MEDIUM |
| S3 | Large-scale (1,000-liter-plus) biomanufacturing facility batch contamination rate, and the real-world cost of a failed/contaminated biomanufacturing batch | Contamination rate: 2.3% of batches at large-scale facilities. Cost of a failed batch: "greater than $1-2 million" (Beth Junker, PhD, Senior Director of Bioprocess R&D, Merck Research Laboratories) | BioProcess International, "Biotech Facilities Average a Batch Failure Every 40.6 Weeks," citing the 5th Annual Report and Survey of Biopharmaceutical Manufacturing Capacity and Production (BioPlan Associates, 145 organizations surveyed worldwide) | 2008-09-01 (accessed 2026-09-09) | MEDIUM |
| S4 | Real-world list price of a single-patient CAR-T cell-therapy treatment (used only as a scale-and-stakes comparison, Appendix C's "A note on scale" — not a modeling input to any D2/D3/D4 calculation) | Kymriah and Yescarta: $373,000 per patient for adult lymphomas (cancers of the lymphatic system); Kymriah: $475,000 per patient for pediatric/young-adult leukemia (a cancer of blood-forming tissue); total cost (with side-effect management) can exceed $1,000,000 | KFF Health News, "Staggering Prices Slow Insurers' Coverage Of CAR-T Cancer Therapy" | accessed 2026-09-10 | HIGH — a health-policy newsroom's direct reporting of publicly disclosed drug list prices |

**A note on S3's age:** this is the most specific, directly-attributed, dollar-and-percentage
figure found for batch-level biomanufacturing contamination rates and failure costs — it is real,
named (Beth Junker, Merck), and dated, but it is an 18-year-old figure and no more recent public
equivalent with the same specificity was found (see `RESEARCH_LOG.md`). All of this case's S3-based
numbers are treated as a 2008-dated industry benchmark, not a current one — a Hero may reasonably
ask whether contamination rates and batch costs have moved since 2008, and that is itself a fair
discussion question this case does not resolve for them.

See `RESEARCH_LOG.md` for the full search trail, including a search that did NOT turn up a public,
company-specific single-use-consumable defect or leak rate (from Sartorius, Thermo Fisher, Cytiva,
or the BioPhorum/BPOG industry group), which is why MA1 exists as a stated assumption rather than a
citation.

## Appendix F — Learn More

Curious about the real-world manufacturing and quality-control world behind this case? These
resources go beyond what the challenges require.

| Resource | What it's for |
|---|---|
| [Manifold (fluid mechanics) — Wikipedia](https://en.wikipedia.org/wiki/Manifold_(fluid_mechanics)) | What a manifold assembly like Lot 4471's actually is: a branching fitting or network of tubing joining multiple inputs or outputs. |
| [Single-use bioreactor — Wikipedia](https://en.wikipedia.org/wiki/Single-use_bioreactor) | The flexible-bag bioreactor design used in the single-use manufacturing Background describes. |
| [Bioreactor — Wikipedia](https://en.wikipedia.org/wiki/Bioreactor) | The general category of vessel in which a biologic drug is grown. |
| [Biopharmaceutical — Wikipedia](https://en.wikipedia.org/wiki/Biopharmaceutical) | Background on "biologics," drugs manufactured from living cells. |
| [Cell therapy — Wikipedia](https://en.wikipedia.org/wiki/Cell_therapy) | The patient-specific treatment category the customer's manufacturing line in Overview produces. |
| [Acceptance sampling — Wikipedia](https://en.wikipedia.org/wiki/Acceptance_sampling) | The general statistical method (ANSI/ASQ Z1.4 is one real, published version of it) behind Renata's whole decision. |
| [Acceptable quality limit — Wikipedia](https://en.wikipedia.org/wiki/Acceptable_quality_limit) | The standard's own vocabulary for the worst tolerable defect rate, referenced by MA1's basis. |
| [Certificate of analysis — Wikipedia](https://en.wikipedia.org/wiki/Certificate_of_analysis) | The real document Renata signs to release a lot, described in Overview. |
| [Quality control — Wikipedia](https://en.wikipedia.org/wiki/Quality_control) | The general discipline this entire case sits inside. |
| ["Staggering Prices Slow Insurers' Coverage Of CAR-T Cancer Therapy" — KFF Health News](https://kffhealthnews.org/news/staggering-prices-slow-insurers-coverage-of-car-t-cancer-therapy/) | Real, reported per-patient CAR-T treatment costs (Appendix C's "note on scale," source S4), for a feel of what's actually riding on the customer's manufacturing line. |

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
