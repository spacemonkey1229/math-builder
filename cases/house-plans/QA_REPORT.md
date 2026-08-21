# QA Report: House Plans

## case-readiness run — 2026-08-19
**State:** TIER1_PASS → TIER2 run, 2 probes FAIL   **Verdict:** TIER2_PASS NOT reached

### Tier 1 — structural (19 checks)
Re-run this session (`tier1_structural.py --case house-plans`), sha256(case.md) =
`0b7c07604d3bd8abe5b1f636cd3c0df61ebc3450ad694d89ade6f9a1fbc79ea0` (matches `case.json.qa.case_md_sha256`,
no drift). 17 PASS · 2 GAP · 0 FAIL.

| id | result | note |
|---|---|---|
| T1-01..T1-13 | PASS | |
| T1-14 | GAP | CONTINUITY — 1 number in FACILITATOR.md (80.0) appears in neither case.md nor case.json; guide-only derived figure, not moved into `case.json.derived` |
| T1-15 | PASS | |
| T1-16 | PASS | |
| T1-17 | PASS | |
| T1-18 | GAP | CONTINUITY — 35 numbers in `House Plans - Interactive.html` prose/markup appear in neither case.md nor case.json (small decorative/UI figures) |
| T1-19 | PASS | |

**BLOCKER (0).** **GAP (2):** T1-14, T1-18 (as above). **POLISH (1):** T1-07 rendering note (non-blocking).

VERDICT: `TIER1_PASS` (0 blockers, 2 gaps) — unchanged from the prior run recorded in `case.json.qa`.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **FAIL** | A genuinely fresh subagent (no access to FACILITATOR.md/QA_REPORT.md/case.json), given only the leak-free packet, chose option A (Country Farmhouse), correctly performed D2's find-the-whole step (`495,000 / 0.90 = 550,000`), and reached the correct qualitative tier conclusions (Farmhouse affords Luxury; Ranch affords only Standard). But its D3 arithmetic was genuinely wrong in two places: Farmhouse Luxury build cost computed as `2,912 × 148.57 = $432,675.84` (correct: **$432,635.84**, a $40 multiplication error) and Ranch Standard build cost computed as `4,494 × 101.20 = $454,864.80` (correct: **$454,792.80**, a $72 error). Neither error happened to flip a tier-affordability threshold, but SKILL.md's pass bar is explicit — "reaches a defensible position **with correct arithmetic**... reaching the right answer by the wrong route is a FAIL" — and decimal multiplication is literally one of this case's own taught skills (Appendix F). Verified against the case's own numbers: `2912*148.57 = 432635.84`, `4494*101.20 = 454792.8` (Python-checked). |
| P2 both-sides | **PASS** | Argument A (Farmhouse): Luxury tier at $432,635.84, 5-amenity package ($117,200 of $117,364.16 available — Pool, Detached Shop, Putting Green, Sport Court, Outdoor Kitchen, verified as the exact maximum-value knapsack subset under that budget), total 99.97% of the $550,000 ceiling. Argument B (Ranch): Standard tier at $454,792.80, 5-amenity package ($94,420 of $95,207.20 — Pool, Landscaping, Putting Green, Custom Gate, Outdoor Kitchen, also the exact optimum), 54% more heated square footage (4,494 vs 2,912 sq ft), total 99.86% of ceiling. Neither side is a paper concession; both carry real, independently-optimized numbers. Margin: 0.11 points, far inside the SPEC §2 20% cap. |
| P3 trap | **FAIL** | FACILITATOR.md's stated trap: "A Hero treats $495,000 as the real ceiling and never finds the true $550,000 figure... Watch for a pitch that never mentions the 90% condition at all" — i.e., *ignoring* Appendix C's condition entirely. A second genuinely fresh subagent, working from the packet alone (no FACILITATOR.md), independently named a different, more specific and more plausible trap: computing the ceiling by **adding** 10% instead of **dividing** by 90% — `$495,000 × 1.10 = $544,500` instead of `$495,000 / 0.90 = $550,000`. This trap *engages* with the 90% condition (unlike the guide's trap, which assumes the student ignores it) and produces a deceptively close, plausible-looking wrong number ($544,500 vs the correct $550,000, only ~1% off) that would not visibly break anything downstream — exactly the "looks right, isn't" profile P3 is checking for. This is corroborated by the tier2_probes.py mechanical screen, which independently flagged the guide's trap text as reading "as a difficulty note, not a trap" (it doesn't describe a specific wrong action). Two independent signals converge: the guide has not anticipated the trap a fresh solver actually finds most natural. |
| P4 twist | **PASS** (with a named finding — see P5) | Both integrity questions checked against `sensitivity_model.py`: (1) the twist has a real effect — it does not change which tier either house affords, but visibly shrinks both amenity budgets, forcing a real trade-off, matching FACILITATOR.md's own description exactly (`evaluate_twist` reproduces case.json.derived's twist figures to the cent: Farmhouse build $458,593.99 [+$25,958.15], Ranch build $482,080.37 [+$27,287.57]). (2) No unstated convention is needed to apply the twist — "lumber prices jumped 6%" unambiguously multiplies build cost only, under every natural reading of Appendix C. Neither failure condition in SKILL.md's P4 criteria is met. However: mechanically recomputing the case's own `primary_metric` (total cost as % of the $550,000 ceiling) before and after the twist shows the numeric optimization "winner" flips — base: A 99.9702% > B 99.8569% (A ahead); twist: A 99.9544% < B 99.9946% (B ahead). This is real and undisclosed in `case.json.balance` or FACILITATOR.md (which frames the twist purely as an amenity-budget squeeze). It does not fail P4 on its own terms because the dilemma is explicitly a values question, not one this metric adjudicates, and no tier/position is invalidated — but see the P5 finding below, which shows this flip is itself unstable and not a real signal. |
| P5 sensitivity | **PASS**, with a caveat finding | `python3 skills/case-readiness/scripts/tier2_probes.py --case house-plans --probe 5 --flex 0.5` swept the case's one genuine `FLEX[]` dial, `twist_lumber_increase_pct` (6.0 → 3.0 / 9.0), against `evaluate()`: **no flip, margin unchanged at 0.1 pts** in both directions (script output: `flips: false` both runs). Everything else in `PARAMS` (square footages, tier prices, the 90%-loan condition, amenity costs) is given fictional-scenario data, not an author-chosen convention — flexing it would be "a different case," per the same rule Cold Chain's reference model documents, so it is correctly excluded from `FLEX[]`. **Caveat, mechanically verified but not caught by the script:** `evaluate()` never reads `twist_lumber_increase_pct` at all (it's twist-only), so this sweep is structurally inert for the case's *base* metric — there is effectively nothing left in `FLEX[]` capable of moving the pre-twist result. Manually sweeping the same ±50% range through `evaluate_twist()` instead (the only place this dial has any effect) shows the post-twist %-of-ceiling "winner" is highly unstable — it flips repeatedly across 0%–12% (A at 0-3%, B at 4-6%, A again at 7-9%+) — but the margin never exceeds ~0.11 percentage points anywhere in the range, nowhere near the SPEC §2 20% cap. This reads as noise inherent to a knapsack-optimized "% of ceiling" metric sitting right at ~99.9% utilization on both sides, not a substantive verdict change. Real, undisclosed, and not currently written into `case.json.sensitivity_note` (`null`) or the Guide Notes' "Facilitator note — sensitivity" (which says "None required"). Recommend: if this metric is ever used as more than an internal balance-tightness statistic, disclose that it is volatile near the twist; the tier/amenity/space-vs-finish conclusions the guide actually asks students to weigh are stable. |
| P6 data decay | **PASS / N/A** | `case.json.sources[]` is empty — the case cites no external figures that require decay-tracking, so the probe's worklist is correspondingly empty (nothing load-bearing to check). As a bonus check (these are not `sources[]` entries), the four Appendix E "Learn More" links were fetched live: CFPB construction-loan explainer — reachable (HTTP 200), content matches the case's description. NAHB 2024 cost-of-constructing-a-home study — reachable (HTTP 200), resolves to a versioned PDF matching the described report. Khan Academy percent-word-problem video — reachable (HTTP 200). U.S. News "How to Measure the Square Footage of a House" — **could not be verified**: timed out on every fetch attempt (WebFetch ×2, curl ×2 with different TLS/HTTP settings). Reporting this as NOT FOUND/unverifiable rather than guessing at its live status, per MCS-21 — recommend a manual check before next publish. None of these four are load-bearing (Appendix E is explicitly non-required reading), so none of this rises to a BLOCKER. |

### Tier 3 — human dry-run
NOT RUN.

---
**Result:** 2 of 6 Tier 2 probes FAIL (P1, P3). Per SKILL.md, `TIER2_PASS` requires all six probes
PASS/PASS-disclosed with zero FAIL — **not reached**. State remains `TIER1_PASS`.

**Next step:** the two FAILs point `case-write`/the guide-authoring pass at two concrete, non-cosmetic
fixes — neither applied here, per "Never fix the case":
1. **P3 trap fix** — rewrite FACILITATOR.md's "The trap" section to name the additive-percent error
   (`495,000 × 1.10` instead of `÷ 0.90`) as the primary trap to watch for, alongside or instead of
   the current "ignores the 90% condition entirely" framing.
2. **P5/P4 disclosure** — either add a `sensitivity_note` acknowledging the %-of-ceiling metric's
   volatility near the twist, or stop presenting `margin_pct`/the post-twist comparison as a
   meaningful tiebreaker at all (the case's own Guide Notes already correctly frame the real
   discussion as space-vs-finish values, not this statistic — the fix may be as simple as making
   that explicit).

P1's FAIL is a solver-execution finding (arithmetic), not a case-clarity defect — no case edit is
implied by it, though it is a useful data point on how easy it is to mis-multiply Appendix D's
decimal price table under time pressure, which is exactly the case's own D3 skill.

---

## Remediation + re-verify — 2026-08-20
**State:** TIER1_PASS → both P1/P3 FAILs remediated and re-verified   **Verdict:** `TIER2_PASS` reached

### P1 (cold-solve arithmetic) — investigated first, per instructions

Inspected Appendix D's finish-tier table in `case.md` directly for a presentation defect before
touching anything:

```
| Tier | Price / sq. ft. |
|---|---|
| Standard | $101.20 |
| Plus | $122.63 |
| Luxury | $148.57 |
```

Findings: all three rates carry exactly 2 decimal places, a consistent `$` prefix, and a clear
tier label per row — no ambiguous units, no mixed precision, no columns that could be
mis-paired (only one numeric column). Cross-checked the same table as it actually renders in
`published/House Plans - Interactive.html` (line ~325): it renders as a proper `<table>` with a
`class="num"` right-aligned numeric column, i.e. even better-aligned than the raw markdown. No
formatting defect was found — **no edit was made to case.md**, per the instruction not to force a
change if the table is genuinely fine.

To check whether this was actually solver error rather than a false negative, a second, genuinely
fresh cold-solve subagent was dispatched against the regenerated leak-free packet
(`/tmp/coldsolve-house-plans/PACKET.md`, produced by `tier2_probes.py --case house-plans`),
explicitly instructed to show every multiplication step in full, unrounded precision. Result: it
independently reproduced `2,912 × 148.57 = $432,635.84` and `4,494 × 101.20 = $454,792.80` —
**both exactly correct, zero arithmetic errors**, along with correct D1/D2/D4/D5 work and the
same qualitative conclusions as the 2026-08-19 run (Farmhouse affords Luxury, Ranch affords only
Standard). This corroborates the table-inspection finding: **the 2026-08-19 solver's $40/$72
errors were solver-execution slips, not a defect reproducible from the case itself.** P1 is now
PASS.

### P3 (trap) — fixed and re-verified, with a second finding along the way

`FACILITATOR.md`'s "The trap" section was rewritten to lead with the wrong-operation error a
fresh solver actually found most plausible on 2026-08-19 (`$495,000 × 1.10 = $544,500` instead of
`÷ 0.90`), keeping the original "ignores the 90% condition entirely" framing as a secondary,
less-likely trap.

A third, genuinely fresh subagent was then dispatched to the same packet with the standalone
trap-check prompt (case document only, no FACILITATOR.md). It converged on a *different* concrete
wrong-operation error not previously recorded: `$495,000 × 0.90 = $445,500` — misreading the
$495,000 loan as the *whole* rather than the *part*, i.e. the over-practiced "part = whole ×
percent" reflex fired on the first dollar figure next to a percent. This is a real, distinct
finding (not the ×1.10 variant, and arguably more dangerous — it produces a ceiling *below*
$495,000, which should be a red flag but often isn't checked, and it can silently make the Ranch
Estate's Standard tier unbuildable, eliminating Option B before a fair comparison happens).

`FACILITATOR.md` was updated a second time to name both wrong-operation variants (×1.10 and
×0.90) explicitly, alongside the original ignores-the-condition trap, so the guide now anticipates
every trap two independent fresh solvers have actually produced from the packet alone. P3 is now
PASS — a fresh trap-check against the case document converges on traps the guide now names.

### Tier 1 re-run

`python3 skills/case-readiness/scripts/tier1_structural.py --case house-plans` after the
`FACILITATOR.md` edits: 17 PASS · 2 GAP · 0 FAIL, same two non-blocking CONTINUITY gaps as before
(T1-14, T1-18 — guide-only/decorative numbers not moved into `case.json.derived`; T1-14's count
grew from 1 to 3 numbers as an artifact of the new trap text citing `1.10`, `0.90`×`$495,000`
components — still non-blocking). `case.md` was not touched, so `case_md_sha256` is unchanged
(`0b7c07604...`). VERDICT: `TIER1_PASS` (0 blockers, 2 gaps), unchanged.

### Result

| probe | 2026-08-19 | 2026-08-20 |
|---|---|---|
| P1 cold solve | FAIL | **PASS** — table inspected and found clean; a second fresh solver reproduced correct arithmetic exactly |
| P2 both-sides | PASS | PASS (unchanged, not re-run) |
| P3 trap | FAIL | **PASS** — guide rewritten to name both wrong-operation traps fresh solvers actually found; a third fresh trap-check converges on a guide-named trap |
| P4 twist | PASS | PASS (unchanged, not re-run) |
| P5 sensitivity | PASS | PASS (unchanged, not re-run) |
| P6 data decay | PASS/N/A | PASS/N/A (unchanged, not re-run) |

All six Tier 2 probes now PASS/PASS-disclosed with zero FAIL. `case.json.qa` updated:
`state: TIER2_PASS`, `verdict: TIER2_PASS`, `run_on: 2026-08-20`, `tier2.P1`/`tier2.P3` set to
`PASS`. The still-open, non-blocking disclosure items from the 2026-08-19 P4/P5/P6 findings
(primary_metric volatility near the twist; the one unreachable Appendix E link) remain recorded
in that entry and were not re-litigated here — they did not block `TIER2_PASS` on 2026-08-19
either, since neither breaks the SPEC §2 20% cap nor invalidates a load-bearing figure.

**Files changed:** `cases/house-plans/FACILITATOR.md` (trap section only), `cases/house-plans/case.json`
(`qa` block only). `cases/house-plans/case.md` was not modified.
