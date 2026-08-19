Case Study: The Sunset Ramp
MS | Math | Case Study | 2026 | Launchpad

## Overview

The west wall of monitors is doing the thing it does every clear evening: six generation curves
sliding down together, and one number in the corner ticking downward faster than any of the others
can climb to meet it. Lena Marsh doesn't look away from it while she answers the phone one-handed.
"I see it," she says. "I'm looking at the same slope you are." On the desk beside her keyboard, a
procurement folder sits open to a bid page she has read four times tonight, a sticky note wedged in
the margin in her own handwriting: *how fast, not just how much.*

Tomorrow's evening ramp is forecast to be worse than today's — clearer skies, a little more solar
on the system than last month, the same stubborn need for something else to pick up the slack in
the exact minutes the sun gives up. Cascade Grid Authority's capital committee wants her
recommendation by morning, and the committee does not want to hear about total megawatts. They
already know both bids on her desk deliver plenty of megawatts. What they are going to ask, in the
first sixty seconds of tomorrow's meeting, is whether either one can actually keep up — not over an
hour, not on average, but at the single worst instant of the drop.

She minimizes the phone call and pulls two folders side by side: one full of battery discharge
curves, one full of a turbine's startup log. Somewhere in the gap between how fast a system can
respond and how fast the sun actually sets is the answer the committee is going to hold her to.

Her cursor sits on the tab she hasn't opened yet — the raw hourly generation data from tonight,
the actual slope she'll need to beat.

## Background

Lena Marsh is a resource-planning dispatcher at Cascade Grid Authority, a balancing authority
responsible for keeping electricity supply matched to demand, second by second, across its
service territory. Her specific accountability is the evening net-load ramp: the window each
clear day when the sun sets and solar generation falls away while electricity demand is still
high, and the rest of the system's dispatchable resources have to increase output, in real time,
to replace exactly what the sun stops providing. Cascade Grid Authority is a fictional balancing
authority; the evening ramp pattern this case asks Lena to analyze is modeled directly on real,
published net-load ramp statistics from CAISO, the real balancing authority most associated with
the "duck curve" (SEE APPENDIX B), because this evening ramp is a real, well-documented feature of
solar-heavy grids and not a hypothetical one.

The capital committee has two vendor bids in front of it for the same job — covering the evening
ramp — and it is evaluating them on the same basis: cost per unit of ramp-rate capability
delivered, not total price tag (SEE APPENDIX A).

**The Solar Stack** pairs 200 MW of new utility-scale solar generation with a 4-hour battery
energy storage system, sized to the same 200 MW of power for its full 4-hour discharge duration.
A battery can, in principle, respond to any rate of change almost instantly — its limit is not
speed, it is how many total megawatt-hours it holds before it runs out (SEE APPENDIX A).

**The Peaker Call** is a new 120 MW natural-gas peaker plant — a simple-cycle combustion turbine
built specifically to start quickly and run only during high-demand hours. A gas peaker has a
real, physical minimum ramp rate: the fastest rate at which its turbine can safely increase output
after starting, a mechanical limit that does not depend on how much fuel is in the tank (SEE
APPENDIX A).

Both resources are candidates for the same job: covering the evening ramp. Neither bid is useful to
the committee unless Lena can show, using the actual measured rate at which net system load rises
on a clear evening as solar falls away, whether that resource's response capability is fast enough
to cover it — and, if so, what it costs per unit of ramp rate covered, which is the number the
committee will actually compare (SEE APPENDIX A). The raw evening net-load data Lena must model is
in (SEE APPENDIX B). Any figure in this case that is not a matter of public record is stated as an
explicit modeling assumption (SEE APPENDIX C) rather than guessed, and every sourced figure is
listed in (SEE APPENDIX D). The vocabulary and the "how to…" skills this case will ask of you are
listed in **APPENDIX F** — that is where Challenge 1 sends you. For real-world background reading
beyond the required standards (SEE APPENDIX E).

## Dilemma

You are Lena Marsh.
Do you:
A.) Recommend The Solar Stack — 200 MW of solar plus a 4-hour, 200 MW battery OR
B.) Recommend The Peaker Call — a new 120 MW natural-gas peaker plant

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A continuous model P(t) of net system load (MW) versus time (minutes) fit to the hourly
    evening net-load data points spanning the steepest part of the ramp (SEE APPENDIX B), written
    as a polynomial in t — and its derivative dP/dt, found using the power rule and reported as
    the instantaneous rate of change of net load with respect to time. (Net load rising is exactly
    the amount of *other* generation — battery discharge, a peaker, or anything else on the system
    — that has to come online to replace the solar generation the sun is taking away.)
    D2. The equation of the tangent line to P(t) at the specific clock time of the steepest
    measured rise (found by evaluating dP/dt across the fitted window), with the tangent line's
    slope reported as the instantaneous ramp rate, in MW per minute, the grid must cover at that
    instant — plus a short, explicit justification that P(t) is differentiable at that point
    (addressing why a single smooth model is used across an hour boundary where the raw hourly
    data itself is not).
    D3. A ramp-response capability table: the battery's continuous full-power ramp-rate capability
    versus the gas peaker's minimum ramp rate after start, both converted to MW per minute (SEE
    APPENDIX A), set against the instantaneous ramp rate from D2, with a covered / not covered
    determination shown for each option — that is, does the option's own capability meet or exceed
    the D2 instantaneous rate?
    D4. A dollars-of-capital-cost-per-MW-per-minute-of-ramp-rate-covered calculation for each
    option, using each option's total capital cost (SEE APPENDIX A) divided by the MW/minute of
    the D2 rate that option actually delivers — its own capability figure from D3, capped at the
    D2 rate for any option whose own capability exceeds it — with the percent margin between
    Option A's and Option B's cost-per-ramp-rate-covered shown explicitly.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — The Two Ramp-Response Options

**The Solar Stack**

| | Value |
|---|---|
| Solar capacity | 200 MW (fixed by the bid) |
| Battery power rating | 200 MW |
| Battery duration | 4 hours (800 MWh total usable energy) |
| Battery full-power response time | **≤ about 1 second** to full rated output [S4] — grid-scale lithium-ion BESS are widely characterized as able to go from zero to full charge or discharge "almost instantaneously," with the frequency-regulation literature reporting response on the order of 100–500 milliseconds |
| Battery ramp-rate capability, derived | derived: 200 MW achieved within 1 second = 200 MW ÷ (1/60 min) = **12,000 MW per minute**, the student's own work in D3 — this is a theoretical ceiling; APPENDIX C notes why it is not the binding limit on this option |
| Solar PV capital cost basis | **$1,502 per kW** (overnight capital cost, 150 MWAC single-axis-tracking utility-scale solar PV reference case) [S1] |
| Total installed capital cost, solar PV portion | derived: 200,000 kW × $1,502/kW = **$300,400,000** — the student's own work in D4 |
| Battery storage capital cost basis | **$1,744 per kW** (equivalently $436/kWh; 150 MW / 600 MWh, 4-hour lithium-ion BESS reference case — the same 4-hour duration class as this option's battery) [S2] |
| Total installed capital cost, battery portion | derived: 200,000 kW × $1,744/kW = **$348,800,000** — the student's own work in D4 |
| Total capital cost, The Solar Stack | derived: $300,400,000 + $348,800,000 = **$649,200,000** — the student's own work in D4 |

**The Peaker Call**

| | Value |
|---|---|
| Nameplate capacity | 120 MW (fixed by the bid) |
| Peaker minimum ramp rate after start | **50 MW per minute** — GE Vernova's own published characterization of the "nominal ramp rate" for the aeroderivative combustion-turbine class this reference case belongs to (as opposed to ~5 MW/min for reciprocating engines) [S3] |
| Peaker capital cost basis | **$1,606 per kW** (overnight capital cost, 4×54 MW gross aeroderivative simple-cycle reference case, 211 MW net) [S1] |
| Total installed capital cost | derived: 120,000 kW × $1,606/kW = **$192,720,000** — the student's own work in D4 |

Both capital-cost figures are drawn from the same single EIA-commissioned cost study (SEE APPENDIX
D, source S1), so the comparison uses one consistent cost basis across all three technologies. The
solar and battery capital-cost figures for The Solar Stack come from the same study's companion
reference cases, at matching plant sizes and, for the battery, the matching 4-hour duration class.

## Appendix B — The Evening Net-Load Data

Cascade Grid Authority is fictional; the table below is a stated Modeling Assumption, not a
directly-sourced table (SEE APPENDIX C, MA1) — but it is not invented out of nothing. It is shaped
to match the one real, dated, cited statistic this case could obtain for a specific hour of
CAISO's evening ramp: CAISO's net load increases by an average of **6.5 GW during the 6:00 p.m.
hour** [S5], the steepest single hour of a typical clear-day evening ramp. The table below places
that real 6,500 MW rise between its 18:00 and 19:00 points exactly, and fills in the hours before
and after with a smooth, realistic evening-ramp shape (low and flat in the afternoon, steepest
around sunset, leveling off by 20:00):

| Clock time | Net system load (MW) |
|---|---|
| 16:00 | 18,000 |
| 17:00 | 19,500 |
| 18:00 | 22,500 |
| 19:00 | 29,000 |
| 20:00 | 32,500 |

Model P(t) (D1) from the three consecutive data points spanning the steepest single-hour rise in
the table above — 17:00, 18:00, and 19:00; the remaining points are for context and for checking
the model against the data outside the fitted window.

## Appendix C — Modeling Assumptions

> These figures are **not sourced** as a directly-published table. They are a stated scenario
> assumption chosen by the case author, anchored to a real, cited statistic. A Hero may challenge
> them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | The five hourly net-system-load figures in Appendix B, 16:00–20:00 | 18,000 / 19,500 / 22,500 / 29,000 / 32,500 MW | A genuine attempt was made to source a real, timestamped, minute-or-hour-resolution net-load or generation-by-fuel table for a specific real evening from EIA's Hourly Electric Grid Monitor, EIA's legacy Electricity Data Browser, CAISO's Today's Outlook/OASIS system, and CAISO's legacy Daily Renewables Watch archive — all four are genuinely real, primary data sources, but none returned a fetchable, machine-readable table through the tools available for this research pass (see RESEARCH_LOG.md for the specific attempts and failure modes). Rather than invent an unanchored table, this case instead builds the table to reproduce exactly one real, dated, cited figure — CAISO's own reported average net-load increase of 6.5 GW during the 6:00 p.m. hour [S5] — placed between the table's 18:00 and 19:00 points, with the surrounding hours shaped to a realistic, smooth evening-ramp curve. | The fitted model's peak instantaneous rate (D2) is highly sensitive to the exact shape chosen between data points, not just their hourly totals — a quadratic fit constrained to match the same 6,500 MW hourly total could still return a peak instantaneous rate anywhere from a little above 108 MW/min (the hourly average) to well above 137.5 MW/min, depending on how convex the true curve is. This is exactly the kind of "how much does the shape between two anchor points matter" question the Socratic discussion should surface. |

## Appendix D — Sources

| # | Claim | Value | Source | Accessed | Confidence |
|---|---|---|---|---|---|
| S1 | Overnight capital cost for three reference generating technologies: (a) 150 MWAC single-axis-tracking solar PV, (b) 4×54 MW gross aeroderivative simple-cycle combustion turbine (211 MW net), used as the basis for this case's peaker | (a) $1,502/kW; (b) $1,606/kW | U.S. Energy Information Administration / Sargent & Lundy, *Capital Cost and Performance Characteristics for Utility-Scale Electric Power Generating Technologies* (report SL-018001, prepared for AEO2025), January 2024, Table 1-2 — Cost & Performance Summary Table ([link](https://www.eia.gov/analysis/studies/powerplants/capitalcost/pdf/capital_cost_AEO2025.pdf)) | 2026-08-13 | HIGH — the primary EIA-commissioned engineering cost study used to build EIA's own National Energy Modeling System; one consistent methodology across every technology this case compares |
| S2 | Overnight capital cost for a 150 MW / 600 MWh (4-hour) lithium-ion battery energy storage system reference case | $1,744/kW (equivalently $436/kWh) | Same source and table as S1, Case 19 — Battery Energy Storage System ([link](https://www.eia.gov/analysis/studies/powerplants/capitalcost/pdf/capital_cost_AEO2025.pdf)) | 2026-08-13 | HIGH — same primary source as S1; the reference case's 4-hour duration matches this case's battery exactly, so no duration-adjustment assumption is needed |
| S3 | "Nominal ramp rate" for the aeroderivative gas-turbine class (as distinct from reciprocating engines, cited at ~5 MW/min) | ~50 MW/min | GE Vernova, LM6000 Aeroderivative Gas Turbine product page — GE Vernova's own published comparison of aeroderivative vs. reciprocating-engine ramp rates ([link](https://www.gevernova.com/gas-power/products/gas-turbines/lm6000)) | 2026-08-13 | MEDIUM — a manufacturer's own stated class-level figure (not tied to a specific unit count or a specific 120 MW plant configuration); it is applied here as a representative plant-level capability for a new aeroderivative simple-cycle peaker of this class, which is how the source itself frames the comparison, but the source does not confirm whether "50 MW/min" scales linearly with the number of turbine units in a specific plant |
| S4 | Grid-scale lithium-ion battery response time to full rated power | "almost instantaneously"; frequency-regulation literature reports 100–500 ms | Modo Energy, *Ramp rates in Dynamic frequency response services* ([link](https://modoenergy.com/research/ramp-rates-dynamic-frequency-response-services-battery-energy-storage)), corroborated by published battery-frequency-regulation response-time figures (100–500 ms) reported across multiple peer-reviewed and industry sources | 2026-08-13 | MEDIUM — a qualitative/order-of-magnitude characterization from a specialist battery-market research firm rather than a single manufacturer datasheet for one specific unit; used here only to establish that the battery's ramp *rate* is not the binding constraint on this option (its *duration* is), so the exact millisecond figure is not load-bearing to the dilemma the way the peaker's 50 MW/min figure is |
| S5 | CAISO's average net-load increase during the steepest single hour (6:00 p.m.) of a typical evening ramp | 6.5 GW (6,500 MW) | Modo Energy, *CAISO: Flexible Ramping Product is tailored to BESS, but opportunity is limited* ([link](https://modoenergy.com/research/en/caiso-flexible-ramping-product-reliability-challenge-battery-energy-storage-revenue-opportunity)) | 2026-08-13 | MEDIUM — a reputable specialist grid/battery-market research firm publishing CAISO operational statistics; the article does not name the specific underlying CAISO database (e.g., OASIS) it drew the figure from, so it is graded MEDIUM rather than HIGH despite being the load-bearing anchor for Appendix B's Modeling Assumption (MA1) |

## Appendix E — Learn More

These are real, live, outside resources for anyone curious about the evening ramp and the
technologies in this case, beyond what the Challenges require. They are optional background
reading, not part of any graded deliverable.

- [Wikipedia — Duck curve](https://en.wikipedia.org/wiki/Duck_curve): an overview of how the
  "duck curve" got its name and why solar-heavy grids like CAISO's face a steep evening ramp.
- [CAISO — Today's Outlook](https://www.caiso.com/todays-outlook): California ISO's live
  dashboard of real-time grid demand, net demand, and renewable output, the same kind of data
  behind Appendix B.
- [U.S. EIA — "Battery storage capacity averaged 70% growth over the last three
  years"](https://www.eia.gov/todayinenergy/detail.php?id=67925): a short EIA article on how fast
  utility-scale battery storage like The Solar Stack's has actually been growing nationwide.
- [U.S. EIA — How electricity is
  generated](https://www.eia.gov/energyexplained/electricity/how-electricity-is-generated.php): a
  plain-English explainer on turbines, generators, and the different technologies (including gas
  combustion turbines like The Peaker Call) that make U.S. electricity.
- [Math Is Fun — Derivative Rules](https://www.mathsisfun.com/calculus/derivatives-rules.html): a
  clear walkthrough of the power rule and other derivative rules, useful alongside D1's
  power-rule work.

## Appendix F — "How To…" Math Questions To Research

**Vocabulary terms**

- Derivative
- Instantaneous Rate Of Change
- Tangent Line
- Differentiable

**"How to…" questions**

- How to find a derivative using the power rule
- How to find the equation of a tangent line at a point
- How to convert an amount with compound units
- How to find the percent of a number

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
