# FACILITATOR.md — The Deferred Repair

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the top of case.md.*

**Case:** The Deferred Repair · **Tier:** T3 (MS-stretch / HS-entry) · **Studio:** MS Adventure
**Standards:** Statistics And Probability — Probability, Event, Outcome, Dependent Event,
Conditional Probability, and three "how to…" skills (single event, compound event, conditional
events), plus Advanced Numbers' percent-of-a-number how-to (see `case.json.standards[]` for exact
ids).

**Status:** `case-research` complete (2026-09-03). All `{{NEEDS_SOURCE: ...}}` placeholders in
`case.md` are resolved — five real RepairPal prices/costs are sourced (Appendix E), and the three
per-year/cumulative failure probabilities (Appendix B, Appendix C) are disclosed Modeling
Assumptions MA1-MA3, not sourced figures, because no publishable schedule exists for any of them.
`case.json.balance.margin_pct` is a real, computed **13.0%**. Everything below is the case of
record, not a placeholder.

**Sensitivity note (SPEC §6):** this case touches ordinary money stress — a single-income home
health aide budgeting a car repair against her ability to keep working. No illness, death, or
family hardship beyond that. Facilitators should not need a heavier touch than usual, but should
be ready if a Hero's own family situation makes "the car is how I earn my income" land harder
than expected.

## Argument for A — The Standing Order

Option A's case is a **risk-management argument, not a raw-dollar-average argument**: it converts
an uncertain, right-tailed risk (a $2,938 repair that may or may not happen) into a small, certain,
budgetable cost Elena can plan around. This matters because the compound probability of at least
one coolant-related failure across all three years she has committed to keeping the car — computed
via the complement of "fails in none of the three years" — comes out to roughly 36.7% (D2), a real
and non-trivial chance for a repair bill that could otherwise force her to replace the car early.
**Under the case's own current numbers, this is the harder argument to win on raw dollars alone**
(see "The margin" below) — its real strength is that it eliminates variance, which is worth
something even when it is not the cheapest option on average, and it is only a thin margin away
from also being the cheaper option.

## Argument for B — The Reactive Route

B's real, quantitative case is D3's actual expected-cost comparison, correctly weighted by
probability: under MA1's stated Year 1-3 schedule, The Reactive Route's expected annual cost comes
out **lower** than the flush's certain price (see "The margin" below). This is a genuinely
different route to a similar-sounding conclusion than the reasoning shortcut named later in this
guide (which reaches the same-sounding conclusion by comparing $473 to $2,938 directly, with no
probability weighting at all) — B's D3-based case is the correct answer to the correctly-posed
question, at least under MA1's current values. It is also fragile: because Appendix B's Year 1-3
probabilities are a stated Modeling Assumption (MA1), not an empirical certainty, a Hero who mounts
a defensible
challenge that the real risk is somewhat *higher* than assumed can legitimately move the
comparison back toward A.

## The margin — real numbers, and which way the fragility runs

`case.json.balance.margin_pct` = **13.0%**, inside the SPEC §2 target 10-15% band. The arithmetic,
in full:

- **The Standing Order (A):** $473.00/yr, certain, every year [S1].
- **The Reactive Route (B), expected annual cost:** average across the three years of
  (that year's MA1 probability x the $2,938 repair cost [S4]):
  - Year 1: 9% x 2,938 = $264.42
  - Year 2: 13% x 2,938 = $381.94
  - Year 3: 20% x 2,938 = $587.60
  - Average: (264.42 + 381.94 + 587.60) / 3 = **$411.32/yr**
- **Margin:** |473.00 - 411.32| / 473.00 = **13.0%**

**Under MA1's current values, B is the cheaper option** — $411.32/yr against A's $473.00/yr. This
margin is a designed property of MA1's chosen values, not an empirical finding — the $473 flush
price and $2,938 repair cost are real, sourced figures, but the 9%/13%/20% schedule that drives
B's side of the comparison is an authored Modeling Assumption (see
`case.json.modeling_assumptions[MA1]` for the full search trail and basis: RepairPal, CarMD's
Vehicle Health Index, AAA newsroom releases, Car Care Council, and mechanic-trade press all turned
up no publishable per-year schedule for this claim).

**Why this matters for the facilitator, specifically:** MA1 is the load-bearing, dilemma-flipping
assumption in this case, and the fragility runs **upward, not downward**. The three-year average
probability under MA1 is currently (9% + 13% + 20%) / 3 = 14%. The break-even average is 473 /
2,938 ≈ **16.1%** — if the real average probability were higher than that (roughly two points
above the current 14%), The Standing Order would become the cheaper option and the recommendation
would flip to A. This can happen by raising all three years a little, or by raising just one:
`sensitivity_model.py` shows **Year 3 alone needs only about a 31% relative increase (20% → ~26%)
to flip the case**, versus roughly 48% for Year 2 alone and 70% for Year 1 alone — Year 3 is the
single most leverage-sensitive number in Appendix B, precisely because it carries the largest
weight in the three-year average. A sharp student who argues Year 3's escalation to 20% looks too
aggressive, or that all three years should read a bit higher than assumed (a defensible position —
MA1's own basis text concedes the escalation schedule is chosen, not measured), can flip the case's
own recommendation from B to A with a single clean, *upward* challenge to Appendix B. **Do not
treat a student who argues the probabilities should be lower, and concludes "B wins by even more,"
as having found the case's fragility — the fragile direction is the other way.** The Socratic
questions below are built to surface exactly that upward fragility
rather than paper over it, and a facilitator who has internalized the wrong direction will
mis-referee the discussion.

## Five Socratic questions

1. Your D3 table multiplies each year's probability by the $2,938 repair cost to get an expected cost — why is that the right thing to compare against the flush's certain $473, instead of comparing $473 to $2,938 directly?
2. MA1's Year 3 probability is set at 20%, but no source publishes that number — if you argued the escalation should top out closer to 26%, would The Reactive Route still come out cheaper, or does the recommendation flip to The Standing Order?
3. You computed the chance of at least one failure across three years by taking a complement instead of adding the three yearly probabilities together — what would adding them have gotten wrong, and by how much?
4. Appendix C's cabin air filter carries the exact same shop tone and a similar price to the coolant flush, but D4 says you should not treat it the same way — what specific number, not tone or price, made the difference?
5. If the whole case rests on a single assumed schedule of probabilities that nobody actually measured, what would you need to see to trust MA1's 9%/13%/20% more than you do right now — and does knowing the case's own margin is only 13.0% wide make that question more or less urgent?

## The trap

**A learner who compares the flush's certain price directly to the repair's certain price —
ignoring the probability weighting entirely — will conclude "just pay for the repair if it
happens," and land on the same option D3's correct math also favors, but for the wrong reason and
with no idea how close that answer is to flipping.** This is the whole point of the case: the flush
price and the repair price are not directly comparable numbers, even though, this time, the naive
comparison and the correct one happen to point the same way. Only the *expected* value of the
repair — probability times cost — belongs next to the flush's certain price, and only the correct
route reveals the 13.0% margin and its closeness to the 16.1% flip point. A pitch that never runs
D2's compound-probability step, or never multiplies Appendix B's probability against the repair
cost in D3, has fallen into this trap even if it reaches the same recommendation and even if its
prose sounds confident.

**A second, more likely trap (Tier 2 P3 finding, added after adversarial review):** a student who
correctly builds D1 and D2 can still get D3 wrong by reusing D2's single *compound* three-year
probability (~36.7%) as if it were a per-year multiplier — e.g. multiplying 36.7% by $2,938 once
and comparing that single number to three years of flush payments ($473 x 3 = $1,419) — instead of
computing each year's *own* expected cost (Year 1: 9% x $2,938, Year 2: 13% x $2,938, Year 3: 20% x
$2,938) and summing those three separately. This produces a plausible-looking dollar figure from
real numbers in the case, but blurs "probability of at least one failure across the whole window"
(D2's job) with "expected cost per year" (D3's job) — watch for a pitch whose D3 table has only one
row instead of three. A related version of this same trap collapses Challenge 3 (D4) into "the shop
flags everything urgently, so either pay for all three or decline all three" — riding the
Background's own "shops flag everything the same shade of red" framing one step too far, and
skipping the actual per-service three-year expected-cost comparison Appendix C's data is there to
force. Watch for a pitch that reaches a filtering conclusion on tone or price alone rather than on
each service's own number.

## Twist

Not built as a scripted mid-discussion reveal for this case — the "twist" here is structural
rather than a dropped new fact, and it lives inside MA1 itself: **the assumption a Hero is most
likely to challenge upward (Year 1's 9%, the least-escalated and easiest to argue against) is also
the lever most likely to flip the entire recommendation from B to A.** Facilitators should treat
the moment a student notices this — usually while working through Socratic Question 2 — as the
twist moment, and can manufacture it directly by asking Question 2 if no student raises it
unprompted.

---

## Guide Notes — the anchor ladder (SPEC Section 7, anchor-ladder subsection)

### Intro

Frame the format: three checkboxes, one shop tablet, one estimate Elena cannot fully
afford today. This is a real household budgeting choice dressed as a car-repair worksheet, not
the other way around.

### Launch

Read the Overview aloud. Stop at "she's not sure which of the shop's warnings is a
real number and which one is just how shops talk." Ask the room: "Before you've seen a single
number, which of the three flagged items do you already suspect is the real risk, and which do
you suspect is just how shops talk? Why?"

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "Standing Order or Reactive Route — show
of hands." Record the split. Most rooms will split closer than they expect once they realize the
shop's identical "overdue" tone is being used to sell three genuinely different risks.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push the room past "which repair is scarier"
toward "which of these three flagged items has a real, quantifiable expected cost, and which is
priced on tone alone." Let the room sit with the fact that Appendix B's own probabilities are not
published anywhere — they are the case's stated Modeling Assumption, not a fact anyone can look up.

### Anchor 3 — WHAT IS THE PROCESS?

Before touching Appendix B's numbers, get the room to state
the actual comparison method out loud: build the three-year conditional-probability table (D1),
compound it into a single three-year failure risk (D2), then weight the repair cost by that risk
to get an expected annual cost comparable to the flush's certain price (D3). Re-ask: "Now that we
have a process, is 'which repair is scarier' still the right question?"

### Anchor 4 — WHAT DON'T WE KNOW?

Name the load-bearing unknown explicitly: nobody — not
RepairPal, not the shop, not this case — has ever measured a real per-year probability schedule
for a skipped coolant flush. "Is 9%/13%/20% a fact, or a stated, defensible guess? What would make
a different guess just as defensible?"

### Data Deep Dive

Now open Appendices A-D. Run D1-D5 as a room, or have groups report out.
This is also the moment to run Socratic Questions 1 and 3 (the expected-value logic and the
compound-probability mechanics).

### Twist

Once D3's numbers are on the table and a recommendation has started to form, run
Socratic Question 2 directly: "MA1's Year 1 number is 9%, and nobody measured it. If the real risk
actually starts higher, does your recommendation survive?" Let the room discover that the margin is
only 13.0% and the flip point is ~16.1% (against a current average of 14%) — closer than almost
anyone will expect from a "the math says so" pitch, and that the fragile direction is upward, not
downward.

### Close

VOTE AGAIN. "Did the vote move? For the people who didn't move, what would it take to
change your mind — a different number, or a different assumption entirely?"

### Lessons Learned

The core transferable idea: an expected-value comparison can look
decisive on paper while actually resting on an assumption a reasonable person could argue with —
and the size of the margin (13.0%, against a flip point of ~16.1%) is exactly what tells you how
much room that assumption has to be wrong before the "right" answer changes.

### Standards Touched On

Probability, Event, Outcome, Dependent Event, Conditional Probability;
How to determine the probability of a single event; How to determine the probability of a compound
event; How to determine the probability of conditional events; How to find the percent of a
number.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00-3:00 | Cold read of the Overview, gut-check vote (Anchor 1) — no numbers shown yet |
| 3:00-8:00 | Position defense: "Convince us your pick is the safer bet, not just the one that feels safer" |
| 8:00-20:00 | Data Deep Dive — build D1's conditional-probability table and D2's compound probability as a room |
| 20:00-30:00 | Build D3's expected-cost comparison; confirm the 13.0% margin and where it comes from |
| **30:00** | **DROP THE TWIST** — Socratic Question 2: MA1's Year 1 number (9%) is unmeasured; if the real risk starts higher, does the recommendation survive? |
| 30:00-38:00 | Pressure-test MA1 directly: how close is 13.0% to the ~16.1% flip point, and what would a defensible challenge to any one year's number actually change? |
| 38:00-45:00 | Close, re-vote, D4's filtering exercise on the transmission/cabin-filter rows, lessons learned |

## Cohort bands (SPEC Section 7, cohort-bands subsection)

| Band | Typical size | What changes |
|---|---|---|
| **Full (12-20)** | the size this case is written for | Anchors and the 45-minute timed plan run as written above |
| **Compressed (6-11)** | smaller room | Anchors 2-3 combine into one pass; the 20:00-30:00 expected-cost build-out runs as a single worked example instead of small-group work; total runtime shortens proportionally |
| **1:1 / pair (1-2)** | tutoring context | No vote at Anchor 1 — ask for a stated initial position and why instead; the facilitator plays devil's advocate directly rather than cold-calling the room; the MA1 pressure-test (30:00-38:00) still runs in full, since it is the single most important move in the case |
