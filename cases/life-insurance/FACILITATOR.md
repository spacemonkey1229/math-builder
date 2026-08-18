# Facilitator Guide — Life Insurance

MS | Launchpad | Anchor-ladder format (SPEC.md, Section 7, "The facilitator artifacts")
**Primary metric (graded, retuned 2026-08-17 — see Sensitivity note):** whole life's strongest
real GUARANTEED claim (top of Appendix D's real, cited 2%-4% guaranteed range, 4.0%) vs. the best
available 5-year CD rate (4.50%) · **Margin:** 0.5pp / 12.5% · winner **B (term/CD)**. The raw
headline comparison Jake's browser tabs actually show — whole life's dividend-inclusive rate
(corrected 2026-08-17 to a real 6.20%) vs. the same 4.50% CD — is real, disclosed, and is what the
Twist reveals; at ~37.8% it is not close enough to be the graded margin (SPEC.md §2's 20% cap).

Legacy source: `source/Y2/Session 3/Life Insurance/Case Study_ Life Insurance Agent.docx`. The
original docx had no separate Guide Notes document — only the case text itself, which named a
real company (StateFarm) and relied on an external, non-reproducible calculator tool. This guide
is authored fresh for the anchor-ladder format, with a genuinely new, sourced Twist the original
had no equivalent of.

**Do not share this document with students before the discussion.**

---

## Intro

Frame the format: this is a decision a real family is trusting an agent to make for them, and the
room should feel the weight of "just tell us which one" before any math happens. Don't open with
rates or dollars — open with the kitchen table.

## Launch

Read the Overview aloud, or act it out — pause right where the case does, on Jake with his mouth
open, two browser tabs still open, no answer yet. Do not show Appendix D's rate data yet.

## Anchor 1 — TAKE A STAND AND VOTE

"Is anyone courageous enough to stand with Jake on whole life?" Cold-call for a vote, no reasoning
allowed yet. Write the split on the board (e.g., "6 whole life / 11 term / 3 unsure").

## Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

"What are we actually trying to find out here?" Let it get messy. Some rooms will land on "which
is cheaper" immediately — push back gently: cheaper *per what*? Per month? Per dollar of coverage?
Per dollar eventually returned to the family? Let the room sit with the fact that "cheaper" is not
yet a well-defined question.

## Anchor 3 — WHAT IS THE PROCESS?

"If we had the data, how would we actually decide?" Push for a concrete comparison, not a vibe.
Re-ask Anchor 2's question once a process is on the board: "Given this process, is our question
still the right one?"

## Anchor 4 — WHAT DON'T WE KNOW?

"What are we assuming? Which assumptions are load-bearing?" Surface, without confirming or denying
yet: do we know exactly how much coverage the Fawsons need? Do we know what rate whole life's cash
value actually earns? Bank these — Anchor 4's questions are exactly what Appendix D's Modeling
Assumptions (MA1–MA5) answer.

## Data Deep Dive

Now, and only now, hand out Appendices B, C, and D. Let Heroes work D1 (coverage need) and D2/D3
(term total premiums; whole life's recursive-to-explicit cash-value projection) before revealing
anything about D4's rate framing.

## Twist

**Drop this at roughly the 15-minute mark**, slowly, with pauses — after the room has worked D4's
rate comparison (whole life's headline 6.20% dividend-inclusive rate vs. 4.50% CD) and likely
landed on "whole life clearly wins, it's the higher rate."

> "One more thing. That 6.20% number isn't guaranteed. It's a **dividend** — declared year to
> year by the insurer, based on how the company's investments and mortality experience actually
> performed that year. In a bad year, it can be cut, or paid as zero. The CD's 4.50% is nothing
> like that: it's contractually fixed and federally insured for the full five years, no matter
> what happens. If you strip the dividend out and compare only whole life's *guaranteed* range —
> a real 2%–4%, published by the same source — to the CD's 4.50%, does your Step 4 comparison
> still favor the same option? Even at the very top of that guaranteed range (4%), the CD is
> still higher."

**What this invalidates:** the popular position that "whole life's headline rate makes it the
clear winner." That position was built entirely on treating a non-guaranteed dividend rate as if
it were as solid as a federally insured CD rate — once the room sees those two numbers are not
the same *kind* of number, and that the actual guaranteed floor (2%–4%) never beats the CD, the
comparison that looked like a landslide a minute ago reverses.

**The follow-up (the whole point):** *"What just broke in your model? Were you wrong, or just
missing information?"* Push the room toward the deeper, still-undisclosed-until-now number: the
actual whole life premium this family would pay is roughly **12 times** the term premium for the
same coverage (`sensitivity_model.py:derived_dollar_picture()`). Even a Hero who now correctly
distrusts the 6.20% headline rate and lands on term/CD should still see that the rate comparison,
at any of its readings, was comparing returns on two very differently sized pools of money.

**Soundness check (SPEC.md §6 / case-write §11):** read sequentially — the room works D1→D4 in
order, reaches a rate-based position, then the twist drops directly against the number just used.
Sound. Read simultaneously — a Hero who reads every appendix at once before forming any position —
Appendix D never states that dividends are non-guaranteed anywhere in `case.md`; that fact lives
only in this document. So even a "read everything first" Hero has no way to derive the twist from
the case text alone, and it still lands as genuinely new information under this reading too. The
twist does not depend on any convention `case.md` leaves ambiguous — it is a single, independently
true fact about how participating whole life dividends work, not a reinterpretation of a number
already given. Checked and confirmed sound under both readings.

## Close (10 minutes left)

VOTE AGAIN. "Did we ask the right question? Who's changing their answer, and why?" Ask specifically
who moved *because of the 12-to-1 dollar gap* versus who moved *because of the dividend/guarantee
distinction*. Those are two different kinds of "wrong" and worth distinguishing out loud.

## Lessons Learned

Three numbers, three different stories: the "obvious" headline rate comparison (6.20% vs. 4.50%,
favors whole life), the guaranteed-only comparison (2%–4% vs. 4.50%, favors the CD), and the
*full-cost* picture (roughly 12x more premium dollars for whole life, favors term regardless of
rate). All three are real. None of them alone answers the question the Fawsons are actually
asking Jake: which option leaves their family better off. A rate comparison that looks like a
landslide can flip once you check what's actually guaranteed — and even a guaranteed comparison
can hide a much larger, unclose dollar gap. That layered distinction is the transferable skill,
and it shows up constantly outside insurance too, anywhere a rate of return is quoted without also
stating whether it's promised and how much money it's actually earning on.

## Standards Touched On

See `case.json.standards[]` and the case.md Appendix E "How To…" list — generated mechanically
from `readmodel/standards_spine.json`, not retyped by hand.

---

## Five Socratic questions

1. Jake's rate comparison shows whole life's headline return (6.20%) is actually higher than the best CD rate (4.50%) — if that's true, why would anyone ever recommend term instead?
2. The whole life premium is roughly 12 times the term premium for the same $1,300,000 of coverage — if whole life's return is well above a CD's, where does all that extra premium money actually go?
3. The CD's 4.50% is guaranteed by federal deposit insurance for five years — what, specifically, guarantees whole life's 6.20%, and what happens to your Step 4 answer once you find out it's a real 2%–4% instead?
4. Neil's income is projected to grow 4.8% a year, but D1 sizes the coverage using his income today — if Neil's real income is meaningfully higher by year 15, does a policy sized today still cover the family's real need?
5. If the Fawsons genuinely can only afford term's monthly premium, not whole life's, does the rate-of-return comparison from D4 matter to their decision at all?

## The trap, named explicitly

Most students will only compare the two *headline* rates in D4 (6.20% vs. 4.50%) and conclude
whole life is the clear winner. That comparison is real and correctly computed, but it silently
assumes a non-guaranteed, year-to-year dividend declaration is as solid as a federally insured CD
rate — the
case's own real, cited guaranteed-rate data (2%–4%) shows the CD winning once the dividend is
stripped out. Layered on top of even that guaranteed-vs-guaranteed reading is a second trap: the
two options are not growing the *same size pool of money* — whole life's cash value compounds
from a base funded by a premium roughly 12 times larger than term's. "Which rate wins" and "which
option leaves the family with more usable money" are two different questions that can point in
different directions depending on which real number a Hero trusts. Facilitators should let a room
reach the headline-rate conclusion out loud before the Twist corrects it to the guaranteed
comparison, then let the dollar-gap reveal complicate it a second time — that double reversal is
the case's real payoff.

## Sensitivity note

This case touches money stress — a young family with two small children weighing how to protect
against a parent's death — but contains no death-toll optimization: the math never asks a student
to treat Neil's death as an abstract quantity to optimize, only dollar and percentage comparisons
on financial products (SPEC.md §6). Facilitators should name this plainly at the Intro so the room
understands why the case takes the framing it does.

**Retuned 2026-08-17 (P6 fix):** `sources[] S3`'s old "4.65% average dividend-inclusive crediting
rate" claim was unsupported by its own live source page (re-fetched 2026-08-17: 5 real 2026
carrier rates, 5.75%–6.60%, no stated combined average; case-computed average 6.20%). That
correction pushed the raw D4 rate gap to ~37.8%, past the SPEC.md §2 20% cap, so the **graded**
primary metric moved from `dividend_inclusive_rate` vs. `cd_rate` to `guaranteed_rate_ceiling` vs.
`cd_rate` — see the case.json.balance.margin_basis rationale (also copied into case.md's Balance
Argument section). `evaluate()`/`evaluate_twist()` swapped roles in `sensitivity_model.py` to
match: the base metric is now the guaranteed comparison, and the Twist reveals the (now correct)
6.20% headline dividend rate.

**Assumption-sensitivity disclosure:** Per `sensitivity_model.py`, `FLEX[]` now contains
`guaranteed_growth_rate` (MA5), `cv0_multiple_of_premium` (MA4), and `guaranteed_rate_ceiling`
(which end of the real 2%–4% guaranteed range is graded) — never the cited market rates
(`dividend_inclusive_rate`, `cd_rate`), which Tier 2 probe 6 stress-tests instead, per SKILL.md's
"only FLEX[] is swept by default" rule.

**Tier 2 probe 5 result (2026-08-17, `--flex 0.5`, re-run after the retune):** Base: A=4.0%,
B=4.5%, winner **B**, margin **12.5%** (under the 20% cap). `guaranteed_growth_rate` and
`cv0_multiple_of_premium` flexed ±50%: winner and margin unmoved (12.5%) in all four runs — D3's
cash-value dollar figures move, the D4 rate margin does not, since neither dial feeds it.
`guaranteed_rate_ceiling` flexed ±50%: at **+50%** (to 6.0%) the winner **flips to A**, margin
33.3% (breaks the cap); at **-50%** (to 2.0%) the winner stays B but margin balloons to 125%
(also breaks the cap). Both are real, disclosed instabilities
(`case.json.sensitivity_disclosure[]`, param `guaranteed_rate_ceiling`, category I) — not a model
bug: the +50% flip is structurally the same real number as the Twist's 6.20% dividend rate.
Verdict: **PASS (disclosed)**, not stable-margin PASS. Facilitators should not defend the base
12.5% margin as immovable — name the real instability if a room pushes on "well, what if the
guaranteed rate really is closer to 6%."

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00-3:00 | Cold-call launch (Overview read/acted aloud), 30-second commitments, stand/sit vote — no explanation (Anchor 1) |
| 3:00-10:00 | Position defense: "Convince us why it's better, not just fair" (Anchors 2-3, define the real question and a process) |
| 10:00-15:00 | Pressure-test the models: hand out Appendices B/C/D, let D1-D4 develop |
| **15:00** | **DROP THE TWIST** — delivered slowly, with pauses |
| 15:00-20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00-30:00 | Threaded deep conflict: (1) rate-of-return thinking vs. raw-dollar-cost thinking, (2) how much a guarantee should be worth in a financial decision |
| 30:00-45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands

See `case.json.cohort_bands[]` (Full 12-20 / Compressed 6-11 / 1:1-pair 1-2) — three bands
declared per the cohort-bands floor in SPEC.md's "Cohort bands" subsection of Section 7.
