# Concept sheet — Networks, Graphs & Social Structure (`network-science`), RE-RUN

**Why this file exists.** This supersedes (does not overwrite) `CONCEPTS_network-science_2026-09-12.md`,
written earlier this same session. That sheet's top pick, **C1 "The Overlap Call"** (target:
Discrete Mathematics / Set Theory, then 8/8 thin), is now a **dead end**: while this session was
mid-pipeline, a concurrent session published **Grant Reach** (2026-08-24) and **The Overlap Send**
(2026-09-06) — both targeting the exact same 8-skill Set Theory group with the exact same
union/intersection framing the old C1 proposed. Live-verified just now against
`readmodel/standards_spine.json`: all 8 Set Theory skills now read `n=2`, `covered_by: ["Grant
Reach", "The Overlap Send"]`. A third case there closes nothing new.

**This re-run found the damage is worse than one dead concept — all three old picks are dead.**
Re-verifying C2 and C3 live (not reused from memory, per instructions):

- **C2 "The Kill Switch"** targeted Statistics And Probability / Probability's 4 remaining thin
  skills (`independent-event`, `permutation`, both "number of outcomes" how-tos). Live spine check:
  `independent-event` → `n=2`, `covered_by: ["Wildfire", "Heist"]`. `permutation` and its how-to →
  `n=2`, `covered_by: ["Codebreaker", "The Placement Test"]`. `how-to-...-combination` → `n=2`,
  `covered_by: ["Codebreaker", "Archery Camp"]`. **All four already closed by two different
  concurrent-session case pairs.** Dead.
- **C3 "The Hub Choice"** targeted Discrete Mathematics / Combinatorics's 2 remaining thin skills
  (`binomial-coefficient` + its how-to). Live spine check: both → `n=2`,
  `covered_by: ["Pattern Rights", "Redrawing Lines"]`. Dead.
- **C4 "The Fifty"** mixed the now-dead Combinatorics pair with `independent-event` (also now dead,
  see C2 above) and `non-linear` (Displaying Data) — live check: `non-linear` → `n=2`,
  `covered_by: ["Rent Vs. Own", "Movie Executive"]`, dead too. C4 as constituted no longer closes
  anything live.

**Conclusion from the live re-pull: this is not bad luck on one pick, it is a spine-wide pattern.**
Every Discrete Mathematics group is now either fully saturated (Formal Logic and Graph Theory both
read `thin=0` — no skill in either group sits at `n≤2` any more) or thin-but-already-exactly-2x-covered
(Set Theory 8/8, Combinatorics's binomial pair, Proof And Recursion's induction trio — see below).
A fresh, live, whole-spine sweep (`readmodel/standards_spine.json`, run this session) found **zero
skills anywhere at `n==0`** — the corpus has no true zero-coverage gaps left at all (437/437 skills
at `n≥1`). Every "thin" (`n≤2`) skill in a network-science-relevant group that I checked is sitting
at exactly `n=2` with exactly two named covering cases — meaning concurrent sessions have been
racing the same `gap_queue.json` thin-convention list and have already doubled-up almost everything
reachable from Discrete Mathematics / Statistics And Probability. Genuinely **fresh** targets — a
skill still at `n=1`, one case away from being thickened past a single point of failure, not yet
raced — are rare and had to be found by a full skill-by-skill sweep, not by trusting the group-level
`gap_queue.json` summary (which flags `n≤2` without distinguishing "never touched" from "already
raced twice").

**What's still genuinely open for network-science** (live, verified just now): exactly two `n=1`
skills fall inside this domain's stated math branches (`prob-stats`) — `statistics-and-probability-how-to-find-a-missing-data-element-given-the-mean-and-the-remaining-`
and `statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data`, both
singly-covered by the same legacy case (`LeBron Vs. Michael`) — plus, once I widened the search
outside the domain's four *stated* math branches to any group a network story can *honestly* reach,
three `n=1` terms in Number Sense / Numbers And Counting (`even`, `odd`, `digit` — each covered by
exactly one case, none of them each other's case) that map cleanly onto a real, textbook network-
engineering topic: parity/checksum error-detection, which genuinely uses even/odd digit-sum
classification. Below are 4 ranked concepts built from what's actually still open, plus one
transparently-flagged low-priority option built on an already-2x-saturated group (included for
completeness, not recommended).

| # | Concept | Score | Tier | Group(s) touched | Status |
|---|---|---|---|---|---|
| C1 | The Parity Check | **3.8** | T2 | Number Sense / Numbers And Counting (3/3 remaining thin, fully closed) | fresh, n=1→2 on all three |
| C2 | The Missing Hub | **2.0** | T3 | Statistics And Probability / Data Analysis + Displaying Data (2 skills, both n=1) | fresh, n=1→2 |
| C3 | The Route That Can't Repeat | **1.2** | T2 | Number Sense / Numbers And Counting (2 of the 3, no full closure) | fresh, n=1→2, weaker closure than C1 |
| C4 | The Redundant Link | **1.6** | T3 | Discrete Mathematics / Proof And Recursion (3 skills, already n=2) | **NOT RECOMMENDED** — already 2x-covered, see note |

**Recommendation.** Write **C1, The Parity Check**, first. It is the only concept in this batch
that closes every remaining live gap in a spine group (`even`, `odd`, `digit` — Numbers And
Counting's full remaining-thin set, all currently `n=1`, none previously claimed by any concurrent
session I can find in `covered_by`), it maps onto a real, textbook network-engineering topic
(parity-bit / checksum error detection — genuinely uses even/odd digit-sum classification, not a
forced vocabulary stretch), and its core overhead fact (IEEE 802.11's 4-byte CRC-32 frame check
sequence) is spot-checked live this session against a real, current source. **C2** is a solid,
low-risk second pick — small (2 skills) but genuine, thickens two skills sitting at a fragile
single point of failure, and pairs naturally with the domain's own real SNAP data. **C3** is a
fine, even lower-effort third pick (reuses two of C1's three target skills without needing
`digit`) — hold it if C1 is written, since writing both would double-claim `even`/`odd`. **C4 is
included only for transparency and is not recommended**: live-verifying it turned up the same
already-raced pattern that killed the *entire* previous sheet, so proposing it now would risk
repeating this run's own lesson. I list it so the human reviewer can see it was checked and
rejected, not silently dropped.

---

### C1 — The Parity Check   ·   score 3.8   ·   tier T2

**Protagonist.** Renata Kuo, a network reliability engineer at a small satellite-IoT operator,
responsible for choosing the error-detection scheme for a new low-power sensor uplink before a
firmware freeze next week. Personally at stake: she has to defend the choice to the hardware team,
who own the battery budget her scheme eats into.

**The dilemma.** A.) Use a single even-parity bit appended to every byte of sensor data (cheap:
1 extra bit per 8 data bits, ~12.5% overhead) OR B.) use a 4-byte CRC-32 frame check sequence
appended once per whole packet, the same scheme IEEE 802.11 uses (costs more bits per packet but
catches far more error patterns than parity, which only ever catches an *odd* number of flipped
bits per byte and silently misses an even number).

**Primary metric.** Extra overhead bits transmitted per additional error pattern caught (a ratio —
raw overhead bytes make CRC look worse; raw error-catch rate makes CRC look obviously better; the
question is which scheme catches more *per bit spent*, and that depends on packet size, which
Renata's sensors can vary).

**Why it's close.** Parity is nearly free per byte but is *blind by construction* to any even
number of bit-flips in that byte — a real, provable gap, not a tuning choice. CRC-32 catches
essentially all realistic error bursts but its 4-byte tax is trivial on a large packet and
punishing on Renata's tiny sensor packets (some as small as 8–16 bytes), where it can be a third of
the transmission. The break-even packet size — where CRC's catch-rate advantage stops being worth
its fixed overhead — is a real number a student has to compute, not read off a chart.

**Would close (3 skills, 0 how-to / 3 term, all of Number Sense/Numbers And Counting's remaining
thin skills):**

| id | kind | label | n |
|---|---|---|---|
| number-sense-even | term | Even | 1 |
| number-sense-odd | term | Odd | 1 |
| number-sense-numbers-and-counting-digit | term | Digit | 1 |

**Already-covered skills it also exercises.** `number-sense-number` (n=25) — reading raw byte
values as numbers before classifying parity; `statistics-and-probability-probability` (n=17) — a
parity bit's blind spot is exactly "probability an even number of the byte's bits flip," which the
case has the student estimate from a stated per-bit error-rate assumption.

**Data feasibility: MEDIUM.** Named source I fetched and confirmed live this session: the IEEE
802.11 standard's Frame Check Sequence is a 4-byte CRC-32 appended per MAC frame — confirmed via a
live search returning matching, current technical sources (Intel FPGA documentation and a
ScienceDirect topic overview both describe the same 4-byte CRC-32 FCS field). That fixes Option B's
overhead figure at HIGH confidence. Option A's "1 bit per byte" parity overhead is standard,
decades-old UART/RS-232 practice and not seriously disputed, but I have not pinned one single
canonical spec document for it the way I have for 802.11's FCS — it needs a second source assembled
alongside the first, which is exactly the skill's MEDIUM criterion ("category of source exists...
may require assembling several"). Sources I am NOT confident about: a real, published per-bit error
rate for a *specific* commercial LPWAN/satellite-IoT sensor link — that number will most likely need
to be a disclosed Modeling Assumption (a stated, cited-as-typical LPWAN bit-error-rate range) rather
than one exact sourced figure.

**Sensitivity (SPEC §6).** None required.

**Split risk.** None — 3 skills, one coherent arc (byte → parity bit → even/odd blind spot →
packet-level CRC → break-even packet size).

---

### C2 — The Missing Hub   ·   score 2.0   ·   tier T3

**Protagonist.** Sam Iyer, a data analyst at a university's network-science lab, cleaning a
partially-corrupted export of a real social graph before a conference deadline. One node's degree
count was dropped in the export; the deadline doesn't allow re-scraping.

**The dilemma.** A.) Reconstruct the missing node's degree from the dataset's already-known mean
degree and the other 4,038 nodes' values (algebraic recovery — trusts the mean, which is sensitive
to the graph's few very-high-degree hub nodes) OR B.) drop the node entirely and re-report every
summary statistic on 4,038 nodes instead of 4,039 (loses one data point outright, but never risks
compounding an error onto a fragile hub-skewed mean).

**Primary metric.** Change in reported summary statistics (mean degree, and the box-and-whisker
plot's whisker/outlier boundaries) per node added or dropped — a ratio showing how much one node
can move the picture in a graph this hub-skewed.

**Why it's close.** Reconstructing from the mean is exact algebra and preserves the full node
count, but Sam doesn't know the true missing value is a hub or a leaf until *after* trusting the
mean-based answer — and if it's secretly a hub, the reconstruction is fabricating an especially
consequential number from an assumption. Dropping the node is honest about the uncertainty but
throws away real information and slightly shifts every other statistic. A box-and-whisker plot of
the degree distribution, built either way, is the deliverable that shows the reader exactly how
much the choice matters.

**Would close (2 skills, 2 how-to / 0 term, both currently n=1):**

| id | kind | label | n |
|---|---|---|---|
| statistics-and-probability-how-to-find-a-missing-data-element-given-the-mean-and-the-remaining- | how-to | How to find a missing data element given the mean and the remaining data | 1 |
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data | how-to | How to create a box-and-whisker plot given a set of data | 1 |

**Already-covered skills it also exercises.** `statistics-and-probability-outlier` (n=3) — the
graph's real hub nodes are legitimate high-degree outliers, not data errors, and the case has to
teach the difference; `statistics-and-probability-mean` (n=26) — the whole dilemma turns on how
much one value can move a hub-skewed mean.

**Data feasibility: HIGH.** Named source, fetched and confirmed live this session: Stanford SNAP's
`ego-Facebook` dataset (`https://snap.stanford.edu/data/ego-Facebook.html`) — confirmed live,
4,039 real anonymized nodes and 88,234 edges across 10 ego networks, with per-node degree directly
computable from the edge list. Sources I am NOT confident about: none load-bearing — the "missing
node" framing is a disclosed scenario device (a stated, in-the-open modeling choice: "for this case,
assume node X's row was lost in an export"), not a claim about a real corrupted file, and must be
labeled as such per SPEC §5.

**Sensitivity (SPEC §6).** None required.

**Split risk.** None, but flagged as the thinnest concept here — only 2 new-coverage skills, both
terms of a small local group (Data Analysis / Displaying Data each contribute one), so no group
bonus. A fine second pick, not a headline case alone.

---

### C3 — The Route That Can't Repeat   ·   score 1.2   ·   tier T2

**Protagonist.** Oren Vasquez, a metro fiber-network field technician tasked with inspecting every
physical cable segment in a neighborhood mesh network in one truck run, without re-driving any
segment twice if it can be avoided.

**The dilemma.** A.) Attempt the full inspection as one continuous route that never repeats an
edge (an Eulerian circuit) OR B.) accept that the network's junction points have the wrong mix of
even/odd connection counts, split the run into two trips, and repeat exactly the two segments
needed to make each trip's junctions balance.

**Primary metric.** Extra cable-miles driven (repeated segments) per junction that has odd degree
— because the classic real theorem here is exact: a connected network has a single
edge-non-repeating circuit if and only if every junction has an even number of connections; every
odd junction beyond the first two forces at least one repeated segment.

**Why it's close.** Option A is free if the network happens to qualify, but Oren doesn't know
until he's counted every junction's degree by hand from the real map — and if it doesn't qualify,
claiming it does wastes the whole day. Option B is always available and mechanically safe, but pre-
committing to two trips before checking costs a guaranteed extra trip even on networks that would
have qualified for one clean pass.

**Would close (2 skills, 0 how-to / 2 term, 2 of the 3 remaining Numbers And Counting thin
skills — does not close `digit`, so no group bonus):**

| id | kind | label | n |
|---|---|---|---|
| number-sense-even | term | Even | 1 |
| number-sense-odd | term | Odd | 1 |

**Already-covered skills it also exercises.** `discrete-mathematics-vertex` (n=5),
`discrete-mathematics-edge` (n=4), `discrete-mathematics-graph-vertices-and-edges` (n=4) — reading
the real mesh map as a graph and computing each vertex's degree.

**Data feasibility: HIGH.** Named source, fetched and confirmed live this session: OpenStreetMap
(`https://www.openstreetmap.org/`) — confirmed live, a real, freely-licensed source for extracting
an actual neighborhood road/utility layout as a node-and-edge graph for a named real town.
Sources I am NOT confident about: none load-bearing — degree parity is computed directly from the
extracted map, not sourced externally.

**Sensitivity (SPEC §6).** None required.

**Split risk.** Overlaps C1 on `even`/`odd` — **write at most one of C1 or C3**, not both, or the
corpus double-claims the same two skills in the same brainstorming round for no reason. Recommend
holding C3 if C1 is written; C3 is a fallback if C1's parity/checksum framing doesn't survive
`case-research`.

---

### C4 — The Redundant Link   ·   score 1.6   ·   tier T3   ·   **NOT RECOMMENDED**

**Protagonist.** A regional ISP's network-redundancy planner proving that a proposed backbone
topology keeps every city connected even if any single link fails, for every network size the
company might grow to — not just the one they have today.

**The dilemma.** A.) Prove by mathematical induction that a proposed "ring plus one cross-link"
topology stays fully connected after any single link failure, for a network of any size n OR B.)
skip the general proof and instead test failure-tolerance by brute-force simulation on the current
20-city network only, re-testing manually every time a city is added.

**Primary metric.** Engineering hours spent verifying failure-tolerance per city added to the
network (a ratio — the induction proof costs more up front but is a one-time cost; brute-force
testing is cheap once but repeats, and grows, with every expansion).

**Would close (3 skills, 1 how-to / 2 term):**

| id | kind | label | n |
|---|---|---|---|
| discrete-mathematics-mathematical-induction | term | Mathematical Induction | 2 |
| discrete-mathematics-inductive-step | term | Inductive Step | 2 |
| discrete-mathematics-how-to-prove-a-statement-using-mathematical-induction | how-to | How to prove a statement using mathematical induction | 2 |

**Why this is flagged, not recommended.** Live-verified against the spine just now: all three
skills already sit at `n=2`, `covered_by: ["Redrawing Lines", "Prove It Scales"]` — **already
closed by two concurrent-session cases**, the exact pattern that killed every concept in the
previous sheet. A third case here adds no new coverage under SPEC §4's `new_coverage[]` test
(which requires `n==0` *before* the case — impossible here, the skill hasn't been at 0 all
session) and duplicates ground `Prove It Scales` already covers with, plausibly, the same "prove
a network property holds for all n" framing. I kept it in this sheet only so the reviewer can see
it was checked, live, and rejected — not quietly dropped the way the first sheet's authors would
have had to guess about it.

**Data feasibility: HIGH.** Named source: Network Repository (`https://networkrepository.com/`) —
previously verified live per `domains.json`; a real backbone/ISP-style topology graph is a
plausible pull from it, but this is moot given the rejection above.

**Sensitivity (SPEC §6).** None required.

**Split risk.** N/A — not recommended for writing.

---

## A note on the spine's actual state (for whoever picks up this file next)

The spine-wide sweep this session found **no skill anywhere at `n==0`.** That is a materially
different situation than the one `case-brainstorm/SKILL.md`'s own worked example describes ("100 of
322 skills have zero coverage") — this corpus has since closed every true zero-coverage skill, and
`gap_queue.json`'s `n≤2` "thin" convention is now the *only* remaining signal, but it does not
distinguish a skill that has never been touched (`n=1`, one case, a real single point of failure)
from one two concurrent sessions have already raced to `n=2` in the time since the queue was last
regenerated. Anyone re-running this skill soon should sweep `covered_by[]` on every candidate skill,
not just its `n`, before committing to a target — that is the specific, mechanical check that would
have caught this session's dead end before three concept sheets were spent on it.

**Next step.** Approve a concept, then run `case-write` on it. If C1 and C3 are both under
consideration, resolve the `even`/`odd` overlap first — do not approve both in the same batch.
