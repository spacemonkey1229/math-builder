# CONCEPTS: agriculture-food v2 (Protein Per Dollar, revised after R1) - 2026-10-28

Tags: **[CONFIRMED]** fetched and parsed this session; **[DERIVED]** recomputed in python from the fetched CSVs (this session); **[ASSUMPTION]** disclosed scenario input; **[UNVERIFIED]** not fetched/confirmed.
Single concept. Supersedes C1 of `CONCEPTS_agriculture-food_2026-10-27.md`.

**Margin convention (stated once, used everywhere).** Margin = (winner's value - loser's value) / winner's value, on the primary metric. Break-even price moves are stated as a percent change of the *current* price and labeled as such.

### Protein Per Dollar   ·   tier T2   ·   domain agriculture-food

**Protagonist.** Esperanza Haldane (fictional; grep of `/cases` and repo: 0 hits for "Esperanza" and "Haldane"), purchasing coordinator for a mid-size community food pantry.
She places the pantry's standing refrigerated-protein order on a Friday in August 2024.

**Overview-level story (150-300 words in the case; no numbers).** Opens at the walk-in cooler at 6:40 a.m.: Esperanza is pulling the last flats of eggs off a shelf that was full on Monday, while a volunteer reads out the sign-in sheet - more families than last month, again. A client told her last week that her kids will only eat protein that "comes out of the fridge", not another bag of beans; the regional food bank's cold-chain agreement for this grant line says the same thing in contract language. Her phone holds two supplier quotes. One is a pallet of eggs, the other cases of chicken breast, and the egg quote came in higher than the last one. She has until the 9:00 a.m. cutoff; after that the order is locked for the quarter. She remembers last winter, when a neighbouring pantry guessed wrong and ran short of protein in week nine. Behind her a child is stacking egg cartons into a tower. She opens both quotes side by side. Ends at the instant she must pick one. (Specific sensory detail and ending are new: cooler, carton tower; not the "phone buzzes" ending.)

**Background constraints (frozen at August 2024; no later price appears here).**
- Budget: $12,000 a month for **refrigerated fresh protein**, $36,000 for the 13-week quarter [ASSUMPTION, constructed pantry]. One order, one protein, locked quantity; the supplier invoices at the going monthly market price (BLS US city average used as the stand-in) [ASSUMPTION].
- **Why dry beans are out (realistic, stated binding constraint):** this grant line is funded under the regional food bank's cold-chain agreement, which restricts it to refrigerated protein; shelf-stable protein (dry beans, canned) is bought from a separate pantry-staple fund that is already spent for the quarter. Clients have also asked for fresh protein. The case *discloses* the cost of the constraint: at August 2024 dry beans cost $1.711/lb and deliver about 57.3 g protein per dollar, 2.2 times chicken [DERIVED; bean protein per 100 g 21.6 is UNVERIFIED, see below]. Students are told beans win the pure protein-per-dollar metric and why they are not on the ballot - and the pitch must name what the constraint costs (about 31 g/$).
- As of date: all prices are BLS monthly national averages through **August 2024**, which is the latest data the Hero has. Series values stop there in the Background.
- Option labels: **Eggs** (Grade A large, by the dozen) and **Chicken** (fresh boneless breast, by the pound).

**The dilemma.**
You are Esperanza Haldane.
Do you:
A.) Spend the quarter's refrigerated-protein budget on Grade A large eggs OR
B.) Spend it on fresh boneless chicken breast.

**Why not three options (decision-shape note).** SPEC 1.4 requires binary. A mixed order was tested and rejected as a third option: at a fixed budget a mix is a weighted average of the endpoints (50/50 gives 24.67 g/$ vs 23.52 and 25.82), so it can never beat the better pure option on the primary metric - it is not "live." It is kept as a *deliverable* (see 4) so students find that out. The shape differs from the break-even-on-one-parameter pattern: here the argument is **how much of a spike to trust** (reversion vs. run length) and **what the metric leaves out**, not a single solved threshold.

**Primary metric.** Grams of protein per dollar at August 2024 prices. Eggs: 12 eggs x 50 g x 12.56 g protein/100 g = 75.36 g per dozen [large egg 50 g edible weight: 243 g / 4.86 portion, FDC portion table, v1 read; now UNVERIFIED re-confirmation]. Chicken: 453.6 g x 22.5 g/100 g = 102.06 g per lb.

**Computed [DERIVED, python from FRED CSVs fetched 2026-10-28].**
- Aug 2024: eggs $3.204/doz -> 23.52 g/$; chicken $3.952/lb -> 25.82 g/$. **Chicken wins by 8.9%** (gap/winner = 2.30 / 25.82 = 0.0892). The 9.8% in v1 was gap/loser (25.82/23.52 - 1 = 0.0980); retired.
- Break-even egg price at Aug chicken price: **$2.918/doz**, i.e. 8.9% below $3.204 (eggs must fall 8.9%). Break-even chicken price at Aug egg price: **$4.339/lb**, i.e. 9.8% above $3.952 (chicken must rise 9.8%).
- Quarter totals at Aug prices on $36,000: eggs 846,742 g, chicken 929,696 g; difference 82,955 g (about 83 kg); eggs deliver 8.9% less than chicken under the gap/winner convention (82,955 / 929,696).
- Per month on $12,000: eggs 282,247 g, chicken 309,899 g.
- 12-pack check: 12,000 / 3.204 = 3,745 dozen vs 12,000 / 3.952 = 3,036 lb.

**Both options win somewhere [DERIVED].** Months with both BLS series Jan 2006 - Aug 2024 (224 months, Background-visible): eggs win 209, chicken wins 15 (Jun-Dec 2015 = 7; Nov 2022-Apr 2023 = 6; Jul-Aug 2024 = 2). Medians: eggs 42.1 g/$, chicken 30.7 g/$. Jun 2024: eggs $2.715 -> 27.76 g/$ vs chicken $4.046 -> 25.22, eggs ahead by 9.2% (same convention: (27.76-25.22)/27.76). May 2024: 27.92 vs 24.78, eggs ahead 11.2%. Jan 2024: eggs $2.522 -> 29.88 vs chicken 24.98, eggs ahead 16.4%. So eggs were the better protein buy two months before the decision and in 93% of history. Prior two chicken-win runs lasted 7 and 6 months and then reversed.

**Why it's close / what the student must defend.**
- *For Eggs (A):* history - eggs win 93% of months; both earlier spikes (2015, 2022-23) lasted under 8 months and reversed; Aug 2024 is only the second chicken-win month; the order is price-floating, so an egg price that falls 8.9% flips the result; eggs are easy for families to cook and for kids to accept.
- *For Chicken (B):* wins today by 8.9%, with a stable price ($3.95-$4.12 over the prior 15 months); no price risk if the quarter is taken as the horizon; more grams per dollar per lb is certain. The student must decide how much weight a *spike run length* deserves against a certain 8.9%.
- Each side is defensible at August 2024; neither dominates.

**Deliverables (SPEC 1.5 section 3; each forces math).**
1. A unit-rate table: g protein per dollar for both options in Aug 2024, with the dozen/lb conversions shown (equivalent ratios).
2. Quarter and month protein totals on $12,000/month for each option, and the difference in grams (scaling a ratio to the budget).
3. The margin by the stated convention and both break-even prices expressed as percent changes of current price (percent-of).
4. A 50/50 and one other blend of the budget, showing that a blend lies between the endpoints and cannot beat the better option (weighted ratio reasoning; forces the student to see why the dilemma is binary).
5. One original visual: monthly g/$ for both options Jan 2006 - Aug 2024 with the Aug 2024 point marked, plus a line on what the beans constraint costs.
6. A paragraph on what the metric leaves out (fat, edible yield, acceptance, cold storage, price risk) and the cost of the dry-beans constraint.

**Spine skills (only those the deliverables force).**
- `measurement-how-to-find-equivalent-ratios` (n=7): deliverables 1-2 (dozen to grams, $ to budget scaling).
- `measurement-ratio` (term): deliverable 1.
- `advanced-numbers-how-to-find-the-percent-of-a-number`: deliverable 3 (margin; break-even % moves).
- **Dropped:** `statistics-and-probability-range` (no deliverable forces a range; the chart only plots it).
Labels verified in `readmodel/standards_spine.json`.

**Tier T2** (ratio, rates, a margin, two competing variables: price now vs. price risk). Wrapped in a binary dilemma.

**Twist (post-decision; the ONLY place later prices appear).** Eggs rise and chicken stays flat: Sep 2024 $3.821 (19.72 g/$) vs chicken $3.974 (25.68); Oct $3.370 (22.36) vs $4.037 (25.28); Nov $3.649 (20.65) vs $4.011 (25.45); Dec $4.146 (18.18) vs $4.104 (24.87); Jan 2025 $4.953 (15.22) vs $3.969 (25.71); **Feb 2025 $5.897** (12.78) vs $4.079 (25.02); **Mar 2025 $6.227** (12.10, window peak) vs $4.160 (24.53). Sep-Nov 2024 average egg price $3.613 (+12.8% over Aug; +23.8% over the $2.918 break-even) [DERIVED]. A pantry that picked Eggs and paid the Sep-Nov average gets 20.86 g/$ instead of the planned 23.52, 11.3% fewer grams than planned; Chicken averages $4.007/lb, 25.47 g/$, 1.3% below plan. The twist lets students revisit: did the Aug 2024 call anticipate it, and was run-length history the right evidence?

**Facilitator note (SPEC 6).** This case touches food insecurity and family hardship. Some students and their families may use pantries. Frame the Hero as a professional making a budget decision, avoid asking students to imagine specific families going without, and discuss the beans constraint as a funding rule, not a judgment on what families "should" eat.

**Data feasibility - HIGH.**
- FRED `APU0000708111` Eggs, Grade A, Large, per dozen (BLS, US city average): [CONFIRMED] CSV fetched 2026-10-28 via `https://fred.stlouisfed.org/graph/fredgraph.csv?id=APU0000708111` (data through Sep 2026).
- FRED `APU0000FF1101` Chicken breast, boneless, per lb (BLS, from Jan 2006): [CONFIRMED] same method. **Month count: Jan 2006 - Sep 2026 spans 249 months; the series has 248 observations because Oct 2025 is blank** (BLS suspended collection). Chicken-win run totals (7 + 6 + 15 = 28) over the 248 observed months; eggs win 220. Within the Background cutoff (Jan 2006 - Aug 2024) there are 224 months with 209 egg wins and 15 chicken wins.
- FRED `APU0000714233` Dry beans, any type, per lb (BLS): [CONFIRMED] fetched; Aug 2024 $1.711.
- USDA FoodData Central ids (v1 read of 171287 eggs 12.56 g/100 g; 171077 chicken breast meat only, raw 22.5 g/100 g; 173734 black beans 21.6 g/100 g): **[UNVERIFIED this session].** Re-fetch attempts on 2026-10-28 returned HTTP 429 OVER_RATE_LIMIT (DEMO_KEY, Retry-After ~68,000 s) and `fdc.nal.usda.gov` did not resolve from this sandbox (WebFetch also 429). `case-research` must re-confirm ids and values from `https://fdc.nal.usda.gov/` with a registered api.data.gov key before write-up. Note the black-bean value likely refers to raw/dry; verify the FDC id and state "dry, raw" in the appendix. The beans-win conclusion holds for any plausible value (dry beans would still be >2x).

### Fixes applied
| Reviewer finding | Change |
|---|---|
| R1a blocking: dry beans 2.27x chicken dominate | Beans excluded by a stated Background constraint (cold-chain grant line / fresh-protein request) with the cost disclosed (57.3 g/$, 2.2x) and a pitch obligation to name it. (Recomputed ratio is 2.22x at the Aug 2024 price $1.711/lb; reviewer's 2.27x used a different price.) |
| R1a: keep post-Aug-2024 prices in Twist only | Background frozen at Aug 2024; Sep 2024 - Mar 2025 prices ($5.897 Feb, $6.227 peak) appear only in the Twist. Removed from the dilemma and "why close" sections. |
| R1b: chicken-win month ranges wrong | Corrected to Jun-Dec 2015 (7), Nov 2022-Apr 2023 (6), Jul 2024-Sep 2025 (15) = 28; Background-visible runs reduced to Jul-Aug 2024 (2). 248 vs 249 explained (Oct 2025 blank). |
| R1b: FDC ids unconfirmed | Fetch attempted (API 429 rate limit; fdc site unresolvable); marked UNVERIFIED with a research instruction. |
| R1a: `range` skill not forced | Dropped. |
| Margin convention (cross-cutting) | One convention (gap / winner): 8.9% (9.8% retired as gap/loser). All margins restated. |
| R1c: facilitator note family hardship | Added per SPEC 6. |
| R1c: protagonist/collision | New name, Esperanza Haldane; no hits in repo; avoids Priya, Mara, Okafor, Raman. |
| Decision-shape variety | Mixed-order tested; rejected as a third option because it is a weighted average and cannot beat the better endpoint (SPEC 1.4 also binary). Kept as deliverable 4. Argument shifts to spike run-length vs certainty, with a floating-price order that makes the egg bet live. |
| Ending reuse | New ending: cooler, carton tower, 9:00 a.m. cutoff. |

### Still open
- FDC ids and protein values [UNVERIFIED] (rate-limited, site unresolvable here).
- 50 g large-egg edible weight (portion table) re-confirmation.
- Twist egg-recovery after Mar 2025 not stated; case-research should read the Apr 2025+ series and add if a clean as-of line is wanted.
- The "supplier invoices at monthly market price" is an [ASSUMPTION]; case must state it in Modeling Assumptions and name BLS national average as a stand-in for local quotes.
- Twist shortfall figures assume the quarter is priced at the Sep-Nov monthly average (assumption; the case states it).
- Unresolved tension for review: SPEC says binary, brief prefers richer shapes; this sheet keeps binary and enriches the argument instead.
