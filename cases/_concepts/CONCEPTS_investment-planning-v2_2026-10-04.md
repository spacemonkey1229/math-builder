# Concepts — Gao structure, fused with real stories (v2) — 2026-10-04

**Supersedes** `CONCEPTS_investment-planning_2026-10-03.md` (correct math, no soul: a generic analyst picking a percentile).

## The idea: the Gao case is three structures, not one portfolio
1. **Fund a fixed promise from an uncertain pool** (ten $50K payments from a risky portfolio).
2. **Quote a credible range** before the outcome is known (the 2031 sponsor range).
3. **Sequence risk** (same average, different order, different survival once money leaves).

Money is only one costume. The same three structures run the **Colorado River**, **hurricane evacuation**, **Voyager's power
budget** and **Hubble's gyros**, each with a true story, free public data, and a domain the corpus has not touched
(hydrology 0 cases, climate 0, spaceflight 0 cases; disaster-response 3).

Spine sweep: zero n==0 skills, so the reinforcement-carve-out bar applies (>= 2 thin skills genuinely forced).
Rubric unchanged: score = sum(1.0 how-to / 0.6 term) x availability; calibration anchor = Cold Chain at 4.2.

| Concept | Domain | Score | Tier | Thin forced | Data | Verdict |
|---|---|---|---|---|---|---|
| **C1 The Compact** | hydrology-water | 9.6 | T4 | 6 | HIGH | **Write** |
| **C2 The Cone** | climate / disaster-response | 8.0 | T3 | 5 | HIGH | **Write** |
| C3 The Last Instrument | spaceflight | 5.3 | T4 | 6 | MEDIUM | Research first, then write |
| C4 The One-Gyro Decision | spaceflight | 4.1 | T3 | 2 | MEDIUM | Hold (below anchor; 2 thin) |
| C5 Sell the Songs | music business | 4.1 | T4 | 5 | MEDIUM | Hold (data unverified) |

**Recommendation.** Write **C1** and **C2**. Both have HIGH, fetched, raw student-explorable data, force 11 thin skills between them,
and sit in domains with no cases. Take **C3** next once its one unpublished figure (Voyager's power margin) is researched; it is the
most emotionally compelling and the most current. Hold C4 and C5. Spaceflight is the only domain used twice, so write at most one of C3/C4.

---

### C1 — The Compact   ·   score 9.6   ·   tier T4
**Protagonist.** Camille Duarte, water-resources planner for a fast-growing Arizona city. Personally at stake: her city signs a
ten-year supply promise to new neighborhoods, and its Colorado River share is among the first cut in a shortage.
**The dilemma.** A.) Size the promise on the **full 1906-2024 river record** (119 years, includes the wet early decades) OR
B.) Size it on the **last 25 years** (fewer data, but the warmer, drier river the city actually lives on).
**Primary metric.** Acre-feet per year promised, per percentage point of historical 10-year windows in which river flow falls short of it.
**Why it's close.** A rests on far more data; B rests on the data that is more relevant. A straight-line fit through the whole record
already slopes downward, so a third reading (extrapolate the trend) lands between them. Each is defensible; none is obviously 2x better.
The Gao fusion: storage as a **reserve** (S(t+1) = S(t) + inflow - release), the quoted figure as a **range**, and drought years that
**cluster** (order matters once water leaves the reservoir).
**Would close (12 skills, 6 how-to / 6 term):**
| id | kind | label | spine n |
|---|---|---|---|
| statistics-and-probability-quartiles | term | Quartiles | 3 ◀ thin |
| statistics-and-probability-box-and-whisker-plot | term | Box And Whisker Plot | 3 ◀ thin |
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data | how-to | How to create a box and whisker plot given a set of data | 1 ◀ thin |
| statistics-and-probability-median | term | Median | 8 |
| statistics-and-probability-outlier | term | Outlier | 4 |
| statistics-and-probability-line-of-best-fit | term | Line Of Best Fit | 3 ◀ thin |
| statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data | how-to | How to draw a line of best fit given a set of data | 3 ◀ thin |
| discrete-mathematics-recursive-formula | term | Recursive Formula | 4 |
| discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence | how-to | How to write a recursive formula for a sequence | 4 |
| statistics-and-probability-how-to-find-a-missing-data-element-given-the-mean-and-the-remaining- | how-to | How to find a missing data element given the mean and the remaining elements of its set | 1 ◀ thin |
| statistics-and-probability-how-to-find-the-mean-of-a-set-of-data | how-to | How to find the mean of a set of data | 25 |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | How to find the percent of a number | 89 |
**Data feasibility: HIGH.** Reclamation, *Colorado River Natural Flow Data* (`usbr.gov/lc/region/g4000/NaturalFlow/`): current Excel 1906-2020, provisional 1906-2024; **fetched 2026-10-04**, free .xlsx. Stretch (not counted): NOAA paleoclimate tree-ring reconstruction of the river back centuries, showing the early record was unusually wet.
Not confident about (verify in case-research): the 1922 Compact's assumed flow and apportionment; the city's real shortage priority; units of the Excel columns (the page did not state them).
**Timeliness.** The 2007 operating guidelines expire at the end of 2026; the next set is being negotiated now (verify current status).
**Sensitivity (SPEC §6).** NONE.   **Split risk.** NONE (12 skills).

### C2 — The Cone   ·   score 8.0   ·   tier T3
**Protagonist.** Dana Ortiz, emergency-management director of a Gulf Coast county, the night a hurricane is two days out. Personally at stake: order too wide and people stop obeying orders; too narrow and some are left in the path.
**The dilemma.** A.) Evacuate the area inside the **official NHC cone circle at 72 hours** (2026 Atlantic radius 95 nautical miles, set to cover two-thirds of past errors) OR B.) Evacuate a circle sized to the **90th percentile** of the same errors.
**Primary metric.** Residents ordered out per percentage point of additional historical forecast tracks covered.
**Why it's close.** Going from 67% to 90% coverage needs a larger radius, but **area grows with the square of the radius**, so the people ordered out grow much faster than the coverage gained. Students find that crux themselves from raw errors. A second tension: the cone only uses the last 5 years of errors, and errors have fallen steadily since 1970, so the right sample window is itself a choice (a line of best fit over the 1970-2025 record).
**Would close (10 skills, 5 how-to / 5 term):**
| id | kind | label | spine n |
|---|---|---|---|
| statistics-and-probability-quartiles | term | Quartiles | 3 ◀ thin |
| statistics-and-probability-box-and-whisker-plot | term | Box And Whisker Plot | 3 ◀ thin |
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data | how-to | How to create a box and whisker plot given a set of data | 1 ◀ thin |
| statistics-and-probability-outlier | term | Outlier | 4 |
| statistics-and-probability-line-of-best-fit | term | Line Of Best Fit | 3 ◀ thin |
| statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data | how-to | How to draw a line of best fit given a set of data | 3 ◀ thin |
| geometry-radius | term | Radius | 5 |
| geometry-how-to-find-the-area-of-a-circle | how-to | How to find the area of a circle | 5 |
| measurement-how-to-find-a-missing-amount-in-a-proportion | how-to | How to find a missing amount in a proportion | 13 |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | How to find the percent of a number | 89 |
**Data feasibility: HIGH.** NHC, *Official Atlantic Track Forecast Errors 1970-2025* (`nhc.noaa.gov/verification/verify7.shtml`, zip/text files) and *About the Cone* (`nhc.noaa.gov/aboutcone.shtml`): both **fetched 2026-10-04**; page states the cone circle is sized so two-thirds of 5-year historical errors fall inside, with a 2026 radii table (12 h 25 nm ... 120 h 200 nm, from 2021-2025 errors).
Not confident about: residents per square mile (Census block data, to assemble); a real coastal county's zone boundaries.
**Sensitivity (SPEC §6).** FLAG: hurricane evacuation. Facilitator note: no casualty counts, no named-storm fatalities; frame as zone sizing and order compliance.
**Split risk.** NONE.

### C3 — The Last Instrument   ·   score 5.3   ·   tier T4
**Protagonist.** A flight engineer on the Voyager team at JPL (fictional person; real team). Personally at stake: the only working spacecraft that ever left the Sun's bubble, launched 1977, is running out of electricity.
**The dilemma.** A.) Run the "Big Bang" power fix on Voyager 1 **now**, while the margin from the latest instrument shutdown lasts OR B.) **Wait for the Voyager 2 test** first, as the team's own plan says, and spend that margin.
**Primary metric.** Expected additional years of Voyager 1 operation.
**Why it's close.** Power falls by about 4 W a year, an arithmetic sequence that makes waiting cost real margin. Acting now risks an untried fix on the only craft at that distance. How good the fix is, and how likely it is to fail, are the open numbers: a stated Modeling Assumption and the lever that sets the margin. **Balance is fragile and must be tuned in research.** NASA has not framed it as this binary; the case must label it as constructed.
**Would close (10 skills, 7 how-to / 3 term):**
| id | kind | label | spine n |
|---|---|---|---|
| calculus-sequence | term | Sequence | 3 ◀ thin |
| calculus-series | term | Series | 2 ◀ thin |
| discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula | how-to | How to convert a recursive formula to an explicit formula | 3 ◀ thin |
| discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence | how-to | How to write a recursive formula for a sequence | 4 |
| statistics-and-probability-how-to-find-a-missing-data-element-given-the-mean-and-the-remaining- | how-to | How to find a missing data element given the mean and the remaining elements of its set | 1 ◀ thin |
| statistics-and-probability-line-of-best-fit | term | Line Of Best Fit | 3 ◀ thin |
| statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data | how-to | How to draw a line of best fit given a set of data | 3 ◀ thin |
| advanced-operations-how-to-evaluate-an-exponential-expression | how-to | How to evaluate an exponential expression | 8 |
| measurement-how-to-find-a-missing-amount-in-a-proportion | how-to | How to find a missing amount in a proportion | 13 |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | How to find the percent of a number | 89 |
**Data feasibility: MEDIUM.** NASA blog "NASA Shuts Off Instrument on Voyager 1 to Keep Spacecraft Operating," 2026-04-17 (`science.nasa.gov/blogs/voyager/2026/04/17/...`), **fetched 2026-10-04**: both probes lose about 4 W/yr; LECP shut off with a 0.5 W motor left on; "about a year of breathing room"; the Big Bang is to be tested on Voyager 2 first.
Not confident about: the actual remaining power margin (unpublished), and instruments remaining (**NASA says two; one aggregator says three: use NASA**). Both become assumptions.
**Sensitivity.** NONE.   **Split risk.** NONE.

### C4 — The One-Gyro Decision   ·   score 4.1   ·   tier T3   ·   HOLD
**Protagonist.** A Hubble operations scientist at STScI, June 2024.
**The dilemma.** A.) Keep **two gyros** running (full observing time, both wearing) OR B.) Switch to **one-gyro mode** (fewer orbits, the other gyro preserved as a backup).
**Primary metric.** Expected observing orbits through 2035.
**Why it's close.** One-gyro mode costs observing time but protects the telescope's survival odds. Independent failure events and combinations decide the odds.
**Would close (8 skills, 5 how-to / 3 term):**
| id | kind | label | spine n |
|---|---|---|---|
| statistics-and-probability-independent-event | term | Independent Event | 2 ◀ thin |
| statistics-and-probability-combination | term | Combination | 4 |
| statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination | how-to | How to determine the number of outcomes of a combination | 2 ◀ thin |
| statistics-and-probability-experimental-probability | term | Experimental Probability | 4 |
| statistics-and-probability-how-to-determine-the-probability-of-a-compound-event | how-to | How to determine the probability of a compound event | 7 |
| statistics-and-probability-how-to-determine-the-probability-of-a-single-event | how-to | How to determine the probability of a single event | 14 |
| advanced-operations-how-to-evaluate-an-exponential-expression | how-to | How to evaluate an exponential expression | 8 |
| advanced-numbers-how-to-convert-numbers-to-percents | how-to | How to convert numbers to percents | 42 |
**Data feasibility: MEDIUM.** NASA one-gyro page **fetched**: 3 of 6 gyros failed; 8 of 22 gyros have failed in Hubble's history. Orbits per week (85 to 74) and ">70% chance of a gyro through 2035" come from news coverage only, **not the primary page**; need NASA/STScI sources.
**Why hold.** Score 4.1 is under the 4.2 anchor, only 2 thin skills (it is C3's coin-flip math in a costume), and spaceflight is already used by C3.

### C5 — Sell the Songs   ·   score 4.1   ·   tier T4   ·   HOLD
**Protagonist.** A manager for an indie artist whose back catalog just got a buyout offer (echoing the real masters fight over an artist's early albums).
**The dilemma.** A.) Sell the catalog now at a lump-sum multiple of yearly royalties OR B.) Keep it and collect a royalty stream that decays each year.
**Primary metric.** Present value of the royalty stream as a multiple of year-one royalties.
**Why it's close.** A decaying stream is a convergent geometric series; the buyer's multiple is effectively its price, and the artist's own decay rate decides whether the offer is fair.
**Would close (8 skills, 5 how-to / 3 term):**
| id | kind | label | spine n |
|---|---|---|---|
| calculus-series | term | Series | 2 ◀ thin |
| calculus-sequence | term | Sequence | 3 ◀ thin |
| calculus-how-to-determine-whether-a-series-converges-or-diverges | how-to | How to determine whether a series converges or diverges | 2 ◀ thin |
| pre-calculus-limit | term | Limit | 2 ◀ thin |
| discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula | how-to | How to convert a recursive formula to an explicit formula | 3 ◀ thin |
| advanced-operations-how-to-evaluate-an-exponential-expression | how-to | How to evaluate an exponential expression | 8 |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | How to find the percent of a number | 89 |
| advanced-numbers-how-to-convert-numbers-to-percents | how-to | How to convert numbers to percents | 42 |
**Data feasibility: MEDIUM.** Spotify *Loud & Clear* exists, but its figures were **not retrievable** from the landing page; catalog-sale multiples and per-stream rates are unverified. **Hold until a source is fetched.**

### Killed
- **Everest oxygen ladder**: strongest "reserve" story but death-adjacent (SPEC §6) and the expedition database is not freely downloadable.
- **Kickstarter delivery-date range**: great Gao analogue, but no public data on actual vs promised delivery.
- **Marathon pacing (Kipchoge)**: fits sequence-risk, but sports already holds 7 cases and `the-eight-second-tour` covers drag.

**Next step:** R1a/R1b/R1c review on C1-C3, then `Approve a concept, then run case-write on it.`
