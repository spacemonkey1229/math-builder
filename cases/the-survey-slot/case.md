Case Study: The Survey Slot
MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

Renee Okafor has the observatory's control-room monitor split into two windows, and she still hasn't clicked either one. On the left: a live countdown to moonrise, the moment tonight's faint-target brightness measurements stop being usable at all. On the right: the queue console, blinking, waiting for her to submit one target assignment before the allocation committee's nightly sign-off (their final go-ahead, needed before the telescope will run either option) closes.

"Four hours," the on-call operator says from the doorway, not really a question. "Which target?"

Renee doesn't decide how many transit candidates the survey program has flagged this month, or how bright the moon comes up. She decides what tonight's one open telescope slot actually points at. Right now there's a folder on her desk — printed, because she reads these on paper — for a single transit candidate the pipeline flagged weeks ago, with a predicted transit window that lines up almost perfectly with tonight. Point the telescope there for the full four hours, watch it happen, and either confirm it or don't.

Next to that folder is a second tab open on her laptop: a target list of twelve unexplored fields, each one a quick look for a brand-new signal nobody has ever flagged. Twelve short looks instead of one long stare. Faster science, if any of them hit. Nothing at all, if none of them do.

The operator is still standing there. The countdown clock ticks down another minute.

Renee pulls both windows to the front of her screen and does not press submit on either one.

---

## Background

Renee Okafor is the telescope-time allocation scheduler for a university robotic (automated-schedule, not manually pointed) observatory's exoplanet (a planet orbiting a star other than our Sun) program. Every clear night, she is personally responsible for deciding what the observatory's single telescope points at during its open science slots, and for defending that recommendation to the program's allocation committee before the night's assignment locks in. Tonight's slot is short — the Moon rises bright enough, partway through the night, to wash out the faint brightness dips this program is built to measure, which caps tonight's usable window at a fixed length regardless of which target Renee picks (SEE APPENDIX B).

Two options are on the table. **The Candidate Watch** commits the full slot to re-observing one already-flagged transit candidate — a star whose brightness-over-time record (a **light curve** — a plot of how bright the star measured at each moment) has already shown one promising dip, now waiting on a second, confirming look during its next predicted transit window — because a transiting planet orbits on a fixed, repeating cycle, the timing of its next dip can be calculated in advance. A transit candidate like this is vetted against a real, published pattern: large all-sky surveys flag many such candidates, and a well-documented fraction of them turn out to be false positives — a background **eclipsing binary star** (two stars orbiting each other, periodically blocking each other's light in a way that can look from far away like one planet crossing in front of one star), an instrument artifact (a glitch in the camera or electronics that mimics a real brightness dip), or a data-processing error mimicking a planet's dip — rather than a genuine transiting planet (SEE APPENDIX A, APPENDIX C). **The Twelve-Field Sweep** instead splits the same slot across twelve short looks at fields the survey has never examined, each one an independent search for a new, as-yet-undetected transit signal (SEE APPENDIX C).

Either option clears the whole slot; neither can be extended once the Moon comes up — no telescope pointing time exists for anything past that boundary, for either option. Appendix C's per-field Sweep rate already represents a genuinely confirmed new detection — the same "survives the false-positive check" standard Appendix A/C applies to The Candidate Watch — not merely a raw, unvetted flag; both options' probabilities answer the same question (did tonight's slot produce a real, confirmed signal), which is what makes Challenge D3's comparison a fair one (SEE APPENDIX F, MA6, for exactly how "a confirmed detection" is counted). What Appendix D governs is a separate, later decision drawing on a different, larger population: the automated pipeline's preliminary flags (generous by design, like Appendix A's real TESS pipeline, so it always flags more than the number that go on to survive the false-positive check). The program's small on-call analysis team can only fully write up and cross-check a limited number of tonight's preliminary flags before the morning report is due, so only some get that fuller write-up before the deadline, and the rest wait for the day team to pick up tomorrow (SEE APPENDIX D). The real NASA Exoplanet Archive publishes transit-depth measurements for confirmed planets in a compact scientific-notation form that the program's own report template requires converting to plain decimal notation before it goes in front of the committee (SEE APPENDIX E).

Every figure in this case is either cited to a real published source or disclosed as a stated Modeling Assumption (SEE APPENDIX F, APPENDIX G). The vocabulary and "how to…" skills this case will ask you to research are listed in Appendix H — that is where Challenge 1 sends you.

---

## Dilemma

You are Renee Okafor.

Do you:

**A.)** Run The Candidate Watch — commit the full slot to re-observing the one already-flagged transit candidate **OR**

**B.)** Run The Twelve-Field Sweep — split the slot across twelve independent fields searching for new, undetected transit signals

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A compound-probability calculation for The Twelve-Field Sweep.** Using Appendix C's per-field detection probability, calculate the probability that *at least one* of the twelve independent fields yields a confirmed new detection tonight. Show a probability tree or the complement-rule arithmetic — do not just multiply the per-field probability by twelve and report that as a probability.
- **D2 — A single-event probability statement for The Candidate Watch.** Using Appendix C's non-false-positive rate, state the probability that tonight's re-observation of the flagged candidate confirms a real detection.
- **D3 — An expected-detections-per-hour comparison table.** Using D1, D2, and Appendix B's slot length, compute the expected confirmed detections per hour of telescope time for each option, and the percent margin between them. State which option wins on tonight's numbers.
- **D4 — A write-up combinations-and-permutations plan.** Using Appendix D's preliminary-flag count and same-night write-up capacity, calculate (a) the number of different possible subsets of flagged fields the on-call team could choose to fully write up before the morning deadline (a combination), and (b) the number of different possible orders in which a chosen subset of that size could be written up (a permutation). Explain, using your combination count, why writing up every flagged field before the deadline is not realistic tonight.
- **D5 — A standard-notation data table.** Using Appendix E's real transit-depth figures (given in scientific notation), convert each to standard (decimal) notation. Then identify which columns in Appendix E are not needed to answer tonight's question, and explain why.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A — Transit Candidates and Vetting: The Real Numbers

Referenced in Background and Challenge 3 (D2). A transit candidate is a star whose brightness dipped in a pattern consistent with a planet passing in front of it. Large sky surveys flag thousands of these, but not every flagged candidate is a real planet. NASA's TESS (Transiting Exoplanet Survey Satellite) mission publishes its full list of flagged candidates — called TESS Objects of Interest, or TOIs — and tracks which ones follow-up observation later re-classifies as false positives: a background eclipsing binary star, an instrument artifact (a glitch in the camera or electronics mimicking a real dip), or a data-processing error that only looked like a planet's dip [S1].

| Outcome, TESS Prime Mission TOI catalog | Count | Share |
|---|---|---|
| Total TOIs in the catalog | 2,241 | 100% |
| Re-classified as false positives after follow-up | 565 | ≈25.2% |
| Remaining candidates (planet candidates or confirmed planets) | 1,676 | ≈74.8% |

This case does not need the specific reasons a candidate becomes a false positive — they are included here because the vetting system is real and because the "not every flagged dip is a real planet" fact is exactly why a second, confirming look matters.

---

## Appendix B — Tonight's Slot

Referenced in Background and Challenge 3 (D3).

| Quantity | Value | How it's set |
|---|---|---|
| Length of tonight's open telescope slot | **4 hours** | Fixed by tonight's moonrise time — the point at which scattered moonlight overwhelms the faint brightness dips this program measures. Identical regardless of which option is chosen. |
| Number of fields in The Twelve-Field Sweep | **12** | The survey's standard field count for one open slot's "shallow sweep" — a quick, short look at each field, as opposed to a single long stare at one target — sized so each field gets a short, equal-length look within the available time. |
| Time per field, Twelve-Field Sweep | **20 minutes** | 4 hours ÷ 12 fields, split evenly. |

These slot parameters are specific to tonight's schedule and are disclosed Modeling Assumptions — see Appendix F, MA1. Every per-hour rate in this case is computed against this fixed 4-hour nominal slot length throughout, even if new information arrives partway through the slot.

---

## Appendix C — Detection Probability Inputs

Referenced in Background and Challenge 3 (D1, D2). Each field's 20-minute look produces its own brightness-versus-time record, screened by the program's detection software the same way real transit-search pipelines work: an automated statistical test flags any dip that crosses a preset significance threshold, the same basic technique real missions use to sort a night's raw data down to a manageable list before a human reviews any of it. This appendix also carries columns that are real, published, and **not needed** to answer tonight's question — deciding what to ignore is part of the work.

| Option | Quantity | Value | Basis |
|---|---|---|---|
| The Candidate Watch | Probability tonight's re-observation confirms a real detection (not a false positive) | **≈74.8%** | Applied from Appendix A's real, published TESS Prime Mission catalog rate [S1] to tonight's specific candidate, as a stated modeling convention — see Appendix F, MA2. |
| The Twelve-Field Sweep | Probability any one field yields a confirmed new detection (not a false positive) in its 20-minute look | **10%** | Disclosed Modeling Assumption, informed by (not equal to) a real completed survey's realized planet-candidate yield per target star [S2] — see Appendix F, MA3. |
| The Twelve-Field Sweep | Average number of catalogued stars per shallow-sweep field | ≈2,400 | Real-format figure, not needed for tonight's calculation at this case's level — already folded into the per-field rate above. |
| The Candidate Watch | Predicted transit duration | 2.1 hours | Real-format figure, texture only — the slot is long enough to cover it either way. |

---

## Appendix D — Same-Night Write-Up Capacity

Referenced in Background and Challenge 3 (D4). This appendix governs a decision that comes *after* tonight's D1–D3 detection math is already settled, and it works from a different, earlier STAGE of the same twelve fields' data — not a confirmed detection, but the raw, generous first-pass flag every 20-minute look produces before the stricter false-positive check (Appendix C) narrows it down. In order, on the same clock as the 4-hour slot: (1) each 20-minute look finishes and the onboard automated significance test — software on the telescope's own computer, checking in real time whether the star's brightness dipped more than random noise would explain — either flags the field or doesn't; (2) after the slot ends, whichever flags came in tonight go through the same false-positive check as The Candidate Watch, which is what Appendix C's confirmed-detection probability describes; (3) separately, once the morning report deadline approaches, the program's small on-call analyst team can only fully write up and cross-check a limited number of tonight's flags before the deadline — this write-up step happens after the 4-hour telescope slot is already over and does not use any telescope time at all. Because the automated flag is deliberately generous — like Appendix A's real TESS pipeline, built to flag anything that might be real rather than risk missing a true signal — a typical night produces more flags than confirmed detections (exactly the same real relationship Appendix A shows for TESS's own catalog, where thousands of preliminary TOIs shake out to far fewer confirmed planets).

| Quantity | Value | Basis |
|---|---|---|
| Number of preliminary flags the same twelve fields' shallow pass typically produces (before the false-positive check narrows them down) | **5, out of the 12** | Disclosed Modeling Assumption — see Appendix F, MA4. |
| Number of those preliminary flags the on-call analysis team can fully write up and cross-check before the morning report deadline | **2** | Disclosed Modeling Assumption, grounded in the real operational fact that a small on-call team has a fixed number of working hours before a fixed deadline — see Appendix F, MA5. |

---

## Appendix E — Real Transit-Depth Data (NASA Exoplanet Archive)

Referenced in Background and Challenge 3 (D5). The NASA Exoplanet Archive publishes transit depth — how much a star's brightness drops during a transit, as a fraction of its total light — for confirmed planets. The archive and its source papers report this fraction in scientific notation.

| Planet | Transit depth (scientific notation, fraction of stellar brightness) | Source |
|---|---|---|
| TOI-700 d | 6.13 × 10⁻⁴ | Spitzer Space Telescope (a retired NASA infrared space telescope) confirmation paper [S3] |
| Kepler-186f | 4.41 × 10⁻⁴ | Derived from Kepler-186f's published planet-to-star radius ratio (how much smaller the planet is than its star — squaring that ratio gives the fraction of the star's light the planet blocks during a transit) [S4] |

Real papers routinely report a depth this small in scientific notation, exactly like the TOI-700 d and Kepler-186f figures above [S5]. This case's report template requires standard (decimal) notation instead, because the committee's spreadsheet tool does not accept scientific notation as input.

---

## Appendix F — Modeling Assumptions

> These figures are **not directly published for tonight's specific slot**. No public source reports a specific observatory's specific nightly target list, its specific candidate's real-time confirmation odds, or its specific analysis-team staffing for a given night — that information is operational and specific to one program on one night. They are stated scenario assumptions chosen by the case author, several of them informed by real published statistics without being identical to them. A Hero may challenge any of these numbers in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Tonight's slot length and field count | 4 hours; 12 fields at 20 min each | No public source publishes one specific observatory's specific nightly schedule. Set at a scale consistent with a real robotic survey program's typical single-slot allocation. | The case's structure depends on this split, but the comparison itself is not sensitive to the exact field count chosen — the same method applies at 10 or 15 fields. |
| MA2 | Probability tonight's specific candidate confirms as a real detection | 74.8% | Applies Appendix A's real, published TESS Prime Mission non-false-positive rate (computed across its whole real catalog of candidates, not for one specific star) [S1] to this one candidate, as a modeling convention — no public source publishes a real-time confirmation probability for one specific, still-unconfirmed candidate. | The case's numbers are sensitive to this figure — see case.json.sensitivity_disclosure. |
| MA3 | Per-field probability of a confirmed new detection in a 20-minute shallow look | 10% | Informed by, but not equal to, a real completed survey's realized planet-candidate yield: Kepler's DR25 catalog (the mission's 25th official data release) identified 4,034 planet candidates from its roughly 200,000 target stars [S2] (a little over 2%) over a four-year continuous baseline. This case's value is set higher than that raw per-star figure to reflect that a single sweep field contains thousands of stars, but lower than what a naive per-star-count scale-up would suggest, to reflect that a 20-minute look is a vastly shorter baseline than four continuous years. No public source publishes a per-field rate for a hypothetical new shallow sweep directly. | The case's numbers are highly sensitive to this figure — see case.json.sensitivity_disclosure. |
| MA4 | Number of preliminary flags (pre-confirmation) in a given night's shallow pass | 5 of 12 | No public source publishes a specific sweep's preliminary-flag rate for a hypothetical new program. Set at a plausible fraction — deliberately higher than Appendix C's ~1-2 expected *confirmed* detections per night — consistent with a real automated significance test flagging more candidates than end up surviving the false-positive check, the same relationship Appendix A shows for TESS's own real catalog. | Changes the size of the combination/permutation counts in D4, not the D1–D3 rate comparison. |
| MA5 | Same-night write-up capacity | 2 of the 5 preliminary flags | Grounded in the real, general operational fact that a small on-call analysis team has a fixed number of working hours before a fixed morning-report deadline; no public source publishes an exact per-night write-up count for a specific program. | Changes the size of the combination/permutation counts in D4 only. |
| MA6 | How "a confirmed detection" is counted, for the purposes of D1 and D3 | A night counts as producing one confirmed detection if *at least one* independent event succeeds — additional simultaneous successes within the same option are not double-counted | This is a stated counting convention, not a sourced figure: Renee's report to the committee is a yes/no ("did tonight's slot produce a new confirmed signal"), not a raw tally, so "at least one" is the quantity that actually matters for both options — and it is the only convention under which The Candidate Watch (which can only ever produce one detection) and The Twelve-Field Sweep are compared on the same basis. Under this convention, D1's compound-probability answer (via the complement rule) is itself the correct "expected confirmed detections" figure for the Sweep, because the expected value of a yes/no (indicator) outcome equals its probability of occurring. | This convention is why D1 uses "at least one," not a raw expected count (12 × the per-field rate) — a raw count answers a different question ("how many total confirmed signals," which is not what a same-night committee report asks) and is not the metric this case uses. |

---

## Appendix G — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | TESS Prime Mission TOI catalog false-positive rate | 565/2,241 TOIs (≈25.2%) re-classified as false positives after follow-up | Guerrero et al. — [The TESS Objects of Interest Catalog from the TESS Prime Mission](https://arxiv.org/pdf/2103.12538), published in *The Astronomical Journal* | 2021 | HIGH |
| S2 | Kepler DR25 planet-candidate yield | 4,034 planet candidates identified from roughly 200,000 target stars (a little over 2%) | Thompson et al. — [Planetary Candidates Observed by Kepler VIII: A Fully Automated Catalog With Measured Completeness and Reliability Based on Data Release 25](https://arxiv.org/abs/1710.06758), *ApJS* 235, 38 | 2018 | HIGH |
| S3 | TOI-700 d transit depth | 0.000613 (fraction of stellar brightness) = 6.13 × 10⁻⁴ | Rodriguez et al. — [The First Habitable Zone Earth-Sized Planet From TESS II: Spitzer Confirms TOI-700 d](https://arxiv.org/pdf/2001.00954) | 2020 | HIGH |
| S4 | Kepler-186f planet-to-star radius ratio (used to derive transit depth: depth = (Rp/Rs)²) | 0.021 → depth ≈ 4.41 × 10⁻⁴ (derived) | [Kepler-186f — Wikipedia](https://en.wikipedia.org/wiki/Kepler-186f), citing Quintana et al. 2014 | accessed 2026-09-18 | MEDIUM (secondary republication of the discovery paper's figure, not the primary paper itself; the depth value is derived by this case from the page's stated radius ratio using the standard transit-depth relation, not read directly off the page) |
| S5 | NASA Exoplanet Archive's Transiting Planets Table reports transit depth as a percentage (its own "Depth [%]" column) | — | NASA Exoplanet Archive — [Data Column Definitions for the Transiting Planets Table](https://exoplanetarchive.ipac.caltech.edu/docs/API_transit_detection.html) | accessed 2026-09-18 | HIGH (context — establishes the real, live, student-explorable data portal this case's Appendix E is drawn from; the archive's own unit is percent, not literally "ppm" or scientific notation, but real published papers on these same planets — S3, S4 — do report depths this small in scientific notation, which is what this case's D5 conversion exercise uses) |

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->

---

## Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Independent Event
- Permutation
- Standard Notation
- Combination
- Theoretical Probability
- Experimental Probability
- Scientific Notation

**"How to…" questions**

- How to determine the number of outcomes of a combination
- How to determine the number of outcomes of a permutation
- How to write a number in standard notation given its scientific notation
- How to determine the probability of a compound event
