# FACILITATOR.md — Electoral College

**Answer-key content. Never copy any of this into `case.md`.**

## Argument for A — The Big-Prize Strategy (greedy big-state read: Texas + Florida)

Texas (40 EV) and Florida (30 EV) are the largest single blocks of electoral votes still genuinely
reachable in one focused push among states Farnsworth currently leads. Committing to just two
states means paying the flat per-state travel cost only twice, not three or four times — most of
the budget goes to actual voter-swaying half-days, not setup overhead. This strategy spends the
entire $3,000,000 travel budget and reaches **296 total electoral votes** — a comfortable 26-vote
cushion over the 270 needed.

## Argument for B — The Margin Strategy (narrowest gaps, any size)

Chasing the two biggest prizes puts the whole travel budget behind two bets. Pennsylvania (an
exact tie — the narrowest possible gap), Nevada (2-point gap), and Wisconsin (4-point gap) can
each be closed in just 1-3 half-days — the fewest of any states in Appendix C — so a single week
can realistically put three separate states in play instead of two. That breadth is the real
argument for B: if any one state's polls move against Peaken in the campaign's final days, the
plan still has two others in reserve, and a win assembled from several states carries broader
state-by-state momentum than a win assembled from two. This is **not** the same claim as "most
votes per dollar" — narrow-gap states need fewer half-days each, but their flat per-state travel
fee is still spread across fewer electoral votes than a big state's, so B is not always the more
dollar-efficient choice (see "The trap," below). B's real case is resilience and breadth across
several winnable races, not cost-per-vote.

## The margin

**How it was computed:** `sensitivity_model.py` runs both strategies' literal state-selection
logic (Big-Prize: descending EV among states Farnsworth leads or ties; Margin: ascending
current-gap among the same states) against the fixed $3,000,000 travel budget and the
6-day/12-half-day-equivalent schedule cap, then compares each strategy's total projected electoral
votes (locked + already-leaning + newly flipped) against the real 270 threshold. A tie (gap = 0,
Pennsylvania) still needs exactly 1 half-day to strictly exceed Farnsworth — Challenge D2
explicitly asks the Hero to make the projection *exceed*, not match, the opponent's share, and the
model enforces that literally.

**Verified result:**

- Locked + already-Peaken-leaning contested states = 226 EV before any visits (50 locked via
  Appendix B + 176 already ahead in the November 1 poll per Appendix C).
- **Strategy A, literal execution:** visits Texas (40 EV, gap 6, $1,300,000) then Florida (30 EV,
  gap 11, $1,700,000) — spends the entire $3,000,000 budget, reaches **296 total electoral
  votes**. Comfortably clears 270.
- **Strategy B, literal execution:** visits Pennsylvania (19 EV, gap 0, $700,000, 1 half-day) then
  Nevada (6 EV, gap 2, $900,000) then Wisconsin (10 EV, gap 4, $1,100,000) — spends $2,700,000,
  reaches **261 total electoral votes**. The next-narrowest state, Michigan (gap 5), doesn't fit
  the remaining $300,000. **Still falls 9 votes short of 270** under this literal, mechanical
  "narrowest gap first" execution.
- **Margin on the primary metric (total EV secured): 13.4%** — comfortably inside SPEC's ~20%
  balance cap.
- **The naive-vs-smart execution gap (elaborated in the next section below):** a Hero who defends B by actually solving the
  allocation thoughtfully — Pennsylvania + Wisconsin + Michigan reaches exactly **270 EV for
  $2,900,000**, a legitimate, defensible B-philosophy plan that does win, once Nevada (cheap but
  low-payoff at only 6 EV) is swapped out for the better-value Michigan (15 EV for the same
  $1,100,000 Wisconsin costs). The gap between the naive sort and the smart solve is the
  discussion's real content.
- Run `python3 cases/electoral-college/sensitivity_model.py` for the full ±50% flex on the two
  load-bearing assumptions (MA2 per-visit cost, MA3 the swing rate) — margin ranges from 11.8% to
  12.4% across the flex, and Strategy A wins under every tested value; the direction of the result
  never flips, and its size barely moves either — this case's answer is genuinely stable.

## Five Socratic questions

1. Your plan spends money achieving more than 270 electoral votes in some states and comes up short in others — if you had exactly one more half-day to schedule anywhere, where would it do the most good, and how do you know?
2. Pennsylvania costs almost nothing to flip compared to Texas or Florida — so why would anyone ever choose the Big-Prize strategy over just picking every tied or near-tied state you can find?
3. Ohio's undecided pool is exactly the same size as the gap Peaken needs to close there — what happens if you spend six half-days campaigning in Ohio anyway, and what does that tell you about reading Appendix C's "Undecided %" column before committing budget to a state?
4. You have $3,000,000 and a state that would cost $3,200,000 to flip on paper — what is the actual right move, and is "get as close as possible" ever the correct answer in a winner-take-all electoral system?
5. If two students both correctly followed the Margin Strategy's logic — "narrowest margin first" — but ended up recommending different sets of states, what does that tell you about whether "narrowest margin" is actually a complete, well-defined strategy on its own?

## The trap

Most students will reflexively treat "narrowest polling margin" and "best value per dollar" as
the same thing. They are not: a state's per-half-day swing rate is fixed at 2 percentage points regardless of the
state's size, so a large state with a moderate gap (Texas: 6 points behind, 40 electoral votes)
can cost less per electoral vote than a small state with a very narrow gap (Nevada: 2 points
behind, only 6 electoral votes) — because Nevada's payoff is small even though it's cheap to
flip, while Texas's large payoff amortizes its flat per-state setup cost across far more
electoral votes. A Hero who reflexively picks the smallest gaps first, without checking each
state's actual electoral-vote payoff and its undecided-voter ceiling, can spend most of the
budget and still fall 9 votes short of 270 — precisely the failure mode the verified Strategy B
run hits, and the reason this case is not simply "pick the closest races."

## Sensitivity note

The 2%-per-half-day swing rate (MA3) and the flat per-state travel cost (MA2) are the two most
load-bearing assumptions in the whole model — every state-selection decision is a direct function
of both. `sensitivity_model.py`'s ±50% flex confirms Strategy A wins under every tested value
(margin ranges 11.8%-12.4%), so both the *direction* and the *size* of the recommended answer are
stable — a genuinely robust result, not one riding on a single fragile assumption.

---

## Guide Notes — the anchor ladder

### Intro

Frame the format: this is not a worksheet, it's a campaign strategy room. Name the opener —
"You have 6 days and $3,000,000 left. Where do you send your candidate?"

### Launch

Show the map from Appendix A/B (locked-state shading) and read the Background's closing line
aloud: two strategies, one budget, one shot. Do not show the state-by-state poll table (Appendix
C) yet — that comes at the Data Deep Dive.

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet, just commit. "Is anyone courageous enough to stand with the Big-Prize
Strategy? With the Margin Strategy?" Record the room's initial split — it is the number Anchor
close re-votes against.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

"Is this the right question?" "What do you mean by 'flip a state'?" "Does 'winning' mean 270
exactly, or 270 with room to spare?" Let confusion grow deliberately — "Wow, this is a genuinely
hard resource-allocation problem" is a good place to let the room sit for a minute.

### Anchor 3 — WHAT IS THE PROCESS?

"If we go through this process and find the data, how will we decide?" Push the room toward
naming an actual procedure (rank states by something, spend until the budget or the threshold is
hit) before anyone is allowed to open Appendix C. Re-ask: "Is our question still the right
question?"

### Anchor 4 — WHAT DON'T WE KNOW?

"Do we need to make assumptions? Which ones are critical?" Surface Appendix F's Modeling
Assumptions (the swing rate, the per-visit costs) without revealing their exact sensitivity —
just that they are stated assumptions, not measured facts, and a Hero may challenge them.

### Data Deep Dive

Now, and only now, the numbers: Appendix C's full 37-state poll table, Appendix E's budget
mechanics. Let the room actually start building visit plans.

### Twist

At roughly the 15-minute mark: **"Indiana just released a corrected poll. A follow-up
verification round found that 4 points of Indiana's previously counted 'undecided' voters had
already committed to Farnsworth before November 1 — undecided isn't 23%, it's 19%, and
Farnsworth's share rises from 48% to 52%. (Peaken's 29% is unchanged — Indiana's row still sums
to 100%.)"**

Before the correction, Indiana was a real, if expensive, option: closing its 19-point gap at 2
points per half-day needs exactly 10 half-days (20 points of movement), which fits inside the
original 23-point undecided ceiling — **mathematically reachable**, even though at
$2,500,000 (flat fee + 10 half-days) it costs more than the entire remaining travel budget on its
own, so no verified plan ever actually picks it. After the correction, the gap widens to 23
points while the ceiling shrinks to 19 — 10 half-days would need 20 points of movement, now
*more* than the new 19-point ceiling allows, and no number of half-days can close it. **Indiana
flips from mathematically reachable to mathematically impossible.**

Ask: **"Does this change your plan? You have 60 seconds — are you changing your states, or
not?"** This invalidates any position that was quietly counting on Indiana (an 11-EV state that
looks cheap on the surface but actually needs more half-days than any other state in Appendix C)
as a hidden reserve, without making either named strategy obviously correct — neither verified
plan (Big-Prize: Texas + Florida; Margin literal: Pennsylvania + Nevada + Wisconsin) ever used
Indiana, so the twist doesn't move either strategy's bottom-line EV total. Its job is to close off
a real backup some Heroes were eyeing, and to reward anyone who checked the undecided-pool ceiling
before penciling Indiana in as a fallback.

*(Separately, independent of the twist: Ohio's 12%-undecided ceiling exactly matches its 12-point
gap, so Ohio was already a dead-tie-at-best, mathematically unwinnable state from the November 1
data alone — see Socratic question 3 below. Ohio needs no twist to make this point; it's a trap
built into the original data.)*

### Close

VOTE AGAIN. "Did we ask the right question?" "What math was new to you today, and how did you
attack it?" Compare the final vote to the Anchor 1 vote — who moved, and toward which strategy.

### Lessons Learned

The gap between "wins states" and "wins the presidency": the Margin Strategy's literal
narrowest-first sort does win three separate states (Pennsylvania, Nevada, Wisconsin) — breadth
achieved — but still lands 9 electoral votes short of 270, because breadth alone was never the
actual win condition. A thoughtfully-solved version of the exact same philosophy (swap Nevada,
cheap but only 6 EV, for the better-payoff Michigan) reaches 270 for barely more money — the
strategy's *name* is not the same thing as a *correct execution* of it. Reading a ceiling
constraint (undecided %) before committing budget is not optional — Ohio punishes anyone who
skipped it.

### Standards Touched On

Percent; Ratio; Proportion; How to find the percent of a number; How to convert numbers to
percents; How to find a missing amount in a proportion; How to solve a one-step equation; How to
evaluate an expression with multiple operations without exponents (Order of Operations).

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00-3:00 | Cold-call launch, 30-second commitments, stand/sit vote (Anchor 1) — no explanation yet |
| 3:00-10:00 | Position defense: "Convince us why your strategy is better, not just that it sounds efficient/big" (Anchors 2-3) |
| 10:00-15:00 | Pressure-test the models: "Whose plan is most fragile if one state's poll is off by a few points?" |
| 15:00 | **DROP THE TWIST** — Indiana's undecided share is corrected from 23% to 19% (Farnsworth 48%→52%), delivered slowly, with pauses |
| 15:00-20:00 | Immediate recommit: who reverses, and who was quietly counting on Ohio? "What just broke?" |
| 20:00-30:00 | Threaded deep conflict, two named threads: (1) efficiency-per-dollar vs. certainty-of-reaching-270; (2) reading a ceiling constraint (undecided %) before spending vs. chasing the raw poll gap |
| 30:00-45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands (SPEC's cohort-bands requirement)

- **Full (12-14)** — the size the case was authored for. Both strategies get a full defense
  round; Anchor 3's process discussion can split the room into an "A" camp and a "B" camp before
  the numbers land; the full timed 45-minute Socratic plan runs as written.
- **Compressed (6-7)** — combine Anchors 2-3 into one pass; run one deep-conflict thread instead
  of two (efficiency vs. certainty of reaching 270); keep the Ohio-ceiling twist — it is cheap to
  run at any size; total runtime shortens proportionally, not the content.
- **1:1 / pair (1-2)** — no vote to take; Anchor 1 becomes each learner stating an initial
  position instead of a stand/sit vote; the guide plays devil's advocate on the other strategy
  directly rather than cold-calling; the twist still lands; "who reverses" becomes "would you
  reverse, and why."
