## case-readiness run — 2026-08-20

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (19 checks)

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview length OK; load-bearing numerals cleared (ages removed, "six days" reworded) |
| T1-03 | PASS | Dilemma binary, "You are Tamara Murray." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | numeral form matches |
| T1-06 | GAP | final Appendix J not referenced by letter from Background/Challenges (Challenge 1 points at it by construction — accepted, named explicitly) |
| T1-07 | PASS | all 22 final-appendix labels verbatim-match the spine (fixed: added Addition/Multiplication/Division terms and "How to multiply decimal numbers"/"How to convert between units of time" how-tos that were initially missing) |
| T1-08 | PASS | every number cited or a declared Modeling Assumption |
| T1-09 | GAP | margin 19.05% inside the 20% cap but wide — the discussion is expected to be genuinely one-sided on the primary metric alone (the ethical/robustness argument for A is what keeps the discussion live — see FACILITATOR.md) |
| T1-10 | GAP | `new_coverage[]` empty — legacy-conversion carve-out applies (`legacy_conversion_note` present); see LEARNING_GOALS.md for why this is honest, not padded |
| T1-11 | PASS | learning-goal mutual reachability clean |
| T1-12 | PASS | tier T4 matches numeric load (multi-step arithmetic + percent + ratio/proportion + a genuinely stated-and-defended assumption) |
| T1-13 | PASS | facilitator guide complete: anchor ladder (all 11 headings, correctly ordered), 5 Socratic questions (single-line, mechanically detected), trap named (two traps, in fact), Twist authored, timed 45-minute plan present, sensitivity note present |
| T1-14 | PASS | FACILITATOR.md agrees with case.md/case.json |
| T1-15 | PASS | no `published/` yet — nothing to drift |
| T1-16 | PASS | hash current: `35e2fb0f3e9ab0f0eb519262aaf69850a56a974df61c954d502ff73ffdc9565c` |
| T1-17 | PASS | 3 cohort bands declared (Full/Compressed/1:1) |
| T1-18 | PASS | no `published/` yet — MCS-37 has nothing to check |
| T1-19 | PASS | no `published/` yet — MCS-39 has nothing to check |

BLOCKER: none. GAP: T1-06, T1-09, T1-10 (all reviewed and accepted, see notes above). POLISH: T1-07 (separator-run note, informational), T1-15/18/19 (no `published/` dir yet, expected pre-publish).

**VERDICT: TIER1_PASS**

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh subagent, packet-only. Chose B, reconstructed the full 21-item, 51,650 kcal caloric inventory independently (matched case.json to the kcal), computed Option A/B days-of-coverage and the 19.0% margin exactly matching `sensitivity_model.py`, named its metric explicitly ("days-of-supply coverage subject to not violating anyone's non-negotiable physiological floor"), proposed and defended its own 10-day rationing horizon (D2) with real reasoning, built a full D3 per-person plan with percent-of-need, correctly identified MA1 (Easton's sedentary reclassification) as the most sensitive assumption, and named S18 (the FDA 2,000-kcal anchor) as the least-supported figure — all without ever reading FACILITATOR.md, case.json, or QA_REPORT.md. Reached the answer via the intended route, not by luck. |
| P2 both-sides | PASS | Machine pre-screen: both `balance.argument_a` and `balance.argument_b` are number-heavy (2,000/2,200 kcal + real SOLAS 10,000 kJ citation for A; the individual Appendix E figures + the 19% stretch for B), neither reads as a concession. Direct analysis: A's real weakest point (efficiency loss — "wastes" calories on lower-need people) is answered by the real international liferaft-ration precedent and by genuine risk-robustness against a wrong age-table estimate; B's real weakest point (trusting a population-average table for an individual) is answered by the case's own disclosed sensitivity note, which turns a potential collapse into an honest, already-anticipated caveat rather than an unaddressed hole. Neither side collapses to a bare concession at any single question. |
| P3 trap | PASS | Fresh subagent, case.md-only prediction matched FACILITATOR.md's stated "values trap" (assuming need-based = more food for the vulnerable) almost exactly. The subagent additionally flagged a more probable execution-layer trap (D4 arithmetic errors: mis-adding Option B's five figures, dividing by the wrong base for percent difference, or quietly un-excluding Appendix D's disclosed MA4 omissions) that the original guide did not name. Fixed: FACILITATOR.md's "## The trap" section now names both the values trap and this arithmetic-execution trap explicitly, closing the gap the probe found. |
| P4 twist | PASS | Two questions: (1) the Twist invalidates "either plan already has comfortably enough food" and "the two plans are basically equivalent," both real positions a room could hold. (2) Re-derivation found a real defect during modeling: a flat `total_supply += hidden_ration` addition is mathematically INVARIANT to the A-vs-B ratio (adding a constant to a shared numerator can never change the ratio of two numbers divided by different fixed denominators) — meaning the original twist mechanic would have failed the "winner AND margin both unmoved" check. Fixed: `sensitivity_model.py`'s `evaluate_twist()` now models each option's own stated philosophy (A splits the pack five ways; B earmarks it entirely to Easton, the person the Twist names as most at risk) — a real, asymmetric, and now explicitly-stated convention (added to FACILITATOR.md's Twist section, not left implicit in code only). Recomputed: base margin 19.05% → twist margin 41.44%, winner unchanged (B). Survives every defensible reading of the case's stated assumptions; the mechanic is now written down, not an unstated convention. |
| P5 sensitivity | PASS (disclosed) | `sensitivity_model.py` FLEX = [`flat_ration_kcal`, `easton_need_b_kcal`] (the two genuine case-author modeling choices; the four individually-cited USDA-table figures and the cited total supply are correctly excluded from FLEX per the "only real assumptions" scoping rule). Mechanical sweep: genuinely unstable — `flat_ration_kcal` −50% flips the winner to A; all four ±50% flexes push the margin past the 20% cap. Both unstable params have a matching `case.json.sensitivity_disclosure[]` entry (category F, 20+ char justification each). Machine verdict: `PASS (disclosed)`. |
| P6 data decay | PASS | All 21 `sources[]` URLs enumerated and worked. Directly fetched/confirmed matching: S9 (ground beef, 1,152 kcal/lb exact), S12 (butter, 102 kcal/tbsp confirming the 717 kcal/100g figure), S15 (corn, 344 kcal/15oz can exact). Two real defects found and fixed: **S17** (the single most load-bearing source) — the original URL now 302-redirects to a rebuilt health.gov page that no longer shows the table inline, only a PDF link; re-pointed to the actual PDF, whose reachability was confirmed (too large to re-fetch page-by-page in-session, but the identical table was already fully read from a stable secondary mirror during original research). **S19** — the original URL resolves but its fetchable content cuts off before the actual ration figure; re-pointed to a page that explicitly states the 10,000 kJ liferaft figure this case uses. Several MEDIUM-confidence food-calorie sources (myfooddata.com, mayoclinic.org) 403'd to automated fetch on this run — bot-blocked, not confirmed dead; same treatment as Family Trip's precedent (long-stable, well-known domains, values not contradicted anywhere found). No dead link carries a load-bearing figure with no fix or explanation. |

### Tier 3 — human dry-run

NOT RUN. This case has not been published; Tier 3 requires a real cohort.

---

## case.json.qa (written by this run)

```json
{"state": "TIER2_PASS", "verdict": "PASS", "run_on": "2026-08-20", "blockers_open": 0, "gaps_open": 3,
 "tier2": {"P1": "PASS", "P2": "PASS", "P3": "PASS", "P4": "PASS", "P5": "PASS_DISCLOSED", "P6": "PASS"},
 "tier3_runs": [], "case_md_sha256": "35e2fb0f3e9ab0f0eb519262aaf69850a56a974df61c954d502ff73ffdc9565c"}
```

**Next step:** `case-publish` may run on `food-rationing`. Per this conversion's instructions, stopping
here — TIER2_PASS reached, case-publish intentionally NOT run.
