# Case Study: The Compute Lease

MS | Math | Case Study | 2026-27 | Heroes Academy

---

## Overview

Sofia Reyes has the same spreadsheet open in two windows, and neither one is winning.

It's late enough that the office kitchen light has gone to its dim auto-off setting, and the only sound is the low whir of the demo rack in the corner — a handful of GPUs still churning through some customer's overnight training job. Sofia is Kestrel Compute's infrastructure capacity planner, which mostly means she is the person who has to say, in writing, how many GPUs the company commits to and for how long. Friday she stands in front of the board with a recommendation. Whichever way it goes, her name is the one attached to the cost line for the next two years.

One window holds an email from a hardware vendor's sales rep, subject line still bolded from this morning, laying out a multi-year GPU cluster contract. The other holds a tab full of on-demand pricing pages, scrollable, cancelable, unforgiving on a per-hour basis. Both get Kestrel to the same place — enough GPU capacity to serve its customers. They get there in completely different ways.

Sofia pulls a blank legal pad toward her, uncaps a pen, and writes two headers at the top of the page, one for each option. She doesn't write anything under either one yet. She just sits there, pen hovering, rack humming, with two days left to decide which header she's going to fill in.

---

## Background

Kestrel Compute is a mid-size AI cloud provider that rents GPU capacity to customers running machine-learning workloads — from small research teams renting a handful of GPUs by the hour to larger customers running sustained training jobs. Sofia Reyes is Kestrel's Infrastructure Capacity Planner, responsible for recommending how the company acquires the GPU capacity it resells. The board has asked her for a single recommendation, backed by numbers, by Friday's meeting (SEE APPENDIX A).

Two paths are on the table.

**The Long Lock.** Kestrel signs a fixed-rate, multi-year commitment for a dedicated GPU cluster. The per-GPU-hour rate is lower than any on-demand price Kestrel could get elsewhere, and it is locked in for the full term of the contract — Kestrel pays the same fixed amount every month whether its customers rent every GPU-hour available or almost none of it (SEE APPENDIX B). The commitment term extends past the two-year window the board has asked Sofia to evaluate, so a portion of the fixed cost keeps arriving even after that evaluation window closes (SEE APPENDIX A).

**The Open Tap.** Kestrel instead buys GPU capacity on the on-demand market, month by month, only paying for the GPU-hours its customers actually consume. The per-GPU-hour rate is higher than the Long Lock's locked-in rate, but Kestrel never pays for capacity nobody rents, and spend scales automatically with however fast — or slowly — Kestrel's customer base actually grows (SEE APPENDIX C).

Kestrel's own month-over-month customer growth rate is not a fixed, known number — it depends on how fast the company's sales team closes new accounts and how much existing customers expand their usage, and it could land anywhere across a real, published range of growth rates seen elsewhere in the AI-infrastructure industry (SEE APPENDIX D). Whichever option Kestrel picks, the board's decision criterion is the same: which one delivers a lower total infrastructure cost per GPU-hour actually delivered to paying customers, over the two-year window Sofia has been asked to evaluate.

Every dollar figure, rate, and growth-rate range this case depends on is either given directly above, or fixed in Appendices A through D. Every external source cited anywhere in this case is collected in APPENDIX E. The vocabulary and "how to…" skills this case will ask you to research are listed in APPENDIX F — that is where Challenge 1 sends you.

---

## Dilemma

You are Sofia Reyes.

Do you:

**A.)** Recommend **the Long Lock** — sign the fixed-rate, multi-year GPU cluster commitment **OR**

**B.)** Recommend **the Open Tap** — buy on-demand GPU capacity that scales month to month with actual customer growth

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A monthly GPU-hour demand sequence.** Using Kestrel's starting monthly GPU-hour demand and the growth-rate range in Appendix D, write both a recursive rule and a closed (explicit) formula for Kestrel's projected monthly GPU-hour demand, month by month, for the full 24-month evaluation window, under the low, mid, and high growth-rate scenarios.
- **D2 — Two 24-month total-cost series.** Write the Long Lock's 24-month total-cost series (Appendix B) and the Open Tap's 24-month total-cost series (Appendix C, driven by your D1 demand sequence) as explicit sums, term by term. Show what kind of series each one is and why.
- **D3 — A convergence/divergence classification.** Take the Open Tap's underlying monthly-cost sequence and extend its growth pattern hypothetically past the 24-month window, out to an unlimited number of months. Identify the common ratio of the resulting series, state whether that series converges or diverges, and explain in plain terms what your answer means for Kestrel's exposure if its growth rate held steady forever instead of just for two years.
- **D4 — Total cost per GPU-hour delivered, both options, all three growth scenarios.** Using your D2 series sums, compute each option's total infrastructure cost per GPU-hour delivered to paying customers over the full 24-month window, under the low, mid, and high growth-rate scenarios from Appendix D. Present all six results (2 options × 3 scenarios) in one table.
- **D5 — The crossover point.** Find (by calculation, graph, or both) the growth rate at which the Long Lock and the Open Tap produce the same 24-month cost per GPU-hour delivered. State whether that crossover rate falls inside or outside the range given in Appendix D, and what that tells Sofia about how much the recommendation actually depends on which end of the growth-rate range Kestrel lands on.
- **D6 — A recommendation.** State which option you recommend to the board and defend it using your D4 and D5 results, including what would have to be true about Kestrel's actual growth rate for your recommendation to be wrong.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

## Appendix A: Kestrel's Board Directive and Decision Constraints

| Quantity | Value |
|---|---|
| Days until Sofia's board recommendation is due | 2 days [MA3] |
| Evaluation window for the primary metric | 24 months |
| Long Lock contract term (may exceed the evaluation window) | 36 months [S2] |
| Number of GPUs Kestrel is deciding whether to commit to | 512 GPUs [MA1] |
| Kestrel's starting (month 0) monthly GPU-hour demand from paying customers | 120,000 GPU-hours/month [MA2] |

*Note: Kestrel Compute is a scenario construction for this case — there is no real company by this name. The evaluation window (24 months) and the fact that the Long Lock's own contract term runs longer than that window are both fixed constraints of the board's request, not sourced figures. See the Modeling Assumptions block below for MA1–MA3.*

---

## Appendix B: The Long Lock — 3-Year Fixed-Rate GPU Cluster Lease

| Spec | Value |
|---|---|
| Fixed rate per GPU-hour of cluster capacity, locked for the full contract term | $2.97 [S2] |
| Monthly fixed cost (rate × committed GPU-hours per month, regardless of usage) | $1,110,067 (= $2.97/GPU-hr × 512 GPUs [MA1] × 730 hr/month) [S2] |
| Whether the monthly payment changes if fewer GPU-hours are actually used | No — fixed regardless of utilization |

---

## Appendix C: The Open Tap — On-Demand GPU Capacity

| Spec | Value |
|---|---|
| On-demand rate per GPU-hour | $6.88 [S1] |
| Billing basis | Pay only for GPU-hours actually consumed by paying customers that month |
| Minimum commitment | None |

---

## Appendix D: Industry AI-Infrastructure Growth-Rate Range

| Scenario | Month-over-month customer GPU-hour demand growth rate |
|---|---|
| Low | 1.1% [S5] |
| Mid | 1.7% [S3] |
| High | 2.1% [S4] |

*Kestrel's own actual growth rate is not independently known or sourceable — it is a fictional company. The range above anchors Kestrel's planning scenarios to a real, publicly-traded, mid-size cloud infrastructure provider's own recent quarterly revenue growth trajectory (see Appendix E) — the closest available real-world analog to Kestrel's own stated scale.*

---

## Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, needed because Kestrel Compute is a fictional company and no real business supplies
> them. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Number of GPUs Kestrel commits to under the Long Lock | 512 GPUs | No real committed-cluster size exists for a fictional company. 512 GPUs (64 × 8-GPU instances) aligns with the published ceiling for AWS's own EC2 Capacity Blocks for ML cluster product, which supports reservations up to 64 p5 instances / 512 GPUs. | Load-bearing. Sets the Long Lock's fixed monthly cost floor ($1,110,067/month regardless of usage). A materially different cluster size shifts every D2/D4/D5 result and could move the D5 crossover growth rate. |
| MA2 | Kestrel's starting (month 0) monthly GPU-hour demand | 120,000 GPU-hours/month | No real company exists to supply this figure. 120,000 GPU-hours/month is ≈32% of MA1's 373,760 GPU-hour/month committed capacity (512 GPUs × 730 hr), representing a newly-signed reserved cluster that starts under-utilized and is expected to grow into its capacity — a standard reserved-capacity planning pattern. | The single most sensitivity-loaded figure in the case: it is the seed value for every month of D1's demand sequence under all three growth scenarios, and therefore feeds every D2, D4, and D5 result directly. A higher starting utilization makes the Long Lock look better sooner; a lower one favors the Open Tap longer. |
| MA3 | Days until Sofia's board recommendation is due | 2 days | Purely narrative detail internal to the fictional scenario — not externally sourceable. Matches the Overview's existing prose ("two days left to decide"). | None. Decorative only; does not feed any Challenge (D1–D6) calculation. |

---

## Appendix E: Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | On-demand hourly price of AWS EC2 p5.48xlarge (8× H100 GPUs), us-east-1 → derived per-GPU rate | $55.04/instance-hr → $6.88/GPU-hour | AWS list price, via [instances.vantage.sh](https://instances.vantage.sh/aws/ec2/p5.48xlarge) and cross-checked at [aws-pricing.com](https://aws-pricing.com/p5.48xlarge.html) | Accessed 2026-08-26 | MEDIUM |
| S2 | AWS EC2 p5.48xlarge 3-Year Reserved Instance (No Upfront) hourly rate, us-east-1 → derived per-GPU rate and Long Lock contract term | $23.7773/instance-hr → $2.97/GPU-hour; 3-year (36-month) term | AWS list price, via [instances.vantage.sh](https://instances.vantage.sh/aws/ec2/p5.48xlarge) | Accessed 2026-08-26 | MEDIUM |
| S3 | DigitalOcean Holdings (NYSE: DOCN) Q1 2026 revenue growth, year-over-year (proxy for Mid growth scenario) | +22% YoY ($258M) → 1.7%/month | DigitalOcean Holdings, Inc. — [DigitalOcean Announces First Quarter 2026 Financial Results](https://investors.digitalocean.com/news/news-details/2026/DigitalOcean-Announces-First-Quarter-2026-Financial-Results/default.aspx) | Published 2026-05-04, accessed 2026-08-30 | HIGH |
| S4 | DigitalOcean Holdings (NYSE: DOCN) Q2 2026 revenue growth guidance, year-over-year (proxy for High growth scenario) | +29% YoY (guided) → 2.1%/month | DigitalOcean Holdings, Inc. — [DigitalOcean Expects to Report Record Q2 2026 Results with RPO to Exceed $800M, Up More Than 10X Year Over Year](https://investors.digitalocean.com/news/news-details/2026/DigitalOcean-Expects-to-Report-Record-Q2-2026-Results-with-RPO-to-Exceed-800M-Up-More-Than-10X-Year-Over-Year/default.aspx) | Published 2026-06, accessed 2026-08-30 | HIGH |
| S5 | DigitalOcean Holdings (NYSE: DOCN) Q2 2025 revenue growth, year-over-year (proxy for Low growth scenario) | +14% YoY → 1.1%/month | DigitalOcean Holdings, Inc. — [DigitalOcean Expects to Report Record Q2 2026 Results with RPO to Exceed $800M, Up More Than 10X Year Over Year](https://investors.digitalocean.com/news/news-details/2026/DigitalOcean-Expects-to-Report-Record-Q2-2026-Results-with-RPO-to-Exceed-800M-Up-More-Than-10X-Year-Over-Year/default.aspx) | Published 2026-06, accessed 2026-08-30 | HIGH |

*S3, S4, and S5 are proxy figures — three points along one real, publicly-traded, mid-size cloud infrastructure company's (DigitalOcean) own disclosed quarterly revenue growth trajectory, converted from a year-over-year percentage to an equivalent constant monthly compound rate (shown in each source's note in case.json). They are not literally "GPU-hours rented by Kestrel's own paying customers" — no such disclosure exists for a fictional company — which is why Appendix D already frames them as an anchor, not as Kestrel's own known rate. DigitalOcean was chosen over the previously-cited hyperscaler-scale AI-infrastructure figures (see RESEARCH_LOG.md and the case's own QA history) because it is a much closer real-world analog to Kestrel's stated mid-size scale. Full derivations and rejected alternatives are in RESEARCH_LOG.md.*

---

### Appendix F — "How To…" Math Questions To Research

**Vocabulary terms**

- Series
- Sequence

**"How to…" questions**

- How to determine whether a series converges or diverges

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
