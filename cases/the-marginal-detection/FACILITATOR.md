# FACILITATOR.md — The Marginal Detection

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Marginal Detection · **Tier:** T2 (MS-core) · **Studio:** MS Adventure
**Standards:** Statistics And Probability/Displaying Data — Non-linear, Scatter Plot, Correlation,
and three "how to…" skills (line of best fit, box-and-whisker plot, scatter plot, identify
correlation), plus Data Analysis's Outlier and Quartiles — see `case.json.standards[]` for exact ids.

**Status:** `case-research` complete (2026-09-18). All `{{NEEDS_SOURCE: ...}}` placeholders are
resolved — two real, peer-reviewed astronomy sources (TESS precision [S1], Kepler's 7.1σ
threshold [S2]) plus two real organization/tool sources ([S3], [S4]) and one real comparison
figure ([S5]) are sourced; the candidate's exact light curve (MA1) and the survey's own follow-up
threshold (MA2) are disclosed Modeling Assumptions, because no publishable figure exists for
either. `case.json.balance.margin_pct` is a real, computed **19.2%**. Everything below is the
case of record, not a placeholder.

**Sensitivity note (SPEC §6):** ordinary scientific/workplace decision pressure — a survey lead
allocating a scarce shared telescope slot. No illness, death, or family hardship. Standard
facilitator handling suffices.

## Argument for A — Re-observe the marginal candidate

Under the naive line-of-best-fit read (Method 1, Appendix B), the dip's significance is
230.56 ppm ÷ 76.71 ppm = **3.006σ** — clearing the Sable Peak Survey's own 3.0 follow-up threshold
[MA2]. A's case is that the survey wrote its policy in exactly these terms, the candidate clears
the bar under the most commonly taught method (fit a trend, measure how far the dip falls from
it), and declining a slot on a candidate that meets the stated bar quietly moves the goalposts
without the team ever agreeing to move them. A straight-line fit is also the more familiar,
easier-to-audit method — any teammate can redo the same regression and get the same number.

## Argument for B — Abandon it, take the fresh target

Under the distribution-aware box-and-whisker read (Method 2, Appendix B), the same dip's
significance is 213.5 ppm ÷ 84.69 ppm = **2.521σ** — below the 3.0 threshold. B's real, honest
case is that Appendix A's baseline is visibly non-linear — a curved, not straight, drift across
the night — so fitting a straight line is the wrong tool for measuring "normal" noise here: it
can't distinguish real leftover static from the shape its straight line simply failed to capture,
and it folds both into one number that can mislead in either direction depending on where in the
curve the dip happens to fall. The box-and-whisker read makes no assumption about the drift's
shape at all; by that more conservative, assumption-light read, the candidate does not clear the
bar, and the scarce slot is better spent on a fresh target with no accumulated marginal history.

## The margin — real numbers, and how fragile this case actually is

`case.json.balance.margin_pct` = **19.2%**, within SPEC §2's 20% cap (close to it, deliberately —
see below). The arithmetic, in full (winner-minus-loser over loser, the corpus-standard
convention):

- **Method 1 (naive):** line fit to the 16 out-of-transit points gives residual SD = 76.71 ppm;
  the dip measured against the extended line is 230.56 ppm; **3.006 ÷ 3.0 threshold = clears it,
  by 0.006σ.**
- **Method 2 (robust):** Q1 = −42.5, Q3 = 71.75, IQR = 114.25, so 0.7413×IQR = 84.69 ppm; the dip
  measured against the out-of-transit median is 213.5 ppm; **2.521, below the 3.0 threshold by
  0.479σ.**
- **Margin:** (3.006 − 2.521) / 2.521 × 100 = **19.2%.**

**This case is deliberately tuned to straddle the 3.0 line** — that is the entire point, and it is
why the margin matters here in a different way than a dollar-cost case: the two methods don't just
disagree by a little, they land on *opposite sides of the survey's own decision rule*.
`sensitivity_model.py`'s mechanical ±50% flex sweep on `transit_dip_ppm` (MA1) finds the naive
reading stays numerically higher than the robust reading at every flexed value (the win/lose test
itself never flips) — but a −50% flex does breach the SPEC §2 20% margin cap (24.5%). A separate,
qualitative check (also in `sensitivity_model.py`, not part of the mechanical win/lose test) shows
what actually matters for the dilemma: at −50% dip depth, both methods fall below the 3.0
threshold (both agree: abandon); at +50%, both clear it (both agree: re-observe) — only the case's
own chosen middle value puts the two methods in genuine disagreement. `followup_threshold_sigma`
(MA2) is held fixed, not swept mechanically (moving it can't change which reading is numerically
larger), but the same qualitative check shows the live disagreement only survives for a threshold
roughly between 2.8 and 3.0. Both dials are disclosed in `case.json.sensitivity_disclosure[]` as
Category X. **Do not treat a student who argues the whole naive-vs-robust distinction is
manufactured, right at this exact threshold, as having missed the point — recognizing that the
disagreement lives in a narrow, chosen window is itself a sophisticated read of the case.**

## Five Socratic questions

1. Both methods use the same twenty numbers. How can they disagree about whether this candidate clears the bar?
2. Look at your scatter plot (D1) — does the night's drift actually look like a straight line, or does it curve? What does that do to a line-of-best-fit's residuals near the middle of the night?
3. The box-and-whisker method never tries to model a trend at all — is "ignore the shape of the data" actually more honest here, or is it throwing away real information the line-of-best-fit uses?
4. The team's own 3.0 threshold (Appendix B, MA2) is an internal policy, not a scientific law — if the team had set that threshold at 2.5 instead, would this still be a hard decision?
5. Kepler's real discovery threshold is 7.1σ — nowhere close to either of tonight's numbers. Does that make tonight's decision less important, or does it change what "worth a follow-up" should even mean?

## The trap

**A learner who computes only one of the two significance ratios — whichever their calculator or
spreadsheet's default trendline tool spits out first — and treats that single number as "the"
answer has fallen into the case's central trap.** The case has no single correct significance
ratio; it has two defensible methods that happen to disagree at exactly this candidate's numbers.
A pitch that reports only Method 1 (because it's the more familiar tool) or only Method 2 (because
it "sounds more rigorous") without ever explaining *why* the two methods diverge — the curved,
non-linear baseline — has not done Challenge 3's real work, even if it lands on a confident
recommendation.

**A second, related trap:** a student who correctly computes both numbers can still recommend the
wrong thing by treating "3.006 is basically the same as 2.521" as noise-level rounding rather than
as a genuine disagreement about whether the survey's own stated policy is met. The case is built
so that the *closeness* of the two numbers is exactly what makes the choice of method matter — not
a reason to shrug and average them.

## Twist

The twist lives in Appendix A's shape, not in withheld information — the case never adds new data
mid-discussion, so a facilitator who wants a live twist moment can manufacture one by asking the
room, before revealing Method 2's answer: "Given only Method 1's 3.006σ, would you approve the
slot?" then, after a vote, revealing Method 2's 2.521σ and asking Socratic Question 1 directly.
The reveal that "the same 20 numbers give two different verdicts depending only on how you
measure 'normal'" is the case's real invalidating moment for whichever side voted with total
confidence.

---

## Guide Notes — the anchor ladder (SPEC Section 7, anchor-ladder subsection)

### Intro

Frame the format: a survey lead has one scarce telescope slot and one marginal candidate that
either just clears or just misses the team's own follow-up bar, depending entirely on which of two
legitimate statistical methods she trusts.

### Launch

Read the Overview aloud. Stop at "Ingrid's cursor sits over the scheduling form, the cursor
blinking in the box marked TOMORROW'S SLOT." Ask the room: "Before you've seen a single number,
what would make you trust a 'marginal' detection enough to spend a scarce slot on it?"

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "Re-observe or abandon — show of hands." Record the split.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push the room past "is the dip real" toward "how do we even measure how big a dip is, relative to
normal noise, when normal noise isn't flat." Let the room sit with the fact that nobody has yet
agreed on a method.

### Anchor 3 — WHAT IS THE PROCESS?

Before computing anything, get the room to state the actual comparison method out loud: plot the
data (D1), fit a line and check whether it's a good description of the drift (D2), compute the
naive significance ratio (D3), then compute the distribution-aware ratio (D4) and compare both to
the 3.0 threshold. Re-ask: "Is 'is the dip real' still the right question, or is it actually 'which
method do we trust'?"

### Anchor 4 — WHAT DON'T WE KNOW?

Name the load-bearing unknowns explicitly: this candidate's exact overnight numbers and the
survey's own 3.0 threshold are both stated assumptions, not published facts — the noise scale is
bounded by real TESS precision data and the threshold is set well below Kepler's real, formal
7.1σ bar. "Which of these two assumptions would you most want to challenge, and why?"

### Data Deep Dive

Now open Appendices A–C. Run D1–D5 as a room, or have groups report out.

### Twist

Once D3's naive ratio (3.006σ) is on the table and the room has provisionally voted based on it,
reveal D4's robust ratio (2.521σ) and ask Socratic Question 1 directly: "The same twenty numbers —
how can they disagree?" Let the room discover that the answer is Appendix A's non-linear drift.

### Close

VOTE AGAIN. "Did the vote move? For the people who didn't move, what would it take to change your
mind?"

### Lessons Learned

The core transferable idea: "how big is normal noise" is not a single, objective number — it
depends on the method, and a curved (non-linear) trend can make two reasonable methods disagree by
a wide enough margin to flip a real decision. A second, equally real lesson: a threshold written as
a single clean number (3.0σ) can hide a real methodological choice underneath it.

### Standards Touched On

Non-linear, Scatter Plot, Correlation, Outlier, Quartiles; How to draw a line of best fit given a
set of data; How to create a box and whisker plot given a set of data; How to create a scatter
plot given a set of data; How to identify correlation given a scatter plot or set of data.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold read of the Overview, gut-check vote (Anchor 1) — no numbers shown yet |
| 3:00–8:00 | Position defense: "Convince us your slot decision is right, not just that it sounds cautious or bold" |
| 8:00–20:00 | Data Deep Dive — build the scatter plot (D1) and the line of best fit (D2) as a room; discuss why the drift is curved |
| 20:00–30:00 | Compute D3's naive ratio and D4's box-and-whisker ratio; confirm both numbers against the 3.0 threshold |
| **30:00** | **DROP THE TWIST** — reveal both ratios side by side and ask Socratic Question 1 |
| 30:00–38:00 | Pressure-test the case's assumptions: how close is 3.006 to 3.0, and what would a defensible challenge to the dip depth or the threshold itself actually change? |
| 38:00–45:00 | Close, re-vote, lessons learned |

## Cohort bands (SPEC Section 7, cohort-bands subsection)

| Band | Typical size | What changes |
|---|---|---|
| **Full (12–20)** | the size this case is written for | Anchors and the 45-minute timed plan run as written above |
| **Compressed (6–11)** | smaller room | Anchors 2–3 combine into one pass; the 20:00–30:00 dual-method build-out runs as a single worked example instead of small-group work; total runtime shortens proportionally |
| **1:1 / pair (1–2)** | tutoring context | No vote at Anchor 1 — a stated initial position instead; facilitator plays devil's advocate directly; the 30:00–38:00 sensitivity pressure-test still runs in full |
