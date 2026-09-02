# Guide Notes: The Stake-Out

**Case:** The Stake-Out · **Tier:** T2 · **Band:** MS-core · **Studio:** MS Adventure
**Standards:** Geometry/Fundamentals Of Geometry (all 13 currently-n=1 skills) plus three
round-out skills (unit conversion, percent-of-a-number, comparing values) — see
`case.json.standards[]` for the exact ids. See `case.json.reinforcement_note` for the full
coverage justification.

**Researched 2026-09-01; `case-qa` Tier 2 PASS 2026-09-01 (see `QA_REPORT.md`).** All 22 research
placeholders are resolved: 12 to real cited figures, 10 to disclosed Modeling Assumptions (see
`cases/the-stake-out/RESEARCH_LOG.md` for the full trail and `case.json.modeling_assumptions[]`
for the MA table). `margin_pct` = **19.9%** (retuned 2026-09-01 from an original 47.4%; see
`RESEARCH_LOG.md`), winner = **Option A (Total Station Polar Staking)**. Cleared to run with a
room.

**Read this before running the room:** the margin is real but not robust. It is computed from
five Modeling Assumptions (MA1–MA5), and MA5 (near-structure RTK multipath degradation, retuned to
+17 mm RMS from an original +25 mm RMS to bring the margin under SPEC.md §2's ~20% cap) can flip
the winner to Option B if the true value is below its breakeven of ~13.4 mm — a value squarely
inside the same "several centimeters" literature range MA5 was drawn from. The retuned value sits
only ~3.6 mm above that breakeven (versus ~11.6 mm before the retune), so MA5 is, if anything, a
*more* fragile single point of failure now than it was at the old, unbalanced margin — a live
discussion point, not a fixed fact. See "The margin" below for the full breakeven analysis.

> **Run-of-show box (read before facilitating).** margin_pct = **19.9%**, winner = **Option A
> (Total Station Polar Staking)**. Option A wins on accuracy-driven expected time (≈26.0 min/corner
> vs. Option B's ≈31.2 min/corner) — but the whole result rests on MA5 (near-structure GNSS
> multipath, +17 mm RMS), which sits only ~3.6 mm above its own ~13.4 mm breakeven. Have ready: the
> two arguments below, the five Socratic questions, the pitfall (stopping at D5's accuracy table
> instead of pricing D6's time), and the skills this case exercises (see "Standards Touched On").
> Sensitivity note is reproduced in full near the end of this file.

## Argument for A (Total Station Polar Staking)

Total Station Polar Staking's real combined accuracy margin (EDM + angular error) is **≈1.3 mm**
against the sourced 13 mm tolerance — a huge cushion, effectively zero rework risk at every
corner it stakes, including the obstructed ones, once the corner is actually staked. Its real
weakness is entirely a time cost, not an accuracy one: the second instrument setup the
obstruction forces (stated at 20 min, MA3) is a known, one-time time penalty at those corners,
not a recurring accuracy risk that follows the method to every future job.

## Argument for B (GNSS/RTK Coordinate Staking)

GNSS/RTK Coordinate Staking needs no backsight or sightline at all, so it never pays the
second-setup time cost the obstruction forces on Option A — and its raw per-point throughput (up
to 500 points/hour in open terrain, a real cited industry figure, S8) is far faster than any
sightline-dependent method. Its real weakness is accuracy margin, not time: its open-sky spec
already leaves only **8.5 mm** of cushion inside the same 13 mm tolerance band, and the same
structure that costs Option A a time penalty is a real, literature-documented multipath source
(S6, S7) that pushes GNSS/RTK's combined accuracy at an obstructed corner out to **≈19.0 mm** —
still well past the tolerance — under the case's stated Modeling Assumption for the degradation
magnitude (MA5, +17 mm RMS, retuned 2026-09-01 from an original +25 mm RMS).

## The margin

**`case.json.balance.margin_pct` = 19.9%. Winner: Option A (Total Station Polar Staking).**
*(Retuned 2026-09-01 from an original 47.4% margin — see RESEARCH_LOG.md.)*

Computed as expected total minutes per obstructed corner:
- Option A = base layout (6 min, MA1) + second setup (20 min, MA3) + (miss probability × rework
  [MA4]). Miss probability ≈ 0% (1.3 mm accuracy vs. 13 mm tolerance) → **total ≈ 26.0 min**.
- Option B = base layout (3 min, MA2) + (miss probability × rework [MA4]). Miss probability ≈
  62.6% (19.0 mm combined accuracy vs. 13 mm tolerance, modeled as a 2D circular-normal radial
  error) → **total ≈ 31.2 min**.
- margin_pct = (31.2 − 26.0) / 26.0 × 100 ≈ **19.9%**, Option A wins.

**This margin was originally 47.4% (at MA5 = +25 mm RMS), which exceeded SPEC.md §2's ~20%
unbalanced-case cap. MA5 was retuned to +17 mm RMS** — a defensible low-to-mid point in the same
10–50 mm literature-anchored range it was already drawn from (the original 25 mm sat at that
range's high end) — bringing the margin to 19.9%. **This margin is smaller now but not more
robust.** MA5's breakeven is unchanged at **≈13.4 mm** (a function of the tolerance and open-sky
spec, not of MA5's chosen value): below it, Option B's faster base time wins outright instead. At
the retuned 17 mm, the case sits only ~3.6 mm above that breakeven — versus ~11.6 mm at the old 25
mm value — so MA5 is, if anything, a *more* fragile single point of failure post-retune. Two
secondary flip risks shifted too, both tighter than before: MA3 (second setup time) now breaks
even at ~25.2 min against its stated 20 min (was ~32 min before the retune), and MA4 (rework time)
now breaks even at ~36.7 min against its stated 45 min (was ~29 min before the retune). See
`case.json.modeling_assumptions[]` and `RESEARCH_LOG.md` for the full derivation and every
assumption's basis.

## Anchor ladder (SPEC §7.1)

### Intro

Frame the format: a real job-site call with real consequences (a tear-out and re-pour if wrong),
not a worksheet. Name the opener: "You are Renata Cruz. Daylight is running out. One corner left.
Both of your tools are fighting the same wall. Your foreman is trusting you to make this call
yourself."

### Launch

Read the Overview aloud, stop at "the one corner where both of her tools are working against the
same wall," and ask: "Before any numbers — just from that framing — which tool would you trust
more at that one corner, and why?"

### Anchor 1 — Take a stand and vote

"Is anyone courageous enough to stand with Total Station Polar Staking — the one that needs a
second setup?" Count hands. "And GNSS/RTK — the one that's faster but fighting the same wall for
accuracy?" Count hands. Record the split.

### Anchor 2 — What is the problem we're solving?

Let confusion grow. Heroes will want to jump to "which one is more accurate" — push instead: "Is
this actually a question about accuracy, or about time? Can a method be more accurate and still be
the worse choice?" The room should arrive at "we need one metric that folds accuracy risk INTO a
time cost" before Anchor 3.

### Anchor 3 — What is the process?

Walk the room toward: classify the unobstructed-corner angle (D1), diagram the second setup as a
transversal crossing the original baseline (D2), prove the two baselines are parallel (D3), check
whether each method's marked point is congruent to the target within tolerance (D4), build the
accuracy-margin table (D5), then combine accuracy risk and time cost into one total-minutes
recommendation (D6).

### Anchor 4 — What don't we know?

Surface honestly: the exact multipath degradation at this specific distance/structure (MA5) has no
single published figure — only a real, peer-reviewed "several centimeters" range; the base layout
times, second-setup time, and rework time (MA1-MA4) are all disclosed scenario assumptions, not
published figures. Ask: "Which of these, if it moved, would actually flip your Anchor 1 vote?"
(Good answer: MA5 — it is the case's real fault line, see the Twist below.)

### Data Deep Dive

Walk D1 through D6 together. Reveal Appendix A's 13 mm tolerance, then Appendix B/C's real
combined-accuracy figures (1.3 mm vs. 19.0 mm at an obstructed corner), then Appendix E's derived
miss probabilities and the D6 total-time comparison: Option A ≈26.0 min, Option B ≈31.2 min,
margin 19.9% favoring A. Cold-call specifically for whether a Hero got past D5's accuracy table to
D6's actual time-cost combination, since the pitfall lives exactly at that seam.

### Twist

MA5 is the case's real fault line. Reveal that the case's own multipath assumption (+17 mm RMS,
itself already a retune off an original +25 mm RMS that ran too high) still sits close to the low
side of the literature's documented range, and ask the room to defend a lower value (say 10-13 mm)
instead — at which point Option B's total time (≈20-27 min) undercuts Option A's fixed 26 min, and
the recommendation flips. This is not a fabricated twist; it is the case's own real, disclosed
sensitivity (MA5's breakeven of ≈13.4 mm sits only ≈3.6 mm below the case's stated 17 mm value).

### Close

Re-vote. Compare against the Anchor 1 tally. "Did we ask the right question at Anchor 2? Was this
ever really about which method is more accurate, or about which single assumption the entire
recommendation actually rests on?"

### Lessons Learned

- A method with more accuracy margin is not automatically the better choice once time is also
  priced in — the case's primary metric folds a rework-probability cost INTO a time total
  specifically so accuracy and time can be compared on one scale.
- One physical obstruction can threaten two completely different technologies through two
  completely different failure modes (a blocked sightline vs. signal multipath) — recognizing
  that it's the same root cause is part of correctly scoping D2-D3's second-setup geometry.
- A margin that rests on one disclosed Modeling Assumption (here, MA5) close to its own breakeven
  is a genuinely fragile recommendation, and a good pitch says so rather than presenting 19.9% as
  a settled fact.

### Standards Touched On

Geometry/Fundamentals Of Geometry — Ray, Degree, Acute Angle, Obtuse Angle, Right Angle,
Transversal Line, Congruent, Supplementary Angles, Complementary Angles, Vertical Angles, Adjacent
Angles, and both how-to-find-angle-measures skills (all reinforcement; see
`case.json.reinforcement_note`). Round-out skills: unit conversion, percent-of-a-number, comparing
two or more values (D5-D6).

---

## 45-Minute Socratic Plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch (Intro/Launch above), 30-second commitments, stand/sit vote (Anchor 1) — no explanation. |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just more accurate" (Anchor 2). |
| 10:00–15:00 | Pressure-test the models: process and open assumptions (Anchors 3–4) — "Whose plan is most fragile?" |
| 15:00–25:00 | Data Deep Dive — D1–D6 together, then reveal the 19.9% margin. |
| **25:00** | **DROP THE TWIST** — MA5's real fragility, delivered slowly. |
| 25:00–30:00 | Immediate recommit: who reverses? "What just broke?" |
| 30:00–40:00 | Threaded deep conflict (accuracy-margin vs. time-cost; a known cost vs. a probability; what the D3 parallel-lines proof is actually protecting). |
| 40:00–45:00 | Close, re-vote, reflection, Lessons Learned. |

---

## Five Socratic questions

1. The same structure blocks Option A's sightline and degrades Option B's rover accuracy. Is that a coincidence of this particular site, or is there a reason a single obstruction would threaten two completely different surveying technologies at once?
2. Your D5 accuracy-margin table shows one method with more room inside the tolerance band than the other. Does "more room" automatically mean "choose that method," or does the case's primary metric ask you to weigh something else against that margin?
3. Option A's second-setup time cost is a one-time, known number. Option B's accuracy risk near the obstruction is a probability, not a certainty. Which kind of cost is easier to plan around — a number you know you'll pay, or a risk that might not happen at all — and does "easier to plan around" mean "smaller expected cost"?
4. Your D3 calculation proves the relocated total-station baseline is parallel to the original. Why does that specific proof matter to whether Renata's second setup produces a corner that's actually where the design says it should be?
5. If the adjacent structure were twenty feet farther from these two corners instead of right next to them, which of the case's two problems — the blocked sightline, or the degraded GNSS accuracy — would you expect to improve, and would the other one improve too, less, or not at all?

## The trap

**Most learners will compare the two methods on accuracy margin alone (D5's table) and stop
there** — declaring Total Station Polar Staking the clear winner because it has more room inside
the tolerance band, without ever pricing in the time cost of the second setup its own obstruction
forces. The case's primary metric is explicitly a *time* metric that already has accuracy folded
into it as a rework-probability cost, not a raw accuracy comparison — a Hero who never gets past
D5 to D6 has done real, correct geometry and still not answered the question the case actually
asks.

## What a strong defense sounds like

There is no single right answer here, so don't grade toward "picked Option A." A strong defense
gets D1–D6 arithmetically right, states a clear recommendation, and then does two things a weak
defense skips: it prices Option A's accuracy margin against Option B's time advantage on the
*same* scale (total expected minutes, not "accuracy is better so accuracy wins"), and it names
MA5 — the near-structure multipath figure — as a real, disclosed assumption rather than treating
19.9% as settled fact. A Hero who says "I'd pick Option A, but if the multipath number really runs
closer to 13 mm than 17 mm this flips, and here's why that's plausible" is defending better than
one who confidently declares Option A the clear winner and never mentions the assumption the whole
recommendation leans on. Confidence in the final call matters less than showing where the call
could break.

## Sensitivity note

`margin_pct` = 19.9% (retuned 2026-09-01 from an original 47.4% — see RESEARCH_LOG.md), Option A
wins at the case's stated Modeling Assumption values — reported without softening per SPEC §5/§6,
but genuinely fragile, and more so on MA5 specifically than before the retune. Tier 2 P5 probe
result: **the recommended winner does flip** under a plausible (not even a full ±50%) flex on MA5
— the breakeven of ≈13.4 mm sits inside the same "several centimeters" (~10–50 mm) literature
range the assumption itself was drawn from, meaning a defensible real-world value on either side of
that line changes the answer; the retuned +17 mm value sits only ~3.6 mm above that breakeven
(versus ~11.6 mm at the old +25 mm value). Two secondary, smaller flip risks exist, both tighter
than before the retune: MA3 (second-setup time, breakeven ~25.2 min vs. stated 20 min, was ~32 min)
and MA4 (rework time, breakeven ~36.7 min vs. stated 45 min, was ~29 min). Full derivation in
`case.json.balance.margin_basis`, `case.json.modeling_assumptions[]`, and `RESEARCH_LOG.md`.

## Facilitator note — sensitive subject matter (SPEC §6)

None required. The stakes here are professional accountability, a deadline, and a rework cost —
not personal loss, illness, or hardship.

## Facilitator note — research-stage finding on the ACI 117M-10 source (resolved 2026-09-01)

`case-research` attempted a direct read of concrete.org's own ACI 117M-10 PDF; the free preview
exposes only front matter and the table of contents (Section 3, "Foundations," is at p. 117M-25,
beyond the preview — genuinely paywalled, not a shortcut avoided). A civilenghub-hosted sample
PDF was also attempted and returned unreadable content. The case therefore cites two sources
together: the Pennsylvania Dept. of Labor & Industry's hosted ACI 117-10 (US-customary companion
standard) committee text — HIGH confidence, primary — and theconstructor.org's secondary summary
of the metric ACI 117M-10 figure itself ("greater of 13 mm or 2% of specified dimension") — MEDIUM
confidence. Both agree in substance and in unit-converted magnitude. This is the honest resting
point after a genuine primary-source attempt; see `RESEARCH_LOG.md` (P01) for the full trail.
