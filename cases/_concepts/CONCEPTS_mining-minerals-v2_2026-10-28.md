# Concept sheet v2 (single concept) — The Last Bench (`mining-minerals`)

Revision of C1 from `CONCEPTS_mining-minerals_2026-10-27.md` after R1 review (R1a REVISE blocking, R1b GO, R1c REVISE). Domain entry: `readmodel/domains.json` id `mining-minerals`. Overlap check: no mining/pit/ore case in `readmodel/cases_index.json` or other sheets. Every number below was recomputed in Python (scripts `lb.py`, `d.py` in the session scratchpad; volumes checked two ways, frustum formula and cone-minus-cone, identical to 1e-8). C1 was balanceable after honest work, so the C3 fallback was **not** used.

## Data confirmation log (re-fetched 2026-10-28, scripted `curl` + `pdftotext`)

| Source | URL | Result |
|---|---|---|
| USGS Mineral Commodity Summaries 2026, Gold | https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-gold.pdf | HTTP 200, parsed. Salient statistics, "Price, dollars per troy ounce" 2021-25e = 1,801 / 1,802 / 1,945 / 2,388 / 3,300. Footnote: Engelhard's average quotation for the year; **the 2025 price "was estimated by the U.S. Geological Survey based on data from January through November" 2025.** Text: "estimated gold price in 2025 increased by 38%" over 2024. |
| USGS MRDS (location/commodity only, optional exploration) | https://mrdata.usgs.gov/mrds/ | Fetched 2026-10-27; USGS states systematic updates ceased 2011. Not load-bearing. |

Everything else (pit geometry, grade, recovery, costs, throughput, crew, town, discount rate) is a **stated scenario assumption**, not data (SPEC section 5(b)). No real mine is represented.

---

## The Last Bench · tier T3 · single concept

**Protagonist.** Corwin Brandvold **[CONSTRUCTED]**, planning engineer at a fictional open-pit gold mine, "Quartz Mesa", outside the fictional town of Ebbet Wells. (Grep of `cases/` and `readmodel/` for Corwin, Brandvold, Ebbet, Quartz Mesa: no hits.) The gold price series is real; the mine, the town and the people are constructed and labelled so.

**Story (Overview seed; no numbers the student needs).** Corwin stands on the last bench of the pit at shift change, hard hat in hand, watching haul trucks crawl up the ramp in single file like ants on a wall. The pit floor is scraped almost clean. Below it, the drill cores show one more block of ore, but reaching it means cutting the whole rim back and hauling a mountain of barren rock out first. Up on the rim, the first-shift crew is lining up at the dry shed; he knows most of their kids by name. The board wants his recommendation on Monday. He has two signature blocks on his desk and a pen in his hand. The scene ends with the pen above the paper, not the ink.

**Dilemma (exact SPEC 1.4 shape).**
You are Corwin Brandvold. Do you:
A.) Close the pit at its current floor and finish only the reserve already planned (25 Mt of ore plus the 50 Mt of waste that must be moved with it, 75 Mt in all) OR
B.) Approve a 60 m pushback that widens and deepens the pit to reach the next block of ore, on top of that same planned reserve.

*(Wording fix (c): Option A is **not** "only the exposed ore". It still moves 75 Mt, of which 50 Mt is waste; it simply stops there.)*

**Primary metric.** Life-of-pit cash margin, **undiscounted**, in $M:
(ore tonnes x (recovered gold value per tonne - processing cost per tonne)) - (all tonnes moved x mining cost per tonne) - pushback capital.
A = planned reserve only. B = planned reserve + pushback ore, minus the pushback capital.

**Margin convention (stated once, applied everywhere): margin = (winner - loser) / winner.**

**Secondary lens (the stake, not the metric): crew-years of work** = years of mine life x crew size. This is the people-side of the choice and a reason B can be defended even in a year when A wins on cash.

### Modeling Assumptions block (SPEC section 5; all labelled assumptions, none are facts)

*Geometry (assumption).* Overall wall angle 42 degrees. Current pit: floor radius 180 m, depth 300 m. Pushback: +60 m deeper, floor radius unchanged at 180 m, walls kept at 42 degrees. Ore pipe: cylinder, radius 140 m, so the new 60 m of depth exposes a pipe 60 m tall. Rock density 2.6 t per cubic metre for ore and waste alike.
*Rim radii and cone heights are **given** to the student (Appendix B).* The student does not need trigonometry; see "Fixes applied (b)".
*Grade and recovery (assumption).* Head grade 1.0 g/t for planned reserve and pushback ore alike; plant recovery 88%; 1 troy oz = 31.1035 g.
*Costs (assumption).* Mining $3.00 per tonne moved (ore and waste); processing $22 per tonne of ore; pushback capital $60M.
*Planned reserve (assumption).* 25 Mt ore and 50 Mt waste, mined in both options.
*Throughput and timing (assumption, used for years/crew/discounting only).* The fleet moves 20 Mt of rock per year. In B the pushback is mined after the planned reserve, and the $60M is spent when the pushback begins (this ordering is the harsher one for B under discounting).
*Scenario stake (assumption, **not fact**).* Crew of 180 workers, all employed for as long as the pit operates and assumed to leave the district when it closes; town of Ebbet Wells, scenario population 2,100. These figures are inputs the class may challenge and change; nothing here is real employment data.
*Excluded (disclosed).* Royalties, income and severance taxes, reclamation and closure liabilities, working capital, price risk after the decision, and by-product silver. The metric is undiscounted by design; discounting is tested as a sensitivity (below).
*As-of cutoff (SPEC section 5).* All price data frozen at USGS MCS 2026 (published January 2026; the 2025 figure is a USGS estimate from January-November 2025 data). Case cutoff: **2026-10-28**. Anything after the MCS 2026 is excluded.

### Recomputed results (Python)

**Geometry (identical by two methods).** Rim radii: 513.18 m (current), 579.82 m (after pushback). Pit volumes 121.93 Mm3 (current), 178.30 Mm3 (pushback). **Pushback shell = 56.367 Mm3 = 146.55 Mt moved.** Ore pipe = pi x 140^2 x 60 = 3.695 Mm3 = **9.606 Mt** (271.8 koz recovered). Waste in shell 136.95 Mt. **Pushback stripping ratio = 14.26 : 1** (waste tonnes per ore tonne).
Totals: A moves 75.00 Mt (25 ore); B moves 221.55 Mt (34.61 ore, 186.95 waste).

**Break-even stripping ratio (corrected: includes the $60M capital).**
Break-even SR = (recovered value per ore tonne - processing)/mining - 1 - capital/(pushback ore tonnes x mining cost).

| Year | Price $/oz | Recovered value $/t ore | Break-even SR | Pushback SR | B pays? |
|---|---|---|---|---|---|
| 2021 | 1,801 | 50.96 | 6.57 | 14.26 | no |
| 2022 | 1,802 | 50.98 | 6.58 | 14.26 | no |
| 2023 | 1,945 | 55.03 | 7.93 | 14.26 | no |
| **2024** | **2,388** | 67.56 | **12.11** | 14.26 | **no** (SR above break-even) |
| 2025e | 3,300 | 93.37 | **20.71** | 14.26 | yes |

(The 27-Oct draft showed 14.19 and 22.79 because the capital term was missing; corrected values are 12.11 and 20.71.)

**Cash margin, undiscounted, $M (margin = gap / winner):**

| Year | Price | A | B | Winner | Gap | Margin |
|---|---|---|---|---|---|---|
| 2021 | 1,801 | 498.9 | 277.4 | A | 221.5 | 44.4% |
| 2022 | 1,802 | 499.6 | 278.3 | A | 221.3 | 44.3% |
| 2023 | 1,945 | 600.7 | 418.3 | A | 182.4 | 30.4% |
| **2024 (anchor)** | **2,388** | **914.1** | **852.1** | **A** | 62.0 | **6.8%** |
| 2025e (Twist) | 3,300 | 1,559.1 | 1,745.0 | B | 185.9 | 10.7% |

**Break-even gold price = $2,616/oz** (A and B tie). It sits between the real 2024 and 2025e prices. At 2024 prices B trails A by $62.0M; even with $0 capital B would still trail by $2.0M, so the live lever is price, not capital.
Sensitivities (all with the others held fixed): mining cost $2.50 / $3.00 / $3.50 per t moves break-even to $2,346 / $2,616 / $2,886; capital $40M / $60M / $80M gives $2,543 / $2,616 / $2,690; wall angle (rim radii in Appendix B) 38 / 42 / 50 degrees gives pushback SR 17.54 / 14.26 / 9.66 and break-even $2,964 / $2,616 / $2,129.

**Discounting does not flip either anchor year (8% a year, 20 Mt/yr, pushback after reserve, capital at start of pushback):**

| Year | A PV $M | B PV $M | Winner | Margin |
|---|---|---|---|---|
| 2024 | 794.0 | 747.9 | A | 5.8% |
| 2025e | 1,354.3 | 1,450.2 | B | 6.6% |

Robustness: across throughput 10-50 Mt/yr and discount rates 5%, 8%, 10%, 12%, both anchor winners hold (2024 A, 2025e B). Discounted B at 8% for 20 Mt/yr is the less favourable ordering for B; moving the capital to time 0 lowers B further in 2024 (732.8) and 2025e (1,435.1), and still leaves 2025e with B ahead. Even at 15% and 30% (20 Mt/yr) 2025e stays with B (1,269 vs 1,213; 1,011 vs 992). Discounted break-even price at 8%, 20 Mt/yr: about $2,684/oz, still between 2024 and 2025e.

**Stake numbers (scenario).** Mine life: A = 75 / 20 = **3.75 years**, B = 221.55 / 20 = **11.08 years**. Crew-years: A 675, B 1,994; B adds **7.33 more years / 1,319 crew-years** of work. So at 2024 prices Corwin can say: "A earns $62M more cash, B keeps 180 people employed 7.3 years longer." That is the dilemma.

**Balance test (SPEC section 2).** Anchor 2024: A wins by **6.8%** (undiscounted), 5.8% discounted. Twist 2025e: B wins by **10.7%**, 6.6% discounted. Both inside 20%. Strongest quantitative argument for A: at $2,388/oz the pushback's stripping ratio (14.26) is above the break-even (12.11), so each extra ounce costs more to uncover than it earns, and A banks $62M more with no capital at risk. Strongest for B: the gold price already crossed the $2,616 break-even in the same USGS series one year later, the pushback adds 271.8 koz of recoverable gold, and it extends the mine's life from 3.75 to 11.08 years.

### Deliverables (Challenge 3, the pitch must contain)
1. **Volume table:** current pit and pushback pit volumes from the given radii and heights (cone volume, big cone minus small cone), the shell in Mm3 and Mt, with the check that both methods agree.
2. **Ore pipe:** cylinder volume of the new 60 m of pipe in Mm3 and Mt; ounces recovered at 1.0 g/t and 88%.
3. **Stripping ratio vs break-even stripping ratio** at 2024 and 2025e prices, with the one-line rule "pay for the pushback only if its stripping ratio is below the break-even".
4. **Cash margin table A vs B** at the 2024 anchor, with margin stated as gap / winner, and the break-even gold price.
5. **Stake table:** years of mine life and crew-years for A and B at the stated crew size, plus the student's own re-run with a different crew or throughput they choose and justify.
6. **One original visual:** margin A vs B across the five USGS years, break-even price marked.
7. **Twist step:** re-run with the 2025e price; say what changes and why the answer does not simply track the latest number.

### Spine skills closed (honest claim; all ids exist in `readmodel/standards_spine.json`)

| id | kind | n now | Forced by |
|---|---|---|---|
| geometry-how-to-find-the-volume-of-a-cone | how-to | 2 | Deliverable 1 (cones from given radius and height) |
| geometry-how-to-find-the-volume-of-a-cylinder | how-to | 2 | Deliverable 2 (ore pipe) |
| geometry-cone | term | 3 | Deliverable 1 |
| geometry-cylinder | term | 3 | Deliverable 2 |

Not claimed (v1 claimed these and they are **withdrawn**): `geometry-angle`, `geometry-degree`. With radii given, the 42-degree angle is a stated context number that students never operate on. `pre-calculus-tangent-function` (n=2) was considered and rejected: claiming it would require the student to compute the rim radii as 180 + depth / tan 42, which is a precalculus step and moves the case to T4. Score (v1 formula) = (1.0 + 1.0 + 0.6 x 2) x 0.6 (MEDIUM data) = **1.92**; the two how-tos are true holes (n=2) that this case thickens.
Appendix "How To..." list (verbatim labels): *How to find the volume of a cone*; *How to find the volume of a cylinder*; *Cone*; *Cylinder*.

**Tier: T3.** Three or more interacting variables (price, stripping ratio, capital, throughput), some data deliberately irrelevant (wall angle, density is a pass-through, 2021-22 prices); multi-step volume work and an optimization/break-even over a set of years. Not T4: no function modeling, no assumption the student must invent (all inputs given, with an optional extension in which the student chooses their own crew size).

### Data / feasibility: MEDIUM
Price series (the decisive variable) is real, fetched, and reproducible from one USGS PDF (HIGH). Geometry, grade, cost, throughput and crew are labelled scenario assumptions (SPEC 5(b)); upgrade path is a real NI 43-101 / S-K 1300 technical report (UNVERIFIED, not fetched). Student-explorable: MCS gold PDF; MRDS records for real gold deposits (location/commodity only; stale since 2011). Case remains solvable if the link dies because the price row is reproduced in Appendix A.

### Appendices (planned)
A. USGS gold price row 2021-2025e with the footnote text and as-of statement. B. Modeling Assumptions block plus **given geometry**: rim radii 513.2 m and 579.8 m; full-cone apex heights 462.1 m and 522.1 m (so the removed floor cone is the same 5.50 Mm3 in both; hint, not a trigonometric task); other-angle table (rim radius before / after pushback: 38 degrees 564.0 / 640.8 m; 42 degrees 513.2 / 579.8 m; 50 degrees 431.7 / 482.1 m). C. Unit conversions (oz to g, short note that tonnes here are metric). D. Stake scenario sheet (crew, town, throughput) marked as inputs. E. How-To list.

### Facilitator note (SPEC 6)
This case touches job loss and the future of a small town. Some students may have a family member in mining, energy or another industry that has closed. Frame the crew and town figures as a **scenario** the class may change, not a prediction; invite the discussion to ask who bears the cost of each option without assigning blame to a person. Do not let the cash margin alone end the debate: the stake is a legitimate argument, but the math must show it, not assume it.

---

## Fixes applied

| # | Reviewer finding | Change |
|---|---|---|
| a | R1a blocking: break-even SR omitted $60M capex (14.19 / 22.79) | Formula now includes capital/(ore x mining). Python gives **12.11 (2024)** and **20.71 (2025e)** (also 6.57, 6.58, 7.93 for earlier years); break-even price recomputed ($2,616/oz, unchanged because margin tables already included capex) |
| b | R1a: tan(42) not covered by skills | Chose **given radii** (513.2 m, 579.8 m) plus cone apex heights; no trig claimed or needed; tier stays T3; `geometry-angle` and `geometry-degree` claims withdrawn; tangent considered and rejected |
| c | Option A wording ("only exposed ore") wrong | A now stated as 25 Mt ore + 50 Mt waste = 75 Mt moved; B = same plus the pushback |
| d | Label assumptions; exclusions; discounting | Modeling Assumptions block; royalties/taxes/reclamation/by-product excluded; 8% discounting tested (2024 A 794.0 vs B 747.9; 2025e B 1,450.2 vs A 1,354.3), rate and throughput grid shows no flip |
| e | As-of date for 2025e | Frozen at USGS MCS 2026; 2025 figure is a USGS estimate from Jan-Nov 2025 data; case cutoff 2026-10-28; anchor 2024, 2025e only in the Twist |
| f | R1c: no people stake | Added scenario crew (180), town (2,100), throughput (20 Mt/yr), crew-years lens (A 675 vs B 1,994), labelled as inputs, with student re-run deliverable and facilitator note |
| g | One margin convention | gap / winner everywhere (6.8%, 10.7% undiscounted; 5.8%, 6.6% discounted) |
| h | Protagonist name collisions | Corwin Brandvold; greps show no hits in `cases/` or `readmodel/`; avoids Priya, Mara, Okafor, Raman |
| – | Cross-cutting: ending | Ends on a pen above a signature block, not a buzzing phone |
| – | Cross-cutting: decision shape | Still binary (SPEC 1.4) but the argument is now metric-vs-stake (cash vs crew-years) plus a price break-even, not a single parameter alone |

## Still open
1. **Discounted-figure discrepancy with the review note.** The reviewer's discounted values (730 vs 669; 1,319 vs 1,245) differ from mine (794.0 vs 747.9; 1,450.2 vs 1,354.3) because throughput and timing are assumptions the review did not state; my own run reproduces the reviewer's pair near 12 Mt/yr. The no-flip conclusion holds across both. R1a should confirm the throughput convention (20 Mt/yr here).
2. **UNVERIFIED:** all geometry, grade, recovery, cost, capital, throughput, crew and town figures are scenario assumptions with no real-world source; no technical report fetched.
3. **UNVERIFIED:** the 1.0 g/t grade applying equally to the planned reserve and the pushback pipe; the consistency of a 25 Mt "planned reserve" sitting inside the same pit that has a 140 m-radius ore pipe (a simplification, not derived).
4. MCS landing page returned 403 to scripts on 2026-10-27; per-commodity PDF used instead. MRDS is stale (2011).
5. 2025e price is an estimate; the final 2025 figure will appear in MCS 2027 and may differ.
