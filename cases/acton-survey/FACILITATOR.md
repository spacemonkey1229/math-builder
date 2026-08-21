# Guide Notes: Acton Survey

**Case:** Acton Survey · **Tier:** T4 · **Band:** MS-stretch/HS-entry · **Studio:** Launchpad
**Standards:** see `case.json.standards[]` for the exact ids (22 skills — sampling/probability
vocabulary, combinations, percent, proportion, rounding, time, basic arithmetic, and two required
visual displays)

Legacy conversion, 2026-08-20, built from the original case study docx
(`source/Y2/Session 5/Acton Survey/Case Study_ Acton Survey.docx`, `Guide Notes.docx`, and the real
2021 roster xlsx) onto the current 11-anchor ladder. Jeff and Laura's retirement, Xander's role,
the 15–20-min call constraint, and the "at least two studios" eligibility rule are preserved
verbatim from the source. The dilemma is narrowed from the original's 5 options to 2, per
`cases/_concepts/LEGACY_DILEMMA_LOCKS_2026-08-20.md` — see `case.json.legacy_conversion_note` for
the full account.

**A note on content (SPEC §6):** this case is low-stakes emotionally (a mascot vote), but it does
touch the real, human idea of a group being "unheard" by a decision that affects them. Keep the
discussion on the math and the disclosed probabilities, not on which real-world groups get
under-surveyed in practice — that's a legitimate adjacent conversation but not this case's job.

## Argument for A (Simple Random Sample)

A wins the graded primary metric — Jeff's total personal call time — because it never pays for a
guide-coordination call at a campus that, by chance, contributes no one to the sample. That's real,
but it's a thin edge (51.23 h vs. B's 53.92 h) against a 3-month runway with enormous slack — don't
let a Hero lean on "we need the time savings to hit the deadline," because the numbers don't
support it (a Hero pressed with "would Option B actually have blown your deadline?" has to admit
no).

The stronger, honest case for A is administrative simplicity as a real operational cost distinct
from the hours already counted: Jeff is running this whole survey himself, one call at a time,
with no team to divide the bookkeeping. SRS needs only one flat list of 1,420 IDs and a single
random draw of 142 — nothing to reconcile. Stratified means Jeff has to carry 50 separate running
quotas at once (Appendix C's largest-remainder table), each needing its own tally of
interviews-completed-vs-target as calls trickle in over three months, with real risk of over- or
under-shooting a campus along the way. That's a genuine cost a single-person, one-call-at-a-time
operation should weigh. A also gives every individual learner in the network an equal, unbiased
chance of being chosen — a real fairness argument on its own terms (one learner, one equal shot),
not merely "the lazy option."

## Argument for B (Stratified Sample)

B guarantees all 50 campuses are heard — zero campuses silenced by chance, by construction
(Appendix C's proportional allocation, reconciled by largest remainder to sum to exactly 142).
Under A, several of the network's smallest (12-learner) campuses each carry a real, computable,
double-digit-percent probability of contributing *zero* learners to the sample — and summed across
the whole network, the *expected* number of campuses that go entirely unheard is large enough that
a real slice of the network is silenced on a survey whose entire stated purpose is giving every
age of learner a voice (Background). B closes that gap for a small amount of extra call time.

## The margin

`margin_basis` (case.json.balance): total call time for each option = 142 learner interviews ×
17.5 min (MA2) + (campuses reached) × 15 min (MA1). B always reaches all 50 campuses; A reaches an
*expected* 39.235 (50 minus the exact hypergeometric shutout sum, Appendix C, computed from the
real 50-campus size list). **Total_A ≈ 51.23 h, Total_B ≈ 53.92 h — margin = 5.3%, Option A wins
the primary metric by 5.3%.** This is a thin margin by design: the learner-interview time
(identical either way) dwarfs the coordination-time difference between the two options, so A's
time advantage is real but small, while B's coverage advantage (closing an expected ~10.8-campus,
~21.5%-of-network gap) is large and computed exactly from the real roster. This is why the case
works: A wins the graded number, but by little enough that a Hero who actually does the coverage
arithmetic has a real, quantified case for B too.

## Five Socratic questions

1. "You computed the probability that a specific 12-learner campus gets zero calls under Option A — what does that number become once you add up all the small campuses in the network, not just one?"
2. "Option A wins on total call time. By how much, in hours — and is that gap big enough to be the reason you'd pick it, or is something else actually driving your choice?"
3. "If Jeff's real goal was 'give every age of learner a voice,' does a method that has a real chance of silencing entire campuses actually deliver on that goal, even if it's statistically unbiased at the individual-learner level?"
4. "Your Stratified allocation table didn't come out to exactly 142 when you just rounded every campus separately — how did you fix that, and could you have fixed it a different, equally defensible way?"
5. "If Jeff decided he only had time for half as many total calls, which of your two methods' advantages would matter more — the time savings, or the coverage guarantee?"

## The trap

Most students will compute the per-campus "probability of being shut out" for one or two small
campuses (Appendix C), see a number like "28%," and reflexively assume Option A is unacceptably
risky and Option B is the obvious right answer — without ever tallying *how much total call time
Option B actually costs to fix that*. Learners who skip the coverage-vs-cost comparison and stop
at "28% chance of exclusion sounds bad" have found the right instinct without doing the arithmetic
that actually justifies it. The real numbers show B's fix is cheap in call-time (a handful of
extra hours), which matters. Cold-call on this specifically: "You said Option A's risk is
unacceptable — unacceptable compared to what cost? Show me the hours."

## Sensitivity note (SPEC §6 / T4)

The coordination-call-length assumption and the choice of 17.5 min (vs. 15 or 20) as the
interview-length point are both stated Modeling Assumptions a Hero could challenge. Tier 2 probe 5
flexes both ±50% via `sensitivity_model.py` — see that file's own header for which reading is more
fragile.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch, 30-second commitments, stand/sit vote — no explanation |
| **3:00–10:00** | Position defense: "Convince us why it's better, not just simpler" |
| **10:00–15:00** | Pressure-test the models: "Whose plan is most fragile to a small campus?" |
| **15:00** | **DROP THE TWIST** — coordination calls run at the top of the stated 15–20 min range, not the bottom MA1 assumed — delivered slowly, with pauses |
| **15:00–20:00** | Immediate recommit: who reverses? "What just broke in your total?" |
| **20:00–30:00** | Threaded deep conflict — two named threads: (1) fairness-by-learner (SRS's equal individual chance) vs. fairness-by-campus (Stratified's guaranteed coverage); (2) statistical purity vs. practical time cost |
| **30:00–45:00** | Close, re-vote, reflection, lessons learned |

## Intro

Frame the format: this is a real Acton-network decision, drawn from a real 1,420-learner roster,
not a worksheet with a story stapled on. Name the opener — "One founder, three months to go, one
phone in his hand, and fifty campuses of wildly different sizes. How do you make sure everybody
actually gets asked?"

## Launch

Read the Overview aloud, then Background's population/sample facts (1,420 learners, 50 campuses,
target of 142) with no Appendix C/D numbers shown yet. Ask: "Just from what you've heard — does
picking who to call sound like a simple decision, or a genuinely hard one?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who's calling Simple Random? Who's calling Stratified?" Show of hands, no discussion yet. Record
the count — Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'fair'?"**

Push on what "represents the population" even means here. Fair to each *learner* equally? Fair to
each *campus* equally, regardless of size? Let the room sit in the ambiguity — "Is anyone
courageous enough to define 'fair' before we start computing anything?"

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has picked a working definition of "fair" or "representative," ask them to name the
actual steps: how big is the population, how big is the sample, what's each method's probability
or allocation math, and what does each method actually cost in call time. Re-ask: "Given how we
just defined 'fair' — is that still the right process?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix D's coordination-call-length assumption and the 17.5-min interview choice as a
group, out loud, before anyone computes final totals. Ask which one the room thinks matters most.

## Data Deep Dive

Now, and only now, the numbers. Walk D3's per-campus shutout probabilities and D4's allocation
table together as a room, then D5's total call-time comparison.

**The trap:** see above — Heroes stop at "a small campus has a real chance of exclusion" and skip
the actual call-time cost comparison that would tell them whether fixing that risk is cheap or
expensive. Cold-call: "How many total hours does closing that gap actually cost?"

## Twist — drop this at roughly the 15-minute mark

Deliver slowly, with pauses:

"Jeff just called back. He says: 'Forget the campus count for a second — turns out every guide
wants to talk shop before they hand the phone over, so coordination calls are running at the full
20 minutes the range allows, not the 15 you assumed.' You now have 60 seconds. Does your total
call-time comparison still favor the same option — or did it just flip?"

Run `python3 sensitivity_model.py` with the coordination-call length at 20 minutes (still inside
the case's own stated 15–20 minute bracket, Appendix A) to check whether this actually flips the
verdict for this case's real numbers, and report the real answer to the room — do not assert an
outcome here that the model doesn't confirm.

## Close — vote again

VOTE AGAIN. "Did we ask the right question? What math was new to you today, and how did you
attack it?"

## Lessons Learned

- How would you rank this case study in terms of difficulty, 1–5?
- What was the hardest single step — the probability, the proportional allocation, or the
  time-budget arithmetic?
- What math concepts were new to you, and how did you take on that challenge?
- If given a similar case next time, what would you do differently?

## Standards Touched On

Share the standards checklist from `case.json.standards[]`.
