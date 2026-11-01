# FACILITATOR.md — The Sample Plan

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the end of case.md.*

**Case:** The Sample Plan · **Tier:** T3 (MS-stretch / HS-entry) · **Studio:** MS Adventure
**Standards:** Statistics And Probability — Population, Sample, Individual, Sample Size,
Systematic Sampling, Experiment, Random, Variability, Dot Plot, Probability, Event, Outcome, and
two "how to…" skills (single event, compound event), plus Advanced Numbers' percent-of-a-number
how-to (see `case.json.standards[]` for exact ids).

**Status:** `case-research` complete (2026-09-09). All `{{NEEDS_SOURCE: ...}}` placeholders in
`case.md` are resolved — the ANSI/ASQ Z1.4-2003 sample sizes (Appendix A/B) and the real
lot-contamination-occurrence rate and escape-cost range (Appendix C) are sourced and cited;
Appendix C's unit-level defect fraction (MA1) and the supplier-deviation-notice lot risk (MA2)
are disclosed Modeling Assumptions, because neither is publicly published anywhere.
`case.json.balance.margin_pct` is a real, computed **11.0%**. Everything below is the case of
record, not a placeholder.

**Sensitivity note (SPEC §6):** this case involves a real, if modest, workplace-safety stake (an
undetected quality escape reaching a customer's manufacturing line) but no illness, death, or
personal hardship to the protagonist — Renata's own stake is professional (her signature, her
shift's judgment), not medical or financial-personal. No sensitivity flag required.

## Argument for A — The Lean Draw

The Lean Draw's real, quantitative case is the D3 expected-cost math itself: at the sourced,
industry-wide baseline lot-occurrence rate (2.3%) and the case's stated unit-level defect-fraction
assumption (MA1, 2.5%), the smaller Level II sample's much lower certain destructive-testing cost
($12,500 vs. $20,000 — a real $7,500 gap) is **not** offset by its higher escape probability, once
that probability is correctly weighted by how rarely an average lot is actually bad in the first
place. A's expected total cost comes out lower than B's, by a real 11.0% margin — and this holds
across the ENTIRE possible range of MA1 (0% to 100%), not just a ±50% flex, verified by binary
search. This is the case's central rubric trap in reverse: a Hero who assumes "more samples must
be worth it" without weighting by the real, low baseline occurrence rate will overestimate The
Deep Draw's advantage.

## Argument for B — The Deep Draw

The Deep Draw's case is **not** a raw-expected-value argument against an average lot — under the
case's baseline numbers, it loses that argument. Its real strength is a targeted-risk argument
that becomes the mathematically CORRECT expected-value choice the moment Lot 4471 stops being an
average, randomly-selected lot: once a real, disclosed reason to suspect elevated risk exists (a
supplier deviation notice, MA2), the Deep Draw's better escape-probability performance is no
longer buying protection against a rare, industry-average risk — it is buying protection against a
meaningfully more likely event, and D4's own recomputed arithmetic shows the recommendation flips
to B, by a real 14.1% margin, at MA2's stated value. A Hero arguing for B honestly on the baseline
Challenge 2 pitch should frame it as a values-based "we'd rather over-inspect than under-inspect
when a customer's manufacturing run is riding on this" argument, not a cost argument — the cost
argument only becomes real once D4's scenario is on the table.

## The margin — real numbers

`case.json.balance.margin_pct` = **11.0%**, inside the concept brief's target 8–12% band. The
arithmetic, in full (see `sensitivity_model.py` for the exact reproducible computation):

- **Certain destructive-testing cost (Appendix A, sourced sample sizes [S1], assumed unit cost):**
  A = 50 × $250 = **$12,500.00**. B = 80 × $250 = **$20,000.00**.
- **Escape probability, using the c=0 rule [S2] and MA1 (2.5% defect fraction):**
  A: (1 − 0.025)^50 = **28.20%**. B: (1 − 0.025)^80 = **13.19%**.
- **Probability-weighted risk cost**, using Appendix C's sourced baseline lot-occurrence rate
  (2.3% [S3]) and the $1,400,000 cost-of-escape figure (chosen within [S3]'s real $1M–$2M range):
  A = 0.023 × 0.2820 × $1,400,000 = **$9,080.02**. B = 0.023 × 0.1319 × $1,400,000 = **$4,248.40**.
- **Expected total cost per lot:** A = $12,500.00 + $9,080.02 = **$21,580.02**.
  B = $20,000.00 + $4,248.40 = **$24,248.40**.
- **Margin:** |21,580.02 − 24,248.40| / 24,248.40 = **11.0%**.

**Under the case's current numbers, A (The Lean Draw) is the cheaper option in expectation.** This
mirrors `cases/deductible-roulette`'s own structural finding — the sourced, real-world figures (the
sample sizes, the baseline occurrence rate) carry the primary recommendation, and the case's one
PRIMARY-metric assumption (MA1) turns out not to be where the real fragility lives.

**Why this matters for the facilitator, specifically — and this has two DIFFERENT answers
depending on which question is being asked.** `sensitivity_model.py`'s binary search across the
FULL [0%, 100%] range of MA1 (not just ±50%) finds **no value of MA1 flips the PRIMARY
recommendation** — A wins at every fraction-defective value, because the fixed $7,500
destructive-testing cost gap is always large relative to what the escape-probability difference is
worth at the sourced 2.3% baseline occurrence rate. **Do not tell a Hero "the assumption never
matters" as a blanket statement — it is true for the primary, average-lot question and false for
the D4, flagged-lot question.** This distinction, not a single flat "it's robust" or "it's
fragile" answer, is the actual twist (below).

**But Challenge 3 (D4) and `sensitivity_model.py`'s `evaluate_twist()` ask a DIFFERENT, narrower
question — "if this specific lot has been flagged by a supplier deviation notice, does the
recommendation still hold?"** — and THAT metric is genuinely fragile, not to MA1, but to the
lot-occurrence probability itself. Once a real reason exists to suspect elevated risk for this one
lot, the sourced 2.3% population-average rate no longer applies, and the case's own MA2 (6%, a
deliberately moderate multiple of the baseline) both flips the recommendation to B AND is far more
than what's actually needed: a binary search finds the flip happens at a lot-occurrence probability
of only **~3.57%** — barely above the sourced 2.3% baseline, and well below MA2's own stated value.
A Hero (or a facilitator) who assumes MA2 has to be pushed hard to matter is wrong; it barely has
to move at all.

## Five Socratic questions

1. Your D3 calculation weights the escape cost by both a *sourced* population rate (2.3%) and a *stated assumption* (MA1) — which of those two numbers, if you doubled it, would change your recommendation? Try both before you answer.
2. Appendix C's MA1 (2.5% defect fraction) is a stated assumption, not a published number — if it were actually 50%, or even 100% (every out-of-spec lot is riddled with defects), would the recommendation change? Rerun D3 with that value before you answer.
3. You computed the escape probability by multiplying the same single-trial probability by itself n times — why does that repeated multiplication matter more than just subtracting the fraction defective from 100% once?
4. Appendix B shows that Alden's own quality system does not permit ANSI/ASQ Level I (an even smaller, cheaper sample) for this product family — why might a real quality system rule out the cheapest legal option before the math is even run?
5. If Lot 4471 had actually been flagged by a supplier deviation notice, would you still recommend the same sampling plan? Redo D3 under that scenario (Challenge 3 D4) before you answer.

## The trap

**A learner who assumes "the bigger sample must be worth its extra cost, because it obviously
catches more problems" — without ever weighting that improvement by how rarely an average lot is
actually bad — will land on The Deep Draw, and will be choosing the option that costs more in
expectation for a typical, unflagged lot.** This is the whole point of the case: a bigger sample
does not just multiply your protection, it multiplies your CERTAIN cost, and only the *expected*
value of the escape risk — a real, low base rate, times a real (if smaller than intuition
suggests) improvement in detection — belongs next to that certain cost. Only the correct route
(D1 through D3) reveals the real 11.0% margin favoring the smaller, cheaper sample.

**A second, more likely trap once a Hero has correctly built D1–D3:** assuming the escape
probability drops by roughly the same *ratio* as the sample size grows (a linear-scaling
assumption — sample size grows 1.6x, so "detection should improve about 1.6x too"). The real
relationship is exponential/multiplicative, not linear: going from n=50 to n=80 does not divide the
escape probability by 1.6, it divides it by about 2.1 (28.20% → 13.19%). A Hero who reasons
linearly will underestimate how much better The Deep Draw's detection really is — which matters
directly for D5's dot plot, whose whole purpose is to make that non-linear (diminishing-returns)
shape visible rather than assumed.

**A third trap:** substituting Appendix C's *cost of an undetected escape* ($1,400,000) for the
*per-unit destructive-testing cost* ($250) somewhere in the D3 arithmetic, or vice versa — i.e.
computing the certain inspection-cost term using the wrong dollar figure. This produces a
wildly-wrong total that a careless reader might not notice is off by several orders of magnitude,
specifically because both figures are real, cited dollar amounts that genuinely appear in the case.

## Twist

The twist is structural, not a scripted mid-discussion reveal, and it has **two parts a
facilitator must not collapse into one**:

**Part 1 — the primary recommendation is robust to the assumption a Hero is most likely to
challenge.** MA1 (the unit-level defect fraction) is the case's one clearly-labeled, clearly
unsourced Modeling Assumption, and most Heroes, on first seeing it, assume it must be the case's
weak spot. Run Socratic Question 2 as the first twist moment: have the room recompute D3 with MA1
pushed to 50%, then to 100%. The primary recommendation never flips — verified across the full
[0%, 100%] range. The lesson: a case's headline number can rest on one stated assumption without
that assumption being where the real uncertainty lives — here, the primary recommendation is
carried almost entirely by the sourced sample sizes and the sourced baseline occurrence rate.

**Part 2 — but the D4 scenario is NOT robust, and the fragile parameter is a DIFFERENT one than
the one everyone just finished stress-testing.** Once the room has convinced itself "the
assumption doesn't matter," push further with Challenge 3 (D4): "Lot 4471 has actually been
flagged by a supplier deviation notice — is your recommendation still the same?" Run the numbers
on `evaluate_twist()`, and let the room discover it flips from A to B — and that it flips at a
lot-occurrence probability barely above the sourced baseline (~3.57%, versus the sourced 2.3%),
not at some extreme value. MA1 (the 2.5% unit-level defect fraction) is held constant at its
baseline value throughout this D4 elevated-risk scenario — only the lot-occurrence probability
(MA2) moves; if a Hero asks whether MA1 changes too, the answer is no, and that is exactly why the
fragile lever in Part 2 is a genuinely different number from the one Part 1 already stress-tested.
**A Hero (or a facilitator) who generalizes Part 1's robustness finding
to Part 2 without checking is making exactly the kind of confident, plausible-but-wrong leap this
case exists to catch — and the fact that the fragile lever in Part 2 (the lot-occurrence
probability) is a completely different number than the one tested in Part 1 (MA1) is itself the
lesson.** "Robust to this assumption" is a claim about a specific metric and a specific parameter,
not a property of the case as a whole.

---

## Guide Notes — the anchor ladder (SPEC, anchor-ladder subsection)

### Intro

Frame the format: a batch-release screen, a truck waiting at the dock, two saved sampling plans,
one decision Renata has never had to defend out loud before.

### Launch

Read the Overview aloud. Stop at "'fast' and 'fully covered' are two different questions." Ask the
room: "Before you've seen a single number, which sampling plan do you think is actually the better
value over time — the faster one, or the more thorough one? Why?"

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "The Lean Draw or The Deep Draw — show of hands." Record the split. Most rooms
lean toward the more thorough sample before seeing any numbers — that instinct is exactly what
this case is built to test.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push the room past "which sample size sounds more careful" toward "which plan has the lower real
expected cost, once the actual chance of a bad lot is factored in." Let the room sit with the fact
that Appendix C's unit-level defect fraction is not published anywhere — it is the case's stated
Modeling Assumption, not a fact anyone can look up.

### Anchor 3 — WHAT IS THE PROCESS?

Before touching Appendix C's numbers, get the room to state the actual comparison method out loud:
identify the population/sample/individual/sample size for each plan (D1), compute the escape
probability for each (D2), then combine certain inspection cost with probability-weighted risk
cost to get a true expected cost (D3). Re-ask: "Is 'which sample size sounds more thorough' still
the right question?"

### Anchor 4 — WHAT DON'T WE KNOW?

Name the load-bearing unknown explicitly: nobody has ever published what fraction of units inside
a bad lot are actually defective, or exactly how much a supplier deviation notice should raise a
specific lot's risk. "Are 2.5% and 6% facts, or stated, defensible guesses? What would make
different guesses just as defensible?"

### Data Deep Dive

Now open Appendices A–D. Run D1–D5 as a room, or have groups report out. This is also the moment
to run Socratic Questions 1 and 3 (the sourced-vs-assumed weighting and the compound-probability
mechanics).

### Twist

Once D3's numbers are on the table and a recommendation has started to form, run Socratic Question
2 directly: push the room to recompute D3 with MA1 doubled, then pushed to an extreme. Let the room
discover the margin barely moves and the winner never changes — then introduce the supplier
deviation notice (D4) and let the room discover THAT changes everything, at a much smaller push
than they just finished ruling out.

### Close

VOTE AGAIN. "Did the vote move? For the people who didn't move, what would it take to change your
mind — a different number, or different information about this specific lot?"

### Lessons Learned

The core transferable idea: an option that "feels more thorough" is not automatically the option
with the lower *expected* cost for a typical case — and testing whether the case's stated
assumption is actually the load-bearing one (it usually is not, here) is itself a real analytical
skill, distinct from just plugging numbers into a formula. The second lesson: population-average
data does not automatically apply to a specific, flagged case — recognizing when to depart from a
baseline rate is a real, transferable judgment call.

### Standards Touched On

Population, Sample, Individual, Sample Size, Systematic Sampling, Experiment, Random, Variability,
Dot Plot, Probability, Event, Outcome; How to determine the probability of a single event; How to
determine the probability of a compound event; How to find the percent of a number.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold read of the Overview, gut-check vote (Anchor 1) — no numbers shown yet |
| 3:00–8:00 | Position defense: "Convince us your pick is the cheaper bet in expectation, not just the one that feels more careful" |
| 8:00–20:00 | Data Deep Dive — build D1's sampling-design table and D2's escape-probability calculation as a room |
| 20:00–30:00 | Build D3's full expected-cost comparison; confirm the 11.0% margin and where it comes from |
| **30:00** | **DROP THE TWIST** — Socratic Question 2: recompute D3 with MA1 doubled, then pushed to an extreme — does the recommendation survive? |
| 30:00–38:00 | Introduce the supplier deviation notice (D4): recompute, discover the flip, and discuss why the fragile number here is different from the one just pressure-tested |
| 38:00–45:00 | Close, re-vote, D5's dot plot exercise, lessons learned |

## Cohort bands (SPEC §7.4)

| Band | Typical size | What changes |
|---|---|---|
| **Full (12–20)** | the size this case is written for | Anchors and the 45-minute timed plan run as written above |
| **Compressed (6–11)** | smaller room | Anchors 2–3 combine into one pass; the 20:00–30:00 D3 build-out runs as a single worked example instead of small-group work; total runtime shortens proportionally |
| **1:1 / pair (1–2)** | tutoring context | No vote at Anchor 1 — ask for a stated initial position and why instead; the facilitator plays devil's advocate directly rather than cold-calling the room; the D4/Twist pressure-test still runs in full, since it is the single most important move in the case |
