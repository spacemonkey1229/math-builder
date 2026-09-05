# Guide Notes: The Two Offers

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — the
balance argument, margin, and sensitivity notes live only here and in `case.json`'s `balance`
object.*

**Case:** The Two Offers · **Tier:** T2 · **Band:** MS-core · **Studio:** MS Adventure
**Standards:** Statistics And Probability/Algebra — `statistics-and-probability-system-of-equations`,
`statistics-and-probability-how-to-solve-a-system-of-linear-equations`,
`statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data`,
`statistics-and-probability-how-to-identify-the-slope-of-a-line-given-a-set-of-data-or-a-graph-o`,
`statistics-and-probability-slope`, `statistics-and-probability-y-intercept`,
`statistics-and-probability-how-to-draw-a-line-of-a-set-of-data-given-its-linear-equation` (all
already n>0 in the spine; this case reinforces the group's two thinnest skills — see
`case.json.reinforcement_note` — while closing the Employment & Income topic gap named in
`case.json.topic_gap_closed`).

**Status:** Researched 2026-09-03. Numbers below are the real, sourced figures — never state them,
or the margin's size/direction, inside `case.md`.

## The real numbers (facilitator reference — never appears in case.md)

- V_A(t) = 7500.83t + 8663 — Cascadia's net monthly value is $96,250/12 base minus $520/month
  commuting + parking (Appendix A, MA1); the y-intercept is the $8,663 signing bonus.
- V_B(t) = 6980.00t + 12000 — Northwind's net monthly value is $80,000/12 base plus $313.33/month
  401(k) match (Appendix B); the y-intercept is the $12,000 signing bonus.
- **Crossover: t ≈ 6.41 months, at a cumulative value of ≈ $56,721.** Below that tenure, Northwind
  (Option B) delivers more; above it, Cascadia (Option A) pulls ahead and its lead widens every
  month, because its slope is $520.83/month steeper.
- **Margin at a 24-month reference tenure:** V_A(24) = $188,683 vs. V_B(24) = $179,520 — a 5.10%
  margin in Cascadia's favor (`case.json.margin_pct` = 5.1, well inside the SPEC §2 20% cap).
- **Why this stays a genuine two-sided case, not a landslide:** the crossover (~6.41 months) is
  well inside a plausible "first job might not work out" tenure — a real, common Hero position —
  while the 24-month margin (5.1%) is close enough that a Hero who argues for the long horizon is
  not coasting on an obvious answer either. Both arguments are quantitatively live.

## Intro

Frame the format before anything else: this is a real accept-by-Friday decision with a signed
offer letter on the other side of it, not a worksheet. Name the opener — "You're Maya Ortiz.
Whichever offer you recommend is the one she actually signs Friday. There's no 'take more time to
think about it' — the deadline is real." Let the stakes land before moving to the Launch.

## Launch

Read Maya's two nicknames for the offers out loud — the Steady Offer and the Frontloaded Offer —
with no numbers attached yet. Ask: "If all you knew was those two names, which sounds better to
you, right now, and why?" Take answers without correcting anyone. Most rooms will split roughly
along a "steady is safer" vs. "frontloaded is more money now" line — record that split out loud,
because the case's job is to replace both gut reactions with an actual number.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the Frontloaded Offer — the one with the smaller base
salary?" Show of hands, both options, no discussion. Record the count — Close will ask again.

## Anchor 2 — What is the problem we're solving?

**"Is 'which offer pays more' the right question?" · "What do you mean by 'better' — better on day
one, or better by the time Maya actually leaves?"**

Push the room to state the actual metric before touching an appendix: not "which base salary is
bigger" and not "which signing bonus is bigger," but cumulative net value **as a function of how
long Maya stays**. If the room lands on "we can't answer this with one number — we need an
equation for each offer, in terms of time," the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Make the room name the steps before opening an appendix: (1) find each offer's net monthly value
(base salary minus any recurring cost, plus any recurring benefit), (2) write each offer as
V(t) = (net monthly value)(t) + (signing bonus) — a linear equation with slope and y-intercept
pulled straight from the offer data, (3) graph both lines on the same axes, (4) solve the two
equations together as a system to find the exact month they cross, (5) use the equations (not just
the graph) to name a winner at two different assumed tenure lengths, one on each side of the
crossover. Re-ask: "Now that we can see the steps, is our question still the right one?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the one honest gap: Appendix C's commuting + parking figure (MA1) is a stated modeling
assumption, not a sourced number — no public source publishes one combined figure for a generic
mid-size-metro commute, so the case built it from an IRS per-mile rate and a representative parking
rate. Ask: "If this number were higher or lower, would it change which offer eventually wins over
several years — or just move the exact crossover month?" A sharp Hero should be able to say it only
moves the crossover month; Cascadia's base-salary advantage is large enough that MA1 alone can't
flip the multi-year winner.

## Data Deep Dive

Now, and only now, open Appendices A–C and work D1–D4. Cold-call for D3 specifically — this is
where a Hero who correctly wrote both V(t) equations (D1) but never solved them together will not
yet have an exact answer, only a graph-based guess.

**Facilitator-only arithmetic note.** Net monthly value: Cascadia $96,250/12 − $520 = $7,500.83;
Northwind $80,000/12 + $313.33 = $6,980.00. Setting 7500.83t + 8663 = 6980.00t + 12000 gives
520.83t = 3337, so t ≈ 6.41 months (≈ $56,721). Full derivation in `case.json.balance.margin_basis`.

## Twist

**Twist: N/A.** This case's tension is a genuine, already-fully-disclosed two-variable trade-off
(a steeper slope vs. a higher starting value) that resolves entirely through the system of
equations the Challenges already require — there is no additional real-world fact withheld from
Appendices A–C whose reveal at the 15-minute mark would invalidate a popular position without
either (a) leaking the margin's size/direction into case.md, which the case-write skill's balance
rule forbids, or (b) inventing a number the research pass didn't source, which this case does not
do. The Data Deep Dive's own D3 crossover reveal (many rooms expect the higher-base offer to need
"about a year" to catch up; the real crossover is ~6.41 months) already produces the
surprise-and-recompute moment a Twist is meant to create, without adding new information — see
Anchor 4 and the Immediate Recommit note below, which the facilitator should treat as carrying that
weight instead.

## Immediate recommit

Right after D3 lands on the board, ask by name: "The exact crossover is about 6.41
months — is that sooner or later than you expected before you did the algebra? Does it change your
vote?" Many Heroes who voted for the Steady Offer at Anchor 1 on a "safer year-one number" instinct
will not have realized how quickly Northwind's head start gets erased; conversely, a Hero who voted
Frontloaded expecting it to "obviously" win for a normal 2+ year tenure should recompute in front of
the room.

## Deep conflict — two threads (20–30 min)

1. **Slope vs. y-intercept: what "better" depends on.** Walk the room through why a lower
   y-intercept with a steeper slope always eventually overtakes a higher y-intercept with a
   shallower slope — the only question `case-write`'s system-of-equations tools can answer is
   *when*. Push a Hero to state, in plain English, why "the bonus is worth more" and "the base
   salary is worth more" are both true statements that need a time horizon attached to mean
   anything.
2. **What D3's exact month actually decides.** D4 asks for a recommendation at two tenure lengths,
   one on each side of the crossover. Push past "Maya should just pick whichever offer wins for how
   long she plans to stay" to the harder, honest point: Maya does not actually know how long she'll
   stay at either job. Ask: "Given that uncertainty, is there a case for weighting the *short*-tenure
   scenario more heavily, even though the long-run multi-year margin favors the other offer?" There
   is no single correct answer; the point is that the model doesn't remove the judgment call, it
   just makes the judgment call precise instead of vague.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — read both offer nicknames with no numbers, cold-call for a gut read |
| 3:00–10:00 | Position defense — *"Walk us through your V(t) equation for your chosen offer — what's your slope, what's your y-intercept, and where do they come from in Appendix A or B?"* |
| 10:00–15:00 | Pressure-test the process — *"Which of your D1 numbers, if it changed, would move your crossover month — and which would change your equation but not who eventually wins?"* |
| **15:00** | **DROP THE TWIST (N/A — instead, land the D3 crossover reveal)** — 6.41 months, sooner than most rooms expect |
| 15:00–20:00 | Immediate recommit — does the exact crossover month change anyone's vote |
| 20:00–30:00 | Threaded deep conflict (slope vs. y-intercept; what to do about tenure uncertainty) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

A Hero compares only day-one or year-one numbers — total signing bonus size, or which base salary
is bigger — and picks an offer without ever extending either number past month one. That comparison
is not wrong, exactly; it is *incomplete*: it silently assumes a tenure of zero (or one) months,
which is nobody's actual plan. The named trap in this case is exactly that failure mode: for anyone
who expects to stay more than roughly 6.41 months, the offer that looks better on day one
(Northwind's bigger bonus) is not the offer that delivers more cumulative value by the time they'd
actually leave. A Hero who never sets up and solves the system of equations has no way to know which
side of that line their own plans put them on — they are guessing, even if they guess right.

**A second, quieter trap lives inside the correct methodology, not before it — watch for it even
in Heroes who did build V(t) equations.** A Hero can write both equations in the right *form* and
still smuggle in an asymmetry: treating Northwind's $313.33/month 401(k) match as "not really
income, it's locked up until retirement" and excluding it from B's net monthly value, while still
subtracting Cascadia's $520/month commute cost from A's — two real recurring dollar flows treated
inconsistently because one *feels* more like a bill and the other *feels* more like savings. Either
treat both as immediate net cash flow (as this case's answer key does) or neither; a Hero who drops
only one produces a plausible-looking but wrong crossover month. The same asymmetry can appear as a
units slip — plugging an annual salary directly into a per-month slope instead of dividing by 12 for
one offer but not the other. Cold-call a Hero's D1 net-monthly-value line item by item (not just
their final V(t)) to catch this before it reaches D3.

## Socratic questions

1. Your V(t) equations for the Steady Offer and the Frontloaded Offer have different slopes and different y-intercepts — which offer has the bigger head start, and which one is gaining ground faster every month?
2. You solved for the exact month the two lines cross. What does that number *mean* to Maya, in plain English, that a "the bonus is worth more" argument doesn't capture?
3. If Maya told you today, honestly, that she doesn't expect to stay at either job more than a year, does your recommendation change? Why or why not, using your own equations?
4. Two people could look at the exact same two offer letters and correctly recommend opposite options. What is the one piece of information about Maya's own plans — not about the offers — that decides which of them is right?
5. Cascadia's 401(k) column says "None offered" — you didn't need Appendix C for that one. What's the difference between a constraint you can read directly off a table and one you have to compute? Which deliverable required which?

## Close

**VOTE AGAIN.** "Did your recommendation change — or just your confidence in the number behind it?"
Ask what math was new to each Hero, and specifically whether writing the V(t) equations (D1),
solving the system (D3), or naming a winner at two tenure lengths (D4) was the step that actually
changed their thinking.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes' Anchor-1 gut vote (Steady vs. Frontloaded) matched their post-D3 recommendation,
  or whether the exact crossover month (~6.41 months) flipped a meaningful share of the room.
- Whether the "which offer is better depends on how long you stay" framing landed as an obvious
  point restated with numbers, or as a genuine reframe of a question Heroes initially treated as
  having one fixed answer.
- Whether any Hero challenged Appendix C's MA1 commuting-cost assumption in Challenge 2, and
  whether they correctly identified that it moves the crossover month but not the long-run winner.

## Standards Touched On

System Of Equations; Slope; Y-Intercept; How to write a linear equation given a set of data; How to
identify the slope of a line given a set of data, or a graph of a line of a set of data, or its
linear equation; How to solve a system of linear equations; How to draw a line of a set of data
given its linear equation.

## Facilitator note — sensitivity (SPEC §6)

Per SPEC §6: this case touches a real personal-finance decision (income, cost of living, employer
benefits) but at comparatively low stakes — a career and income choice, not illness, death, or
acute hardship. No special framing beyond normal care is required, but the facilitator should be
alert to a room where a Hero's real family financial pressure makes the "which offer is objectively
better" framing land more personally than expected; keep the discussion on the computable model,
not on judging any Hero's real circumstances.
