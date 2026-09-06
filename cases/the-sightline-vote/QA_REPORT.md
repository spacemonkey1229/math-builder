## case-readiness run — 2026-09-05
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Preflight lint
Clean — no advisory findings.

### Tier 1 — structural (21 checks)

First pass: 2 BLOCKERs (T1-06 Appendix E orphaned by a line-wrap splitting "APPENDIX" and "E"
across a hard newline so the reference regex never matched; T1-11 deliverable D5 mapped to no
skill) and 4 GAPs. Fixed: reflowed the Background sentence so "APPENDIX E" is not split across a
line break; added the three already-covered arithmetic skills
(`advanced-numbers-how-to-multiply-decimal-numbers`, `-divide-decimal-numbers`,
`-find-the-percent-of-a-number`) to D5's `skills[]` and to `standards[]`/Appendix G's "how to…"
list (mirroring roofline-call's D5 pattern); reformatted FACILITATOR.md's 5 Socratic questions
onto single lines so the numeral+`?` regex could see them (T1-13); added 9 orphan figures
(relative-gain percentages, the twist's grant terms, the co-interior/supplementary angle values,
the twist's net cost) into `case.json.derived` so FACILITATOR.md's numbers are all traceable
(T1-14); recorded `case_md_sha256` (T1-16).

Second pass:

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview 226 words, no load-bearing numerals; "two years ago"/"eleven days"/"ten days" cleared as texture |
| T1-03 | PASS | Dilemma binary, opens "You are Dana Whitcombe." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | numeral form `N.)` consistent |
| T1-06 | PASS | appendices A–G, lettered, ordered, no orphans |
| T1-07 | PASS | all 21 final-appendix lines verbatim spine labels (16 vocabulary + 5 how-to) |
| T1-08 | PASS | every number cited (S1–S3) or a declared Modeling Assumption (MA1–MA3) |
| T1-09 | PASS | both arguments written, margin 14.56% ≤ 20% |
| T1-10 | GAP (accepted) | `new_coverage[]` is empty by design — all 18 Geometry/Fundamentals skills already sit at n=2; `reinforcement_note` records the adjacent-coverage check (only Geometry n=0 skill is `geometry-how-to-find-the-volume-of-a-sphere`, not forceable here). Downgraded from BLOCKER to GAP per the 2026-08-17 reinforcement carve-out, same doctrine roofline-call's sibling T1-10 carve-out (legacy conversion) rests on. |
| T1-11 | PASS | mutual reachability — 0 unmapped deliverables, 0 unreachable skills |
| T1-12 | PASS | T2 tier matches numeric load (multi-step angle derivation + cost ratio, two competing variables) |
| T1-13 | PASS | facilitator guide, anchor ladder, twist, timed plan, 5 Socratic questions, trap, sensitivity note all present |
| T1-14 | PASS | continuity — every FACILITATOR.md number traced to case.json.derived or case.md |
| T1-15 | PASS | no published/ yet, nothing stale |
| T1-16 | PASS | hash current |
| T1-17 | PASS | cohort_bands[] declared, 3 bands |
| T1-18 | PASS | no published/ yet (nothing to check) |
| T1-19 | PASS | no published/ yet (nothing to check) |
| T1-20 | PASS | no published/ yet (nothing to check) |
| T1-21 | PASS | no published/ yet (nothing to check) |

BLOCKER (0). GAP (1): T1-10 (accepted reinforcement carve-out, see above). POLISH (6): T1-07
label-parsing note (informational); T1-15/18/19/20/21 "no published/ directory yet" (expected
pre-publish).

**VERDICT: TIER1_PASS**

### Tier 2 — simulated play (6 probes required by this run; P7 also executed by the script but is
out of scope for this pass per instruction)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | A genuinely fresh, unbriefed subagent given only the leak-checked student packet reached Option B, correctly named safety-score-per-dollar as the graded metric, independently reproduced the 2.058e-6 vs 2.358e-6 arithmetic (angles, costs, and the 14.6% margin all matched `case.json.derived` exactly), correctly flagged MA2 (the $80,000 land cost) as both the most sensitive assumption and the least-supported figure, and even computed its own breakeven point (~$24,150) showing the recommendation would flip under a plausible land-cost revision — a genuine, useful finding, not an error. Reached the intended answer for the intended reason. |
| P2 both-sides | PASS | See below (Note A) |
| P3 trap | PASS | A fresh subagent reading `case.md` alone predicted the exact trap named in `FACILITATOR.md`: treating raw safety-score magnitude (90° beats 75°) as the decision criterion without running D5's score-per-dollar division. The guide anticipates the real trap; both the case and the guide's own honest "Lessons Learned" placeholder agree the D4 angle-pair mechanics are a secondary, more mechanical failure mode, not the primary trap. |
| P4 twist | PASS | (1) The twist invalidates the position "B wins the graded metric, therefore it's the obvious recommendation" — a real position Anchor 1's vote would produce. (2) Re-derived under the case's own stated Appendix C/D figures exactly as written (no ambiguous convention: total costs $485,880/$409,660 are unambiguous arithmetic) and cross-checked against `sensitivity_model.py`'s `evaluate()`/`evaluate_twist()` divergence: twist scores A=5.1453e-6, B=2.3579e-6, margin 118.22%, matching `FACILITATOR.md` exactly. The twist's grant terms (85° threshold, 60% share) are genuinely new information withheld until the Twist beat (per SPEC §7.2), not a reinterpretation of an existing case.md assumption, so there is no unstated-convention risk. The twist fully reverses the winner (not merely erodes the margin). |
| P5 sensitivity | PASS (disclosed) | `sensitivity_model.py` flexes both declared assumptions (`base_cost_usd`, `land_cost_usd`) ±50%, one at a time. Neither flips the winner (Option B wins at every tested combination) but both push the margin outside the SPEC §2 20% cap at their extremes (`base_cost_usd` −50% → 31.7%; `land_cost_usd` +50% → 24.0%). This is a real instability in the SIZE of the margin, not the winner, and unlike roofline-call's assumptions (which touched nothing graded) it could not be waved off as inapplicable — it required an actual disclosure. Added `case.json.sensitivity_disclosure[]` with Category-X (proprietary/inaccessible, good-faith-estimate-from-analogue) entries and a real justification for both params, per the 2026-08-13 disclosure-aware pass state. `tier2_probes.py` now reports `PASS (disclosed)`, not silently hidden. |
| P6 data decay | PASS | S1 (up.codes / Caltrans HDM) — reachable, value confirmed verbatim ("should not be less than 75 degrees"). S2 (FHWA-HRT-20-067 index page) — reachable, publication number/date and abstract confirmed verbatim. S3 (Idaho Falls Public Works) — reachable, value confirmed verbatim ("$21.00 per linear foot"). All three sources are 0 days old as of this run (accessed the same day they were cited) and none has drifted or moved. |

**Note A — P2 both-sides adjudication:** A fresh subagent, given only `case.md`, built independent,
non-conceding, numeric best-sentence arguments for both sides: for A, "the only option that hits
the model's maximum possible safety score — sin(90°) = 1.000, a full 15° above the state's 75°
legal minimum... and it's the fix both crash reports recommended outright"; for B, "still clears
the state's binding 75° minimum... while costing $76,220 less (15.7% cheaper)... and beating the
Squared Corner on the case's own safety-score-per-dollar test by 14.6%." Asked which side collapses
first, the subagent correctly identified that A loses the case's own D5 tie-breaker question
arithmetically (2.058e-6 < 2.358e-6 per dollar) and has no further *quantitative* rebuttal to that
specific question — but this is losing the graded metric, not collapsing to zero numbers: A still
holds real, undisputed ground (perfect safety score, 15° of legal margin, explicit crash-report
endorsement) independent of D5. B was pressed on its own weak point (zero margin above the legal
floor, 75°−75°=0°) and answered with real numbers rather than folding. Consistent with
roofline-call's own P2 precedent: neither side collapses to having no numbers, they are defensible
on two different real questions, which is the design intent, not a paper margin.

**VERDICT: TIER2_PASS** (all six required probes recorded, 0 FAIL; P7 recorded separately below
for completeness though out of this run's required scope)

### Tier 2, P7 (recorded for completeness, not required by this run)
Mechanical pre-screen FAILED: D1 asks for a labeled diagram/sketch and no `published/` directory
exists yet, so there is no interactive HTML to check for a real visual. This is expected and not
a defect — the case has not been published yet. Re-run P7 once `published/` exists.

### Tier 3 — human dry-run
NOT RUN. `PUBLISHED` is reachable without it; `VERIFIED` is not. No `runs/` directory yet.

### Corrections made during this run
- Fixed a line-wrap bug in Background that orphaned Appendix E from T1-06's reference regex.
- Added 3 already-covered arithmetic skills to D5 and Appendix G to clear a T1-11 BLOCKER
  (unmapped deliverable) — mirrors roofline-call's own D5 pattern exactly.
- Reformatted FACILITATOR.md's Socratic questions onto single lines to clear a T1-13 GAP.
- Added 9 previously-orphaned FACILITATOR.md figures into `case.json.derived` to clear a T1-14 GAP.
- Added `case.json.sensitivity_disclosure[]` (2 Category-X entries) to convert a genuine P5
  mechanical FAIL into a disclosed PASS, per the 2026-08-13 disclosure-aware pass state — the
  underlying instability (margin size, not winner) is real and is not hidden by this.
- Recorded `case_md_sha256` and `qa.state = TIER2_PASS`.

**Next step:** human review, then `case-publish` on `the-sightline-vote` (not run by this agent
per instruction — stopping here at `TIER2_PASS` for review).
