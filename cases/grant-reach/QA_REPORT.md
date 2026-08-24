# QA Report — Grant Reach

## case-readiness run — 2026-08-22

### Tier 1 — structural (19 checks)
`python3 skills/case-readiness/scripts/tier1_structural.py --case grant-reach`
19 checks: 19 PASS, 0 GAP, 0 FAIL.

Fixed this session: 4 BLOCKERs (stray Overview numeral "7 a.m." cleared in
`case.json.overview_numerals_cleared[]`; `FACILITATOR.md` rebuilt into the required
anchor-ladder format with a timed 45-minute plan; missing `cohort_bands[]` and
`case_md_sha256` added). All 4 GAPs from the first pass (Socratic-question line-wrap
miscount, an orphan "60%" hypothetical in a Socratic question, the same two missing-field
items) also cleared.

`sha256(case.md) = e33fcfac335cafd0b258dbcf0a2a4fd4723cb3fe0723286555af669c601c1bc7`
(recomputed after the Background-paragraph fix below; hash current as of this report)

**VERDICT: TIER1_PASS (0 blockers, 0 gaps)**

### Tier 2 — simulated play (6 probes)

| Probe | Verdict | Basis |
|---|---|---|
| P1 cold-solve | **PASS** | Fresh subagent, packet-only (`/tmp/coldsolve-grant-reach/PACKET.md`), no other project file read. Reached **A** via the required set-theory pipeline (union-intersection formula, D4 renewal projection by region, D5/D6 cost and margin comparison) — independently reproduced 2,275 vs. 1,987.9 renewals, a ~287-student gap. Named the metric (total on-time renewals, not cost) and why, named the strongest counter-argument (Order A spends 94.9% of the year's discretionary budget), correctly named MA5 as the most sensitive assumption — matching what P5's mechanical sweep actually found. |
| P2 both-sides-solve | **PASS (after a real fix)** | Both A and B got real, non-concession opening arguments. The probe then surfaced a genuine case-definition defect: `case.md`'s Background paragraph asserted the entire 9,000-student population "received either a federal Pell Grant, a state Cal Grant, or both" — a strict identity claim that contradicts Appendix B's own "Neither: 5,750" Venn region, which requires some of the 9,000 to hold neither grant. This let the probe construct an alternate "full-population" margin (5.6%) against the case's stated 12.6%, calling the headline margin a paper number. **Root cause, not just the symptom, was fixed this session**: reworded Background so the 9,000 is explicitly Deja's screening pool (not a set already restricted to grant-holders), and added a sentence to Appendix B explaining the 5,750 "Neither" students have no aid to renew and are correctly outside D4–D6's scope — which also shows the probe's "full-population" alternate margin was itself a modeling error (applying a renewal rate to students with nothing to renew), not evidence the case's own 12.6% scoping was wrong. Re-verified via Tier 1 (T1-16 hash updated, 0 blockers). |
| P3 trap-check | **PASS** | Independently named the same trap `FACILITATOR.md` names — the "$0.00 = obviously correct" bias, where a hurried student reads Order B's zero university cost as an unambiguous win without computing the 287-student/thousands-of-dollars-of-aid gap it hides. Numbers matched exactly (2,275 vs. 1,987.9, gap ≈287). |
| P4 twist-integrity | **PASS** | Twist (the $0.00 cost is a ratio artifact, not proof nothing is lost) invalidates the naive first-vote position for Order B. Re-derived the 287-student gap under every defensible reading of MA1–MA6 and the stated budget/rate constraints — the twist survives in every case (changes magnitude, never direction or existence), and its core mechanism, gap = (Pell-only + State-only) × (MA5 − MA4), is structurally forced by the case's own model, not dependent on an unstated convention. One minor non-blocking note: MA2's displayed "18.6%" is a rounded display of the unrounded 453,000/2,440,631 = 18.56% used to derive the actual 1,670/334 counts — a cosmetic rounding note, not a defect, since Appendix B hands students the exact counts directly rather than asking them to reconstruct from the rounded percentage. |
| P5 assumption-sensitivity | **PASS (disclosed)** | `tier2_probes.py --case grant-reach --probe 5 --flex 0.5` via `cases/grant-reach/sensitivity_model.py` (authored this session): swept all 5 declared dials (MA1–MA5). Winner (A) flips to B under two flexes (MA4 +50%, MA5 −50%), and 5 of 10 flex points push the margin past the SPEC §2 20% cap. All 4 unstable params (`state_share`/MA2, `overlap_share`/MA3, `rate_no_reminder`/MA4, `rate_with_reminder`/MA5) are disclosed in `case.json.sensitivity_disclosure[]` as Category F (irreducible unknowns — no public per-campus dataset could ever pin these down exactly). Also written into `case.json.balance.sensitivity_caveat` and a new "Facilitator note — margin stability" section in `FACILITATOR.md`, consistent with the Modeling Assumptions table's own pre-existing "the answer is sensitive to this value" flags on MA2–MA5. Passes per the disclosure-aware pass state, not the stable-margin state. |
| P6 data-decay | **PASS** | 7 of 8 `sources[]` URLs fetched live 2026-08-22, all reachable with their recorded figures confirmed verbatim (S1/S2 32.4%/$5,300; S3 Cal Grant income ceilings; S4 453,000 recipients; S5 2,440,631 enrollment; S7 $0.467/piece; S8 4.34%→7.77%). S6 (csac.ca.gov Cal Grant B Access Award page) could not be programmatically verified — blocked by AWS WAF bot protection on every fetch attempt (this tool, raw curl, and the Wayback Machine's own crawler all blocked/pending), reported as NOT FOUND rather than guessed, per MCS-21. This is not new information: S6 was already recorded at MEDIUM confidence in `RESEARCH_LOG.md` with an explicit "needs direct re-verification" flag, and is used only in Appendix E context, never in a load-bearing calculation. Recommend a human/browser check of that one URL before upgrading its confidence, but it does not block Tier 2. |

**MECHANICAL RESULT:** 0 probes failed after remediation. One real case-content defect
(P2's population-definition contradiction) was found and fixed during this run — not a
disclosure, an actual bug in `case.md`'s Background paragraph — then re-verified via Tier 1.
All 6 probes carry a recorded verdict (P1–P4 and P6 by independently-dispatched subagents
this session, P5 by the script).

**Tier 1 clean (0 blockers) AND all six Tier 2 probes PASS → state promoted to `TIER2_PASS`.**
`case.json.qa` updated: `verdict: "PASS"`, `run_on: "2026-08-22"`, `blockers_open: 0`,
`case_md_sha256` recorded and current. Per SKILL.md's ladder, `case-publish` may now run —
Tier 3 (a filed human `RUN_REPORT`) remains required before `VERIFIED`.
