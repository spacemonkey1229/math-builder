# Concept sheet — Mining & Mineral Extraction (`mining-minerals`)

Domain entry: `readmodel/domains.json` id `mining-minerals` (cluster Food, Energy & Resources; `existing_cases: []`).
Overlap check: no title in `readmodel/cases_index.json` and no sheet in `cases/_concepts/` covers mining, pits, ore grade, or coal mine types
(grep for stripping / ore grade / tailings / copper / lithium / open-pit found only passing mentions in unrelated sheets).
Subject-matter notes: no private individuals, no living people, no deaths. Protagonists are fictional and labelled **[CONSTRUCTED]**.

## Data confirmation log (fetched 2026-10-27, scripted `curl`)

| Source | URL | Result |
|---|---|---|
| USGS MCS 2026 — Copper | https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-copper.pdf | 200, parsed; COMEX 2021-25e cents/lb = 424.3, 400.7, 385.7, 421.6, 480 |
| USGS MCS 2026 — Gold | https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-gold.pdf | 200, parsed; price $/troy oz 2021-25e = 1,801, 1,802, 1,945, 2,388, 3,300 |
| USGS MCS 2026 — Lithium | https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-lithium.pdf | 200 (downloaded, not used) |
| MCS landing page | https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries | **403 to scripted fetch** (page exists; use the per-commodity pubs.usgs.gov PDFs above) |
| USGS MRDS | https://mrdata.usgs.gov/mrds/ ; record page `https://mrdata.usgs.gov/mrds/show-mrds.php?dep_id=10015868` (Monarch Mine, MT) | 200, content parsed. Page itself says USGS ceased systematic updates in 2011 (stale-ish; fine for location/commodity only). The WFS typename guess `mrds` failed, so no bulk/CSV query confirmed. |
| EIA Annual Coal Report 2024 | https://www.eia.gov/coal/annual/ ; tables at `https://www.eia.gov/coal/annual/pdf/table21.pdf` (productivity by state & mine type), `.../table28.pdf` (sales price by state & mine type) | 200, parsed. The `xls/tableN.xls` links 200 but return an HTML page, so use the `pdf/` tables or the `xlsx` links shown on the index. |
| MSHA Open Government Data | https://arlweb.msha.gov/OpenGovernmentData/OGIMSHA.asp | 200, dataset list read (mines, quarterly employment/production by subunit); data files not downloaded |
| Rail/truck haul $ per tonne-km, plant capital cost | none fetched | **UNVERIFIED**; carried as stated scenario assumptions only |

All numbers below were computed in Python from the parsed tables, not typed from memory. Scripts: `/private/tmp/claude-501/-Users-manan-Documents-Claude-Projects-Math-Builder/5233bf10-b939-463f-bbe3-7a3c2a3e2f2f/scratchpad/c/{c1b,c2c,c3}.py`.

---

## C1 — The Last Bench · tier T3 · RECOMMENDED

**Protagonist.** Mara Okonkwo-Reyes **[CONSTRUCTED]**, planning engineer at a fictional Nevada-style open-pit gold mine, "Quartz Mesa". Framing is disclosed as constructed; the *price series* and the US gold context are real (USGS MCS 2026).

**Dilemma.** A.) Close the pit at its current floor and process only the ore already exposed OR B.) Approve a 60 m pushback that widens and deepens the pit to reach the next block of ore.

**Why the math decides it.** The pit is an inverted truncated cone; deepening it at a fixed wall angle also widens the rim, so waste grows much faster than ore. Ore sits in a cylindrical pipe. A student must compute the frustum shell volume, the ore-pipe cylinder volume, the stripping ratio, and compare it with the break-even stripping ratio set by the gold price.

**Primary metric.** Life-of-pit cash margin, undiscounted, $M: (ore tonnes x (recovered gold value - processing cost)) - (all tonnes moved x mining cost) - fixed pushback capital. Option A = remaining reserve only; Option B = remaining reserve + pushback.

**Scenario assumptions (disclosed, T3):** wall angle 42 degrees overall; current floor radius 180 m, depth 300 m, pushback +60 m; ore pipe radius 140 m; rock density 2.6 t/m3; head grade 1.0 g/t, recovery 88%; mining $3.00 per tonne moved, processing $22 per tonne ore, pushback capital $60M; remaining reserve 25 Mt ore + 50 Mt waste; 1 troy oz = 31.1035 g.

**Computed (volume checked two ways: frustum formula and big-cone-minus-small-cone, identical):**
- Pushback shell 56.37 million m3 = 146.55 Mt moved; ore 9.61 Mt (271.8 koz recovered); waste 136.95 Mt; **stripping ratio 14.26 : 1**.
- Break-even stripping ratio = (recovered value per t - 22)/3 - 1: 8.65 (2021), 8.66 (2022), 10.01 (2023), **14.19 (2024)**, 22.79 (2025e).
- Cash margin A vs B ($M), real USGS annual prices:

| Year | Price $/oz | A | B | Winner | Margin |
|---|---|---|---|---|---|
| 2021 | 1,801 | 498.9 | 277.4 | A | 44.4% |
| 2022 | 1,802 | 499.6 | 278.3 | A | 44.3% |
| 2023 | 1,945 | 600.7 | 418.3 | A | 30.4% |
| 2024 | 2,388 | 914.1 | 852.1 | **A** | **6.8%** |
| 2025e | 3,300 | 1,559.1 | 1,745.0 | **B** | **10.7%** |

- **Break-even gold price $2,616/oz** (sits between 2024 and 2025e of the real series). Anchor the case at the 2024 final average ($2,388, A by 6.8%) with 2025e ($3,300, B by 10.7%) as the Twist; both options win somewhere and both margins are inside 20%. Fix an "as of" cutoff (SPEC section 5) because the 2025 figure is an estimate.
- Wall-angle lever: break-even price falls from $2,964 (38 deg) to $2,616 (42 deg) to $2,129 (50 deg); steeper walls cut waste but raise stability risk, the natural strongest-counter-argument for B.

**Spine skills closed (all from `readmodel/standards_spine.json`):**

| id | kind | n now |
|---|---|---|
| geometry-how-to-find-the-volume-of-a-cone | how-to | 2 |
| geometry-how-to-find-the-volume-of-a-cylinder | how-to | 2 |
| geometry-cone | term | 3 |
| geometry-angle | term | 3 |
| geometry-degree | term | 3 |

Score = (1.0 + 1.0 + 0.6 x 3) x 0.6 (MEDIUM) = **2.28**. Within the 15-skill guard. Honest caveat: only the two how-tos are true holes-to-thin; the terms are thickening.

**Data feasibility: MEDIUM (price HIGH, geometry/cost = disclosed assumptions).** The decisive variable (annual gold price, USGS MCS 2026) is live and fetched. Pit dimensions, grade and costs are **not** from a real mine; they are stated assumptions. Upgrade path: swap in a real NI 43-101 / S-K 1300 technical report for one pit (UNVERIFIED, not fetched). Student-explorable: MCS gold PDF; MRDS record pages for real gold deposits (location/commodity only).

---

## C2 — Rich and Far, or Lean and Near · tier T3

**Protagonist.** Tomas Whitcombe-Alvarez **[CONSTRUCTED]**, development geologist for a fictional copper junior choosing which of two owned deposits to advance. (Mirrors the domain archetype "0.4% near the rail line vs 1.1% far from anywhere".)

**Dilemma.** A.) Develop Body N: a large 0.40% Cu open pit 14 km from the rail loadout OR B.) Develop Body F: a small 1.10% Cu underground deposit 190 km away that needs a new access road and power line.

**Primary metric.** Life-of-project operating cash margin net of access infrastructure ($M, undiscounted). Plant capital and discounting are **deliberately excluded and disclosed**; R1 may demand a plant-capex assumption (a lever, not a flaw).

**Assumptions (disclosed):** N: 200 Mt, $20/t ore, 14 km. F: 55 Mt, $36/t ore, 190 km. Recovery 88%; concentrate 28% Cu; concentrate haul $0.12 per tonne-km (UNVERIFIED); access infrastructure $1.5M per km. 1 tonne = 2,204.62 lb.

**Computed:** N yields 7.76 lb Cu per tonne ore (4.0 kg/t grade), F 21.34 lb (11.0 kg/t). Break-even (crossover) copper price **$4.54/lb**. Using real USGS COMEX annual averages:

| Year | COMEX $/lb | N $M | F $M | Winner | Margin |
|---|---|---|---|---|---|
| 2021 | 4.243 | 2,560 | 2,672 | F | 4.2% |
| 2022 | 4.007 | 2,194 | 2,395 | F | 8.4% |
| 2023 | 3.857 | 1,961 | 2,219 | F | 11.6% |
| 2024 | 4.216 | 2,518 | 2,640 | **F** | **4.6%** |
| 2025e | 4.800 | 3,425 | 3,326 | **N** | **2.9%** |

High grade survives low prices; bulk tonnage wins on upside leverage, a real mining trade-off. Infrastructure cost lever at 2024: $0.5M/km gives F 2,830; $4M/km gives F 2,165 (flips to N). Margins stay <=12% in every real year.

**Spine skills closed:** `number-sense-place-value` (term, n=3; grade % to kg/t and lb/t decimal shifts). The compound-unit and percent skills are already heavily covered (n=21, 90), so this concept **adds almost no new coverage**; `Digit` ids (n=1, n=2) are NOT honestly forced and are not claimed. Score = 0.6 x 0.6 = 0.36.

**Data feasibility: MEDIUM.** Real: copper price series, 2025 "lower ore grades at multiple mines" context, US production (1,000 kt 2025e), all from MCS 2026 copper (fetched). Assumed: grades, tonnages, costs, haul rate, infrastructure cost. Grade/tonnage of real porphyry deposits (USGS grade-tonnage models) NOT located or fetched: UNVERIFIED.

---

## C3 — Tons per Hour, Dollars per Ton · tier T2 (HIGH data, low new coverage)

**Protagonist.** Dale Hutchins-Ngo **[CONSTRUCTED]**, operations analyst at a fictional mid-size Indiana coal producer deciding the next property's mining method. Real numbers: EIA Annual Coal Report 2024, Tables 21 and 28.

**Dilemma.** A.) Open an underground room-and-pillar mine OR B.) Open a surface (strip) mine on the next property.

**Primary metric.** Sales value produced per employee-hour = (average sales price, $/short ton) x (production per employee-hour, short tons). A ratio of two published rates, so it is a unit-conversion exercise by design. Excludes capital, royalties, reclamation (disclosed scope limit).

**Computed (parsed from the EIA PDFs, Indiana):**

| Year | Underground: $/ton x tons/hr | Surface: $/ton x tons/hr | $ per employee-hour (UG vs Surf) | Winner | Margin |
|---|---|---|---|---|---|
| 2024 | 67.29 x 3.89 | 53.64 x 4.75 | 261.8 vs 254.8 | **Underground** | **2.7%** |
| 2023 | 59.52 x 3.84 | 59.51 x 4.42 | 228.6 vs 263.0 | **Surface** | **13.1%** |

The winner flips between two consecutive real years, so neither method dominates. Other states in the same tables show where each side wins decisively (Colorado and Kentucky-East favor surface; Pennsylvania, Virginia, Alabama favor underground), useful as an Appendix "does it generalize?" check. Kentucky Total 2024 is also close (surface +5.9%).

**Break-even (2024):** the tie is at $261.8 vs $254.8 per employee-hour. Surface would need 4.88 tons/hr (reported 4.75) to tie underground; underground would fall to a tie at 3.79 tons/hr (reported 3.89) or at $65.50/ton (reported $67.29).

**Spine skills closed:** none at n<=2. Exercises `measurement-how-to-convert-an-amount-with-compound-units` (n=21) and `measurement-ratio` (n=30). Score ~0 for coverage; value is as a HIGH-data, low-risk, easily facilitated case or as a warm-up pairing for C1.

**Data feasibility: HIGH.** EIA tables fetched and parsed; free, annual, per-state, student-downloadable. Caveats to disclose: mine-type price differences partly reflect coal rank and market (e.g. Alabama's metallurgical coal), some cells are "withheld"; Indiana is thermal bituminous with both mine types reported. As-of cutoff = ACR 2024 final.

---

## Ranking and recommendation

| Rank | Concept | Score | Data | Min margin / max margin across real years |
|---|---|---|---|---|
| 1 | C1 The Last Bench | 2.28 | MEDIUM | 6.8% (2024) to 10.7% (2025e) at the two anchor years |
| 2 | C2 Rich and Far, or Lean and Near | 0.36 | MEDIUM | 2.9% to 11.6% in all five years |
| 3 | C3 Tons per Hour, Dollars per Ton | ~0 | HIGH | 2.7% (2024), 13.1% (2023) |

**Pick C1.** It is the only concept that closes true thin-skill holes (cone volume, cylinder volume), has a clean break-even ($2,616/oz) that falls inside the real five-year price range, and the decisive input is a live fetched USGS series. If the reviewers weight data grade over skill closure, swap to C3.

**Open issues for R1:** (1) C1/C2 cost and geometry inputs are assumptions, not sourced; (2) C1 2025 price is a USGS estimate (needs as-of cutoff); (3) C2 omits plant capex and discounting; (4) C3 metric ignores costs and conflates coal rank with mine type.
