# Research Log — Six Degrees of Exposure

One row per placeholder from the `case-write` draft: what was searched, what was fetched, what was
found, what was rejected and why.

## P01/P02 — Appendix A network stats (vertices, edges, weight sum, degree distribution, window)

**The core sourcing decision for this case.** SPEC §6/brainstorm require a *real* social/contact-
structure graph, not an invented one, because actual county contact-tracing data is protected
health information and cannot be published for a classroom exercise.

- Tier-1 attempt: searched for a real, public **weighted physical-contact** network at a scale
  where "50 highest-degree" and "500 random" are both meaningful fractions of the population (i.e.
  population meaningfully larger than 500). Found and evaluated the SocioPatterns hospital-ward
  contact network (Vanhems et al. 2013, PLOS ONE) — real, weighted, thematically perfect, but only
  75 people (46 HCWs + 29 patients). **Rejected for scale**: a random sample of 500 is not
  meaningful from a 75-person population.
- Checked the SocioPatterns high-school contact network (Mastrandrea et al. 2015, PLOS ONE;
  Fournet & Barrat 2014). Downloaded and directly aggregated the raw proximity file
  (`HighSchool2013_proximity_net.csv.gz`, 653 KB, 188,508 rows) myself: confirmed **327 nodes,
  5,818 weighted edges**, matching the published literature exactly (cross-check passed). **Still
  rejected for scale** — 327 people is smaller than the 500-person Wide Net operation itself.
- Moved to SNAP's larger interaction-network datasets. Selected **CollegeMsg** (Panzarasa, Opsahl &
  Carley 2009; distributed by Stanford SNAP) — 1,899 people, large enough that both a 50-person hub
  set (2.6% of the population) and a 500-person random set (26.3%) are meaningful, non-degenerate
  fractions. Downloaded the raw file directly
  (`https://snap.stanford.edu/data/CollegeMsg.txt.gz`, 345,339 bytes) and processed it with Python:
  aggregated 59,835 timestamped one-to-one interaction records into an undirected simple weighted
  graph (unordered pair → one edge, weight = interaction count). Result: **1,899 nodes, 13,838
  edges, total weight 59,835, mean degree 14.57, median 5, max degree 255, min 1**. This differs
  from SNAP's own posted "edges in static graph: 20,296" statistic because that figure counts the
  *directed* static graph; this case needed an undirected "were these two people ever in contact"
  graph instead, so it is this case's own derivation, disclosed as such (S3, `derived: true`).
- **Accepted.** Real, public, large enough for both options to be meaningful, and structurally
  representative (heavily right-skewed degree distribution) of the kind of network the
  network-epidemiology literature uses for targeted-vs-random immunization comparisons. Recorded as
  Modeling Assumption MA1 (the specific network is a stand-in, not literally Calloway County's own
  data) rather than as a plain source, because the *substitution itself* — not just the network's
  statistics — is the thing a Hero should be able to see and challenge.

## P03 — Appendix B ranked top-50 degree list

Direct computation from the same processed dataset (P01/P02), not a separate search. Computed the
degree (count of distinct edges) of every node, sorted descending with ties broken by lower traced
ID, and took the top 50. Cross-checked the 50th/51st boundary (both degree 78 and lower; rank 50 =
ID 605 at degree 78, rank 51 = ID 871 at degree 78, tie broken by ID) to confirm the cutoff was
handled deterministically. Recorded in Appendix B with the same S3 citation, `derived: true`.

**2026-08-18 addendum — closing the D3 data gap.** Tier 2 (P1/P2) found that D3 asks Heroes to
state Hub Sweep's exact total weight-eliminated "with the full arithmetic shown," but Appendix B
originally published only unweighted degree, not enough to reach the exact 27,643 figure without
either the full 13,838-edge list or a hand-wave. Re-downloaded the raw
`CollegeMsg.txt.gz` and re-ran the same aggregation as P01/P02/P03 to compute, for each of the same
50 individuals, their **weighted degree** (sum of incident edge weights, not just edge count) and
the **internal edges** connecting two of those same 50 individuals to each other. Result: weighted
degree sum over the 50 = 30,224; 382 internal edges with combined weight 2,581; 30,224 − 2,581 =
27,643 exactly, and 6,241 − 382 = 5,859 distinct edges exactly — both reproducing the case's
existing, previously-facilitator-only figures byte-for-byte. Cross-checked the full top-50 ID/degree
list from this re-run against the published Appendix B table: all 50 rows match exactly, confirming
this is the same underlying computation, re-run rather than re-derived differently. Added a Weighted
Degree column plus the 30,224/382/2,581 disclosure to Appendix B and rewrote D3 to ask for this
double-counting-correction arithmetic explicitly, restoring an honest, fully-derivable path from the
published appendices to the case's own graded Hub Sweep total. See QA_REPORT.md's 2026-08-18 entry.

## P04 — Appendix C sample weighted subgraph

Direct computation from the same processed dataset. First tried a pure ego-network around a
moderate-degree node (Contact 78, degree 9) — rejected because none of its neighbors were connected
to each other, producing a bare star graph with no alternate path, which makes D4's "compare at
least two candidate paths" impossible. Selected Contact 47 (degree 8) instead and extended two hops
through its heaviest-weight neighbor (Contact 814) to Contact 63 and Contact 105, confirming real
edges (814–63 weight 20; 814–105 weight 1; 63–105 weight 4) existed in the raw data. This produces
two genuine, real candidate paths from Contact 47 to Contact 105 with different total notification
cost (direct-ish 2-hop: cost 1.2; longer 3-hop: cost 0.5) — the 3-hop path is actually cheaper,
which is exactly the point of a *weighted* shortest-path exercise. All 11 nodes and 11 edges in
Appendix C are real, verified rows from the raw file, not invented.

## P05 — Fully-loaded cost per Operation Hub Sweep dose (case-investigation labor)

- Tier-1 attempt: searched for a published per-contact labor cost specific to *mumps* contact
  investigation. **Not found** — mumps-specific per-contact cost studies are not common in the
  literature; most published contact-investigation cost studies are TB- or COVID-specific.
- Tier-2 attempt: searched broadly for "cost per contact traced / case investigation, USD, public
  health program." Found a systematic review of **TB** contact-investigation costs (Beeler Asay et
  al. 2025, *Emerging Infectious Diseases*, a CDC journal): labor cost per contact **$175.94**
  (range $79.97–$293.51, 2022 USD), from 10 US studies (1990–2024).
- **Accepted as a disease-agnostic proxy, graded MEDIUM (not HIGH)** — the underlying fieldwork
  (locate, interview, confirm one named contact) is largely disease-agnostic, but the figure comes
  from TB programs, not mumps, and that substitution is disclosed plainly in Appendix D and
  Appendix E MA3 rather than presented as mumps-specific.

## P06 — Cost per Operation Wide Net dose (standard outreach clinic)

- Tier-1 attempt: searched for CDC/state per-dose administration cost figures. Found Yarnoff et al.
  2022 (*Journal of Public Health Management and Practice*): median cost per COVID-19 vaccination
  administered at 34 public-health-department-run clinics = **$38.00** (range $9–$206), fetched
  directly from the open-access PMC copy.
- **Accepted, HIGH confidence** — primary, dated, named authors, a direct government-program cost
  assessment across 34 real clinics in 8 states + 1 metro area. Used as Wide Net's per-dose cost and
  as the administration-cost component folded into Hub Sweep's fully-loaded per-dose cost (S1 + S2).

## The budget-parity discrepancy (found during research, not hidden)

Combining P05 and P06: Hub Sweep's fully-loaded per-dose cost = $175.94 + $38.00 = $213.94. At these
sourced national-median rates, a budget sized for 500 Wide Net doses ($19,000.00) would buy only
about 88.8 Hub Sweep doses, not the case's stated 50. **This is a real finding, not an error to
correct by adjusting the sourced figures.** Calloway County is fictional; its actual internal budget
and per-dose contract rates are not public record, so this case fixes the two operations' headcounts
at 50 and 500 as the county's own stated operational plan (Modeling Assumption MA3) rather than
deriving them from national medians, and states the discrepancy openly in Appendix D and asks
students to find and reason about it in Challenge D3. It does not affect the primary-metric
comparison, which depends only on Appendix A/B network data, not on Appendix D's dollar figures.

## Verification

Ran the case-research Step 7 script (below). Result: 0 placeholders remaining, every `[S#]` marker
has a matching Appendix F row, every Appendix F row is cited at least once, no source record is
missing a required field, and no LOW-confidence source is used (S1 and S3 are HIGH; S2 is MEDIUM,
disclosed and non-load-bearing to the primary metric).
