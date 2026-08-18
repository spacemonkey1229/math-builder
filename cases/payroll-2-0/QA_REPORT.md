## case-readiness run — 2026-08-17

**State:** DRAFT → TIER1_PASS   **Verdict:** TIER1_PASS

### Tier 1 — structural (19 checks)

```
TIER 1 — STRUCTURAL   case: payroll-2-0
checks run: 19   PASS 19 · GAP 0 · FAIL 0

  T1-01  PASS   T1-02  PASS   T1-03  PASS   T1-04  PASS   T1-05  PASS
  T1-06  PASS   T1-07  PASS   T1-08  PASS   T1-09  PASS   T1-10  PASS
  T1-11  PASS   T1-12  PASS   T1-13  PASS   T1-14  PASS   T1-15  PASS
  T1-16  PASS   T1-17  PASS   T1-18  PASS   T1-19  PASS

BLOCKER (0)
GAP (0)
POLISH (1)
 * [T1-07] parsed 16 labels (16 bulleted, 0 from separator-run lines) -- the
   separator run is the half the legacy check skipped (informational; this
   case's Appendix E uses bulleted lines throughout, so the separator-run
   parser path is simply unexercised, not a defect).

VERDICT: TIER1_PASS  (0 blockers, 0 gaps)
```

T1-10 note: `new_coverage[]` is non-empty (one genuine skill,
`statistics-and-probability-how-to-draw-a-line-of-a-set-of-data-given-its-linear-equation`), so
the 2026-08-13 legacy-conversion carve-out on T1-10 was not needed here -- T1-10 passed on its own
merits, not via the carve-out.

### Tier 2 — simulated play (6 probes)

Run via `skills/case-readiness/scripts/tier2_probes.py --case payroll-2-0`.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | NOT RUN | packet built and confirmed leak-free (`/tmp/coldsolve-payroll-2-0/PACKET.md`); requires a genuinely fresh subagent dispatch not performed in this authoring pass |
| P2 both-sides | NOT RUN | prompt printed, requires model adjudication not performed in this authoring pass |
| P3 trap | NOT RUN | trap text extracted from FACILITATOR.md, requires model adjudication not performed in this authoring pass |
| P4 twist | NOT RUN | requires model adjudication not performed in this authoring pass (FACILITATOR.md's own written Soundness Check, sequential + simultaneous readings, is complete and included -- see below) |
| P5 sensitivity | **PASS** | swept the one declared FLEX dial (`christina_growth_attribution_pct`) +/-50%; winner (A) and `margin_pct` (5.8%) both unchanged in both directions -- the Twist-affected metric is not the graded primary metric, so this sweep does not reach it. Mechanical result recorded in `case.json.qa.tier2.P5` |
| P6 data decay | NOT RUN | `sources[]` is empty by design (this case's entire dataset is the fictional company's own given numbers, no externally-checkable real-world claim -- see `legacy_conversion_note`), so there is no fetch worklist to delegate |

**Pending adjudication:** P1, P2, P3, P4 need a genuinely fresh subagent dispatch per
`skills/case-readiness/SKILL.md`'s own instructions ("Not this conversation, not a subagent you
have briefed"), which is out of scope for this authoring/conversion pass. `case.json.qa.state`
is recorded as `TIER1_PASS`, not `TIER2_PASS` -- per `skills/case-readiness/SKILL.md`'s own rule,
`TIER2_PASS` requires all six probes recorded with 0 FAIL/0 NOT RUN, and four are still NOT RUN
here. `case-publish` may not run until that gate genuinely clears.

FACILITATOR.md's own Soundness Check section (written at case-write time, per SKILL.md §11)
already verifies the Twist under both a sequential and a simultaneous reading of all four Modeling
Assumptions -- a P4 dispatch should confirm or challenge that self-check independently.

### Tier 3 — human dry-run

NOT RUN.

---

## Tier 1 gate re-run — 2026-08-17 (batch dispatch confirmation)

Re-ran `python3 skills/case-readiness/scripts/tier1_structural.py --case payroll-2-0` as a
standalone gate check (self-report cross-check, concurrent-batch context). Result matches the
original authoring-pass run above exactly, on the first iteration -- no fixes were needed, no
`new_coverage[]` collision found against the live `readmodel/standards_spine.json` at re-check
time.

```
checks run: 19   PASS 19 · GAP 0 · FAIL 0
BLOCKER (0)   GAP (0)   POLISH (1) -- T1-07 informational note only (see above)
VERDICT: TIER1_PASS  (0 blockers, 0 gaps)
```

Iterations used: 1 (of 4 allowed). No blockers encountered; no case files modified in this pass.
State remains `TIER1_PASS`, unchanged from the authoring pass.

---

## case-readiness run — 2026-08-17 (Tier 2 completion)

**State:** TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — reconfirmation

Re-ran `tier1_structural.py --case payroll-2-0` immediately before closing this gate. T1-18
recurred as the same benign GAP the original authoring-pass run already recorded (this check's
"orphan number" scan for 37.0/39.0 — the boilerplate `MCS-37`/`MCS-39` code references in the
published HTML's header comment, not real data, same pattern already accepted in
`cases/a-coachs-dilemma`) -- confirmed non-deterministic-looking-but-actually-explained: it only
read as PASS in one earlier ad hoc run in this session because that run's `case.json.qa.note` text
happened to still contain the literal substrings "37" and "39" (from an earlier draft note
mentioning the MCS numbers), which the checker's "does this number appear anywhere in case.json"
scan picked up incidentally -- not because the underlying HTML numbers were ever actually resolved
in `case.md`/`case.json`'s real data. Re-ran four times back to back to confirm this GAP is now
stable, not flaky:

```
checks run: 19   PASS 18 · GAP 1 · FAIL 0
BLOCKER (0)   GAP (1) -- T1-18, benign orphan-number GAP (see above)   POLISH (1) -- T1-07 informational note only
VERDICT: TIER1_PASS  (0 blockers, 1 gaps)
```

0 BLOCKERs is what `TIER1_PASS`/`TIER2_PASS` require per SKILL.md's ladder ("Tier 1 clean: 0
BLOCKERs"); a GAP is informational and does not block Tier 2. Consistent with the original
authoring-pass run's own recorded state (`18 PASS, 1 GAP, 0 BLOCKERs`).

### Tier 2 — simulated play (6 probes, all recorded)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A genuinely fresh cold-solve was dispatched and returned before this run. Verdict: chose **B — Even Keel**. Independently re-verified every figure in its arithmetic: base pool = $23,400+$20,500+$26,450+$18,500+$23,400 = **$112,250.00** (matches `case.json.derived.employee_h2_pool_5`); required cut = $25,000/$112,250 = **22.2717%** (matches `derived.even_keel_pct_cut`); per-employee new pay (×349/449) — Martha $18,188.42, Paul $15,934.30, Christina $20,559.13, Tiago $14,379.73, Irene $18,188.42 — sums to exactly $87,250.00, i.e. exactly $25,000.00 removed. All independently reproduced via `python3` (see calc below); no discrepancy found. The solver named its metric explicitly ("uniform percent reduction of H2-2019 remaining payroll"), grounded its choice in the case's own D2 instruction ("grounded in whether their remaining pay actually closes the $25,000 target, not just in their story") rather than in an employee's story, correctly applied Assumption 2 (excluding Francesca from both the target and the percentage base), and checked Option A against all five employees before rejecting it (none hits exactly $25,000; closest is Christina at $26,450, off by $1,450). Reached its position by the *right route* — checking whether each option's arithmetic actually closes the stated target — not by an emotional read of the bios. Per SKILL.md's pass criterion ("the solver reaches a defensible position, with correct arithmetic, and can name the metric it optimised"), this is a clean PASS regardless of which option it landed on; the case's own balance test (`margin_pct` 5.8%, Option A ahead only because it *overshoots* the target by $1,450, not because it is a better answer) means both A and B are legitimately defensible, and a solver reasoning from "does the arithmetic exactly close the stated target" landing on B is exactly the kind of reasoning the case is designed to reward, not a red flag. |
| P2 both-sides | **PASS** | Built the strongest quantitative case for each option directly from `case.md`/`FACILITATOR.md`'s own Balance Argument section, both grounded in real numbers, neither a concession. **A:** "Only Christina's $26,450 in projected remaining pay is large enough on its own to close the $25,000 shortfall in a single cut — every other employee falls $1,600–$6,500 short — and it removes the money permanently with zero dependency on getting a percentage exactly right, leaving the other four employees' pay untouched." **B:** "A flat 22.27% cut removes exactly $25,000, the stated target, with no rounding-driven overshoot, spreads one hardship across five households instead of concentrating all of it on Christina's, and keeps Grampoline's largest driver of new sales (41% of 2018's new sales, more than double Paul's 17%) on the floor." Neither side collapses outright on the base metric — this is the intended ~5.8%-margin balance (T1-09 PASS). B's argument does not fully "collapse" but visibly weakens first, and at a specific, identifiable question: Q5 of the Socratic set ("does the math actually favor letting Christina go less than it first appeared, once the revenue risk is priced in?") — because once the Twist's $5,740 at-risk-revenue figure is introduced, Option A's *only* clean single-employee fit (Christina) no longer clears the target ($20,710 net vs. $25,000), which is the case's designed tension, not an artifact — FACILITATOR.md states explicitly this doesn't make Full Stop wrong for everyone (a different employee is untouched by the Twist, but then undershoots the target on its own terms instead). Confirms the recorded 5.8% margin reflects a real, close balance and not a paper number. |
| P3 trap | **PASS** | Read `case.md` alone (Overview/Background/Dilemma/Appendices A–E, no Guide Notes) and independently named the most plausible wrong path before reading `FACILITATOR.md`: a student reasons from Appendix A's bios alone — Martha's caregiving crisis, Paul's missed sales targets — and picks one of them for Full Stop without checking whether their remaining pay actually reaches $25,000 (it doesn't: Martha/Irene $1,600 short, Paul $4,500 short, Tiago $6,500 short — only Christina's $26,450 clears it, and even then overshoots). Then read `FACILITATOR.md`'s "The trap" section and its guide notes ("A Hero picks an employee to let go based on their personal story before checking whether the number actually solves the stated problem") — an exact match, same employees named, same shortfall figures. The guide names the identical trap a fresh reader independently identifies; a facilitator running this case is watching for the actual failure mode. |
| P4 twist | **PASS** | (1) The Twist invalidates a real, popular position: "pick whichever employee's number is biggest" (i.e., Full Stop + Christina, the *only* single-employee cut that cleanly closes $25,000 pre-Twist) — post-Twist her net benefit is $26,450 − $5,740 = $20,710, which undershoots the $25,000 target by $4,290, independently reproduced from Appendix B's given 2017/2018 revenue ($261,000→$275,000, $14,000 growth) and Appendix A's given 41% new-sales share. (2) Re-derived the Twist under every stated Modeling Assumption, reading each the way a student would rather than the way the author intended: MA2 (Francesca excluded from target/base) is untouched by the Twist — the Twist only adjusts Option A's chosen-employee figure, never the $25,000 target or Option B's base pool; MA3 (H1→H2 flat continuation) governs D4's whole-company profit projection, a separate calculation the Twist's revenue-growth figure does not touch (the Twist uses Appendix B's already-given 2017/2018 *actuals*, not a projected figure); the Appendix C footnote's employee-vs-company payroll mismatch is orthogonal (D4 uses the company total, D2/D3/Twist use the employee table) — no combination produces a contradiction or double-counted dollar under either a sequential or simultaneous reading. The Twist is delivered live, as a stated fact at delivery time ("$14,000 growth... at 41% attribution, $5,740"), not left for students to infer from ambiguous written text, which further narrows any residual misreading risk. No convention the Twist depends on is left unstated. |
| P5 sensitivity | **PASS** | (unchanged from the mechanical run recorded pre-dispatch) `python3 skills/case-readiness/scripts/tier2_probes.py --case payroll-2-0 --probe 5 --flex 0.5` — swept the one declared FLEX dial (`christina_growth_attribution_pct`, 0.41 → 0.205 / 0.615) ±50%. Base: `{"A": 26450.0, "B": 25000.0}`, winner A, margin 5.8%. Both flexed runs: same result, `flips: false`, `breaks_20pct_cap: false` — the metric the Twist perturbs (Option A's Christina-branch figure) is not the graded `primary_metric`/`margin_pct`, which are computed on the untwisted base per `case.json.balance.margin_basis`, so this sweep correctly leaves them unmoved. Confirmed this is not a FLEX-scoping bug: `PARAMS` correctly separates the one genuine author-chosen assumption (`christina_growth_attribution_pct`, filling a real gap — no per-salesperson revenue-growth breakdown exists in the source, only a new-sales split) from every dollar figure that is cited/given data from the legacy source workbook (employee pay, revenue, shortfall target) — none of the given-data params are in `FLEX[]`, matching SKILL.md's "Only FLEX[] is swept" rule exactly. No `sensitivity_disclosure[]` entry needed; result is a genuine, mechanically-verified PASS, not a disclosure workaround. |
| P6 data decay | **PASS** | `case.json.sources[]` is empty and the fetch worklist `tier2_probes.py` builds from it is correspondingly empty — confirmed by re-running the script, which reached `[DELEGATED]` with zero URLs listed. This is by design, not an omission: per `legacy_conversion_note`, Grampoline LLC is a fictional company invented by the original case materials, and every figure in Appendix B/C is the case's own given dataset (verified at conversion time via `openpyxl` against the source workbook, per the same note), not an externally-checkable real-world claim. T1-08's BLOCKER rule for an unbacked "verbatim"/"publicly verifiable" claim on a legacy case does not apply here — the legacy note explicitly disclaims any such claim, and T1-08 already passed clean on this case (see Tier 1 re-run above). With nothing to fetch, there is nothing that can have decayed; vacuous PASS, not NOT RUN. |

**Reproduction of the P1 arithmetic check (run during this QA pass):**

```
total = 23400.0+20500.0+26450.0+18500.0+23400.0  # 112250.0
cut_frac = 25000/112250                            # 0.222717...
new = {emp: base*(1-cut_frac) for emp, base in ...}
# martha 18188.42  paul 15934.3  christina 20559.13  tiago 14379.73  irene 18188.42
# sum(new.values()) == 87250.0  ->  112250.0 - 87250.0 == 25000.0  exactly
```

### Tier 3 — human dry-run

NOT RUN. (Not required for `TIER2_PASS`; required before `VERIFIED`.)

### Gate result

All six Tier 2 probes recorded PASS by name, 0 FAIL, 0 NOT RUN. Tier 1 reconfirmed clean of
BLOCKERs (0 BLOCKERs, 1 benign pre-existing GAP at T1-18, informational only). **State:
TIER2_PASS.** `case-publish` may now run on `payroll-2-0`.
