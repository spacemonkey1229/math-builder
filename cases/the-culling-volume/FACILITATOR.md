# FACILITATOR.md — The Culling Volume

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Culling Volume · **Tier:** T2 (MS-core) · **Studio:** MS Adventure
**Standards:** Geometry/Surface Area And Volume — six "how to…" skills (surface area of a
pyramid/cylinder; volume of a pyramid/cylinder/cone/sphere) — see `case.json.standards[]` for
exact ids.

**Status:** `case-research` complete (2026-09-18). All `{{NEEDS_SOURCE: ...}}` placeholders are
resolved — two real, cited figures ground the geometry (a street-light pole height range [S1], a
real ASME B36.10 pipe diameter standard [S2]) and one real, exact quote from Unreal Engine's own
documentation [S3] grounds the entire premise (real engines build visibility tests from simplified
bounding shapes); every other dimension and every cost figure is a disclosed Modeling Assumption,
because no publishable figure exists for any of them. `case.json.balance.margin_pct` is a real,
computed **13.2%**. Everything below is the case of record, not a placeholder.

**Sensitivity note (SPEC §6):** ordinary workplace/engineering decision pressure — a frame-budget
review with a ship deadline. No illness, death, or family hardship. Standard facilitator handling
suffices.

## Argument for A — Keep the bounding sphere

Option A's cost is pure and cheap: 1,800 tested props/frame × 0.0005 ms [MA7] = **0.900 ms** of
CPU cost, full stop. A's case is that a single distance-squared-vs-radius-squared comparison is
about as fast as a geometric test can possibly be, and that cost is completely predictable
regardless of how oddly-shaped the scene's props are. Under the case's stated wasted-volume
conversion [MA9], A's total cost including render/overdraw waste is **3.063 ms** — higher than B's,
but A's argument doesn't have to concede that: MA9 is the single most disclosed-fragile dial in
the whole case (see Sensitivity, below), and a Hero who successfully challenges it downward can
flip the recommendation back to A.

## Argument for B — Switch to the bounding capsule

Option B costs three times as much per test — 1,800 × 0.0015 ms [MA8] = **2.700 ms** of CPU cost —
but wastes dramatically less bounding volume: roughly 306,500 liters scene-wide versus A's roughly
108.2 *million* liters, a gap of two and a half orders of magnitude. Under the case's stated
conversion [MA9], that difference in wasted volume matters more than the 1.8 ms of extra CPU cost:
B's total cost is **2.706 ms**, versus A's 3.063 ms. B's real case is that for this specific class
of prop — long, thin, elongated — a sphere's waste is not a rounding error, it is the dominant term
in the whole cost comparison, and the "cheap test" argument for A only looks true if you ignore
what that cheap test is actually buying.

## The margin — real numbers, and how fragile this case actually is

`case.json.balance.margin_pct` = **13.2%**, within SPEC §2's 20% cap. The arithmetic, in full:

- **CPU cost:** A = 1,800 × 0.0005 = 0.900 ms. B = 1,800 × 0.0015 = 2.700 ms.
- **Wasted volume (scene-wide, 600 of each of 3 prop types):** A ≈ 108,172,271 L. B ≈ 306,525 L.
- **Render/overdraw cost:** A = 108,172,271 × 0.00000002 = 2.163 ms. B = 306,525 × 0.00000002 =
  0.006 ms.
- **Total:** A = 0.900 + 2.163 = **3.063 ms**. B = 2.700 + 0.006 = **2.706 ms** (winner, lower
  cost).
- **Margin:** |3.063 − 2.706| / 2.706 × 100 = **13.2%.**

**This case is genuinely fragile, and deliberately so — all three of its cost dials (MA7, MA8,
MA9) are disclosed as Category X.** `sensitivity_model.py`'s ±50% flex sweep found:
- `sphere_cost_per_test` (MA7): −50% **flips the winner to A** (margin 3.5%); +50% breaches the
  20% cap (29.8%, B still wins).
- `capsule_cost_per_test` (MA8): −50% breaches the cap (125.9%, B still wins); +50% **flips the
  winner to A** and breaches the cap (32.4%).
- `render_cost_per_liter` (MA9): −50% **flips the winner to A** and breaches the cap (36.4%); +50%
  breaches the cap the other way (53.0%, B still wins).

**Do not treat a student who challenges any one of these three figures as having missed the
point** — every one of them has a real, defensible flip case, because none of them has a hard
public source behind it. This is the case's central teaching point: the geometry (whose bounding
shape wastes how much) is solid and computable; the *verdict* rides entirely on cost figures
nobody can look up.

## Five Socratic questions

1. Option A's per-test cost is 3× cheaper than Option B's — so why does Option A end up costing *more* overall?
2. Look at the wasted-volume numbers for the lamppost specifically — the bounding sphere wastes 137,143.4 liters for one prop. Does that number surprise you, and why does a sphere waste so much more on a *long, thin* object specifically than a *compact* one would?
3. MA9 (the liters-to-milliseconds conversion) has no public source behind it at all — if that number were cut in half, does the recommendation change? What does that tell you about how much this case's "answer" actually depends on real geometry versus an invented conversion rate?
4. The capsule's own hemispherical end caps use the same volume formula as Option A's bounding sphere — where exactly does that formula show up inside Option B's own construction?
5. If the game world simply had fewer of these props (say, 100 of each instead of 600), would that change which option wins? Why or why not?

## The trap

**A learner who compares only the two per-test CPU costs (0.0005 ms vs. 0.0015 ms) and stops there
— concluding "the sphere is 3× cheaper, so keep the sphere" — has fallen into the case's central
trap.** That comparison is real and correctly computed, but it silently drops the render/overdraw
term entirely, which is where the actual scene-wide cost gap lives for this class of prop. A pitch
that never computes Appendix B's wasted-volume figures, or computes them but never carries them
into Appendix D's full cost formula, has done half the assignment's real work at best, even if it
lands on a confident recommendation.

**A second, related trap:** a student who does compute both terms can still misread the sphere's
wasted-volume numbers (in the hundred-million-liter range) as a sign of a math error, rather than
recognizing that this is the correct, if startling, consequence of a sphere sized to a long, thin
object's farthest tip. The number is supposed to look absurd — that absurdity *is* the case's
point about why spheres are a poor fit for this specific prop class.

**A third trap, found independently by a fresh cold-read of the packet, and easy to miss because
it quietly favors Option B:** a student can build the bounding capsule from a component's own
height and radius instead of the *prop's full total height and widest radius*. For the lamppost,
this means using the pole's 6.1 m height and 0.075 m radius instead of the full 6.4 m height and
the cone cap's 0.15 m radius — the same mistake for the sign post (2.5 m/0.05 m instead of
2.65 m/0.1414 m). This reads plausibly ("the capsule hugs the pole; the pointy cap sticks out past
the rounded hemisphere caps"), but Appendix B is explicit that the capsule must span the prop's
*full* height at its *widest* radius, specifically so the capsule fully contains the object —
skipping this produces an undersized capsule that doesn't actually contain the prop, and an
artificially small capsule volume that makes Option B look cheaper than it really is. Watch for
this specifically when a group's Option B numbers look suspiciously good.

## Twist

The structural twist is Appendix D's MA9 conversion rate itself, revealed as fragile rather than
fixed. Facilitators can manufacture the twist moment directly: after the room has computed and
voted on the base-case numbers (favoring B, 2.706 ms vs. 3.063 ms), reveal that MA9 is not a real,
sourced figure — it is a stated scenario assumption with no public backing at all — and ask
Socratic Question 3. Let the room discover that halving MA9 flips the recommendation back to A.

---

## Guide Notes — the anchor ladder (SPEC Section 7, anchor-ladder subsection)

### Intro

Frame the format: a rendering engineer has nineteen minutes before a frame-budget review and has
to recommend one bounding-shape policy for an entire class of scene prop, using real geometry and
cost figures she mostly has to estimate herself.

### Launch

Read the Overview aloud. Stop at "cursor hovering between the two candidate builds, the review
meeting nineteen minutes away." Ask the room: "Before you've computed a single volume, which
sounds like the safer engineering choice — the cheaper test, or the tighter fit? Why?"

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "Keep the bounding sphere or switch to a bounding capsule — show of hands."
Record the split.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push the room past "which shape is cheaper to test" toward "how do we combine a compute-time cost
and a wasted-space cost into one comparable number." Let the room sit with the fact that these are
two genuinely different kinds of cost (CPU time vs. rendering time) that Appendix D's MA9 is what
lets you add together at all.

### Anchor 3 — WHAT IS THE PROCESS?

Get the room to state the actual comparison method out loud before touching numbers: compute each
prop's real volume and surface area (D1), then each prop's bounding sphere and its waste (D2), then
each prop's bounding capsule and its waste (D3), then convert both to a total per-frame millisecond
cost using Appendix D (D4), then compare.

### Anchor 4 — WHAT DON'T WE KNOW?

Name the load-bearing unknowns explicitly: every cost figure in Appendix D (MA7, MA8, MA9) and the
scene's own prop counts (MA6) are stated assumptions, not measured facts — only the lamppost's
height range and the pipe's diameter are real, cited figures. "Which of these assumptions would
you most want to challenge, and why?"

### Data Deep Dive

Now open Appendices A–D. Run D1–D5 as a room, or have groups each take one prop.

### Twist

Once D4's base-case totals are on the table (A=3.063ms, B=2.706ms, B wins), reveal that MA9 has no
real source behind it and ask Socratic Question 3 directly. Let the room discover the flip.

### Close

VOTE AGAIN. "Did the vote move? For the people who didn't move, what would it take to change your
mind?"

### Lessons Learned

The core transferable idea: a bounding shape's *fit* (how much empty volume it wastes) can matter
far more than its *test cost* — but only once you have a way to convert "wasted volume" into the
same units as "compute time," and that conversion is often the real, unstated assumption doing all
the work. A second, equally real lesson: the same volume formula (sphere) can show up as both an
option's whole shape (A) and a hidden component of the other option's shape (B's hemispherical
caps) — geometry doesn't disappear just because you switched bounding shapes.

### Standards Touched On

How to find the surface area of a pyramid; how to find the surface area of a cylinder; how to find
the volume of a pyramid; how to find the volume of a cylinder; how to find the volume of a cone;
how to find the volume of a sphere.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold read of the Overview, gut-check vote (Anchor 1) — no numbers shown yet |
| 3:00–8:00 | Position defense: "Convince us your bounding-shape policy is right, not just that it sounds cheaper or tighter" |
| 8:00–20:00 | Data Deep Dive — compute D1's three prop volumes/surface areas and D2/D3's bounding-shape volumes as a room |
| 20:00–30:00 | Compute D4's full per-frame cost for both options; confirm the margin and where it comes from |
| **30:00** | **DROP THE TWIST** — reveal MA9 has no real source and ask Socratic Question 3 |
| 30:00–38:00 | Pressure-test the case's assumptions: which of MA7/MA8/MA9 would a defensible challenge actually flip? |
| 38:00–45:00 | Close, re-vote, lessons learned |

## Cohort bands (SPEC Section 7, cohort-bands subsection)

| Band | Typical size | What changes |
|---|---|---|
| **Full (12–20)** | the size this case is written for | Anchors and the 45-minute timed plan run as written above |
| **Compressed (6–11)** | smaller room | Anchors 2–3 combine into one pass; the 20:00–30:00 three-prop geometry build-out runs as a single worked example (one prop, not all three) instead of small-group work; total runtime shortens proportionally |
| **1:1 / pair (1–2)** | tutoring context | No vote at Anchor 1 — a stated initial position instead; facilitator plays devil's advocate directly; the 30:00–38:00 sensitivity pressure-test still runs in full |
