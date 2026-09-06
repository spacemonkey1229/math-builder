# Facilitator Guide — The Marginal Call

**Status:** post-research. All figures below are the value of record, matching
`case.json.balance`/`derived` and `sensitivity_model.py`. If any of these three ever disagree,
`sensitivity_model.py` is the arithmetic source of truth — fix the other two to match it.

**SPEC §6 flag:** this case touches money stress for a small business (a shop risking its biggest
order and a bank call it may not control) but no illness, death, or family hardship — one-line flag
for the discussion lead, not a heavier content warning.

---

## Argument for A — The Steady Order

The Steady Order is the standing batch size Renata's shop has always run: no new financing risk,
no dependence on a same-day bank approval, and no exposure to the mill's last slot getting bid away
by the national chain before the deposit clears. Its raw average cost per board foot ($18.50/bf) is
only 1.1% higher than The Full Kiln's ($18.30/bf) — but because all 2,000 of its board feet fit
inside Appendix C's 2,700 bf sellable limit, its net cost per board foot **sold** is also $18.50/bf:
no carrying-cost penalty at all. A is also the only option financeable entirely within the shop's
$25,000 credit-line headroom (Appendix D) — its $18,500 deposit fits with room to spare, with zero
dependence on a same-day bank call.

## Argument for B — The Full Kiln

The Full Kiln spreads the run's fixed setup cost over more board feet, genuinely lowering the raw
average cost to $18.30/bf — a real, correctly-computed result of D2's quotient-rule minimization,
not a trick. The flaw is that only 2,700 of its 3,000 board feet can be sold this quarter (Appendix
C); the other 300 sit as unsold inventory carrying a real cost. Once that carrying cost is folded in
and divided by board feet actually sold (D4), The Full Kiln's net cost climbs to $20.43/bf — 9.45%
higher than The Steady Order's $18.50/bf. B's deposit ($27,450) also exceeds the shop's $25,000
credit-line headroom by $2,450, requiring the same-day bank call to clear.

## The margin

**9.45%**, on the primary metric (net cost per board foot sold, D4) — The Steady Order is cheaper.
This sits inside the case's 8–15% target band and well inside SPEC §2's 20% cap. Note the two
different numbers in this case: the **raw** average-cost gap (D3) is only 1.1% and favors The Full
Kiln; the **real, graded** net-cost gap (D4) is 9.45% and favors The Steady Order. The gap between
those two numbers *is* the trap — see below. Full arithmetic: `sensitivity_model.py`,
`case.json.balance.margin_basis`, `case.json.derived`.

## The trap

A learner who computes A(x) = C(x)/x, finds x* via the quotient rule, and simply picks whichever of
The Steady Order or The Full Kiln is closer to x* — or picks The Full Kiln outright because its raw
average cost is lower — has done the calculus correctly and still reached the wrong real-world
answer, because they never checked D4: how many of The Full Kiln's board feet the hotel order and
the shop's standing accounts can actually absorb this quarter. If The Full Kiln's board footage
exceeds Appendix C's sellable limit, the unsold excess carries its own cost, and the *real* decision
metric is D4's net cost per board foot **sold**, not D3's raw average cost per board foot
**produced**. A confident learner who stops at D3 has fallen into exactly this trap.

## Five Socratic questions

1. Your D3 table says The Full Kiln has the lower raw average cost per board foot — so why might that not be the number that should decide this?
2. If the bank call doesn't clear before end of day, what happens to the deposit Renata already committed on The Full Kiln, and how does that change your pitch?
3. Appendix C caps how many board feet can actually be sold this quarter — what would have to be true about that number for The Full Kiln to stop being the better real-world choice?
4. Your D2 quotient-rule work found x*, the board footage that minimizes raw average cost — is x* itself one of the two options Renata is actually choosing between, and if not, what does it still tell you?
5. A classmate argues "bigger batch, lower cost per unit, obviously the Full Kiln" — using only your D4 numbers, what is the one sentence that proves them wrong?

---

## Guide Notes — the anchor ladder (SPEC's facilitator-artifacts section, anchor-ladder subsection)

### Intro

Frame the format: a real decision under a real deadline, and math is the only defensible way to argue either side.

### Launch

Read the Overview aloud. Stop before either tab gets touched. Ask the room: "Before you've seen a single number, would you lock in the bigger batch or the usual one — and why?"

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "The Steady Order or The Full Kiln — show of hands. Is anyone courageous enough to stand with The Full Kiln before you've seen the numbers?"

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push the room past "which batch is cheaper" toward "which batch is cheaper to actually sell." Let the confusion sit: "Wow, this is a harder question than it looked."

### Anchor 3 — WHAT IS THE PROCESS?

Get the room to state the method out loud before touching numbers: build the cost function, minimize average cost with the quotient rule, then check how much of each batch can actually be sold. Re-ask: "Is our question still the right question?"

### Anchor 4 — WHAT DON'T WE KNOW?

Name the load-bearing unknowns explicitly: the overtime cost coefficient (MA3) and, especially, how many board feet the hotel order and standing accounts can actually absorb this quarter (MA6). "Which of those assumptions is doing the most work?"

### Data Deep Dive

Now open Appendices A-D. Run D1-D5 as a room, or have groups report out. This is also the moment to run Socratic Questions 1 and 4 (the raw-average-cost trap and what x* does and does not tell you).

### Twist

Once D3's numbers are on the table and a recommendation has started to form, reveal that the mill just confirmed the competing national chain's bid for the same kiln slot came in higher than Renata's original Full Kiln offer. **State explicitly to the room: this repricing applies only to The Full Kiln's contested run — The Full Kiln is the larger, deep-discount slot the competitor is also bidding on; The Steady Order is the shop's own, uncontested standing order with this mill and is not affected.** (This explicit scoping was added 2026-09-05 after Tier 2 P4 found the case, as originally drafted, never stated which batch's cost the competing bid actually touched — a real ambiguity a student could reasonably resolve either way, which is exactly the kind of unstated convention this probe exists to catch.) `sensitivity_model.py`'s `evaluate_twist()` models this as a 50% jump in the fixed cost term (F: $1,800 to $2,700) applied ONLY to The Full Kiln's evaluation; recomputed, The Steady Order's net cost is unchanged at $18.50/bf and The Full Kiln's rises to $20.76/bf — The Steady Order still wins, and by a wider margin than before (10.9% vs. the original 9.45%). This does not make The Steady Order's original case any different; it raises the stakes of The Full Kiln's financing risk without changing which option the D4 math favors. Ask immediately: "What just broke in your model? Was your math wrong, or were you just missing information?"

### Close

VOTE AGAIN. "Did the vote move? What math was new to you, and how did you attack the quotient rule?"

### Lessons Learned

Average cost versus marginal cost, and net cost per unit sold versus raw cost per unit produced: a lower per-unit cost on paper is not the same as a lower real cost once you cannot sell everything you made.

### Standards Touched On

Derivative, Critical Point, Local Minimum; How to find a derivative using the power rule; How to use the quotient rule to differentiate a quotient of functions; How to find critical points of a function; How to use the first derivative test to classify a critical point; How to solve an optimization problem using derivatives; How to find the percent of a number.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote on A vs. B — no explanation |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just cheaper" |
| 10:00–15:00 | Pressure-test: "Whose plan collapses first if one assumption moves?" |
| **15:00** | **DROP THE TWIST** — the competing bid, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00–30:00 | Threaded deep conflict: (1) raw average cost vs. net cost per unit sold, (2) certainty (A) vs. optimized-but-fragile (B) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands (SPEC's facilitator-artifacts section, cohort-bands subsection)

| Band | Typical size | What changes |
|---|---|---|
| Full (12–20) | the size this case is authored for | Anchors and the 45-minute plan run as written |
| Compressed (6–11) | roughly half | Anchors 2–3 combine into one pass; the 20:00–30:00 deep-conflict step runs as a single thread (net cost vs. raw cost) instead of two; runtime shortens proportionally |
| 1:1 / pair (1–2) | one or two learners | no vote at Anchor 1 — a stated initial position instead; facilitator plays devil's advocate directly; the twist still drops but "who reverses" becomes "would you reverse, and why" |

## Sensitivity note

Six stated Modeling Assumptions carry this case (MA1, MA3–MA6, MA8; see `case.json` and Appendix
A–D's Modeling Assumptions block) — no public source publishes any of them for a specific mill or
shop. Tier 2 P5 (`sensitivity_model.py`, ±50% flex on every `FLEX[]` dial) found:

- **The sellable limit (MA6) is the load-bearing, dilemma-flipping dial.** At +50% (2,700 → 4,050
  bf), The Full Kiln's unsold-inventory penalty disappears entirely and the recommendation flips
  from The Steady Order to The Full Kiln — the raw average-cost advantage is all that's left. A
  Hero who argues the hotel/standing-account demand is understated is making exactly this move.
- The fixed cost (MA1), overtime coefficient (MA3), and both batch sizes (MA4, MA5) do **not** flip
  the verdict at ±50% individually.
- Also disclosed (Category F, not an independent instability): flexing The Steady Order's board
  footage (MA4) up 50% happens to land it exactly on The Full Kiln's stated 3,000 bf, producing a
  mechanical tie — a coincidence of the flex arithmetic at this specific percentage, not a
  generalizable fragility. See `case.json.sensitivity_disclosure`.
