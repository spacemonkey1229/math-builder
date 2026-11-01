Case Study: The Surge Trigger
MS | Math | Case Study | 2026 | Launchpad

## Overview

Dr. Renata Cho has one laptop, two tabs open, and a mobile vaccination-and-testing unit idling in a parking lot on the wrong side of the county. On the left tab: a case-count model she built herself, fitted to Eastgate's earliest numbers, curving upward in a way that makes her stomach tighten. On the right: the county's own daily dashboard — the numbers her director actually watches, the numbers that will show up in tomorrow's briefing — climbing, but slower, gentler, nothing like the shape on the left.

Her phone buzzes. It's the mobile unit's driver: *"Still in the Riverside lot. You said stand by. Standing by."* Riverside has been quiet for two weeks. Eastgate hasn't.

The gap between her two screens is the whole problem. One shows what she believes is actually happening. The other shows what the county can currently prove is happening. Moving the unit off a model nobody has confirmed costs her department real money and real credibility if she's wrong. Waiting for the dashboard to catch up costs something else entirely — every day the unit sits in Riverside is a day Eastgate goes uncovered while its numbers keep climbing underneath the surface everyone else can see.

She pulls up her derivative work again. Somewhere in these two curves is the exact day each of them crosses the line her department already agreed would trigger a move. She just has to find it — and defend which curve she trusted.

## Background

Dr. Renata Cho is the epidemiologist responsible for mobile-resource allocation at the Two Rivers County Health Department. She owns the call on when the department's single mobile vaccination-and-testing unit — currently stationed in the Riverside neighborhood — gets redeployed to Eastgate, where a new respiratory-illness cluster is accelerating (SEE APPENDIX A). The unit cannot be split or duplicated; moving it is a same-day, one-time decision, and the department's own policy requires that decision be defended with the math behind it, not a gut call.

Two curves are available to make that call. The first is Eastgate's *true* daily new-case count — never directly observable, but modeled by fitting an exponential growth curve to the earliest confirmed cases (SEE APPENDIX A). The second is Eastgate's *reported* daily new-case count — the only curve the department can actually see in real time, because it depends on how large a share of true cases the county's testing sites are actually catching, a share that is not constant (SEE APPENDIX C). Two trigger designs are on the table, and they disagree about which curve to trust (SEE APPENDIX B): the department's existing policy sets a numeric growth-rate threshold for each curve, and neither option is free — a wrong or late call has a real, disclosed cost either way (SEE APPENDIX D). The vocabulary and "how to…" procedures needed to build and compare both trigger designs are listed in (SEE APPENDIX E), and every sourced or assumed figure in this case is documented in (SEE APPENDIX F).

The two options are named on Dr. Cho's whiteboard: **The True-Curve Trigger**, which redeploys the unit the moment the modeled true-infection curve's growth rate crosses its threshold, or **The Reported-Curve Trigger**, which waits for the only curve the department can directly observe to cross its own threshold. Dr. Cho has to pick one, defend the total-cost math behind it, and radio the driver before the day is out.

## Dilemma

You are Dr. Renata Cho.
Do you:
A.) Order the move under the True-Curve Trigger — redeploy the moment the modeled true-infection curve's growth rate crosses threshold OR
B.) Order the move under the Reported-Curve Trigger — wait for the observable reported-case curve's growth rate to cross its own threshold

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. The true-infection model I(t) from Appendix A, differentiated using the chain rule to
    find I'(t) (shown step by step, naming the outer and inner functions), the exact day t_A
    where I'(t) first equals Appendix D's True-Curve threshold, and the equation of the tangent
    line to I(t) at t = t_A.
    D2. The reported-case model D(t) = I(t) × c(t) from Appendices A and C, differentiated using
    the product rule to find D'(t) (shown step by step, naming both factors and their own
    derivatives), and the exact day t_B where D'(t) first equals Appendix D's Reported-Curve
    threshold.
    D3. A classification of D(t)'s one critical point in this window as a local maximum (using
    D'(t) from D2 and a sign argument or equivalent reasoning), the day it occurs and D(t)'s
    value there, and a written comparison to I(t)'s behavior over the same window — specifically,
    whether I(t) has any turning point of its own in this window, and what that difference means
    for anyone who assumes the reported curve peaking means the true outbreak is peaking.
    D4. A quotient-rule derivation of R(t) = D(t) / I(t), shown step by step with the full
    (D′I − DI′)/I² setup before any simplification, verifying algebraically that R(t) reduces
    exactly to Appendix C's capture-rate model c(t) — then, using t_A (D1) and t_B (D2), the
    resulting lag in days, the resulting gap in that day's new-case count between the two trigger
    days, and a total-expected-cost calculation for each trigger design using Appendix D's cost
    figures, shown step by step for both options.
    D5. A one-paragraph written recommendation that names which trigger design has the lower
    total expected cost and explicitly addresses why assuming the reported curve is "the same
    outbreak, just a delayed copy" of the true curve — rather than a curve with its own,
    genuinely different shape — would have been misleading, citing D3's finding directly.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — Outbreak Model Inputs

Referenced in Background and Challenge 3 (D1, D3). Eastgate's true daily new-case count is
modeled as exponential growth, unmitigated by any intervention yet in this window:

I(t) = I0 · e^(k·t), where t is measured in days since the model's start date.

| Input | Value used |
|---|---|
| I0 — true new cases on day 0 | 4 cases/day (MA1) |
| k — true daily growth-rate constant | 0.094 per day (MA2) |

**RESEARCH FLAG RESOLVED:** no public source publishes Two Rivers County's own real-time case
count or growth-rate constant — this is internal, day-to-day operational surveillance data
specific to one (fictional) county, and it does not exist anywhere as a citable external dataset.
I0 is a stated, disclosed Modeling Assumption (MA1). k is also a stated Modeling Assumption (MA2),
but it is directly informed by a real, cited early-outbreak growth-rate figure — see the Modeling
Assumptions section below and Appendix F, [S1].

## Appendix B — Two Proposed Trigger Designs

Referenced in Background and Dilemma. Both designs watch for the same underlying kind of signal —
a case-count curve's growth rate crossing a threshold — but apply it to two different curves.

| Design | Signal watched | Trigger condition | Proposed by |
|---|---|---|---|
| Option A — The True-Curve Trigger | I(t), Appendix A's modeled true-infection curve | I'(t) ≥ Appendix D's True-Curve threshold | Dr. Cho's own design, using her fitted model directly |
| Option B — The Reported-Curve Trigger | D(t) = I(t) · c(t), Appendix C's reported-case curve | D'(t) ≥ Appendix D's Reported-Curve threshold | The department's existing default policy, since D(t) is the only curve visible in real time |

Neither design is free to act on. Option A relies on an unconfirmed model of a curve nobody can
directly observe, which is why the department's own protocol requires a paid verification step
before committing the unit on that signal alone (SEE APPENDIX D). Option B relies only on data the
department already has, but Appendix C's declining testing-capture rate means D(t) is not simply a
scaled-down copy of I(t) — real, published research on outbreak response documents that testing
and reporting capacity commonly comes under strain as case volume rises, reducing the share of
true infections that get captured and reported in real time, which is exactly the mechanism
Appendix C's capture-rate model represents.

## Appendix C — Testing Capture-Rate Model

Referenced in Background, Appendix B, and Challenge 3 (D2, D4). Not every true infection in
Eastgate is caught and reported — only a share, and that share is not constant. It is modeled as a
declining linear function of time:

c(t) = c0 − m·t, where c(t) is the fraction of that day's true cases that show up in the county's
reported numbers.

| Input | Value used |
|---|---|
| c0 — capture rate at day 0 | 0.65 (65% of true cases captured) (MA3) |
| m — daily rate of capture-rate decline | 0.015 per day (MA3) |

The reported-case curve is then D(t) = I(t) · c(t) — Appendix A's true-infection curve, scaled down
by whatever share of it the county's testing capacity can actually catch that day.

**RESEARCH FLAG RESOLVED:** no public source publishes any specific county's real-time testing-
capture-rate curve for a specific (fictional) local outbreak — this is stated as Modeling
Assumption MA3, disclosed below.

## Appendix D — Trigger Thresholds and Cost Inputs

Referenced in Background and Challenge 3 (D1, D2, D4).

| Item | Value used |
|---|---|
| True-Curve trigger threshold (on I'(t)) | 1.00 new cases/day, per day (MA4) |
| Reported-Curve trigger threshold (on D'(t)) | 0.40 new cases/day, per day (MA4) |
| Cost of Option A's mandatory verification protocol (flat, one-time) | $1,700.00 (MA5) |
| Average cost per additional case in that day's case count, if the department's response to it is delayed | $312.00 [S4] |

**What "total expected cost" means here:** Option A is charged the flat verification-protocol cost
no matter what, because department policy requires it before acting on any unconfirmed model.
Option B is charged for the gap in that day's new-case count between the day Option A's signal
would have fired and the day Option B's signal actually fires — a real, dollar-costed consequence
of the reported curve reacting later than the true curve.

## Modeling Assumptions

> These figures are **not sourced from an external publisher**. They are stated scenario
> assumptions chosen by the case author because Two Rivers County's own daily case counts, testing-
> capture curve, and internal trigger-threshold policy are internal operational data no public
> health department publishes. A Hero may challenge these numbers in discussion — that is a
> legitimate move, and the sensitivity column shows exactly where the challenge would matter.
>
> The Basis columns below cite real research: a peer-reviewed early-outbreak growth-rate estimate
> (independently confirmed via a CDC journal), and real published economic-burden and mobile-
> clinic-cost research — see Appendix F for what each source is and how each figure is used.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | True new cases in Eastgate on day 0 (I0) | 4 cases/day | No source publishes any specific (fictional) county's own internal daily case count. Chosen as a small, realistic count for an outbreak just beginning to accelerate — large enough to be a real signal, small enough that the department is not already in visible crisis. | This value scales both curves proportionally, but the case's cost comparison depends on the *gap* between the two trigger days, not the absolute scale — work the comparison yourself with a different plausible starting count before assuming the recommendation is unaffected. |
| MA2 | True daily growth-rate constant (k) | 0.094 per day | No source publishes Two Rivers County's own real-time growth constant. Directly informed by a real, peer-reviewed early-outbreak doubling-time estimate of 7.4 days [S1] (k = ln(2) ÷ 7.4 ≈ 0.094), applied here as this case's stated growth scenario since no source exists for this specific fictional county's own rate. | Held fixed in this case's sensitivity testing — changing k would redesign the entire outbreak scenario rather than flex a single operational dial, the same treatment this corpus gives a structural threshold rather than a cost or count assumption. |
| MA3 | Testing capture-rate model (c0, m) | c0 = 0.65, m = 0.015/day | No source publishes any specific county's own real-time testing-capture curve. The declining share reflects a well-documented operational pattern — testing and reporting capacity commonly comes under strain as case volume rises during a surge, reducing the share of true infections actually captured in real time. | Both c0 and m shift when Option B's trigger fires and how large Appendix C's gap in D3/D4 turns out to be — a Hero who challenges either value should redo Challenge 3 (D2, D4) with a different plausible pair before assuming the recommendation is unaffected. |
| MA4 | True-Curve and Reported-Curve trigger thresholds | 1.00 and 0.40 new cases/day, per day, respectively | These are Two Rivers County's own internal policy thresholds — no public source publishes the exact numeric trigger threshold any specific health department sets for either a modeled or an observed case-growth signal, and the two thresholds are set independently because the two curves are measured on genuinely different scales (Appendix C's capture rate keeps D(t) and its derivative structurally smaller than I(t) and its derivative). | Held fixed in this case's sensitivity testing for the same structural reason as MA2 — changing a threshold reshuffles which day each design fires on entirely, a redesign rather than a dial. |
| MA5 | Cost of Option A's mandatory verification protocol | $1,700.00 | No single published source states the exact dollar cost of a county health department's own model-verification protocol. Informed by real, cited mobile-clinic operating-cost research [S3] (roughly $753/day of equivalent mobile-unit operating cost) plus the additional senior-staff review time a verification step realistically requires beyond a single unit-day. | This figure sets Option A's entire cost total directly — a Hero who challenges it should redo Challenge 3 (D4) with a different value before assuming the recommendation is unaffected. |

## Appendix E — "How To…" Math Questions To Research

**Vocabulary terms**

- Local Maximum

**"How to…" questions**

- How to use the chain rule to differentiate a composite function
- How to use the product rule to differentiate a product of functions
- How to use the quotient rule to differentiate a quotient of functions
- How to find the equation of a tangent line at a point

## Appendix F — Sources

All sourced (non-assumption) figures in this case are cited here.

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Early-outbreak epidemic doubling time, a well-established peer-reviewed estimate | 7.4 days (95% CI, 4.2–14) | Li Q, Guan X, Wu P, et al. — "Early Transmission Dynamics in Wuhan, China, of Novel Coronavirus–Infected Pneumonia," *New England Journal of Medicine*, 382:1199-1207, independently confirmed via Muniz-Rodriguez K, et al. — ["Doubling Time of the COVID-19 Epidemic by Province, China"](https://pmc.ncbi.nlm.nih.gov/articles/PMC7392464), *Emerging Infectious Diseases* (CDC), which directly quotes this figure | published 2020-01-29 (Li et al.); citing article published 2020-08 | HIGH |
| S2 | Real public-health case investigations carry substantial, individually documented dollar costs (grounds Background's framing that timely detection has real financial stakes) | qualitative — two real investigations cost $49,769 and $18,423 respectively | Marx GE, Chase J, Jasperse J, et al. — ["Public Health Economic Burden Associated with Two Single Measles Case Investigations — Colorado, 2016–2017"](https://pmc.ncbi.nlm.nih.gov/articles/PMC5769785/), *MMWR* (CDC) | published 2017-11-24 | HIGH |
| S3 | Average operating cost of running a mobile health clinic | ~$275,000/year (≈ $753/day, derived) | Mobile Health Map — ["How Much Does It Cost To Run a Mobile Clinic?"](https://www.mobilehealthmap.org/how-much-it-costs-to-run-a-mobile-clinic/) | accessed 2026-09-18; no external publication date on the aggregating page | MEDIUM (the page's own aggregated registered-clinic data, no external primary source cited) |
| S4 | Average cost of an outpatient (ambulatory) visit for a respiratory illness (influenza) in the US | $312 per person | Statista — ["Influenza treatments costs per person by type of treatment U.S. 2016-2017"](https://www.statista.com/statistics/1111205/per-person-costs-of-treatment-for-influenza-in-the-us-by-treatment-type/) | survey period 2016-01-01 to 2017-12-31; accessed 2026-09-18 | MEDIUM (secondary aggregator, no primary underlying source named on the page) |

**Who these sources are:** the *New England Journal of Medicine* is a leading peer-reviewed
medical journal; *Emerging Infectious Diseases* is a peer-reviewed CDC journal that independently
confirms S1's exact figure while citing the original study. *MMWR* (Morbidity and Mortality Weekly
Report) is the CDC's own weekly epidemiological report. Mobile Health Map is a nonprofit research
initiative (Harvard-affiliated) that aggregates operating data from mobile clinics nationwide.
Statista is a data-aggregation platform; its influenza cost-per-visit figure is used here as
informing evidence for a *different*, fictional respiratory illness's per-case cost, not a direct
claim about this case's own disease. S1 is used directly in this case's arithmetic (MA2's growth
constant is derived from it); S2, S3, and S4 are supplemental or inform an assumption's chosen
value without being quoted as this case's own literal figure — S4's $312 is the one exception,
used directly as MA5's neighboring per-case cost input in Appendix D. See `RESEARCH_LOG.md` for
the full search trail, including what was searched and rejected.

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
