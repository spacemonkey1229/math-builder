# Concept sheet — Formal Logic, Vectors, Matrices, Number-Theory branch

Generated 2026-08-23, revised 2026-08-24, per `skills/case-brainstorm/SKILL.md`. Target
selection: user asked for a batch closing **number-theory** branch starvation (only 4 feeding
domains, only 4 corpus cases — `domain_starved: true`, `case_starved: true` in
`readmodel/domain_coverage.json`) plus the three `gap_queue.json` groups **Formal Logic** (8/8
thin, 7/8 genuinely zero), **Vectors** (7/7 thin, n=1 on every skill), and **Matrices** (7/7
thin, n=1 on every skill; now n=2 with the addition of `discrete-mathematics-set` etc. from
Grant Reach's promotion — Matrices/Vectors/Formal-Logic are unaffected by that promotion, it
closed Set Theory only).

## Quality rubric (added 2026-08-24)

**Correction (2026-08-24, second pass):** the coverage scores below were originally hand-waved —
several unrelated concepts were all labeled "4.9" without actually running the formula, which was
misleading. Recomputed honestly: `raw` only counts skills the concept closes that sit at **n==0**
(0.6/term, 1.0/how-to); `bonus` is +2.0 only if every remaining gap in the group closes;
`score = (raw + bonus) × availability_factor`. C1 closes 7 skills that are genuinely at n=0 in
Discrete Mathematics/Formal Logic (5 terms + 2 how-tos = raw 5.0, +2.0 group-complete bonus = 7.0,
× 1.0 HIGH = **7.0**, not the 9.6 originally stated). Every other concept here (C2–C8) targets
skills that already sit at **n=1** — thin, not zero — so `raw = 0` for all of them and the honest
mechanical score is **0.0**, full stop. That is not a close call or a rounding difference; the
formula literally awards zero credit to a case that only thickens existing coverage or opens a new
domain, no matter how sharp the dilemma is. That's a real, structural blind spot in the formula
(see the skill's own "Calibration point" acknowledging it's bounded by group size, not quality),
and it's exactly why a second axis is needed — scoring coverage alone would silently pick the
mathematically-convenient concept over the compelling one:

**QUALITY = Q1+Q2+Q3+Q4, each 0–2, max 8:**
- **Q1 Dilemma sharpness** — genuine two-sided tension a reasonable person could defend either
  way, or a disguised single right answer?
- **Q2 Career/stakes authenticity** — is the protagonist's job and personal stake specific and
  real, or a generic "a student must decide" wrapper?
- **Q3 Engagement hook** — would a MS/HS student find the premise inherently interesting,
  independent of the math?
- **Q4 Metric integrity** — is the primary metric a real ratio that genuinely forces the
  tradeoff, or is it gameable/degenerate (one option trivially wins once you compute it)?

`7–8` excellent · `5–6` good, write as-is · `3–4` workable, needs a sharper hook or metric before
`case-write` · `0–2` do not write yet.

| # | Concept | Target | Coverage score | Quality | Data | Skills closed |
|---|---|---|---|---|---|---|
| C1 | Perimeter Protocol | Formal Logic | **7.0** | 8/8 | HIGH | 7 (7 genuinely zero) |
| C6 | The Cold Start | Matrices (AI/streaming) | **0.0** | 7/8 | HIGH | 0 new / thickens 7 |
| C7 | The Rig Split | Matrices (oil & gas) | **0.0** | 7/8 | HIGH | 0 new / thickens 7 |
| C8 | The Bot Farm | Matrices (AI/network) | **0.0** | 7/8 | HIGH | 0 new / thickens 7 |
| C2 | The Course Correction | Vectors | **0.0** | 6/8 | HIGH | 0 new / thickens 7 |
| C4 | The Fret Board | Number-theory (music-acoustics) | **0.0** | 6/8 | MEDIUM | 0 new / thickens 2 + domain diversification |
| C5 | The Plaza Bid | Number-theory (tiling-pattern-art) | **0.0** | 6/8 | MEDIUM | 0 new / thickens 2 + domain diversification |
| C3 | The Rig Budget | Matrices (gaming) | **0.0** | 5/8 | HIGH | 0 new / thickens 7 |

At `0.0` coverage the ranking among C2–C8 is carried entirely by the quality axis — which is the
point: the mechanical score cannot distinguish them at all (it isn't "low," it's literally zero
for seven of eight concepts), so pretending otherwise with invented numbers like the original
"4.9" was worse than useless — it implied a distinction that didn't exist and buried the real
signal (quality) under a fake one. C3 sits last on quality, not on coverage: "matrix
multiplications per frame" is a real engineering metric but it's a pure compute-cost count with no
accuracy/quality tradeoff on the other side — a sharp engineer picks the cheaper option with no
real argument for B once the count is computed. That's a metric-integrity problem, and it's
exactly the kind of thing the quality axis exists to catch that the coverage formula cannot see.

**Recommendation (revised 2026-08-24, C1 and C4 now drafted+researched):** C1 (Perimeter Protocol)
came back clean — 7 skills genuinely closed, real CISA KEV citation, 16.7% margin, no fabricated
numbers. Ready for `case-readiness`. **C4 (The Fret Board) came back with a real problem, not a
polish issue:** the researched Rule-of-18 deviation is ~12.5 cents against a 5-cent tolerance
assumption — roughly 2.5× over, not the close race SPEC §2 wants, and the drafting agent correctly
refused to paper over it. Needs a redesign pass (compare an earlier fret where the drift is
smaller, or reframe the primary metric around cost/deadline vs. a known-larger accuracy cost)
before it goes to `case-readiness` — do not QA it as-is.

For the next Matrices pick, prefer **C6 (The Cold Start) or C7 (The Rig Split) over C3 (The Rig
Budget)** — both score identically to C3 on coverage (all three only thicken, none close a
zero-coverage skill) but land 7/8 on quality against C3's 5/8, because C3's metric is a pure
compute-cost count with no real counter-argument once computed, while C6 and C7 both have a real,
citable cost sitting on the other side of the ledger (onboarding drop-off; rig-relocation
downtime). Between C6 and C7: **C7 (oil & gas) is the stronger pick** if the goal is corpus
diversification — this corpus has no oil & gas / energy-extraction case at all, while
media-recommendation already has two cases (Movie Producer, Cinema); C7 also uses the matrices via
a genuine system-of-equations application rather than C6's matrix-arithmetic application, which
diversifies *how* the skill is exercised, not just the setting. C8 (The Bot Farm) is the strongest
pick if the goal is instead opening `network-science` (zero existing cases, HIGH priority) — treat
it as a peer to C4 for branch-opening value, not strictly a Matrices consolation prize.

Do not write more than 2 cases per Matrices/Vectors group at once without a QA checkpoint — C1 and
C4 already surfaced one real defect between them (C4's margin), which is exactly the value of
validating the pattern before scaling it.

---

### C1 — Perimeter Protocol   ·   score 7.0   ·   quality 8/8   ·   tier T2
**Protagonist.** Marcus Webb, Security Operations Analyst at a regional hospital network's IT
security desk. Personally at stake: whichever firewall rule set he recommends tonight ships to
production before the weekend, and a wrong call either blocks a legitimate vendor integration
(clinical data feed) or lets a known-bad IP range through.

**The dilemma.** A.) Deploy Rule Set A — a broad **disjunction** rule ("block if source IP is on
the CISA KEV-linked watchlist **OR** the request hits an unpatched port") that catches more real
threats but also flags more legitimate traffic OR B.) Deploy Rule Set B — a narrow **conjunction**
rule ("block only if source IP is on the watchlist **AND** the request hits an unpatched port")
that flags far less legitimate traffic but lets more real threats slip through.

**Primary metric.** True threats blocked per false positive generated (a ratio, not a raw block
count).

**Why it's close.** Rule Set A (OR) catches every threat Rule Set B (AND) catches, plus more —
but it also flags legitimate traffic at a materially higher rate, and each false positive costs a
real analyst-minutes triage cost that a small SOC desk can't always absorb. The case forces
students to build a truth table for both compound conditions across a sampled traffic log, count
true/false positives for each rule, and confront that "catches more threats" and "is the better
rule" are not the same claim once the false-positive cost is priced in.

**Would close (7 skills, 6 how-to+term at true zero, 1 thickened):**
| id | kind | label |
|---|---|---|
| discrete-mathematics-conjunction | term | Conjunction |
| discrete-mathematics-disjunction | term | Disjunction |
| discrete-mathematics-negation | term | Negation |
| discrete-mathematics-conditional-statement | term | Conditional Statement |
| discrete-mathematics-truth-table | term | Truth Table |
| discrete-mathematics-how-to-construct-a-truth-table-for-a-compound-statement | how-to | How to construct a truth table for a compound statement |
| discrete-mathematics-how-to-determine-the-converse-inverse-and-contrapositive-of-a-conditional-statement | how-to | How to determine the converse, inverse, and contrapositive of a conditional statement (fits naturally: "if IP is unlisted, is it safe?" is the converse of the rule, and the case can show why assuming it is a trap) |

**Already-covered skills it also exercises.** `discrete-mathematics-logical-statement` (already
n=1, Key Length), `advanced-numbers-how-to-find-the-percent-of-a-number` (false-positive rate),
`statistics-and-probability-*` optionally if the traffic sample is framed as a population/sample —
keep this light so the case stays a Formal Logic case, not a stats case wearing a logic costume.

**Data feasibility: HIGH.** Named sources:
- CISA Known Exploited Vulnerabilities catalog (`cisa.gov/known-exploited-vulnerabilities-catalog`)
  — real, dated CVE list with CSV/JSON feed, already verified LIVE in `readmodel/domains.json`'s
  `cryptography-security` entry.
- A published SOC false-positive-rate benchmark (IBM/Ponemon Cost of a Data Breach report, or a
  vendor SOC report) for the "cost of a false positive" side — cited as a survey average per the
  domain note, not a specific firm's number.
- The traffic log itself is the one place this case needs a **stated scenario sample** (a
  synthetic but realistic table of N requests, each tagged watchlist-hit T/F and unpatched-port
  T/F) — there is no public per-hospital firewall log, and there should not be one. Frame this
  explicitly as a Modeling Assumption, same pattern grant-reach used for its 9,000-student
  population.
Sources I am NOT confident about: a real, citable false-positive-rate delta specifically for
AND-vs-OR firewall rule logic (this is usually vendor marketing, not measured research) — expect
this to become a stated Modeling Assumption, not a `{{NEEDS_SOURCE}}` that resolves.

**Sensitivity (SPEC §6).** Hospital/clinical framing touches infrastructure protecting patient
care — keep the case about the *access-control decision*, never about a specific breach's harm to
patients. No named real hospital, no real incident. Routine administrative security math,
comparable in register to Key Length or Codebreaker.

**Split risk.** NONE — 7 skills is the group's entire remaining footprint (8 total, 1 already
thin-covered); this is a complete-the-group case, not an inflated one.

---

### C2 — The Course Correction   ·   score 0.0   ·   quality 6/8   ·   tier T2

> **Moved to drafting 2026-09-01.** Written up as `cases/the-course-correction/`, status
> `researched`, margin_pct 16.88 (under the ~20% cap, no retune needed). Note for the concept-log
> maintainer: this writeup's "currently covered by exactly one case (Wind Triangle)" line below is
> now stale — `readmodel/standards_spine.json` shows the Vectors group at n=2 (Wind Triangle,
> Crosswind Cut) as of case-research; this case thickens it to n=3, not n=1→2 as scored here. See
> `cases/the-course-correction/RESEARCH_LOG.md`'s "Judgment call" section.

**Protagonist.** Priya Anand, research vessel Second Mate on an oceanographic survey ship.
Personally at stake: her course correction has to get the ship to a fixed rendezvous buoy before
a weather window closes, and burning extra fuel on the wrong heading eats into the cruise's actual
science budget.

**The dilemma.** A.) Steer the vector sum of the direct heading plus a hard correction for the
measured current, burning more fuel per hour but arriving on the shortest real-distance track OR
B.) Steer the uncorrected direct heading and let the current push the ship off course over the
transit, arriving later (missing the tightest part of the weather window) but burning less fuel
per hour along the way.

**Primary metric.** Fuel cost per nautical mile of net progress toward the rendezvous point (a
ratio — this is what makes "burns less fuel" not automatically win).

**Why it's close.** Option B's lower fuel burn rate is real, but the current pushes the
uncorrected heading's net vector off-target, so B's ship travels a longer effective path to reach
the same point — the case is a vector-addition/resultant-vector problem where "slower burn rate"
and "cheaper trip" are not the same claim once the actual displacement vector is computed.

**Would close (0 new skills — thickens the entire Vectors group from n=1 to n=2):** all 7 Vectors
skills (`pre-calculus-vector`, `pre-calculus-magnitude-of-a-vector`, `pre-calculus-unit-vector`,
`pre-calculus-dot-product`, and their three how-tos) — currently covered by exactly one case
(Wind Triangle) across the whole spine.

**Data feasibility: HIGH.** NOAA/NDBC publishes real, live ocean current and vessel-speed data by
buoy station (`ndbc.noaa.gov`); marine diesel fuel-burn-per-hour figures are published in vessel
spec sheets and widely available for research-vessel classes; nautical fuel pricing has public
bunker-price indices. The one soft spot: pinning the case to one *named* real vessel's exact
fuel-burn curve may not be public — use a stated, sourced-range spec (a named vessel class) rather
than one ship's proprietary numbers.
Sources I am NOT confident about: a real research cruise's actual rendezvous-point weather-window
constraint — this will be a stated scenario constraint, not a sourced figure, same as Wind
Triangle's own approach.

**Sensitivity (SPEC §6).** None — routine maritime operations math.

**Split risk.** NONE.

---

### C3 — The Rig Budget   ·   score 0.0   ·   quality 5/8   ·   tier T2
**Protagonist.** Dana Ruiz, Technical Artist / Rigger at a small mobile-game animation studio.
Personally at stake: the studio ships on a fixed device-performance budget, and her transform
pipeline choice for the hero character's rig has to fit inside it without the art director
reworking the model.

**The dilemma.** A.) Rig the character with a single combined transform matrix per bone (rotate,
scale, and translate composed into one 2×2-plus-offset matrix, computed once) OR B.) Rig the
character with three separate transform steps per bone (rotate, then scale, then translate,
applied in sequence every frame) — B is simpler to author and debug per-bone, A costs less compute
per frame at render time.

**Primary metric.** Matrix multiplications required per rendered frame, per rigged bone (a ratio
that scales with the character's bone count and the game's target frame rate).

**Would close (0 new skills — thickens the entire Matrices group from n=1 to n=2):** all 7
Matrices skills, currently covered by exactly one case (The Multiplier Recruit).

**Data feasibility: HIGH.** The math itself (matrix composition operation counts, 2×2 determinant
for checking a transform is invertible/non-degenerate, identity matrix as the "no transform"
baseline) needs no external citation — it's a computation the case derives directly, same pattern
as music-acoustics' interval ratios. The device-performance-budget side (target frame rate,
typical mobile GPU matrix-op budget) has real, citable published mobile game dev benchmarks
(Unity/Unreal published performance guidance, GDC talks).
Sources I am NOT confident about: a specific real studio's exact frame budget — stated scenario
constraint, same pattern as every existing constrained-budget case in this corpus.

**Sensitivity (SPEC §6).** None.

**Split risk.** NONE.

> **MOVED TO DRAFTING/RESEARCH 2026-09-01.** Written up and fully researched as
> `cases/the-rig-budget/`. Real sourced data: Unity Technologies' own published mobile-rigging
> guidance (docs.unity3d.com, Unity 5.6 Manual, fetched and confirmed directly) for the hero rig's
> bone count (below 30 for mobile) and mesh density (300-1500 polygons for mobile), and Ocean View
> Games' two published guides (gamedevcheatsheet.com/frame-budget and a dev.to Unity checklist,
> both fetched and confirmed) for the 60fps action-game frame-rate choice and the 16.6ms/frame
> budget. Note for the concept-log maintainer: this write-up's "currently covered by exactly one
> case (The Multiplier Recruit)" line is stale — `readmodel/standards_spine.json` already showed
> the Matrices group at n=2 (The Multiplier Recruit, The Skin Pack Atlas) at authoring time, so
> this case thickens it to n=3, not n=1→2 as scored here. `case.json.status = "researched"`;
> `margin_pct` = 45.0% (per-bone, per-frame), computed directly from real cited bone-count and
> mesh-density guidance — well over SPEC §2's ~20% cap. A retune was attempted across the entire
> real cited mesh-density range and only moved the margin from 45.0% to 49.0%; this is flagged as
> an open balance concern for case-readiness to adjudicate (no waiver self-granted). See
> `cases/the-rig-budget/RESEARCH_LOG.md`.

### C3 — REDESIGNED (balance retune, 2026-09-01)

**Status: REDESIGNED (balance retune, 2026-09-01) — original writeup and the "MOVED TO
DRAFTING/RESEARCH" note above are retained for historical record; do not delete.** The project
owner reviewed the 45.0% margin flagged above and explicitly declined an MCS-46-style waiver,
directing a redesign of the underlying dilemma/dataset instead of a numeric patch — the "compose
once vs. redo every time" cost model was proven algebraically incapable of dropping under SPEC
§2's ~20% cap for any realistic vertices-per-bone value (margin(V) = (V−1)/(2V) → 50% as V grows;
see `cases/the-rig-budget/RESEARCH_LOG.md`'s REDESIGN PASS section for the full proof).

The redesign kept the same protagonist (Dana Ruiz), studio (Fenwick Games), domain (game-character
rigging / mobile performance budgeting), and Matrices skill target, but replaced the specific
dilemma: instead of "cache a bone's transform once vs. never cache it" (an artificial comparison
whose real-world cost ratio is structurally lopsided), the case now compares two real, distinct,
industry-documented skin-blending techniques at a rig's genuine multi-bone blend zones (shoulder,
underarm, cape mount) — linear blend skinning ("The Direct Blend") vs. direct quaternion blending
("The Quaternion Blend"). A real, peer-reviewed graphics paper — Kavan, Collins, Žára, O'Sullivan,
"Skinning with Dual Quaternions" (SI3D 2007), fetched and read in full — reports real, measured
GPU runtimes for exactly this technique pair: 0.32 ms/frame vs. 0.39 ms/frame, a real margin of
17.9%, under SPEC §2's ~20% cap on real data, no retuning of any scenario dial required. The same
paper also supplied a real, citable mathematical explanation for *why* the cheaper technique has a
real visual defect (a weighted sum of rotation matrices need not have determinant 1 — provable by
hand, strengthening the case's own determinant deliverable rather than just asserting the defect),
and a real, documented limitation of the more expensive technique at more complex joints — a
genuine, sourced, two-sided tension neither the original design nor a simple numeric retune could
have produced. `case.json.status` remains `"researched"`; `margin_pct` = 17.9%. See
`cases/the-rig-budget/RESEARCH_LOG.md` for the full retune history, the directions tried and
rejected, and the complete source trail (S6/S7/S8).

> **MOVED TO DRAFTING/RESEARCH 2026-09-01.** Written up and fully researched as
> `cases/the-plaza-bid/`. Real sourced data: Stone & Tile Shoppe (stoneandtileshoppe.com), a live
> named retailer, for both tile lines — Daltile Color Wheel Mosaic hexagon ($6.59/sq ft listed,
> 11⅝″×10¼″ sheet) and Daltile Octagon & Dot ($9.69/sq ft, 12″×12″ sheet), same manufacturer, same
> supplier, both fetched and confirmed 2026-09-01. Real research finding that inverted this
> writeup's own initial framing: the octagon-and-square tile's manufactured sheet is a perfect
> 1-sq-ft square that divides the plaza's whole-foot dimensions with zero grid waste, while the
> hexagon's real sheet size does not — computed cut-waste is actually *higher* for the hexagon
> (10.5%) than for the octagon-and-square (9.1%), the opposite of "minimal cut waste" as
> hypothesized above. The regular hexagon still wins on total installed cost per square foot,
> driven by its real 32%-cheaper listed tile price surviving both its own higher waste and a
> stated labor premium. `case.json.status = "researched"`; `margin_pct` = 9.9%, real and modest,
> well inside SPEC §2's ~20% cap, no retune needed. See `cases/the-plaza-bid/RESEARCH_LOG.md`.

---

### C6 — The Cold Start   ·   score 0.0   ·   quality 7/8 → sharpened   ·   tier T2
**Sharpened 2026-08-24** (was generic "product analytics," now a concrete on-screen failure with
a name and a deadline).
**→ Moved to drafting 2026-09-01** — `cases/the-cold-start/`, case-write + case-research complete,
`case.json.status: "researched"`, margin_pct 4.76 (real S1/S2/S3/S4 sources; MA3's modeled 2026
dropout is the load-bearing retune — see RESEARCH_LOG.md).

**Protagonist.** Priya Shah, Recommendation Systems Engineer at a mid-size streaming service. Her
team just spent eight months and the platform's whole original-content budget on a prestige
limited series meant to be the service's next big word-of-mouth hit. It premieres Friday. Priya's
onboarding-flow choice decides whether a brand-new subscriber who signs up specifically because a
friend told them to watch it can actually **find** it in their first ten minutes on the app —
and the launch review is Thursday, with her name on the slide.

**The dilemma.** A.) Launch new users straight into recommendations built from a **small
item-similarity matrix** seeded only by what's popular overall — the premiere show, having zero
watch history of its own on day one, doesn't reliably surface at all against titles with months of
accumulated popularity, even though it's the exact reason this cohort signed up (zero onboarding
friction, but the thing they came for can get buried) OR B.) Require 10 explicit ratings before
showing any recommendation, building a real (if sparse) row of the user-item ratings matrix first —
this surfaces the premiere reliably for anyone who rates even one similar show, but a real,
measurable share of new users abandon during the rating step and never reach a recommendation, the
premiere, or anything else.

**Primary metric.** Recommendations clicked per 100 users who *started* signup — not per user who
finished it. This is the metric-integrity fix that keeps the dilemma real: scoring only completers
would make B look artificially strong, since it silently discards everyone who dropped off.

**Why it's close.** The domain's own framing is exactly the math: "a ratings table is a matrix
with holes in it, and the whole business is guessing the holes" (`readmodel/domains.json`,
`media-recommendation`). Option B's row-based personalization measurably out-clicks A's cold
popularity matrix *among users who complete it* — reliably surfacing the premiere for anyone who
gets through onboarding — but the rating-step drop-off is real and not small, and once it's priced
into a per-100-starters metric instead of a per-100-completers metric, a Hero has to confront that
Option B can lose the premiere to *more* new subscribers than Option A does, just by a different
mechanism (never reaching it at all, instead of it getting buried) — the two options come much
closer than the completer-only comparison would suggest.

**Would close (0 new skills — thickens the Matrices group from n=1/2 to n=2/3):** all 7 Matrices
skills (`pre-calculus-matrix`, `-matrix-dimension`, `-determinant`, `-identity-matrix`, and their
three how-tos), reused via matrix dimension/sparsity (how many of the matrix's cells are filled
vs. empty, per option) and a 2×2-scale worked example of matrix addition (blending the
popularity-matrix baseline with a new user's first few ratings).

**Already-covered skills it also exercises.** `statistics-and-probability-correlation`,
`-scatter-plot` (already domain signature skills) if the write-up wants a visual for the
similarity computation — keep optional so this stays a Matrices case first.

**Data feasibility: HIGH.** MovieLens (`grouplens.org/datasets/movielens`) is a real, public,
long-running dataset with genuine user-item rating sparsity figures — already flagged HIGH in the
domain's own `data_availability`. The onboarding-funnel drop-off rate is the soft spot: real
published onboarding-friction studies exist (industry UX research, e.g. Baymard Institute-style
signup-friction studies) but not one specific to "rating 10 items before first recommendation" —
expect a stated Modeling Assumption anchored to general onboarding-friction research, not a
literal transferred number.
Sources I am NOT confident about: a streaming-specific (not general SaaS) onboarding abandonment
rate — likely MEDIUM at best.

**Sensitivity (SPEC §6).** None — routine product-analytics math.

**Split risk.** NONE.

---

### C7 — The Rig Split   ·   score 0.0   ·   quality 7/8 → sharpened   ·   tier T2

> **MOVED TO DRAFTING/RESEARCH 2026-09-01.** Written up and fully researched as
> `cases/the-rig-split/`. Real sourced data: the U.S. EIA's final Drilling Productivity Report
> (Permian 1,400 bbl/day/rig, Bakken 1,747 bbl/day/rig, June 2024 cutoff — the last month EIA
> published before folding this series into STEO) and Baker Hughes' real weekly rig count by basin
> for scale grounding. Relocation downtime (14 days) is a stated Modeling Assumption anchored to a
> real, cited 1-4-week out-of-region rig-move range, as this concept's own writeup anticipated.
> `case.json.status = "researched"`; `margin_pct` = 1.02% — a genuinely razor-thin margin from real
> data, well inside SPEC §2's ~20% cap, no retune needed. See `cases/the-rig-split/RESEARCH_LOG.md`.

**Sharpened 2026-08-24** (was generic "Basin 1 / Basin 2," now two real, named U.S. shale
basins — both are separately tracked in the actual EIA Drilling Productivity Report and Baker
Hughes Rig Count, so naming them is a real grounding improvement, not embellishment).

**Protagonist.** Wade Kessler, Drilling Operations Manager for a mid-size independent operator
with rigs running in both the **Permian Basin** (West Texas — the company's original, still-active
acreage) and the **Bakken** (North Dakota — where they expanded three years ago). He has a fixed
pool of rigs under contract this quarter and a real, painful complication: the two rigs he'd move
are run by his most experienced crew — the same hands who've worked the company's original Permian
leases for a decade. His reallocation call is the one his VP will ask him to defend line-by-line
at Friday's quarterly review, in front of the people whose jobs move with the rigs.

**The dilemma.** A.) Move 2 rigs out of the company's Permian leases into the Bakken, where recent
per-rig productivity has been running higher — paying a real, citable relocation/downtime cost per
rig, and asking the crew to relocate, but shifting future production toward the more productive
basin OR B.) Hold the current allocation — no relocation downtime cost, no crew disruption, but the
Permian rigs keep producing at their currently lower barrels-per-rig-day rate for the rest of the
quarter.

**Primary metric.** Barrels produced per rig-day, blended across both basins for the remainder of
the quarter (a ratio that has to net the one-time relocation downtime against the ongoing
per-basin productivity gap — this is what keeps A from being an obvious win, and it's also the
number Wade has to be able to defend out loud on Friday).

**Why it's close.** The Bakken genuinely out-produces the Permian per rig in the case's sourced
window — that's real data from the EIA's own Drilling Productivity Report, not manufactured
tension. But moving a rig isn't instant: each relocated rig sits idle (zero production) for a real,
citable number of days during the move, and the quarter is only so long — plus Wade's own
read of his crew is that a forced relocation costs him something the spreadsheet can't
price, which is exactly the kind of "the math says X but there's a real cost outside the model"
tension SPEC §6 rewards naming honestly rather than papering over. The case is a
**system-of-equations-via-matrix** problem: given total rig-days available, the relocation-downtime
cost per moved rig, and each basin's real barrels-per-rig-day rate, solve for the blended output
under each option — students set it up as a small linear system and solve it with matrix methods
(this is a direct, non-contrived fit for
`pre-calculus-how-to-solve-a-system-of-equations-using-a-matrix`, not a case bending itself around
the skill).

**Would close (0 new skills — thickens the Matrices group; also a first case for the
`mining-minerals`-adjacent energy-extraction space this corpus has never touched from the oil &
gas side, only nuclear/mining):** all 7 Matrices skills, same as C6, via a genuine
system-of-equations application rather than C6's matrix-arithmetic application — the two concepts
exercise the group differently, which matters if both eventually get written (see Recommendation).

**Data feasibility: HIGH.** The **Baker Hughes Rig Count** (`rigcount.bakerhughes.com`) is a real,
famous, weekly-published public dataset of active drilling rigs by basin — exactly the kind of
named, verifiable, government/industry-standard source `case-research` needs. The U.S. EIA's
**Drilling Productivity Report** (`eia.gov/petroleum/drilling`) separately publishes real,
per-basin barrels-of-oil-per-rig productivity figures, updated monthly. Both are HIGH-confidence,
named, and already known to exist (not a guess).
Sources I am NOT confident about: an exact per-rig relocation-downtime figure (days idle during a
physical rig move) — this is proprietary operator data in reality; expect a stated Modeling
Assumption anchored to general industry commentary on rig-move logistics, not a hard citation.

**Sensitivity (SPEC §6).** None — routine commercial operations math, no environmental-harm or
safety framing (keep it that way: this is a resource-allocation case, not a drilling-safety case).

**Split risk.** NONE.

---

### C8 — The Bot Farm   ·   score 0.0   ·   quality 7/8 → sharpened   ·   tier T2
**Sharpened 2026-08-24** (was a generic weekend review, now tied to a specific traffic spike that
raises the cost of being wrong in both directions at once).

> **MOVED TO DRAFTING/RESEARCH 2026-09-01.** Written up and fully researched as
> `cases/the-bot-farm/`. Uses only 3 of the Matrices group's 7 skills (matrix, matrix-dimension,
> how-to-add-and-multiply-matrices), not all 7 — a disclosed scoping choice, see
> `case.json.reinforcement_note`. Real sourced data: Varol et al. 2017 ("Online Human-Bot
> Interactions," arXiv:1703.03107 — combined-system 0.95 AUC, real FP/FN rates 0.15/0.11, and the
> real finding that connectivity features alone reach a lower standalone AUC than content/volume
> features alone); Stanford SNAP's ego-Facebook dataset (4,039 nodes, 88,234 edges, 0.6055 average
> local clustering coefficient); and X's real, current API rate-limit documentation. Per-cluster
> false-positive rates (20% / 22.5%) are stated Modeling Assumptions derived from the real 0.15
> baseline, as this concept's own writeup anticipated. `case.json.status = "researched"`;
> `margin_pct` = 13.9%, well inside SPEC §2's ~20% cap on the first construction — no retune
> needed. See `cases/the-bot-farm/RESEARCH_LOG.md`.

**Protagonist.** Aisha Bello, Fraud Analyst on a mid-size social platform's Trust & Safety team.
The platform's single biggest traffic weekend of the year starts in six hours — a major live
event that always brings a surge of both real first-time visitors and a predictable wave of
engagement-farming bots trying to ride the same trending tag. Aisha has to recommend one cluster
for suspension before the surge hits, and she only gets to act on one: the platform's abuse
tooling can suspend a cluster this size safely once per incident without a slower, human-reviewed
rollout. Get it wrong high and she suspends real accounts — some of them the exact mid-size
creators whose posts are about to carry the platform's traffic that weekend. Get it wrong low and
a live bot ring runs freely through the platform's highest-visibility hours of the year.

**The dilemma.** A.) Suspend Cluster A — a set of accounts identified by **high mutual
connectivity** in the network's adjacency matrix (they all follow/message each other densely,
classic bot-ring signature) but with only moderate posting-volume anomaly, and dense mutual
connectivity is also exactly what a real, tight-knit creator collab group looks like OR B.) Suspend
Cluster B — accounts with extreme posting-volume anomaly (each posts far more than a real person
could, especially with the surge six hours out) but lower mutual connectivity, since they mostly
target real users rather than each other.

**Primary metric.** Confirmed-bot accounts removed per real (false-positive) account wrongly
suspended — same balance-integrity shape as C1's Perimeter Protocol, applied to a graph/matrix
context instead of formal logic.

**Why it's close.** Dense mutual connectivity (Cluster A) is a textbook bot-ring signal — but
tightly-connected real friend groups also produce dense sub-blocks in a real adjacency matrix, so
Cluster A's signal is strong but not clean. Cluster B's extreme-volume signal is individually
stronger per account, but volume-anomaly detection alone is exactly the kind of rule real platforms
have had to walk back after suspending legitimate power-users. Building the adjacency matrix for
both clusters from a stated sample and computing each cluster's actual connectivity density is
what turns "which looks more suspicious" into a defensible number.

**Would close (0 new skills — thickens Matrices; also opens `network-science`, a zero-existing-
case, HIGH-authoring-priority domain per `readmodel/domains.json`, which also touches this
corpus's existing Graph Theory group — `discrete-mathematics-graph-vertices-and-edges` etc. — via
the same adjacency-matrix structure, a natural connective case between the two spine groups):**
Matrices skills via representing a small social graph as an adjacency matrix and computing
row/column sums (each account's connection count) directly from it.

**Data feasibility: HIGH.** Stanford SNAP (`snap.stanford.edu/data`) publishes real, public
social-network datasets, several specifically curated for bot/anomaly-detection research, already
flagged HIGH in the domain's own `data_availability`. Real bot-detection research (academic papers
on Twitter/X bot networks, widely published) gives real, citable connectivity-density figures for
confirmed bot rings vs. real user clusters.
Sources I am NOT confident about: an exact false-positive rate for volume-based vs.
connectivity-based bot detection specific to one platform — expect a stated Modeling Assumption
anchored to published academic bot-detection precision/recall figures rather than a platform-
specific number.

**Sensitivity (SPEC §6).** Keep this about the *detection-method tradeoff*, never about a named
real platform, named real users, or real account content — same register as Heist or Key Length,
not a harassment/moderation-harm case.

**Split risk.** NONE.

---

### C4 — The Fret Board   ·   score 0.0   ·   quality 6/8   ·   tier T1/T2
**Protagonist.** Yuki Tanaka, apprentice Luthier at a small custom-guitar workshop. Personally at
stake: her first solo fret-placement job on a client's build — get the ratios wrong and the
instrument goes out of tune the moment it's played, and a re-fret is a full week of unpaid rework.

**The dilemma.** A.) Place frets using the exact twelfth-root-of-two equal-temperament ratio,
computed to four decimal places for every fret OR B.) Place frets using a simplified whole-number
ratio approximation (the traditional "rule of 18" luthier's shortcut), faster to mark and cut but
carrying small, compounding rounding error toward the higher frets.

**Primary metric.** Cents of pitch deviation from true equal temperament at the 12th fret (a
ratio/error metric, not a total).

**Would close (0 new zero-coverage skills — thickens `basic-operations-greatest-common-factor` /
`basic-operations-factor`-family skills from n=1 to n=2, and opens `music-acoustics`, a
zero-existing-case HIGH-authoring-priority domain per `readmodel/domains.json`):** GCF/factor
skills reused from a ratio-simplification angle (simplifying string-length ratios to lowest
terms), plus this case is the vehicle for opening the domain itself — `readmodel/domain_coverage.json`
counts any case assigned to `music-acoustics` toward the `number-theory` branch's starved case
count (currently 4, needs 10+).

**Data feasibility: MEDIUM.** The twelfth-root-of-two equal-temperament math needs no citation.
The "rule of 18" traditional approximation and its known error curve are documented in published
lutherie references (Stewart-MacDonald and other lutherie-supply technical guides publish fret
scale calculators and the underlying math). The cents-of-deviation tolerance a professional luthier
actually targets is the soft spot — likely to need a stated Modeling Assumption anchored to a
published "acceptable intonation tolerance" figure rather than a single hard citation.

**Sensitivity (SPEC §6).** None.

**Split risk.** NONE — this deliberately claims few *new* spine ids; its value is domain-opening,
not skill-count, and should be evaluated as that, per the brainstorm skill's own guidance on
small-group ceilings.

---

### C5 — The Plaza Bid   ·   score 0.0   ·   quality 6/8   ·   tier T1/T2
**Protagonist.** Marcus Ibe, junior estimator at an architectural tile-design firm bidding on a
public plaza contract. Personally at stake: his waste-percentage estimate is the line the firm's
bid lives or dies on — bid too high on waste and lose the contract, too low and the firm eats the
overage cost itself.

**The dilemma.** A.) Bid the plaza in a regular hexagon tiling (tessellates with zero gaps, larger
individual tile cost, minimal cut waste) OR B.) Bid the plaza in the client's preferred
octagon-and-square combination tiling (cheaper per-tile, but every edge row requires cut pieces,
raising waste percentage).

**Primary metric.** Total installed cost per square foot, including cut-waste (a ratio that
prices out the "cheaper tile" claim once waste is counted).

**Would close (0 new zero-coverage skills — thickens GCF/interior-angle-sum-family skills, opens
`tiling-pattern-art`, a zero-existing-case HIGH-authoring-priority domain):** same branch-opening
logic as C4 — this case's real value is the fourth case in the number-theory branch's thinnest
feeding-domain set, not new spine ids.

**Data feasibility: MEDIUM.** Interior-angle-sum geometry needs no citation. Tile unit prices and
installer labor rates are NOT centrally published (flagged explicitly in the domain's own
`data_availability` note) — this case must use a named retailer's live price list captured with a
date, same approach the domain note recommends. That is a real, doable HIGH-confidence citation
for the cost leg; it just requires a live retailer lookup during `case-research`, not a government
dataset.

**Sensitivity (SPEC §6).** None.

**Split risk.** NONE.

---

## Next step

`Approve a concept, then run case-write on it.` Given the recommendation above, the suggested
order is **C1 → C4 → (C2 or C3, whichever is picked)**. Say which to write first, or approve the
whole ordered batch and each will move through `case-write` → `case-research` →
`case-readiness` in sequence.
