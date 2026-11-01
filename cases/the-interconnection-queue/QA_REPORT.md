# QA_REPORT.md — The Interconnection Queue

## Addendum — citation fix + Interactive HTML + P7 first run — 2026-09-09

**P6 citation-wording fix.** Appendix F row S3 originally mis-cited a paraphrase ("AI campuses at
500 MW or more become transmission-planning events") as if it were a direct quote from DOE's draft
National Transmission Needs Study itself. Re-fetching the same Data Center Knowledge article live
confirmed the actual verbatim sentence is: *"At 500 MW or more, transmission is not a downstream
interconnection issue... The campus itself becomes a transmission-planning event"* — said by **Ihab
Osman**, an independent strategist specializing in data center and other mission-critical
infrastructure, quoted *in* the article's coverage of the DOE study, not a line from the DOE study's
own text. Corrected `case.md` (Appendix F table + the confidence-rationale paragraph),
`case.json.sources[S3]` (value/org/title/note), and appended a correction note to
`RESEARCH_LOG.md` (original entry left intact for the audit trail). `published/The Interconnection
Queue - Case Study.docx` was rebuilt (edited `word/document.xml` directly for the same two text
runs, re-validated, re-rendered to PDF and grepped for "Osman"/"500 MW" to confirm the fix landed).

**Interactive HTML built** (`published/The Interconnection Queue - Interactive.html`, the missing
packet piece) from `templates/interactive_shell.html` per `templates/INTERACTIVE_HTML_CONTRACT.md`.
The JS `PARAMS`/`evaluate()`/`evaluate_twist()` is a direct port of `sensitivity_model.py`, but
using an exact `{n, d}` fraction object — never a JS float — for every capacity figure, so every
number a student sees on the page stays in fraction/mixed-number form exactly as `case.md` demands.
Verified against a standalone Node.js run of the identical fraction library: remaining = 27/8,
stranded A = 1/2, combined B = 35/12, stranded B = 11/24, total demand (D1) = 61/8 — exact match to
`case.json.derived` and `case.json.balance.margin_pct` = 8.33%, winner B. The Twist section
demonstrates FACILITATOR.md's own named trap (subtracting fraction parts without regrouping/
borrowing) as a live, computed side-by-side comparison rather than stating the case's verdict as a
literal — confirmed live that the no-borrow shortcut coincidentally matches the correct D2 answer
(1/2 block) but diverges at D4 (13/24 vs. the correct 11/24), exactly as `FACILITATOR.md` describes.
Added an 8-term math `GLOSSARY` (Common Denominator, Unlike Denominators, Mixed Number, Improper
Fraction, Regrouping, Numerator, Denominator, Least Common Denominator) and a 5-term
`STORY_GLOSSARY` (interconnection queue, substation, MW, FERC, transmission-planning event), all
URLs fetched and confirmed live this session. `tier1_structural.py --case the-interconnection-queue`
now reports **TIER1_PASS, 0 BLOCKER, 2 GAP** (T1-10 reinforcement carve-out; T1-15 the same
SPEC-section/HH:MM-time false-positive class already waived on other cases in this corpus) — T1-18/
T1-19/T1-20/T1-21 all PASS.

**P6 re-run** (data decay, post-fix): all 5 `sources[]` URLs re-fetched live and re-confirmed
reachable and figure-bearing — S1/S2 (55-month/4.5-year 2024 queue wait, ~2,290 GW total queue
capacity), S3 (now the corrected verbatim Ihab Osman quote, confirmed word-for-word), S4 (FERC Order
2023 cluster-study language), S5 (RMI's ~20 MW threshold). Fix holds; no drift.

**P7 accessibility cold-read — first run.** Mechanical pre-screen: READY (Deliverable D5 asks for a
visual; the Working Notebook's Step 5 worked-example `<svg>` matched). Qualitative cold-read:
dispatched a genuinely fresh, zero-context subagent against the *published HTML's own rendered
text* (glossary hover-definitions inlined per `tier2_probes.py`'s `build_html_cold_read_packet()`),
told only the protagonist/setting and primary metric, asked to list any real-world (non-math) term
or concept it could not picture or understand. Result: **at most one** unexplained concept named
("engineering study / engineering-cleared" — used as a pass/fail gate but never itself explained);
every other domain term (substation, interconnection queue, capacity block, transmission-planning
event, megawatt, stranded capacity) was confirmed understandable from the page's own inline
glosses. 0–1 named concepts is a genuine PASS per MCS-48's pass criteria — no remediation round or
waiver needed. `case.json.qa.tier2.P7` set to `"PASS"`.

`resync_artifacts.py` run afterward to bring `case.json.qa.case_md_sha256` current with the edited
`case.md` and touch every published artifact's mtime forward. Final state: `qa.state` =
`TIER2_PASS`, `qa.verdict` = `PASS`, all 7 Tier 2 probes PASS, Tier 1 `TIER1_PASS` with 0 blockers.
Per this task's instruction, `case-publish`'s read-model promotion stage was not run by this task,
and no other case's files were touched.

## case-readiness run — 2026-09-09

**State:** `TIER1_PASS` → `TIER2_PASS`
**Verdict:** TIER2_PASS — 0 BLOCKERs, 2 GAPs (T1-10 reinforcement carve-out; T1-16 first-run hash
recorded) · Tier 2: P1–P6 all PASS

### Tier 1 — structural (21 checks)

```
python3 skills/case-readiness/scripts/tier1_structural.py --case the-interconnection-queue
```
0 BLOCKERs. GAPs: T1-10 (`new_coverage[]` empty; `reinforcement_note` present — this case's mixed-
number/fraction arithmetic genuinely does not reach any other uncovered adjacent skill); T1-16 (no
`case_md_sha256` recorded yet — first gate run, expected). 7 POLISH items (Overview clock/number
texture, T1-07 separator note, 5x "no `published/` dir yet").

**VERDICT: TIER1_PASS — 0 blockers, 2 gaps.**

### Tier 2 — simulated play (6 probes, per this task's scope)

| Probe | Verdict | Finding |
|---|---|---|
| **P1 — Cold solve** | **PASS** | A genuinely fresh, unbriefed subagent read only `/tmp/coldsolve-the-interconnection-queue/PACKET.md`. Chose **B** (hold for the combined Cobalt Peak + Fenwick Yards bids), correctly named the metric (capacity stranded as a fraction of a block), and reproduced the exact fraction arithmetic independently: remaining capacity 3‑3/8 blocks; Option A stranded 1/2 block (3‑3/8 − 2‑7/8, requiring borrowing/regrouping); combined B bids 2‑11/12 blocks, Option B stranded 11/24 block; margin = (1/2−11/24)/(11/24) — the subagent reported the case's own convention (≈8.33%). It independently flagged the confirmation risk on two separate, non-cleared bids as the strongest argument against B, and correctly named the two-bid-confirmation-risk assumption (not any MW figure) as the case's true sensitivity driver — consistent with `sensitivity_model.py`'s own finding that the MW block-size assumption cancels out algebraically. Reached the case-of-record answer for the case-of-record reasons. |
| **P2 — Both-sides solve** | **PASS** | Neither side collapses. A's best sentence: Aurora Ridge is cleared and ready to sign today — zero confirmation risk — while B requires two independent, not-yet-engineering-cleared bids to both land before the queue deadline, and a single miss turns B's razor-thin 1/24-block paper edge into a strictly worse outcome (an idle slot). B's best sentence: on the numbers actually in hand today, B strands measurably less capacity (11/24 vs. 1/2 block) and that gap, however thin, is real, computed, disclosed arithmetic, not an estimate — and `sensitivity_model.py` confirms the MW block-size assumption (the only stated dial) cannot flip it even swept 3x/0.1x. The case's real crux is confirmation-risk tolerance, not the arithmetic itself, which is the concept sheet's intended tension. |
| **P3 — Trap check** | **PASS** | Fresh subagent (blind to `FACILITATOR.md`) independently predicted the exact trap the guide names: subtracting 3/8 from 7/8 (the wrong way) instead of regrouping the borrowed whole block, which coincidentally produces the same numeric answer (1/2) as the correct method at this specific step but would not generalize to D3/D4's uglier denominators. `FACILITATOR.md` names this trap almost verbatim, including the "coincidentally the same numeric answer" framing. Guide's stated trap confirmed present and would actually catch a room. |
| **P4 — Twist integrity** | **PASS** | (a) The twist (the true A-vs-B margin is exactly 1/24 of a block, the smallest fractional unit in the case) invalidates the confident "B is obviously the better fit" position a room reaches after D4, since it shows a single regrouping error upstream (the same error P3's trap describes) could silently flip which option looks better without anyone noticing. (b) Survives a natural student reading: `sensitivity_model.py` confirms algebraically that the case's one stated assumption (MA1, block-size MW) cancels out of the block-unit comparison and cannot flip the winner even at extreme flex; the fourth bid (Briar Hollow) that a student might wonder whether to net out is explicitly addressed in the text ("queue data Renata has to look at and set aside"), so no unstated convention is required. |
| **P5 — Assumption sensitivity (±50%)** | **PASS** | `sensitivity_model.py --probe 5 --flex 0.5`, sweeping the 1 declared dial (`block_size_mw`). Base: A=-0.5, B=-0.46 (stranded-block metric, lower is better), margin 8.3%, winner B. **Both ±50% flex points (12 MW and 36 MW) leave the winner and margin completely unchanged (8.3% both times)** — the block-size assumption is definitionally scale-invariant in a block-fraction comparison, exactly as `sensitivity_model.py`'s own module docstring predicts. Clean machine PASS, not disclosed — no instability found, none to disclose. |
| **P6 — Data decay** | **PASS** | All 5 `sources[]` URLs fetched live this session (2 rows share one URL, loopback.systems). **Confirmed reachable and figure-bearing, all figures verbatim-present**: S1/S2 (loopback.systems Berkeley Lab queue report — 55-month/4.5-year 2024 median vs. 22 months in 2008 confirmed exactly; ~2,290 GW total active queue capacity confirmed exactly). S3 (datacenterknowledge.com — "500 MW or more...the campus itself becomes a transmission-planning event" confirmed verbatim). S4 (klgates.com — FERC Order 2023's shift to "first-ready, first-served" cluster-study process from serial first-come-first-served confirmed, matching the case's characterization). S5 (rmi.org — "approximately 20 megawatts (MW)" transmission-vs-distribution threshold confirmed verbatim). No dead links, no drifted figures, all sources 0 days old as of this session. |

**MECHANICAL RESULT: 6 of 6 in-scope probes PASS.** `case.json.qa.state` set to `TIER2_PASS`.

### Tier 3 — human dry-run

NOT RUN (not published this pass, per task scope).

## Summary for the project owner

The Interconnection Queue is a clean, thin (8.33%), robust dilemma: its one stated assumption
(block-size MW) provably cancels out of the comparison and cannot move the verdict at any flex, so
the case's real fragility is entirely in the *arithmetic method* (the borrow/regroup trap, confirmed
independently by a fresh solver and matched exactly by the guide's own named trap) rather than in
any disclosed real-world uncertainty. All 5 cited sources were fetched live and confirmed
figure-accurate with no drift or dead links. **Recommended next step:** `case-publish` (with its own
two required human confirms).
