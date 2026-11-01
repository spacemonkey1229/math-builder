# Concepts — Gao structure fused with real stories (v3, revised after R1 round 1) — 2026-10-04

**Supersedes** v2 for C1 and C2. **C3 (The Last Instrument) is DROPPED as written** (R1a/R1b: premise stale, margin unpublished; R1c: strawman). See `REVIEW_BRIEF_investment-planning-v2_2026-10-04.md`.
All numbers below were **computed from the real files** (R1b's downloads in the session scratchpad: Lees Ferry water-year natural flow 1906-2024; NHC OFCL Atlantic errors 1970-2025). They must be recomputed in case-research from fresh downloads.

| Concept | Domain | Score | Tier | Thin forced | Data | Round-1 findings addressed |
|---|---|---|---|---|---|---|
| **C1 The Compact** | hydrology-water | 8.6 | T4 | 5 | HIGH | metric, false skill, independence, framing, timeliness, proxy, Powell overlap |
| **C2 The Cone** | climate / disaster-response | 8.0 | T4 | 5 | HIGH | balance, undefined metric, evacuation framing, F-column trap, sensitivity |

---

### C1 — The Compact   ·   score 8.6   ·   tier T4
**Protagonist.** Camille Duarte, water-resources planner for a fast-growing Arizona city (fictional). A builder, **Saguaro Ridge** (fictional), needs her written promise of ten years of water before the city will approve its lots. Personally at stake: the families who buy those lots, and her signature.
**The dilemma.** A.) Size the promise on the **full 1906-2024 record**: more data, a larger promise, more homes approved OR B.) Size it on the **2000-2024 record**: the river the city actually lives on, a smaller promise, fewer homes now.
**Primary metric.** The largest river-equivalent promise (MAF/yr) that fails in no more than 10% of 10-year windows, under each baseline. (A quantile, defined at any shortfall rate.)
**Computed from the real data (to re-verify).**
| | Full record (110 windows) | 2000-2024 (16 windows) |
|---|---|---|
| Largest promise failing in <= 10% of windows (10th percentile of window means) | **12.60 MAF/yr** | **11.99 MAF/yr** |
| Gap | | **4.9%** of the promise (well inside the ~20% balance rule) |
| Cost if the other baseline is the truth | A's 12.60 fails in **5 of 16 (31%)** recent windows | B gives up **0.62 MAF/yr** (4.9%) of homes if the long record is the truth |
Window means: full record mean 14.61, 2000-2024 mean 12.92 MAF/yr. Trend slope -0.0355 MAF/yr (about -3.5 MAF/yr per century); 1906-1962 mean 15.45 vs 1963-2024 mean 13.88.
**Why it's close.** A promises about 5% more homes but, if the recent river persists, fails about three times as often as the 10% it advertises. B protects against that and costs the builder real lots. Neither is the consensus answer, because the gap is small and the downside of each is quantified in the other's currency. The trend line is **not** a third option: it is a deliverable that shows why extrapolating a 119-point autocorrelated series is descriptive only.
**The independence lesson (R1a).** 110 overlapping windows are really **11 independent 10-year blocks**; the recent record has only **2**. Students recompute shortfall on non-overlapping blocks and see how little precision the 16 recent windows carry.
**The Compact discovery.** Among the 11 non-overlapping 10-year block means, **1915-1924 (18.2 MAF/yr) is the only outlier** (Q1 13.63, Q3 14.77, upper fence 16.47). The 1922 Compact was negotiated at the end of that wet decade (verify date and wording against a CRS summary). Students find the outlier themselves.
**Gao fusion kept.** Reserve (D4: a stylized storage balance with a floor at empty and a cap at full, where the order of wet and dry years now matters, unlike with no walls), range (the quantile), sequence risk.
**Deliverables → skills (all genuinely forced):**
| id | kind | label | spine n | forced by |
|---|---|---|---|---|
| statistics-and-probability-quartiles | term | Quartiles | 3 ◀ thin | D1 box plot of 10-year block means |
| statistics-and-probability-box-and-whisker-plot | term | Box And Whisker Plot | 3 ◀ thin | D1 |
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data | how-to | How to create a box and whisker plot given a set of data | 1 ◀ thin | D1 |
| statistics-and-probability-median | term | Median | 8 | D1 |
| statistics-and-probability-outlier | term | Outlier | 4 | D2 fence test on blocks (1915-24 flagged) |
| statistics-and-probability-line-of-best-fit | term | Line Of Best Fit | 3 ◀ thin | D3 trend line, with the argument for not extrapolating it |
| statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data | how-to | How to draw a line of best fit given a set of data | 3 ◀ thin | D3 trend line, with the argument for not extrapolating it |
| discrete-mathematics-recursive-formula | term | Recursive Formula | 4 | D4 stylized reservoir S(t+1)=S(t)+inflow-release, floor 0 and cap |
| discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence | how-to | How to write a recursive formula for a sequence | 4 | D4 stylized reservoir S(t+1)=S(t)+inflow-release, floor 0 and cap |
| statistics-and-probability-how-to-find-the-mean-of-a-set-of-data | how-to | How to find the mean of a set of data | 25 | D1 window and block means |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | How to find the percent of a number | 89 | D5 shortfall share, promise as % of record |
Dropped from v2: `how-to-find-a-missing-data-element...` (nothing solved for an unknown element).
**Data feasibility: HIGH.** Reclamation `LFnatFlow1906-2024.2024.9.12.xlsx` (page `usbr.gov/lc/region/g4000/NaturalFlow/provisional.html`): Lees Ferry only, acre-feet, 119 water years; confirmed free and opened (R1b). 2024 is a **provisional estimate**; there is no 2025 value; the post-2000 window leans on estimated recent years. Compact: 7.5 MAF/yr per basin, 75 MAF per 10 years at Lees Ferry (CRS IN11982 via R1b).
**Constructed binary + proxy, stated in the case.** No planner faced exactly "full record vs last 25 years." Natural flow at Lees Ferry is not what a CAP city receives (its supply follows Lake Mead tiers, and CAP is junior in a shortage per CAP/ADWR/PPIC pages via R1b); the case uses river-equivalent promise as a stated proxy and says so.
**Timeliness.** The 2007 guidelines and 2019 Drought Contingency Plans expire at the end of 2026; Reclamation issued the post-2026 Record of Decision on **21 Aug 2026** with two-year operating guidelines (`usbr.gov/ColoradoRiverBasin/post2026/`).
**Still to research.** Reservoir capacities for D4 (cite Reclamation), acre-feet per home (cite ADWR or similar), the Compact date and wording.
**Overlap.** Same river and portal as the unreviewed Powell concept (`CONCEPTS_hydrology-water_2026-10-03.md` C2 "Whose Acre-Feet"). That one is **supply operations** (reservoir volume/area, where to find 500,000 acre-feet); C1 is **demand-side promise sizing** from natural flow. Different decision and math. Sequence C2 (Cone) first, then C1.
**Sensitivity (SPEC §6).** NONE.   **Split risk.** NONE (11 skills).

### C2 — The Cone   ·   score 8.0   ·   tier T4
**Protagonist.** Dana Ortiz, emergency-management director of a Gulf Coast county (fictional), with a **fictional storm** two days out. She is not choosing "the cone." She is choosing **the radius around the forecast point that her county will treat as at risk** for its own planning, with the National Hurricane Center's cone as the anchor.
**The dilemma.** A.) Use the **official cone radius** at 72 h (2026 Atlantic: **95 nm**, set so about two-thirds of 2021-2025 errors fall inside) OR B.) Use the **90th-percentile radius** of the same errors (**152 nm**).
**Primary metric.** Expected loss, in "order-out equivalents": **L(r) = r² + k × P(error > r)**, where r² is the area ordered out (in nm², dropping the constant π) and k is Dana's stated exchange rate: how many square nautical miles of unnecessary ordering one unit of "storm lands outside our circle" is worth. Students must choose and defend k.
**Computed from the real errors (to re-verify).** 2021-2025, 72 h, 669 forecasts from **46 storms**: median 67.1; Q1 43.7, Q3 106.0; 66.7th pct 92.7 (published 95); 80th 115.1; 90th 152.1. Coverage of 95 nm is 68.5%, of 152 nm 90.0%. Area ratio (152/95)² = **2.56**.
| Exchange rate k | Best radius | L(95) | L(152) | A vs B |
|---|---|---|---|---|
| 40,000 | 104 nm | 21,641 | 27,110 | A better by 20% |
| 60,000 | 119 nm | 27,949 | 29,113 | **within 4%** |
| 80,000 | 127 nm | 34,257 | 31,116 | B better by 9% |
**Break-even** k\* = (152² - 95²) / (0.900 - 0.685) = **about 65,400 nm²**. Below it the official cone wins; above it the wider circle wins. The case is balanced because the decision hinges on one value judgment that the student must name, size and defend; and both options sit within about 17% of the minimum possible loss near the break-even (at k = 60,000: 12% and 17% above it), which is the flat-bottom insight (the best answer is between A and B).
**This is not a hidden parameter** (R1a's C3 objection): k is declared as the policy judgment, shown in a sensitivity table, and anchored in research to a real figure (county evacuation cost per person, shelter capacity, compliance data), not set by the author to force a winner.
**The window lesson.** Using all 1970-2025 errors, the 66.7th percentile is **206.9 nm**, an area **4.7×** the 2021-2025 one. Yearly mean 72 h error fell from 224 nm (1970) to 84 nm (2025), about **-7.3 nm per year**. Students fit that line to decide whether the 5-year window is fair.
**Statistical honesty.** 669 forecasts come from 46 storms and are strongly autocorrelated; the effective n for a 90th percentile is far smaller. The cone covers each forecast's *error*; it says nothing about wind-field size or surge. Percentiles are not quartiles: the box plot gives Q1/Q3; the 66.7th and 90th are read from the sorted list.
**Deliverables → skills:**
| id | kind | label | spine n | forced by |
|---|---|---|---|---|
| statistics-and-probability-quartiles | term | Quartiles | 3 ◀ thin | D1 box plot of 72 h errors |
| statistics-and-probability-box-and-whisker-plot | term | Box And Whisker Plot | 3 ◀ thin | D1 |
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data | how-to | How to create a box and whisker plot given a set of data | 1 ◀ thin | D1 |
| statistics-and-probability-outlier | term | Outlier | 4 | D1 fence at Q3+1.5 IQR |
| statistics-and-probability-line-of-best-fit | term | Line Of Best Fit | 3 ◀ thin | D3 yearly mean error 1970-2025, to judge the 5-year window |
| statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data | how-to | How to draw a line of best fit given a set of data | 3 ◀ thin | D3 yearly mean error 1970-2025, to judge the 5-year window |
| geometry-radius | term | Radius | 5 | D2 radius from percentile |
| geometry-how-to-find-the-area-of-a-circle | how-to | How to find the area of a circle | 5 | D2 area ordered out |
| measurement-how-to-find-a-missing-amount-in-a-proportion | how-to | How to find a missing amount in a proportion | 13 | D4 scale a sample coast to the county |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | How to find the percent of a number | 89 | D4 coverage and compliance shares |
**Data feasibility: HIGH.** NHC `nhc.noaa.gov/verification/verify7.shtml` → `errors/1970-present_OFCL_v_BCD5_ind_ATL_TI_errors_noTDs.txt` (4 MB, 13,278 six-hourly rows; fetched and reproduced by R1b and again here). **Student trap, stated in the brief:** columns `F012..F168` are availability flags (0 or 0.33), **not errors**; the errors are `xxxhT01` (nm); `-9999` is missing. Link the format PDF. Cone method and 2026 radii: `nhc.noaa.gov/aboutcone.shtml`.
Scenario inputs (not observed data, so labeled): residents per square mile along the coast (Census), shelter capacity.
**Sensitivity (SPEC §6).** FLAG, with the full treatment R1c asked for: fictional storm (no named hurricane); no casualty figures anywhere in student text; an in-case note that real evacuation orders use **surge zones and wind forecasts**, and the cone is not an evacuation zone; a classroom note that some students may have evacuated and may opt out.
**Overlap.** `the-surge-trigger` (epidemic) and `wildfire` (lead time); disaster-response gets a 4th case but this is the only weather-error case.
**Split risk.** NONE (10 skills).
