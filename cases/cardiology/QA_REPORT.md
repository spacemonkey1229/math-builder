## case-readiness run — 2026-08-19
**State:** TIER1_PASS → TIER2 run (not clean)   **Verdict:** below TIER2_PASS — 2 of 6 probes FAIL

### Tier 1 — structural
Not re-run in this pass; case.json.qa already records a TIER1_PASS run (2026-08-04, re-run after
`correction_2026_08_04`'s real-data rewrite): 17/19 PASS, 2 GAP (both accepted classes — CSS/SVG
decorative decimals, clock-time labels), 0 blockers. This Tier 2 run assumes that result stands;
`case_md_sha256` below reconfirms the file has not changed since.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | A genuinely fresh subagent (no access to FACILITATOR.md/case.json), given only the leak-free packet, chose B, reproduced the arithmetic exactly (59% vs 64% survival, EF = 72.5/228.6 = 31.7%, $27,000 vs $94,000 5-yr cost), correctly named the graded metric (5-year survival rate, with cost/EF as supporting context), and correctly flagged Assumption 2 (the disclosed cost convention) as the dial its answer was most sensitive to. Right answer, right route. |
| P2 both-sides | PASS | From the packet alone: strongest A = "MT delivers a real 59% five-year survival rate at less than a third of CABG's cost ($27,000 vs $94,000) without open-heart surgery." Strongest B = "CABG raises Paul's real five-year survival rate from 59% to 64% — a 5-point edge from the same trial Dr. Hotchkiss helped run, for a patient whose 98% occlusion and family history put him in the profile most likely to benefit." Neither side collapses — each has real, packet-sourced numbers, not a concession. The recorded 5.0-point margin is not a paper number. |
| P3 trap | FAIL | Mechanical screen (`tier2_probes.py`) already flags FACILITATOR.md's trap text as reading like "a difficulty note, not a trap" — it names *which factor a student weighs exclusively* (cost-only or survival-only), not a concrete wrong *move*. A second, independent fresh subagent (packet only, no FACILITATOR.md) was asked to name the most plausible wrong path and found a different, more insidious one: Appendix A's table is headed **mortality** (41%/36% at 5yr), while Challenge D1 asks for **survival rate**. A hurried student can copy the mortality figures straight into D1 as if they were survival rates. The point gap still comes out to 5 (41−36 = 64−59), so the arithmetic "checks out," but the labels invert — MT now looks like the better performer (higher number) when CABG is actually the real winner. This can silently flip a student's D5 recommendation while looking internally consistent. FACILITATOR.md's actual trap section (§"The trap") never anticipates this — it is entirely about which factor gets ignored, not about the mortality/survival sign flip. Per SKILL.md: "A trap the guide has not anticipated is a FAIL even if the case is sound." |
| P4 twist | FAIL | Mechanical recompute via `sensitivity_model.py.evaluate_twist()` reproduces FACILITATOR.md's twist exactly (survival margin widens 5.0 → 7.2 points, same winner B), so the twist is not a no-op in the narrow numeric sense. But the qualitative check (does the twist survive the case's own document read the way a student actually reads it, not the way the author staged it) fails: case.md's own Appendix A is headed "Real Outcomes at **~5 and ~10 Years**" and prints both rows in one table, available to every reader from the first pass through the case — not gated behind the facilitator's minute-15 reveal. The independent P1 cold-solve subagent (packet only) *saw the 10-year row on its first read* and explicitly reported deciding to ignore it because D1 asks for 5-year data (see its answer to Q6). That means the "twist" the guide plans to spring at 15:00 is not actually hidden information — it is sitting in plain sight in the reading material every student has before Anchor 1's vote. The twist survives the author's *intended* reading (do not look ahead) but not the most natural student reading of a document that puts both timeframes in one Appendix A table. This is exactly the class of failure SKILL.md's P4 §2 describes (Cold Chain's twist under a sequential Assumption-1 reading): a twist whose surprise value depends on a pacing convention the case document itself does not enforce. |
| P5 sensitivity | PASS (disclosed) | Ran `sensitivity_model.py`, sweeping the only genuine author-chosen assumptions (`FLEX = mt_monthly_cost, cabg_surgery_cost, cabg_monthly_followup`, all from the disclosed Appendix C/Assumption-2 cost convention) at ±50%. All 6 flexes: no flip, no cap breach (`tier2_probes.py --probe 5 --flex 0.5` output, base A=59.0/B=64.0, margin 8.5%, all flexes unchanged). This is not a script artifact: the case's own `balance.margin_basis` (case.json) states plainly that the graded primary metric is the survival-rate gap and that the cost figures, while real and central to D3/D4, are "not the graded primary metric" — so a param that only feeds the cost line cannot by construction move the win/loss metric. The disclosure is real and explicit in case.json, so this is a genuine PASS, not a hidden fragility. Reported as a finding for completeness: the case's real graded metric (5-yr survival) is 100% cited trial data with no author-chosen dial in it at all — P5 could never find instability in the graded metric itself even in principle, because nothing about it is an assumption. That is a property of the case design, not a defect. |
| P6 data decay | PASS | All 3 `sources[]` URLs fetched live via browser. **S1** (nejm.org/doi/full/10.1056/NEJMoa1100356): reachable, confirms "244 patients (41%) in the medical-therapy group and 218 (36%) in the CABG group," P=0.12, median follow-up 56 months, NCT00023595 — exact match to case.json. **S2** (nejm.org/doi/full/10.1056/NEJMoa1602001): reachable, confirms "359 patients (58.9%) in the CABG group and... 398 patients (66.1%) in the medical-therapy group," P=0.02, median 9.8-year follow-up — exact match. **S3** (clinicaltrials.gov/study/NCT00023595): reachable, confirms Sponsor: Duke University, ID NCT00023595 — exact match. No dead links, no drifted figures, no NOT FOUND. All three sources accessed 2026-08-04, now 15 days old — well within the 365-day flag threshold. |

### Tier 3 — human dry-run
NOT RUN.

### Blocking summary
2 of 6 probes FAIL (P3 trap, P4 twist). Per SKILL.md: "A case whose named trap is not the trap
that actually catches the room, or whose twist does not survive the most natural student reading
of its own document, does not reach TIER2_PASS regardless of how the other four probes score."
Neither finding is fixed here — per "Never fix the case," both are named and handed back:

- **P3 fix direction (not applied):** rewrite FACILITATOR.md's "The trap" section to name the
  mortality-vs-survival label inversion as the primary trap (or add it alongside the existing
  cost/survival-weighting trap), so the guide is actually watching for the failure mode a real
  cold solver is likely to produce.
- **P4 fix direction (not applied):** either (a) restructure case.md's Appendix A so the 10-year
  row is not printed until the facilitator wants it revealed (e.g. a separate, later appendix, or
  a note that Challenge 3/D1 only uses the 5-year row and the 10-year row is facilitator material),
  or (b) accept that the twist is not a withheld-information reveal at all and redesign the twist
  moment around something the case document does not already disclose in full.

## case-readiness re-verification — 2026-08-22
**State:** TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

The P3/P4 fixes named as "not applied" above (case-write direction) were found already implemented
in the live files — FACILITATOR.md's trap section rewritten to name the mortality/survival label
inversion, and case.md restructured with a `<!-- FACILITATOR ONLY -->` marker gating the 10-year
STICH data out of the student-facing read — but never re-verified through Tier 2 or recorded here.
This entry closes that gap.

### Tier 1 re-run
`tier1_structural.py --case cardiology`: 18/19 PASS, 1 GAP (T1-18, CSS/SVG decorative decimals —
accepted class), 0 blockers. `case.md` changed (10-year data moved below the FACILITATOR ONLY
marker); `case_md_sha256` updated accordingly.

### Tier 2 re-verification

| probe | 2026-08-19 | 2026-08-22 |
|---|---|---|
| P1 cold solve | PASS | **PASS (re-confirmed)** — genuinely fresh subagent, packet-only, reached B with correct arithmetic; explicitly asked whether any 10-year/longer data was visible anywhere in the packet — answered no, none found. Confirms the FACILITATOR ONLY gate holds under an adversarial read. |
| P2 both-sides | PASS | PASS (unchanged, not re-run — trap/twist fix does not touch either argument's numbers) |
| P3 trap | FAIL | **PASS** — a second genuinely fresh subagent, packet-only, independently named the exact mortality/survival label-swap trap (41%/36% copied into D1 unconverted, gap surviving arithmetic-check at 5.0 points either way) before reading the guide. Read against FACILITATOR.md afterward: exact match, no divergence — the guide's rewritten trap is the one that would actually catch a room. |
| P4 twist | FAIL | **PASS** — a third fresh subagent confirmed (a) the twist has real bite: survival gap widens 5.0→7.2 points AND the significance story flips (p=0.12 at 5yr → p=0.02 at 10yr, a room that hedged on "not proven yet" now has real grounds to reconsider); (b) the 10-year figures ("Facilitator-Only: STICH Extended Follow-Up") sit strictly after the FACILITATOR ONLY marker — confirmed by direct file inspection, not just the cold-solve's negative report; (c) no unstated convention — D1 explicitly scopes to 5-year data, nothing under the stated Challenge instructions surfaces the 10-year row. |
| P5 sensitivity | PASS | PASS (unchanged, not re-run) |
| P6 data decay | PASS | PASS (unchanged, not re-run) |

All six Tier 2 probes now PASS with zero FAIL. `case.json.qa` updated: `state: TIER2_PASS`,
`verdict: PASS`, `run_on: 2026-08-22`, `tier2.P3`/`tier2.P4` set to `PASS`.

**Files changed this pass:** none (`cases/cardiology/case.json` `qa` block only — the FACILITATOR.md
and case.md edits themselves were already in place from 2026-08-20, this pass only re-verified and
recorded them).
