# QA_REPORT.md — The Approval Gate

## case-readiness run — 2026-09-09

**State reached:** DRAFT → TIER1_PASS → Tier 2 (P1–P6 clean; P7 structurally blocked, see below)
**Verdict on P1–P6 (the probes achievable without running `case-publish`):** PASS

`case-publish` was explicitly out of scope for this pipeline run (per task instructions). Because
Tier 2's probe 7 (accessibility cold-read, MCS-48) is designed to grade the **published**
Interactive HTML's hover glossary — and falls back to a plain `case.md` text packet with no
glossary mechanism when no `published/` directory exists yet — P7 cannot reach a genuine PASS
at this pipeline stage. This is documented honestly below rather than suppressed or faked.
`case.json.qa.state` is therefore recorded as `TIER1_PASS` with all seven Tier 2 probes run and
verdicts on file, not as a literal `TIER2_PASS` (which per the current `case-readiness/SKILL.md`
doctrine requires 0 FAIL across all seven probes). See "Tier 2 — probe 7" below for the exact
remediation path once `case-publish` runs.

### Tier 1 — structural (21 checks)

Ran `python3 skills/case-readiness/scripts/tier1_structural.py --case the-approval-gate`.

Initial run: `checks run: 21   PASS 18 · GAP 3 · FAIL 0` → `TIER1_PASS (0 blockers, 3 gaps)`, with
T1-13 (0 Socratic questions found) fixed by reformatting the five questions onto single lines
(see "Real defects" below), then T1-14 (one orphan-number false positive on "SPEC Section 7") and
T1-16 (no hash recorded yet) both cleared once `resync_artifacts.py` ran and the `case.json.qa`
note was written. Final run: `checks run: 21   PASS 20 · GAP 1 · FAIL 0` →
**VERDICT: TIER1_PASS (0 blockers, 1 gap)**

| id | result | note |
|---|---|---|
| T1-01–T1-09 | PASS | structural sections, Overview/Dilemma/Challenge boilerplate, appendix referencing, appendix-G verbatim labels, sourcing discipline, balance test all clean |
| T1-10 | GAP | `new_coverage[]` is empty — reinforcement carve-out applies (`case.json.reinforcement_note` records every one of the 8 claimed skills was checked and is genuinely `n=2`, not `n=0`, before writing) |
| T1-11 | PASS | learning-goal mutual reachability — 0 unmapped deliverables, 0 unreachable skills |
| T1-12 | PASS | tier (T3) matches numeric load (3 boolean conditions, 8-row truth tables, multi-step cost derivation) |
| T1-13 | PASS | 5 Socratic questions (single-line, mechanically countable), trap named, full anchor ladder present |
| T1-14 | GAP | one orphan number `[7.0]` in FACILITATOR.md — confirmed false positive: it comes from the literal text "SPEC Section 7" / "SPEC §7.3" (a section-number reference, not a case fact), the same precedented false-positive class noted in `cases/the-overlap-send`'s own QA history |
| T1-15 | PASS | (no `published/` dir — nothing to drift) |
| T1-16 | GAP | no `case_md_sha256` recorded yet — expected before this report's own hash is written below |
| T1-17 | PASS | `cohort_bands[]` declared, 3 bands |
| T1-18–T1-21 | PASS (POLISH: no `published/` dir yet) | glossary/visual/interactive checks have nothing to check pre-publish |

**BLOCKER (0).** **GAP (1, final):** T1-10 (carve-out, documented). T1-14 and T1-16 were transient GAPs on the intermediate run, both resolved (T1-14's "SPEC Section 7" false positive cleared once the full `case.json.qa` record was written; T1-16 cleared once `resync_artifacts.py` recorded the real `case_md_sha256` below).

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh, unbriefed subagent given only the leak-free packet chose Option A, named "total expected monthly cost" as the metric, and reproduced the exact arithmetic to the cent ($14,400.00 vs. $15,972.95). Unprompted, it named MA4 (the $66 average value at risk) as the assumption its answer is most sensitive to and as the least-supported number in the case — matching `case.json.sensitivity_disclosure[]` exactly. |
| P2 both-sides | **PASS** | Fresh subagent, case.md only. Both options got a genuine best-sentence defense; neither is a bare concession. B's honest defense ("a deliberate bet that killing 1,585 escalations is worth absorbing ~$15,838 in expected fraud loss") only holds once it stops claiming logical equivalence with A — the subagent correctly identified the exact question where B's *equivalence* claim collapses (a row-by-row truth-table challenge), while B's *cost* argument does not collapse outright. |
| P3 trap | **PASS** | Fresh subagent named the case's central trap (treating ¬p∧¬q∧r and ¬p∨¬q∨r as "basically the same negation") from case.md alone, before reading FACILITATOR.md — then confirmed FACILITATOR.md names the same trap nearly verbatim, plus independently surfaced the guide's second trap (stopping at the truth table without pricing D4's cost). |
| P4 twist | **PASS** | Fresh subagent independently re-derived the De Morgan negation, built all 8 rows of both rules, confirmed A and B agree on only 2 of 8 rows, and confirmed no defensible alternate reading of Appendix A/B's text produces equivalence — the twist is mathematically airtight, not a technicality, and invalidates a real room's plausible pre-math "it's just reworded" position. |
| P5 sensitivity | **PASS (disclosed)** | Machine-run `sensitivity_model.py`, `--probe 5`. Base: A=$14,400.00, B=$15,972.95, margin **9.8%** (winner A). The 8 request-volume category counts (MA1) are stable (~9.8–9.9% margin, never flip, never breach the 20% cap). Two dials are genuinely unstable — `cost_per_escalation` (+50% flips to B, 25.7% margin) and `avg_value_at_risk` (−50% flips to B, 44.1% margin) — both disclosed in `case.json.sensitivity_disclosure[]` as Category X with a real justification ≥20 chars. Script verdict: `PASS (disclosed)`. |
| P6 data decay | **PASS** | All 4 `sources[]` URLs fetched live during this session (the QA sandbox itself has no outbound network, so this was done directly rather than delegated): S1 (Microsoft Learn) reachable, exact quoted text confirmed; S2 (Appriss Retail) reachable, exact "15.14%" figure confirmed; S3 (Salesforce Architects) reachable, exact quote confirmed; S4 (Ringly.io) reachable, Gartner ($13.50) and Opensend ($2.70–$5.60) figures confirmed. **A real defect was found and fixed**: the $6–$12 small-store range had been mis-attributed to "Gorgias" in the initial draft; the live re-fetch showed this range is Ringly.io's own benchmark assessment (Gorgias is credited only for ticket-volume data on that page), not a Gorgias-published figure. Corrected in `case.md` (Appendix F, Modeling Assumptions), `case.json.sources[S4]`/`modeling_assumptions[MA3]`, and `RESEARCH_LOG.md`. 0 dead links, 0 days old (all fetched same-session). |
| P7 accessibility | **FAIL (structural, pre-publish)** | Mechanical pre-screen: 0 deliverables use sketch/diagram/graph language, so no missing-visual finding. Model-judged cold-read: no `published/` directory exists (case-publish out of scope for this run), so the probe fell back to a plain-text `case.md` packet with no `STORY_GLOSSARY` hover mechanism. A fresh, zero-context subagent named well over 20 unexplained real-world terms (AI Operations Lead, VP of Customer Operations, "the board deck," agentic-workflow platform, configuration console, account tenure, cost per contact, Modeling Assumption apparatus, etc.) — far past the 2-concept FAIL threshold. **This is an expected, documented limitation of running Tier 2 without `case-publish`, not a defect in the case's content** — SKILL.md's own P7 documentation states the case.md fallback exists "so a case mid-pipeline isn't broken by this," implying the real remediation (a `STORY_GLOSSARY` built into the Interactive HTML) happens at `case-publish` time. **Not waived** — no `qa.tier2.P7_waiver` is recorded, since a waiver requires real remediation rounds this task's scope does not include. Recommendation for whoever runs `case-publish` next: build `published/`'s Interactive HTML with a `STORY_GLOSSARY` covering at minimum the terms this cold-read flagged (AI Operations Lead, VP of Customer Operations, board deck, agentic-workflow platform, configuration console, account tenure, cost per contact, escalation, Modeling Assumption), then re-run P7 before publishing. |

### Tier 3 — human dry-run

NOT RUN. No `cases/the-approval-gate/runs/` directory exists yet; this case has not been assigned to a real cohort. `PUBLISHED` (once reached) does not require this; `VERIFIED` does.

## Real defects found and fixed during this pass

1. **T1-13 mechanical miss (self-corrected before final Tier 1 run):** the first draft of FACILITATOR.md's five Socratic questions wrapped each question onto two lines, so `tier1_structural.py`'s line-anchored `\?$` regex counted 0 questions instead of 5. Fixed by reformatting each question onto a single line — a real authoring-format defect the mechanical check caught, not a false positive.
2. **Margin-formula sign error (self-corrected before Tier 2 P5 was finalized):** because this case's primary metric is *lower-cost-wins* (unlike most of the corpus's higher-is-better metrics), an initial hand computation divided the margin by the **winner's** cost ($14,400, giving 10.9%) instead of the corpus-standard convention of dividing by the **loser's** cost ($15,972.95, giving the correct 9.8%) — the same convention `tier2_probes.py`'s `probe_sensitivity` uses. Caught by cross-checking the official P5 script output against the hand-written `case.json.balance`/`FACILITATOR.md` numbers; corrected everywhere (`case.json.balance.margin_pct`, `case.json.derived.margin_pct`, `case.json.sensitivity_disclosure[]`'s flip percentages, and `FACILITATOR.md`'s margin section). The case's real margin is **9.8%**, still within the approved concept's 8–15% target band.
3. **Source misattribution found during Tier 2 P6 (data decay):** the $6–$12 small-ecommerce-store cost-per-contact range was originally credited to "Gorgias" in `case.md`/`case.json`. A live re-fetch of the Ringly.io source page during P6 confirmed this range is Ringly.io's own benchmark assessment, not a quote from Gorgias (Gorgias is credited on that page only for ticket-volume/order-count data). Corrected in `case.md`, `case.json.sources[S4]`/`modeling_assumptions[MA3]`, and `RESEARCH_LOG.md`. Did not change MA3's chosen $9.00 value or any downstream arithmetic — only the attribution.

## case.json.qa (written by this report)

```json
{
  "state": "TIER1_PASS",
  "verdict": "PASS",
  "run_on": "2026-09-09",
  "blockers_open": 0,
  "gaps_open": 1,
  "tier2": {
    "P1": "PASS",
    "P2": "PASS",
    "P3": "PASS",
    "P4": "PASS",
    "P5": "PASS (disclosed)",
    "P6": "PASS",
    "P7": "FAIL (structural, pre-publish -- see Tier 2 table above; not waived)"
  },
  "tier3_runs": [],
  "case_md_sha256": "e570404dc3245484dbcd0fe30c8f4f5ede34d5285a8c6a0bf0d769003fc56847"
}
```

**Note on state:** six of the seven Tier 2 probes (P1–P6, the full set achievable without running
`case-publish`) are genuinely clean, several adjudicated by fresh unbriefed subagents per the
no-self-grading rule. P7 cannot be fairly evaluated (or waived) without the Interactive HTML that
`case-publish` builds — this is a scope boundary of this pipeline run, not a defect discovered in
the case's math, sourcing, or balance.

**Reconciliation, 2026-09-09 (Batch C QA pass):** this task's own instructions define the readiness
gate as "the six Tier 2 probes" (P1–P6) — P7/MCS-48 postdates that instruction and, per a live
corpus check this same session, is inconsistently recorded across the existing corpus (most
already-`TIER2_PASS` cases published before 2026-09-03 carry no `P7` key at all; several published
after that date reached `TIER2_PASS` with `P7: None`). To keep this batch internally consistent with
that live precedent and with the task's own explicit 6-probe scope, `qa.state` is updated here from
`TIER1_PASS` to **`TIER2_PASS`** — the P1–P6 verdicts above are unchanged, and P7's structural FAIL
finding (a real, disclosed, not-waived gap tied to `published/` not existing yet) is preserved
verbatim in the Tier 2 table rather than deleted or silently upgraded. This case proceeds to
`case-publish`; P7 should be genuinely re-run against the resulting Interactive HTML once it exists,
and any real accessibility gap it finds remediated on its own merits, independent of this
reconciliation.

---

## P7 re-run — 2026-09-09 (post case-publish)

`case-publish` built `published/The Approval Gate - Interactive.html` (plus the Case Study/Data/
Facilitator Guide docx/xlsx, all verified against the current `case.md`). With the Interactive HTML
now in place, P7 was re-run for real per `skills/case-readiness/SKILL.md`'s P7 procedure, exactly as
the reconciliation note above committed to.

**Mechanical pre-screen** (`tier2_probes.py --probe 7`): 1 real visual found (the Working Notebook's
two interactive 8-row truth tables, matching Challenge 3 D1's own truth-table deliverable) — clean.

**Cold-read round 1** (fresh, zero-context subagent, packet built from the published HTML per P7's
contract — not from `case.md`): named 4 unexplained real-world concepts —

1. "the board deck" (Slack quote) — not explained what a board deck is.
2. "trailing 90-day window" (Appendix A) — "trailing" mechanics not spelled out.
3. Why [S2]'s industry-wide retail return-fraud rate is applied to this company's own
   auto-approved-mistake category — the transfer was asserted, not bridged.
4. "'assisted' (human-handled) contacts" (Appendix D / MA3) — jargon used as if self-evident.

4 named concepts is past the 0-1 pass threshold — **FAIL**.

**Remediation** (in the interactive HTML only — `case.md` stays untouched at its already-QA'd hash):

- Added `STORY_GLOSSARY` entries `"Board Deck"` (linking Wikipedia's *Board of directors* article)
  and `"Assisted"` (linking NICE's *Contact Center Self-Service Options* glossary page), both
  fetched and confirmed live 2026-09-09.
- Added an inline side-note under Appendix A clarifying the rolling/trailing 90-day window mechanic.
- Added an inline side-note under Appendix D bridging why the sourced industry-wide fraud rate [S2]
  is used as a proxy for Foothill Outfitters' own risky-request category, and flagging it as a
  legitimate point to challenge.

Re-ran `tier1_structural.py` after the edit: unchanged `TIER1_PASS`, 0 blockers, T1-18/T1-19/T1-20/
T1-21 all still PASS.

**Cold-read round 2** (a second fresh, zero-context subagent, packet rebuilt from the corrected
HTML): named **0** unexplained real-world concepts — every term it considered flagging turned out to
already be explained inline, including all four terms fixed above. Genuine **PASS**, no
`P7_waiver` needed (unlike Cardiology's disclosed-partial precedent, this case reached a clean pass
on round 2 rather than requiring a documented partial-disclosure waiver).

### Final QA state

```json
{
  "state": "TIER2_PASS",
  "verdict": "PASS",
  "run_on": "2026-09-09",
  "blockers_open": 0,
  "gaps_open": 1,
  "tier2": {
    "P1": "PASS",
    "P2": "PASS",
    "P3": "PASS",
    "P4": "PASS",
    "P5": "PASS (disclosed)",
    "P6": "PASS",
    "P7": "PASS"
  },
  "tier3_runs": [],
  "case_md_sha256": "e570404dc3245484dbcd0fe30c8f4f5ede34d5285a8c6a0bf0d769003fc56847"
}
```

All seven Tier 2 probes are now genuinely PASS. The one remaining GAP (T1-10, the reinforcement
carve-out) is unchanged and pre-existing — not related to P7.
