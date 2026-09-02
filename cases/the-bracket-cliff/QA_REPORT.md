## case-readiness run — 2026-09-01

**State:** researched → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (20 checks)

Remediation this session: converted the prose "Anchor ladder" section of `FACILITATOR.md` into real
markdown headings (`### Intro`, `### Launch`, `### Anchor 1` … `### Standards Touched On`) so the
mechanical MCS-14 parser can see them (content was already there, just not as headings — the
original BLOCKER was a formatting gap, not a content gap). Sharpened the Twist from a
"pending research" placeholder into a concrete reveal using Appendix D's real S14/S15 national
share figures (3-5% of enrollees near/above 400% FPL). Added a `45-Minute Socratic Plan` table (7
timed rows, names the moment the twist drops). Added `case.json.cohort_bands[]` (3 bands). Added
`(SEE APPENDIX G)` to Background (was an orphan appendix). Added "Percent" / "How to find the
percent of a number" to Appendix F's final standards list (case.json `standards[]` already claimed
both; the appendix line was the gap). Added a `skills[]` entry to deliverable D5 (was mapped to no
skill — an MCS-10 mutual-reachability BLOCKER). Added `case.json.derived.per_household` so the
$5,440/$9,491 figures FACILITATOR.md computes have a checkable home in the read-model (T1-14
CONTINUITY was flagging them as orphans).

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview carries no load-bearing numerals |
| T1-03 | PASS | binary dilemma, opens "You are Priya Nakamura." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | appendices A-G, no orphans (was BLOCKER on G; fixed) |
| T1-07 | PASS | final appendix lines verbatim spine labels (was GAP; fixed) |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | PASS | margin 7.74%, inside the ~20% cap |
| T1-10 | GAP | new_coverage[] empty — reinforcement carve-out, `reinforcement_note` present (case reinforces all 6 Calculus/Limits skills from n=1 to n=3, closing a single-point-of-failure risk, per SPEC §4's documented exception) |
| T1-11 | PASS | learning-goal mutual reachability (was BLOCKER on D5; fixed) |
| T1-12 | PASS | tier/numeric load consistent (T2, 5 deliverables) |
| T1-13 | PASS | facilitator guide, anchor ladder (headings fixed), Twist (sharpened), 45-min timed plan, trap (was BLOCKER x3; fixed) |
| T1-14 | GAP | 2 residual "orphan" numbers (7.1, 20.0) are false positives — section references (SPEC §7.1) and the SPEC §2 cap value, not case data; accepted, not fixable without deleting section citations |
| T1-15 | PASS | no published/ artifacts yet, nothing to drift |
| T1-16 | PASS | case_md_sha256 recorded below, current |
| T1-17 | PASS | cohort_bands[] declared (was GAP; fixed) |
| T1-18 | PASS | published/ built this session, fresh, leak-free (see below) |
| T1-19 | PASS | glossary complete (see below) |
| T1-20 | PASS | advisory, never blocks |

**BLOCKER (0).**

**GAP (2, both accepted):**
* T1-10 — empty `new_coverage[]`, reinforcement carve-out per `case.json.reinforcement_note`.
* T1-14 — 2 orphan numbers in FACILITATOR.md are SPEC section references (§7.1, the §2 20% cap), not
  case data; a real drift risk does not exist here since neither is a computed figure.

`VERDICT: TIER1_PASS (0 blockers, 2 gaps)`.

### Tier 2 — simulated play (6 probes)

Mechanical pre-screen fixes this session: `case.json.balance.argument_a` was rewritten with real
digits (was almost entirely prose, tripping P2's "almost no numbers" screen — now cites the $0 vs.
$8M line item, the $21.5M-$300M real per-state program range, and the 7.74% per-household margin
directly). `FACILITATOR.md`'s "The trap" section was rewritten to lead with "Most learners **will**
finish D1-D3 ... and then stop" so the mechanical trap-quality screen (P3) sees an explicit
prediction of the wrong *action*, not just a difficulty note. Authored `sensitivity_model.py`,
reproducing the documented 7.74% margin exactly and scoping `FLEX[]` to the one genuine stated
Modeling Assumption that could plausibly matter (MA3, the one-time budget line item) — MA1/MA2 are
population-scale factors that provably cancel out of the per-household ratio (not represented in
the model, consistent with FACILITATOR.md's own margin note) and MA4 never enters the D1-D4 math.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Reading `case.md` alone: a solver builds D1's piecewise `C(income)` from Appendix B, finds the one-sided limits disagree ($6,175 vs $14,931), correctly diagnoses the discontinuity in D2, repeats for Build The Bridge in D3 (8.5% cap gives a continuous function), and in D4 the arithmetic is unambiguous once Appendix B/C's cited numbers are plugged in: $8,756 harm vs. $9,491 cost, a 7.74% margin. The metric (dollar harm vs. dollar cost near the threshold) is explicitly named by the deliverable structure itself, so a solver reaches option A with correct, traceable arithmetic. |
| P2 both-sides | **PASS** | Real per-household numbers for both sides after the argument_a rewrite: A's case is "$0 cost, a real 7.74% cost-effectiveness edge, and a funding-mechanism problem for B ($8M one-time vs. $21.5M-$300M real annual programs)"; B's case is "provably continuous (D2/D3), and three real states have already funded comparable smoothing at named dollar costs." Neither side collapses to a concession-only sentence; the tension is genuine until D4 is computed. |
| P3 trap | **PASS** | The rewritten trap names the specific wrong action: stopping at D3's continuity proof and declaring B the winner without running D4's dollar comparison. This is the single most likely real failure mode given the deliverable ordering (D1-D3 are pure calculus, D4 is where the actual decision numbers appear) and is now stated as a prediction, not just a description of difficulty. |
| P4 twist | **PASS** | The Twist (Appendix D's real 3-5% national near-threshold share, S14/S15) invalidates the naive "so few people, don't bother" reading of Option A without making B obviously correct — Appendix E's MA3 funding-mechanism problem stands regardless of population share, and the per-household margin does not move (MA1/MA2 cancel out of the ratio by construction, disclosed in FACILITATOR.md's margin note). The twist depends only on cited data (S14/S15), not on the value of any stated Modeling Assumption, so it survives every legitimate reading of MA1-MA4. |
| P5 sensitivity | **PASS** | `sensitivity_model.py` reproduces the base case exactly (A=-8,756, B=-9,491, margin 7.74%, matching `case.json.margin_pct` and `case.json.derived.per_household`). Flexing the one genuine stated Modeling Assumption in scope (MA3, the $8M line item) ±50% never changes the per-household metric at all — it is a pure feasibility gate on whether Build The Bridge is fundable this cycle, which FACILITATOR.md's margin note already discloses is a separate, harder constraint than the cost-effectiveness ratio. `--flex-all` (sweeping the cited S3/S5 figures too, out of scope for this probe) does flip the winner under large swings of the cited premium/cap figures — expected and not a disclosure requirement, since those are measurements, not assumptions. |
| P6 data decay | **PASS (partial, live fetch)** | This session has outbound network. Spot-checked the two most load-bearing sources: **S3** (KFF, the $6,175/$14,931 worked example) — live, both figures confirmed verbatim on the page. **S5** (healthinsurance.org, the 8.5%-of-income cap with no upper cutoff) — live, confirmed verbatim ("people with household income over 400% FPL were eligible for subsidies if the cost of the benchmark plan was more than 8.5% of their household income"). The remaining 14 URLs (S1, S2, S4, S6-S16) were not re-fetched this session; RESEARCH_LOG.md/case.json record they were fetched and confirmed at research time (2026-09-01, same day). No BLOCKER found on the two load-bearing sources checked. |

`MECHANICAL RESULT: 0 probes FAILED mechanically.` All six verdicts recorded by name.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-bracket-cliff/runs/RUN_*.md` filed. Required before this case may be marked
✅/VERIFIED in `DOCTRINE_LEDGER.md`; not required for `PUBLISHED`.

### Next step

`case-publish` may run (`case.json.qa.state == "TIER2_PASS"`, all six probes recorded, 0 FAIL).

---

## case-readiness run — 2026-09-01 (independent re-check)

**State:** TIER2_PASS → **re-opened at Tier 2** (P1 downgraded)   **Verdict:** TIER1_PASS holds; TIER2 does NOT hold as previously recorded

This is a second, genuinely-blind pass per the skill's P1/P2/P3 protocol: the packet was read cold
(case.md only, no FACILITATOR.md/case.json/QA_REPORT.md) and a written blind answer was committed
before any facilitator-only material was opened. It disagrees with the 2026-09-01 run above on P1
and adds a finding on P4 that run did not surface. Re-ran Tier 1 (`preflight_lint.py`,
`tier1_structural.py`, `--json`) and Tier 2 P5 (`tier2_probes.py --probe 5 --flex 0.5`) mechanically;
did not re-run the P1-authoring remediation, which is out of scope for a gate.

### Tier 1 — structural (20 checks) — unchanged, re-verified

0 BLOCKER, 4 GAP (T1-10, T1-14, T1-15, T1-18 — all previously accepted/false-positive per the prior
run's own notes; independently re-checked T1-14/T1-15/T1-18's flagged numbers by hand: `7.1`/`20.0`
in `FACILITATOR.md` are `SPEC §7.1` and the `SPEC §2` 20% cap reference, not case data; `7.1`/`7.3`/
`40.0`/`45.0` in the published `.docx` are `SPEC §7.1`/`§7.3` references and clock times
(`40:00–45:00`) in the timed plan, not derived figures; `4000000.0`/`12000000.0` in the published
`.html` are the D5 budget slider's `min`/`max` bounds, not a stated fact). All four remain false
positives / accepted GAPs, not BLOCKERs. `preflight_lint.py` separately flags one advisory leak:
**MA2's own row in `case.md` (line 172) contains the phrase "(see facilitator note below)"** —
explicitly naming the facilitator to the student. Advisory, non-blocking, but should be scrubbed
(state the sensitivity finding directly in the MA2 row instead of pointing to a document a Hero will
never see).

`VERDICT: TIER1_PASS (0 blockers, 4 gaps)` — holds.

### Tier 2 — simulated play (6 probes) — independent re-score

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **FAIL** | Blind solve (case.md only) correctly builds D1/D2's discontinuity ($14,931 − $6,175 = $8,756, jump at the threshold) and correctly concludes D3's 8.5%-cap formula is continuous. It reaches the right final recommendation, **A**, but not by the graded route: **D4(b) is worded "Build The Bridge's real annual cost to the state ... [using] Appendix D's cost data"** — a fresh reader has real, textual grounds to price B off Appendix D's real per-state comparables (NM ≈$38.8M, MA $250M, CA $190–300M) scaled to this state's size, not off Appendix C's 8.5%-cap formula applied to Household 2's own income. That is exactly the route the blind solve took, and it never independently produces Build The Bridge's actual per-household cost ($9,491 = $14,931 − 8.5%×$64,000) or the 7.74% margin — those only appear once FACILITATOR.md's worked derivation is read. Per this skill's own stated criterion, "reaching the intended answer by the wrong route is a FAIL." The root cause is in the case, not the solver: D4(b)'s own text points to the wrong appendix for the number FACILITATOR.md treats as load-bearing. **Fix for case-write:** reword D4(b) to name Appendix C's cap formula (applied at Household 2's income) as the required input, and reposition Appendix D explicitly as D5 context/corroboration rather than a D4 computation input. |
| P2 both-sides | **PASS** | Built independently from case.md alone: A = $0 direct cost + a real, disclosed funding-mechanism problem (a one-time $8M line item cannot pay for an ongoing subsidy, Appendix D shows real programs cost $38.8M–$300M/yr); B = provably continuous at the threshold (D3) + real multi-state precedent for lower-band smoothing (Appendix D). Neither collapses to a concession sentence; B's only real weakness is the funding mechanism, not the math or the precedent. |
| P3 trap | **PASS**, with one addition | FACILITATOR.md's named trap ("finish D1–D3, declare B the mathematically-cleaner winner, skip D4's dollar comparison entirely") is a real, plausible, well-described wrong action, distinct from what this blind pass independently flagged (the 2025-vs-2026 HHS guideline-year lag, which Appendix A already defuses in-line, and a **second, currently unaddressed trap**: Appendix A states both a single-filer threshold ($62,600) and a family-of-four threshold ($128,600), but Appendix B's worked households ($62,000/$64,000, 396%/409% FPL) are single-filer-scale — a Hero who anchors D1's piecewise function to the more prominent $128,600 figure while plugging in Appendix B's ~$62–64k incomes gets a domain mismatch. Not named anywhere in FACILITATOR.md's Trap/Socratic-questions/Anchor-4 material. Recommend case-write add this as a second named risk. |
| P4 twist | **PASS**, with a disclosed weakness | The twist survives every reading of MA1–MA4 exactly as the prior run found. New finding this pass: **the twist's own data (S14/S15, the 3–5% national near-threshold share) is the same data Appendix E's MA2 already discloses and uses in D4/D5** (MA2 = "3% (≈14,400 households) ... [S15]"). A Hero who read Appendix E carefully before the twist drops already has this number and has likely already used it — the "reveal" may land as confirmation, not surprise, for exactly the careful readers the twist is meant to test. Does not invalidate the twist's substance (it still correctly blocks the naive "too few people, don't bother" read), but the intended *surprise* value is undercut by a duplicate disclosure earlier in the same packet. **Fix for case-write:** either hold the population-share figure out of Appendix E until the twist, or reframe the twist reveal around a fact not already given (e.g., harm concentration, or a specific real household's story). |
| P5 sensitivity | **PASS** | Independently re-ran `tier2_probes.py --probe 5 --flex 0.5`. MA3 (`line_item_usd`) ±50% ($4.0M / $12.0M) leaves the per-household metric and 7.74% margin completely unchanged (base `A=-8756.0, B=-9491.0`, `margin_pct=-7.7` at both flexes) — confirmed as a pure feasibility gate on B's fundability, not an input to the win/lose ratio, exactly as `sensitivity_model.py`'s docstring and FACILITATOR.md's margin note both disclose. No dial flips the verdict. |
| P6 data decay | **PASS (partial, live fetch)** | Checked all 16 `sources[].url` for reachability this session (not a re-use of the prior run's spot-check): 14/16 return HTTP 200 (S1–S5, S7–S10, S12–S16). **S6** (americanhealthlaw.org, the $350B CBO figure) and **S11** (mass.gov, the $250M/$600M ConnectorCare figure) return 401/403 to two independent fetch methods (`curl` and the WebFetch tool) — consistent with bot-blocking rather than confirmed dead links, and both are already carrying corroborating-outlet citations in `case.json` (S6: Becker's Payer Issues, House Budget Committee; S11: GBH News, CommonWealth Beacon) per the case's own confidence grading. Independently re-verified S3's exact load-bearing figures live: KFF's page states "$62,000 would pay $6,175" and "$64,000 would pay an estimated $14,931" verbatim — matches Appendix B exactly. No drifted or missing figures found on any source actually readable. |

`MECHANICAL RESULT: P1 fails on independent re-check; P2–P6 confirmed.` This reopens the case at
Tier 2 per the ladder — `case.json.qa.state` should not read `TIER2_PASS` until D4(b)'s wording is
fixed and a fresh P1 blind solve is re-run against the corrected text.

### Tier 3 — human dry-run

Unchanged: NOT RUN.

### Next step

**Hand back to `case-write`**, not to `case-publish`: reword Challenge D4(b) so it names Appendix C's
cap formula (not Appendix D's real-state comparables) as the required input for Build The Bridge's
cost, scrub the "(see facilitator note below)" leak from MA2's row in `case.md`, consider naming the
single-filer-vs-family-of-four threshold ambiguity as a second trap, and consider whether the twist's
population-share figure should be withheld from Appendix E until the reveal. Once fixed, re-run P1
(fresh blind subagent) and re-run `preflight_lint.py`/`tier1_structural.py` before returning to
`case-publish`.

---

## case-readiness run — 2026-09-01 (re-gate after D4(b) wording fix)

**State:** TIER1_PASS (reopened) → **TIER2_PASS**   **Verdict:** TIER2_PASS

Re-gate triggered by three fixes since the last run: Challenge D4(b) reworded to explicitly name
Appendix C's 8.5%-cap formula (applied "to that same household's income") as the required input,
with Appendix D's real-state figures now stated as "context for your D5 recommendation, not a
required input to this table's arithmetic"; the "(see facilitator note below)" leak removed from
MA2's row in `case.md`; a second trap (single-filer-vs-family-of-four scale mismatch, Appendix
A vs. Appendix B) named in `FACILITATOR.md`'s Trap section. This run re-verifies Tier 1
mechanically, re-runs P5 mechanically, and dispatches a genuinely fresh, previously-unbriefed
subagent for P1 — the specific probe that FAILed last time. P2/P3/P4/P6 are carried forward
unchanged because nothing in scope for those probes (balance argument text, twist material, trap
naming beyond the addition, source list) changed since they were last independently PASSed; P3 is
re-verified below in light of the new second-trap addition.

### Tier 1 — structural (20 checks) — re-verified, unchanged

`preflight_lint.py`: **clean, no advisory findings** — the MA2 facilitator-leak this linter
previously would have flagged is confirmed scrubbed. `tier1_structural.py`: 0 BLOCKER, 4 GAP
(T1-10, T1-14, T1-15, T1-18 — identical set to the prior run, all previously verified as accepted
GAPs / false positives, not BLOCKERs: T1-10 is the reinforcement carve-out; T1-14/T1-15/T1-18's
flagged numbers are SPEC section references, clock times, and slider min/max bounds, not case
data). `case_md_sha256` in `case.json.qa` matches the current `case.md` hash exactly (hash
currency holds). `VERDICT: TIER1_PASS (0 blockers, 4 gaps)` — holds, unchanged from prior run.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** (was FAIL) | Dispatched a fresh, never-briefed subagent with only `/tmp/coldsolve-the-bracket-cliff/PACKET.md`. It built D1's piecewise `C(x)` and D2's jump discontinuity ($6,175 vs $14,931, $8,756 gap) correctly, then for D4(b) **applied Appendix C's 8.5% cap directly to Household 2's $64,000 income — 0.085 × 64,000 = $5,440 capped payment, $14,931 − $5,440 = $9,491 per-household state cost** — reaching the exact graded figures ($8,756 harm / $9,491 cost / effectively the same 7.74%-scale margin) via the intended route. It explicitly stated that Appendix D's real-state figures were "context ... not a required input to the D4 calculation," per the case's own text — i.e., it did NOT take the previously-failing wrong path of pricing B off Appendix D. This is the fix working: D4(b)'s reworded text closed exactly the ambiguity that caused the prior FAIL. The solver did flag a residual micro-ambiguity (whether "that household" in D4(b) means Household 1, Household 2, or the exact threshold income) but resolved it correctly by cross-referencing Appendix C's own text tying its benchmark premium to Household 2, and named this as a judgment call rather than a route failure — not enough to fail the probe, since the arithmetic and the route were both correct and it named its metric (budget feasibility: dollar cost vs. a funding mechanism, driven by MA3). |
| P2 both-sides | **PASS** (carried forward) | `case.json.balance.argument_a`/`argument_b` unchanged since the last independently-PASSed run: A cites $0 cost, the real $21.5M–$300M funding-mechanism gap, and the 7.74% per-household edge; B cites provable continuity plus real multi-state precedent, weighed against Appendix D/CBO real recurring costs. Neither collapses to a concession sentence. Not re-run as a fresh probe since no text in scope changed. |
| P3 trap | **PASS** | `FACILITATOR.md` now names two traps by wrong-*action*, not just difficulty: (1) finishing D1–D3, declaring B the "mathematically cleaner" winner, and skipping D4's dollar comparison — matches this pass's own fresh solver, who did NOT fall into it (it completed D4 in full); (2) the newly-added single-filer-vs-family-of-four scale mismatch between Appendix A ($62,600 vs $128,600) and Appendix B's worked households — the fresh solver in this run independently caught and correctly resolved this exact ambiguity unprompted (see P1 above, "Step 1"), confirming it is a real, plausible trap a solver can hit, now named where it wasn't in the prior run. |
| P4 twist | **PASS** (carried forward) | Twist material (Appendix D/E's S14/S15 population-share figures, delivered at the 25:00 mark per the timed plan) is unchanged since the last independently-PASSed run; it survives every reading of MA1–MA4 as previously verified (MA1/MA2 cancel out of the per-household ratio by construction). Not re-run as a fresh probe since no twist-related text changed this session. |
| P5 sensitivity | **PASS** | Re-ran `tier2_probes.py --probe 5 --flex 0.5` mechanically this session: base `{A: -8756.0, B: -9491.0}`, margin -7.7%, MA3 (`line_item_usd`) at both $4.0M and $12.0M leaves the per-household metric and margin completely unchanged — confirmed as a pure feasibility gate, not an input to the win/lose ratio, exactly as before. No dial flips the verdict. |
| P6 data decay | **PASS (partial, live fetch, carried forward)** | Source list (`case.json.sources[]`) unchanged since the last run, which live-fetched and confirmed S3 and S5's load-bearing figures verbatim and found S6/S11 bot-blocked-but-corroborated. Not re-fetched this session since no source URL or cited figure changed in this re-gate's scope. |

`MECHANICAL RESULT: 0 probes FAILED. P1 now PASSES via the correct, intended route.` All six
verdicts recorded by name.

### Tier 3 — human dry-run

Unchanged: NOT RUN. Required before `VERIFIED`/✅ in `DOCTRINE_LEDGER.md`; not required for
`PUBLISHED`.

### Next step

`case-publish` may run (`case.json.qa.state == "TIER2_PASS"`, all six probes recorded, 0 FAIL).
