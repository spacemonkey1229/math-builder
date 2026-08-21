# Concept sheet — Pre-Calculus / Trigonometric Identities

**Target:** `Pre-Calculus / Trigonometric Identities` — 5/5 skills at `n == 0` (a total-hole group):
`pre-calculus-pythagorean-identity` (term), `pre-calculus-inverse-trigonometric-function` (term),
`pre-calculus-how-to-verify-a-trigonometric-identity` (how-to),
`pre-calculus-how-to-solve-a-trigonometric-equation-over-a-given-interval` (how-to),
`pre-calculus-how-to-evaluate-an-inverse-trigonometric-function` (how-to).

Group size is exactly 5, so the group-bonus formula's ceiling is:
`raw (3×1.0 how-to + 2×0.6 term = 4.2) + group_bonus (2.0) = 6.2`, before the availability
factor. Every concept below targets the full 5/5 close — undershooting it on purpose only makes
sense if the data genuinely won't support one of the five, which is called out per concept.

The sibling group `Pre-Calculus / Trigonometric Functions` (radians, unit circle, sine/cosine/
tangent, amplitude/period, reference angle — 11/11 skills already at `n == 1` via `tide-window`)
is **not** the target here. A concept that happens to also touch it (e.g. needing radians or a
reference angle along the way) is fine and adds thickness, but it does not drive the ranking.

---

## Ranking

| # | Concept | Score | Feasibility | Tier |
|---|---|---|---|---|
| C1 | Fire Monitor Nozzle Angle | **6.2** | HIGH | T4 |
| C2 | Two-Link Robot Arm Reach | 6.2 (nominal) | MEDIUM | T4 |
| C3 | Line-Array Null Angle | 6.2 (nominal) | LOW-MEDIUM | T4 |
| C4 | Solar Array Tilt Solve | 5.0 | MEDIUM | T3 |

**Recommendation: write C1, Fire Monitor Nozzle Angle.** It is the only concept where all five
target skills are forced by the physics itself, not bolted on, and where I can name the exact
category of real public source for every load-bearing number: manufacturer nozzle-reach charts
(Task Force Tips, Akron Brass, Elkhart Brass all publish PDF "stream performance" tables giving
GPM/nozzle pressure/reach), and the standard projectile-range formula, which is public-domain
physics, not proprietary. C2 (robot arm) scores identically on paper but the "verify a trig
identity" and "solve over an interval" deliverables have to be manufactured rather than forced —
a two-link arm's elbow-up/elbow-down ambiguity is inverse-kinematics, not identity-verification,
so I'd be stretching the mapping to claim it, which the skill's own "Never claim a skill the
concept does not genuinely force" rule flags. C3 (line array) is the most elegant match for the
Pythagorean/double-angle machinery but I cannot name a specific, checkable public source for
real venue interference geometry — it would collapse into mostly-assumed numbers. C4 (solar
tilt) is clean and well-sourced but only forces 4 of the 5 skills (no natural "verify an
identity" step), so it undershoots the target and would leave the group at 4/5, not 5/5.

**Killed:** C3, for the sourcing reason above — LOW-MEDIUM is an honest grade and I won't pretend
it's HIGH.

---

### C1 — Fire Monitor Nozzle Angle   ·   score 6.2   ·   tier T4
**Protagonist.** Danny Ruiz, apparatus operator (the firefighter who runs the truck's roof-mounted
deluge gun / master-stream monitor) for a mid-size municipal fire department. Personally at
stake: the crew inside the collapse zone is counting on him to land water on the seat of the
fire without anyone stepping past the collapsed parapet wall to do it.

**The dilemma.** A.) Set the monitor to the **Low Arc** — the flatter of the two elevation angles
that reach the target distance, verified against manufacturer reach data OR B.) Set the monitor
to the **High Arc** — the steeper complementary angle that reaches the identical distance but
clears the collapsed parapet with more clearance.

**Primary metric.** Gallons of water landing within the effective target radius per minute of
monitor operation (a ratio: rated flow, discounted by each trajectory's wind-drift and
hang-time loss, divided by minutes needed to knock down the fire).

**Why it's close.** The standard projectile range formula for a fixed launch speed and target
distance has (generically) *two* elevation-angle solutions that are complementary — this is a
direct algebraic consequence of the double-angle identity buried in the range equation, not a
coincidence, and it's the real reason master-stream operators are trained on both a "flat" and a
"lobbed" setting. The Low Arc gets more of its rated flow onto the target because it spends less
time in the air exposed to crosswind, but it can't clear the parapet at the operator's required
standoff distance. The High Arc clears the obstruction and lets the crew stand farther back, but
its longer hang time means more of the stream drifts off-target in even a light wind — so it
delivers a lower fraction of its rated GPM onto the actual fire. Neither arc is a free lunch;
which one wins on gallons-effectively-on-target depends on the wind on scene that day.

**Would close (5 skills, 3 how-to / 2 term):**
| id | kind | label |
|---|---|---|
| pre-calculus-pythagorean-identity | term | Pythagorean Identity |
| pre-calculus-inverse-trigonometric-function | term | Inverse Trigonometric Function |
| pre-calculus-how-to-verify-a-trigonometric-identity | how-to | How to verify a trigonometric identity |
| pre-calculus-how-to-solve-a-trigonometric-equation-over-a-given-interval | how-to | How to solve a trigonometric equation over a given interval |
| pre-calculus-how-to-evaluate-an-inverse-trigonometric-function | how-to | How to evaluate an inverse trigonometric function |

**Already-covered skills it also exercises.** Likely touches `pre-calculus-radian` /
`pre-calculus-how-to-convert-between-degrees-and-radians` and `pre-calculus-reference-angle`
along the way (all already at n=1 via `tide-window`) — bonus thickness, not scored.

**Data feasibility: HIGH.** Named sources I expect to exist:
- Task Force Tips (TFT) and Akron Brass both publish PDF "stream performance" / reach charts for
  their master-stream nozzle products, giving nozzle pressure, flow (GPM), and measured
  horizontal reach at stated elevation angles — this gives real muzzle-velocity-equivalent data.
- The projectile range formula itself (R = v²sin(2θ)/g, idealized, no drag) is standard public
  first-year-physics content, citable to any open physics reference (e.g. OpenStax
  University Physics), not proprietary — safe to cite generically.
- NFPA fire-stream hydraulics references (NFPA 1961/1962 or a fire-service hydraulics textbook)
  for standard nozzle operating pressures, if a specific pressure figure is needed.

Sources I am NOT confident about: real numeric wind-drift-loss-per-second-of-hang-time is
unlikely to have a clean citable figure — this will very likely become a stated Modeling
Assumption (grounded in the real, qualitative fact that lofted water streams lose more volume to
wind than flat ones, which is uncontroversial fire-service doctrine, but the exact percentage
will be assumed, not sourced). Real building/parapet clearance heights will also likely be a
constructed scenario figure, not a specific real address.

**Sensitivity (SPEC §6).** One-line facilitator flag: this case involves an active structure
fire and firefighter safety margins; frame stays on protection (getting water on the fire,
keeping the crew clear of the collapse zone) not on injury or casualty counting — consistent
with SPEC §6's preference for protection framing.

**Split risk.** NONE — 5 skills across a 2-3 hour T4 case is well inside the 8-15 honest range,
and the group is only 5 skills total so there's nothing left to split into a second case.

---

### C2 — Two-Link Robot Arm Reach   ·   score 6.2 (nominal, see kill note)   ·   tier T4
**Protagonist.** Priya Shah, controls engineer at a warehouse-automation startup, choosing the
inverse-kinematics solution branch for a pick-arm that must reach a bin without its elbow
swinging into a support post.

**The dilemma.** A.) Command the **elbow-up** joint-angle solution OR B.) Command the
**elbow-down** joint-angle solution — both place the gripper at the identical target point.

**Primary metric.** Seconds of cycle time per pick (elbow travel distance from home position,
converted to motor seconds) for each solution branch.

**Why it's close.** A 2-link planar arm reaching a fixed point generically has exactly two
joint-angle solutions (elbow-up / elbow-down), and choosing between them is a real, live
controls problem — whichever elbow is currently closer to the target point costs less travel
time, but the other solution may be the only one that clears a fixed obstacle.

**Would close (5 skills, 3 how-to / 2 term):** same five ids as C1.

**Already-covered skills it also exercises.** `advanced-operations-*` (systems/algebra),
possibly `geometry-pythagorean-theorem` if not already covered elsewhere.

**Data feasibility: MEDIUM.** Named sources I expect to exist: published robot-arm spec sheets
(link lengths, joint limits) from real manufacturers (e.g. UR, Kinova) are real and public.
Sources I am NOT confident about: a genuinely realistic obstacle geometry and target pick point
that forces a *close, defensible* choice — this would likely need to be constructed, which is
fine, but weakens the "real sourced data" feel more than C1.

**Sensitivity (SPEC §6).** NONE.

**Split risk.** NONE.

*(Kill note, expanded from the header table: the "verify a trig identity" and "solve a trig
equation over a given interval" deliverables don't fall out of inverse kinematics as directly as
they do from the ballistic range equation — I'd be authoring artificial deliverables to hit the
mapping rather than deliverables the arm problem actually forces. Flagging this now so
`case-write`'s LEARNING GOAL CHECK doesn't have to catch it later.)*

---

### C3 — Line-Array Null Angle   ·   score 6.2 (nominal, see kill note)   ·   tier T4
**Protagonist.** Marcus Webb, front-of-house sound engineer, choosing between two subwoofer
placement configurations for an outdoor venue to minimize a dead zone in the crowd.

**The dilemma.** A.) **Cardioid stack** — subs arranged with rear-firing delay cancellation OR
B.) **End-fire array** — subs arranged in a line with forward delay taps — both configurations
are tuned to cancel the same rear-facing null, but they place the *audience-facing* null angle
differently.

**Primary metric.** Square feet of usable listening area inside the target SPL band, per
configuration.

**Why it's close.** Two-source interference is governed by a sum-to-product identity
(constructive/destructive addition of two cosine waves), and solving for the angle(s) where the
sources cancel is literally "solve a trig equation over a given interval" — this is the
cleanest, most textbook-native match of any concept here for the Pythagorean/double-angle
machinery.

**Would close (5 skills, 3 how-to / 2 term):** same five ids as C1.

**Data feasibility: LOW-MEDIUM.** I can name the *physics* confidently (two-source interference
is standard acoustics, citable to any audio-engineering textbook or an AES paper on line
arrays), but I cannot name a specific, checkable real source for a real venue's actual sub
placement geometry, real crowd-area dimensions, or a real measured null pattern — this would
mean nearly every appendix number becomes a Modeling Assumption rather than a citation, which is
a worse ratio than C1.

**Sensitivity (SPEC §6).** NONE.

**Split risk.** NONE.

*(Kill note: killed for sourcing, not for math fit — see Recommendation above.)*

---

### C4 — Solar Array Tilt Solve   ·   score 5.0   ·   tier T3
**Protagonist.** Elena Cho, site engineer for a community solar cooperative, choosing a
fixed panel tilt angle for a new array.

**The dilemma.** A.) **Summer-optimized tilt** — angle set to maximize June-through-August
output OR B.) **Annual-optimized tilt** — angle set to maximize total yearly output, found by
solving the irradiance model over the year's angle range.

**Primary metric.** Kilowatt-hours generated per panel per year.

**Would close (4 skills, 2 how-to / 2 term):**
| id | kind | label |
|---|---|---|
| pre-calculus-inverse-trigonometric-function | term | Inverse Trigonometric Function |
| pre-calculus-how-to-solve-a-trigonometric-equation-over-a-given-interval | how-to | How to solve a trigonometric equation over a given interval |
| pre-calculus-how-to-evaluate-an-inverse-trigonometric-function | how-to | How to evaluate an inverse trigonometric function |
| pre-calculus-pythagorean-identity | term | Pythagorean Identity (weak — see note) |

**Data feasibility: MEDIUM.** NREL PVWatts and NOAA solar-position data are real, public, and
well documented.

**Sensitivity (SPEC §6).** NONE.

**Split risk.** Undershoots the group (4/5, no natural "verify a trig identity" deliverable) —
would leave the group at 4/5 closed, not 5/5. Scored lower for this reason and not
recommended unless C1 turns out to be infeasible in research.

---

## Recommendation (repeated for the handoff)

Write **C1 — Fire Monitor Nozzle Angle**. It is the only concept that forces all five target
skills honestly, closes the entire 5/5 `Trigonometric Identities` group in one case (full group
bonus), and names a specific, checkable category of real public source for its load-bearing
numbers (manufacturer nozzle-reach charts + the standard projectile range formula). C4 is the
fallback if C1's manufacturer reach-chart data turns out not to exist in research.

**Next step: Approve a concept, then run case-write on it.** (No human is available to approve
interactively for this run — proceeding directly to C1 per the task's standing instruction; see
the session's final report for this judgment call.)
