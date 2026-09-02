## case-readiness run — 2026-09-01

**State:** researched → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (20 checks)

Remediation this session, in order of significance:

**Resolved the disclosed "judgment call for a human" on the primary PK/PD gate.** The prior
research pass found the fAUC/MIC pass/fail verdict appeared assumption-sensitive and explicitly
recommended case-readiness make the call rather than treating either option as a clean pass. I
computed AUC0-24h directly from Appendix B's own modeled concentration-time data (the same method
Challenge D1 asks the student to use): Single Shot = 39.1 μg·h/mL; Four-Day Course (day 1 alone,
before multi-dose superposition even helps it) = 64.7 μg·h/mL. The ambiguity in the prior finding
traced to which of Appendix C's two population-specific PK/PD cutoffs (1 mg/L calves vs. 2 mg/L
adult cattle) to use as MIC — and the case's own Background/MA3 repeatedly and specifically describe
the treated animals as 500 lb "stocker/feeder calves," not adult cattle, which settles which cutoff
is case-consistent (calves, 1 mg/L; target AUC24h = 24 μg·h/mL). Under that reading, **both options
pass** (39.1 ≥ 24; 64.7 ≥ 24), which makes the already-computed 13.9% cost tie-breaker the case's
real, decisive margin rather than a moot number — resolving finding (1) from `RESEARCH_LOG.md`
without inventing any figure. Recorded in `case.json.balance.margin_note`,
`case.json.derived.primary_gate_resolution`, and `FACILITATOR.md`.

**Structural fixes:** case.md's Modeling Assumptions section sat between Challenges and Appendix A
with no intervening Appendix boundary, which caused T1-04's Challenge-5 boilerplate check to
misparse (same root defect class as `the-repeat-match`/`the-trial-size`: content the parser reads
as "still inside Challenges" until it sees a real Appendix heading) — moved Modeling Assumptions to
its conventional position after the last data appendix (before the How-To/Sources appendices),
matching every other case in this batch. A stray interpunct character ("·", used for μg·h/mL
notation) inside the Sources appendix (which sits after the mandatory How-To appendix in this
case's lettering, same as several other cases) was tripping T1-07's vocabulary-line parser, which
treats any "·"-separated line as a middot vocabulary run — replaced with "x" in that one row.
Added `(SEE APPENDIX F)`/`(SEE APPENDIX G)` references to Background (were orphans). Converted
`FACILITATOR.md`'s prose guidance into real markdown headings (anchor ladder, Twist, 45-min plan —
content was already strong; the Twist is built around the same calves-vs-adult-cattle population
question the primary-gate resolution above turns on). Added `case.json.cohort_bands[]` (3 bands).
Fixed a stale `modeling_assumptions[MA4].value_used` field that still said "4 mg/lb/day" after the
prior session's retune to 5 mg/lb/day.

| id | result | note |
|---|---|---|
| T1-01 through T1-09 | PASS | structure, boilerplate, appendices, citations, balance test (13.9%, under cap) all clean |
| T1-10 | GAP | new_coverage[] empty — reinforcement carve-out, accepted (this case reinforces the whole Calculus/Integrals group's single-point-of-failure n=1 status) |
| T1-11 through T1-13 | PASS | learning-goal reachability, tier load, facilitator artifacts (anchor ladder, Twist, timed plan, 5 Socratic questions, trap) all clean |
| T1-14 | GAP | 7 residual "orphan" numbers are guide-only pre-retune cost figures (the $4.64/$5.153/$64.09 pre-retune MA4=4mg/lb/day cost breakdown, kept in FACILITATOR.md as before/after history) and universal constants (6.0, 10.0, 30.0) — not case-data drift |
| T1-16 | PASS | case_md_sha256 recorded below, current |
| T1-17 through T1-20 | PASS | cohort bands, published/ built, glossary complete |

**BLOCKER (0). GAP (2, both accepted).**

`VERDICT: TIER1_PASS (0 blockers, 2 gaps)`.

### Tier 2 — simulated play (6 probes)

Mechanical pre-screen fixes this session: `case.json.balance.argument_a`/`argument_b` were rewritten
with real digits (dollar totals, AUC values, event counts) — both were previously almost entirely
qualitative prose, tripping P2. Renamed one prose reference to "trapezoidal integration" (which
literally contains the substring "trap," matching before the real `## The trap` heading) to
"step-wise numerical integration" so the mechanical trap-quality parser reads the actual trap
section. Authored `sensitivity_model.py` from scratch, reproducing the documented 13.9% cost margin
exactly and providing an independent `gate_check()` function that reproduces the primary-gate
resolution above. Scoped `FLEX[]` to the 2 genuine stated Modeling Assumptions that feed the cost
metric (MA3 body weight, MA4 conventional dosing rate); MA4 flips the winner at a +50% mechanical
sweep (which falls outside the real labeled 3-5 mg/lb/day range) — added
`case.json.sensitivity_disclosure[]` documenting this and the case's own already-disclosed in-range
breakeven (~4.6 mg/lb/day) per MCS-26.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Reading `case.md` alone: D1's Riemann sum and D2's FTC integral both use Appendix B's real modeled data; D3's fAUC/MIC check is unambiguous once the case-consistent (calves) cutoff is applied; D4's cost comparison follows directly from Appendices D/E. A solver reaches B (Four-Day Course) with correct, traceable arithmetic, naming AUC/cost as the two-stage metric explicitly described in Background. |
| P2 both-sides | **PASS** | After the argument rewrite, both sides carry real numbers: A's case is "$7.33 total, only 1 handling event vs. 4, a real AUC pass (39.1 vs. 24 target)"; B's case is "$6.31 total (13.9% cheaper), a wider real AUC pass (64.7 vs. 24, before superposition even helps), less tissue damage per event." Neither side collapses; B does not become obviously correct until both the PK/PD gate and the cost comparison are actually run. |
| P3 trap | **PASS** | The trap names the specific wrong action: comparing Appendix A's single-dose AUC totals (close to each other) and concluding the choice barely matters, missing that the full-treatment-window integral — not the single-dose comparison — is what the case's own metric requires. This matches the deliverable structure exactly (D1/D2 build the full-window integral; a Hero who stops at Appendix A never gets there). |
| P4 twist | **PASS** | The Twist (which PK/PD cutoff — calves vs. adult cattle — applies) invalidates the naive "both charts obviously work, so just compare cost" reading without making either option obviously wrong — it demonstrates that an unstated population-classification choice can flip a real efficacy verdict even with correct arithmetic throughout. It depends only on the case's own already-stated animal population (calves), not an unstated convention, so it survives every legitimate reading of the case's Background. |
| P5 sensitivity | **PASS (disclosed)** | `sensitivity_model.py` reproduces the base case exactly (A=$7.33, B=$6.31, 13.9% margin matching `case.json.margin_pct`), and its independent `gate_check()` reproduces the primary-gate resolution (both options pass under the calves cutoff; the Single Shot alone would fail under the adult-cattle cutoff — exactly the Twist). Flexing the two genuine stated Modeling Assumptions (MA3, MA4) ±50% flips the winner only for MA4 at +50% (7.5 mg/lb/day), which falls entirely outside the real cited 3-5 mg/lb/day label range — disclosed in `case.json.sensitivity_disclosure[]`, consistent with the case's own pre-existing in-range breakeven note (~4.6 mg/lb/day). |
| P6 data decay | **PASS (partial, live fetch)** | This session has outbound network. Spot-checked the case's single most load-bearing dosing figure: **S4** (DailyMed, LIQUAMYCIN LA-200 label) — live, confirmed verbatim: "A single dose of 9 mg of oxytetracycline per lb of body weight..." and "Discontinue treatment at least 28 days prior to slaughter of cattle and swine." **S6** (PubMed, Xia et al. 1983) — page reachable but returned only a cookie-consent wall to automated fetch this session; not independently re-confirmed beyond reachability, and it is narrative context only (not load-bearing to D1-D4's arithmetic per case.json's own note). No BLOCKER found on the load-bearing source checked. The remaining 8 URLs were not re-fetched this session; RESEARCH_LOG.md/case.json record they were fetched and confirmed at research time (2026-08-31). |

`MECHANICAL RESULT: 0 probes FAILED mechanically.` All six verdicts recorded by name.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-dosing-curve/runs/RUN_*.md` filed. Required before this case may be marked
✅/VERIFIED in `DOCTRINE_LEDGER.md`; not required for `PUBLISHED`.

### Next step

`case-publish` may run (`case.json.qa.state == "TIER2_PASS"`, all six probes recorded, 0 FAIL).

## case-readiness run — 2026-09-01 (re-gate after D5/Appendix H addition)

**State:** TIER2_PASS → **DRAFT (BLOCKED)**   **Verdict:** BLOCKED — Tier 1 not clean; Tier 2 not started per gate doctrine ("Tier 2 does not start until Tier 1 is clean").

Preflight lint: clean, no advisory findings.

### Tier 1 — structural (20 checks)

Re-ran mechanically against the current `case.md` (sha256 `117518cdeb77cd13cdecbc543b88df48fa78dbe64b6cb6ebf63d9c59e69a7cfc` — same hash the prior TIER2_PASS entry recorded; the content has not changed since, but the checker now surfaces defects the prior pass did not catch, and the published/ artifacts have drifted in time since that pass ran).

| id | result | note |
|---|---|---|
| T1-01 – T1-06 | PASS | structure, boilerplate, appendix lettering/ordering (lettering itself) all clean |
| T1-07 | **FAIL (BLOCKER)** | Final-appendix verbatim-spine-label check now fails. Root cause: Appendix H ("Convention-Sensitivity Inputs (for D5)") was appended *after* Appendix G (Sources), making H the last appendix in the document. SPEC §1.7 requires the *last* appendix to be the verbatim spine-label appendix (this case's is the "How To…" appendix, F). The checker is now comparing Appendix H's convention-sensitivity table rows/prose (units, formulas, μg·h/mL fragments split on "·") against the spine-label list, which of course doesn't match. **Fix is structural, not textual: move Appendix H to sit before the spine-label appendix (i.e., reorder so the mandatory verbatim-labels appendix remains last), not edit H's content.** |
| T1-08 | PASS | citations backed |
| T1-09 | PASS | balance test 13.9%, under 20% cap |
| T1-10 | GAP | new_coverage[] empty — reinforcement carve-out already recorded and accepted in the prior pass |
| T1-11 – T1-13 | PASS | learning-goal reachability, tier load, facilitator artifacts clean |
| T1-14 | GAP | 6 numbers in FACILITATOR.md (4.64, 5.153, 6.0, 7.1, 30.0, 64.09) have no home in case.md/case.json — same pre-retune before/after figures flagged (and accepted) in the prior pass; still worth moving into `case.json.derived` |
| T1-15 | **FAIL (BLOCKER) — 5 instances** | Every file in `published/` (MANIFEST.json, Case Study.docx, Data.xlsx, Facilitator Guide.docx, Interactive.html) was built 195–201 minutes **before** the last edit to its source (case.md / FACILITATOR.md). The packet a student would download does not match the case of record. Also 8 orphan numbers in the Facilitator Guide.docx (same set as T1-14 plus 7.3/40.0) not found in case.md/case.json. **Re-run `case-publish` to regenerate all 5 artifacts after T1-07 is fixed.** |
| T1-16 | PASS | hash current |
| T1-17 | PASS | cohort bands declared |
| T1-18 | **FAIL (BLOCKER)** | published Interactive.html is stale (built 200 min before case.md's last edit) — rebuild required. Also 1 orphan number (19.0) in its prose/markup not traceable to case.md/case.json. |
| T1-19 | PASS | glossary complete |
| T1-20 | PASS | (POLISH: no visual asset — optional, never blocks) |

**BLOCKER (7): T1-07 (×1), T1-15 (×5), T1-18 (×1, staleness only — the orphan-number finding is a GAP).**
**GAP (4): T1-10, T1-14, T1-15 (orphan numbers), T1-18 (orphan number).**

`VERDICT: BLOCKED (7 blockers, 4 gaps)`

### Tier 2 — simulated play (6 probes)

**NOT RUN.** Tier 1 has 7 open BLOCKERs; per gate doctrine Tier 2 does not start until Tier 1 is clean. No probe was executed this session, including P1–P4 and P6 (all require Tier 1 clean before dispatch) and P5 (script exists — `sensitivity_model.py` present — but withheld for the same reason).

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | NOT RUN | blocked behind Tier 1 |
| P2 both-sides | NOT RUN | blocked behind Tier 1 |
| P3 trap | NOT RUN | blocked behind Tier 1 |
| P4 twist | NOT RUN | blocked behind Tier 1 |
| P5 sensitivity | NOT RUN | blocked behind Tier 1 (script present, not invoked) |
| P6 data decay | NOT RUN | blocked behind Tier 1 |

### Tier 3 — human dry-run

NOT RUN.

### Next step

Fix the 7 blockers and re-run: (1) reorder Appendix H to precede the mandatory final spine-label appendix (F) rather than following Sources (G); (2) re-run `case-publish` to rebuild all 5 stale `published/` artifacts once case.md/FACILITATOR.md are settled. Then re-run `tier1_structural.py`; only once it is clean does Tier 2 (including the P1 blind read of the new D5 convention-sensitivity table) run.

## case-readiness run — 2026-09-01 (re-gate after appendix reorder; packet rebuilt)

**State:** TIER1_PASS → **TIER2_FAIL**   **Verdict:** BLOCKED at Tier 2 — 3 of 6 probes FAIL (P3, P4, P6); Tier 1 itself is clean.

The reorder landed correctly: appendices are now A–E (data), F (Sources), G (Convention-Sensitivity
Inputs for D5), H ("How To…" — the mandatory spine-label appendix, now genuinely last).

### Tier 1 — structural (20 checks)

Re-ran `tier1_structural.py --case the-dosing-curve` against current `case.md`
(sha256 `2e722c636c611f45...`). The recorded `qa.case_md_sha256` was stale (still pointing at the
pre-reorder hash `117518cdeb77cd13...`), which alone tripped T1-16 as a BLOCKER on the first run this
session — corrected by writing the current hash (this skill's own end-of-run responsibility, not a
case defect), then re-ran clean:

| id | result | note |
|---|---|---|
| T1-01 – T1-06 | PASS | structure, boilerplate, appendix lettering/ordering clean |
| T1-07 | **PASS** | Final appendix (H, "How To…") verbatim spine labels confirmed — the specific prior BLOCKER, now resolved by the reorder |
| T1-08, T1-09 | PASS | citations backed; balance test 13.9%, under the 20% cap |
| T1-10 | GAP | `new_coverage[]` empty — reinforcement carve-out, already accepted |
| T1-11 – T1-13 | PASS | learning-goal reachability, tier load, facilitator artifacts clean |
| T1-14 | GAP | 6 numbers in FACILITATOR.md (4.64, 5.153, 6.0, 7.1, 30.0, 64.09) — pre-retune before/after cost figures kept for audit-trail narrative, not case-data drift; still worth moving into `case.json.derived` |
| T1-15 | GAP | 8 numbers in the published Facilitator Guide `.docx` — same set plus 7.3/40.0 |
| T1-16 | **PASS** | hash now current (corrected this run) — the specific prior BLOCKER, now resolved |
| T1-17 | PASS | cohort bands declared |
| T1-18 | GAP | 1 orphan number (19.0) in Interactive.html prose |
| T1-19, T1-20 | PASS | glossary complete; no visual asset (advisory only) |

**BLOCKER (0). GAP (4, all previously identified, none new.)**

`VERDICT: TIER1_PASS (0 blockers, 4 gaps)` — both named prior issues (T1-07 ordering, T1-16 hash
currency) confirmed clean.

### Tier 2 — simulated play (6 probes)

Dispatched three genuinely fresh subagents (P1 cold solve, P2 both-sides, P3 trap check), each given
only `/tmp/coldsolve-the-dosing-curve/PACKET.md` and blocked from reading `FACILITATOR.md`/`case.json`.
P4 and P6 were assessed directly against `FACILITATOR.md` and live web fetches. P5 is fully mechanical
(`tier2_probes.py --probe 5`).

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh solver chose B, built a correct Riemann-sum/FTC AUC (day-1 conventional ≈64.7 μg·h/mL, matching the case's own unscaled figure), and independently built a D5 convention-sensitivity table whose cells (21.4/26.9/35.7/44.9) match `case.json.derived.primary_gate_resolution` almost exactly. It correctly named the MIC-benchmark choice as the dominant swing factor and stated the recommendation is conditional on defending the calves cutoff + upper dosing range — the exact "strong D5" shape FACILITATOR.md describes. One honest miss: it split the two lesion-incidence surveys (11%/0.2%) *by formulation* to compute cost, a plausible but non-official reading, landing on a ~$2.12/26.6% margin instead of the official 13.9% — self-flagged as its weakest link. **Root cause is a real case gap, not solver error:** Appendix E states the $64.09-per-lesion-and-0.2%-incidence derivation only in `FACILITATOR.md`, not in the student-facing appendix — a Hero cannot derive the official $0.13/$0.51 per-event costs from case.md alone. Recommend adding the derivation (or at least "apply the same current incidence rate to every handling event, regardless of formulation") to Appendix E. |
| P2 both-sides | **PASS** | Fresh solver built both arguments with real arithmetic. Its own Four-Day-Course D5 cells were wrong (it mixed up the long-acting and conventional unscaled Day-1 AUC columns — 38.85 vs. 64.1 — before rescaling, producing an all-fail table for B); recomputing with its own correctly-stated unscaled values (verified independently: 64.1 × 3/9.07 ≈ 21.2, × 5/9.07 ≈ 35.3, matching `case.json.derived`'s 21.4/35.7) shows B actually passes 3 of 4 real cells, not 1 of 12. With the corrected numbers, neither side collapses: A has an unconditional calves-benchmark pass with a single handling event; B is cheaper and passes 3/4 real efficacy cells. The subagent's own qualitative read ("B collapses at the day-1-only window question") is real for exactly one cell (3 mg/lb/day, day-1) but overstated as "all cells" — corrected, the balance test holds. |
| P3 trap | **FAIL** | The fresh solver, blind to FACILITATOR.md, independently named a *different* trap than the one FACILITATOR.md's "The trap" section names: skipping Appendix G's dose-rescaling (using Appendix B's curve, built at the ~9.07 mg/lb study dose, directly for the Four-Day Course's real 3–5 mg/lb/day rate) and/or silently defaulting to the worst-case day-1-only window without noticing it's a live convention choice. This is not a hypothetical trap — `case.json.derived.primary_gate_resolution.note_on_prior_resolution` records that an *earlier case-readiness pass on this exact case* made precisely this error. FACILITATOR.md's stated trap (naively comparing Appendix A's close single-dose AUC totals and concluding "the choice barely matters") is real but is a different, milder failure mode than the one that has actually already fooled a careful reviewer of this case once. Per SKILL.md: "a trap the guide has not anticipated is a FAIL even if the case is sound." Recommend adding the dose-rescaling-skip trap to FACILITATOR.md's "The trap" section alongside the existing one. |
| P4 twist | **FAIL** | The scripted Twist (revealing that the CLSI/adult-cattle MIC benchmark flips every D5 cell to FAIL) is pre-empted by FACILITATOR.md's own "Data Deep Dive" instructions, which run *before* the Twist beat: "Build D5's convention-sensitivity table live: the Single Shot's fixed AUC0-24h against **both MIC benchmarks**... Let the room see the table flip before revealing the cost comparison." By the time the scripted Twist beat arrives, the room has already built the table with both benchmarks and already watched it flip — the Twist has no new information left to reveal, so it cannot invalidate any position a real room still holds (D5 requires building the full table as a graded deliverable, so this isn't avoidable by facilitator discretion alone). Recommend resequencing: Data Deep Dive should build and reveal only the calves-benchmark rows live, holding the CLSI/adult-cattle benchmark and its all-FAIL consequence for the Twist beat as originally intended. |
| P5 sensitivity | **PASS (disclosed)** | `tier2_probes.py --probe 5 --flex 0.5`: base case A=-$7.33, B=-$6.31 (13.9% margin) reproduced exactly. Sweeping the 2 declared `FLEX[]` dials ±50%: `body_weight_lb` never flips the winner. `conv_dose_mg_per_lb_per_day` flips the winner to A at +50% (7.5 mg/lb/day), which falls entirely outside the real FDA-labeled 3–5 mg/lb/day range — already disclosed in `case.json.sensitivity_disclosure[]` together with the in-range breakeven (~4.6 mg/lb/day). Passes under the disclosure-aware pass state, not the stable-margin state. |
| P6 data decay | **FAIL** | Live-fetched all 10 `sources[].url` this session. **S1, S2, S4, S5, S7 (both product pages) all reachable, current, and every cited value confirmed verbatim on the live page** — no drift. S3 (EMA PDF) reachable but binary/unparseable by automated fetch, consistent with the case's own disclosed MEDIUM-confidence caveat — not a new problem. S6 (PubMed) reachable but returns only a cookie-consent wall to automated fetch — reachability only, content not independently re-confirmed this session (narrative-only source, not load-bearing). S10 (beefmagazine) returned HTTP 403 — could not verify; non-load-bearing (used only as MA5's real-world anchor, not a case figure). **S9 is the real finding: the cited 0.2%/2022-audit incidence figure does not appear anywhere on the cited URL** (https://www.ag.ndsu.edu/bqa/documents/injections) — that page contains only the 1995 audit's 11% figure. Independently checked the named companion primary paper (doi:10.1093/tas/txaf150, fetched via its DOI redirect) — it explicitly states lesion presence/absence was recorded but **reports no numerical incidence figure at all**. This is exactly the "resolves but doesn't carry the figure" case P6 warns is worse than a dead link: S9's 0.2% is load-bearing (it is the current-incidence multiplier behind both options' $0.13/$0.51 expected lesion cost in the official 13.9% margin) and is unverifiable in either the cited secondary source or its own named primary reference. |

`MECHANICAL RESULT: 3 of 6 probes FAIL (P3, P4, P6). Tier 2 is not clean; TIER2_PASS may not be recorded.`

### Tier 3 — human dry-run

NOT RUN (unreachable — Tier 2 did not clear).

### Next step

Fix the 3 Tier 2 failures and re-run Tier 2 only (Tier 1 remains clean, does not need re-running unless
case.md changes again):
1. **P3/FACILITATOR.md** — add the dose-rescaling-skip trap to "The trap" section.
2. **P4/FACILITATOR.md** — resequence the Data Deep Dive to reveal only the calves-benchmark rows
   live, saving the CLSI/adult-cattle benchmark and its all-FAIL consequence for the Twist beat.
3. **P6/case.json + case.md** — either find a source that actually states the 2022 fed-cattle 0.2%
   incidence figure, or replace S9 with a figure that is genuinely verifiable, and recompute the
   $0.13/$0.51 expected lesion costs and the 13.9% margin if the replacement value differs.
4. (Non-blocking, noted under P1) consider adding the per-lesion-cost derivation to student-facing
   Appendix E so D4's cost comparison is reproducible from `case.md` alone.

`case-publish` may **not** run until Tier 2 is re-cleared (`qa.state` requires `TIER2_PASS`, not
`TIER1_PASS`).

## case-readiness run — 2026-09-01 (targeted re-check: P3, P4, P6 after fixes; P1/P2/P5 carried forward)

**State:** TIER1_PASS → **BLOCKED (staleness regression)**   **Verdict:** Tier 2 content probes now 6/6 PASS, but Tier 1 currently fails (6 BLOCKERs, all publish-staleness — not content defects). `qa.state` cannot advance to `TIER2_PASS` until the published artifacts are rebuilt and Tier 1 re-confirmed clean.

### Carried forward unchanged (per this run's scope)

| probe | verdict |
|---|---|
| P1 cold solve | PASS (carried forward, unchanged) |
| P2 both-sides | PASS (carried forward, unchanged) |
| P5 sensitivity | PASS (disclosed) (carried forward, unchanged) |

### Freshly re-verified this run

| probe | verdict | finding |
|---|---|---|
| P3 trap | **PASS** | Dispatched a genuinely fresh subagent given only `case.md` + appendices (FACILITATOR.md/QA_REPORT.md/case.json withheld). Blind, it independently predicted, before being shown either candidate: "a solver builds the Four-Day Course's AUC straight from Appendix B's curve (anchored to the ~9.07 mg/lb study dose) and plugs it into D3's fAUC/MIC check without rescaling to the labeled 3–5 mg/lb/day rate — D1/D2 read as a clean pipeline into D3, and the rescaling requirement is quarantined in Appendix G, only pulled in by D5." This matches **Trap 1** in FACILITATOR.md (the dose-rescaling error) exactly, and explicitly did not match Trap 2 (the solver noted Appendix A's close single-dose totals are telegraphed as a red herring in the Background, easy to catch, unlike the rescaling trap). Confirms Trap 1 is the real, empirically-reproducible failure mode and is now correctly named in the guide. |
| P4 twist | **PASS** | Read the full Socratic-plan/Data-Deep-Dive/Twist sequence in FACILITATOR.md. The Data Deep Dive section (lines ~195–208) now explicitly restricts the live-built D5 table to "only the calves benchmark (target 24 μg·h/mL)," reveals the Single Shot pass / Four-Day-Course 3-of-4-pass result and the 13.9% cost margin, and contains an explicit instruction: "Do not yet mention Appendix C's second (adult-cattle/CLSI) cutoff or that the target is population-specific — hold that reveal for the Twist below." The Twist section (lines ~210–220) is the first place the CLSI/adult-cattle benchmark and the "every cell flips to FAIL" finding appear. The timed plan (line 257) echoes the same restriction ("build the...table live using the calves benchmark only... Hold the second... benchmark back for the Twist"). Nothing earlier in Data Deep Dive gives away the second benchmark or its consequence — the Twist genuinely still has new information to reveal. |
| P6 data decay | **PASS** | Directly fetched https://extension.sdstate.edu/injection-site-lesions (S9's corrected URL) via WebFetch. Confirmed verbatim: "Even better, 99.8% of cattle processed in the fed cattle processing plants surveyed had no visible injection site lesions," attributed to the 2022 NBQA, byline Addie Stamps (SDSU Extension). Matches case.json's S9 value (0.2%/99.8%) and its `note` documenting the correction from the prior mis-cited NDSU URL. Spot-checked two other sources: S1 (frontiersin.org PK study) — refetched, all five parameter pairs (Cmax 13.57/8.72, Tmax 0.46/0.60, t1/2 10.47/27.96, AUC 80.21/87.35, F 69.71%/83.15%) confirmed verbatim, no drift. S7 (EntirelyPets retail pages) not re-fetched in full this run — already MEDIUM-confidence-flagged as live retail pricing in case.json, consistent with its prior pass; no new concern raised. |

`Tier 2 mechanical result: 6 of 6 probes PASS.`

### Tier 1 — re-run to confirm 0 BLOCKERs (found 6, all new/staleness — not related to P3/P4/P6 content)

Re-ran `tier1_structural.py --case the-dosing-curve`. First pass failed T1-16 (MCS-11 hash stale: recorded `2e722c636c611f45...` vs. actual `6523e529206270c3...` — case.md changed after the last QA write, corrected here as this skill's own end-of-run responsibility per established precedent, not a case defect). After correcting the hash, 6 BLOCKERs remain, all **T1-15/T1-18 continuity-staleness**, not new content problems:

- `published/MANIFEST.json`, `...Case Study.docx`, `...Data.xlsx`, `...Interactive.html` were built ~23–27 minutes **before** the last edit to `case.md`.
- `published/...Facilitator Guide.docx` was built ~27 minutes before the last edit to `FACILITATOR.md`.
- T1-18 flags the same Interactive.html staleness a second time (its own dedicated check).

This means the P3/P4/P6 fixes landed in `case.md`/`FACILITATOR.md` **after** the `published/` artifacts were last built — the published packet a student would download does not yet reflect the fixed trap language, the resequenced Data Deep Dive, or the corrected S9 citation. This is a real, current gate failure, not a stale finding from a prior run. GAPs are unchanged from the last Tier 1 pass (T1-10 reinforcement carve-out, T1-14 six FACILITATOR.md-only numbers, T1-15 nine docx-only numbers, T1-18 one Interactive.html-only number — none new).

`VERDICT: Tier 1 BLOCKED (6 blockers, 5 gaps) — all 6 blockers are publish-staleness, none are content regressions.`

### Next step

1. Run `case-publish` to rebuild `published/MANIFEST.json`, both `.docx` files, the `.xlsx`, and `Interactive.html` from the current `case.md`/`FACILITATOR.md` (this rebuild is outside case-readiness's remit — it only gates, per SKILL.md "Never").
2. Re-run `tier1_structural.py --case the-dosing-curve` — expect 0 BLOCKERs once artifacts are rebuilt (content-side checks are already clean).
3. Once Tier 1 is genuinely 0-BLOCKER, `qa.state` may be set to `TIER2_PASS` (all 6 Tier 2 probes already PASS as of this run) and `case-publish`'s human-confirm step may proceed.

`case-publish` may not run its human-confirm gate, and `qa.state` may not be written as `TIER2_PASS`, until Tier 1 is re-confirmed clean after the rebuild.

### Publish-staleness rebuild — CONFIRMED FIXED (2026-09-01, second pass)

Rebuilt `published/` from the current `case.md`/`FACILITATOR.md` (both files untouched by this
pass — no content changes made):

- `The Dosing Curve - Case Study.docx` and `...Facilitator Guide.docx` rebuilt via
  `skills/case-publish/scripts/build_docx.js`, which strips everything from
  `<!-- FACILITATOR ONLY -->` onward from the student docx.
- `The Dosing Curve - Data.xlsx` rebuilt via `build_xlsx.py`, after fixing one stale citation
  baked into the script itself: its source note said S9 was published "via NDSU Extension" —
  case.json's corrected S9 is South Dakota State University Extension
  (`extension.sdstate.edu`), not North Dakota State. No appendix data values changed.
- `The Dosing Curve - Interactive.html` was already current on trap/twist/D5 content (verified by
  grep — Trap 1/Trap 2 language, the D5/Appendix G convention-sensitivity table, and the
  margin_pct hard-line gate were all already correct), but carried the same stale NDSU-vs-SDSU S9
  citation in two spots (Sources appendix + footer source list). Patched those two lines in place
  rather than regenerating the file wholesale.
- `MANIFEST.json` updated: `case_md_sha256` now matches case.md's actual hash
  (`6523e529206270c3...`), all four file byte sizes refreshed, `built_on` and a `rebuild_note`
  added documenting this pass.

**Verified no facilitator-only leak:** rendered the rebuilt student docx to PDF
(`soffice.py --headless --convert-to pdf`, then `pdftoppm` + Read on every page image) and
confirmed no Trap 1/Trap 2 text, no "Argument for A/B," no Socratic plan, no `margin_pct`/13.9/
retuned-margin narrative anywhere in the 11-page student document — it ends cleanly at Appendix H.
Also confirmed programmatically (searched the docx's raw `word/document.xml`) that none of
`FACILITATOR`, `Trap 1`, `Trap 2`, `The trap`, `Argument for A`, `Argument for B`, `margin_pct`,
`13.9`, or `Socratic` appear anywhere in the student docx.

**Re-ran `tier1_structural.py --case the-dosing-curve`: 0 BLOCKERs** (20 checks: 16 PASS, 4 GAP,
0 FAIL — the 4 remaining GAPs are the pre-existing T1-10/T1-14/T1-15/T1-18 continuity items,
unchanged in kind from the prior Tier 1 pass, none of them publish-staleness).

`case.json.qa.state` and `qa.verdict` set to `TIER2_PASS` (all 6 Tier 2 probes — P1-P6 — already
recorded PASS above from the prior run; not re-run here per instruction). `blockers_open: 0`,
`gaps_open: 4`.

`VERDICT: TIER2_PASS — publish-staleness fully resolved, packet matches current case.md/FACILITATOR.md.`
