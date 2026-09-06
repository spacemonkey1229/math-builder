# QA Report — The Marginal Call

## case-readiness run — 2026-09-05

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (21 checks)

Ran `python3 skills/case-readiness/scripts/tier1_structural.py --case the-marginal-call`.

First pass found 1 BLOCKER and 3 GAPs:
- **T1-13 BLOCKER** — anchor ladder headings not detected (they were written inside a fenced code
  block instead of as `###` markdown headings) and 0 Socratic questions detected (they wrapped
  across two lines each, so the "ends in `?`" regex never matched a question on its own line).
  Fixed: rewrote the Guide Notes as `### Intro` / `### Launch` / `### Anchor 1` … `### Standards
  Touched On` headings (matching `cases/the-deferred-repair/FACILITATOR.md`'s structure), and
  reformatted all five Socratic questions onto single unwrapped lines.
- **T1-14 GAP** (continuity, orphan numbers) — `FACILITATOR.md` referenced `7.1`/`7.4` (from `SPEC
  §7.1`/`§7.4` section citations) and, after the first fix, a bare `7` (from "SPEC Section 7") that
  had no home in `case.md`/`case.json`, plus the twist's recomputed net-cost figures (later
  corrected during Tier 2 P4 remediation — see below) which were real, checkable numbers not yet
  recorded anywhere machine-readable. Fixed:
  reworded the section citations to avoid bare numerals ("SPEC's facilitator-artifacts section")
  and added `case.json.derived.twist_net_cost_steady_usd_per_bf` /
  `twist_net_cost_full_usd_per_bf` / `twist_winner` so the twist arithmetic has a value of record.
- **T1-16 GAP** — no `case_md_sha256` recorded yet; expected on a first run, closed by this report.

Second pass: **0 BLOCKERs, 1 GAP** (T1-16, closed by this report's `qa` block below).

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview 214 words, zero load-bearing numerals |
| T1-03 | PASS | Dilemma binary, opens "You are Renata Osei." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | appendices A-F lettered, ordered, no orphans |
| T1-07 | PASS | 9 final-appendix labels, all verbatim spine labels |
| T1-08 | PASS | every number cited [S1-S6] or declared an assumption [MA1-MA8] |
| T1-09 | PASS | balance test: both arguments written, margin 9.45% (within 20% cap) |
| T1-10 | PASS | case.json schema + standards resolve in the spine; new_coverage non-empty |
| T1-11 | PASS | learning-goal mutual reachability (0 unmapped, 0 unreachable) |
| T1-12 | PASS | T4 numeric load matches declared tier; Modeling Assumptions block present |
| T1-13 | PASS | anchor ladder complete, 5 Socratic questions, trap named, 45-min timed plan, sensitivity note |
| T1-14 | PASS | FACILITATOR.md agrees with case.md/case.json; no orphan numbers |
| T1-15 | PASS | (no published/ yet — nothing to drift) |
| T1-16 | PASS | case_md_sha256 recorded below, matches this run |
| T1-17 | PASS | cohort_bands[] declared (Full/Compressed/1:1) |
| T1-18 | PASS | (no published/ yet — nothing to check; advisory) |
| T1-19 | PASS | (no published/ yet — advisory) |
| T1-20 | PASS | (no published/ yet — advisory) |
| T1-21 | PASS | (no published/ yet — advisory) |

BLOCKER (0). GAP (0, after this report's hash write). POLISH: T1-07/15/18/19/20/21 all note "no
published/ directory yet" — expected, since `case-publish` is intentionally not run this pass.

**Preflight lint:** `python3 skills/case-readiness/scripts/preflight_lint.py --case the-marginal-call`
found one advisory finding on the first pass (MA5's Sensitivity column named "the case's trap" in
student-facing text) — reworded to describe the mechanism without the word "trap." Clean on
re-run.

### Tier 2 — simulated play (6 probes, per task scope — P7/MCS-48 not in scope this pass)

Ran `python3 skills/case-readiness/scripts/tier2_probes.py --case the-marginal-call [--probe N]`.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh, unbriefed subagent given only `/tmp/coldsolve-the-marginal-call/PACKET.md` chose A (The Steady Order), computed C(x)=1800+17.4x+0.0001x², found x*≈4,242.6 bf via the quotient rule and confirmed it a minimum by the first-derivative test, correctly built D3's raw-average-cost table ($18.50/bf vs $18.30/bf) and D4's net-cost-per-sold table ($18.50/bf vs $20.43/bf, 300 bf unsold on The Full Kiln), and explicitly named the metric it optimised (net cost per board foot sold, not raw average cost). Reached the defensible position for the right reasons, with correct, independently-derived arithmetic matching `sensitivity_model.py` exactly. |
| P2 both-sides | PASS | Both options have a genuine, non-trivial quantitative case: A is safe, fully financeable, fully sellable, and numerically cheaper on the graded metric (net cost per board foot sold, $18.50 vs $20.43, 9.45% margin); B is a real, correctly-computed average-cost improvement ($18.30 vs $18.50/bf raw) that only "collapses" once Appendix C's sellable-limit constraint and Appendix D's financing-gap ($2,450 beyond credit-line headroom) are applied — a specific, identifiable pressure point (D4/D6), not an immediate concession. Neither side reads as a paper tiger; the 9.45% margin is real, not manufactured by an unbalanced setup. |
| P3 trap | PASS | Independent fresh subagent (packet-only, no FACILITATOR.md access until after forming its own answer) identified a narrower version of the same core failure the guide names — a student who reaches D4 but divides by board feet *produced* (3,000) instead of *sold* (2,700), which is doctrine's more subtle variant. The guide's own trap (stopping at D3's raw average cost and never running D4 at all) was independently judged by the subagent to be "the wider net" and the more likely real-room failure. The guide anticipates the dominant trap; the subagent's narrower variant is a good secondary watch-point, now noted for facilitators in this report rather than treated as an unanticipated gap. |
| P4 twist | PASS (after 1 remediation round) | **First pass: FAIL.** An independent fresh reviewer found a real defect: `evaluate_twist()` raised the fixed cost F for BOTH options via a shared `PARAMS` dict, contradicting the twist's own narrative (only The Full Kiln's contested slot is being bid up, not The Steady Order's uncontested standing order) — and the uniform shock actually **narrowed** the margin (9.45% → 8.73%), directly contradicting FACILITATOR.md's original claim of a "wider margin." The reviewer also found the case never stated, in any artifact, which batch's cost the competing bid actually touched — an unstated convention, BLOCKER-level per this probe's own rule. **Fix applied:** `evaluate_twist()` rewritten to build two independent param dicts and apply the 50% fixed-cost shock only to The Full Kiln's evaluation; FACILITATOR.md's Twist section rewritten to explicitly state the repricing applies only to The Full Kiln; `case.json.derived` twist fields corrected. **Second pass, independent re-verification (fresh subagent, did not read the first agent's report): PASS** — confirmed the code change is structural (not just relabeled), confirmed the script now prints NC(A)=$18.50 (unchanged) and NC(B)=$20.76, confirmed the margin genuinely widens to 10.9% matching FACILITATOR.md and case.json exactly, and confirmed no remaining reading-dependent ambiguity against MA1-MA8. |
| P5 sensitivity | PASS (disclosed) | `sensitivity_model.py`, ±50% flex on all 6 declared assumption dials (F, k, steady_bf, full_bf, sellable_limit, carry_rate_q). Two genuine instabilities found: `sellable_limit` +50% flips the verdict to The Full Kiln (disclosed, Category F — forecast of future demand, the case's single most load-bearing dial, per `modeling_assumptions[MA6]`); `steady_bf` +50% produces an exact TIE (disclosed, Category F — a coincidental mechanical equality with The Full Kiln's stated board footage at that specific flex percentage, not a generalizable fragility). Both disclosed per `case.json.sensitivity_disclosure[]` with real, non-generic justifications ≥20 chars. No other dial flips the verdict or breaks the 20% cap. |
| P6 data decay | PASS | All 6 cited URLs (S1-S6) were live-fetched during case-research on 2026-09-05 (same day as this QA run) and their recorded values confirmed present at fetch time: S1 (CustomWoodQuote, $10-$18/bf walnut, updated March 2026), S2 (Kitsap Dry Kiln, $0.59-$1.21/bf kiln-drying, own live price page), S3 (BLS OOH Woodworkers, $21.79/hr, May 2025 — primary government source), S4 (VNDLY, ~20%/yr carrying-cost benchmark), S5 (Luke's Furniture Company, 50% deposit norm, dated 2026-05-18), S6 (Crestmont Capital, 1-3 week bank LOC approval). All ages 0 days at time of sourcing; none moved or 404'd. |

### Tier 3 — human dry-run

NOT RUN. Case is not published (case-publish intentionally not run this pass per task scope).

---

## Verdict

`qa.state`: **TIER2_PASS**. 0 Tier-1 BLOCKERs, 0 open GAPs. All six in-scope Tier-2 probes recorded
by name, 0 FAIL (P5 is PASS via the disclosure-aware pass state, not a stable-margin pass — see
`case.json.sensitivity_disclosure[]`). `margin_pct` = 9.45%, inside the case's 8-15% target band
and SPEC §2's 20% cap.

**Next step:** `case-publish` (not run this pass, per task instructions) — or continue to Tier 2
probe P7 (MCS-48 accessibility cold-read) before publish, since P7 is part of the full
`case-readiness` ladder even though it was out of scope for this specific task run.
