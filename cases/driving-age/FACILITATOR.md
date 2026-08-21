# Facilitator Guide — Driving Age

**Cases touching family cost stress get a one-line flag:** this case discusses real insurance and
transportation costs that some families in the room may be currently navigating. Keep the framing
on Congresswoman Edmunds's fictional vote, not on any Hero's own family situation, unless a Hero
opens that door themselves.

## Argument for A (Vote AYE — raise the age to 18)

Over the two years HB 3320 would delay licensure (current unsupervised-driving age 16, to the
bill's 18), a family avoids the full **$4,050/year** cost of insuring a 16-year-old driver —
**$8,100.00** total over two years. The chauffeuring cost the delay creates instead, at a disclosed
assumption of 6,000 miles/year and AAA's fully-loaded 66.37 cents/mile, is **$7,964.40**. The
dollar math genuinely favors AYE, even though it's razor-close. The real safety case for AYE is
**not** Appendix B's per-100,000-population table — that table actually *rises* with age and does
not support "raising the age is safer" (see The Trap, below). It is Appendix B's separately cited
per-mile statistic (S8): drivers 16–17 crash nearly twice as often per mile as drivers 18–19 —
real, age-matched evidence that the youngest, least-experienced drivers carry the highest per-mile
risk, even though S8's bands (16–17 vs. 18–19) are not an exact match for this case's actual
15½-vs-18 comparison.

## Argument for B (Vote NAY — keep the age at 15½)

The per-100,000-population data (Appendix B's main table) undercuts a naive "raising the age makes
it safer" argument in the most literal sense: that rate does **not** fall from age 16 to 18 or 19 —
it climbs, from 3.5 to 7.0 to 8.8, because more of each age cohort is driving, and driving more, as
they get older. Whatever HB 3320 buys, a clean per-capita safety win from that table is not
automatically it. The real per-mile stat (S8) does favor AYE's safety case, but only at
16–17-vs-18–19 granularity, not this case's actual 15½-vs-18 comparison — a real gap a Hero can
legitimately press on. And in dollar terms, NAY isn't just competitive — it's barely behind:
**$8,100.00** in extra insurance cost against **$7,964.40** in extra chauffeuring cost is a
**$135.60** gap on a nearly $8,000 base, and that entire gap sits inside one disclosed, unsourced
modeling assumption (MA1's 6,000 mi/year) that a Hero is fully entitled to challenge.

## The margin

**Primary metric:** net two-year dollar cost per Arizona family with one 16-to-17-year-old.

| | Option A (raise to 18) | Option B (keep 15½) |
|---|---|---|
| Insurance cost | $0.00 | $4,050.00/yr × 2 = $8,100.00 |
| Chauffeuring cost | 6,000 mi/yr × 2 × $0.6637/mi = $7,964.40 | $0.00 |
| **Total** | **$7,964.40** | **$8,100.00** |

**Margin = ($8,100.00 − $7,964.40) / $7,964.40 = 1.70%.** Option A (AYE) is cheaper, by a hair.
This matches `case.json.balance.margin_pct` and `derived.margin_pct` exactly — if this table and
those fields ever disagree, this document is stale and must be regenerated from `case.json`.

## Five Socratic questions

1. Your net-cost table puts Option A about $135.60 cheaper over two years on an almost-$8,000 base — what would MA1's chauffeuring-mileage assumption have to be, in miles per year, for that to flip?
2. Appendix B shows the fatal-crash rate climbing from 3.5 (age 16) to 8.8 (age 19), not falling — if raising the minimum age doesn't lower that number, what exactly is the safety argument for HB 3320 actually claiming?
3. The case gives you a per-100,000-*people* rate, not a per-*mile* or per-*licensed-driver* rate — why might a 19-year-old's rate be higher than a 16-year-old's even if 19-year-olds are, mile for mile, safer drivers?
4. Your D2 equation was read off your hand-drawn graph and your D3 equation was built from two raw data points — if they don't predict the exact same value at age 18, which one do you trust more, and why?
5. Congresswoman Edmunds has a 14-year-old at home who is two years from a permit either way this vote goes — does that personal stake belong in a dollars-and-safety argument on the House floor, or is it a different kind of argument entirely?

## The trap

A room will reflexively read Appendix B as proof that raising the minimum age *is* the safer
choice — "the case gave us a chart, older is more mature, so an older minimum age must mean fewer
deaths." The chart says the opposite of what they expect: the rate *rises* with age from 16 to 19.
The trap is treating a per-100,000-*population* fatality rate as if it were a per-mile risk rate —
the population rate rises with age partly because more of that age cohort is driving, and driving
more miles, not because 19-year-olds are worse drivers than 16-year-olds. A Hero who plants a flag
on "the data proves A is safer" without checking which rate they're reading has walked into it.
Watch for pitches that cite Appendix B's numbers to support Option A's *safety* case — that
citation, read straight, argues against them.

## The Twist

**Timing:** ~15 minutes in, after Anchors 1–3, before the Data Deep Dive concludes.

**What breaks:** Reveal that Appendix B's main table is a per-100,000-*people* rate, not a per-mile
or per-licensed-driver rate — and that Appendix B's separately cited per-mile statistic (S8, AAA
Foundation for Traffic Safety) shows drivers 16–17 crashing nearly twice as often per mile as
drivers 18–19. Two real, correctly-cited statistics about nearly the same age group point in
opposite directions depending which denominator you pick — and neither one is an exact match for
this case's actual 15½-vs-18 comparison; S8's bands are the closest real data available, not a
perfect fit. Ask: **"You have 60 seconds. Does this change your vote — or not?"**

**What just broke:** Any position built on "the chart proves it" collapses the moment the room
realizes there are two different, both-real ways to measure the same risk, and the case never told
them which one Congresswoman Edmunds should use. That is not a data problem — it's a *modeling*
problem, and modeling problems don't have a clean right answer. The follow-up question is the
whole point: **"Were you wrong, or just using the wrong ruler?"**

## Cohort bands

See `case.json.cohort_bands[]` (Full 12–20 / Compressed 6–11 / 1:1 pair 1–2) — reproduced there,
not duplicated here to avoid drift.

## Sensitivity note

The 1.70% margin is genuinely thin and load-bearing on MA1 (the 6,000 mi/year chauffeuring
assumption) — a `case-readiness` Tier 2 probe 5 run is required before this case may reach
`TIER2_PASS`, and its verdict must be disclosed here and in `case.json.sensitivity_disclosure[]`
once run. Do not tell a room the margin is "close" without also being ready to show exactly how
thin the assumption underneath it is.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote on AYE vs. NAY — no explanation yet |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just fair" |
| 10:00–15:00 | Pressure-test: "Whose plan is most fragile?" — push on Appendix B's data and MA1's assumption |
| **15:00** | **DROP THE TWIST** — per-mile vs. per-population framing, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00–30:00 | Threaded deep conflict — two named threads: (1) which real statistic actually answers the question, (2) is a 1.7% dollar margin even worth voting on, or does something else (safety intuition, rural-family practicality, the constituent poll) have to break the tie |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## Guide Notes — anchor ladder

### Intro

Frame the format: this is a real bill-format case (excerpt from an actual Arizona
legislative bill in Appendix A). Name the opener: read the bill's opening lines aloud, then run the
floor-debate script from the original launch (Mr. Speaker / motion to open debate).

### Launch

Read HB 3320's opening lines (Appendix A). Pose the two Monday-launch questions from
the original Guide Notes: "which group most deserves license revocation, seniors past eighty or
youth in their teens?" and "which trait corresponds most closely with poor driving — age, gender,
or experience?"
Do not resolve either question; let them sit.

### Anchor 1

TAKE A STAND AND VOTE. Invite one Hero to present their position as if addressing
the House floor. Cold-call stand/sit vote, no reasoning yet. Let confusion grow: "Wow, this is a
challenging problem."

### Anchor 2

WHAT IS THE PROBLEM WE'RE SOLVING? Is this just "which age results in fewer
crashes," or is there something else (cost, rural practicality, personal liberty) that has to be
weighed too? What do you mean by "safer"? Is this the right question?

### Anchor 3

WHAT IS THE PROCESS? If we just look at Appendix B's chart and nothing else, will
we actually know the answer? Ask again: is our question still the right question? If we go through
this process and land on a number, how do we decide — a margin, or something else?

### Anchor 4

WHAT DON'T WE KNOW? Do we need to make any assumptions to answer this? (Point toward
MA1 without naming its value yet.) Is there anything we don't know that would be critical here?

### Data Deep Dive

Now the numbers: Appendix B's real crash-rate table, Appendix C's real
insurance and driving-cost figures, and MA1's disclosed assumption.

### Twist (guide notes cross-reference)

See "The Twist" section above for the full reveal script.

### Close

Vote again. "We asked ______ as our key question — did we ask the right question?
Was this case study challenging, and why? What math was new to you, and how did you attack it? If
you got a similar case study next time, what would you do differently?"

### Lessons Learned

Two real, correctly-cited statistics can point in opposite directions
depending on what you divide by — and even a well-matched real citation (S8's 16–17-vs-18–19
per-mile data) can still not be an exact match for the question the case actually asks
(15½-vs-18). A margin under 2% is not the same thing as a landslide, and a disclosed assumption
inside that margin is fair game to challenge in discussion, not a flaw to hide.

### Standards Touched On

See Appendix H of `case.md` for the verbatim spine list.
