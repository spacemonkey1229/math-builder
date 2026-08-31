# Guide Notes: Tilt Decision

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — the
balance argument, margin, and sensitivity notes live only here and in `case.json`'s `balance`
and `derived` objects.*

**Case:** Tilt Decision · **Tier:** T2 · **Band:** MS-core · **Studio:** MS Adventure
**Standards:** Pre-Calculus / Trigonometric Functions — every group skill in `case.json.standards[]`,
none `new_coverage` (this case is a deliberate second, independent touch on the group; `tide-window`
is the group's first case and already carries the group's `new_coverage`; see
`case.json.reinforcement_note`). Exact ids in `case.json.standards[]`.

**Status:** drafted at `case-write` 2026-08-30, sourced at `case-research` 2026-08-30.
`margin_pct` = **2.13** — Summer Shift (Option B) wins the case's primary metric (rate-weighted
effective annual kWh per panel: 1187.5 vs. 1162.8), while Latitude Lock (Option A) wins raw annual
kWh per panel by a smaller margin (659.3 vs. 656.2, +0.47%) — the number a competing installer's
quote is likely to print. This margin holds under both readings of "the non-summer rate" tested in
`RESEARCH_LOG.md` (2.13% using the off-peak rate as denominator, 1.37% using the on-peak rate);
Summer Shift wins either way, only the size of the margin changes. See `case.json`'s `sources[]`
(S5, S6) and `derived` object, and `cases/the-tilt-decision/sensitivity_model.py`, for the
underlying PVWatts and SMUD figures and a runnable reproduction.

## Balance argument

**Argument for A (Latitude Lock).** Setting a fixed array's tilt equal to the site's latitude is
the textbook-optimal angle for maximizing total annual energy collection — it minimizes the sun's
average angle of incidence integrated across the whole year. It is also the number the competing
installer's quote is likely built around, printed as a single bold annual-kWh figure, because raw
annual kWh is the easiest number to put on a cover page. Latitude Lock wins the "how much power,
total" argument outright (659.3 vs. 656.2 kWh per panel per year).

**Argument for B (Summer Shift).** The primary metric this case asks Priya to defend is not raw
annual kWh — it is annual kWh *weighted by the utility's time-of-use rate schedule*, because a
kilowatt-hour generated in a summer on-peak hour is worth more, dollar for dollar, than one
generated on a winter afternoon. A shallower tilt gives up some low-value winter and
shoulder-season output in exchange for a better angle match during the exact months the rate
schedule pays its premium multiplier. Once Appendix C's multiplier is applied month by month,
Summer Shift's rate-weighted total (1187.5) passes Latitude Lock's (1162.8) even though its raw
annual kWh trails it.

**The margin.** Computed from Appendix B's PVWatts monthly output for both tilt angles and
Appendix C's summer on-peak multiplier and summer-month definition: multiply each month's modeled
output by that month's applicable rate multiplier (the summer multiplier for June–September, 1.0
otherwise), sum across the year for each option, and compare. `case.json` records the method as
`balance.margin_basis` and the resulting totals as `derived.weighted_annual_kwh_a/b`.

## Intro

Frame the format before anything else: this is a real bid going head-to-head with a competitor's
quote on the homeowner's kitchen table, not a worksheet. Name the opener: *"You're Priya Desai. The
Reyes family already has a competitor's quote in hand, printing a bigger number than yours. Whose
number wins depends entirely on what 'wins' even means — and you have to be able to defend that in
plain English before you can defend it in trigonometry."* Let the stakes land before moving to the
Launch.

## Launch

Show Appendix A's two tilt options side by side — Latitude Lock at 39°, Summer Shift at 24° — with
no output numbers yet, just the two angles and the racking's 10°–60° supported range. Ask: *"Same
roof, same panels, same racking hardware — only the angle changes. Which one do you think produces
more power over a year, and why?"* Take answers without correcting anyone; most rooms will
correctly guess Latitude Lock wins on raw total, which is exactly the trap (see below).

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

*"Is anyone courageous enough to stand with Summer Shift — the option that gives up raw annual
power?"* Show of hands, both options, no discussion. Record the count — Close will ask them to vote
again.

## Anchor 2 — What is the problem we're solving?

**"Is 'more total power' the right question?" · "What do you mean by 'better'?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which tilt
produces more total kWh," but push on what the Background actually states: the Reyes family's
utility does not pay the same price for every kilowatt-hour. Ask: *"Is every kilowatt-hour worth
the same amount of money to this homeowner, once you know their utility bills them differently by
season and hour?"* If the room lands on "we need power weighted by what it's actually worth on the
bill, not raw power" on its own, the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "which tilt produces more total energy" from "which tilt produces more
*valuable* energy," ask them to name the actual steps before opening an appendix: (1) find the
sun's position at representative times of year (Appendix D), (2) convert those positions into
angles usable with the unit circle (D1–D2), (3) model each tilt option's fixed angle-of-incidence
relationship against the sun's seasonal path and check it against Appendix B's modeled monthly
output (D3–D4), (4) weight each month's output by what SMUD actually charges that month (Appendix
C, D4), (5) sum the weighted totals and compare. Re-ask: *"Now that we can see the steps, is our
question still the right one?"*

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the honest gap: the number of panels in the Reyes family's array (Appendix A, MA1) has no
public record for a fictional household and is a stated Modeling Assumption, not a sourced figure.
Ask: *"Is that assumption critical to who wins — or does it wash out?"* Push until a Hero notices
the primary metric (Background, Dilemma) is stated **per panel**, and panel count is identical for
both options — it cancels out of the A-vs-B comparison entirely and cannot flip the recommendation
(exactly what `sensitivity_model.py`'s `panel_count` flex confirms mechanically). The load-bearing
assumption is elsewhere: which of SMUD's two published non-summer rates (Appendix C) counts as
"the" non-summer rate — that choice is not a gap in the data, it is a documented modeling
convention (see S6, and the Twist below).

## Data Deep Dive

Now, and only now, open Appendices A–D and work D1–D4. Walk D1's degrees-to-radians table, D2's
unit-circle sine/cosine/tangent evaluations, D3's amplitude-and-period graph, and D4's weighted
comparison together as a room, cold-calling for D4 specifically — this is where a Hero who
correctly found Latitude Lock's larger raw annual total (D1–D3 territory) but never applied
Appendix C's rate multiplier will visibly struggle to explain why Summer Shift still wins on the
metric the case actually asks for. That struggle is useful information for the facilitator, not a
moment to rescue.

**Facilitator-only arithmetic note.** Appendix B's twelve monthly figures, summed with no
weighting, give Latitude Lock 659.3 kWh/panel/year vs. Summer Shift's 656.2 — Latitude Lock's raw
edge, +0.47%. Applying Appendix C's summer on-peak multiplier (0.3765 ÷ 0.1285 = 2.93) to the four
summer months (June–September) and 1.0 to the other eight, then summing, gives Latitude Lock
1162.8 weighted kWh/panel/year and Summer Shift 1187.5 — Summer Shift's weighted edge, **2.13%**.
The reason the ranking flips: Summer Shift trails in the winter and shoulder months (already priced
at the cheap non-summer rate) but leads in exactly the four summer months the 2.93× multiplier
applies to (e.g. July: Summer Shift 72.6 vs. Latitude Lock 66.5), so the weighting more than makes
up its raw-total deficit. Full derivation, and a runnable reproduction, in
`sensitivity_model.py` and `case.json.derived`.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Appendix C's non-summer rate — $0.1285/kWh — is the *off-peak* non-summer rate. SMUD's own rate
page also publishes a non-summer *on-peak* rate: $0.1776/kWh, for the same 5–8pm window the summer
on-peak rate applies to, just charged less because it's not summer. Appendix C picked the off-peak
figure because it's what most non-summer hours are actually billed at — but if the Reyes family
runs their evening routine (dinner, laundry, the dishwasher) inside that 5–8pm window year-round,
not just in summer, a meaningful share of their *non-summer* usage is actually billed at $0.1776,
not $0.1285."

"If the non-summer rate you should be weighting against is really $0.1776, not $0.1285 — does your
recommendation change?"

**Facilitator-only: what this actually does, and does not, change.** Re-running D4's weighting with
$0.1776 as the non-summer denominator instead of $0.1285 changes the summer multiplier from 2.93×
to about 2.12× — and the recommendation *does not flip*: Summer Shift still wins, just by a much
thinner margin (1.37% instead of 2.13%). `RESEARCH_LOG.md` and `sensitivity_model.py` both confirm
this directly — running `evaluate({"nonsummer_rate_used_usd_per_kwh": 0.1776})` still returns
Summer Shift ahead of Latitude Lock. What the twist *does* do is surface a real modeling question
D4 alone doesn't ask: Appendix C's own note admits SMUD publishes *two* non-summer rates for the
same clock hours, and the case's simplified month-level (not hour-level) weighting scheme had to
pick one. **The twist reframes, it doesn't resolve:** "which tilt wins under the stated rate
convention" is a different question from "is the off-peak rate the right non-summer denominator for
a specific family's actual evening usage pattern" — and the case has no sourced answer for the
Reyes family's real hour-by-hour usage. Inventing one here would be exactly the fabrication SPEC §5
forbids. Do not hand a specific answer to the second question; its openness is the point, and the
fact that the *winner survives it anyway* is the reassuring finding worth landing explicitly.

## Immediate recommit

Re-vote immediately. Ask by name: *"Does the on-peak-vs-off-peak question change your vote — or
does it just tell you that '$0.1285' was a modeling choice worth pressure-testing, not an
unshakeable fact?"* That distinction is the transferable skill, not the vote itself.

## Deep conflict — three threads (20–30 min)

1. **Raw total is not the same as rate-weighted total.** Latitude Lock wins Appendix B's raw sum
   every time — yet it loses D4. Why does printing only the raw annual-kWh number mislead here, and
   what does the weighting step actually protect the homeowner from?
2. **A rate "convention" is only as solid as the usage pattern it assumes.** The twist shows the
   case's own source (S6) publishes two valid non-summer rates for the same clock window. Does that
   change how confident the room should be in Argument B's framing — even though the recommendation
   itself doesn't flip?
3. **What a 2.13% margin, built on a stated convention, can and can't tell you.** The rate-choice
   between $0.1285 and $0.1776 is the single most load-bearing modeling decision in the whole case.
   Is a margin this size, resting on a choice this contested, worth defending with real confidence —
   or does the closeness argue for hedging the recommendation rather than stating it flatly?

## The trap

The trap is comparing the two options on **raw total annual kWh alone** — exactly the number a
competing installer's quote is likely to print, and exactly the number Latitude Lock is built to
win (659.3 vs. 656.2). A Hero who stops there has quietly assumed every kilowatt-hour is worth the
same amount, which the case's own Background states is false: SMUD's time-of-use schedule prices a
summer on-peak kWh differently from every other kWh in the year. The primary metric this case asks
students to defend is explicitly the *rate-weighted* figure (D4), not the raw total — a Hero who
never applies Appendix C's multiplier to Appendix B's monthly curve has answered a different,
easier question than the one Priya actually has to answer, and may confidently recommend the wrong
option (Latitude Lock) as a result.

## Socratic questions

1. Your D4 weighted-kWh figures — which option wins, and by how much? Now compare that to your raw annual-kWh totals from Appendix B alone (no weighting) — does the ranking hold, or does it flip?
2. Appendix C's summer on-peak multiplier is 0.3765 ÷ 0.1285. At roughly what multiplier value would Latitude Lock and Summer Shift produce exactly equal weighted annual kWh per panel — and is SMUD's actual published multiplier above or below that value?
3. In D2 you had to find a reference angle for at least one sun position outside the first quadrant. Suppose a student instead used the raw azimuth angle directly in a sine or cosine calculation, without ever finding the reference angle — for which time of day does that error actually change a sign, and how far off does the resulting angle-of-incidence estimate end up?
4. Appendix A's racking system has a hard maximum tilt angle, 60°. If a site at a much higher latitude pushed Latitude Lock's ideal tilt angle past that maximum, would Option A even be buildable as stated — and what would you recommend instead?
5. SMUD's own rate page publishes two different non-summer rates for the same clock hours (off-peak and on-peak). Appendix C uses the off-peak one. If you re-ran D4 with the on-peak rate instead, would your recommendation change — and what does the answer tell you about how much confidence to put in a 2.13% margin?

## Close

**VOTE AGAIN.** *"Did we ask the right question at the start?"* *"What math was new to you
tonight, and how did you actually attack it?"* Compare the closing vote to Anchor 1's — a room that
voted for Summer Shift at Anchor 1 purely on "the shallower angle feels smarter for summer" and
stays with Summer Shift after the twist for a *different, weighted-arithmetic-based* reason has
genuinely moved, even if the vote count looks unchanged.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Anchor 2's "is every kWh worth the same amount" reframe landed as a discovery or had to
  be told outright.
- Whether the "raw total vs. rate-weighted total" trap was the actual sticking point, or whether
  D4's month-by-month weighting arithmetic itself was the harder gate for most Heroes.
- Whether the on-peak/off-peak twist felt like a genuine pressure test of a real modeling choice or
  felt like the case manufacturing doubt — worth listening for directly, since the margin (2.13%,
  narrowing to 1.37% under the twist) is genuinely close either way.

## Standards Touched On

Radian; Unit Circle; Sine Function; Cosine Function; Tangent Function; Amplitude; Period (Of A
Function); Reference Angle; How to convert between degrees and radians; How to find the sine,
cosine, and tangent of an angle using the unit circle; How to find the amplitude and period of a
sine or cosine function.

## Facilitator note — sensitivity (SPEC §6)

None declared by the concept sheet — routine solar-design and utility-billing math, no illness,
death, financial-hardship, or other protected-subject stakes. `case.json.sensitivity_note` records
the load-bearing modeling-assumption finding instead, which is a different (non-§6) kind of note:
the choice of which SMUD non-summer rate to weight against (off-peak vs. on-peak) is the figure
most likely to move D4's margin — a higher non-summer rate narrows the summer multiplier and
shrinks Summer Shift's advantage, though not enough (per `RESEARCH_LOG.md` and
`sensitivity_model.py`) to flip the winner under either of SMUD's two published readings. Per
`case-write` SKILL.md §8, this note states the *direction* of that sensitivity only — the actual
computed numbers are recorded in `case.json.derived` and this file for facilitator reference.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show the two tilt angles side by side, cold-call for a gut read, no output numbers yet |
| 3:00–10:00 | Position defense — *"Convince us your option actually wins on what the Reyes family gets billed, not just on raw power"* |
| 10:00–15:00 | Pressure-test the models — *"Which SMUD rate choice would have to change, and how, for your answer to flip?"* |
| **15:00** | **DROP THE TWIST** — the off-peak-vs-on-peak non-summer rate, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (raw total vs. rate-weighted total; how solid is a rate "convention"; is a margin this size worth defending flatly) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands (minimum specification, drafted at write time)

| Band | Typical size | What changes |
|---|---|---|
| **Full** | the size this T2 case is authored for (a full MS-core class section) | the Socratic plan above runs as written; both stand/sit votes are taken as a group |
| **Compressed** | roughly half | Anchors 2–3 combine into one pass; the deep-conflict thread (raw kWh vs. rate-weighted kWh) runs as a single thread instead of two; total runtime shortens proportionally |
| **1:1 / pair** | one or two learners | no vote to take — Anchor 1 becomes a stated initial position instead of a stand/sit count; the guide plays devil's advocate directly rather than cold-calling; Socratic question 2 (the break-even multiplier) still lands but is asked directly rather than opened to the room |
