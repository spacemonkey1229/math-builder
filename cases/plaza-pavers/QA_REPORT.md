## case-readiness run — 2026-08-12

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (19 checks)

First run: 3 BLOCKERs (11 open `{{NEEDS_SOURCE}}` placeholders, `margin_pct` not recorded, Appendix
E orphan). All resolved after `case-research` filled every placeholder and the border-cut/appendix
references were added. **Final run: 0 BLOCKERs, 1 accepted GAP.**

| id | result | note |
|---|---|---|
| T1-01…T1-08, T1-10…T1-13, T1-15, T1-17…T1-19 | PASS | |
| T1-09 | GAP (accepted) | margin 16.07% is inside the SPEC §2 ~20% cap but wide — the discussion will lean toward Option A. Accepted: retuning further would require either an unrealistically small material premium or an unrealistically low cost basis; 16% still leaves genuine defensible-ambiguity room (Option B's historic-match argument is qualitative, not just a numbers gap — see P2 below). |
| T1-14 | PASS | continuity — FACILITATOR.md numbers all resolve in case.json.derived |
| T1-16 | PASS | hash current as of this report: see `case.json.qa.case_md_sha256` |

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | **First pass FAILED mechanically and substantively**: the packet leaked `margin_pct` and FACILITATOR.md headings (a bug in `tier2_probes.py`'s packet builder — it never stripped the `<!-- FACILITATOR ONLY -->` section; fixed in the script, verified against `tide-window` too, same pre-existing bug). After the fix, a fresh cold-solve agent working from the stripped packet alone found a **real substantive defect**: the case's original cost model priced Option A from a per-paver retail listing (~$16.40/sq ft) while Appendix D advertised a $2–$8/sq ft contractor range, and blended an undisclosed "how much of the area is cut" fraction nowhere written in case.md — a fresh solver following the document literally reached materially different numbers than the case's own claimed margin, in one run even flipping the recommendation to Option B. **Fixed**: D5 is now a single disclosed formula (`material × (1+waste) + labor`), all inputs stated in Appendix D/G, nothing else. Re-verified with two independent fresh agents after the fix: both reproduced the exact intended figures ($16.665/$19.855, A cheaper, A under target, B over) with no ambiguity reported. |
| P2 both-sides | PASS | Re-verification agent additionally proved algebraically that Option A stays cheaper than Option B across the *entire* stated Appendix D range (not just the chosen point values) — a stronger stability result than the point-estimate flex alone shows. It also surfaced a genuine, usable discussion finding not previously written up: Option A has its own qualitative vulnerability — it is literally the pattern the commission's own pre-bid materials already flagged as underpricing the historic-match criterion, so "clears the target numerically" is not a complete defense. Folded into Deep Conflict thread 2 in FACILITATOR.md. |
| P3 trap | PASS | Fresh agent (before reading the guide) independently predicted a *different* wrong path (a dropped labor multiplier) than the guide's named trap (the infinite-plane-vs-finite-border overgeneralization). On comparison, the agent judged the guide's trap more likely to catch a real room (more common misconception, more subtly buried in the text, cascades across D1/D3/D4/D5 at once) and confirmed it is specific/actionable for a facilitator. Machine pre-screen also required the trap description use an explicit "will...miss/skip/assume" construction (fixed a wording gap: "and skips" → "will...assume...and skip"). |
| P4 twist | PASS | **First pass FAILED**: `evaluate_twist()`'s curved-edge cost-growth fractions (0.015/0.03) were bare, unlabeled Python constants with no basis anywhere in case.md — undisclosed, and a fresh agent showed swapping them (an equally defensible physical reading) reverses the twist's headline "gap widens" claim. **Fixed**: promoted to MA5 in Appendix G, with a stated value, an honest "asserted, not proven" basis, and a sensitivity note naming the reversal risk explicitly; FACILITATOR.md rewritten to present the twist's direction as a challengeable assumption, not a settled fact. Re-verified: MA5's disclosed value matches the code's literal constant exactly, the script's live output matches FACILITATOR.md's claimed numbers exactly, and the guide now explicitly rewards a Hero who is skeptical of MA5 rather than treating it as derived truth. One minor non-blocking note: a student must infer "cut-labor cost" = Appendix D's single disclosed installation-labor line for the affected option (a reasonable inference, not a hidden number). |
| P5 sensitivity | PASS | Fully machine (`sensitivity_model.py`). Base margin 16.07%. First pass at 20%/12% (MA1b/MA4) broke the 20% cap under a +50% flex (21.4%); retuned to 10%/10% (SPEC §2: retune a constraint, not hide data). Final sweep of all 4 FLEX dials: margin ranges 14.8%–17.3%, Option A cheaper throughout, no flips, no cap breaks. |
| P6 data decay | PASS | All 8 cited URLs (S1–S8) were fetched live during `case-research` on 2026-08-12 (same day as this report) — see `RESEARCH_LOG.md` for what was found/rejected at each. Two URLs (Angi's interlocking-pavers-cost article) returned HTTP 403 on direct fetch and were correctly **not cited** as sources per the never-cite-an-unfetched-URL rule, even though a search-engine snippet looked useful. All 8 cited sources: reachable, values confirmed present on the page, none moved. Re-verification not re-run as a separate delegated pass since the original fetches are same-day and directly attributable in this report. |

### Tier 3 — human dry-run

NOT RUN — no real cohort available in this session. In lieu of a real classroom dry-run, Tier 2's
P1–P4 were each run through independent, genuinely fresh subagents (no access to FACILITATOR.md,
case.json, or prior context) twice: once against the case's first researched draft (which caught
two real, substantive defects) and once against the revised version (which confirmed both were
resolved). This is real adversarial verification, not a simulated stand-in for the thing Tier 3
actually tests (facilitation quality, room dynamics, timing) — **this case is not `VERIFIED`, only
`PUBLISHED`-eligible**, and should not be marked ✅ in `DOCTRINE_LEDGER.md` until a real guide files
a `RUN_REPORT.md` from an actual cohort.

### Revision history

1. **2026-08-12, case-write + case-research**: initial draft, 25 skills claimed, 11 placeholders,
   researched to 0 open placeholders, margin 13.55% (later found unreliable — see below).
2. **2026-08-12, Tier 2 pass 1**: P1/P3/P5 FAILED mechanically (packet-leak script bug, trap-wording
   regex miss, `evaluate()` dict-contract violation). Fixed the shared `tier2_probes.py` script
   (packet stripping) and this case's `sensitivity_model.py` (CONTRACT-compliant two-key return).
3. **2026-08-12, Tier 2 pass 2**: P1 cold-solve (fresh agent) found the cost model itself was not
   reproducible from the student document — undisclosed interior/border blend, wrong material
   basis. P4 found the twist's magnitude was two undisclosed Python constants. Both are real
   defects a mechanical Tier 1 pass cannot see.
4. **2026-08-12, redesign**: D5's formula fully disclosed and simplified (Appendix D); twist
   promoted to MA5; MA1b/MA4 retuned from 20%/12% to 10%/10% after the new, honest formula's base
   margin (19.1%) proved fragile under flex (21.4% at +50%). Final margin: 16.07%.
5. **2026-08-12, Tier 2 pass 3**: all 6 probes re-verified. P1/P2/P4 re-run with fresh subagents
   against the revised case; all PASS with no remaining ambiguity reported.
