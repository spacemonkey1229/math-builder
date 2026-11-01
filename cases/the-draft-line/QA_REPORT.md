# QA Report — The Draft Line

## case-readiness run — 2026-09-18
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (24 checks)

Ran `python3 skills/case-readiness/scripts/preflight_lint.py --case the-draft-line` first — clean, no
advisory findings.

Ran `python3 skills/case-readiness/scripts/tier1_structural.py --case the-draft-line` (final run, after
the fixes below):

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview numerals ("six hours") auto-classified as texture, no load-bearing numbers |
| T1-03 | PASS | Dilemma binary, opens "You are Aisha Rahman." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | appendices A-G lettered, ordered, no orphans (fixed — see change log) |
| T1-07 | PASS | 5 final-appendix labels, all verbatim spine labels |
| T1-08 | PASS | every number cited (S1-S6) or a declared Modeling Assumption (MA1-MA8) |
| T1-09 | PASS | balance test: both arguments written, margin 0.96% (well under the 20% cap) |
| T1-10 | **GAP** | `new_coverage[]` empty — reinforcement carve-out (see below), not a padding attempt |
| T1-11 | PASS | learning-goal mutual reachability (see LEARNING_GOALS.md) |
| T1-12 | PASS | T3 tier vs. numeric load (multi-variable, compound-unit conversions, one clear trade-off) |
| T1-13 | PASS | facilitator guide, anchor ladder, twist, timed plan, sensitivity note |
| T1-14 | PASS | FACILITATOR.md numbers all traced into case.json.derived (fixed — see change log) |
| T1-15 | PASS | published docx/xlsx built after this run, verified fresh |
| T1-16 | PASS (after finalization) | case_md_sha256 recorded below |
| T1-17 | PASS | cohort bands declared (3 bands) |
| T1-18 | GAP | Interactive HTML present, fresh, leak-free; one illustrative worked-example number (4,000 nm, a made-up distance in the D2 worked-example figure) flagged as an orphan — accepted false-positive class, same as manifest-split's survey-example numbers |
| T1-19 | PASS | math GLOSSARY: 8 terms (Depth, Currency, Distance, Elapsed Time, Compound Units, Percent, Ratio, Rate), all mathsisfun.com, verified live 2026-09-18 |
| T1-20 | PASS | visual asset present (worked-example transit-time figure SVG), sourced |
| T1-21 | PASS | STORY_GLOSSARY (`.sterm` anchors): 9 real-world terms, each a real https:// Wikipedia link outside the math allowlist |
| T1-22 | PASS | published HTML's sections match case.md's |
| T1-23 | PASS | inline `<script>` parses clean (`node --check`) |
| T1-24 | PASS | no hand-drawn SVG connector lines in this case |

**BLOCKER (0).**

**GAP (3):**
- **T1-10** — `new_coverage[]` is empty under the reinforcement carve-out
  (`skills/case-readiness/SKILL.md`, "The reinforcement carve-out on T1-10," 2026-08-17). At
  case-write time (2026-09-18) a fresh read of `readmodel/standards_spine.json` found
  `number-sense-depth` already at `n=2` (`covered_by=['The Deep End', 'The Custom Die']`), not `n=2`
  with zero prior cases as the concept sheet recorded when it scored this concept — two sibling
  cases authored concurrently in this batch closed it first. `case.json.reinforcement_note` records
  the adjacent-skill check performed (Height, Weight, Length, Width, Age, Data, Bar Graph all
  checked and correctly not claimed — none are genuinely forced by this case's deliverables).
  `number-sense-depth` is still genuinely forced by D1/D4 (see LEARNING_GOALS.md) and stays in
  `standards[]`.
- **T1-16** — resolved at finalization; hash recorded below.
- **T1-18** — one illustrative number (4,000 nm) in a made-up worked-example SVG in Appendix C,
  explicitly labeled as an example distinct from the case's real 10,600/13,800 nm figures. Same
  accepted-false-positive class as Cold Chain's CSS/SVG decimals and the-manifest-split's 30-student
  survey example.

**POLISH (1):** T1-07 (all 5 labels are bulleted, none from a separator-run line — informational only).

**Change log during this run:**
1. **T1-06 BLOCKER fixed** — Appendix F (Sources) was an orphan (never cross-referenced from
   Background). Added "(SEE APPENDIX F for sources)" to Background's closing sentence. Re-run
   confirmed clean.
2. **T1-10 BLOCKER downgraded to GAP** via the reinforcement carve-out — `new_coverage[]` set to
   `[]` (was `["number-sense-depth"]`), `reinforcement_note` added documenting the adjacent-skill
   check.
3. **T1-14 GAP fixed** — 5 guide-only derived numbers (transit hours, rounded rates, revenue-loss
   figure) moved into `case.json.derived`.
4. **Major arithmetic-model revision** — see Tier 2 P1 below. `sensitivity_model.py`, `case.md`'s D3
   deliverable text, `case.json.balance`/`derived`/`sensitivity_disclosure`, `FACILITATOR.md`'s Data
   Deep Dive and Twist sections, and the Interactive HTML's JS model and Working Notebook Step 3 were
   all updated together and re-verified for internal consistency.

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** (after one real revision) | **First run: FAIL-by-route.** A genuinely fresh subagent, given only `/tmp/coldsolve-the-draft-line/PACKET.md`, reached the same winner (A, ~0.96-0.98%) but via *different arithmetic* than the model of record — it charged BOTH routes their own full fuel + operating cost for their own full transit time, while the original model only charged The Cape Diversion an "extra days" differential. This revealed a genuine, undisclosed convention in case.md's D3 wording ("calculate each route's total voyage net revenue" did not say whether Canal's own fuel/opex applied). **Fix applied at case-write/case-research level**: redesigned the cost model so each route pays its own full fuel + operating cost for its own transit time (more realistic — a ship burns fuel every day at sea, canal or not) and rewrote D3's deliverable text in case.md to state this explicitly. Winner and approximate margin preserved (was A by 0.98%, now A by 0.96%). **Second run, post-fix**: a fresh subagent reached the exact intended arithmetic ($1,596.59/TEU vs. $1,581.40/TEU, 0.96% margin, winner A) with correct reasoning throughout, named the correct metric, and correctly identified MA6 (bunker fuel price) as the most sensitive assumption and MA8 (daily opex) as the least-sourced figure — both match `case.json`'s own disclosures. |
| P2 both-sides | **PASS** | **For A:** The Canal Passage's dramatically shorter transit (22.08 vs. 28.75 days) keeps total cost low enough to win on net revenue per TEU even after the toll and 200 TEU left behind. **For B:** The Cape Diversion carries every contracted TEU with zero toll and zero missed-sailing risk, and the Canal's edge is only 0.96% — thin enough that 5 of 8 stated assumptions flip the winner at a plausible ±50% swing. Neither side collapses to "technically true but obviously worse"; both a real, numbers-backed 1-sentence case exists for each. |
| P3 trap | **PASS** | Cold-named trap (before reading FACILITATOR.md): a learner assumes the shorter route trivially wins on cost without dividing by TEU actually carried, missing that the 200 TEU left behind cost the Canal Passage nearly as much in lost revenue ($362,600) as its whole time-and-cost advantage over Cape (~$316,667). This matches FACILITATOR.md's stated trap in mechanism. |
| P4 twist | **PASS** | Re-derived under the model-of-record: the $1,800/TEU missed-sailing penalty on the 200 offloaded containers adds $360,000 to Canal's cost, dropping its rate from $1,596.59 to $1,576.37/TEU — below Cape's unchanged $1,581.40/TEU. Winner flips A → B, margin 0.32%. Checked for ambiguity in "the 200 containers" phrasing (per Cold Chain's precedent bug) — the twist text explicitly ties the penalty to "the 200 containers coming off at the load port," the exact D1 offload count, with no alternate reading available. Mechanical check (`tier2_probes.py --probe 4`) confirms 0 findings after the `evaluate()`/`evaluate_twist()` return-shape fix below. |
| P5 sensitivity | **PASS (disclosed)** | `sensitivity_model.py`'s ±50% sweep of all 8 FLEX dials: 5 of 8 (draft_m, speed_kn, toll_usd, fuel_price_per_ton, fuel_tons_per_day) flip the winner; none breach the SPEC §2 20% cap in either direction (max observed margin 8.11%, on draft_m +50%). Fully disclosed in `case.json.sensitivity_disclosure[]` (8 entries, Category F — irreducible scenario/voyage-specific assumptions, no public source exists to tighten any of them) and in FACILITATOR.md's Lessons Learned. **A real script bug was found and fixed during this run**: `evaluate()`/`evaluate_twist()` originally returned extra diagnostic keys (`net_a`, `net_b`, ~$28M magnitude) alongside `A`/`B` (~$1,600 magnitude); Tier 2 probe 4's naive `max(dict, key=dict.get)` winner-detection was silently hijacked by the larger-magnitude keys, producing a false P4 mechanical FAIL. Fixed by having `evaluate()`/`evaluate_twist()` return exactly `{"A":.., "B":..}` per the stated contract, with a separate `full_metrics()`/`full_metrics_twist()` pair added for walkthrough/reporting use. |
| P6 data decay | **PASS** | Fetched all 6 cited URLs live twice this session (during research, and again for this formal probe, 2026-09-18): S1 (suezcanal.gov.eg) reachable, 66 ft / 20.1 m figure confirmed verbatim; S2 (Wikipedia, Triple E-class) reachable, 18,000+ TEU (18,270 TEU precise) confirmed; S3 (porteconomicsmanagement.org) reachable, 10,600 nm / 13,800 nm confirmed verbatim; S4 (Drewry WCI) reachable, $3,626/FEU confirmed at the same 2026-09-17 assessment date; S5 (transportgeography.org) reachable, 150-225 t/day figures confirmed verbatim; S6 (Ballast Markets) reachable, $500k-800k toll range and $600/ton VLSFO figure confirmed. Zero dead links, zero drifted figures. |
| P7 accessibility | **FAIL (waived — see `case.json.qa.tier2.P7_waiver`)** | Mechanical pre-screen: 2 real visuals found (worked-example SVGs for D1's draft concept context and D2's transit-time method), 0 missing-visual findings. Qualitative cold-read: run three times (baseline, and after two real remediation rounds). Baseline named 10 unexplained concepts + 1 MCS-51 finding. Round 1 (0→9 STORY_GLOSSARY terms, buoyancy explanation, opex/toll clarifications) still returned 10 concepts (different set — count didn't drop, but the *easier* gaps closed). Round 2 (beam term, VLSFO spelled out, great-circle explained, berth-window/FEU-TEU reasoning, explicit "this is a simplification" note on the draft-to-offload rate) still returned 11 concepts + the same MCS-51 finding. This domain (naval architecture / maritime operations: buoyancy, draft certification, dredged-channel geometry, containerized-cargo handling) carries irreducibly dense technical vocabulary; per MCS-49 (the same disclosure-waiver mechanism Cardiology used), granted a documented waiver rather than a false PASS or endless remediation loops working against this case's own T3 pedagogy. All 7 required waiver fields recorded in `case.json.qa.tier2.P7_waiver`, including the full verbatim remaining-gap list from the third cold-read. |

**MECHANICAL RESULT (script):** 0 probes failed mechanically after the P4/P5 return-shape fix; P7's
mechanical pre-screen (visuals) is clean — its FAIL is from the qualitative cold-read layer, waived
per MCS-49.

### Tier 3 — human dry-run

NOT RUN. `cohort_bands[]` is declared (3 bands) for whenever a facilitator schedules a live session;
no `cases/the-draft-line/runs/RUN_*.md` exists yet. This does not block `TIER2_PASS` / `PUBLISHED`
per the ladder in `skills/case-readiness/SKILL.md` — it blocks `VERIFIED` only.

## case.json.qa (written by this report)

```json
{
  "state": "TIER2_PASS",
  "verdict": "PASS",
  "run_on": "2026-09-18",
  "blockers_open": 0,
  "gaps_open": 3,
  "case_md_sha256": "5c9f0a0b3fd75335dab58e44082b3b69cccd8e54f4cd293ce7b82f6d85476540",
  "tier2": {
    "P1": "PASS",
    "P2": "PASS",
    "P3": "PASS",
    "P4": "PASS",
    "P5": "PASS (disclosed)",
    "P6": "PASS",
    "P7": "FAIL (waived -- see qa.tier2.P7_waiver)",
    "P7_waiver": { "...": "see cases/the-draft-line/case.json for the full 7-field record" }
  },
  "tier3_runs": []
}
```

## Next step

`Run case-publish on the-draft-line` — packet build only, per this task's own scope (no read-model
write, no Drive push).
