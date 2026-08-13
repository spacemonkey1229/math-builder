# Guide Notes: Wildfire

**Case:** Wildfire · **Tier:** T3 · **Band:** MS-stretch · **Studio:** Heroes Academy
**Standards:** see `case.json.standards[]` for the exact ids (15 skills — area of a circle, unit
and compound-unit conversion, ratio/proportion, percent, decimal multiplication/division, and
comparison)

Legacy conversion, 2026-08-13, built from the original case study docx
(`source/Y3/Session 3/Wildfire/Case Study_ Wildfire.docx` and `Guide Notes.docx`) onto the current
11-anchor ladder. Agua Dulce, Santa Clarita, and San Fernando are real places with real, cited
2020 Census data (case.md Appendix C); the Soledad Canyon Fire itself and its reported spread
rates are the legacy scenario's own given field data, not independently sourceable since the fire
is fictional. See `case.json.legacy_conversion_note` for the full accounting of what changed.

## Intro

Frame the format: this is a real resource-allocation decision (which town gets 235 troops) laid
over real Southern California geography, not a worksheet. Name the opener — "One fire, two real
towns, 235 soldiers who can only go to one of them. You're the Response Commander. Line two is
holding."

## Launch

Read the Background aloud through the two 05:00 field reports (35 chains/hour southern head, 27
chains/hour southwestern flank) — but do not do any unit conversion yet, and do not show Appendix
C's town data yet. Ask: "Just from '35 vs 27,' does one of these already feel more urgent to you?"
Do not confirm or correct answers here — the raw chains/hour numbers are deliberately
uninterpretable without a unit conversion, and that is the point.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who sends the rapid response force to San Fernando? Who sends it to Santa Clarita?" Show of
hands, no discussion. Record the count — Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do we need to consider in order to decide?"**

Push on what "best" means here for a fire commander: raw urgency (which town does the fire reach
first), total population protected, and total damage in the immediate area tonight (regardless of
which town wins the vote) are all real, different considerations. Is the question "which town
burns first" or "where does 235 troops save the most people, fastest"?

## Anchor 3 — What is the process?

**"Do we consider all of these factors, focus on 2-3, or focus on only one? Which one(s)?"**

Once the room has picked its deciding factor(s), ask them to name the actual steps: converting
chains/hour to a usable speed, converting the real town distances into a time-to-arrival for each
option, and comparing that against each town's real population. Re-ask: "Do we agree that's the
right process for the factor we picked?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the five stated conventions in Appendix D (MA1–MA5): the sector-growth model for
acreage, the Agua Dulce density proxy for people-at-risk, the fire's modeled position at Agua
Dulce, using route distance instead of straight-line, and holding the 05:00 rate constant all day
despite Appendix A's forecast showing wind climbing after 11:00. Ask which one the room thinks
matters most to whether the final recommendation is trustworthy.

## Data Deep Dive

Now, and only now, the numbers. Walk D3/D4's rate-to-time calculation together as a room first —
cold-call for the chains/hour → mph conversion specifically, since a Hero who forgets the
66-feet-per-chain step will get a wildly wrong (10x-plus off) travel time. Then walk D1's sector
area and D2's density-proportion together — cold-call for the 45°/360° fraction, since skipping it
(treating D1 as a full circle) overstates the acreage by 8×.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Central Command radios in: 'Sir, San Fernando city manager wants to know — does the fire reach us
tonight?'"

**Facilitator-only.** Once D3/D4 are computed honestly against the real, 2026-08-13-re-verified
route distances, both towns turn out to be **more than two full days away** at the reported 05:00
rates (San Fernando ≈57.8 hours, Santa Clarita ≈57.2 hours) — not hours, and not "tonight." This is
a genuine finding
from the case's own real data, not an invented complication: the legacy case's own framing ("how
long will it take for the fire to reach [town]... deployed to today") implicitly suggested
same-day urgency, but the math built from the fire's own field-reported rates does not support
that. Ask the room: "If neither town is actually threatened tonight, what was Commander Dobson
actually deciding when he picked a deployment location? What does '235 troops, one place, today'
even mean if the fire is two days out from both options?"

The real, disclosed reframe: D1/D2 (the immediate acreage and structure loss tonight, in the fire's
current vicinity near Agua Dulce) are what's actually urgent *today*. D3/D4's town-arrival numbers
are a longer-horizon question about where to pre-position a fire line before the fire's multi-day
advance reaches either urban edge — a real and legitimate use of a rapid-response force, just not
a "stop it before midnight" one. Ask: "Does that change which option you'd pick — or just change
why you'd pick it?"

## Immediate recommit

Re-vote immediately. Ask by name: "Did realizing neither town is at risk *tonight* change your
recommendation, or did it just change what argument you'd use to defend it?"

## Deep conflict — three threads (20-30 min)

1. **Lead time vs. population.** After the 2026-08-13 route-distance correction (see case.md's
   Balance Argument section), Santa Clarita is now reached ~1.1% *sooner* than San Fernando by the
   raw rate math, not later — and Santa Clarita's population is nearly 9.6× larger. There is no
   longer a real trade-off to debate on the raw numbers: the population argument and the lead-time
   argument now point the same direction. Push the room on this directly: "Before this correction,
   the case looked like a real trade-off — more people, but less time. Now that the real distances
   put Santa Clarita both bigger *and* (barely) sooner, was San Fernando ever really the stronger
   pick, or did the original case just have the wrong numbers?" This is also the moment to surface
   that the margin is only ~1.1% and flips under a small change in either distance (Twist soundness
   check / Lessons Learned) — a real decision this close should not be described as clean or settled.
2. **The held-constant assumption.** MA5 holds each flank's 05:00 rate constant through 23:59, but
   Appendix A's own forecast shows wind climbing sharply after 11:00. If real fire behavior
   accelerates with wind the way the forecast suggests, which of D1–D4's numbers becomes the most
   dangerously wrong, and in which direction?
3. **The sector-angle choice (MA1).** D1's acreage model uses a 45° wedge because that's the real
   compass angle between the fire's own two reported bearings (south, southwest). Is that
   defensible, or is it just as arbitrary as guessing a number outright — and what would you need
   to know to do better?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — read the two raw ROS numbers aloud, cold-call for a gut read, no conversions or town data yet |
| 3:00–10:00 | Position defense — *"Convince us your town is the right call, not just 'the number felt bigger'"* |
| 10:00–15:00 | Pressure-test the models — *"Which factor is actually deciding your vote — speed, population, or something else?"* |
| **15:00** | **DROP THE TWIST** — neither town is actually reached tonight, delivered slowly |
| 15:00–20:00 | Immediate recommit — did the two-day finding change anyone's answer, or just their reasoning |
| 20:00–30:00 | Threaded deep conflict (lead time vs. population; the held-constant wind assumption; the 45° sector choice) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

A Hero computes "35 > 27, so San Fernando's flank is faster, therefore San Fernando is more
urgent," recommends Option A, and never converts chains/hour into an actual mph, never checks it
against a real town distance, and never notices that at that rate the fire is over two days from
either town. The raw ROS comparison alone (35 vs. 27 chains/hour) is real data, but by itself it
answers a different question than "which town do we send help to today" — the case's real tension
is that the more urgent-*feeling* number (35) doesn't automatically win once you do the actual
rate-time-distance math and put a real population figure next to it.

## Socratic questions

1. San Fernando's flank has a faster reported rate of spread than Santa Clarita's — once you convert both to miles per hour and divide into the real route distance, which town is actually reached sooner, and by how many hours?
2. The corrected lead-time margin between the two options is only about 1.1% — and Santa Clarita's population is about 9.6 times San Fernando's. With a margin this thin, is "shorter lead time" even a meaningful reason to prefer one option over the other, or does a ~1.1% difference in an estimate built on multiple modeling assumptions (MA3–MA5) tell you almost nothing?
3. D1's acreage estimate uses a 45° sector instead of a full circle, based on the real compass angle between the fire's two reported bearings — what would change about your answer if the true angle between the head and the flank were narrower, say 20° instead of 45°?
4. Appendix A's forecast shows wind climbing sharply after 11:00, but D1–D4 hold the 05:00 rate constant all day — does that make your numbers more likely too high or too low, and does it matter for which option you'd pick?
5. Neither town turns out to be reached by 23:59 tonight at the reported rates — does that mean the original dilemma ("where do you send the rapid response force today") was the wrong question to ask, or does it just mean "today" answers a different part of the question than "tonight"?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that voted
the same way both times is worth asking about directly: did the twist not change the actual
recommendation, or did it just change *why* people hold their position?

## Lessons Learned

*(Migrated from the legacy Guide Notes' Close/Lessons Learned section — preserved as the
structural content, since the original recorded no case-run-specific findings yet.)*

- Whether the chains-to-mph conversion (D3/D4) or the sector-area/proportion chain (D1/D2) was
  where most Heroes actually got stuck.
- Whether Heroes anchored on raw ROS, computed lead time, or population as their real deciding
  factor, and whether that split along any pattern.
- Whether discovering neither town is reached "tonight" changed recommendations outright, or only
  changed the stated reasoning behind an unchanged vote.
- Whether any Hero independently challenged MA1's 45° sector angle or MA5's held-constant rate
  before the twist surfaced it explicitly — that would be a genuinely strong catch.

**2026-08-13 sensitivity disclosure (required reading before facilitating this case — MCS-26/MCS-41).**
A Tier 2 readiness re-check found the case's cited Agua Dulce→Santa Clarita and Agua Dulce→San
Fernando route distances (previously 23 mi / 24 mi) had drifted from their sources, and the San
Fernando figure had never actually carried a real citation at all. A genuine retune was attempted
first: both distances were re-verified against live Google Maps routing (case.json sources[]
S5/S5b). Elimination of the instability was not honestly achievable — the corrected, real distances
(19.3 mi / 25.3 mi) are *more* lopsided in ratio than the stale ones, and they flip which town has
the shorter modeled lead time: Santa Clarita is now marginally shorter-fuse (≈57.2h) than San
Fernando (≈57.8h), a ~1.1% margin, reversed from the case's original 19.5%-in-San-Fernando's-favor
framing. Because the honest margin is this thin, `sensitivity_model.py`'s ±50% flex sweep on either
distance flips the A/B winner in both directions — this is disclosed here and in case.json
(`balance.stability`), and is recorded as a real, permanent **Tier 2 probe 5 FAIL**, not a pass, per
this project's own doctrine (a disclosed-but-not-eliminated instability does not pass — the same
standard this project holds its own flagship case, Cold Chain, to). A facilitator running this case
should present the lead-time comparison as genuinely too close to call on the raw math (the
Socratic questions above are written to surface this), not as a settled 19.5%-margin result.

## Standards Touched On

Area · Unit · Distance · Ratio · Proportion · Percent · Decimal · How to find the area of a circle
· How to convert an amount from one unit to another unit · How to convert an amount with compound
units · How to find a missing amount in a proportion · How to convert percents to numbers · How to
multiply decimal numbers · How to divide decimal numbers · How to compare two or more values

## Twist soundness check (SPEC.md §6 / case-write §5)

Checked the twist ("neither town is reached tonight at the reported rates") against every stated
Modeling Assumption (Appendix D, MA1–MA5), reading them both **sequentially** (does each
assumption, applied one after another, still support the twist holding?) and **simultaneously**
(does the twist survive if all five are true at once, not just one at a time)?

- MA1 (sector model) and MA2 (density proxy) affect D1/D2 only — they do not touch D3/D4's
  distance/rate/time arithmetic, so they cannot invalidate the twist.
- MA3 (fire modeled at Agua Dulce) and MA4 (route distance, not straight-line) both work in the
  *same* direction: both slightly shorten the fire's real path if anything, since Agua Dulce is
  the closest confirmed point and route distance already roughly follows the terrain a fire would
  actually spread along. Neither pushes the arrival time hard enough to bring it under 24 hours —
  even a straight-line distance at roughly 75-80% of the route mileage still leaves both towns over
  40 hours out at these rates.
- MA5 (held-constant rate) is the one assumption that could genuinely break the twist if relaxed —
  if real wind-driven acceleration roughly doubled the effective ROS after 11:00, San Fernando's
  ~57.8-hour estimate could fall toward ~36 hours (see sensitivity_model.py's `evaluate_twist()`,
  which runs exactly this at a 1.6× factor and lands both towns around 35-36h), still past "tonight"
  but meaningfully closer. This is disclosed explicitly in Appendix D's sensitivity column and in
  Deep Conflict thread 2 — the twist is presented as true *under the case's own stated model*, not
  as an unconditional claim about the real fire, and the discussion is designed to surface exactly
  this limitation rather than hide it.
- Holding all five simultaneously (the case's actual as-published state): both D3 and D4 land
  solidly past 48 hours (57.8h and 57.2h), so the **Twist itself** ("not tonight, for either town")
  holds robustly — a 50% swing on either distance still leaves both towns well past 24 hours (see
  the FLEX sweep in sensitivity_model.py). **This is a different question from whether A beats B**,
  and the two must not be conflated: the twist (neither town is reached tonight) is robust; the
  balance-test winner (which town has the shorter lead time, A or B) is NOT robust — it is a real,
  disclosed Tier 2 probe 5 FAIL, because the honest margin between the two options is only ~1.1%
  and flips order under the same ±50% distance flex that leaves the twist untouched. See the Balance
  Argument section's sensitivity disclosure and Lessons Learned below.

## Sensitivity note

Real people, a real disaster type, and a real resource-scarcity decision (SPEC.md §6). The framing
is deliberately protection-oriented (which town's fire line to defend, how many homes are at risk)
rather than casualty-optimization. Facilitators should keep the discussion on the real geography
and the case's own disclosed modeling assumptions — steer away from personal wildfire-evacuation
stories from the room, which can turn a math discussion into something a facilitator isn't
equipped to hold.
