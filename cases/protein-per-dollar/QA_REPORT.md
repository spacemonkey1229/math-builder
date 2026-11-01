# QA Report — Protein Per Dollar

## case-readiness run — 2026-10-28
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS (0 BLOCKERs; GAPs below)
sha256(case.md) = 6f40a72926508197b84818f8818727b47cdcb4639b9a54d4cc1eb6d5772ba9be

### Tier 1 — structural (24 checks, `tier1_structural.py`)
22 PASS, 0 BLOCKER, GAPs: T1-10 (new_coverage[] empty; reinforcement carve-out, the spine has no skill at n == 0 and `reinforcement_note` records adjacent skills considered), T1-16 (hash not yet recorded at first run; now recorded). T1-15, T1-18 to T1-24 are POLISH "no published/ directory yet": no interactive HTML, docx or xlsx has been built (case-publish not run). Earlier in the run Tier 1 found and the author fixed: T1-06 (Appendix F not referenced by letter), T1-14 (nine/three guide numbers not in case.json.derived), uncited S4, and Tier 2 P3 mechanical FAIL (trap wording).

### Tier 2 — simulated play
| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh solver (packet only) chose Chicken, named grams of protein per dollar, arithmetic correct for D1-D6 (23.52 vs 25.82 g/$, margin 8.92%, break-evens $2.918 / $4.339, 50/50 blend 24.67, beans 57.26). |
| P2 both-sides | PASS (soft) | Both sides defensible; Eggs is the weaker side and collapses first at "where does a number that flips the answer come from, and why bet a quarter on a reversal that has not started". Solver judged the case "moderately lopsided toward Chicken": see GAP G2. |
| P3 trap | PASS (guide amended) | Blind solver's wrong paths: (1) correct calculation read as a verdict; (2) per-100-g unit slip; (3) price-tag comparison and symmetric 9% break-evens. Guide covered (1) and (3a); forms for the unit slip and symmetric break-evens were added to FACILITATOR.md. |
| P4 twist | PASS | Adversarial reviewer verified all twist figures; found one rounding typo (25.44 → 25.45) and two wording ambiguities (simple vs harmonic mean price; the break-even yardstick), all fixed. Twist depends on MA2's floating-order rule, stated in Background and Appendix A. |
| P5 sensitivity | PASS (disclosed) | `sensitivity_model.py`. Flexing ±50%: budget never moves the margin; egg weight, egg protein, chicken protein, and the quarter's egg and chicken price ratios each flip the winner (price ratios Category F, nutrition Category X, recorded in `case.json.sensitivity_disclosure[]`). At ±5% on any nutrition value Chicken stays ahead (margins 4.1% to 13.5%). Script's printed base margin is 9.8% (gap/loser); the case's convention is gap/winner, 8.9%. |
| P6 data decay | PASS (notes) | S1, S2, S3 reachable, Aug 2024 values match (3.204, 3.952, 1.711); S1 and S2 have 224 rows, no blanks, in the window; S2 series title contains "453.6 Grams". S3 has two blank months in 2020 (unused). S4 reachable by WebFetch only (curl 403) and confirms "weighted averages of retail price"; its "not direct quotes" wording was not found, so the case claims only the former. S5 serves the Food bank article (redirect). Nine mathsisfun glossary pages load. |
| P7 accessibility | PASS (judged) | First cold read named about six unexplained terms (standing order, grant line, shelf-stable, edible yield, price risk, and a quote-vs-BLS ambiguity); fixed in Background and Challenges. Second fresh read: no blocking term; residual procurement jargon (pallet, case, flat) is not used by the math. Run on case.md because no published HTML exists: see GAP G4. |

### Tier 2 detail — P1 full solve
D1: egg 12 × 50 g × 12.56% = 75.36 g per dozen, ÷ $3.204 = 23.52 g/$; chicken 453.6 × 22.5% = 102.06 g per lb, ÷ $3.952 = 25.82 g/$. D2: 3,745 dozen and 3,036 lb per month; 282,247 vs 309,899 g per month; 846,742 vs 929,696 g per quarter; difference 82,955 g. D3: margin (25.8249 − 23.5206) ÷ 25.8249 = 8.92%; egg break-even $2.918 (−8.92%); chicken break-even $4.339 (+9.80%). D4: 50/50 = 24.67 g/$; 25/75 = 25.25; blend lies between the endpoints. D5: eggs lead 209 of 224 months; chicken leads Jun-Dec 2015, Nov 2022-Apr 2023, Jul-Aug 2024; egg range 15.6 to 62.6 g/$, chicken 21.5 to 35.2. D6: beans 97.98 g/lb ÷ $1.711 = 57.26 g/$, +31.4 g/$ and 2.22 times chicken. Metric named: grams of protein per dollar. Strongest counter-argument: eggs win 93% of months, August is a spike, 8.9% fall flips it. Most sensitive: MA3/MA4/MA5. Ambiguities found: 50/50 split meaning (clarified to dollars), rounding, edible-weight treatment of eggs but not chicken, quotes vs BLS prices (clarified).

### Tier 2 detail — P2 full solve
Eggs: 209 of 224 months; medians 42.1 vs 30.7 g/$; June 2024 eggs ahead 9.1%; the 8.9% edge is smaller than uncertainty in unverified nutrition inputs (egg weight ≥54.9 g, egg protein ≥13.79% or chicken protein ≤20.5% erases it); reversion buys more units under MA2. Chicken: 25.82 vs 23.52 g/$, +82,955 g; price range $3.946 to $4.229 vs egg swings; eggs need −8.9%, chicken +9.8%; protein density per unit of storage. Eggs collapses first (needs a number from outside the packet or a forecast).

### Tier 3 — human dry-run
NOT RUN.

## Open items
- **G1 UNVERIFIED nutrition values (MA3 to MA6):** USDA FoodData Central unreachable here (host unresolvable; API 429). Re-confirm with a registered api.data.gov key before publish; chicken FDC id also unconfirmed.
- **G2 balance:** a cold solver judged the case moderately lopsided to Chicken on the stated numbers. Margin 8.9% is inside the 20% cap; Eggs' case is history/reversion and input uncertainty. Revisit at the Tier 3 dry-run (Anchor 1 split).
- **G3 T1-10:** new_coverage[] empty under the reinforcement carve-out (spine has no n == 0 skill).
- **G4 not built:** interactive HTML (with hover+hyperlink `math_glossary` ≥8 terms and `context_glossary`), docx, xlsx, visual; P1/P7 should be re-run against the published HTML (T1-22 doctrine) after publish artifacts exist.
- **G5 minor:** S4 only partly supports its former "not a quote" wording (claim narrowed); S5 and S6 resolve to the same Wikipedia page.
