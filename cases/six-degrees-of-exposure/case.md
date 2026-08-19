Case Study: Six Degrees of Exposure
MS | Math | Case Study | 2026 | Launchpad

## Overview

Dr. Yolanda Marsh has the county's outbreak-response line open in one ear and a spreadsheet of
contact-tracing interviews open on both monitors. Calloway State's health center called it in nine
days ago: mumps, confirmed, then confirmed again, then confirmed a third time in a different
residence hall. Her team has spent the week doing what contact tracers do — sitting across from
sick and exposed students, asking who they eat with, who they study with, whose room they crashed
in after a party — and logging every name into the same interaction graph the university's own
platform already keeps. The graph is open on her second monitor now, a mess of dots and lines she
can no longer read by eye.

Her regional director is blunter on the phone than usual. The county's rapid-response vaccination
clinic can go live tomorrow morning, but the dose allocation that just cleared the state warehouse
is fixed, and so is the outreach staff assigned to administer it — not a dose or a labor-hour more.
Two operational plans sit in her inbox, both built to spend that exact same allocation and neither
one a dollar more. One plan sends her contact-tracing team back out to confirm and vaccinate the
small number of students its own graph says are the most connected people on campus. The other
skips that confirmation work entirely and vaccinates a much larger number of students chosen at
random from the same traced population.

Her director wants an answer before the clinic opens its doors. Dr. Marsh minimizes the
spreadsheet, opens both plans side by side, and starts reading.

## Background

Dr. Yolanda Marsh is the lead epidemiologist for the Calloway County Department of Public Health.
She is responsible for the county's outbreak-response operations and accountable to the county
health director for how the fixed, one-time state dose allocation is spent (SEE APPENDIX D). She
does not set the size of that allocation and cannot request more once the clinic opens, but she
authors the operational plan the clinic runs on.

The outbreak is centered on Calloway State University. Over nine days, the county's contact-tracing
team built a traced-contact network of **1,899** students and staff, connected by **13,838**
confirmed contact pairs (SEE APPENDIX A; SEE APPENDIX E, MA1). Every pair in the network carries a weight equal to the number of
separate contact events logged between those two people during the surveillance window (SEE
APPENDIX A) — two people who crossed paths once carry a light edge; roommates or lab partners who
were logged together dozens of times carry a heavy one. Like every real contact-tracing graph, this
one is badly uneven: most people in it have only a handful of traced contacts, a small number have
dozens, and a very small number are traced to far more contacts than a typical person in the graph
(SEE APPENDIX A).

Two operational plans are under consideration. Both are sized to draw down the exact same fixed
dose-and-outreach budget (SEE APPENDIX D) — neither can run over it, and neither is required to run
under it:

**Operation Hub Sweep** would send the contact-tracing team back out to confirm and vaccinate the
50 individuals the traced network ranks highest by degree — the number of distinct people each one
is confirmed to have been in contact with (SEE APPENDIX B). Locating, re-confirming, and physically
reaching each of these 50 people costs more per dose, because it requires the same case-investigation
fieldwork the tracing team has been doing all week (SEE APPENDIX D).

**Operation Wide Net** would skip that confirmation fieldwork and vaccinate 500 individuals selected
uniformly at random from the same traced population, at the lower per-dose cost of a standard
outreach-clinic invitation — a postcard, a text, a scheduled slot, no case investigation required
(SEE APPENDIX D).

The two operations are judged on a single number: the total weight of traced-contact connections
eliminated from further spread once vaccination takes effect, per dollar of the shared budget (SEE
APPENDICES A, B and D). Because both operations spend the identical budget, the comparison reduces
to a direct question — which operation's vaccinated set removes more of the network's total
contact-weight? Dr. Marsh's team also needs a fast way to warn newly-exposed contacts down a chain
of confirmed contacts once a case is found (SEE APPENDIX C). Every sourced figure in this case is
listed in **APPENDIX F**, and the vocabulary and "how to…" skills this case will ask of you are
listed in **APPENDIX G** — that is where Challenge 1 sends you.

## Dilemma

You are Dr. Yolanda Marsh.
Do you:
A.) Run Operation Hub Sweep — vaccinate the 50 highest-degree individuals in the traced network OR
B.) Run Operation Wide Net — vaccinate 500 individuals chosen at random from the same population

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A labeled, weighted diagram of the sample contact subgraph (SEE APPENDIX C): every vertex
    drawn and labeled with its traced ID, every edge drawn and labeled with its weight (the number
    of recorded contact events between that pair).
    D2. A ranked degree table (SEE APPENDIX B): the 50 individuals with the highest degree in the
    full traced network, each row showing that vertex's degree — the count of distinct edges
    (contacts) touching it — used to build Operation Hub Sweep's vaccination list.
    D3. A transmission-weight-eliminated comparison table (SEE APPENDICES A and B): for Operation
    Hub Sweep and for Operation Wide Net, the total weight of every edge with at least one endpoint
    in that operation's vaccinated set — with the full arithmetic shown. For Operation Wide Net, that
    means the counting argument used to find its expected value (a random selection cannot be listed
    out by hand the way Hub Sweep's fixed 50 can). For Operation Hub Sweep, that means summing the 50
    individuals' weighted degrees (SEE APPENDIX B) and then correcting for double-counting: every
    edge that connects two of those same 50 individuals gets summed twice (once at each endpoint),
    so its weight must be subtracted once to reach the true total. Appendix B gives you every number
    that correction needs. Then, using Appendix D, check whether the two operations' sourced per-dose
    costs are actually consistent with a single shared budget buying exactly 50 Hub Sweep doses and
    500 Wide Net doses — and if they are not, compute what split that shared budget would actually
    imply at the sourced rates, and state the discrepancy.
    D4. A shortest notification-path calculation (SEE APPENDIX C): using the sample subgraph's edge
    weights, at least two candidate paths between the two named individuals identified there,
    compared by total path cost, with the lower-cost path identified as the fastest realistic
    notification chain.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — The Traced Contact Network

| | Value |
|---|---|
| Individuals in the network (vertices) | **1,899** [S3] (SEE APPENDIX E, MA1) |
| Confirmed contact pairs (edges) | **13,838** [S3, derived] |
| Total contact-weight across all edges (sum of every edge's contact-event count) | **59,835** [S3] |
| Mean degree (average number of distinct contacts per person) | **14.57** [S3, derived] |
| Median degree | **5** [S3, derived] |
| Maximum degree (single most-connected individual) | **255** [S3, derived] |
| Minimum degree | **1** [S3, derived] |
| Surveillance window covered by the network | **193 days** [S3] |

**How Appendix A was built.** The network is derived from a real, public, anonymized ID-to-ID
interaction dataset (SEE APPENDIX E, MA1). The raw data is 59,835 timestamped one-to-one interaction records
between 1,899 people over 193 days. This case collapses that into a single undirected weighted
graph: each unordered pair (i, j) that interacted at least once becomes one edge, and that edge's
weight is the total count of interaction records between i and j. That collapse produced the
13,838 edges and the degree figures above — this is this case's own derivation from the raw
records, not a number printed on the source's own page (the source's own summary reports a
*directed* static-graph edge count instead; SEE APPENDIX F, S3).

## Appendix B — Operation Hub Sweep Candidate List

The 50 individuals with the highest degree in the full 1,899-person traced network [S3, derived],
ranked by degree. Ties broken by lower traced ID.

| Rank | Traced ID | Degree | Weighted Degree | | Rank | Traced ID | Degree | Weighted Degree |
|---|---|---|---|---|---|---|---|---|
| 1 | 103 | 255 | 1,179 | | 26 | 277 | 105 | 717 |
| 2 | 9 | 241 | 1,289 | | 27 | 323 | 104 | 1,546 |
| 3 | 105 | 227 | 1,031 | | 28 | 523 | 101 | 212 |
| 4 | 400 | 227 | 679 | | 29 | 1189 | 99 | 541 |
| 5 | 32 | 207 | 958 | | 30 | 1543 | 99 | 329 |
| 6 | 41 | 183 | 747 | | 31 | 840 | 93 | 294 |
| 7 | 3 | 178 | 467 | | 32 | 1598 | 93 | 185 |
| 8 | 42 | 177 | 609 | | 33 | 144 | 91 | 376 |
| 9 | 249 | 172 | 750 | | 34 | 770 | 91 | 355 |
| 10 | 638 | 169 | 628 | | 35 | 95 | 90 | 516 |
| 11 | 713 | 161 | 642 | | 36 | 36 | 89 | 326 |
| 12 | 194 | 160 | 537 | | 37 | 325 | 89 | 488 |
| 13 | 67 | 156 | 484 | | 38 | 1624 | 89 | 1,198 |
| 14 | 1283 | 152 | 385 | | 39 | 475 | 88 | 553 |
| 15 | 372 | 146 | 913 | | 40 | 697 | 86 | 337 |
| 16 | 357 | 143 | 384 | | 41 | 128 | 85 | 530 |
| 17 | 12 | 142 | 1,210 | | 42 | 679 | 85 | 730 |
| 18 | 598 | 123 | 528 | | 43 | 297 | 84 | 561 |
| 19 | 176 | 121 | 611 | | 44 | 212 | 83 | 475 |
| 20 | 321 | 117 | 370 | | 45 | 644 | 83 | 292 |
| 21 | 1281 | 117 | 545 | | 46 | 63 | 82 | 499 |
| 22 | 704 | 113 | 524 | | 47 | 204 | 82 | 348 |
| 23 | 19 | 110 | 425 | | 48 | 1236 | 80 | 392 |
| 24 | 1713 | 110 | 658 | | 49 | 254 | 79 | 564 |
| 25 | 308 | 106 | 505 | | 50 | 605 | 78 | 802 |

**Sum of these 50 degrees:** 6,241 (double-counts any edge with both endpoints in this list) [S3, derived]

**Sum of these 50 weighted degrees:** 30,224 [S3, derived]. This double-counts too — for the same
reason as the plain degree sum above, but now in contact-weight instead of edge count: an edge
connecting two individuals who are *both* on this list gets added into the weighted-degree total
twice, once at each endpoint.

**The double-counted edges themselves.** Of this list's 6,241 counted edges, exactly **382** connect
two of these same 50 individuals to each other rather than to someone outside the list; those 382
internal edges carry a combined weight of **2,581** [S3, derived]. Each of those 382 is counted
*twice* in the 30,224 weighted-degree sum above (once at each of its two top-50 endpoints) and
*twice* in the 6,241 degree sum, so each needs to be subtracted back out exactly once — not left in
at full double-weight, and not removed entirely — to reach the true, non-double-counted total. D3
asks you to carry out that subtraction yourself and show it; this appendix gives you every number
the correction needs (30,224; 382; 2,581) but not the finished result.

## Appendix C — Sample Weighted Contact Subgraph

A small, real excerpt of the traced network, kept to a size a person can trace by hand [S3, derived].
Used for D1 and D4.

**Vertices:** Contact 47, Contact 46, Contact 78, Contact 91, Contact 567, Contact 814, Contact
1142, Contact 1299, Contact 1540, Contact 63, Contact 105

**Weighted edges:**

| Edge | Weight (recorded contact events) |
|---|---|
| Contact 47 — Contact 46 | 1 |
| Contact 47 — Contact 78 | 1 |
| Contact 47 — Contact 91 | 1 |
| Contact 47 — Contact 567 | 2 |
| Contact 47 — Contact 814 | 5 |
| Contact 47 — Contact 1142 | 1 |
| Contact 47 — Contact 1299 | 1 |
| Contact 47 — Contact 1540 | 2 |
| Contact 814 — Contact 63 | 20 |
| Contact 814 — Contact 105 | 1 |
| Contact 63 — Contact 105 | 4 |

[S3, derived]

**Notification-cost rule (for D4).** A pair recorded in contact more times has a faster, more
reliable line for passing along an exposure notification. Define the notification cost of an edge
as 1 ÷ (that edge's weight). The fastest way to notify one traced individual starting from another
is the path — direct or through intermediate people — that minimizes the total summed notification
cost, not necessarily the path with the fewest steps. D4 asks you to find the fastest notification
path from **Contact 47** to **Contact 105**.

## Appendix D — Program Cost

| | Value |
|---|---|
| Cost per dose delivered through Operation Wide Net (standard outreach-clinic invitation, no case investigation) | **$38.00** (median; range $9–$206) [S1] |
| Case-investigation labor cost to confirm and locate one Operation Hub Sweep contact | **$175.94** (range $79.97–$293.51) [S2] |
| Fully-loaded cost per dose delivered through Operation Hub Sweep (case-investigation labor + the same $38.00 administration cost as Wide Net) | **$213.94** = $175.94 + $38.00 [S1, S2, derived] |
| Doses funded by the shared budget, Operation Hub Sweep | 50 |
| Doses funded by the shared budget, Operation Wide Net | 500 |

**A discrepancy this case does not hide.** At these sourced national-median rates, 500 Wide Net
doses at $38.00 draw down $19,000.00. That same $19,000.00 at Hub Sweep's $213.94-per-dose rate
buys about **88.8 doses** ($19,000.00 ÷ $213.94), not 50. Calloway County is fictional and its own
internal budget and staffing figures are not public record, so this case fixes Hub Sweep and Wide
Net's headcounts at the stated 50 and 500 as the county's own announced operational plan (SEE
APPENDIX E, MA3) rather than deriving them from Appendix D. Appendix D's real, sourced figures
establish the right *order of magnitude and direction* — a targeted, case-investigation-based dose
costs meaningfully more than a random-outreach dose, by roughly 5.6× at these national medians —
without pretending they pin down Calloway County's exact, non-public split. D3 asks you to find
and state this discrepancy yourself.

## Appendix E — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | The traced contact network's identity | Modeled using the real, public **CollegeMsg** dataset (Panzarasa, Opsahl & Carley, 2009; distributed by Stanford SNAP) as a structural stand-in for Calloway County's actual contact-tracing graph | Real public-health contact-tracing data is protected health information and cannot be published for a classroom exercise. CollegeMsg is a real, public, anonymized person-to-person interaction network of a comparable, classroom-workable size (1,899 people) with the same qualitative shape — a small number of highly-connected people and a long tail of lightly-connected ones — that the network-epidemiology literature uses for exactly this targeted-vs-random comparison. | The case's entire primary-metric margin (Appendix A/B data) depends on this specific network's actual degree distribution. A different real network with a different skew could change the margin or flip which operation wins — that dependency is the honest core of the case, not a flaw to be hidden. |
| MA2 | Edge weight meaning | Each edge's weight is treated as its number of recorded contact events, standing in for how often two traced individuals were in contact during the surveillance window | The source dataset's edges are private-message counts between two people; this case treats repeated messages as a proxy for repeated real-world contact, the same substitution MA1 already makes at the network level. | Does not change which edges exist, only how "heavier" edges are interpreted; does not affect the primary-metric arithmetic, which only needs the weight values themselves. |
| MA3 | Operation headcounts (50 and 500) | Fixed at 50 (Hub Sweep) and 500 (Wide Net), as stated in the case brief | Calloway County is fictional; its real budget and internal per-dose costs are not public record. Appendix D's real, sourced national-median costs do not, at their exact values, divide one shared budget into precisely 50 and 500 (SEE APPENDIX D) — the case fixes the headcounts directly rather than forcing a fit to national data that would not represent one specific county's real contract rates anyway. | Does not affect the primary-metric comparison in D3's first half (which uses Appendix A/B network data directly, independent of Appendix D). It is the reason D3's second half exists — to make the discrepancy a Hero must reckon with, rather than a fact hidden in a footnote. |

## Appendix F — Sources

| id | Claim | Value | Source | Accessed | Confidence |
|---|---|---|---|---|---|
| S1 | Median cost per COVID-19 vaccination dose administered at a public-health-department-run outreach clinic, and its range | $38.00 (range $9–$206) | Yarnoff BO, Pike JJ, Athar HM, Bates LG, Tayebali ZA, Harris LQ, Jones-Jack NH, Washington ML, Cho B-H. "Assessment of the Costs of Implementing COVID-19 Vaccination Clinics in 34 Sites, United States, March 2021." *Journal of Public Health Management and Practice* 28(6):624-630 (2022). DOI: 10.1097/PHH.0000000000001561. ([PMC open-access copy](https://pmc.ncbi.nlm.nih.gov/articles/PMC9532365/)) | 2026-08-13 | HIGH — primary, dated, named authors and venue, fetched directly; 34 public-health-department clinics across 8 states and 1 metro area |
| S2 | Labor cost to confirm and investigate one contact during a contact-tracing operation, and its range | $175.94 per contact (range $79.97–$293.51), 2022 USD | Beeler Asay GR, Young KH, Hill TD, Njie GJ. "Systematic Review of Contact Investigation Costs for Tuberculosis, United States." *Emerging Infectious Diseases* 31(7), July 2025. ([cdc.gov](https://wwwnc.cdc.gov/eid/article/31/7/24-1827_article)) | 2026-08-13 | HIGH — primary CDC journal, systematic review of 10 US studies (Jan 1990–Aug 2024), fetched directly. Figure is a labor-cost proxy: it is drawn from tuberculosis contact-investigation programs, not mumps, because no equivalent published per-contact labor-cost figure specific to mumps case investigation could be located in this session; the fieldwork itself (locate, interview, confirm a named contact) is disease-agnostic in a way the case relies on, and that substitution is disclosed here rather than presented as mumps-specific data |
| S3 | The traced contact network's raw structure (nodes, timestamped edges, time span) | 1,899 nodes; 59,835 timestamped person-to-person interaction records; 193-day span; SNAP's own summary separately reports 20,296 edges in a *directed* static graph (this case instead derives 13,838 edges in an *undirected* weighted graph — SEE APPENDIX A for that derivation) | Panzarasa P, Opsahl T, Carley KM. "Patterns and dynamics of users' behavior and interaction: Network analysis of an online community." *Journal of the American Society for Information Science and Technology* 60(5):911-932 (2009). Distributed as the "CollegeMsg temporal network" by Stanford SNAP: [snap.stanford.edu/data/CollegeMsg.html](https://snap.stanford.edu/data/CollegeMsg.html), raw file [CollegeMsg.txt.gz](https://snap.stanford.edu/data/CollegeMsg.txt.gz) | 2026-08-13 | HIGH — primary published dataset with an academic citation, raw edge list fetched and directly processed for this case (SEE RESEARCH_LOG.md for the exact derivation and its cross-check against SNAP's own posted summary statistics) |

## Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Graph (Vertices And Edges)
- Vertex
- Edge
- Weighted Graph

**"How to…" questions**

- How to find the shortest path between two vertices in a weighted graph

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
