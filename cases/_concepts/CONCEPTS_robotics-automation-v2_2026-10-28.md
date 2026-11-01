# Concept sheet v2 — Robotics & Automation (`robotics-automation`), single concept: C2 "Technician Track"

**Chosen: C2 (renamed working title "Technician Track").** C3 "Three of Six" was developed and tested first and rejected (section "C3 test"). C1 stays dropped. **R1c's warning stands and is not fully solved:** C2 is a two-path earnings comparison and so resembles `the-two-offers`. Mitigation is in the design (a second dimension, job-placement odds, beside the horizon; a wage-scarcity counterweight from real employment data; see "Why this is not the-two-offers" below). R1c should judge whether that is enough.

**Margin convention (stated once, applied everywhere): margin = (winner's value minus loser's value) / winner's value.** Primary metric value at the stated horizon, unless a row says otherwise.

---

## Sources: what was actually fetched (2026-10-28) and what was not

| Item | Result | Value used |
|---|---|---|
| BLS Occupational Outlook Handbook, Welders, Cutters, Solderers, and Brazers (`bls.gov/ooh/production/welders-cutters-solderers-and-brazers.htm`), fetched with WebFetch | HTTP OK | **Median pay $53,750/yr, $25.84/h, May 2025; 437,700 jobs (2025)**. Check: 25.84 x 2,080 = 53,747, consistent. |
| O*NET OnLine 17-3024.00 Electro-Mechanical and Mechatronics Technologists and Technicians (`onetonline.org/link/summary/17-3024.00`), fetched with WebFetch; O*NET republishes BLS data | HTTP OK | **Median wage $73,900/yr, $35.53/h (2025 wage data); 15,700 employed (2025); Job Zone 3 (vocational training or associate degree)**. |
| NCES Fast Facts "Tuition costs of colleges and universities" (`nces.ed.gov/fastfacts/display.asp?id=76`), fetched with WebFetch | HTTP OK | **Average published tuition and required fees, public 2-year institutions, 2022-23: $4,000, constant 2022-23 dollars** (NCES footnote: lower of in-district or in-state rate). Not inflated to 2026. |
| BLS OOH Hand Laborers; Assemblers and Fabricators; Metal and Plastic Machine Workers (WebFetch, OK) | HTTP OK | Medians $38,220; $45,450; $47,700 (CNC tool operators $50,690), May 2025. Used only in the rejected C3 test. |
| Universal Robots UR5e datasheet PDF (`universal-robots.com/media/1807465/ur5e_e-series_datasheets_web.pdf`), downloaded and text-extracted with `pdftotext` | OK | **Datasheet states "Updated December 2024", Copyright 2024; payload 5 kg, reach 850 mm, maximum power 570 W, repeatability +/-0.03 mm.** Used only in the rejected C3 test. (The "average power" row did not extract; the earlier sheet's 200 W is not re-verified.) |
| BLS Public Data API v1 | **FAILED today**: "daily threshold ... has been reached" | Nothing. |
| BLS OEWS national tables ZIP (`bls.gov/oes/special-requests/oesm25nat.zip`) | **FAILED**: "Access Denied" page | Nothing. |
| BLS OOH Industrial Machinery Mechanics; OOH Electrical and Electronics Engineering Technologists and Technicians; BLS OEWS occupation pages (`oes514121`, `oes537062`) | **403 or index page only** | Nothing. |
| **Mean** wages $56,760 (welders) and $76,420 (technicians) from the v1 sheet | **NOT re-fetched; UNVERIFIED today.** Dropped. This v2 uses **medians** (above), which were fetched. All R1a figures built on the means are superseded. | |

Note on method: WebFetch returns a summary produced by a small model, not a raw table. Each value above should be spot-checked by a human on the cited page before publication (listed under "Still open").

---

## C2 — The Technician Track · tier T3

### Protagonist
**Delphine Aldercott**, 18, high-school senior in a mid-sized manufacturing town. Constructed (no real person); disclose as constructed. Name grepped against `cases/` and `readmodel/`: 0 hits for "Delphine" and "Aldercott" (checked 2026-10-28).

### Story (beats, not final prose)
Delphine has spent summers sweeping the floor and learning to tack-weld at her uncle's fabrication shop. The shop has offered her a full-time welder's job starting the week after graduation. The same week she was admitted to the community college's two-year mechatronics associate program, whose graduates install and keep running the robot weld cells that the region's plants are buying. Her uncle says the cells are the future and also says the cells are why he is training fewer welders. Her mother, who is paying attention to the family budget, points out the program means two years with no paycheck. Overview ends at the kitchen table at the signing instant: the shop's offer letter in one hand, the enrollment form in the other, the pen above the line on whichever sheet she picks up first. (Ending is deliberately not the "buzzing phone" ending used by The Tilt Decision and The Overlap Call.)

### Dilemma
You are Delphine Aldercott. Do you:
**A.)** Take the welding job now and start earning at the median welder's wage, OR
**B.)** Enroll in the two-year mechatronics program, earn nothing for two years, then work as a robotics-cell technician at the median technician wage.

### Primary metric
**Cumulative pre-tax earnings, net of programme costs, N years after high-school graduation.** Stated horizon for the case: **N = 10** (age 28), a Modeling Assumption the student may move but must defend. Margin per the convention above.

### Model (recomputed by me in Python, medians fetched today)
- A(N) = 53,750 N
- B(N) = 73,900 (N - 2) - 2 x 6,000 = 73,900 N - 159,800, for N >= 2
- Programme cost per year: **$6,000 = $4,000 tuition and fees (NCES, 2022-23 $) + $2,000 books, tools, transport (Modeling Assumption, UNVERIFIED)**.
- **Break-even N\* = 159,800 / (73,900 - 53,750) = 159,800 / 20,150 = 7.93 years.**

| N (years) | A welder | B technician | Winner | Margin (gap/winner) |
|---|---|---|---|---|
| 5 | $268,750 | $209,700 | A | 22.0% (outside the 20% test; not the stated horizon) |
| 6 | $322,500 | $283,600 | A | 12.1% |
| 7 | $376,250 | $357,500 | A | 5.0% |
| 8 | $430,000 | $431,400 | B | 0.3% |
| 9 | $483,750 | $505,300 | B | 4.3% |
| **10 (stated)** | **$537,500** | **$579,200** | **B** | **7.2%** |
| 12 | $645,000 | $727,000 | B | 11.3% |

Both options win somewhere: A for horizons under 7.93 years, B after. Stated-horizon margin **7.2% (<= 20%)**. Sensitivity of the 10-year margin to programme cost per year: $4,000 -> 7.8%; $8,000 -> 6.6%; $10,000 -> 5.9% (B stays ahead; cost is not the pivot, horizon is).

**Second dimension (placement odds).** If only a fraction q of graduates land the technician wage and the rest earn the welder wage for the same years (fallback = Modeling Assumption), B(10) = 8 x [q x 73,900 + (1 - q) x 53,750] - 12,000. B beats A at N = 10 only if **q > 0.741** (q = 0.8: B ahead 1.7%; q = 0.7: A ahead 1.2%; q = 0.5: A ahead 7.2%). So the student must argue two beliefs: how long will she stay in the trade, and how likely is she to land the job.

**Real-data counterweight (scarcity).** 437,700 welder jobs vs 15,700 electro-mechanical and mechatronics technician jobs (2025): ratio 27.9 : 1, and O*NET lists 1,400 projected job openings for the technician occupation over 2025-35. This is the honest reason a careful student can pick A even past the break-even. Wage premium of B over A: 73,900 / 53,750 - 1 = 37.5%.

### Why this is not the-two-offers (R1c)
Honest answer: same family (earnings stream with an upfront gap). Differences: (1) the metric pivots on two independent beliefs (horizon and placement odds), so students must defend a joint position, not read a crossover; (2) the key beliefs are testable against real employment counts, not only against taste; (3) the domain object is the automation labour market (the technicians who keep robots running), which the corpus lacks. If R1c still calls it a repeat, the fallback is to re-open C3 with a different people-stake design (see "Still open"); I do not have a better third candidate with real inputs.

### Deliverables (what forces the math)
1. Write the earnings function for each path as a linear equation from the data (A: slope 53,750; B: slope 73,900 after a two-year delay with a negative starting intercept).
2. A table of cumulative net earnings for N = 4 through 12 and **one original graph of both lines**, break-even marked.
3. Solve the system A(N) = B(N) and give the break-even in years and months; state which side of it the stated horizon falls on.
4. Percent calculations: B's wage premium over A, and the margin (gap/winner) at N = 10.
5. Placement test: compute the smallest q at which B still beats A at N = 10 and say whether it is believable given the 27.9 : 1 employment ratio.
6. A recommendation (250+ words) that names the horizon and the placement odds Delphine is betting on.

### Spine skills (ids verified present in `readmodel/standards_spine.json`)
- `statistics-and-probability-how-to-solve-a-system-of-linear-equations` (n=6): deliverable 3.
- `statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data` (n=11): deliverable 1.
- `statistics-and-probability-how-to-identify-the-slope-of-a-line-given-a-set-of-data-or-a-graph-o` (n=7): deliverables 1 and 2 (slope = annual earnings; break-even is where the steeper line catches up).
- `advanced-numbers-how-to-find-the-percent-of-a-number` (n=90): deliverable 4.
Four ids claimed, each tied to a numbered deliverable. No skill is at n=0 here; thinnest is n=6. The robotics link is occupational, not geometric; say so plainly.

### Tier
**T3**, with one T4-style assumption (horizon, placement fallback) the student must justify. Not T4 overall.

### Data feasibility
Wage medians, job counts and tuition are fetched primary-source values (grade HIGH, with the WebFetch-summary caveat). Programme extras ($2,000/yr), the horizon, the 100% placement baseline, the flat wages (no raises) and "no earnings while in school" are Modeling Assumptions, disclosed as such. As-of: BLS wages May 2025 (accessed 2026-10-28); employment 2025; NCES 2022-23 dollars.

### Facilitator note (SPEC 6)
Touches family finances and the cost of college; some students will be from families for whom two years without a paycheck is not a real option. Discuss both paths as dignified, do not rank "college" over "trades", and note that loans, aid, tax and part-time work during the programme are deliberately excluded from the model.

### Fixes applied
| Review point | Fix |
|---|---|
| R1a: C1 dominated (salaried or premium hire) | C1 dropped. C2 A/B are two fixed linear streams; balance comes from the real wage gap and the 2-year gap, no pro-rata term. |
| R1a recomputed C2 numbers (454,080 / 442,520; break-even 8.59 y) | Superseded: those used v1 mean wages and $8,000/yr that were not re-verified. Recomputed with fetched medians and $6,000/yr: break-even 7.93 y; 10-year margin 7.2%. |
| R1b: wages unverified | BLS API and OEWS ZIP failed today. Switched to OOH and O*NET pages that were fetched; medians cited with page, year and value. Means dropped. |
| R1b: do not say "fetched" for unfetched items | Table above separates fetched from failed and not-fetched. |
| R1c: same shape as breakeven-mile / weekly-rate | C1 dropped; C2 is not a fixed-vs-per-unit cost. |
| R1c: resembles the-two-offers | Partially mitigated (second dimension, scarcity data); flagged for R1c's judgment. |
| Cross-cutting: one margin convention | Gap/winner, stated at top and used in every row. |
| Cross-cutting: protagonist name | Delphine Aldercott; zero hits in `cases/` and `readmodel/`. |
| Cross-cutting: ending | Kitchen-table pen-above-the-line, not the buzzing phone. |
| Cross-cutting: facilitator note, as-of dates | Added. |

### Still open
- **UNVERIFIED:** $2,000/yr books/tools/transport; horizon N = 10; fallback wage when placement fails (welder median); 100% placement baseline; flat wages; the specific mechatronics program and its real tuition (NCES figure is a national public 2-year average in 2022-23 dollars, not inflated).
- Medians were obtained through WebFetch summaries; spot-check on bls.gov/ooh and onetonline.org before publication. O*NET employment (15,700) vs BLS-OEWS May 2025 employment for 17-3024 not cross-checked against the OEWS table (blocked today).
- Mean-wage figures from the v1 sheet ($56,760, $76,420) and the v1 UR5e "200 W average" are unverified and unused.
- R1c's overlap judgment with `the-two-offers` (read of that case's actual numbers/shape was not re-done here).
- Tuition is 2022-23 dollars; a current-year figure would be better.

---

## C3 test: "Three of Six" (developed, tested, rejected)

**Redesign tried.** Plant manager (name not chosen) must pick 3 of 6 stations to automate under a **no-layoff pledge**: displaced operators are redeployed to a backlog, which only has room for R full-time equivalents. Cash saving counts only the redeployable hours (highest-wage hours first); excess displaced hours are stranded. Net = redeployed wage value (BLS median x 1.30 load / 2,080 h) minus annual robot cost, with a 25% human tending share. All **C(6,3) = 20** packages brute-forced in Python.

**Inputs by provenance.** Real: four wage medians (welders $53,750; hand laborers $38,220; assemblers and fabricators $45,450; CNC tool operators $50,690; all May 2025, fetched today), UR5e payload 5 kg / reach 850 mm / 570 W max (datasheet "Updated December 2024"). **Invented: six station hour counts, six robot annual costs, the 25% tending share, the 1.30 load, the backlog capacity R.** 5 real inputs against about 16 invented ones.

**Balance result (best of a search over invented hours/costs; one tuned set reported).** Stations (hours, annual robot cost): W1 900/$20k, W2 1,500/$22k, P1 1,000/$32k, P2 1,800/$20k, F1 1,200/$22k, A1 1,500/$34k. At R = 2.0 FTE:

| Rank | Package | Net $/yr | Displaced FTE |
|---|---|---|---|
| 1 | W2,P2,F1 | 34,554 | 1.62 |
| 2 | W1,W2,P2 | 30,717 | 1.51 |
| 3 | W2,P2,A1 | 25,998 | 1.73 |
| 4 | W1,W2,F1 | 24,982 | 1.30 |
| ... | (16 more) | down to -13,452 | |

Gap/winner top two = 3,837 / 34,554 = **11.1%**. Nothing dominates the top two (third place is 24.8% below the winner). But:
- Winner flips to W1,W2,P2 only when R falls below about 1.5 to 1.6 FTE (R = 1.5: 30,000 vs 28,463, margin 5.1%), and to a third package (W1,W2,F1) below about 1.3 to 1.4. B's winning window is roughly 0.2 FTE wide; above R = 1.62 the answer is a flat plateau (11.1% for every R from 1.7 to 3.0).
- Under the first-draft model (additive, no cap) the "winner" is just the top three stations by net saving, a sort, not a dilemma.

**Why rejected.** (1) Inputs "rest almost entirely on invention": the balance was obtained by tuning invented hours and costs until two packages sat within 11%; a different invented set gives a different dilemma (a random search over invented hours and costs, with the same flip and gap tests, turned up four balanced sets quickly and was stopped at four, so balance here is a product of the invented values, not of any real station). (2) B wins only in a narrow window of an invented parameter. (3) The "people stake" lives entirely in R, also invented. Under SPEC section 5 ("never fabricate; plausible is not true") this fails the evidence test. A version with real station data (e.g. a plant's actual cycle times and quotes) could revive it, but none is available from free primary sources.
