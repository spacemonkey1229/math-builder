# Guide Notes: The Phasing Call

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — case.md
carries no marker comment for this by design (see the "Balance argument" guidance in `case-write`
SKILL.md); the balance argument, margin, and sensitivity notes live only here and in `case.json`'s
`balance` object.*

**Case:** The Phasing Call · **Tier:** T2 · **Band:** MS-core · **Studio:** MS Adventure
**Standards:** Pre-Calculus/Polar And Parametric — `pre-calculus-polar-coordinate`,
`pre-calculus-parametric-equation`, `pre-calculus-parameter`,
`pre-calculus-how-to-convert-a-point-between-rectangular-and-polar-coordinates`,
`pre-calculus-how-to-graph-a-polar-equation`,
`pre-calculus-how-to-eliminate-the-parameter-to-find-a-rectangular-equation` (the full group; this
case is a second/third touch beyond `Feedback`'s and `the-search-box`'s own coverage — none are
`new_coverage`, see `case.json.reinforcement_note`), plus three heavily-covered supporting skills
from Advanced Numbers/Percents and Measurement/Units. Exact ids in `case.json.standards[]`.

**Status:** Researched 2026-08-31. **`margin_pct` = 1991.18. Winner on the stated ratio metric:
Option A, The Fast-Track, by roughly 20x.** This fails SPEC §2's ~20% balance cap by about two
orders of magnitude on a literal reading — **waived under MCS-46** (`case.json.balance_test_waiver`;
see `DOCTRINE_LEDGER.md`). The waiver does not mean "treat this as close." It means the opposite:
this case is not built for a Socratic debate over which side wins — Option A wins, clearly, on
real, honestly-sourced numbers, and every Hero should land there. **What this case is actually
built to teach is why the margin is this large** — that two independently-real ratios, each modest
on its own, compound multiplicatively rather than trade off, and that a landslide this size is not
guessable from the premise. It has to be computed. The facilitator's job is to run an audit of the
analysis, not a debate.

## The real numbers (facilitator reference — never appears in case.md)

- Reserve-hours term: Fast-Track retains 94.8 h / 100.8 h (94.0%) of the vehicle's fixed
  autonomous-flight allowance; Phasing Climb retains 40.8 h (40.5%). Ratio ≈ 2.3x, Fast-Track ahead.
- Phase-angle-tolerance term: Fast-Track's workable window is 30° of 360° (2.5 of 30 launch days);
  Phasing Climb's is 270° of 360° (22.5 of 30 launch days). Ratio ≈ 9x, Phasing Climb ahead.
- Primary metric = reserve-hours ÷ workable-launch-days: Fast-Track 37.92 h/day; Phasing Climb
  1.81 h/day. Because the metric is a straight ratio (not a weighted sum), the 9x term Phasing Climb
  wins on lands in the *denominator* of Fast-Track's number and the *denominator* of Phasing Climb's
  number the same way — it does not partially offset the 2.3x term Fast-Track wins on, it
  compounds with it: 2.3x × 9x ≈ 20x (1991.18%). See `case.json.balance.margin_note` for the full
  derivation and `sensitivity_model.py` for a runnable reproduction.
- Every plausible real-precedent transit-time combination researched (3–6 h Fast-Track; 24–60 h
  Phasing Climb) lands the ratio between ~11x and ~21x. The blowout is structural to the real,
  sourced figures — not an artifact of picking one number over another inside its documented range.

## Intro

Frame the format before anything else: this is a real trajectory sign-off with a flight plan on
the other side of it, not a worksheet. Name the opener — "You're Talia Brooks. Whichever profile
you recommend becomes the number written into the flight plan. There's no 'we'll see' — you sign
one." Let the stakes land before moving to the Launch.

## Launch

Show the two rendezvous profiles side by side (illustrative shapes, not the case's real numbers) —
one short and steep, one long and gradual — with no other context. Ask: "If all you knew was which
one gets there first, which would you pick, right now?" Take the answers without correcting anyone.
Most rooms will expect this to be close, a genuine trade-off between "gets there fastest" and
"forgives more launch days" — that instinct is worth recording out loud, because the case's whole
point is that the real numbers do not bear it out.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the Phasing Climb — the profile that opens the most
launch days?" Show of hands, both options, no discussion. Record the count — Close will ask again.

## Anchor 2 — What is the problem we're solving?

**"Is 'gets there first' the right question?" · "What do you mean by 'more reserve,' and what do
you mean by 'more flexible'?"**

Push the room to state the actual metric before touching an appendix: not "which profile is
faster" and not "which profile forgives more launch days," but hours of reserve remaining at
docking *per calendar day of launch flexibility gained* — a ratio of two real, independently-sourced
quantities, not either one alone. If the room lands on "we need to divide one real number by
another real number, not just eyeball two separate advantages," the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Make the room name the steps before opening an appendix: (1) convert the station's tracked position
from polar to rectangular, (2) write each profile's closing position as a function of a parameter,
(3) eliminate that parameter to get an equation you can check against the station's position, (4)
verify each profile really reaches the station when it claims to, (5) work out what percent of the
reserve each profile burns getting there, (6) graph and compare each profile's phase-angle tolerance
band, (7) count workable launch days per calendar from that graph, (8) divide reserve-hours by
workable-days for each profile and compare. Re-ask: "Now that we can see the steps, is our question
still the right one?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the honest gaps: Appendix A's tracked bearing/range (MA1), contract deadline (MA2), and
minimum reserve floor (MA3) are all stated, disclosed assumptions for a fictional company and
mission — none of them changes which profile wins D7's ratio (MA1 affects both profiles equally;
MA2 and MA3 are pass/fail floors both profiles clear comfortably under the case's real figures).
MA4 (modeling each profile as one constant angular rate instead of its real multi-burn sequence)
only affects the D2/D3 algebra, not the D4–D7 comparison, which runs on each profile's real, sourced
total transit time regardless of how that time is broken into burns. Ask: "Which of these
assumptions, if it moved, would actually change who wins — and which ones just change the specific
number without changing the answer?" A sharp Hero should be able to name that none of MA1–MA4 is
where the real margin comes from — Appendix B and D's *sourced* figures are.

## Data Deep Dive

Now, and only now, open Appendices A–D and work D1–D7. Cold-call for D7 specifically — this is
where a Hero who correctly computed both the reserve percentages (D4) and the launch-day counts
(D6) but never divided one by the other for both profiles will not yet see the scale of the result.

**Facilitator-only arithmetic note.** Reserve-hours: Fast-Track 100.8 − 6 = 94.8 h; Phasing Climb
100.8 − 60 = 40.8 h. Workable launch-days per 30-day calendar: Fast-Track 30 × (30°/360°) = 2.5
days; Phasing Climb 30 × (270°/360°) = 22.5 days. D7 ratio: Fast-Track 94.8 ÷ 2.5 = 37.92 h/day;
Phasing Climb 40.8 ÷ 22.5 = 1.81 h/day. Percent difference (37.92 − 1.81) / 1.81 × 100 ≈ 1991.18%.
Full derivation in `case.json.balance.margin_note`; reproduced mechanically in
`sensitivity_model.py`.

## Twist — drop this once D7 is on the board, roughly 15 minutes in

Deliver slowly:

"Somebody on the team says: 'Wait — the Phasing Climb wins on flexibility by 9x, and the Fast-Track
only wins on reserve by about 2.3x. Shouldn't those partially cancel out? Why isn't this close?'"

Let the room sit with that. Then: "The primary metric isn't reserve-hours *plus* some flexibility
credit — it's reserve-hours *divided by* workable-launch-days. When two real advantages both point
the same direction inside a single ratio like that, they don't average or partially offset each
other the way they would if you added them — they compound. A profile that is 2.3x better in the
numerator **and** 9x worse in the denominator doesn't land near a wash; it lands at roughly
2.3x × 9x ≈ 20x apart, because dividing by a much smaller number has the same effect as multiplying
by its reciprocal."

**Facilitator-only: what this actually is, and is not.** This is not a "did you pick the right
side" reveal for the case as actually asked — Option A is the correct answer to D7's stated ratio
metric, and a Hero who reached it with correct D1–D7 arithmetic has not been tricked. The twist is
that the *size* of the win is not what a reasonable pre-computation intuition would predict, and
the reason is a real mathematical mechanism (ratio vs. sum), not an authorial trick. Ask directly:
"If this case had instead asked you to *add* an evenly-weighted reserve-fraction score and a
phase-angle-tolerance-fraction score, instead of dividing one by the other, would the Phasing Climb
have a real shot at winning?" **The mechanically verified answer is yes — under that specific,
evenly-weighted (50/50) additive construction, using the exact same real D4/D6 figures, the Phasing
Climb actually wins** (see `sensitivity_model.py`'s `evaluate_twist()`: reserve-fraction/tolerance-fraction
scores of roughly 0.512 for the Fast-Track vs. 0.577 for the Phasing Climb). Nothing about the real
world changed — only how the two real quantities were combined. This is the real content of the
twist: the metric's *shape*, not just its inputs, decides both how large a result looks and, in
this case, which option a different reasonable construction would even recommend.

**Facilitator-only, read before presenting this as settled: the flip itself is a knife-edge
result, not a robust one — say so if a Hero pushes on it.** The 0.512-vs-0.577 gap is only about
12.7% apart, nothing like D7's ~20x landslide, and it depends on the exact 50/50 weighting: solving
for the weight `w` on the reserve-fraction term at which the two scores tie gives `w ≈ 0.554` —
tilt the weighting only slightly toward reserve (say `w = 0.60`, an equally defensible choice, since
one could reasonably argue reserve is a safety margin and deserves more weight than schedule
convenience) and the Fast-Track wins again. Unlike D7's own ratio result — which the case's research
found stable across the *entire* plausible range of real transit-time figures (~11x to ~21x, never
flipping) — this additive-construction flip has no such robustness and none is claimed. The correct,
honest framing for a Hero is: "a specific, reasonable alternate construction flips the winner, which
proves the ratio's landslide is a property of *that* choice and not a law of nature — but the flip
itself is fragile to the weighting choice, unlike D7's real result, which is not." Do not let the
twist land as "additive scoring proves B should win" — it proves only that metric construction
matters, which is the actual, intended lesson. D7's own ratio construction is the one this case is
actually graded on and the one with a real operational rationale (reserve *per* day of flexibility,
not reserve *plus* flexibility on an arbitrary common scale).

## Immediate recommit

Re-vote immediately. Ask by name: "Does this change your recommendation — or does it just change
how surprised you are by the *size* of the gap you already computed?" Most Heroes who did D1–D7
correctly should not flip; the point is whether they can now explain *why* the gap is this large,
not whether they change their answer.

## Deep conflict — two threads (20–30 min)

1. **Ratio vs. sum: why compounding beats trade-off.** The room already computed a 2.3x reserve
   advantage for A and a 9x flexibility advantage for B. Why does dividing produce ~20x apart
   instead of something closer to "these mostly cancel"? Walk a Hero through a same-units,
   evenly-weighted additive score built from the real D4/D6 figures instead of a ratio, and show it
   does not produce a 20x gap — the compounding is a property of the ratio construction, not of the
   raw numbers alone.
2. **What would actually have to change.** D8 asks what would have to change about either profile
   for the recommendation to flip. Push past "the numbers would have to be different" to a specific
   answer: since metric(A)/metric(B) ≈ 20, closing the gap to parity requires roughly a 20x
   combined swing in the reserve-hours ratio and/or the phase-angle-tolerance ratio — for instance,
   the Fast-Track's tolerance band would need to widen from 30° to somewhere near its own 270°
   figure (erasing the entire phase-angle asymmetry) before the two profiles would even approach a
   fair fight on this metric. That is a specific, checkable claim a Hero should be able to state,
   not a vague "if things were different."

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both rendezvous profiles side by side, cold-call for a gut read, no numbers yet |
| 3:00–10:00 | Position defense — *"Walk us through your D7 ratio — which profile wins, and by roughly how much?"* |
| 10:00–15:00 | Pressure-test the process — *"Which of your D1–D6 steps, if it were wrong, would change who wins — and which ones just change the specific numbers?"* |
| **15:00** | **DROP THE TWIST** — why a 2.3x term and a 9x term compound to ~20x instead of partially canceling |
| 15:00–20:00 | Immediate recommit — does the recommendation change, or just the room's read on the *size* of the gap |
| 20:00–30:00 | Threaded deep conflict (ratio vs. additive scoring; what a real flip would actually require) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

The trap is not "picking the wrong option" — it is under-estimating the size of the correct
answer before computing it, and specifically assuming the reserve-hours term and the
phase-angle-tolerance term should carry roughly equal weight, the way a Hero's intuition would
treat two "modest" advantages pointing in opposite directions. A Hero who reasons "Fast-Track wins
reserve by a bit, Phasing Climb wins flexibility by a bit more, so this is probably a close call
that favors B" has made a real, specific analysis mistake: treating a divided metric as if it
behaved like a weighted sum. The second, related trap is stopping at D4 or D6 alone and never
actually computing D7's division — a Hero who reports "the Fast-Track keeps more reserve" and "the
Phasing Climb opens more launch days" as two separate, competing facts, without dividing one by the
other, will never see that the two facts do not offset — they multiply.

## Socratic questions

1. Your D7 ratio divides reserve-hours by workable-launch-days for each profile — which appendix figure is the numerator, which is the denominator, and why is that order (not the reverse) the one the case's primary metric actually asks for?
2. Your D6 answer converts Appendix D's phase-angle tolerance band into a number of workable launch days — where does the full 360° range enter your arithmetic, and would your answer change if the launch calendar were twice as long?
3. The Fast-Track wins on reserve-hours by roughly 2.3x and the Phasing Climb wins on phase-angle tolerance by roughly 9x — why does the D7 ratio end up favoring the Fast-Track by roughly 20x, an amount neither individual advantage alone would suggest, instead of landing somewhere between the two or favoring the Phasing Climb?
4. Suppose the Fast-Track's phase-angle tolerance band in Appendix D were quite a bit wider than the 30° this case states, closer to matching the Phasing Climb's own tolerance — would that fully close the D7 gap by itself, or would the reserve-hours term still leave a real gap, and what is the smallest change to a single Appendix B or D figure that would make this a genuinely close call?
5. If D7 had instead asked you to build a single score by adding an evenly-weighted reserve-based number and a flexibility-based number, instead of dividing one by the other, would you expect anything like a 20x gap between the two profiles, and what does that tell you about whether the size of a result depends on the inputs alone or also on how you choose to combine them?

## Close

**VOTE AGAIN.** "Did your recommendation change — or just your sense of how large the real gap
is?" Ask what math was new to each Hero, and specifically whether eliminating the parameter in D3,
graphing the polar boundary in D5, or dividing D4 by D6 in D7 was the step that actually surprised
them.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes correctly predicted, before computing D7, that the two "modest" per-term
  advantages (2.3x and 9x) would compound into a ~20x gap rather than partially cancel — or whether
  most rooms expected a much closer race until the arithmetic forced the surprise.
- Whether the additive-vs-ratio reframing in Anchor 4/the Twist landed as a genuine new insight
  about metric construction, or felt like a technicality once the winner was already settled.
- Whether any Hero, prompted by Socratic question 4/D8, could actually name the specific change
  (roughly a 20x combined swing, concretely: the Fast-Track's tolerance band widening toward the
  Phasing Climb's own 270° figure) that would be needed to flip or even meaningfully close this
  case's real margin.

## Standards Touched On

Polar Coordinate; Parametric Equation; Parameter; Percent; How to convert a point between
rectangular and polar coordinates; How to graph a polar equation; How to eliminate the parameter to
find a rectangular equation; How to find the percent of a number; How to convert an amount with
compound units.

## Facilitator note — sensitivity (SPEC §6)

None required. This case carries no illness, death, financial-hardship, or other protected-subject
stakes — it is a routine mission-design and launch-scheduling trade-off between two legitimate,
professionally defensible rendezvous strategies, comparable in register to Wind Triangle or
Navigation. `case.json.balance_test_waiver` documents the separate, unrelated MCS-46 exception this
case carries for its balance-test margin — a landslide margin driven by real, sourced figures, not a
modeling shortcut, kept because the setup still forces genuine multi-step analysis and the
magnitude itself is the pedagogical payoff (see the Status note above).
