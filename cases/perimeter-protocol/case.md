# Case Study: Perimeter Protocol

MS | Math | Case Study | 2026-27 | Heroes Academy

---

## Overview

The change ticket has been open on Marcus Webb's second monitor for forty minutes, cursor blinking in the approval field, while his first monitor scrolls a live feed of blocked and allowed traffic hitting the hospital network's edge firewall. It's Friday, 4:50 p.m. Whatever rule set he approves in the next few minutes goes live at the start of the deployment window tonight and holds through the weekend — the network security team runs a skeleton crew until Monday, and nobody is rewriting firewall logic from a phone at 2 a.m.

Two configuration files sit open in two tabs. Both were built by the same engineer, tested against the same log data, and both do exactly what they claim. One tab casts a wider net — it flags more of the traffic that actually turns out to be dangerous, but it also flags more of the traffic that's just a vendor's badly-behaved integration pinging the wrong port. The other tab is tighter — quieter alerts, a cleaner queue for whoever's on call, but real risk gets a little more room to slip through underneath it.

Marcus's badge is still clipped to his lanyard from the walk back from the vending machine. Somewhere down the hall, the clinical systems the firewall protects are still logging patient encounters. He pulls both tabs into view side by side and rests his hand on the mouse.

---

## Background

Marcus Webb is a Security Operations Analyst on the IT security desk of a regional hospital network. He is responsible for recommending the edge-firewall rule logic that screens inbound traffic to the network's clinical and administrative systems, and for the false-positive load that recommendation places on the analyst rotation that has to review it (SEE APPENDIX A).

Every inbound request the firewall inspects is evaluated against two yes/no conditions:

- **p** — the source IP address matches an entry on a CISA Known Exploited Vulnerabilities (KEV)-linked watchlist (SEE APPENDIX B).
- **q** — the request targets a network port with a known, currently unpatched vulnerability.

Marcus has two fully-built, fully-tested rule sets in front of him, and the deployment window opens tonight (SEE APPENDIX A):

**Rule Set A — "Broad Net."** Block the request if **p OR q** — the source IP is on the watchlist, or the port is unpatched, or both. This is a disjunction: it blocks every request Rule Set B blocks, plus more. It catches more real threats. It also flags more legitimate traffic, because plenty of harmless traffic trips exactly one of the two conditions without being dangerous at all.

**Rule Set B — "Narrow Gate."** Block the request only if **p AND q** — the source IP must be on the watchlist *and* the port must be unpatched, both at once. This is a conjunction: it blocks a request only when every condition is true. It generates far fewer false alarms for the weekend's skeleton crew to chase down. It also lets through any request that trips only one of the two conditions — including a watchlisted IP hitting a fully patched port, or an unlisted IP hitting an unpatched one.

The security desk runs on a two-person weekend skeleton crew, with a fixed total of **20 analyst-hours** available to triage every blocked-and-flagged alert before Monday's full-staff handoff (SEE APPENDIX A; this figure is a stated Modeling Assumption — see Modeling Assumptions below). Each false positive an analyst has to review costs real time pulled from that fixed pool — time that isn't available for anything else that comes up over the weekend (SEE APPENDIX D). Every request the firewall sees over the deployment weekend is logged in a sampled traffic set Marcus is working from (SEE APPENDIX C).

Appendix A gives Marcus's role and the weekend staffing constraint. Appendix B gives the real-world grounding for the watchlist condition, p. Appendix C is the sampled traffic Marcus has to classify under both rule sets. Appendix D is what a single false positive costs the weekend crew. Appendix E lays out the conditional statement both rule sets are built on. Appendix F lists every source. Appendix G is where Challenge 1 sends you.

He has to approve one rule set before the change window opens.

---

## Dilemma

You are Marcus Webb.

Do you:

**A.)** Approve Rule Set A ("Broad Net") — block on **p OR q**, catching more real threats at the cost of more false positives **OR**

**B.)** Approve Rule Set B ("Narrow Gate") — block only on **p AND q**, generating far fewer false positives at the cost of letting more real threats through

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — Two complete truth tables.** Build a full truth table for Rule Set A's block condition (**p OR q**) and a full truth table for Rule Set B's block condition (**p AND q**), each with all four rows of p and q and every output labeled True (block) or False (allow).
- **D2 — A worked classification table.** Apply both truth tables from D1 to every request in the Traffic Sample (Appendix C): for each request, evaluate whether Rule Set A blocks it and whether Rule Set B blocks it, then total the number of true threats blocked and false positives generated under each rule set.
- **D3 — A negation exercise.** Write the negation of p, the negation of q, and the negation of Rule Set A's full block condition (**NOT (p OR q)**). Then identify, by request number, every entry in the Traffic Sample (Appendix C) that satisfies that negation — the requests Rule Set A allows through untouched.
- **D4 — A converse/inverse/contrapositive analysis.** Take the conditional statement in Appendix E ("If a source IP is on the watchlist, then it is a genuine threat"). Write its converse, its inverse, and its contrapositive. For each of the four statements (original, converse, inverse, contrapositive), state whether the Traffic Sample (Appendix C) shows it to be reliably true or shows a counterexample. Close with a short paragraph naming exactly which of the four statements Rule Set B implicitly relies on being true, and what that means for whether Rule Set B's assumption is safe.
- **D5 — A false-positive-cost comparison.** Using your D2 totals and the per-alert triage cost in Appendix D, compute the total weekend triage time each rule set would impose on the skeleton crew, and state whether that total fits within the fixed analyst-hour pool in Appendix A. Then compute each rule set's true-threats-blocked-per-false-positive ratio (the primary metric). Close with a one-paragraph statement of which rule set you are recommending and the margin between them on that ratio.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A — Marcus's Role and the Weekend Staffing Constraint

Marcus Webb is a Security Operations Analyst on the IT security desk of a regional hospital network — a multi-facility system whose edge firewall screens inbound traffic to both clinical data systems and administrative systems. He is responsible for recommending which of two fully-tested rule sets ships to production before the weekend deployment window (SEE BACKGROUND).

The security desk staffs a two-person weekend skeleton crew from Friday evening's deployment through Monday morning's full-staff handoff, with a fixed total of **20 analyst-hours** available across both analysts combined to triage every alert the firewall generates (Modeling Assumption MA1 — see Modeling Assumptions below). Alerts beyond that pool queue untouched until Monday morning.

## Appendix B — The CISA Known Exploited Vulnerabilities Watchlist

Proposition **p** — "the source IP address matches an entry on a CISA Known Exploited Vulnerabilities (KEV)-linked watchlist" — is grounded in a real, actively maintained federal catalog. The U.S. Cybersecurity and Infrastructure Security Agency (CISA) publishes the Known Exploited Vulnerabilities catalog, a list of vulnerabilities confirmed to have been exploited in the wild, updated on an ongoing basis. As of **August 21, 2026** (catalog version 2026.08.21), the catalog listed **1,674 entries** [S1]. Security teams commonly build IP/indicator watchlists that flag traffic associated with infrastructure linked to cataloged vulnerabilities — this is the real-world practice Rule Set A and Rule Set B's condition p represents.

## Appendix C — The Weekend Traffic Sample

No public per-hospital firewall log exists — real logs are never published, for the obvious reason that publishing one would hand attackers a map. This table is a **stated Modeling Assumption**: a synthetic, 20-request sample of the deployment weekend's inbound traffic, built by hand so that both propositions (p and q) and a ground-truth threat determination are known for every row. It is not sourced to a real log, the same way `cases/grant-reach/case.md`'s 9,000-student population is a stated scenario scale rather than a real per-university roster (see Modeling Assumptions below, MA2).

**Table C-1 — Weekend Traffic Sample (20 requests)**

| Req. # | p — Watchlist Hit? | q — Unpatched-Port Hit? | Ground Truth: Confirmed Threat? | Traffic description |
|---|---|---|---|---|
| 1 | T | T | T | Known malware C2 IP hitting an unpatched RDP port |
| 2 | T | T | T | Watchlisted IP scanning an unpatched VPN appliance port |
| 3 | T | T | T | Watchlisted IP exploiting an unpatched file-transfer service |
| 4 | T | T | T | Watchlisted IP probing an unpatched legacy print-server port |
| 5 | T | T | F | Decommissioned vendor lab server, stale watchlist entry, dev port still open |
| 6 | T | T | F | Security researcher's authorized scanner, IP flagged by an outdated feed |
| 7 | T | F | T | Watchlisted IP attempting credential stuffing on a patched login portal |
| 8 | T | F | T | Watchlisted IP delivering phishing payload via a patched mail relay |
| 9 | T | F | T | Watchlisted IP probing a patched imaging-system API |
| 10 | T | F | F | Cloud host reused by a prior campaign, now leased to an unrelated SaaS vendor |
| 11 | T | F | F | Shared university research-network IP, stale watchlist listing |
| 12 | F | T | T | Unlisted IP exploiting an unpatched building-management-system port |
| 13 | F | T | T | Unlisted IP exploiting an unpatched lab-equipment integration port |
| 14 | F | T | T | Unlisted IP exploiting an unpatched guest-WiFi controller port |
| 15 | F | T | F | Vendor clinical-data integration hitting its own not-yet-patched port |
| 16 | F | T | F | Internal maintenance scanner hitting an unpatched legacy scheduling port |
| 17 | F | F | T | Unlisted IP using a patched-port social-engineering follow-up request |
| 18 | F | F | F | Routine patient-portal login |
| 19 | F | F | F | Routine insurance-eligibility lookup |
| 20 | F | F | F | Routine appointment-reminder API call |

## Appendix D — The Cost of a False Positive

No single published figure gives a clean, current dollar or time cost for one false-positive security alert — the two candidate surveys below measure a rate (share of analyst time) and a whole-organization annual total, not a clean per-alert figure. Real published research consistently shows this cost is large and real:

- A Ponemon Institute survey conducted with Exabeam found that **25% of a security analyst's time is spent chasing false positives** [S2].
- An earlier Ponemon Institute survey (sponsored by Damballa), *The Cost of Malware Containment*, found that organizations spend an average of **$1.3 million per year and roughly 21,000 hours per year** investigating alerts that turn out to be inaccurate or unreliable, out of an average 16,937 alerts received per week (of which only 19% were deemed reliable) [S3].

Neither figure converts cleanly into "cost of one false-positive alert" without an extra assumption this case is not going to smuggle in as though it were measured. This case therefore sets a stated Modeling Assumption — **15 analyst-minutes per false-positive alert** — anchored to the real scale these two surveys establish (a meaningful share of analyst time, and real annual costs in the hundreds-of-thousands-to-millions range for a full organization), not a literal transfer of either survey's own number (Modeling Assumption MA3 — see Modeling Assumptions below).

## Appendix E — The Conditional Statement

Consider the conditional statement: **"If a source IP is on the CISA KEV-linked watchlist, then it is a genuine threat."** This is the conditional Rule Set A and Rule Set B are both, in different ways, built on top of. Deliverable D4 asks you to work out its converse, inverse, and contrapositive, and to test each one against the Traffic Sample (Appendix C) — because at least one of those four statements is *not* reliably true, and a rule set like Rule Set B can quietly depend on assuming it is true anyway.

## Modeling Assumptions

> These figures are **not sourced to a real hospital network's own logs or staffing roster** — no
> public dataset reports a specific hospital's firewall traffic, SOC weekend staffing, or per-alert
> triage cost. They are stated scenario assumptions, built to be realistic in scale using real
> published research (Appendices B and D) rather than picked arbitrarily. A Hero may challenge them
> in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Weekend skeleton-crew analyst-hour pool | 20 analyst-hours | Stated scenario constraint: a two-person weekend on-call crew, sized to be realistic for a small hospital-network SOC desk without claiming a specific real organization's staffing. | The answer is sensitive to this value. |
| MA2 | Weekend traffic sample (Table C-1) | 20 requests, hand-built with p, q, and ground-truth-threat flags on every row | No public per-hospital firewall log exists, and none should be published even if one did. Built by hand so that the mix of watchlist-only, unpatched-port-only, both, and neither traffic — and the share of each that is a genuine threat versus legitimate — is internally consistent and gradable, following the same stated-scenario pattern as the 9,000-student population in `cases/grant-reach/case.md`. | The answer is sensitive to this value. |
| MA3 | Average analyst time to triage one false-positive alert | 15 minutes | No clean per-alert figure is published. Anchored to two real Ponemon Institute surveys (Appendix D, [S2] [S3]) establishing that false-positive triage consumes a large, real share of analyst time and produces real six- and seven-figure annual costs for a full organization — not a literal transfer of either survey's own number, which measure a rate and a whole-organization annual total respectively, not a single alert. | The answer is sensitive to this value. |

## Appendix F — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Total entries in the CISA Known Exploited Vulnerabilities (KEV) catalog | 1,674 entries, catalog version 2026.08.21 | Cybersecurity and Infrastructure Security Agency (CISA) — [Known Exploited Vulnerabilities Catalog JSON feed](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) | released 2026-08-21; accessed 2026-08-24 | HIGH |
| S2 | Share of a security analyst's time spent chasing false-positive alerts | 25% | Ponemon Institute, with Exabeam — *SIEM Productivity Report*, as reported by Bitdefender — ["Every Hour SOCs Run, 15 Minutes Are Wasted on False Positives"](https://www.bitdefender.com/en-us/blog/businessinsights/every-hour-socs-run-15-minutes-are-wasted-on-false-positives) | August 2019; accessed 2026-08-24 | MEDIUM |
| S3 | Average annual cost and hours organizations spend investigating inaccurate/unreliable security alerts | $1.3 million/year; ~21,000 hours/year; 16,937 average weekly alerts, 19% deemed reliable | Ponemon Institute, sponsored by Damballa — *The Cost of Malware Containment*, as reported by SecurityWeek — ["False Positive Alerts Cost Organizations $1.3 Million Per Year: Report"](https://www.securityweek.com/false-positive-alerts-cost-organizations-13-million-year-report/) | 2015; accessed 2026-08-24 | MEDIUM |

## Appendix G — "How To…" Math Questions To Research

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

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
