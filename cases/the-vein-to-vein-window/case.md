# Case Study: The Vein-to-Vein Window

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

Dana Whitfield's pager goes off at 6:52 a.m. with a single line: *cells released, courier confirmed.*
Somewhere across town, a bag of a patient's own re-engineered immune cells has just come out of a
liquid-nitrogen freezer for the last time. Everything before this moment — the collection, the
weeks in a manufacturing lab, the quality testing — is already done and cannot be redone. Everything
after this moment happens on a clock that started the second that freezer door opened, a clock
Dana did not set and cannot pause.

Dana runs cell-therapy logistics for the hospital's transplant unit, and this patient has been
waiting for this exact bag for over a month, having already tried and failed two other treatments.
There is no backup dose in a drawer somewhere. If this one is not delivered while it is still good,
there is no quick do-over — just a much longer, much worse conversation with a very sick patient.

Two routes exist to get this bag from the freezer to the patient's vein, and the unit has used both
before. One keeps the whole process in-house, fast and comfortably clear of the label's cutoff. The
other saves real money and staff time by sending the bag to a shared central pharmacy first — a
route that has always worked, right up until the one day it didn't quite make it in time.

Dana's supervisor is waiting on a one-line answer before the courier van leaves the loading dock:
which route does today's dose take.

---

## Background

**CAR T-cell therapy** (chimeric antigen receptor T-cell therapy) is a real, FDA-approved category
of cancer treatment in which a patient's own immune cells are collected, genetically re-engineered
in a manufacturing lab — given new instructions that let them recognize and attach to a marker
found on that patient's specific cancer cells, the way a lock is cut to fit one particular key — to
hunt a specific cancer, frozen, shipped back, thawed, and infused back
into the same patient. Because the cells come from the patient's own body, there is no substitute
dose sitting in inventory — if a given bag cannot be used, replacing it means re-collecting cells
from the patient and restarting a multi-week manufacturing process from zero (SEE APPENDIX A).

The entire span from a patient's cell collection to the moment those cells are re-infused is called
the **vein-to-vein time**, and it is a real, published, closely-tracked metric in cell-therapy
logistics — a real-world median of **27 days** for the commercial CAR T-cell therapy Yescarta
(axicabtagene ciloleucel) is a commonly cited figure [S1] (SEE APPENDIX A). By the morning this case
takes place, that entire multi-week process is already finished. What is left is the **last mile**:
the short, tightly time-boxed window between the moment the frozen bag is thawed and the moment the
infusion into the patient actually begins.

That window has a hard boundary. Every FDA-approved drug ships with **prescribing information** — a
long, formal document the manufacturer writes and the FDA reviews and approves, stating exactly how
the product must be stored, handled, and used. The manufacturer's own FDA-approved prescribing
information for this product states exactly how long the thawed product may be held at room
temperature before it is no longer within the product's tested and approved stability data (SEE
APPENDIX B) — for Yescarta, **up to 3 hours** [S2]. Once that boundary is crossed, hospital protocol requires the dose to be
discarded — not because the cells are known to have failed at that exact instant, but because no
one has data on what happens past that point, and a therapy this scarce is never administered
outside its tested and approved window.

Dana's unit has two named, already-used routes for getting a thawed dose from the pharmacy to the
patient's bedside. **On-Site Rapid Thaw** keeps the unit's one specially certified cell-therapy
pharmacist and thawing unit inside the transplant floor itself, so there is no transport step at
all — it is the faster, more reliable route, and also the more expensive one, since it requires
that single specialized staff member on standby around the clock, able to attend only one dose at
a time (SEE APPENDIX C). **Central Pharmacy Courier** thaws the dose at
the hospital system's shared central pharmacy instead — the one main pharmacy, typically a floor or
building away, that prepares and dispatches every other medication for the whole hospital, not just
cell therapy — and sends it to the bedside by the same courier route used for every other medication — cheaper, and it frees up the specialized pharmacist
for other patients, but it adds a transport and hand-off step that On-Site Rapid Thaw never faces,
pushing its total elapsed time much closer to the label's hard cutoff (SEE APPENDIX C). Both routes
carry a real, disclosed chance of an unplanned delay — an elevator wait, a callback because the
paperwork double-checking that this exact bag belongs to this exact patient doesn't quite match up
(a routine safety check, since infusing the wrong patient's cells would be its own emergency), a
traffic slowdown on the courier's route — and Appendix C states how each route's total
elapsed time behaves under each delay scenario (SEE APPENDIX C AND APPENDIX E).

The vocabulary and the "how to…" skills this case will ask you to research are listed in the final
appendix — that is where Challenge 1 sends you (SEE APPENDIX G). All figures in this case are
sourced or disclosed as stated assumptions (SEE APPENDIX F).

---

## Dilemma

You are Dana Whitfield.

Do you:

**A.)** Send today's dose by **On-Site Rapid Thaw** — thaw and infuse on the transplant floor
itself, keeping the total elapsed time comfortably inside the label's cutoff, at the higher cost of
a dedicated standby pharmacist **OR**

**B.)** Send today's dose by **Central Pharmacy Courier** — thaw at the shared central pharmacy and
transport it by courier to the bedside, at meaningfully lower cost, even though the total elapsed
time runs much closer to that same cutoff

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case
study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would
choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — One-sided limits of the protocol viability function at the hard cutoff.** Appendix B
  defines a **viability function** `V(t)`, where `t` is the total elapsed minutes from the start of
  thaw to the start of infusion: `V(t) = 1` (the dose is within the label's tested stability window
  and may be administered) for every `t` less than the cutoff, and `V(t) = 0` (the dose is outside
  that tested window and must be discarded per protocol) for every `t` at or past the cutoff.
  Evaluate, algebraically and from the definition of `V(t)`, both **one-sided limits** of `V(t)` as
  `t` approaches the cutoff — the limit approaching from below and the limit approaching from above
  — and state clearly whether the two-sided limit of `V(t)` at the cutoff exists.
- **D2 — The continuity test at the hard cutoff.** Apply the formal, three-part continuity test at
  the cutoff to `V(t)`: (i) Is `V` defined at the cutoff? (ii) Does the limit of `V(t)` exist there
  (using D1's result)? (iii) Do the function's value and the limit agree? Conclude, showing each of
  the three parts, whether `V(t)` is continuous at the cutoff, name the type of discontinuity if it
  is not, and explain in your own words why this particular hard cutoff is a genuine discontinuity
  rather than a smooth, gradual fade in viability.
- **D3 — A worked contrast: an algebraic limit with a removable discontinuity.** Appendix D gives a
  second, unrelated function, `S(x)`, built purely to teach a contrast. Evaluate `lim(x→0) S(x)`
  algebraically by factoring the numerator and canceling the common factor, note that `S(0)` itself
  is undefined, and explain why this is a **removable** discontinuity — one that algebra can patch
  — in contrast to D2's hard cutoff, which cannot be patched by any algebraic trick because it is a
  real, deliberately tested boundary, not an artifact of how the function happens to be written.
- **D4 — Comparing the two routes' probability of a viable dose (the primary metric).** Using
  Appendix C's stated nominal elapsed time and delay-scenario probabilities for each route, compute
  the total elapsed time `t` under each of the three delay scenarios (no delay / minor delay / major
  delay) for both On-Site Rapid Thaw and Central Pharmacy Courier. For each route and each scenario,
  use D1's `V(t)` to determine whether that scenario keeps the dose viable. Sum the probabilities of
  the viable scenarios for each route to compute that route's overall probability that today's dose
  remains viable at re-administration, and state the margin between the two routes' probabilities as
  a percentage.
- **D5 — Writing the cutoff argument into the pitch.** Using the terms **Limit**, **One-Sided
  Limit**, **Continuity**, and **Discontinuity** correctly, write the part of your Challenge 2
  pitch that explains — in plain language a non-math reader could follow — why "a delay that only
  runs a little past the cutoff" is not "a little bit less viable." Name, specifically, why
  treating the cutoff as a soft average instead of a hard discontinuity is a mathematical mistake,
  not just an overly cautious one.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

## Appendix A — The Vein-to-Vein Window

Background on why this last mile matters so much by the time it happens.

| Quantity | Value |
|---|---|
| Real published median vein-to-vein time, Yescarta (axicabtagene ciloleucel), real-world U.S. commercial setting | 27 days [S1] |
| Real published median manufacturing turnaround time, Yescarta (leukapheresis to product release), as of the January 2024 FDA-approved process change | 14 days [S3] |

**Leukapheresis** is the medical procedure that collects a patient's white blood cells (which
include the T-cells CAR T-cell therapy re-engineers) by drawing blood, filtering out those cells
with a machine, and returning the rest of the blood to the patient — it is how "cell collection"
in Appendix A actually happens, and it is the starting line both real-world time figures above are
measured from.

An **autologous** therapy is one made from a patient's own cells, as opposed to a donor's — this is
what makes a CAR T-cell dose irreplaceable on short notice: there is no donor bank to draw a
replacement from, only the same patient, who would need to be re-collected from and would need to
wait through the whole manufacturing process again.

Referenced from Background. Establishes the stakes; does not enter any D1–D5 calculation.

---

## Appendix B — The Hard Cutoff: Post-Thaw Stability

The single real, sourced number this case's discontinuity is built on.

| Quantity | Value |
|---|---|
| Maximum time Yescarta (axicabtagene ciloleucel) may be held at room temperature after thaw, per its FDA-approved prescribing information | 3 hours [S2] |
| That same cutoff, converted to minutes (used as `t`'s unit throughout D1–D4) | 180 minutes (3 hours × 60 minutes/hour — arithmetic, derived from [S2], not independently sourced) |

**Viability function**, formally, for this case:

```
V(t) = 1   for 0 ≤ t < cutoff       (within the label's tested stability window)
V(t) = 0   for t ≥ cutoff           (outside the tested window; discard per protocol)
```

Referenced from Background and Challenge 3. Forces D1's one-sided limits and D2's continuity test.

---

## Appendix C — Two Last-Mile Routes

The scenario data D4's probability comparison is built from. These figures are hospital-internal
operational estimates, not published data — see Appendix E for the disclosed assumptions behind
each one.

| Quantity | On-Site Rapid Thaw (Option A) | Central Pharmacy Courier (Option B) |
|---|---|---|
| Nominal (no-delay) total elapsed time, thaw start to infusion start | 45 minutes [MA1] | 150 minutes [MA2] |
| Minor delay scenario — extra minutes added | +20 minutes [MA3] | +20 minutes [MA3] (same figure, shared assumption) |
| Major delay scenario — extra minutes added | +50 minutes [MA3] | +50 minutes [MA3] (same figure, shared assumption) |
| Probability of no delay / minor delay / major delay | 71% / 20% / 9% [MA4] | 71% / 20% / 9% [MA4] (same distribution, shared assumption) |
| Estimated incremental staffing cost of this route over Central Pharmacy Courier, per dose | +$500 [MA5] | $0 (baseline; On-Site's figure is the incremental amount above this) |

Referenced from Background and Challenge 3. Forces D4's probability-of-viability computation, and
gives Challenge 2's pitch a real number to weigh against the probability gap on the other side.

---

## Appendix D — A Worked Contrast: Two Kinds of Discontinuity

A standalone teaching construct, disclosed here as exactly that — **not** a real hospital figure.
It exists purely so D3 has a clean algebraic limit to contrast against D2's real, unremovable hard
cutoff.

`S(x)` represents a hypothetical staffing-cost-savings model: the dollars saved in pharmacist
overtime for every `x` minutes shaved off a routine double-check step, for `x ≠ 0`.

```
S(x) = (x² + 5x) / x
```

Referenced from Challenge 3. Forces D3's algebraic limit evaluation.

---

## Appendix E — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | On-Site Rapid Thaw's nominal elapsed time | 45 minutes | No public data exists on any specific hospital's internal thaw-to-infusion timing; a value is fixed here, built from realistic same-floor process steps (thaw, identity verification, zero transport), so both routes can be compared on the same basis. | The case's answer is sensitive to how far below the cutoff this value sits. |
| MA2 | Central Pharmacy Courier's nominal elapsed time | 150 minutes | Same reasoning as MA1, applied to the route that adds a transport and hand-off step (thaw, verification, cross-campus courier transport, bedside intake). | The case's answer is sensitive to how close to the cutoff this value sits. |
| MA3 | Minor and major delay-scenario extra minutes | +20 minutes (minor); +50 minutes (major) | No public rate exists for hospital-internal courier or workflow delays; a shared two-tier delay model (a modest hold-up vs. a larger one, e.g. an elevator wait vs. a traffic-snarled courier route or an identity-verification callback) is fixed here so the same risk applies fairly to both routes. | The case's answer is sensitive to how large the major-delay figure is relative to each route's remaining margin before the cutoff. |
| MA4 | Delay-scenario probability distribution | 71% no delay / 20% minor delay / 9% major delay | Same reasoning as MA3 — no public institution-specific delay-rate data exists; a single shared distribution is fixed so the comparison isolates the routes' elapsed-time difference rather than an assumed difference in delay risk. | The case's answer is sensitive to the probability assigned to the scenario that pushes a route's elapsed time past the cutoff. |
| MA5 | Estimated incremental staffing cost of On-Site Rapid Thaw over Central Pharmacy Courier, per dose | $500 | No public, per-dose figure exists for this exact comparison. Real hospitals do pay staff extra for working overnight, weekend, or always-on-call shifts ("shift-differential" and "on-call" pay, on top of regular wages) — a genuine, documented practice that makes continuous specialty-staff standby coverage cost something real, but no institution publishes a per-dose breakdown of that cost. This figure is a disclosed, order-of-magnitude modeling estimate, not a citation. | The case's answer is sensitive to whether this figure is larger or smaller than a Hero believes a 9-percentage-point viability gap is worth in dollar terms — that comparison is a values judgment the case deliberately leaves to the Hero, not a threshold the case computes for them. |

---

## Appendix F — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Real-world median vein-to-vein time, Yescarta (axicabtagene ciloleucel), U.S. commercial setting, from a CIBMTR (Center for International Blood and Marrow Transplant Research — a real, independent patient-outcomes registry) analysis | 27 days | Kite Pharma / Gilead Sciences — [Time to CAR T-cell Therapy May Impact Outcomes for Patients With Relapsed/Refractory Large B-cell Lymphoma in New CIBMTR Analysis](https://www.kitepharma.com/news/press-releases/2022/12/time-to-car-t-cell-therapy-may-impact-outcomes-for-patients-with-relapsedrefractory-large-b-cell-lymphoma-in-new-cibmtr-analysis) | published 2022-12-11, accessed 2026-09-09 | MEDIUM |
| S2 | Maximum room-temperature holding time for Yescarta after thaw, per FDA-approved prescribing information | 3 hours | U.S. Food and Drug Administration — Yescarta (axicabtagene ciloleucel) full prescribing information, [FDA label (accessdata.fda.gov)](https://www.accessdata.fda.gov/spl/data/7ec02549-737e-4a56-9dac-5dbbc63cc2b7/7ec02549-737e-4a56-9dac-5dbbc63cc2b7.xml) | accessed 2026-09-09 | HIGH |
| S3 | Median manufacturing turnaround time for Yescarta (leukapheresis to product release), following a January 2024 FDA-approved manufacturing process change | 14 days (reduced from a prior 16-day median) | Kite Pharma — [Kite Receives U.S. FDA Approval of Manufacturing Process Change Resulting in Reduced Median Turnaround Time for Yescarta CAR T-cell Therapy](https://www.kitepharma.com/news/press-releases/2024/1/kite-receives-us-fda-approval-of-manufacturing-process-change-resulting-in-reduced-median-turnaround-time-for-yescarta-car-tcell-therapy) | published 2024-01-30, accessed 2026-09-09 | MEDIUM |

**A note on S1's confidence grade:** this figure comes from a company press release describing a
CIBMTR (Center for International Blood and Marrow Transplant Research — a real, independent
patient-outcomes registry) analysis, rather than from the underlying peer-reviewed publication or
registry report directly. The press release is a secondary description of a primary analysis, and
the exact 27-day figure could not be independently cross-checked against the original CIBMTR
dataset within this case's research pass — hence MEDIUM, not HIGH. This figure is background-only
(SEE APPENDIX A) and does not enter any D1–D5 calculation, so its confidence grade does not affect
the case's load-bearing math. **S3 is similarly a company (Kite/Gilead) press release announcing
its own FDA-approved change** — factual and specific (an exact regulatory action with dates and
day-counts), but not independently republished by a third party, hence MEDIUM rather than HIGH; it
is likewise background-only. **S2, by contrast, is load-bearing** (it sets the case's hard cutoff)
and is graded HIGH: it is the actual FDA-approved prescribing information, a primary regulatory
document, with an unambiguous unit (hours) and no version ambiguity for the product as currently
labeled.

Full research trail and rejected leads are in `RESEARCH_LOG.md`.

## Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Limit
- One-Sided Limit
- Continuity
- Discontinuity

**"How to…" questions**

- How to evaluate a limit algebraically
- How to determine whether a function is continuous at a point

---

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
