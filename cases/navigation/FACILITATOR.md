# Navigation — Facilitator Guide

**Sensitive-subject flag (SPEC §6):** this case turns on a medical emergency (labor/childbirth)
and a livelihood-ending financial penalty. Neither is graphic, but a guide should read the room —
a Hero with a personal connection to a difficult birth or to a parent's job loss may need a beat
before diving in.

## Argument for A (The Clean Run)

The real time gap between the Clean Run and the Hot Run is small: **67 seconds, 18.15%** of the
Clean Run's own total (Appendix C/sensitivity_model.py `evaluate()`, +6 mph over the limit on
every segment). Most of the route's total time is stop-sign delay on ordinary streets, not speed —
Route 9's one highway stretch is the only segment where speeding buys real time without a stop
sign eating part of it back. Against that modest saving, Option B risks a fine north of $10,000
plus the loss of the only license Filberto has ever needed to earn a living — priced conservatively
at one year of the real U.S. median taxi-driver wage, $42,100 (Appendix E, S1), for a combined
exposure of roughly $52,100 if a single camera catches him. Zero traffic on a Sunday morning also
means zero cover: every intersection is watched, and there is no crowd to hide a violation in.

## Argument for B (The Hot Run)

Rachel's first child arrived about 1.5 hours after labor began, and 20 minutes of that window are
already gone — by that pace, something on the order of 70 minutes may be left, and second labors
often move faster than first ones, not slower. Sixty-seven seconds is a small number against a
whole trip, but it is not a small number against a shrinking, life-and-death buffer — every one of
those seconds is a second Filberto does not get back. The fine is real and severe, but it is a
number on paper; a baby arriving in the back seat of a cab, or arriving too late for something to
go wrong, is not.

## The margin

**Primary metric: total drive time, Hotel to Hospital (seconds).** Option A (Clean Run) = 436.6 seconds
(7:16.6). Option B (Hot Run, +6 mph over the limit on every segment) = 369.5 seconds (6:09.5). Margin
`(A-B)/B` = **18.15%**, inside the SPEC §2 20% cap — computed by `sensitivity_model.py:evaluate()`.
The two ordinary-street segments (Cannery Row, Fairview Ave) carry 6 of the route's 8 stop signs
between them; the highway segment (Route 9) carries none. This is why the time gap is real but
modest: speeding on a stop-sign-heavy street buys back very little, because most of the delay on
those streets is the stop, not the drive between stops.

## Five Socratic questions

1. Your Clean Run and Hot Run tables come out about 67 seconds apart — what percent of the whole Clean Run trip is that, and does seeing it as a percent change how confident your pitch is?
2. D4 asks you to price Option B's risk in dollars per minute actually saved — what number did you get, and what does it tell you about whether the time saved is "worth it" in Filberto's own terms?
3. Route 9 is the only segment with zero stop signs — if it were twice as long and Cannery Row and Fairview Ave were half as long, what would happen to the total time Option B saves?
4. Rachel's first labor ran about 1.5 hours start to finish, and 20 minutes are already gone — how many of the minutes she may have left does your Hot Run actually buy back?
5. If Modus City's law fined a driver only for how many seconds over the limit they were caught, instead of one flat $10,000 regardless of the violation, would your pitch change?

## The trap

Heroes reliably eyeball the two options and assume speeding "obviously" saves a lot of time,
because a 25-to-31-mph street feels like a big jump. It is not, once you actually build the
segment-by-segment table: **most of this route's total delay is stop-sign time, not driving
time**, and a stop sign costs the same 4-9 seconds no matter how fast the car was going before it
stopped. A Hero who speeds through Cannery Row and Fairview Ave without noticing this will report
a Hot Run time far faster than the real arithmetic supports — the guide should watch for a D3
total that is suspiciously close to (Clean Run time) × (25/31), which is the wrong-route error of
scaling the *entire* trip by the speed ratio instead of recomputing each segment (including the
fixed stop-sign seconds) individually.

**A second, independent trap sits in D4.** D2/D3 train a Hero to compute and report *grand total*
trip times for each option — those big numbers are what's sitting in front of them when D4 asks
for "dollars of risk per minute **actually** saved." The fluent, wrong move is to divide the total
dollar exposure by one option's total trip time (giving a tame, misleadingly small rate) instead
of by the small *delta* between the two options' totals — the minutes the Hot Run genuinely buys
back. Watch for a D4 answer built on a denominator anywhere near "5-7 minutes" instead of the real
~1-2 minute time-saved figure; it will produce a rate an order of magnitude too small and undercut
the case's actual point.

## The Twist — Route 9 is closed

At roughly the 15-minute mark, reveal: **Route 9, the one divided highway on this route, is closed
overnight for construction.** Filberto has to detour: Fifth Ave (0.7 mi, 3 stop signs: 1 left, 1
right, 1 straight) and Ridge Rd (0.6 mi, 2 stop signs: 1 left, 1 right) replace the highway segment
entirely. Recompute with `sensitivity_model.py:evaluate_twist()` (case.json `derived.twist_option_a_total_time_s`
/ `twist_option_b_total_time_s`): both options get slower, B is still faster, and the **margin grows
to 20.20%** — it now breaks the SPEC §2 cap. The size of the time Option B buys back is no longer
small. The Clean Run argument's core claim — "the time saved isn't worth the
risk" — gets measurably weaker at exactly the moment there are also two more stop signs' worth of
extra camera exposure per run. Ask directly: **"What just broke in your original model? Was your
Clean Run pitch wrong, or was it just missing information?"**

## Sensitivity note (Tier 2 probe 5)

`sensitivity_model.py` declares `FLEX = ["speeding_mph_over", "license_loss_years"]` — the two
genuine author-chosen dials (how many mph over Option B's illustrative worked answer drives, and
how many years of income a "permanent" license loss is conservatively priced at), as distinct from
the route's fixed fictional scenario facts (segment distances, stop counts, posted limits) and the
one real cited figure (median taxi wage, stress-tested by P6 instead).

- **`speeding_mph_over` ±50% (6 → 3 or 9 mph):** at -50% (3 mph over) the margin drops to 9.2% —
  still balanced. At +50% (9 mph over) the margin rises to 26.9% — **breaks the 20% cap**. B never
  stops being the faster option at either extreme (no flip), but the case's "the time saved is
  modest" framing only holds for a genuinely modest speeding choice; a Hero who pitches a much
  larger speed increment is pitching a materially less-balanced case and should say so.
- **`license_loss_years` ±50% (1 → 0.5 or 1.5 years):** has **zero effect** on the graded primary
  metric (drive time) — it only scales D4's supplemental dollars-risked-per-minute figure, which
  is disclosed context, not the graded comparison. This is itself a real, worth-naming finding:
  the time-based verdict is completely insulated from how conservatively or generously the case
  prices "permanent."

**Verdict: PASS_DISCLOSED.** No flip under either dial; one real cap-breach under
`speeding_mph_over` at +50%, disclosed here and in `case.json.sensitivity_disclosure[]` rather than
left for a guide to discover live.

## Guide Notes — the anchor ladder

### Intro

Frame the format: a Socratic discussion, not a lecture. Read the taxi-hail scene aloud, or play
it as a two-voice read (Thomas/Filberto). Name the opener: *"You're already going the speed
limit. Do you go faster — or not?"*

### Launch

Show the Appendix A map on the board, zoomed to the hotel/hospital pins. Let the room sit with
the distance for a beat before anyone speaks.

### Anchor 1

TAKE A STAND AND VOTE. No reasoning yet. *"Is anyone courageous enough to stand with Filberto's
Clean Run — or his Hot Run?"* Get a show of hands, no debate.

### Anchor 2

WHAT IS THE PROBLEM WE'RE SOLVING? *"Is this just about which is faster, or is there something
else we need to weigh?"* *"What do you mean by 'worth it'?"* Let confusion grow — *"Wow, this is
a challenging problem"* — before moving on.

### Anchor 3

WHAT IS THE PROCESS? *"If we build both time tables and find the gap, how do we actually decide
from there?"* *"Is comparing raw minutes enough, or do we need the risk side of this too?"*
Re-ask: *"Is our question still the right question?"*

### Anchor 4

WHAT DON'T WE KNOW? *"Do we know exactly how much time speeding buys? Do we know exactly what a
lost license costs Filberto? What are we assuming?"* Surface Appendix D's MA1 (the one-year
income assumption) here if nobody has raised it yet.

### Data Deep Dive

Now, and only now, work the Appendix C segment table live. Build the Clean Run total together;
let table groups build the Hot Run total on their own numbers.

### Twist

Deliver the Route 9 closure slowly, with a pause. *"You now have 60 seconds. Are you changing
your plan — or not?"*

### Close

Vote again. *"We asked whether Filberto should speed. Did we ask the right question?"* *"What
math was new to you, and how did you attack it?"*

### Lessons Learned

Name the trap explicitly if nobody caught it live: most of this route's delay is stop signs, not
speed.

### Standards Touched On

Read Appendix F aloud; ask which "how to…" question each Hero actually used.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote on Anchor 1 — no explanation |
| 3:00–10:00 | Position defense: "Convince us it's the better call, not just the fair one" |
| 10:00–15:00 | Pressure-test: "Whose Hot Run number would fall apart if a stop-sign count were off by one?" |
| **15:00** | **DROP THE TWIST** — Route 9 is closed |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00–30:00 | Threaded conflict: (1) time-value-of-a-minute vs. dollar-risk framing; (2) whether a "conservative" one-year income assumption undersells the real cost of "permanent" |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands

| Band | Typical size | What changes |
|---|---|---|
| Full (12–20) | the case as written | Anchors run as written; table groups build both Clean Run and Hot Run tables independently before comparing |
| Compressed (6–11) | roughly half | Anchors 2–3 combine into one pass; the room builds one shared Hot Run table (one agreed mph-over choice) instead of every Hero picking their own |
| 1:1 / pair (1–2) | one or two Heroes | No vote to take — Anchor 1 becomes a stated initial position; the guide plays devil's advocate directly, arguing whichever side the Hero didn't pick; the Twist still lands but "who reverses" becomes "would you reverse, and why" |
