# Guide Notes: The Point Cloud Match

MS | Guide Notes | Adventure | 2026
**Tier:** T3 (MS stretch / HS entry) · **Primary metric:** registration error (mm of point-to-point
mismatch) per minute of technician time spent · **Margin:** **0.61%** on the face-value ratio
(Option A's naive ratio, trusting the rig's self-reported 0.40 mm, is marginally *smaller* — looks
better — than Option B's ratio using its real 0.55 mm corrected residual). Once the D2–D4 marker
evidence replaces that self-report with Option A's real leftover error (~160.65 mm), Option A's true
ratio is ~1.785 mm/min — roughly **400x worse** than Option B's ~0.0045 mm/min. See "The margin" below.

---

## Argument for A — Ship As Converged

The rig reported **converged**, which is the studio's own accepted signal that the alignment
solver is done. Option A costs zero additional technician minutes — Priya has already spent time
on this job before the deadline, and every minute of manual rework is a minute she may not have.
Two of the three markers land exactly where they should. The registration-error-per-minute ratio
for Option A is extremely favorable *if* the rig's reported error is trustworthy, because the
denominator (technician minutes) is as close to zero as this decision ever gets.

## Argument for B — The Marker Recheck

The rig's software cannot distinguish a rotation from a reflection on its own — that is a
documented limitation of automatic point-cloud alignment (Appendix A), not a guess. Marker 3's
actual position is consistent with a **reflection** of its expected position, not a rotation or
translation like Markers 1 and 2 — D2's congruence-vs-similarity test and D3's reflection test
are both built to catch exactly this. If the mirror is real, Option A ships a defect that costs
the studio a full re-shoot (Appendix C) — a cost that dwarfs the technician minutes Option B
would have spent. Option B's ratio is worse on paper (more minutes spent) but only Option B's
number is actually trustworthy, because it is checked against ground-truth markers rather than
against the solver's own self-report.

## The margin

**Total technician minutes on the job** (Appendix C's 90 minutes already spent is common to both
options; each option adds its own):

- **Option A** adds 0 minutes → 90 total. Face-value ratio = rig's self-reported error (0.40 mm,
  MA4) / 90 min = **0.004444 mm/min**.
- **Option B** adds 3 markers × 7 min (MA2) + 12 min re-export/re-check (MA3) = 33 minutes → 123
  total. Face-value ratio = manual-correction residual (0.55 mm, MA5) / 123 min = **0.004472
  mm/min**.

**Face-value margin = 0.61%** — Option A's naive ratio is *marginally smaller* (looks better) than
Option B's, by trusting the rig's unverified 0.40 mm. This is the trap: a student who stops here
concludes "A wins by the numbers." It is a razor-thin margin, in the spirit of the Robotics
Engineering exemplar (0.09%), and it is entirely an artifact of MA4.

**The reveal, using D2–D4's real marker geometry instead:** Markers 1 and 2 confirm a genuine
translation offset of (Δx, Δy) = (+3.00, +2.00) cm. Applying that same offset to Marker 3's
expected position predicts where it *should* land under a pure translation: (−6.47, 14.42).
Marker 3's actual scanned position is (9.47, 12.42) — a gap of **16.065 cm = 160.65 mm**, matching
almost exactly a reflection of its expected position across the rig's y-axis, not a rotation or
translation. That 160.65 mm — not the rig's 0.40 mm — is Option A's real leftover error if shipped.
Option A's *true* ratio is 160.65 / 90 ≈ **1.785 mm/min**, roughly **400x worse** than Option B's
0.004472 mm/min, and it blows through Appendix D's 1.0 mm tolerance (MA1) by two orders of
magnitude, while Option B's 0.55 mm residual passes comfortably.

**Deadline check:** the rig converged at 4:40 PM; the client deadline is 5:30 PM — a 50-minute
window. Option B's 33 task-specific minutes fit with 17 minutes to spare.

**Sensitivity:** MA1 (tolerance, 1.0 mm) and MA5 (Option B's residual, 0.55 mm) are each other's
tripwire — if the tolerance were tightened below ~0.55 mm, even Option B's corrected file would
fail client acceptance, a genuinely different and sharper classroom conversation ("the recheck
caught the mirror, but is 'close enough by eye' actually close enough for this client?").

## Five Socratic questions

1. Your D2 distance calculations show Markers 1 and 2 forming a triangle congruent to their
   expected positions, but Marker 3 doesn't fit that same rigid motion — what does it mean that
   *two out of three* markers "pass" and one doesn't? Does two-out-of-three tell you the file is
   mostly fine, or does it tell you nothing at all?
2. If your D5 ratio says Option A "wins" on millimeters-of-error-per-minute, what number in that
   ratio are you trusting that you haven't actually verified?
3. D4 asked you to predict Marker 3's position under a *pure translation*, using only the two
   trustworthy markers. How far off was the actual scanned position from that prediction — and
   is that gap closer to what a reflection would produce, or closer to ordinary measurement
   noise?
4. The rig reported "converged" with a low error number. Can a solver be *low-error* and *wrong*
   at the same time? What would have to be true about how it computes error for that to happen?
5. Appendix C gives you a hard deadline and an estimated number of minutes Option B costs. Before
   you argue Option B is "obviously right," did you actually check whether it fits in the time
   left?

## The trap

The confident wrong answer is: *"Two of three markers check out, so the scan is basically fine —
ship it."* That reasoning treats the marker check as a vote, where a majority passing is good
enough. It isn't. A single mirrored region doesn't shrink because most of the object is fine —
whatever geometry sits in the mirrored pass is now wrong regardless of what the rest of the mesh
looks like, and the client's downstream pipeline doesn't average across the mesh to decide
pass/fail. A student who computes D2–D4 correctly but then reasons "2 out of 3 is a passing
grade" has done the math right and drawn the wrong conclusion from it. Push on this directly:
*"If your car had three wheels and one of them was on backward, would '2 out of 3 are fine' be
your headline?"*

---

## Intro

Heroes, today's case is about trusting a tool that tells you it's done — versus trusting your own
eyes when something looks slightly off. There's no partial credit for "the software said so."

## Launch

Show a side-by-side of two nearly identical 3-D renders — one correctly aligned, one with a subtly
mirrored region (a real or illustrative example; if you don't have a raw asset, describe it: "one
arm of the statue is a mirror image of the other, not a rotation of it"). Ask: *"What's wrong with
the second one? Take your time."* Let it take a moment for someone to spot it.

> Priya has a converged file, a deadline in hours, and a bad feeling about one marker.
> **Hero name — what do you do? Open for us.**

## Anchor 1 — Take a stand and vote

Option A or Option B. No reasoning yet. Hands up. Write the split on the board.

*"Is anyone courageous enough to stand with ______?"*

## Anchor 2 — What is the problem we're solving?

Do **not** let them start calculating yet.

- What is the actual question here? Say it in one sentence.
- Is it "did the software converge"? Is it "is the file actually correct"? Is it "do we have time
  to check"? **Those are three different questions.**
- Someone will say "the software says it's fine, that's the point of the software." Is that true
  here? What would make a "converged" result untrustworthy?

> Let the confusion grow. *"Wow. This is a challenging problem."* Do not rescue them.

**The trap to let them walk into:** described above. Let a hero present the "2 of 3 markers check
out" argument confidently before anyone pressure-tests it.

## Anchor 3 — What is the process?

- What's the process we'll go through to answer it?
- If Marker 3 doesn't match, does that automatically mean the mesh is mirrored, or could it be
  something else — an unusually large measurement error, a marker that was misplaced when it was
  physically stuck to the object?
- If we end up with a ratio for each option, how will we decide? What's our tiebreaker *before*
  we see the numbers?

## Anchor 4 — What don't we know?

- What is missing that we'd need to answer this properly?
- Do we know the client's actual tolerance for registration error (Appendix D)? What if
  `case-research` couldn't find one and it's an assumption instead — does that change how
  confident either argument can be?
- Does Priya know for certain the mirroring is confined to Marker 3's region, or could it extend
  further into the mesh than three markers can tell her?

---

## Data Deep Dive

Now the numbers — walk D1 through D5 on the board using the real, populated Appendix B/C/D. In
particular:

- **D1:** Bunny reconstruction = 3.5947×10⁴ vertices, 6.9451×10⁴ triangles; Dragon = 5.66098×10⁵
  vertices; the stand-in "suspect pass," `bun315.ply`, is 35,336 of the Bunny's 362,272 real raw
  scanned points ≈ **9.75%**.
- **D2:** Distance(Marker 1, Marker 2) is *identical* in the expected set (11.848 cm) and the
  actual set (11.848 cm) — a genuine rigid transform, congruent. But Distance(1,3) collapses from
  16.755 cm (expected) to 4.206 cm (actual), and Distance(2,3) grows from 9.995 cm to 13.825 cm —
  neither a uniform scale change nor a rigid motion. The 1–2–3 triangle is **neither** congruent
  nor similar.
- **D3:** Marker 3 sits in Quadrant II expected, (−9.47, 12.42); reflecting across the rig's
  y-axis predicts (9.47, 12.42) — Quadrant I. Marker 3's actual scanned position is exactly
  **(9.47, 12.42)** — the reflected prediction lands exactly on it. That's the tell.
- **D4:** Solving with Markers 1 & 2 gives a consistent (Δx, Δy) = (+3.00, +2.00) cm for both.
  Applying that to Marker 3's expected position predicts (−6.47, 14.42) under a pure translation —
  16.065 cm (160.65 mm) away from where Marker 3 actually landed. Translation alone cannot explain
  it; reflection does, exactly.
- **D5:** Face-value ratios (A: 0.40mm/90min=0.004444; B: 0.55mm/123min=0.004472) are 0.61% apart —
  A looks marginally better. The real ratio, substituting Option A's 160.65 mm true error, is
  ~1.785 mm/min — ~400x worse than Option B. Deadline: 4:40 PM → 5:30 PM (50 min); Option B needs
  33 minutes, fits with 17 to spare.

## Twist — drop this at ~15 minutes into the discussion

Deliver it slowly.

> *"While you were building your case, the studio's QA lead ran Marker 4 — the one nobody thought
> they needed — through the same check, just out of habit."*
>
> (pause)
>
> *"It doesn't match either. Not the same way Marker 3 doesn't match — differently."*

**The real numbers behind the twist:** Marker 4's expected position is (−1.75, 18.73) cm —
Quadrant II. If Marker 4 followed Marker 3's exact failure mode (a reflection across the rig's
y-axis), its actual position would land at (1.75, 18.73). It does not. Marker 4's actual scanned
position is **(−1.75, −18.73)** — a reflection across the rig's *x*-axis instead, dropping it into
Quadrant III. Two different mirror axes on two different markers is worse news than one marker
being wrong twice: it suggests the scan isn't cleanly "one flipped pass," but something less
tidy — which is exactly why a three-marker manual recheck, as Option B is scoped, may not be
sufficient.
>
> (pause)
>
> *"Whatever's wrong with this scan might not be confined to one region after all."*

This does not hand anyone a clean win. It invalidates the popular position that "we only need to
fix the one marker we already suspected" — Option B, as scoped in Challenge 3, only re-registers
against the three known markers, and now a fourth, previously-ignored point suggests the problem
may be bigger than three markers can characterize. It does **not** make Option A right either —
if anything it strengthens the case that the rig's output can't be trusted blind. The room now has
to reckon with: *is a three-marker manual recheck even sufficient, or does this now need a full
re-scan regardless of which option we "chose"?*

> *"You have sixty seconds. Does this change your plan — or does it just make you want a fourth
> marker's worth more of time you don't have?"*

## Immediate recommit

- Who is still confident in their original choice? Why?
- **What just broke in your original model?**
- **Were you wrong — or were you just missing information?**
- Is there a third path hiding here — flagging the file as *not ready*, deadline or not, rather
  than choosing between A and B as scoped?

## Deep conflict — threads (20–30 min)

**Thread 1 — Trusting the tool vs. trusting the eye.** The rig is right almost every time; that's
why it's used. *"How do you decide when 'almost every time' isn't good enough for this file,
specifically?"*

**Thread 2 — Scope creep on the fix.** Option B as scoped only checks three known markers. The
twist suggests the real problem might be bigger. *"Is Option B still 'the marker recheck,' or has
the twist quietly turned it into a different, bigger job?"*

**Thread 3 — Who eats the cost of being wrong.** Priya, personally, is the one who signs off. If
she ships Option A and it's wrong, it's on her. If she chooses Option B and misses the deadline
over a marker that turns out fine, that's also on her. *"Which mistake is more forgivable, and
does that change what she should do — or just how she should feel about it?"*

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. *"Thirty seconds — A or B?"* Two or three heroes, fast. Stand/sit vote, no explanation. |
| **3:00–10:00** | Position defense (pre-twist). *"Convince us it's better, not just faster."* Press anyone leaning A: *"What are you trusting that you haven't verified?"* |
| **10:00–15:00** | Pressure-test the models. *"Whose plan is most fragile if Marker 3 really is mirrored?"* *"Whose plan is most wasteful if it isn't?"* |
| **15:00** | **DROP THE TWIST.** Slowly, with pauses. Finish: *"Sixty seconds — does this change your plan?"* |
| **15:00–20:00** | Immediate recommit. Who reverses? What broke? |
| **20:00–30:00** | The three threads: trusting the tool · scope creep · who eats the cost. |
| **30:00–45:00** | Close, re-vote against the Anchor 1 board, reflection, lessons learned. |

## Close

- **Vote again.** Compare to the Anchor 1 board. Who moved?
- We asked ______ as our key question. Was it the right question?
- What math was new to you here, and how did you attack it?
- If you got a case like this next time, what would you do differently?

## Lessons Learned

A tool that reports success is not the same as a tool that verified success — "converged" is a
statement about the solver's own internal error metric, not an independent check against ground
truth. The three (then four) marker points are the only genuinely independent evidence in this
case, and reading them correctly required distinguishing congruence from similarity, a rotation
from a reflection, and a real defect from measurement noise — the actual geometry content of this
case, not decoration on top of a story.

## Standards Touched On

**Reinforcement case, not new coverage.** `Congruent` · `Similar` · `Quadrant` · `How to reflect
a figure across the Y-Axis` were originally scoped as this case's new coverage, but by the time
this case was gated, two concurrently-authored sibling cases (Company Front / The Repeat Match,
and Airstrike / Urban Planner) had already published claiming the same four skills — each now
sits at n=2 in the standards spine. This case reinforces them with a genuinely different scenario
(point-cloud/photogrammetry registration) rather than closing a new gap; see
`case.json.reinforcement_note` and `LEARNING_GOALS.md` for the full adjacent-coverage check.

**Also exercised:** Coordinate Pair (also Ordered Pair) · Transformation · Translation · Rotation
· Reflection · Scientific Notation · Ratio · System Of Equations · How to find the distance
between two coordinate pairs on a coordinate plane · How to write a number in scientific notation
given its standard notation · How to find the percent of a number

---

## Sensitivity note

The case's real, trap-independent recommendation (Option B) rests on a fixed geometric fact
(Marker 3's actual position matches a reflection of its expected position, a 160.65mm real error
for Option A) that does not move under +/-50% flexing of any Modeling Assumption (MA1 tolerance,
MA2 marker time, MA3 re-export time) — Option A's true ratio stays ~400x worse than Option B's
across the full sweep. The naive, pre-trap face-value D5 ratio (the one a student computes before
doing D2–D4) is a different story: it DOES flip winner under a standard +/-50% sweep of MA2 and
MA3, because the case's own primary metric (mm of error per minute) rewards Option B for spending
more minutes at a fixed residual. See `case.json.sensitivity_disclosure[]` and
`cases/the-point-cloud-match/sensitivity_model.py` for the full sweep and numbers.

## Cohort bands

| Band | Typical size | What changes |
|---|---|---|
| **Full** | 12–20 | Socratic plan runs as written, 0:00–45:00. Anchor 1 vote is a real show-of-hands split. All three deep-conflict threads run. |
| **Compressed** | 6–11 | Combine Anchor 2 and Anchor 3 into one pass. Run only Thread 1 (trusting the tool vs. trusting the eye) at 20:00–30:00 — it's the sharpest and needs the least setup. Twist still drops at 15:00. Total runtime ~30 min. |
| **1:1 / pair** | 1–2 | No vote at Anchor 1 — the learner states an initial position instead. The guide argues the other side directly rather than cold-calling. The twist still lands; "who reverses" becomes "would you reverse, and why." Skip the deep-conflict threads; go straight from twist-recommit to Close. |

## Facilitator note — sensitivity of subject matter

None required. This case's stakes are professional (a studio's re-shoot cost, a technician's
workload) rather than personal hardship — no SPEC §6 flag applies.
