# QA Report — Perimeter Protocol

## case-readiness run — 2026-08-24
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Preflight lint

`preflight_lint.py --case perimeter-protocol` initially flagged 5 `[leak]` findings — all variants
of one real defect: `case.md` explicitly named "the trap" before students discover it (Appendix E
heading "...and Its Trap," the Background roadmap sentence, Appendix E's own body text, and
Deliverable D4's closing clause). All four student-facing occurrences were reworded to neutral
framing with no "trap"/"twist"/"facilitator" language:
- Appendix E heading → "Appendix E — The Conditional Statement"
- Background roadmap sentence → "Appendix E lays out the conditional statement both rule sets are
  built on."
- Appendix E body → "...and a rule set like Rule Set B can quietly depend on assuming it is true
  anyway" (no "trap"/"twist")
- Deliverable D4 → "...and what that means for whether Rule Set B's assumption is safe"

The 5th finding (line 164, the `<!-- FACILITATOR ONLY -->` HTML comment) is the documented,
corpus-wide false-positive class — an unrendered editorial comment present verbatim in ~20+ other
published cases (`air-traffic-controller`, `acton-survey`, `a-coachs-dilemma`, etc.) — confirmed
not a real leak.

Re-run after fixes: **0 findings.**

### Tier 1 — structural (20 checks)

Initial run: **BLOCKED**, 4 BLOCKERs.
- T1-02: Overview numeral "2" (from "a phone at 2 a.m.") unclear — fixed by recording a clearance
  in `case.json.overview_numerals_cleared[]` (colloquial time-of-day reference, not load-bearing).
- T1-13 (×3): `FACILITATOR.md` was missing the full MCS-14 anchor ladder (Intro/Launch/Anchor
  1-4/Data Deep Dive/Twist/Close/Lessons Learned/Standards Touched On), had no `## Twist` section,
  and had no timed 45-minute Socratic plan — the guide only had the balance argument, Socratic
  questions, and trap note. Rewrote `FACILITATOR.md` to the full required structure, preserving all
  original content (arguments for A/B, the trap, the sensitivity note) and adding Intro, Launch,
  Anchor 1-4, Data Deep Dive, Twist, Close, Deep Conflict, the 45-minute timed plan, Lessons
  Learned, and Standards Touched On.

Re-run after `sensitivity_disclosure[]` and `case_md_sha256` were added: **TIER1_PASS**, 0
BLOCKERs, 2 GAPs (reviewed, both genuinely non-blocking, neither chased further):

| id | result | note |
|---|---|---|
| T1-09 | GAP | margin 16.7% is inside the SPEC §2 20% cap but wide; discussion will lean toward B. Confirmed by P2 below — B's numeric edge is real but the thinner of the two arguments, and P5 shows it is the more assumption-sensitive side. Not retuned: the margin is a real, computed result of the stated Traffic Sample, not an authoring error. |
| T1-14 | GAP | 1 number in `FACILITATOR.md` (1.667, Rule Set A's ratio) doesn't appear verbatim in case.md/case.json — a guide-only derived figure computed from case.json's own `n_pq_true` etc. and checkable via `sensitivity_model.py`, not a stale/drifted value. |

All other checks PASS. T1-15/18/19/20 report "no `published/` directory yet" (POLISH, expected —
this case has not been through `case-publish`).

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent, given only `/tmp/coldsolve-perimeter-protocol/PACKET.md`, built both truth tables and classified all 20 Traffic Sample requests with arithmetic that matches the case's own numbers exactly (A: 10 true threats blocked / 6 false positives; B: 4/2; ratio A=1.67, B=2.0). It named its metric explicitly (threat recall subject to the 20-hour capacity constraint, not the case's stated primary metric) and recommended **Rule Set A** — the opposite of the facilitator's recommended Rule Set B. This is a defensible position reached by valid, shown arithmetic and an explicitly named metric (the pass criterion per `skills/case-readiness/SKILL.md`), not a lucky guess or an arithmetic error — the solver correctly computed the case's own ratio, explicitly considered it, and gave a substantive reason (life-safety stakes in a hospital network) for weighting recall over the ratio instead. This is a genuine, real tension the case's SPEC §2 balance test is built to produce, not a defect — but it is worth flagging for facilitators: a Hero can reach A by a fully defensible route, and D5's instruction to close "on the ratio" should be watched for during Anchor 3/4 if a Hero pushes back on the ratio's framing. |
| P2 both-sides | **PASS** | Both options have real, non-concession, quantitative opening arguments (verified against `case.json.balance` and case.md directly, no "cheaper but worse in every way" phrasing present). A: "blocks 10 of 11 confirmed threats, missing only 1, at a triage cost that's a small fraction of the fixed pool." B: "wins the case's own primary metric outright — 2.0 vs. 1.667 true-threats-per-false-positive, a real 16.7% edge — using a third of A's triage time." Neither side collapses from the packet alone. Under pressure, B's position is the thinner of the two: P5 (below) shows 6 of 8 flexed Traffic Sample dials flip the winner to A or break the SPEC §2 cap, meaning B's numeric edge, while real and correctly computed, rests on the specific hand-built sample more than A's structurally-guaranteed raw coverage does. This is disclosed via `sensitivity_disclosure[]`, not a defect in the balance test. |
| P3 trap | **PASS** | Fresh subagent, given only the packet, independently named the exact trap `FACILITATOR.md` names: a hurried student mislabels the statement Rule Set B implicitly depends on (¬p → ¬threat, the **inverse**) as the contrapositive, then invokes the true fact "the contrapositive is always logically equivalent to the original" to wrongly declare B's dependency safe — when the real dependency (the inverse) is directly falsified by Traffic Sample rows 12, 13, 14, and 17 (unlisted IPs that are genuine threats). This is word-for-word the same mechanism and the same four counterexample rows `FACILITATOR.md`'s trap section names. |
| P4 twist | **PASS** | The twist ("Rule Set A's raw threats-blocked count is guaranteed ≥ Rule Set B's by the OR/AND structure, before any data is looked at — so raw coverage alone can't justify a recommendation") is a pure structural fact of set containment (p AND q ⊆ p OR q), not dependent on any Traffic Sample value. `sensitivity_model.py`'s `evaluate_twist()` confirms `raw_containment_holds == True` under every flex tested in P5, including the ones that flip the ratio-based winner — the twist survives every defensible reading of every stated assumption because it never depended on any of them. It also genuinely invalidates the naive "A blocks more, so A wins" position a first-vote room would hold, forcing the ratio computation that is the case's actual point. |
| P5 sensitivity | **PASS (disclosed)** | `sensitivity_model.py` authored (models the Traffic Sample as 6 p/q-category true-threat/false-positive counts, which correctly preserves the p-OR-q ⊇ p-AND-q containment under any flex, plus MA1's pool and MA3's per-alert minutes). Flexing MA1 and MA3 ±50% moves nothing (neither enters the ratio). Flexing 6 of the 8 MA2 category-count dials ±50% is genuinely unstable: `n_pq_true` -50% and `n_pq_false` +50% both flip the winner to Rule Set A outright; `n_p_notq_false` -50% and `n_notp_q_false` -50% both produce an exact tie; several other flexes push the margin past the SPEC §2 20% cap without flipping the winner. All 6 unstable params are disclosed in `case.json.sensitivity_disclosure[]` as Category F (no real per-hospital firewall log exists or could be published — the true composition is an irreducible unknown, not a research gap), and the finding is now written into `FACILITATOR.md`'s margin-stability note for Anchor 4. This is the same "disclosed, not eliminated" pass state used by `grant-reach`. |
| P6 data decay | **PASS** | All 3 cited URLs fetched live and reachable, all 3 figures confirmed current: S1 (CISA KEV catalog, https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) — confirmed 1,674 entries, catalog version 2026.08.21, matches exactly. S2 (Bitdefender/Ponemon-Exabeam, https://www.bitdefender.com/en-us/blog/businessinsights/every-hour-socs-run-15-minutes-are-wasted-on-false-positives) — confirmed the 25%-of-analyst-time figure attributed to Ponemon/Exabeam, matches exactly. S3 (SecurityWeek/Ponemon-Damballa, https://www.securityweek.com/false-positive-alerts-cost-organizations-13-million-year-report/) — confirmed $1.3M/year, ~21,000 hours/year, 16,937 weekly alerts, 19% reliable, matches exactly. No dead links, no drifted figures. |

### Tier 3 — human dry-run

NOT RUN (blocking only for `VERIFIED`, not for `TIER2_PASS`/`PUBLISHED`).

### Notable findings for facilitators (not defects, disclosed)

1. **P1's cold solver reached Rule Set A, not the facilitator-recommended Rule Set B**, via
   correct arithmetic and an explicitly named, defensible alternative metric (recall under a
   non-binding capacity constraint, reasoned from the hospital-network life-safety framing). This
   is consistent with SPEC §2's balance-test design (both sides must be real) rather than a defect,
   but Anchor 3/4 should be ready for a room that pushes back on why the ratio is "the" metric
   before accepting D5's instruction to close on it.
2. **The margin is genuinely assumption-sensitive** (P5) — disclosed in `case.json` and
   `FACILITATOR.md`, not hidden. If a Hero treats 16.7% as rock-solid, Anchor 4 is where to surface
   this.
