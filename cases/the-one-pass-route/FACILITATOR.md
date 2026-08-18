# Facilitator Guide — The One-Pass Route

MS | Guide Notes | Adventure | 2026

**Tier:** T3 (MS stretch / HS entry) · **Primary metric:** deadhead ratio — total miles driven per
mile of street actually serviced, for one full sweep of the Larkspur Hollow network · **Margin:**
**1.9%** on the stated primary metric (1.2285 → 1.2050) — close, in the project's own "defensible"
range. **Read this whole guide before running the discussion**: the case's real tension is not the
ratio margin, it is what happens when you convert that margin to dollars.

## Intro

Frame the format before the map ever comes out: this is Renata's own routing memo, due to a real
division director by end of day, not a worksheet about graphs. Say plainly: *"Both options are
already sitting on Renata's desk. The room's job today is to write the memo she'd actually sign."*

## Launch

Hand out (or project) Larkspur Hollow's street map — Appendix A's vertex/edge list is enough, drawn
out or sketched on the board. Ask one question and take answers without correcting any of them:
*"If you had to sweep every one of these streets and end up back where you started, could you do
it without ever driving down the same block twice?"* Let the guesses stand; Anchor 2 comes back to
this.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

*"Show of hands: As-Is Loop, no construction — or petition for the Persimmon Connector?"*
Show-of-hands, both options, no discussion permitted yet. Record the count — the Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'closes into one loop'?"**

Let confusion grow here; it is deliberate. The room will want to say "just find the shortest route"
without asking what makes a route unable to close into a single loop in the first place. Push:

- *"What has to be true about every corner on this map for a route to never repeat a block?"*
- *"If 48 of the 58 corners fail that test, does adding one new street fix all 48 of them, or just
  two?"*
- *"Whose problem is a slightly longer route — Renata's, or the division director's, or both?"*

Do not resolve this. A room that leaves Anchor 2 still arguing about *what* "closing the loop" even
requires is exactly where it should be.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Make them name the steps before any appendix is opened:

1. Count how many street segments touch each corner (D1) — even or odd.
2. Use the odd/even count to determine whether a single-pass route is possible at all (D2).
3. If it isn't, find the minimum extra mileage needed to pair up every odd corner and close the loop
   (D3).
4. Test whether adding one new street (the Persimmon Connector) changes the odd/even count enough to
   matter, and at what one-time cost (D4).

Re-ask: *"Now that we can see the steps, is our question still the right question?"*

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the honest gaps, all of which live in `case.md` Appendix E:

- Larkspur Hollow's exact street layout doesn't exist for the fictional Talbrook, so this case uses
  a real town's real streets (Seaside, FL) as a stand-in (MA1).
- Where a mapped street's data run keeps going for miles past any sensible neighborhood boundary,
  someone had to draw a line for what counts as "Renata's district" (MA2).
- How often Larkspur Hollow actually gets swept isn't published anywhere for a fictional city, so
  this case adopts a real municipal program's stated frequency (MA3).

Ask which of these changes the recommendation if it moves, and which only changes the size of the
answer. MA3 is the one worth pressing on directly — it moves every dollar figure in Appendix D but,
as Appendix E's own sensitivity note says, it cannot move the deadhead-ratio margin by even a
fraction of a percent. A Hero who assumes every assumption must be equally load-bearing has missed
that.

## Data Deep Dive

Now, and only now, the numbers.

Work D1 → D4 as a room. Cold-call specifically on **D2**: a Hero who counts 48 odd-degree vertices
and says "the route is just hard" rather than "a true single-pass route is mathematically
impossible, not merely difficult" has not actually applied Euler's theorem — fish for the sentence
that names *impossible*, not *hard*.

Two facilitator-only notes to hold in reserve:

- **The Practice Block (D3) is not a toy version of D2's answer.** Its own 14-odd-vertex distance
  table is real Dijkstra output over a real 23-vertex excerpt — a Hero should get a Practice Block
  deadhead ratio close to, but not identical to, the full network's 1.2285, and should be able to
  say *why* (a smaller sample skews toward whichever few odd vertices happen to sit in the excerpt).
- **D4's two dollar figures are not there to trip anyone up on arithmetic.** They are there so a
  sharp Hero notices the conclusion doesn't change between them — the real skill being tested is
  recognizing when a nearly-5× uncertainty in one input simply doesn't matter to the decision.

Full worked figures live in the **Facilitator-only numbers** section below.

## Twist

**Twist: N/A.** Unlike a case where a mid-discussion event forces a recompute, this case's whole
pedagogical payload is the tension between two lenses that are both fully knowable from Appendix C
and D at the start — the ratio margin (1.9%, favors the connector) and the payback period (millions
of years, favors doing nothing). Introducing a mid-discussion event on top of that would either
leak one side of that tension early or bury the real question (which metric should decide a real
capital request) under a second, unrelated complication. Anchor 2 and the Deep Conflict section
below already carry the pressure a twist would otherwise add.

## Deep conflict — one thread (T3 compression: pick one, do not attempt three)

**A metric that says yes versus a dollar figure that says no, computed from the exact same data.**
The deadhead ratio genuinely, measurably improves with the connector — that is not in dispute. The
payback period, built from the same underlying graph plus three real sourced dollar figures, is
longer than recorded human civilization. Push: *"If your department's only stated success metric
is deadhead ratio, and it never once mentions a dollar amount, is 'the metric says so' ever enough
reason, by itself, to ask for half a million real dollars?"*

## The trap

The case's stated primary metric (deadhead ratio) says the connector wins, by a margin squarely in
this project's own "close and defensible" range. A Hero who computes only that number will
confidently recommend The Persimmon Connector. But Appendix D's dollar figures, computed from the
same underlying data, show the connector's real payback period is not merely long — it is longer
than recorded human history, several times over. The two lenses do not just disagree in degree;
they point in opposite directions almost totally, and the case does not resolve which one should
decide Renata's memo.

A second-order trap for a sharp Hero: Appendix D shows *two different* sourced construction-cost
figures ($1,600/ft vs. $345/ft, a 4.6x spread) — and it does not matter which one is used. The
payback period is millions of years either way. A Hero who spends their pitch litigating which
construction estimate is more accurate has missed that the conclusion is completely insensitive to
that choice.

## Socratic questions

1. Appendix B tells you 48 of 58 vertices are odd. Why can't a route ever avoid repeating some street segment if that count is anything other than 0 or 2?
2. Your Practice Block deadhead ratio (D3) and the full network's official deadhead ratio (Appendix C, Part 2) are close but not identical — what real difference between the two networks explains that gap?
3. The deadhead ratio says the connector wins by 1.9%. The payback period says it would take roughly three million years to earn back its own construction cost in fuel savings. Both numbers came from real, correctly-computed data — how can they both be right, and which one should actually decide Renata's memo?
4. Appendix D shows two different real construction-cost estimates, nearly 5x apart, and the conclusion doesn't change either way — when does a big uncertainty in one number not matter to a decision, and how do you tell, before you've done the arithmetic, whether it will?
5. If Renata's memo used deadhead ratio as her department's only stated success metric and never mentioned a dollar figure at all, would The Persimmon Connector be the "correct" answer by her own department's rules — and what does that tell you about how a department should choose its metrics in the first place?

## 45-minute Socratic plan

| Time | Beat |
|---|---|
| 0:00–3:00 | Intro + Launch — frame the memo's real stakes, put the street map up, take the gut-read question without correcting anyone |
| 3:00–8:00 | Anchor 1 — take a stand and vote, no reasoning yet |
| 8:00–15:00 | Anchor 2 — "what does 'closes into one loop' even require?" Let the room sit in the ambiguity |
| 15:00–20:00 | Anchor 3 — name the four-step process before opening any appendix |
| 20:00–25:00 | Anchor 4 — surface the three assumptions (MA1–MA3); ask which are load-bearing |
| 25:00–35:00 | Data Deep Dive — work D1→D4 as a room, cold-call on D2's "impossible, not hard" distinction |
| 35:00–40:00 | Deep conflict — the ratio that says yes vs. the dollars that say no. No TWIST to drop in this case (see Twist: N/A above); this slot carries the "which metric should decide" pressure instead |
| 40:00–45:00 | Close — re-vote, "did we ask the right question?", lessons learned |

## Close

**VOTE AGAIN.** Then: *"Did we ask the right question at the start?"* and *"What math was new to
you tonight, and how did you actually attack it?"*

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

## Standards Touched On

Vertex · Path · Cycle · How to determine whether a graph has an Euler path or circuit

## Facilitator note — sensitivity

Not required (SPEC §6) — this case is a municipal budget-and-routing decision with no illness,
death, money stress, or family-hardship content. No facilitator flag is needed beyond ordinary care
with a case that touches a real household's tax dollars.

## Facilitator-only numbers

Every figure below is reproduced exactly by `cases/the-one-pass-route/sensitivity_model.py`.

| | The As-Is Loop | The Persimmon Connector |
|---|---|---|
| Base street mileage | 3.9597 mi | 4.0169 mi (adds the 302-ft / 0.0572-mi connector) |
| Minimum repeat mileage | 0.9046 mi | 0.8236 mi |
| Total miles driven, one sweep | 4.8643 mi | 4.8405 mi |
| **Deadhead ratio** | **1.2285** | **1.2050** |
| Odd-degree vertex count | 48 | 46 |

**Margin.** `margin_pct` = **1.9** (computed on deadhead ratio: (1.2285 − 1.2050) ÷ 1.2285).
`margin_basis`: The As-Is Loop's official deadhead ratio (Appendix C, Part 2) against the deadhead
ratio after the connector is built (Appendix D), both computed the same way over the same full
58-vertex network.

**Dollar side (Appendix D).** Construction cost: 302 ft x $1,600/ft = $483,200. Annual fuel-cost
savings at 6 sweeps/yr, 5.2 mpg, $5.257/gal: **$0.14/year**. Payback period: **≈3.35 million years**
— five to six orders of magnitude past any real 20–40-year municipal capital-planning horizon.
Using the lower-bound $345/ft reference figure instead: $104,190 construction cost, payback ≈722,000
years — the conclusion does not change.

**Sensitivity, the one genuine flexible assumption (MA3, sweep frequency, per Tier 2 probe 5's
standard flex):** flexing sweep
frequency up or down moves the annual fuel savings and the payback period proportionally, but never
brings the payback period within reach of a real capital-planning horizon in either direction, and
it has **zero** effect on the deadhead-ratio margin (1.9% stays 1.9% at any sweep frequency),
because deadhead ratio is a per-sweep, frequency-independent quantity by construction. This is the
case's own disclosed finding (Appendix E, MA3), not a limitation of the model.

**The verdict.** The Persimmon Connector wins on the case's stated primary metric (deadhead ratio)
by **1.9%** — close, defensible, and in this project's own "the metric genuinely moved" range. The
As-Is Loop wins decisively on the only dollar-denominated lens available, by five to six orders of
magnitude. The case does not pick a winner between the two lenses; that choice is the discussion.
