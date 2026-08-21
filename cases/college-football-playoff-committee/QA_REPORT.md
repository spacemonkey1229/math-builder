# QA Report — College Football Playoff Committee

## case-readiness run — 2026-08-20

### Tier 1 — structural (19 checks)
18 checks: 18 PASS, 1 GAP, 0 FAIL (T1-10 expected legacy carve-out).

**VERDICT: TIER1_PASS (0 blockers, 1 gap)**

Two real defects were found and fixed before/during Tier 2:

1. **Structural**: the case-write pass left the `<!-- FACILITATOR ONLY -->` marker immediately
   after the Dilemma (before Challenges/Appendices A-H), which would have stripped the entire
   student packet — including all real AP/SRS data tables — down to just
   Overview/Background/Dilemma. Moved to the end of the file.
2. **Personality rights**: the case's protagonist was originally the real, currently-serving CFP
   committee member and University of Utah Athletic Director this case's source docx named,
   with a fabricated internal deliberation and invented career biography attached to his real
   name — the same risk already avoided in this session's `movie-producer` conversion. Renamed
   the protagonist to a fictional "Derek Talcott" at a fictional program, and generalized his
   biography so it no longer traces to the real person, throughout `case.md`, `case.json`, and
   `QA_REPORT.md`.

Also missing at first Tier 1 pass and authored during this run: `sensitivity_model.py` (none
existed).

### Tier 2 — simulated play (6 probes)

One real citation defect found and fixed; the case's own disclosed assumption-instability was
confirmed real and formalized via `sensitivity_disclosure[]`.

| Probe | Verdict | Basis |
|---|---|---|
| P1 cold-solve | **PASS** | Fresh subagent, packet-only. Reproduced the Composite Selection Score exactly (Oklahoma 66.08%, Michigan 73.79%, matching `case.json.balance` to the decimal), backed Michigan, and independently derived the crossover weighting (~63% human weight flips the verdict to Oklahoma) — confirming MA4 is the case's most load-bearing, least-supported number, exactly as `case.json` already states. |
| P2 both-sides-solve | **PASS** | Fresh subagent reproduced the same composite scores exactly and identified precisely where Oklahoma's case collapses: its own SRS (11.52) is lower than 5-3 Penn State's (12.74) in the same Appendix C table — the undefeated record isn't backed by the underlying performance data. Michigan's case has no equivalently sharp single-number weakness in the packet. |
| P3 trap-check / P4 twist-integrity | **PASS** | Fresh subagent's cold-read trap prediction (students treat the Georgia-SRS-ceiling denominator as a neutral, objective anchor without noticing Georgia isn't actually competing for the contested spot) matched the guide's named trap exactly. Independently re-derived the Twist's full recomputation (Alabama's 20.95 as the new ceiling instead of Georgia's 25.94) from the packet's own raw data: Oklahoma 54.99%/71.37 composite, Michigan 100.33%/83.44 composite, margin 16.91% — every figure matches `FACILITATOR.md` exactly, including Michigan's Machine% legitimately exceeding 100%. Direction doesn't flip; the guide's own "gap changes, direction doesn't" framing is accurate. |
| P5 assumption-sensitivity | **PASS (disclosed)** | Authored `sensitivity_model.py` (none existed at TIER1_PASS), reproducing the base Composite Selection Score exactly (66.08/73.79, margin 11.7%). Flexing `human_weight` ±50% genuinely flips the winner (to Oklahoma at +50%) and flexing `ap_max`/`srs_ceiling`/`human_weight` in the other direction breaks the 20% cap — this instability is already named explicitly in `case.json`'s own Appendix F/MA4 prose ("the single most load-bearing assumption... flagged for the ±50% sensitivity flex") and is the case's real teaching point (the real CFP committee itself uses no fixed weighting). **Fixed the mechanical gate**: added formal `case.json.sensitivity_disclosure[]` entries (category F) for all three dials so the probe recognizes this as disclosed, expected behavior rather than an undiscovered defect, and strengthened `FACILITATOR.md`'s sensitivity note with the exact quantified swings. |
| P6 data-decay | **PASS** (after a real fix) | S2, S3, S4, S5 all fetched and confirmed exact. **S6 (CBS Sports) was found mis-cited**: the case claimed it supports "12-team format continuing through at least the 2026 season," but the article's own text says that exact question was still undetermined as of its March 2024 publication date ("Still to be determined is whether the CFP will feature a 12- or 14-team format beginning in 2026"). **Fixed**: narrowed S6's claim to only what the article actually states (the $1.3B media-rights deal), and moved the "12-team format through 2027" claim onto S3 (Wikipedia), which P6 independently confirmed does support it ("expanded to a 12-team format for the 2024 through 2027 seasons"). Updated `case.md` Appendix D and `case.json`'s S3/S6 source entries accordingly. |

**MECHANICAL RESULT:** 0 probes failed. All 6 probes carry a recorded verdict. One real citation
defect (P6's S6 mis-citation) was found and fixed; P5's disclosed instability was formalized
rather than papered over.

**Tier 1 clean (0 blockers, 1 gap) AND all six Tier 2 probes PASS → state promoted to
`TIER2_PASS`.** `case.json.qa` updated: `state: "TIER2_PASS"`, `verdict: "PASS"`,
`run_on: "2026-08-20"`, `blockers_open: 0`, `gaps_open: 1`, `case_md_sha256` recorded (re-hashed
after the marker fix, protagonist fictionalization, and S6 citation fix above). Per SKILL.md's
ladder, `case-publish` may now run — Tier 3 (a filed human `RUN_REPORT`) remains required before
`VERIFIED`.
