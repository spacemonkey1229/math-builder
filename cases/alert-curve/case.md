# Case Study: The Alert Curve

MS | Math | Case Study | 2026-27 | Heroes Academy

---

## Overview

The dashboard's third monitor throws blue light across Jordan Lee's face, and the coffee next to
his keyboard went cold an hour ago. It's the dead middle of the overnight shift, the SOC bullpen
empty except for the hum of the server room through the wall, and the alert queue just kicked out
a spike he can't ignore. Somewhere in the network, traffic to one edge node has been climbing for
the last several minutes, and the automated dashboard just painted the tile red.

Jordan's cursor hovers over two things at once: the escalation button that would put the on-call
incident commander's phone buzzing on a nightstand three time zones away, and a second browser
tab, still loading, where the SOC's own analytics console can plot the actual rate of change of
that alert curve — traffic volume and threat score multiplied together, a real live function he
could differentiate right now if he waits one more sampling interval for the data to fill in.

He's been burned both ways before. The senior analyst who paged the incident commander over a
traffic spike that turned out to be nothing. The other one — quieter, worse — who waited to be
sure, and by the time anyone woke up, the real thing had already been running loose for longer
than anyone wanted to admit.

The red tile blinks. Jordan's hand is still on the mouse, hovering between the two tabs, deciding
which one to click first.

---

## Background

Jordan Lee is a Tier-2 Security Operations Center (SOC) analyst on the overnight shift at a
financial-services company, responsible for triaging automated alerts before any human above him
gets paged. Escalating incorrectly costs him credibility with the rest of the SOC team; missing
or delaying a real escalation risks a live compromise inside a network that moves other people's
money (SEE APPENDIX C).

The SOC's monitoring platform tracks, for the edge node in question, two live quantities every
sampling interval: traffic volume — the raw rate of incoming requests — and a threat score
computed by the platform's detection engine from pattern-matching against known attack
signatures. Together they define a composite alert-rate function: the number of automated alerts
the system is generating per minute, equal to traffic volume multiplied by threat score at every
instant (SEE APPENDIX A). Jordan has two ways to decide whether tonight's spike is real:

**Option A — The Threshold Trip.** The platform already has a built-in rule: if the raw alert
count in the current hour crosses a fixed threshold, escalate immediately, no further analysis
required (SEE APPENDIX C).

**Option B — The Curve Check.** Wait one more sampling interval, then use the composite
alert-rate function's actual instantaneous rate of change — its derivative at this moment — to
confirm the alert rate is truly accelerating, not just elevated by a volume spike that never
touches the threat-scoring engine (SEE APPENDIX A).

Both options work from the same underlying data; neither requires new instrumentation. What
differs is timing and false-positive risk. The Threshold Trip escalates the instant the raw count
crosses the line, whether the driver is a genuine coordinated attack or an ordinary traffic surge
— a batch job, a marketing push, a monitoring tool's own polling — that happens to push the count
over without the threat score ever moving. The Curve Check waits exactly one sampling interval
(SEE APPENDIX C) before it can even evaluate a derivative, and during that wait a genuine
accelerating attack keeps running, uninterrupted, for that same extra interval. Every escalation
decision the SOC makes over a stretch of past shifts is logged, along with whether it was later
confirmed a real incident (SEE APPENDIX D) — that log is what will ultimately show which policy
actually protects the SOC's credibility and the company's exposure at once.

All figures in this case are sourced in Appendix F, or stated as explicit modeling assumptions in
Appendix E where no public figure exists. The vocabulary and the "how to…" skills this case will
ask of you are listed in Appendix G — that is where Challenge 1 sends you.

---

## Dilemma

You are Jordan Lee.

Do you:

A.) Escalate now under the Threshold Trip — the raw alert count this hour has already crossed the
threshold OR

B.) Hold for the Curve Check — wait one more sampling interval and confirm the alert rate is truly
accelerating before escalating

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A full symbolic derivation of dS/dt — the threat score's rate of change — using the chain
    rule, with the composite's outer function and inner function explicitly identified
    (Appendix A).
    D2. A full symbolic derivation of dA/dt — the alert rate's rate of change — using the product
    rule on A(t) = V(t) · S(t), substituting D1's chain-rule result for dS/dt (Appendix A).
    D3. A written justification, using the definition of differentiable, of why the SOC's raw
    minute-by-minute alert count cannot supply a true instantaneous rate of change, and why the
    continuous composite model A(t) can (Appendix B).
    D4. The equation of the tangent line to A(t) at the current sampling instant t0, using D2's
    dA/dt as its slope, and what that tangent line predicts for A at the next sampling instant
    (Appendix C).
    D5. A confirmed-incidents-per-false-escalation ratio for the Threshold Trip policy and for the
    Curve Check policy, computed from Appendix D's historical log by classifying each past
    interval under both policies' rules — Appendix C's threshold for Threshold Trip, the sign of
    the D4-style tangent-line slope at confirmation for Curve Check — with the percentage margin
    between the two ratios and a recommendation.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

## Appendix A — The Composite Alert-Rate Model

Let *t* be the number of minutes elapsed since the start of the current one-hour monitoring
window, with *t*₀ the instant Jordan is deciding, "now."

**Traffic volume** — the raw rate of incoming requests to the edge node, in requests per minute —
is modeled as a smooth function of time:

```
V(t) = p·t² + q·t + r
```

**Threat score** is not measured directly; it is *computed* by the detection engine in two steps,
which is exactly why it is a composite function. First, the engine tallies a raw pattern-match
count against known attack signatures, rising over time:

```
g(t) = k·t + m          (inner function — raw pattern-match count)
```

Second, the engine runs that raw count through a diminishing-returns scoring transform to produce
the threat score itself:

```
f(x) = c·√x             (outer function — the scoring transform)
S(t) = f(g(t)) = c·√(k·t + m)
```

**The composite alert-rate function**, the number this case is actually about, is the product of
the two:

```
A(t) = V(t) · S(t)
```

Differentiating A(t) requires the **product rule** (A is a product of V and S), and inside that,
differentiating S(t) requires the **chain rule** (S is a composition of f and g) — this single
function is deliberately built to force both.

| Coefficient | Meaning | Value |
|---|---|---|
| p, q, r | Traffic-volume model coefficients | p = 0.4, q = 15, r = 800 (requests/min) — **Modeling Assumption MA1** (SEE APPENDIX E) |
| k, m | Inner function coefficients (pattern-match count accumulation rate and starting count) | k = 3, m = 20 — **Modeling Assumption MA2** (SEE APPENDIX E) |
| c | Outer function scaling coefficient (scoring transform) | c = 6 — **Modeling Assumption MA3** (SEE APPENDIX E) |

Referenced from Background and Challenges D1, D2, D3, D4, D5.

---

## Appendix B — Why the Raw Count Isn't Differentiable

The SOC's dashboard displays the raw alert count as a running tally, incremented by whole numbers
only at the instant each individual alert fires — a step function in time, not a smooth curve. A
step function has no defined instantaneous rate of change at the instant it jumps: no tangent
line exists there, because the function is not differentiable at that point.

The composite alert-rate function A(t) built from the platform's underlying continuous telemetry
(Appendix A) is a different object. Because V(t) and S(t) are each differentiable at every *t*,
and because a product and a composition of functions that are differentiable everywhere is itself
differentiable everywhere both pieces are, A(t) is differentiable across the whole sampling
window. That gap — a step function with no instantaneous rate of change anywhere, versus a
continuous model that has one everywhere — is exactly what the Curve Check policy exploits and
the Threshold Trip policy cannot: only a differentiable function has an instantaneous rate of
change to compute in the first place.

Referenced from Background and Challenge D3.

---

## Appendix C — Escalation Policy Parameters

| Quantity | Value |
|---|---|
| Threshold, raw alerts/hour that triggers the Threshold Trip | 500 alerts/hour — **Modeling Assumption MA4** (SEE APPENDIX E) |
| Sampling interval length, minutes (the wait required by the Curve Check) | 5 minutes [S1] |
| Current sampling instant t₀, minutes into the monitoring window | 42 minutes — **Modeling Assumption MA5** (SEE APPENDIX E) |
| Mean time to detect (MTTD) a real security incident, industry benchmark | 247 days (mean time to identify **and** contain, global average) [S2] |

The MTTD figure anchors why the extra sampling interval the Curve Check spends confirming is a
real, non-trivial cost against real industry detection timelines, not a free wait.

Referenced from Background and Challenge D4.

---

## Appendix D — Historical Escalation Outcome Log

A log of past shifts' escalation decisions, used to compute Challenge D5's confirmed-incidents-
per-false-escalation ratio for each policy. "Crossed threshold?" applies the Threshold Trip's
rule from Appendix C; "sign of dA/dt at confirmation" applies the Curve Check's rule from
Appendix A, evaluated one sampling interval after the alert first appeared. The log spans just
over two full overnight shifts rather than one, so the ratio each policy is graded on rests on
more than a handful of intervals.

| Past interval | Raw alert count this hour | Crossed threshold? | Sign of dA/dt at confirmation | Later confirmed a real incident? |
|---|---|---|---|---|
| 1 | 610 | Yes | + | Yes |
| 2 | 635 | Yes | + | Yes |
| 3 | 730 | Yes | + | Yes |
| 4 | 515 | Yes | − | No |
| 5 | 410 | No | + | Yes |
| 6 | 555 | Yes | + | No |
| 7 | 675 | Yes | + | Yes |
| 8 | 695 | Yes | + | Yes |
| 9 | 545 | Yes | − | No |
| 10 | 715 | Yes | + | Yes |
| 11 | 585 | Yes | + | No |
| 12 | 425 | No | + | No |
| 13 | 655 | Yes | + | Yes |
| 14 | 460 | No | + | No |

This full table is **Modeling Assumption MA6** (SEE APPENDIX E) — a constructed illustrative log,
not a real SOC's internal data. Its *scale* (how often a threshold-crossing alert turns out to be
a false positive, and how often a real incident's rate of change stays under a raw-count
threshold) is anchored to published SOC-industry alert-quality benchmarks — a 2026 Microsoft/Omdia
survey finding 46% of SOC alerts prove to be false positives, and a 2026 Ponemon Institute survey
finding the average organization's alert queue is overwhelming enough that analysts investigate
only 37% of what arrives — not to any single named institution's real internal data (SEE APPENDIX
F, [S3], [S4]).

Referenced from Challenge D5.

---

## Appendix E — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, because no public SOC or SIEM vendor publishes the internal scoring-engine coefficients,
> escalation-threshold defaults, or per-shift alert logs of a real detection platform — that data
> is proprietary to each vendor and each SOC. A Hero may challenge them in discussion — that is a
> legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Traffic-volume model coefficients p, q, r | p = 0.4, q = 15, r = 800 (requests/min) | No public source publishes a real edge node's requests-per-minute curve. The scale (hundreds to low thousands of requests/min, mildly accelerating) is chosen to sit above the escalation threshold (MA4) by the current sampling instant, consistent with a genuinely climbing traffic pattern. | High — a smaller p (flatter climb) can make V(t) never drive A(t) into a threshold-crossing regime at all, changing whether the scenario's "spike" is real. |
| MA2 | Inner-function coefficients k, m (pattern-match accumulation) | k = 3, m = 20 | No detection-engine vendor publishes its raw pattern-match accumulation rate. Chosen so g(t) stays positive and growing across the full 60-minute window, which S(t) = c·√(g(t)) requires. | Medium — affects the magnitude of dS/dt and therefore dA/dt (D1, D2), but a proportional rescaling of k does not by itself flip the sign of dA/dt at t0. |
| MA3 | Outer-function scaling coefficient c | c = 6 | No detection-engine vendor documents its scoring-transform scale. Chosen so S(t) lands in a 0–100-style threat-score range at realistic pattern-match counts, matching how commercial detection engines commonly present a bounded severity score. | Medium — rescales S(t) and A(t) uniformly; does not change the sign of dA/dt, but changes the numeric value D4's tangent line predicts. |
| MA4 | Threshold Trip's raw-alert threshold | 500 alerts/hour | No SIEM/SOAR vendor publishes a universal default "alerts per hour" escalation threshold — Microsoft Sentinel's own alert-threshold setting [S1] is explicitly configured per rule, not fixed. 500/hour is chosen to sit inside the range of the Appendix D log's raw counts (410–730), so some past intervals cross it and some do not, as a real threshold would. | High — this is the single most flip-capable figure in the case. Raising it above 730 means the Threshold Trip never escalates in Appendix D's log at all; lowering it below 410 means it always does. Either extreme collapses the D5 comparison. |
| MA5 | Current sampling instant t₀ | 42 minutes into the 60-minute window | Narrative anchor only — Jordan's decision has to happen at *some* point in the hour, with enough of the window left (18 minutes, more than 3 sampling intervals at 5 minutes each) that "wait one more interval" is a live option. No public source could ever supply this — it is authored, not measured. | Low — changes the numeric value of D4's tangent-line prediction, but does not change which policy the D5 ratio favors. |
| MA6 | Appendix D's 14-row historical escalation log (all four columns) | See Appendix D table | Constructed to illustrate a realistic mix of true positives, false escalations, and a missed-by-raw-count/caught-by-derivative case, spanning slightly more than two shifts so the D5 ratio rests on more than a handful of intervals, at a false-positive rate in the neighborhood of the published SOC-industry benchmarks [S3] [S4] (roughly 2 in 5 alerts being false positives, and well under half of all alerts being fully investigated). No real institution's internal log is used or implied. | High — this table is what D5's ratio and its percentage margin are computed from directly. A different constructed log could shift, or even reverse, which policy the ratio favors. |

Referenced from Appendix A, Appendix C, Appendix D, and Challenges D1–D5.

---

## Appendix F — Sources

| id | Claim | Value | Source | Accessed | Confidence |
|---|---|---|---|---|---|
| S1 | Minimum configurable run-query interval for a scheduled analytics rule (a real SIEM/SOAR platform's fastest supported polling cadence) | 5 minutes | Microsoft — [Scheduled analytics rules in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/scheduled-rules-overview) | 2026-08-27 | HIGH |
| S2 | Mean time to identify and contain a data breach, global average | 247 days | IBM, *Cost of a Data Breach Report 2026*, as reported in [Help Net Security — "Data breach cost 2026 averaged $4.99 million, AI attacks ran higher"](https://www.helpnetsecurity.com/2026/07/30/ibm-cost-of-a-data-breach-2026/) | 2026-08-27 | MEDIUM |
| S3 | Share of SOC security alerts that prove to be false positives, and share left uninvestigated | 46% false positives; 42% uninvestigated | Omdia (commissioned by Microsoft, N=300 SOC practitioners, fielded Jun–Jul 2025), reported in Microsoft — [Unify now or pay later: New research exposes the operational cost of a fragmented SOC](https://www.microsoft.com/en-us/security/blog/2026/02/17/unify-now-or-pay-later-new-research-exposes-the-operational-cost-of-a-fragmented-soc/) | 2026-08-27 | MEDIUM |
| S4 | Average daily security-alert volume per organization, and share of alerts actually investigated | 4,330 alerts/day; 37% investigated | Ponemon Institute (commissioned by Crogl), *2026 State of SecOps Report*, as reported on [Crogl's newsroom summary](https://www.crogl.com/newsroom/state-of-secops-ai) | 2026-08-27 | MEDIUM |

**Rejected anchor.** Appendix D's original draft note (see case-write's stub) proposed anchoring
the historical log's scale to "the Verizon DBIR's reporting on the share of security alerts that
convert to confirmed incidents." A genuine search — two distinct framings plus a direct check of
Verizon's own DBIR pages — found no such alert-to-incident conversion statistic published in the
Verizon DBIR; the DBIR reports on confirmed breaches and incidents, not on raw alert-triage
outcomes. S3 and S4 above (Microsoft/Omdia and Ponemon SOC-alert-quality research) measure the
same underlying phenomenon — how often an alert is noise versus signal — and are used in its
place. See `RESEARCH_LOG.md` for the full search trail.

Referenced from Background, Appendix A, Appendix C, Appendix D, Appendix E.

---

## Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Tangent Line
- Differentiable

**"How to…" questions**

- How to use the chain rule to differentiate a composite function
- How to use the product rule to differentiate a product of functions
