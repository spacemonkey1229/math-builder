# Guide Notes: The Curve's Turn

**Case:** The Curve's Turn · **Tier:** T4 · **Band:** HS · **Studio:** Heroes Academy
**Standards:** Calculus / Applications Of Derivatives (the complete group, 7 skills) + Calculus /
Derivatives (6 of 9) — all thirteen `new_coverage` (see `case.json.standards[]` for the exact ids)

Researched and margin-resolved 2026-08-12. Current `margin_pct` = **11.68** (see
`sensitivity_model.py` and `case.json.derived`). Every figure below is also in `case.md` or
`case.json`; if you find one here that is not, that is drift and a defect, not a shortcut. This file
is re-checked at every readiness run by the continuity checks in `case-readiness`.

## Intro

Frame the format before anything else. This is not a modelling exercise with a story on it — it is
a recommendation a named person has to sign, in a room, tonight. Name the opener: "You are the one
who has to give the board a date. Not a range. A date." Then say the thing the room needs to hear
before it can think: nobody in this case is asked to price a life. The board's own metric counts
transmissions prevented, and that is the whole of it.

## Launch

Put the twelve reported weekly counts from Appendix B on the screen as bare points — no fitted
curve, no labels beyond the week. Ask one question and take no answers longer than a sentence:
*"Has this turned yet?"* Let people argue about what "turned" even means. Do not define it. Do not
draw the curve.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Dr. Vance and close the schools tomorrow, before the
case rate has crossed anything at all?" Hands up, both options, no discussion. Record the count —
Close asks the room to vote again, and the comparison is the point.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'the curve turned'?"**

Let the confusion grow here; it is the most valuable stretch in the session. Heroes will reach
straight for "are cases going up." Push: "Going up is a *level*. Dr. Vance's whole case is about a
*rate*, and her opponent's whole case is about a *level*. Which one is 'has it turned'?" A room that
gets to "there are three different things here — how many, how fast, and how fast the how-fast is
changing — and they can each turn at different times" has done the real work. Wow, this is a
challenging problem.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Only once the room has separated level from rate from acceleration, ask them to name the steps
before touching an appendix: accept the fitted model and check it (D1), differentiate it (D1), read
the instantaneous rate at the decision week and the tangent line it implies (D1, D2), find the
critical points on a wave that has already finished so you can see what a turn actually looks like
(D3), find the second derivative's sign change on the wave you are actually in (D4), ask
retrospectively when you *should* have closed last time (D5), and only then total the two plans
(D6). Re-ask: "Is our question still the right question, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the honest gaps. Appendix F carries nine stated assumptions and they are not equal:

- **MA2, the board's 500-per-100,000 level, decides the case.** It is not swept in probe 5 because
  halving a plan's own written trigger makes it a different plan — but the sweep is disclosed
  anyway, and Heroes should see it: at 250 the Tripwire fires in the same week as the Early Brake
  and wins by 10.0%; at 750 the forecast never reaches it, the Tripwire never fires, and the Early
  Brake wins by 42.41%. This one number is where the case actually lives.
- **MA6, the transmission coefficient `k` = 0.5, changes nothing at all.** Both plans scale
  linearly in it, so the margin is 11.68% at 0.25, at 0.5 and at 0.75. A Hero who works that out
  has understood something about ratios that most adults in this argument have not.
- **MA7, the screening removal rate 0.10, is the biggest genuine estimate.** Flexed to 0.05 the
  margin widens to 16.33%; flexed to 0.15 it narrows to 6.48%. The winner never changes.
- **MA8, the chain multiplier, is a modelling choice and not a measurement.** Flexing `g` by half
  gives 7.76%, by half again upward gives 15.61%.
- **MA9, the zero-reporting-lag timing convention, is the seam.** Appendix D scores the Tripwire as
  closing the week its level is crossed — the reading most generous to it. Charge it a one-week
  reporting lag and it closes weeks 15 and 16, leaves **41.5402** and loses by **21.56%**, past this
  project's own 20% balance cap. A Hero who raises this is right, and the honest answer is that the
  case scores both plans on the same clock and that no reactive rule really gets that clock.

Then the harder one: the fitted cubic itself is neither a stated assumption nor a citation. It is a
*choice*. Ask what would have changed if the epidemiologist had fitted a straight line, or an
exponential, or nothing at all.

## Data Deep Dive

Now, and only now, the numbers.

**The current wave.** `D(t) = 0.2174 t^3 - 1.8006 t^2 + 25.3255 t + 247.9597`, so
`D'(t) = 0.6522 t^2 - 3.6012 t + 25.3255` and `D''(t) = 1.3044 t - 3.6012`. The second derivative
changes sign at **t = 2.7608**, between the weeks ending 2021-10-20 and 2021-10-27 — the curve
turned roughly two months before this board meeting, which is the whole of Dr. Vance's case. At the
decision week, `D(11) = 598.027` and `D'(11) = 64.6285` cases per week per week, against an average
rate of change of only **37.5** across the last two reported weeks: the instantaneous rate is
nearly twice the recent average, and a Hero who reports the average as if it were the rate has
missed the point of D1.

**The tangent line.** `y = 64.6285 t - 112.8865`. It reaches the board's level (818.87 cases) at
**t = 14.4171**, while the curve itself gets there at **t = 13.7293** — the straight line promises
about **0.6878** of a week the district does not have. That gap is small, and it is small *because*
the curve is concave up; say so.

**The previous wave.** `P(t) = -0.3348 t^3 + 8.9975 t^2 - 42.0177 t + 38.2994`. Critical points at
**t = 2.7602**, a local minimum whose fitted value is **-16.17**, and **t = 15.156**, a local
maximum at **302.67** — the week ending 2021-09-15. Its inflection is at **t = 8.9581**.

**Facilitator-only geometry note.** The negative local minimum is not a bug in the case, it is the
case. A cubic fitted to a real epidemic trough returns a number of cases that cannot exist. Let a
Hero find it. If nobody does, ask directly: "Your model says the county had minus sixteen cases
that week. Do you believe your model?"

**D5's answer, and the gift in it.** `G(w) = P(w) + P(w+1)`, so `G'(w) = P'(w) + P'(w+1) = 0` at
**w = 14.6358**, with `G = 602.24` — a maximum by the first derivative test, sitting **5.6777**
weeks after that wave's concavity turned. And the previous wave never crossed the board's level at
all: it peaked at a fitted **302.67** cases against a level of **818.87**. A district on The
Tripwire would have spent nothing that entire autumn.

**The decision table.**

| t | week ending | D(t) | R(t) | w(t) | X(t) |
|---|---|---|---|---|---|
| 12 | 2021-12-29 | 668.25 | 408.03 | 7.8744 | 16.0649 |
| 13 | 2022-01-05 | 750.52 | 458.26 | 6.2039 | 14.2152 |
| 14 | 2022-01-12 | 846.14 | 516.65 | 4.6964 | 12.1321 |
| 15 | 2022-01-19 | 956.43 | 584.0 | 3.3359 | 9.7407 |
| 16 | 2022-01-26 | 1082.68 | 661.08 | 2.1081 | 6.9681 |
| 17 | 2022-02-02 | 1226.21 | 748.72 | 1.0 | 3.7436 |

No action leaves **62.8646**. The Early Brake closes weeks 12 and 13 and leaves **32.5844**. The
Tripwire's level is crossed at **t = 14**, so it closes weeks 14 and 15 and leaves **36.8926** —
**11.68%** worse. The rates at the edges of the two closure windows are `D'(12) = 76.03` and
`D'(13) = 88.73` for the Early Brake against `D'(14) = 102.74` and `D'(15) = 118.05` for the
Tripwire: the Tripwire closes on *more* cases per week and still loses, because its chain
multipliers are smaller. That sentence is D6, and it is the sentence to fish for.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses. This is not a hypothetical; it is what the county's reported series
actually did in the six weeks the case document stops short of.

"Six weeks on, the county's own reported series is in front of you. Week twelve came in at **896**,
not the fitted **668.25**. Week thirteen at **1,732**. Week fourteen at **3,612** — more than four
times what your cubic said, and the crest, after which it fell away."

"Run your board's rule against those numbers and the tripwire trips in week **12**: the very week
The Early Brake would already have shut the doors."

Then the question: **"What just broke in your model — and were you wrong, or were you only missing
information?"**

**Facilitator-only: what the numbers actually do.** `evaluate_twist()` re-runs the whole table on
the real observed counts, and credits each prevented transmission with the chain the county
*actually* went on to have — realised week-to-week ratios, which fall below one after the peak —
instead of the planning growth rate. The verdict flips. No action leaves **145.2031**; The Early
Brake leaves **67.9992**; The Tripwire leaves **61.1993**, and now wins by **10.0%**. The model
under-called the peak week by a factor of **4.27**.

**Facilitator-only: what the reversal actually rests on.** Two checks, both worth having in your
pocket. (1) It is *not* the chain-multiplier convention: re-run the twist on the real rates but keep
MA8's planning-`g` chain and The Tripwire still wins by **10.00%**. (2) It *is* the MA9 zero-lag
convention: charge the Tripwire a one-week reporting lag on the real counts and it closes weeks 13
and 14, leaving **68.4202** against The Early Brake's **67.9992** — a **0.62%** margin the other
way, and the reversal is gone. If a Hero raises the lag after the twist lands, say so plainly. The
twist is a lesson about model error, not a proof that The Tripwire was right.

The lesson is sharper than "the model was wrong." Under the real data both plans close in the same
week, so the earliest-warning advantage — the entire argument the room just spent a quarter of an
hour on — was worth exactly nothing, and the only thing separating the two memos was the screening
programme one of them declined to run. **A twist that destroys the reason without destroying the
answer is the hardest kind to sit with, and that is the one to press on.**

## Immediate recommit

Re-vote at once. Ask by name: "Does that change your vote, or only your confidence?" Then the
follow-up that matters more: "Whose argument survived the reveal *for the reason they gave*, and
whose survived by luck?"

## Deep conflict — three threads (20-30 min)

1. **Rate versus level.** One plan watches how fast the number is changing; the other watches the number. Is a rule you can only evaluate by fitting a curve a legitimate basis for a public decision a parent has to be able to check?
2. **Spending an irreversible budget.** The board authorised one closure for the term. Does a plan that keeps something in reserve deserve credit the board's own metric does not give it — and if so, is the metric wrong?
3. **The model's own honesty.** The previous wave's fitted model returns **-16.17** cases at its local minimum. Does that disqualify the model, disqualify one deliverable, or disqualify nothing at all?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — bare points on screen, "has this turned yet", 30-second commitments, stand/sit vote, no explanation |
| 3:00–10:00 | Position defense — *"Convince us it's better, not just more careful"* |
| 10:00–15:00 | Pressure-test the models — *"Whose number is most fragile, and which assumption breaks it?"* |
| **15:00** | **DROP THE TWIST** — the reported series after the decision week, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and did their reason survive or only their answer |
| 20:00–30:00 | Threaded deep conflict (rate versus level; spending an irreversible budget; the model's own honesty) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes will read "concave up" as a restatement of "cases are rising," treat the second
derivative as decoration, and argue for The Early Brake on the level alone — never noticing that
the entire quantitative case for acting early lives in the chain multiplier column, not in the case
count. They will produce a pitch that is right about the recommendation and wrong about the reason,
which is exactly what a cold solve is supposed to catch. Watch for a decision table with a `D(t)`
column and an `R(t)` column and no `w(t)` column: that Hero cannot explain why closing on
**16.0649** and **14.2152** beats closing on **12.1321** and **9.7407** when the second pair sits on
the higher case counts.

The same Hero will report the previous wave's local minimum of **-16.17** as a case count without
noticing it could not be one. Do not correct this in the deep dive; let it reach the pitch and let
a peer find it.

**A second wrong path, and this one the case invites.** D2 asks which of the tangent line and the
curve a Hero would defend. A Hero who answers "the tangent" and then stays consistent will read the
Tripwire's crossing week off the tangent (**t = 14.4171**) rather than off the curve
(**t = 13.7293**), close weeks 15 and 16 instead of 14 and 15, and report the Tripwire at
**41.5402** and a margin of **21.56%** instead of 36.8926 and 11.68%. That is not sloppiness — it
is a defensible chain of reasoning that lands on a different number, and it is arithmetically the
same window a one-week reporting lag produces (MA9). Do not mark it wrong. Ask which object the
board's rule is written against, and make the room notice that the answer changes the margin by ten
points.

## Socratic questions

1. What is the difference, this week in this county, between "cases are rising", "cases are rising faster", and "cases are rising faster than they were rising" — and which of the three did the board actually write into its rule?
2. The chain multiplier falls from 7.8744 to 1.0 across the horizon while the case rate climbs from 408.03 to 748.72. What would have to be true about the growth rate for those two to cancel exactly, and what does it mean for the decision that they very nearly do?
3. The transmission coefficient `k` is a stated assumption of 0.5 with a real range behind it of roughly 0.3 to 0.8 — show what the margin does when you halve it and when you multiply it by 1.5, and then explain why?
4. The Tripwire's whole advantage is a screening programme whose removal rate of 0.10 is assumed, not measured — how far would it have to move before you changed your recommendation, given the margin is 16.33% at half that value and 6.48% at one and a half times it?
5. The board authorised one closure for the term, and the previous wave never crossed its written level once, peaking at a fitted 302.67 against 818.87. If you spend the budget now and the wave turns out three times larger in six weeks, what exactly have you lost — and does the board's metric charge you for it?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's. A room that did not
move at all after the twist is worth asking about directly: did the reveal not land, or did the
room already have the right structure built in?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether the second derivative landed as a real quantity about a real curve, or stayed a rule
  about polynomials.
- Whether the chain multiplier read as a modelling choice a Hero could argue with, or as arithmetic
  handed down.
- Whether the twist produced reasoning about model error, or only relief that the vote was safe.
- Whether anyone found the negative local minimum without being pointed at it.

## Standards Touched On

Derivative · Instantaneous Rate Of Change · Tangent Line · Differentiable · Critical Point · Local
Maximum · Local Minimum · Concavity · How to find a derivative using the power rule · How to find
the equation of a tangent line at a point · How to find critical points of a function · How to use
the first derivative test to classify a critical point · How to solve an optimization problem using
derivatives

## Facilitator note — sensitivity

**Required (SPEC §6).** This case is built on a real respiratory-illness wave and on a school
closure. Some Heroes in the room lost school time, and some lost people. The framing is deliberately
administrative and protective — transmissions prevented, instructional days spent — and at no point
is anyone asked to optimise a death toll or price a life. Note that Appendices A and B carry real
death counts as columns the case does not use; that is deliberate filtering practice, and it is also
a column some Heroes will read twice. Flag the topic before the Launch, in plain words, and make it
easy and unremarkable for anyone to step out. If a Hero brings a personal story into the room, let
it be a story; do not turn it into a data point.
