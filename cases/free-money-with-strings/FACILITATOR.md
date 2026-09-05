# Guide Notes: Free Money, With Strings

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — the
balance argument, margin, and sensitivity notes live only here and in `case.json`'s `balance`
object.*

**Case:** Free Money, With Strings · **Tier:** T4 · **Band:** MS-stretch / HS-entry · **Studio:** MS Adventure
**Standards:** Advanced Numbers/Percents — `advanced-numbers-percent`,
`advanced-numbers-how-to-find-the-percent-of-a-number`, `advanced-numbers-how-to-convert-percents-to-numbers`;
Advanced Operations/Exponents — `advanced-operations-exponent-also-power`,
`advanced-operations-how-to-evaluate-an-exponential-expression`; Calculus/Derivatives —
`calculus-instantaneous-rate-of-change` (all already n>0 in the spine; this case reinforces three of
the thinnest skills in the entire spine — see `case.json.reinforcement_note` — while closing the
Taxes & tax-advantaged-accounts/employer-match topic gap named in `case.json.topic_gap_closed`).

**Status:** Researched 2026-09-04. Numbers below are the real, sourced/assumed figures — never
state them, or the margin's size/direction, inside `case.md`.

## The real numbers (facilitator reference — never appears in case.md)

- Salary $72,744/yr [S1]. Both strategies contribute at least 6% of salary ($4,364.64/yr) and both
  receive the full 50%-of-6% employer match ($2,182.32/yr) — this shared stream is **identical**
  between the two strategies and is not actually in dispute.
- Match & Move's extra 9% of salary ($6,546.96/yr) goes to loan paydown, "earning" the loan's own
  guaranteed rate of 6.39%/yr [S6] (MA3). Stack & Grow's extra 9% of salary goes into the 401(k),
  earning the assumed 10%/yr market rate [S7-based, MA1] instead.
- Ten-year future value (FV_annuity = PMT × [(1+r)^n − 1] / r, n=10):
  - Shared 6%-plus-match stream at 10%: $6,546.96/yr → **$104,341.68**.
  - Match & Move's extra stream at 6.39% (guaranteed): $6,546.96/yr → **$87,891.05**. **Total A =
    $192,232.73.**
  - Stack & Grow's full 15%-plus-match stream at 10%: $13,093.92/yr → **Total B = $208,683.36.**
- **Margin: Stack & Grow (B) wins by $16,450.63, or 8.56%** (`case.json.margin_pct` = 8.56, well
  inside the SPEC §2 20% cap).
- **Why this stays a genuine two-sided case, not a landslide:** Match & Move's return is
  *contractually guaranteed* (6.39%, a real published federal loan rate); Stack & Grow's return
  depends entirely on MA1 (10%, a disclosed assumption about the future, however well-grounded in
  historical data). A Hero who distrusts the market assumption — or who is more debt-averse than
  return-maximizing — has a live, quantitative reason to prefer Match & Move even though it loses
  under the case's own stated central assumption. See Tier 2 P5 for exactly how far MA1 would have
  to fall before Match & Move wins outright.

## The structural argument (true regardless of the exact sourced numbers)

- **Argument for A (Match & Move):** Every dollar Devon contributes up to the match cap is matched
  by the employer — a guaranteed, immediate return on that dollar that no ordinary investment can
  beat (the match rate itself, before any market growth even starts). Once the cap is reached,
  every next dollar earns zero match. Devon's own loan carries a fixed, guaranteed interest rate;
  paying it down early is mathematically equivalent to earning a guaranteed return equal to that
  rate (MA3) — a real, certain number, not a hoped-for market average. Match & Move argues that
  once the free money stops, a guaranteed debt-interest-avoidance return can beat an uncertain
  market-average return, especially if the loan's rate turns out to be close to or above the
  assumed market growth rate.
- **Argument for B (Stack & Grow):** The employer match on the first dollars is real and both
  strategies capture 100% of it — that part is not actually in dispute. What differs is what
  happens to dollars *beyond* the cap: Stack & Grow keeps investing them at the market growth rate
  (MA1) for the full ten-year horizon, compounding the whole time, while Match & Move only avoids
  the loan's interest rate on those dollars and stops "earning" once the loan itself is paid off
  (a fixed, finite benefit) — whereas continued market investment has no such ceiling and keeps
  compounding for the entire horizon. Stack & Grow argues that if the assumed market growth rate
  exceeds the loan's guaranteed rate by enough, and the ten-year horizon is long enough for
  compounding to matter, contributing beyond the cap wins even though those extra dollars get no
  match.
- **The actual margin (8.56% in Stack & Grow's favor) confirms neither argument has collapsed:**
  Match & Move's guaranteed 6.39% return is real and large in absolute terms ($87,891.05 over ten
  years on the extra dollars alone), it simply loses to a 10%-assumed market return by 3.61 points
  compounded for a decade. Tier 2 P2 (both-sides solve) confirmed both arguments carry real,
  specific numbers rather than a concession — see `QA_REPORT.md`.

## Intro

Frame the format before anything else: Devon has one shot at this — the contribution percentage
chosen this pay period is locked until next year's open enrollment. Name the opener: "You're
Devon. Whatever percentage you type into that portal today is what actually happens to every
paycheck for the next year. There's no 'let me think about it and change it Monday.'"

## Launch

Read the two strategy nicknames — Match & Move and Stack & Grow — with no numbers attached yet.
Ask: "If all you knew was those two names, which sounds smarter to you, right now, and why?" Take
answers without correcting anyone. Record the room's initial split — the case's job is to replace
the gut read with an actual number.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Match & Move — capping contributions and paying down
debt instead?" Show of hands, both options, no discussion. Record the count — Close will ask again.

## Anchor 2 — What is the problem we're solving?

**"Is 'which strategy gets more free money' the right question?" · "What do you mean by
'better' — better this year, or better ten years from now?"**

Push the room to state the actual metric before touching an appendix: not "which strategy gets a
bigger match" (both strategies get 100% of the available match — that is not actually the
dispute), but total combined value across *both* accounts (401(k) plus loan position) at a fixed
future horizon. If the room lands on "we need to know what happens to the dollars *beyond* the
match cap, specifically," the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Make the room name the steps before opening an appendix: (1) find each strategy's contribution
ledger — own money, employer match, and where the "extra" dollars go (D1), (2) project each
strategy's accounts ten years out using the stated growth assumption, showing the exponent step
(D2), (3) compare the marginal return earned on the last dollar under the cap versus the first
dollar over it (D3), (4) total each strategy's ten-year value and state the margin (D4). Re-ask:
"Now that we can see the steps, is our question still the right one?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the honest gaps: Appendix C's MA1 (assumed future market growth rate) is a stated
assumption about the future, not a fact — nobody can know what the market will actually return
over the next ten years, even when the assumed value is grounded in real historical data. Ask:
"If this number were higher or lower, would it change which strategy eventually wins — or just
change by how much?" A sharp Hero should be able to say MA1 is large enough, relative to the
guaranteed loan rate, that it plausibly *could* flip the verdict — unlike the-two-offers' MA1,
which only moved a crossover month without changing the long-run winner. See Tier 2 P5 for the
exact flex range that flips it.

## Data Deep Dive

Now, and only now, open Appendices A–C and work D1–D4. Cold-call for D3 specifically — this is
where a Hero who correctly built the D1 ledger but never named the marginal-rate discontinuity
explicitly will describe the match as if it applies smoothly to every dollar, rather than stopping
abruptly at the cap.

**Facilitator-only arithmetic note.** Shared 6%-plus-match stream: $6,546.96/yr at the assumed 10%
market rate over 10 years → $104,341.68. Match & Move's extra 9%-of-salary stream ($6,546.96/yr) at
the loan's guaranteed 6.39% → $87,891.05 (Total A = $192,232.73). Stack & Grow's full 15%-plus-match
stream ($13,093.92/yr) at 10% → Total B = $208,683.36. Margin: B wins by $16,450.63 (8.56%). Full
derivation in `case.json.balance.margin_basis`.

## Twist

**Twist: N/A.** This case's tension is a genuine, already-fully-disclosed sensitivity built into
Appendix C's MA1 (the assumed market growth rate) — the case already tells the Hero this figure is
an assumption about the future, not a fact, and inviting them to challenge it (Challenge 2 permits
this explicitly). Introducing a real, held-back Twist here would require either (a) revealing the
margin's size/direction ahead of D3/D4, which case-write's balance rule forbids, or (b) inventing a
new unsourced fact (a hypothetical market crash with a specific invented percentage, a hypothetical
raise), which this case's research pass does not do. D3's marginal-return reveal (many Heroes
expect "getting the match" to feel like one continuous benefit; the real math shows an abrupt,
discontinuous drop in return right at the cap) already produces the surprise-and-recompute moment a
Twist is meant to create, without adding new information — treat that reveal as carrying the Twist's
weight instead, per the-two-offers' identical precedent.

## Immediate recommit

Right after D3's marginal-return table lands on the board, ask by name: "The return on the dollar
right below the cap and the dollar right above it — how different are those two numbers? Did you
expect the drop to be that abrupt?" Many Heroes who voted Stack & Grow at Anchor 1 on a "more in the
401(k) is always better" instinct will not have separated the matched dollars from the unmatched
ones; conversely, a Hero who voted Match & Move expecting "no match = no point contributing more"
should recompute once D4's total shows Stack & Grow still wins on the case's stated assumption.

## Deep conflict — two threads (20–30 min)

1. **"Free money" only applies to some of the dollars, not all of them.** Walk the room through
   why the match cap creates a hard line: dollars below it are categorically different (matched)
   from dollars above it (not matched). A Hero who has not internalized this will keep describing
   the whole contribution as uniformly "getting free money" — see the case's named failure mode
   below, in its own section.
2. **A guaranteed return versus an uncertain one.** Push past "the market usually beats loan
   interest rates" to the harder point: Match & Move's loan-interest-avoidance return is
   *guaranteed*; Stack & Grow's market return is an *assumption* (MA1), even when grounded in real
   historical averages. Ask: "Does a guaranteed smaller return ever beat an uncertain larger one?
   What would have to be true about Devon's own risk tolerance for that to matter?" **Facilitator-only:**
   Tier 2 P5 found the verdict actually does flip under a realistic flex — if MA1's assumed 10%
   market rate is 50% lower (5%), Match & Move wins with a 3.37% margin, and the breakeven market
   rate is exactly 6.39% (the loan's own rate) — mathematically necessary, since at that rate the
   extra dollars grow identically wherever they're placed. Do not state this breakeven number to
   the room; use it only to gauge whether a Hero's own challenge to MA1 in discussion is
   quantitatively serious or just a gut objection.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — read both strategy nicknames with no numbers, cold-call for a gut read |
| 3:00–10:00 | Position defense — *"Walk us through your D1 ledger for your chosen strategy — how much of each paycheck is matched, and how much isn't?"* |
| 10:00–15:00 | Pressure-test the process — *"Which of your D1 numbers, if it changed, would move your D3 marginal-return table — and which would only change your D2 totals?"* |
| **15:00** | **DROP THE TWIST (N/A — instead, land the D3 marginal-return reveal)** — the return drops abruptly from a matched rate to an unmatched rate right at the cap, sharper than most rooms expect |
| 15:00–20:00 | Immediate recommit — does the marginal-return discontinuity change anyone's vote |
| 20:00–30:00 | Threaded deep conflict (the cap line; guaranteed vs. uncertain return) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

A Hero treats the employer match as if it applies at a flat, uniform rate to *every* dollar
contributed, rather than only to dollars up to the cap. This produces an overstated benefit for
Stack & Grow's extra contributions — a Hero who does this will credit dollars *beyond* the cap
with match money they never actually receive, making Stack & Grow look stronger than the real
data supports. The named trap in this case is exactly that failure mode: confusing "the match
rate" (which applies only below the cap) with "the return on this dollar" (which is categorically
different above the cap) — this is precisely what D3's marginal-return table is built to force a
Hero to confront explicitly, one dollar at a time, rather than average away. Appendix A's own table
layout invites this mistake, listing "Employer match rate: 50%" and "Stack & Grow contribution
rate: 15%" as adjacent rows over the same salary — a Hero racing through the arithmetic can
multiply the two directly (salary × 15% × 50%) instead of applying the 50% only to the 6% slice.

**A second, related trap found by Tier 2's fresh trap-check agent, worth watching for in D2/D4:** a
Hero who compounds Match & Move's full $6,546.96/yr "extra" stream against the loan's guaranteed
rate for all ten years, without checking that the $28,613 loan (Appendix B) would actually be paid
off in well under ten years at that payment size. The case's own Appendix C (MA3) discloses that it
deliberately keeps modeling those dollars at the guaranteed rate for the full horizon rather than
switching them onto the market rate once the loan is gone — a Hero who is not shown MA3's basis
text, or who skips it, may instead try to build a real amortization schedule and get a different,
also-defensible number. Cold-call whether a Hero read MA3's basis column, not just its "value used."

## Socratic questions

1. Your D1 ledger shows the employer match stopping at a specific dollar amount — what happens, mathematically, to the very next dollar Devon contributes after that point?
2. D3 asks for the rate of return just below the cap and just above it, side by side — why are those two numbers so different, when they're both still going into the exact same 401(k) account?
3. If the assumed market growth rate in Appendix C turned out to be wrong — too high or too low — which of your D2/D4 numbers would change, and which strategy's core argument would still hold up regardless?
4. Match & Move treats paying down the loan early as "earning" a return. Is that actually true, or is it just a way of avoiding a cost? Does the difference matter for Devon's decision?
5. Two people could look at the exact same appendix and correctly recommend opposite strategies. What is the one thing about Devon's own situation — not about the numbers in the case — that would decide which of them is right?

## Close

**VOTE AGAIN.** "Did your recommendation change — or just your confidence in the number behind
it?" Ask what math was new to each Hero, and specifically whether building the D1 ledger, the D2
projection, or the D3 marginal-return table was the step that actually changed their thinking.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes' Anchor-1 gut vote matched their post-D3 recommendation, or whether naming the
  marginal-return discontinuity explicitly flipped a meaningful share of the room.
- Whether the "the match cap is a hard line, not a gradual taper" framing landed as an obvious
  point restated with numbers, or as a genuine reframe.
- Whether any Hero challenged Appendix C's MA1 (assumed market growth rate) in Challenge 2, and
  whether they correctly identified what it does and does not change about the verdict.

## Standards Touched On

Percent; Exponent (also Power); Instantaneous Rate Of Change; How to find the percent of a number;
How to convert percents to numbers; How to evaluate an exponential expression.

## Facilitator note — sensitivity (SPEC §6)

Per SPEC §6: this case touches a real personal-finance decision (a new employee's income, debt,
and retirement savings) at comparatively low stakes — a savings-strategy choice, not illness,
death, or acute hardship. No special framing beyond normal care is required, but the facilitator
should be alert to a room where a Hero's real family financial pressure (e.g., their own or a
family member's student debt) makes the "which strategy is objectively better" framing land more
personally than expected; keep the discussion on the computable model, not on judging any Hero's
real circumstances.
