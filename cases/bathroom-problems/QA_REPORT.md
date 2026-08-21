## case-readiness run — 2026-08-20
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (19 checks)
19 checks: 17 PASS, 2 GAP, 0 FAIL. GAP T1-06 (final Appendix F referenced only by construction via
Challenge 1 — expected). GAP T1-10 (legacy-conversion carve-out, `legacy_conversion_note` present
— not a BLOCKER per 2026-08-13 doctrine amendment).

**VERDICT: TIER1_PASS (0 blockers, 2 gaps)**

`sha256(case.md)` = `819db8a2e8832e691a049bc03a50f559a0906abc9af868305c31db048b911285`, recorded in
`case.json.qa.case_md_sha256`. (Fixes below live entirely in `FACILITATOR.md` and `case.json`'s
facilitator-only `balance`/`derived` blocks — `case.md` itself was untouched, so its hash is
unchanged from the first Tier 1 run.)

### Tier 2 — simulated play (6 probes)

One real, non-trivial defect found and fixed during this run: Option B's own turn-order rule
silently and permanently disadvantages one family member in a way the case's top-line "everyone
gets the same 30.8%" framing didn't disclose.

| Probe | Verdict | Basis |
|---|---|---|
| P1 cold-solve | **PASS** | Fresh subagent, packet-only. Chose the Priority Line, correctly built the full D1 schedule and D2/D3 water math, and — without being prompted — independently surfaced the same finding P2/P3 confirm below: Marta's Option B slot finishes at 8:00:02 (essentially exactly her leave-by time), a zero-buffer edge case. |
| P2 both-sides-solve | **PASS** (after a real fix) | Fresh subagent built both schedules in full and identified precisely where Option B's case collapses: its turn order (leave-by time, ties broken by lower total need) never rotates, so Marta — latest leave-by time, highest need in that tier — is permanently last every single day, finishes at exactly 8:00:00 with zero buffer, and showers entirely in cold water once the 28-minute hot-water supply (D3) is exhausted by the seven people ahead of her. This is real and structural, not incidental. |
| P3 trap-check | **PASS** (confirms P2) | Independent fresh subagent, given a more targeted prompt, reproduced the identical turn order, hot-water cutoff (mid-George's shower), and cold-water list (Rulon, Olivia, Marta) via independent arithmetic, and reached the same assessment: the uniform-30.8% framing hides a real, non-incidental double disadvantage for Marta (proportionally-scaled minutes AND guaranteed cold water AND permanently last). Two independent probes reaching the same numeric trace is strong confirmation this is real, not a probe artifact. |
| P4 twist-integrity | **PASS** | Twist (grandparents arrive, 10-person recompute) verified independently: Option A's flat slot drops to 7.0 min (below George's 8-min need for the first time), Option B stays at 70.0 useful minutes but uniform percent-met drops to ~25.3%, margin compresses from 10.24% to 6.06% — winner unchanged, consistent with `case.json.derived.twist_*` values. |
| P5 assumption-sensitivity | **PASS** | Mechanical script run (`--flex 0.5` on `window_minutes`), clean. Margin moves between 4.1% and 17.0% across the swept range but never flips the winner or breaches the 20% cap. |
| P6 data-decay | **PASS** | Both live sources (S2: ENERGY STAR First Hour Rating definition; S3: EPA WaterSense showerhead flow-rate figures) independently fetched and confirmed exact, current, and at the correct URLs. No changes needed. |

**The fix:** Option B's math and margin (10.24%, 70.0 vs. 63.5 useful minutes) are correct and
unchanged — this was not a computational error. What was missing was disclosure: `case.json`'s
`balance.argument_a` and `FACILITATOR.md`'s "Argument for A" section were strengthened with the
concrete, checkable finding (Marta permanently last, zero-buffer 8:00:00 finish, guaranteed cold
water), a new Socratic question (4b) was added, `FACILITATOR.md`'s trap section gained a second
named trap ("uniform percentage = fair"), and the full turn-order/hot-water trace was recorded in
`case.json.derived` (`option_b_turn_order`, `option_b_hot_water_cutoff_person`,
`option_b_fully_cold_water`, `option_b_marta_finish_time`) so it's checkable rather than a
probe-only finding. The case's balance and margin remain genuinely close (10.24%, under the 20%
cap) — Option B still wins on its own stated metric — but the discussion is now honest about what
that metric doesn't capture, which materially strengthens Argument A rather than invalidating
Argument B.

**MECHANICAL RESULT:** 0 probes failed. All 6 probes carry a recorded verdict. One real defect
(an undisclosed structural cost of Option B, independently confirmed by two probes) was found and
fixed during this run.

**Tier 1 clean (0 blockers, 2 gaps) AND all six Tier 2 probes PASS → state promoted to
`TIER2_PASS`.** `case.json.qa` updated: `state: "TIER2_PASS"`, `verdict: "PASS"`,
`run_on: "2026-08-20"`, `blockers_open: 0`, `gaps_open: 2`, `case_md_sha256` recorded. Per
SKILL.md's ladder, `case-publish` may now run — Tier 3 (a filed human `RUN_REPORT`) remains
required before `VERIFIED`.
