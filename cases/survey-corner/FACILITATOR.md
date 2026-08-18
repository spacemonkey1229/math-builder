# Guide Notes: Survey Corner

**Case:** Survey Corner · **Tier:** T2 · **Band:** MS-core · **Studio:** Heroes Academy
**Standards:** Parallel Lines & Transversals (partial) + Triangle Classification (partial) —
all `new_coverage` (see `case.json.standards[]` for the exact ids)

Researched and margin-resolved 2026-08-12 (`margin_pct` = 11.11, see `sensitivity_model.py`). This
file is re-checked for drift at every readiness run (the continuity checks in `case-readiness`).

## Intro

Frame the format before anything else: this is a real professional judgment call with a
contractor's schedule on the line, not a worksheet. Name the opener — "Two pins, eleven inches
apart, and only one of them is the corner the 1962 plat actually meant. Priya has one
recommendation to make before seven this morning." Let the stakes land before moving to the Launch.

## Launch

Show both candidate pins side by side — Pin 1 (older, rust-streaked) and Pin 2 (newer, sharp
edges) — with no angle data labeled, just a description of their physical condition. Ask: "Which
one do you think is the real corner, just from how they look?" Do not confirm or correct answers
here. The point is a gut read before anyone touches the geometry.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Priya on Pin 2 — the newer one, the one that doesn't
look the part?" Show of hands, both options, no discussion. Record the count — Close will ask them
to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What actually tells you a pin is the true corner?"**

Let confusion grow here — this is deliberate. Heroes will want to reason from the pins' physical
appearance (age, rust, sharpness). Push on it: "Priya isn't a historian. She's a surveyor. What
does the plat itself — the actual recorded document — tell her, that a pin's appearance can't?" If
the room lands on "the plat's recorded angle" on its own, the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has the right question, ask them to name the actual steps before touching the
appendices: find the plat's expected corner angle (D1), find each pin's actual angle from the field
data (D2, D3), run a second independent check with the witness triangles (D4, D5), then compare how
far off each pin is (D6, D7). Re-ask: "Is our question still the right one, now that we can see the
steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gaps honestly: Appendix F's two Modeling Assumptions (MA1 the plat's recorded
angle, MA2 all of Priya's own field readings) are stated, not sourced from a public database — no
public archive of real property-line disputes' raw total-station field books exists. Ask which one
actually changes the recommendation if it moves (MA1 — see Data Deep Dive).

Also surface that Appendix C gives Priya **two** independent checks — angle and distance — and
they disagree (the distance check favors Pin 1, the angle check favors Pin 2). This is not a bug in
the case; it is real. Ask: "Which piece of evidence would you trust more, and why?" before telling
the room which one Priya trusts.

## Data Deep Dive

Now, and only now, the numbers. Walk D1-D6's angle work and D7's margin comparison together as a
room, cold-calling for D1 (the parallel-lines derivation) and D4/D5 (the triangle classifications)
specifically — these are the two places a Hero who tries to shortcut by just reading a total-station
number directly, instead of applying the actual angle relationship, will visibly get the wrong
answer, which is useful information for the facilitator, not a moment to rescue.

**Facilitator-only angle note.** D1: co-interior angles sum to 180°, so expected = 180 − 93 = 87°.
D2: Pin 1's raw reading (88.5°) is supplementary to its interior angle, so actual = 180 − 88.5 =
91.5°. D3: Pin 2's raw reading (89.0°) gives actual = 180 − 89.0 = 91.0°. Both actual angles land
on the *same side* of the expected 87° (both larger) — worth naming explicitly once a Hero notices
it, because it is exactly why the base-case verdict is stable under MA1's flex (see Twist).

**Facilitator-only triangle note.** D4 (Pin 1 witness triangle): 96° + 45° + third = 180°, third =
39° — classify obtuse (96° > 90°), scalene (96/45/39 all distinct). D5 (Pin 2 witness triangle):
61° + 55° + third = 180°, third = 64° — classify acute (all under 90°), scalene (61/55/64 all
distinct). Neither triangle by itself proves which pin is correct — they're a second, independent
check, not the primary metric — but the "acute vs. obtuse" contrast is a good hook for the room
("Pin 2's own witness triangle is the tidier shape too" — argument for B).

**Facilitator-only distance note.** Pin 1's measured distance from the NW corner (247.8 ft) is only
2.8 ft off the plat's recorded 245.0 ft; Pin 2's (251.5 ft) is 6.5 ft off — the distance check
favors Pin 1, real and quantified, the opposite direction from the angle check. Priya's stated
reason for weighting angle over distance: a rough, overgrown fence line exposes a distance shot to
more real-world measuring error (brush, slope, an uneven tape or laser path) than a single clean
angle shot from a leveled instrument. This is a genuine professional judgment call, not a hidden
tie-breaker — a strong pitch should name it and argue for (or against) it, not just report both
numbers and move on.

**Facilitator-only margin note.** Deviation from expected: Pin 1 = |91.5 − 87| = 4.5°, Pin 2 =
|91.0 − 87| = 4.0°. Margin: **11.11%**, Pin 2 wins (smaller deviation). MA1's real uncertainty is
modeled against the northwest angle's 3° excess past square (93° = 90° + 3°), not the whole 93° —
a real deed recording error plausibly moves that 3° excess by a lot in relative terms, but moving
the *whole angle* by the same relative amount (e.g. to 46.5° or 139.5°) would be absurd for a real
plat. Flexing the 3° excess ±50% (giving an effective NW angle of 91.5°-94.5°) holds Pin 2 as the
winner across the whole swept range — margin ranges 8.33%-16.67% — because both pins' actual angles
sit on the *same side* of the expected angle, so a shift in the expected angle moves both deviations
in the same direction and preserves their order.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"It's the middle of the discussion. Priya goes back to double-check her own field notes against the
total station's raw digital export — the numbers she wrote down by hand versus what the instrument
actually logged."

"Pin 2's hand-written reading doesn't match the logger. Does the verdict still hold?"

**Facilitator-only: what the numbers actually do.** The digital export shows Pin 2's true raw
reading was 88.3°, not the hand-transcribed 89.0° — a real, disclosed transcription-error scenario.
Recomputed: Pin 2's actual angle becomes 180 − 88.3 = 91.7°, deviation |91.7 − 87| = **4.7°** — now
*larger* than Pin 1's unchanged 4.5° deviation. **The verdict flips: Pin 1 is now the closer match**,
by a thin **4.26%** margin. Do not hand this reasoning over unprompted; let a Hero who did D2/D3/D6
carefully reason toward it — the real skill being tested is recognizing that a verdict this close
(11.11% base) was never as solid as it looked, and that a surveyor's own transcription is exactly
the kind of thing worth double-checking before making a professional recommendation.

**Facilitator-only: the checks converge after the twist, and it cuts against Priya's own reasoning.**
Before the twist, angle favors Pin 2 and distance favors Pin 1 — genuine disagreement. After the
twist, Pin 1's angle deviation (4.5°, unchanged) becomes *smaller* than Pin 2's (4.7°), so angle now
also favors Pin 1 — the two checks **converge**, they no longer disagree. Thread 4 below is written
as if the checks still conflict; by the time it runs (20:00-30:00, after the 15:00 twist), they
don't anymore — reframe it live as "they used to disagree; why don't they now?" rather than running
it as originally scripted. There is also a sharper point worth surfacing if the room is ready for
it: Priya's own stated reason for trusting angle over distance was that a clean, leveled-instrument
angle shot is less exposed to error than a distance shot dragged across brush and slope — but the
twist's actual content is that the angle reading is the one that turned out to have an error (a
hand transcription mistake), while the distance reading needed no correction at all. A sharp Hero
can legitimately argue the twist undercuts Priya's own methodology, not just her numbers. Let a
Hero find this rather than announcing it — it is the strongest possible version of thread 4's
question, not a gotcha to spring unprompted.

## Immediate recommit

Re-vote immediately. Ask by name: "Does the corrected reading change your vote, or just how
confident you are in it?" That distinction is the transferable skill, not the vote itself.

## Deep conflict — four threads (20-30 min)

1. **Appearance vs. math.** A pin's age and condition feel like real evidence. Why does the case's
   actual verdict have nothing to do with either — and what would it take for physical condition to
   matter at all in a real boundary dispute?
2. **Two independent checks, one verdict.** D2/D3's corner-intersection angle and D4/D5's witness
   triangle are separate measurements. Why bother with both instead of trusting the first one?
3. **A verdict that flips on your own error.** The twist doesn't change the plat, the pins, or the
   geometry — only a transcription mistake. Is a margin that can flip from a single hand-written
   number ever really "safe," or does professional surveying practice exist specifically because of
   moments like this one?
4. **When two real numbers disagree.** Before the twist, the angle check and the distance check are
   both real, quantified, and they point at different pins. Priya picks the angle check for a stated
   reason (measuring error is more likely on a rough distance shot than a clean angle shot). Is that
   reason actually strong enough to decide a real property dispute, or is it just the tiebreaker
   Priya reaches for because the angle math is the one she already trusts? Push further if the room
   is ready: after the twist, the two checks stop disagreeing — does that make Priya's original
   reasoning look better, or does the fact that the "clean" angle reading was the one with the actual
   error undercut it?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both pins, cold-call for a gut read, no angle data yet |
| 3:00–10:00 | Position defense — *"Convince us a pin's age isn't enough to trust it"* |
| 10:00–15:00 | Pressure-test the models — *"Whose angle number is most fragile?"* |
| **15:00** | **DROP THE TWIST** — the transcription correction, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (appearance vs. math; two checks, one verdict; a flip on your own error; when two real numbers disagree) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes will assume the older, rust-streaked pin must be the "real" one — it looks more
official, more permanently placed — and recommend Pin 1 without ever finishing the angle math.
Watch for a pitch that leans on physical description (age, rust, sharpness) and never actually
computes and compares D1/D2/D3's angles — it has not actually settled the dispute. A second,
subtler version: a Hero who does finish the math might notice the distance check (Appendix C) also
favors Pin 1 and treat that as confirmation, without ever asking why Priya weights the angle
evidence more heavily — two pieces of quantified evidence disagreeing is not the same as one of
them being wrong.

## Socratic questions

1. Pin 1 is older. Pin 2's angle is closer to the plat's math. Which one would you trust if you only had one of those two facts — and why doesn't "older" win on its own here?
2. D1 uses a same-side (co-interior) angle relationship, not an alternate-interior one. What would change about the expected southwest angle if the case had instead described the two corners as being on opposite sides of the transversal?
3. Both pins' actual angles came out larger than the plat's expected 87°, neither one smaller. Does that pattern tell you anything about where a resurvey error is more likely to have crept in?
4. D4 and D5 give you two independent triangles built the same way. Why does a professional surveyor bother with a second, independent check instead of just trusting the corner-intersection angle from D2/D3 alone?
5. Priya has one recommendation to make before the contractor arrives. What does she tell him — and does the twist change the answer?
6. The distance check favors Pin 1; the angle check favors Pin 2. Priya trusts the angle check more, because a rough fence line exposes a distance shot to more real-world error than a clean angle shot. Is that a good enough reason on its own, or does a strong pitch need to argue it more directly?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that didn't
move at all after the twist is worth asking about directly: did the twist not land, or did the room
already understand how thin the base margin was?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes distrusted the "both pins are on the same side of expected" pattern (D2/D3) as too
  convenient, or used it correctly to reason about the flex sensitivity.
- Whether the "physical appearance isn't evidence" trap landed as a genuine surprise or as something
  the room caught quickly given the case's framing.
- Whether the twist's transcription-error framing produced real reflection on professional
  double-checking, or just a shrug that the vote didn't have to change.

## Standards Touched On

Transversal Line · How to find angle measures of intersecting lines · How to find angle measures
given parallel lines, a transversal line and at least one angle measure · Acute Triangle · Obtuse
Triangle · Scalene Triangle

## Facilitator note — sensitivity

None required (SPEC §6) — the stakes here are a professional resurvey judgment call and a
contractor's schedule, not personal loss or hardship.
