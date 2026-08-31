# FACILITATOR.md — The Crosswind Cut

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — case.md
carries no marker comment for this by design (see the "Balance argument" guidance in `case-write`
SKILL.md); the balance argument, margin, and sensitivity notes live only here and in `case.json`'s
`balance` object and `derived` block.*

**Case:** The Crosswind Cut · **Tier:** T2 (MS-core) · **Studio:** MS Launchpad
**Standards:** Vector, Magnitude (Of A Vector), Unit Vector, Dot Product, How to find the magnitude
and direction of a vector, How to add and subtract vectors, How to find the dot product of two
vectors, Variable, How to find the percent of a number (see `case.json.standards[]` for exact ids).

**Status:** Researched and computed 2026-08-30. All `{{NEEDS_SOURCE}}` tokens in `case.md` are
closed (`RESEARCH_LOG.md`). The D1–D5 arithmetic is done and recorded below and in
`case.json.derived`.

**Balance flag, read before you facilitate:** on the primary metric (net forward-progress thrust
per amp), **Configuration Sparrow (A) beats Configuration Albatross (B) by only 1.8%** — the
tightest margin in this batch, and still inside SPEC §2's ~20% cap. This is not a close call the
case manufactured for drama: it is a real crossover in T-Motor's own published throttle-sweep data
(see "The margin — COMPUTED" below). Run this case knowing that a Hero who works only from the
Appendix A "advertised calm-air thrust-per-amp" row will confidently pick the *wrong* configuration
— Albatross wins that row by ~11%. The whole pedagogical point is that the calm-air number and the
real-route number do not have to agree, and only the D1–D4 vector/dot-product chain tells you which
one governs.

## Intro

Frame the format before anything else: this is a real prelaunch sign-off with a hard operational
consequence, not a worksheet. Name the opener — "You are Jordan Reyes, flight-operations engineer
at Swiftwing Regional Logistics, standing over a checklist with one blank field: motor/prop config.
Drone 114 does not fly until you fill it in, and once ground crew bolts a configuration on, there is
no swapping mid-route." Let the stakes land — the FAA BVLOS waiver's lateral-boundary requirement
and the mandatory battery reserve are both hard constraints, not suggestions — before moving to the
Launch.

## Launch

Show Appendix A's two configurations side by side — Sparrow's higher RPM and higher current draw,
Albatross's lower RPM and lower current draw — with no efficiency arithmetic done yet. Ask: "Just
looking at the raw thrust and current numbers, which rig do you think wins, and on what?" Do not
confirm or correct answers here. Most rooms will jump to "Albatross, because the Background says it
produces more thrust per amp in calm air" — that instinct is worth recording out loud before anyone
touches the crosswind in Appendix B, because it is exactly the trap (see below).

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Configuration Sparrow — the rig that draws *more*
current and does not win the printed efficiency spec?" Show of hands, both options, no discussion.
Record the count — Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What does 'better' mean here?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which
configuration is more efficient," but push on what the flight actually needs: "The Background says
this route has a mandatory lateral boundary *and* a mandatory battery reserve — so is 'most
efficient in calm air' actually the question Jordan has to answer, or is there a step missing
before efficiency even means anything on this route?" If the room lands on "we need thrust that
actually points down the corridor, after the crosswind is paid for, per amp spent" on its own, the
case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "calm-air efficiency" from "net forward-progress efficiency," ask them to
name the actual steps before touching the appendices: find each configuration's total available
thrust and current at the route's throttle setting (D1, from Appendix A), build the
crosswind-cancellation vector diagram and subtract it from the total thrust vector (D2, from
Appendix B and Appendix D's MA1/MA2), take the dot product of what's left with the heading unit
vector to get net forward-progress thrust (D3), divide by current draw to compare the two
per-amp rankings (D4), then check both configurations against the mandatory battery reserve before
recommending (D5). Re-ask: "Is our question still the right one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gaps honestly: MA1 (crosswind speed), MA2 (crossing angle), MA3 (motor count),
MA4 (groundspeed), MA5 (route length), MA6 (battery capacity), and MA7 (reserve rule) are all
stated Modeling Assumptions, not sourced figures — no public spec exists for the fictional Drone
114 or Swiftwing. Ask which ones actually change the *graded* D4 ranking if they move. The honest
answer, which a sharp Hero can discover but should not be told outright yet, is: none of them do.
MA1/MA2/MA4 set the wind-correction angle identically for both configurations, so the cosine factor
they produce is common to both and cancels out of the *ranking* (see the margin-invariance finding
under the Twist, below) — it only changes the *magnitude* of both configurations' numbers. MA3
scales both configurations' thrust and current identically and also cancels out of the per-amp
ratio. MA5–MA7 only feed the separate D5 reserve check, not D3/D4 at all. What *does* decide the
ranking is Appendix A's real sourced throttle-sweep data — a figure no Modeling Assumption touches.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's two thrust-and-current totals, D2's two
crosswind-cancellation vectors, D3's two net forward-progress thrust figures, and D4's two rankings
together as a room, cold-calling for D4 specifically — this is where a Hero who correctly read
Albatross's advertised 264.9 g/A against Sparrow's 238.3 g/A but never carried the crosswind
subtraction through D2/D3 will visibly struggle to explain why Sparrow can still win on the metric
that actually matters. That struggle is useful information for the facilitator, not a moment to
rescue.

**Facilitator-only arithmetic note.** At the route's 90% throttle setting (4 motors, MA3): Sparrow
totals 11,128 g thrust and 82.4 A; Albatross totals 15,636 g thrust and 117.84 A (Appendix A, ×4).
The wind-correction angle from MA1 (15 mph crosswind) crossing MA2's 80° against MA4's 33.5 mph
groundspeed is θ = arcsin(15·sin80° / 33.5) ≈ 26.16°, so cos θ ≈ 0.8975 — identical for both
configurations. Net forward-progress thrust: Sparrow 11,128 × 0.8975 ≈ 9,987.5 g; Albatross
15,636 × 0.8975 ≈ 14,032.6 g. Net forward-progress thrust per amp: Sparrow 9,987.5 ÷ 82.4 ≈
121.21 g/A; Albatross 14,032.6 ÷ 117.84 ≈ 119.07 g/A. **Sparrow wins by (121.21 − 119.07) / 119.07
× 100 ≈ 1.8%.** Compare against the *advertised* calm-air row (238.3 g/A vs. 264.9 g/A, Albatross
ahead by ~11%) — the two rankings disagree, and that disagreement is the entire reason this case
exists. Full derivation and the runnable model in `cases/the-crosswind-cut/sensitivity_model.py`
and `case.json.derived`.

**Why the rankings disagree.** T-Motor's own published throttle sweep shows the two combos'
current-efficiency curves cross somewhere between roughly 70–80% throttle. Below that crossover,
Albatross really is the more efficient combo (which is what the 40%-throttle "advertised" row
captures). Above it — at the route's actual 90% throttle — Sparrow has become the more
current-efficient combo. A Hero only sees this if they build D1 and D4 from the real sourced
per-throttle numbers instead of trusting the single advertised spec-sheet figure.

**D5 does not overturn this.** At 33.5 mph over the 4 mi route (0.1194 hr of flight time), Sparrow
draws 9.84 Ah (55.3% of the 22 Ah pack remains — comfortably above the 25% mandatory reserve) and
Albatross draws 14.07 Ah (36.1% remains) — both configurations are legal to fly today; Albatross's
reserve margin is thinner but not violated.

## Twist — drop this at ~18 minutes into the discussion

Deliver slowly, with pauses:

"Dispatch pings again: today's crosswind reading is climbing. It's not at 15 mph anymore — it's
gusting, though still nowhere near the National Weather Service's Wind Advisory threshold. Does a
stronger crosswind change which configuration you'd recommend?"

Let the room work this — most will assume yes, because a stronger crosswind should punish the
configuration with the smaller surplus thrust harder. Then reveal the actual mechanism:

**Facilitator-only: what this actually does, and does not, change.** Re-run the D2/D3/D4 chain at,
say, 25 mph instead of 15 mph (same 80° crossing angle, same 33.5 mph groundspeed): the
wind-correction angle grows to θ ≈ 47.3° and cos θ drops to ≈ 0.678 — both configurations' net
forward-progress thrust numbers shrink substantially (Sparrow's per-amp figure falls from 121.21 to
about 91.6 g/A; Albatross's falls from 119.07 to about 90.0 g/A). **But the margin between them —
1.8% — does not move at all.** Cos θ is a single multiplicative factor common to both
configurations' net forward-progress thrust, and it cancels exactly out of the *ratio* that decides
the ranking (`case.json.balance.margin_basis`'s own algebra shows this: multiply both numerators
by the same constant and their percentage difference is unchanged). Walk a Hero through the algebra
directly if they don't spot it: the winner and the margin are decided entirely by Appendix A's
throttle-dependent efficiency crossover — the crosswind reading, however strong, cannot flip this
recommendation on its own.

**Where the twist actually bites.** The crab-angle correction the case is built on only has a
solution while the crosswind's cross-corridor component stays smaller than the groundspeed —
mechanically, `wind_speed × sin(crossing angle) ≤ groundspeed`. At MA2's 80° crossing angle and
MA4's 33.5 mph groundspeed, that ceiling is about 34 mph. The NWS Wind Advisory range named in
Appendix D's own sourcing (S3) is *sustained* 31–39 mph, with *gusts* to 46–57 mph — meaning a
genuine advisory-level gust would push this route past the point where a simple "cancel the
crosswind and fly the corridor" correction even has a mathematical answer. Ask: "So if the ranking
between Sparrow and Albatross can't be changed by wind speed, what real-world thing actually *would*
force Jordan to scrub the flight instead of just picking a configuration?" The honest answer the
case supports is an operational one, not a D3/D4 one: at high enough gusts, the corridor simply
cannot be flown safely inside the waiver's lateral boundary by either configuration, which is a
different failure mode than "the wrong configuration was bolted on."

## Immediate recommit

Re-vote immediately. Ask by name: "Did the stronger-gust news change your vote — or does it just
tell you that the crosswind was never the thing deciding this argument?" That distinction is the
transferable skill, not the vote itself.

## Deep conflict — three threads (20–30 min)

1. **A spec-sheet's headline efficiency number is not the number that governs a real route.**
   Albatross wins the advertised 40%-throttle thrust-per-amp figure by ~11%, yet loses the route's
   actual 90%-throttle comparison by not quite enough to change Jordan's decision. What does that
   gap tell you about trusting a single advertised number over building the full D1–D4 chain
   yourself?
2. **A shared factor cancels out of a ratio.** The wind-correction cosine multiplies both
   configurations' net forward-progress thrust by the same amount. Why does that guarantee the
   *ranking* is wind-speed-independent even while both raw numbers change a lot as the wind
   strengthens?
3. **1.8% is a real margin, not a rounding artifact.** It comes from a genuine crossover in
   T-Motor's own published data, not an engineered near-tie. Given how thin it is, would you want
   Jordan to treat this as a settled call, or as a decision worth re-checking every time the T-Motor
   combo data (not the weather) gets updated?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both configurations' raw thrust/current numbers side by side, cold-call for a gut read, no efficiency math yet |
| 3:00–10:00 | Position defense — *"Convince us your configuration actually wins on net forward-progress thrust per amp, not just the advertised spec"* |
| 10:00–18:00 | Pressure-test the models — *"Which of MA1–MA7 would have to change, and by how much, for your answer to flip?"* |
| **18:00** | **DROP THE TWIST** — the climbing crosswind reading, and whether it changes the recommendation |
| 18:00–23:00 | Immediate recommit — who reverses, and why |
| 23:00–33:00 | Threaded deep conflict (advertised spec vs. real-route number; why the wind cancels out of the ranking; how much confidence a 1.8% margin deserves) |
| 33:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

The plausible wrong answer is picking Configuration Albatross on the strength of Appendix A's
advertised calm-air thrust-per-amp row alone — "264.9 g/A beats 238.3 g/A, done" — without ever
building the crosswind-cancellation vector in D2 or taking the dot product in D3. That skips the
entire reason this case exists: the advertised figure describes calm air at 40% throttle, and
today's route flies at 90% throttle through a real crosswind, neither of which the advertised
number accounts for. The argument only becomes defensible once the Hero has built the crosswind
vector, subtracted the cancellation component, taken the dot product of what's left with the
heading, and divided by the real current draw at the *route's* throttle setting — which is exactly
the "why it's close" mechanism this case is designed around: calm-air efficiency and net
forward-progress efficiency are not guaranteed to rank the same way, and only the vector work
resolves which one actually wins.

## Socratic questions

1. Your D1 table gives Albatross more total thrust than Sparrow, and the advertised spec gives Albatross the better thrust-per-amp figure too — so why isn't Albatross the obvious winner?
2. Your D2 diagram builds a unit vector for the delivery heading and a separate vector for the crosswind. If the crossing angle in Appendix D's MA2 were much smaller — the wind crossing the corridor at a shallow, near-parallel angle instead of close to 90° — what would happen to the size of the corrective thrust vector each configuration has to supply?
3. D3's net forward-progress thrust is a dot product, not a plain subtraction of magnitudes. If a Hero computed it by just subtracting the crosswind's 15 mph from the total thrust's magnitude instead of projecting with a dot product, where exactly would that go wrong?
4. Your D4 table has two rankings in it — the manufacturer's advertised thrust-per-amp ranking and your own net-forward-progress-per-amp ranking. They disagree by only 1.8% on the number that actually matters. What does that tell you about when a spec sheet's headline number is the wrong number to trust?
5. D5 asks you to check both configurations against the mandatory 25% battery reserve. Even though Sparrow wins D4, could the reserve check in D5 have overturned Jordan's decision if Albatross had come out ahead on thrust-per-amp but failed the reserve rule instead?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that voted for
Sparrow at Anchor 1 purely on "it feels like the sportier rig" and stays with Sparrow after the
twist for a *different, vector-and-dot-product-based* reason has genuinely moved, even if the vote
count looks unchanged.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Anchor 4's "none of MA1–MA7 actually decides the ranking" finding landed as a discovery
  or had to be told outright.
- Whether the "advertised spec vs. real-route number" trap was the actual sticking point, or
  whether D2's crosswind-cancellation vector subtraction itself was the harder gate for most
  Heroes.
- Whether the Twist's "stronger wind doesn't flip it" reveal felt like a genuine insight or felt
  like the case dodging an intuitive answer — worth listening for directly, since this case's own
  balance note records a 1.8% margin (inside SPEC §2's cap, but the thinnest in this batch) that the
  Twist does not paper over.

## Standards Touched On

Vector · Magnitude (Of A Vector) · Unit Vector · Dot Product · How to find the magnitude and
direction of a vector · How to add and subtract vectors · How to find the dot product of two
vectors · Variable · How to find the percent of a number

## Facilitator note — sensitivity (SPEC §6)

None declared by the concept sheet — this is a routine engineering trade-off with no
contested or emotionally weighted subject matter (`case.json.sensitivity_note`). The load-bearing
*modeling-assumption* finding is recorded instead, which is a different (non-§6) kind of note: per
`case-write` SKILL.md §8, this states only the *direction* of the sensitivity, not its size, even
though the actual computed numbers are recorded above and in `case.json.derived` for facilitator
reference. MA1/MA2/MA4 (crosswind speed, crossing angle, groundspeed) set a cosine factor common to
both configurations, so they cannot flip the D4 ranking by themselves, only its magnitude; MA3
(motor count) cancels out of the per-amp ratio the same way; MA5–MA7 (route length, battery
capacity, reserve rule) feed only the separate D5 reserve check. The one dial that *can* flip the
ranking is not a Modeling Assumption at all — it is Appendix A's sourced throttle-sweep data itself,
specifically which side of T-Motor's ~70–80% throttle efficiency crossover the route's commanded
throttle setting falls on. See `cases/the-crosswind-cut/sensitivity_model.py` (Tier 2 Probe 5) for
the full assumption-flex sweep.
