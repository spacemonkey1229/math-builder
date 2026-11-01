# Review brief: investment-planning v2 slate, C1-C3 (R1a / R1b / R1c)

**Sheet reviewed:** `CONCEPTS_investment-planning-v2_2026-10-04.md`. **Gate:** proceed only if R1a, R1b and R1c are unanimous.

## Verdicts (round 1, 2026-10-04)
| Concept | R1a math | R1b evidence | R1c student/corpus | Unanimous GO? |
|---|---|---|---|---|
| C1 The Compact | REVISE: metric degenerates; overlapping windows not independent; "missing-element-of-mean" is a false claim | REVISE: timeliness claim stale; Lees Ferry natural flow is a proxy for a CAP city; 2024 is an estimate | REVISE: option B is the consensus answer (lopsided); overlaps Powell concept in `CONCEPTS_hydrology-water_2026-10-03.md` | No. Fixable. |
| C2 The Cone | REVISE (heavy): fails balance on the stated metric; metric undefined for A | GO (minor): data confirmed live and reproduces the published radius | REVISE: cone is not an evacuation order; needs fictional storm and stronger sensitivity handling | No. Fixable. |
| C3 The Last Instrument | DROP as written: power margin and failure odds are invented | DROP as written: premise is stale | REVISE (heavy): waiting is the obvious answer; constructed binary; space cluster over-mined | No. DROP as written. |

## Findings that change the sheet
**C1**
- Replace the metric with the largest promise that fails in at most 10% of rolling 10-year windows, compared across A and B (a quantile). Teach non-overlapping blocks or a bootstrap (about 11 independent windows in the full record, about 2.5 in the last 25 years).
- Drop `how-to-find-a-missing-data-element...` (nothing solves for a missing element). Thin-forced count 6 to 5. State the storage balance S(t+1) = S + inflow - release as an assumption.
- Pick one framing: the trend-line "third option" breaks the binary.
- Make B costly (a neighborhood told "no" or "fewer homes") and A costly (homes stranded in a dry decade). Label as constructed.
- Balance looks plausible: R1b measured Lees Ferry water-year means of 14.63 MAF (1906-2024) vs 12.40 (2000-2024), about 15% apart; median 14.45 vs 12.32; trend about -0.035 MAF per year; share of 10-year windows below 13 MAF about 14.5%.
- Timeliness line was wrong. Reclamation issued the post-2026 Record of Decision on 21 Aug 2026 with two-year guidelines; the 2007 rules and 2019 DCP expire end of 2026. It is not "being negotiated now".
- Cite `LFnatFlow1906-2024.2024.9.12.xlsx` (Lees Ferry only, acre-feet, 119 water years; 2024 is a provisional estimate, no 2025). 1922 Compact: 7.5 MAF/yr per basin, 75 MAF per 10 years at Lees Ferry. The "16.4 MAF assumed" claim is still unsourced; cite a CRS document or drop it.
- A CAP city's supply depends on Lake Mead tiers, not Lees Ferry flow: state the proxy.
- Sequence behind or differentiate from the Powell supply-operations concept (same river and portal, different decision).

**C2**
- R1b reproduced from raw errors (2021-2025, 72 h, 669 forecasts): 66.7th percentile 92.7 nm (published 95), 90th percentile 152 nm, area ratio about 2.6 (R1a's circular-Gaussian estimate was 2.1). On "additional coverage" the per-point cost for B is roughly 2x A's, far past the ~20% margin.
- Redesign proposal (not yet reviewed): state a loss (cost of leaving a resident uncovered vs ordering one out unnecessarily), then pick options adjacent to its optimum so the two come close; absolute metric, not a ratio.
- Data trap: columns `F012..F168` are availability flags; the errors are `xxxhT01` (nm); `-9999` is missing. Link the format PDF. Errors from one storm are autocorrelated (669 six-hourly rows, far fewer independent storms).
- The cone covers each forecast's error, not "the storm path". Word it carefully. Census residents per area is unverified: scenario input.
- Fictional storm, no casualty figures, in-case note that surge zones (not the cone) drive real orders, classroom note that some students have evacuated. Name percentiles honestly (not quartiles). Tier T4 if percentiles from data plus trend are required.

**C3**
- NASA's Aug 2026 post reports the "Big Bang" already ran successfully on Voyager 2; the same swap is planned for Voyager 1 "in the coming months". The Voyager 2 test is done, so option B no longer exists.
- The sheet's "only craft that ever left the Sun's bubble" is false (Voyager 2 crossed in 2018 and still works). The "two vs three instruments" conflict was a Voyager 1 vs Voyager 2 mix-up (V1: two left; V2: three).
- No published power margin exists. Hold; do not rework unless a public source for the margin appears.

## Disposition
C1, C2: REVISE and resubmit to round 2. C3: DROP as written.

---

# Round 2 (2026-10-04) — `CONCEPTS_investment-planning-v3_2026-10-04.md`

| Concept | R1a math | R1b evidence | R1c student/corpus | Unanimous GO? |
|---|---|---|---|---|
| C1 The Compact | REVISE (minor), then GO: all numbers recomputed and match; outlier robust to every quartile method | REVISE (minor): Compact "wet decade" wording must change; fill in D4 and household sources | REVISE (minor): human-scale stakes; make the 1915-24 outlier the reveal | No. Minor fixes only. |
| C2 The Cone | REVISE (substantive): π dropped, loss-table error at k=80k, A/B binary dominated by an in-between radius | REVISE: NOAA's 2026 experimental 90% cone changes option B; no free anchor for k | REVISE (heavier): k not student-ownable; overlaps the Ian evacuation concept; shares ~7 skills with C1 | No. Needs a decision, see below. |

## C1 fixes before round 3
- Put A's and B's downside in the same currency (homes stranded vs lots refused); say B's 11.99 rests on 2 independent decades.
- Name the quartile method (Excel and textbook differ at n=11; the 1915-24 verdict holds under all methods tested, fences 16.24-16.77).
- **Correct the Compact claim.** v3 said it was "negotiated at the end of that wet decade." The Compact was signed 24 Nov 1922, so two of the ten years in 1915-24 postdate it. Claimable: "signed in 1922 during an unusually wet stretch of the record; students find 1915-24 is the one outlier decade; CRS says the assumed 16.4 MAF/yr is well above the 1906-2024 average of 14.6." Read Compact Art. III(a) and (d) directly in case-research.
- D4 inputs: Lake Powell total capacity 25,160,000 acre-feet at 3,700 ft (Reclamation, `usbr.gov/uc/rm/crsp/gc/`); Lake Mead live storage about 26.12 MAF (2022 Reclamation capacity PDF, **unconfirmed**); older Powell figure 24.3 MAF still circulates, so pick one and cite. ADWR: about 3-3.5 homes per acre-foot (about 0.29-0.33 AF/home/yr), seen only in a search summary; **verify in a browser**.
- Open on a named family or lot ("Lot 14, closing in March"); promote the outlier and the Compact to the reveal; frame the 11-blocks lesson as "how much do I really know?"; never say "Powell" in student text; confirm D4 does not become a second metric.
- Recompute everything from fresh downloads.

## C2 findings
- **R1a:** use πr² (k* about 20,800) or define the unit; at k=80,000 the best radius is 130.5 nm (not 127) and A is 21% above the minimum; at every k tested a radius between A and B beats both, so the binary is decorative unless the county is limited to the two published products; derive k from stated inputs (density, cost per person, cost per miss) with a range; 1970 has only 2 forecasts (start at 1971 or weight); the trend slope depends on the window (about -3.9 nm/yr over 5 years vs -7.3 over the full record); add a by-storm bootstrap.
- **R1b:** NOAA announced an experimental 2026 cone using ellipses covering 90% instead of 67%, so option B partly exists as a real NHC product (`noaa.gov/news-release/national-hurricane-center-to-issue-new-forecast-cone-graphics-for-2026-hurricane-season`). NHC says the cone gives "little to no information about projected impacts". **No free, student-checkable figure for k exists.** Best anchors measure only the evacuation-cost side: Whitehead 2003, "One Million Dollars per Mile?" (about $194-$211 per household voluntary, $292+ mandatory, from search summaries; read the papers first).
- **R1c:** a different file, `CONCEPTS_disaster-response_2026-10-04.md` C1 (Hurricane Ian, Lee County just-in-time order), already covers a Gulf Coast evacuation decision, and it anchors its value-of-life term to sourced ranges. Two hurricane evacuation cases in one batch is too many.

## Disposition
- **C1: REVISE (minor)** and resubmit to a short round 3.
- **C2: HOLD** for a scope decision (fold into the Ian concept, or recast on the NOAA 2026 cone-change question with the county limited to two published products, or drop).
