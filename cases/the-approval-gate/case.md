Case Study: The Approval Gate
MS | Math | Case Study | 2026 | Adventure

## Overview

Priya Nandakumar has two screens open and one Slack thread she keeps re-reading. On the left monitor: the configuration console for Foothill Outfitters' refund-handling agent, the automated system that decides — thousands of times a month — whether a customer's refund request gets approved on the spot or kicked to a human. On the right: a spreadsheet of every refund request the agent mishandled last quarter, sorted by dollar amount.

The Slack thread is from the VP of Customer Operations: *"Support queue is drowning in escalations. Legal signed off on a simpler rule — ship it before the board deck goes out."* Attached is a one-line rewrite of the agent's escalation logic, pitched as "the same policy, just cleaner." Priya has read it four times. Something about it doesn't sit right, but restating why requires more than a gut feeling — it requires actually building out every case the rule can hit and checking, row by row, whether the rewrite really does what the old rule did.

The office is quiet except for the low whir of a laptop fan working too hard and a half-eaten protein bar wedged against the keyboard. Two configuration files sit open side by side, one already staged for deployment. Priya's cursor hovers over the console's "Publish" button, one config away from changing how every refund request at Foothill Outfitters gets decided starting tomorrow morning.

One gate. One config. One number to defend when Legal asks why.

## Background

Priya Nandakumar is the AI Operations Lead at Foothill Outfitters, a mid-size online outdoor-apparel retailer. Priya owns the approval-gate logic inside the company's customer-service AI agent — the software, built on the same kind of agentic-workflow platform used across the retail and enterprise-software industry (real, named systems in this category include Salesforce Agentforce, ServiceNow AI Agents, and Microsoft Copilot Studio's multistage approval flows), that decides in real time whether an incoming refund request is auto-approved or escalated to a human reviewer (SEE APPENDIX A).

The agent's decision is built from three yes/no conditions checked on every refund request, defined precisely in (SEE APPENDIX A): whether the requested amount is under a set dollar threshold, whether the requesting customer's account tenure is over a set length of time, and whether the request is a repeat request from the same customer within a recent window. Compliance's original rule — never disputed, and not up for debate in this case — auto-approves a request only when all three safety conditions hold at once. The disagreement is entirely about how to correctly write down every other case: the two designs on the table encode that "everything else" condition differently (SEE APPENDIX B), and the two designs do not send the same requests to the same place.

Both designs must operate inside the same fixed monthly volume of refund requests the agent actually sees, broken down by which of the three conditions each request satisfies (SEE APPENDIX C). Every escalation costs the company a human reviewer's time; every request auto-approved that should not have been carries a real, documented risk of loss (SEE APPENDIX D). Priya has to pick one design, defend the total cost math behind it, and publish the config before the day is out.

The two options are named on Priya's whiteboard: **The Compound Gate**, which escalates a request whenever any one of the three safety conditions fails, or **The Streamlined Gate** — the VP's proposed rewrite — which escalates a request only when all three unsafe conditions hold at once. The vocabulary and "how to…" procedures needed to build and compare these designs are listed in (SEE APPENDIX E), and every sourced or assumed figure in this case is documented in (SEE APPENDIX F).

## Dilemma

You are Priya Nandakumar.
Do you:
A.) Ship The Compound Gate — escalate whenever any one of the three safety conditions fails OR
B.) Ship The Streamlined Gate — escalate only when all three unsafe conditions hold at once, the VP's proposed rewrite

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A complete truth table for Option A's escalation rule and a complete truth table for
    Option B's escalation rule, each showing all eight true/false combinations of the three
    conditions defined in Appendix A — p (amount under threshold), q (tenure over threshold),
    and r (repeat request) — with a final column giving each rule's Approve/Escalate output for
    every row.
    D2. A formal conditional ("if…then") statement of Compliance's shared approval rule ("if a
    request is auto-approved, then…"), plus its converse, inverse, and contrapositive, each
    written out in full and each given a one-sentence plain-English interpretation of what it
    would mean operationally for Foothill Outfitters.
    D3. A symbolic De Morgan's-Laws derivation of the true logical negation of the shared
    approval condition (p ∧ q ∧ ¬r), shown step by step, with a written verdict — citing the
    specific mismatched row or rows from your Challenge 3 (D1) truth tables — on whether Option
    B's escalation rule is or is not logically equivalent to Option A's.
    D4. A monthly-volume table applying Appendix C's request-category counts to each design's
    truth table (D1) to compute how many requests each design auto-approves versus escalates,
    followed by a total-expected-monthly-cost calculation for each design — escalation cost plus
    expected false-approval loss cost, using Appendix D's figures — shown step by step for both
    options.
    D5. A one-paragraph written recommendation, using correct logical notation (∧, ∨, ¬, →)
    throughout, that names which gate design has the lower total expected monthly cost and
    explicitly addresses why assuming Option B was "the same rule written differently," without
    building the truth table to check, would have been misleading.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — The Approval Gate: Conditions and Thresholds

Referenced in Background and Challenge 3 (D1, D2, D3). Every refund request the agent sees is
checked against exactly three conditions.

| Condition | Definition | Threshold used in this case |
|---|---|---|
| p | The requested refund amount is under Foothill Outfitters' auto-approval dollar threshold | Under $60 (MA2) |
| q | The requesting customer's account tenure is over Foothill Outfitters' trust threshold | Over 1 year (MA2) |
| r | This is a repeat refund request from the same customer within the lookback window | 2nd or more refund request within a trailing 90-day window (MA2) |

**Compliance's rule, not in dispute:** auto-approve a request only when p ∧ q ∧ ¬r — the amount
is under threshold, the customer is trusted, and this is not a repeat request. What every other
combination of p, q, and r should do — the "everything else" case — is exactly what Options A and
B (SEE APPENDIX B) disagree about.

## Appendix B — Two Proposed Gate Logic Designs

Referenced in Background and Dilemma. Both designs share Appendix A's three conditions and
Compliance's shared approve rule (p ∧ q ∧ ¬r). They differ only in how "everything else" is
written down as an escalation rule.

| Design | Escalation rule (Escalate when TRUE) | Proposed by |
|---|---|---|
| Option A — The Compound Gate | ¬p ∨ ¬q ∨ r | Priya's own design, applying De Morgan's Laws directly to the negation of Compliance's approve rule |
| Option B — The Streamlined Gate | ¬p ∧ ¬q ∧ r | The VP of Customer Operations, pitched as "the same policy, just cleaner" |

Real agentic-workflow platforms structure exactly this kind of automated gate as a set of
explicit, human-authored logical conditions rather than a black-box judgment call — for example,
Microsoft's own Copilot Studio documentation for its multistage approval feature instructs
builders to write approval logic as an explicit list of conditions joined by AND/OR, worded as
"Reject … if ANY of the following conditions are true" (SEE APPENDIX F, [S1]) — the same
disjunction-of-failure-conditions structure Option A's escalation rule uses. Salesforce's own
architecture guidance for agentic workflows likewise states that "agentic workflows operating at
high density should incorporate explicit human approval or escalation gates for actions with
irreversible consequences, such as financial transactions" (SEE APPENDIX F, [S3]), consistent with
Foothill Outfitters treating an automated refund decision as exactly this kind of gated action.

## Appendix C — Monthly Refund Request Volume by Category

Referenced in Background and Challenge 3 (D4). Foothill Outfitters' refund-handling agent logs
every request it receives against the three conditions in Appendix A. One month's request volume,
broken into all eight possible true/false combinations of p, q, and r:

| p (amount under threshold) | q (tenure over threshold) | r (repeat request) | Requests this month |
|---|---|---|---|
| T | T | T | 40 (MA1) |
| T | T | F | 2,000 (MA1) |
| T | F | T | 30 (MA1) |
| T | F | F | 430 (MA1) |
| F | T | T | 25 (MA1) |
| F | T | F | 850 (MA1) |
| F | F | T | 15 (MA1) |
| F | F | F | 210 (MA1) |
| **Total** | | | **3,600 (MA1)** |

**RESEARCH FLAG RESOLVED:** no public company publishes the exact monthly volume or condition
breakdown of its own refund-handling agent — this is proprietary, day-to-day operational data
specific to one company's customer-service pipeline, and it does not exist anywhere as a citable
external dataset. Every count above is a stated, disclosed **Modeling Assumption (MA1)** — see the
Modeling Assumptions section below.

## Appendix D — Cost Inputs

Referenced in Background and Challenge 3 (D4).

| Item | Value |
|---|---|
| Cost per escalated review (a human reviewer's time to manually decide one refund request) | $9.00 (MA3) |
| Rate at which an undetected, incorrectly auto-approved risky refund request turns out to be fraudulent or otherwise a real loss | 15.14% [S2] |
| Average dollar value at risk per incorrectly auto-approved, risky refund request | $66.00 (MA4) |

**What "expected false-approval loss cost" means here:** not every risky refund request that gets
auto-approved by mistake turns out to be a real loss — most are perfectly legitimate customers who
simply didn't meet one threshold. Multiplying the return-fraud rate by the average dollar value at
risk turns "how many risky requests got waved through" into a real dollar figure for the *expected*
loss, the same way an insurer prices a policy without knowing which individual claim will occur.

## Modeling Assumptions

> These figures are **not sourced from an external publisher**. They are stated scenario
> assumptions chosen by the case author because Foothill Outfitters' own request volume, condition
> breakdown, and gate thresholds are internal operational data no public company publishes. A Hero
> may challenge these numbers in discussion — that is a legitimate move, and the sensitivity
> column shows exactly where the challenge would matter.
>
> The Basis columns below cite real research from Microsoft (a company that makes enterprise
> workflow and AI-agent software), and Appriss Retail with Deloitte (organizations that publish
> annual retail-returns-fraud research) — see Appendix F for what each organization is and how
> each figure is used.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Monthly refund request volume, by all eight p/q/r categories | See Appendix C for the full 8-row breakdown; total 3,600 per month | No source publishes any specific company's internal AI-agent request logs, broken down by condition. Chosen to reflect a realistic pattern for a mid-size retailer: the large majority of requests are fully safe (all three conditions favorable), with smaller counts spread across the seven riskier categories, and the rarest category being requests that fail every condition at once. | Several of these category counts are load-bearing — a defensible challenge to the largest "safe" bucket or to any risky-category count could change the total cost gap between the two designs. Work the comparison yourself with a different plausible set of counts rather than taking Appendix C's numbers as unchallengeable fact. |
| MA2 | Dollar amount threshold, tenure threshold, and repeat-request definition (Appendix A) | See Appendix A | These are Foothill Outfitters' own internal policy thresholds — no public source publishes the exact dollar figure, tenure length, or lookback window any specific company sets for its own auto-approval gate, though Microsoft's own Copilot Studio documentation confirms that real platforms structure approval logic around exactly this kind of explicit numeric threshold and condition set [S1]. | Changing any one threshold reshuffles which requests fall into which of Appendix C's eight categories, which could change the total-cost comparison. This case holds the thresholds fixed and varies only the category counts and cost inputs when testing sensitivity. |
| MA3 | Cost per escalated review | $9.00 | No single published source states the exact dollar cost of one manually reviewed refund request. Informed by real, cited ecommerce/retail customer-service cost-per-contact research (SEE APPENDIX F, [S4]) spanning roughly $2.70–$15.56 per contact depending on channel and company size — including a Gartner-cited $13.50 average for "assisted" (human-handled) contacts generally and $6–$12 for smaller ecommerce/retail stores specifically; set toward the middle-upper part of the smaller-retailer range, since a refund review requires pulling order and customer history rather than answering a simple question. | This figure scales Option A's entire cost total directly (Option A escalates far more requests than Option B) — a Hero who challenges it should redo Challenge 3 (D4) with a different value before assuming the recommendation is unaffected. |
| MA4 | Average dollar value at risk per incorrectly auto-approved, risky refund request | $66.00 | No source publishes Foothill Outfitters' own average refund amount. Set as a company-specific figure near Appendix A's own $60 dollar threshold, since risky requests cluster close to (and sometimes just past) the auto-approval line. | This figure, multiplied by the sourced fraud rate [S2], sets the per-incident loss size used in Challenge 3 (D4) — a Hero who challenges it changes Option B's expected loss cost directly, and it is the single most sensitive dial in this case. |

## Appendix E — "How To…" Math Questions To Research

**Vocabulary terms**

- Logical Statement
- Conjunction
- Disjunction
- Negation
- Conditional Statement
- Truth Table

**"How to…" questions**

- How to construct a truth table for a compound statement
- How to determine the converse, inverse, and contrapositive of a conditional statement

## Appendix F — Sources

All sourced (non-assumption) figures in this case are cited here.

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Real enterprise agentic-workflow platforms structure automated approval/escalation logic as explicit numeric-threshold conditions joined by AND/OR ("Reject … if ANY of the following conditions are true") | qualitative — grounds Appendix A/B's structure, not a dollar figure | Microsoft Learn — [Multistage and AI approvals in agent flows, Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-advanced-approvals) | dated 2025-09-04, updated 2026-06-30 | HIGH |
| S2 | Percentage of all retail merchandise returns that were fraudulent, industry-wide, 2024 | 15.14% | Appriss Retail (with Deloitte) — [Appriss Retail Annual Research: Fraudulent Returns and Claims Cost Retailers $103B in 2024](https://apprissretail.com/news/appriss-retail-annual-research-fraudulent-returns-and-claims-cost-retailers-103b-in-2024/) | published 2024-12-30 | HIGH |
| S3 | Guidance that agentic workflows should incorporate explicit human approval/escalation gates for actions with irreversible consequences, such as financial transactions | qualitative — grounds Background's framing that a refund decision is exactly this kind of gated action | Salesforce Architects — [Determining Agentic and Traditional Workflow Automation](https://architect.salesforce.com/docs/architect/decision-guides/guide/determining-agentic-vs-traditional-workflow-automation) | no publication date shown on page | MEDIUM (supplemental — real, primary-publisher guidance, but undated) |
| S4 | Average dollar cost of a human-handled ("assisted") customer-service contact, and ecommerce/retail-specific cost-per-contact ranges by store size | Cross-industry assisted-channel average ~$13.50 (Gartner-cited); ecommerce ticket range ~$2.70–$5.60 (Opensend-cited); small ecommerce/retail stores ~$6–$12 per contact (Ringly.io's own benchmark assessment, informed by Gorgias ticket-volume data, not a figure directly attributed to Gorgias) | Ringly.io — [Ecommerce Customer Service Cost Per Contact: 2026 Benchmarks](https://www.ringly.io/blog/ecommerce-customer-service-cost-per-contact) | accessed 2026-09-09, no single publication date on the aggregating page | MEDIUM (supplemental — a secondary page aggregating several named third-party studies/vendors; no figure is quoted directly as this case's value, only used to bound MA3's chosen range) |

**Who these sources are:** Microsoft and Salesforce are both companies that make enterprise
workflow and AI-agent software — the kind of platform Foothill Outfitters' refund-handling agent
is built on. Appriss Retail is a retail-analytics firm that, together with the accounting and
consulting firm Deloitte, publishes an annual industry-wide study of retail returns. Ringly.io is
a customer-support software vendor whose blog aggregates cost-per-contact figures from several
named third-party research firms and its own benchmark assessment (Gartner, Opensend, and Gorgias-informed ticket-volume data). S1 and S2 are used directly in this
case's arithmetic and structure; S3 and S4 are supplemental — they inform Appendix A's realism and
Modeling Assumption MA3's chosen range without being quoted as a direct value themselves. See
`RESEARCH_LOG.md` for the full search trail, including what was searched and rejected for the
request-volume, threshold, and cost figures now recorded as Modeling Assumptions MA1–MA4 above.

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
