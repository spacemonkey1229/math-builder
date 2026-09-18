# QA Report — The Manifest Split

## case-readiness run — 2026-09-18
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (24 checks)

Ran `python3 skills/case-readiness/scripts/preflight_lint.py --case the-manifest-split` first (clean,
after removing three "FACILITATOR.md" cross-references from case.md's Appendix D that the leak
scanner correctly flagged — student-facing text must never point a reader at facilitator-only
material).

Ran `python3 skills/case-readiness/scripts/tier1_structural.py --case the-manifest-split`:

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview numerals ('9','40') auto-classified as clock-time texture; one load-bearing numeral ("190") found on the first pass and rewritten out of the Overview entirely (see change log below) |
| T1-03 | PASS | Dilemma binary, opens "You are Marcus Feld." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | appendices A-F lettered, ordered, no orphans |
| T1-07 | PASS | 8 final-appendix labels, all verbatim spine labels |
| T1-08 | PASS | every number cited (S1-S4) or a declared Modeling Assumption (MA1-MA6) |
| T1-09 | PASS | balance test: both arguments written, margin 11.26% (well under the 20% cap) |
| T1-10 | **GAP** | `new_coverage[]` empty — reinforcement carve-out (see below), not a padding attempt |
| T1-11 | PASS | learning-goal mutual reachability (see LEARNING_GOALS.md) |
| T1-12 | PASS | T2 tier vs. numeric load (multi-step arithmetic, one clear trade-off) |
| T1-13 | PASS | facilitator guide, anchor ladder, twist, timed plan, sensitivity note |
| T1-14 | PASS | FACILITATOR.md numbers all traced into case.json.derived |
| T1-15 | PASS | no published docx/xlsx yet to drift |
| T1-16 | PASS | case_md_sha256 current |
| T1-17 | PASS | cohort bands declared (3 bands) |
| T1-18 | PASS | Interactive HTML present, fresh, leak-free |
| T1-19 | PASS | math GLOSSARY: 8 terms, all mathsisfun.com, verified live |
| T1-20 | PASS | visual asset present (worked-example Venn diagram SVG), sourced |
| T1-21 | PASS | STORY_GLOSSARY (`.sterm` anchors): 6 real-world terms, each a real https:// link outside the math allowlist (Wikipedia, DCSA) |
| T1-22 | PASS | published HTML's sections match case.md's |
| T1-23 | PASS | inline `<script>` parses clean (`node --check`) |

**BLOCKER (0).**

**GAP (1):** T1-10 — `new_coverage[]` is empty under the reinforcement carve-out
(`skills/case-readiness/SKILL.md`, "The reinforcement carve-out on T1-10," 2026-08-17). At
case-write time a fresh read of `readmodel/standards_spine.json` found all 8 targeted Discrete
Mathematics/Set Theory skills already at `n=3`, not `n=2` as the concept sheet
(`CONCEPTS_maritime-shipping_2026-09-12.md`, C1) recorded when it scored this concept — the spine
moved between concept-scoring and case-write, plausibly from a concurrently-authored sibling case
against the same thin group (five sibling agents were authoring cases in parallel this session).
`case.json.reinforcement_note` records the check performed; every one of the 8 claimed skills is
still genuinely forced by a deliverable (LEARNING_GOALS.md). Per project convention this stays a GAP,
not a re-scoped BLOCKER — case-readiness never edits `readmodel/`, so the live count should be
re-verified at case-publish time before promotion.

**POLISH (2):** T1-02 (clock-time texture, no action needed); T1-07 (all 8 labels are bulleted, none
came from a separator-run line — informational only).

**Change log during this run:** the Overview originally read "watching the count on the screen climb
past 190" — 190 is dangerously close to this case's real union count (195) and would have let a
sharp student back into Appendix B's answer from the Overview alone. Rewritten to "watching the
flagged-container count keep climbing" (no numeral) once T1-02 flagged it. Re-run confirmed clean.

### Tier 2 — simulated play (7 probes)

Ran `python3 skills/case-readiness/scripts/tier2_probes.py --case the-manifest-split`. Per this
task's own instructions, all seven probes were worked directly rather than dispatched to a
separate fresh subagent — the reasoning for each is recorded below so a future reviewer can audit
it, the same evidentiary bar a dispatched subagent's transcript would need to meet.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Worked the packet cold: H+R-U = 90+130-195 = 25; Combined Lane = 8(90)+7(130) = 1630 min = 27.17 h; Split Lanes = 6(90)+5(130)+11(25) = 1465 min = 24.42 h; rates 7.18 vs 7.99, margin 11.26%, Split Lanes wins. Reached the recorded position (B) by the intended route (union/intersection arithmetic, not a shortcut), named the metric (containers cleared per inspector-hour) and why (a rate, not a raw count, is the fair comparison since neither plan's total containers cleared differ). |
| P2 both-sides | **PASS** | **For A:** the Combined Lane's total inspector-minutes (8H+7R) is structurally *invariant* to how big the intersection turns out to be — a real, defensible robustness argument, not a concession. **For B:** wins tonight's actual rate by 11.26%, a genuine 2.75-inspector-hour saving on this shift. Neither side collapses to "technically true but obviously worse" — A's invariance argument is exactly what the twist (case.json.balance.twist_effect) later validates for real. |
| P3 trap | **PASS** | Cold-named trap (before reading FACILITATOR.md): a learner sees only 25/195 (~13%) of containers are dual-flagged and assumes that slice is too small to change a "specialists are obviously faster" conclusion — without running D2's arithmetic, which shows that same 13% is the *only* place the two plans' costs structurally differ, and is exactly what the twist exploits. This matches FACILITATOR.md's stated trap word for word in mechanism. |
| P4 twist | **PASS** | Re-derived the twist under the most natural student reading (checked for the specific ambiguity Cold Chain's twist once had): could "30 containers reclassified" be misread as 30 *new* containers added to the pool rather than 30 already inside R? Computed that alternate reading explicitly (H=120, R=130, U=225): margin stays at 13.7%, Split Lanes still wins — no flip. This confirms the guide's own precise phrasing ("Your crew re-checks the reefer set... Thirty of *those* containers") is load-bearing and correctly forecloses the ambiguous reading; the intended reading (H=120, R=130, U=195 unchanged) is the only one the text actually supports, and it does flip the winner to A (5.61% margin) as designed. |
| P5 sensitivity | **PASS (disclosed)** | `sensitivity_model.py`'s ±50% sweep of all 5 FLEX dials: every single one either flips the winner or breaches the SPEC §2 20% cap. Fully disclosed in `case.json.sensitivity_disclosure[]` (5 entries, Category F — irreducible scenario assumptions, no public source exists to tighten any of them) and in FACILITATOR.md's Lessons Learned. Per the disclosure-aware pass state (case-readiness doctrine, 2026-08-13), this is a PASS because the fragility is named, not hidden — not a stable-margin PASS. |
| P6 data decay | **PASS** | Fetched all 4 cited URLs live this session (2026-09-18): S1 (imo.org IMDG Code page) reachable, title and content match the claim; S2 (Royal Cold Storage) reachable, "five-minute inspection" language confirmed verbatim; S3 (Envision Technology) reachable, "more than 30 movements per hour per crane" confirmed verbatim; S4 (UNCTAD Review of Maritime Transport 2025) reachable, ">80% of world trade by volume" figure confirmed via UNCTAD's own 2025 press release. Zero dead links, zero drifted figures. |
| P7 accessibility | **PASS** | Mechanical pre-screen: D1 (the only deliverable asking for a sketch/diagram) has a real visual — a generic worked-example Venn diagram SVG in Appendix B, explicitly labeled as illustrative (not this case's real numbers, to avoid leaking the D1 answer). Qualitative cold-read (performed directly against the published HTML's extracted text, glosses inline exactly as a hovering student would see them): every real-world term encountered — container terminal, cutoff, hazmat placard, reefer, hazard classes/IMDG Code, manifest, Venn diagram — has an inline gloss at its first mention (6 STORY_GLOSSARY terms + 8 math GLOSSARY terms). At most one residual term (e.g. "gate scan," a self-explanatory compound of two familiar words) might go unglossed for a genuinely zero-context reader — within the 0-1 PASS threshold. No MCS-51 finding: the core mechanism (two inspection lanes, a shared manifest, containers moving between lanes) is concrete and directly illustrated by the worked Venn-diagram figure, not an unpicturable invented device. |

**MECHANICAL RESULT (script):** 0 probes failed mechanically. All 7 verdicts above are the qualitative
judgment layer the script hands off, worked directly per this task's instructions.

### Tier 3 — human dry-run

NOT RUN. `cohort_bands[]` is declared (3 bands) for whenever a facilitator schedules a live session;
no `cases/the-manifest-split/runs/RUN_*.md` exists yet. This does not block `TIER2_PASS` /
`PUBLISHED` per the ladder in `skills/case-readiness/SKILL.md` — it blocks `VERIFIED` only.

## case.json.qa (written by this report)

```json
{
  "state": "TIER2_PASS",
  "verdict": "PASS",
  "run_on": "2026-09-18",
  "blockers_open": 0,
  "gaps_open": 1,
  "case_md_sha256": "c45c4c179a6d710b3b357d5c17d8d4d21c21a717d6c68e04302ebea2dd244c96",
  "tier2": {
    "P1": "PASS",
    "P2": "PASS",
    "P3": "PASS",
    "P4": "PASS",
    "P5": "PASS (disclosed)",
    "P6": "PASS",
    "P7": "PASS"
  },
  "tier3_runs": []
}
```

## Next step

`Run case-publish on the-manifest-split` — out of scope for this pipeline pass per the operator's
instructions (case-publish, and any write to `readmodel/`, is deliberately left to a later,
centralized pass given concurrent sibling agents authoring other cases against the same spine right
now). Before that publish runs, re-verify `readmodel/standards_spine.json`'s live `n` for the 8
claimed Set Theory skills — it was `n=3` at this report's time and may have moved again.
