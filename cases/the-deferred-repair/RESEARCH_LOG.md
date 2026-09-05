# Research Log — The Deferred Repair

Stage 3 (`case-research`) run on `cases/the-deferred-repair/`. 11 `{{NEEDS_SOURCE}}` placeholders
enumerated. Worked in load-bearing order: Appendix B (flagged HIGHEST priority at concept
approval, T1-08) first, then Appendix A, then Appendix C.

## Appendix B — the core sourcing risk (worked first)

### P04/P05/P06 — Year 1 / Year 2 / Year 3 conditional coolant-failure probability

**Searched:**
- "probability engine failure if coolant flush skipped statistics study"
- "RepairPal CarMD annual vehicle health index coolant system failure rate study"
- "overheating engine failure caused by lack of maintenance percentage AAA study"
- site-restricted search on repairpal.com / carmd.com for a coolant-skip failure probability
- Direct fetch attempts on the primary pages that surfaced in search

**Fetched directly (tier 1/2 attempt):**
- `https://newsroom.aaa.com/2013/07/extreme-heat-presents-invisible-danger-to-motorists-and-vehicles/`
  — no percentage figures at all for overheating/cooling-system breakdowns; only a raw call-volume
  estimate unrelated to failure probability.
- `https://southjersey.aaa.com/news/automotive/roadside-breakdowns-preventable-proper-maintenance-finds-aaa`
  (AAA 2014 roadside data) — gives top-3 breakdown causes (battery, tires, keys) and total call
  volume, but no overheating/coolant-specific percentage and no conditional/per-year structure.
- `https://newsroom.aaa.com/2015/10/roadside-breakdowns-preventable-with-proper-maintenance-finds-aaa/`
  — real, dated, primary source. Gives "600,000 vehicles towed for transmission failure" and "29
  million total roadside calls" in 2014, but nothing about coolant/overheating, and the
  transmission figure is an unconditioned population base rate, not a probability conditional on
  skipped maintenance — used only as background context for MA2's basis, never as a cited value.
- CarMD's 2026 Vehicle Health Index (search-surfaced PDF) discusses check-engine-light repair
  categories and cost inflation; does not break out coolant-system failure rates or any
  skip-conditional schedule.
- RepairPal site search for "coolant flush skipped probability engine failure" returned only
  cost-estimator and symptom pages — no probability/failure-rate content of any kind.

**Rejected (tier 4, not usable for a load-bearing figure):**
- machinerylubrication.com, fleetmaintenance.com, cleverdude.com and similar blog/trade content
  surfaced by initial web search repeated numbers like "71% of fleet engine failures," "50% of
  engine failures," "25% of engine damage," "15% of vehicles have cooling issues" — none of these
  is dated to a specific study with public methodology, several are clearly heavy-truck/fleet
  context rather than passenger cars, and a direct fetch attempt on cleverdude.com failed
  (connection reset) confirming its unreliability as a citable primary source. These are
  disqualified per SPEC §5 / the skill's tier-4 rule: undated, no stated methodology, several
  contradict each other in scale (50% vs 71% vs 25%), classic sign of recycled unsourced SEO
  content, not a real study.
- Car Care Council's "26% of vehicles had low/leaky/dirty coolant" figure (from a 2017 community
  inspection event, surfaced via search) could not be independently verified: both
  `media.carcare.org` and `brakeandfrontend.com` returned HTTP 403 on direct fetch, so per the
  skill's rule ("never cite a URL you did not fetch") this figure is **not** used anywhere in the
  case, sourced or as assumption basis, despite search summaries repeating it.

**Outcome:** NOT FOUND, genuinely — this is not a "hard to find" figure, it does not exist as a
publishable dataset. No tier-1 (manufacturer/regulator/statistical agency), tier-2 (trade
association/industry database), or tier-3 (reputable journalism citing a named tier-1 source)
document publishes a per-year or conditional probability of coolant-system failure following a
skipped flush, for passenger vehicles, at any confidence grade. **Exit chosen: Modeling Assumption
(MA1)**, value 9% / 13% / 20%, stated openly with a sensitivity note — see `case.md`'s Modeling
Assumptions block and `case.json.modeling_assumptions[0]`. Redesign (Exit 2) was considered and
rejected: the entire dilemma (compounding probability across three years) is the reason this case
exists per the concept sheet's coverage rationale, so swapping out the constraint would gut the
case rather than repair it — an honest, sensitivity-labeled assumption is the correct exit here,
consistent with SPEC §3's T4-adjacent expectation that a flippable, defensible assumption is a
feature, not a defect, at this tier.

### P07 — Repair cost if the coolant system fails

**Searched/fetched:** RepairPal's head-gasket-replacement estimator
(`https://repairpal.com/estimator/head-gasket-replacement-cost`) — fetched directly, confirmed
range $2,538–$3,337 (labor $1,635–$2,399, parts $903–$938), page states "Estimates last updated
August 7, 2026."

**Outcome:** SOURCED as [S4], MEDIUM confidence, explicitly flagged as a **proxy**: no source
publishes a generic "coolant-related failure repair cost" figure; head-gasket replacement is the
most commonly cited real-world consequence of chronic coolant-system neglect across mechanic-trade
sources, so it stands in for "the repair cost" in Appendix B. Value used: $2,938 (range midpoint).

## Appendix A — the three shop prices

### P01/P02/P03 — coolant flush, transmission fluid service, cabin air filter costs

**Fetched directly:**
- `https://repairpal.com/estimator/coolant-change-cost` → $437–$508 (labor $151–$222, parts ~$286)
- `https://repairpal.com/estimator/transmission-fluid-change-cost` → $282–$343 (labor $131–$192,
  parts ~$152)
- `https://repairpal.com/estimator/cabin-air-filter-replacement-cost` → $91–$113 (labor $45–$66,
  parts $46–$47)

All three pages carry the same "Estimates last updated August 7, 2026" stamp. All three are tier-2
(a well-attributed cost aggregator, not a single shop's actual invoice, and not location- or
2016-sedan-specific) — graded MEDIUM rather than HIGH for that reason.

**Outcome:** SOURCED as S1 ($473), S2 ($313), S3 ($102) — range midpoints in each case.

## Appendix C — the comparison services

### P09 — Transmission 3-year cumulative failure probability if fluid service skipped

**Searched:** "probability transmission failure if fluid never changed percentage study"; AAA/CarMD
breakdown-percentage searches.

**Found:** Engine Builder Magazine, Transmission Digest, Tomorrow's Technician and similar
mechanic-trade coverage consistently describe complete transmission failure from never-changed
fluid as occurring around 80,000–120,000 miles of neglect, but none gives a percentage/probability
figure, and none frames it as a 3-year or annual rate. The AAA 2015 press release's "600,000
transmission tows out of 29 million calls" (~2%) is a real, dated figure but is an unconditioned
population base rate across all vehicles (regardless of maintenance history) — using it directly
as "the" answer to a maintenance-conditional question would misrepresent it, so it was used only
as directional context in MA2's basis, not cited as the value itself.

**Outcome:** NOT FOUND as a directly citable figure. **Exit chosen: Modeling Assumption (MA2)**,
value 15%, set deliberately lower than the coolant system's ~36.7% compound probability with the
80,000–120,000-mile neglect threshold as the stated rationale (a typical 3-year skip is
~30,000–36,000 miles, well short of that threshold).

### P10 — Transmission repair/replacement cost

**Fetched directly:** `https://repairpal.com/estimator/transmission-replacement-cost` → $6,166–
$6,685 (labor $1,112–$1,632, parts ~$5,053), same August 2026 update stamp.

**Outcome:** SOURCED as [S5], MEDIUM confidence, value $6,426 (range midpoint).

### P11 — Probability a skipped cabin air filter causes a billable mechanical repair

**Searched:** "does skipping cabin air filter replacement cause mechanical damage or only reduced
airflow"; filter-manufacturer and mechanic-trade sources (CARFAX, FilterBuy, Premium Guard,
Interfil).

**Found:** Universal agreement across every source that the consequences of a skipped cabin
filter are reduced airflow, uneven cooling, cabin odor, mold/bacteria growth, and (in "extreme
cases," per Premium Guard/Interfil, without quantification) added strain on the blower motor.
No source quantifies an actual billable-repair rate, and none treats this as a mechanical-failure
risk in the same category as coolant or transmission neglect.

**Outcome:** This absence of any credible mechanical-failure claim IS the finding. **Exit chosen:
Modeling Assumption (MA3)**, value ~0% / negligible, stated as such rather than forced into a
fabricated small percentage. This is deliberately the pedagogical answer for Challenge 3 (D4): the
cabin filter looks identical to the other two flagged items on the shop's estimate but carries no
comparable real risk.

### P12 — Cost of a repair attributable to a skipped cabin air filter

**Outcome: DROPPED.** Since MA3 finds no billable mechanical repair is attributable to this
service, no cost figure applies. `case.md` states this row as "N/A" rather than assigning any
dollar value (fabricated or otherwise).

## Summary table

| ID | Placeholder | Resolution | Value | Confidence |
|---|---|---|---|---|
| P01 | Coolant flush price | SOURCED (S1) | $473 | MEDIUM |
| P02 | Transmission fluid service price | SOURCED (S2) | $313 | MEDIUM |
| P03 | Cabin air filter price | SOURCED (S3) | $102 | MEDIUM |
| P04 | Coolant failure prob., Year 1 | ASSUMPTION (MA1) | 9% | n/a (assumption) |
| P05 | Coolant failure prob., Year 2 \| no Y1 fail | ASSUMPTION (MA1) | 13% | n/a (assumption) |
| P06 | Coolant failure prob., Year 3 \| no Y1-2 fail | ASSUMPTION (MA1) | 20% | n/a (assumption) |
| P07 | Coolant failure repair cost | SOURCED (S4, proxy) | $2,938 | MEDIUM |
| P09 | Transmission 3-yr failure prob. | ASSUMPTION (MA2) | 15% | n/a (assumption) |
| P10 | Transmission repair/replace cost | SOURCED (S5) | $6,426 | MEDIUM |
| P11 | Cabin filter mechanical-failure prob. | ASSUMPTION (MA3) | ~0% | n/a (assumption) |
| P12 | Cabin filter repair cost | DROPPED | N/A | — |

Sourced: 6 (S1–S5, one figure cited twice is not double counted — 5 source records, 6 placeholders
resolved by them since S1/S2/S3/S4/S5 map one-to-one except none double up). Assumption: 4
placeholders (P04, P05, P06, P09, P11) collapse into 3 Modeling Assumption records (MA1 covers
P04–P06 as one three-row schedule). Dropped: 1 (P12). Open: 0.

## Next step

Run `case-qa` on `the-deferred-repair`.
