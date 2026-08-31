Case Study: Panel Layout
MS | Math | Case Study | 2026 | Adventure

## Overview

Marcus Feld has the two prototypes side by side on his bench, and for the third time this
morning he reaches across each of them in turn, the way an operator would reach after setting an
infusion rate — thumb landing on the Confirm control, then across to the panel's other required
controls in the same motion. On his monitor, the motion-capture software still has a small red
dot frozen over yesterday's test session, a tester's fingertip traced frame by frame across two
control panels that look almost the same and measure completely differently. Both panels are
freshly milled prototypes, and the room still smells faintly of warm plastic from the model shop
three doors down.

His inbox has the tooling vendor's email open in the background tab, subject line unread twice
already: *time to lock the panel drawing.* Once that drawing goes out, the injection-mold cavity
gets cut, and there is no cheap way back — a hardware revision this far along does not get a
second layout without a very uncomfortable conversation, and whichever panel he signs off on this
afternoon is the one with his name on the sign-off line if a miss-rate problem ever turns up in
the field.

Marcus picks up the Close Reach panel first. Bigger Confirm control, right where his thumb
already wants to be. Then the Long Reach panel — smaller Confirm control, farther out, but the
panel's other required controls sit closer together than they do on the first prototype, easier
to reach in the same breath.

He sets both panels down, side by side, and opens the sign-off form.

## Background

Marcus Feld is a Human Factors Engineer at Meridian Medical, responsible for signing off on the
control-panel layout of the company's bedside infusion-therapy console before its next hardware
revision goes to tooling. Once his sign-off is submitted, the panel's injection-molding cavity is
cut and the layout is locked for the life of that hardware revision — any layout problem found
afterward becomes a design-history-file finding with Marcus's own sign-off attached to it.

The console's post-setup confirmation sequence requires an operator to reach the Confirm
control — the single most frequently used control in the sequence — and then, in the same reach
cycle, the panel's other required controls (SEE APPENDIX A). Panel space near the operator's
resting hand position is limited: the near-zone closest to that resting position can comfortably
fit either a larger Confirm control or more generous spacing for the other required controls, but
not both at once (SEE APPENDIX A).

Two fully tooled prototype panels have already been built and tested (SEE APPENDICES A AND C):

**Close Reach** claims most of the near-zone for the Confirm control — a larger target, placed
close to the resting hand position — which lowers the Confirm control's own predicted movement
time and tested miss rate, but pushes the panel's other required controls farther from the
resting hand position, raising their predicted movement time and tested miss rate.

**Long Reach** gives most of the near-zone to the other required controls instead, placing them
closer to the resting hand position, but shrinks the Confirm control and moves it farther out,
raising its own predicted movement time and tested miss rate.

Every control's predicted movement time is modeled with Fitts's Law, the standard human-factors
model for target-acquisition movement time, using coefficients from a published ISO 9241-9
evaluation (SEE APPENDIX B). Marcus's recommendation has to be judged on one figure: the whole
panel's predicted seconds of task-completion time per successful actuation, across the full
control sequence — not the Confirm control in isolation, and not either option's raw movement-time
total without accounting for how often an operator misses and has to try again (SEE APPENDICES A,
B AND C).

Every sourced and assumed figure in this case is listed in **Appendices D and E**, and the
vocabulary and "how to…" skills this case will ask of you are listed in **Appendix F** — that is
where Challenge 1 sends you.

## Dilemma

You are Marcus Feld.

Do you:

A.) Recommend Close Reach — lock in the larger Confirm control close to the resting hand
position, even though it claims panel space the other required controls need OR

B.) Recommend Long Reach — lock in the smaller Confirm control farther from the resting hand
position, freeing panel space for the other required controls

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. The whole-panel Fitts's Law time model, built and differentiated (SEE APPENDICES A AND
    B): the Confirm control's width and distance, and the other required controls' shared
    distance, expressed as functions of a single allocation variable x (the fraction of near-zone
    capacity given to the Confirm control, x = 0 at Long Reach and x = 1 at Close Reach), the
    resulting total predicted completion time T(x) for one pass through the full control
    sequence, its derivative T'(x) shown step by step, and the full algebra used to solve
    T'(x) = 0 for every critical point in the feasible domain 0 ≤ x ≤ 1.
    D2. A first-derivative-test sign chart (SEE D1): the sign of T'(x) evaluated at a test point
    on each side of every critical point found in D1, each critical point classified as a local
    minimum, local maximum, or neither, with a stated reason for each classification.
    D3. A closed-domain optimization table: T(x) evaluated at the domain's two endpoints
    (x = 0, Long Reach, and x = 1, Close Reach) and at every interior critical point classified in
    D2, with the global minimum of T(x) on the feasible domain identified and justified by
    comparing all of those values against each other, not asserted.
    D4. A miss-rate-weighted final decision table (SEE APPENDIX C): using the panel's tested miss
    rates for the Confirm control and for the other required controls at Long Reach and at Close
    Reach, and stating explicitly what is and is not known about miss rate at any interior layout
    identified as the time-minimizer in D3, compute the expected seconds of predicted
    task-completion time per successful actuation — accounting for the expected extra attempts a
    miss requires — for Long Reach, for Close Reach, and for D3's global minimizer, with a final
    recommendation stated in terms of that per-successful-actuation figure.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — Panel Layout & Option Endpoint Specifications

Close Reach and Long Reach are the two ends of a single continuous design choice: how much of the
panel's scarce **near-zone** — the strip of panel real estate closest to the resting hand
position — is allocated to the Confirm control versus reserved for the panel's other required
controls. Let **x** stand for the fraction of near-zone capacity allocated to the Confirm control,
with x = 0 at Long Reach, x = 1 at Close Reach, and 0 ≤ x ≤ 1 for any layout physically buildable
inside the current hardware revision's enclosure.

All figures in this table are stated **Modeling Assumptions**, not measurements of a real
product — Meridian Medical and this hardware revision are invented for this case (SEE APPENDIX D
for the basis and sensitivity of each).

| | Value |
|---|---|
| Confirm control width at x = 0 (Long Reach), mm | 10 (MA1) |
| Confirm control width at x = 1 (Close Reach), mm | 30 (MA2) |
| Confirm control distance from the resting hand position at x = 0 (Long Reach), mm | 120 (MA3) |
| Confirm control distance from the resting hand position at x = 1 (Close Reach), mm | 60 (MA4) |
| Shared distance from the resting hand position to the other required controls at x = 0 (Long Reach), mm | 80 (MA5) |
| Shared distance from the resting hand position to the other required controls at x = 1 (Close Reach), mm | 140 (MA6) |
| Fixed target width of each of the other required controls (does not change with x), mm | 20 (MA7) |
| Count of other required controls sharing the near-zone trade-off with the Confirm control | 3 (MA8) |

For any x strictly between 0 and 1, this case models the Confirm control's width and distance, and
the other controls' shared distance, as varying linearly between their two named-option endpoint
values above — the simplest model consistent with a continuous range of buildable layouts between
the two prototypes actually tooled and tested (SEE APPENDIX C). This linear-interpolation choice
is itself a stated Modeling Assumption (MA9, SEE APPENDIX D).

## Appendix B — Fitts's Law Model & ISO 9241-9 Coefficients

Fitts's Law predicts the movement time required to acquire a target of a given width at a given
distance (Paul Fitts, 1954), and is the model international usability-testing standard ISO
9241-9 uses to evaluate pointing-device and control performance. This case uses the common
Shannon-formulation index of difficulty:

ID = log2(D/W + 1), in bits

MT = a + b · ID, in seconds

where D is the movement distance from the resting hand position to a control's center, W is that
control's target width, and a and b are regression coefficients fit to real human performance
data.

| | Value |
|---|---|
| Fitts's Law intercept coefficient, a, seconds | 0.6992 [S1] |
| Fitts's Law slope coefficient, b, seconds per bit | 0.1714 [S1] |

These coefficients are drawn from the "touchpad + tap" condition of a published ISO 9241-9
conformant Fitts's Law evaluation (SEE APPENDIX E, S1) — a real, dated, peer-reviewed measurement
of human target-acquisition performance for a hand-operated tap-to-select task, used here as the
best available public stand-in for this panel's hand-reach-and-press task (no public ISO 9241-9
study of a bedside medical-device control panel specifically was found; SEE the Research Log for
what else was tried).

The whole-panel model built in Challenge D1 applies this formula once for the Confirm control and
once for each of the other required controls (Appendix A), summed into a single predicted
completion time T(x) for one pass through the full control sequence.

## Appendix C — Panel Usability Test Log (Tested Miss Rates)

Meridian Medical's usability lab tested a small panel of operators at both named prototype
configurations — no layout in between has been physically built or tested — and recorded the
following:

All figures in this table are stated **Modeling Assumptions**, not a real usability test log —
Meridian Medical's test panel is invented for this case (SEE APPENDIX D for the basis and
sensitivity of each).

| | Confirm control miss rate | Other-required-controls average miss rate |
|---|---|---|
| Long Reach (x = 0) | 0.06 (MA10) | 0.02 (MA11) |
| Close Reach (x = 1) | 0.01 (MA12) | 0.07 (MA13) |

No layout between the two named options has been physically prototyped or tested, so no tested
miss-rate figure exists yet for an interior layout — Challenge D4 states explicitly what is and is
not known about that layout's miss rate before using it in a recommendation.

## Appendix D — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author. A Hero may challenge them in discussion — that is a legitimate move; Appendix F names
> the skills a Hero would need to test one.

Meridian Medical and this specific hardware revision are invented for this case — no real public
product's panel drawing exists to cite. The dimensions below are chosen to sit inside real,
generally-published human-factors ranges for hand-operated console controls: touch/push targets
sized for reliable actuation under time pressure (or gloved use) commonly cluster at roughly
20 mm and above in the human-factors usability literature, and a bedside console's near-zone —
the reach envelope closest to a defined resting hand position — is commonly on the order of
50–150 mm. Nothing below claims a specific published document for the exact numbers; that is the
whole reason they are here and not in Appendix E.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Confirm control width, Long Reach (x=0) | 10 mm | Below the ~20 mm range commonly associated with reliable, low-error touch/push actuation — consistent with Long Reach's narrative of a deliberately undersized Confirm control. | Feeds MTc(0) in D1's model. Raising this value shrinks Long Reach's Confirm-control disadvantage; see MA9's note on the interior critical point x*. |
| MA2 | Confirm control width, Close Reach (x=1) | 30 mm | Comfortably above the ~20 mm reliable-actuation range, consistent with Close Reach's narrative of a deliberately oversized Confirm control. | Feeds MTc(1). Lowering this toward MA1's value flattens the whole trade-off and can remove the interior critical point entirely. |
| MA3 | Confirm control distance, Long Reach (x=0) | 120 mm | Outer edge of a plausible near-zone reach envelope. | Feeds MTc(0) and D3's endpoint comparison directly. |
| MA4 | Confirm control distance, Close Reach (x=1) | 60 mm | Inner portion of the same envelope, close to the resting hand position. | Feeds MTc(1); a smaller value here strengthens Close Reach's own-control advantage without changing the whole-panel result much, since the other controls dominate D4 (see MA13). |
| MA5 | Other-controls shared distance, Long Reach (x=0) | 80 mm | Inner portion of the envelope — Long Reach's whole narrative premise is that these controls stay close. | Feeds MTo(0), which is the term multiplied by MA8's count — the single most consequential distance figure for D4's outcome. |
| MA6 | Other-controls shared distance, Close Reach (x=1) | 140 mm | Outer edge of the envelope — Close Reach's premise is that these controls get pushed out. | Feeds MTo(1). Numerically, Close Reach only wins D4's final comparison if this value drops below **≈118 mm** (holding every other figure fixed) — this is one of the most dilemma-flippable figures in the case. |
| MA7 | Fixed target width of each other required control | 20 mm | Set at the same ~20 mm reliable-actuation benchmark used for MA1/MA2, since these controls' size does not change with x. | Feeds both MTo(0) and MTo(1) equally; changing it shifts both options' other-control time by roughly the same amount and does not by itself flip D4. |
| MA8 | Count of other required controls | 3 | A short post-setup confirmation sequence on a bedside infusion console plausibly has a small number of required checks beyond Confirm (e.g. rate/target confirmation, an alarm-silence acknowledgment, a start acknowledgment) — 3 is a mid-range, defensible count for that kind of sequence. | **Directly dilemma-flipping.** At n=1 or n=2 other required controls, Close Reach wins D4's expected-time comparison; at n=3 (the value used) or higher, Long Reach wins. A Hero who checks this sensitivity has found the real lever in this case. |
| MA9 | Linear interpolation of width/distance in x between the two named endpoints | (structural choice, not a numeric value) | The simplest model consistent with a continuous range of buildable layouts between the only two prototypes actually tooled — with no third prototype tested, a straight line is the least additional assumption a modeler can add. | A non-linear interpolation (e.g. one that saturates faster near an endpoint) could move x* without changing which of D3's compared values is largest, but a Hero should be able to say so explicitly rather than assume linearity is "the truth." |
| MA10 | Confirm control tested miss rate, Long Reach (x=0) | 0.06 (6%) | Set higher than Close Reach's, consistent with a smaller, farther target; within the range usability testing commonly reports for a non-trivial but not extreme error rate under a small, first-generation sample of test operators. | Feeds D4's expected-attempts multiplier for the Confirm term at Long Reach; a lower value here would make Long Reach's D4 win even larger, not smaller. |
| MA11 | Other-controls average tested miss rate, Long Reach (x=0) | 0.02 (2%) | Set low, consistent with those controls sitting in the easiest, closest part of the near-zone at this option. | Small individual effect, but multiplied by MA8's count of 3 in D4 — see MA8 and MA6 for the more consequential levers. |
| MA12 | Confirm control tested miss rate, Close Reach (x=1) | 0.01 (1%) | Set low, consistent with a large, close target. | Even setting this to 0 does not flip D4's result on its own — the case's real sensitivity lives in the other-controls figures (MA6, MA13), not here; a Hero who spends their sensitivity argument only on this figure has picked the less consequential lever. |
| MA13 | Other-controls average tested miss rate, Close Reach (x=1) | 0.07 (7%) | Set higher than Long Reach's, consistent with those controls being pushed to the outer, more error-prone part of the near-zone at this option. | Multiplied by MA8's count of 3 in D4. Close Reach only wins D4's final comparison if this value drops below **≈4.1%** (holding every other figure fixed) — one of the most dilemma-flippable figures in the case, alongside MA6 and MA8. |

No tested miss-rate figure exists, or could exist, for the interior time-minimizing x* found in
D1–D3 — no layout strictly between the two named options has ever been built. Challenge D4 asks
you to state this limitation explicitly rather than assume x*'s miss rate can be interpolated the
same way its distances and widths were (MA9); this case does not supply a value for it, by design.

## Appendix E — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Fitts's Law regression coefficients (intercept a, slope b) for the Shannon-formulation model MT = a + b·log2(D/W+1), "touchpad + tap" condition, ISO 9241-9 conformant two-dimensional target-acquisition task | a = 699.2 ms (0.6992 s), b = 171.4 ms/bit (0.1714 s/bit), r = .9124 | Hassan, M., Magee, J., & MacKenzie, I. S. — "A Fitts' Law Evaluation of Hands-Free and Hands-On Input on a Laptop Computer," *Proceedings of HCII 2019* (LNCS 11573), pp. 234–249 ([DOI](https://doi.org/10.1007/978-3-030-23563-5_20); [author's page](https://www.yorku.ca/mack/hcii2019.html)) | 2019 | MEDIUM |

**Note on S1's confidence grade.** This is a real, dated, peer-reviewed ISO 9241-9 conformant
study with unambiguous units (the paper explicitly ties its task to the ISO 9241-9 two-dimensional
circular target layout and Shannon ID formula). It is graded MEDIUM rather than HIGH because the
measured task — a fingertip tap on a laptop touchpad — is a proxy for this case's actual task, a
hand reaching to press a physical control-panel button; no public ISO 9241-9 study of a bedside
medical-device control panel specifically was found (SEE the Research Log for the searches
attempted and rejected, including MacKenzie's widely-cited 1992 device-comparison table, which
predates the ISO 9241-9 standard itself and was set aside for that reason).

## Appendix F — "How To…" Math Questions To Research

**Vocabulary terms**

- Critical Point

**"How to…" questions**

- How to find critical points of a function
- How to use the first derivative test to classify a critical point
- How to solve an optimization problem using derivatives

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
