## case-readiness run — 2026-09-01

**State:** researched → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

Note: this case already carries a recorded `case.json.balance_test_waiver` under MCS-46
(`granted: true`, `approved_by: manan.atit@gmail.com`, `date: 2026-09-01`, matching the
DOCTRINE_LEDGER.md MCS-46 entry) for its real, sourced 95.8% margin. That waiver was already on
file before this session's work began; this session did not self-grant it. This session's work was
gate remediation (structural fixes) plus the standard Tier 2 probe run, not a further retune.

### Tier 1 — structural (20 checks)

Remediation this session: trimmed the Overview from 467 to 297 words (SPEC §1.2's 150-300 range)
while preserving the hook and every load-bearing beat; the trim also removed the Overview's stray
numeral ("depth 6" in a code comment), resolving the T1-02 BLOCKER. Added `(SEE APPENDIX F)` to
Background (was an orphan appendix — G was already referenced, F was not). Fixed the final Appendix
G: it listed "Tail-Call Optimization (TCO)" as a Vocabulary term with a full explanatory paragraph
inline — TCO is not itself a `readmodel/standards_spine.json` skill (this case's actual claimed
skills are Mathematical Induction, Base Case, Inductive Step, and their how-to), so no phrasing of
it can pass SPEC §1.7's "verbatim spine label" test; moved the explanation to a clearly-marked
non-vocabulary background note instead of listing it as a spine term. Added a `45-Minute Socratic
Plan` table to `FACILITATOR.md` (the anchor ladder, Twist, and deep-conflict threads were already
present and strong; the timed table was the missing MCS-16 piece). Joined the 5 Socratic questions
onto single physical lines.

| id | result | note |
|---|---|---|
| T1-01 through T1-08 | PASS | structure, boilerplate, appendices, citations all clean |
| T1-09 | GAP | margin 95.8% — MCS-46 waiver on file (already recorded, not self-granted this session), correctly downgraded from BLOCKER |
| T1-10 | GAP | new_coverage[] empty — reinforcement carve-out, `reinforcement_note` present |
| T1-11 through T1-13 | PASS | learning-goal reachability, tier load, facilitator artifacts (anchor ladder, Twist, timed plan, 5 Socratic questions, trap) all clean |
| T1-14 | GAP | 3 residual "orphan" numbers (0.0, 11.0, 2015.0) are the facilitator-only "real-world grounding" section's references to AWS TLA+/seL4 papers (e.g. "2015" as a publication year, "0" as a citation index) — not case data drift |
| T1-16 | PASS | case_md_sha256 recorded below, current |
| T1-17 through T1-20 | PASS | cohort bands (already declared), published/ built, glossary complete |

**BLOCKER (0). GAP (4, all accepted).**

`VERDICT: TIER1_PASS (0 blockers, 4 gaps)`.

### Tier 2 — simulated play (6 probes)

Mechanical pre-screen fixes this session: `case.json.balance.argument_a`/`argument_b` were rewritten
with real digits (the 0.333/0.164 ms Shallow-row TCO-honored comparison for A; the 3.94/0.164 ms
TCO-not-honored comparison, the 8.8-million-times extreme-case figure, and the real RavenDB
postmortem numbers for B) — both were previously almost entirely qualitative. Authored
`sensitivity_model.py` from scratch, reproducing the documented 95.8% margin exactly and its
disclosed 50.8% TCO-honoring counterfactual. Because the three ms/10,000-rollups figures driving
this metric are **directly measured benchmark data (S1), not stated Modeling Assumptions**,
`FLEX[]` sweeps only the one genuine stated assumption that selects which measured column applies
(MA7, the target runtime) rather than perturbing the real measured numbers themselves — perturbing
real cited data by an arbitrary percentage would itself violate SPEC §5, which is exactly why this
case carries an MCS-46 waiver instead of a retune.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Reading `case.md` alone: D1's induction proof (base case + inductive step), D2's recursion trace, D3's per-call cost interpretation, and D4's six-cell runtime table are unambiguous once Appendix D's cited figures are plugged in. The metric (ms/10,000 rollups under the actual target runtime, Go, non-TCO) is named directly in Background/Appendix A. A solver reaches B (The Guaranteed Floor) with correct, traceable arithmetic. |
| P2 both-sides | **PASS** | After the argument rewrite, both sides carry real numbers: A's case is "airtight for every depth, and the TCO-honored cost gap is only 50.8%, not extreme"; B's case is "flat per-call cost, a real 95.8% gap under the actual target runtime, and a real documented production-bug precedent (RavenDB, S3) for exactly the failure mode A's proof doesn't cover." Neither side collapses to a concession; A's correctness argument stands independently of the performance numbers. |
| P3 trap | **PASS** | The trap names two specific wrong actions: (1) treating "recursive is slower" as a flat universal fact without checking the TCO fork the whole case is built around, and (2) treating D1's proof as a guarantee about the *deployed* system rather than the function *as specified* — exactly what the Twist (a real production incident of that exact failure shape) is built to catch. Both are the single most likely real failure modes given the case's two-layer structure (a performance fork and a correctness-scope distinction). |
| P4 twist | **PASS** | The Twist (the real Ayende/RavenDB postmortem, S3) invalidates the "I wrote a correct induction proof, so the Provable Path is safe" reading without making Option B obviously correct — it demonstrates that a proof about a function's recurrence is not automatically a proof that deployed code satisfies every premise the proof assumed at every call site. It is real, externally documented precedent (not a fabricated plot device) and depends only on the case's own stated framing (a formal proof exists for the recurrence, not for the deployed system), so it survives every legitimate reading of the case's assumptions. |
| P5 sensitivity | **PASS** | `sensitivity_model.py` reproduces the base case exactly (A=3.94 ms, B=0.164 ms, 95.8% margin matching `case.json.margin_pct`) and its own disclosed TCO-honoring counterfactual (50.8%, matching `case.json.balance.margin_note`). The one genuine stated Modeling Assumption in scope (MA7, target runtime) never flips the winner — B wins under both real measured columns S1 reports, confirming case.json's own finding that the lopsidedness is structural to the real cited benchmarks, not an artifact of the runtime choice. |
| P6 data decay | **PASS (partial, live fetch)** | This session has outbound network. Spot-checked the case's two most load-bearing/sensitive sources: **S4** (the golang/go GitHub issue on tail-call optimization) — live, confirmed verbatim: "The current Go language does not support tail calls, because they affect runtime.Callers and stack backtraces and the like." **S3** (the Ayende/RavenDB production postmortem, the basis for the Twist) — live, confirmed verbatim: "we have one result with –67,343 and another with +67,329," matching the case's cited figures exactly. No BLOCKER found on either source checked. The remaining 6 URLs (S1, S2, S5, S6) were not re-fetched this session; RESEARCH_LOG.md/case.json record they were fetched and confirmed at research time (2026-09-01, same day). |

`MECHANICAL RESULT: 0 probes FAILED mechanically.` All six verdicts recorded by name.

### Tier 3 — human dry-run

NOT RUN. No `cases/prove-it-scales/runs/RUN_*.md` filed. Required before this case may be marked
✅/VERIFIED in `DOCTRINE_LEDGER.md`; not required for `PUBLISHED`.

### Next step

`case-publish` may run (`case.json.qa.state == "TIER2_PASS"`, all six probes recorded, 0 FAIL,
MCS-46 waiver on file for the one open GAP that would otherwise be a BLOCKER).

---

## case-readiness run — 2026-09-01 (independent re-gate)

**State:** TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

Independent re-run of the full gate (mechanical checks + a genuine blind P1/P2/P3 cold-solve, not
a continuation of the prior session's work). Confirms the prior run's verdict and closes the prior
run's P6 gap (only S3/S4 were live-fetched before; all 6 unique cited URLs are checked here).

### Tier 1 — structural (20 checks)

Re-ran `preflight_lint.py` (clean) and `tier1_structural.py` (20/20 checks executed).

| id | result | note |
|---|---|---|
| T1-01–T1-08, T1-11–T1-13, T1-16–T1-20 | PASS | structure, boilerplate, appendices, sourcing, learning-goal reachability, facilitator artifacts, hash currency, cohort bands, HTML, glossary all clean |
| T1-08 | GAP | LOW-confidence sources present (S8) — confirmed by P6 below: derived/interpolated, not load-bearing on the margin, correctly flagged not blocked |
| T1-09 | **GAP, correctly downgraded** | margin is 95.8% (SPEC §2 cap ~20%) — **MCS-46 `balance_test_waiver` on file and complete** (ledger_ref, approved_by=manan.atit@gmail.com, date=2026-09-01, full rationale). `tier1_structural.py`'s T1-09 logic correctly reads the waiver and downgrades this specific finding from BLOCKER to GAP; it does not suppress T1-09 generally, and no other case gets this treatment. Confirmed working as designed. |
| T1-10 | GAP | `new_coverage[]` empty — reinforcement carve-out applies (`reinforcement_note` present, adjacent skills honestly checked and ruled out) |
| T1-14 | GAP | 2 residual numbers in FACILITATOR.md (11.0, 2015.0) not in case.md/case.json — these are the "real-world grounding" section's citation of AWS TLA+/seL4 (Klein et al., 2015) background reading, not case data; correctly not conflated with the balance/derived figures |
| T1-15 | GAP | 3 residual numbers in the published `.docx` (7.3, 15.0, 2015.0) — same grounding-section citation plus one more; published artifact is otherwise current (built after last case.md/FACILITATOR.md edit) |

**BLOCKER (0). GAP (5, all reviewed and accepted — none is a fresh finding requiring case-write.)**

`VERDICT: TIER1_PASS (0 blockers, 5 gaps)` — confirmed via `--json` output
(`/tmp/t1-prove-it-scales.json`), Tier 2 may proceed.

### Tier 2 — simulated play (6 probes)

**P1 cold solve — blind, self-performed.** Read ONLY the packet (`/tmp/coldsolve-prove-it-scales/PACKET.md`,
case.md + appendices) and committed answers in writing before opening FACILITATOR.md or case.json.
Blind result: chose **Option B**; correctly named the metric (ms/10,000 rollups under the actual
stated target runtime, Go/non-TCO, against the 500ms SLA); arithmetic reproduced the real Shallow/
Medium/Deep gaps (≈24x / ≈13,500x / ≈8.8M x) from Appendix D's own cited figures; produced a
correct induction-proof structure (base case = leaf account; inductive step = parent total = own
usage + sum of already-correct child totals, by the induction hypothesis; closing argument by
well-founded induction on finite depth) matching what D1 asks for; named MA7 (target runtime) as
the most sensitive assumption unprompted. **PASS** — reached B for the right reasons, with correct
arithmetic, and named the metric.

**P2 both-sides — self-performed.** Built independently: A's strongest sentence rests on D1's
depth-independent correctness guarantee plus Appendix E's real, quantified precedent
(–67,343/+67,329) for what "no proof" can cost; B's strongest sentence rests on the real, directly-
measured Shallow-row gap (95.8%, S1) and the fact its cost never depends on a runtime detail Devon
doesn't control. Neither collapses to a concession — A's case is not merely "slower but safer," it
is substantively grounded in real cited numbers of its own (Appendix E's figures, the 50.8%
TCO-honored counterfactual). Matches FACILITATOR.md's own framing that the real tension is
qualitative (is the guarantee worth the cost) not a numeric contest. **PASS.**

**P3 trap check — blind, self-performed, before reading FACILITATOR.md.** Named, unprompted: (1) a
solver treating "recursion is slower" as a flat fact without registering that Appendix B's TCO fact
is the actual analytical fork, and (2) conflating the induction proof's correctness-of-the-recurrence
with an implicit guarantee about runtime/deployment behavior. FACILITATOR.md's stated trap names
both of these exactly, including the second (correctness-vs-deployment) one the SKILL.md flagged as
the likely miss. **PASS** — blind trap matches the named trap on both counts.

**P4 twist integrity.** (1) The twist (real Ayende/RavenDB postmortem) invalidates the "a written
proof means the Provable Path is safe" position a real room would hold. (2) It survives every
natural reading of the case's stated assumptions — it does not touch D4's numbers or claim to, only
the separate claim that a correctness proof about the recurrence is not automatically a proof the
deployed call sites satisfy every premise; no unstated convention is required for it to land.
**PASS**, with one finding for `case-write`/`case-research` to reconcile, not a P4 fail: **FACILITATOR.md
is internally inconsistent about the twist's timing** — the Twist section header says "drop this at
~15 minutes into the discussion" (line 107) but the 45-Minute Socratic Plan table fixes it at
"25:00" (line 134). Minor, does not affect twist validity, but a guide following the header literally
and a guide following the table will drop it at different points in the same room.

**P5 assumption sensitivity — machine, re-run.** `tier2_probes.py --probe 5 --flex 0.5`: base
{A: -3.94, B: -0.16}, winner B, margin -95.8%. ±50% flex on the one declared dial (`tco_not_honored`)
does not flip the winner and does not change `breaks_20pct_cap` in either direction (already
over cap at base, per the MCS-46 waiver, not a fresh P5 finding). **PASS.**

**P6 data decay — full live fetch, all 6 unique cited URLs (this session, not partial).**

| src | URL | reachable | cited value present | note |
|---|---|---|---|---|
| S1/S8 | medium.com/@felipedutratine/... | yes | yes — 16.4 / 33.3 / 394 ns/op confirmed verbatim | dated Jan 24 2017 on page vs. 2017-01-25 cited (1-day rounding, immaterial) |
| S2/S7 | github.com/pope/go_recursive_benchmark | yes | yes — 312238250 ns/op and 35.36 ns/op confirmed verbatim | — |
| S3 | ayende.com/blog/197637-A/... | yes | yes — "–67,343" / "+67,329" confirmed verbatim | — |
| S4 | github.com/golang/go/issues/22624 | yes | yes — Ian Lance Taylor's quote confirmed verbatim | **drifted metadata**: case.json/case.md's Appendix F records this issue's date as "Ongoing (issue open)"; the issue is now **Closed**. The load-bearing quote is unchanged and still accurately represents Go's position, so this is not a BLOCKER, but the "issue open" status field is stale and should be corrected to reflect the closed state next time case.json is touched. |
| S5 | aws.amazon.com/organizations/faqs/ | yes | yes — "five levels deep" confirmed verbatim | — |
| S6 | confluent.io/customers/metronome/ | yes | yes — "billions of events per day" and "tens of thousands of invoices... per second" confirmed verbatim | — |

No dead links, no silently-drifted load-bearing figures. **PASS**, with one non-blocking metadata
staleness finding (S4 status field) named above for the next author touch.

`MECHANICAL RESULT: 0 probes FAILED.` All six verdicts recorded by name: P1 PASS, P2 PASS, P3 PASS,
P4 PASS, P5 PASS, P6 PASS.

### Tier 3 — human dry-run

NOT RUN. No `cases/prove-it-scales/runs/RUN_*.md` filed. Required before ✅/VERIFIED, not required
for `PUBLISHED`.

### Next step

`case-publish` may run. Two non-blocking items for a future case-write/case-research touch (not
required before publish): (1) correct Appendix F's S4 status field from "Ongoing (issue open)" to
reflect the issue is now Closed; (2) reconcile FACILITATOR.md's twist-timing mismatch (header says
~15 min, timed-plan table says 25:00) to a single number.
