# Guide Notes: Patrol Triangle

MS | Guide Notes | Adventure | 2026-27
**Tier:** T2 (MS-core) · **Primary metric:** minutes of ranger response time per square kilometer of reserve covered · **Margin:** **13.95% — the Interior Web (B) wins**

---

## Argument for A (the Perimeter Loop)

The Perimeter Loop covers far more total ground: six 18/11/9 km boundary sectors cover 233.9 km² of the reserve's 360 km² (about 65%), versus the Interior Web's eight 5.7 km equilateral sectors covering only 112.5 km² (about 31%) — more than double the total area under patrol. A poaching incident is more likely to occur somewhere inside *some* Perimeter Loop sector simply because the Perimeter Loop claims so much more of the map. The strongest real argument for A is raw footprint: a faster response to an incident that never gets patrolled at all is worthless, and A patrols twice as much reserve.

## Argument for B (the Interior Web)

The Interior Web wins the case's actual primary metric. Each Interior Web sector is equilateral (5.7 km a side), so no point inside it is ever farther than one full side length (5.7 km) from its outpost — a direct, geometric consequence of building the sector around equal sides. That gives a response time of 6.84 minutes at the reserve's shared 50 km/h patrol speed. The Perimeter Loop's longest side (18 km) sets its worst-case response distance at 21.6 minutes — over three times longer — because a long, narrow scalene triangle by construction has one vertex much farther from the outpost than the others. Dividing each option's time by its own sector's area: Perimeter Loop = 21.6 min ÷ 38.99 km² ≈ **0.5540 min/km²**; Interior Web = 6.84 min ÷ 14.07 km² ≈ **0.4862 min/km²**. The Interior Web is more efficient per square kilometer it actually covers, and needs fewer total patrol teams to staff (16 vs. 18) despite its denser layout.

## Margin

**Computed: 13.95%, the Interior Web (B) wins.**

| Option | Standard sector | Area | Response distance | Response time | Ratio (min/km²) |
|---|---|---|---|---|---|
| A — Perimeter Loop | scalene, obtuse (18/11/9 km) | 38.99 km² | 18 km | 21.6 min | 0.5540 |
| B — Interior Web | equilateral, acute (5.7 km) | 14.07 km² | 5.7 km | 6.84 min | 0.4862 |

`margin_pct = (0.5540 − 0.4862) / 0.4862 × 100 = 13.95%` (margin is computed relative to the winning option's own value, B's ratio — the same convention `sensitivity_model.py`/`tier2_probes.py` apply to the efficiency-framed metric, so the two never silently disagree)

**How the margin was tuned to land inside SPEC §2's ~20% cap:** the Perimeter Loop's sector (18/11/9 km, chosen to be genuinely scalene and obtuse) and the Interior Web's sector (5.7 km equilateral, chosen so its area lands close to the reserve's real 14 km²-per-team density standard) were sized independently for pedagogical clarity first. The resulting 13.95% margin was not separately re-tuned — it fell out of these two geometrically-motivated shapes, which is itself worth noting to a sharp Hero who asks "did you pick these numbers to make it close?" (Answer: the shapes were picked to be clean teaching examples of scalene/obtuse and equilateral/acute triangles first; the margin landing under the cap was a genuine, not-guaranteed outcome — an early version with a 20 km longest side for A pushed the margin to just over 20% and was revised down to 18 km specifically for balance, which **is** a real tuning step and should be named if asked directly).

---

## Five Socratic questions

1. "The Perimeter Loop covers about twice as much total reserve area as the Interior Web. Why doesn't that automatically make it the better plan under this case's own primary metric?"
2. "Your D1 table classifies the Interior Web's sector as equilateral. What is it about *all three sides being equal* that guarantees no point inside that triangle is more than one side length from the outpost — could you make the same guarantee for the Perimeter Loop's sector?"
3. "If the Perimeter Loop's longest side were 12 km instead of 18 km, would your D3 response time change? Would your D1 classification (scalene, obtuse) still hold?"
4. "Your D5(a) check found the three outposts' reported distances can't actually form a triangle. What does that tell you about whether the Interior Web's 'triangulate the sighting' claim can be trusted right now?"
5. "You needed 18 total patrol teams for the Perimeter Loop and 16 for the Interior Web. Does that change your recommendation, or is it a separate consideration from the primary metric?"

## The trap

**Two versions of the same underlying trap — building D4's ratio from mismatched numbers.**

The obvious version: comparing raw totals from only one column instead of computing the combined ratio. A learner who compares total area covered (233.9 km² vs. 112.5 km²) will confidently pick the Perimeter Loop. A learner who compares raw response times (21.6 min vs. 6.84 min) will just as confidently pick the Interior Web. **Both comparisons are real and both are incomplete** — the case's actual primary metric is a ratio of the two (minutes per square kilometer *covered*), and only that ratio settles which option is actually more efficient with the ground it patrols.

The subtler, more dangerous version (found independently by a fresh trap-check pass on this case): a learner who *does* build a ratio, but crosses scales while doing it — dividing the standard sector's response time by the option's **total** coverage area (D2's 233.9 km² or 112.5 km² figure), instead of by that same **standard sector's own** area (38.99 km² or 14.07 km²). This still produces a number with the right units (min/km²) and still "feels" more rigorous ("I used the whole-reserve total, not just one triangle"), so nothing about it looks broken — but Appendix E says explicitly that the sector-count assumptions (MA2/MA4) "change total coverage... but do not change the standard-sector ratio used for the primary metric," precisely to warn against this substitution. A pitch that reports only total area, only response time, or a ratio that mixes a total-scale number with a single-sector number has not actually answered the dilemma as posed — ask directly: "is the area in your denominator the same triangle your time is measured across?"

## Twist

**A confirmed sighting report comes in from a location that sits inside one of the Perimeter Loop's six boundary sectors but falls entirely outside all eight of the Interior Web's sectors** — squarely in one of the "real gaps" the Interior Web's smaller footprint leaves in the reserve's interior-facing edge. Read it slowly: *"Dispatch just confirmed a sighting. Here's its location on the map. Under the Interior Web, which outpost handles this? ... None of them do — it's outside every Interior Web sector you drew. Under the Perimeter Loop, it's inside Sector 4. You have sixty seconds: are you changing your recommendation, or not?"*

The follow-up is the whole point: **did the primary metric (minutes per km² covered) stop mattering the moment an incident happened somewhere it doesn't apply?** A Hero who reverses to A should be pressed on whether one incident location is enough evidence to overturn a 13.95% efficiency edge that holds everywhere the Interior Web *does* reach — and a Hero who holds B should be pressed on what they'd tell the director about the ground B simply never touches. Neither position is obviously correct after the twist; that is the design.

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. Show both maps side by side, unlabeled A/B. *"Thirty seconds — which patrol plan do you think responds to trouble faster? Stand if you'd pick the tighter mesh, sit if you'd pick the wide loop."* No calculation yet. |
| **3:00–10:00** | Position defense. *"Convince us it's better, not just that it looks tighter or wider."* Press anyone arguing from total area alone or response time alone: *"What's the other number you're not using?"* |
| **10:00–15:00** | Pressure-test the models. *"Which classification in your D1 are you least sure of — scalene vs. equilateral, or acute vs. obtuse? Walk me through how you checked it."* |
| **15:00** | **DROP THE TWIST** — the sighting outside every Interior Web sector, delivered slowly. |
| **15:00–20:00** | Immediate recommit. Who reverses? *"What just broke in your model — were you wrong, or just missing information?"* |
| **20:00–30:00** | Two threads: **(1) ratio vs. total** — "does covering more ground always beat responding faster to the ground you do cover?"; **(2) trust in the network** — "your D5(a) check found the outposts' own reported distances can't form a real triangle — does that change how much you trust the Interior Web's 'triangulation' pitch, independent of the twist?" |
| **30:00–45:00** | Close, re-vote against the Anchor 1 board, reflection, lessons learned. |

---

## Guide Notes — the anchor ladder

### Intro
Heroes, today's case is a real trade-off patrol planners actually face: cover more ground, or reach any single point on that ground faster. The only way to settle it honestly is to do the triangle geometry, not just eyeball the two maps.

### Launch
Show both patrol maps side by side, unlabeled. *"One of these plans could get a truck to almost any point in its sector in under seven minutes. The other one covers twice as much of the reserve. Which one do you trust more with the dry season starting in four days?"*

### Anchor 1 — Take a stand and vote
Perimeter Loop or Interior Web. No reasoning yet. Hands up, write the split on the board.
*"Is anyone courageous enough to stand with the smaller footprint?"*

### Anchor 2 — What is the problem we're solving?
Do not let them calculate yet.
- What is the actual question? "Which plan covers more reserve"? "Which plan responds fastest"? "Which plan is most efficient per square kilometer it actually covers"? **Those are three different questions, and only the third is what Derek was asked to answer.**
- Someone will say "obviously the tighter mesh is better, it's faster." Faster to where — averaged over how much ground?
- Let the confusion grow. *"Wow — turns out 'better patrol plan' isn't one number, it's at least three."*

### Anchor 3 — What is the process?
- If we just compare total area covered, are we done? (No — the Perimeter Loop wins that outright, and yet the case's own metric still favors the Interior Web.)
- If we just compare response time, are we done? (No — same problem in reverse; raw time alone ignores how much ground each plan is responsible for.)
- Is our question still the right question? (Push toward: the ratio is the only number that answers "efficient with the ground you patrol," which is what was actually asked.)

### Anchor 4 — What don't we know?
- What's missing that we'd need to trust this fully? (The reserve's own real GPS logs for the fixed outposts don't even agree with each other, per Appendix D and D5(a) — do we trust the "triangulation" claim before that's fixed?)
- Do the stated sector counts (6 for the Loop, 8 for the Web) themselves need re-checking against the real 360 km² reserve — could either plan realistically add more sectors?
- Does the shared 50 km/h speed limit (Appendix A) hold on every road inside the reserve, or is that itself an assumption worth challenging?

## Data Deep Dive
Walk the room through classifying each standard sector (side-length and angle comparisons), computing area (Heron's formula or an equivalent method for the scalene case; the standard equilateral-triangle area formula for the other), converting distance and speed into elapsed time, and building the final ratio. Ground truth for cross-checking a Hero's own work:

| Option | Area | Response time | Ratio |
|---|---|---|---|
| Perimeter Loop | 38.99 km² | 21.6 min | 0.5540 min/km² |
| Interior Web | 14.07 km² | 6.84 min | 0.4862 min/km² |

## Close
- Vote again. Who moved, and why — because of the ratio, or because of the twist?
- Was "which plan responds fastest" the right question, or was it really "which plan is most efficient with the ground it patrols" — and does the twist mean even that wasn't quite right either?
- What math was new to you here — classifying the triangles, finding the area, or building the final ratio?

## Lessons Learned
The case's real lesson is that a ratio built from two real, correctly-computed numbers (time and area) can point one direction while either number alone points the other way — and that a plan can be the more *efficient* choice everywhere it operates while still leaving real gaps the other plan would have caught. Both things can be true at once; the twist exists specifically to keep the discussion from resolving into "the math already told us the answer."

## Standards Touched On

**New coverage:** none — see `case.json.reinforcement_note` (a live spine sweep found zero skills anywhere at literal n==0; the reinforcement carve-out applies). This case reinforces all six of Geometry/Triangles's remaining thin skills — `Acute Triangle` · `Obtuse Triangle` · `Scalene Triangle` · `Equilateral Triangle` · `Leg` · `Triangle Inequality Theorem` — from n=2 to n=3, the group's entire remaining thin set.

**Reinforced:** `Area` · `How to find elapsed time` · `How to find a missing amount in a proportion`.

## Facilitator note — sensitivity

**Low-level flag, per SPEC §6.** This case's setting is anti-poaching patrol planning, which implies a human threat (poachers) off-page. **No casualty math is required or implied anywhere in this case** — the entire dilemma is pure coverage geometry (triangle classification, area, rate, and a network-consistency check). The discussion lead should say this explicitly at the Intro if the room starts speculating about confrontations: the math here is about triangles and travel time, not about modeling violence.
