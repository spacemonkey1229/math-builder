# FACILITATOR.md — Deductible Roulette

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the end of case.md.*

**Case:** Deductible Roulette · **Tier:** T3 (MS-stretch / HS-entry) · **Studio:** MS Adventure
**Standards:** Statistics And Probability — Probability, Event, Outcome, Dependent Event,
Conditional Probability, and three "how to…" skills (single event, compound event, conditional
events), plus Advanced Numbers' percent-of-a-number how-to (see `case.json.standards[]` for exact
ids).

**Status:** `case-research` complete (2026-09-04). All `{{NEEDS_SOURCE: ...}}` placeholders in
`case.md` are resolved — two real sourced figures cover Appendix A's premiums and Appendix B's
claim frequency/severity (Appendix E), and Appendix C's repeat-claim probability is a disclosed
Modeling Assumption (MA1), not a sourced figure, because no general-population schedule exists.
`case.json.balance.margin_pct` is a real, computed **10.3%**. Everything below is the case of
record, not a placeholder.

**Sensitivity note (SPEC §6):** this case touches ordinary money stress — a young single-income
worker (a pharmacy technician, 2 years into managing her own budget) making a recurring insurance
decision. No illness, death, or family hardship beyond ordinary budget pressure.

## Argument for A — The Guarded Lane

Option A's real strength is not a dollar argument — it is a **variance-reduction argument**: the
$500 deductible caps Priya's single-claim exposure at half of what The Long Shot would charge her,
which matters for a driver with no cash cushion, independent of which option wins on raw expected
value. **Under the case's own current numbers, A does not win on raw three-year expected cost**
(see "The margin" below) — its case has to be made on cash-flow risk tolerance, not on the
math alone, and a Hero arguing for A honestly should say so rather than disputing D3's arithmetic.

## Argument for B — The Long Shot

B's real, quantitative case is D3's full three-year expected-cost calculation, correctly weighted
by branch probability: once Appendix B's real 4.9% baseline collision-claim frequency is properly
applied across all three years — including the branch where a first claim raises the probability
of a second one (Appendix C/MA1) — The Long Shot's three-year expected total cost comes out
**lower** than The Guarded Lane's, by a real 10.3% margin. This is the case's central rubric trap:
a Hero who picks the lower deductible by default, on the instinct that it "feels safer," is
choosing the option that costs more in the large majority of realistic three-year outcomes, because
the deductible is only ever paid if a claim actually happens, and it usually does not (Appendix B's
own 4.9% baseline says so directly).

## The margin — real numbers

`case.json.balance.margin_pct` = **10.3%**, inside the concept brief's target 8-12% band. The
arithmetic, in full (see `sensitivity_model.py` for the exact reproducible computation):

- **Three-year premium totals (Appendix A, sourced [S1]):** A = $7,914.00. B = $7,008.00.
- **Expected deductible-payment weight, three years, using the branch structure** (Year N's
  probability = "still clean" weight × 4.9% baseline + "already claimed" weight × 20% MA1 rate):
  - Year 1: 0.0490
  - Year 2: (1−0.049)×0.049 + 0.049×0.20 = 0.0466 + 0.0098 = 0.0564
  - Year 3: (1−0.049)²×0.049 + [1−(1−0.049)²]×0.20 = 0.0443 + 0.0191 = 0.0634
  - Total weight: **0.1688**
- **Expected 3-year deductible payment:** A = 500 × 0.1688 = **$84.42**. B = 1,000 × 0.1688 =
  **$168.83**.
- **Three-year expected total cost:** A = 7,914.00 + 84.42 = **$7,998.42**. B = 7,008.00 + 168.83 =
  **$7,176.83**.
- **Margin:** |7,998.42 − 7,176.83| / 7,998.42 = **10.3%**.

**Under the case's current numbers, B is the cheaper option** — $7,176.83 against A's $7,998.42
over three years. Unlike `cases/the-deferred-repair`, this margin is built almost entirely from
**sourced, real-world figures** — Appendix A's premiums and Appendix B's claim frequency are both
cited numbers, not assumptions. MA1 (the 20% repeat-claim rate) is the case's one stated Modeling
Assumption, and it plays a smaller role here than a comparable assumption did in that sibling case.

**Why this matters for the facilitator, specifically — and this has two DIFFERENT answers
depending on which question is being asked, so read carefully.** `sensitivity_model.py`'s ±50%
sweep of MA1 (10% to 30%) moves the **primary three-year recommendation's** margin only from about
10.2% to 10.4% — essentially flat. Pushed all the way to a mechanically extreme 100% (every driver
who ever files one claim is certain to file a second one within the window), B *still* wins the
**primary, whole-window** comparison, at a reduced but real ~9.5% margin. **There is no value of
MA1 that flips the PRIMARY three-year recommendation** — confirmed by binary search across the
full [0%, 100%] range, not just the ±50% band. The reason is structural: in the primary metric,
MA1 only ever weights a fraction of the three-year window's probability mass (Year 1 can never be
"post-claim"), and it can never outweigh the fixed $906 three-year premium gap between the two
policies.

**But Challenge 3 (D4) and `sensitivity_model.py`'s `evaluate_twist()` ask a DIFFERENT, narrower
question — "if a claim already happened in Year 1, what should Priya do for the remaining two
years?" — and THAT metric is genuinely fragile to MA1.** Once a claim has already occurred, MA1
applies undiluted to both remaining years (there is no "still clean" branch left to dilute it), and
a binary search finds this narrower recommendation flips from B to A at MA1 ≈ **60.4%** — about 3x
the case's stated 20%, and a value the case's own MA1 basis note does not rule out as implausible
("not the high end of what the literature's subgroup-specific ratios could suggest"). **Do not tell
a Hero "MA1 never flips the recommendation" as a blanket statement — it is true for the primary,
whole-window question and false for the D4, already-claimed question.** This distinction, not a
single flat "it's robust" or "it's fragile" answer, is the actual twist (below).

## Five Socratic questions

1. Your D3 calculation weights each year's expected deductible payment by whether Priya is still "clean" or has already had a claim — why does that weighting matter more than just multiplying one flat probability by one flat deductible for all three years?
2. Appendix C's 20% repeat-claim rate is a stated assumption, not a published number — if that number were actually 40%, or even 80%, would the recommendation change? Rerun D3 with that value before you answer.
3. You computed the probability Priya stays claim-free through Year 1 AND Year 2 by multiplying, not adding — what would adding have gotten wrong, and by how much?
4. Appendix B lists real comprehensive-coverage claim data right next to the collision data this case actually uses — why doesn't the comprehensive data belong in your D3 calculation?
5. If you had already filed one claim in Year 1, would you still recommend the same policy for Years 2 and 3? Redo D3 for just the remaining two years under that condition (Challenge 3 D4) before you answer.

## The trap

**A learner who compares the two deductibles directly — "$500 is safer than $1,000, so pick the
lower one" — without ever weighting that comparison by how likely a claim actually is, will land
on The Guarded Lane, and will be choosing the option that costs more in the large majority of
realistic three-year outcomes.** This is the whole point of the case: a deductible is not a cost
you pay every year, it is a cost you pay *only if a claim happens*, and Appendix B's own 4.9%
baseline says that in a given year it usually does not. Only the *expected* value of the
deductible — probability times dollar amount — belongs next to the certain premium difference, and
only the correct route (D1 through D3) reveals the real 10.3% margin favoring the higher-deductible
option.

**A second, more likely trap once a Hero has correctly built D1–D3:** reusing D2's *compound*
"at least one claim across three years" probability (~14.0%) as if it were a single flat per-year
rate for D3's weighting, instead of using each year's own branch-conditional probability (Year 1:
4.9%; Year 2: a blend of 4.9% and 20% depending on branch; Year 3: a further blend). This produces
a plausible-looking but wrong dollar figure that conflates "probability of at least one claim ever"
(D2's job) with "expected cost in a specific year" (D3's job) — watch for a pitch whose D3 table
uses the same probability in all three rows.

**A third trap (Tier 2 P3 finding, added after adversarial review):** a student who correctly
sets up D3's probability-weighting structure can still get the dollar side of the calculation
wrong by substituting Appendix B's *average paid claim amount* ($5,992 for collision) for the
*deductible* in the expected-cost formula — i.e. computing (probability × $5,992) instead of
(probability × the policy's own $500 or $1,000 deductible). This produces a plausible-looking but
wildly inflated dollar figure built from a real number that genuinely appears in the case, and it
specifically requires the reader to correctly apply Appendix B's own modeling note ("Priya pays
the full deductible out of pocket; the insurer covers the remainder") rather than reflexively
reaching for the biggest cost-shaped number on the page. Watch for a pitch whose expected
out-of-pocket figures are in the thousands of dollars rather than the tens to low hundreds.

## Twist

The twist is structural, not a scripted mid-discussion reveal, and it has **two parts that a
facilitator must not collapse into one**:

**Part 1 — the primary recommendation is robust.** The assumption a Hero is most likely to
challenge (Appendix C's 20% repeat-claim rate) turns out NOT to be the case's fragile point for the
whole-window, three-year question, no matter how far it is pushed (verified across the full [0%,
100%] range, not just ±50%). Most Heroes, on first seeing a stated Modeling Assumption, assume it
must be the case's weak spot and attack it directly. Run Socratic Question 2 as the first twist
moment: have the room actually recompute D3 with MA1 doubled, then quadrupled, then pushed to 100%.
The primary recommendation never flips. The lesson: a case's headline number can rest on one stated
assumption without that assumption being where the real uncertainty lives — here, the primary
recommendation is carried almost entirely by the two *sourced* figures (the real premium gap and
the real baseline claim frequency).

**Part 2 — but the D4 scenario is NOT robust, and this is the part a facilitator must not skip.**
Once the room has convinced itself MA1 "doesn't matter," push further with Challenge 3 (D4): "if
Priya has already had a claim in Year 1, is your recommendation for Years 2 and 3 still the same?"
Run the numbers on `evaluate_twist()`'s remaining-years comparison, and let the room discover it
flips from B to A once MA1 is pushed to roughly 60% — a number only 3x the stated value, not the
mechanically extreme 100% that Part 1 required. **A Hero (or a facilitator) who generalizes Part
1's robustness finding to Part 2 without checking is making exactly the kind of confident,
plausible-but-wrong leap this case exists to catch.** The real, transferable lesson is that
"robust to this assumption" is a claim about a *specific* metric, not a property of the case as a
whole — the same input can be safely ignorable for one question and load-bearing for a different
one asked of the same numbers. This is the opposite failure mode from `the-deferred-repair`, where
a single stated assumption was uniformly the fragile lever for that case's one graded metric —
facilitators who have run that case recently should watch for themselves assuming a finding from
Part 1 here settles Part 2 as well.

---

## Guide Notes — the anchor ladder (SPEC, anchor-ladder subsection)

### Intro

Frame the format: two renewal quotes, one countdown banner, one decision Priya has
never had to make for herself before. This is a real personal-finance decision dressed as an
insurance-portal screenshot, not the other way around.

### Launch

Read the Overview aloud. Stop at "whether 'safer' and 'cheaper' are even pointing at
the same option this time." Ask the room: "Before you've seen a single number, which policy do
you think is actually cheaper over three years — the one with the lower deductible, or the one
with the lower premium? Why?"

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "The Guarded Lane or The Long Shot — show
of hands." Record the split. Most rooms lean toward the lower deductible before seeing any
numbers — that instinct is exactly what the case is built to test.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push the room past "which deductible amount
sounds scarier" toward "which policy has the lower real expected cost, once the actual chance of a
claim is factored in." Let the room sit with the fact that Appendix C's repeat-claim number is not
published anywhere — it is the case's stated Modeling Assumption, not a fact anyone can look up.

### Anchor 3 — WHAT IS THE PROCESS?

Before touching Appendix B's numbers, get the room to state
the actual comparison method out loud: build the branch-conditional probability table (D1),
compute the probability of staying claim-free through the window (D2), then weight each year's
deductible cost by the right branch probability to get a true three-year expected cost (D3).
Re-ask: "Now that we have a process, is 'which deductible feels bigger' still the right question?"

### Anchor 4 — WHAT DON'T WE KNOW?

Name the load-bearing unknown explicitly: nobody has ever
published a general-population probability that a driver who's already had one claim gets a
second one. "Is 20% a fact, or a stated, defensible guess? What would make a different guess just
as defensible?"

### Data Deep Dive

Now open Appendices A–D. Run D1–D5 as a room, or have groups report out.
This is also the moment to run Socratic Questions 1 and 3 (the branch-weighting logic and the
compound-probability mechanics).

### Twist

Once D3's numbers are on the table and a recommendation has started to form, run
Socratic Question 2 directly: push the room to recompute D3 with MA1 doubled, then pushed to an
extreme. Let the room discover that the margin barely moves (10.3% → roughly 9.5% even at the most
extreme possible assumption) — the opposite of what most rooms expect from "the case's only
assumption."

### Close

VOTE AGAIN. "Did the vote move? For the people who didn't move, what would it take to
change your mind — a different number, or a different kind of argument entirely (cash-flow risk,
not expected value)?"

### Lessons Learned

The core transferable idea: an option that "feels safer" because it caps
worst-case loss is not automatically the option with the lower *expected* cost — and testing
whether the case's one stated assumption is actually load-bearing (it usually is not, here) is
itself a real analytical skill, distinct from just plugging numbers into a formula.

### Standards Touched On

Probability, Event, Outcome, Dependent Event, Conditional Probability;
How to determine the probability of a single event; How to determine the probability of a compound
event; How to determine the probability of conditional events; How to find the percent of a
number.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold read of the Overview, gut-check vote (Anchor 1) — no numbers shown yet |
| 3:00–8:00 | Position defense: "Convince us your pick is the cheaper bet over three years, not just the one that feels safer" |
| 8:00–20:00 | Data Deep Dive — build D1's branch-conditional probability table and D2's compound probability as a room |
| 20:00–30:00 | Build D3's full three-year expected-cost comparison; confirm the 10.3% margin and where it comes from |
| **30:00** | **DROP THE TWIST** — Socratic Question 2: recompute D3 with MA1 doubled, then pushed to an extreme — does the recommendation survive? |
| 30:00–38:00 | Pressure-test MA1 directly: confirm the margin barely moves even at the most extreme defensible value, and discuss why (the fixed premium gap dominates) |
| 38:00–45:00 | Close, re-vote, D4's "what if a claim already happened" exercise, lessons learned |

## Cohort bands (SPEC §7.4)

| Band | Typical size | What changes |
|---|---|---|
| **Full (12–20)** | the size this case is written for | Anchors and the 45-minute timed plan run as written above |
| **Compressed (6–11)** | smaller room | Anchors 2–3 combine into one pass; the 20:00–30:00 D3 build-out runs as a single worked example instead of small-group work; total runtime shortens proportionally |
| **1:1 / pair (1–2)** | tutoring context | No vote at Anchor 1 — ask for a stated initial position and why instead; the facilitator plays devil's advocate directly rather than cold-calling the room; the MA1 pressure-test (30:00–38:00) still runs in full, since it is the single most important move in the case |
