# Guide Notes: Wind Triangle

**Case:** Wind Triangle · **Tier:** T4 · **Band:** HS · **Studio:** Launchpad
**Standards:** Pre-Calculus / Vectors — the complete seven-skill group, all `new_coverage` — plus four
already-covered supports (Pythagorean theorem, right triangle, compound-unit conversion,
percent of a number). Exact ids in `case.json.standards[]`.

**Status:** drafted at `case-write` and filled at `case-research`, both 2026-08-12. Current
`margin_pct` = **1.67** (Routing B cheaper). Every figure quoted below resolves in
`case.json.derived` or in `case.md`, and is reproduced live by `sensitivity_model.py`; this file is
re-checked for drift at every readiness run (the continuity checks in `case-readiness`).

## Intro

Frame the format before anything else. This is not a word problem about airplanes — it is a real
job with a real signature on it. Name the opener: *"You hold an aircraft dispatcher certificate.
By law you and the captain are jointly responsible for this flight, and the fuel number on the
release is yours. Push is in under an hour."* Say plainly that both routings in front of them are
legal, filable, and defensible, and that the room's job is to decide which one they would put
their own certificate number on.

## Launch

Show a real jet-stream analysis chart for the case's date — any public upper-level wind chart will
do, as long as the ribbon of fast air is visible crossing the country. No route lines drawn on it
yet, no numbers read out. Ask one question and take answers without correcting any of them:
*"If you were flying from New York to Los Angeles tomorrow morning, would you rather go over the
top of that, under it, or straight through it?"* Let the gut reads stand. They will be revisited at
the Close.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

*"Is anyone courageous enough to stand with Reza on the long way round?"* Stand-or-sit, both
options, no discussion permitted. Record the count on the board — the Close will ask for the vote
again and the comparison is the point.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'the better route'?"**

Let confusion grow here; it is deliberate. The room will want to say "the shorter one" or "the one
with less wind," and both are wrong in an interesting way. Push:

- *"Better at what? Name the unit."* (Nautical miles? Hours? Pounds? Dollars? They are not the
  same ranking.)
- *"The case says the wind is stronger on one route. Stronger in what direction?"*
- *"If a route were twenty percent longer but the airplane went twenty percent faster along it,
  which one costs more fuel?"*

Do not resolve this. Say out loud: *"Wow — this is a harder question than it looked."* A room that
leaves Anchor 2 still arguing about the unit is exactly where it should be.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Now make them name the steps before any appendix is opened. The chain they should arrive at, in
some form:

1. Turn each published wind into a vector with components (D1).
2. Turn each leg's course into a unit vector (D2).
3. Project the wind onto the course to get the part of it that actually pushes back (D3).
4. Add the air vector and the wind vector to get ground speed (D4).
5. Divide distance by ground speed to get time, multiply time by fuel flow to get fuel (D5).

Re-ask: *"Is our question still the right question, now that we can see the steps?"* If someone
notices that step 3 is where "the wind is stronger" turns into a number that might be smaller than
the wind speed, that is the whole case arriving early — do not step on it, but do not confirm it
either.

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the honest gaps, all of which live in `case.md` Appendix E:

- The wind field is a **forecast for a stated date and hour**, not a measurement of this flight.
  Everything downstream inherits that.
- One wind vector is applied per leg and held constant along it (MA3). A real system interpolates
  continuously.
- The forecast-error band the dispatcher plans against (MA2) is stated, not measured for this
  flight.
- The scheduled block time and what missing it costs (MA1) belong to a fictional carrier.

Ask which of these changes the recommendation if it moves, and which merely changes the size of
the answer. The answer is worth withholding: the wind field changes the recommendation; the fuel
flow does not, because both routings burn at the same rate and it cancels out of the comparison.
A Hero who works that out unprompted has understood the structure of the case.

## Data Deep Dive

Now, and only now, the numbers.

Work D1 → D5 as a room. Cold-call specifically on **D3**, the dot product: this is where a Hero who
has treated "dot product" as a formula to memorise rather than a tool that answers a question will
visibly struggle, and that struggle is information, not a moment to rescue. The sentence to fish
for is some version of *"only part of the wind is pointed at us."*

Two facilitator-only notes to hold in reserve:

- **The crosswind is not free.** A large crosswind component reduces ground speed even when the
  along-course component is zero, because the aircraft must crab into it and spend part of its
  airspeed going sideways. That is what the √(TAS² − crosswind²) term in D4 is doing. Most rooms
  miss this entirely and it is a good late-stage prompt.
- **The metric hides in plain sight.** "Fuel per nautical mile of *net progress*" divides by the
  direct distance between the airports, not by the distance actually flown. Ask why the case
  defines it that way, and whether a route could look good on fuel-per-mile-flown while being
  worse on fuel-per-mile-of-progress.

Full worked figures — leg components, along-course and crosswind components, ground speeds, leg
times, trip fuel for each routing, the break-even, and the recorded `margin_pct` — are in
`case.json.derived` and reproduced in the **Facilitator-only numbers** section below.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses.

*"It is now forty minutes to push. A line of thunderstorms has gone up across the Ozarks, and
air traffic control has shut the corridor through Springfield. Nobody is going through there
tonight."*

*"If you still want the southern plan, you re-file it through Memphis instead — which is further
again. Both of those waypoints are already in your corridor file, so you can price it. Same
aircraft, same fuel flow, same rules."*

*"You have about a minute. Is the southern plan still the plan?"*

Then the follow-up, which is the actual point: **"What just broke in your original model? Were you
wrong — or were you missing information?"**

**Facilitator-only: what the numbers actually do.** Routing B re-filed through KMEM runs 2,467.0 nm
of filed track instead of 2,402.7 nm, and burns **28,410.4 lb** instead of 27,756.2 lb — which is
**181.4 lb more than Routing A's 28,228.9 lb**. **The verdict flips.** Routing A becomes the cheaper
plan by **0.64%**, a margin thinner than the one it just overturned. Every position built on "the
southern route is cheaper" is now wrong, and the room has to notice that the thing that changed was
not the wind but the distance.

The twist introduces **no new number**: KMEM's position is in Appendix A's corridor-file table and
its 34,000 ft wind (350/17) is in Appendix B. Everything needed is already in the packet, which is
why a Hero can genuinely price it in the room.

**One honest caveat, and hand it over if a Hero pushes.** The flip depends on MA2, the
airway-structure allowance. At the low end of MA2's ±50% flex range for the southern corridor
(0.75% instead of 1.5%) the reroute does *not* flip the verdict — Routing B stays cheaper by 0.10%.
The flip holds for every southern allowance from about 1.0% upward and under all of MA5's course
conventions, but at the thinnest of those it is only 0.08%. This is a real reversal, not a robust
one. It is written out in the facilitator-only half of `case.md`; MA2's student-facing sensitivity
column deliberately does **not** mention the twist, because naming it there would hand the room the
amendment before it is dropped. A Hero who challenges the direction of MA2 is not being difficult;
they have found the load-bearing assumption.

Do not hand the arithmetic over unprompted. A Hero who says *"I would need KMEM's course and its
along-course component before I answered"* has given the strongest possible answer and should be
told so.

## Immediate recommit

Re-vote at once, by name where the room is small enough. Ask: *"Did the amendment change your
vote, or only your confidence?"* That distinction is the transferable skill; the vote itself is
not.

## Deep conflict — three threads (20–30 min)

1. **Certain cost versus forecast benefit.** The extra track miles on the southern routing are
   real and are spent whether or not the forecast verifies. The saving is conditional. Is a
   dispatcher who declines to pay a certain cost for a probable benefit being prudent, or being
   superstitious about forecasts?

   **Guide: do not let the room finish this thread believing the northern routing is the "safe"
   one.** It is the opposite, and the numbers are unambiguous. Scale the whole published wind field
   from 0× to 1.5× and Routing A's trip fuel moves **3,489 lb (+12.4%)** while Routing B's moves
   **86 lb (+0.3%)** — Routing A is the plan whose cost depends on the forecast, because Routing A
   is the plan with the large winds in it. Routing A only becomes cheaper below about **0.80×**,
   i.e. if the field is overstated by roughly a fifth *in that one direction*; an error of the same
   size the other way makes Routing A worse still. The defensible form of Argument A is therefore
   not "B's benefit is uncertain" — that claims A is the lower-variance choice, and it is not — but
   "the gap is small enough that I would rather not pay 136 certain miles for it," and that claim is
   now evidenced rather than asserted: `case.md` Appendix F [S8] cites peer-reviewed verification
   research (Schafler et al. 2020, *Monthly Weather Review*) documenting individual-case
   jet-stream-level wind errors up to ±10 m/s (≈19.4 kt) in NWP analyses/short-range forecasts —
   several times the 7.2 kt/leg break-even — concentrated in exactly the upper-level-ridge structure
   that produces this case's own strongest winds. It verifies a different jet and forecast system
   (North Atlantic, ECMWF/Met Office, not the domestic NWS FD product this case cites), so it is not
   proof of this issuance's own error; a guide pushed on that point should say so. If a Hero reaches
   for "safer" or "certainty," ask which routing the uncertainty actually lands on (A) — then ask
   them to defend the narrower, noise-floor version of the argument instead, which does not depend
   on that claim being true.
2. **Whose number settles it.** The dispatcher signs the release; the captain commands the
   aircraft; the schedulers own the block time. Three people, three different quantities, one
   flight. When they disagree, which quantity should win — and is that a math question at all?
3. **What the reserve rule is really for.** The regulation does not say "carry extra fuel because
   forecasts are unreliable." It says carry fuel to destination, to alternate, plus a fixed
   additional period. Ask whether that rule is doing the job the room assumed it was doing, and
   what it does *not* protect against.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — jet-stream chart, cold-call gut reads, stand/sit vote, no explanation |
| 3:00–10:00 | Position defense — *"Convince us it is better, not just shorter"* |
| 10:00–15:00 | Pressure-test the models — *"Whose ground-speed number is most fragile, and why?"* |
| **15:00** | **DROP THE TWIST** — the amended forecast, delivered slowly, with pauses |
| 15:00–20:00 | Immediate recommit — who reverses, and was it the vote or the confidence that moved |
| 20:00–30:00 | Threaded deep conflict (certain cost vs. forecast benefit; whose number settles it; what the reserve rule is for) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes **will** compare the two routings on the wind's raw published speed — "the northern
wind is ninety-odd knots and the southern wind is not, so the northern route is worse" — and **will
skip** the projection onto the course entirely. A wind angled off the nose contributes only its
component along the track; on a leg where the wind sits well off the nose, most of a very large
wind speed does nothing to ground speed at all, and a Hero who never computes D3 will confidently
report a headwind that is tens of knots too large.

The second half of the same trap: **most will default** to comparing distance flown rather than
time aloft. Fuel is bought by the hour, not by the mile. Watch for a pitch that leads with "it is
two hundred miles longer" and never converts that into hours.

Both halves produce a *confident* wrong answer that looks like work — tables, arithmetic, a
recommendation — which is exactly why it needs naming in advance. Watch for a D3 table whose
headwind column equals the wind-speed column.

**The third trap, and the most convincing one: the FROM/TOWARD sign inversion.** Appendix B says
wind is reported as the direction it blows *from*, so `300/78` is a vector pointing toward 120°. A
Hero who resolves it into components without that 180° reversal flips the sign of every
along-course figure: KDBQ reads **+74.8 kt of tailwind** instead of −74.8 kt of headwind, the first
leg's ground speed comes out near 534 kt instead of 384.7 kt, and Routing A wins by a wide and
completely spurious margin. **The diagnostic for the first trap does not catch this one** — a
sign-inverted table has the right magnitudes, so its headwind column will *not* equal the
wind-speed column. The tell is a D3 table whose signs claim the jet stream is helping a westbound
flight. When a room recommends Routing A on ground speed, ask it to say out loud which way the air
over Dubuque is moving.

## Socratic questions

1. One routing is shorter and one is faster. Which of those two facts shows up in the fuel number, and why does the other one not?
2. Your D3 table gives a headwind component smaller than the wind's own speed on almost every leg — where did the rest of the wind go, and is it doing nothing at all?
3. By what percentage would the forecast headwind along The Great Circle have to be overstated before you would change your recommendation, and is that a percentage a real forecast is ever wrong by?
4. Both routings clear the reserve requirement. Is "it is legal" doing any work in your argument, or is it just the floor you had to clear before the argument started?
5. Reza's certificate is on the release and the captain's is on the aircraft — if the two of you disagreed about which routing to fly, which number would you want the disagreement settled with, and who chose that number?

## Close

**VOTE AGAIN.** Then: *"Did we ask the right question at the start?"* and *"What math was new to
you tonight, and how did you actually attack it?"*

Compare the closing vote with Anchor 1's. A room that did not move at all after the amended
forecast is worth asking about directly: did the twist not land, or did the room already have the
right structure built in and simply recompute?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether D3 (the dot product) was genuinely where the room got stuck, versus D4's
  √(TAS² − crosswind²) closing step, which is arithmetically harder but conceptually simpler.
- Whether anyone caught that the fuel-flow figure cancels out of the comparison, and whether that
  realisation helped or derailed the discussion.
- Whether the twist produced real recomputation or only a change of mood.
- Whether "net progress" as a metric was understood or quietly replaced with "miles flown."

## Standards Touched On

Vector · Magnitude (Of A Vector) · Unit Vector · Dot Product · Pythagorean Theorem · Right Triangle ·
How to find the magnitude and direction of a vector · How to add and subtract vectors · How to find
the dot product of two vectors · How to convert an amount with compound units · How to find the
percent of a number

## Facilitator note — sensitivity

None required (SPEC §6). The stakes in this case are commercial and professional — a fuel bill and
a dispatcher's certificate. No personal loss, no family hardship. Both routings are legal and safe;
nothing in the case asks a learner to trade safety for money.

## Facilitator-only numbers

Every figure below resolves in `case.json.derived` and is regenerated by
`python3 cases/wind-triangle/sensitivity_model.py`. Do not retype a number here that is not in that
block — the continuity check exists to catch exactly that.

**Routing A — The Great Circle** (airway allowance +1.0%, filed 2,266.3 nm, great circle 2,243.9 nm)

| Leg | Filed nm | Course | Wind | Wind components (E, N) | Course unit vector | Along-course | Crosswind | Ground speed | Time | Fuel |
|---|---|---|---|---|---|---|---|---|---|---|
| KJFK→KDBQ | 774.8 | 283.5 | 300/78 | (+67.55, −39.0) | (−0.9724, +0.2333) | **−74.78** | 22.16 | 384.7 | 2.0141 | 10,683 |
| KDBQ→KSLC | 966.9 | 271.4 | 200/42 | (+14.36, +39.47) | (−0.9997, +0.0241) | **−13.41** | 39.8 | 444.9 | 2.1735 | 11,529 |
| KSLC→KSFO | 524.6 | 251.9 | 150/13 | (−6.5, +11.26) | (−0.9504, −0.3111) | **+2.68** | 12.72 | 462.5 | 1.1343 | 6,017 |

Totals: **5.3219 h**, **28,228.9 lb**, **12.592 lb per nm of net progress**.

**Routing B — The Southern Swing** (airway allowance +1.5%, filed 2,402.7 nm, great circle 2,367.2 nm)

| Leg | Filed nm | Course | Wind | Wind components (E, N) | Course unit vector | Along-course | Crosswind | Ground speed | Time | Fuel |
|---|---|---|---|---|---|---|---|---|---|---|
| KJFK→KSGF | 950.1 | 263.8 | 340/14 | (+4.79, −13.16) | (−0.9941, −0.1084) | **−3.33** | 13.6 | 456.5 | 2.0813 | 11,040 |
| KSGF→KABQ | 663.7 | 262.3 | 280/09 | (+8.86, −1.56) | (−0.9909, −0.1343) | **−8.57** | 2.74 | 451.4 | 1.4703 | 7,799 |
| KABQ→KSFO | 788.9 | 286.1 | 150/13 | (−6.5, +11.26) | (−0.9608, +0.2773) | **+9.37** | 9.01 | 469.3 | 1.6811 | 8,917 |

Totals: **5.2328 h**, **27,756.2 lb**, **12.381 lb per nm of net progress**.

**The verdict.** Routing B is cheaper by **472.8 lb**, `margin_pct` **1.67**, while flying
**136.4 nm** (6.0%) further. That is the whole case in one line: the longer way round is the
cheaper way round, under this wind field.

**The reserve check (D5).** Alternate KSFO→KLAX, 293.3 nm on 137.6°, against the KSFO wind: ground
speed 447.3 kt, 0.6557 h, **3,478 lb**. Forty-five minutes at cruise flow: **3,978 lb**. Minimum
dispatch fuel therefore **35,685 lb** on Routing A and **35,213 lb** on Routing B. Both are legal.
Nothing hinges on this — and Socratic question 4 exists to make the room notice that a check which
clears is not an argument.

**The break-even (D5).** Scale Routing A's along-course components by **0.7952** — that is, assume
the forecast headwind was **overstated by 20.5%**, or by a uniform **7.21 kt** on each leg — and the
two routings burn identical fuel. Above that error, Routing A wins. This number is Argument A, and
it is the most important number in the case: it converts "the forecast might be wrong" from a
feeling into a threshold.

**What the difference is worth.** 472.8 lb is **70.6 US gallons**, **$240.13** at July 2026 Gulf
Coast spot, and — at MA1's two departures a day — **345,127 lb** and **$175,293** a year. Useful for
the room that says "it's only four hundred pounds."

**The twist.** Routing B via KMEM: filed 2,467.0 nm, 5.3561 h, **28,410.4 lb**. Routing A becomes
cheaper by **181.4 lb**, margin **0.64%**.

**Probe 5 sweep.** Flexing all four stated numeric assumptions ±50%: Routing B stays cheaper
throughout, margin between **0.95%** and **2.40%**, no flips, no breach of the 20% cap.
