# QA Report — Firm Power

## case-readiness run — 2026-09-18
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (24 checks)
22 PASS · 2 GAP · 0 FAIL. sha256(case.md) = `b2e93121fbfb349f2c3df2a4e7285cb0c4606a1038aab8bac5fb63e9ae5015b1`

GAPs (both reviewed, neither blocking):
- **T1-10** — `new_coverage[]` empty; downgraded to GAP via the reinforcement carve-out. `case.json.reinforcement_note` records every claimed skill's `n` as of 2026-09-18 and confirms a full spine sweep found zero skills anywhere at `n==0` (same finding as `the-turbine-channel`, `wind-call`). Statistics And Probability/Data Analysis is the thinnest reachable group for this domain, and every claimed skill is forced by a named deliverable (see `LEARNING_GOALS.md`).
- **T1-13** — Twist is N/A; the justification is written out in full in `FACILITATOR.md`'s "Twist" section (advisory-only GAP, confirming a human read it).

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | A fresh subagent, given only the student packet, correctly reconstructed the missing 19:00 hour (33,086.6 MW, matching the true value), computed the real quartiles/median/range, correctly found the 6-hour peak window, correctly scaled by MA1's 3% share, correctly converted Net CONE and set up D4's equation, chose Option B, named the real primary metric, and correctly identified MA1 as its most sensitive assumption while correctly noting MA2 does not affect the balance. A clean, defensible cold solve. |
| P2 both-sides | PASS | A fresh subagent built strong, numeric, real-data-grounded defenses for both options. A's defense stands on real grounds (raw dispatchability, no accreditation-formula dependency); B's defense is the case's own intended comparison. Under pressure A's defense weakens (both cost figures are equally well-sourced to the same Lazard report, undercutting an "unverifiable formula" objection to B) but does not become indefensible — the intended tension, not a sign the case is broken. |
| P3 trap | PASS | A fresh subagent, reading only the student packet, independently named the exact trap authored in `FACILITATOR.md`: comparing solar's raw $73/MWh LCOE directly against gas's $149-$251/MWh range without adding the real $69/MWh firming charge. Matches the guide's own trap closely, including the secondary "compute the firming charge in D4 but forget to carry it into D5" variant. |
| P4 twist | N/A | `case.json.facilitator.has_twist = false`. Genuinely economic/technical tension, not an information-withholding twist — see `FACILITATOR.md`. |
| P5 sensitivity | PASS | `sensitivity_model.py` run fresh: base A=-$87,996.42, B=-$83,862.36 (cost, lower-magnitude-is-better sign convention), winner B. Flexing both declared assumptions (`ccas_share_pct`, `monthly_budget_usd`) ±50% never flips the winner — `ccas_share_pct` scales both options' totals proportionally by construction (same shape as `the-turbine-channel`'s MA2), and `monthly_budget_usd` doesn't enter `evaluate()` at all, a correct, honest no-op matching its documented scope. The case's real fragility (which point in gas peaking's cited cost range to use) is cited data, not a stated assumption, and is disclosed separately in `case.json.sensitivity_disclosure[]` per P5's own FLEX-scoping rule. |
| P6 data decay | PASS | All 4 sources (S1-S4) were fetched live on 2026-09-18, the same day as this report: CAISO's live CSV feed, Lazard's LCOE+ June 2025 PDF (read directly via page-image extraction), and CalCCA public reporting. Zero-day-old sources; no decay possible yet. |
| P7 accessibility | **FAIL (waived — see `case.json.qa.tier2.P7_waiver`)** | Mechanical pre-screen: no deliverable asks for a sketch/diagram/graph the published HTML lacks (D1's box-plot-style worked example and the icon set both count as real visuals; 2 found). Model-judged cold-read: four rounds run against genuinely fresh subagents, with two real remediation passes in between (expanding the ELCC methodology explanation, adding a concrete 3-step firming-charge payment/trigger mechanism with an insurance analogy, and expanding the community-choice-aggregator/utility-wires split). The named-gap count did not drop below the 2-concept threshold across rounds (see the waiver's full `remaining_gaps[]` list) — this case's real-world setting is genuinely dense capacity-market financial machinery that resists full de-jargoning without becoming a case about energy-market design rather than the statistics/algebra it is built to teach. Waived per MCS-49 on the same evidentiary basis as this project's Cardiology precedent. The underlying FAIL and all four cold-read transcripts are preserved, not hidden. |

### Tier 3 — human dry-run
NOT RUN. `cohort_bands[]` is declared in `case.json` per SPEC §7.4 but untested. `PUBLISHED` does not require Tier 3; `VERIFIED` does.
