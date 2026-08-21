# FACILITATOR.md — Playoff Committee

**Answer-key content. Never copy any of this into `case.md`.**

## Argument for A — the Resume Path (Oklahoma)

Oklahoma is undefeated (9-0), the only team ranked AP #4 or better with a zero in the loss
column, and sits at roughly 87.7% of the maximum possible AP voting points — near-unanimous
human consensus. The committee's own real 2014-2023 track record backs this instinct: no team
with two or more losses was ever selected in the four-team era, and the large majority of
selections were power-conference champions or one-loss power-conference teams (Appendix D).
Trusting the accumulated human judgment behind that pattern over a single formula's opinion is a
defensible, evidence-backed stance.

## Argument for B — the Power-Rating Path (Michigan)

Michigan's SRS (21.02) is the second-highest of the roughly 130-team full dataset — only
Georgia's is higher — reflecting dominant point differentials against a real schedule that the
human poll (AP #9, only 66.5% of maximum voting points) has been slow to recognize. This is
precisely the historical complaint (poll voters anchored on preseason reputation and name-brand
recognition) that produced the BCS and then the CFP committee system in the first place. Under
this case's own neutral, equally-weighted Composite Selection Score, Michigan leads Oklahoma by
about 11.7%, because Michigan's human-poll deficit is proportionally smaller than Oklahoma's SRS
deficit.

## The margin

**How it was computed:** each team's Composite Selection Score (Modeling Assumption MA4) is the
unweighted mean of (a) AP voting points as a percent of the maximum possible (63 first-place
votes x 25 points = 1,575), and (b) SRS as a percent of the season's single highest SRS (MA3,
Georgia's 25.94).

- Oklahoma: Human 87.75%, Machine 44.41%, composite ≈ 66.08
- Michigan: Human 66.54%, Machine 81.03%, composite ≈ 73.79
- Margin (100 x |A-B| / min(A,B) on the composite): **≈11.67%, favoring Michigan (Option B)**

This is what a specific, disclosed 50/50 weighting produces — not the case's "correct" answer. A
strong pitch for Option A does not need to beat this number on its own terms; it can argue the
weighting itself is wrong, or that the committee's real historical bias toward clean records
belongs in the decision even though it is not part of the Composite Selection Score's formula.

## Five Socratic questions

1. Your Composite Selection Score put Michigan about 11.7% ahead of Oklahoma — what happens to that gap if you weight the human score more heavily than the machine score, and can you defend the weighting you chose?
2. Oklahoma's machine score is only 44.41% of the season's ceiling — is that because Oklahoma is actually a weak team, or because the SRS ceiling belongs to a team (Georgia) that isn't even one of your two options?
3. The committee's own real four-team-era history (Appendix D) almost never selected a two-loss team, and Oklahoma has zero losses to Michigan's one — does that historical pattern belong in your composite score at all, or is it a separate, non-numeric argument?
4. If your SRS ceiling were the highest rating among teams that are genuine competitors for this specific spot, not the presumptive #1 overall seed, would Michigan's machine score still look the same?
5. Which of your five supporting data points in D4 would change your recommendation if it were removed, and which are just decoration that would not move your pitch either way?

## The trap

The trap is treating the Composite Selection Score as a computed, objective answer rather than
what it actually is: one specific, disclosed 50/50 blend of two normalized percentages, built on
a modeling choice (MA4) made for this exercise, not an official CFP formula. Heroes who confuse
"I built a formula and computed a number" with "the math proved my team should get the spot" miss
that a different, equally defensible weighting (e.g., weighting the human score more heavily,
matching the committee's own real historical bias toward clean won-loss records) can move the
composite back toward Oklahoma without it ever exceeding the composite's neutral read for
Michigan. The strongest pitches name the weighting choice explicitly and defend it, rather than
presenting the 50/50 split as neutral or inevitable.

## Sensitivity note

The Composite Selection Score's 50/50 weighting (MA4) and the choice of SRS ceiling (MA3,
Georgia — a team not itself one of the two contested options) are this case's most load-bearing
assumptions; both are flagged for the ±50% sensitivity flex (Tier 2 probe 3). Run the flex and the
winner genuinely moves: weighting the human score more heavily (human_weight → 0.75, a defensible
alternative given the committee's own real historical bias toward clean records) flips the verdict
to Oklahoma; weighting it less (→ 0.25) or widening the AP-points denominator instead pushes
Michigan's lead past a 20%-plus margin. This instability is disclosed, not eliminated —
`case.json.sensitivity_disclosure[]` records it — and it is itself worth putting to a room: ask
directly whether a "neutral" 50/50 split is really neutral when the committee's own real-world
voting pattern (Appendix D) already leans toward trusting resumes over ratings. SPEC section 6
does not otherwise apply — the case's stakes are athletic postseason selection, not death/illness/
financial hardship.

---

## Guide Notes — the anchor ladder

### Intro

Frame the format: this is not a worksheet, it's a locked-room committee vote. Name the opener —
"Two teams. One spot. The vote keeps landing exactly split. You break the tie."

### Launch

Read the Overview aloud, stopping at the five-minute clock. Show only the two teams' names and
records (Oklahoma 9-0, Michigan 7-1) — do not show the AP points or SRS numbers yet. Ask: "Just
from the records, who deserves the spot?"

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet, just commit. "Is anyone courageous enough to stand with Oklahoma? With
Michigan?" Record the room's initial split — it is the number the Close re-votes against.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

"Is this the right question?" "What do you mean by 'deserves'?" "Is the question 'who is the
better team,' or 'whose case can you defend with numbers'?" Let confusion grow deliberately —
"Wow, this is a genuinely hard problem when the two data sources disagree" is a good place to let
the room sit for a minute.

### Anchor 3 — WHAT IS THE PROCESS?

"If we go through this process and find the data, how will we decide?" Push the room toward
naming an actual procedure (compare the human poll, compare the computer rating, then decide how
to combine them) before anyone is allowed to open Appendix B or C. Re-ask: "Is our question still
the right question?"

### Anchor 4 — WHAT DON'T WE KNOW?

"Do we need to make assumptions? Which ones are critical?" Surface Appendix F's Modeling
Assumptions (the 50/50 weighting, the choice of SRS ceiling) without revealing their exact
sensitivity — just that they are stated assumptions, not measured facts, and a Hero may
challenge them.

### Data Deep Dive

Now, and only now, the numbers: Appendix B's AP Top 25 table and Appendix C's SRS table. Let the
room start computing Human% and Machine% for both teams, and building their Composite Selection
Score tables.

### Twist

At roughly the 15-minute mark, after most groups have a composite score for both teams:
**"The committee chair points out something: Georgia — the team supplying the SRS ceiling you've
been dividing by — isn't a real competitor for this spot. It's the presumptive #1 overall seed,
locked in from week one. If you recompute the Machine score using the highest SRS among teams
that are actually in the room's conversation for an at-large bid — Alabama's 20.95 — instead of
Georgia's 25.94, what happens to your numbers?"**

Recomputed: Oklahoma's machine score rises to 54.99% (11.52/20.95), and Michigan's machine score
rises to 100.33% (21.02/20.95) — Michigan's SRS is now *higher* than the new ceiling entirely.
New composites: Oklahoma ≈71.37, Michigan ≈83.44 — margin widens to roughly 16.9%, still favoring
Michigan. **The direction of the recommendation does not flip**, but the size of the gap changes
meaningfully, and a team's score exceeding 100% of its own "ceiling" is a genuinely useful
moment: it means the ceiling was never a hard cap, only a reference point the case chose, and
choosing a different reference point changes the story you can tell with the same underlying
data.

Ask: **"Does this change your plan? You have 60 seconds — are you changing your recommendation,
or not?"** This tests whether groups quietly treated their first denominator as sacred, versus
understanding it as a modeling choice (MA3) they can name and defend.

### Close

VOTE AGAIN. "Did we ask the right question?" "What math was new to you today, and how did you
attack it?" Compare the final vote to the Anchor 1 vote — who moved, and toward which team.

### Lessons Learned

The gap between "the computer rates Michigan higher" and "the computer rating proves Michigan
should get the spot": a rating is only as meaningful as the reference point it's measured
against, and this case's own SRS ceiling (Georgia) belongs to a team that isn't even competing
for the spot in question. Changing that one modeling choice (MA3) doesn't flip the answer here,
but it does change the size of the gap by nearly 50% in relative terms — a preview of exactly
the kind of assumption a rigorous pitch has to name and defend, not treat as neutral.

### Standards Touched On

Percent; How to convert numbers to percents; Mean; How to find the mean of a set of data.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00-3:00 | Cold-call launch, records only, stand/sit vote (Anchor 1) — no explanation yet |
| 3:00-10:00 | Position defense: "Convince us why your team deserves it, not just that its record/rating sounds good" (Anchors 2-3) |
| 10:00-15:00 | Pressure-test the models: "Whose case depends on which single number you trust most?" |
| 15:00 | **DROP THE TWIST** — Georgia isn't a real competitor for this spot; recompute the Machine-score ceiling using Alabama's SRS instead |
| 15:00-20:00 | Immediate recommit: who reverses, and who was quietly treating their first ceiling as fixed? "What just broke?" |
| 20:00-30:00 | Threaded deep conflict, two named threads: (1) trusting nine games of human judgment vs. trusting one season's point-differential formula; (2) how the choice of a "ceiling" or "ceiling team" changes what a percent-of-maximum score actually means |
| 30:00-45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands

- **Full (12-14)** — the size the case was authored for. Both teams get a full defense round;
  Anchor 3's process discussion can split the room into an Oklahoma camp and a Michigan camp
  before the numbers land; the full timed 45-minute Socratic plan runs as written.
- **Compressed (6-7)** — combine Anchors 2-3 into one pass; run one deep-conflict thread instead
  of two (human judgment vs. computer rating); keep the ceiling-team twist — it is cheap to run
  at any size; total runtime shortens proportionally, not the content.
- **1:1 / pair (1-2)** — no vote to take; Anchor 1 becomes the learner stating an initial position
  instead of a stand/sit vote; the guide plays devil's advocate for the other team directly rather
  than cold-calling; the twist still lands; "who reverses" becomes "would you reverse, and why."
