# Facilitator Notes: The Downbeat Split

**Case:** The Downbeat Split · **Tier:** T2 (MS-core) · **Studio:** Adventure
**Standards:** Fractions/Multiplication Of Fractions, Fractions/Division Of Fractions — how to
multiply two mixed numbers; how to divide a fraction by a fraction; how to multiply a fraction and
a mixed number; how to divide fractions and mixed numbers (see `case.json.standards[]` for exact
ids; `new_coverage[]` = the first two, both currently unclaimed before this case)

Balance is computed and recorded (`case.json.balance.margin_pct` = 10.0 — see "The margin" below
for the full arithmetic). **Retuned 2026-08-29**: the original primary metric (rehearsal minutes
per second of timing accuracy gained) was structurally unbalanceable — Option A's rehearsal-minute
numerator is exactly zero by construction, so any nonzero Option B cost computed to a 100% margin
no matter how the other assumptions were tuned. The primary metric was reframed to expected total
studio minutes (rehearsal minutes plus probability-weighted redelivery-risk minutes), grounded
directly in the Twist that was already drafted below — see "The margin" for the full derivation.

## Intro

Frame the format before anything else: this is a two-option dilemma, one recommendation, defended
with real arithmetic. Name the opener — Elena Cross, staff arranger, has two versions of the same
sixteen-bar cue on her stand and a producer standing in the doorway. Tell the room: "You are going
to vote on this before you've seen a single number. Then we're going to do the math and see if the
vote holds."

## Launch

Read the Overview aloud, or have a student read it — it is written to be read aloud. Stop exactly
where the document stops: Elena picking up her pencil, looking up. Do not preview the Dilemma or
Background yet; let the Overview alone set the stakes (the click track, the "hair long" take, the
producer's "whenever you're ready").

## Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet, just commit. "Is anyone courageous enough to stand with the Straight Cut? With
the Downbeat Split?" Take the vote, record the split, and move on without debating it — the vote
is a baseline to return to at Close, not a discussion.

## Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

"Is this the right question?" "What do you mean by 'cost' — is it dollars, minutes, or something
else?" "Is 'rehearsal minutes' the whole cost of a decision like this?" Let confusion grow
deliberately here: "Wow, this is a harder question than it looked a minute ago." Push until the
room lands on the case's own framing: expected total studio minutes required to deliver a
broadcast-ready take — booked rehearsal minutes plus the probability-weighted cost of a re-booked
session if delivery is rejected (the primary metric named in Background) — and surface, without
answering it yet, Socratic question 1 below.

**Socratic question 1** (use here): If Option A books zero additional rehearsal minutes, does that
make it automatically the cheaper choice — or is "rehearsal minutes" only counting one of the two
ways this decision can cost the studio money?

## Anchor 3 — WHAT IS THE PROCESS?

"If we go through this process and find the data, how will we decide?" Get the room to name the
five deliverables (D1–D5) as the process, in order — total running time, partial-phrase check,
subdivision split, read-through fit-check, decision table — without doing any arithmetic yet.
Re-ask: "Is our question still the right question?"

**Socratic question 3** (use here): D3 finds the exact subdivision needed to close the gap by
dividing one fraction by another — what would happen to that computed subdivision if the timing gap
you're closing were half as large, or twice as large?

## Anchor 4 — WHAT DON'T WE KNOW?

"Do we need to make assumptions? Which ones are critical?" Walk the room through Appendix E's
Modeling Assumptions at a high level — not the values yet, just which quantities had to be assumed
rather than looked up (the target duration, the phrase structure, the tempo, the read-through
length, the remaining session time) versus the two real, sourced AFM figures in Appendix C.

**Socratic question 2** (use here): The Straight Cut's timing gap is "close, but not exact" — how
close does "close" have to be before the network's frame-accuracy tolerance in Appendix A treats it
as a failed delivery instead of a rounding error?

## Data Deep Dive

Now, and only now, the numbers. Walk D1–D5 in order:

- **D1** — 3¾ beats × 1⅓ sec/beat × 4 repeats = 20 seconds (the Straight Cut's written total).
- **D2** — 3/8 × 3¾ beats × 1⅓ sec/beat = 1⅞ seconds (1.875 sec) — exactly the gap between the
  20-second written total and the 21⅞-second target (Appendix A / MA1).
- **D3** — 3/8 (the gap, as a fraction of the final phrase's beat length) ÷ 1/2 (the ensemble's
  normal subdivision unit, MA8) = 3/4. The syncopated beat splits at 3/4 of a normal subdivision
  unit into the phrase.
- **D4** — 22½ minutes remaining (MA10) ÷ 2½ minutes per read-through (MA9) = 9 complete
  read-throughs.
- **D5** — Rehearsal minutes: Option A = 0 (already rehearsed, no new read-throughs booked); Option
  B = 2½ min × 9 read-throughs = 22.5 min. Redelivery-risk minutes: Option A = 1/3 (MA11) × 1½ hr
  (MA2, the total booked session length, since a rejected take has to be re-booked as a whole new
  session) = 1/3 × 90 min = 30 min; Option B = 1/20 (MA12) × 90 min = 4.5 min. Expected total
  minutes: Option A = 0 + 30 = **30.0 min**; Option B = 22.5 + 4.5 = **27.0 min**. The Downbeat
  Split is now the lower-expected-cost option, even though its booked rehearsal minutes are higher.

**Socratic question 4** (use here): D4 tells you how many read-throughs fit in the time remaining
in the session — what happens to Elena's recommendation if that number comes out to zero, meaning
the Downbeat Split literally cannot be rehearsed clean before the session ends?

## Twist

At roughly the 15-minute mark: the producer, checking his phone, mentions — almost as an aside —
that this is not the first time Larkspur Sound has delivered a cue to this exact client on a tight
tempo compromise. The last time, the network's traffic department rejected the take on delivery for
running outside frame-accuracy tolerance, and Larkspur had to re-book the ensemble and re-cut the
spot on the studio's own dime, after the ad buy's air date had already been locked.

This does not hand the room a new number — Appendix E's MA11 (1/3 redelivery-risk probability for
the Straight Cut) was on the page the whole time, and D1–D5 still compute exactly as stated. What
the Twist changes is the *weight* the room puts on that number: MA11 is easy to read as an abstract,
hypothetical "what if" and discount while doing the arithmetic — the Twist confirms it is not
hypothetical, it already happened, to this exact client, on this exact kind of compromise. A room
that priced Option A's real cost at 0 because "no new rehearsal minutes are booked" — treating
MA11's 30 expected redelivery-risk minutes as a formality rather than a real number to weigh against
Option B's — now has to reckon with the fact that Option A's zero *rehearsal* cost was never a zero
*total* cost, and the case's own expected-total-minutes math already said so (30.0 min vs. 27.0 min)
before the Twist ever landed. It does not make Option B obviously correct either: MA12's own 1/20
risk is small but not zero, and a smaller MA11 would flip the recommendation right back.

**Follow-up (the whole point):** "What just broke in your original model? Were you wrong — or did
you have the right number and just not take it seriously?" Push the room to notice the difference
between a number being *on the page* and a number being *believed* — the trap here is not a missing
term, it is a discounted one.

## Close

Vote again. "Did we ask the right question?" "What math was new to you, and how did you attack it?"
Compare the second vote to Anchor 1's. A room that flips after the Twist — with no new number to
justify it — is the intended outcome; the discussion is about naming why fraction arithmetic alone
did not settle the question.

**Socratic question 5** (use here, as the closing prompt): Argument for A treats the tempo
compromise as cheap because no new rehearsal time is booked — once you weight in MA11's redelivery
risk, Option A's expected cost (30.0 min) is still close to Option B's (27.0 min), not far behind
it. What would MA11 have to be for Option A to actually win?

## Lessons Learned

- Fraction and mixed-number arithmetic (D1–D5) is necessary but not sufficient here: the numbers
  resolve cleanly (30.0 vs. 27.0 expected total minutes), but a clean number is not the same as a
  settled decision — the margin is only 10%.
- A "zero" in booked rehearsal minutes is not automatically "free" — Option A's real cost was always
  there in the case's own data (MA11), just not in the column most people look at first.
- The closest arithmetic result in this case (30.0 vs. 27.0, a 10% margin) is exactly where the
  discussion should slow down, not speed up — a small, defensible change to MA11 or MA12 flips it.

## Standards Touched On

Fractions — how to multiply two mixed numbers; how to divide a fraction by a fraction; how to
multiply a fraction and a mixed number; how to divide fractions and mixed numbers. See
`case.json.standards[]` for exact spine ids and Appendix G of `case.md` for the verbatim labels
students research in Challenge 1.

## Argument for A — The Straight Cut

The Straight Cut costs nothing more in rehearsal time — it is already clean, already sight-read,
already banked. The only thing it costs is a small, uniform tempo nudge across the whole cue to
absorb the leftover gap between its computed total running time (D1) and the broadcast slot's exact
target. Its weakness is MA11: because that nudge is a live, one-shot adjustment rather than
material rehearsed to an exact target, the case sets its redelivery-risk probability at 1/3 —
already-happened-once, per the Twist. Weighted against the full re-book cost of a rejected take
(MA2's 90-minute session), that risk alone adds 30 expected minutes, making Option A's real expected
cost (30.0 min) close to, not obviously better than, Option B's.

## Argument for B — The Downbeat Split

The Downbeat Split is the only version that lands on the broadcast slot's target exactly rather
than approximately, and a broadcast slot is not a target with a tolerance the arranger gets to set
— it is fixed by the network and the client. Its rehearsal cost is small, bounded, and one-time: a
fixed number of read-throughs (9, per D4) at the AFM's real published rehearsal rate (Appendix C).
Because it is rehearsed to an exact target across all 9 read-throughs rather than delivered on a
single live adjustment, its redelivery-risk probability (MA12, 1/20) is far lower than Option A's —
adding only 4.5 expected minutes to its 22.5 booked rehearsal minutes, for an expected total of
27.0 min. That undercuts Option A's 30.0 min, even though Option B's raw rehearsal-minute cost is
the higher of the two.

## The margin

`margin_basis` (computed): D1–D5 resolve, from Appendices A–D and the Modeling Assumptions, to
Option A = 30.0 expected total minutes (0 rehearsal + 1/3 × 90 min redelivery-risk), Option B =
27.0 expected total minutes (22.5 rehearsal + 1/20 × 90 min redelivery-risk) — full arithmetic in
"Data Deep Dive" above and in `case.json.derived`. `margin_pct` = 100 × (loser − winner) / loser =
100 × (30.0 − 27.0) / 30.0 = **10.0%**, comfortably inside SPEC §2's ~20% cap and below the 15%
"wide" threshold.

**Retune history.** The original primary metric ("rehearsal minutes required per second of timing
accuracy gained") was structurally unbalanceable, not just unluckily tuned: Option A's rehearsal-
minute numerator was exactly zero by the case's own construction (already rehearsed; a uniform
tempo nudge closes any residual gap exactly, by definition, regardless of the gap's size), so any
nonzero Option B cost computed to a 100% margin under the standard formula — the same structural
pattern found in `fret-board`'s QA precedent (`cases/fret-board/case.json`'s balance object). No
amount of retuning MA1–MA10 could have fixed this; the primary metric itself had to change. The fix
applied: reframe the primary metric to expected total studio minutes, adding a redelivery-risk term
(MA11/MA12) that is nonzero for both options — grounded directly in the Twist that was already
drafted in this file, not invented from nothing. This margin is genuinely close (10.0%) and
genuinely sensitive to MA11/MA12 — see `sensitivity_model.py` and the Judgment call note in
`QA_REPORT.md` for the exact flip points. That sensitivity is intended discussion content, not a
defect.

## Five Socratic questions

1. If Option A books zero additional rehearsal minutes, does that make it automatically the cheaper choice — or is "rehearsal minutes" only counting one of the two ways this decision can cost the studio money? *(Anchor 2)*
2. The Straight Cut's timing gap is "close, but not exact" — how close does "close" have to be before the network's frame-accuracy tolerance in Appendix A treats it as a failed delivery instead of a rounding error? *(Anchor 4)*
3. D3 finds the exact subdivision needed to close the gap by dividing one fraction by another — what would happen to that computed subdivision if the timing gap you're closing were half as large, or twice as large? *(Anchor 3)*
4. D4 tells you how many read-throughs fit in the time remaining in the session — what happens to Elena's recommendation if that number comes out to zero, meaning the Downbeat Split literally cannot be rehearsed clean before the session ends? *(Data Deep Dive)*
5. Argument for A treats the tempo compromise as cheap because no new rehearsal time is booked — once you weight in MA11's redelivery risk, Option A's expected cost (30.0 min) is still close to Option B's (27.0 min). What would MA11 have to be for Option A to actually win? *(Close)*

## The trap

Heroes will price the Straight Cut's rehearsal-minute cost as zero and stop there, because the
ensemble has already learned it — reading Appendix E's MA11 (the 1/3 redelivery-risk probability)
as a formality to skim past rather than a real term to multiply into the decision table, and
comparing the Downbeat Split's real, booked rehearsal minutes against a phantom zero instead of
against Option A's real expected cost (30.0 min, computed in D5). "Already rehearsed" is not the
same as "free" once the thing being measured is whether the take is actually deliverable, not just
whether it was cheap to record — and the number that says so was on the page the whole time.

## Sensitivity note

MA11/MA12 (the redelivery-risk probabilities added in the 2026-08-29 retune) are dilemma-flipping —
see `sensitivity_model.py` for the exact flip points. `sensitivity_note` in `case.json` (a distinct,
always-present field naming which Modeling Assumptions are dilemma-flipping) still applies for the
rest: MA1/MA4/MA5/MA6/MA7 jointly fix the size of the timing gap, and MA2/MA9/MA10 jointly fix the
Downbeat Split's rehearsal-minute cost.

## Facilitator note — assumption sensitivity (Tier 2 probe P5)

`sensitivity_model.py --flex-all` confirms the 10.0% margin flips from B to A under a -50% flex on
either MA11 (1/3 -> 1/6) or MA2's re-book length (90 -> 45 min) — no other stated dial flips it at
±50%. This is disclosed, not hidden: `case.json.sensitivity_disclosure[]` records both (Category X —
no published rejection-rate or re-book-length data exists for either quantity; both are good-faith
scenario estimates, not discovered facts). If a Hero pushes hard on "why 1/3, why not 1/6 or 1/4,"
that is intended pedagogy, not a defect to deflect — the honest answer is "there is no public number
for this; the case's own Twist is the best evidence we have that it isn't negligible, and reasonable
people could land somewhere else." Do not let the discussion pretend MA11 is more solid than it is.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch (read the Overview aloud), 30-second commitments, stand/sit vote (Anchor 1) — no explanation |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just cheaper" (Anchor 2 — define the question; Socratic question 1) |
| 10:00–15:00 | Pressure-test the models: name the process (Anchor 3 — Socratic question 3), name the unknowns (Anchor 4 — Socratic question 2) |
| **15:00** | **DROP THE TWIST** — the producer's aside about the client's earlier rejected take — delivered slowly, with pauses |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke in your model?" |
| 20:00–30:00 | Data Deep Dive: walk D1–D5 together (Socratic question 4); two threaded deep-conflict threads — (a) "does zero rehearsal minutes mean zero cost?" and (b) "a 10% margin that flips on MA11/MA12 — how much should that shake your confidence?" |
| 30:00–45:00 | Close: re-vote, Socratic question 5, reflection, Lessons Learned |
