# Case Study: Firm Power

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

Priya Anand has the board packet open on the conference table, untouched, because she's still staring at the wall monitor instead. It's showing tonight's live system curve — the same shape it makes every single evening, a low shallow bowl all afternoon that suddenly rears up into a spike right around dinnertime and holds there for hours before it finally lets go. She has watched that exact shape happen enough times now that she doesn't need the monitor to know when it's coming. What she needs is a number.

Two folders sit in front of her, each one a signed-ready capacity contract her legal team finalized this week. One locks in a gas plant. The other locks in solar paired with batteries, plus a second charge nobody outside this industry has ever heard of, that exists specifically to make an intermittent resource promise to show up anyway. Both contracts cost real money the district doesn't get to spend twice. Both get voted on Thursday.

Her intern taps on the glass door, holds up two fingers — two minutes until the pre-board call. Priya doesn't look away from the monitor. The spike is already climbing.

She pulls both folders toward her.

---

## Background

Priya Anand is the resource adequacy planner for Solano Bay Community Power, a community choice aggregator (SEE APPENDIX F) that buys and contracts electricity supply on behalf of its member cities within the California ISO (CAISO) grid. Her job is to recommend, to the district's board, exactly one new capacity contract that closes the gap between what Solano Bay already has under contract and what its customers actually demand during the hours that matter most — and to defend that recommendation with real numbers, not a general sense of which technology "feels" more modern.

Two contracts are on the table, and Priya has already nicknamed them the way the board will hear them read into the record:

- **The Peaker Contract** — new natural-gas peaking capacity, fully dispatchable on demand at any hour.
- **The Firmed Solar Contract** — solar-plus-storage capacity, paired with a real, published capacity-accreditation charge (SEE APPENDIX D) that pays to bring its reliability up to the same standard as a gas plant's.

Solano Bay's own load is a small, stated share of CAISO's total system load (SEE APPENDIX E). CAISO itself publishes its real, system-wide hourly demand data (SEE APPENDIX A) — and Priya's district's own demand rises and falls with that same real system-wide curve, because Solano Bay's customers are part of the same grid, subject to the same heat and the same evening routines as everyone else on it.

Whichever contract Priya recommends has to cover Solano Bay's own peak — the hours each evening when demand climbs above what the district's existing contracts already reliably cover (SEE APPENDIX A, APPENDIX B). Both technologies price out in dollars per megawatt-hour, but only once solar-plus-storage's own raw cost is combined with the real firming charge that brings it to full reliability (SEE APPENDIX C, APPENDIX D) — comparing solar's cost alone against gas would not be a fair fight, and Priya knows the board will catch it if she tries.

The board also authorized a fixed monthly budget for this specific contract tranche (SEE APPENDIX E) — not enough, on its own, to fully explain either contract, but enough to be a real constraint Priya has to reason through.

The vocabulary and the "how to…" skills this case will ask you to research are listed in **Appendix G** — that is where Challenge 1 sends you. Every sourced figure and stated assumption in this case is documented in **Appendix H**.

Priya opens both folders.

---

## Dilemma

You are Priya Anand.

Do you:

**A.)** Recommend **the Peaker Contract** — new natural-gas peaking capacity **OR**

**B.)** Recommend **the Firmed Solar Contract** — solar-plus-storage capacity, firmed to full reliability

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A descriptive-statistics table** for the full 24-hour demand record (after you've filled in the missing hour in D2): the median, the first and third quartiles, the range, and a stated conclusion — with work shown, using the standard 1.5×IQR fence test — on whether the data set contains a statistical outlier.
- **D2 — A missing-data reconstruction**, showing your algebra: use the daily average logged separately by the district's monitoring system and the 23 known hourly readings to find the one redacted hour's demand, then verify your answer by recomputing the full 24-hour mean.
- **D3 — A peak-window and capacity-sizing table**: using your Appendix A/B work, the hours of the day Solano Bay's demand exceeds its third quartile, the district's own peak demand and third-quartile demand (both scaled from the real CAISO figures using Appendix E's stated share), and the resulting new capacity, in megawatts, Solano Bay needs to contract.
- **D4 — A unit-conversion and equation worksheet**: convert Appendix D's real firming charge from dollars per kilowatt-month into dollars per megawatt-year, shown as work, then set up and solve a multi-step equation for the megawatts of firming capacity Appendix E's monthly board budget could support on its own.
- **D5 — A total-cost comparison table**: for each contract, the megawatt-hours of coverage needed (from D3), the real dollar-per-megawatt-hour rate (Appendix C/D), and the resulting total dollar cost, with the two contracts' dollar-per-megawatt-hour rates stated side by side.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A — CAISO Real-Time Demand Record, 2026-09-01

The California Independent System Operator (CAISO) publishes its own real, system-wide electricity demand at five-minute resolution. The table below is the actual on-the-hour reading for each hour of a real day, drawn from that public feed.

| Hour | System demand (MW) | Hour | System demand (MW) |
|---|---|---|---|
| 00:00 | 26,956 | 12:00 | 24,473 |
| 01:00 | 25,795 | 13:00 | 24,811 |
| 02:00 | 24,558 | 14:00 | 25,821 |
| 03:00 | 23,822 | 15:00 | 27,257 |
| 04:00 | 23,371 | 16:00 | 29,388 |
| 05:00 | 23,893 | 17:00 | 30,943 |
| 06:00 | 25,151 | 18:00 | 32,842 |
| 07:00 | 26,390 | 19:00 | *(redacted — see below)* |
| 08:00 | 26,699 | 20:00 | 32,456 |
| 09:00 | 26,137 | 21:00 | 31,496 |
| 10:00 | 24,908 | 22:00 | 30,224 |
| 11:00 | 24,577 | 23:00 | 28,115 |

*The 19:00 reading was lost to a feed error. Before the outage, the district's own monitoring system had already logged that day's cumulative 24-hour average system demand as exactly **27,215.4 MW** — use that logged average, and the 23 known readings above, for Challenge D2.*

*Source and scope note: this is CAISO's real, published, system-wide demand — not Solano Bay's own demand directly. Appendix E states the assumption connecting the two.*

---

## Appendix B — Demand Shape, In Words

CAISO's real curve for this day is a shallow bowl through the morning and early afternoon, then a sharp evening climb, matching the well-documented "duck curve" pattern California's grid operators discuss publicly: solar generation drops off in the evening at the same time residential demand rises, and the two effects stack. Where that evening climb starts and ends, and how many hours it lasts, is exactly what Challenge D3 asks you to find from Appendix A's own data — this appendix deliberately does not give you the count.

---

## Appendix C — Gas Peaking: Levelized Cost

| Quantity | Value |
|---|---|
| Unsubsidized levelized cost of energy, new-build natural gas peaking plant, U.S. national range | $149 – $251 per megawatt-hour |
| Value used in this case | $149 per megawatt-hour (the low end of the real published range — SEE APPENDIX H for why) |

---

## Appendix D — Firmed Solar: Levelized Cost Plus Firming Charge

Grid operators including CAISO use a real, published measure called **effective load-carrying capability (ELCC)** to score how much of an intermittent resource's nameplate capacity can be counted on during the hours of highest system need — computed by grid operators from historical performance data: how often, in practice, a resource like this one was actually still producing power during the system's worst hours. A resource with ELCC below 100% has to be "firmed" — its contract requires the developer to also pay a real, published monthly capacity charge ("Net CONE," below) to a separate, fully-dispatchable backstop resource (in practice, usually an existing gas plant with spare capacity), so that if the batteries run low during an extended peak, that backup resource is contractually obligated to cover the shortfall. Concretely, in three steps: (1) Solano Bay pays the Net CONE rate every month to whichever backstop plant CAISO designates, whether or not that plant ever actually runs; (2) that standing payment is what obligates the backstop plant to be available and ready; (3) if an evening ever comes when the batteries run down before demand does, CAISO calls on that already-paid-for backstop plant to physically generate the remaining power, the same way an insurance premium is paid every month whether or not a claim is ever filed. It is not solar-plus-storage getting physically better at showing up — it is the contract paying someone else to guarantee it, the same way a band might pay a backup singer who almost never has to sing, just to guarantee the show never gets cancelled. This is what lets the combined package reach the same reliability as a plant like a gas peaker, which is scored at essentially 100% on its own and needs no such backup payment.

| Quantity (CAISO, solar-plus-4-hour-battery-storage) | Value |
|---|---|
| Unsubsidized levelized cost of energy | $73 per megawatt-hour |
| Effective load-carrying capability (ELCC) | 41% |
| Regional capacity factor used in the firming calculation | 43% |
| Net cost of new entry ("Net CONE") — the real, published monthly capacity payment | $18.92 per kilowatt-month |
| Levelized firming cost (published, computed from the figures above) | $69 per megawatt-hour |
| **Total: levelized cost plus firming cost** | **$142 per megawatt-hour** |

*The published formula behind the firming-cost row: Levelized Firming Cost ($/MWh) = [Nameplate Capacity (kW) × (1 − ELCC%) × Net CONE ($/kW-month) × 12 months] ÷ [Nameplate Capacity (MW) × Regional Capacity Factor (%) × 8,760 hours]. Challenge D4 asks you to work with the Net CONE figure directly, in different units — not to reproduce this exact formula end to end.*

---

## Appendix E — Modeling Assumptions

> These figures are **not sourced** as direct external citations. They are stated scenario assumptions, each grounded in a real basis described below. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Solano Bay Community Power's share of CAISO's total system demand | 3% | Real California community choice aggregators vary enormously in size — from under 100,000 customers to multiple millions (SEE APPENDIX H) — and no single real published figure exists for this fictional district. 3% is a stated, mid-range illustrative share, not a real utility's disclosed number. | This assumption scales every megawatt and megawatt-hour figure in Appendices A-D's downstream calculations (Challenges D3-D5) up or down together, proportionally — it does not change which contract wins the dollar-per-megawatt-hour comparison, since that ratio is scale-independent. It does change the absolute size of the capacity gap and the total dollar costs in D3 and D5. |
| MA2 | The board's authorized monthly budget for this specific capacity tranche | $10,000 per month | No public figure exists for a fictional district's internal budget authorization. Stated as a scenario constraint specifically to give Challenge D4's equation-solving work a real number to solve for, not to influence the Dilemma's own recommendation. | This value only affects Challenge D4's illustrative "how much firming capacity could the monthly budget alone support" side-calculation. It is not part of either contract's dollar-per-megawatt-hour rate and does not affect the balance between Option A and Option B. |

*No other figure in this case required a Modeling Assumption — see `RESEARCH_LOG.md` for the full source-by-source trail.*

---

## Appendix F — What a Community Choice Aggregator Is

A community choice aggregator (CCA) is a real kind of public agency that California law allows a city or group of cities to form. The split works like this: the CCA (Solano Bay, here) signs the actual supply contracts and decides where the electrons come from — a gas plant, a solar farm, a battery. The existing investor-owned utility (in Solano Bay's real-world region, this would be Pacific Gas & Electric) keeps owning and running the physical wires, poles, and meters, and keeps billing and repairing outages, exactly as before. A household doesn't notice the switch in daily life; the change happens entirely in who is contractually responsible for lining up the power supply. Dozens of real CCAs currently operate across California, ranging from a few hundred thousand customers to several million — Solano Bay Community Power in this case is a fictional, mid-size example of a real kind of organization.

---

## Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Quartiles
- Outlier
- Median
- Range
- Mean

**"How to…" questions**

- How to find a missing data element given the mean and the remaining elements of its set
- How to find the mean of a set of data
- How to find the percent of a number
- How to convert an amount with compound units
- How to solve a multi-step equation with a variable on one side

---

## Appendix H — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Real hourly CAISO system-wide demand, 2026-09-01 | 23,371 to 33,087 MW across the day | CAISO "Today's Outlook" historical demand feed ([data](https://www.caiso.com/outlook/history/20260901/demand.csv)) | fetched 2026-09-18 | HIGH |
| S2 | Gas peaking unsubsidized LCOE, U.S. national range | $149 – $251/MWh | Lazard, "Levelized Cost of Energy+," June 2025 (Version 18.0), Energy Generation section | accessed 2026-09-18 | HIGH |
| S3 | CAISO solar-plus-storage LCOE, ELCC, capacity factor, Net CONE, and levelized firming cost | $73/MWh LCOE; 41% ELCC; 43% capacity factor; $18.92/kW-month Net CONE; $69/MWh firming cost; $142/MWh total | Lazard, "Levelized Cost of Energy+," June 2025 (Version 18.0), "Cost of Firming Intermittency" section | accessed 2026-09-18 | HIGH |
| S4 | Real California CCAs vary from under 100,000 to several million customers | qualitative range | Clean Power Alliance / CalCCA public reporting (via general web search, multiple corroborating outlets) | accessed 2026-09-18 | MEDIUM |

*Modeling Assumptions MA1 and MA2 are documented in Appendix E, not repeated here. Full search trail and derivation arithmetic: `RESEARCH_LOG.md`.*

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
