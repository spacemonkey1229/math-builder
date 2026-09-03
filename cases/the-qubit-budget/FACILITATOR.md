# FACILITATOR.md — The Qubit Budget

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Qubit Budget · **Tier:** T2 (MS-core) · **Studio:** Frontier
**Standards:** Advanced Operations / Exponents — Exponent (also Power), Base, How to evaluate an
exponential expression, How to evaluate an expression with multiple operations with exponents
(Order Of Operations) (see `case.json.standards[]` for exact ids).

**Status:** `case-research` complete (2026-09-01) — all 10 `{{NEEDS_SOURCE}}` tokens closed (6
SOURCED, 4 ASSUMPTION, 0 DROPPED, 0 OPEN; see `RESEARCH_LOG.md`). `case.json.status` is
`"researched"`. `margin_pct` is `16.98` (see the Balance section below). Not yet run through
`case-qa`; treat the numbers as sourced-and-computed but not yet QA-adjudicated.

## Real-world grounding (for the facilitator's own background, not for case.md)

- **Amazon Braket** (`aws.amazon.com/braket/pricing`) is a real cloud quantum-computing
  marketplace; IonQ Forte is a real, currently-offered trapped-ion QPU on it, priced at
  $0.08/shot + $0.30/task. This case's entire cost side is anchored to this one real, live rate
  card.
- **Chen et al. (IonQ), "Benchmarking a trapped-ion quantum computer with 30 qubits"**
  (arXiv:2308.05071) is the real academic paper behind Appendix D. It reports a median two-qubit
  gate error rate of 0.464% on IonQ Forte, and states that application-oriented circuits at width
  ≈20 qubits sustain up to ≈200 two-qubit gates before their fidelity drops below the 1/e
  threshold IonQ uses to define its own "Algorithmic Qubits" (#AQ) metric. The paper's own real
  application-circuit examples (phase estimation, amplitude estimation) show gate counts that do
  *not* follow a simple n² rule — this is the real basis for choosing the case's calibrated linear
  gate-count model over IonQ's own n² worst-case formula. A facilitator fielding "why not just use
  n²?" should be ready to point at this — both choices are defensible, they just tell very
  different stories about how close the race is (see Balance).
- **IBM Quantum's own pricing page** (`ibm.com/quantum/products`) bills by QPU *time*, not by shot
  ($96/minute, billed per second) — a genuinely different billing philosophy from Braket's
  per-shot model. This is real, useful color for why "dollars per shot" is even a coherent
  cross-provider yardstick on Braket specifically, and it's worth one sentence in the Intro.

## Intro

Frame the format: this is a real budget-committee register-size decision, not a worksheet. Name
the opener — "You have to recommend a qubit count to a room that includes the CFO, and the
CFO doesn't care about qubits, she cares about the number that comes out of the cost model behind
you." Mention, once, that cloud-quantum billing is genuinely how real companies without their own
hardware access quantum compute today (Amazon Braket, IBM Quantum) — this is a real cost
structure, not an invented one for the case.

## Launch

Show the two boxes exactly as the Overview describes them — no numbers yet, just "20 qubits" and
"24 qubits," and the one-line fact that 24 qubits represents the client's problem exactly and 20
doesn't. Ask: "Which one would you commit to, just from what you see here?" Do not confirm or
correct. Most rooms will split toward "of course you'd pay more to get it right" — record the
split, Close will re-ask it.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the cheaper register — the one that can't even
represent the whole problem?" Show of hands, both options, no discussion yet. Record the count.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'represents the problem exactly'?"**

Let confusion grow here on purpose. Heroes will want to jump straight to "which one is cheaper,"
but push on what "exact" is actually buying the client: "If the 20-qubit register's classical
fallback heuristic gets those last 4 lanes right almost every time anyway, does the 24-qubit
register's exactness matter at all? What would have to be true about the client's routing problem
for that exactness to actually change the answer they get?" If the room lands on "we don't
actually know how good the fallback heuristic is — that's exactly the thing nobody costed," the
case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "which one is cheaper per shot" from "which one actually solves the whole
problem," ask them to name the actual steps before touching the appendices: compute the two state
spaces and their ratio (D1); figure out how many two-qubit gates a real circuit needs at each
width (D2); turn a per-gate error rate into a whole-circuit success probability (D3); turn a
success probability into a real dollar figure per successful shot (D4); and decide, using all of
that plus the uncosted fallback-heuristic risk, which register to commit to (D5). Re-ask: "Is our
question still the right one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gap honestly: the client's routing problem, Latticeworks' actual budget ceiling,
and what the classical fallback heuristic even is are all fictional scenario detail — none of
that can be independently verified, because Latticeworks is fictional. What *can* be verified is
the real per-shot pricing (Appendix B/C) and the real per-gate error rate (Appendix D) — both come
from live, named, currently-operating sources. Ask which of the open figures is actually
load-bearing for the recommendation. The honest answer: the gate-count-vs-qubit-count *scaling
model* (MA5 — how many two-qubit gates a real circuit needs at a given width) is the single most
load-bearing open item in the whole case — it is the modeling choice that decides whether the two
options are 17% apart or 56% apart, without changing which one wins.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's state-space ratio, D2's gate counts, D3's success
probabilities, and D4's cost-per-successful-shot table together as a room, cold-calling for D4
specifically — this is where a Hero who computed D3 correctly but never divides price by
probability the right way round will visibly struggle to explain why a *smaller* success
probability produces a *bigger* dollar figure.

**Facilitator-only arithmetic check (do not read this number out until D4 has been worked
live):** cost(20) ≈ $0.2028/successful shot, cost(24) ≈ $0.2443/successful shot, margin ≈ 17.0%.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses: "One more real number. IonQ's own benchmark paper — the same one
your Appendix D numbers come from — says something else: their published gate-count model, the
one *they* use to certify a circuit width as 'working,' isn't the simple one this case gave you.
It's not 10 gates per qubit. It's qubits, squared."

"If you recompute D2 through D4 using qubit-count-squared instead of the model in Appendix D —
200 gates at 20 qubits becomes 400, and 240 gates at 24 qubits becomes 576 — does Option A still
win? By how much? And does that change what you'd tell the CFO — not which box to pick, but how
confident you'd sound saying it?"

**Facilitator-only: what this does and doesn't change.** Both models are real modeling choices
consistent with S2 — this is not new data revealing a hidden number, it's a real, disclosed
second interpretation of the *same* source. Under the n² model, Option A still wins — but the
margin jumps from ≈17.0% to ≈55.9% (`case.json.balance.margin_note`). A Hero who says "the answer
doesn't change" is right about the winner and wrong about the confidence — a 17% race and a 56%
race are not the same claim to make in a budget meeting, even when they point the same direction.

## Deep conflict — threads (20–30 min)

1. **A cheaper successful shot is not the same as a cheaper correct answer.** D4's numbers are
   real and honestly computed, but they only price *quantum* shots — the 20-qubit option's 4
   uncovered lanes are handled by an un-costed classical heuristic that appears nowhere in the
   dollar figures. Push: "If you had to put a number on the fallback heuristic's own error rate,
   how would that change your recommendation — and what does it tell you that the 'cheaper'
   option's biggest risk isn't in Appendix E at all?"
2. **The price on the vendor's rate card never decides this.** Per-shot price is identical for
   both options and cancels completely out of the margin — a cheaper or pricier cloud-compute
   vendor changes the dollar figures in Appendix E but never the winner. Push: "If Latticeworks
   switched providers tomorrow to one that charged half as much per shot, would today's
   recommendation change at all? What does that tell you about what this decision is actually
   about?"
3. **Two defensible models, two different stories about how close this is.** The linear model
   (Appendix D) and IonQ's own n² model (the twist) agree on the winner and disagree by more than
   3x on the margin. Push: "Is 'which option wins' the only number that matters in a real budget
   meeting, or does 'how close was it' change what you'd be willing to bet on that answer?"

## The trap

Heroes will treat "24 qubits is exact, 20 isn't" as settling the question by itself — voting for
Option B without ever pricing what that exactness costs per successful shot, or conversely will
treat "Option A is cheaper" as settling it the other way, without ever pricing what the 20-qubit
register's classical fallback heuristic is quietly *not* guaranteeing. A second, related trap:
assuming a different or cheaper cloud-compute vendor could flip the recommendation — missing that
per-shot price is identical for both options in this case and cancels out of the margin
arithmetic entirely, so the vendor's rate card is never actually the lever.

## 45-Minute Socratic Plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch (Intro/Launch), 30-second commitments, stand/sit vote (Anchor 1) — no explanation. |
| 3:00–10:00 | Position defense: "Convince us the cheaper register is still the right call — or isn't" (Anchor 2). |
| 10:00–15:00 | Pressure-test the models: process and open assumptions (Anchors 3–4) — name D1-D5, surface which figures are real vs. modeled. |
| 15:00–25:00 | Data Deep Dive — D1-D5 together; cold-call the D4 cost-per-successful-shot table specifically. |
| **25:00** | **DROP THE TWIST** — the real n² gate-count model reveal, delivered slowly. |
| 25:00–30:00 | Immediate recommit: who reverses? "What just changed — the winner, or your confidence in it?" |
| 30:00–40:00 | Threaded deep conflict — see below. |
| 40:00–45:00 | Close, re-vote, reflection, Lessons Learned. |

## Socratic questions

1. Your D4 table shows Option A costing less per successfully-completed shot. Does that number, by itself, tell you Option A is the better choice for the client? What is it not accounting for?
2. The per-shot price is exactly the same for both options — and yet Appendix E shows two different dollar-per-successful-shot figures. Where does that difference actually come from, if not from the price?
3. The twist gave you a second, real, sourced way to count two-qubit gates that changes the margin from ~17% to ~56% without changing who wins. If both models are defensible, how do you decide which one to put in your recommendation memo — or do you present both?
4. If the client's routing problem only had 20 decision variables instead of 24, would this still be a hard decision? What does that tell you about which fact is actually driving the dilemma — the register size, or the fact that the register size doesn't match the problem size?
5. Appendix A never states a specific dollar figure for the fallback heuristic's own error cost. If you had to estimate one before recommending Option A, what would you need to know, and how would a bad estimate there change your D5 memo?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare to Anchor 1's vote — a room that moves after the
twist should be pressed to explain the move using D3/D4, not just the twist's rhetorical weight.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

## Standards Touched On

Exponent (also Power) · Base · How to evaluate an exponential expression · How to evaluate an
expression with multiple operations with exponents (Order Of Operations)

## Balance argument (SPEC §2)

**Argument for A (the Near-Term Register).** At IonQ Forte's real, published median two-qubit
gate error rate (0.464%, S2), the smaller circuit width means fewer two-qubit gates under the
case's calibrated model (200 vs. 240), a higher below-threshold success probability (0.3945 vs.
0.3275), and a genuinely lower, real, sourced dollars-per-successful-shot figure ($0.2028 vs.
$0.2443) — a real 17.0% margin. It also comfortably fits this quarter's budget.

**Argument for B (the Full Register).** The Near-Term Register's cheaper successful shots only
solve 20 of the client's 24 decision variables — the remaining 4 lanes go to an un-costed
classical fallback heuristic that appears nowhere in D4's dollar figures. A cheaper wrong-shaped
answer is not obviously a better deal on a client contract than a costlier exactly-shaped one, and
the 24-qubit register's exactness is a structural guarantee the 20-qubit register cannot offer at
any price.

**Margin — COMPUTED 2026-09-01 (case-research).** `margin_pct: 16.98`. **Winner (on the raw D4
numbers): Option A, The Near-Term Register.** Comfortably inside SPEC §2's ~20% cap — no retune or
waiver was needed. Full arithmetic trail: `case.json.balance.margin_note`.

**Model-sensitivity finding, disclosed and not hidden.** The margin is real but model-dependent:
this case's calibrated linear gate-count model (MA5, matched exactly to S2's own stated real
anchor) gives 17.0%; the alternative, equally real IonQ #AQ n² worst-case formula gives 55.9%
instead (same winner, much less close race). This is exactly what the Twist is built around —
two defensible readings of the *same* real source that agree on direction and disagree sharply on
confidence.

**What this means for facilitation.** The room's real work is not just "which option wins" — the
case is built so both live models point the same direction. The sharper discussion is: (1) whether
D4's dollar figures actually settle the question at all, given the uncosted fallback-heuristic
risk under Option A (`argument_a`/`argument_b`), and (2) what it means to recommend a number when
two defensible ways of computing it disagree by more than 3x on how close the race is, even while
agreeing on the winner.

## Facilitator note — sensitivity (SPEC §6)

NONE. This is routine quantum-computing cost/error-rate math for a fictional client and company —
no subject-matter sensitivity flag applies.
