# Facilitator Guide — The Absorption Call

**Content note (SPEC subject-matter guidance):** none of the corpus's heavier-weight triggers (illness, death, money
stress, family hardship) apply here. This is a straightforward professional-decision case.

## The balance argument (answer-key content — do not hand to Heroes)

**Argument for A (The Dead Wall).** Option A drives Hollow Oak's rear wall to a broadband
absorptive NRC of 1.05, bringing the whole room's RT60 to roughly **1.00 s** against a **1.05 s**
target for the theater's dominant, season-majority use (speech and amplified shows) — a ratio of
about **0.95**, within roughly 5% of that target. It is the tightest, most defensible fix for the
exact complaint Dana raised in the Overview.

**Argument for B (The Scatter Wall).** Option B brings RT60 to roughly **1.64 s** against a
**1.6 s** target for the unamplified acoustic series — a ratio of about **1.02**, similarly close
to *its own* target — while leaving the room roughly 60% livelier than Option A for a use the room
would otherwise fail outright. It trades a small amount of precision on the season-majority use for
solvency on the minority use.

**The margin.** `margin_pct ≈ 2.3` (per `sensitivity_model.py`'s closeness-score metric, base case)
— both options land close to their own target ratio of 1.0; neither wins by anything close to
SPEC §2's 20% cap in the base case. This is intentional: the case is not "A is right and B is a
worse version of A" — it is two different, each individually well-executed answers to two
different questions, and the real fork is *which question the room should be optimized for*, not
who did the math better.

**Verdict stability — disclosed, not eliminated.** Because both options are tuned close to their
own targets, the *closeness comparison itself* is not robust to the case's two disclosed
assumptions (MA2, the diffusive coefficient; MA3, the music target): `sensitivity_model.py`'s
±50% flex sweep flips which option scores marginally higher in every one of its four rows (see
`case.json.sensitivity_disclosure[]`, both Category X — a documented good-faith estimate standing
in for a real citation that does not publicly exist). **This is the correct, honest shape of this
case, not a defect to hide**: the case's actual teaching point is that Option A's number is solid
ground (it depends on no disclosed assumption) while Option B's number rests on a real, named
unknown. A guide should surface this directly — "notice that only one side of this argument is
standing on a number nobody had to guess" is itself a legitimate discussion thread, not a spoiler.

**The trap (primary — mechanical, catches it first).** D1/D2 require converting square-foot areas
(Appendix A/B, given in feet) into square meters for Sabine's equation. A hurried Hero who
correctly converts the *linear* room dimensions in D1 (multiply by 0.3048) will often carry that
same linear factor straight into D2's *areas* instead of squaring it (1 ft² = 0.3048² ≈ 0.0929 m²,
not 0.3048 m²) — a roughly 3.3x systematic overstatement of every surface's area. This error is
dangerous precisely because it is **internally consistent**: every sabins figure, every RT60, and
every ratio downstream is wrong by the same multiple, so nothing looks asymmetric or obviously
broken, the units label still correctly says "m²," and the mis-scaled numbers can even look *more*
dramatic in a way a hurried Hero reads as confirmation rather than a red flag. It compounds into D3
if the (wrongly-scaled) metric wall area is then mixed with the $/ft² cost rate without converting
back — an error the case's own cost budget ($50,000, comfortably above either option's real cost)
is generous enough to hide, since a wrong cost still clears the budget check either way. **Ask for
the area-conversion arithmetic explicitly, in square meters, before accepting any RT60 figure** —
this is the fastest way to catch it, and it is the trap most likely to actually catch a room, ahead
of the one below.

**The trap (secondary — conceptual, catches whoever gets past the first one).** Heroes will often
reach for total-price or coefficient-size comparisons ("1.05 is way bigger than 0.48, so A is
obviously more effective") and stop there, missing that "more effective" isn't the actual metric —
the metric is *closeness to the target RT60 for the use a given option is meant to serve*. A Hero
who computes only Option A's ratio and declares victory has not actually evaluated Option B on its
own terms. The third-order trap: some Heroes will assume "dominant use" settles the question by
itself (majority of the calendar = majority of the weight), without asking whether "majority of
shows" is actually the right proxy for "what the room must be good at" — which is exactly what the
Twist below pressures.

## Five Socratic questions

1. Option A's ratio (≈0.95) is closer to 1.0 than Option B's ratio (≈1.02, using its own target) — does that make Option A the mathematically better choice, or the better choice for a *different question* than the one Option B is answering?
2. If Hollow Oak's amplified season were twice as long as its acoustic series, would that change which target RT60 should count as "the room's dominant use," and would it change your recommendation?
3. MA2 sets the diffusive panel's absorption coefficient at 0.48 out of a stated 0.25–0.55 range — if the true value were at the low end of that range instead, what would happen to Option B's RT60, and would your recommendation survive that?
4. Both options fit inside the board's $50,000 budget — if cost were not a constraint at all, does anything about the underlying math change?
5. The theater treats only the rear wall in both options — what would have to be true about the *other* surfaces in the room for treating just one wall to be enough to hit either target?

## Twist (SPEC twist guidance)

At roughly the 15-minute mark: **Dana emails Marcus that the theater just added a third,
previously unconfirmed booking — a string quartet doing an unamplified holiday concert — to the
same month as the rock trio's amplified run.** The acoustic (non-amplified) portion of the
calendar, which most Heroes will have treated as a minor secondary use, is now roughly as large as
the amplified portion for that stretch of the season. Nothing about the computed RT60 values
changes — the physics is exactly what it was — but the framing that let Heroes call one use
"dominant" and the other "secondary" just got shakier.

**Follow-up:** *"What just broke in your original model? Was your math wrong — or was it your
assumption about which use counts as 'dominant'?"* The distinction is the transferable skill: the
Sabine calculation was never in question; the weighting of *which target to chase* was.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote for A or B — no explanation yet. |
| 3:00–10:00 | Position defense: *"Convince us why it's better, not just fair."* |
| 10:00–15:00 | Pressure-test the models: *"Whose plan is most fragile if the diffusive coefficient (MA2) is wrong?"* |
| **15:00** | **DROP THE TWIST** — the string-quartet booking — delivered slowly, with pauses. |
| 15:00–20:00 | Immediate recommit: who reverses? *"What just broke?"* |
| 20:00–30:00 | Threaded deep conflict — two named threads: (1) precision-for-the-majority-use vs. solvency-for-the-minority-use; (2) is "dominant use" actually the right proxy for "what the room must be good at," now that the calendar is closer to even? |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned. |

## Guide Notes — the anchor ladder

### Intro

Frame the format (case study, binary decision, 45 minutes); name the opener (the claim-and-echo
moment from the Overview).

### Launch

Read the Overview aloud, or better, clap once in the room and let the silence sit before
continuing, to give Heroes the same sensory cue Marcus gets.

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. *"Is anyone courageous enough to stand with the Dead Wall? With the Scatter
Wall?"*

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

*"Is this the right question? What do you mean by 'boomy'?"* Let confusion grow before resolving
it: reverberation time isn't loudness, and a short RT60 isn't automatically "better" everywhere.

### Anchor 3 — WHAT IS THE PROCESS?

*"If we go through this process and find the data, how will we decide?"* Re-ask: *"Is our question
still the right question?"*

### Anchor 4 — WHAT DON'T WE KNOW?

*"Do we need to make assumptions? Which ones are critical?"* Surface MA2 (diffusive coefficient)
and MA3 (music target) here, before the Data Deep Dive.

### Data Deep Dive

Now, and only now, Appendices A–D.

### Close

VOTE AGAIN. *"Did we ask the right question? What math was new to you, and how did you attack
it?"*

### Lessons Learned

Sabine's equation turns a subjective complaint ("boomy") into a number; but the *choice of target*
the number is measured against is itself a judgment call, and that judgment call is where the real
decision lives.

### Standards Touched On

Volume; Surface Area; How to convert an amount with compound units; How to find the surface area
of a prism; How to find the volume of a prism.

## Sensitivity note

MA2 (diffusive panel absorption coefficient, α = 0.48) and MA3 (unamplified-music target, 1.6 s)
are the two assumptions that move Option B's own score. `sensitivity_model.py` flexes each ±50%
and finds the *base-case* margin (≈2.3%, well under SPEC §2's cap) does **not** survive that flex —
every one of the four swept rows shows Option A's fixed, assumption-free score overtaking Option
B's. This is disclosed, not eliminated: `case.json.sensitivity_disclosure[]` records both
parameters as Category X (a documented good-faith estimate standing in for a real citation that
does not publicly exist), per `skills/case-readiness/SKILL.md`'s disclosure-aware Tier 2 pass
state. The honest framing for a guide: **Option A's number does not depend on anything Marcus had
to guess; Option B's number does.** That asymmetry is real content for the discussion, not a flaw
to paper over. See `sensitivity_model.py` and `QA_REPORT.md` for the recorded run.
