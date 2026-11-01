# CONCEPTS: construction-architecture v2 (Built Environment) - 2026-10-28

Single concept, round-2 revision after R1. **Swapped** v1 C1 (Overhang Depth: dropped by R1c as a near-twin of The Tilt Decision; winner flipped at heating weight 0.43 per R1a) for v1 C2 **Up or Out**, re-pulled and recomputed from the live API on **2026-10-28**.
Tags: **[CONFIRMED]** fetched and read; **[DERIVED]** my own python computation on the fetched data; **[UNVERIFIED]** not sourced, must be disclosed as a Modeling Assumption.
Nothing under `cases/<id>/` was created.

## Concept: Up or Out

**Protagonist.** Ilse Marchetti (fictional), a first-year community-college student in Woodhaven, Queens. Her grandparents own the family's two-family house and have set aside their savings so that Nonna can move onto the ground floor with a bathroom and bedroom she can use without stairs; the paperwork has landed on Ilse because she is the one who reads English-language forms fastest. Name grep over `cases/` and `readmodel/`: "Ilse" and "Marchetti" have 0 hits; not Priya, Mara, Okafor or Raman. The owners are constructed; no real filing, owner, address or applicant is named or used (the pull omits owner and address columns).
**Story / framing.** Constructed family, real records. The two option labels are the DOB's own filing checkboxes ("vertical enlargement", "horizontal enlargement"). The family has already fixed the job: **a 400 sq ft addition**. What is open is how to build it.
**Overview ending (not the phone-buzz ending).** Ilse has the filing form open at the page with two checkboxes and the architect's pencil, tapping the paper, hovering between them while Nonna's tape measure retracts in the hallway behind her. Stops before she ticks one. (No numbers in the Overview, per SPEC 1.2.)
**Dilemma (SPEC 1.4).** You are Ilse Marchetti. Do you:
A.) File a **vertical enlargement** (build up: a partial new floor over the existing footprint) OR
B.) File a **horizontal enlargement** (build out: extend into the rear yard)?
**Primary metric (one, stated once).** Median declared job cost per square foot of enlargement ($/sq ft, lower wins) over comparable filings: signed-off Alteration-1 filings on 1-2-3 family buildings, pre-filed 2011 onward, whose stated enlargement is within **plus or minus 50 sq ft of the job size** (here 350-450 sq ft). The band rule is fixed in advance as job size +/- 50 and is applied unchanged at every size in the sensitivity table.
**Margin convention (stated once, applied to every margin below).** Margin = (higher median - lower median) / **lower median** (the winner's value), as a percent. SPEC 2 test: headline must be <= 20%.
**Budget stake.** Savings are a constructed scenario input of **$135,000** [UNVERIFIED, constructed, labeled "Modeling Assumption"], chosen to sit between the two scaled medians so the budget question is live, not a prediction about any real family. The job size (400 sq ft) is the fixed input; scaled cost = $/sq ft x 400.

### Balance computed [DERIVED] from the live API (pulled 2026-10-28)

Headline, 400 sq ft job (350-450 band): **Vertical $311.2/sf (n=57) vs Horizontal $364.2/sf (n=171). Vertical wins by 17.0%.** Scaled to 400 sq ft: vertical $124,485, horizontal $145,682, a gap of about $21,200. Bootstrap 95% intervals on the medians (5,000 resamples, seed fixed): vertical $256-371, horizontal $307-406: **they overlap**; share of resamples in which vertical's median is below horizontal's = **0.88**. So the win is probable, not proven (this is the discussion, not a flaw).
Strongest argument for A (vertical): lower median at the stated size, 17.0%; 59.6% of comparable vertical filings (34 of 57) scale to <= $135,000 versus 47.4% (81 of 171) for horizontal; vertical also wins at every size of 325 sq ft and up in the table below.
Strongest argument for B (horizontal): it is the only option that is cheaper below about 300 sq ft (by 52-125% in the 200-300 sq ft windows), and its cost per sq ft is flat across 300-450 (about $364-$421) while vertical's falls off a cliff at ~300; if the real scope lands below ~300 sq ft (scope cut, setback limits on the rear yard), horizontal protects the family from the $/sf jump (vertical $719 vs horizontal $422 in the 200-300 window). It also has the same dispersion but more evidence behind it (n=171 vs 57).

**Size sensitivity (same rule, +/- 50 window around each stated job size; lower median $/sf wins; margin per convention above):**
| Stated job size (sq ft) | Window | Vertical $/sf (n) | Horizontal $/sf (n) | Winner | Margin |
|---|---|---|---|---|---|
| 250 | 200-300 | 718.8 (66) | 421.5 (194) | Horizontal | 70.5% |
| 275 | 225-325 | 667.3 (62) | 437.1 (183) | Horizontal | 52.7% |
| 300 | 250-350 | 454.5 (70) | 434.4 (178) | Horizontal | 4.6% |
| 325 | 275-375 | 312.7 (68) | 426.1 (177) | Vertical | 36.3% |
| 350 | 300-400 | 304.9 (63) | 373.8 (180) | Vertical | 22.6% |
| 375 | 325-425 | 300.8 (65) | 364.2 (167) | Vertical | 21.1% |
| **400** | **350-450** | **311.2 (57)** | **364.2 (171)** | **Vertical** | **17.0%** |
| 425 | 375-475 | 314.8 (62) | 390.7 (169) | Vertical | 24.1% |
| 450 | 400-500 | 318.7 (67) | 418.5 (167) | Vertical | 31.3% |
| 500 | 450-550 | 318.7 (69) | 397.6 (168) | Vertical | 24.8% |
| 550 | 500-600 | 291.5 (71) | 333.3 (177) | Vertical | 14.4% |

**Break-even size: about 300 sq ft** (horizontal by 4.6% in the 250-350 window, vertical by 36.3% in the 275-375 window; the crossing is a step between 300 and 325, not a smooth line, with n of only 11-22 per option in 25-sq-ft bins, so state it as "roughly 300, plausibly 275-325"). Both options win somewhere; the headline is the only size where the margin is <= 20% by this rule; the 350-475 neighbours are 21-24% (honest: SPEC 2's 20% test is met at the stated job size, and the sheet does not claim it holds at every size; the case is fixed at 400).

**Robustness at 400 sq ft [DERIVED], same band, one change at a time (margin per convention):**
| Variant | Vertical $/sf (n) | Horizontal $/sf (n) | Winner | Margin |
|---|---|---|---|---|
| Base (above) | 311.2 (57) | 364.2 (171) | Vertical | 17.0% |
| Keep $/sf outside 20-2,000 | 314.8 (62) | 371.2 (182) | Vertical | 17.9% |
| Keep duplicate docs of a job | 314.8 (82) | 364.2 (237) | Vertical | 15.7% |
| Queens filings only | 318.4 (31) | 336.6 (98) | Vertical | 5.7% |
| Filed 2011-2015 | 212.8 (32) | 302.7 (104) | Vertical | 42.2% |
| Filed 2016-2020 | 370.6 (25) | 421.6 (67) | Vertical | 13.8% |
| Filed 2008 onward | 288.4 (78) | 304.6 (239) | Vertical | 5.6% |
| Crude year-index adjustment (each filing divided by its filing year's median $/sf, rescaled) | 306.9 (57) | 372.7 (171) | Vertical | 21.4% |
Takeaway: vertical wins at 400 sq ft in every variant, but the margin ranges 5.6% to 42.2%; the verdict is a direction, with an uncertain size.

**The pooled trap (deliverable-forced) [DERIVED].** Pooling all sizes (n = 1,424 vertical, 2,050 horizontal): medians **$203.7 vs $265.8**, vertical "wins" by 30.5%. Vertical filings are bigger (median 931 sq ft vs 669; 78.7% of vertical filings are 600 sq ft or more, vs 55.4% of horizontal; only 7.8% of vertical but 20.2% of horizontal are under 300 sq ft). $/sf falls steeply with size for both options, so the pool largely measures *what size of job each option tends to be filed for*. The pooled "answer" (vertical, by 30.5%) is wrong in direction for the 200-300 sq ft jobs and overstates the gap at 400. This is Simpson-style confounding (size is the lurking variable), and a student who answers from the pool misses it.

### Why Option B's low-size win may be partly a scope artifact (disclose; this is a deliverable)
`initial_cost` is DOB's "Estimated cost of job" for the *whole filing*, but the denominator is only `enlargement_sq_footage`. A small enlargement bundled with a gut renovation shows a huge $/sf. Evidence: the median total declared cost of vertical filings with 100-299 sq ft of enlargement is **$159,190** (n=107), *higher* than the median total for vertical filings with 300-449 sq ft, **$121,255** (n=92) [DERIVED]. A smaller addition costing more in total cannot be a pure construction-cost effect; the likely explanation is that small vertical filings carry extra scope (this is an inference, **[UNVERIFIED]** from the filing text), and the Marchettis' job is an addition only. Students must say whether the "below 300 sq ft, horizontal wins" result applies to a job that is just an addition, which is a modeling assumption they state, not a thing the data settles.

### Data / feasibility: HIGH (all [CONFIRMED] live, with the exceptions flagged)
- **Source:** NYC Open Data, DOB Job Application Filings, dataset `ic3t-wcy2`, `https://data.cityofnewyork.us/resource/ic3t-wcy2.json` (Socrata SODA API, free, no key for these queries). Dataset metadata `rowsUpdatedAt` = 2026-10-27 21:56 UTC; **pull made 2026-10-28 05:01 UTC**. The case freezes all numbers at this pull as its SPEC 5 "as of" date. License: the dataset's license field is empty in the API metadata **[UNVERIFIED]**; NYC Open Data terms of use should be cited at build.
- **Dataset scope [CONFIRMED]:** description states it includes jobs submitted through Borough Offices, eFiling or the HUB with a Latest Action Date since 1 Jan 2000, and **does not include DOB NOW jobs**. Observed: pre-filing years drop from 978 (2020) to 103 (2021) to 36 (2022) in the raw rows, consistent with that scope; that the legacy system stopped taking new filings is the likely cause **[UNVERIFIED]**.
- **Filter (SoQL `$where`):** `job_type='A1' AND building_type='1-2-3 FAMILY' AND job_status_descrp='SIGNED OFF'`, citywide (not just Queens: Queens-only n=31 vertical is too thin, shown as a robustness row). Fields used: `job__`, `doc__`, `borough`, `pre__filing_date`, `initial_cost`, `horizontal_enlrgmt`, `vertical_enlrgmt`, `enlargement_sq_footage`. Owner, applicant, address and filing text fields are not pulled.
- **Cleaning, applied in this order (row counts [DERIVED]):** start 71,003 signed-off A1 1-2-3-family rows; drop 49,527 with not exactly one of the horizontal/vertical flags set (both blank or both "Y"); drop 603 with enlargement outside 50-5,000 sq ft; drop 4 with cost <= 0; drop 15,874 pre-filed before 2011-01-01; drop 1,301 repeat `doc__` records of a job already counted (keep the first by `job__, doc__`); drop 220 with cost per sq ft outside $20-$2,000; **3,474 filings remain (1,424 vertical, 2,050 horizontal)**. Years kept: 2011-2020 (no 2021+ filing survives the other filters).
- **Why 2011+:** the raw rows hold filings since 1989, with costs far lower in earlier years. In the 350-450 band, using all years gives medians of about $86 (vertical) and $110 (horizontal) per sq ft, versus $311 and $364 for 2011+; mixing eras would compare dollars from different decades. 2011 begins after the 2007-2010 downturn (filings fall from 4,566 in 2006 to roughly 2,150 by 2010 and are stable at 2,000-2,600 a year after) and leaves ten years of filings. Using 2008 onward changes the margin to 5.6% (robustness row), so the cutoff is a modeling choice, stated, not a fact.
- **Disclosures to carry into the case (Modeling Assumptions):** (1) declared costs are applicant-stated estimates, **unaudited**; the lowest values ($41-$90/sf) are likely understated; the median is used because it resists these; (2) costs are **not inflation-adjusted**: the 2016-2020 medians are well above 2011-2015 (vertical 370.6 vs 212.8, horizontal 421.6 vs 302.7 at 350-450), so a 2011 filing and a 2020 filing are not in the same dollars; the crude year-index row is a classroom approximation, not CPI; (3) the denominator is the stated enlargement size, whole-job cost; see scope artifact above; (4) filings are citywide and mixed across boroughs and decades; no permit or construction price is a quote for the family's house; (5) "signed off" filings are survivors (abandoned or withdrawn projects are excluded) **[survivorship, UNVERIFIED in size]**; (6) the $135,000 savings figure is constructed.
- **No second source:** Census Building Permits state files carry units only, not valuation **[CONFIRMED in v1]**; no independent cost check was found. Cost-per-sq-ft guides from contractors were not fetched.
- **Weakness:** small vertical bins (n = 57 at the headline); self-declared; the break-even rests on 11-22 filings per 25-sq-ft bin.

### Tier: **T4**
Statistics with inference (overlapping intervals, bootstrap result supplied), confounding, an explicit stated assumption (scope of the job), and a sensitivity table. Numeric load is moderate: medians, percents, compound units, box plots. The bootstrap intervals are computed by the author and **given to students** as an appendix (resampling is not asked of students).

### Deliverables (SPEC 1.5 item 3) and the skills each forces
1. **Five-number summaries and side-by-side box-and-whisker plots of $/sq ft for the 57 vertical and 171 horizontal comparable filings** (Appendix: all 228 values, reproduced in-document so the case survives a dead link; the five-number summary and fences are in Appendix B). Students state which points the 1.5 x IQR rule flags as outliers (7 vertical, 14 horizontal, all high) and whether the box overlap supports the 17.0% "win". *Forces:* box-and-whisker construction, quartiles, outliers, median.
2. **The size-sensitivity chart:** median $/sq ft for each option against stated job size using the table above, with a one-sentence reading of the *shape*. *Forces:* scatter plot, and the term **Non-linear** (the curve for vertical falls steeply near 300 sq ft and is not a straight line).
3. **The pooled-versus-banded table and a paragraph catching the trap:** reproduce the pooled medians (30.5% for vertical), then show why the pool misleads using the share of each option's filings by size. *Forces:* median, percent of a number, compare values; reasoning with a lurking variable.
4. **Budget stake memo:** scale each option to 400 sq ft ($ per sq ft x sq ft), state dollars and the gap, compare to the $135,000 savings, and give the share of comparable filings that scale to within it (34 of 57 vs 81 of 171). *Forces:* compound-unit conversion, percent conversion, a whole-number proportion.
5. **A break-even statement:** at what stated job size does the winner change, in plain words, with the uncertainty on that size.
6. **Two-sentence confession of the weakest assumption** (unaudited, undeflated, whole-job cost over enlargement size), and what they would do before the family signs (e.g., get a contractor quote for the actual scope).

### Spine skills genuinely forced (ids all verified in `readmodel/standards_spine.json`; n = current number of covering cases)
| id | kind | n | Forced by |
|---|---|---|---|
| `statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data` | how-to | **1 (thin)** | Deliverable 1 |
| `statistics-and-probability-non-linear` | term | **2 (thin)** | Deliverable 2 (describing the curve; weaker, see note) |
| `statistics-and-probability-box-and-whisker-plot` | term | 3 | Deliverable 1 |
| `statistics-and-probability-quartiles` | term | 3 | Deliverable 1 |
| `statistics-and-probability-outlier` | term | 5 | Deliverable 1 |
| `statistics-and-probability-median` | term | 8 | primary metric |
| `statistics-and-probability-scatter-plot` | term | 10 | Deliverable 2 |
| `measurement-how-to-convert-an-amount-with-compound-units` | how-to | 21 | Deliverable 4 ($/sq ft x sq ft = $) |
| `advanced-numbers-how-to-find-the-percent-of-a-number` | how-to | 90 | margin / share under budget |
| `number-sense-how-to-compare-two-or-more-values` | how-to | 55 | thick; reinforcement only |

**Thin-skill honesty.** The box-and-whisker how-to (n=1) is cleanly forced: the case cannot be answered well without building the plot from the raw data. "Non-linear" (n=2) is forced only in the loose sense that the student must name the shape and say it is not linear; a student could do deliverable 2 and write "curved" without ever using the term, so the sheet relies on the case-build step to put the term in the challenge wording. Closing 1 skill at n=1 and thickening 1 at n=2 is the real yield; this is a statistics-and-data slot, not a gap-filler on the order of the dropped trig concept. The remaining skills (median, compound units, percent) are reinforcement of already well-covered skills and are listed only because the deliverables require them.

### Facilitator note (SPEC 6)
Family finances and housing for an aging relative are the stake; keep the discussion on the numbers and the decision, not on what families "should" be able to afford. Some students' families rent or live in crowded housing; do not ask students to disclose their own home situation. No real filing, owner, address or applicant is shown; if students browse the dataset themselves, remind them it contains real owners' names and addresses and they should not search for or post identifiable people. The savings figure is invented. Nothing about this case is construction or legal advice; permits, structural limits and zoning are not modeled.

### Fixes applied
| # | Round-1 / v1 finding | Fix in v2 |
|---|---|---|
| 1 | R1c: C1 Overhang Depth is a near-twin of The Tilt Decision; degree-days have no stake. R1a: winner flips at heating weight 0.43 (879 vs 957, 8.9%) | C1 removed; swapped to v1 C2 Up or Out; nothing of C1 retained |
| 2 | v1 stated "filings 2011+" but the v1 counts (10,141 vertical, 10,706 horizontal) match an *undated* pull (this pull finds about 15,900 of the roughly 20,800 in-range flagged filings pre-date 2011), so v1's medians mixed 1989-2020 dollars. The v1 headline "9.7% at 300-450" does not reproduce | Re-pulled and recomputed from the live API with an explicit 2011-01-01 pre-filing cutoff and a logged cleaning chain; new headline 17.0% at 350-450 (19.7% at v1's 300-450 band); old v1 bins are discarded, not patched |
| 3 | v1 had no as-of date, no cleaning log, no duplicate handling | Pull date 2026-10-28, `rowsUpdatedAt` 2026-10-27, step-by-step row counts, `job__` de-dup (1,301 dropped, with a keep-them robustness row) |
| 4 | Brief: one margin convention | Margin = gap / lower (winner's) median, stated once, applied to every figure |
| 5 | Brief: headline margin <= 20% and both options win somewhere | 17.0% at the fixed 400 sq ft job; horizontal wins below ~300 sq ft (4.6% to 70.5%), vertical above; neighbouring sizes 21-31% disclosed rather than hidden |
| 6 | v1 band choice and the 20% test were not tied together (v1 selected a band to display) | Band rule fixed in advance (job size +/- 50) and applied to every row; the other windows are shown; a student can see the headline sits at the smallest margin among 325-500, and the sheet says so |
| 7 | Brief: real budget stake; job size fixed; show size sensitivity | Family savings of $135,000 (constructed, labeled); job fixed at 400 sq ft; scaled-dollar memo and share-under-budget (34/57 vs 81/171); 11-row size sensitivity |
| 8 | v1: pooled medians mislead (Simpson-style) as a note only | Made a deliverable (3) with the size-mix shares and the lurking-variable reasoning |
| 9 | Declared costs unaudited and not inflation-adjusted, undisclosed in v1 | Disclosed; time-split and crude year-index robustness rows; the whole-job-cost-over-enlargement-size artifact (small vertical totals exceed larger ones) added as a discussion item |
| 10 | Brief: thin spine skill | Box-and-whisker how-to (n=1) forced by deliverable 1; Non-linear (n=2) loosely forced; limits stated honestly |
| 11 | Brief: protagonist not Dev Raman, not found in `cases/`, no Priya/Mara/Okafor/Raman | Ilse Marchetti (0 grep hits for each part of the name); ending is the checkbox hover, not the phone buzz |
| 12 | Brief: facilitator note | Added (family finances, no real owner identification) |

### Still open
1. **[UNVERIFIED] Meaning of `enlargement_sq_footage` and `initial_cost` for vertical filings.** The API's column descriptions are the bare labels "Enlargement SQ Footage" and "Estimated cost of job"; whether vertical filings report added floor area or footprint is not documented in what I fetched. The cost cliff near 300 sq ft may be partly a reporting or scope artifact (inference only; sample the `job_description` text on a few dozen filings before build, without publishing owner data).
2. **[UNVERIFIED] Dataset license / terms.** License field empty in the API; cite NYC Open Data terms of use at build.
3. **[UNVERIFIED] Why the legacy dataset stops (2021 onward)** is inferred from the description and the filing-year counts, not from a DOB statement.
4. **[UNVERIFIED] Survivorship** (SIGNED OFF only) and its size.
5. No independent cost source (contractor guides, RSMeans, Census valuation); the $/sf are declared estimates only.
6. The headline 17.0% is sensitive to window choice (14.0% at +/-25, 23.6% at 300-500) and to inflation treatment (21.4% with the crude index); the build step must keep the stated fixed rule and show the table, or re-center the job size.
7. Quartile convention (median of halves, as used in Appendix B) differs from Python's default; the case must state which convention it uses for the box plot.
8. The bootstrap intervals and the 0.88 probability were computed once with seed 5-11 in python; reproduce at build and report as "approximately".
9. The savings figure ($135,000) and 400 sq ft job size are author choices (job size changed from v1's "about 350" so that the headline margin is under 20%; at 350 the same rule gives 22.6%). R1 should confirm this is an acceptable fixed input rather than a tuned one.
10. Tier T4 vs T3: the supplied-bootstrap approach keeps the work at "read an interval" level; R1a to confirm.

---

## Appendix A - Raw $/sq ft values, 350-450 sq ft band, rounded to nearest dollar [DERIVED from the 2026-10-28 pull]
**Vertical (n=57):** 50 53 61 85 86 86 100 119 120 125 164 168 171 174 174 178 180 182 201 225 253 256 267 285 292 296 297 301 311 318 330 333 333 335 369 371 430 442 471 482 483 516 519 545 581 633 681 751 858 980 1088 1099 1100 1180 1439 1724 1922

**Horizontal (n=171):** 41 43 50 52 52 56 59 62 71 74 77 78 79 80 86 90 91 97 98 103 104 104 106 112 113 113 114 138 147 153 158 162 167 172 176 177 180 181 181 183 183 190 195 200 201 205 206 210 212 215 216 217 218 218 219 223 224 235 236 240 246 264 266 275 276 281 283 289 296 297 298 305 307 307 311 319 320 321 328 331 336 343 351 354 356 364 366 371 371 375 377 384 386 386 391 397 400 400 406 408 416 421 421 422 425 429 432 432 438 441 444 446 449 475 480 481 488 488 490 498 514 524 528 565 567 586 586 587 595 596 613 618 628 632 637 649 683 683 706 709 784 804 807 819 847 863 894 900 992 993 999 1052 1124 1144 1156 1157 1165 1207 1217 1250 1256 1304 1408 1431 1476 1515 1641 1714 1773 1870 1907

(Medians of the rounded values: 311 and 364. The headline 311.2 / 364.2 are from unrounded values.)

## Appendix B - Five-number summaries (median-of-halves quartiles), same band
| | Min | Q1 | Median | Q3 | Max | IQR | Upper fence (Q3 + 1.5 IQR) | Flagged high outliers |
|---|---|---|---|---|---|---|---|---|
| Vertical (57) | 50 | 174 | 311 | 532 | 1,922 | 358 | 1,069 | 7 (1,088 to 1,922) |
| Horizontal (171) | 41 | 195 | 364 | 595 | 1,907 | 400 | 1,195 | 14 (1,207 to 1,907) |
The boxes overlap heavily (vertical 174-532, horizontal 195-595), which is the visual form of the overlapping bootstrap intervals.

## Appendix C - Hand-off to R1 (reproduction)
Pull: `GET https://data.cityofnewyork.us/resource/ic3t-wcy2.json` with `$select=job__,doc__,borough,pre__filing_date,signoff_date,job_status_descrp,initial_cost,horizontal_enlrgmt,vertical_enlrgmt,enlargement_sq_footage,proposed_no_of_stories,existingno_of_stories,building_type,job_type`, `$where=job_type='A1' AND building_type='1-2-3 FAMILY' AND job_status_descrp='SIGNED OFF'`, `$order=job__,doc__`, paged at 50,000 (two pages, 71,003 rows). Costs parsed from strings like `$297160.00`; $/sf = cost / enlargement_sq_footage. Scripts and raw/clean JSON are in the session scratchpad (`pull.py`, `an.py`-`an4.py`, `raw.json`, `clean.json`), not in the repo.
