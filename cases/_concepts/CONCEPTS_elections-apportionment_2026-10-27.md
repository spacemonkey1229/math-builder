# Concept sheet — Elections, Districting & Apportionment (`elections-apportionment`)

**Target and why.** Domain is MEDIUM authoring priority / HIGH data grade with 5 existing cases
(Electoral College, Gerrymandering, Redrawing Lines, The Gijon Rule, The Approval Gate). Those cover
the Electoral College, map-drawing, and voting-rule premises. This sheet deliberately avoids all of
them and uses three untouched angles: (1) the House seat-allocation rule itself, (2) polling-place
design, (3) paper-ballot print runs. Nonpartisan throughout: no candidates, no parties.

**Honest scoring note.** `domains.json` lists 0 uncovered signature skills for this domain, and the
signature skills are well covered (measurement-rounding n=40, measurement-ratio n=30,
geometry-area n=11). So none of these closes a true hole; the thin skill in play is
`advanced-operations-absolute-value` (n=4). The value here is domain breadth plus HIGH-grade live
data, not gap-closing. Skills below carry their real current `n`.

All numbers were recomputed in code this session (scratchpad scripts; data fetched live from
census.gov and eac.gov, see each feasibility note).

| # | Concept | Tier | Data grade | Computed margin |
|---|---|---|---|---|
| C1 | The Eighty-Nine | T3 | HIGH | HH vs Webster: 4.1% (2020), 1.5% the other way (2010) |
| C2 | Six Vote Centers | T3 | MEDIUM-HIGH (real counts, disclosed behavioural parameters) | 0.9% to 17.7% either side of break-even |
| C3 | The Print Run | T2 | MEDIUM-HIGH | 7.3% at M=10, 6.9% the other way at M=20 (break-even M = 11.3) |

**Recommendation: write C1.** Strongest real story (the 2020 last seat was decided by 89 people),
all inputs are official Census tables, every number reproduces exactly, and it has a genuine
both-win structure. C2 is the best runner-up for a student-engagement angle (a county you can name,
real counts) but its break-even depends on assumptions that case-research must disclose.

---

### C1 — The Eighty-Nine   ·   T3

**Protagonist.** Priya Venkataraman, a (fictional) mathematical statistician on the Census Bureau's
apportionment team, preparing the method memo for the next decennial apportionment. Constructed
framing, clearly disclosed; the underlying facts are all real and official.

**True story it rests on.** In the 2020 apportionment the 435th House seat went to Minnesota (8th
seat) and the 436th (first one left out) would have gone to New York (27th seat). Priority values
from the Census Bureau's own file: Minnesota 762,997.705 vs New York 762,994.353. Recomputed: New York
needed about **89 more residents** (88.8) to take the seat. Real, official, widely reported.

**Dilemma.** A) Keep the Huntington-Hill method (equal proportions, current law since 1941) OR
B) switch to Webster (Sainte-Lague, round at the half). The two give different seat counts for four
states in 2020 (Montana, New York, Ohio, Rhode Island).

**Primary metric.** Largest gap in district size: persons per representative in the biggest
single-seat-or-multi-seat district divided by the smallest (max/min ratio). Lower is fairer.

**Computed with real data** (Census Table C2 apportionment populations, H = 435, recomputed from
scratch; Huntington-Hill reproduces the actual seat allocation in all 8 censuses 1950-2020, which is
the integrity check):

| Census | HH max/min | Webster max/min | Winner (margin) |
|---|---|---|---|
| 2020 | 1.8257 (Delaware 990,837 vs Montana 542,704) | 1.9009 | HH by 4.1% |
| 2010 | 1.8847 | 1.8568 | **Webster by 1.5%** |
| 2000 / 1990 / 1980 / 1950 | identical | identical | tie |
| 1970 | 2.0528 | 2.3073 | HH by 12.4% |
| 1960 | 2.1428 | 2.6835 | HH by 25.2% (outside the 20% cap; use as a backtest footnote, not the headline) |

Break-even structure: holding the 2020 populations fixed and sweeping House size 300 to 600,
Webster beats HH only at H = 428 through 433 (1.9009 vs 1.9768, Webster by 3.8%), HH wins at 127
sizes and they tie at 168. So at 435 HH wins, but the answer flips just below the real House size.
Neither option dominates; the headline decision margin is 4.1%.

**Why it's close / balanced.** HH wins on the "worst-gap" metric; Webster wins the sum of
absolute seat errors (11.67 vs 12.07 seats in 2020, 3.4%). A student arguing for Webster must use a
different yardstick, which is the actual intellectual history of the method fight.

**Spine skills (prefer n<=2; none exist here, real n shown).**
- `measurement-ratio` (n=30), `measurement-rounding` (n=40), `advanced-operations-absolute-value` (n=4).
- Optional: `statistics-and-probability-population` (n=11).
Claimed new coverage: honestly 0 holes; thickens absolute value (n=4 -> 5).

**Data feasibility — HIGH (fetched and confirmed).**
- Census 2020 apportionment table 1 and priority values (fetched, parsed): `https://www2.census.gov/programs-surveys/decennial/2020/data/apportionment/apportionment-2020-table01.xlsx` and `.../2020PriorityValues.xlsx`.
- Table C2, 1910-2020 apportionment population and seats by state (fetched, parsed): `https://www2.census.gov/programs-surveys/decennial/2020/data/apportionment/apportionment-2020-tableC2.xlsx`.
- Historical CSV: `https://www2.census.gov/programs-surveys/decennial/2020/data/apportionment/apportionment.csv` (fetched).
- Landing page `https://www.census.gov/data/tables/2020/dec/2020-apportionment-data.html` (fetched; lists the files above).
All free, no login. Students can reproduce every figure with a spreadsheet.

**Risk / R1 notes.** Needs the plain-language HH vs Webster explanation (priority = pop / sqrt(n(n+1)) vs pop / (n + 0.5)). No living individuals named; "New York" and "Minnesota" are states, and no party is mentioned.

---

### C2 — Six Vote Centers (working title)   ·   T3

**Protagonist.** A county election director (fictional, unnamed individual), Kalamazoo County,
Michigan, deciding the polling-place layout.

**Dilemma.** A) Keep the current **83** neighborhood polling places OR B) consolidate to about
**41-42** larger vote centers with twice the check-in stations each (same total staff and stations).

**Primary metric.** Average minutes a voter spends getting there plus waiting plus checking in
(ratio: minutes per voter, not a total).

**Real inputs (EAC 2024 EAVS, Census Gazetteer):** 83 Election Day polling places (D3a), 859 Election
Day poll workers (D5a), 64,139 voters at physical polling places (F1b), land area 561.959 sq mi.
That is 10.3 workers and 773 voters per place.

**Constructed/disclosed parameters (case-research must source or flag as modeling assumptions):**
40% of workers staff check-in (4 stations per current place), 2.0 minutes per check-in, travel at
30 mph, mean distance to nearest place = 0.377 x sqrt(area / places) (hexagonal-grid approximation),
and h = share of a place's voters arriving in the busiest hour. Queue wait is M/M/c (Erlang C).

**Computed (code):** both options win depending on peak-hour share.

| h | A: 83 places (min) | B: 41.5 centers (min) | Result |
|---|---|---|---|
| 0.10 | 4.45 | 4.91 | A better by 10.4% |
| 0.12 | 5.17 | 5.22 | A better by 0.9% |
| **0.1214** | **5.256** | **5.256** | **break-even** |
| 0.14 | 7.98 | 6.57 | B better by 17.7% |
| 0.15 | 17.55 | 11.33 | B better by 35.5% (outside cap; use as the "stress" extension) |

Travel A 1.96 min vs B 2.77 min; waiting at h=0.14 is 4.02 min vs 1.79 min. Sensitivity: break-even
h moves to about 0.171 at 1.5 min/voter and 0.093 at 2.5 min/voter, so the service time is the
single assumption to source. The queue goes unstable (infinite wait) above about h = 0.155.

**Spine skills (real n):** `geometry-area` (n=11), `measurement-ratio` (n=30), plus
`geometry-perimeter` (n=6) if the case uses a rectangular county sketch for distance. No thin skill
closed.

**Data feasibility — MEDIUM-HIGH.**
- EAC EAVS 2024 CSV (fetched, 6,461 jurisdictions, parsed): `https://www.eac.gov/sites/default/files/2026-02/2024_EAVS_for_Public_Release_nolabel_V2_csv.zip`. Variable labels confirmed from the codebook (fetched): `https://www.eac.gov/sites/default/files/2025-06/2024_EAVS_Codebook.xlsx`. Dataset index page fetched: `https://www.eac.gov/research-and-data/datasets-codebooks-and-surveys`.
- Census Gazetteer counties (fetched, parsed): `https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2024_Gazetteer/2024_Gaz_counties_national.zip` (ALAND_SQMI column).
- Peak-hour share and per-voter check-in time: **UNVERIFIED** — no source fetched; would be modeling assumptions unless case-research finds a published figure.

**Risk / R1 notes.** Vote centers versus precinct polling places is a live policy topic; keep the framing strictly about minutes, not turnout effects or who benefits. EAVS jurisdictions with towns-as-jurisdictions need care (county rows only).

---

### C3 — The Print Run (working title)   ·   T2

**Protagonist.** A state elections logistics officer (fictional) setting the paper-ballot print
order for in-person voting for every county.

**Dilemma.** A) Print for **50% of each county's active registered voters** OR B) print **120% of
that county's 2020 in-person voter count**.

**Primary metric.** Cost per ballot actually cast = (surplus ballots printed + M x ballots short) / ballots cast, where M is how many times costlier an emergency ballot is than a planned one (disclosed assumption).

**Computed (code, 2,412 counties with matching 2020 and 2024 EAVS rows, both years in-person count >= 500):** In 2024, in-person voters were a median 37.1% of active registered (10th-90th percentile 15.2%-59.5%), and in-person voting grew a median 1.143x from 2020 (p10 0.903, p90 1.613).

| M | A: 50% of active | B: 120% of 2020 | Result |
|---|---|---|---|
| 5 | 1.060 | 0.624 | B better by 41% |
| 10 | 1.237 | 1.148 | B better by 7.3% |
| **11.30** | **1.283** | **1.283** | **break-even** |
| 20 | 1.592 | 2.194 | A better by 27% |

Surplus/shortage as share of ballots cast: A 88.3% / 3.5%, B 10.1% / 10.5%. Both options have a
region where they win; honest margins near the break-even are within 20% (M between about 8 and
16, margin vs the costlier option); outside that one dominates, so the case must pin M down from a cited source.

**Spine skills (real n):** `advanced-numbers-how-to-convert-numbers-to-percents` (n=44),
`measurement-rounding` (n=40), `measurement-ratio` (n=30). No thin skill closed.

**Data feasibility — MEDIUM-HIGH.**
- EAVS 2024 CSV and codebook (fetched, see C2). EAVS 2020 v1.2 CSV (fetched, parsed): `https://www.eac.gov/sites/default/files/2023-12/2020_EAVS_for_Public_Release_nolabel_V1.2_CSV.zip`.
- 2020 variable *labels* (that F1b = physical polling place voters in 2020) were matched by column name only; **UNVERIFIED** against the 2020 codebook. County-level aggregation also hides precinct-level shortages.
- Emergency-reprint cost multiplier M: **UNVERIFIED**, constructed assumption.

**Risk / R1 notes.** Weakest of the three: the multiplier M drives the winner, so a reviewer may call it assumption-dependent. Ballot shortages have been politically charged; keep the framing about paper logistics, with no state or party named as at fault.

---

## Not recommended / dropped

- **MIT Election Lab precinct and House returns**: the dataset exists (Harvard Dataverse DOI 10.7910/DVN/IG0UN2, file `1976-2024-house.tab` listed via API) but a direct download returns a guestbook-required error, so it could not be computed on here. Student-explorable via browser click-through only. Useful for a later recount-threshold concept; mark LOW until fetched.
- **Census API (api.census.gov)**: requires a free key; not used. A town-level weighted-voting (Banzhaf) concept needs it.
- **Hamilton vs Huntington-Hill as the headline**: HH dominates on max/min in every census (never loses), so it fails the both-win rule; the HH vs Webster pairing in C1 replaces it.
