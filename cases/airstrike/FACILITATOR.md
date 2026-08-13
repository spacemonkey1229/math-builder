# Guide Notes: Airstrike

**Case:** Airstrike · **Tier:** T3 · **Band:** MS-stretch/HS-entry · **Studio:** Heroes Academy
**Standards:** see `case.json.standards[]` for the exact ids (26 skills — coordinate geometry,
distance/rate/time, percent and decimal arithmetic, single-event probability, comparison)

Legacy conversion, 2026-08-13, built from the original case study docx
(`source/Y1/Session 6/Airstrike/Case Study_ Airstrike.docx`) and its Guide Notes onto the current
11-anchor ladder. The 15-site coordinate map is real data lifted directly from an image embedded in
the source docx (see `case.json.legacy_conversion_note`); the F-16, ICBM-analog and SRBM-analog
hardware specs are fact-checked against real public sources (Appendix E). The protagonist was
renamed from the legacy source's real, named former CENTCOM commander to a fictional general — see
`case.json.legacy_conversion_note` for why. Per SPEC.md §6, this conversion reframes the primary
metric from "casualties from missiles that get through" to "population protected" — same math,
protection framing.

## Intro

Frame the format: this is a real routing-and-time problem wearing a high-stakes scenario, not a
worksheet. Name the opener — "Two jets. Twelve minutes. Fifteen live targets. You don't get to fly
both plans." Flag the subject matter once, plainly, and move on: this case is about protecting
people, not about optimizing a body count — say that directly if the room needs it named.

## Launch

Read the Overview aloud, cold open, no numbers from Appendix A yet. Ask: "Four minutes to read two
folders and commit to one. What's your gut telling you before you've seen a single number?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who chooses Grey Dawn — ICBM sites first, no matter what? Who chooses Desert Sparrow — hit
whatever's closest, no priority?" Show of hands, record the count. Close will ask them to vote
again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do we need to consider in order to decide?"**

Push on what "better" means here: is it the most total people protected, or protecting the people
an ICBM strike could reach (anyone in the continental United States) over the people an SRBM strike
could reach (regional allies and nearby U.S. bases)? Those are two different optimization targets
that don't have to agree — let the room sit with that before naming a metric.

## Anchor 3 — What is the process?

**"Do we consider all of these factors, focus on 2-3, or focus on only one? Which one(s)?"**

Once the room has picked its deciding factor(s), ask them to name the actual steps: plot every site
(Appendix A), compute distance for every leg of every jet's route (Appendix A + C), convert that
distance to flight time (Appendix C's speed), decide which sites each operation reaches inside 12
minutes, then total the population protected (Appendix B, with Appendix D's SRBM discount). Re-ask:
"Do we agree that's the right process for the factor we picked?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix D's two real conventions: the SRBM intercept rate (5.6%) and the
population-per-warhead-class table are both stated scenario numbers, not sourced data — unlike the
hardware specs in Appendix C, which are real and cited. Ask which one actually moves the final
recommendation more if a Hero challenges it. **Corrected 2026-08-13 after a real Tier 2 P5
assumption-flex run:** it is the population table (MA3), not the intercept rate (MA2) — a ±50% flex
on a single warhead class's population figure can flip the winner or blow past SPEC.md §2's 20%
balance cap, while the intercept rate barely moves the margin at all. See `sensitivity_model.py`'s
`FLEX` and the twist soundness check below.

## Data Deep Dive

Now, and only now, the numbers. Walk one full route together as a room — Camp Dragonbreath to the
nearest ICBM site to the next-nearest site — cold-calling for the distance formula on the first leg
specifically. This is where a Hero who mixes up which coordinate is x and which is y, or forgets to
subtract the 2 km firing standoff before converting to time, gets a visibly wrong flight-time
number instead of the real one.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Sir — we can get one more F-16 off the ground. Three total. It'll be airborne two minutes after the
first two."

**Facilitator-only.** A third jet sounds like it should help both operations equally, or help
Desert Sparrow more (it already destroys more sites per jet). It doesn't. Recompute with 3 jets and
a 10-minute window for the new jet: **Grey Dawn now finishes all 9 ICBM sites** (it only had one
left, ICBM-Golf, sitting exactly in range for the extra jet) **plus 3 SRBM sites** — 12 of 15 total,
protecting 6,247,319. Desert Sparrow reaches 13 of 15, protecting 6,561,439. The margin **narrows
from 13.6% to 5.0%**, without flipping which option wins.

Here's the real mechanism worth naming out loud: Grey Dawn's "wasted" capacity — the fact that it
was already 8/9 done with ICBM sites and had nowhere efficient left to send jet capacity — turns out
to be exactly what the third jet is good for. Desert Sparrow's extra jet has to work harder for the
same gain, because its easy, close targets are already gone. Ask: "Which operation had more to gain
from a third jet, and why didn't you see that coming from the first two jets' numbers alone?"

## Immediate recommit

Re-vote immediately. Ask by name: "Did the third jet change your recommendation, or just make you
more confident in it?"

## Deep conflict — three threads (20-30 min)

1. **Total protected vs. threat class protected.** Desert Sparrow protects more total people
   (13.6% more with 2 jets); Grey Dawn protects nearly the entire population an ICBM strike could
   reach. Is "more total people" the right metric, or does a threat that can reach any U.S. city
   deserve to be weighted higher than a threat that can't?
2. **Appendix B's population-per-warhead-class table.** It's a stated scenario convention with no
   real per-city source. Ask: "If the 5.2 MT figure were half what Appendix B states, does your
   recommendation change?" (It does — a real Tier 2 run found this single number can flip the
   winner. This table, not the 5.6% intercept rate, is the case's most sensitive assumption — see
   `sensitivity_model.py`'s `FLEX`.)
3. **What the third jet reveals.** Route capacity isn't linear — the jet that seems "idle" after
   finishing its priority targets first is actually positioned to benefit most from reinforcement.
   Where else does that logic apply outside this case?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — read the Overview aloud, cold-call for a gut read, no site data yet |
| 3:00–10:00 | Position defense — *"Convince us your operation protects the people who matter most, not just the most people"* |
| 10:00–15:00 | Pressure-test the models — *"Which single number is actually deciding your vote?"* |
| **15:00** | **DROP THE TWIST** — the third F-16, delivered slowly |
| 15:00–20:00 | Immediate recommit — did the third jet change anyone's answer |
| 20:00–30:00 | Threaded deep conflict (total vs. threat-class protection; the intercept-rate assumption; what the third jet reveals about "wasted" capacity) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Corrected 2026-08-13 (real Tier 2 P3 run): the trap below is what a fresh solver actually falls into
— a computational one, not a values disagreement. (The values question — total population vs.
threat-class weighting — is real and worth running, but it lives in Deep conflict thread 1 below; it
is not what catches most Heroes on the arithmetic itself.)

Most Heroes will assume that once an F-16 destroys a site, its full, undiscounted population-at-risk
figure (Appendix B) counts as protected. That is wrong for SRBM sites specifically: Appendix D's MA4
says the SRBM intercept discount is already baked into every SRBM site's population-at-risk figure —
whether that site is destroyed by a jet or left standing when the window closes — because even an
undestroyed SRBM missile only has a 94.4% chance of reaching its target. A Hero who forgets this and
gives full credit for every destroyed SRBM site will still pick Desert Sparrow (it destroys more SRBM
sites either way, so the recommendation happens to land right), but will report a margin of 15.2%
instead of the real 13.6%, and every D4/D5/D6 total involving a destroyed SRBM site is quietly wrong.
This is the trap most likely to catch the room: the right recommendation, reached with arithmetic
that does not actually hold up if anyone checks it leg by leg. Watch for it specifically at D4→D6,
where "destroyed = fully protected, no discount" is the intuitive (and wrong) shortcut. See
`case.json.derived.p3_trap_wrong_margin_pct` and `sensitivity_model.py`'s `_pop_value`, which applies
`discount_srbm=True` to every SRBM site regardless of whether it was destroyed.

## Socratic questions

1. Desert Sparrow protects a real, computed 13.6% more total people than Grey Dawn — walk us through how you'd explain to General Reyes why that gap is or isn't decisive on its own.
2. Grey Dawn leaves only 1 ICBM site live; Desert Sparrow leaves 2. An ICBM site can reach any city in the continental United States and can't be intercepted. Does that asymmetry change how you'd weigh a percentage-point gap in *total* population protected?
3. Appendix B's population-per-warhead-class table is a stated assumption, not sourced data — and a real sensitivity check found it's the single number most likely to flip your recommendation. Using the "how to…" resource you researched, defend why your own version of that table is reasonable.
4. The third F-16 narrows the margin from 13.6% to 5.0% without changing which operation wins. What does that tell you about which operation had more "room to improve" before the twist, and could you have predicted that from the first two jets' routes alone?
5. If you had to defend your operation to the families of the people it does *not* protect — not the people it does — what would you say, using only the numbers from Appendix B and D4?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight, and
how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that already
treated "total population protected" as the deciding metric from the first vote is worth asking
directly: did anyone actually consider threat-class weighting, or did the room converge on the
easier-to-compute total from the start?

## Lessons Learned

- How would you rank this case in terms of difficulty, 5 being the hardest one done yet?
- What was challenging about the case study — the coordinate geometry, the rate/time conversions,
  or weighing two real, computed metrics that disagree?
- What math concepts were new to you, and how did you take on that challenge — google, ask a fellow
  traveler, or something else?
- If given a similar case next time, what would you do differently?

## Standards Touched On

See `case.json.standards[]` (26 ids) and `case.md` Appendix F for the verbatim spine labels this
case exercises — coordinate-plane geometry and the distance formula, compound-unit rate-to-time
conversion, percent/decimal arithmetic, single-event probability, and multi-metric comparison.

## Twist soundness check (SPEC.md §6, sequential and simultaneous reading)

Checked the twist holds under every stated assumption in Appendix D, read both one at a time and
all together:

- **MA1 (2 km standoff) alone:** negligible effect on the twist's routing (legs are 30–340 km); the
  twist's narrowing still holds.
- **MA2 (5.6% intercept) alone:** changes the *size* of the margin at both 2 and 3 jets
  proportionally on the SRBM-heavy legs, but does not change *which* operation the third jet helps
  more — Grey Dawn still had exactly one ICBM site left over for the third jet to finish; that fact
  is purely geometric (route length, not population weighting) and is intercept-rate-independent. A
  real Tier 2 P5 flex confirms MA2 barely moves the base margin (13.9%-15.5% across a ±50% flex).
- **MA3 (population table) alone:** rescaling the *whole table* by one common constant (e.g., a
  different but internally consistent casualty-per-yield scale) rescales both operations' totals
  proportionally and does not change the direction of the margin narrowing, only its absolute size
  in people. **But a real Tier 2 P5 run flexing individual warhead-class values (not the whole
  table together) found this is NOT true of MA3's individual entries**: a -50% flex on just the 5.2
  MT figure flips the base-case winner from B to A, and a +50% flex on the 3.1 MT figure ALSO
  flips it (to A, margin 1.2%); a +50% flex on 5.2 MT or a -50% flex on 3.1 MT both push the base
  margin past SPEC.md §2's 20% cap (to 28.1% and 37.0%). This is corrected from this file's
  original claim that MA2 was the case's most load-bearing assumption — MA3's individual class
  values are. See `sensitivity_model.py --probe 5` output and QA_REPORT.md.

  **Why this is disclosed, not eliminated (re-derived 2026-08-13):** Appendix B's population
  figures are no longer a bare, unsourced convention — they are computed from two real, cited
  sources: a validated cube-root blast-radius scaling law (Glasstone & Dolan; well within the
  tested yield range for 50 kt-5.2 Mt, not an extrapolation past known data — this is the kind of
  formula-based calculation that SHOULD be sourced and accurate) and the real 2020 Census average
  population density for large U.S. cities. What's genuinely, irreducibly uncertain is not the
  formula — it's which real density applies to this case's deliberately unnamed "major urban
  center." That's a forecast-shaped unknown (like a future price or a medical estimate), not a
  research gap: no amount of further research produces the one true density of a fictional city.
  A guide should frame a Hero's challenge to this table exactly that way — "which real city are
  you assuming, and how would a denser or sparser one change your recommendation?" — rather than
  as "the numbers might just be wrong."
- **MA4 (destroyed = fully protected) alone:** this is definitional, not a free parameter; nothing
  to stress-test.
- **All four simultaneously:** re-ran the full route-and-population computation with all four
  assumptions applied together (the numbers reported throughout this file and `case.json.derived`
  already are exactly this combined computation) — the twist narrows the margin from 13.6% to 5.0%
  without flipping the winner under the stated assumption set. `sensitivity_model.py`'s `FLEX` list
  documents which of these assumptions actually move the *recommendation*, not just the margin size
  (only MA2, taken to an extreme like 0% or ~100%, can do that — see the file's own comments).
