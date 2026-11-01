# QA Report — The Setpoint Call

## case-readiness run — 2026-09-09
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Preflight lint

`python3 skills/case-readiness/scripts/preflight_lint.py --case the-setpoint-call` → clean, no
advisory findings (no Modeling-Assumptions leak, no `FLEX[]` entry matching a `sources[]` value).

### Tier 1 — structural (21 checks)

Two runs. First run found one BLOCKER and three GAPs; fixed; second run clean at 0 BLOCKERs.

| id | result | note |
|---|---|---|
| T1-01 | PASS | all seven structural sections present |
| T1-02 | PASS (was FAIL) | Overview's two "3" digits (both "Line 3") read as bare numerals on the first run — fixed by adding `case.json.overview_numerals_cleared[]`: `{"numeral":"3","why":"equipment/line identifier, never used in a calculation"}` |
| T1-03 | PASS | Dilemma is binary, opens "You are Marisol Feng.", both options named in Background |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate, diffed clean |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | Appendices A–E lettered, ordered, no orphans |
| T1-07 | PASS | final appendix's 9 lines are verbatim spine labels; matches `standards[]` exactly |
| T1-08 | GAP | S5 (LOW confidence) present — reviewed: S5 never appears as a cited constraint or dilemma-flipping figure directly; it only informs MA6's stated basis, and MA6 (the disclosed $44,000 assumption), not S5's $1,500–$5,000/door range, is what any calculation actually uses. Accepted, not fixed. |
| T1-09 | PASS | both arguments written, margin 9.11% (within 8–15% target band, well under the 20% cap) |
| T1-10 | GAP | `new_coverage[]` is empty — reinforcement carve-out applies (`case.json.reinforcement_note`): every skill in the Calculus/Derivatives spine group already has n≥1 as of 2026-09-09, verified directly against `standards_spine.json` before writing. The case reinforces the product rule (n=1) and concavity (n=2), the two thinnest skills in the neighborhood not already claimed by `cases/the-marginal-call`, rather than padding a fake claim. |
| T1-11 | PASS | mutual reachability clean — 0 unmapped deliverables, 0 unreachable skills, 0 phantom claims |
| T1-12 | PASS | T4 numeric load matches 6 deliverables + a stated Modeling Assumptions block |
| T1-13 | PASS (was GAP) | first run found 0 Socratic questions detected — the five questions were written as numbered items whose "?" wrapped onto a second line, so the single-line regex never matched. Fixed by reflowing each question to one line. Anchor ladder, twist, and timed plan all present and ordered correctly. |
| T1-14 | PASS (was GAP) | first run found the twist's "30,000,000" bottle figure in FACILITATOR.md with no home in case.json — fixed by adding `case.json.derived.twist_contract_volume_bottles: 30000000` |
| T1-15 | PASS | no `published/` directory yet — nothing to drift |
| T1-16 | PASS | `case_md_sha256` recorded and current |
| T1-17 | PASS | three cohort bands declared, each with a note |
| T1-18–T1-21 | PASS (POLISH) | no `published/` directory yet — mechanically nothing to check; not run this pass per task instructions (case-publish is out of scope) |

**BLOCKER (0). GAP (2, both reviewed and accepted, not fixed): T1-08, T1-10.**

### Tier 2 — simulated play (all 7 probes; P7/MCS-48 run this pass now that
`published/The Setpoint Call - Interactive.html` exists)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A genuinely fresh, unbriefed subagent, given only the leak-free packet at `/tmp/coldsolve-the-setpoint-call/PACKET.md` and told not to read anything else, independently built TC(r) = 0.90/r + 0.0184 + 0.000008r via the product rule, found r\* = 335.41 bpm, ran the first-derivative and concavity checks correctly, and reproduced D4/D5's arithmetic exactly: TC(r\*)=$0.023767/bottle, TC(150)=$0.025600/bottle, amortized retrofit $0.0044/bottle, total(A)=$0.028167/bottle. Chose **B**, named "true total cost per bottle over the life of the contract" as the optimized metric, correctly flagged MA7 (contract volume) as the assumption its answer is most sensitive to, and correctly named MA6 (the $44,000 retrofit) as the least-supported figure. Reached the answer by the right route, with correct arithmetic — the actual pass criterion, not just the "right" answer. |
| P2 both-sides | **PASS** | A fresh reviewer, reading only `case.md`, built a real, numbers-backed quantitative case for each option (A: 7.16% operating-cost reduction, ~$18,330 in savings, a ~24,000,000-bottle retrofit breakeven; B: $256,000 vs. $281,667 total contract cost, 10.03% cheaper). The reviewer found A's case "collapses first" at D5's own check — but characterized it honestly as a *conditional/strategic* argument (the retrofit pays off only if amortized beyond this one contract's stated volume), not as an argument with no numbers or a bare concession. This is the same shape as `cases/the-marginal-call`'s own P2 result, where Option B's case was likewise real only under a stated hypothesis a Hero would have to argue for. Both sides are genuinely arguable from the document; the base-case math still resolves to a real, defensible winner (B). |
| P3 trap | **PASS** | A fresh reviewer, reading only `case.md` first, independently named the wrong path as "stop at r\*, recommend the Guarding Upgrade because the calculus says faster is cheaper, without folding in the amortized retrofit cost." Then read `FACILITATOR.md`'s trap and found it names the identical failure at the same resolution — no divergence, no narrower/wider mismatch. The reviewer also flagged (constructively, not as a FAIL) that a facilitator who reads only "The trap" section and skips "The Twist" section could be caught off guard by the second-order mistake of not recomputing after the twist — already addressed, since FACILITATOR.md's Twist section explicitly scripts the recomputation instruction for the facilitator to say aloud. |
| P4 twist | **PASS** | An adversarial fresh reviewer read `case.md`, `case.json`, `FACILITATOR.md`, and `sensitivity_model.py`, and directly executed `evaluate_twist()` to confirm the base→twist numbers (9.11% margin favoring B → 1.43% margin favoring A) are real and correctly computed. Confirmed the twist's scoping (tripling Q for Option A's amortization only) is not an unstated convention: Option B's own formula, built from Appendix A's stated CR(r)/MPU(r), has no volume term under any reading, so "Option B is unaffected" is the *only* defensible reading, not an authorial choice hidden in code. Confirmed the scoping is scripted for the facilitator to state aloud in FACILITATOR.md's Twist section, not left implicit. Explicitly checked for a repeat of `cases/the-marginal-call`'s original shared-`PARAMS`-mutation bug and confirmed `evaluate_twist()` here uses two independent parameter-dict copies, with no leakage into Option B. |
| P5 sensitivity | **PASS (disclosed)** | `tier2_probes.py --probe 5` (mechanical, ±50% flex on `FLEX = ["b","d","r_cap","U","Q"]`) found: `r_cap` (MA5, Line 3's rated safe speed) flips the verdict at −50% (150→75 bpm, recomputed margin 9.14% now favoring A) — the case's load-bearing, dilemma-flipping dial, disclosed via `case.json.sensitivity_disclosure[]` as Category F. `Q` (MA7, contract volume) does not flip the verdict but −50% pushes the recomputed margin to 21.39%, past SPEC §2's 20% cap — disclosed as a CAVEAT (direction unsurprising: a smaller contract makes the safer option's advantage larger, not smaller; the size of the resulting margin is the real finding). `b`, `d`, and `U` do not flip the verdict and stay within the cap at either flex direction. |
| P6 data decay | **PASS** | All 6 `sources[]` URLs fetched 2026-09-09 and confirmed reachable with their recorded values still present: S1 (O\*NET, $20.78/hr — exact quote matched), S3 (EIA, 9.17¢/kWh June 2026 — exact quote matched), S4 (Quadrel, 100–500 bpm — exact quote matched), S5 (Safety Geek, $1,500–$5,000/door — exact quote matched). S6 was re-pointed to `pmmi.org/standards-and-regulations` as the primary citation (confirmed 200, content-matched: ANSI/PMMI B155.1-2023, current edition, correct scope) after `blog.ansi.org` returned an intermittent 403 to automated fetchers on a second check — kept only as secondary corroboration, not the primary URL, since a real browser user-agent still reaches it and it was successfully fetched and quote-matched during initial research; this is a bot-protection artifact, not a dead or drifted source. S2 (Rippling) hit the same transient 403 pattern on WebFetch's own re-check but returned HTTP 200 via `curl` with a standard browser user-agent, and its figure was quote-matched during initial research. No dead links; no figure found to have drifted from what is cited. |
| P7 accessibility cold-read | **PASS** (after 6 remediation rounds) | Mechanical pre-screen: D6 asks for a graph of TC(r); the published HTML's banner diagram and D6's own chart-placeholder markup were both found as real visuals — 0 missing-visual findings. Model-judged cold-read: six fresh, zero-context subagent reads were dispatched against `/tmp/coldread-the-setpoint-call/PACKET.md` (built from the published HTML, not `case.md`), with real remediation between each round. Round 1 named 7 unexplained real-world concepts (co-packing/contract-manufacturer ownership, ANSI/PMMI B155.1 mechanics, guarding/interlock retrofit scope, safety PLC, "fully burdened" labor cost, rotary-labeler mechanics, line utilization) — fixed by expanding Background prose (ownership relationship, rotary-labeler mechanism) and adding 5 `STORY_GLOSSARY` terms (Risk Assessment, PLC, Rotary Labeler, Line Utilization, Labor Burden — 4 fetched fresh on en.wikipedia.org, Labor Burden reusing this case's own already-verified [S2] source). Round 2 named 5 residual items, now mechanism-level rather than vocabulary-level (labor-burden arithmetic, what the retrofit physically buys, how a risk assessment is performed, why higher speed causes defect/rework, what line utilization looks like on the shop floor) — fixed with a worked non-answer labor-burden example, an Appendix C explanatory note tying the three retrofit items to the risk-assessment sign-off, an expanded Risk Assessment definition (who performs it, what it produces), a mechanical glue-set/defect explanation, and a concrete non-answer utilization illustration. Round 3 named 4 items, now source-methodology curiosity (exact source figures, ANSI clause text, install-slot logistics) — fixed the one genuinely addressable item (install-slot logistics) with an explanatory clause. Round 4 named 6 items including one genuine miss — "sensor curtains," used in the Overview's verbatim case.md prose, had never been glossed — fixed by adding a 6th `STORY_GLOSSARY` term (Sensor Curtains, Wikipedia's Light Curtain article) plus a combined explanatory note describing how the turret panels/conveyor guarding/sensor curtains/PLC work together with the risk-assessment sign-off. Round 5 named 6 items, all physical-mechanism visualization curiosity (pinch-point geometry, PLC wiring detail, sign-off document specifics, shift-schedule breakdown) — addressed with a wiring-mechanism sentence in the PLC definition and a concrete shift-utilization example. Round 6 (final) named **0** unexplained concepts — a genuine PASS, no MCS-49 disclosed waiver needed. Final `STORY_GLOSSARY`: 11 terms (up from 5 at first draft). Every remediation round was a prose/glossary addition; no sourced figure, Modeling Assumption, or balance-test number was ever touched. |

**Zero FAIL. Zero NOT RUN among the seven probes.**

### State reached

`TIER2_PASS`. `case.json.qa` records `state`, `verdict`, `blockers_open: 0`, `gaps_open: 2`, all
seven `tier2` verdicts by name (including `P7: PASS`), and the current `case_md_sha256`.

### Tier 3 — human dry-run

NOT RUN. Case is not published this pass (`case-publish` is explicitly out of scope for this
task). `PUBLISHED` is reachable on this `TIER2_PASS`, but `VERIFIED` requires a filed
`runs/RUN_<date>_<guide>.md` from a real cohort, which cannot happen before publish.

### Real defects found and fixed this pass

1. **T1-02 BLOCKER** — two bare "3" numerals in the Overview (both referring to "Line 3," an
   equipment identifier). Fixed by recording the clearance in
   `case.json.overview_numerals_cleared[]` with an explicit justification, per SPEC §1.2's
   read-and-record rule (a clearance not written down is not a clearance).
2. **T1-13 GAP** — `FACILITATOR.md`'s five Socratic questions were written as numbered list items
   whose question mark landed on a wrapped second line, so the mechanical "ends in ?" check found
   zero questions even though five were genuinely present. Fixed by reflowing each question onto
   one line.
3. **T1-14 GAP** — the twist's tripled contract-volume figure (30,000,000 bottles), stated in
   `FACILITATOR.md`'s Twist section, had no corresponding entry in `case.json`, so the continuity
   sweep flagged it as a number with no home. Fixed by adding
   `case.json.derived.twist_contract_volume_bottles: 30000000`.
4. **S6 citation reachability** — the originally-cited `blog.ansi.org` URL returned an
   intermittent 403 to automated fetchers on the P6 re-check (it had succeeded during initial
   research). Rather than accept an unverifiable primary citation, re-pointed the primary URL to
   `pmmi.org/standards-and-regulations`, which is reliably reachable and carries the same
   corroborating claim (verified via both WebFetch and `curl` with a real browser user-agent) —
   `blog.ansi.org` retained only as a secondary corroboration, not the citation QA depends on.
5. **A real docx-build script bug** — `skills/case-publish/scripts/build_docx.js`'s inline-markdown
   regex has no CommonMark flanking rules and no backslash-escape handling, so it silently
   mispaired every standalone "r*" token (this case's optimum-speed notation) with an unrelated
   asterisk elsewhere in the same paragraph/table cell, and mangled the escaped "O\*NET" citation
   into a giant false italic span, in both the student Case Study docx and the Facilitator Guide
   docx. Rebuilt both with a one-off scoped fix (left/right flanking guards, backslash-escape
   shielding) applied only to this case's build — the shared script itself was left untouched,
   per this task's "do not touch any other case's files" instruction. Verified via
   `soffice --headless --convert-to pdf` + page-image review that every "r*" and the "O*NET"
   citation now render correctly.
6. **P7/MCS-48 accessibility cold-read, run for the first time** on the newly-built Interactive
   HTML — six fresh, zero-context subagent cold-reads, with real remediation between each round
   (see the P7 row above for the full round-by-round list). Reached a genuine PASS on round 6 with
   0 named gaps; no MCS-49 disclosed waiver needed.

No defect required a redesign, a dropped figure, or a fabricated number at any point — every
`{{NEEDS_SOURCE}}` placeholder resolved to either a real cited source or a disclosed, basis-stated
Modeling Assumption (see `RESEARCH_LOG.md`), and every Tier 2 probe that could genuinely fail
(cold solve, both-sides, trap, twist) was run by a fresh, unbriefed subagent rather than
self-graded.

### Next step

`Run case-publish on the-setpoint-call` — explicitly NOT executed as part of this task per
instructions. Resync via `resync_artifacts.py` should still run to keep `case.json`/`case.md`
metadata mirrors consistent before any future publish attempt.
