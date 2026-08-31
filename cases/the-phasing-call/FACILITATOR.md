# Guide Notes: The Phasing Call

**Case:** The Phasing Call · **Tier:** T2 · **Band:** MS-core · **Studio:** MS Adventure
**Standards:** Pre-Calculus/Polar And Parametric — `pre-calculus-polar-coordinate`,
`pre-calculus-parametric-equation`, `pre-calculus-parameter`,
`pre-calculus-how-to-convert-a-point-between-rectangular-and-polar-coordinates`,
`pre-calculus-how-to-graph-a-polar-equation`,
`pre-calculus-how-to-eliminate-the-parameter-to-find-a-rectangular-equation` (the full group; this
case is a second/third touch beyond `Feedback`'s and `the-search-box`'s own coverage — none are
`new_coverage`), plus three heavily-covered supporting skills from Advanced Numbers/Percents and
Measurement/Units. Exact ids in `case.json.standards[]`.

**Status:** written at `case-write`, 2026-08-31. **Not yet researched — `margin_pct` is `null`.**
This is the direct replacement for `the-transfer-window`, which failed `case-qa`'s balance test by
roughly two orders of magnitude (chemical vs. full-electric propulsion, a fixed ~800x transit-time
asymmetry — see `cases/the-transfer-window/RESEARCH_LOG.md`'s RETUNE PASS). The deciding physical
asymmetry here is different in kind, not just degree: both rendezvous profiles fly the **same**
vehicle and the **same** propulsion system, and real crewed/cargo rendezvous precedent (Murtazin &
Budylov 2010; NASA's operational Soyuz timelines; Northrop Grumman's Cygnus) puts the two
profiles' raw transit times on the same order of magnitude — hours vs. days, not hours vs. months.
That is the whole basis for this case's honest expectation that `case-research` can land a margin
inside SPEC §2's ~20% cap; it is not yet confirmed.

## Balance argument (drafted pre-research — both arguments and the margin basis, not the number)

**Argument for A (The Fast-Track).** Reaching the station in a small number of orbits leaves the
largest possible share of the vehicle's fixed autonomous-flight/consumables allowance untouched at
docking (Appendix C) — real operational precedent (the modern 4-orbit/~6-hour and 2-orbit/~3-hour
Soyuz profiles) shows this is the profile actually flown today whenever the launch conditions
allow it, precisely because it preserves the largest contingency reserve for a failed first
approach or a docking hold-off. A larger reserve at docking is a direct, quantifiable safety and
schedule-resilience margin, not a soft preference.

**Argument for B (The Phasing Climb).** Tolerating a much wider range of initial phase angle means
far more days on the calendar are workable launch attempts (Appendix D) — real orbital-mechanics
precedent documents phasing-orbit rendezvous durations spanning roughly one to five days depending
on how far off the phase angle starts, precisely because the vehicle can simply fly more or fewer
phasing orbits to absorb the mismatch. A launch provider that can launch on far more of its
scheduled days avoids the real, recurring cost of a scrubbed or slipped launch attempt (weather
holds, range conflicts, technical delays) — schedule reliability is not free, and the Fast-Track's
narrow phase-angle tolerance makes every one of those real-world disruptions more likely to force
an expensive full recycle.

**The margin — basis, not yet computed.** Primary metric: hours of autonomous-flight/consumables
reserve remaining at docking (D4), divided by the number of days per 30-day launch calendar that
fall inside that profile's workable phase-angle tolerance band (D6) — hours of reserve per
calendar day of launch-window flexibility, for each profile, compared as a ratio (D7). This is
deliberately a ratio of two real, independently-sourced quantities (a consumables/reserve figure
and a phase-angle-tolerance figure), not a single total — the same structural move that failed for
`the-transfer-window` (a straight kg/day ratio dominated entirely by an ~800x transit-time term)
is not expected to recur here because neither term in this case's ratio is itself an
order-of-magnitude outlier: real sources put both profiles' *reserve-at-docking* and
*phase-angle-tolerance* figures within a roughly 2–5x band of each other, not a several-hundred-x
one. `case.json.balance.margin_pct` is `null` pending `case-research`; do not treat this
expectation as a finding.

**The second, non-numeric constraint.** Appendix A's minimum required reserve at docking (MA3) is
a pass/fail gate, not part of the margin itself — an option that wins D7's ratio but fails to
clear that minimum reserve is disqualified outright. Facilitators should watch for Heroes who
compute D7 correctly but never check D4 against Appendix A's stated minimum.

## Socratic questions

1. Your D7 table gives an hours-of-reserve-per-calendar-day figure for each profile. Which one is
   larger, and by roughly how much — does that margin survive if the Fast-Track's phase-angle
   tolerance band turned out to be even narrower than Appendix D states?
2. Appendix A states a minimum required reserve remaining at docking. Does either profile's D4
   result come close to that floor — and if the Fast-Track's reserve fell below it, would D7's
   ratio even matter anymore?
3. In D3 you solved for the elapsed time at which each profile's rectangular equation reaches the
   station's D1 position. What would it mean, physically, if that solved time did not match
   Appendix B's stated modeled transit time — what part of Appendix B would you go back and
   question first?
4. Appendix D compares each profile's phase-angle tolerance band against the full 0°–360° range a
   launch could face on a given day. Suppose the Phasing Climb wins D7 comfortably but its D6
   launch-window count is barely above the Fast-Track's — does a narrow win in calendar flexibility
   change how confidently you'd defend the Phasing Climb, or is a win a win?
5. If the named vehicle's actual published autonomous-flight/consumables allowance (Appendix C)
   turned out to be meaningfully shorter than this case states, which of your D4 and D7 results
   would change first, and would that plausibly flip your D8 recommendation?

## The trap

The trap is treating "gets there first" and "leaves the most reserve" as automatically the safer
choice, full stop — and separately, treating "opens the most launch days" as automatically the
better business choice, full stop. The Fast-Track's large reserve at docking is real and
valuable, but it is not free: it exists only on the narrow set of days its phase-angle tolerance
allows, and a Hero who never checks D6 against a real launch calendar may be defending a profile
that, in practice, gets scrubbed and re-attempted so often that its reserve advantage rarely gets
used the way the case's clean D4 number suggests. The reverse trap: a Hero who fixates on the
Phasing Climb's wide launch-window flexibility and never checks D4 against Appendix A's minimum
required reserve may recommend a profile that is not actually flyable under the contract's own
safety floor. Both traps come from computing one part of the picture (reserve, or flexibility) and
treating it as the whole answer — the case's actual primary metric is the ratio of the two.

## Sensitivity note

None required. Per SPEC §6, this case carries no illness, death, financial-hardship, or other
protected-subject stakes — it is a routine mission-design and launch-scheduling trade-off between
two legitimate, professionally defensible rendezvous strategies, comparable in register to Wind
Triangle, Navigation, or the superseded Transfer Window.

## Cohort bands (SPEC §7.4 — minimum specification, drafted at write time)

| Band | Typical size | What changes |
|---|---|---|
| **Full** | the size this T2 case is authored for (a full MS-core class section) | the Socratic plan below runs as written; both stand/sit votes are taken as a group |
| **Compressed** | roughly half | Anchors 2–3 combine into one pass; the deep-conflict thread (reserve vs. flexibility) runs as a single thread instead of two; total runtime shortens proportionally |
| **1:1 / pair** | 1–2 learners | no vote to take — Anchor 1 becomes a stated initial position instead of a stand/sit count; the guide plays devil's advocate directly rather than cold-calling; Socratic question 2 (the reserve floor) still lands but is asked directly rather than opened to the room |

## Guide Notes — anchor ladder

**Intro.** Frame the format: this is a real trajectory sign-off, not a worksheet. Name the
opener: *"You're the analyst. Whichever profile you recommend becomes the number written into the
flight plan. There's no 'we'll see' — you sign one."*

**Launch.** Show the two rendezvous profiles side by side (illustrative shapes, not the case's
real numbers) — one short and steep, one long and gradual — with no other context. Ask: *"If all
you knew was which one gets there first, which would you pick, right now?"* Take the answers
without correcting anyone.

**Anchor 1 — Take a stand and vote.** *"Is anyone courageous enough to stand with the slower
profile?"* Stand-or-sit, no reasoning yet. Record the count; the Close re-asks it.

**Anchor 2 — What is the problem we're solving?** *"Is 'gets there first' the right question?"
"What do you mean by 'more reserve'?"* Push on: *"Is a launch you can attempt on more days worth
more than a launch that leaves you more fuel and oxygen once you're finally there?"* Let the room
sit with that discomfort — a room that leaves Anchor 2 still arguing about what the metric should
even measure is exactly where it should be.

**Anchor 3 — What is the process?** Make the room name the steps before opening an appendix:
(1) convert the station's tracked position from polar to rectangular, (2) write each profile's
closing position as a function of a parameter, (3) eliminate that parameter to get an equation you
can actually check against the station's position, (4) verify each profile really reaches the
station when it says it does, (5) work out what percent of the reserve each profile burns getting
there, (6) graph and compare each profile's phase-angle tolerance band, (7) count workable launch
days per calendar, (8) divide reserve by flexibility for each profile. Re-ask: *"Now that we can
see the steps, is our question still the right one?"*

**Anchor 4 — What don't we know?** Surface the honest gaps once `case-research` fills the
`{{NEEDS_SOURCE}}` placeholders: most likely, Meridian Launch Systems' own contract deadline and
minimum-reserve figures in Appendix A cannot be sourced for a fictional company and mission, and
will be stated, disclosed assumptions anchored to a real comparable mission's own published
requirements — same pattern as `the-transfer-window`'s MA1. Ask: *"Is that assumption critical to
who wins — or does it wash out?"*

**Data Deep Dive.** Now, and only now, open Appendices A–D and work D1–D7.

**Twist.** N/A at draft time — no twist is authored yet. A strong candidate for `case-research` or
a later pass to consider: a real documented case of a launch scrub or delay that forced a planned
Fast-Track mission to fall back to a Phasing-Climb-style profile instead (this has real precedent
in crewed spaceflight history), which would let the room see the Fast-Track's "narrow window" risk
actually materialize rather than stay hypothetical. Left `N/A` here because it depends on a real,
specific documented incident not yet sourced; it should not be invented as a stated fact without a
real basis.

**Close.** VOTE AGAIN: *"Did we ask the right question?"* Ask what math was new to each Hero, and
specifically whether eliminating the parameter in D3, or graphing the polar boundary in D5,
tripped anyone up.

**Lessons Learned.** The recurring lesson this case is built to teach: the option that "wins" on
the most intuitively persuasive single number (arrives soonest, or opens the most calendar days)
is not automatically the option that wins on the actual metric being asked about — a ratio of two
real, competing constraints can flip the comparison that either raw number alone would suggest,
and the only way to know is to compute the ratio, not to trust which raw number sounds more
impressive.

**Standards Touched On.** Polar Coordinate; Parametric Equation; Parameter; Percent; How to
convert a point between rectangular and polar coordinates; How to graph a polar equation; How to
eliminate the parameter to find a rectangular equation; How to find the percent of a number; How
to convert an amount with compound units.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, the two rendezvous-profile plots, stand/sit vote — no explanation |
| 3:00–10:00 | Position defense: *"Convince us why your reserve-per-calendar-day number is the one that matters, not just who gets there first"* |
| 10:00–15:00 | Pressure-test: *"Whose recommendation is most fragile if the transit-time or phase-angle-tolerance figures came in different from Appendix B/D?"* |
| **15:00** | **DROP a scrub/delay twist**, if authored in a later pass (see Twist, above); otherwise substitute Socratic question 4 (a narrow win in launch-window count) as the pressure point |
| 15:00–20:00 | Immediate recommit: who reverses, and why? |
| 20:00–30:00 | Threaded deep conflict: reserve-as-safety-margin vs. flexibility-as-schedule-resilience (one thread at Full band; the same single thread at Compressed) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |
