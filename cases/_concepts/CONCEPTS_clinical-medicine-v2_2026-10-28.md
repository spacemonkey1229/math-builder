# CONCEPTS v2 — Clinical Medicine (clinical-medicine) — 2026-10-28

Revision of `CONCEPTS_clinical-medicine_2026-10-27.md` after R1 round 1 (R1a/R1b/R1c). **Single concept kept: C3 The Flat Dose (re-tiered T4).** The v1 lead, C1 The Pool Size, was tried first and abandoned; the reason is in "Why C1 was dropped" below, with recomputed numbers. Every figure below was recomputed on 2026-10-28 in Python from files fetched that day (CDC NHANES P_ files HTTP 200; openFDA label API; CDC data.cdc.gov `seuz-s2cv`, rowsUpdatedAt 2026-10-23). Scratch scripts live in the session scratchpad, not the repo.

**Margin convention (stated once, applied to every margin in this sheet): margin = (loser's value - winner's value) / winner's value** on the primary metric, where lower mg drawn is better. This is the SPEC §2 20% test.

---

## Why C1 (The Pool Size) was dropped (R1a blocking + R1c twin finding)

1. **Protocol lock repairs the math but not the stake.** With individual testing and mid-season switching barred, pool 5 vs pool 10 still computes as v1 said, but on the CDC flu series (`seuz-s2cv`, values as published 2026-10-23): break-even closed form q=(1-p)^5 satisfies q^2-q+0.1=0, q=(1+sqrt(0.6))/2=0.88730, **p*=2.363%** (verified: E(5,p*)-E(10,p*) = 0). Season sums of E=1/k+1-(1-p)^k per sample, gap/winner: 2022-23 (53 wk) B wins 2.04% (A 20.144, B 19.742); 2023-24 A wins 7.81% (22.869 vs 24.656); 2024-25 A wins 2.95% (23.649 vs 24.346); 2025-26 A wins 5.65% (23.903 vs 25.253). (v1 divided by the loser, so its "7.3 / 2.9 / 5.3" figures were smaller; under this sheet's convention they are 7.8 / 2.9 / 5.6.)
2. **A patient-facing consequence kills the balance.** The honest patient cost of pooling is that every member of a positive pool waits one more run for a result. Share of samples so delayed, 2022-23 weekly mean: pool 5 = 18.3%, pool 10 = 27.6%. Pool 5 is better on delay in every week and on tests in most seasons, so adding the delay as a labeled input makes A dominant. Priced into one metric, B is only better if a one-day delay is worth less than **0.081 of one PCR test** (0.402 tests saved per sample-season vs 4.95 extra delayed sample-weeks), a value nobody could defend. Dropping the delay restores balance but leaves exactly the R1c objection: no patient stake, and a per-kit scarcity metric in the same domain family as The Overlap Call.
3. **Honest differentiation from The Overlap Call is not available at acceptable cost.** The lesson differs mathematically (two-stage expected value vs union/intersection), but the decision shape (stretch scarce test kits, judged per kit) and the stake do not. R1c's instruction was to switch if we could not differentiate honestly; we switch.

(Side finding for the record: best-of-{pool 5, pool 10, individual} chosen week by week on 2022-23 data costs 18.08 tests per sample vs 19.74 for the best fixed pool, an 8.4% gain from adaptivity, which is why R1a's "switch weekly" objection was correct.)

---

## C3 — The Flat Dose   ·   tier T4   ·   data HIGH (weights, label) / ASSUMPTION (vial-reuse f, disclosed)

### Protagonist
**Beatrix Lindqvist** (constructed; disclosed as a composite), chief oncology pharmacist at a regional cancer center. Name checked: no match for "Beatrix" or "Lindqvist" anywhere under the project tree. Not Priya, Mara, Okafor, or Raman. She writes the adult dosing policy for the center's formulary monoclonal antibody and signs the monthly drug-spend report; the nurses in the infusion suite will carry out whatever she writes.

### Story seed (Overview material; ends at the instant of decision, not on a buzzing phone)
Thursday 6:40 a.m., the compounding room. Nine infusion chairs on the whiteboard, nine names, nine weights taken at the last visit and written in grease pencil. Beatrix is standing at the biosafety cabinet with a 100 mg vial in each gloved hand, turning them so the light catches the label, when the technician asks the question she has been putting off for a month: which dose sheet does he print for Thursdays from now on, the single "200 mg" line, or the one with a mg/kg column and a leftover box at the bottom? The vials in her hands are the same either way. The sheet is not. (Overview carries no numbers; the Background and appendices do.)

### Real / recognizable story (explicit constructed framing)
Current FDA labeling for pembrolizumab (KEYTRUDA, IV) gives adults 200 mg every 3 weeks, and for pediatrics **2 mg/kg (up to 200 mg)** every 3 weeks, supplied as 100 mg/4 mL single-dose vials, with the instruction "Discard any unused portion left in the vial" (openFDA drug-label API, label effective 2026-07-10, fetched and read 2026-10-28; the DOSAGE AND ADMINISTRATION highlights line and Section 2 preparation text). The case is **not** about that drug's real adult regimen. It uses a generic "Antibody X" and a **constructed hypothetical adult policy of 2 mg/kg**, to compare two dosing styles that both exist in real oncology practice. Cite the label only in the appendix, as the origin of the 100 mg vial size, the flat-dose pattern, the pediatric cap, and the discard instruction. State plainly in the case that the real adult label is flat and that nothing here is clinical advice or a claim about which regimen is clinically better.

### Dilemma (binary)
**A.)** Flat 200 mg for every adult (always exactly two 100 mg vials) OR **B.)** Weight-based 2 mg/kg of the patient's actual weight, drawn from whole 100 mg vials, with the leftover in each last-opened vial partly reusable for another patient.

### Primary metric
**Mean mg of drug drawn from pharmacy stock per adult dose** (lower is better). For option B: mg drawn per dose = d + (1 - f)(V - d), where d = 2 x weight (mg administered), V = vials opened x 100 mg, and **f = share of the leftover in an opened vial that the pharmacy reuses for another patient**. Option A: 200 mg flat, no waste. Patient-facing consequence (labeled input, not part of the metric, must appear in the pitch): **dose accuracy against the policy's own 2 mg/kg target.** See "Patient-facing consequence".

### Why it's close, and what the student must assume (T4)
Weight-based dosing administers less drug (mean 166.7 mg vs 200 mg) but whole-vial rounding means each dose opens 2.18 vials on average, so stock drawn is 218.4 mg unless leftovers get reused. The winner flips on one pharmacy-operations parameter, f, which **no dataset supplies**. The case states f as an explicit **Modeling Assumption the student must choose and defend** inside [0, 1], with only two anchors given: (i) the manufacturer label says discard (anchor f = 0); (ii) some sterile-compounding standards allow a punctured single-dose vial to be reused within a short beyond-use window if entered only in ISO Class 5 air (secondary sources say 12 hours under current USP <797>, 6 hours under older versions; official USP text **not** verified, see Still open). The case does not endorse vial sharing; it asks which f is defensible and what it would take to reach it (batching patients by day, compounding order, scheduling).

### Computed (code, on the data below)
**Population:** NHANES 2017-March 2020 pre-pandemic files `P_DEMO.xpt` + `P_BMX.xpt`; adults age >= 18 (RIDAGEYR; ages 80+ are top-coded at 80 in NHANES) with non-missing BMXWT; **n = 8,811**; unweighted (disclosed). Mean 83.33 kg, median 79.6 kg; survey-weighted mean 83.98 kg (WTMECPRP).

**Hand-computable band table (vial count depends only on 50-kg bands, because 2 mg/kg x 50 kg = 100 mg):**
| Weight band (kg) | Adults | Vials opened | Sum of weights (kg) |
|---|---|---|---|
| up to 50 | 273 | 1 | 12,629.3 |
| over 50 to 100 | 6,778 | 2 | 511,940.9 |
| over 100 to 150 | 1,633 | 3 | 188,318.0 |
| over 150 to 200 | 118 | 4 | 19,389.2 |
| over 200 to 250 | 8 | 5 | 1,707.4 |
| over 250 | 1 | 6 | 254.3 |

From the table: mean vial mg V-bar = 218.43 mg (sum of count x vials x 100 / 8,811); mean exact dose d-bar = 2 x mean weight = 166.66 mg.

- **Exact-dose mean (f = 1): 166.66 mg.** Whole-vial, no reuse (f = 0): 218.43 mg.
- Mean drawn for B at f: 166.66 + (1 - f)(218.43 - 166.66) = 218.43 - 51.77 f. **Break-even f\* = (218.43 - 200)/(218.43 - 166.66) = 0.356** (one-variable linear equation; bootstrap 95% CI for f\* from resampling adults: 0.337 to 0.376; survey-weighted f\* = 0.379).
- Margins, gap/winner: f = 0: A wins by **9.22%** (218.43 vs 200). f = 0.25: A wins 2.74% (205.49). f = 0.356: tie. **Reference case f = 0.5: B wins by 3.87%** (192.55 vs 200; 95% bootstrap CI on B at f = 0.5 is 191.6 to 193.6, so sampling error is much smaller than the f effect). f = 0.75: B wins 11.35% (179.61). f = 1: B wins **20.00%**, the edge of the SPEC band, so the case should state that f = 1 is not a defensible operating assumption (it requires zero residue, ever) and cap the student's range at f <= 0.9 (B = 171.84 mg, B wins 16.4%). **Primary-metric margin reported in case.json: 3.87% at reference f = 0.5; range 9.22% (A) to 16.4% (B) over f in [0, 0.9].** All within the 20% band.
- **Cap note (R1: add the label's 200 mg cap):** the real pediatric label caps 2 mg/kg at 200 mg. If B is capped at 200 mg the dilemma collapses: mean drawn becomes 196.90 / 177.96 / 159.02 mg at f = 0 / 0.5 / 1, so B beats A at **every** f and the case has no fork. The case therefore states, as a Modeling Assumption, that the constructed adult policy is **uncapped** (as many weight-based antibody regimens are), and records the cap and the collapse in the appendix and facilitator notes. This is a deliberate design choice, disclosed, not a hidden one.
- **Subgroups (real, unweighted):** women (n 4,525, mean 78.4 kg) f\* = 0.207; men (n 4,286, mean 88.6 kg) f\* = 0.532; ages 18-39 f\* = 0.342, 40-59 f\* = 0.470, 60+ f\* = 0.266. A center's case-mix moves the break-even a lot; use as a discussion extension. Caveat the case must state: NHANES is the general US adult population, **not cancer patients** (weight loss in cancer is common; the real infusion population's weight distribution is UNVERIFIED and may differ).
- **Spread/outliers:** five-number summary 32.6 / 67.2 / 79.6 / 95.5 / 254.3 kg (quartiles by the linear-interpolation convention; state the convention in the case); IQR 28.3; upper fence Q3 + 1.5 IQR = 137.95 kg with **217** adults above it; no adults below the lower fence (24.75 kg). 20.0% of adults weigh over 100 kg (where 2 mg/kg exceeds 200 mg).

### Patient-facing consequence (labeled input, per R1c)
Under the flat dose, relative to the policy's own 2 mg/kg target: **37.8%** of adults land within +/-20% (1.6 to 2.4 mg/kg); **56.7%** receive more than 120% of target (weight below 83.3 kg); **5.5%** receive less than 80% (weight above 125 kg); 5th to 95th percentile of delivered dose 1.58 to 3.80 mg/kg. Women: 29.4% within band; men: 46.6%. Under B, every patient receives exactly the target dose (100% within band), because the leftover is discarded or reused, not given. Nobody in the case is told the target is clinically optimal; the point for the pitch is that the policy must say who it is willing to give more or less than its own target, and whether the saving is worth the extra handling (a nurse-facing and pharmacist-facing error risk of mg/kg arithmetic, and a contamination-control burden if vials are shared, neither of which is quantified here and both of which the student should name as unpriced). This gives each option a real defender: A for simplicity, label compliance (f = 0 by label) and no sharing risk; B for accuracy to target and for savings once reuse is real.

### Deliverables (Challenge 3 forces the spine skills)
1. **D1 Weight spread.** Box-and-whisker plot of the 8,811 adult weights from the five-number summary, with the upper fence computed and the 217 outliers identified; one sentence on why the plot, not the mean alone, matters for a vial-based policy. (How to create a box and whisker plot; Quartiles; Outlier.)
2. **D2 Band-to-vials table.** From the weight-band table, show that 2 mg/kg x 50 kg = 100 mg is why bands are 50 kg wide, compute mean vial mg (218.43) and mean exact dose (166.66) with arithmetic shown. (Mean.)
3. **D3 Break-even.** Write mg drawn for B as a function of f and solve for the f where it equals 200 mg, by hand. (How to solve a multi-step equation with a variable on one side.)
4. **D4 Decision table at the student's own f.** State and defend one f in [0, 0.9] with a sentence citing the label's discard instruction and the pharmacy's own batching ability; give mg drawn per dose for A and B and the margin using the sheet's convention; add one other f to show sensitivity.
5. **D5 Accuracy table.** Share of adults within +/-20% of 2 mg/kg under A, and one sentence on whether the saving justifies the accuracy gap or the reverse.

### Skills the deliverables genuinely force (5 ids, all verified present in `readmodel/standards_spine.json` on 2026-10-28)
| id | kind | n now | forced by |
|---|---|---|---|
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data | how-to | 1 | D1 |
| statistics-and-probability-quartiles | term | 3 | D1 (fence needs Q1, Q3, IQR) |
| statistics-and-probability-outlier | term | 5 | D1 (217 above the fence) |
| statistics-and-probability-mean | term | 28 | D2 |
| advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-one-side | how-to | 4 | D3 |

New coverage (n<=2 before): the box-and-whisker how-to only (1 skill, score 1.0). No other skills claimed; "Box And Whisker Plot" (term), percent and unit-conversion skills may be added at case-write if the deliverables use them, not claimed here. Split risk: NONE (5 ids).

### Data and feasibility (fetched 2026-10-28)
| Claim | Value | Source | Grade |
|---|---|---|---|
| Adult weights | 8,811 adults, mean 83.33 kg | `https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/P_BMX.xpt` and `P_DEMO.xpt` (both HTTP 200; public domain US government data) | HIGH |
| 100 mg/4 mL single-dose vial; flat 200 mg; pediatric 2 mg/kg (up to 200 mg); "Discard any unused portion left in the vial" | label effective 2026-07-10, version 228 | `https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22pembrolizumab%22&limit=10` (the IV KEYTRUDA record; a second record, KEYTRUDA QLEX subcutaneous, has different vials and is not used) | HIGH |
| Vial reuse share f | student's assumption in [0, 0.9] | none (Modeling Assumption) | ASSUMPTION |
| USP <797> single-dose vial window | 12 h (current), 6 h (older) | secondary sources only (search 2026-10-28: icarepharmacyservices.org update, floridahealth.gov, jhoponline.com 2022); official text not read | UNVERIFIED |

Modeling Assumptions block the case must carry: (1) hypothetical adult 2 mg/kg uncapped policy, generic "Antibody X"; (2) f chosen by the student; (3) NHANES general adults as proxy for the cancer-center population; (4) unweighted analysis, survey-weighted figures differ by under 3 percentage points of f\*; (5) metric is mg of drug, no price (Medicare ASP per mg was not fetched and is not needed); (6) weights as measured in NHANES, not actual current weights at infusion; (7) as-of date: weights frozen as released 2017-March 2020; label as of 2026-07-10 (re-verify at write time since labels update).

### Sensitivity note (SPEC §6) and facilitator note
Oncology and drug dosing; patients are an abstraction. Facilitator note to include: this case concerns real cancer drugs and students may have family members in treatment; keep discussion on policy and arithmetic, not on any individual's care; the case is constructed and is not medical advice; the real adult regimen is a flat dose and the case does not question it; no student should leave thinking weight-based dosing is "right". Also flag that weight can be a sensitive topic: use the distribution and bands, not individual or body-shaming language.

### Overlap and differentiation check
Not a twin of The Overlap Call (no testing, no per-kit yield, no sets) or The Dosing Curve (veterinary AUC), Cold Chain (cold-chain spoilage), or The Vein-to-Vein Window (thaw clock). Different decision shape from the v1 one-break-even picks only in that the break-even is a *policy parameter* (f) the student must justify, plus a population-composition extension (sex and age subgroups give f\* from 0.21 to 0.53). Honest limit: it is still one break-even on one parameter (cross-cutting shape-variety note); the shape-variety extension is the subgroup case-mix argument.

---

## Fixes applied
| Finding | Reviewer | Disposition |
|---|---|---|
| Pool Size: "test individually / switch weekly" beats both pools by 6-7% | R1a | Resolved by dropping C1. Recomputed adaptive gain: 8.4% on 2022-23 data. Locking the protocol (no individual testing, no mid-season change) was workable, but see next row. |
| Add independence/clustered positivity assumption; drop decorative "non-linear"; compound-event only if forced; state closed form | R1a | Recorded in "Why C1 was dropped" (closed form q^2-q+0.1=0, p\*=2.363% verified). Not carried into C3 because C1 is dropped; C3 claims no probability skills. |
| Unit wording "expected PCR tests per sample, summed over weeks"; keep % positivity is not prevalence disclosure | R1b | Moot after switch; the disclosure is preserved in the C1 summary above as the data limitation (percent of tests positive among those tested, nationally). |
| One margin convention gap/winner | R1a | Stated once at top; every margin in this sheet uses (loser - winner)/winner. Corrected v1's C1 figures accordingly. |
| No patient stake; twin of The Overlap Call | R1c | Tried a delay input; it made pool 5 dominant (break-even value of delay 0.081 tests per delayed result), so the stake could not coexist with balance. Switched to C3 per instruction. C3 carries a patient-facing dose-accuracy input (37.8% within +/-20% of target under A, 100% under B) plus facilitator note. |
| C3 as fallback: re-tier T4, f as Modeling Assumption, add the label's 200 mg cap note | R1 | T4; f is an explicit student-chosen assumption with anchors; cap documented and shown to collapse the fork (B beats A at all f), so the constructed policy is uncapped and disclosed. |
| New protagonist name not in `cases/`; avoid Priya, Mara, Okafor, Raman | cross-cutting | Beatrix Lindqvist; grep for both names over the whole project returned nothing. |
| Ending not "phone buzzes" | cross-cutting | Technician's question at the cabinet; no phone. |
| Facilitator note for patient sensitivity | cross-cutting | Included (cancer care, weight sensitivity, not medical advice). |
| As-of dates | cross-cutting | NHANES release window and label effective date 2026-07-10 stated; label to be re-checked at write time. |
| Spine ids exist, do not over-claim | cross-cutting | 5 ids, each tied to a deliverable. |

## Still open
- **UNVERIFIED:** USP <797> single-dose-vial beyond-use window (12 h vs 6 h); only secondary sources read. Case should either cite the official chapter or phrase as "some sterile-compounding standards allow a short window".
- **UNVERIFIED:** weight distribution of actual cancer-center infusion patients (NHANES is a general-population proxy).
- **UNVERIFIED:** any real hospital's vial-sharing rate; f is an assumption by design.
- Drug price per mg (Medicare ASP) not fetched; metric is mg, not dollars. If R1b wants dollars, fetch the current ASP file and add a price Modeling Assumption.
- Label text may change between now and case-write; re-fetch and re-read the dose and discard lines then.
- f upper bound: this sheet caps the student's range at 0.9 because f = 1 puts B at exactly 20.00% margin; R1a should confirm the cap and the 0.9 margin (16.4% by the winner convention; check at write time).
- The 217-adult upper-outlier count depends on the quartile convention (numpy linear interpolation); the case should name its convention or give the quartiles explicitly.
- Shape variety remains one break-even on one parameter; the subgroup case-mix extension is the only added structure. R1c may still prefer a different shape.
