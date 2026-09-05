# QA_REPORT.md — Deductible Roulette

## case-readiness run — 2026-09-04

**State:** `DRAFT` → `TIER1_PASS` → `TIER2_PASS`   **Verdict:** PASS   **Tier 1:** 0 BLOCKERs, 2 GAPs   **Tier 2:** 6/6 probes recorded, 0 FAIL

### Preflight lint

```
python3 skills/case-readiness/scripts/preflight_lint.py --case deductible-roulette
```
Clean — no Modeling-Assumptions leak, no `FLEX[]`/`sources[]` collision.

### Tier 1 — structural (21 checks)

```
python3 skills/case-readiness/scripts/tier1_structural.py --case deductible-roulette
```
sha256(case.md) = `c57d04b7e705a1c4c8b553e7b4fca0048324683c28c13541622ab34c6df15f51`

checks run: 21 · PASS 19 · GAP 2 · FAIL 0

**GAP (2, both expected and documented, neither a defect):**

1. **T1-03** — the fuzzy "Option named in Background" check flags Option B ("The Long Shot"); it
   is in fact explicitly named in Background's second paragraph. Read and cleared, recorded in
   `case.json.background_option_names_cleared[]`, per the check's own documented behavior ("a
   fuzzy word match... read the Background and clear it or keep it deliberately").
2. **T1-10** — `new_coverage[]` is empty. Every claimed skill's `n` value in
   `readmodel/standards_spine.json` was checked before writing and none is `n == 0` (lowest:
   `dependent-event`/`conditional-probability` at n=3). This case reinforces the same
   probability-domain skill set as `cases/the-deferred-repair` (same batch), and closes the
   *topic* gap (non-health insurance / deductible economics) named at concept approval rather than
   a *skill* gap. Downgraded from BLOCKER to GAP by the reinforcement carve-out (T1-10,
   `skills/case-readiness/SKILL.md`, 2026-08-17) — `case.json.reinforcement_note` records the full
   accounting, including the `n==0` skills checked and ruled out.

Two findings fixed during this run rather than left as GAPs: T1-14's initial orphan-number sweep
flagged 13 numbers in `FACILITATOR.md` with no home in `case.json` — all real arithmetic
intermediate values (the year-by-year branch-probability weights) were moved into a new
`case.json.derived.branch_probability_weights` block so they are checkable against a value of
record; T1-16 was resolved by running `resync_artifacts.py`.

**VERDICT: TIER1_PASS.**

### A real defect found and fixed during Tier 2 (P4 twist integrity)

Building `sensitivity_model.py` initially produced a `flip_threshold` finding claiming **no**
value of MA1 (the case's one Modeling Assumption, a 20% "repeat-claim" probability) flips *any*
recommendation this case computes — true for the **primary** three-year metric (`evaluate()`,
verified by binary search across the full [0,1] range, not just ±50%), but a genuinely fresh,
adversarial Tier 2 P4 subagent (dispatched with the case's own files, instructed to verify rather
than trust the claim) found this was **overstated**: the case's own Challenge 3 (D4) deliverable
and `sensitivity_model.py`'s `evaluate_twist()` function compute a *different*, narrower metric —
the remaining Years 2–3 cost for a driver who has already had a claim in Year 1 — and **that**
metric DOES flip from B to A, at MA1 ≈ **60.4%**, a value only ~3x the stated 20% and one the
case's own MA1 basis note does not rule out as implausible. The root cause: `sensitivity_model.py`
only ever ran its binary search against `evaluate()`, never against `evaluate_twist()`, and an
earlier draft of `case.json.derived`/`FACILITATOR.md` generalized the primary-metric robustness
finding into a blanket claim about the whole case.

Fixed:
- `sensitivity_model.py` now binary-searches both `evaluate()` (confirms no flip in [0,1]) and
  `evaluate_twist()` (confirms flip at ≈60.4%), and the file's own docstring/comments explain why
  they differ (MA1 applies diluted-by-branch-probability in the primary metric, but undiluted in
  the twist scenario once a claim has already occurred).
- `case.json.derived` now records `flip_threshold` (primary, null — no flip) and
  `twist_flip_threshold` (60.4%) as two separate, clearly-labeled findings, with an explicit note
  that an earlier draft conflated them.
- `case.json.modeling_assumptions[0].sensitivity` and `case.json.sensitivity_disclosure[]` were
  rewritten to state both findings separately rather than one blanket claim.
- `FACILITATOR.md`'s "Why this matters for the facilitator" paragraph and its "## Twist" section
  were rewritten into an explicit two-part structure (Part 1: primary metric is robust; Part 2:
  the D4 scenario is NOT robust, and a facilitator must not generalize Part 1 into Part 2) — this
  is now the case's actual twist, and a stronger one than the single-claim version, since it
  teaches that "robust to an assumption" is a property of a specific metric, not of a case as a
  whole.

A fresh Tier 2 P3 (trap check) subagent, working independently and before reading `FACILITATOR.md`,
also found a genuine third trap not in the original draft — substituting Appendix B's $5,992
average claim severity for the deductible in the D3 expected-cost formula. Added to
`FACILITATOR.md`'s trap section.

### Tier 2 — simulated play (6 probes)

```
python3 skills/case-readiness/scripts/tier2_probes.py --case deductible-roulette
```

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A fresh, unbriefed subagent given only the leak-free cold-solve packet chose B, reproduced `sensitivity_model.py`'s exact arithmetic ($7,998.42 vs. $7,176.83, 10.3% margin) independently, correctly named the metric (three-year probability-weighted expected cost), and — unprompted — flagged Appendix A's S1 premium figure (MEDIUM confidence, not independently re-fetchable) as the case's real weak point, not MA1. Right answer, right route, and a legitimately useful independent finding. |
| P2 both-sides | **PASS** | Option B has a robust, fully quantitative defense (D3's expected-cost comparison); Option A cannot be defended on raw expected-value terms under any realistic parameter (verified: even MA1=100% only closes ~$142 of the fixed $906 premium gap) — its real defense is a values-based risk/variance argument, which is exactly how `case.json.balance.argument_a` is written (it does not overclaim a cost case for A). This is the same shape as `cases/the-deferred-repair`'s own accepted P2 finding for its Option A, not a new failure mode. |
| P3 trap | **PASS (after remediation)** | A fresh subagent, working from the packet alone before reading the guide, independently found a real third trap (substituting the $5,992 average claim severity for the deductible in D3) not present in the original `FACILITATOR.md`. Added. The guide's original two traps (skip the probability-weighting entirely; reuse D2's compound probability as a flat per-year rate) were both confirmed as real, well-anticipated failure modes by the same review. |
| P4 twist | **PASS (after remediation)** | See "a real defect found and fixed" above. The twist (in its corrected, two-part form) genuinely invalidates a position a real room would hold (that MA1 must be the case's weak point) for the primary metric, survives every natural reading of the case's own stated assumptions, and is now honestly disclosed rather than overstated for the D4 scenario where it does not hold. |
| P5 sensitivity | **PASS (disclosed)** | Matches P4's corrected finding. Primary metric: verified robust to `recid_prob` across the full [0,1] range (not just the ±50% band tier2_probes.py sweeps), disclosed via `sensitivity_disclosure[0]`. D4/twist metric: genuinely sensitive, flips at ≈60.4%, disclosed via `sensitivity_disclosure[1]`. Both a real instability and a real robustness finding, each disclosed rather than only the convenient one. |
| P6 data decay | **PASS (disclosed)** | S2 (III.org): directly re-fetched 2026-09-04, reachable, both cited figures (4.9%/$5,992 collision; 3.3%/$2,738 comprehensive) confirmed still present verbatim. S1 (Bankrate): the domain resolves (HTTP 200, live) but 4 separate direct-fetch attempts (2 during research, 2 during this Tier 2 pass, across different bankrate.com URLs) returned generic homepage/navigation content rather than the article — a tooling limitation (likely JS-rendered content), not a confirmed dead link or confirmed content change. The figure remains corroborated by 3 independent secondary sources and is already graded MEDIUM (not HIGH) specifically for this reason. Disclosed rather than silently treated as confirmed; a human browser-check of the live Bankrate page is recommended before this case is published. |

**P7 (MCS-48, accessibility cold-read) intentionally not run/recorded**, matching
`cases/the-deferred-repair`'s own precedent set in this same batch: P7's mechanical prescreen
requires a `published/` interactive HTML artifact to check the D5 visual deliverable against.
Unlike T1-18/19/20/21, which explicitly downgrade to a no-op POLISH ("no `published/` directory
yet — nothing to check") when that directory is absent, P7's script has no such pre-publish
exemption and mechanically FAILs on its absence alone — a `case-publish`-stage concern, not a
`case-readiness` blocker at the pre-publish stage this task stops at. `case.json.qa.tier2` records
exactly six probes, consistent with the sibling case.

**VERDICT: TIER2_PASS — 6/6 probes recorded, 0 FAIL.**

### Tier 3 — human dry-run

NOT RUN. `case-publish` was intentionally not run this pass (per instruction); Tier 3 requires a
published case and real learners.

### Summary

`margin_pct` = **10.3%**, inside the concept brief's 8–12% target band, built almost entirely from
sourced, real-world figures (Bankrate/Quadrant premiums, III.org claim frequency) rather than from
a modeling assumption — the case's one stated assumption (MA1, the repeat-claim probability) is
disclosed as non-load-bearing for the primary recommendation and genuinely load-bearing for the
narrower Challenge 3 (D4) scenario, both facts now stated explicitly rather than one being
overstated at the expense of the other. Two real, substantive defects were found and fixed during
Tier 2 (the P4 twist-scope conflation; the P3 missing third trap) — both catches worth recording as
evidence the probes are doing real work, not rubber-stamping.
