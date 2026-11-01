# CONCEPTS — Clinical Medicine, Diagnostics & Trials (clinical-medicine) — 2026-10-27

Target: `readmodel/domains.json` → `clinical-medicine` (cluster Health & Life Sciences, authoring_priority LOW, signature skills all covered). The domain is saturated on its signature skills, so these concepts aim at thin (n<=2) stats/probability skills and at the "is the test telling the truth" theme. Existing cases avoided: Cardiology (STICH), Medical Statistician, Biostatician, End Of Life, Medical Transport, Psychologist, The Vein-to-Vein Window (CAR-T thaw), The Trial Size (cluster survey precision), The Dosing Curve (veterinary AUC), Cold Chain, Health Insurance. No prior concept sheet covers pooled testing, A1c-vs-fasting-glucose, or flat-vs-weight-based dosing (grepped `cases/_concepts/` and `cases_index.json`).

Every number below was recomputed in code on 2026-10-27 from data fetched live that day (scripts reproduce from the quoted endpoints; scratch copies live in the session scratchpad, not in the repo). No private individuals, no named living people, no recent deaths. Protagonists are constructed and disclosed as such.

## Ranking

| Rank | Id | Title | Tier | Score* | Data | Computed margin (primary metric) |
|---|---|---|---|---|---|---|
| 1 | C1 | The Pool Size | T3 | 1.2 | HIGH | 3-8% per season (flu, pool 5 vs 10); each wins in ~half of weeks |
| 2 | C2 | The Fasting Gap | T4 | 0.0 thin (see note) | HIGH | 6.6% (A1c 33.2 vs fasting-glucose 31.0 detections per 1,000) |
| 3 | C3 | The Flat Dose | T3 | 1.0 | HIGH (data) / assumption (f) | 3.7% at f=0.5; break-even f=0.356; range +9% to -17% over f in [0,1] |

*Score = sum of skill weights (how-to 1.0, term 0.6) over n<=2 spine skills x availability factor (HIGH 1.0). C2 closes no n<=2 skill; it is ranked 2nd for clinical depth (it is the one that actually exercises Bayes/conditional-probability reasoning on real lab data) and is the best "true vs false negative" story in the sheet. No concept claims more than 5 skills; no split risk.

**Recommendation.** Write **C1 The Pool Size** first: fully live-portal data (CDC data.cdc.gov weekly positivity, refreshed 2026-10-23), a closed-form model the student can hand-derive (expected tests per person = 1/k + 1 - (1-p)^k), no sensitive subject matter, and a break-even prevalence (p* = 2.36%) that students can locate on the actual data. Hold C3 for last: its decisive parameter (vial-sharing rate f) is an assumption, so it is the most "modeling-assumption"-heavy. Kill nothing outright, but C2 needs one R1b-style check on circular reference standard (flagged below) before it is written.

---

### C1 — The Pool Size   ·   score 1.2   ·   tier T3
**Protagonist.** Dana Okafor (constructed; disclosed as a composite), laboratory director at a 300-bed community hospital's respiratory-virus testing lab. Personally at stake: she must fix one pooling protocol for the whole season, because the lab's automation and SOPs cannot change pool size week to week, and she signs the reagent budget.
**Real/recognizable story.** Group testing was introduced by Robert Dorfman in 1943 to screen army blood samples for syphilis (Wikipedia "Group testing" confirms the 1943 Dorfman origin; fetched). It returned in 2020 when labs pooled SARS-CoV-2 swabs to stretch scarce reagents. The hospital and protagonist are constructed framing; the method and the positivity data are real.
**The dilemma.** A.) Pool 5 samples per test (retest each member individually only if the pool is positive) OR B.) Pool 10 samples per test, same retest rule.
**Primary metric.** Expected PCR tests consumed per patient sample, summed over a 52-week influenza season (units: tests per patient-week-summed, i.e. total tests per 1 patient sampled every week; or equivalently average tests per sample x 52). Lower is better.
**Why it's close.** Larger pools save more tests when the virus is rare and waste them when it is common (a positive pool forces all 10 retests). Real weekly flu positivity sits below the break-even for roughly half the weeks and above it for the rest, so neither pool size wins every week, and over a season the totals land within a few percent.
**Computed (code, data below):** E[tests/sample] = 1/k + 1 - (1-p)^k, with p = weekly percent positivity. Break-even p* where k=5 equals k=10 is **2.36%** (bisection; hand-checkable). Season totals (A=pool 5, B=pool 10; sum of weekly E):
| Season (Oct-Sep) | weeks | A (pool 5) | B (pool 10) | B/A | weeks A cheaper |
|---|---|---|---|---|---|
| 2022-23 | 53 | 20.14 | 19.74 | 0.980 (B wins 2.0%) | 16 |
| 2023-24 | 52 | 22.87 | 24.66 | 1.078 (A wins 7.3%) | 27 |
| 2024-25 | 52 | 23.65 | 24.35 | 1.029 (A wins 2.9%) | 25 |
| 2025-26 | 52 | 23.90 | 25.25 | 1.056 (A wins 5.3%) | 28 |
All four full seasons are inside the 20% band, and **both options win**: B wins 2022-23 and in roughly half of all individual weeks; A wins the three later seasons. (Alternates computed: pool 4 vs 8 gives B/A 0.905 / 1.002 / 0.969 / 0.992 with break-even 3.88%; pool 5 vs 8 break-even 3.00%.) Pooling the whole 212-week series for COVID-19 instead (pool 5 vs 10: B/A 1.169) and RSV (1.011) show how the same rule flips by pathogen, a natural extension but not the core.
**Would close (2 skills, 0 how-to / 2 term):**
| id | kind | label |
|---|---|---|
| statistics-and-probability-independent-event | term | Independent Event (n=2; the (1-p)^k pool-negative model assumes independence) |
| statistics-and-probability-non-linear | term | Non-linear (n=2; E(k) is a non-linear function with an interior optimum) |
**Already-covered skills it also exercises.** `statistics-and-probability-how-to-determine-the-probability-of-a-compound-event` (n=7), `statistics-and-probability-probability`, mean, percent/rate skills. T4 extension (optional): a stated assumption that pooling a 10-sample batch lowers PCR sensitivity (dilution), which the student must justify.
**Data feasibility: HIGH.** Fetched and confirmed:
- CDC data.cdc.gov dataset `seuz-s2cv` "Percent of Tests Positive for Viral Respiratory Pathogens" — Socrata JSON API, columns `week_end`, `pathogen`, `percent_test_positivity`; 212 weekly rows per pathogen from 2022-10-01 to 2026-10-17; dataset updated 2026-10-23 (rowsUpdatedAt confirmed from the view JSON). Flu positivity range 0.3%-31.7%. Endpoint used: `https://data.cdc.gov/resource/seuz-s2cv.json?$limit=5000&$order=week_end`. Free, no key, a student can open it in a browser.
- Dorfman's formula is a textbook result; students derive it themselves (the 1943 paper page was Incapsula-blocked when fetched, so cite the Wikipedia group-testing article, which I did fetch, rather than the paper — the paper itself is UNVERIFIED as a fetchable source).
Honest gaps: the series is national percent of tests positive among people already tested (symptomatic/clinical), not prevalence in an unselected screened population, and the CDC page itself notes it is tests, not individuals. That must be a disclosed Modeling Assumption; it does not break the math (the student uses it as p). Also p is nationwide; a real lab would use its own local positivity.
**Sensitivity (SPEC §6).** NONE (infectious-disease surveillance; no individuals).
**Split risk.** NONE.

---

### C2 — The Fasting Gap   ·   score n/a (no n<=2 skill)   ·   tier T4
**Protagonist.** Marcus Webb (constructed; disclosed), medical director of a federally qualified community health center that screens adults for undiagnosed type 2 diabetes. Personally at stake: his clinic is walk-in heavy, patients arrive at all hours, and he must choose one default screening test for the coming year.
**Real/recognizable story.** The ADA recognizes both A1c >= 6.5% and fasting plasma glucose >= 126 mg/dL as diagnostic, and the two tests famously disagree on who is flagged. Clinic and director are constructed; the concordance and fasting behavior below are computed from real national survey microdata.
**The dilemma.** A.) Screen every patient with a point-of-care A1c (no preparation, any time of day) OR B.) Screen every patient with fasting plasma glucose (usable only if the patient has fasted at least 8 hours).
**Primary metric.** Undiagnosed diabetes cases detected per 1,000 patients screened (cases whose own test result is >= its cutoff).
**Why it's close.** Fasting glucose catches a much larger share of true cases per test performed, but a walk-in clinic can only use the result when the patient happened to be fasting. A1c catches fewer cases but works on every patient. The fasting rate of unprompted patients (56.8%) sits just under the break-even fasting rate (60.8%), and subgroups fall on either side.
**Computed (NHANES 2017-March 2020 pre-pandemic files; adults >= 20, not told they have diabetes):**
- Analysis sample n = 3,220 with both A1c and fasting glucose; 211 "cases" = A1c >= 6.5 OR glucose >= 126 (prevalence 6.55%).
- A1c sensitivity vs that union = 0.507; fasting-glucose sensitivity = 0.834. **Break-even fasting rate = 0.507/0.834 = 0.608.** (Bootstrap 95% CI for the A1c/FPG ratio 0.511-0.723, so the break-even is itself uncertain, which is good for discussion.)
- Fasting >= 8 h (PHAFSTHR) among all examined adults 20+ with a fasting record (n = 8,406): 4,771 = **56.8%** (this is the proxy for "patient shows up at a random time with no fasting instruction"). Among morning-session participants who were told to fast: 95.3%.
- Detections per 1,000 screened: A (A1c) **33.2**; B (fasting glucose, walk-in fasting 56.8%) **31.0**. A wins by **6.6%** (B/A = 0.934). If the clinic could instead schedule everyone for a fasted morning visit (95.3%), B would detect 52.1 per 1,000 (B/A 1.57), so the decision is genuinely about the clinic's patient flow.
- By age band (cases/n; walk-in B/A): 20-39 29/1151, B/A 1.085 (B wins 8.5%); 40-59 81/1090, B/A 0.781 (A wins; note this subgroup is outside the 20% band, a feature for the Socratic discussion, not the primary metric); 60+ 101/979, B/A 1.021 (B barely wins 2.1%). Both options win somewhere.
**Would close (2 skills, 1 how-to / 1 term; both n=5, not thin — this concept's value is clinical depth, not thin-skill yield):**
| id | kind | label |
|---|---|---|
| statistics-and-probability-conditional-probability | term | Conditional Probability (sensitivity = P(test+ | case)) |
| statistics-and-probability-how-to-determine-the-probability-of-conditional-events | how-to | How to determine the probability of conditional events |
**Already-covered skills it also exercises.** `statistics-and-probability-stratified-sampling` (n=4; age strata), ratio, mean, percent.
**Data feasibility: HIGH.** Fetched and confirmed, all free anonymous downloads:
- CDC NHANES 2017-March 2020 Pre-Pandemic files: `P_GHB.xpt` (A1c, LBXGH), `P_GLU.xpt` (fasting glucose, LBXGLU), `P_DEMO.xpt` (age), `P_DIQ.xpt` (told-diabetes, DIQ010), `P_FASTQX.xpt` (PHAFSTHR hours fasted, PHDSESN session) under `https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/` (HTTP 200 on each). Codebook page for P_FASTQX fetched; PHDSESN 0=morning (6,454), 1=afternoon (5,090), 2=evening (2,228).
Honest gaps and risks (R1b should look at these): (1) circular reference standard — "case" is defined as either test positive, because NHANES has no gold standard here; ADA diagnosis normally requires confirmation, and the union flatters whichever test finds more. Disclose it and let students stress it. (2) Walk-in fasting proxy: afternoon/evening NHANES participants were not instructed to fast, so 56.8% mixes instructed and uninstructed people; that is intended but must be stated. (3) Unweighted analysis; NHANES weights were not applied (weighted figures could shift margins by a few points). (4) A1c point-of-care vs lab A1c differ; the case uses lab values. (5) The 56.8%-vs-60.8% gap is 4 percentage points inside a 95% CI of 0.51-0.72, so a student could argue either way with statistical honesty.
**Sensitivity (SPEC §6).** Light: diabetes/health-equity (A1c performs differently by ancestry); add a facilitator note to keep discussion on method, not on groups. No individuals.
**Split risk.** NONE.

---

### C3 — The Flat Dose   ·   score 1.0   ·   tier T3
**Protagonist.** Priya Raman (constructed; disclosed), chief oncology pharmacist at a regional cancer center. Personally at stake: she writes the dosing policy for a hospital-formulary monoclonal antibody that comes in single-dose 100-mg vials, and the policy drives both drug spend and who is under- or over-dosed.
**Real/recognizable story.** Current FDA labeling for pembrolizumab (KEYTRUDA) gives 200 mg every 3 weeks for adults but 2 mg/kg (up to 200 mg) for pediatrics, and supplies 100 mg/4 mL single-dose vials (openFDA drug-label endpoint, label effective 2026-07-10, fetched and read). The case is explicitly constructed framing modeled on that label pattern (flat adult dose vs weight-based dose); it does not claim this hospital or its numbers are real. Use a generic "monoclonal antibody" in the student text to avoid brand endorsement; cite the label only in the appendix.
**The dilemma.** A.) Flat 200 mg dose for every adult OR B.) Weight-based 2 mg/kg, rounded up to whole 100-mg vials with the unused remainder partly reusable.
**Primary metric.** Mg of drug drawn from pharmacy stock per adult dose (lower is better), with f = share of each opened vial's leftover that the pharmacy can reuse for another patient.
**Why it's close.** Weight-based dosing needs less drug on paper (the average adult needs about 167 mg, not 200), but whole-vial rounding wastes up to 99 mg per dose unless the leftover can be shared. The winner flips on one pharmacy-operations parameter.
**Computed (NHANES 2017-March 2020 adult body weight, n = 8,811 adults >= 18 with BMXWT; unweighted):**
- Mean weight 83.3 kg (weighted 84.0); median 79.6; five-number summary 32.6 / 67.2 / 79.6 / 95.5 / 254.3 kg; upper outlier fence 137.9 kg with 217 adults above it. 20.0% of adults are over 100 kg (the weight where 2 mg/kg equals 200 mg).
- A = 200 mg. B exact (no waste) = 166.7 mg/dose (0.833 of A, B wins 16.7%). B with vials rounded up and nothing reused = 218.4 mg (1.092, A wins 8.4%). Mg drawn for B = 166.7 + (1-f)(218.4-166.7). **Break-even f* = 0.356.** f=0.25: 205.5 (A wins 2.7%); f=0.5: 192.5 (B wins 3.7%); f=0.75: 179.6 (B wins 10.2%). The whole f range [0,1] stays within ±20%.
- Clinical tension: under the flat dose, 62.2% of adults land outside +/-20% of the 2 mg/kg target (5th-95th percentile 1.58-3.80 mg/kg). By sex, men median 2.35 mg/kg, women 2.70 mg/kg.
**Would close (1 skill thin, 1 how-to):**
| id | kind | label |
|---|---|---|
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data | how-to | How to create a box and whisker plot given a set of data (n=1; weights' spread and outliers) |
**Already-covered / also exercises.** `statistics-and-probability-box-and-whisker-plot` (n=3), `statistics-and-probability-quartiles` (n=3), `statistics-and-probability-outlier` (n=5), mean, unit conversion (mg/kg), rounding up to whole units.
**Data feasibility: HIGH for the weights and label; f is an assumption.** Fetched and confirmed:
- NHANES `P_BMX.xpt` (BMXWT) and `P_DEMO.xpt` at `https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/` (HTTP 200).
- openFDA drug label API `https://api.fda.gov/drug/label.json?search=openfda.brand_name:"KEYTRUDA"&limit=5` (HTTP 200; dosage text and 100 mg/4 mL vial supply text read).
- The vial-sharing rate f is NOT in any dataset I fetched; the case must treat it as a stated Modeling Assumption (T4-style) and a hospital's real vial-sharing practice is UNVERIFIED. Medicare ASP (price per mg) was not fetched and is not needed for a mg-based metric.
**Sensitivity (SPEC §6).** Light: oncology/drug dosing; no patient stories needed. Note it is constructed and not medical advice.
**Split risk.** NONE.

---

## Method notes (for case-research handoff)
- Tests-per-sample formula: Dorfman two-stage: 1 pool test + k retests with probability 1-(1-p)^k, so E = 1/k + 1 - (1-p)^k for k >= 2.
- C1 break-even computed by bisection on E(5,p) = E(10,p); p* = 0.0236. Season totals summed over week_end dates, season starting each October.
- C2/C3 derived with pandas `read_sas` on the XPT files listed; adult filters RIDAGEYR >= 20 (C2) and >= 18 (C3); C2 excludes DIQ010 in {1 yes, 3 borderline}; fasting >= 8 h by PHAFSTHR.
- Overlap check: no existing case or concept premise matches pooled testing, A1c vs fasting glucose, or flat vs weight-based dose.

Next step: Approve a concept, then run case-write on it.
