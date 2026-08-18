## case-readiness run — 2026-08-12

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (19 checks)

First run: 2 BLOCKERs (Appendix A orphan, D3/D4/D5 mapped to no skill) plus 2 GAPs (a vocabulary
term absent from `standards[]`, two already-covered skills claimed but not forced). All resolved:
Appendix A referenced from Background; D3/D4/D5 mapped to already-covered arithmetic skills they
genuinely use (decimal division, multiplication, percent); `geometry-3-dimensional` added to
`standards[]` and forced via D1. **Final run: 0 BLOCKERs, 0 GAPs.**

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh agent reached the case's own intended numbers and recommendation (Option B, $1,040.34 vs $1,181.95, 11.98% margin) with correct arithmetic, and cross-validated the ±50% sensitivity band exactly against Appendix E's own stated range. Flagged a real, genuine ambiguity: whether the open-bottomed vent cap has 4 or 5 faces was not stated unambiguously (the agent had to infer 4 from Appendix D's "4 weld seams" phrasing). **Fixed**: D1's own text now states explicitly to count faces "as actually fabricated... open at the bottom, so there is no base panel." |
| P2 both-sides | PASS | Both sides built and defended competently. The agent went beyond the ask and derived the exact batch-size window (N=13-14) where the recommendation would flip to Option A — a genuine, correct piece of mathematical reasoning that strengthens FACILITATOR.md's Deep Conflict thread 2 ("a small design change, multiplied") without requiring any case change. |
| P3 trap | PASS | Fresh agent (before reading the guide) independently identified the same "tighter nesting = cheaper, stop there" trap as the guide's own named trap. Noted a legitimate secondary trap (the face/edge count) that the guide documents elsewhere (Data Deep Dive, Lessons Learned) but doesn't cross-reference from "The trap" section itself — a minor structural note, not a defect requiring a fix. |
| P4 twist | **FAIL, then PASS after fix** | First pass found a real, direct leak: Appendix E's MA3 row explicitly named "the Twist," stated the exact "+40% price spike" magnitude, and pointed to "see FACILITATOR.md" — all in the student-facing document, before the scripted reveal. **Fixed**: MA3 rewritten to state only real, general, direction-neutral commodity-volatility context ("swung 30-50%+... could matter if the market moves") with no reference to a twist, no specific magnitude, and no facilitator pointer. Re-verified with a second fresh agent, which confirmed no tell remains on any of four specific leak vectors (that a twist is coming; its direction; its magnitude; that this row is suspiciously different from its neighbors). |
| P5 sensitivity | PASS | Base margin 11.98% (CONTRACT-shaped `evaluate()`, same ceiling-collapse transform as Plaza Pavers/Company Front). Sweep of the sole FLEX dial (`weld_cost_per_seam`) ±50%: margin ranges 4.80%-15.39%, Option B cheaper throughout, no flips, no cap breaks. |
| P6 data decay | PASS | All 5 cited URLs (S1, S3, S4, S5, S6) were fetched live during `case-research` on 2026-08-12 (same day as this report) — see `RESEARCH_LOG.md`. Reachable, values confirmed present, none moved. S3 (M&K Metal sheet price) carries the source's own "sample pricing" caveat, already disclosed as MEDIUM confidence. |

### Tier 3 — human dry-run

NOT RUN — no real cohort available in this session. This case is **not `VERIFIED`, only
`PUBLISHED`-eligible** — should not be marked ✅ in `DOCTRINE_LEDGER.md` until a real guide files a
`RUN_REPORT.md` from an actual cohort.

### Minor accepted polish note

Appendix E's MA1/MA2 sensitivity columns reference internal pipeline terms ("Tier 2 probe 5,"
"RESEARCH_LOG.md") in student-facing text — present in this case and its two predecessors (Plaza
Pavers, Company Front). Doesn't leak any answer or twist (confirmed by the P4 re-verification
agent, which noted it in passing and found it didn't functionally telegraph anything), just
slightly informal for student consumption. Not fixed here; flagged for a future editing pass
across all three published cases rather than a one-off fix on this case alone.
