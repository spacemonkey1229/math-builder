# Facilitator Guide — Biostatician

**Sensitive-content flag (SPEC.md Section 6):** this case touches weight-based discrimination in
healthcare, a topic some learners may have direct personal experience with. Keep the discussion
about the *data and the decision*, not about any individual student's body or health. If the
conversation drifts toward a specific learner's experience, redirect gently to the numbers.

---

## Intro

Frame the format: this is a real decision a hospital biostatistician has to defend to her CEO,
using a real, published dataset. There is no "correct" answer key — there is a defensible
argument on each side, and the room's job is to find both, then decide which one wins.

**Opener:** "Ingrid Robertson has 109 real physician responses in front of her, and her CEO wants
one word: recommend the training, or don't. What's your gut answer, before you've touched a
single number?"

## Launch

Show the case's Overview (or read it aloud) and Appendix C's complaint-count table (15/435 last
quarter, 82/1,458 this year). Do not show Appendix B's dataset yet — that's the Data Deep Dive,
deliberately later.

## Anchor 1 — Take a Stand and Vote

No reasoning yet, just commit. "Show of hands: who recommends the training? Who doesn't? Who's
not sure?" Record the split — you'll return to it at the Close.

"Is anyone courageous enough to stand behind 'don't recommend it' with the complaint numbers
climbing the way they are?"

## Anchor 2 — What Is The Problem We're Solving?

"Is this the right question? What do you mean by 'discriminate' — does it mean physicians spend
less time, order fewer tests, something else? What would actually convince you either way?"

Let confusion grow deliberately here. A common early stumble: conflating the *complaint counts*
(which are not evidence of anything on their own — no baseline, no per-physician breakdown) with
the *time-spent data* (which is the case's real evidence). "Wow, this is a harder question to
even define than it looked."

## Anchor 3 — What Is The Process?

"If we go through Appendix B and find real differences in time spent, how do we decide if
they're big enough to matter? Big enough to spend $265-per-physician on?"

Re-ask: "Is our question still the right question — or is it actually two questions (is there a
real gap? and is fixing it worth the cost?) that we've been treating as one?"

## Anchor 4 — What Don't We Know?

"Do we need to make assumptions? Which ones are load-bearing?" Surface, without answering yet:

- Who counts as "its physicians" if the training is approved — all 1,852, or just the 1,228
  primary care physicians the study actually surveyed? (Appendix D, MA1)
- Which profit years should count as "typical" when judging whether $265/physician is
  affordable? (Appendix D, MA2)
- 13 of the 122 physicians who got a chart never had a time answer recorded. Does that matter?
  (Appendix D, MA3 — this is the seed for the Twist, don't over-explain it yet)

## Data Deep Dive

Now, and only now, hand out or reveal Appendix B's full 109-row dataset. Let the room work D1–D5
(histograms, box plots, the percent-above-median comparison, the gender/age mean comparison, the
outlier check). This typically takes the bulk of the working session before discussion.

## Twist

**Named trap, so you're watching for it, not discovering it live:** a Hero computes the mean or
median time gap between average-weight and heavier patients, calls it "proof of bias," and
recommends the training — without ever asking whether the 109 recorded responses are a fair
stand-in for the 122 physicians who were actually surveyed. This is the most natural reading of
the data and the easiest way to reach a confident, under-examined answer either direction.

**The twist, dropped around the 15-minute mark:** "One more thing. 122 physicians were mailed a
chart. Only 109 answers are on record. That's 13 missing — about 1 in 9. Here's the breakdown by
which chart they got: if the 122 physicians split evenly three ways across weight condition,
you'd expect about 41 responses per group. The overweight and obese groups came in close to that
(38 each — short about 3 apiece). The average-weight group came in at 33 — short about 8, roughly
double either of the other groups' shortfall, and more than half of everything missing across the
whole study. The physicians who got a completely unremarkable, average-weight chart were the ones
most likely to never send back a time estimate at all."

Follow-up: **"What just broke in your model? Were you wrong about the gap being real — or just
missing information about how big it really is?"** Push toward the actual open question: if
"boring chart → skip the survey" is the reason those 13 are missing, does that make the measured
26.6% gap too *big* (some of the missing average-weight physicians might have said something
short and unremarkable, dragging the average-weight *mean* down if they'd answered) or too
*small* (physicians who felt strongly enough about an overweight/obese chart to have an opinion
may have been more likely to answer at all, in either direction)? There is no single correct
resolution — that's the point. The case does not resolve this; it asks the Hero to state which
reading they're using and defend it (SPEC.md Section 3's T4 requirement).

**Soundness check (both readings hold):** Under a *sequential* reading (a Hero first computes the
26.6% gap from the 109 recorded responses, then is told about the missing 13), the twist directly
undercuts the confidence of a conclusion already reached — the natural reaction is "wait, is my
26.6% even the right number?" Under a *simultaneous* reading (a Hero is handed Appendix B and
Appendix D's Assumption 3 together from the start, before computing anything), the twist still
lands: it forces the Hero to state, in writing, which nonresponse-mechanism assumption they're
using *before* they can defend a specific gap percentage, rather than computing first and
rationalizing second. Neither reading makes the twist a no-op, and neither reading resolves it
for the Hero — both leave "is the missingness random?" as a genuinely open, stated assumption.
This twist does not touch the training-cost side of the ledger (Appendix C, D) at all, so it
never collides with the profit-window or training-scope assumptions.

## Close

**Re-vote.** "Did we ask the right question? Who's changed their mind since Anchor 1, and why?"

"What math was new to you today, and how did you attack it?" (percent-above-median, comparing a
gap to a spread rather than just eyeballing two means, reasoning about missing data)

## Lessons Learned

From the original 2021-22 Guide Notes and this conversion: the strongest discussions did not
settle on "recommend" or "don't recommend" quickly — the room that spent real time on Anchor 2
(defining what "discriminate" even means, operationally, before touching a calculator) produced
sharper D3/D4 work than a room that jumped straight to computing. The complaint-count trap (see
case.md's facilitator-only Balance Argument) is easy to fall into precisely because it's the
first number in Background — watch for a Hero anchoring on it before ever opening Appendix B.

## Standards Touched On

See `case.json.standards[]` and Appendix G of case.md for the full verbatim list: Mean, Median,
Range, Quartiles, Outlier, Histogram, Box And Whisker Plot, Percent, and their associated
"how to…" procedures.

---

## Five Socratic Questions

1. Your D3 work shows roughly three-quarters of average-weight patients got *more* time than the overweight group's median, and a similar fraction got more time than the obese group's median (22.5 vs. 20 minutes) — why might those two percentages land so close together even though the medians themselves are different?
2. You have both a mean gap and a median gap between the average-weight and heavier groups, and they don't tell exactly the same story — which one would you put in front of a hospital CEO, and why, given what the obese group's box plot (D2) shows about its outlier(s)?
3. Your D4 table breaks the data down by gender and by age — if neither split shows a gap anywhere near as large as the weight-status gap, what does that do to an argument that "physicians are just busier with older or male patients, not weight-biased"?
4. The training costs $265 per physician — multiply that out for the physician count you chose under MA1, compare it to the typical-year profit you chose under MA2, and tell me: at what physician count would that total cost stop being smaller than the size of the 26.6% gap you measured?
5. Thirteen of 122 physicians never sent back a time estimate, and they weren't missing evenly — what's your best guess for why the "average-weight" chart's physicians were the least likely to respond, and does that guess make you trust the measured gap more, or less?

---

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second gut-check commitments, stand/sit vote at Anchor 1 — no reasoning yet |
| 3:00–10:00 | Position defense: "Convince us why it's the right call, not just a defensible one" |
| 10:00–15:00 | Pressure-test the models: "Whose recommendation is resting on the shakiest number?" (steer toward the complaint-count trap if nobody's found it yet) |
| **15:00** | **DROP THE TWIST** — the 13 missing responses, delivered slowly, with the actual shortfall numbers |
| 15:00–20:00 | Immediate recommit: who reverses, who holds? "What just broke — was your gap wrong, or just uncertain?" |
| 20:00–30:00 | Threaded deep conflict, 2–3 named threads: (a) mean vs. median as the "right" summary statistic given the obese group's outlier(s); (b) the training-scope assumption (MA1) vs. the profit-window assumption (MA2) — which one a Hero picks changes the cost side of the ledger more; (c) whether one single-scenario study (a migraine visit) should drive a hospital-wide policy at all |
| 30:00–45:00 | Close, re-vote, reflection, Lessons Learned |

---

## Sensitivity Note

`cases/biostatician/sensitivity_model.py` flexes the case's two genuine stated assumptions
(Appendix D MA1 — how many physicians the training covers; MA2 — how many profit years count as
"typical") by ±50% each, against the case's own recorded base margin of **13.1 percentage
points** (`case.json.balance.margin_pct`). **Result: the winner never flips** — Option A
(recommend) leads at every tested flex of either dial, and in the case's own percentage-point
framing the margin stays a defensible spread throughout (worst case: +50% on
`trained_physician_count`, margin narrows to 6.4 percentage points; -50% on the same dial widens
it to 19.9 points; -50% on `profit_window_years` widens it to 17.4 points).

That said, this case's own automated Tier 2 probe (`tier2_probes.py`, which checks SPEC Section
2's 20% cap using a *relative*-margin formula rather than the case's own percentage-point framing)
mechanically flags a cap breach on both dials at both flex directions, because B (the training
cost as a percent of profit) is itself a small percentage and the relative formula amplifies any
change to it. This is disclosed, not eliminated, in `case.json.sensitivity_disclosure[]` as a
Category F (irreducible forecast uncertainty) finding on both `trained_physician_count` and
`profit_window_years`: neither how many physicians would actually enroll nor which future year
counts as "typical" is knowable in advance, and B is bounded above by the case's own given data
(1,852 physicians, 6 years of history) — no honest retune of either dial raises B enough to satisfy
the relative-margin formula. This is a real, disclosed property of the case, not a claim that the
decision is easy: the *evidentiary* question (does the 26.6% gap mean what a Hero thinks it means,
given the missing-data twist) is where the case's real difficulty lives, not the cost-vs-benefit
arithmetic. See `case.json.balance.stability` and `case.json.sensitivity_disclosure[]` for the
full figures.

This case also touches a real, contested-adjacent claim worth naming for a facilitator: the
Overview's premise (do physicians treat heavier patients differently) is a real, live topic in
public health research, not settled science with one universally agreed effect size. Appendix A
is explicit that this case's dataset comes from one study design (a migraine-visit vignette); a
Hero should not walk away believing this proves a universal clinical bias beyond what the data
actually shows.

---

## Cohort Bands

| Band | Typical size | What changes |
|---|---|---|
| **Full (12–20)** | Anchors 2–3 run as written, with real debate over what "discriminate" means operationally before any calculator comes out; the Twist reveal (15:00) produces an audible reaction once the room realizes the missing-13 breakdown isn't even across groups. |
| **Compressed (6–11)** | Anchors 2–3 combine into a single pass; D1–D2's six charts (3 histograms + 3 box plots) are split so each pair only builds 2 of the 6 before comparing as a full group, rather than every Hero building all six. |
| **1:1 / pair (1–2)** | No vote to take at Anchor 1 — the Hero states an initial position instead of a cold-call. The guide plays devil's advocate directly, specifically defending whichever side the Hero did *not* pick, to see whether the Hero catches the complaint-count trap or the missing-data twist unprompted. |
