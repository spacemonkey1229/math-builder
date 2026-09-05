# FACILITATOR.md — The Quiet Thief

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Quiet Thief · **Tier:** T4 (HS-entry) · **Studio:** Adventure
**Standards:** Advanced Operations/Exponents — Exponent (also Power), Base, How to evaluate an
exponential expression, How to evaluate an expression with multiple operations with exponents
(Order Of Operations); Advanced Numbers/Percents — Percent, How to convert percents to numbers,
How to find the percent of a number (see `case.json.standards[]` for exact ids).

**Status:** `case-research` complete (2026-09-04) — every `{{NEEDS_SOURCE}}` token in `case.json`
is resolved (`SOURCED` or disclosed `ASSUMPTION`). `margin_pct = 13.66` — see Balance argument
below. Currently in `case-readiness` remediation.

**One-line sensitivity flag (SPEC §6):** this case touches a real personal-finance decision (a
friend's retirement savings, and a decade of a Hero's own past inaction) at comparatively low
acute stakes — a long-horizon planning choice, not illness, death, or acute hardship. A facilitator
should read the room before pushing hard on "you're already behind" framing — for some learners,
their own family's retirement-savings situation is not abstract, and Jordan's ten-year gap may land
uncomfortably close to home.

## Real-world grounding (for the facilitator's own background, not for case.md)

- The mechanism this case is named for — inflation quietly eroding what a saved dollar is actually
  worth by the time it's spent — is real, uncontroversial, and precisely why "the same dollar
  amount, contributed later" does not close a savings gap the way intuition suggests. The genuine
  pedagogical trap is not the finance content itself (compounding and inflation are both fully
  knowable, sourced mechanisms) but the arithmetic shortcut of skipping the real-rate derivation
  and using the larger, more exciting nominal return number instead.
- The "just contribute more later" plan is extremely common real-world thinking, and it is
  *directionally* reasonable — more money later does help — but D5 exists specifically to show how
  badly it is usually miscalculated: a saver who plugs in the nominal ~10% return instead of the
  correctly-derived ~6.6925% real return will underestimate the required catch-up contribution by
  roughly half. That gap between "sounds like enough" and "actually enough" is the case's entire
  reason to exist.
- A useful framing for Anchor 2: nobody in the room is being asked to guess Jordan's future income
  or the market's future return — both rates in Appendix C are long-run historical averages, real
  and cited. The genuine open question is a values question (Bridge vs. Extended), not a
  forecasting question — the opposite structural shape from a case like The Bracket Bet, where the
  unknown itself is what's contested.

## Balance argument

- **Argument for A (Bridge Plan):** wins on certainty and timeline — it is the only plan that
  actually reaches Priya's real target balance by the same age Priya is retiring, without betting
  on two more years of health, employment, and market conditions cooperating. The cost is a
  materially larger monthly number starting immediately: $817.00/month, about 2.04x Priya's
  $400/month (D3).
- **Argument for B (Extended Plan):** wins on affordability today — it reaches the *identical* real
  target balance for a meaningfully smaller monthly commitment, $705.38/month, about 1.76x Priya's
  contribution (D4), by trading two additional years of account growth for less monthly sacrifice
  right now. For a Hero whose budget genuinely cannot absorb the Bridge Plan's larger number, the
  Extended Plan is not a consolation prize — it reaches the same real dollar destination, just on a
  different clock.
- **The margin — CONFIRMED by case-research:** Real annual rate of return = (1+0.10)/(1+0.031) − 1
  = 6.6925% [S2, S3, D1]. Real monthly rate = (1.066925)^(1/12) − 1 = 0.5413%/month. Priya's real
  target balance (504 months at $400/month) = $1,048,768.04 (D2). Bridge Plan (384 months):
  $817.00/month (D3). Extended Plan (408 months): $705.38/month (D4).
  `margin_pct` = (817.00 − 705.38) / 817.00 × 100 = **13.66%** — comfortably inside the case's
  10–15% target band and well under SPEC §2's 20% cap. Full arithmetic in `RESEARCH_LOG.md` and
  `sensitivity_model.py`.
- **Why a 2-year delay (MA3), not some other number:** a 1-year delay narrows the margin
  (less time to matter); a 5+ year delay would start to look like an obviously-better deal for
  Option B, flattening the genuine tension. Two years was chosen, and verified by running the
  actual model, to land the margin inside the case's target band without engineering the specific
  percentage — see `case.json.sensitivity_disclosure[]` (Category D: a disclosed case-design dial,
  not a hidden fragility).

## Five Socratic questions

1. D3 and D4 both reach the exact same real target balance — if the destination is identical, what is actually different between the Bridge Plan and the Extended Plan, and is that difference about money, or about something else?
2. D5 shows that using the nominal rate instead of the real rate understates the Bridge Plan's required contribution by about half — in your own words, where does that missing money actually go, and whose pocket is it landing in?
3. If Jordan had waited fifteen years instead of ten before starting, would you expect the gap between the Bridge Plan and Extended Plan's monthly contributions (in dollars) to grow, shrink, or stay the same, and can you defend your answer using D1's formula instead of just intuition?
4. Appendix D's MA2 fixes both savers' contribution at $400/month — if that number doubled for both Priya and Jordan, would the 13.66% margin between the Bridge and Extended Plans change, and what does your answer say about which numbers in this case are load-bearing for the percentage versus the dollar amounts?
5. A friend tells Jordan, "don't worry about the exact math, just start contributing whatever you can and figure out the rest later" — what, specifically, does that advice get right, and what does it get dangerously wrong given what D3–D5 actually show?

## The trap

**The primary, most likely trap — a linear ("simple-subtraction") shortcut in place of D1's exact
compounding formulas.** D1 explicitly requires two compounding operations most learners already
have a *simpler, wrong* shortcut memorized for, and the shortcut is dangerously close-looking:
(1) instead of the real-rate formula `(1+nominal)/(1+inflation) − 1`, a learner subtracts —
`10% − 3.1% = 6.9%` — the classic "Fisher approximation" taught informally as if it were equivalent
to the compounded version; (2) instead of the monthly-conversion formula
`(1+annual real rate)^(1/12) − 1`, a learner divides by 12 — the "annual rate ÷ 12 = monthly rate"
reflex used for simple interest, which directly contradicts D1's explicit instruction to evaluate
the exponential expression step by step. Each individual shortcut error looks small (6.9% vs. the
correct ~6.69%; a monthly rate a few hundredths of a percent too high), but raised to the large
exponents in D2-D5 (n = 384-504 months), the error compounds into every downstream dollar figure
being systematically too large by roughly 10% — while the *qualitative* story survives untouched
(Bridge still costs more than Extended; the nominal-rate figure in D5 still understates the truth),
so a grader skimming for "does the argument make sense" can easily miss it. **The tell in
discussion:** ask a Hero to show the actual exponent step in D1 and D2 written out — `(1+r)^n`, not
a decimal that appeared from nowhere — and ask them to explain, out loud, why `10% − 3.1%` is not
the same operation as `(1.10/1.031) − 1`. A Hero who cannot produce the written-out exponent step
has very likely taken the shortcut, whether or not their final recommendation happens to still be
directionally correct.

**A second trap: reaching for the nominal rate instead of the real rate entirely.** A learner who
accepts "just start contributing more, you'll catch up" without ever deriving the
real rate of return will reach for the more familiar, larger nominal return figure (10%) instead of
the smaller, correctly-adjusted real rate (6.6925%) — and D5 exists to make this failure mode
explicit and gradable. The naive nominal-rate calculation understates the Bridge Plan's true
required contribution by roughly half: a learner who skips D1's derivation entirely, or who derives
it but then reaches for the nominal rate anyway "because it's the number everyone quotes," will
walk away believing catching up costs far less than it actually does. The tell in discussion: ask a
Hero to explain, in plain language, *why* the real rate is smaller than the nominal rate — a Hero
who has not internalized D1 will not be able to explain that inflation is being subtracted out, and
will be tempted to treat the smaller real-rate number as somehow the more "conservative" or
"padded" choice rather than the mathematically correct one.

**A second, quieter trap: mistaking the Extended Plan for a smaller version of the same problem.**
A Hero can correctly compute D3 and D4 and still frame the Extended Plan as "basically the same
plan, just cheaper" — missing that it is not a discount on the Bridge Plan's price, but a genuinely
different trade (money now vs. time later) that happens to reach the identical real destination.
Cold-call a Hero on whether the Extended Plan is "worse," "better," or "different but equal" to
surface this.

## Socratic questions — sensitivity note

The primary metric is deliberately built from two real, sourced, long-run average rates (nominal
return and inflation) rather than a single unknowable forecast — unlike a case such as The Bracket
Bet, where the open question *is* a genuinely unknowable future value. Here, the open question is a
values trade-off between two fully-computed, equally-real outcomes. `case.json.sensitivity_note`
and this file's Balance argument record the specific numbers; `case.md` never states which plan a
Hero "should" prefer or states the margin's size/direction.

---

## Guide Notes — the anchor ladder (SPEC §7)

### Intro

Frame the format: this is a real, one-time contribution-setting decision under a real one-week
lock-in window, not a worksheet. Name the opener: "Jordan has a week. Bridge or Extended. Go."

### Launch

Read the Overview's opening beat aloud — Priya's screenshot, the blinking cursor in the blank
contribution field — with no numbers attached yet. Ask: "If all you knew was that Jordan started
ten years after Priya, what do you think 'catching up' should cost — a little more per month, or a
lot more?" Take answers without correcting anyone; most rooms underestimate the size of the gap,
which is the point.

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "Is anyone courageous enough to stand with the Extended Plan — the one that means
working two extra years?" Show of hands, both options, no discussion. Record the count — Close will
ask again.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push the room past "which plan is better" toward "what does it actually mean for two different
plans to reach the *same* real balance." Ask: "Is 'catch up' even well-defined yet — catch up to
what, exactly, and measured in what kind of dollars?" If the room lands on "we need to know what a
dollar today is actually going to be worth decades from now, not just how many of them pile up,"
the case is working as designed.

### Anchor 3 — WHAT IS THE PROCESS?

Make the room name the steps before opening an appendix: (1) turn the two sourced rates (nominal
return, inflation) into one real rate that already accounts for inflation, (2) use that real rate
to find out what Priya's own plan is actually worth in today's dollars at retirement, (3) work
backwards from that same target to find what monthly contribution each of Jordan's two plans
actually requires, (4) compare the two required contributions to see the real, computed gap between
them. Re-ask: "Now that we can see the steps, is 'which plan is better' still the right question —
or is it 'which trade-off do you personally want to make'?"

### Anchor 4 — WHAT DON'T WE KNOW?

Surface the disclosed scenario constants: Appendix D's MA1 (the two starting ages), MA2 (the
$400/month contribution figure), and MA3 (the Extended Plan's 2-year delay) are all stated
modeling assumptions, not sourced facts. Ask: "If Priya and Jordan's contribution amount from
Appendix A were doubled, would today's arithmetic answer change? Would the *conclusion* change?" A
sharp Hero should be able to say the dollar figures would double but the 13.66% margin between the
two plans would not move — that ratio is scale-independent (see FACILITATOR.md's Balance
argument).

### Data Deep Dive

Now, and only now, open Appendices A–D and work D1–D5. Cold-call for D1 specifically — this is
where a Hero who jumps straight to "just use 10%" without deriving the real rate first will produce
every downstream number wrong, without necessarily noticing.

**Facilitator-only arithmetic note.** Real annual rate: (1+0.10)/(1+0.031) − 1 = 6.6925%. Real monthly
rate: (1.066925)^(1/12) − 1 = 0.5413%/month. Priya's FV (504 months, $400/mo): $1,048,768.04. Bridge
Plan PMT (384 months): $817.00/month. Extended Plan PMT (408 months): $705.38/month. Nominal-rate
(wrong) Bridge Plan PMT: $415.79/month — a 49.11% understatement of the true $817.00 figure. Full
derivation in `case.json.balance.margin_basis` and `sensitivity_model.py`.

### Twist

**Twist: N/A.** This case's tension is a genuine, already fully-disclosed two-option trade-off
(money now vs. time later, at a real, computed 13.66% margin) that resolves entirely through the
arithmetic the Challenges already require — there is no additional real-world fact withheld from
Appendices A–D whose reveal at the 15-minute mark would invalidate a popular position without
either (a) leaking the margin's size/direction into case.md, which case-write's balance rule
forbids, or (b) inventing a number the research pass didn't source. D5's own nominal-vs-real
comparison already produces the surprise-and-recompute moment a Twist is meant to create — many
rooms expect "just use whatever rate you remember reading about" to be close enough, and D5 shows
it understates the truth by roughly half. See the Immediate Recommit note below, which the
facilitator should treat as carrying that weight instead.

### Immediate recommit

Right after D5 lands on the board, ask by name: "If you had computed your Bridge Plan number using
the nominal rate instead of the real rate, you'd have been off by about half. Does that change how
much you trust your Anchor 1 gut vote?" Many Heroes who voted Bridge Plan on a "just tough it out"
instinct will not have realized how much larger the real number actually is until D5's contrast
lands; conversely, a Hero who assumed the Extended Plan was "obviously" the easier way out should
recompute in front of the room and see it is still well above Priya's own $400/month contribution.

### Deep conflict — two threads (20–30 min)

1. **Money now vs. time later.** Push the room to state, in plain English, why $817.00/month
   starting today and $705.38/month starting today both reach the exact same real destination —
   and what that says about how "more time" and "more money" can substitute for each other in a
   compounding system. Ask: "Is there a version of this trade-off where the two plans stop being
   comparable — where one clearly wins regardless of preference?"
2. **What the nominal-rate trap reveals about trusting a "quoted" number.** D5 shows that reaching
   for the more commonly quoted 10% figure — instead of doing the extra step to find the real rate
   — produces a confidently wrong answer, not an obviously wrong one. Push a Hero to name one other
   real-world situation where the "commonly quoted" number and the "actually relevant" number
   differ this much, and ask what habit would have caught the gap before committing real money to
   it.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — read the Overview's opening beat with no numbers, cold-call for a gut read on the size of the gap |
| 3:00–10:00 | Position defense — *"Walk us through your D1 real-rate derivation — what's the nominal rate, what's the inflation rate, and why isn't the answer just 10% minus 3.1%?"* |
| 10:00–15:00 | Pressure-test the process — *"Which of your D1–D2 numbers, if it changed, would move your D3/D4 dollar amounts — and which would leave the 13.66% margin between them untouched?"* |
| **15:00** | **DROP THE TWIST (N/A — instead, land the D5 nominal-rate-trap reveal)** — the "quick" 10% calculation understates the truth by about half |
| 15:00–20:00 | Immediate recommit — does the D5 reveal change anyone's confidence in their Anchor 1 vote |
| 20:00–30:00 | Threaded deep conflict (money now vs. time later; trusting a quoted number vs. deriving the real one) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## Close

**VOTE AGAIN.** "Did your recommendation change — or just your confidence in the number behind it?"
Ask what math was new to each Hero, and specifically whether deriving the real rate (D1), computing
Priya's target (D2), or seeing the nominal-rate trap's size (D5) was the step that actually changed
their thinking.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes' Anchor-1 gut vote (Bridge vs. Extended) matched their post-D4 recommendation, or
  whether the exact 13.66% margin flipped a meaningful share of the room.
- Whether the "starting later costs roughly double, not just a little more" finding (D3) landed as
  a genuine surprise or as an obvious restatement of something Heroes already suspected.
- Whether any Hero caught, unprompted, that MA2's $400/month figure does not affect the 13.66%
  margin — a sign the "which numbers are load-bearing for a ratio vs. a dollar amount" distinction
  actually transferred.

## Standards Touched On

Exponent (also Power); Base; Percent; How to evaluate an exponential expression; How to evaluate an
expression with multiple operations with exponents (Order Of Operations); How to convert percents
to numbers; How to find the percent of a number.

## Cohort bands (SPEC §7)

| Band | Typical size | What changes |
|---|---|---|
| **Full** | 12-20 (the size this case is written for) | Anchors and timings run as written above |
| **Compressed** | 6-11 | Anchors 2-3 combine into one pass; the deep-conflict section (20:00-30:00) runs one thread instead of two; total runtime shortens proportionally |
| **1:1 / pair** | 1-2 | No vote at Anchor 1 — instead ask for a stated initial position and why; the facilitator plays devil's advocate directly rather than cold-calling the room; the D5 reveal still lands, and "who reverses" becomes "would you reverse, and why" |
