## case-readiness run — 2026-09-01

**State:** researched → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (20 checks)

Remediation this session: fixed 2 T1-06 orphan-appendix BLOCKERs — added `(SEE APPENDIX C)` to
Challenge D3 (was never referenced by letter) and `(SEE APPENDIX F for real, published
industry-scale rig counts)` to Background. Added `(SEE APPENDIX H)` reference for the final
standards appendix. Added `reinforcement_note` after checking the full Pre-Calculus domain — no
`n==0` skills exist. Recorded `qa.case_md_sha256`.

`VERDICT: TIER1_PASS (0 blockers, 1 gap: T1-10 reinforcement carve-out)`.

### Tier 2 — simulated play (6 probes)

Added `case.json.sensitivity_disclosure[]` (2 entries: `remaining_days`, `relocation_downtime_days`)
— `tier2_probes.py`'s own sweep correctly found these flip the verdict at ±50%. This is expected
and by design: the base margin is only **1.03%**, matching SPEC §2's own cited gold standard (the
Robotics Engineering exemplar's 0.09% margin) — a case this close is *supposed* to flip under
almost any perturbation, and MA3 (relocation downtime, the dominant driver) is explicitly the
one modeling choice case.md calls out as HIGH sensitivity, with D5 itself asking the student to
compute the exact breakeven value.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A solver sets up D1's 3-unknown linear system (Permian rig-days, Bakken rig-days, idle relocation rig-days) from Appendix A/B's constraints, solves via Gaussian elimination or matrix inverse (D2), repeats for Hold the Line (D3, same coefficient matrix — a real, findable structural fact), and computes D4's blended bbl/rig-day comparison from Appendix D's real EIA figures. The metric (total blended barrels/rig-day) is named explicitly by Background and D4. |
| P2 both-sides | **PASS** | A's best sentence: "The Bakken really does produce more oil per rig (real EIA data, 1,747 vs 1,400 bbl/day), and moving 2 rigs captures that edge for the rest of the quarter." B's best sentence: "The relocation cost is real too — 14 days of zero production on 2 rigs, close to the exact number of days needed to cancel the Bakken's edge, plus a real, named cost to Torchline's most experienced crew that never shows up in the barrels-per-rig-day number at all." Neither concedes; the margin (1.03%) means the arithmetic alone barely decides it, so the crew-disruption argument in Background is doing real work for B. |
| P3 trap | **PASS** | The stated trap (reading Appendix D's raw per-rig productivity numbers as already answering the question, without building the actual rig-day accounting that shows relocation downtime nearly cancels the edge) is the single most plausible failure mode — the productivity gap is the more visually striking number, and D1-D4's actual system-of-equations work is the only way to see how close it really is. FACILITATOR.md names this trap explicitly. |
| P4 twist | **PASS** | (twist reviewed in FACILITATOR.md.) Holds under every reading of MA1-MA3; does not depend on any unstated convention. |
| P5 sensitivity | **PASS (disclosed)** | Base margin 1.03% — the tightest race in this batch, deliberately mirroring SPEC §2's own gold-standard exemplar. `remaining_days` (MA2) and `relocation_downtime_days` (MA3) flip the verdict at ±50% — MA3 is explicitly named "the single most dilemma-relevant modeling choice in the case" in case.md, with D5 itself asking students to derive the exact breakeven point; both are now recorded in `sensitivity_disclosure[]`. This instability is the case's designed mechanism, not a defect. |
| P6 data decay | **PASS (live fetch)** | S1 (EIA Permian DPR PDF) and S2 (EIA Bakken DPR PDF) — both re-fetched live via `curl` (WebFetch's PDF text extraction failed on the binary; `pdftotext` succeeded) and confirmed verbatim: Permian "1,400 / 1,386 barrels/day" (June/May); Bakken "1,747 / 1,745 barrels/day" (June/May) — both exactly matching the case's cited values and June-2024 cutoff. S3-S5 (industry commentary/context, not load-bearing on the D1-D4 metric) not independently re-fetched; RESEARCH_LOG.md records same-day confirmation. |

`MECHANICAL RESULT: 0 probes FAILED. All six verdicts recorded by name.`

**No retune needed.** Base margin 1.03% — an intentionally razor-thin, SPEC-gold-standard race —
both load-bearing EIA sources confirmed live and exact at the stated June-2024 cutoff.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-rig-split/runs/RUN_*.md` filed.
