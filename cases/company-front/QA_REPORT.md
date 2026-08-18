## case-readiness run — 2026-08-12

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (19 checks)

First run: 2 BLOCKERs (Overview numerals 88/104 needing clearance; D6 mapped to no skill) plus
several GAPs (already-covered skills claimed in `standards[]` but not forced by any deliverable or
present in the final appendix). All resolved: numerals cleared as texture (the counts actually used
in every calculation, 16 and the twist's 14, are stated separately in Background/Appendix D);
D6 mapped to `advanced-numbers-how-to-find-the-percent-of-a-number` (D6 explicitly computes headroom
as a percentage); `geometry-translation` dropped from `standards[]` (nothing in this case forces
it — removed rather than artificially mapped, per the anti-inflation doctrine); the remaining
already-covered skills (`transformation`, `rotation`, `clockwise`, `counter-clockwise`, the CW
how-to) mapped to D1/D3 where genuinely forced and added to the final appendix. **Final run: 0
BLOCKERs, 0 GAPs.**

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh agent independently solved D1–D6 and reached the case's own intended numbers (27.05 / 11.25 in/step, 9.84% headroom) with correct arithmetic. Flagged one real ambiguity: Appendix B's marker coordinates are in "steps" but the appendix never explicitly stated 1 step = 22.5 in — the agent had to infer it from MA1's own claim. **Fixed**: Appendix B now states the unit explicitly. |
| P2 both-sides | PASS | Both sides built and defended competently. The agent went further than requested and *proved* Option A can never beat any rotation about the same center on raw travel (since this case's scale-factor-minus-one, 3.4, exceeds a rotation's maximum possible travel multiplier of 2) — a stronger, more rigorous version of the case's own "structurally always cheaper" claim. Confirmed the dilemma stays genuine because the two options don't compete on the same axis (a rotation cannot produce a full-field visual spread). Folded the proof into FACILITATOR.md's Data Deep Dive note. |
| P3 trap | PASS | Fresh agent (before reading the guide) predicted a units-conflation trap; on comparison, judged the guide's actual trap (treating a thin-but-passing margin as settled) as more central to the case's real design — it's wired into the Twist, Deep Conflict thread 1, and Socratic Q1, and the case's own D2 phrasing ("in inches per count") already guards against the agent's predicted units trap. Confirmed the guide's trap is specific and actionable. Machine pre-screen required an exact trigger-word match ("Most Heroes will... assume... missing that") — fixed on first pass this time (lesson from Plaza Pavers). |
| P4 twist | PASS | Independently reran `sensitivity_model.py` and hand-rederived the twist arithmetic from raw Appendix B/C figures: 432.75 in travel ÷ 14 counts = 30.91 in/step, exceeding the 30.0 in/step ceiling by a real ~3%. Confirmed the twist changes only the `counts` variable (no second variable slipped in), depends on no undisclosed convention (Appendix C's "one step = one count" is the only rule needed), and is never pre-leaked in the student-facing document. Genuine verdict flip, honestly derived. |
| P5 sensitivity | PASS (disclosed instability) | Base margin 9.84%, computed via `sensitivity_model.py`'s CONTRACT-shaped `evaluate()` (`"B"` represents the real 30in ceiling, not Option B's own Mirror-Turn number — see the function's docstring for why, same non-ratio shape Tide Window resolved with its clearance-vs-policy-floor framing). Mechanical sweep of `scale_factor`/`counts` at ±50% finds the verdict flips and the 20% cap breaks under several flexes. **This is the case's own intended design, not a defect**: the Twist demonstrates exactly this fragility with a real, disclosed 2-count cut. Recorded as a disclosed, accepted P5 finding (`case.json.balance.stability`), the same precedent as Cold Chain's own mechanical P5 FAIL on a real, disclosed sensitivity (see `ROADMAP.md`). |
| P6 data decay | PASS | Both cited URLs (S1, S2) were fetched live during `case-research` on 2026-08-12 (same day as this report) — see `RESEARCH_LOG.md`. Reachable, values confirmed present, none moved. |

### Tier 3 — human dry-run

NOT RUN — no real cohort available in this session. In lieu of a real classroom dry-run, Tier 2's
P1–P4 were each run through independent, genuinely fresh subagents with no access to
FACILITATOR.md, case.json, or prior context. This case is **not `VERIFIED`, only
`PUBLISHED`-eligible** — should not be marked ✅ in `DOCTRINE_LEDGER.md` until a real guide files a
`RUN_REPORT.md` from an actual cohort.

### Notable: this case shipped clean on the first design pass

Unlike Plaza Pavers (which needed a full redesign cycle after Tier 2 caught an undisclosed cost
model), Company Front's formula was fully disclosed from the first draft — every input traced to
Appendix B/C/D/E, no hidden blending constants — and the only Tier 2 finding requiring a fix was a
genuine but minor unit-clarity gap (P1). Applying the previous case's lesson up front paid off.
