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

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->

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
| p, q, r | Traffic-volume model coefficients | {{NEEDS_SOURCE: realistic coefficients (or calibration scale) for a quadratic requests-per-minute traffic model at a financial-services SOC edge node, anchored to Verizon Data Breach Investigations Report (DBIR) alert/traffic-volume statistics, most recent edition}} |
| k, m | Inner function coefficients (pattern-match count accumulation rate and starting count) | {{NEEDS_SOURCE: realistic rate of accumulation and starting value for a detection engine's raw pattern-match count over a sampling window, anchored to a published SOC/SIEM alert-volume benchmark}} |
| c | Outer function scaling coefficient (scoring transform) | {{NEEDS_SOURCE: realistic scaling coefficient for a square-root-shaped threat-scoring transform, anchored to published detection-engine scoring documentation or a comparable benchmark}} |

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
| Threshold, raw alerts/hour that triggers the Threshold Trip | {{NEEDS_SOURCE: automated-escalation threshold, raw alerts per hour, financial-services SOC, industry-typical SIEM/SOAR platform default or published benchmark}} |
| Sampling interval length, minutes (the wait required by the Curve Check) | {{NEEDS_SOURCE: SOC alert-platform sampling interval length, minutes, industry-typical SIEM/SOAR platform configuration}} |
| Current sampling instant t₀, minutes into the monitoring window | {{NEEDS_SOURCE: elapsed minutes into the current one-hour monitoring window at the moment Jordan is deciding, scenario value}} |
| Mean time to detect (MTTD) a real security incident, industry benchmark | {{NEEDS_SOURCE: mean time to detect a security incident, IBM Cost of a Data Breach Report, most recent edition}} |

The MTTD figure anchors why the extra sampling interval the Curve Check spends confirming is a
real, non-trivial cost against real industry detection timelines, not a free wait.

Referenced from Background and Challenge D4.

---

## Appendix D — Historical Escalation Outcome Log

A log of past shifts' escalation decisions, used to compute Challenge D5's confirmed-incidents-
per-false-escalation ratio for each policy. "Crossed threshold?" applies the Threshold Trip's
rule from Appendix C; "sign of dA/dt at confirmation" applies the Curve Check's rule from
Appendix A, evaluated one sampling interval after the alert first appeared.

| Past interval | Raw alert count this hour | Crossed threshold? | Sign of dA/dt at confirmation | Later confirmed a real incident? |
|---|---|---|---|---|
| 1 | {{NEEDS_SOURCE: raw alert count, past shift interval 1, this SOC's alert log or a comparable published SOC benchmark dataset}} | {{NEEDS_SOURCE: threshold-crossed status, interval 1}} | {{NEEDS_SOURCE: sign of dA/dt at confirmation, interval 1}} | {{NEEDS_SOURCE: confirmed-incident outcome, interval 1}} |
| 2 | {{NEEDS_SOURCE: raw alert count, interval 2}} | {{NEEDS_SOURCE: threshold-crossed status, interval 2}} | {{NEEDS_SOURCE: sign of dA/dt at confirmation, interval 2}} | {{NEEDS_SOURCE: confirmed-incident outcome, interval 2}} |
| 3 | {{NEEDS_SOURCE: raw alert count, interval 3}} | {{NEEDS_SOURCE: threshold-crossed status, interval 3}} | {{NEEDS_SOURCE: sign of dA/dt at confirmation, interval 3}} | {{NEEDS_SOURCE: confirmed-incident outcome, interval 3}} |
| 4 | {{NEEDS_SOURCE: raw alert count, interval 4}} | {{NEEDS_SOURCE: threshold-crossed status, interval 4}} | {{NEEDS_SOURCE: sign of dA/dt at confirmation, interval 4}} | {{NEEDS_SOURCE: confirmed-incident outcome, interval 4}} |
| 5 | {{NEEDS_SOURCE: raw alert count, interval 5}} | {{NEEDS_SOURCE: threshold-crossed status, interval 5}} | {{NEEDS_SOURCE: sign of dA/dt at confirmation, interval 5}} | {{NEEDS_SOURCE: confirmed-incident outcome, interval 5}} |
| 6 | {{NEEDS_SOURCE: raw alert count, interval 6}} | {{NEEDS_SOURCE: threshold-crossed status, interval 6}} | {{NEEDS_SOURCE: sign of dA/dt at confirmation, interval 6}} | {{NEEDS_SOURCE: confirmed-incident outcome, interval 6}} |

This log's scale is anchored to published SOC-industry alert-to-incident conversion statistics
(e.g. the Verizon DBIR's reporting on the share of security alerts that convert to confirmed
incidents), not to any single named institution's real internal data (SEE APPENDIX F).

Referenced from Challenge D5.

---

## Appendix E — Modeling Assumptions

> No modeling assumptions are recorded yet. This case leaves every figure in Appendices A–D as
> `{{NEEDS_SOURCE}}` until `case-research` either finds a citable public figure or returns NOT
> FOUND. Only a NOT FOUND figure, accepted by a human, gets recorded here as a stated Modeling
> Assumption — never invented at write time. Appendix A's composite alert-rate function *form*
> (a quadratic traffic-volume model composed with a square-root threat-scoring transform) is
> expected to end up here as a stated Modeling Assumption, since no public SOC platform
> documents its detection engine's exact scoring formula — the scale of its coefficients should
> still be anchored to the named benchmark reports above.

---

## Appendix F — Sources

> No sources are recorded yet. `case-research` populates this table as it resolves each
> `{{NEEDS_SOURCE}}` placeholder above, each row citing a real source with a URL, access date,
> and confidence grade — anchored to named published incident-response benchmark reports (e.g.
> IBM's Cost of a Data Breach Report, Verizon's Data Breach Investigations Report) per this
> case's approved concept.

| id | Claim | Value | Source | Accessed | Confidence |
|---|---|---|---|---|---|
| *(none yet)* | | | | | |

Referenced from Background.

---

## Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Tangent Line
- Differentiable

**"How to…" questions**

- How to use the chain rule to differentiate a composite function
- How to use the product rule to differentiate a product of functions
