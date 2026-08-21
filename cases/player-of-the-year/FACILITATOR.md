# FACILITATOR.md — Player Of The Year

**Sensitive-content flag:** none. This case carries no illness/death/money-stress/family-hardship
weight — the stakes are reputational/professional (an award, a committee's credibility), not
personal hardship.

## Argument for A — Adopt the All-Purpose Production Index

Anna Stevenson posts the single highest average z-score of any of the 14 finalists (+0.526),
built almost entirely on two categories: a .427 hitting percentage and 1.35 blocks/set, both
elite even against the already-elite national leaderboard population (Appendix B). The strongest
version of this argument is philosophical as much as numeric: Methodology A treats every finalist
by the exact same yardstick, with no position-based curve-fitting — nobody's score depends on
which categories got chosen for her role. That consistency is itself a defensible value. The
numeric case is real but fragile: Stevenson's +0.526 beats Sydney Hilley's +0.517 by just 0.009
composite points — a 1.74% relative margin. Whoever argues for A has to be honest that they are
defending a near-tie, not a landslide.

## Argument for B — Adopt the Role-Weighted × Team-Success Composite

Sydney Hilley's 11.95 assists/set is the single largest z-score anywhere in the dataset (+2.585)
— more standard deviations above her positional peers than any other stat, for any other player,
in either methodology. Diluting that dominance by averaging it against four categories she
structurally cannot contribute to (kills, aces, blocks, digs) — which is exactly what Methodology
A does by scoring her at z=0 in all four — arguably erases the single most extreme performance in
the whole class of finalists. Combine that with Wisconsin's #2 RPI and their actual championship
upset over #1 Louisville, and Hilley's composite (+3.851) leads Nicole Peterson, the #2 finalist
under this system, by 0.731 points — a 23.4% relative margin. This is not a coin flip; it is a
comfortable, reproducible result under its own rules.

## The margin

Methodology A's own top-two margin: **0.009 composite points, 1.74% relative** (Stevenson +0.526
vs. Hilley +0.517).
Methodology B's own top-two margin: **0.731 composite points, 23.4% relative** (Hilley +3.851 vs.
Peterson +3.117).

The case's real balance-test tension is not "which number is bigger" — it's that switching
methodologies doesn't just change the *winner*, it changes how *close* the verdict even is. A
committee that values a decisive result has a real, numeric reason to prefer B over A independent
of who wins.

## The trap

Most students will treat "lots of stats and composite stats" as license to cherry-pick whichever
numbers make their favorite player look best, then reverse-engineer a "formula" to justify a pick
they already made. The case is built specifically to close that door: both formulas are fixed,
disclosed, and must be run identically across all 14 finalists before a single argument is
written. Students who skip straight to defending a player instead of first computing both full
composite tables (D1/D2) will produce a pitch that looks like Methodology B language wrapped
around a Methodology A-style cherry pick — internally inconsistent, and a fast tell that they
never actually ran the numbers. A second, quieter version of the same trap: students who compute
Methodology A correctly but never check how thin its 1.74% margin actually is will confidently
declare Stevenson "the best," never noticing that the same process places Hilley close enough
behind her that a single rounding convention could flip the result.

## Sensitivity note

Per SPEC §6 / `case.json.balance`, both `case.json.modeling_assumptions` MA1 (the z=0 convention)
and MA3 (the TeamMult curve shape) are load-bearing. Flexing MA3's +50% cap up or down changes
Hilley's and Peterson's composites (both Wisconsin, both getting the top-tier bonus) without
changing their z-scores — worth having a pair actually recompute CompositeB under a different cap
live during the discussion to see whether Methodology B's 23.4% margin is as robust as it looks,
or whether it's just as sensitive to a hidden design choice as Methodology A's razor-thin one.

---

## Guide Notes — the anchor ladder

### Intro

Frame the format for the room: "You are being handed two finished, disclosed, real formulas.
Your job is not to invent a third one — it's to run both, honestly, across all 14 real players,
and then decide which committee member's math the AVCA should trust." Name the opener: the
envelope moment, Renata Voss holding two spreadsheets with two minutes on the clock.

### Launch

Show the room Appendix A's full 14-player table cold, before any formula. Ask: "Just looking at
this — no math yet — who do you think wins Player Of The Year?" Let instinct answer first; most
rooms will gravitate to whoever has the flashiest single number (Hilley's 11.95 assists, or
Stevenson's .427 hitting%). Note the instinctive pick on the board — it's the thing the twist
will test later.

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet, just commit. "Is anyone courageous enough to stand with Methodology A? With
Methodology B?" Split the room physically if the cohort size allows it (see `cohort_bands` in
case.json for how this changes below Full size).

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

"Is 'who is the best player' even the right question, or is the real question 'which way of
measuring 'best' do we trust'?" Push: "What do you mean by 'best'? Best at what?" Let the
confusion sit — a room that starts arguing about what "best" even means before touching a
calculator is doing the case correctly. "Wow, this is a harder question than it looked."

### Anchor 3 — WHAT IS THE PROCESS?

"If we actually run both formulas end to end on all 14 players, how will we decide between the
two committee members?" Re-ask Anchor 2's question here: "Now that we've named a process, is
'which methodology' still the right question, or is it really 'which margin do we trust more'?"

### Anchor 4 — WHAT DON'T WE KNOW?

"Do we need to make any assumptions to run either formula? Which ones are load-bearing?" Steer
the room toward Appendix E without reading it to them yet: the z=0-for-unranked convention, the
already-elite national reference population, and the shape of the team-success multiplier curve
are all disclosed choices, not neutral facts. "Which of these, if changed, would you expect to
actually move the answer?"

### Data Deep Dive

Now, and only now, work the numbers: both composite tables (D1/D2), the force ranking (D3), and
the two margins (D5). Confirm as a room: Methodology A's margin is 1.74%; Methodology B's margin
is 23.4%.

### Twist

At roughly the 15-minute mark, once the room has Methodology A's 0.009-point margin in hand:
**"That margin is smaller than routine sports statistics precision allows for."** Real NCAA
per-set stats are reported to two decimal places — a single late scorer's-table correction can
move a player's Kills/Set or Blocks/Set by more than 0.009 composite points once averaged into a
five-category mean. Concretely: Anna Stevenson's Blocks/Set would only need to move from 1.35 to
1.344 — a swing of six one-hundredths of a block per set, well within ordinary box-score revision
— to erase her entire lead and hand Methodology A's title to Sydney Hilley instead. Deliver it
slowly: "Methodology A's entire margin is smaller than a single stat-sheet correction. Does
Methodology A still have a winner?" Give the room 60 seconds: "Are you changing your vote, or
not?" **Facilitator note:** an earlier draft of this Twist claimed several of Stevenson's own
inputs were flagged **(d)** (back-computed, not a direct leaderboard read) in Appendix A — that
claim does not hold up: Stevenson's actual Methodology-A inputs (Kills/Set 2.79, Blocks/Set 1.35)
carry no **(d)** marker in Appendix A; only her (unused) Attacks/Set does. Do not tell students
her inputs are "derived" — a sharp Hero who checks Appendix A directly will correctly call that
claim out, and the Twist's real, defensible point (the margin is thinner than realistic
measurement precision) stands without needing that claim at all. This does not hand anyone a new
number or resolve the case — it invalidates overconfidence in Methodology A's precision without
making Methodology B automatically correct (B's 23.4% margin is real, but Diane's specific
multiplier curve, Appendix E Note 3, is its own disclosed
assumption, equally open to challenge).

### Close

Re-vote. "Did we ask the right question at the start? What math was new to you today, and how
did you attack it?" Land on the real takeaway: two honest, real, fully-disclosed formulas,
applied to the exact same real data, produce two different winners *and* two different-looking
margins — and the choice of methodology is itself the decision, not a technicality standing in
front of the "real" answer.

### Lessons Learned

- A composite score is only as trustworthy as its narrowest input's precision — a 1.74% margin
  built partly on derived/estimated stats may not be a real margin at all.
- "Position-blind and consistent" and "position-aware and comparative" are both legitimate
  fairness principles that can point in opposite directions on the same real data.
- A scoring system's design choices (what counts as "unranked," how team success is weighted)
  are themselves decisions with consequences — not neutral plumbing.

### Standards Touched On

Mean; how to find the mean of a set of data; Negative Number; how to subtract, divide, and
multiply with negative numbers; how to divide and multiply decimal numbers; Rounding; how to
round a number to a specified place value; how to compare two or more values; how to evaluate an
expression with multiple operations without exponents (Order of Operations); Bar Graph; how to
create a scatter plot given a set of data.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch on Appendix A alone (no formulas yet); 30-second gut-instinct picks; stand/sit vote |
| 3:00–10:00 | Position defense: "Convince us your methodology is better, not just that your player is good" |
| 10:00–15:00 | Pressure-test the models: "Whose composite table is most fragile to a rounding choice?" |
| **15:00** | **DROP THE TWIST** — the (d)-derived-stat precision problem, delivered slowly, with pauses |
| 15:00–20:00 | Immediate recommit: who reverses their vote? "What just broke in your model?" |
| 20:00–30:00 | Threaded deep conflict: (1) consistency vs. positional fairness as competing values, (2) whether a 1.74% margin is meaningful at all given estimation error |
| 30:00–45:00 | Close, re-vote, reflection, Lessons Learned |

## Five Socratic questions

1. Methodology A's winning margin is 1.74% — smaller than the estimation error on several of the "(d)" derived statistics in Appendix A. Does a 1.74% margin mean anything at all, mathematically?
2. If Methodology A treats a missing national rank as "average" (z=0) rather than "zero," who does that convention help most, and who does it quietly punish?
3. Sydney Hilley's dominance under Methodology B comes from being compared only to other setters. Is that a fairer comparison, or is it just a comparison that was rigged the moment the category list was drawn up?
4. Wisconsin's #2 RPI — and the team-success bonus it buys Hilley and Peterson — is largely the product of one championship run. Should a single tournament outcome be allowed to swing an individual season-long award this much?
5. If you had to defend your chosen methodology to the players it didn't pick, what would you say to Anna Stevenson if the committee chose B, or to Sydney Hilley if the committee chose A?
