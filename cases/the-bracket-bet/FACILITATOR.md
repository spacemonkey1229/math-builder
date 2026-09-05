# FACILITATOR.md — The Bracket Bet

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Bracket Bet · **Tier:** T4 (HS-entry) · **Studio:** Adventure
**Standards:** Advanced Operations/Exponents — Exponent (also Power), Base, How to evaluate an
exponential expression, How to evaluate an expression with multiple operations with exponents
(Order Of Operations); Advanced Numbers/Percents — Percent, How to find the percent of a number
(see `case.json.standards[]` for exact ids).

**Status:** `case-research` complete (2026-09-03) — every `{{NEEDS_SOURCE}}` token in `case.json`
is resolved (`SOURCED` or disclosed `ASSUMPTION`). `margin_pct = 12.8` (Scenario 1, Roth wins) /
`2.3` (Scenario 2, Traditional wins) — see Balance argument below. Currently in `case-readiness`
remediation.

**One-line sensitivity flag (SPEC §6):** this case touches a real personal-finance decision with
mild money-stress stakes (a 24-year-old's own retirement savings, made under a real deadline
pressure). Nothing here rises to illness, death, or family hardship, but a facilitator should read
the room before pushing hard on "you only get one shot at this" framing — for some learners,
retirement-account anxiety is not abstract.

## Real-world grounding (for the facilitator's own background, not for case.md)

- This is standard, uncontroversial personal-finance content: Traditional vs. Roth IRA tax
  treatment is public IRS rule, not a modeled or disputed mechanism. The genuine uncertainty in the
  case is not "how do these accounts work" (that's fully knowable) but "what tax bracket will this
  specific person actually be in decades from now" (that's genuinely unknowable in advance).
- The folk wisdom ("Roth is just better") is real and common in personal-finance media — it is
  directionally true only under one assumption (future rate higher than today's), and false under
  the other. That asymmetry — a popular rule of thumb that is conditionally true, not universally
  true — is the entire pedagogical point of this case. See the section below (after "Five
  Socratic questions") for the specific wrong path this produces.
- A useful framing for Anchor 2: nobody in the room can look up Devon's real future tax bracket.
  This is not a research-skill gap to fix; it is a structural feature of the problem. The case
  should not let students believe more research would settle it — only a stated, defensible
  assumption can.

## Balance argument

- **Argument for A (Pay Later / Traditional):** wins whenever Devon's real future marginal rate
  turns out *lower* than today's rate. The logic: the deduction today is worth today's (higher)
  rate, while the eventual tax bite is assessed at the lower future rate on the same dollars — the
  government effectively takes a smaller cut than it would have taken today.
- **Argument for B (Pay Now / Roth):** wins whenever Devon's real future marginal rate turns out
  *higher* than today's rate. The logic: paying tax once, now, at a known and comparatively low
  rate, beats paying tax later on a much larger balance (contributions plus ~40 years of growth) at
  a higher rate.
- **The margin — RESOLVED by case-research, both scenarios real:** computed in D3/D4 as the
  after-tax value gap between the two options under each of Appendix D's two scenarios, using
  C=$3,000/yr, r=10%, n=43 years (FV ≈ $1,777,200). Under **Scenario 1** (future rate 22%, higher
  than today's 12%), **Pay Now (Roth) wins by 12.8%** — after-tax value $1,563,936 vs. Traditional's
  $1,386,216. Under **Scenario 2** (future rate 10%, lower than today's 12%), **Pay Later
  (Traditional) wins by 2.3%** — after-tax value $1,599,480 vs. Roth's $1,563,936. `margin_pct` in
  `case.json` (`12.8`) records the Scenario 1 figure of record; both margins are disclosed here
  because this case's whole design intent is that *both* are real possibilities depending on the
  assumed future bracket — a guide who only teaches the 12.8% figure has quietly resolved the
  dilemma the case is built to keep open. `margin_basis` in `case.json` records the full method;
  full arithmetic is in `RESEARCH_LOG.md`.
- **Why these two brackets (resolved research target):** Devon's current bracket verified at 12%
  (not the originally-floated 10-12% guess) against the real 2026 IRS bracket table. Scenario 1
  (22%) and Scenario 2 (10%) are the real published brackets one step up and one step down from
  12%, chosen because a two-bracket swing over a ~43-year career is a realistic income trajectory in
  either direction. Both margins (12.8% and 2.3%) landed comfortably inside SPEC §2's ~20% cap on
  the first pass — no retune of Appendix A's contribution amount or Appendix B's return rate was
  needed, and no MCS-46 waiver applies.

## Five Socratic questions

1. Your D3 table shows two different "winners" depending on which Appendix D scenario is true. Which one do *you* believe is more likely for someone Devon's age, and why does that belief — not the math — decide your recommendation?
2. If a classmate said "Roth is just always better, everyone says so," what specific row in your D3 table would you show them to prove that claim is only sometimes true?
3. Your D2 table shows Pay Later and Pay Now growing identically before any tax is applied. What does that tell you about where, exactly, the two options actually diverge?
4. D5 asks you to name the one number your recommendation depends on most. What would that number have to be, exactly, for your recommendation to flip to the other option?
5. Appendix A caps how much Devon can contribute in a single year. If that cap were cut in half, would it change which option you'd recommend, or only how large the dollar gap between them ends up being?

## The trap

A learner who assumes "Roth is just better" — common personal-finance folk wisdom — and only runs
the math under a future tax rate *higher* than today's will get a confident, correctly-computed, but
incomplete answer: Roth wins in that one scenario, and they will believe the case is settled.
The case only works if D3 forces the *lower*-future-rate scenario too, where Traditional wins by the
same underlying logic run in the other direction. A learner who skips Scenario 2 entirely, or who
runs it half-heartedly because they've already "decided," has fallen into the trap this case is
built around. The tell in discussion: ask them to defend Traditional under Scenario 2 with the same
rigor they used to defend Roth under Scenario 1 — most will not have actually done that arithmetic.

## Sensitivity note

The primary metric is *defined* as a function of the assumed future tax rate specifically because
the honest answer is "it depends." This is not a defect to manage down — it is the case's entire
reason to exist (see the concept sheet's stated 5-10% margin target). `case.json.sensitivity_note`
and `balance.candidate_rate_scenario_for_research` record the specific research direction; case.md
never states which scenario wins or by how much.

---

## Guide Notes — the anchor ladder (SPEC §7)

### Intro

Frame the format: this is a real, one-time, irreversible-for-a-year election under a
real payroll deadline, not a worksheet. Name the opener: "You have until Friday. Traditional or
Roth. Go."

### Launch

Show the Overview's two radio buttons and the coworker's line ("Roth. Everybody says
Roth.") with no numbers yet. Ask the room to react to the coworker's confidence before anyone has
seen Appendix D.

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "Is anyone courageous enough to stand with
Pay Later — the option with no visible advantage yet?" Record the split; most rooms will lean Roth
before seeing any math, which is the point.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push past "which account is better" toward "what
has to be true about the future for each option to win." Let the room sit with the discomfort that
nobody — not the facilitator, not any published source — can tell them Devon's real future bracket.
"Is 'which account is better' even the right question, or is the real question 'what am I betting
on the future to look like'?"

### Anchor 3 — WHAT IS THE PROCESS?

Before touching Appendix D's numbers, get the room to state the
actual comparison method: grow the same contribution the same way in both accounts (D1/D2), then
apply each account's real tax rule once, at the right rate, at the right time (D3). Re-ask: "Now
that we know the process, do we still think the question is 'which is better' — or 'which
assumption about the future do you believe'?"

### Anchor 4 — WHAT DON'T WE KNOW?

Name the load-bearing unknown explicitly: Devon's real future tax
bracket. "Is this an assumption we can make carefully, or are we just guessing? What would make one
guess more defensible than another?"

### Data Deep Dive

Now open Appendices A-D. Run D1-D4 as a room, or have groups report out.

### Twist

At roughly the 15-minute mark: "Congress just changed the tax brackets for the year
Devon retires — the rate you all just used for Scenario 1 or Scenario 2 no longer exists. You have
60 seconds: does your recommendation change, or was it never really about the exact number in the
first place?" This is designed to reveal whether a group's recommendation depended on the *specific*
assumed rate (fragile) or on the *direction* of the bet they were making (robust). A group whose
argument was "Roth wins because rates only go up" should be visibly shaken; a group whose argument
was "I recommend Roth because I personally expect to earn more later, and here's why" should barely
flinch — that contrast is the whole teaching moment.

The trap this Twist is built to expose is the same one named above: a learner who assumed "Roth is
just better" without ever running Scenario 2's lower-bracket case will discover, under time
pressure, that their recommendation was really riding on an unstated bet about the future, not on
the math itself.

### Close

VOTE AGAIN. "Did we ask the right question?" "What math was new to you today?" Compare
the re-vote to Anchor 1's cold vote — a shift is expected and good; no shift, with confident new
reasoning behind it, is also a legitimate outcome worth naming.

### Lessons Learned

The core transferable idea: two options can be mathematically identical in
every respect except one (D2's identical pre-tax growth), and the entire decision still rides on
that one respect — you cannot average away the disagreement, you have to actually take a position on
the unknown.

### Standards Touched On

Exponent (also Power), Base, Percent; How to evaluate an exponential
expression; How to evaluate an expression with multiple operations with exponents (Order Of
Operations); How to find the percent of a number.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00-3:00 | Cold-call launch, 30-second gut-check vote (Anchor 1) — no explanation |
| 3:00-10:00 | Position defense: "Convince us why your pick is better, not just popular" |
| 10:00-15:00 | Pressure-test: "Whose recommendation is most fragile to being wrong about the future?" |
| **15:00** | **DROP THE TWIST** — the bracket table changes; deliver slowly, with a pause before "does your recommendation change?" |
| 15:00-20:00 | Immediate recommit: who reverses, who holds? "What just broke — the number, or the reasoning?" |
| 20:00-30:00 | Threaded deep conflict — two named threads: (1) "betting on your own future income" vs. "betting on tax policy," (2) "a rule of thumb vs. running your own numbers" |
| 30:00-45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands (SPEC §7)

| Band | Typical size | What changes |
|---|---|---|
| **Full** | 12-20 (the size this case is written for) | Anchors and timings run as written above |
| **Compressed** | 6-11 | Anchors 2-3 combine into one pass; the deep-conflict section (20:00-30:00) runs one thread instead of two; total runtime shortens proportionally |
| **1:1 / pair** | 1-2 | No vote at Anchor 1 — instead ask for a stated initial position and why; the facilitator plays devil's advocate directly rather than cold-calling the room; the Twist still lands, and "who reverses" becomes "would you reverse, and why" |
