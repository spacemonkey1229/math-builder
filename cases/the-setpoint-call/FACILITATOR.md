# Facilitator Guide — The Setpoint Call

**Status:** post-research. All figures below are the value of record, matching
`case.json.balance`/`derived` and `sensitivity_model.py`. If any of these three ever disagree,
`sensitivity_model.py` is the arithmetic source of truth — fix the other two to match it.

**SPEC §6 flag:** none required — this case touches a capital-spending decision and a real
machine-safety standard, but no illness, death, or family hardship.

---

## Argument for A — The Guarding Upgrade

The Guarding Upgrade genuinely lowers the theoretical cost per bottle: TC(r*) = $0.023767/bottle
at r* = 335.41 bpm, versus $0.025600/bottle at Line 3's current rated ceiling — a real,
correctly-computed result of D2's product-rule minimization, 7.7% cheaper on the calculus alone.
The flaw in stopping there is that reaching r* costs money: a $44,000 guarding/interlock retrofit
(MA6) must be amortized across the contract's 10,000,000-bottle volume (MA7), adding $0.0044 to
every bottle's true cost. Once that's folded in (D5), The Guarding Upgrade's real total cost is
$0.028167/bottle — 9.11% higher than The Rated Cap. A's case is real only if a Hero can show the
contract volume is understated, or argue the retrofit buys flexibility beyond this one contract.

## Argument for B — The Rated Cap

The Rated Cap requires no capital outlay and no dependence on the guarding contractor's single
install slot clearing before the contract's first production week. Its cost, $0.025600/bottle, is
simply TC(150) — fully computed today, with no assumption about future contract volume required.
Once Appendix C's amortized retrofit cost is folded into The Guarding Upgrade's total (D5), The
Rated Cap is the cheaper real path by 9.11%, even though the underlying calculus optimum (r*, D2)
is mathematically real and correctly found.

## The margin

**9.11%**, on the primary metric (total cost per bottle over the life of the contract, D5) — The
Rated Cap is cheaper. This sits inside the case's 8–15% target band and well inside SPEC §2's 20%
cap. Note the two different numbers in this case: the **theoretical** cost-per-bottle gap at the
calculus optimum versus the rated ceiling (D4) is 7.7% and favors The Guarding Upgrade; the
**real, graded** total-cost gap (D5) is 9.11% and favors The Rated Cap. The gap between those two
numbers *is* the trap — see below. Full arithmetic: `sensitivity_model.py`,
`case.json.balance.margin_basis`, `case.json.derived`.

## The trap

A learner who differentiates TC(r), finds r* via the product rule, and recommends "run at r*"
without ever checking Appendix B's rated safe-speed ceiling has done the calculus correctly and
still reached an unsafe, non-compliant, or economically incomplete answer — because r* is not
automatically a speed Line 3 is legally allowed to run at today. The real decision requires
comparing the FULL cost of reaching r* (the retrofit, amortized over the contract) against the
FULL cost of staying at the rated ceiling — not simply declaring "r* is cheaper per bottle" and
stopping there.

## Five Socratic questions

1. Your D2 work found r*, the speed that minimizes cost per bottle — is r* itself one of the two real choices Marisol is actually deciding between, and if not, what does it still tell you?
2. If the guarding contractor's one install slot before the contract's first production week is missed, what happens to The Guarding Upgrade as a real option?
3. Your D4 check compares r* against the rated ceiling — what would have to be true about the retrofit's cost, or the contract's volume, for The Guarding Upgrade to stop being the better real-world choice?
4. A classmate argues "the math says r* is cheaper, so obviously upgrade the guarding" — using only your D5 numbers, what is the one sentence that tests that claim?
5. Your D3 work used both the first derivative test and a concavity check on the same critical point — why bother with both, when either one alone would classify it as a minimum?

---

## Guide Notes — the anchor ladder (SPEC's facilitator-artifacts section, anchor-ladder subsection)

### Intro

Frame the format: a real capital-spending decision under a real safety ceiling, and calculus is
the only defensible way to find the number everyone is arguing about.

### Launch

Read the Overview aloud. Stop before either tab gets touched. Ask the room: "Before you've seen a
single number, would you pay for the guarding upgrade or hold the line where it is — and why?"

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "The Guarding Upgrade or The Rated Cap — show of hands. Is anyone courageous
enough to stand with the upgrade before you've seen a single dollar figure?"

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push the room past "which speed is cheaper" toward "which PATH is cheaper, once you count what it
costs to reach that speed." Let the confusion sit: "Wow, this is a harder question than it looked."

### Anchor 3 — WHAT IS THE PROCESS?

Get the room to state the method out loud before touching numbers: build TC(r) as a product of two
factors, differentiate with the product rule, find and classify the critical point, then check it
against the rated ceiling before ever comparing dollars. Re-ask: "Is our question still the right
question?"

### Anchor 4 — WHAT DON'T WE KNOW?

Name the load-bearing unknowns explicitly: Line 3's own rated speed ceiling (MA5, the case's
dilemma-flipping dial) and, especially, the contract's total bottle volume (MA7 — not
dilemma-flipping on its own, but the assumption a smaller-than-stated contract would hurt the
most). "Which of those assumptions is doing the most work?"

### Data Deep Dive

Now open Appendices A–C. Run D1–D6 as a room, or have groups report out. This is also the moment
to run Socratic Questions 1 and 5 (what r* does and doesn't tell you; why check both tests).

### Twist

Once D5's numbers are on the table and a recommendation has started to form, reveal that corporate
just confirmed the sports-drink brand exercised its volume-renewal option: the contract's total
bottle commitment on Line 3 **triples**, from 10,000,000 to 30,000,000 bottles. **State explicitly
to the room: this changes only how thinly The Guarding Upgrade's retrofit cost is spread — The
Rated Cap has no retrofit cost to amortize in the first place, so its $0.0256/bottle figure is
completely unaffected.** `sensitivity_model.py`'s `evaluate_twist()` models this as tripling Q for
Option A's evaluation only; recomputed, The Guarding Upgrade's total cost drops to $0.025233/bottle
while The Rated Cap stays at $0.025600/bottle — the recommendation **flips**, and by a thin margin
(1.43%). Ask immediately: "What just broke in your model? Was your math wrong, or were you just
missing information?"

### Close

VOTE AGAIN. "Did the vote move? What math was new to you, and how did you attack the product
rule?"

### Lessons Learned

The cost-minimizing answer to a calculus problem is not automatically the cost-minimizing answer
to the real decision: reaching a theoretical optimum can itself cost money, and that cost has to be
counted before the comparison is fair.

### Standards Touched On

Derivative, Critical Point, Concavity; How to find a derivative using the power rule; How to use
the product rule to differentiate a product of functions; How to find critical points of a
function; How to use the first derivative test to classify a critical point; How to solve an
optimization problem using derivatives; How to find the percent of a number.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote on A vs. B — no explanation |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just faster" |
| 10:00–15:00 | Pressure-test: "Whose plan collapses first if one assumption moves?" |
| **15:00** | **DROP THE TWIST** — new information, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00–30:00 | Threaded deep conflict: (1) theoretical optimum vs. legally/economically reachable optimum, (2) certainty (B) vs. optimized-but-capital-dependent (A) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands (SPEC's facilitator-artifacts section, cohort-bands subsection)

| Band | Typical size | What changes |
|---|---|---|
| Full (12–20) | the size this case is authored for | Anchors and the 45-minute plan run as written |
| Compressed (6–11) | roughly half | Anchors 2–3 combine into one pass; the 20:00–30:00 deep-conflict step runs as a single thread instead of two; runtime shortens proportionally |
| 1:1 / pair (1–2) | one or two learners | no vote at Anchor 1 — a stated initial position instead; facilitator plays devil's advocate directly; the twist still drops but "who reverses" becomes "would you reverse, and why" |

## Sensitivity note

Eight stated Modeling Assumptions carry this case (MA1–MA8; see `case.json` and Appendix A–C's
Modeling Assumptions block) — no public source publishes any of them for a specific bottling line
or a one-off safety retrofit. Tier 2 P5 (`sensitivity_model.py`, ±50% flex on every `FLEX[]` dial)
found:

- **Line 3's rated maximum safe speed (MA5) is the load-bearing, dilemma-flipping dial.** At -50%
  (150 → 75 bpm), the recommendation flips from The Rated Cap to The Guarding Upgrade (margin
  9.14%, now favoring A) — a more conservatively-guarded existing line makes paying for the
  retrofit worth it. +50% (150 → 225 bpm) does not flip it (margin widens to 14.08%, still
  favoring B).
- The incremental cost rate (MA3) and downstream handling time (MA4) do **not** flip the verdict
  at ±50% individually (margins stay in the 6–11% range).
- The retrofit cost (MA6) does not flip the verdict either, but at +50% the margin widens to
  15.70% — wide but still under SPEC §2's 20% cap.
- Also disclosed (Category F, a CAVEAT, not an independent instability): flexing the contract
  volume (MA7) down 50% (10M → 5M bottles) does not flip the verdict, but pushes the recomputed
  margin to 21.39% — past SPEC §2's 20% cap. A smaller contract makes The Rated Cap's advantage
  even larger, not smaller; the direction is unsurprising, but the resulting margin size is real.
  See `case.json.sensitivity_disclosure`.
