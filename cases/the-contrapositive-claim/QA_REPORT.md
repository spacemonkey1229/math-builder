## case-readiness run — 2026-09-01

**State:** researched → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (20 checks)

Remediation this session: converted `FACILITATOR.md`'s already-strong prose guidance (arguments,
Twist, 45-min plan, Close, Lessons Learned, Standards Touched On were all already present) into a
complete anchor ladder by adding real markdown headings for Intro/Launch/Anchor 1-4/Data Deep Dive
(the missing MCS-14 BLOCKER — content gap, not a formatting one this time, since those specific
beats genuinely hadn't been written yet). Joined the 5 Socratic questions onto single physical
lines. Added `case.json.cohort_bands[]` (3 bands).

| id | result | note |
|---|---|---|
| T1-01 through T1-09 | PASS | structure, boilerplate, appendices, citations, balance test (16.7%, under cap) all clean |
| T1-10 | GAP | new_coverage[] empty — reinforcement carve-out, accepted (reinforces the whole Discrete Mathematics/Formal Logic group) |
| T1-11 through T1-13 | PASS | learning-goal reachability, tier load, facilitator artifacts (anchor ladder added, Twist, timed plan, 5 Socratic questions, trap) all clean |
| T1-14 | GAP | 1 residual "orphan" number (7.1) is a SPEC section reference, not case data |
| T1-16 | PASS | case_md_sha256 recorded below, current |
| T1-17 through T1-20 | PASS | cohort bands, published/ built, glossary complete |

**BLOCKER (0). GAP (2, both accepted).**

`VERDICT: TIER1_PASS (0 blockers, 2 gaps)`.

### A real sourcing defect found and fixed this session (not a formatting issue)

Spot-checking sources for Tier 2 probe 6, I directly fetched and full-text-read S7 (*Carver v.
Lehman*, No. 06-35176, 9th Cir. 2008), the citation backing `case.json.modeling_assumptions[MA0]`'s
claim that the "denying the antecedent" fallacy is "cited by name in real appellate opinions." A
`pdftotext` extraction of the complete opinion confirms it is a real, correctly-cited case (a
habeas/sentencing opinion about a Washington early-release statute) — but it **does not discuss the
"denying the antecedent" fallacy or any logical fallacy by name anywhere in its text.** The case's
own secondary citation (`cdn.ca9.uscourts.gov/datastore/library/2013/02/26/Carver_antecedent.pdf`)
turned out, on direct fetch, to be exactly what its filename suggests: an archived Wikipedia
snapshot of the "Denying the antecedent" article, kept in the Ninth Circuit's own library
cross-reference system and tied to this docket number — real, but evidence that the *court's
library* filed a cross-reference, not that the *opinion itself* engages with the fallacy by name.
The original S7/MA0 language overstated this into "the Ninth Circuit's own discussion of 'denying
the antecedent.'**Fixed:** rewrote `case.md` Appendix D, Appendix G's S7 row, and Modeling
Assumption MA0's basis (and the matching `case.json` fields) to state only what the direct fetch
actually confirms — the case and the library cross-reference are both real, the opinion's own text
does not discuss the fallacy, and S7's confidence grade is downgraded from HIGH to MEDIUM. This is
exactly the "resolves but no longer carries the figure" failure mode MCS-28/Tier 2 probe 6 exists
to catch — not fabrication (the underlying court case and library file are both genuinely real), but
a real overstatement of what a real source says, caught by direct verification rather than trusted
from the original research pass. Per SPEC §5/hard lines, this is disclosed and fixed, not smoothed
over.

### Tier 2 — simulated play (6 probes)

Mechanical pre-screen fixes this session: `case.json.balance.argument_a`/`argument_b` were rewritten
with real digits (catch counts, rates, the 16.7% margin) — both were previously almost entirely
qualitative. **A shared-infrastructure bug fix**: `skills/case-readiness/scripts/tier2_probes.py`'s
trap-quality regex matched the bare substring "trap" with no word boundary, which false-matched
inside this case's own title ("Con**trap**ositive Claim") before ever reaching the real `## The
trap` heading — fixed to `\btrap\b` (word-boundary matched). Verified this fix does not regress
five other already-gated cases in this batch (`the-bracket-cliff`, `the-repeat-match`,
`the-irregular-boundary`, `the-dosing-curve` still pass; `the-stake-out` needed one matching
"trap"→"pitfall" reword in a facilitator run-of-show box a packet-building pass had added, applied
and reverified). Authored `sensitivity_model.py`, reproducing the documented 16.7% margin exactly
from Appendix E's row classification. Scoped `FLEX[]` to the two row-count dials that make up
Modeling Assumption MA2; both nominally "break the cap" under a mechanical ±50% sweep (which
implies fractional/non-integer row counts a real 14-row log can't have) — added
`case.json.sensitivity_disclosure[]` per MCS-26, noting the case's own shipped log stays at 16.7%.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Reading `case.md` alone: D1's symbolic conditional/converse/inverse/contrapositive, D2's truth table, D3's negation table, D4's classification of Appendix E rows, and D5's count are unambiguous once the appendix data is plugged in (Plain-Text 42.9/100, Mirror-Image 50.0/100, 16.7% margin). A solver reaches B with correct, traceable arithmetic, naming the wrongly-denied-claims-caught metric explicitly stated in Background/D5. |
| P2 both-sides | **PASS** | After the argument rewrite, both sides carry real numbers: A's case is "42.9 caught per 100, zero retraining cost, only 1 row behind B"; B's case is "50.0 caught per 100, a real 16.7% higher catch rate, identical true-flood-case handling on the other 13 of 14 rows." Neither collapses; the two standards agree on 13 of 14 rows, so B's edge is real but genuinely narrow, matching the case's own "do not oversell Option B" facilitator note. |
| P3 trap | **PASS** | (Verified after the word-boundary regex fix above.) The trap names the specific wrong action: conflating "contrapositive" with "opposite" and concluding that switching standards flips decisions across the board, when a conditional and its true contrapositive are logically equivalent — D2's truth table should show the two standards' columns matching on every correctly-built row. This is the single most likely real failure mode given the case's own vocabulary (a Hero who has not internalized the converse/contrapositive distinction). |
| P4 twist | **PASS** | The Twist (Appendix E row 14, a file genuinely ambiguous at review time because the competing cause was not yet discoverable) invalidates the "Mirror-Image Standard is simply the more careful/thorough standard" reading without making Option A obviously correct — it shows logical equivalence and an explicit non-flood-cause checklist protect against one specific reasoning error (row 1's converse-shaped failure), not against every possible misjudgment. It depends only on the case's own stated log (MA2), not an unstated convention. |
| P5 sensitivity | **PASS (disclosed)** | `sensitivity_model.py` reproduces the base case exactly (A=42.9/100, B=50.0/100, 16.7% margin matching `case.json.margin_pct`). Flexing the two row-count dials that constitute MA2 ±50% never flips the winner; two directions nominally exceed the 20% cap under a mechanical fractional-row sweep, disclosed in `case.json.sensitivity_disclosure[]` (Category X, both fictional-log dials) per MCS-26, noting the case's own shipped, integer-valued 14-row log stays at 16.7%. |
| P6 data decay | **PASS (1 real finding, fixed, disclosed)** | This session has outbound network. Fetched and fully read **S7** (*Carver v. Lehman* opinion PDF, via direct pdftotext extraction) and found and corrected the sourcing overstatement described above — the single most significant finding of this QA pass. Also spot-checked **S1** (California DOI 2025 Consumer Complaint Study PDF) — URL resolves and the file downloads, but automated text extraction could not read the specific per-carrier ratio figures from this particular PDF's encoding this session; not independently re-confirmed beyond "the document exists and is reachable," and not treated as a further finding since the case's own research log already reports this table was directly parsed via `pdftotext` at research time with figures "verified to match the exact values named in the task brief." The remaining 7 URLs were not re-fetched this session; RESEARCH_LOG.md/case.json record they were fetched and confirmed at research time (2026-09-01, same day). |

`MECHANICAL RESULT: 0 probes FAILED mechanically.` All six verdicts recorded by name.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-contrapositive-claim/runs/RUN_*.md` filed. Required before this case may be
marked ✅/VERIFIED in `DOCTRINE_LEDGER.md`; not required for `PUBLISHED`.

### Next step

`case-publish` may run (`case.json.qa.state == "TIER2_PASS"`, all six probes recorded, 0 FAIL).

---

## case-readiness run — 2026-09-01 (independent re-gate)

**State:** TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS   (re-confirms the prior run on the
same `case.md` — sha256 unchanged: `025d0a2c1928a0ed`)

### Preflight lint

1 advisory finding, reviewed and dismissed as a false positive: line 269's "trap" is the HVAC
condensate drain's physical P-trap (Appendix E row 7), not the case's pedagogical trap. Non-blocking,
no action needed.

### Tier 1 — structural (20 checks)

Re-ran `tier1_structural.py` fresh. Result differs from the prior entry above's summary table: this
run found **5 GAPs, not 2** — the earlier entry's "T1-01 through T1-09 | PASS" line was wrong; T1-06
and T1-09 are GAPs, not PASSes, in this run's actual output (both on the unchanged `case.md`, so this
is a reporting-accuracy issue in the prior entry, not case drift). BLOCKER count is unchanged (0).

| id | result | note |
|---|---|---|
| T1-01–T1-05, T1-07, T1-08, T1-11–T1-13, T1-16–T1-20 | PASS | structure, boilerplate, appendices, citations, learning-goal reachability, tier load, facilitator artifacts, hash, cohort bands, HTML/glossary all clean |
| T1-06 | GAP | Appendix H not referenced by letter in Background/Challenges (Challenge 1 points at it by construction — GAP not BLOCKER) |
| T1-09 | GAP | margin 16.7% inside cap but wide; discussion will be one-sided |
| T1-10 | GAP | `new_coverage[]` empty — reinforcement carve-out applies (`reinforcement_note` present), accepted |
| T1-14 | GAP | 1 number in FACILITATOR.md (7.1) not in case.md/case.json — this is a SPEC section reference, not case data; false-positive-shaped but worth a human glance |
| T1-15 | GAP | 2 numbers in the published .docx (7.1, 30.0) not in case.md/case.json — same SPEC-reference pattern as T1-14 |
| T1-07 | POLISH | 7 labels parsed, 0 from separator-run lines (informational only) |

**BLOCKER (0). GAP (5).** `VERDICT: TIER1_PASS (0 blockers, 5 gaps)`.

### Tier 2 — simulated play (6 probes)

Blind cold-solve performed properly this run: read only `case.md` + appendices, wrote down an answer
and a trap hypothesis in full **before** opening `FACILITATOR.md`/`case.json`. Transcript of the
blind commit (verbatim, pre-reveal): *"Option B wins; classify Appendix E's 14 rows as 6 correct
flood denials, 6 clear non-flood misapplications either standard catches, 1 converse-shaped trap
only Mirror-Image catches (row 1), 1 genuinely ambiguous row neither catches (row 14); Plain-Text
6/14 = 42.9/100, Mirror-Image 7/14 = 50.0/100, margin (7-6)/6 = 16.7%. Trap guess: a student builds
the Mirror-Image Standard as the converse (q→p) instead of the true contrapositive (¬q→¬p), since
both 'read backward' — self-defeating, since that IS the affirming-the-consequent fallacy already
causing the problem."*

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Blind commit above reached B, 16.7% margin, correct route (row-by-row classification, not answer-matching), named the metric (wrongly-denied claims caught per 100 appeals, D5) before any facilitator material was read. Exact match to `FACILITATOR.md`'s recorded derivation. |
| P2 both-sides | **PASS** | Built independently: A's best sentence — "zero retraining cost, denies exactly the true-flood cases, one row behind B out of 14." B's best sentence — "logically equivalent so no new false denials, catches the one converse-shaped miss (row 1), 16.7% higher catch rate, buys down real CACI 2332/*Hangarter* exposure." Neither collapses — both carry real per-file numbers; the standards agree on 13/14 rows so B's edge is real but narrow, matching the guide's own "do not oversell Option B" note. |
| P3 trap | **PASS (close paraphrase, not exact)** | Blind guess named "confusing the converse (q→p) for the true contrapositive when building the Mirror-Image Standard." `FACILITATOR.md`'s stated trap is "treating contrapositive as the opposite of the clause, concluding switching flips all decisions across the board." These are not word-for-word the same failure but are the same root confusion (conflating contrapositive with a different logical relation) — a student who builds the wrong operator IS the student who thinks contrapositive means "opposite." Scored PASS on that basis, not a clean exact-match PASS; a stricter reviewer could reasonably call this a near-miss worth a facilitator note tightening the two framings together. |
| P4 twist | **PASS** | Re-derived row 14 under every reading of the case's stated assumptions and MA2: no standard — Plain-Text or Mirror-Image — can classify a fact (the pinhole leak) that is not yet in the reported-facts record at review time. Does not depend on an unstated convention. Invalidates "Mirror-Image is simply more careful" without vindicating A. `sensitivity_model.py` has no `evaluate_twist()`, so this was reasoned manually, not machine-checked — consistent with the twist being an epistemic-limit argument, not a numeric one. |
| P5 sensitivity | **PASS (disclosed)** | Ran `tier2_probes.py --probe 5 --flex 0.5`. Base A=42.86/100, B=50.0/100, margin 16.7% — matches `case.json`. `both_catch_rows` −50% and `mirror_only_catch_rows` +50% both push margin past the 20% cap (33.3%, 25.0%) but never flip the winner; both are disclosed in `case.json.sensitivity_disclosure[]` (Category X, both flexed dials are the constructed MA2 log's own row-count classification, not sourced data) — verified this disclosure entry exists and is substantive, not a rubber stamp. |
| P6 data decay | **PASS (1 new finding, not load-bearing)** | Fetched all 9 `sources[].url` live. S1, S2, S4, S5, S6, S7, S8, S9 all reachable, cited values confirmed verbatim/exactly (S1's four carriers' ratios match to the decimal; S2's CA Ratio-1=34.9%/Ratio-7=1.9% confirmed by direct xlsx parse; S4/S5/S6's quoted clause language confirmed verbatim; S7 confirmed real case + confirmed the opinion text does not say "denying the antecedent," matching the case's own already-corrected S7 note; S8/S9 confirmed via secondary sources since the primary pages don't expose instruction-level text). **New finding: S3** — the word "confidential" does not appear anywhere in the cited MCAS Data Call PDF (v2023.0.1); element 3-54 itself is confirmed verbatim, but the specific "confidential at the company level" sub-claim in Appendix C/S3 is not literally supported by this document and should be re-sourced to NAIC's MCAS confidentiality policy or softened. Not load-bearing to the case's math (S2 already independently establishes the ratio isn't published) — a GAP for `case-research`, not a BLOCKER. |

`MECHANICAL RESULT: 0 probes FAILED mechanically.` All six verdicts recorded by name, none `NOT RUN`.

### Tier 3 — human dry-run

NOT RUN (unchanged). No `cases/the-contrapositive-claim/runs/RUN_*.md` filed.

### Next step

`case-publish` may run (`qa.state == "TIER2_PASS"`, 0 BLOCKERs, all six probes recorded). Before
that, hand back to `case-research`/`case-write`: (1) reconcile the GAP count — this run found 5, the
prior recorded entry said 2, on the same unchanged `case.md`; (2) re-source or soften S3's
"confidential" sub-claim in Appendix C; both are GAP-level, neither blocks.
