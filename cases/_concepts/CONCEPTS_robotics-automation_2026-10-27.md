# Concept sheet — Robotics & Automation (`robotics-automation`)

**Target and why.** Domain `robotics-automation` (Making & Materials, authoring priority MEDIUM, data grade MEDIUM in `domains.json`). Existing legacy: `robotics-engineer` (two-link IK route choice) and `the-setpoint-call` (PID setpoint). All three concepts avoid kinematics-route and PID premises; they are about the *economics and labour side* of automation, which the corpus does not yet cover. No titles in `cases_index.json` or sheets in `cases/_concepts/` overlap (checked: no robot/cobot/weld/mechatronics premise outside the two legacy cases).

**Sources actually fetched 2026-10-27/28 (all via curl/WebFetch, raw values recomputed in Python `-I`):**

| Source | Fetched | Values used |
|---|---|---|
| BLS Public Data API v1 (`api.bls.gov/publicAPI/v1/timeseries/data/<seriesID>`, no key) OEWS May 2025, national, all industries | LIVE, HTTP 200 | Welders 51-4121: `OEUN000000000000051412104` annual mean wage **$56,760**; `...01` employment **416,210**; `...13` median **$53,750**. Electro-mechanical & Mechatronics Technologists/Technicians 17-3024: `OEUN000000000000017302404` mean **$76,420**; `...01` employment **15,520**; `...13` median $73,900. Industrial machinery mechanics 49-9041: mean **$68,460**, employment 439,640. Laborers & freight/stock/material movers, hand 53-7062: mean **$42,260**, employment 2,950,280. |
| BLS Average Price Data `APU000072610` (electricity, $/kWh, US city avg) | LIVE | Sept 2026 **$0.196/kWh** (Jul 0.197, Jun 0.198) |
| Universal Robots UR5e datasheet PDF (URL listed in `domains.json`, re-fetched, 282,416 bytes, text extracted with `pdftotext`) | LIVE | payload **5 kg**, reach **850 mm**, 6 rotating joints, all joints +/-180 deg/s, max TCP speed 4 m/s, repeatability +/-0.03 mm, average power moderate settings **200 W** (max 570 W), footprint dia 149 mm |
| IFR press release "Global robot demand in factories doubles over 10 years" (`ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years`) | LIVE, 39,549 bytes | World Robotics 2025: **542,000** industrial robots installed in 2024; operational stock **4,664,000** (+9%); Asia 74% / Europe 16% / Americas 9% of new installs; Japan 44,500 installs, Korea 30,600 |
| NASA Perseverance traverse GeoJSON (`mars.nasa.gov/mmgis-maps/M20/Layers/json/M20_traverse.json`) | LIVE, 1.7 MB, 558 drive segments through sol 2009, 46,027.5 m | Fetched and analysed, then **rejected as a decision metric** (see "Considered and dropped") |
| Statbotics API (FIRST Robotics) | **FAILED** — HTTP 500 / empty `{}` on every endpoint tried | **UNVERIFIED — not used** |
| UR10e / UR3e datasheets | **NOT fetched** (UR product page has no PDF links) | **UNVERIFIED — not used** |

**Spine check (live `standards_spine.json`).** No skill below is at n==0 (the spine has none, consistent with earlier sweeps). Thin (n<=2): only `...number-of-outcomes-of-a-combination` (n=2) is thin; the rest are n=3-21. Stated honestly per skill below; no concept claims to close a zero.

| # | Concept | Tier | Data grade | Margin at stated volume | Thin skills touched |
|---|---|---|---|---|---|
| C1 | The Weld Cell | T3 | MEDIUM-HIGH | **10.9%** (B cheaper); flips at **1,129 h** | 0 (n=3 skill) |
| C2 | The Technician Track | T3 | HIGH | **2.6%** (A ahead at 8 y) / **4.9%** (B ahead at 10 y); flips at **8.59 y** | 0 |
| C3 | Three of Six | T4 | MEDIUM | **7.0%**; flips on a **~6%** hours change | 1 (combination, n=2) |

**Recommendation: write C1, The Weld Cell** — best mix of live data, a real robot spec sheet, a break-even that both sides can win, and a margin inside the 20% cap. C2 is a safe, very high-data second; C3 is the only one that closes a thin skill but rests on constructed station hours.

---

### C1 — The Weld Cell   ·   rank 1   ·   tier T3

**Protagonist.** Fictional: Priya Raman, owner-operator of a 6-person job shop that fabricates steel equipment frames. (Constructed; no real person or company. Disclose as constructed.)

**Framing.** Constructed, clearly disclosed. The shop has a backlog of repeat weldments and must choose now. The robot is a UR5e-class collaborative arm (real spec sheet: 5 kg payload, 850 mm reach, 200 W average draw).

**Binary dilemma.**
- **A — Hire a second welder** at the BLS mean wage, scale hours up or down with orders.
- **B — Buy a cobot weld cell** (fixed annual cost) that still needs a welder tending it 25% of its run time.

**Primary metric.** Annual cost per year of the welding workload, i.e. total dollars/year at the forecast hours (ratio form: dollars per weld-hour at forecast volume).

**Computed model (Python, recomputed).**
- Loaded welder rate = 56,760 x 1.30 / 2,080 = **$35.475/h** (1.30 benefits load and 2,080 h/yr are disclosed assumptions).
- Cobot electricity = 0.200 kW x $0.196/kWh = **$0.0392/h**.
- Cell: assumed installed cost $120,000, 5-year life, 5% of price/yr maintenance → fixed **$30,000/yr** (UNVERIFIED assumption; cell price is the one key unverified input — the student gets it as a stated/justified assumption, which is T4-style, so flag tier T3 only if price is supplied in the brief).
- Hire: C_A = 35.475 H. Cobot: C_B = 30,000 + (0.25 x 35.475 + 0.0392) H.
- **Break-even H\* = 30,000 / (0.75 x 35.475 − 0.0392) = 1,129 h/yr.**

| Hours/yr | A hire | B cell | Winner, margin |
|---|---|---|---|
| 900 | $31,928 | $38,017 | A, 19.1% |
| 1,129 | ~$40,050 | ~$40,050 | tie |
| **1,300 (stated volume)** | **$46,118** | **$41,580** | **B, 10.9%** |
| 1,600 | $56,760 | $44,253 | B, 28.3% (outside the stated band) |

Both options win somewhere; the stated 1,300 h forecast sits 15% above break-even, margin 10.9% (<=20%). Sensitivity: cell price $100k → H\* = 941; $140k → H\* = 1,317 (so at +17% price the answer flips — a nice T4 extension).

**Why a reasonable person argues either side.** A wins if orders are lumpy (volume can drop to ~900 h), and a welder can do other work; B wins if the repeat jobs are steady (consistency, no turnover). Honest unmodelled factors: programming time, payload check of torch plus wire feeder against the 5 kg limit, reach 850 mm vs. weldment size.

**Spine skills closed.**
- `advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-both-sides` (how-to, n=3) — set C_A = C_B.
- `measurement-how-to-convert-an-amount-with-compound-units` (how-to, n=21) — dollars/year to dollars/hour, kW x $/kWh.
- `advanced-numbers-how-to-find-the-percent-of-a-number` (how-to, n=90) — 30% load, 25% tend share, margin %.
n=3 skills, within the n<=2 preference's spirit (not strictly thin).

**Data feasibility — grade MEDIUM-HIGH (factor ~0.8).** HIGH for the four fetched inputs (BLS wage, BLS electricity, UR5e datasheet, IFR context: 542,000 robots installed in 2024, 4,664,000 in operation). The cell price, 25% tend share, 5-year life and 1.30 load are disclosed assumptions (UNVERIFIED). Students can reproduce wage and electricity themselves from the BLS API/tables.

---

### C2 — The Technician Track   ·   rank 2   ·   tier T3

**Protagonist.** Fictional: Dani Okafor, a high-school senior in a manufacturing town deciding after graduation. (Constructed, clearly disclosed; no real person.)

**Binary dilemma.**
- **A — Start welding now** (BLS mean $56,760/yr from year 0).
- **B — Two-year mechatronics associate programme** (assumed $8,000/yr all-in cost, no earnings for 2 years), then an electro-mechanical / mechatronics technician job at BLS mean **$76,420/yr** — the robotics-cell maintenance job from the domain's `careers[]`.

**Primary metric.** Cumulative pre-tax earnings net of programme cost after N years.

**Computed (Python).** A(N) = 56,760 N. B(N) = 76,420 (N − 2) − 16,000.

| N (years) | A | B | Winner, margin |
|---|---|---|---|
| 7 | $397,320 | $366,100 | A, 8.5% |
| **8** | **$454,080** | **$442,520** | **A, 2.6%** |
| 9 | $510,840 | $518,940 | B, 1.6% |
| **10** | **$567,600** | **$595,360** | **B, 4.9%** |

**Break-even = (2 x 76,420 + 16,000)/(76,420 − 56,760) = 8.59 years.** Both win: A for horizons under ~8.6 y, B after. The wage premium is 34.6%. Counterweight that is also real data: BLS employment is 416,210 welders vs 15,520 mechatronics technicians (ratio 26.8 : 1), so B's openings are scarcer — an honest reason to prefer A even past the break-even.

**Spine skills closed.**
- `statistics-and-probability-how-to-solve-a-system-of-linear-equations` (how-to, n=6) — solve A(N) = B(N).
- `statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data` (how-to, n=11).
- `advanced-numbers-how-to-find-the-percent-of-a-number` (n=90).
No thin skill; robotics link is occupational, weaker on geometry (state plainly).

**Data feasibility — HIGH (factor 1.0).** Wages and employment fetched live from BLS (series IDs above). Programme cost is the one disclosed assumption; community-college tuition tables are public but not fetched (UNVERIFIED).

---

### C3 — Three of Six   ·   rank 3   ·   tier T4

**Protagonist.** Fictional: Marcus Hale, plant engineer at a regional food-equipment maker (constructed).

**Binary dilemma.** Budget covers automating exactly 3 of 6 manual stations (two welding stations W1, W3 and palletizing P1, P2; plus W2 and P3 that are not worth it). Option **X**: automate {W1, P1, P2}. Option **Y**: automate {W1, P1, W3} to concentrate on one welding integrator.

**Primary metric.** Annual net saving = loaded labour cost removed x (1 − 0.25 tending) − annual robot cost, summed over the three stations.

**Computed (Python).** Wage rates from BLS: welders $56,760, material movers $42,260; load 1.30; 2,080 h. Station hours and annual robot cost are **constructed** (W1 1,500 h/$30k, W2 900 h/$30k, W3 1,200 h/$30k, P1 2,000 h/$26k, P2 1,500 h/$26k, P3 800 h/$26k).
- Net per station: W1 $9,909; W2 −$6,054; W3 $1,928; P1 $13,619; P2 $3,714; P3 −$10,152.
- All C(6,3) = **20** packages evaluated: best X = $27,242; second Y = $25,456; **margin 7.0%** (X ahead).
- Flip: if P2 runs ~1,410 h (−6%) instead of 1,500, Y wins; if W3 runs ~1,267 h (+5.6%), Y wins. Both options genuinely win under defensible hour forecasts.

**Spine skills closed.**
- `statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination` (how-to, n=2, **thin**) — C(6,3) = 20 packages.
- `measurement-how-to-convert-an-amount-with-compound-units` (n=21), `advanced-numbers-how-to-find-the-percent-of-a-number` (n=90).
Claims 3 skills, well under the 15-skill inflation flag.

**Data feasibility — MEDIUM (factor 0.6).** Wages live from BLS (fetched). Station hours and robot cost are constructed and must be disclosed; the BLS occupation codes for other station types (inspection, assembly) were attempted and **returned no series** with my guessed IDs, so only welders and material movers are verified. IFR context (542,000 installs in 2024) is verified.

---

## Considered and dropped (honest negative results)

- **Perseverance drive-length strategy.** Fetched the NASA traverse (558 segments, 46,027.5 m). Drive-length classes: >=100 m (n=183, mean 187.5 m) vs 50-100 m (n=84, mean 73.8 m). Meters-per-sol favours the long class by 2.5x; an expected-progress model only ties if the long drive fails ~43% of the time (solving 187.5(1−p)/(1+p) = 73.8), which no real data supports. Fails the "no dominance" rule. Elevation gain did not explain drive speed either (correlation −0.07). The dataset is excellent for a descriptive/box-plot case (quartiles 15.4 / 44.7 / 135.3 m, 6 outliers above the 315 m fence) but not for a balanced binary; kept as a possible reuse for a statistics-flavoured case.
- **FIRST alliance selection** — Statbotics API returned HTTP 500; UNVERIFIED, dropped.
- **UR5e fence vs speed layout** — datasheet does not carry fence or collaborative-speed data; the model would be invented.
