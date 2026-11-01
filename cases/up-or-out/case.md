Case Study: Up or Out
MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

The pencil is tapping the paper, and it has been tapping for a while. Tomas Quartey, the family's architect, sits at the dining table with a roll of tracing paper under one elbow and a form open to the page that matters. Two boxes sit side by side on it. One says *vertical*. The other says *horizontal*.

Ilse Marchetti never planned to be the person who reads the forms. She is a first-year community-college student, but she reads English paperwork fastest in the family, so the folder is hers. Behind her, in the hallway, Nonna is measuring the wall by the staircase again, the metal tape zipping out and snapping back, out and back. Every morning Nonna takes the stairs one at a time with both hands on the rail, and every morning nobody says anything about it.

"I can't draw a line until you pick," Mr. Quartey says, not unkindly. "The survey isn't back. I can tell you the new space will come in somewhere on the small side or the big side, and I can't tell you which."

The kitchen smells of coffee and the radiator that has been ticking since October. Ilse looks at the two boxes, and then at the pencil, which has stopped. She lifts her pen over one of them and holds it there, and out in the hallway the tape measure snaps shut.

---

## Background

Ilse Marchetti is a first-year community-college student who handles the paperwork for her grandparents' two-family house in Woodhaven, Queens. Her grandparents have set aside $150,000 [MA1] so that her grandmother, Nonna, can live on one level with a bedroom and a bathroom she can reach without stairs. The family's architect, Tomas Quartey, has proposed two ways to add the space, and the filing needs to name one before he can draw.

**The Tall Plan** adds a partial new floor on top of the existing house, a *vertical enlargement*; the upstairs household moves into the new rooms and Nonna takes the old ground-floor rooms. **The Wide Plan** extends the house into the rear yard, a *horizontal enlargement*, and Nonna moves into the new ground-level rooms. In the city's zoning law, an enlargement is an addition to the floor area of an existing building [S4]. Either plan is an addition only: the new rooms and their connection to the house, with no other renovation [MA5].

The survey is not back, so the size of the addition is not fixed. Mr. Quartey says it will land somewhere from 250 to 450 square feet [MA2], depending on the rear-yard measurements and where the stairs fit. This case treats the nine sizes in that range, 25 square feet apart, as equally likely, for both plans [MA3].

To compare the plans, Ilse uses the city's own records: signed-off Alteration Type 1 jobs on one-, two- and three-family buildings in the Department of Buildings' job-filing database, each with a declared cost and the size of its enlargement (SEE APPENDIX A) [S1][S2]. For each possible size, the comparable filings are those whose enlargement is within 50 square feet of that size [MA4]. A plan's cost at a size is the median cost per square foot of its comparable filings times that size (SEE APPENDIX B). The case's primary metric is a plan's average cost over the nine sizes; the lower average wins.

Raw values for two of the size windows are in Appendix C, and the same records pooled over all sizes are in Appendix D. Appendix E shows what the declared costs do and do not include. Appendix F lists the stated assumptions, Appendix G every source, and Appendix H the "how to…" questions you will research.

---

## Dilemma

You are Ilse Marchetti.

Do you:

**A.)** File **The Tall Plan** — a vertical enlargement, a partial new floor over the existing house **OR**

**B.)** File **The Wide Plan** — a horizontal enlargement, an extension into the rear yard

---

## Challenges

Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:

- **D1 — Box plots at both ends of the range.** Using the raw values in Appendix C, build side-by-side box-and-whisker plots of cost per square foot for the Tall Plan and the Wide Plan in the 250 sq ft window and again in the 450 sq ft window (four boxes). Show each five-number summary, find the outliers with the 1.5 x IQR rule, and say in one sentence per window whether the two boxes overlap and what that does to your confidence in the two medians.
- **D2 — The size curve.** Plot the median cost per square foot against job size for both plans on one set of axes using Appendix B. Find each plan's slope across the 250-300 sq ft stretch and across the 350-450 sq ft stretch, say whether each plan's curve is linear or non-linear and why, and estimate the job size at which the cheaper plan changes by straight-line interpolation between the two sizes where it does.
- **D3 — All sizes pooled.** Using Appendix D, find the gap between the two plans' all-sizes medians as a percent of the lower one. Then use the size mix in Appendix D to explain why that gap does not answer the family's question, and compare it with the gaps you can read from Appendix B.
- **D4 — The cost memo.** For each plan, find the cost at each of the nine sizes (median cost per square foot times square feet), the average cost over the nine sizes, and the gap between the averages in dollars and as a percent of the lower average. List the sizes at which each plan would cost more than the family's savings.
- **D5 — The decision under an unknown size.** For each plan, find its largest regret: the most, over the nine sizes, by which it costs more than the other plan at the same size. Then, in at most two sentences, name the one fact in Appendix E you would want checked before the family signs, and say which plan that fact favors.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

## Appendix A — The Filing Records and the Comparable-Filings Rule

Referenced in Background and Challenge 3 (D5). The records are the New York City Department of Buildings' *DOB Job Application Filings* dataset on NYC Open Data, pulled live on 2026-10-28 through the dataset's public API [S1]. The portal shows the data last updated 2026-10-27. The dataset's own description says it covers jobs filed through Borough Offices, eFiling or the HUB with a latest action date since 2000, and does not include jobs filed through the newer DOB NOW system [S1].

What the two fields mean, in the dataset's data dictionary [S2]: *Initial Cost* is the "Estimated Job Cost on the PW1" (the applicant's own estimate on the filing form); *Enlargement SQ Footage* is "the Additional Square Footage added by the construction enlargement, if any." A job type of A1 is an Alteration Type I, "a major alteration that will change the use, egress, or occupancy of the building."

**The comparable-filings rule (fixed in advance, applied unchanged at every size).** A filing counts if it is an A1 job on a "1-2-3 FAMILY" building, with status "SIGNED OFF", flagged as exactly one of vertical or horizontal enlargement, and pre-filed on or after 2011-01-01. For a stated job size S, the comparable filings for a plan are those of that plan whose enlargement is from S - 50 to S + 50 square feet, inclusive. Cost per square foot is declared cost divided by enlargement size.

**How the records were cleaned, in this order (rows remaining).**

| Step | Rows left |
|---|---|
| Signed-off A1 jobs on 1-2-3 family buildings | 71,003 |
| Exactly one of the vertical or horizontal flags set | 21,476 |
| Enlargement between 50 and 5,000 sq ft | 20,873 |
| Declared cost above $0 | 20,869 |
| Pre-filed 2011-01-01 or later | 4,995 |
| Only the first document of each job number kept | 3,694 |
| Cost per sq ft between $20 and $2,000 | 3,474 (1,424 vertical, 2,050 horizontal) |

No filing in the final set was pre-filed after 2020. Owner, applicant and address fields were not used.

**Cautions that apply to every number in this case.** Declared costs are estimates written on a form, not audited bills, and not adjusted for inflation: filings from 2011 and 2020 are in different dollars. "Signed off" filings are the ones that finished; abandoned projects are not in the records. A filing's declared cost covers the whole filing, but the size is only the enlargement. The records are citywide, not Woodhaven. No filing, owner or address is named in this case.

**Terms of use.** New York City's Administrative Code §23-502(d) says public data sets are to be made available "without any registration requirement, license requirement or restrictions on their use," while allowing the city to require users "to explicitly identify the source and version of the public data set, and a description of any modifications made" [S3]. The dataset's own metadata carries no license field. Source: NYC Open Data, Department of Buildings, *DOB Job Application Filings* (ic3t-wcy2), pulled 2026-10-28; this case modifies it by the cleaning steps above.

---

## Appendix B — Median Cost per Square Foot by Job Size

Referenced in Background and Challenge 3 (D2, D3, D4, D5). For each stated job size, the median declared cost per square foot of the comparable filings of each plan, with the number of filings in parentheses [S6]. The Tall Plan is vertical; the Wide Plan is horizontal.

| Job size (sq ft) | Window (sq ft) | Tall Plan: median $/sq ft (n) | Wide Plan: median $/sq ft (n) |
|---|---|---|---|
| 250 | 200-300 | $718.8 (66) | $421.5 (194) |
| 275 | 225-325 | $667.3 (62) | $437.1 (183) |
| 300 | 250-350 | $454.5 (70) | $434.4 (178) |
| 325 | 275-375 | $312.7 (68) | $426.1 (177) |
| 350 | 300-400 | $304.9 (63) | $373.8 (180) |
| 375 | 325-425 | $300.8 (65) | $364.2 (167) |
| 400 | 350-450 | $311.2 (57) | $364.2 (171) |
| 425 | 375-475 | $314.8 (62) | $390.7 (169) |
| 450 | 400-500 | $318.7 (67) | $418.5 (167) |

The windows overlap, so neighboring rows share many filings.

---

## Appendix C — Raw Cost per Square Foot, Two Windows

Referenced in Background and Challenge 3 (D1). Every comparable filing's declared cost per square foot, rounded to the nearest dollar, sorted from least to greatest [S8]. Use the **median-of-halves** convention for quartiles: the median splits the sorted list into a lower half and an upper half (leave the median itself out of both halves when n is odd), and Q1 and Q3 are the medians of those halves. An outlier is a value more than 1.5 x IQR above Q3 or below Q1.

**250 sq ft window (filings of 200-300 sq ft), Tall Plan, n = 66:**
58 77 100 104 116 118 122 135 145 171 228 251 253 260 262 265 277 290 337 375 398 409 472 510 513 522 634 637 650 653 667 676 697 741 768 838 897 900 905 916 976 1000 1004 1037 1055 1109 1136 1146 1190 1250 1289 1296 1309 1411 1414 1470 1486 1491 1498 1515 1546 1555 1577 1586 1687 1935

**250 sq ft window, Wide Plan, n = 194:**
24 32 48 50 52 57 71 75 75 84 91 91 92 92 95 98 99 100 100 100 101 103 105 106 109 114 115 115 123 125 126 131 132 134 137 138 149 150 150 168 183 184 187 188 188 190 194 194 200 200 204 206 208 218 220 220 221 228 234 235 236 236 242 252 253 255 264 274 278 279 279 282 292 300 312 314 319 337 339 346 347 359 362 370 372 375 377 386 392 398 399 401 403 406 415 419 421 422 422 437 438 443 449 450 473 492 509 515 530 541 543 543 554 557 558 569 574 579 585 606 612 616 618 625 642 650 651 659 667 687 700 706 707 712 719 738 741 741 749 759 771 779 782 805 839 857 895 903 925 927 937 941 946 1008 1030 1038 1050 1077 1079 1098 1116 1117 1119 1127 1130 1131 1162 1179 1182 1185 1228 1232 1243 1263 1272 1287 1311 1332 1377 1412 1413 1425 1449 1483 1488 1504 1511 1527 1552 1569 1691 1805 1824 1911

**450 sq ft window (filings of 400-500 sq ft), Tall Plan, n = 67:**
27 27 50 61 71 76 86 99 100 119 120 144 150 163 164 168 170 178 190 201 202 218 231 239 248 256 275 285 286 292 296 311 318 319 325 330 333 335 364 369 397 414 419 430 457 461 516 519 523 535 548 581 633 651 681 802 858 980 1014 1051 1088 1100 1159 1180 1247 1303 1534

**450 sq ft window, Wide Plan, n = 167:**
59 62 71 74 76 78 79 86 90 100 103 104 112 113 134 162 167 172 173 176 177 180 181 181 183 185 186 190 196 200 205 205 208 210 215 216 217 218 219 221 224 226 228 235 236 241 246 247 250 266 266 268 276 284 289 289 290 292 296 319 319 320 321 321 327 328 337 354 354 361 366 371 375 377 386 391 391 392 394 397 402 406 408 419 420 421 422 423 425 431 436 438 441 444 444 449 453 456 466 467 480 481 488 488 494 498 501 504 505 518 521 525 525 533 539 541 548 560 570 585 586 586 587 587 595 600 610 611 613 618 628 640 649 683 685 709 763 773 778 784 804 817 849 863 883 900 993 1016 1025 1086 1144 1156 1157 1157 1162 1165 1239 1250 1256 1387 1408 1420 1444 1467 1515 1680 1773

---

## Appendix D — All Sizes Pooled

Referenced in Background and Challenge 3 (D3). The same cleaned records [S7], with every size mixed together.

| | Tall Plan (vertical) | Wide Plan (horizontal) |
|---|---|---|
| Filings | 1,424 | 2,050 |
| Median cost per square foot, all sizes | $203.7 | $265.8 |
| Median enlargement size (sq ft) | 931 | 669 |
| Share under 300 sq ft | 7.8% (111 filings) | 20.2% (414 filings) |
| Share 300-599 sq ft | 13.6% (193 filings) | 24.4% (501 filings) |
| Share 600 sq ft or more | 78.7% (1,120 filings) | 55.4% (1,135 filings) |

---

## Appendix E — What the Declared Costs Do and Do Not Include

Referenced in Background and Challenge 3 (D5). A filing's declared cost is for the whole filing, but the size in these records is only the enlargement [S2]. A small enlargement filed together with other work shows a high cost per square foot. Two summaries of the same records [S9]:

| Tall Plan (vertical) filings | Enlargement under 300 sq ft | Enlargement 300-449 sq ft |
|---|---|---|
| Median total declared cost | $159,190 (107 filings) | $121,255 (92 filings) |

| Wide Plan (horizontal) filings | Enlargement under 300 sq ft | Enlargement 300-449 sq ft |
|---|---|---|
| Median total declared cost | $90,125 (358 filings) | $140,598 (252 filings) |

Among Tall Plan filings, the share that report more stories after the work than before is 28% (18 of 65) for enlargements of 200-299 sq ft, 60% (21 of 35) for 300-349 sq ft, and 58% (33 of 57) for 350-450 sq ft [S9]. These records do not say what other work, if any, a filing included.

---

## Appendix F — Modeling Assumptions

Referenced in Background and Challenge 3 (D4, D5). This case is built so that you must decide what Appendix E means for the Marchettis' job, state it, and defend it. It is not given.

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case author. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | The family's savings | $150,000 | A round sum of the same order as the declared costs of the filings in Appendix B; no public source applies to a made-up family. | The answer to D4's list of sizes depends on this value. |
| MA2 | The architect's range for the addition | 250 to 450 sq ft, in steps of 25 | A bedroom, an accessible bathroom and a hall fit at the low end; a larger room and a stair landing fit at the high end. No public source gives the size of a particular addition before its survey. | The answer to the dilemma is sensitive to this range. |
| MA3 | How likely each size is | All nine sizes equally likely, the same for both plans | The architect cannot rank the sizes, and the plan chosen does not change what the survey finds. | The answer is sensitive to this assumption. |
| MA4 | The comparable-filings rule | Window of 50 sq ft either side of each size; filings pre-filed from 2011 | A fixed window, chosen before looking at results, wide enough to hold dozens of filings at every size; 2011 is after the 2007-2010 downturn in filings and leaves ten years of records. | The answer is sensitive to the window and the start year. |
| MA5 | Declared cost stands in for the family's cost | The family's job is an addition only, and a filing's declared cost is a fair stand-in for what it would cost | Declared costs are the only public cost records by plan and size; they are estimates, not quotes. | The answer is sensitive to this assumption. |

---

## Appendix G — Sources

Referenced in Background. Every figure in this case is either sourced here or declared as a stated assumption in Appendix F.

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Job-filing records: type, status, declared cost, enlargement flags and size | 71,003 signed-off A1 jobs on 1-2-3 family buildings before cleaning | NYC Open Data, Department of Buildings (DOB) — DOB Job Application Filings, dataset ic3t-wcy2 ([link](https://data.cityofnewyork.us/Housing-Development/DOB-Job-Application-Filings/ic3t-wcy2)) | pulled 2026-10-28; rows updated 2026-10-27 | MEDIUM |
| S2 | Meaning of Initial Cost, Enlargement SQ Footage and job type A1 | data dictionary wording quoted in Appendix A | NYC DOB — DOB Job Application Filings data dictionary, attached to dataset ic3t-wcy2 ([link](https://data.cityofnewyork.us/api/views/ic3t-wcy2/files/9bb3688e-1bf8-4f8f-9541-ce936f1d00f4?download=true&filename=DD_DOB%20Job%20Application%20Filings_2019-06-19.xlsx)) | file dated 2019-06-19 | HIGH |
| S3 | Public data sets are to be available without license requirements or restrictions on use, with source and version identified | quoted in Appendix A | New York City Administrative Code §23-502(d) (Local Law 11 of 2012), as reproduced at NYC Laws ([link](https://nyc-laws.readthedocs.io/en/latest/nycadmincode/t23/c05/)) | read 2026-10-28 | MEDIUM |
| S4 | Definition of "enlargement" | an addition to the floor area of an existing building | NYC Department of City Planning — Zoning Resolution, Article I, Chapter 2, Section 12-10 definitions, last amended 2/2/2011 ([link](https://zr.planning.nyc.gov/article-i/chapter-2)) | last amended 2011-02-02 | HIGH |
| S6 | Median cost per square foot by job size, each plan (Appendix B) | 18 medians, 2 per size | Computed from S1 by the comparable-filings rule ([link](https://data.cityofnewyork.us/resource/ic3t-wcy2.json)) | pulled 2026-10-28 | MEDIUM |
| S7 | All-sizes medians and size mix (Appendix D) | $203.7 and $265.8 per sq ft; shares in Appendix D | Computed from S1 after cleaning ([link](https://data.cityofnewyork.us/resource/ic3t-wcy2.json)) | pulled 2026-10-28 | MEDIUM |
| S8 | Raw cost-per-square-foot values for the four windows (Appendix C) | 494 values | Computed from S1 after cleaning ([link](https://data.cityofnewyork.us/resource/ic3t-wcy2.json)) | pulled 2026-10-28 | MEDIUM |
| S9 | Total declared costs and story counts (Appendix E) | medians and shares in Appendix E | Computed from S1 (fields initial_cost, enlargement_sq_footage, existingno_of_stories, proposed_no_of_stories) after cleaning ([link](https://data.cityofnewyork.us/resource/ic3t-wcy2.json)) | pulled 2026-10-28 | MEDIUM |

The Marchettis, Mr. Quartey and the family's savings are fictional; no real filing, owner, applicant or address appears in this case. The records are as of the 2026-10-28 pull, and every number computed from them is frozen at that pull; the live dataset keeps being updated and older versions are not kept, so a later pull will not reproduce these figures exactly. Declared costs are applicant estimates, which is why the dataset is graded MEDIUM. Nothing in this case is construction, permit or legal advice: zoning limits, structural limits and permits are not modeled.

---

## Appendix H — "How To…" Math Questions To Research

Referenced in Challenge 1. The questions below are the skills this case asks you to use.

**Vocabulary terms**

- Box And Whisker Plot
- Quartiles
- Outlier
- Median
- Scatter Plot
- Slope
- Linear
- Non-linear
- Mean

**"How to…" questions**

- How to create a box and whisker plot given a set of data
- How to create a scatter plot given a set of data
- How to find the mean of a set of data
- How to convert an amount with compound units
- How to convert numbers to percents
- How to compare two or more values
