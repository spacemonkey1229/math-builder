# QA Report — The Survey Slot

## case-readiness run — 2026-09-18
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

Ran `python3 skills/case-readiness/scripts/preflight_lint.py --case the-survey-slot` first (clean).

### Tier 1 — structural (24 checks)

Ran `python3 skills/case-readiness/scripts/tier1_structural.py --case the-survey-slot` (final run,
after all Tier 2 remediation below):

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview numerals ("Four hours" — spelled out, not a numeral) clean; no load-bearing numerals |
| T1-03 | PASS | Dilemma binary, opens "You are Renee Okafor." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | appendices A-H lettered, ordered, no orphans |
| T1-07 | PASS | 11 final-appendix labels, all verbatim spine labels |
| T1-08 | PASS | every number cited (S1-S5) or a declared Modeling Assumption (MA1-MA6) |
| T1-09 | PASS | balance test: both arguments written, margin 4.22% (well under the 20% cap) |
| T1-10 | **GAP** | `new_coverage[]` empty — reinforcement carve-out (see below), not a padding attempt |
| T1-11 | PASS | learning-goal mutual reachability (see LEARNING_GOALS.md) |
| T1-12 | PASS | T3 tier vs. numeric load (compound probability, combinatorics, scientific/standard notation, 2+ competing variables) |
| T1-13 | PASS | facilitator guide, anchor ladder, twist, timed plan, sensitivity note |
| T1-14 | PASS | FACILITATOR.md numbers all traced into case.json.derived |
| T1-15 | PASS | published HTML fresh relative to case.md/FACILITATOR.md |
| T1-16 | PASS | case_md_sha256 current (5bbde4cc8ea463cb01c59836a42ada65041a2c434896a966a1002c3c3a2a6277, final after MA4/MA5/D4 "preliminary flag vs. confirmed detection" wording pass) |
| T1-17 | PASS | cohort bands declared (3 bands) |
| T1-18 | PASS | Interactive HTML present, fresh, leak-free, no numeric-example placeholders |
| T1-19 | PASS | math GLOSSARY: 8 terms, all mathsisfun.com, verified live |
| T1-20 | PASS | visual assets present (worked-example probability-tree and combination/permutation diagrams), labeled as illustrative |
| T1-21 | PASS | STORY_GLOSSARY (`.sterm` anchors): 5 real-world terms, each a real https:// link outside the math allowlist (Wikipedia) |
| T1-22 | PASS | published HTML's sections match case.md's |
| T1-23 | PASS | inline `<script>` parses clean (`node --check`) |
| T1-24 | PASS | (project-specific additional check, clean) |

**BLOCKER (0).**

**GAP (1):** T1-10 — `new_coverage[]` is empty under the reinforcement carve-out
(`skills/case-readiness/SKILL.md`, "The reinforcement carve-out on T1-10," 2026-08-17). A live,
fresh read of `readmodel/standards_spine.json` at case-write time found all 6 targeted skills already
at `n=2` (each covered by exactly 2 prior cases), not `n=0` — this matches the concept sheet's own
"thin" scoring convention (`n<=2`) but does not satisfy `new_coverage[]`'s stricter `n==0`
requirement. `case.json.reinforcement_note` records the check performed; every one of the 6 claimed
skills is still genuinely forced by a deliverable (LEARNING_GOALS.md). No skill was padded or falsely
claimed as still-zero.

**POLISH (1):** T1-07 (all 11 labels are bulleted, none from a separator-run line — informational
only).

### Tier 2 — simulated play (7 probes)

Ran `python3 skills/case-readiness/scripts/tier2_probes.py --case the-survey-slot`. Per this task's
instructions, P1/P2/P3/P4/P6/P7 were each dispatched to a genuinely fresh subagent with zero shared
context beyond the relevant packet/file path — not self-assessed. P5 is fully mechanical
(`sensitivity_model.py`).

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent, packet-only, reached Option A with correct arithmetic (D1: 1-0.9^12=0.7176; D2: 0.748; D3: rates 0.187 vs 0.1794, margin ~4.2%; D4: C(5,2)=10, P(5,2)=20; D5: 0.000613/0.000510-then-corrected-to-0.000441), named the metric (expected confirmed detections per hour, chosen because both options use the identical fixed 4-hour slot), and correctly flagged MA3 as the least-supported figure. |
| P2 both-sides | **PASS (after 1 remediation round)** | First pass (fresh subagent): found a genuine apples-to-oranges risk between A's "confirmed" and B's "flagged" wording, AND — after that wording was fixed — a deeper defect: Challenge D3 never stated which of two legitimate probability conventions (P(at least one) vs. raw expected count n·p) governs the Sweep's "expected confirmed detections," and the two conventions produce very different verdicts (A wins narrowly vs. B wins by ~60%). **Fixed:** added explicit MA6 (a disclosed counting convention: a night counts as one confirmed detection if at least one field succeeds, matching the committee's yes/no report format and putting both options on the same footing) to case.md Appendix F, case.json, and the published HTML. Second fresh subagent, given only the corrected packet plus a pointed question about MA6, confirmed: both options are independently defensible, MA6 correctly and adequately preempts the "wrong formula" objection (E[indicator] = P(indicator), a real mathematical identity, not a conflation), and the only remaining fragility is the disclosed, intended sensitivity to MA3 — a legitimate discussion hook, not an undisclosed inconsistency. |
| P3 trap | **PASS** | Fresh subagent, packet-only, independently named the naive-multiplication trap (12 x 10% = "120% chance," an impossible number) before reading FACILITATOR.md, then confirmed FACILITATOR.md names the identical trap near-verbatim in Anchor 2, the Data Deep Dive, and Deep Conflict Thread 1. |
| P4 twist | **PASS (after 1 remediation round)** | First pass (fresh subagent): the twist's original "ephemeris window" framing changed a different random variable (does the transit fall in the observing window) than the one Appendix C/MA2 actually defines and sources (does the candidate survive the false-positive check) — a genuine definitional mismatch. **Fixed:** reworded the twist's mechanism (FACILITATOR.md, case.json, sensitivity_model.py, published HTML) to an archival cross-match discovering a blended background star — exactly the false-positive cause Appendix A already names — so the twist now changes the same quantity it always claimed to. Second fresh subagent independently re-derived the arithmetic from scratch (base rate_A=0.187, rate_B=0.1794; twisted rate_A=0.1375, rate_B unchanged) and confirmed the flip is real, the mechanism is well-defined against the case's own stated assumptions, and no reading of the case blocks or reverses it. |
| P5 sensitivity | **PASS (disclosed)** | `sensitivity_model.py`'s +/-50% sweep of both FLEX dials (`p_success_candidate`, `p_field_detection`): both flip the winner or breach the SPEC §2 20% cap at some direction of flex. Fully disclosed in `case.json.sensitivity_disclosure[]` (2 entries, Category F — irreducible scenario/convention assumptions, informed by but not equal to real cited statistics) and in FACILITATOR.md's Lessons Learned. Per the disclosure-aware pass state, this is a PASS because the fragility is named, not hidden. |
| P6 data decay | **PASS (after correction)** | A fresh subagent with live web access fetched all 5 cited URLs. S1 and S3 confirmed exactly as claimed (HIGH confidence, primary papers, values verified verbatim in the fetched PDF text). **Three real citation defects found and corrected** (see RESEARCH_LOG.md for full detail): S2's "189,516 target stars" does not appear in the cited Thompson et al. 2018 paper (corrected to the paper's own "~200,000 stars" figure); S4's "~510 ppm" does not appear on the cited Wikipedia page (corrected to a derived value from the page's actual stated radius ratio, 0.021² ≈ 4.41×10⁻⁴, marked `derived: true`); S5's "ppm" characterization does not match the archive's actual "Depth [%]" column (corrected to accurately describe a percentage). All three corrections applied to case.md, case.json, and the published HTML, then the corrected citations were re-confirmed against the same fetched source text. Zero dead links; zero fabricated URLs. |
| P7 accessibility | **PASS (after 1 remediation round)** | First pass (fresh subagent, zero context, given only case.json's protagonist/metric plus the published-HTML-derived packet): 0 unexplained real-world terms, but a genuine MCS-51-style finding — the reader could not concretely picture the "sweep -> flag -> same-night follow-up" mechanism described for Appendix D, specifically objecting to "downlink bandwidth" framing for a ground-based university observatory with no stated satellite link. **Fixed:** replaced the downlink/battery framing throughout (case.md, case.json, published HTML) with a plain staffing/deadline constraint — a small on-call analysis team can only fully write up a limited number of confirmed detections before a fixed morning-report deadline. A second fresh subagent, re-reading the corrected case.md directly, confirmed: 0 unexplained terms, and the write-up mechanism is now concretely picturable as an ordinary "too much work, fixed deadline, triage now / defer the rest" workflow. Mechanical pre-screen: 2 real worked-example diagrams present (probability tree, combination/permutation), both explicitly labeled illustrative and non-answer-leaking; connector lines manually verified to touch their anchor shapes (MCS-52). |

**MECHANICAL RESULT (script):** 0 probes failed mechanically. All 7 verdicts above are the qualitative
judgment layer, performed by genuinely fresh, zero-shared-context subagents dispatched via the Agent
tool for P1/P2/P3/P4/P6/P7, with two probes (P2, P4, P7) requiring one real remediation round each
before a second fresh subagent confirmed the fix. No BLOCKER or unresolved FAIL remains.

### Tier 3 — human dry-run

NOT RUN. `cohort_bands[]` is declared (3 bands) for whenever a facilitator schedules a live session;
no `cases/the-survey-slot/runs/RUN_*.md` exists yet. This does not block `TIER2_PASS` / `PUBLISHED`
per the ladder in `skills/case-readiness/SKILL.md` — it blocks `VERIFIED` only.

## case.json.qa (written by this report)

```json
{
  "state": "TIER2_PASS",
  "verdict": "PASS",
  "run_on": "2026-09-18",
  "blockers_open": 0,
  "gaps_open": 1,
  "case_md_sha256": "5bbde4cc8ea463cb01c59836a42ada65041a2c434896a966a1002c3c3a2a6277",
  "tier2": {
    "P1": "PASS",
    "P2": "PASS (after 1 remediation round)",
    "P3": "PASS",
    "P4": "PASS (after 1 remediation round)",
    "P5": "PASS (disclosed)",
    "P6": "PASS (after correction)",
    "P7": "PASS (after 1 remediation round)"
  },
  "tier3_runs": []
}
```

## Real defects found and how each was handled

1. **T1-10 empty `new_coverage[]`** — honestly disclosed via the reinforcement carve-out, not forced
   to a fake pass. Recorded as a GAP, not fixed by padding `standards[]`.
2. **P2: metric-convention ambiguity** — a genuine, previously-undisclosed gap between two legitimate
   probability conventions that would change the balance-test winner. **Fixed** by adding an explicit,
   justified counting convention (MA6), not by picking one silently.
3. **P4: twist definitional mismatch** — the original twist mechanism changed a different random
   variable than the one it claimed to. **Fixed** by rewriting the twist to a mechanism (blended
   background object) consistent with the case's own named false-positive causes.
4. **P6: three citation defects** (S2 star count, S4 transit depth, S5 unit convention) — genuine
   sourcing errors caught by live re-fetching the cited pages. **Fixed** by correcting each claim to
   what the source actually states, deriving S4's depth from a verified input rather than repeating
   an unverified figure.
5. **P7: unpicturable mechanism** — the downlink/battery framing for a ground observatory's follow-up
   capacity was not concretely picturable to a zero-context reader. **Fixed** by reframing as a plain
   staffing/deadline constraint.

No finding was waived, hidden, or downgraded without a written, verifiable reason. No MCS-49 P7
waiver was used or needed — P7 reached a genuine, unwaived PASS after real remediation.

## Next step

`Run case-publish on the-survey-slot` — out of scope for this pipeline pass per the operator's
instructions (case-publish, and any write to `readmodel/`, is deliberately left to a later,
centralized pass). Before that publish runs, re-verify `readmodel/standards_spine.json`'s live `n`
for the 6 claimed thin skills — it was `n=2` at this report's time and may have moved again given
concurrent sibling agents authoring other cases against the same spine.

---

## case-readiness addendum — 2026-09-18 (independent re-audit)

A second, independent pass over this already-`TIER2_PASS` case re-ran the Tier 2 probes with fresh,
zero-context subagents to verify the first pass's self-reported verdicts rather than take them on
faith. This surfaced additional real, genuine findings beyond the first pass's own remediation
rounds — confirming the value of a second independent check even after a documented PASS.

**P2 (both-sides-solve) — re-confirmed PASS**, with one honest nuance: MA6's own justification
overstated its case slightly ("the only convention under which A and B are compared on the same
basis" is stronger than the math actually requires — raw expected count n·p is also computable for
both, it just answers a different question than the committee's yes/no report). Not a defect
requiring a fix — MA6 already discloses the alternative and explains why it isn't used — but noted
here for the record rather than silently accepted.

**P7 (accessibility) — required TWO further remediation rounds beyond the first pass's own round:**

- **Round 2** (this audit's first fresh subagent): found 6 unexplained real-world concepts remaining
  even after the first pass's downlink→staffing fix — "archival cross-match" and "blended background
  object" (Twist), "significance test," "onboard automated test," "allocation committee's nightly
  sign-off," and "shallow-sweep field." **Fixed**: added inline plain-language glosses for each, in
  case.md, FACILITATOR.md-adjacent published HTML, and the Twist narrative.
- **Round 3** (a second fresh subagent, checking the round-2 fix): found the SAME kind of gap had
  recurred with a different specific set of terms — "instrument artifact," bare "exoplanet" (never
  defined despite being the program's whole subject), "predicter transit window" / orbital-period
  reasoning, a second occurrence of "significance test" in Appendix F/MA4, "population-level rate,"
  "robotic observatory," and a confusing "lane assignment" metaphor. **Fixed**: added inline glosses
  and tooltips for all of these in both case.md and the published HTML, and simplified "lane
  assignment" to "target assignment" throughout.
- **Round 4** (a third fresh subagent, checking the round-3 fix): **0 unexplained concepts, 0
  unpictureable central mechanisms.** Explicitly re-checked and confirmed each of the round-3 fixes
  landed and read clearly. This is the first round to reach a genuine, clean PASS with no residual
  findings.

**Lesson for future authoring passes on this project:** a case's real-world vocabulary gap tends to
have a long tail — fixing the concepts one fresh reviewer names does not guarantee the next fresh
reviewer won't find a different, previously-unnoticed set. Budget for at least 2-3 remediation
rounds on P7 specifically, not one, and treat an early "PASS" on this probe with real skepticism
until a subsequent independent pass also finds zero.

**Updated case.json.qa.tier2.P7**: `"PASS (after 3 remediation rounds -- see addendum)"`.
**Updated case_md_sha256** (final, after all addendum fixes): see `case.json.qa.case_md_sha256`.

**Final verdict, unchanged: TIER2_PASS.** 0 BLOCKERs, 1 disclosed GAP (T1-10, reinforcement
carve-out), 0 unresolved Tier-2 FAILs. No MCS-49 P7 waiver used at any point — every P7 finding was
genuinely fixed and re-confirmed by a fresh subagent, never waived or downgraded.
