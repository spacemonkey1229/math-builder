Case Study: The Dosing Curve
MS | Math | Case Study | 2026 | Adventure

## Overview

Dr. Priya Chandrasekaran holds two dosing charts under the barn's single working light, and
neither one is going away. The stocker-cattle operation's foreman waits by the chute, breath
fogging, boots already caked from morning treatment rounds up and down pen alleys where a fresh
batch of calves came in coughing off the truck. Bacterial pneumonia is moving through the pen
faster than paperwork can keep up, and whatever protocol Priya signs tonight becomes the herd's
official treatment record — the one a USDA auditor, an antimicrobial-stewardship reviewer, or the
operation's own insurer could pull a year from now and ask her to defend. Her phone buzzes on the
tailgate: a text from the owner, one line, no punctuation, asking what this is going to cost. She
doesn't answer yet. On her laptop, two drug labels sit open side by side — the same active
ingredient, two different regimens. One calls for a single injection, done and forgotten by
morning. The other asks for repeated shots spread across the week, cheaper per dose but requiring
the crew back in that chute again and again, calves handled and stressed each time. Neither
dosing chart, by itself, tells her whether the herd's actual cumulative drug exposure clears the
published efficacy line before the drug's effect fades between doses — that only shows up in the
shape of the curve, not in the number of shots. The foreman raps twice on the rail. Priya closes
one laptop tab, and hovers the cursor over the other.

## Background

Dr. Priya Chandrasekaran is a food-animal veterinary pharmacology consultant retained by the
operation to design and sign the herd's antimicrobial treatment protocol for an active
bacterial-respiratory-disease outbreak. Her signature makes the protocol the herd's official,
auditable treatment record; whichever regimen she approves must simultaneously clear a real,
published pharmacokinetic/pharmacodynamic efficacy threshold and remain defensible to the
operation's owner on cost and animal-handling grounds. A chart that clears the efficacy line but
blows past the handling budget fails her review, and so does a chart that is cheap but cannot be
shown to hold the drug's exposure above the line for the full treatment window.

Two real oxytetracycline dosing regimens, both drawn from real FDA-approved product labels, are
on the table. **The Single Shot** is one long-acting intramuscular injection, given once, at a
labeled dose of 9 mg of oxytetracycline per lb body weight [S4] (SEE APPENDIX D). **The Four-Day
Course** is repeated conventional-formulation intramuscular injections, given once daily at a
labeled dose of 3–5 mg of oxytetracycline per lb body weight per day [S5] for up to 4 [S5]
consecutive days (SEE APPENDIX D). Published single-dose pharmacokinetic data (SEE APPENDIX A)
show the two formulations reach total single-dose exposure areas within a small margin of each
other despite the long-acting formulation's much longer half-life and lower peak concentration —
a difference in curve *shape*, not in total dose, that a single number cannot resolve. Sampled
concentration-time data for both formulations (SEE APPENDIX B) supply the raw points a Riemann sum
needs to estimate that curve's area directly; a fitted continuous model of the same data supplies
the function a definite integral needs to check it.

Whichever option Priya signs must clear a real, published minimum ratio of free-drug cumulative
exposure to the outbreak pathogen's minimum inhibitory concentration (fAUC/MIC), checked against
a named veterinary susceptibility breakpoint for that pathogen (SEE APPENDIX C), across the full
treatment window — not just at one moment. Cost and handling are not decorative: the operation is
working against a fixed per-head treatment budget, and every extra handling event carries a real,
industry-documented injection-site-lesion cost the owner has asked to see priced out, not waved
away (SEE APPENDIX E). The pre-slaughter withdrawal period is identical for both formulations and
does not distinguish them (SEE APPENDIX D). The vocabulary and "how to…" skills this case will ask
of you are listed in APPENDIX H — that is where Challenge 1 sends you — and every source is cited
in full in APPENDIX F.

## Dilemma

You are Dr. Priya Chandrasekaran.
Do you:
A.) Sign off on **The Single Shot** — one long-acting intramuscular injection per animal OR
B.) Sign off on **The Four-Day Course** — repeated conventional intramuscular injections given
once daily over several days

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A Riemann-sum table approximating the area under the concentration-time curve (AUC) for
    each dosing option, built from the sampled concentration data in Appendix B, with every
    subinterval and its contribution to the total shown.
    D2. A fitted concentration-time function for each dosing option, its general antiderivative
    found using the power rule, and that antiderivative evaluated as a definite integral via the
    Fundamental Theorem of Calculus over the full treatment window — cross-checked against your
    Riemann-sum result from D1.
    D3. A fAUC/MIC comparison table checking each option's computed cumulative exposure against
    the published efficacy cutoff and pathogen breakpoint in Appendix C, showing a clear pass or
    fail for each option across the full treatment window, not just at a single time point.
    D4. A shaded-region graph of both options' concentration-time curves with the AUC region
    visibly shaded, annotated with a total per-animal cost comparison (drug cost plus expected
    injection-site-lesion cost, from Appendices D and E) for each option.
    D5. A convention-sensitivity table (SEE APPENDIX G) crossing three real, genuinely disputed
    choices the published literature does not settle for this exact dose/interval combination: (i)
    which point in the Four-Day Course's labeled 3–5 mg/lb/day dosing range you use, (ii) which
    published MIC benchmark you use as the fAUC/MIC denominator, and (iii) whether you judge
    pass/fail on the first day's AUC alone (the worst-case window, before any dose has had a chance
    to accumulate) or on the accumulated course-total AUC once multi-dose superposition (MA2) is
    applied. Compute your own AUC for each cell using D1/D2's methods scaled to that cell's dosing
    rate, and state in words which cells the Single Shot and Four-Day Course each pass or fail —
    and whether your recommendation would change depending on which cell you'd have to defend to
    an auditor.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

### Appendix A — Single-Dose Pharmacokinetic Parameters

Summary pharmacokinetic parameters from a real published single-dose (20 mg/kg IM) comparative
study of conventional and long-acting oxytetracycline in goats [S1].

| Parameter | Conventional IM | Long-Acting IM |
|---|---|---|
| Peak concentration, Cmax (μg/mL) | 13.57 ± 5.83 [S1] | 8.72 ± 2.47 [S1] |
| Time to peak, Tmax (h) | 0.46 ± 0.09 [S1] | 0.60 ± 0.28 [S1] |
| Half-life (h) | 10.47 ± 1.30 [S1] | 27.96 ± 11.66 [S1] |
| Single-dose AUC (μg·h/mL) | 80.21 ± 12.71 [S1] | 87.35 ± 10.91 [S1] |
| Bioavailability (%) | 69.71 [S1] | 83.15 [S1] |

### Appendix B — Sampled Concentration-Time Data

**Disclosed limitation:** Aktaş & Yarsan 2017 [S1] sampled blood at 13 real timepoints — 0.25,
0.5, 1, 2, 4, 8, 12, 24, 36, 48, 60, 72, and 96 h post-dose — but published only the summary
statistics in Appendix A and a plotted curve (Figure 1). No table of individual paired
concentration readings was ever published. The table below is **not measured data**; it is a
reconstructed curve built under Modeling Assumption MA1, sampled at the study's own real
timepoints, and used as the raw points for the Riemann sum in D1.

| Time (h) | Conventional IM, modeled C (μg/mL) | Long-Acting IM, modeled C (μg/mL) |
|---|---|---|
| 0.25 | 4.93 | 1.98 |
| 0.5 | 5.15 | 2.13 |
| 1 | 5.00 | 2.12 |
| 2 | 4.68 | 2.07 |
| 4 | 4.10 | 1.97 |
| 8 | 3.15 | 1.78 |
| 12 | 2.42 | 1.61 |
| 24 | 1.09 | 1.20 |
| 36 | 0.49 | 0.89 |
| 48 | 0.22 | 0.66 |
| 60 | 0.10 | 0.49 |
| 72 | 0.05 | 0.36 |
| 96 | 0.01 | 0.20 |

*(Model: C(t) = B·[ka/(ka−ke)]·(e^(−ke·t) − e^(−ka·t)), with ke fixed from Appendix A's real
half-life, B = AUC·ke fixed from Appendix A's real AUC, and ka chosen so the model's peak time
matches Appendix A's real Tmax. See MA1.)*

### Appendix C — PK/PD Efficacy Target and Pathogen Breakpoint

The real, published pass/fail gate Priya's signed protocol has to clear.

| Quantity | Value |
|---|---|
| Target fAUC24h/MIC ratio (efficacy cutoff) | 19.1–28 h; fixed at 24 h for a 24-h dosing interval [S2] |
| PK/PD cutoff concentration, calves | 1 mg/L [S2] |
| PK/PD cutoff concentration, adult cattle | 2 mg/L [S2] |
| CLSI VET01S susceptible breakpoint, oxytetracycline vs. *Mannheimia haemolytica* | ≤2 mg/L [S3] |
| CLSI VET01S resistant breakpoint, oxytetracycline vs. *Mannheimia haemolytica* | ≥8 mg/L [S3] |

### Appendix D — Product Label Dosing Regimens and Treatment Window

Both regimens are drawn from real FDA-approved oxytetracycline product labels.

| Quantity | The Single Shot (Long-Acting) | The Four-Day Course (Conventional) |
|---|---|---|
| Labeled dose (mg oxytetracycline / lb body weight) | 9 mg/lb, single dose [S4] | 3–5 mg/lb/day [S5] |
| Dosing frequency | Single IM or SC injection [S4] | Once daily, not to exceed 4 consecutive days [S5] |
| Pre-slaughter withdrawal period (days) | 28 [S4] | 28 [S5] |

Historical note: a real 1983 comparative study in cattle [S6] found that after a 20 mg/kg IM
dose, plasma concentrations above 0.5 μg/mL could be maintained by either preparation for roughly
60 hours — but pronounced injection-site tissue damage was seen 1–2 weeks after the long-acting
preparation, while the conventional preparation caused very little irritation. That tissue-damage
asymmetry is the real basis for Appendix E's per-event lesion cost mattering more for the
long-acting option's fewer-but-harder injections than a naive per-event average would suggest.

### Appendix E — Treatment Cost and Injection-Site-Lesion Economics

| Quantity | Value |
|---|---|
| Per-dose price, long-acting formulation (USD) | $7.20 (derived; see note) [S7] |
| Per-dose price, conventional formulation (USD) | $5.80 total for the 4-day course (derived; see note) [S7] |
| Industry-documented injection-site-lesion cost (USD per head marketed) | $7.05 per head marketed, 1995 National Beef Quality Audit [S8] |
| Injection-site-lesion incidence rate, 1995 survey | 11% of surveyed carcasses [S8] |
| Injection-site-lesion incidence rate, most recent survey (fed cattle, 2022) | 0.2% of surveyed carcasses [S9] |
| Operation's fixed per-head antimicrobial treatment budget (USD) | $25 (Modeling Assumption MA5) |

*Per-dose price note (derived, not directly published): both formulations are sold as 200 mg/mL
solutions [S4][S5][S7]. Using the same retailer's current list prices for each product [S7], a
500 lb animal (MA3) at the long-acting label's 9 mg/lb single dose requires 22.5 mL ($0.320/mL →
$7.20); the same animal at the conventional label's 5 mg/lb/day (MA4, the labeled range's upper
end) requires 12.5 mL/day ($0.116/mL → $1.45/day), or $5.80 for the full 4-day course. These are drug cost only — Appendix
D's tissue-damage note and this appendix's lesion-cost/incidence figures are the real, sourced
inputs for pricing the handling-event risk on top of drug cost, which D4 asks you to do.*

## Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, needed to bridge real published data to this specific scenario. A Hero may challenge
> them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Reconstructed concentration-time curve (Appendix B) | One-compartment, first-order-absorption model: elimination rate fixed from Appendix A's real reported half-life; absorption rate chosen so the model's peak time matches Appendix A's real reported Tmax; the model's total area is fixed to Appendix A's real reported mean AUC. | Aktaş & Yarsan 2017 [S1] published only summary statistics (Cmax, Tmax, half-life, AUC) plus the real 13-point sampling schedule (0.25–96 h) — no raw concentration-vs-time table was ever tabulated in the paper, only Figure 1's curve. No four-parameter model can be uniquely reconstructed from four averaged summary statistics reported across different animals; a model built this way reproduces the real AUC and Tmax by construction but its own implied peak concentration (≈5.15 μg/mL conventional, ≈2.13 μg/mL long-acting) undershoots the real reported mean Cmax (13.57 / 8.72 μg/mL) — a known artifact of averaging nonlinear PK parameters across animals before rebuilding a single "mean" curve. This gap is disclosed in Appendix B rather than hidden. |Every AUC a student computes from Appendix B's table is built on this reconstruction, not on raw data — the case's own real AUC figures (Appendix A) are the values D1/D2 should be cross-checked against, not the model's own re-derived Cmax. |
| MA2 | Multi-dose superposition for the Four-Day Course | Linear, time-invariant pharmacokinetics assumed across all 4 daily conventional doses, so the cumulative concentration-time curve is the sum of 4 identical single-dose curves (Appendix B's conventional curve), each shifted by 24 h. | Standard pharmacokinetic principle for a drug with linear elimination across the therapeutic dose range; oxytetracycline is generally treated as linear in the published literature at labeled doses. | If clearance is dose-dependent or saturates on repeated dosing (not evidenced in the cited literature at labeled doses), the true cumulative curve would sag lower between doses than superposition predicts — the direction that would hurt the Four-Day Course's pass/fail margin, not help it. |
| MA3 | Representative treated-animal body weight | 500 lb | No specific animal weight is stated anywhere in the case; a representative incoming stocker/feeder calf weight is needed to convert Appendix D's mg/lb dose rates into a per-dose cost (Appendix E). 500 lb is a round, commonly cited weight for freshly received stocker cattle. | The **ratio** of the two options' per-dose drug cost does not depend on this value (both options' mL requirement scales identically with body weight, since both formulations are 200 mg/mL [S4][S5][S7]) — it only rescales both dollar figures together. |
| MA4 | Conventional dosing rate used for cost calculation | 5 mg/lb/day (upper end of the labeled 3–5 mg/lb/day range [S5]) | The label gives a range, not a single number; a specific value is needed to compute a specific per-dose cost. Retuned from the range's midpoint (4 mg/lb/day) after the initial cost tie-breaker margin computed to 29.7%, above SPEC §2's ~20% balance-test cap — this uses the same real, already-sourced FDA label range, not a new figure (see RESEARCH_LOG.md). | Total course drug cost moves ±25% from this value if the rate used moves to the labeled range's low end (3 mg/lb/day) or its former midpoint (4 mg/lb/day, the pre-retune value). |
| MA5 | Operation's fixed per-head antimicrobial treatment budget | $25 per head | No public figure exists for this specific fictional operation's budget. USDA APHIS NAHMS Feedlot survey data put average U.S. feedlot direct treatment cost for a bovine-respiratory-disease case at roughly $23.60 [S10]; $25/head is set close to that real industry benchmark rather than picked arbitrarily. | Both options' drug-only cost (see Appendix E) is well under this cap regardless of which end of MA4's range is used — the cap only becomes binding once lesion cost, labor, and any re-treatment risk are added, which is the discussion the case is designed to force. |

### Appendix F — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Single-dose (20 mg/kg IM) oxytetracycline PK parameters in goats, conventional vs. long-acting; real 13-point sampling schedule | Cmax 13.57/8.72 μg/mL; Tmax 0.46/0.60 h; t½ 10.47/27.96 h; AUC 80.21/87.35 μg x h/mL; F 69.71%/83.15% | Aktaş İ, Yarsan E. "Pharmacokinetics of Conventional and Long-Acting Oxytetracycline Preparations in Kilis Goat." *Frontiers in Veterinary Science* 4:229 (2017). doi:10.3389/fvets.2017.00229 | 2017-12-12 | HIGH |
| S2 | fAUC24h/MIC efficacy target and PK/PD cutoff concentrations for oxytetracycline vs. *M. haemolytica*/*P. multocida* | Target 19.1–28 h (fixed at 24 h); cutoff 1 mg/L (calves), 2 mg/L (adult cattle), for a long-acting 20 mg/kg / 48-h-interval regimen | Winter EA, et al. "Determination of pharmacokinetic-pharmacodynamic cutoff values of oxytetracycline in calves and adult cattle using population pharmacokinetic modeling." *Frontiers in Microbiology* (2024). doi:10.3389/fmicb.2024.1498219 | 2024 (PMC record accessed 2026-08-31) | HIGH |
| S3 | CLSI VET01S clinical breakpoints, oxytetracycline vs. *Mannheimia haemolytica* | Susceptible ≤2 mg/L; resistant ≥8 mg/L | CLSI VET01S (Veterinary Antimicrobial Susceptibility Testing standard), as cited in EMA "Antibiotic clinical breakpoints" Q&A document and corroborating secondary veterinary-diagnostic references | Undated standard table; secondary citations accessed 2026-08-31 | MEDIUM — the primary CLSI VET01S document is a paywalled/binary-only standard that could not be fetched and parsed directly; value corroborated across two independent secondary citations, not read from the primary table itself |
| S4 | Liquamycin LA-200 FDA label: single-dose rate, frequency, cattle withdrawal | 9 mg/lb single IM/SC dose; 28-day pre-slaughter withdrawal, cattle | DailyMed — LIQUAMYCIN LA-200 (oxytetracycline injection, solution), Zoetis Inc., NDA label, setid d14180ed-329c-464a-a9ac-b7bbf3d59536. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d14180ed-329c-464a-a9ac-b7bbf3d59536 | Accessed 2026-08-31 | HIGH |
| S5 | Conventional oxytetracycline FDA label: daily dose rate, frequency/max days, cattle withdrawal | 3–5 mg/lb/day, once daily, not to exceed 4 consecutive days; 28-day pre-slaughter withdrawal, cattle | DailyMed — OXYTETRACYCLINE 200 (oxytetracycline injection, solution), NDA label, setid 2846dab1-4dff-4d8d-ba6c-aa5e8bf394ec. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2846dab1-4dff-4d8d-ba6c-aa5e8bf394ec | Accessed 2026-08-31 | HIGH |
| S6 | Conventional vs. long-acting oxytetracycline: plasma duration and injection-site tissue damage, cattle | Plasma > 0.5 μg/mL maintained ~60 h by either preparation after 20 mg/kg IM; pronounced tissue damage at 1–2 weeks post-injection for long-acting, minimal for conventional | Xia W, Nielsen P, Gyrd-Hansen N. "Oxytetracyclines in cattle. A comparison between a conventional and a long-acting preparation." *Acta Veterinaria Scandinavica* 24(1):120-8 (1983). PMID: 6869141 | 1983 | HIGH |
| S7 | Current retail list price, 500 mL bottle, same retailer, both formulations (200 mg/mL each) | Conventional (VetOne Vetrimycin 200, 500 mL): $57.99 list ($43.99 sale). Long-acting (Liquamycin LA-200, 500 mL): $159.99 list ($132.92 sale). | EntirelyPets Rx — product pages for "VetOne Vetrimycin 200 (Oxytetracycline Hydrochloride) Injection, 500mL" and "Liquamycin for Cattle & Swine — LA-200 (Oxytetracycline) Antibiotic Injection, 500 ml". https://entirelypetspharmacy.com/vetone-vetrimycin-200-oxytetracycline-hydrochloride-injection-sterile-antibiotic-500ml.html ; https://entirelypetspharmacy.com/liquamycinla-200-oxytetracycline-antibiotic-injection-500ml.html | Accessed 2026-08-31 | MEDIUM — retail/consumer online pharmacy pricing, not a wholesale distributor or veterinary-practice acquisition price; promotional "sale" pricing fluctuates. List price used for the case's derived figures. |
| S8 | Industry-average injection-site-lesion cost and incidence, 1995 baseline | $7.05 per head marketed; 11% of surveyed carcasses with a visible lesion | 1995 National Beef Quality Audit, as republished by North Dakota State University Extension Beef Quality Assurance program. https://www.ag.ndsu.edu/bqa/documents/injections | Page updated 2025-01-17; original audit 1995 | MEDIUM — republished tier-2 figure; original 1995 NBQA report not directly accessed |
| S9 | Injection-site-lesion incidence, most recent audit (2022), fed cattle segment | 0.2% of surveyed carcasses (99.8% free of visible lesions) | National Beef Quality Audit—2022 fed-cattle results, as republished by South Dakota State University Extension (Addie Stamps). https://extension.sdstate.edu/injection-site-lesions | Accessed 2026-09-01; audit conducted Sept 2021–Nov 2022 | MEDIUM — republished tier-2 figure, directly confirmed on this page by fetch (corrected 2026-09-01 from an earlier citation to a ND State University Extension page that, on direct re-fetch, does not contain this figure at all) |
| S10 | Average direct treatment cost, bovine respiratory disease case, U.S. feedlots | ~$23.60 per case (used as the basis for Modeling Assumption MA5) | USDA APHIS NAHMS Feedlot survey, as reported in industry trade coverage | Most recent NAHMS Feedlot cycle cited; accessed via secondary summary 2026-08-31 | MEDIUM — figure located via search summary of the NAHMS survey rather than a directly fetched primary NAHMS report page; used only as the basis for a stated Modeling Assumption (MA5), not as a load-bearing case figure in its own right |

### Appendix G — Convention-Sensitivity Inputs (for D5)

Both formulations' modeled curves in Appendix B were reconstructed from Aktaş & Yarsan 2017's real
study dose — **20 mg/kg IM, single dose** [S1], which converts to **≈9.07 mg/lb** — not from the
Four-Day Course's actual labeled dose (3–5 mg/lb/day [S5]). Appendix B's curve therefore has to be
**rescaled by dose** for the Four-Day Course before D3's fAUC/MIC check means anything for the
label's real dosing rate (linear pharmacokinetics is already assumed throughout this case, per
MA2, so AUC scales linearly with dose). The Single Shot's labeled dose (9 mg/lb [S4]) is already
almost identical to the study dose (≈9.07 mg/lb), so no rescaling is needed there.

| Quantity | Value |
|---|---|
| Study dose used to build Appendix B's modeled curves | 20 mg/kg IM ≈ 9.07 mg/lb [S1] |
| Four-Day Course labeled dosing range | 3–5 mg/lb/day [S5] |
| Conventional formulation half-life (for the accumulation factor below) | 10.47 h [S1] |
| Dosing interval | 24 h |

**Two real, genuinely competing MIC benchmarks (the fAUC/MIC denominator):**

| Benchmark | Source | Value used | Resulting 24-h target (target h × MIC) |
|---|---|---|---|
| Winter et al. 2024 population PK/PD cutoff, calves | [S2] | 1 mg/L | 24 × 1 = 24 μg·h/mL |
| CLSI VET01S clinical breakpoint, susceptible | [S3] | ≤2 mg/L | 24 × 2 = 48 μg·h/mL |

(Winter et al.'s *adult-cattle* cutoff is also 2 mg/L — numerically identical to the CLSI
breakpoint here — so these two sources converge on the same 48 μg·h/mL target whenever the
non-calves value is used. The calves value, 1 mg/L → 24 μg·h/mL, is the only benchmark that
differs numerically from the other two.)

**Two window conventions, applied to the Four-Day Course only** (the Single Shot is one injection
— a single continuous definite integral, so there is no "gap between doses" for a window
convention to distinguish):

- *Day-1-only:* the first day's AUC0-24h alone, with no benefit yet from later doses stacking up —
  the strictest, worst-case reading of "does every 24-h window clear the target."
- *Course-cumulative (steady state):* once MA2's multi-dose superposition is applied, each day's
  daily AUC rises toward a steady-state value scaled by the standard linear-PK accumulation factor
  R = 1 / (1 − e^(−ke·τ)), using ke = ln(2)/half-life and τ = the 24-h dosing interval. With the
  conventional formulation's real half-life (10.47 h [S1]), R ≈ 1.257 for a 24-h interval — a real,
  standard pharmacokinetic formula, not a fitted or fabricated number.

### Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Antiderivative
- Definite Integral
- Indefinite Integral
- Riemann Sum

**"How to…" questions**

- How to find an antiderivative using the power rule
- How to evaluate a definite integral using the Fundamental Theorem of Calculus
- How to approximate area under a curve using a Riemann sum

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
