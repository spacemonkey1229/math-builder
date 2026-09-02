## case-readiness run — 2026-09-01

**State:** researched → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (20 checks)

Remediation this session: removed a stray `## Appendices` (plural) wrapper heading between
Challenge 5 and `### Appendix A` — it does not match the T1-06 appendix-boundary regex (which
requires the literal substring "Appendix", singular; "Appendices" does not start with that string
because of the -ix/-ices spelling change), so the Challenges-section parser was reading straight
through it and swallowing the heading into Challenge 5's body, tripping T1-04's verbatim-boilerplate
diff. Added `(SEE APPENDIX C)` to Background (patent buffer-language appendix was previously only
cross-referenced from Appendix B, not from Background/Challenges as SPEC §1.6 requires) and
`(SEE APPENDIX H)` for the Sources appendix. Joined the 5 hard-wrapped Socratic questions in
`FACILITATOR.md` onto single physical lines (content unchanged) so the mechanical Socratic-question
count parser (which requires the question mark on the same line as the numeral) can see all 5 — they
were always present and correctly worded, just wrapped across lines. Reworded one Lessons Learned
bullet ("...exactly the trap that makes..." → "...exactly the pitfall that makes...") because it was
the first literal occurrence of the word "trap" in the file and was shadowing the real `## The trap`
section from the mechanical trap-quality parser.

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview carries no load-bearing numerals |
| T1-03 | PASS | binary dilemma, opens "You are Yuki Alvarez." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate (was BLOCKER on the `## Appendices` swallow; fixed) |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | appendices A-H, no orphans (was BLOCKER x2 on C/H; fixed) |
| T1-07 | PASS | final appendix lines verbatim spine labels |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | GAP | margin 17.0%, inside the ~20% cap but wide — accepted, discussion will lean toward B |
| T1-10 | GAP | new_coverage[] empty — reinforcement carve-out, `reinforcement_note` present (this case reinforces all 20 Geometry/Transformations skills, 14 of them from a single-point-of-failure n=1) |
| T1-11 | PASS | learning-goal mutual reachability |
| T1-12 | PASS | tier/numeric load consistent (T2, 6 deliverables) |
| T1-13 | PASS | facilitator guide, full anchor ladder, Twist, 45-min timed plan, trap, 5 Socratic questions (was GAP on question count; fixed) |
| T1-14 | PASS | continuity — no orphan numbers |
| T1-15 | PASS | no published/ artifacts yet, nothing to drift |
| T1-16 | PASS | case_md_sha256 recorded below, current |
| T1-17 | PASS | cohort_bands[] declared (3 bands) |
| T1-18 | PASS | published/ built this session, fresh, leak-free |
| T1-19 | PASS | glossary complete |
| T1-20 | PASS | advisory, never blocks |

**BLOCKER (0).**

**GAP (2, both accepted):**
* T1-09 — margin 17.0% is real and inside the cap; disclosed as "wide" per the mechanical advisory,
  not a defect. Both sides remain genuinely defensible per Tier 2 probe 2 below.
* T1-10 — empty `new_coverage[]`, reinforcement carve-out per `case.json.reinforcement_note`.

`VERDICT: TIER1_PASS (0 blockers, 2 gaps)`.

### Tier 2 — simulated play (6 probes)

Mechanical pre-screen fixes this session: `case.json.balance.argument_a`/`argument_b` were rewritten
with real dollar figures ($684,450 vs $585,000, $99,450/17.0% gap) — both were previously almost
entirely prose, tripping P2's "almost no numbers" screen. `FACILITATOR.md`'s "The trap" section was
rewritten to lead with "Most learners **will** treat..." so the mechanical trap-quality screen (P3)
sees an explicit prediction of the wrong action. Authored `sensitivity_model.py`, reproducing the
documented 17.0% margin exactly (in the case's own "A costs X% more than B" convention) and scoping
`FLEX[]` to the two genuine stated Modeling Assumptions (MA9 run size, MA10 base yardage) that
FACILITATOR.md's own Data Deep Dive already claims cancel out of the percentage — the model confirms
that claim mechanically.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Reading `case.md` alone: D1/D2 trace the registration point through both composition orders using Appendix A's coordinates; D3 shows the motif has no line of symmetry, which is exactly why the order is non-interchangeable; D6's cost table is unambiguous once Appendix D/F's cited figures are plugged in ($585,000 vs $684,450, 17.0%). The metric (total production-run fabric cost) is named directly in Background. A solver reaches B with correct, traceable arithmetic. |
| P2 both-sides | **PASS** | After the argument rewrite, both sides carry real numbers: A's case is "$99,450 (17.0%) more, but buys a guaranteed-correct nap direction across all 5,000 units, backed by real UCSB Bren School efficiency-variance data"; B's case is "$99,450 cheaper, and the geometry that makes it safe is fully checkable from Appendix A's cited seam-axis and cutting-angle figures, not a guess." Neither side collapses to a concession; B does not become obviously correct until D6's dollar comparison is actually run, since A's safety argument stands independently of the cost gap. |
| P3 trap | **PASS** | The rewritten trap names the specific wrong action: assuming rotation and reflection commute (order doesn't matter) and picking whichever composition order is easier to draw in D1, without checking it against Appendix A's seam axis. This is the single most likely real failure mode, since the two operations "feel" interchangeable to a student who has not yet internalized that they don't commute in general — matches the case's D3 deliverable, which exists specifically to prove why they don't commute here. |
| P4 twist | **PASS** | The Twist (the older marker's real-world cutting-angle mismatch, landing the registration point a quarter-inch off) invalidates the "the geometry is fully checkable, so B is risk-free" reading of Option B without making A obviously correct — it demonstrates that "the correct order is a fixed fact" was itself an unstated assumption about the cutting-angle input never changing. It depends only on the case's own stated setup (Appendix A's cutting-angle figure being an input, not an immutable constant), not on an unstated convention, so it survives every legitimate reading of the case's Modeling Assumptions. |
| P5 sensitivity | **PASS** | `sensitivity_model.py` reproduces the base case exactly (A=-$684,450, B=-$585,000, 17.0% margin in the case's own convention, matching `case.json.margin_pct`). Flexing both genuine stated Modeling Assumptions in scope (MA9 run size, MA10 base yardage) simultaneously ±50% leaves the percentage margin exactly unchanged (17.0% throughout) — mechanically confirms FACILITATOR.md's own disclosure that these are pure common multipliers that cancel out of the ratio. The with-nap premium (17%, chosen inside the cited 15-25% range) and fabric cost ($39.00/yd, S10) are cited data, not stated assumptions, and are correctly excluded from the default sweep. |
| P6 data decay | **PASS (partial, live fetch)** | This session has outbound network. Spot-checked two of the ten sources: **S5** (Sewing & Craft Alliance Guideline 4.120) — PDF fetched and read directly (page-by-page), confirms verbatim: "all the pieces must run in the same direction... Extra fabric is generally required in order to lay out the pieces this way." **S6/S7** (UCSB Bren School report) — PDF fetched and read directly, Table 10 (p.34) confirms 21%/16%/18% (low/high/average) waste, matching S7's cited 16-21% range; the Average column (2,820 of 3,460 tonnes used ≈ 81.5%) is consistent with S6's cited 82.0% utilization figure (Figure 6, adjacent page). No BLOCKER found on either source checked. The remaining 8 URLs (S1-S4, S8-S10) were not re-fetched this session; RESEARCH_LOG.md/case.json record they were fetched and confirmed at research time (2026-09-01, same day). |

`MECHANICAL RESULT: 0 probes FAILED mechanically.` All six verdicts recorded by name.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-repeat-match/runs/RUN_*.md` filed. Required before this case may be marked
✅/VERIFIED in `DOCTRINE_LEDGER.md`; not required for `PUBLISHED`.

### Next step

`case-publish` may run (`case.json.qa.state == "TIER2_PASS"`, all six probes recorded, 0 FAIL).

---

## case-readiness run — 2026-09-01 (re-run, post-publish)

**State:** TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

This run found the case's `published/` artifacts (docx, xlsx, interactive HTML) now exist and have
drifted from `case.md`/`case.json` since the prior run recorded above (which found nothing to drift
against, as no `published/` folder existed yet). This is a GATE re-run, not a fix — the drift is
named below and handed back.

### Tier 1 — structural (20 checks)

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview carries no load-bearing numerals |
| T1-03 | PASS | binary dilemma, opens "You are Yuki Alvarez." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | appendices A-H, no orphans |
| T1-07 | PASS | final appendix lines verbatim spine labels (POLISH: separator-run half of parser found 0 additional labels, all 20 came from bullets) |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | GAP | margin 17.0%, inside the ~20% cap but wide — discussion will lean toward B |
| T1-10 | GAP | `new_coverage[]` empty — reinforcement carve-out, `reinforcement_note` present and verified |
| T1-11 | PASS | learning-goal mutual reachability |
| T1-12 | PASS | tier/numeric load consistent (T2, 6 deliverables) |
| T1-13 | PASS | facilitator guide, full anchor ladder, Twist, 45-min timed plan, trap, 5 Socratic questions |
| T1-14 | PASS | continuity — `case.json.derived`/balance figures agree with FACILITATOR.md |
| T1-15 | **GAP** | CONTINUITY — 2 numbers in `published/The Repeat Match - Facilitator Guide.docx` ([7.3, 60.0]) appear in neither `case.md` nor `case.json` — hand back to whoever regenerates the docx to trace these (7.3 and 60.0 do not match any Appendix/MA/balance figure on file; likely a stray page-number, timestamp, or unit artifact from the docx build, but must be traced, not assumed) |
| T1-16 | PASS | case_md_sha256 current: `da3cc3e9016619c67cb5eceec307494282ef45d140c41a8e90d46c47263a4d1e` |
| T1-17 | PASS | cohort_bands[] declared (3 bands) |
| T1-18 | **GAP** | CONTINUITY — 2 numbers in `The Repeat Match - Interactive.html`'s prose/markup ([70.0, 110.0]) appear in neither `case.md` nor `case.json` — same instruction: trace before republishing |
| T1-19 | PASS | glossary complete |
| T1-20 | POLISH | no visual asset in `published/` HTML — advisory only, never blocks |

**BLOCKER (0).**

**GAP (4):**
* T1-09 — margin 17.0%, real, inside cap, wide (unchanged from prior run, accepted)
* T1-10 — reinforcement carve-out (unchanged from prior run, accepted)
* T1-15 — **new since last run**: 2 untraceable numbers in the published Facilitator Guide docx
* T1-18 — **new since last run**: 2 untraceable numbers in the published Interactive HTML

`VERDICT: TIER1_PASS (0 blockers, 4 gaps)`.

### Tier 2 — simulated play (6 probes)

Blind cold-solve performed by reading `case.md` alone (Overview/Background/Dilemma/Challenges/all
appendices A-H) before opening `FACILITATOR.md` or `case.json`, per the skill's documented
workaround for a same-session subagent limitation. Blind answer committed in writing first, then
compared against facilitator material.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Blind solve from `case.md` alone reached: metric = total production-run fabric cost (stated directly in Background); Option B (Mirror-Match) cheaper using base yardage (MA10=3.0yd) × fabric cost (S10=$39/yd) × run size (MA9=5,000) = $585,000 vs. Same-Grain adding Appendix D's 15-25% with-nap premium ($585,000×1.15 to ×1.25 ≈ $672,750-$731,250). Compared against FACILITATOR.md/case.json: the actual value used is 17% (a specific point inside the disclosed range, documented as a deliberate conservative retune from an original 20% midpoint) giving exactly $684,450 and margin 17.0% — consistent with the blind solve's range and reasoning, correct arithmetic, metric named unprompted. |
| P2 both-sides | **PASS** | Blind read found A's case is real but qualitative-leaning (guaranteed nap safety, zero registration risk) against B's quantitative dollar edge — neither reads as a bare concession or near-zero-number argument. FACILITATOR.md's `argument_a`/`argument_b` confirm both carry real numbers ($99,450/17.0% cited in both) and A's case does not collapse: it treats the premium as insurance against a failure mode "whose cost, if it happened, would likely exceed the premium many times over" — a substantive, not concession-shaped, position. |
| P3 trap | **PASS** | Blind trap hypothesis (before reading FACILITATOR.md): a student will assume rotation and reflection commute and pick whichever composition order is easier to draw, without checking Appendix A's seam axis. FACILITATOR.md's stated trap matches almost verbatim: "Most learners will treat 'rotation and reflection are both just simple moves' as meaning they can be applied in either order with the same result... without ever checking it against the seam axis in Appendix A." Guide names the same trap the blind read predicted. |
| P4 twist | **PASS** | Twist (the older marker's real cutting-angle mismatch, landing the registration point ~1/4" off) invalidates the "checkable = guaranteed" reading some students will hold for Option B, without making A automatically correct. It introduces new information rather than depending on an ambiguous reading of a stated assumption — Appendix A's MA3 (90° CCW, front panel) is not contradicted, only shown to be one machine's input rather than a universal constant. Survives every natural reading of the case's own stated assumptions; no BLOCKER. |
| P5 sensitivity | **PASS** | `python3 skills/case-readiness/scripts/tier2_probes.py --case the-repeat-match --probe 5 --flex 0.5` swept the 2 declared `FLEX[]` dials (MA9 run_size_units, MA10 base_yd_per_unit) at ±50%. Base: A=-$684,450, B=-$585,000, margin -14.5% (script's own (B-A)/A convention; equivalent to the case's 17.0% in its own (A-B)/B convention). All four flexed runs: winner stays B, margin_pct stays exactly -14.5% throughout, `flips: false` on every row — mechanically confirms MA9/MA10 are pure common multipliers that cancel out of the percentage, as FACILITATOR.md/case.json's `sensitivity_note` claims. |
| P6 data decay | **PASS** | Live web access this session — fetched and checked all 10 of 10 `sources[].url` entries (not a partial spot-check this time). **S1** (EFI Reggiani UNICA spec) reachable, confirms 25-40in/640-1018mm repeat range verbatim. **S2** (US Patent 5,333,111) reachable, confirms "often as much as half a fabric design repeat" verbatim. **S3** (Sewing With Ease) reachable, confirms "15 to 25 percent" nap/directional yardage addition. **S4** (Canvas Etc.) reachable, confirms "10 to 25 percent" for directional/nap/velvet/pile. **S5** (Sewing & Craft Alliance Guideline 4.120 PDF) reachable, fetched and read directly page-by-page: confirms "all the pieces must run in the same direction... Extra fabric is generally required," no percentage stated in the primary document, exactly as the case discloses. **S6/S7/S8/S9** (UCSB Bren School report PDF) reachable, fetched and read directly: Figure 6 (p.35) confirms "Used 82.0%" verbatim, matching S6; Table 10 (p.34) confirms 21%/16%/18% (low/high/average) waste, matching S7's 16-21% range exactly; p.9 confirms 686 Technical Apparel's disclosed 87% cutting efficiency (S8) and Rissanen (2005)'s 10-15% baseline (S9) verbatim. **S10** (Discovery Fabrics) reachable; the $39.00/yd figure is confirmed as the listed *regular* price (the page's current sale price is $27.00/yd, but the case correctly cites the regular price, which is still listed and accurate). No dead links, no drifted figures, nothing moved. All 10 sources within 1 day of `accessed` date (2026-09-01), well under the 365-day flag threshold. |

`MECHANICAL RESULT: 0 probes FAILED.` All six verdicts recorded by name.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-repeat-match/runs/RUN_*.md` filed. Required before this case may be marked
✅/VERIFIED in `DOCTRINE_LEDGER.md`; not required for `PUBLISHED`.

### Next step

Tier 1 and Tier 2 remain clean enough to keep `qa.state = "TIER2_PASS"`, but **T1-15 and T1-18 are
new findings this run** and should be handed to whoever regenerates `published/` artifacts: trace
where `7.3`, `60.0` (docx) and `70.0`, `110.0` (HTML) came from and either fix the artifact or move
the number into `case.json.derived` if it is a legitimate figure with no home yet. Re-run
`tier1_structural.py --case the-repeat-match` after the artifacts are regenerated to confirm T1-15/
T1-18 clear. Schedule the Tier 3 dry-run whenever a facilitator is available; not required to keep
the case `PUBLISHED`.
