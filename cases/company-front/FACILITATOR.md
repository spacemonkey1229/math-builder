# Guide Notes: Company Front

**Case:** Company Front · **Tier:** T3 · **Band:** MS-stretch / HS-entry · **Studio:** Heroes Academy
**Standards:** Geometry / Transformations — the remaining 9 skills, closing the group entirely
(see `case.json.standards[]` for the exact ids)

Researched and margin-resolved 2026-08-12 (`margin_pct` = 9.84, see `sensitivity_model.py`). This
file is re-checked for drift at every readiness run (the continuity checks in `case-readiness`).

## Intro

Frame the format before anything else: this is a real deadline, not a worksheet. Name the opener —
"You are the assistant drill designer. The charts go to the printer at nine tomorrow morning, and
your head designer just texted asking if the math works out." Let the stakes land before moving to
the Launch.

## Launch

Show both taped-up transitions side by side (the same pair described in the Overview) with no
numbers labeled — just the shapes. Ask: "Which one do you think is riskier to actually perform,
just from looking at it?" Do not confirm or correct answers here. The point is a gut read before
anyone touches a calculator.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Mara on The Expand — the dramatic one?" Show of hands,
both options, no discussion. Record the count — Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'riskier'?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which one moves
less," but the real question is sharper: *does either option require a step size a real performer
cannot execute?* Push on it: "Mara isn't asking 'which is smaller.' She's asking whether one of
these breaks a real physical limit. What's the limit?" If the room lands on "there's a real ceiling
in inches per step, and we need to check against it" on its own, the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has the right question, ask them to name the actual steps before touching the
appendices: check The Block's own symmetry (D1), work out The Expand's travel and step size (D2),
work out The Mirror Turn's (D3), classify each result as congruent or similar (D4), check the
rejected 180° pivot (D5), then compare against the real ceilings (D6). Re-ask: "Is our question
still the right one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gaps honestly: Appendix E's three Modeling Assumptions (MA1 the scale factor,
MA2 the count budget, MA3 why the 180° pivot was rejected) are all stated, not sourced — no public
drill chart exists for this fictional show. Ask which one actually changes the recommendation if
it moves (MA1 and MA2 both are — see Data Deep Dive), and which one doesn't (MA3 — it was never
actually competing on the numbers).

## Data Deep Dive

Now, and only now, the numbers. Walk D1's symmetry proof, D2's dilation, D3's rotation, D4's
congruent/similar classification, and D5's rejected pivot together as a room, cold-calling for D2's
reverse scale-factor step specifically — this is where a Hero who only memorized "multiply by the
scale factor" rather than understanding what a scale factor *is* will visibly struggle, which is
useful information for the facilitator, not a moment to rescue.

**Facilitator-only geometry note.** D3's comparison question (does rotating the other direction
change the answer) has a clean answer that D1 already gives away: because The Block is symmetric
about the Y-axis (and, by inspection, about the X-axis too — a 3×3 grid centered at the origin has
both), rotating 90° CW or CCW produces the same SET of nine points, just relabeled — so the
*farthest-traveling marker's distance* is identical either direction. A Hero who re-derives all
nine coordinates a second time to answer this isn't wrong, just slower than one who reasons from
symmetry — both are valid, but the second is the stronger answer.

**Facilitator-only cost note.** Option A (The Expand): 27.05 in/step at 16 counts — over the real
22.5 in/step comfort standard, but with **9.84% headroom** under the real 30 in/step aggressive
ceiling. Option B (The Mirror Turn): 11.25 in/step — nowhere near either ceiling, by the geometry
of rotating a compact formation about its own center (a rotation can never move a point farther
than a chord of its own circle, and every marker here starts close to center). This is not a coin
flip on the numbers — Option B is *always* going to be cheaper than a large dilation, structurally,
and it's stronger than that: for a dilation by scale factor S about the shared center, each
marker's travel is (S−1)·r; for *any* rotation about that same center, at *any* angle, travel tops
out at 2·r (only at a full 180°). Since this case's S=4.4 gives (S−1)=3.4 > 2, **Option A cannot
beat any possible rotation of The Block about its own center on raw travel — not just this specific
90° Mirror Turn.** If a sharp Hero notices this and asks "then why is this even a real choice,"
the honest answer is that the two options aren't actually competing on the same axis: The Mirror
Turn structurally cannot deliver a full-field spread (a rotation never changes the formation's
footprint), which is the entire reason The Expand exists. The real tension is qualitative — is the
visual worth executing a design with under 10% real margin to spare? Don't let a Hero present "B is
numerically safer" as if it settles the case — that's true and also not the interesting question.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"It's the middle of the discussion. Mara's phone buzzes again. The music arranger just cut the
ballad's bridge by two counts to tighten the pacing — count 88 to 104 is now count 88 to 102.
Sixteen counts just became fourteen."

"Mara has until the end of rehearsal tonight to tell the head designer whether The Expand still
works."

"Does it still clear the ceiling? What changed, and by how much?"

**Facilitator-only: what the numbers actually do.** At 14 counts instead of 16, Option A's required
step size rises from 27.05 to **30.91 in/step — over the real 30 in/step aggressive ceiling.** This
is not a close call anymore; it is a design that no longer works as drawn. **The twist flips the
verdict**, and it does so with real arithmetic, not narrative hand-waving: the same travel distance
divided by two fewer counts is enough to cross a real physical limit that had under 10% headroom to
begin with. This is the payoff of D6's ceiling framing — a margin that looked "fine" was never far
from a cliff. Do not hand this number over unprompted; let a Hero who did D2/D6 carefully reason
toward it, and treat one who says "the margin was already thin, so a small change was always risky"
as the strongest possible answer — stronger than one who is simply surprised.

## Immediate recommit

Re-vote immediately. Ask by name: "Does the count cut change your vote, or does it change what you
wish you'd asked for from the start?" That distinction is the transferable skill, not the vote
itself.

## Deep conflict — three threads (20-30 min)

1. **A margin that looked fine wasn't far from a cliff.** Option A cleared the ceiling by under
   10% before anything went wrong. Is a "passing" number that thin actually a pass, or should Mara
   have flagged it as risky even before the twist?
2. **Congruent vs. similar, and why a performer should care.** D4 asks for a geometry term, but the
   real-world stakes are different: a congruent (rotated) formation asks every performer to cover
   roughly the same ground; a similar-but-not-congruent (dilated) formation asks outside performers
   to cover far more than inside ones. Is that a fairness question, not just a vocabulary question?
3. **The 180° pivot was cut for staging, not math.** Is that a legitimate way to eliminate an
   option in a case that's supposed to be about the numbers — and does it matter that the math
   would have worked fine (15.91 in/step, comfortably under both ceilings)?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both taped-up transitions, cold-call for a gut read, no formulas yet |
| 3:00–10:00 | Position defense — *"Convince us the visual is worth a margin this thin"* |
| 10:00–15:00 | Pressure-test the models — *"Whose step-size number is most fragile?"* |
| **15:00** | **DROP THE TWIST** — the two-count music cut, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (thin margins; congruent vs. similar; the 180° pivot) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes will compute The Expand's step size, see it clears the real 30 in/step ceiling with
room to spare, and assume the design is settled — missing that a 9.84% margin at 16 counts is one
late music edit away from disappearing entirely: a single cut count doesn't just tighten the
margin, it can erase it completely. Watch for a pitch that reports one step-size number, calls it
"safe," and never asks what happens if anything about the design changes.

## Socratic questions

1. Option A clears the real ceiling with under 10% headroom to spare. Is "it clears the ceiling" the same thing as "it's safe"?
2. D3 asks whether rotating the other direction changes the farthest travel distance — what did D1's symmetry proof already tell you about the answer, before you did a single extra calculation?
3. D4 asks you to call each option's result congruent or similar to the start. Why does that distinction matter to a performer, not just to a geometry teacher?
4. The 180° pivot was rejected for a staging reason, not a math reason, even though the math would have worked fine. Is that a legitimate way to eliminate an option in a case that's supposed to be about the numbers?
5. Mara's text back to the head designer has to be one sentence. What does she say — and does the twist change it?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that didn't
move at all after the twist is worth asking about directly: did the twist not land, or did the room
already understand how thin the margin was?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether D2's reverse scale-factor step (recovering the scale factor from one marker's
  coordinates) was where most Heroes actually got stuck, versus the more mechanical forward
  dilation.
- Whether the symmetry shortcut in D3 (reasoning from D1 rather than re-deriving all nine
  coordinates) was discovered independently or needed a nudge.
- Whether the twist's "the margin was already thin" framing produced real reasoning about what a
  thin margin means, or just surprise that the number changed.

## Standards Touched On

Congruent · Similar · Dilation · Scale Factor · How to reflect a figure across the Y-Axis · How to
rotate a figure on the coordinate plane 90 degrees counterclockwise · How to rotate a figure on the
coordinate plane 180 degrees · How to dilate a figure on the coordinate plane given a scale factor ·
How to find the scale factor of a dilation

## Facilitator note — sensitivity

None required (SPEC §6) — the stakes here are a design deadline and a performance-execution risk,
not personal loss or hardship.
