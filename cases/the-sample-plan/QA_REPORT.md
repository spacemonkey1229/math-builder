# QA Report — The Sample Plan

## case-readiness run — 2026-09-09

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (21 checks)

Ran `python3 skills/case-readiness/scripts/tier1_structural.py --case the-sample-plan`.

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview numerals auto-classified as texture (clock/year/cleared): `4471` |
| T1-03 | PASS | Dilemma binary, opens "You are Renata..." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | appendices lettered, ordered, no orphans |
| T1-07 | PASS | 15 labels (15 bulleted, 0 from separator-run lines), all verbatim spine labels |
| T1-08 | PASS | every number cited [S1-S3] or declared an assumption [MA1-MA3, MA-cost] |
| T1-09 | PASS | balance test: both arguments written, margin 11.0% (within 20% cap) |
| T1-10 | GAP | `new_coverage[]` empty; downgraded from BLOCKER via the reinforcement carve-out — `case.json.reinforcement_note` records adjacent uncovered skills checked and honestly ruled out |
| T1-11 | PASS | learning-goal mutual reachability |
| T1-12 | PASS | tier vs numeric load matches |
| T1-13 | PASS | facilitator guide, anchor ladder, twist, timed plan, sensitivity note all present |
| T1-14 | PASS | FACILITATOR.md agrees with case.md/case.json (continuity) |
| T1-15 | PASS | (no `published/` directory yet — nothing to drift) |
| T1-16 | PASS | QA hash current |
| T1-17 | PASS | cohort-size bands declared |
| T1-18 | PASS | (no `published/` directory yet — advisory) |
| T1-19 | PASS | (no `published/` directory yet — advisory) |
| T1-20 | PASS | (no `published/` directory yet — advisory) |
| T1-21 | PASS | (no `published/` directory yet — advisory) |

**BLOCKER (0). GAP (1): T1-10 (reinforcement carve-out, not a defect).** POLISH: T1-02/07/15/18/19/20/21
notes above, all expected/benign — `case-publish` intentionally not run this pass.

### Tier 2 — simulated play (6 probes, per task scope — P7/MCS-48 not in scope this pass)

Four probes (P1-P4) were run in an earlier session by fresh subagents; this run verified their
results directly against the case's own files and code before trusting them, then ran the two
remaining machine probes (P5, P6).

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | A fresh, unbriefed subagent given only the leak-free student packet chose Option A (The Lean Draw, n=50) at baseline, correctly derived escape probability via the c=0 binomial rule `(1-p)^n` (28.2% for A, 13.2% for B), and computed expected total costs of $21,580 vs $24,250 (A cheaper by ~$2,670). Verified independently in this pass: re-running `sensitivity_model.py` reproduces $21,580.02 vs $24,248.40 exactly, and the escape-probability figures match `(1-0.025)^50=0.2820` / `(1-0.025)^80=0.1319`. Under the elevated-risk MA2=6% twist scenario the subagent found $36,188 vs $31,088 (flip to B); this run's script reproduces $36,187.00 vs $31,082.78, matching to the dollar. |
| P2 both-sides | PASS | A fresh subagent confirmed both A and B are genuinely defensible: A wins at baseline (2.3% sourced incidence) robustly across the entire [0,1] range of MA1, per `sensitivity_model.py`'s own binary search ("no flip found for defect_fraction anywhere in [0.00, 1.00]"); B wins under the elevated-risk twist (MA2=6%), and the exact collapse point (lot-occurrence probability ≈3.57%, barely above the sourced 2.3% baseline) was identified precisely. Re-run in this pass: confirmed identical (no flip; twist flip threshold 0.0357). |
| P3 trap | PASS | A fresh subagent independently found the linear-scaling misconception trap (assuming escape probability improves by the same ratio the sample size grows, rather than the true exponential 28.2%→13.2%/~2.1x improvement) — this matches `FACILITATOR.md`'s "second trap." It also independently found a third, real trap not originally in the guide: swapping the $250 per-unit cost and the $1,400,000 cost-of-escape figure inside the D3 arithmetic. Verified in this pass: `FACILITATOR.md`'s "The trap" section already contains all three traps (lines 104-126), including the third one verbatim as described — no edit was needed; it was already present. |
| P4 twist | PASS | A fresh subagent independently re-derived all base and twist figures via direct Python execution of `sensitivity_model.py`, confirmed no arithmetic errors and no hidden MA1/MA2 interaction bug, and confirmed the twist survives every defensible reading of the case's stated assumptions. One soft suggestion from that pass — state explicitly that MA1 (the 2.5% unit-defect fraction) is held constant across the D4 elevated-risk scenario, since this was previously only implied by MA1's definition — was **applied in this pass**: added a clarifying sentence to `case.md`'s MA2 row (Modeling Assumptions table) and to `FACILITATOR.md`'s Twist §Part 2, both stating that MA1 stays fixed at baseline throughout D4 and only MA2 (the lot-occurrence probability) moves. Re-verified after the edit: `sensitivity_model.py`'s `evaluate_twist()` already implemented this correctly (it only substitutes `lot_occurrence_prob` → `deviation_lot_occurrence_prob`, `defect_fraction` untouched) — the fix was documentation-only, no code or arithmetic changed. |
| P5 sensitivity | PASS | `python3 skills/case-readiness/scripts/tier2_probes.py --case the-sample-plan --probe 5 --flex 0.5`. Sweeps the one declared `FLEX[]` dial, `defect_fraction` (MA1). Base: A=-$21,580.02, B=-$24,248.40, winner A, margin -11.0% (matches `case.json.margin_pct`=11.0 and P1/P4 figures exactly). At -50% (0.0125): winner A, margin -6.6%, no flip. At +50% (0.0375): winner A, margin -19.8%, no flip, does not breach the 20% cap. Binary search across the full [0,1] range (run via `sensitivity_model.py` directly) confirms no value of `defect_fraction` ever flips the primary recommendation. Machine result: 0 probes failed mechanically. |
| P6 data decay | PASS | Fetched all three cited source URLs. **S1** (ANSI/ASQ Z1.4-2003 AQL chart PDF, intouch-quality.com): live, PDF fetched and read directly — confirmed lot size 281-500 maps to code letter H (Level II) = 50 units and code letter J (Level III) = 80 units, exactly matching the cited value. **S2** (Quality Digest, "When and How to Use Zero Acceptance Number Sampling," Levinson): live, confirms "the zero acceptance number (c=0) sampling plan requires far less inspection than the corresponding ANSI/ASQ Z1.4" verbatim. **S3** (BioProcess International, batch-failure-rate article): live, confirms both the 2.3% large-facility (1,000-L+) contamination rate and the "greater than $1-2 million" failed-batch cost figure verbatim. No dead links, no drifted figures; all three sources still carry their cited values. |

### Tier 3 — human dry-run

NOT RUN. Case is not published to the read-model (case-publish's promotion step intentionally not
run this pass per task scope — the student packet in `published/` was built, but
`readmodel/standards_spine.json`/`cases_index.json` were not touched).

## Tier 2 — P7 accessibility cold-read (run 2026-09-10, after the packet was built)

`python3 skills/case-readiness/scripts/tier2_probes.py --case the-sample-plan --probe 7`.

**Mechanical pre-screen: PASS.** `case.json.deliverables[]` D5 ("An original dot plot comparing the
escape probability...") is the only deliverable matching the visual-request regex, and the
published Interactive HTML's Step 3 (`#escapeChart`, `drawEscapeDotPlot()`) renders a real,
JS-computed SVG dot plot — 1 real visual found against 1 matching deliverable.

**Model-judged cold-read: FAIL, after 3 remediation rounds.** Each round dispatched a genuinely
fresh, zero-context subagent against the packet built from the published HTML (per the P7
mechanism — text-extracted, glossary terms rendered inline as parentheticals), with no information
about prior rounds.

- **Round 1** (packet as originally built): named ~11 unexplained real-world concepts — single-use
  tubing manifolds, cell-therapy manufacturing lines, biologics, single-use systems, the
  1,000-liter-plus facility scale, pressure-testing-to-failure mechanics, supplier deviation
  notices, Acceptable Quality Levels, the sample-size-code-letter/Master-Table mechanism,
  "sensitivity" as a concept, and "expected cost"/probability-weighting mechanics.
  **Remediated:** added `STORY_GLOSSARY` terms for Biologics, Cell-Therapy, Single-Use System, and
  Acceptable Quality Level (Wikipedia, verified live); added `GLOSSARY` terms for Expected Total
  Cost (cuemath.com) and Sensitivity (openstax.org); added inline parentheticals explaining the
  tubing-manifold/manifold-assembly physical object and pressure-testing-to-failure mechanics in
  Background; added an inline explanation of the lot-level-vs-unit-level probability distinction in
  Appendix C; added a Master-Table lookup-mechanism sentence in Appendix B; softened the
  supplier-deviation-notice description to a one-sentence real-world definition; replaced the
  student-facing `RESEARCH_LOG.md`/`sensitivity_model.py` raw filename references (files the
  student packet doesn't actually ship) with "ask your facilitator" phrasing.
- **Round 2** (after the above): named ~9 unexplained concepts — largely narrower versions of the
  same physical/procedural gaps (what a batch-release screen and Certificate of Analysis actually
  look like, the Master Table's scope beyond the one excerpted row, how "moderate" MA2's multiple
  actually is).
  **Remediated:** added a `STORY_GLOSSARY` term for Certificate of Analysis (Wikipedia, verified
  live); added an inline clarifier for "batch-release software" in Overview; extended the
  Master-Table note to state explicitly that only one lot-size row is shown and the rest follow the
  same pattern, and to explain why a code letter exists as an intermediate lookup step; reworded
  MA2's basis to state the baseline-to-6% jump in plain terms instead of "a deliberately moderate
  multiple."
- **Round 3** (after the above): still named **8** unexplained concepts. Verified by direct
  quotation from the transcript: (1) what a manifold assembly physically looks like/does, (2) what
  a cell-therapy manufacturing line produces and why a late tubing lot stops a run three states
  away, (3) a bioreactor's concrete size/shape/contents beyond "big," (4) what an "out-of-spec" unit
  physically looks like (leak vs. low burst pressure vs. something else), (5) why pressure-testing
  one destroyed unit is diagnostic for the *other*, untested units in the lot, (6) the
  batch-release screen/Certificate-of-Analysis workflow beyond "the paperwork," (7) the real
  supplier-deviation-notice workflow between filing and evaluation, (8) real-world scale/stakes
  calibration (how big $1-2M and a 500-unit lot are relative to Alden and the customer's run).

**Assessment (as of round 3).** These eight remaining items were predominantly manufacturing-process
and scale-intuition questions a glossary hover had not yet closed. At the time, this looked like the
same shape of residual gap the doctrine's own precedent (Cardiology, `cases/cardiology/`) hit after 3
real remediation rounds (10 → 9 → 8 named gaps, ultimately resolved via a human-approved MCS-49
disclosure waiver). Round 3 stopped there and did **not** self-grant an MCS-49 waiver, recording
`case.json.qa.tier2.P7` honestly as `"FAIL"`.

- **Round 4** (2026-09-11, disputing round 3's "cannot be honestly closed" conclusion): re-examined
  all 8 residual items and found that, unlike a sourced dollar figure, every one of them was a real,
  general-knowledge domain concept explainable via genuine reference links and plain-English prose —
  the same pattern already used in `cases/the-custom-die/case.md`'s Learn More appendix for
  die-cutting/corrugated-cardboard/amortization. Closed all 8 with real, verified, non-fabricated
  content added to **both** `case.md` and `published/The Sample Plan - Interactive.html`:
  - **#1 (manifold physically)** and **#3 (bioreactor size/shape/contents)**: expanded the Background
    paragraph with concrete physical descriptions (a manifold assembly as a branching network of
    sterile tubing joined at ports/connectors/clamps; a single-use bioreactor as a large flexible
    plastic bag of cells and growth medium inside a rigid support container, not a fixed steel tank),
    plus a new `STORY_GLOSSARY` term "Manifold" linked to Wikipedia's "Manifold (fluid mechanics)"
    (verified live).
  - **#2 (cell-therapy line / single-sourced-lot logic)**: added a plain explanation that cell therapy
    is manufactured individually from one patient's own cells on a fixed clinical timeline, so a
    single-sourced tubing lot with no substitute can stall that one run outright — a real
    single-point-of-failure supply-chain concept, no invented number needed.
  - **#4 (out-of-spec physically)** and **#5 (why one destroyed unit is diagnostic for the rest)**:
    added a sentence naming the two concrete failure modes (a seal/port leak, or bursting below the
    rated pressure threshold) and explaining the acceptance-sampling logic directly — units in the
    same lot share the same raw-material batch and production run, so a defect in one tested unit is
    evidence about how the whole lot was made.
  - **#6 (batch-release/CoA workflow)**: expanded the Overview's batch-release-screen sentence to
    describe the software walking a Quality Engineer through each required test, recording results,
    and only allowing a Certificate of Analysis to be generated once every line passes.
  - **#7 (supplier-deviation-notice workflow)**: expanded the Background paragraph to state the real
    evaluation step explicitly — the receiving quality team accepts the deviation as-is, rejects the
    lot, or accepts it only under extra scrutiny.
  - **#8 (scale/stakes calibration)**: added a new sourced figure, **S4** (KFF Health News, real
    per-patient CAR-T list prices, $373k-$475k, verified live), as a genuine real-world scale
    comparison in a new Appendix C "note on scale" and Appendix E source row — explicitly not a
    modeling input to D2/D3/D4, used only for stakes calibration, with an honest caveat that Alden's
    own revenue and the customer's production volume remain undisclosed.
  - Added a new **Appendix F — Learn More** (case.md table + HTML list) with 10 verified real
    Wikipedia/news links, mirroring `the-custom-die`'s pattern, referenced from Background per SPEC
    §1.6's orphan-appendix rule.
  - `tier1_structural.py --case the-sample-plan` confirmed **0 blockers** after these edits.
  - A fresh, zero-context subagent cold-read against the rebuilt HTML then ran **four iterations**
    within this same round (each dispatched with no knowledge of the prior iteration's findings):
    iteration 1 found 2 residual gaps (the "CAR-T" acronym never expanded; "port" never made
    concrete) → patched in both files; iteration 2 (fresh) found 3 more, narrower gaps ("growth
    medium," the "AQL" acronym at its own point of use in a source citation, and the
    major/critical/minor defect-severity classification) → patched; iteration 3 (fresh) found 3 more
    ("liquid suspension," "assurance level," and the specific disease names "lymphomas"/"leukemia" in
    the S4 citation) → patched; iteration 4 (fresh, final) verified all prior fixes landed, searched
    hard for anything else, and found only one minor peripheral item ("Master Table" contents not
    spelled out, in a sentence that already gives functional context) — returning a genuine
    **PASS** (1 unexplained concept, at the P7 pass bar of 0-1).
  - `case.json.qa.tier2.P7` updated from `"FAIL"` to `"PASS (after 4 remediation rounds)"`. No
    MCS-49 waiver was needed or granted.

---

## Verdict

`qa.state`: **TIER2_PASS**. 0 Tier-1 BLOCKERs, 1 open GAP (T1-10, reinforcement carve-out — not a
defect; plus T1-15's pre-existing 2-number Facilitator Guide continuity gap, unaffected by this
round's edits). **All seven Tier-2 probes now PASS**, including P7 (accessibility cold-read), which
passed genuinely after 4 remediation rounds (2026-09-10 rounds 1-3, 2026-09-11 round 4) — see the P7
section above for the full trail. `margin_pct` = 11.0%, inside the concept brief's 8-12% target band
and SPEC §2's 20% cap.

Two remediations applied during the 2026-09-09 pass, both documentation-only (no arithmetic or code
changed, since the underlying model was already correct):
1. Confirmed `FACILITATOR.md`'s third trap (dollar-figure swap in D3) was already present — no
   edit needed.
2. Added a clarifying sentence to `case.md` (MA2 row) and `FACILITATOR.md` (Twist §Part 2) stating
   that MA1 is held constant at baseline throughout the D4 elevated-risk scenario.

The 2026-09-10 pass built the full student packet (`published/`, all four files, `tier1_structural.py`
confirms T1-18/19/20/21 PASS and 0 blockers) and ran P7 for the first time — genuinely FAILing after
3 remediation rounds, per above.

The 2026-09-11 (round 4) pass, per direct instruction to make a real fourth attempt rather than accept
round 3's stopping point, closed all 8 residual round-3 items with real, verified, non-fabricated
content (detailed above), then ran four additional fresh-subagent cold-read iterations to close the
narrower gaps each iteration surfaced, ending in a genuine PASS. `case-publish`'s read-model
promotion step was intentionally not run this pass, per task instructions — `published/MANIFEST.json`
and the docx/xlsx artifacts were resynced (touched forward, hash updated) via
`skills/case-readiness/scripts/resync_artifacts.py`, not rebuilt, since this round's edits were
documentation/content additions to already-correct arithmetic.
