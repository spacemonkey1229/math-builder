Case Study: The Deferred Repair
MS | Math | Case Study | 2026 | Adventure

## Overview

The service bay smells like hot metal and burnt coffee, and the shop's tablet is propped against the counter with three checkboxes still unticked. Elena Castillo checks her phone — a text from her 10:00 a.m. patient's daughter, already fifteen minutes into the window she promised. The mechanic taps a wrench against his palm and points at the tablet screen without looking up. "Coolant's overdue. So's the trans fluid. Cabin filter's due too, but that one's your call." He says it the same way for all three, like they're the same kind of decision.

Elena's cousin — a mechanic two towns over, not this one — told her once, half-joking, that shops flag everything the same shade of red whether it's about to strand you or just about to smell a little musty. She doesn't have the cash today to say yes to all three, and she's not sure which of the shop's warnings is a real number and which one is just how shops talk.

Her thumb hovers over the tablet. Three checkboxes. One phone still buzzing, face-down, on the counter next to the estimate.

## Background

Elena Castillo has been a home health aide for nine years, driving her own car between patients' houses across the county — the job doesn't reimburse mileage unless the car actually runs. Her 2016 sedan is paid off, which is the only reason her monthly budget works at all; a car payment isn't an option, so she has decided the car needs to hold up for at least three more years before she can save enough to replace it.

At today's oil change, the shop's inspection flags three services (SEE APPENDIX A): a coolant flush, a transmission fluid service, and a cabin air filter replacement. All priced and sourced figures in this case are cited in (SEE APPENDIX E); the probability figures in Appendices B and C are, honestly, stated Modeling Assumptions rather than sourced numbers — see the Modeling Assumptions section for why. The vocabulary and "how to…" procedures needed to work through those figures are listed in (SEE APPENDIX D). She can't afford all three today, and she's learned from her cousin, an independent mechanic, that shops routinely flag services with very different real risk profiles using the exact same urgent tone. She has to decide which flagged item, if any, is actually worth paying for now — and which are safe to keep deferring.

The coolant flush is the one her cousin warned her about directly: skip it enough times in a row, and the probability of a serious overheating-related repair climbs every additional year she keeps skipping it (SEE APPENDIX B). Paying for it every time it's flagged — The Standing Order — converts that risk into a small, certain cost: she pays it or she doesn't, and if she pays it, that is the whole cost, regardless of what the engine does later. Declining it and paying only if the engine actually fails — The Reactive Route — keeps the cash in her pocket every year nothing goes wrong, at the price of that climbing risk.

The other two flagged items look identical on the printed estimate — same shop tone, same "overdue" flag, broadly similar price — but their own failure data over Elena's three-year ownership horizon does not necessarily tell the same story as the coolant system (SEE APPENDIX C). Whatever she decides about the coolant flush, some of the shop's other flags may not deserve the same dollar-for-dollar treatment.

Elena has already committed to the three-year horizon: replacing the car early because of a preventable engine failure would cost her far more than the repair bill on the receipt, since the car is how she earns her income in the first place.

## Dilemma

You are Elena Castillo.
Do you:
A.) Approve the coolant flush every time the shop flags it, for as long as you own the car — The Standing Order OR
B.) Decline the flagged coolant flush and pay for the repair only if the engine failure actually happens — The Reactive Route

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A three-year conditional-probability table for The Reactive Route: the Year 1 probability
    of a coolant-related failure, the Year 2 probability given the engine did NOT fail in Year 1,
    and the Year 3 probability given it did not fail in either Year 1 or Year 2 — each pulled from
    Appendix B's sourced failure-rate data, with the conditioning stated in words for every row.
    D2. A compound-probability calculation, shown step by step, of the chance the engine fails at
    least once across all three years of continuous skipping — computed from the complement of
    "no failure in any of the three years," using the Year 1/2/3 probabilities from D1.
    D3. An expected-annual-cost comparison table: The Standing Order's certain, constant per-year
    cost from Appendix A, next to The Reactive Route's probability-weighted expected cost for each
    of the three years (that year's failure probability multiplied by Appendix B's full repair
    cost), with the arithmetic for every cell shown.
    D4. A written filtering decision: using Appendix C's failure and repair data for the
    transmission fluid service and the cabin air filter, state which of those two flagged services
    you would treat the same way as the coolant flush and which you would not — defended with each
    service's own three-year failure probability, not with the shop's tone or price alone.
    D5. An original visual display (a bar chart, a probability tree, or equivalent) comparing The
    Standing Order's three-year total cost against The Reactive Route's three-year expected cost,
    built from your D3 figures.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — The Shop's Inspection Sheet

Three services, flagged the same way on the same printed estimate. (SEE BACKGROUND)

| Flagged service | Shop's quoted price (per visit) | Shop's stated reason if skipped |
|---|---|---|
| Coolant flush | $473 [S1] | "System runs hotter than spec; risk goes up the longer it's put off." |
| Transmission fluid service | $313 [S2] | "Overdue per mileage interval." (shop's standard boilerplate note, printed identically on every visit) |
| Cabin air filter replacement | $102 [S3] | "Overdue per mileage interval." (same boilerplate note as above) |

## Appendix B — Coolant System Failure-Rate Table (if the flush keeps getting skipped)

Referenced in Background and Challenge 3 (D1, D2, D3).

| Year of continuous skipping | Probability of a coolant-related failure that year | Source type needed |
|---|---|---|
| Year 1 (first year skipped) | 9% (MA1) | stated modeling assumption — see Modeling Assumptions |
| Year 2 (given no failure in Year 1) | 13% (MA1) | stated modeling assumption — see Modeling Assumptions |
| Year 3 (given no failure in Years 1–2) | 20% (MA1) | stated modeling assumption — see Modeling Assumptions |
| Repair cost if the coolant system fails | $2,938 [S4] | RepairPal fair-price estimator, head-gasket replacement (proxy — see note) |

**RESEARCH FLAG RESOLVED:** a genuine search (RepairPal, CarMD's Vehicle Health Index, AAA
newsroom releases, Car Care Council press material, and mechanic-trade coverage) turned up no
publicly available per-year or conditional failure-probability schedule for "coolant system fails
after a skipped flush" — this figure is not published anywhere at any confidence grade; it does
not exist as a citable dataset, not merely a hard-to-find one. The Year 1–3 probabilities are
therefore a **stated Modeling Assumption (MA1)**, not a sourced figure — see the Modeling
Assumptions block below for the full basis and sensitivity. The repair-cost row **is** sourced: it
uses RepairPal's head-gasket-replacement estimate as the standard, most commonly cited real-world
outcome of chronic coolant-system neglect (a proxy for "the coolant-related failure," not
necessarily the only possible one — see [S4]'s note).

## Appendix C — Comparison: The Other Two Flagged Services

Referenced in Background and Challenge 3 (D4). Deliberately included so the student must decide,
using each service's own numbers, whether it deserves the same treatment as the coolant flush —
not every flagged service necessarily does.

| Flagged service | Three-year cumulative probability of a billable mechanical failure if skipped | Repair/replacement cost if it fails |
|---|---|---|
| Transmission fluid service | 15% (MA2) | $6,426 [S5] |
| Cabin air filter replacement | ~0% — no billable mechanical failure is attributed to this service in any source found (MA3) | N/A — no repair is attributable (see Modeling Assumptions) |

No published source gives a three-year cumulative transmission-failure probability conditional on
a skipped fluid service, or a probability that a skipped cabin air filter causes a *mechanical*
(as opposed to comfort/air-quality) failure. Both probability cells are stated Modeling
Assumptions (MA2, MA3) — see below. The transmission **replacement cost** is a real sourced
figure [S5]; no cost placeholder applies to the cabin filter row because the research turned up no
source attributing a billable repair to it at all (that absence is itself the answer Challenge 3
(D4) is testing for).

## Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author because a genuine, multi-tier search (RepairPal, CarMD's Vehicle Health Index, AAA
> newsroom releases, Car Care Council press material, and mechanic-trade publications) found no
> publicly published per-year, conditional, or three-year-cumulative failure-probability schedule
> for any of these three services. A Hero may challenge these numbers in discussion — that is a
> legitimate move, and the sensitivity column shows exactly where the challenge would matter.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Year 1 / Year 2 (given no Y1 failure) / Year 3 (given no Y1–Y2 failure) probability of a coolant-related failure after a skipped flush | 9% / 13% / 20% | No source publishes a per-year conditional failure-probability schedule for a skipped coolant flush. The values are chosen to (a) escalate year over year, consistent with the well-documented general finding that deferred maintenance risk compounds the longer a service is skipped, and (b) keep the three-year compound failure probability (≈36.7%, see D2) in the range repeatedly described — without a precise figure — by mechanic-trade sources as "a real, non-trivial risk," not a rounding error. | This is the single assumption the case's recommendation is most sensitive to. A modest, defensible challenge to any one year's value in discussion could change which option comes out ahead once D3's expected-cost comparison is redone with that changed value — work the comparison yourself rather than taking 9%/13%/20% as unchallengeable fact. |
| MA2 | Three-year cumulative probability of a billable transmission failure if fluid service is skipped | 15% | No source publishes this figure. Set lower than the coolant system's compound probability (≈36.7%) because multiple mechanic-trade sources (Engine Builder Magazine, Transmission Digest) independently place complete transmission failure from never-changed fluid at 80,000–120,000 miles of neglect — well beyond a typical 3-year/~36,000-mile skip window — while coolant-system stress from a skipped flush begins accumulating (scale, corrosion, restricted flow) immediately. | A Hero who challenges this probability, up or down, changes how the transmission service compares to the coolant flush in Challenge 3 (D4) — work out the actual expected-cost comparison against Appendix C's $6,426 replacement cost [S5] yourself, rather than relying on the shop's tone or price alone. |
| MA3 | Probability a skipped cabin air filter replacement causes a billable *mechanical* repair (as opposed to reduced airflow, odor, or comfort issues) | ~0% (treated as negligible / not applicable) | Every mechanic-trade and filter-manufacturer source found (CARFAX, FilterBuy, Premium Guard, Interfil) describes the consequences of a skipped cabin air filter exclusively in terms of reduced airflow, uneven cooling, odor, and blower-motor strain in "extreme cases" — none quantifies or documents an actual billable mechanical-repair rate. No source treats this as a mechanical-failure risk on the order of the other two services. | This assumption is not sensitive to challenge in the same dollar-comparison sense as MA1/MA2, since no repair cost exists to weigh it against — but it is central to Challenge 3 (D4)'s filtering exercise. Decide for yourself, from the evidence given here, whether "same shop tone" really means "same risk category." |

## Appendix D — "How To…" Math Questions To Research

**Vocabulary terms**

- Probability
- Event
- Outcome
- Dependent Event
- Conditional Probability

**"How to…" questions**

- How to determine the probability of a single event
- How to determine the probability of a compound event
- How to determine the probability of conditional events
- How to find the percent of a number

## Appendix E — Sources

All sourced (non-assumption) figures in this case are cited here.

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Typical coolant flush/change cost, independent shop, national average | $473 | RepairPal — [Coolant Change Cost Estimate](https://repairpal.com/estimator/coolant-change-cost) | Aug 2026 | MEDIUM |
| S2 | Typical transmission fluid change cost, independent shop, national average | $313 | RepairPal — [Transmission Fluid Change Cost Estimate](https://repairpal.com/estimator/transmission-fluid-change-cost) | Aug 2026 | MEDIUM |
| S3 | Typical cabin air filter replacement cost, independent shop, national average | $102 | RepairPal — [Cabin Air Filter Replacement Cost Estimate](https://repairpal.com/estimator/cabin-air-filter-replacement-cost) | Aug 2026 | MEDIUM |
| S4 | Repair cost for the standard real-world outcome of chronic coolant-system neglect (head-gasket failure) | $2,938 | RepairPal — [Head Gasket Replacement Cost Estimate](https://repairpal.com/estimator/head-gasket-replacement-cost) | Aug 2026 | MEDIUM |
| S5 | Transmission replacement cost, national average | $6,426 | RepairPal — [Transmission Replacement Cost Estimate](https://repairpal.com/estimator/transmission-replacement-cost) | Aug 2026 | MEDIUM |

All five RepairPal figures are the midpoint of RepairPal's published low–high estimate range as of
the access date; ranges do not include taxes, fees, or regional variation, and are not specific to
a 2016 sedan. See `RESEARCH_LOG.md` for the full search trail, including sources consulted and
rejected for Appendix B and Appendix C's probability figures (now Modeling Assumptions MA1–MA3
above).

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
