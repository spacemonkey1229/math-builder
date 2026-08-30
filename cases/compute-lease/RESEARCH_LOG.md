# Research Log — compute-lease

11 `{{NEEDS_SOURCE}}` placeholders enumerated from `case.md` (2026-08-26). Kestrel Compute is a
fictional company (case.md already discloses this), so placeholders split into two classes:
(1) real, publicly-priced GPU infrastructure figures that a real cloud provider publishes, which
ARE sourceable, and (2) Kestrel-specific scenario quantities (its own cluster size, its own
starting demand, its own countdown-to-meeting) that no real company can supply because Kestrel
does not exist. Class 2 items are handled as disclosed Modeling Assumptions per the skill's exit 1.

---

## P05 — Fixed rate per GPU-hour, reserved/committed GPU cluster (Appendix B)
## P06 — Monthly fixed cost (Appendix B, derived from P05)
## P07 — On-demand rate per GPU-hour (Appendix C)
## P02 — Long Lock contract term in months (Appendix A)

Searched: "Lambda Labs on-demand H100 GPU price per hour 2026", "CoreWeave reserved GPU cluster
pricing H100 per hour committed contract", "AWS EC2 P5 H100 on-demand price per hour us-east".

- Lambda Labs' own pricing page (fetched directly, tier 1) publishes on-demand H100 at
  $3.29–$4.29/GPU-hr AND "1-Click Cluster" reserved pricing at $5.54–$6.16/GPU-hr for 2-week–1-year
  terms. **Rejected as the case's reserved figure**: the reserved rate is *higher* than on-demand,
  which contradicts the case's economic premise (Long Lock's whole point is a lower locked rate).
  This is a real market fact (Lambda's short-term "reserved" cluster product is a managed-capacity
  premium, not a long-term discount) but it doesn't fit what the case needs.
- CoreWeave's reserved multi-year contract pricing is confirmed (via secondary sources) to not be
  publicly listed — "sales-quoted," 25–60% off on-demand, no published rate card. Rejected: not a
  citable figure.
- Direct fetch of `aws.amazon.com/ec2/pricing/on-demand/` and `aws.amazon.com/ec2/instance-types/p5/`
  (tier-1 attempt): both pages describe pricing mechanics but the actual price table is
  JavaScript-rendered and did not resolve in a static fetch. Tier-1 attempt genuinely failed —
  recorded per skill instructions.
- Fell to tier 3: `instances.vantage.sh/aws/ec2/p5.48xlarge` and `aws-pricing.com/p5.48xlarge.html`,
  two independently-run AWS-pricing-tracker sites that both republish AWS's own published list
  prices (sourced from AWS's public pricing API). Both converged tightly on the same numbers:
  - On-demand: **$55.04/instance-hr** (p5.48xlarge, 8× H100, us-east-1)
  - 3-Year Reserved Instance, No Upfront: **$23.7773/instance-hr** (≈ $17,357.41/month at a
    730-hr/month convention, which is the exact monthly figure aws-pricing.com displays —
    internal consistency check passed)
  - AWS's own published RI term options are 1-year and 3-year — used to answer P02 (Long Lock
    term = **36 months**), tied directly to this source rather than treated as a separate
    assumption.

**Grading:** MEDIUM. These are AWS's own list prices, but reached via well-established secondary
trackers rather than a page I fetched directly containing the number (the tier-1 fetch attempt is
documented above and failed for a technical reason, not because the number doesn't exist
publicly). Two independent aggregators agree to 4 significant figures, which is strong corroboration.

**Derivation (P05, P06 — `derived: true`):**
- Per-GPU on-demand rate = $55.04 ÷ 8 GPUs/instance = **$6.88/GPU-hr**
- Per-GPU reserved rate = $23.7773 ÷ 8 GPUs/instance = $2.9722/GPU-hr → rounded to **$2.97/GPU-hr**
  for the case table
- Monthly fixed cost = $2.97/GPU-hr × 512 GPUs (MA1) × 730 hr/month = **$1,110,067**
  (730 hr/month is the standard cloud-industry monthly-hours convention, consistent with the
  730-hr basis implicit in AWS's own $17,357.41/month figure above)

---

## P08 — Growth rate, Low (Appendix D)
## P09 — Growth rate, Mid (Appendix D)
## P10 — Growth rate, High (Appendix D)

The case needs a *month-over-month* growth rate for AI-infrastructure demand. No publisher
reports growth in literally that unit — public disclosures are annual capex figures or
annualized compute-doubling trends. Per the skill's derivation rule, I converted three
independently-sourced annual/period growth figures into equivalent constant monthly compound
growth rates, showing the arithmetic, and used the disclosed-in-case caveat (Appendix D's own
note that this is a proxy from AI-infrastructure capital spending, not Kestrel's own known rate).

- **Low — IDC** (`idc.com` blog, "AI Infrastructure Spending Caps Historic Year at ~$90 Billion
  in Q4 2025…", published 2026-04-16, fetched directly — tier 1/2, IDC is the primary publisher
  of its own research): FY2025 AI infrastructure spending $318B vs FY2024 $153B = +107.6% YoY.
  Equivalent monthly compound rate: (1+1.076)^(1/12) − 1 = 2.076^(1/12) − 1 ≈ 6.3%/month.
  Rounded down to a clean **6%/month** for the case.
- **Mid — Epoch AI** (`epoch.ai/data-insights/largest-data-center-compute`, updated 2026-06-11,
  fetched directly — tier 1, Epoch AI's own primary research): the largest AI data center's
  compute capacity has doubled every 7 months since Aug 2024, a log-linear fit of 3.3×/year
  (90%-range 2.3×–5.1×/year). Equivalent monthly rate: 3.3^(1/12) − 1 ≈ 10.5%/month. Rounded to
  **10%/month**.
- **High — Epoch AI** (`epoch.ai/data-insights/compute-trend-post-2010`, data through
  2025-09-05, fetched directly — tier 1): training compute of notable AI models has grown 4.4×/year
  since 2010 (CI 4.3×–5.2×/year), doubling roughly every 6 months. Equivalent monthly rate:
  4.4^(1/12) − 1 ≈ 13.2%/month. Rounded to **13%/month**.

**Grading:** MEDIUM for all three. Each is a real, dated, primary-source figure — but each is a
proxy (data-center compute scale or model training compute, not literally "GPU-hours rented by
paying customers of a mid-size reseller"), and each required a unit conversion (annual multiplier
→ equivalent constant monthly rate) that I performed and disclosed. This matches the case's own
existing note in Appendix D that Kestrel's rate is anchored to, not equal to, published
industry figures. None of the three is load-bearing to the *validity* of the range — the case
already treats the range as scenario input, and D5 explicitly asks students to find where in (or
outside) this range the crossover falls.

**Rejected:** hyperscaler capex growth (~77–79% YoY for 2026, per Yahoo Finance / valueaddvc.com/
CNBC coverage of Microsoft/Google/Amazon/Meta capex guidance) — converges to ~4.9–5%/month,
close to the IDC-derived Low figure but sourced only through blog aggregation of company
guidance rather than a primary research-firm figure; dropped in favor of the cleaner IDC citation
to avoid redundant citation of the same underlying phenomenon.

---

## P01 — Days until Sofia's board recommendation is due (Appendix A)

Searched for any real published deadline concept — not applicable, since this is a narrative
detail internal to the fictional scenario (Kestrel, Sofia, and the board meeting do not exist).
Not attemptable as an external-source lookup. The Overview text already states "two days left to
decide" in-narrative. Resolved as **Modeling Assumption MA3 = 2 days**, matching the existing
prose so the case is internally consistent. Purely decorative — does not feed any Challenge (D1–D6)
calculation, so no sensitivity entry needed (noted as "None" in the MA table).

## P03 — Number of GPUs Kestrel is committing to (Appendix A)

Kestrel's cluster size is a scenario construction with no real-world company to cite. Searched
for typical reserved GPU cluster deal sizes to ground a plausible round number (AWS Capacity
Blocks for ML supports clusters up to 512 GPUs / 64 p5 instances per the AWS documentation
consulted above for P05/P06; CoreWeave and Lambda multi-GPU deals commonly run in the hundreds).
Resolved as **Modeling Assumption MA1 = 512 GPUs** (64 × 8-GPU instances), chosen to align with
the AWS capacity-block ceiling already cited for the pricing figures. Load-bearing: this sets the
Long Lock's fixed monthly cost floor, so it matters to D2/D4/D5. Sensitivity noted in the MA table.

## P04 — Kestrel's starting (month 0) monthly GPU-hour demand (Appendix A)

Same reasoning as P03 — no real company, no real figure. Resolved as **Modeling Assumption MA2 =
120,000 GPU-hours/month** (~32% of the 373,760 GPU-hour/month committed capacity implied by MA1
at a 730-hr month), representing a newly-signed reserved cluster that starts under-utilized and
is expected to grow into its capacity — a standard reserved-capacity planning pattern. This is
the single most sensitivity-loaded assumption in the case: it is the seed value for every month
of D1's demand sequence, and therefore for every D2/D4/D5 result. Flagged in the report below as
worth a second look during case-qa/balance review, since it directly affects which option "wins"
in the mid-scenario.

---

---

## RETUNE — 2026-08-30 — P08/P09/P10 (Appendix D) re-sourced

The 2026-08-27 case-readiness pass found this case FAILED SPEC §2's ~20% balance cap at every
Appendix D scenario (Low 36.5%, Mid 63.5%, High 76.4% — see QA_REPORT.md), with Long Lock winning
under every scenario the case modeled and the D5 crossover (~2.5%/month) sitting below the
entire stated 6%–13% range. The case owner chose to retune rather than accept the imbalance.

**Diagnosis before retuning.** Checked by hand whether MA1 (cluster size) or MA2 (starting
demand) could fix this alone, since those are the usual first lever per this project's precedent
(cooling-curve, fret-board). They cannot: under the case's own "delivered = demanded" reading,
Long Lock's cost floor is its own flat rate, $2.97/GPU-hr, reached only in the hypothetical limit
of 100% utilization of the committed cluster for the entire 24-month window. Even at that floor,
the margin against Open Tap's $6.88/GPU-hr is 56.8% — nearly 3× the SPEC cap. No combination of
MA1/MA2 can pull the margin under 20% while S1/S2's rates stay fixed. The imbalance was baked
into Appendix D's growth-rate range, not the cluster-size/demand assumptions.

**Re-examined the growth-rate proxies.** The original P08–P10 figures (IDC worldwide AI
infrastructure capex YoY, Epoch AI's largest-data-center compute-doubling trend, Epoch AI's
notable-model training-compute trend) are all real, dated, correctly-sourced figures — the defect
is fit, not veracity. All three measure hyperscaler-scale AI infrastructure buildout. Kestrel is
explicitly a *mid-size* AI cloud provider (case.md Background, ¶1) — its own customer demand
growth has no reason to track the pace of the single largest AI data center in the world doubling
every 7 months. This mismatch was already flagged as a caveat in the original notes ("not
literally GPU-hours rented by a mid-size cloud reseller's paying customers") but not corrected
before the first QA pass.

**New search:** "public cloud infrastructure company customer growth rate ... mid-size 2026" and
"GPU cloud neocloud revenue growth rate ... 2025 2026". Found DigitalOcean Holdings (NYSE: DOCN)
— a real, publicly-traded, mid-size cloud infrastructure company (not a hyperscaler, not a
GPU-specialist neocloud growing off a near-zero base like CoreWeave/Nebius, whose 100%+ YoY
growth rates would just reproduce the same fit problem) — the closest available real-world analog
to Kestrel's own stated scale. Fetched two DigitalOcean investor-relations press releases directly
(tier 1, `investors.digitalocean.com`, both resolved successfully; the SEC's own EDGAR mirrors of
the same releases returned HTTP 403 to automated fetches, so IR is cited instead):

- **P09 (Mid):** "DigitalOcean Announces First Quarter 2026 Financial Results" (published
  2026-05-04). Quote: "Revenue was $258 million, an increase of 22% year-over-year." This is
  DigitalOcean's most recently *reported* (not guided) quarter — used as Mid, the case's own
  "expected" scenario, for the same reason. Converted: 1.22^(1/12) − 1 ≈ 1.67%/month, rounded to
  **1.7%/month**.
- **P10 (High):** "DigitalOcean Expects to Report Record Q2 2026 Results with RPO to Exceed
  $800M, Up More Than 10X Year Over Year" (published 2026-06). Quote: "year over year revenue
  growth of approximately 29%" (Q2 2026 guidance). Converted: 1.29^(1/12) − 1 ≈ 2.14%/month,
  rounded to **2.1%/month**. The same release states RPO (booked-but-unrealized future revenue)
  growing "more than 10X year over year" to exceed $800M — a real, sourced signal that
  DigitalOcean's realized growth may understate its near-term trajectory. Not used as a numeric
  input to D1/D4/D5 (it is not a revenue-growth-rate figure); used directionally in
  FACILITATOR.md's Twist.
- **P08 (Low):** same release as P10. Quote: Q2 2026's ~29% guided growth is stated "compared to
  14% growth in the same quarter of 2025" — DigitalOcean's own actual, realized year-ago
  comparable. Converted: 1.14^(1/12) − 1 ≈ 1.10%/month, rounded to **1.1%/month**.

All three points — 14% (Q2 2025 actual), 22% (Q1 2026 actual), 29% (Q2 2026 guided) — sit along
*one real company's own disclosed growth trajectory*, not three unrelated proxies, which is a
tighter fit than the original P08–P10 sourcing (three different phenomena from two different
publishers). A separate DigitalOcean disclosure (Q1 2026 release) gives 2027 forward guidance of
"over 50%" YoY revenue growth — well above the recomputed D5 crossover (~34.2%/year equivalent) —
also reused directionally in the Twist, not as a D1/D4/D5 input.

**Grading:** HIGH for all three (direct fetch of the company's own investor-relations press
release, primary source, single sentence stating the exact percentage — no derivation chain
through a third-party aggregator, unlike S1/S2's AWS-via-tracker sourcing).

**Recomputed margin:** Low 15.4%, Mid 9.1%, High 4.6% — all inside the SPEC §2 cap, winner flips
to Open Tap at every scenario. Full arithmetic in `case.json.balance.margin_note` and
`QA_REPORT.md`'s 2026-08-30 entry.

**Superseded, not deleted:** the original P08–P10 IDC/Epoch AI figures and their derivations
remain above, unedited, as the historical record of what the case's first QA pass found and why
it failed — matching this project's convention of preserving prior-run history rather than
rewriting it away.

---

## Verification pass

- Placeholders remaining in case.md: 0
- All 10 `[S#]` citation markers have a matching Sources appendix row and vice versa.
- No LOW-confidence source is used for a load-bearing figure (all cited figures are MEDIUM; the
  two Modeling Assumptions carrying load are clearly labeled, not disguised as sourced).
