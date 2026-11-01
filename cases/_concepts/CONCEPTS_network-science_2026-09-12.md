# Concept sheet — Networks, Graphs & Social Structure (`network-science`)

**Target and why.** `readmodel/domains.json`'s `network-science` entry is HIGH `authoring_priority`,
HIGH `data_availability.grade`, and `existing_cases: []` — zero cases in the corpus today, the
single clearest "authoring priority HIGH + zero coverage" domain combination available this
session. Its own `n_uncovered_signature_skills` reads 0, which is accurate but misleading: I
cross-checked every one of its 16 `signature_skills` live against `readmodel/standards_spine.json`
and none sit at true `n==0` (confirmed — the spine-wide sweep this session found zero skills
anywhere at `n==0`; scoring below uses `gap_queue.json`'s own `n<=2` thin convention instead, and
every skill id below carries its live `n`). Most of network-science's own signature skills
(Graph Theory group: vertex n=5, edge n=4, weighted-graph n=4, shortest-path how-to n=4) are
already reasonably covered, **not thin** — so I went looking for where this domain can *honestly*
reach a genuinely thin group instead of re-claiming already-adequate skills. It found one cleanly:
**Discrete Mathematics / Set Theory sits at 8/8 thin (every skill n=2)**, and "does person A's
contact/follower set overlap with person B's" is not a stretch for a network case — union,
intersection, and Venn diagrams of two people's connection lists are exactly what a contact-tracer
or trust-and-safety analyst computes by hand. **Discrete Mathematics / Combinatorics (2/5 thin:
binomial coefficient term + how-to)** and **Statistics And Probability / Probability (4/15 thin:
independent-event, permutation, and the two "number of outcomes" how-tos)** also turned out
genuinely reachable — counting possible node-pairs and enumerating bypass paths after a node is
removed are real graph combinatorics, not forced vocabulary.

| # | Concept | Score | Tier | Group(s) touched |
|---|---|---|---|---|
| C1 | The Overlap Call | **7.6** | T2 | Discrete Mathematics / Set Theory (8/8 thin, fully closed) |
| C2 | The Kill Switch | **5.2** | T3 | Statistics And Probability / Probability (4/4 remaining thin, fully closed) |
| C3 | The Hub Choice | **3.6** | T2 | Discrete Mathematics / Combinatorics (2/2 remaining thin, fully closed) |
| C4 | The Fifty | **2.9** | T3 | Combinatorics (2/2) + Probability (1) + Displaying Data (1) — split across groups, MEDIUM data |

**Recommendation.** Write **C1, The Overlap Call**, first. It is the only concept here that closes
a spine group *completely* (all 8 Set Theory skills, all currently thin at n=2) with a dilemma that
is not manufactured — two contact lists genuinely do or don't overlap, and the union/intersection
choice has real operational cost (more tests/suspensions vs. missed risk). Its data anchor, the
Stanford SNAP `ego-Facebook` dataset, is a real, previously-verified-live source
(`domains.json` lists SNAP as `verified: LIVE` this project) that ships literal per-person contact
lists ("circles") — exactly the union/intersection inputs the case needs, with the epidemiological
framing disclosed as a modeling proxy, not a real named outbreak. **C2** is the strong second pick:
it closes all four remaining thin Probability skills and needs nothing more exotic than a graph
with a removable central node. **Kill C4 for this round** — its best numbers (published
targeted-vs-random immunization efficacy) rest on academic papers I can name from memory (Cohen/
Havlin/ben-Avraham; Pastor-Satorras/Vespignani) but did not fetch and confirm live this session, so
it is graded MEDIUM, not HIGH, and it underperforms Cold Chain's 4.2 calibration anchor. **C3** is
a fine, low-effort third pick — real BTS route data, clean Combinatorics closure — but it barely
touches the domain's richer social-network flavor.

---

### C1 — The Overlap Call   ·   score 7.6   ·   tier T2

**Protagonist.** Priya Ostrowski, a county public-health contact-tracing lead who has two test
kits left in her weekly allotment for every ten flagged contacts and has to decide who gets called
today. Personally at stake: her last surge allocation ran out three days early and a supervisor is
asking why.

**The dilemma.** A.) Test everyone in the *union* of both index patients' contact lists — the
widest net, covering anyone exposed to either person OR B.) test only the *intersection* — people
exposed to both index patients, the smaller group with (on paper) the highest shared-risk
concentration.

**Primary metric.** Confirmed secondary cases found per test kit used (a ratio — total cases found
does not settle it, because the union group is bigger and will always find more in raw count; the
question is which set finds more *per kit*).

**Why it's close.** The intersection is small and cheap to fully test, and shared contacts plausibly
carry compounded exposure risk — but if the two index patients' circles barely overlap, the
intersection may be nearly empty while real secondary spread is happening in the union-only part of
each list. The two contact lists are drawn from a real social-graph dataset (not invented), so the
actual overlap size is a genuine unknown until a student computes it — a Venn diagram of the two
sets is the first real deliverable, not decoration.

**Would close (8 skills, 2 how-to / 6 term, all currently n=2, all of Discrete Mathematics/Set Theory):**

| id | kind | label | n |
|---|---|---|---|
| discrete-mathematics-set | term | Set | 2 |
| discrete-mathematics-subset | term | Subset | 2 |
| discrete-mathematics-union | term | Union | 2 |
| discrete-mathematics-intersection | term | Intersection | 2 |
| discrete-mathematics-empty-set | term | Empty Set | 2 |
| discrete-mathematics-venn-diagram | term | Venn Diagram | 2 |
| discrete-mathematics-how-to-find-the-union-and-intersection-of-two-sets | how-to | How to find the union and intersection of two sets | 2 |
| discrete-mathematics-how-to-represent-a-set-relationship-using-a-venn-diagram | how-to | How to represent a set relationship using a Venn diagram | 2 |

**Already-covered skills it also exercises.** `discrete-mathematics-vertex` (n=5), `discrete-mathematics-edge` (n=4), `discrete-mathematics-graph-vertices-and-edges` (n=4) — the two contact lists are read off a real graph; `statistics-and-probability-outlier` (n=3) — one contact appears in an implausibly large number of both lists and has to be flagged as a likely data error, not a real super-spreader.

**Data feasibility: HIGH.** Named source I have checked and that `domains.json` already lists
`verified: LIVE` this project:
- Stanford SNAP `ego-Facebook` dataset (`https://snap.stanford.edu/data/ego-Facebook.html`) — real,
  freely downloadable per-node friend lists with labeled "circles," giving exactly two named
  people's real connection sets to compute union/intersection on.
Sources I am NOT confident about: a real, individually-identifiable public-health contact-tracing
dataset does not exist (correctly — it would be a privacy violation). The case must disclose,
explicitly as a Modeling Assumption, that it repurposes a real social-graph structure as a proxy
for an epidemiological contact network — this is standard practice in the field, but the disclosure
is load-bearing and must be in the open per SPEC §5.

**Sensitivity (SPEC §6).** Flag for facilitator: the case involves disease exposure and limited
testing capacity. Frame the stake as "contacts protected" not "cases missed" per SPEC §6's
protection-over-destruction guidance.

**Split risk.** None — 8 skills, one coherent deliverable (build both contact lists from the real
graph → Venn diagram → union/intersection counts → tests-per-kit ratio).

---

### C2 — The Kill Switch   ·   score 5.2   ·   tier T3

**Protagonist.** Devon Achebe, a social-platform integrity analyst who has to act before a
coordinated harassment campaign's next scheduled post, with a strict "no more than one account
action per incident without a second reviewer" policy limiting Option A.

**The dilemma.** A.) Suspend the single account with the highest betweenness centrality in the
campaign's real interaction graph — the account most posts are relayed through OR B.) leave every
account active but rate-limit (throttle) all of them by the same fixed amount.

**Primary metric.** Reduction in reachable downstream accounts per account actually penalized (a
ratio — suspending one account that turns out to be a weak relay looks the same in raw numbers as
suspending a true bottleneck, until it's normalized by penalty cost).

**Why it's close.** Removing the central account can look decisive, but if the graph has several
near-equally-central alternate relay paths, traffic just reroutes in one hop — the number of
surviving 2-hop paths after removal has to be *counted*, not guessed. Throttling everyone touches
more accounts (a policy cost) but degrades every path a little instead of betting the whole
intervention on one node being irreplaceable.

**Would close (4 skills, 2 how-to / 2 term, all of Statistics And Probability/Probability's
remaining thin skills):**

| id | kind | label | n |
|---|---|---|---|
| statistics-and-probability-independent-event | term | Independent Event | 2 |
| statistics-and-probability-permutation | term | Permutation | 2 |
| statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-permutation | how-to | How to determine the number of outcomes of a permutation | 2 |
| statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination | how-to | How to determine the number of outcomes of a combination | 2 |

**Already-covered skills it also exercises.** `statistics-and-probability-combination` (n=4) —
counting alternate bypass routes as unordered sets of relay hops; `discrete-mathematics-path` (n=4),
`discrete-mathematics-cycle` (n=4) — reading the interaction graph itself.

**Data feasibility: HIGH.** Named source: Stanford SNAP or Network Repository's real interaction/
retweet-style graphs (both `verified: LIVE` per `domains.json`) provide a real directed interaction
graph a student can compute betweenness on and enumerate remaining paths from directly; no
invented network structure needed.
Sources I am NOT confident about: a real, disclosed coordinated-harassment case study with public
data — none exists for privacy/policy reasons, so the "campaign" framing is a disclosed scenario
laid over a real, structurally authentic graph, not a real named incident.

**Sensitivity (SPEC §6).** One-line facilitator flag: harassment is the backdrop; keep the
Socratic discussion on the graph-structure trade-off, not on adjudicating real-world moderation
policy.

**Split risk.** None — 4 skills, one arc (compute centrality → remove node → enumerate surviving
paths as permutations/combinations of remaining edges → compare to uniform throttling).

---

### C3 — The Hub Choice   ·   score 3.6   ·   tier T2

**Protagonist.** Marcus Feld, a regional telecom infrastructure planner with budget for exactly one
new fiber link this fiscal year, choosing between two capital projects already costed out by
finance.

**The dilemma.** A.) Add a new direct link between two already-major hub cities (cuts travel time
for the busiest existing routes) OR B.) add a link connecting one hub to a currently-unserved
smaller city (adds a route that doesn't exist today). (Matches `domains.json` network-science's own
decision archetype #2.)

**Primary metric.** Minutes of aggregate route-time saved (or population newly connected) per
dollar of link cost.

**Why it's close.** The hub-to-hub link improves an already-good route by a small percentage but
touches the highest-volume traffic; the hub-to-unserved link creates a route from nothing, a much
bigger relative improvement for a much smaller population. Before costing either, Marcus's team has
to know how many total city-pairs a candidate hub set even creates — the raw feasibility count is a
real binomial-coefficient computation, not a rounding exercise.

**Would close (2 skills, 1 how-to / 1 term, both remaining thin Combinatorics skills):**

| id | kind | label | n |
|---|---|---|---|
| discrete-mathematics-binomial-coefficient | term | Binomial Coefficient | 2 |
| discrete-mathematics-how-to-compute-a-binomial-coefficient | how-to | How to compute a binomial coefficient | 2 |

**Already-covered skills it also exercises.** `discrete-mathematics-weighted-graph` (n=4),
`discrete-mathematics-how-to-find-the-shortest-path-between-two-vertices-in-a-weighted-graph` (n=4),
`discrete-mathematics-fundamental-counting-principle` (n=4) — computing shortest routes before and
after each candidate link.

**Data feasibility: HIGH.** Named source: BTS On-Time Performance / airport-pair data
(`https://www.transtats.bts.gov/ontime/`), already `verified: LIVE` in `domains.json`, gives a real
weighted route graph with real travel-time weights to compute shortest paths on before/after a new
edge.
Sources I am NOT confident about: real published capital cost per mile of fiber/route buildout for
a specific pair of cities — likely a disclosed Modeling Assumption using a public per-mile cost
range rather than a project-specific quote.

**Sensitivity (SPEC §6).** None required.

**Split risk.** None, but flagged as the thinnest concept here — only 2 new-coverage skills, so it
is a fine third pick, not a headline case on its own.

---

### C4 — The Fifty   ·   score 2.9   ·   tier T3

**Protagonist.** Priya Ostrowski again, wearing her other hat: same contact-tracing office, now
running the county's limited first-week vaccine allocation.

**The dilemma.** A.) Vaccinate the 50 highest-degree (most-connected) people in the real contact
network OR B.) vaccinate 50 people chosen at random from the same network.

**Primary metric.** Modeled secondary infections prevented per dose administered.

**Why it's close.** Targeted vaccination concentrates protection on people who could each infect
many others, but it requires already knowing the degree of every person in the network — real
contact-tracing offices rarely have that map complete in week one. Random vaccination needs no map
at all and is operationally instant, but "spends" doses on many low-degree people. The size of the
gap between the two strategies depends on how skewed (non-linear) the real network's degree
distribution actually is — a network that's nearly uniform makes the two strategies close; a
heavy-tailed one makes targeting dominate.

**Would close (4 skills, 1 how-to / 3 term, split across two groups plus one full Combinatorics
closure):**

| id | kind | label | n |
|---|---|---|---|
| discrete-mathematics-binomial-coefficient | term | Binomial Coefficient | 2 |
| discrete-mathematics-how-to-compute-a-binomial-coefficient | how-to | How to compute a binomial coefficient | 2 |
| statistics-and-probability-independent-event | term | Independent Event | 2 |
| statistics-and-probability-non-linear | term | Non-linear | 2 |

**Already-covered skills it also exercises.** `discrete-mathematics-vertex`/`edge` (degree
computation), `statistics-and-probability-how-to-create-a-histogram-given-a-set-of-data` (n=19,
plotting the degree distribution).

**Data feasibility: MEDIUM.** The network structure itself is HIGH (SNAP, verified LIVE), but the
concept's actual crux — how much better targeted vaccination performs than random, in real
epidemiological terms — rests on published network-immunization research I can name from memory
(Cohen, Havlin & ben-Avraham, "Efficient Immunization Strategies," Phys. Rev. Lett. 2003;
Pastor-Satorras & Vespignani, 2002) but did **not** fetch or confirm live this session. That is
exactly the "category exists, specific document unconfirmed" case the skill scores MEDIUM, not
HIGH. This is the concept most likely to need a disclosed Modeling Assumption for the
effectiveness gap if `case-research` can't pin a specific paper's numbers.

**Sensitivity (SPEC §6).** Facilitator flag: vaccination and infection are the backdrop; frame as
doses/protection, not casualty counts, per SPEC §6.

**Split risk.** None — but this concept and C1 share the same protagonist; if both are ever
written, give Priya a clearly different case name so the corpus doesn't read as a duplicate.

---

**Next step.** Approve a concept, then run `case-write` on it.
