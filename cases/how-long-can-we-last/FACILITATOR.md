# Guide Notes: How Long Can We Last

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — the
balance argument, margin, and sensitivity notes live only here and in `case.json`'s `balance`
object.*

**Case:** How Long Can We Last · **Tier:** T2 · **Band:** MS-core · **Studio:** MS Adventure
**Standards:** Advanced Numbers/Measurement — `advanced-numbers-percent`,
`advanced-numbers-how-to-convert-numbers-to-percents`,
`advanced-numbers-how-to-find-the-percent-of-a-number`,
`advanced-numbers-how-to-find-a-whole-given-the-percent-and-the-part-of-the-whole`,
`measurement-ratio`, `measurement-proportion`,
`measurement-how-to-find-a-missing-amount-in-a-proportion` (all already n>0 in the spine; this case
reinforces the group's two thinnest skills — see `case.json.reinforcement_note` — while closing the
emergency-fund-sizing topic gap named in `case.json.topic_gap_closed`).

**Status:** Researched 2026-09-04. Numbers below are the real, sourced/assumed figures — never
state them, or the margin's size/direction, inside `case.md`.

## The real numbers (facilitator reference — never appears in case.md)

- Essential monthly expenses: $5,874 (Appendix A, BLS CES 2024).
- Renata's fixed monthly income: $2,983 (Appendix B, BLS OOH).
- Julian's typical monthly freelance income: **$3,600** — the D2 answer key ($756 ÷ 21% = $3,600).
  Never state this number in case.md; it must be derived by the Hero.
- Normal-month household surplus: $2,983 + $3,600 − $5,874 = **$709/month** — the amount they want
  to start investing once the fund target is reached.
- Documented dry spell (MA2): 7 consecutive months at $0 Julian income. Monthly shortfall during
  the dry spell = $5,874 − $2,983 − $0 = **$2,891/month**.
- **Fund A (Rule-of-Thumb):** 3 × $5,874 = **$17,622**.
- **Fund B (Real-Stretch):** 7 × $2,891 = **$20,237**.
- **Fund A's actual coverage:** $17,622 ÷ $2,891 = **6.10 months** — 87.1% of the 7-month dry
  spell. It runs dry with about 0.9 months (≈27 days) of the dry spell still remaining.
- **Fund B's actual coverage:** $20,237 ÷ $2,891 = exactly **7.0 months** — 100% of the dry spell,
  by design.
- **Margin:** ($20,237 − $17,622) / $17,622 × 100 = **14.84%** (`case.json.margin_pct` = 14.84,
  inside the SPEC §2 20% cap and inside the case's 10–15% target range).
- **Why this stays a genuine two-sided case, not a landslide:** Option A is not a strawman — it
  covers 87% of the real dry spell and is the standard, universally-cited number, and it frees up
  $2,615 to start investing today. Option B does not require a dramatically larger sacrifice
  (14.8% more) for that last 13% of protection. Both arguments are quantitatively live.

## Intro

Frame the format before anything else: this is a real household deciding, this week, whether to
stop saving and start investing. Name the opener — "You're Renata Osei. You've already hit 'the
number' everyone quotes. Tonight you have to decide whether that's actually true for your
household, or just a number you copied." Let the stakes land before moving to the Launch.

## Launch

Read the two fund nicknames out loud with no numbers attached — the Rule-of-Thumb Fund and the
Real-Stretch Fund. Ask: "If all you knew was those two names, which one sounds like the 'correct'
amount of caution, and which sounds like it might be overthinking it?" Take answers without
correcting anyone. Most rooms will initially treat "Rule-of-Thumb" as obviously sufficient (it's
the famous number) and "Real-Stretch" as excessive caution — record that instinct, because the
case's job is to test it against this household's actual documented pattern.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the Real-Stretch Fund — the one that means saving
longer before you get to invest anything?" Show of hands, both options, no discussion. Record the
count — Close will ask again.

## Anchor 2 — What is the problem we're solving?

**"Is 'which fund is bigger' the right question?" · "What do you mean by 'enough' — enough to
match a rule you read online, or enough to survive what this specific household has actually
lived through?"**

Push the room to state the actual metric before touching an appendix: not "which number is
bigger" and not "which one is safer in general," but *months of real coverage against this
household's own documented dry spell.* If the room lands on "we can't answer this without knowing
how long Julian's dry spells actually run, and how much of the bill Renata's income alone can
carry," the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Make the room name the steps before opening an appendix: (1) find the household's essential
expenses and Renata's fixed income (Appendices A–B), (2) derive Julian's typical income from the
percent relationship given, not by looking it up (D2), (3) size both funds using a proportion —
Option A off total expenses, Option B off the actual monthly shortfall during a $0-Julian-income
stretch (D3), (4) test each fund's actual months of coverage against the 7-month documented dry
spell and convert that to a percent of the stretch covered (D4). Re-ask: "Now that we can see the
steps, is our question still the right one?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the two honest gaps: MA1 (Julian's 21%-of-typical slow month) and, far more importantly,
MA2 (the 7-month, $0-income dry spell). Neither is sourced from an outside publication — both are
stated modeling assumptions with a real basis named in Appendix D. Ask: "If the real dry spell
were shorter — say 5 months instead of 7 — would Option A's answer change? What about if it were
longer, say 9 months?" A sharp Hero should be able to say Option A's *coverage percentage* changes
continuously with the dry-spell length, and there is a specific length at which Option A stops
being "close" and starts being "clearly insufficient."

**Facilitator-only sensitivity disclosure (Tier 2 probe 5, `sensitivity_model.py`).** This case's
verdict genuinely depends on MA2 and does not survive a full ±50% swing without changing: at 3.5
months (−50%), Fund A alone already covers 174% of the stretch — *more* than enough, which would
flip the recommendation toward Option A (same protection, far less cash tied up). At 10.5 months
(+50%), Fund A covers only 58.1% of the stretch and the fund-size gap balloons to a 72.26% margin,
well past the SPEC §2 20% cap that governs the case as authored. The case is balanced and
authored at exactly 7 months because that is this specific household's own documented worst dry
spell (Appendix C), not a free dial — but a facilitator should not defend the 14.84% margin or the
87.1% coverage figure as though they were unconditionally true regardless of dry-spell length. If a
Hero pushes on "what if it were shorter/longer," the honest answer is "then a different option
would genuinely be correct," not "the answer doesn't change."

## Data Deep Dive

Now, and only now, open Appendices A–D and work D1–D4. Cold-call for D2 specifically — this is
where a Hero who never sets up "part = percent × whole, solve for whole" will be stuck with no
numeric answer at all, only a guess, and it is the deliverable most likely to be skipped or
answered by guessing (see the named wrong-path section further below).

**Facilitator-only arithmetic note.** D2: $756 ÷ 0.21 = $3,600. D3: Fund A = 3 × $5,874 = $17,622;
Fund B = 7 × ($5,874 − $2,983) = 7 × $2,891 = $20,237. D4: Fund A coverage = $17,622 ÷ $2,891 =
6.10 months = 87.1% of 7 months; Fund B coverage = $20,237 ÷ $2,891 = 7.00 months = 100%.

## Twist

**Twist: N/A.** This case's tension is a genuine, already-fully-disclosed sizing problem (a flat
rule vs. a rule calculated from this household's own documented pattern) that resolves entirely
through the proportion/percent work Challenge 3 already requires — there is no additional
real-world fact withheld from Appendices A–D whose reveal at the 15-minute mark would invalidate a
popular position without either (a) leaking the margin's size/direction into case.md, which
`case-write`'s balance rule forbids, or (b) inventing a number the research pass didn't source or
disclose as an assumption, which this case does not do. The D4 survival-test reveal — many rooms
expect the famous "3 months" number to comfortably cover any realistic dry spell; the real
coverage is 87.1%, not 100% — already produces the surprise-and-recompute moment a Twist is meant
to create, without adding new information. See Anchor 4 and Immediate Recommit below, which the
facilitator should treat as carrying that weight instead.

## Immediate recommit

Right after D4 lands on the board, ask by name: "Option A covers 87% of the documented dry spell —
not 100%. Is that closer to 'basically fine' or 'a real gap' than you expected before you did the
math? Does it change your vote?" Many Heroes who voted for the Rule-of-Thumb Fund at Anchor 1 on a
"it's the famous number, it must be enough" instinct will not have realized it falls short of this
specific household's own documented pattern; conversely, a Hero who voted Real-Stretch expecting
Option A to be dramatically inadequate should recompute in front of the room and see it's actually
fairly close (87%, not, say, 50%).

## Deep conflict — two threads (20–30 min)

1. **A rule that fits "households in general" vs. a number that fits *this* household.** Walk the
   room through why the "3 months of expenses" figure is a real, defensible, widely-used average —
   and why an average, by construction, is wrong for any specific household on one side of it or
   the other. Push a Hero to state, in plain English, what information about *this* household (not
   about households generally) is the reason 3 months turns out to be 13% short here specifically.
2. **What the 14.8% premium is actually buying.** D4's percent-of-stretch-covered framing makes it
   tempting to treat 87% as "close enough." Push past that to the harder, honest point: the
   remaining 13% is not evenly distributed risk — it is the exact last 0.9 months of a dry spell
   that, per Appendix C, has already happened in this household's own history. Ask: "Is there a
   version of 'good enough' that's still true if this exact scenario happens again next year?"
   There is no single correct answer; the point is that "87% coverage" sounds fine as a percentage
   and much less fine as "we ran out with three and a half weeks of the emergency still going."

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — read both fund nicknames with no numbers, cold-call for a gut read |
| 3:00–10:00 | Position defense — *"Walk us through how you calculated your chosen fund's size — what proportion did you set up, and where do the numbers come from in Appendix A, B, or C?"* |
| 10:00–15:00 | Pressure-test the process — *"Which of your D1/D2 numbers, if it changed, would move your fund size — and which would change the math but not who eventually wins?"* |
| **15:00** | **DROP THE TWIST (N/A — instead, land the D4 survival-test reveal)** — Option A covers 87.1% of the documented dry spell, not 100% |
| 15:00–20:00 | Immediate recommit — does the exact coverage percent change anyone's vote |
| 20:00–30:00 | Threaded deep conflict (a rule for households in general vs. a number for this one; what the 14.8% premium actually buys) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

A Hero computes "3 months × essential expenses" and stops there, treating the famous number as
self-evidently sufficient without ever checking it against the household's own documented income-
variance pattern (Appendix C). That comparison is not wrong on its face — three months of expenses
is a real, substantial cushion — it is *incomplete*: it silently assumes the household's own real
history doesn't matter, when Appendix C states plainly that it has already experienced a longer
dry spell than that. The named trap in this case is exactly that failure mode: for a household with
this specific documented pattern, the number everyone quotes is not the number that survives what
has already happened to them once.

**A second, quieter trap lives inside D2, not D4 — watch for it even in Heroes who get the fund
math right.** A Hero can see "$756" and "21%" in Appendix B and, instead of solving
whole = part ÷ percent, compute part × percent ($756 × 0.21 = $158.76) or treat 21% as a
percentage *decrease* to reverse ($756 ÷ 0.79 = $956.96) rather than the *whole* being asked for.
Either error produces a plausible-looking but wrong "typical income" figure. Because this
particular figure doesn't feed into D3/D4's fund math (see `case.json.modeling_assumptions`,
MA1's sensitivity note), a Hero can get D2 wrong and still land on the correct fund sizes and
recommendation — which makes this error easy for a facilitator to miss unless D2 is checked on its
own terms. Cold-call a Hero's D2 setup specifically, not just their final $3,600 (or wrong) answer.

**A third trap, found by Tier 2 P3 adversarial testing, lives inside D4's own division — watch
for it even in Heroes who correctly compute both fund sizes in D3.** D3's Fund A is built on
*total* essential expenses ($5,874/month), but D4's survival test is supposed to divide Fund A by
the *documented monthly shortfall* ($2,891/month — essential expenses minus Renata's income), not
by total expenses again. A Hero who reuses $5,874 as the D4 divisor computes $17,622 ÷ $5,874 = 3.0
months exactly (100% "coverage" of a 3-month-only test, or a meaningless 42.9% of the real 7-month
stretch) instead of the correct 6.10 months / 87.1%. This substitution is easy to make because it
feels consistent — "I built Fund A off total expenses, so I'll test it against total expenses too"
— but it silently retests Option A against a made-up 3-month bar instead of the household's actual
7-month documented dry spell, which is the entire point of D4. Unlike the D2 error above, this one
changes the final recommendation's supporting numbers directly. Cold-call a Hero's D4 setup for
the specific number they divided by, not just their final months/percent figure.

## Socratic questions

1. You derived Julian's typical monthly income from a part and a percent, without ever looking it up directly — what operation did you use, and how do you know it was the right one instead of its opposite?
2. Option A leaves $2,615 more available to invest today than Option B. What does the household actually get in exchange for giving that up?
3. Fund A covers 87.1% of the documented dry spell. If Renata told you she's comfortable with "pretty close to enough," does your recommendation change? Why or why not, using your own numbers?
4. Appendix C's 7-month, $0-income dry spell is a stated assumption, not a citation from an outside publication — what real evidence in Appendix D is it actually based on, and does that evidence support exactly 7 months, or something looser?
5. Two people could look at the exact same two appendices and correctly recommend opposite options. What is the one fact about this household — not about "the average household" — that decides which of them is right?

## Close

**VOTE AGAIN.** "Did your recommendation change — or just your confidence in the number behind
it?" Ask what math was new to each Hero, and specifically whether deriving Julian's income from a
part and a percent (D2), setting up the fund proportions (D3), or testing survival as a percent of
the dry spell (D4) was the step that actually changed their thinking.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes' Anchor-1 gut vote (Rule-of-Thumb vs. Real-Stretch) matched their post-D4
  recommendation, or whether the exact 87.1% coverage figure flipped a meaningful share of the
  room.
- Whether "the famous number is an average, and this household isn't average" landed as an obvious
  point restated with numbers, or as a genuine reframe of a question Heroes initially treated as
  having one universally correct answer.
- Whether any Hero caught the D2 part/whole reversal error (see The Trap, second variant) and
  whether it changed their D2 answer without changing their final D3/D4 recommendation, as
  designed.

## Standards Touched On

Percent; Ratio; Proportion; How to convert numbers to percents; How to find the percent of a
number; How to find a whole given the percent and the part of the whole; How to find a missing
amount in a proportion.

## Facilitator note — sensitivity (SPEC §6)

Per SPEC §6: this case touches a real, common source of financial stress for irregular-income
households (freelance/1099 income insecurity) but at comparatively modest stakes — a savings/
investing timing decision for an employed, dual-income household with a documented but survivable
history, not illness, death, job loss, or acute hardship. No special framing beyond normal care is
required, but the facilitator should be alert to a room where a Hero's own family's real freelance
or gig-income experience makes the "which fund is objectively right" framing land more personally
than expected; keep the discussion on the computable model, not on judging any Hero's real
circumstances.
