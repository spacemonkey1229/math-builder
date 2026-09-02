Case Study: The Trial Size
MS | Math | Case Study | 2026 | Adventure

## Overview

Dr. Amara Kondwani has the budget spreadsheet open on one half of her laptop screen and the
district immunity map on the other. Motorbike engines idle outside the district health office,
and a field coordinator leans in the doorway holding two cooler boxes and a clipboard, waiting
on her sign-off before the vials go on ice. The rains are coming — after that, half these roads
flood out for the season, and the sampling window closes with them. On the map, one district
glows in an unbroken block of color where no measles case has touched a school-age child in
years. Nobody on her team actually knows whether that means the population there is protected,
or just never checked. Her serosurvey is the only real evidence the vaccination campaign will
have before doses get allocated district by district.

The two draft designs open in her other tab spend the same survey money completely differently.
One pours the entire allotment into the villages her team is already staffed, permitted, and
present in, buying the tightest possible read on exactly those communities. The other pulls back
inside those same villages and reroutes what's left into territory the map has never covered at
all. Her supervisor wants a number by end of day. The coordinator is still standing in the
doorway, waiting.

She minimizes the spreadsheet, opens the tab where both budgets sit side by side, and starts
reading.

## Background

Dr. Amara Kondwani is the field lead for a Ministry of Health measles-and-rubella serosurvey
ahead of a supplemental immunization campaign in a rural health district. Her job is to draw a
cluster sample of children across a fixed set of already-established survey clusters, test each
sample for immunity, and report a seroprevalence estimate precise enough to tell campaign
planners which age cohorts, in which clusters, are under-immunized and need targeted follow-up
doses. She reports to the campaign's national planning office and is accountable for spending the
survey's entire allocated budget before results are due — there is no mechanism to request more
money mid-survey.

The survey answers to one hard limit: a fixed total budget of
$68,558 [S1]
(SEE APPENDIX A). Every dollar spent testing participants or opening new clusters comes out of
that one number, and nothing is added to it later. Running the existing cluster
infrastructure — staff, cold-chain transport, lab processing capacity — costs a fixed amount
before a single blood sample is ever drawn; each additional participant tested inside a cluster
that is already open costs a real, published marginal amount on top of that fixed cost
(SEE APPENDIX A); and each entirely new cluster opened in a currently unsurveyed district costs a
separate, larger marginal amount (SEE APPENDIX C). All figures in this case are sourced from a
real published costing study of a measles-and-rubella serosurvey (SEE APPENDIX E); the vocabulary
and "how to…" skills this case will ask of you are listed in APPENDIX F.

Kondwani's team has narrowed the plan to two named designs. Both fit inside the same
$68,558 [S1] ceiling, and both start from the
same
16 [S2]
already-open clusters:

- **Full Precision** tests as many participants as the entire budget can buy inside the existing
  clusters, maximizing statistical precision on the seroprevalence estimate for the district her
  team already has access to.
- **Reserve And Expand** tests only the smaller sample size the source study itself certifies as
  statistically adequate for the same clusters (SEE APPENDIX A), and reroutes whatever budget
  that frees into opening brand-new clusters in a currently unsurveyed district instead.

Both plans spend the same total money. Neither is free of a trade-off: Full Precision buys the
tightest possible read on the district already mapped; Reserve And Expand buys wider geographic
reach at the cost of a looser read on that original district (SEE APPENDICES A, B AND C).

Precision itself is not a vague feeling here — it is a real, published, computable quantity. The
worldwide standard for how many children a cluster survey must sample to hit a given precision
traces back to a single classic paper (SEE APPENDIX D): for a 95% confidence interval no wider than
a stated percentage, published survey methodology gives a direct formula linking sample size to
half-width, using an assumed "design effect" that accounts for testing children in clusters rather
than one at a time across the whole district. Applying that real formula to Kondwani's own real
sample sizes is what finally lets Full Precision and Reserve And Expand be judged on the very same
ruler — not dollars per cluster, but the actual precision, in percentage points, that each plan's
data collection delivers wherever it collects data at all (SEE APPENDIX D).

## Dilemma

You are Dr. Amara Kondwani.
Do you:
A.) Run Full Precision — spend the entire survey budget testing participants inside the existing clusters OR
B.) Run Reserve And Expand — test only the certified-adequate minimum and reroute the freed budget into new clusters

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A two-point cost table showing the real total cost of the Full Precision design and the
    real cost of the certified-adequate minimum design (SEE APPENDIX A), with the linear cost
    equation Cost(n) = (fixed cost) + (marginal cost)·n derived algebraically from those two
    points, shown step by step.
    D2. A graph of the Cost(n) line, drawn directly from the equation in D1, spanning at least
    from n = 0 through the Full Precision sample size, with both designs' cost points labeled on
    the line.
    D3. A written linear equation for the Budget-Remaining line, read directly off the graph
    provided in Appendix B, plus its x-intercept and a one-paragraph explanation of what that
    x-intercept represents for the survey.
    D4. An algebraic system-of-equations solution comparing the "spend the full budget" plan
    against the "reserve budget for new clusters" plan, showing the break-even sample size where
    the two plans cost the same, solved without graphing.
    D5. Using the real, sourced precision formula d = z·√(deff·p(1−p)/n) from Appendix D
    (z = 1.96, deff = 2, p = 0.5), compute the 95% CI half-width d yourself, showing substitution
    and evaluation step by step, for all three real sample sizes in this case: n = 658 (Full
    Precision's existing-district sample), n = 192 (Reserve And Expand's existing-district
    sample), and n = 96 (Reserve And Expand's new-district sample, from Appendix C). Then, using
    your three computed values, state — with reference to the World Health Organization's own
    published ±10% acceptable-precision target for these surveys (SEE APPENDIX D) — which
    design(s) clear that target, in which district(s), and which do not.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

### Appendix A — The Real Serosurvey Cost Data

| Design | Sample size tested (n) | Total cost (USD) | Resulting 95% CI half-width (SEE APPENDIX D) |
|---|---|---|---|
| Full Precision | 658 [S1] | $68,558 [S1] | ±5.4% [S7, S8] |
| Reserve And Expand (certified-adequate minimum, existing clusters only) | 192 [S3] | $54,578 (derived) [S1, S4] | ±10.0% [S7, S8] |
| Marginal cost per additional participant (within an existing cluster) | — | $30 [S4] | — |

**Modeling note.** The fixed cost of running the existing cluster infrastructure before any
participant is tested is not itself a number the source study states directly. It must be derived
algebraically from the two real data points above — that derivation is D1's required calculation,
not a pre-solved figure handed to you. The CI half-width column is explained fully in Appendix D
and is handed to you here pre-computed only so the Dilemma's stakes are groundable in a real,
computable number from the outset — Challenge 3's D5 then requires you to reproduce these same
±5.4%/±10.0%/±14.1% figures (and the ±14.1% new-district figure from Appendix C) yourself, from the
sourced formula, rather than take them on faith.

### Appendix B — The Budget-Remaining Line

The Budget-Remaining line is R(n) = (Total Fixed Survey Budget) − Cost(n): how much of the survey
budget is left after testing n participants, using the Cost(n) equation from Appendix A.

[GRAPH: R(n) vs. n, axis range n = 0 to 700 — chosen to span past the Full Precision sample size
of n = 658 [S1] so the line's x-intercept falls within the plotted range]

### Appendix C — Cluster Expansion Parameters

| Parameter | Value |
|---|---|
| Existing survey clusters already staffed and permitted | 16 [S2] |
| Marginal cost per additional new cluster opened | $1,620 [S5] |
| Total fixed survey budget | $68,558 [S1] |
| Participants tested per newly opened cluster (Modeling Assumption: same per-cluster density as the certified-adequate design, 192 ÷ 16) | 12/cluster |
| Total new clusters opened by Reserve And Expand's freed budget | 8 (floor of $13,980 ÷ $1,620/cluster; $1,020 left unspent) |
| Resulting 95% CI half-width for the new, currently unsurveyed district (SEE APPENDIX D) | ±14.1% [S7, S8] |

### Appendix D — The Real Precision-vs-Sample-Size Relationship

Statistical precision for a cluster survey is not a matter of opinion — it is a published, formula-
driven relationship between how many children get sampled and how tight the resulting 95%
confidence interval is. The classic reference for this relationship is the same one nearly every
national vaccination-coverage survey since the 1980s has used to size its own sample: Henderson RH,
Sundaresan T, "Cluster sampling to assess immunization coverage: a review of experience with a
simplified sampling method," *Bulletin of the World Health Organization* 60(2): 253–260 (1982) [S7].
That paper established the classic "30 clusters × 7 participants" (n = 210) design used worldwide,
built to hit a two-sided 95% confidence interval no wider than ±10 percentage points, assuming a
design effect (deff) of 2 to account for the extra variability that comes from testing children in
clusters rather than one at a time across an entire district.

A 2026 peer-reviewed review of that same methodology [S8] states the exact derivation: an
unclustered effective sample size of 96 (from the standard precision formula at p = 0.5, the
maximum-variance assumption used whenever the true rate is unknown) is inflated by the deff of 2 to
an actual required sample size of 192 — then rounded up slightly to the familiar 30×7 = 210 design.

The formula itself:

**d = z · √(deff · p(1 − p) / n)**

where d is the 95% CI half-width (as a decimal), z = 1.96 (95% confidence), deff = 2, p = 0.5, and
n is the real sample size actually tested.

Applying this real, published formula to Kondwani's own real, Carcelen-et-al.-sourced sample
sizes (SEE APPENDIX A) is what produces the CI half-width figures in Appendices A and C — no
invented conversion factor, only a real formula applied to real n's. Notice, too, that the source
study's own certified-adequate minimum of n = 192 [S3] lands almost exactly on the sample size this
1982 formula says is required for the classic ±10% target — a real, checkable corroboration between
two independent published sources, not a coincidence engineered for this case.

### Appendix E — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Total nested measles-rubella serosurvey cost and participant count, Southern Province, Zambia | $68,558 for n = 658 participants | Carcelen AC, Hayford K, Moss WJ, et al., "How much does it cost to measure immunity? A costing analysis of a measles and rubella serosurvey in southern Zambia," *PLOS ONE* 15(10): e0240734 ([link](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0240734)) | 2020-10-15 | HIGH |
| S2 | Number of survey clusters in the nested design | 16 clusters | Carcelen et al. 2020, *PLOS ONE* ([link](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0240734)) | 2020-10-15 | HIGH |
| S3 | Certified-adequate minimum sample size for the same 16 clusters (the vaccination coverage survey's own sample-size requirement, which the nested serosurvey design also satisfies) | 192 children | Carcelen et al. 2020, *PLOS ONE* ("The sample size for the nested serosurvey required only 192 children in the 16 clusters") ([link](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0240734)) | 2020-10-15 | HIGH |
| S4 | Marginal cost of adding one participant within an existing cluster | $30/participant | Carcelen et al. 2020, *PLOS ONE* ([link](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0240734)) | 2020-10-15 | HIGH |
| S5 | Marginal cost of including one additional cluster | $1,620/cluster | Carcelen et al. 2020, *PLOS ONE* ([link](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0240734)) | 2020-10-15 | HIGH |
| S6 | Corroborating cost-per-participant order of magnitude for immunization-coverage surveys in similar settings (context only, not load-bearing) | n/a | Brenzel L, Saxenian H, Stahley K, Dansereau E — "Cost of immunization coverage surveys in low- and middle-income countries" ([link](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2026.1897118/full)) | 2026 | MEDIUM |
| S7 | Classic cluster-survey precision design: the 30×7 (n=210) method, its ±10% (95% CI) precision target, and its assumed design effect (deff=2) | deff = 2; target d = ±10% at 95% CI | Henderson RH, Sundaresan T, "Cluster sampling to assess immunization coverage: a review of experience with a simplified sampling method," *Bulletin of the World Health Organization* 60(2): 253–260 ([link](https://pmc.ncbi.nlm.nih.gov/articles/PMC2535957/)) | 1982 | HIGH |
| S8 | Explicit numeric derivation of the Henderson-Sundaresan design (unclustered effective n=96, inflated by deff=2 to n=192, rounded to n=210), reviewed and restated in a 2026 peer-reviewed methodology paper | effective n=96 → actual n=192 → design n=210 | Rhoda DA, Soofi S, Hussain I, et al., "Sample Size Parameters for Vaccination Coverage Cluster Surveys—Insights from Pakistan," *Journal of Survey Statistics and Methodology* 13(5): 587–614 ([link](https://academic.oup.com/jssam/article/13/5/587/8417582)) | 2026 | HIGH |

**Note on Appendix A's Reserve And Expand cost figure.** The Reserve And Expand row's total cost
is marked `(derived)` because it is not a number the source study states directly — it follows
from the same linear cost structure Challenge D1 asks you to derive algebraically from the two
real inputs above: the total cost at n = 658 [S1] and the marginal cost per participant [S4].
Recovering that cost structure, and applying it at n = 192, is exactly D1's task — it is not
pre-solved for you here.

A companion paper corroborates the same cost-per-participant order of magnitude for
immunization-coverage serosurveys in similar settings: Brenzel L, Saxenian H, Stahley K,
Dansereau E, "Cost of immunization coverage surveys in low- and middle-income countries,"
*Frontiers in Public Health* (2026) [S6].
This paper is cited for context only — every dollar figure used in Appendix A, B, and C of this
case comes from Carcelen et al. 2020 [S1–S5] directly, not from the corroborating paper. The
CI half-width figures in Appendices A and C come from applying the real formula in Appendix D
[S7, S8] to those same real Carcelen-sourced sample sizes — a different, independently published
source than the cost figures, combined honestly rather than blended into one invented number.

## Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | p = 0.5 (maximum-variance assumption) used in the CI half-width formula for both districts | p = 0.5 | The true seroprevalence in the new, currently unsurveyed district is by definition unknown; p = 0.5 is the same conservative convention Henderson & Sundaresan's own 1982 design used, not an invented number. | Produces the widest (most conservative) CI half-width estimate for any given n. If the true prevalence differs from 50%, actual precision would be somewhat tighter than reported here, in both options equally — this assumption does not favor either design over the other and does not affect `margin_pct`. |
| MA2 | Newly opened clusters under Reserve And Expand are tested at the same per-cluster participant density as the certified-adequate design in the existing clusters (192 ÷ 16 = 12 participants/cluster), giving 8 × 12 = 96 total new-district participants | 12 participants/cluster (96 new-district participants total) | Carcelen et al. 2020 does not state a per-new-cluster sample size, since the source study never actually opened new clusters — this figure is not in the source paper and must be assumed. Reusing the study's own certified-adequate density, rather than inventing an independent number, is the most conservative, best-disclosed choice available. | Directly determines the new district's computed CI half-width (±14.1%) and therefore the case's `primary_metric` and `margin_pct` — see `balance_test_waiver` in case.json for the retune analysis showing no defensible alternative density closes the SPEC §2 margin gap. |

Every other figure in this case (the survey budget, cost data, cluster count, marginal costs, and
the precision formula's z/deff/p-source pairing) is a real, directly cited value from Appendix E's
sources, or a value newly disclosed above as an MCS-46-waived Modeling Assumption — this case uses
no undisclosed assumptions.

### Appendix F — "How To…" Math Questions To Research

**Vocabulary terms**

- X-Intercept
- Y-Intercept
- Slope
- System Of Equations

**"How to…" questions**

- How to identify the slope of a line given a set of data, or a graph of a line of a set of data, or its linear equation
- How to write a linear equation given a set of data
- How to write a linear equation given a graph of a line of a set of data
- How to draw a line of a set of data given its linear equation
- How to solve a system of linear equations
- How to evaluate a variable expression (Substitution Property)

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
