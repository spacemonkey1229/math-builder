# Facilitator Guide — Creek Span

**Status: RESEARCHED.** Real, cited numbers below (case.json `sources[]`, `derived`).

**Case:** Creek Span · **Tier:** T2 · **Band:** MS-core · **Studio:** Heroes Academy
**Standards:** see `case.json.standards[]` for the exact ids (10 skills — Triangle,
Triangle Inequality Theorem, Acute Triangle, Obtuse Triangle, Equilateral Triangle, Scalene
Triangle, Leg, and the multiply/divide-decimals and percent-of-a-number "how to…" skills)

## Intro

Frame the format: a real professional dilemma, not a worksheet with a story stapled on. Name
the opener — "One engineer, one pallet of free salvage steel, and a shop that starts cutting new
steel at four o'clock whether Suri has an answer or not." Worth naming for the room: Suri grew up
in this town and crossed the old footbridge over this same creek every school morning as a kid —
she can still name the exact board that used to give under her sneaker and never broke, and as a
kid she decided that wobble meant the bridge was alive, not failing. She still carries a tape
measure in her bag out of that same habit, even to meetings where she'll never need it — but she's
a by-the-book engineer first, and the case is about whether that sentimentality gets anywhere near
her actual recommendation (worth pointing out to the room: her own answer to "is a flex a failure?"
is exactly the kind of judgment call D2's Triangle Inequality check forces onto solid ground).

## Launch

Read the Overview aloud, then the first paragraph of Background — the county wants to reuse the
salvage pile, and a triangle is the only shape that can't rack under load — with no Appendix
numbers shown yet. Ask: "Just from what you've heard — does 'free steel is free steel' sound like
it settles this, or not?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"The Warren Line or The Low Line?" Show of hands, no discussion yet. Record the count — Close
asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What does 'fits' actually mean here?"**

Push on what "the salvage fits" means. Fits by eye? Fits because two pieces laid end to end
roughly cover the panel? Or fits in the one sense that actually matters to a shop drawing — two
3.5-ft members physically closing a real triangle at the top-chord node? Let the room sit in the
ambiguity: "Is anyone courageous enough to say exactly what 'fits' has to mean before we start
measuring?"

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has a working definition of "fits," ask them to name the actual steps: check the
Triangle Inequality Theorem for both panel lengths, classify each option's triangles, then run
the full D5 takeoff — chord weight, new-steel diagonal weight, joint count, total cost, cost per
foot of the 24-ft span. Re-ask: "Given how we just defined 'fits' — is checking the geometry
first, before any dollar figure, still the right order to do this in?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix F's one Modeling Assumption (MA1 — 1.5 shop labor hours per gusset joint) out
loud before anyone computes a total cost. Ask the room whether they think a single labor-hour
estimate could actually move the final answer. (Facilitator note: it can — that's exactly what
the Twist tests — but let the room guess first.)

## Data Deep Dive

Now, and only now, the numbers. Walk D2 and D5 together as a room: first the Triangle Inequality
check for both panel lengths, then the full fabrication takeoff.

**The trap:** most Heroes read "free salvage steel" in the Background and jump straight to
totaling material savings for The Low Line, without first checking whether The Warren Line could
use the same salvage — it can't (3.5 + 3.5 = 7 < 8, a hard geometric wall, not a cost one). A
second, subtler version of the same trap: Heroes who do catch the salvage-fit issue often stop
there and declare B the winner on "free steel" alone, without carrying through that B's shallower
depth also raises its chord steel weight and adds two extra gusset joints — costs that can partly
or fully erode the diagonal-steel savings. Cold-call on this specifically: "You just proved the
salvage doesn't fit Option A. Does that alone make Option B the cheaper truss — or do you still
have to run the whole takeoff to find out?"

## Twist — drop this at roughly the 15-minute mark

Deliver slowly, with pauses:

"A text arrives from the fabrication sub. He's looked at The Low Line's shop drawing and thinks
two of its nine panel points — the two closest to the sway braces — can be combined into a single
doubled field connection instead of two separate gusset welds. It's a real technique, and it would
cut The Low Line's effective joint count from 9 to 8."

*"You have 60 seconds. Does this change your recommendation to the county?"*

**Facilitator-only.** Recompute Option B live with the room using `sensitivity_model.py`'s
`evaluate_twist()`: dropping one joint cuts The Low Line's labor cost, moving its cost per foot
from $24.91 to $23.02. The winner does not flip — The Warren Line is still cheaper, $21.22/ft vs.
$23.02/ft — but the margin drops from 14.81% to **7.84%**, roughly half of what it was.

Follow-up: **"What just broke in your model? Were you wrong, or just missing information — and how
confident should Suri actually be in her recommendation now?"** A Hero who declared A the clear
winner has to reckon with how much of that "clear" was really doing the work of a single
unverified labor-hour estimate (MA1).

**Twist soundness check (SPEC §6):** checked against every stated Background/Appendix fact and
Modeling Assumption, read both sequentially and simultaneously — it introduces no new figure that
contradicts an earlier one, only a real fabrication technique applied to a joint count already in
front of the room. `sensitivity_model.py`'s `evaluate()`/`evaluate_twist()` confirm the winner is
unchanged and the margin genuinely narrows (base: A by 14.81%; twist: A by 7.84%).

## Immediate recommit

Re-vote immediately. "Did the twist change your hand — or did it just change how sure you are
about it?"

## Close

Re-vote once more after full discussion. Ask: "Did we ask the right question at Anchor 2, or did
'fits' turn out to mean something more specific than we first said?" And: "What math was new to
you today, and how did you attack it?"

## Lessons Learned

The Background's own framing — "free steel is free steel" — turns out to be the entire trap, once
the geometry and the takeoff are both run honestly. The transferable lesson: **a material being
free does not make it usable, and a design that uses free material is not automatically the
cheaper design.** The Triangle Inequality Theorem is a hard yes/no gate that has nothing to do
with cost, and once past that gate, a design's total cost is still decided by everything else that
changes with it — chord weight, panel count, joint count — not by the one line item that changed
to zero.

## Five Socratic Questions

Use these across Anchors 2–4 and the Data Deep Dive — each is answerable only with this case's own
numbers, not general opinion.

1. The county's pitch was "free steel is free steel" — so why can't The Warren Line use any of it at all? What has to be true about three lengths for them to even form a triangle, and which one of the three did the salvage pieces fail?
2. The Low Line reuses eight salvage pieces and still comes out with a heavier total chord section than The Warren Line. If the diagonals are "free," why does the chord section change at all — what is the actual mechanical reason a shallower truss needs a heavier chord?
3. Every triangle in The Warren Line is equilateral. Does that automatically make it acute, or would you need to check the angles separately to be sure? What's the fastest way to know without measuring?
4. The Low Line's interior triangle and its end triangle share one side length (3.5 ft) and one panel width. Why is one isosceles and the other scalene, when they look almost the same on the elevation?
5. The Warren Line wins by 14.81% — and $21.22 vs. $24.91 per foot is not a landslide. If the gusset-joint labor estimate (1.5 hours) were wrong, which direction would it have to be wrong, and by how much, before The Low Line actually became the cheaper option?

## Standards Touched On

See `case.json.standards[]` (10 ids) for the full list. In brief: Triangle, the Triangle
Inequality Theorem, Acute/Obtuse/Equilateral/Scalene Triangle, Leg, and the multiply-decimals,
divide-decimals, and percent-of-a-number "how to…" skills that drive the D5 fabrication takeoff.

## Cohort Bands

See `case.json.cohort_bands[]`.

- **Full (12–20):** Socratic plan and anchor timings run as written below.
- **Compressed (6–11):** Anchors 2 and 3 combine into one pass; run only one deep-conflict thread
  (geometry-fit vs. full-cost) instead of both. The twist still drops at 15:00. Total runtime
  ~30 min.
- **1:1 / pair (1–2):** No vote at Anchor 1 — the learner states an initial position instead. Skip
  the deep-conflict threads; go straight from twist-recommit to Close.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote (Anchor 1) — no explanation |
| 3:00–10:00 | Position defense: "Convince us it's buildable, not just cheaper" (Anchor 2) |
| 10:00–15:00 | Pressure-test the models: run the Triangle Inequality check together, then start the D5 takeoff (Anchor 3, Anchor 4, start of Data Deep Dive) |
| **15:00** | **DROP THE TWIST** — the fabrication sub's joint-combining call, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses, and how confident are they now? "What just broke?" |
| 20:00–30:00 | Threaded deep conflict — two named threads: (1) "the salvage doesn't fit A" vs. "does that alone make B the winner?" as competing readings of the geometry; (2) up-front material savings vs. the full labor-and-chord-weight cost as competing definitions of "cheaper" |
| 30:00–45:00 | Close, re-vote, reflection, Lessons Learned |

## The margin

**Basis:** total fabricated cost (chord steel weight × price/lb + new-purchase diagonal/brace
steel weight × price/lb + gusset joint count × labor hours/joint × wage rate) ÷ 24-ft span,
computed in `sensitivity_model.py` from Appendix A (angle weights, S1-S3), Appendix D (steel
price, S4), Appendix E (takeoff quantities), and Appendix F (MA1, joint labor hours).

**Value: The Warren Line (A) wins by 14.81%** ($21.22/ft vs. $24.91/ft). The margin is driven
almost entirely by the two extra gusset joints, not by material — a fact most Heroes will not
expect walking in, given how prominently "free salvage steel" features in the Background.

## Sensitivity note

MA1 (gusset-joint labor hours, 1.5 hr/joint) is the case's only stated modeling assumption and the
only cost driver not fixed by sourced or given data. Flexed ±50% in `sensitivity_model.py`
(Tier 2 probe 5), the margin ranges from 10.99% (0.75 hr/joint) to 16.70% (2.25 hr/joint) — The
Warren Line wins across the entire flex range, so MA1 does not flip the verdict, but it does move
the margin by roughly ±6 points around the base 14.81%. Appendix D's steel price (S4, MEDIUM
confidence, derived from an industry blog's stated range rather than a single named index) is the
case's softest *sourced* figure, but because it scales both options' material cost by the same
factor it is not independently dilemma-flipping.
