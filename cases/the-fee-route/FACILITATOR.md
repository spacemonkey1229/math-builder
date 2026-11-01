# FACILITATOR.md — The Fee Route

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Fee Route · **Tier:** T3 (MS-core) · **Studio:** MS Adventure
**Standards:** Discrete Mathematics/Graph Theory — Graph (Vertices And Edges), Vertex, Edge, Path,
Cycle, Weighted Graph, and two "how to…" skills (shortest path, Euler path/circuit) — see
`case.json.standards[]` for exact ids.

**Status:** `case-research` complete (2026-09-09). All `{{NEEDS_SOURCE: ...}}` placeholders in
`case.md` are resolved — two real Visa rate-table figures are sourced (Appendix F, [S1]/[S2]), one
real Base-network fee figure is sourced ([S5]), three supplemental real sources inform two
assumptions' basis ([S3]/[S4]/[S6]), and the dispute-recovery share, average transaction value,
and fraud-incidence probability are disclosed Modeling Assumptions MA1/MA3/MA4, because no
publishable figure exists for any of them (MA2 is a disclosed assumption for an unused map edge).
`case.json.balance.margin_pct` is a real, computed **9.1%**. Everything below is the case of
record, not a placeholder.

**Sensitivity note (SPEC §6):** ordinary workplace pressure — a payments lead facing a same-day
migration deadline. No illness, death, or family hardship. Standard facilitator handling suffices.

## Argument for A — The Card Bridge

The Card Bridge's real strength is structural, not just numeric: two of its three cost components
are real, published Visa figures ([S1] 1.89% + $0.10 interchange, [S2] 0.14% assessment), not
authored guesses, and its chargeback/dispute-resolution process genuinely recovers most of a
disputed transaction's value (modeled at 80% recovered, MA1) — a real protection the Coin Rail
cannot offer by design. A's expected fraud/dispute loss works out to a small 0.18% of volume
precisely because that recourse exists. **A's real weakness is arithmetic**: at Fernbrook's small
$1.30 average transaction size, the interchange rate's flat $0.10 component alone is roughly 7.7%
of a single transaction — small-value, high-frequency transactions are exactly where a flat card
fee stops being a rounding error and starts being the dominant cost, which is the real, current
2026 industry dynamic this case is built on (Appendix F, [S7]).

## Argument for B — The Coin Rail

The Coin Rail's raw fee advantage is real and large: a $0.01 flat network fee [S5] plus a 0.05%
off-ramp fee (informed by [S6]), against the Card Bridge's 2.03% + $0.10. Its real, structural
weakness is total loss exposure: with zero dispute recourse, a fraud or dispute event costs
Fernbrook the *entire* transaction value, not a partial share — five times the Card Bridge's
expected loss rate under this case's own numbers (0.90% vs. 0.18%). **B's real case is that this
gap still isn't enough to erase its fee advantage**: even after weighting the full, unrecoverable
exposure, B retains more net revenue per $1,000 processed than A does (see "The margin" below).
That is a genuinely different, better-supported route to "switch to stablecoin" than the reflexive
"it's basically free" read a Hero might bring in cold.

## The margin — real numbers, and how fragile this case actually is

`case.json.balance.margin_pct` = **9.1%**, inside the SPEC §2 target 10–15% band's lower edge (and
the approved concept's own 8–15% target). The arithmetic, in full:

- **Card Bridge (A), path IB→CN→AQ→MB:** total fee % = 0.14% [S2] + 1.89% [S1] = 2.03%; flat fee
  $0.10/transaction at $1.30/transaction (MA3) = (1000 ÷ 1.30) × $0.10 = **$76.92 per $1,000**;
  expected loss % = 0.90% (MA4) × 20% (MA1) = 0.18%.
  Net revenue = 1000 × (1 − 0.0203 − 0.0018) − 76.92 = 977.90 − 76.92 = **$900.98**.
- **Coin Rail (B), path AW→ST→CU→MB:** total fee % = 0.05% (informed by [S6]); flat fee
  $0.01/transaction at $1.30/transaction = (1000 ÷ 1.30) × $0.01 = **$7.69 per $1,000**; expected
  loss % = 0.90% (MA4) × 100% (definitional, no recourse) = 0.90%.
  Net revenue = 1000 × (1 − 0.0005 − 0.0090) − 7.69 = 990.50 − 7.69 = **$982.81**.
- **Margin:** |982.81 − 900.98| ÷ 900.98 = **9.1%** (the loser's value is the denominator, per the
  corpus's standard margin formula).

**Under the case's current numbers, B (The Coin Rail) is the higher-net-revenue option** —
$982.81 against A's $900.98. This margin is a designed property of three authored Modeling
Assumptions (MA1, MA3, MA4's values), not a pure empirical finding — only [S1] (Visa interchange)
and [S5] (Base network fee) are used as real, directly sourced numeric edge weights; [S2] is a
real but aggregator-sourced figure.

**Why this matters for the facilitator, specifically:** this case turns out to be genuinely
*robust*, not fragile, and that is itself worth teaching. `sensitivity_model.py`'s ±50% flex sweep
of the three genuine Modeling Assumption dials (`loss_share_a`, `avg_txn_value`, `fraud_prob`)
found **no verdict flip and no breach of the SPEC §2 20% cap in either direction** — margins ranged
from 6.3% to 18.3% across all six flex points, but B (The Coin Rail) stayed the winner every time.
`fraud_prob` (MA4) moves the margin the least of the three in absolute terms (8.7%–9.5%) despite
being the one dial with no direct public benchmark behind it; `avg_txn_value` (MA3) moves the
margin the most (6.3%–18.3%), because it rescales both rails' flat-fee drag directly. **Do not
let a student who assumes "the numbers must be fragile because they're unsourced assumptions"
go unchallenged — the honest, tested finding here is the opposite: the Coin Rail's fee advantage
at this transaction size survives a ±50% swing in every genuine assumption in the case.** The
pedagogically interesting move is asking a student to explain *why* it's this robust (the raw fee
gap is simply large relative to the plausible range of fraud exposure), not to hunt for a flip
that the model does not produce.

## Five Socratic questions

1. The Coin Rail's listed fee (about 0.05% plus a penny) looks almost free next to the Card Bridge's 2.03% plus a dime — so why is the real gap between the two options only 9.1%, not the 20-to-1 gap the raw fees alone would suggest?
2. MA4 sets the fraud/dispute-incidence probability at 0.90% for both rails — no source measures this exact rate for AI-agent-initiated micro-transactions — so if the real rate were meaningfully higher than assumed, does the Coin Rail still come out ahead, and by how much does the margin actually move?
3. You found a cycle among four of the graph's vertices — what does that cycle actually tell Fernbrook about its settlement options, beyond the two it's choosing between this week?
4. You determined whether the settlement network has an Euler path, an Euler circuit, or neither — what would it mean, operationally, for Fernbrook's own network map if the answer had come out differently?
5. If the whole case rests on three separate authored assumptions (the dispute-recovery share, the average transaction size, the fraud-incidence rate) rather than three sourced facts, what would you need to see to trust MA1/MA3/MA4 more than you do right now, and does knowing the case's own margin is only 9.1% wide make that question more or less urgent?

## The trap

**A learner who compares the two rails' raw, listed fee percentages — 2.03% + $0.10 versus 0.05% +
$0.01 — and stops there will pick the Coin Rail as an overwhelming, lopsided winner, without ever
computing either rail's real expected fraud/dispute loss.** The whole point of this case is that
"no chargeback recourse" is not a footnote — it converts every fraud event into a full loss instead
of a mostly-recovered one, and *properly weighting* that exposure (not skipping it, and not
guessing at it) is what turns an apparent 20-to-1 fee advantage into a real, much narrower 9.1%
edge. A pitch that only compares the two fee schedules, or that mentions fraud risk in prose
without running the actual expected-value arithmetic in D4, has fallen into this trap even if it
reaches the same final recommendation (Option B) that the correct math also favors.

**A second, related trap:** a student who correctly draws the graph and computes D1–D3 can still
get D4 wrong by applying the wrong recovery share to the wrong rail — e.g., assuming the Card
Bridge also has zero recourse (treating both rails' expected loss as 0.90% of volume), or assuming
the Coin Rail somehow also recovers 80% of a disputed charge. Either swap produces a plausible-
looking dollar figure built from real numbers in the case, but silently erases the entire structural
difference between "recourse" and "no recourse" that the whole dilemma turns on. Watch for a D4
table where both rails show the same expected-loss percentage.

## Twist

Not built as a scripted mid-discussion reveal — the "twist" here is structural, and it is a
genuine, tested finding rather than a planted instability: **the assumption a Hero is most likely
to challenge (the 0.90% fraud-incidence probability, since it is the one Appendix D figure with no
direct public benchmark behind it) turns out NOT to flip the recommendation even at a ±50% swing —
the Coin Rail's raw fee advantage is simply too large at this case's transaction size to be
overcome by a plausible change to fraud risk alone.** Facilitators should treat the moment a
student expects fragility and instead discovers robustness — usually while working through
Socratic Question 2 — as the twist moment, and can manufacture it directly by asking Question 2 if
no student raises the challenge unprompted.

---

## Guide Notes — the anchor ladder (SPEC §7, anchor-ladder subsection)

### Intro

Frame the format: an AI agent has been quietly running thousands of tiny, automatic purchases over
the card network since launch, and today someone finally has to decide whether that should keep
being true.

### Launch

Read the Overview aloud. Stop at "The migration either happens tonight or it doesn't happen this
quarter." Ask the room: "Before you've seen a single number, which rail do you think should win —
the one with fraud protection, or the one that's basically free? Why?"

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "The Card Bridge or the Coin Rail — show of hands." Record the split. Most rooms
will split based on gut reaction to "no chargebacks" sounding either scary or irrelevant.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push the room past "which rail is cheaper" toward "which rail keeps more real, expected revenue
once you account for how differently each one actually handles a fraud event." Let the room sit
with the fact that the fraud-incidence rate (MA4) is not published anywhere for this exact
scenario — it is the case's own stated Modeling Assumption, not a fact anyone can look up.

### Anchor 3 — WHAT IS THE PROCESS?

Before touching Appendix B/C's numbers, get the room to state the actual comparison method out
loud: draw the settlement network as a weighted graph (D1), find the shortest path between two
vertices as a warm-up on the method itself (D2), check whether the network can be fully
edge-audited in one walk (D3), then weight each rail's real path cost by its own recovery share to
get an expected-net-revenue figure comparable across both rails (D4). Re-ask: "Is 'which rail's fee
is lower' still the right question?"

### Anchor 4 — WHAT DON'T WE KNOW?

Name the load-bearing unknown explicitly: nobody — not Visa, not Fernbrook, not this case — has
ever measured a real fraud/dispute-incidence rate for exactly "AI-agent-initiated, card-not-present
micro-transactions." "Is 0.90% a fact, or a stated, defensible guess? What would make a different
guess just as defensible?"

### Data Deep Dive

Now open Appendices A–D. Run D1–D5 as a room, or have groups report out. This is also the moment
to run Socratic Questions 3 and 4 (the cycle finding and the Euler determination).

### Twist

Once D4's numbers are on the table and a recommendation has started to form, run Socratic
Question 2 directly: "MA4's 0.90% is the one number in this case nobody actually measured. If the
real rate is higher, does your recommendation survive?" Let the room discover that the margin is
only 9.1% — much narrower than almost anyone will expect after seeing the raw fee schedules — and
then let them test it: even a defensible upward challenge to MA4 (tested at +50%) narrows the
margin to 8.7% but does not flip the recommendation, because the Coin Rail's raw fee advantage is
large enough at this transaction size to absorb it.

### Close

VOTE AGAIN. "Did the vote move? For the people who didn't move, what would it take to change your
mind — a different number, or a different assumption entirely?"

### Lessons Learned

The core transferable idea: a real protection (chargeback recourse) and a real cost (interchange
fees) both have to be converted into the same unit — expected dollars per $1,000 processed —
before they can be honestly compared; eyeballing either one alone, even from a real, sourced
figure, can point you the wrong way or make the gap look far bigger or smaller than it is. A
second, equally real lesson: a settlement network can hold real structure (a cycle, an Euler-audit
answer) that has nothing to do with either option currently on the table, and reading the full
graph, not just the two paths you already expect to use, is part of doing this kind of analysis
honestly.

### Standards Touched On

Graph (Vertices And Edges), Vertex, Edge, Path, Cycle, Weighted Graph; How to find the shortest
path between two vertices in a weighted graph; How to determine whether a graph has an Euler path
or circuit.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold read of the Overview, gut-check vote (Anchor 1) — no numbers shown yet |
| 3:00–8:00 | Position defense: "Convince us your rail wins, not just that it's cheaper or safer" |
| 8:00–20:00 | Data Deep Dive — draw the weighted graph (D1) and find the shortest path IB→CU (D2) as a room |
| 20:00–30:00 | Run the Euler-audit determination (D3); build D4's expected-net-revenue table; confirm the 9.1% margin and where it comes from |
| **30:00** | **DROP THE TWIST** — Socratic Question 2: MA4's 0.90% fraud-incidence rate is unmeasured; if the real rate is higher, does the recommendation survive? |
| 30:00–38:00 | Pressure-test MA4 directly: does a defensible challenge to the fraud rate, recovery share, or transaction size actually flip the verdict, or just move the margin? (Tested: it moves the margin, 6.3%-18.3%, but never flips it.) |
| 38:00–45:00 | Close, re-vote, the cycle and Euler findings' real-world meaning, lessons learned |

## Cohort bands (SPEC §7, cohort-bands subsection)

| Band | Typical size | What changes |
|---|---|---|
| **Full (12–20)** | the size this case is written for | Anchors and the 45-minute timed plan run as written above |
| **Compressed (6–11)** | smaller room | Anchors 2–3 combine into one pass; the 20:00–30:00 Euler-audit/expected-revenue build-out runs as a single worked example instead of small-group work; total runtime shortens proportionally |
| **1:1 / pair (1–2)** | tutoring context | No vote at Anchor 1 — ask for a stated initial position and why instead; the facilitator plays devil's advocate directly rather than cold-calling the room; the MA4 pressure-test (30:00–38:00) still runs in full, since it is the single most important move in the case |
