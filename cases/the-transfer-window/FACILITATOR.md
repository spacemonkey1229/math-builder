# Guide Notes: The Transfer Window

**Case:** The Transfer Window · **Tier:** T2 · **Band:** MS-core · **Studio:** MS Adventure
**Standards:** Pre-Calculus/Polar And Parametric — `pre-calculus-parametric-equation`,
`pre-calculus-parameter`, `pre-calculus-how-to-eliminate-the-parameter-to-find-a-rectangular-
equation` (this case is the group's second touch beyond its single existing entry; none are
`new_coverage`), plus four heavily-covered supporting skills from Advanced Numbers/Percents,
Advanced Numbers/Decimals, and Measurement/Units. Exact ids in `case.json.standards[]`.

**Status:** researched at `case-research`, 2026-08-31; **retuned (unresolved) 2026-08-31**.
**margin_pct = 15,940.5 — Option A (The Direct Burn) wins by roughly two orders of magnitude, not
a close call.** ⚠️ **RETUNE ATTEMPTED, MARGIN STANDS — do not send to `case-qa` as a "close"
case.** Direct Burn's deliverable payload (17.0 kg over a derived 0.221-day transit) works out to
≈76.9 kg/day; Patient Drift's (86.3 kg over an assumed 180-day transit) works out to ≈0.479
kg/day. The payload advantage (~5x) never comes close to offsetting the ~800x transit-time
disadvantage.

A retune pass (`RESEARCH_LOG.md`, "RETUNE PASS — 2026-08-31") checked both routes this note
originally suggested and found neither works without fabricating a number: (1) **MA3 is not
unrealistically extreme** — 180 days for a full electric GEO orbit-raise sits squarely inside real
precedent (Boeing 702SP-class all-electric satellites, ~6-month transfers), re-confirmed against
fresh search; the ~800x transit-time gap is a real structural fact of chemical (newtons–
kilonewtons, minutes) vs. Hall-effect electric (millinewtons, months) thrust, not a modeling
choice. (2) **No alternative real metric closes the gap**: a cost-per-kg metric would need an
unsourced dollar figure for launch-cost savings or delayed-revenue cost; a pass/fail framing
against Appendix A's 240-day contract window never binds (180 days is comfortably inside it), so
it can't discriminate between the two options as a *primary* metric. Full detail and sources in
`RESEARCH_LOG.md`. No changes were made to `case.md`, `case.json`, or `FACILITATOR.md`'s substance
in that pass. **Recommendation:** treat this case's research as valid and complete but one-sided
(a legitimate, decisive real result, not a "close call" case), and — separately, as a fresh
`case-write` effort — author a new case under a new id, same protagonist/career/skill group, built
around two different real parking-orbit **phasing strategies** for a launch window (direct-ascent
vs. multi-orbit phasing, a real ~2–5x schedule spread rather than chemical-vs-electric's fixed
~800x). See `RESEARCH_LOG.md` for starting sources.

## Balance argument

**Argument for A (The Direct Burn).** A high-thrust chemical burn reaches the target
geostationary orbit radius in a small fraction of the time a low-thrust electric transfer needs —
and the payload customer's contract fixes a hard maximum delivery window (Appendix A). If the
Patient Drift's modeled transit time comes anywhere close to that ceiling, the Direct Burn is the
only option that comfortably clears it, and clearing the contracted delivery window is not
optional the way a marginal payload-mass gain is. Speed converts directly into contract compliance
and customer trust in a way the raw kg/day metric does not fully capture on its own.

**Argument for B (The Patient Drift).** Electric propulsion's much higher specific impulse means a
far smaller propellant mass fraction is needed for the same delta-v budget (Appendix B, C) — so a
larger share of the kick stage's fixed total wet mass survives as deliverable payload. The case's
actual primary metric is not raw payload mass and not raw speed alone, but kilograms of payload
per day of transit — and because that is a ratio, not a race, a trajectory that delivers
meaningfully more payload can still win on kg/day even while taking longer, provided the payload
gain outpaces the added transit days by enough. Whether it actually does is exactly what D4
computes.

**The margin.** For each option, deliverable payload mass (wet mass minus dry mass minus
propellant mass) divided by that option's transit time in days, compared as kg/day. Computed:
Direct Burn ≈76.9 kg/day (17.0 kg / 0.221 days) vs. Patient Drift ≈0.479 kg/day (86.3 kg / 180
days) — **the Direct Burn wins by ≈15,940%,** not a close call. `case.json` records the full
method and every input as `balance.margin_basis`. NASA JPL's Trajectory Browser/Horizons does not
actually apply to an Earth parking-orbit-to-GEO transfer (it models interplanetary trajectories);
the Direct Burn's orbital elements are instead derived directly from real orbital radii and
Earth's real gravitational parameter via the standard Hohmann-transfer equations — see
`RESEARCH_LOG.md` for the full trail, including why this margin is flagged for a possible retune
rather than treated as case-ready.

**The second, non-numeric constraint.** Appendix D's radiation-dose comparison against Appendix
A's tolerance limit is a pass/fail gate, not part of the margin itself. It is possible for an
option to win on kg/day and still be disqualified outright if its cumulative dose exceeds the
payload's rated tolerance — facilitators should watch for students who compute D4 correctly but
never check D5 against Appendix A's limit.

## Socratic questions

1. Your D4 table gives a kilograms-per-day figure for each option. Which one is larger, and by
   roughly how much — does that margin survive if the slower option's transit time turned out to
   be a few days longer than Appendix B's modeled figure?
2. Appendix A states a maximum acceptable delivery window. Does either option's D2 transit-time
   check come close to that ceiling — and if the Patient Drift's transit time crossed it, would
   the kg/day metric even matter anymore?
3. In D2 you solved for the point where each trajectory's rectangular equation crosses the target
   orbit radius. What would it mean, physically, if that solved point did not actually match
   Appendix A's stated target orbit radius — what part of Appendix B would you go back and
   question first?
4. Appendix D compares each option's cumulative radiation dose against a stated tolerance limit.
   Suppose the Direct Burn wins D4 comfortably but its D5 dose estimate is close to that limit —
   does a close-but-passing dose estimate change how confidently you'd defend the Direct Burn, or
   is a pass a pass?
5. If the named kick stage's actual published specific impulse for its electric mode turned out to
   be meaningfully lower than Appendix B states, which of your D3 and D4 results would change
   first, and would that plausibly flip your D6 recommendation?

## The trap

The trap is treating "faster" and "better" as the same claim. A Hero who fixates on the Direct
Burn's shorter transit time and stops there has answered a question the case never actually asked
— the primary metric is kilograms of payload *per day*, a ratio, not a race to be first. A Direct
Burn that arrives quickly but hands over noticeably less payload mass (because a larger share of
launch mass went to propellant) can lose on kg/day to a slower option that protects more payload,
even though "the Direct Burn got there first" remains true and is the more intuitively persuasive
sentence to say out loud. The reverse trap also exists: a Hero who fixates on the Patient Drift's
payload-mass advantage and never checks its transit time against Appendix A's contracted delivery
window, or its Appendix D radiation dose against the tolerance limit, may recommend an option that
is not actually flyable under the contract's own constraints. Both traps come from computing one
part of the picture (speed, or payload mass) and treating it as the whole answer.

## Sensitivity note

None required. Per SPEC §6, this case carries no illness, death, financial-hardship, or other
protected-subject stakes — it is a routine mission-design and contract-delivery trade-off between
two legitimate, professionally defensible trajectory choices, comparable in register to Wind
Triangle or Navigation. No facilitator content warning is needed.

## Cohort bands (SPEC §7.4 — minimum specification, drafted at write time)

| Band | Typical size | What changes |
|---|---|---|
| **Full** | the size this T2 case is authored for (a full MS-core class section) | the Socratic plan below runs as written; both stand/sit votes are taken as a group |
| **Compressed** | roughly half | Anchors 2–3 combine into one pass; the deep-conflict thread (speed vs. payload-per-day) runs as a single thread instead of two; total runtime shortens proportionally |
| **1:1 / pair** | 1–2 learners | no vote to take — Anchor 1 becomes a stated initial position instead of a stand/sit count; the guide plays devil's advocate directly rather than cold-calling; Socratic question 2 (the delivery-window ceiling) still lands but is asked directly rather than opened to the room |

## Guide Notes — anchor ladder

**Intro.** Frame the format: this is a real trajectory sign-off, not a worksheet. Name the
opener: *"You're the analyst. Whichever design you recommend becomes the number written into the
customer's contract. There's no 'we'll see' — you sign one."*

**Launch.** Show the two trajectory plots side by side (illustrative shapes, not the case's real
numbers) — one steep and fast, one long and gradual — with no other context. Ask: *"If all you
knew was which one gets there first, which would you pick, right now?"* Take the answers without
correcting anyone.

**Anchor 1 — Take a stand and vote.** *"Is anyone courageous enough to stand with the slower
trajectory?"* Stand-or-sit, no reasoning yet. Record the count; the Close re-asks it.

**Anchor 2 — What is the problem we're solving?** *"Is 'gets there first' the right question?"
"What do you mean by 'more payload'?"* Push on: *"Is a kilogram delivered today worth the same as
a kilogram delivered three weeks from now?"* Let the room sit with that discomfort — a room that
leaves Anchor 2 still arguing about what the metric should even measure is exactly where it
should be.

**Anchor 3 — What is the process?** Make the room name the steps before opening an appendix:
(1) write each trajectory's position as a function of a parameter, (2) eliminate that parameter to
get an equation you can actually check against the target orbit, (3) verify each trajectory really
reaches the target radius, (4) work out how much propellant each option burns and how much payload
survives, (5) divide payload by transit time for each option, (6) check the radiation dose against
the tolerance limit. Re-ask: *"Now that we can see the steps, is our question still the right
one?"*

**Anchor 4 — What don't we know?** Surface the honest gaps once `case-research` fills Appendix E:
most likely, Meridian Launch Systems' own contract delivery-window and radiation-tolerance limits
in Appendix A cannot be sourced for a fictional company and mission, and will be stated, disclosed
assumptions anchored to a real comparable mission's own published requirements. Ask: *"Is that
assumption critical to who wins — or does it wash out?"*

**Data Deep Dive.** Now, and only now, open Appendices A–D and work D1–D6.

**Twist.** N/A at draft time — no twist is authored yet. A strong candidate for `case-research` or
a later pass to consider: a real published finding that a payload's radiation-tolerance rating can
be exceeded well before its stated maximum-dose limit if a solar event occurs during the transit
window, which would cut against the Patient Drift's payload-mass advantage without changing either
option's physical trajectory. This is left `N/A` here because it depends on real space-weather
data not yet sourced; it should not be invented as a stated fact without a real basis.

**Close.** VOTE AGAIN: *"Did we ask the right question?"* Ask what math was new to each Hero, and
specifically whether eliminating the parameter in D2 tripped anyone up.

**Lessons Learned.** The recurring lesson this case is built to teach: the option that "wins" on
the most intuitively persuasive single number (speed, or raw payload mass) is not automatically
the option that wins on the actual metric being asked about — a ratio can flip the comparison that
either number alone would suggest, and the only way to know is to compute the ratio, not to trust
which raw number sounds more impressive.

**Standards Touched On.** Parametric Equation; Parameter; Percent; How to eliminate the parameter
to find a rectangular equation; How to find the percent of a number; How to divide decimal
numbers; How to convert an amount with compound units.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, the two trajectory plots, stand/sit vote — no explanation |
| 3:00–10:00 | Position defense: *"Convince us why your kg/day number is the one that matters, not just who gets there first"* |
| 10:00–15:00 | Pressure-test: *"Whose recommendation is most fragile if the transit-time or propellant figures came in different from Appendix B?"* |
| **15:00** | **DROP the space-weather/radiation twist**, if authored in a later pass (see Twist, above); otherwise substitute Socratic question 4 (a close-but-passing dose estimate) as the pressure point |
| 15:00–20:00 | Immediate recommit: who reverses, and why? |
| 20:00–30:00 | Threaded deep conflict: speed-as-contract-compliance vs. payload-per-day optimization (one thread at Full band; the same single thread at Compressed) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |
