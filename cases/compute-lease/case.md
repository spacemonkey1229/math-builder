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
| Days until Sofia's board recommendation is due | {{NEEDS_SOURCE: stated in-scenario deadline, days from case launch to board meeting}} |
| Evaluation window for the primary metric | 24 months |
| Long Lock contract term (may exceed the evaluation window) | {{NEEDS_SOURCE: stated contract term in months, e.g. 36}} |
| Number of GPUs Kestrel is deciding whether to commit to | {{NEEDS_SOURCE: GPU cluster size, count of GPUs}} |
| Kestrel's starting (month 0) monthly GPU-hour demand from paying customers | {{NEEDS_SOURCE: baseline monthly GPU-hours actually rented by paying customers, month 0}} |

*Note: Kestrel Compute is a scenario construction for this case — there is no real company by this name. The evaluation window (24 months) and the fact that the Long Lock's own contract term runs longer than that window are both fixed constraints of the board's request, not sourced figures.*

---

## Appendix B: The Long Lock — 3-Year Fixed-Rate GPU Cluster Lease

| Spec | Value |
|---|---|
| Fixed rate per GPU-hour of cluster capacity, locked for the full contract term | {{NEEDS_SOURCE: reserved/committed-use GPU cluster pricing, USD per GPU-hour, e.g. from a published reserved H100/GPU cluster rate card}} |
| Monthly fixed cost (rate × committed GPU-hours per month, regardless of usage) | {{NEEDS_SOURCE: derived from rate and committed capacity once both are sourced}} |
| Whether the monthly payment changes if fewer GPU-hours are actually used | No — fixed regardless of utilization |

---

## Appendix C: The Open Tap — On-Demand GPU Capacity

| Spec | Value |
|---|---|
| On-demand rate per GPU-hour | {{NEEDS_SOURCE: published on-demand GPU pricing, USD per GPU-hour, e.g. AWS EC2 P5/H100 on-demand pricing, or CoreWeave / Lambda Labs published on-demand rate card}} |
| Billing basis | Pay only for GPU-hours actually consumed by paying customers that month |
| Minimum commitment | None |

---

## Appendix D: Industry AI-Infrastructure Growth-Rate Range

| Scenario | Month-over-month customer GPU-hour demand growth rate |
|---|---|
| Low | {{NEEDS_SOURCE: low end of a realistic month-over-month AI infrastructure demand growth rate, drawn from public hyperscaler capex/AI infrastructure growth disclosures}} |
| Mid | {{NEEDS_SOURCE: mid-range month-over-month growth rate from the same disclosures}} |
| High | {{NEEDS_SOURCE: high end of the same published growth-rate range}} |

*Kestrel's own actual growth rate is not independently known or sourceable — it is a fictional company. The range above anchors Kestrel's planning scenarios to real, published growth rates seen in AI-infrastructure capital spending elsewhere in the industry.*

---

## Appendix E: Sources

*(To be completed by case-research. Every {{NEEDS_SOURCE}} placeholder above will be resolved here with a URL, publisher, access date, and confidence grade, or converted to a disclosed Modeling Assumption if no public source exists.)*

---

### Appendix F — "How To…" Math Questions To Research

**Vocabulary terms**

- Series
- Sequence

**"How to…" questions**

- How to determine whether a series converges or diverges

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
