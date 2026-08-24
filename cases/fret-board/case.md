# Case Study: Fret Board

MS | Math | Case Study | 2026-27 | Heroes Academy

---

## Overview

Yuki Tanaka runs a strip of masking tape down the guitar neck clamped in the workshop vise, marking where the first fret line has to land. Sawdust hangs in the light from the shop's one window, and somewhere behind her a radio is playing too quietly to make out the words. This is her first solo fret job — no one checking her marks before the saw touches wood.

The client is due back for the instrument before the week is out. Yuki's mentor left two sticky notes on the bench this morning before heading to a supplier meeting across town: one with a string of decimals under the header "exact," the other with a short column of simple fractions under "shop method." Both get you a playable neck. Only one of them is what she was actually taught to check her work against.

She sets her calculator down next to the fret rule and the calipers, glances at the clock, and picks up the pencil.

---

## Background

Yuki Tanaka is an apprentice at a small custom-guitar workshop that builds and repairs fretted instruments to order. She has assisted on fret jobs for two years but has never marked and cut a fingerboard on her own for a paying client. The shop's owner has told her plainly: a fret placed wrong enough to throw the instrument out of tune is not a small fix. Pulling a fret, filling the slot, and re-cutting it costs roughly a week of unpaid rework on top of whatever else is on her bench (SEE APPENDIX F).

Every fret on a guitar neck marks the point where the string, stopped short by a metal bar, produces one semitone higher in pitch than the fret before it. Modern instruments are built to **equal temperament**: twelve equally-spaced semitones per octave, where doubling the vibrating string length drops the pitch by exactly one octave (SEE APPENDIX A). Two methods exist for finding where those twelve fret lines actually go on the neck:

**Option A — The Precision Method.** Compute each fret's distance from the nut using the exact twelfth-root-of-two ratio that defines equal temperament, carried to four decimal places at every fret (SEE APPENDIX B).

**Option B — The Rule of Eighteen.** Use the traditional luthier's shortcut passed down in the shop: divide the *remaining* string length by a fixed whole-number divisor at each fret, a method generations of luthiers used before calculators were sitting on every bench (SEE APPENDIX C).

The shop's scale length, fret count, and Yuki's client deadline are fixed constraints, not choices (SEE APPENDIX F). Both methods place all twelve frets inside that same deadline — the shop cares about the result, not which arithmetic got there. What differs is how far each method's fret positions drift from true equal temperament, and whether that drift stays inside what a professional's ear — and a client's tuner — will accept (SEE APPENDIX D). Fret-position drift can also be read as a string-length ratio problem: reducing the open-to-fretted length ratio at each fret shows which frets, if any, land on the kind of simple whole-number ratio a musician's ear recognizes as a clean interval (SEE APPENDIX E). Every sourced or derived figure in this case is documented, with its source and confidence, in **Appendix G**; the handful of figures with no public source are stated openly as Modeling Assumptions rather than invented.

The vocabulary and the "how to…" skills this case will ask of you are listed in **Appendix H** — that is where Challenge 1 sends you.

---

## Dilemma

You are Yuki Tanaka.

Do you:

**A.)** Mark every fret using the Precision Method — the exact twelfth-root-of-two ratio, calculated to four decimal places at each fret **OR**

**B.)** Mark every fret using the Rule of Eighteen — the traditional whole-number-divisor shortcut

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A fret-position table, Precision Method.** Using the twelfth-root-of-two ratio, compute the distance from the nut for frets 1 through 12, carried to four decimal places at every step (Appendix B).
- **D2 — A fret-position table, Rule of Eighteen.** Using the traditional whole-number-divisor shortcut, compute the distance from the nut for the same frets 1 through 12 (Appendix C).
- **D3 — A cents-of-deviation conversion.** Using the length difference between your D1 and D2 results at fret 12, convert that difference into cents of pitch deviation from true equal temperament, showing your arithmetic (Appendix D).
- **D4 — A GCF string-length-ratio table.** For frets 1 through 5, express the open-string-length-to-fretted-string-length ratio at each fret in lowest terms using the greatest common factor, and state which of those frets (if any) reduce to a simple whole-number ratio (Appendix E).
- **D5 — A recommendation** comparing the two methods' 12th-fret deviation against the acceptable intonation tolerance in Appendix D, and against the week-long re-fret cost in Appendix F if a method's drift proves unacceptable.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->

---

## Appendix A — Equal Temperament, Defined

The modern Western fretted instrument is built on **equal temperament**: one octave (a 2:1 ratio of vibrating string length) is divided into twelve equal semitone steps, geometrically rather than in equal-sized pieces. Moving up one fret always multiplies the *remaining* vibrating string length by the same constant ratio.

| Quantity | Value |
|---|---|
| Ratio defining one octave (12 semitones) | 2 : 1 |
| Number of equal semitone steps per octave | 12 |
| Per-fret length ratio (constant multiplier applied 12 times to reach 2:1) | 1.059463 [S1] |

This appendix is referenced from Background and forces the exponent math behind Challenge D1.

---

## Appendix B — Fret Position Table, Precision Method (Option A)

The distance of fret *n* from the nut, for a string of scale length *L*, is:

```
distance(n) = L × [1 − (1/2)^(n/12)]
```

| Input | Value |
|---|---|
| Scale length, *L* (SEE APPENDIX F for the shop's build spec) | 25.5000 in [S4] |
| Twelfth-root-of-two constant | 1.0595 [S1] |

| Fret *n* | Distance from nut (in), Precision Method |
|---|---|
| 1 | 1.4312 |
| 2 | 2.7821 |
| 3 | 4.0571 |
| 4 | 5.2606 |
| 5 | 6.3966 |
| 6 | 7.4688 |
| 7 | 8.4808 |
| 8 | 9.4360 |
| 9 | 10.3376 |
| 10 | 11.1886 |
| 11 | 11.9918 |
| 12 | 12.7500 |

*Derived [S1]+[S4]: distance(n) = 25.5000 × [1 − (1/2)^(n/12)], evaluated at each n. Fret 12 lands at exactly half the scale length (12.7500 in), as required by the 2:1 octave ratio.*

Referenced from Background and Challenge D1.

---

## Appendix C — Fret Position Table, Rule of Eighteen (Option B)

The traditional shop shortcut: at each fret, divide the string length that *remains* (from the previous fret to the bridge) by a fixed whole-number divisor to find the distance to the next fret.

```
fret spacing(n) = remaining length after fret (n−1) ÷ divisor
```

| Input | Value |
|---|---|
| Rule-of-Eighteen divisor (the traditional shop constant) | 18 [S3] |
| Scale length, *L* | same as Appendix B |

| Fret *n* | Distance from nut (in), Rule of Eighteen |
|---|---|
| 1 | 1.4167 |
| 2 | 2.7546 |
| 3 | 4.0183 |
| 4 | 5.2117 |
| 5 | 6.3388 |
| 6 | 7.4033 |
| 7 | 8.4087 |
| 8 | 9.3582 |
| 9 | 10.2550 |
| 10 | 11.1019 |
| 11 | 11.9018 |
| 12 | 12.6573 |

*Derived [S3]+[S4]: at each fret, spacing = (L − previous distance) ÷ 18, applied iteratively from the nut (D0 = 0). This is the historical whole-number "rule of 18," distinct from the more accurate 17.817154 divisor some modern shops use instead [S2] — see the Sources appendix note on S2.*

Referenced from Background and Challenge D2.

---

## Appendix D — Cents of Deviation and Intonation Tolerance

Musicians measure pitch difference in **cents**: 1200 cents to an octave, 100 cents to one equal-tempered semitone. The formula converting a length (or frequency) ratio to cents:

```
cents = 3986.3 × log10(ratio)
```

where *ratio* is the true equal-tempered string length (or frequency) divided by the approximated one.

| Quantity | Value |
|---|---|
| 12th-fret length, Precision Method (Appendix B) | 12.7500 in |
| 12th-fret length, Rule of Eighteen (Appendix C) | 12.6573 in |
| Cents of deviation at fret 12 | ≈ 12.5 cents flat (Rule of Eighteen relative to true equal temperament) — see derivation below |
| Acceptable intonation tolerance a professional luthier targets, in cents | 5 cents at the 12th fret — **stated Modeling Assumption, see MA1** |

**Derivation of the cents figure:** the *ratio* that matters is not the raw distance-from-nut difference but the ratio of the two methods' *remaining* (bridge-side) string lengths at fret 12, since pitch is set by the vibrating (remaining) length. Remaining length = *L* − distance(12).

- Precision Method remaining length: 25.5000 − 12.7500 = 12.7500 in
- Rule of Eighteen remaining length: 25.5000 − 12.6573 = 12.8427 in
- Ratio = 12.7500 ÷ 12.8427 = 0.99278
- cents = 3986.3 × log10(0.99278) ≈ **−12.5 cents** (the minus sign means the Rule-of-Eighteen fret sits flat of true pitch — consistent with the qualitative finding in [S3] that rule-of-18 frets "trend flat" against true equal temperament)

Referenced from Challenges D3 and D5.

---

## Appendix E — GCF String-Length-Ratio Table

For each fret, the ratio of the open string's full length to the fretted (shortened) string length can be simplified using the **greatest common factor**. A ratio that reduces to small whole numbers (2:1, 3:2, 4:3 …) corresponds to a fret landing near a simple harmonic interval; a ratio that does not reduce cleanly does not.

Lengths are expressed in **ten-thousandths of an inch** (i.e., the Appendix B distances × 10,000) so both terms of every ratio are whole numbers a GCF can be taken of.

| Fret *n* | Open-string length : fretted-string length (unreduced, ten-thousandths of an inch) | Simplified ratio (lowest terms) |
|---|---|---|
| 1 | 255000 : 240688 | 31875 : 30086 |
| 2 | 255000 : 227179 | 255000 : 227179 (already lowest terms — GCF is 1) |
| 3 | 255000 : 214429 | 255000 : 214429 (already lowest terms — GCF is 1) |
| 4 | 255000 : 202394 | 127500 : 101197 |
| 5 | 255000 : 191034 | 42500 : 31839 |
| 12 (given, for contrast — see Appendix B) | 255000 : 127500 | **2 : 1** (GCF is 127500) |

**None of frets 1 through 5 reduce to a simple whole-number ratio** (2:1, 3:2, 4:3, and similar). Fret 12 — the octave — is the one point on the neck where equal temperament is *exactly* a simple ratio, by construction (SEE APPENDIX A). Every fret between the nut and the octave is an irrational multiple of the open length; a clean small-whole-number ratio at those frets would be a coincidence of rounding, not a property of equal temperament itself. *(Derived from Appendix B's Precision Method distances, [S1]+[S4].)*

Referenced from Challenge D4.

---

## Appendix F — Shop Build Spec and Constraints

| Constraint | Value |
|---|---|
| Instrument type / scale length family for this build | Fender-style, 25.5000 in scale length [S4] |
| Number of frets on this neck | 22 — **stated Modeling Assumption, see MA2** |
| Client deadline (days from today) | 5 days — **stated Modeling Assumption, see MA3** |
| Cost of a re-fret if a method's drift is unacceptable | roughly a week of unpaid rework (see Background) |

Referenced from Background and Challenge D5.

---

## Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Acceptable intonation tolerance a professional luthier targets, at the 12th fret | 5 cents | No single published professional trade standard states one hard number. Guitar-technician and luthier discussion threads converge on a working range of roughly 2–6 cents (tighter for critical bridge-saddle work, looser for general setup), and published psychoacoustic pitch-discrimination research places the just-noticeable difference for most listeners in a similar few-cents range. 5 cents sits inside that commonly cited range as a workable mid-point. | The dilemma's D5 recommendation is sensitive to this value — the answer is sensitive to where this line is drawn. |
| MA2 | Number of frets on this neck | 22 | Falls inside the 21–24 fret range StewMac states is typical for a modern electric guitar [S4]; this build's exact count is a shop/client choice, not a published standard. | Low — the fret count does not change the per-fret math in D1–D4; it only bounds how many rows Appendix B/C could in principle extend to. |
| MA3 | Client turnaround (days from today) | 5 days | Consistent with the Overview's "before the week is out" and a realistic fast custom-shop turnaround for a fretting job on an otherwise-finished neck. | Low for D1–D4; relevant context for D5's discussion of whether a re-fret is survivable within the deadline. |

---

## Appendix G — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Exact formula for fret distance from the nut under equal temperament, and the numeric value of the twelfth root of two | distance(n) = L × [1 − (1/2)^(n/12)]; twelfth root of two ≈ 1.0594630943593 | Liutaio Mottola — ["Calculating Fret Positions"](https://www.liutaiomottola.com/formulae/fret.htm) | accessed 2026-08-24 | HIGH |
| S2 | The modern, more precise fret-spacing divisor some shops use instead of the traditional 18 | 17.817154 | StewMac — ["Fret Scale Rule Instructions"](https://www.stewmac.com/video-and-ideas/online-resources/learn-about-guitar-and-instrument-fretting-and-fretwork/fret-scale-rule-instructions/) | accessed 2026-08-24 | HIGH |
| S3 | The traditional "rule of 18" historically used an exact whole-number divisor of 18, and produces frets that trend flat of true equal temperament | divisor = 18 (exact) | Liutaio Mottola — ["Was the Rule of 18 Good Enough?"](https://www.liutaiomottola.com/PrevPubs/RuleOf18/RuleOf18.htm) | accessed 2026-08-24 | HIGH |
| S4 | Named standard guitar scale lengths and typical modern-electric fret-count range | Fender-style 25.5 in; Gibson-style 24.75 in; PRS-style 25 in; 21–24 frets typical | StewMac — ["Guitar Scale Length Explained"](https://www.stewmac.com/video-and-ideas/online-resources/learn-about-guitar-and-instrument-fretting-and-fretwork/scale-length-explained/) | accessed 2026-08-24 | HIGH |

All computed fret-position, cents-of-deviation, and GCF-ratio figures in Appendices B, C, D, and E are **derived** from S1/S3 (the governing formulas) and S4 (the scale length), not independently sourced numbers — the arithmetic is shown at each step so a reader can verify it.

Referenced from Background ("All figures in this case are sourced or derived in Appendix G, with any unsourced scenario figures stated openly in the Modeling Assumptions block above.").

---

## Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Greatest Common Factor
- Factor
- Exponent (also Power)
- Ratio

**"How to…" questions**

- How to find the greatest common factor of a set of numbers
- How to evaluate an exponential expression
- How to find equivalent ratios
