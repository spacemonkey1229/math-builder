# Guide Notes: Vent Cap

**Case:** Vent Cap · **Tier:** T2 · **Band:** MS-core · **Studio:** Heroes Academy
**Standards:** Geometry / Visual Perceptibility (partial) + Geometry / Fundamentals Of Geometry
(Congruent duplicate) — all `new_coverage` (see `case.json.standards[]` for the exact ids)

Researched and margin-resolved 2026-08-12 (`margin_pct` = 11.98, see `sensitivity_model.py`). This
file is re-checked for drift at every readiness run (the continuity checks in `case-readiness`).

## Intro

Frame the format before anything else: this is a real cost decision, not a worksheet. Name the
opener — "You are a nesting engineer. You have thirty minutes before the afternoon cutting run
locks in, and your supervisor wants the right answer, not just an answer." Let the stakes land
before moving to the Launch.

## Launch

Show both flat-pattern layouts side by side (the same pair described in the Overview) with no
prices labeled — just the shapes on the sheet. Ask: "Which one do you think is cheaper to run,
just from looking at it?" Do not confirm or correct answers here. The point is a gut read before
anyone touches a calculator.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Mara on The 3-Panel Fold — the one that looks less
tightly nested?" Show of hands, both options, no discussion. Record the count — Close will ask
them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'cheaper'?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which one
nests tighter," but the real question has two separate legs that pull in different directions:
material cost (driven by sheets, which favors A) and labor cost (driven by seams, which favors B).
Push on it: "Mara isn't pricing one number. She's pricing two, and they move opposite ways. What
are they?" If the room lands on "material vs. labor" on its own, the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has split "cost" into its two legs, ask them to name the actual steps before
touching the appendices: correctly identify the shape and its faces/edges (D1), understand each
layout's net well enough to trust the seam count (D2), price the material (D3), price the labor
(D4), total both and compare (D5). Re-ask: "Is our question still the right one, now that we can
see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gaps honestly: Appendix E's three Modeling Assumptions (MA1 the per-seam labor
cost, MA2 the caps-per-sheet nesting results, MA3 the Twist's steel-price scenario) are all
stated, not sourced — no public "real factory nesting result" database exists for this specific
authored part. Ask which one actually changes the recommendation if it moves (MA1 — see Data Deep
Dive), and which one is fixed by the geometry, not assumed (the seam counts themselves, 4 vs. 3,
follow directly from the panel counts, not from a separate assumption).

## Data Deep Dive

Now, and only now, the numbers. Walk D1's face/edge count, D2's net description and congruence
check, D3's material cost, and D4's labor cost together as a room, cold-calling for D2's
congruence verification specifically — this is where a Hero who never actually worked out the
slant-edge length (using the base half-width and the slant height) will visibly struggle, which is
useful information for the facilitator, not a moment to rescue.

**Facilitator-only geometry note.** The vent cap is open-bottomed, so it has exactly **4 faces**
(the triangular sides only — no base face) and **8 edges** (4 base edges where the shape meets the
roof, plus 4 slant edges where adjacent faces meet and get welded). A Hero who counts a base face
or forgets the base edges will get D1 wrong in a way that quietly breaks D2's seam-length logic
too, since the seam length is computed from the slant edges specifically.

**Facilitator-only cost note.** Option A: 5 sheets ($341.95) + 280 seams ($840.00) = **$1,181.95**.
Option B: 6 sheets ($410.34) + 210 seams ($630.00) = **$1,040.34**. Margin: **11.98%**, Option B
cheaper. The single biggest lever is MA1 (the $3.00/seam labor rate) — flexed ±50% the margin
holds between 4.80% and 15.39%, Option B stays cheaper throughout. This is a genuinely stable
result, not a coin flip dressed up as a dilemma — the real tension is that the number the nesting
software puts front and center (caps per sheet) is not the number that actually decides the job.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"It's the middle of the discussion. Mara's phone buzzes. A new tariff on imported steel just hit
the news — her supplier is raising sheet prices 40%, effective this week."

"Does the extra sheet Option B needs suddenly matter more than it did five minutes ago?"

**Facilitator-only: what the numbers actually do.** At a 40% steel price spike ($68.39 →
$95.75/sheet), Option A rises to $1,318.73 and Option B rises to $1,204.48 — Option B is **still
cheaper**, but the margin narrows from 11.98% to **8.66%**. **The twist does not flip the verdict;
it erodes it.** Do not hand this reasoning over unprompted; let a Hero who did D3 carefully reason
toward it — the material line item is the one this twist actually touches, and a Hero who
understands *why* (labor cost is untouched by a steel-price change) is giving the strongest
possible answer.

## Immediate recommit

Re-vote immediately. Ask by name: "Does the tariff change your vote, or just how close you think
this call actually is?" That distinction is the transferable skill, not the vote itself.

## Deep conflict — three threads (20-30 min)

1. **The number that looks decisive isn't.** Caps-per-sheet is the number nesting software
   reports first, and it points the wrong way. Is that a flaw in the software, or a reminder that
   the headline number is never automatically the decision number?
2. **A "small" design change, multiplied.** One fewer weld seam per cap sounds minor. Why does it
   end up mattering more than an entire extra sheet, 70 times over?
3. **Whose $3.00.** MA1's per-seam cost is derived from a wage and a time estimate, not quoted
   from a price list. Is a *derived* number as trustworthy as a *quoted* one — and what would
   change your mind either way?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both layouts, cold-call for a gut read, no formulas yet |
| 3:00–10:00 | Position defense — *"Convince us the tighter nest isn't automatically the cheaper job"* |
| 10:00–15:00 | Pressure-test the models — *"Whose cost number is most fragile?"* |
| **15:00** | **DROP THE TWIST** — the steel tariff, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (the misleading headline number; a small change multiplied; whose $3.00) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes will look at "14 caps/sheet vs. 12 caps/sheet," conclude the tighter nesting must be
cheaper, and stop — treating material as the whole cost story because it's the number the nesting
software puts front and center. Watch for a pitch that reports caps-per-sheet and never prices out
the seams — it has not actually costed the job.

## Socratic questions

1. Option A wins on material (fewer sheets) and loses on labor (more seams). Which line item actually decides this job — and would a shop owner watching only the steel budget have gotten the wrong answer?
2. D2 asks you to verify every weld seam in the cap is the same length. Why does that matter to whoever's running the weld cell, not just to the person doing the geometry?
3. MA1's $3.00/seam is derived from a wage and a time estimate, not quoted from a price list. What would you want to see before you trusted it — and what happens to the verdict if a seam actually takes twice as long?
4. The 3-Panel Fold needs one panel with an awkward, less-efficient shape to save one weld. Is there a batch size small enough that this trade stops being worth it?
5. Mara has thirty minutes. What does she tell her supervisor — and does the tariff change the answer?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that didn't
move at all after the twist is worth asking about directly: did the twist not land, or did the
room already understand how thin the margin was?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether D1's face/edge count (open-bottomed, no base face) was where most Heroes actually got
  stuck, versus the more mechanical D3/D4 arithmetic.
- Whether the "headline number points the wrong way" trap landed as a genuine surprise or felt
  telegraphed by the case's own framing.
- Whether the twist's "material moves, labor doesn't" distinction produced real reasoning or just
  a recalculation.

## Standards Touched On

Congruent (Fundamentals Of Geometry) · Face · Edge · Pyramid · How to draw the net of a 3-D shape ·
How to name a 3-D shape

## Facilitator note — sensitivity

None required (SPEC §6) — the stakes here are a production deadline and a job-costing decision,
not personal loss or hardship.
