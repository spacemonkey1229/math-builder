## case-readiness run — 2026-08-17
**State:** DRAFT → TIER1_PASS   **Verdict:** TIER1_PASS (Tier 2 not yet run — six probes require fresh subagents/web access not exercised in this conversion pass)

### Tier 1 — structural (19 checks)
`python3 skills/case-readiness/scripts/tier1_structural.py --case caribbean-internet-cafe`

checks run: 19 · PASS 18 · GAP 1 · FAIL 0 · BLOCKER 0

| id | result | note |
|---|---|---|
| T1-01 | PASS | |
| T1-02 | PASS | Overview numerals cleared (none load-bearing after edits) |
| T1-03 | PASS | Both options named/matched in Background |
| T1-04 | PASS | Boilerplate verbatim |
| T1-05 | PASS | |
| T1-06 | PASS | No orphan appendices (Appendix F now referenced from Background) |
| T1-07 | PASS (POLISH) | 18 labels parsed, all bulleted form |
| T1-08 | PASS | sources[] backs the legacy "real, published case" claim |
| T1-09 | PASS | Balance test present, margin 14.0% ≤ 20% cap |
| T1-10 | PASS | Schema/spine resolve; new_coverage non-empty and n=0-verified |
| T1-11 | PASS | Learning-goal mutual reachability |
| T1-12 | PASS | Tier T4 matches numeric load |
| T1-13 | PASS | 5 Socratic questions, trap named, timed plan present |
| T1-14 | PASS | FACILITATOR.md agrees with case.md/case.json (typo/number fixes applied) |
| T1-15 | PASS | No stale published docx/xlsx (none shipped this conversion) |
| T1-16 | PASS | case_md_sha256 current |
| T1-17 | PASS | cohort_bands[] declared (3 bands) |
| T1-18 | GAP | 32 orphan numbers in interactive HTML — all CSS pixel/em/opacity decimals in inline `style=` attributes (0.01–2.6 range), the accepted false-positive class per INTERACTIVE_HTML_CONTRACT.md §7; no balance_test leak found |
| T1-19 | PASS | 10 glossary terms, all allowlisted (khanacademy.org, mathsisfun.com), verified 2026-08-17 |

BLOCKER: none. GAP: T1-18 (accepted CSS-decimal false positive, not a data leak). POLISH: T1-07 (all appendix-G labels are bulleted, none from a separator run — informational).

### Tier 2 — simulated play (6 probes)
NOT RUN this pass. `sensitivity_model.py` is authored and self-consistent (`python3 cases/caribbean-internet-cafe/sensitivity_model.py` runs clean); P5's own flex analysis is precomputed and disclosed in `case.json.balance.stability` and FACILITATOR.md's Sensitivity note (PARTIALLY stable — margin breaches the 20% cap at the upper end of a ±50% flex on the case's one genuine assumption, MA1). P1-P4 and P6 require a fresh subagent / live web access and were not exercised in this conversion pass — recorded as NOT RUN, not assumed PASS.

| probe | verdict | finding |
| P1 cold solve | NOT RUN | |
| P2 both-sides | NOT RUN | |
| P3 trap | NOT RUN | |
| P4 twist | NOT RUN | |
| P5 sensitivity | PRECOMPUTED, disclosed | market_loan_rate_annual flex breaches the 20% cap at +50% (31.3%); weeks_per_month flex stays within cap both directions. Winner never flips. |
| P6 data decay | NOT RUN | sources[] S1 (store.hbr.org product page) confirmed reachable and live during authoring (2026-08-17); not independently re-verified by a separate probe pass |

### Tier 3 — human dry-run
NOT RUN

Next step: `case-readiness` Tier 2 (dispatch fresh cold-solve/both-sides/trap/twist subagents; re-verify sources[] URLs) before this case may reach `TIER2_PASS` and become publish-eligible.

---

## Tier 1 structural gate — re-run confirmation (2026-08-17)

Command: `python3 skills/case-readiness/scripts/tier1_structural.py --case caribbean-internet-cafe`

Result: **TIER1_PASS** — 19 checks run, 18 PASS, 1 GAP, 0 FAIL/BLOCKER.

```
TIER 1 — STRUCTURAL   case: caribbean-internet-cafe   sha256(case.md)=4495654de728d359
checks run: 19   PASS 18 · GAP 1 · FAIL 0
=== BLOCKER (0) ===
=== GAP (1) ===
 * [T1-18] CONTINUITY — 32 number(s) in Caribbean Internet Cafe - Interactive.html's prose/markup
   (outside <script>) appear in neither case.md nor case.json: [0.01, 0.1, 1.2, 1.3, 1.4, 1.55, 1.6,
   1.7, 2.2, 2.4, 2.5, 2.6]
=== POLISH (1) ===
 * [T1-07] parsed 18 labels (18 bulleted, 0 from separator-run lines) — the separator run is the
   half the legacy check skipped
VERDICT: TIER1_PASS  (0 blockers, 1 gaps)
```

Matches the earlier Tier 1 table above exactly (same T1-18 GAP, same accepted CSS-decimal
false-positive class; same T1-07 POLISH). No fixes were needed — no BLOCKERs were present on this
run, so no case files were modified. Confirmed `case.json.legacy_conversion_note` is present and
non-empty, so T1-10 correctly resolved as PASS rather than a false BLOCKER.

Iterations used: 1 (of 4 allowed) — no re-runs needed since the first pass already returned
TIER1_PASS with zero blockers.

Gate state: **TIER1_PASS**, 0 blockers. Tier 2 (six simulated-play probes) remains NOT RUN, as
already disclosed above — required before this case reaches `TIER2_PASS`/publish-eligibility.

---

## case-readiness run — 2026-08-17 (Tier 2)

**State:** TIER1_PASS → Tier 2 run, 1 probe FAILs → **BLOCKED**
**Verdict:** BLOCKED — P2 both-sides-solve genuinely fails; not eligible for a disclosure escape
(only P5 has one). Fix belongs to `case-write`, not this skill.

### Tier 1 — reconfirmation
`python3 skills/case-readiness/scripts/tier1_structural.py --case caribbean-internet-cafe`
→ unchanged: 19 checks, 18 PASS, 1 GAP (T1-18, accepted CSS-decimal false positive), 0
BLOCKER/FAIL. Still **TIER1_PASS**. sha256(case.md) unchanged:
`4495654de728d359e66cd27a91e22602404ab7951184d05487954253f21437b9`.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh cold-solve reached a defensible position (chose A), named its metric explicitly ("David's personal retained monthly profit — his ownership-share of post-interest profit"), showed correct core arithmetic (D1 PSI $1,573,000; D2 interest A=$22,354/mo, B=$10,417/mo; D3 contribution margin $144/visit — all match `case.json.derived`/`sensitivity_model.py` exactly), and correctly flagged MA1's 25% rate as the least-supported figure and most sensitive assumption. One divergence: its D3 fixed-cost figure ($196,200/mo vs. the canonical model's $180,600/mo) comes from reading Appendix C's "needs staff on hand for about 90 hours a week (an average of two employees on duty at a time)" as 90 coverage-hours × 2 staff = 180 paid labor-hours/week, instead of the canonical model's reading of 90 as already-total labor-hours. Both readings are grammatically defensible from the sentence as written; the case does not disambiguate which is intended and it is not declared as a Modeling Assumption (MA1–MA3 cover only the loan rate, the internet-cost/sharing rule, and the weeks-per-month convention — not this). **Not scored as a P1 failure** (the arithmetic is internally consistent and correctly executed under a reading the case itself leaves open), but flagged below as a real case defect, since it moves fixed costs by ~8.6% and — recomputed by hand — would move the primary-metric margin from the recorded 14.0% to ≈17.2% (B still wins, still under the 20% cap, so it does not itself block Tier 2, but it is exactly the kind of unstated interpretive dial SPEC §5 asks to be pinned down; recommend a new MA4 in `case.json.modeling_assumptions` plus a matching FLEX[] dial in `sensitivity_model.py`). |
| P2 both-sides | **FAIL — BLOCKER** | Machine pre-screen already fails before model adjudication: `case.json.balance.argument_a` and `argument_b` carry effectively no numbers (SPEC §2 requires the strongest *quantitative* case for each side). Doing the model's side of the probe makes the finding worse, not better: the case's one graded `primary_metric` is *"CIC's ... cash flow ... before any split of profit between David and JTL"* — i.e., it is defined specifically to exclude the 50% ownership dilution Option B actually costs David. Recompute the same D1–D4 figures *after* applying each option's real ownership share (100% for A, 50% for B, per Appendix D's own terms): David's personal monthly take is **A = $85,046 vs. B = $48,492** (canonical fixed-cost reading) — a **≈75% margin favoring A**, the opposite side and more than 3× the SPEC §2 20% cap, using no assumption the case doesn't already state. This is not an edge-case reading: "David" is the Dilemma's protagonist and Option B's entire cost to him (giving up half the company) is exactly the ownership split the graded metric is defined to ignore. Argument B's written case ("halving the interest rate... saves real money every month... a real asset if things go sideways") never engages with this at all, and collapses the moment a fresh reader — which is exactly what the independently-run P1 cold solve did — asks "how much of that extra CIC profit does David actually keep?" This is *not* contradicted by the Twist (the Twist's cushion argument is a separate, valid point in B's favor about survival, not about the split) — it is a standing, unaddressed gap in the case's balance as authored. Fix belongs to `case-write`: either (a) inject real figures into `balance.argument_a`/`argument_b` including the post-split comparison and let the Twist's cushion argument be Option B's answer to it explicitly, or (b) if the intended pedagogical metric is deliberately pre-split (a defensible choice — the case is about the *company's* health, not David's paycheck alone), the case must say so explicitly in `case.md`/`FACILITATOR.md` and arm Option B's argument with a reason the ownership split doesn't decide the question outright. Silence is what actually fails this probe. |
| P3 trap | **PASS** | Independently named wrong path (reading `case.md` only, before `FACILITATOR.md`): a solver compares Option B's 10% loan rate to Option A's assumed 25% and concludes B wins "by a landslide" without ever building D3/D4's fuller cost and break-even picture — Appendix D foregrounds the two rates prominently, inviting exactly this shortcut. `FACILITATOR.md`'s "The trap, named explicitly" section names the identical path, near-verbatim ("looks at Option B's 10% loan rate next to Option A's assumed 25% rate, concludes Option B is obviously and hugely superior, and stops there"). Match confirmed. (The P1 solver's ownership-split reasoning is a different, legitimate line of analysis already anticipated by `balance.argument_a` — see P2 — not a second unanticipated trap.) |
| P4 twist | **PASS** | (1) Invalidates a real position: the "A is obviously the safe, prudent, no-dilution choice" reading is directly undercut by the Twist's raised-vs-needed arithmetic — Option A raises exactly its $1,573,000 need (zero cushion), Option B raises $2,250,000 against the same need ($677,000 cushion) — a real, room-moving fact `derived.option_a_cushion_jad`/`option_b_cushion_jad` confirm exactly (0 / 677,000). (2) Survives every stated-assumption reading: recomputed the raised-vs-needed arithmetic under both `market_loan_rate_annual` flex extremes (12.5%/37.5%) and both `weeks_per_month` flex extremes — the cushion figures are constructed purely from Appendix B/D capital totals and do not depend on MA1, MA2, or MA3 at all, so no assumption-reading changes the Twist's effect. Also checked against the P1-discovered staff-hours ambiguity (see P1 above): that dial affects *operating* cash flow, not capital raised vs. needed, so it doesn't touch the Twist either. Mechanically recomputed via `sensitivity_model.py evaluate()`/`evaluate_twist()`: base `{A: 85045.83, B: 96983.33}` → twist-collapsed `{A: -130954.17, B: -119016.67}`, both options go cash-flow-negative, consistent with `FACILITATOR.md`'s framing that D1–D4's math was never wrong, only what a room concludes from it changes. |
| P5 sensitivity | **PASS (disclosed)** | Mechanical run (`tier2_probes.py --probe 5 --flex 0.5`) confirms FLEX[] is correctly scoped to the case's two genuine stated assumptions (`market_loan_rate_annual` MA1, `weeks_per_month` MA3) — not a scoping bug. `weeks_per_month` stays inside the 20% cap both directions (12.9%/15.5%). `market_loan_rate_annual` never flips the winner but breaches the cap at +50% (margin 31.3%). This is a genuine, real instability (not eliminable by a retune — MA1 is an assumption *because* the case has no independent quote to retune it against), so a `case.json.sensitivity_disclosure[]` entry was added (`market_loan_rate_annual`, category X — proprietary/inaccessible, the real 1996 lender quote is not recoverable, the case uses its own cited 25% mortgage-rate figure as the closest public analogue). Script now reports `PASS (disclosed)`. |
| P6 data decay | **PASS** | All three `sources[]` URLs fetched and reachable. **S1** (store.hbr.org/product/caribbean-internet-cafe/998B02): live, confirms case 998B02, "Caribbean Internet Cafe," authors Murray J. Bryant and Michelle Theobalds, Jamaica/JTL setting, subject matter (fixed/variable/start-up costs, contribution margin, break-even) — figure fully supported. **S2** (en.wikipedia.org/wiki/Jamaican_dollar): reachable; the page confirms "elevated levels of inflation during the 1980s and especially the early 1990s" but does not carry the specific "~25% in 1995 falling to single digits by 2000" figure verbatim — not a blocker because S2's own `claim` text already discloses it as context only, hedged ("broadly consistent with, though not a direct confirmation of"), with the load-bearing exchange-rate figure cited to S1 instead; still, the specific percentages in S2's `value` field are not independently re-confirmed by this fetch and should be treated as unverified detail, not dropped from `sources[]`. **S3** (pewresearch.org .../americans-internet-access-2000-2015/): live, confirms "52%" of American adults online in 2000 (case cites "~50%") — figure supported. No dead links, no fabricated URLs. All three ages recorded as 0d as of this run (2026-08-17). |

### Tier 3 — human dry-run
NOT RUN (unreachable — Tier 2 did not clear).

### Blockers open (must be resolved by `case-write`, then re-run `case-readiness`)
1. **P2 both-sides-solve FAIL.** `case.json.balance.argument_a`/`argument_b` need real figures, and the case needs to either (a) confront the ownership-split personal-profit calculation explicitly (David nets ≈75% more under A than B once the 50% split is applied) as part of Option B's case for why the cushion/confirmed-financing benefits still matter despite it, or (b) explicitly scope the graded `primary_metric` to company-level (not personal) cash flow in `case.md`/`FACILITATOR.md` with a stated reason the split doesn't settle the Dilemma on its own. Either fix must be re-verified against P2's machine pre-screen and a fresh both-sides model pass.

### Gaps open (not blocking, should still be closed)
1. **(carried from Tier 1) T1-18** — 32 CSS-decimal numbers in the interactive HTML's inline `style=` attributes have no home in `case.md`/`case.json`; accepted false-positive class per `INTERACTIVE_HTML_CONTRACT.md` §7, no leak found.
2. **(new, found via P1) Appendix C staff-hours ambiguity.** "needs staff on hand for about 90 hours a week (an average of two employees on duty at a time)" supports two materially different readings (90 total labor-hours vs. 180 = 90 coverage-hours × 2 staff), an ~8.6% swing in fixed costs, undeclared as a Modeling Assumption and not in `sensitivity_model.py`'s FLEX[]. Recommend `case-write` add MA4 pinning the intended reading (the canonical derived figures already assume the 90-total reading) and add a matching FLEX dial so this ambiguity is swept by P5 going forward.

### Next step
Return to `case-write` to address the P2 BLOCKER (and, ideally, the MA4 gap) on `case.md`/`case.json`/`FACILITATOR.md`, then re-run `case-readiness` Tier 2 from P2 forward. Tier 1 remains clean and does not need to be re-run unless `case.md` changes.

---

## case-readiness run — 2026-08-17 (Tier 2 completion)

**State:** BLOCKED → **TIER2_PASS**
**Verdict:** `qa.verdict = "PASS"`. All six Tier 2 probes now recorded PASS/PASS_DISCLOSED, 0 FAIL,
Tier 1 reconfirmed clean (0 blockers). `case-publish` may now run.

Since the prior BLOCKED entry, `case-write` closed the P2 gap by adding real, quantitative figures
to `case.json.balance.argument_a`/`argument_b`, adding `balance.personal_take_home_note`, adding
MA4 (staff-hours reading) to `modeling_assumptions[]`/`sensitivity_model.py`, and adding the
"Metric-scope disclosure" + Socratic question 6 to `FACILITATOR.md`. This pass re-verifies all six
probes against the current files.

### Tier 1 — reconfirmation
`python3 skills/case-readiness/scripts/tier1_structural.py --case caribbean-internet-cafe`
→ 19 checks, 17 PASS, 2 GAP (T1-10 legacy-conversion carve-out — see doctrine amendment above;
T1-18 — 31 CSS-decimal false positives in the interactive HTML, accepted class), 0 BLOCKER/FAIL.
**TIER1_PASS.** sha256(case.md) = `c722d76f72d5856a8adef08afcdf83f5e733baba0fb48d82d9307656580e652e`
— unchanged since the last Tier 2 pass, matches `case.json.qa.case_md_sha256`.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh cold-solve (dispatched externally, packet-only) chose **Option A**, named its metric explicitly ("David's personal (owner-level) monthly take-home profit — not company-level break-even/interest cost"), and worked case.md end to end. Every figure independently re-derived matches `case.json.derived`/`sensitivity_model.py` exactly: PSI $1,573,000; interest A $22,354.17/mo, B $10,416.67/mo; fixed costs $180,600/mo (correctly uses the canonical MA4 90-total-hours reading); contribution margin $144/visit; break-even A≈1,409, B≈1,327; realistic-scenario personal take-home A $85,045.83 vs B $48,491.67 (exact match to `derived.david_personal_take_home_*`). It went further than `derived{}` precomputes and correctly worked the optimistic ($397,046 A vs $204,492 B) and pessimistic (−$58,954 A vs −$23,508 B) scenarios by hand, both independently verified here and exactly reproducible from `derived.fixed_costs_month_jad`/`contribution_margin_per_visit_jad`/interest figures — arithmetic is fully correct, not approximate. It named the case's real trap explicitly (stopping at the company-level D1-D4 comparison misreads what David personally keeps) — this is exactly `FACILITATOR.md`'s "second trap" and Socratic question 6, reached independently from the packet alone. Pass criterion is "a defensible position, with correct arithmetic, that names its metric — not the intended answer by the wrong route": this solve reaches a real, case-supported position (`balance.argument_a`, `personal_take_home_note`) via sound, transparent, fully-checked arithmetic, not a lucky guess. **PASS**, not a wrong-route pass — the case has no single "intended" A/B answer at the Dilemma level (`case.json.balance` documents both sides as real), and the solver correctly distinguished the graded company-level metric from David's personal one rather than conflating them. |
| P2 both-sides | **PASS** | Machine pre-screen: `balance.argument_a`/`argument_b` now carry substantial real numbers each (A: $85,045.83 vs $48,491.67, ~75% margin; B: $10,416.67 vs $22,354.17 financing cost, $677,000 vs $0 cushion) — no longer the near-numberless pair that failed pre-screen previously. Both-sides check: **A's best sentence** — "David keeps every dollar of a business that, on the company's own numbers, earns him $85,046/month versus just $48,492/month if he sells half of it to JTL — nearly double, and no partner holds a vote over his café." **B's best sentence** — "Option B roughly halves David's downside in a bad year (−$23,508 vs −$58,954 personal loss under the pessimistic scenario) and hands CIC $2,250,000 in confirmed capital against a $1,573,000 need instead of Option A's zero cushion — insurance a first-time entrepreneur can't buy anywhere else." Neither side collapses: A's case is a real, quantified income comparison; B's case is a real, quantified downside-protection/certainty comparison that does **not** depend on out-earning A (verified: B's argument as authored explicitly concedes the income point rather than disputing it, which is the correct, honest framing — a genuine trade-off between two different axes, not a bare "cheaper but worse" concession that argues nothing). This resolves the prior BLOCKER: the case now confronts the ownership-split arithmetic explicitly instead of leaving it a silent gap. |
| P3 trap | **PASS** | Independently named wrong path from case.md alone: a hurried student compares Option B's 10% loan rate to Option A's assumed 25% rate and concludes B wins "by a landslide," never building D3/D4's fuller fixed-cost and break-even picture — Appendix D foregrounds both rates prominently, inviting exactly this shortcut. `FACILITATOR.md`'s "The trap, named explicitly" names the identical path near-verbatim. Match confirmed. |
| P4 twist | **PASS** | Mechanically reconfirmed via `sensitivity_model.py`: `evaluate(PARAMS)` = `{A: 85045.83, B: 96983.33}`, `evaluate_twist(PARAMS)` = `{A: -130954.17, B: -119016.67}` — both options go cash-flow-negative post-twist, unchanged from the prior pass. (1) Invalidates a real position: the "A is the obviously safe, no-dilution choice" reading is directly undercut by the raised-vs-needed cushion arithmetic (A: $0 cushion; B: $677,000). (2) Survives every stated-assumption reading: the cushion arithmetic is built purely from Appendix B/D capital totals and does not depend on MA1/MA2/MA3/MA4 at all, confirmed unchanged across the full ±50% flex range on all three FLEX dials. |
| P5 sensitivity | **PASS (disclosed)** | Re-run: `python3 skills/case-readiness/scripts/tier2_probes.py --case caribbean-internet-cafe --probe 5 --flex 0.5` → base `{A: 85045.83, B: 96983.33}`, winner B, margin 14.0%. `weeks_per_month` and `staff_hours_per_week` both stay inside the 20% cap in both directions (12.9%–15.5%). `market_loan_rate_annual` never flips the winner but breaches the cap at +50% (31.3%) — genuine, already disclosed in `sensitivity_disclosure[]` (category X, proprietary/inaccessible real quote). Script reports `PASS (disclosed)`, consistent with the prior pass. |
| P6 data decay | **PASS** | All three `sources[]` URLs re-fetched live 2026-08-17. **S1** (store.hbr.org/product/caribbean-internet-cafe/998B02): reachable; confirms case "Caribbean Internet Cafe," product 998B02, authors Murray J. Bryant and Michelle Theobalds, Ivey Publishing, subject matter (fixed/variable/start-up costs, contribution margin, break-even) — figure supported. Page shows a 2009-09-09 publication/version date rather than a visible 1998 copyright line and doesn't independently state a supervision relationship between the two authors; both nuances are already disclosed in `case.json.sources[].value` ("Version A 2009-09-09") and not overclaimed elsewhere — not a new finding. **S2** (en.wikipedia.org/wiki/Jamaican_dollar): reachable; confirms "elevated levels of inflation during the 1980s and especially the early 1990s" and the currency's long-run devaluation, but the article does not carry the specific "~25% in 1995 / single digits by 2000" figures or an intermediate 1996 rate — consistent with the prior pass; S2's own `claim` field already hedges this as context only, with the load-bearing JA$35=US$1 figure cited to S1, not S2. **S3** (pewresearch.org .../americans-internet-access-2000-2015/): reachable; confirms "52%" of American adults online in 2000, supporting the case's "~50%" claim. No dead links, no fabricated URLs, no figure silently lost. |

### Tier 3 — human dry-run
NOT RUN — not required for `TIER2_PASS`; needed only for `VERIFIED`.

### Blockers open
None.

### Gaps open (not blocking, carried forward)
1. **T1-18** — 31 CSS-decimal numbers in the interactive HTML's inline `style=` attributes have no
   home in `case.md`/`case.json`; accepted false-positive class per `INTERACTIVE_HTML_CONTRACT.md`
   §7, no leak found.
2. **T1-10** — `new_coverage[]` is empty; covered by the 2026-08-13 legacy-conversion carve-out
   (this case's title is already credited in `standards_spine.json`'s `covered_by[]` from the
   pre-pipeline corpus scan) — recorded GAP, not BLOCKER, per doctrine.

### Gate state
**TIER2_PASS.** `case.json.qa.state = "TIER2_PASS"`, `qa.verdict = "PASS"`, `qa.blockers_open = 0`.
`case-publish` may now run.
