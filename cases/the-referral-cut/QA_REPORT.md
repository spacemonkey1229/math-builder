# QA_REPORT.md — The Referral Cut

## case-readiness run — 2026-09-09

**State:** `TIER2_PASS` (scoped to Tier 1 + Tier 2 probes 1-6, per instruction — case-publish not
run this pass, so P7 is out of scope; matches the interim pattern `cases/the-special-order`'s own
first readiness pass used)
**Verdict:** PASS   **Tier 1:** 0 BLOCKERs, 2 GAPs (carve-out + first-run hash)   **Tier 2
(in-scope, P1-P6):** 6/6 probes recorded, 0 FAIL

`skills/case-readiness/scripts/preflight_lint.py --case the-referral-cut` ran first: 1 advisory
finding (FLEX[] declares `packaging_cost`, and `case.json.modeling_assumptions[]` is empty) —
expected and addressed below; this case needed no `{{NEEDS_SOURCE}}`-style Modeling Assumption
(all three real figures were SOURCED), so the flexed dial is instead an author-owned operational
figure disclosed via `case.json.sensitivity_disclosure[]`, not a `modeling_assumptions[]` entry.

### Tier 1 — structural (21 checks)

```
checks run: 21   PASS 19 · GAP 2 · FAIL 0
T1-01 PASS   T1-02 PASS   T1-03 PASS   T1-04 PASS   T1-05 PASS   T1-06 PASS   T1-07 PASS
T1-08 PASS   T1-09 PASS   T1-10 GAP    T1-11 PASS   T1-12 PASS   T1-13 PASS   T1-14 PASS
T1-15 PASS   T1-16 GAP    T1-17 PASS   T1-18 PASS   T1-19 PASS   T1-20 PASS   T1-21 PASS
```

**GAP (2):**
- **T1-10** — `new_coverage[]` is empty; the case closes no *new* (`n==0`) skill. Downgraded from
  BLOCKER to GAP via the reinforcement carve-out (`skills/case-readiness/SKILL.md`, 2026-08-17
  amendment). `case.json.reinforcement_note` records that every one of the 10 claimed skills was
  checked against `readmodel/standards_spine.json` before writing and none is `n==0` (lowest are
  the four Multiplication of Fractions how-tos this concept targets, at `n=1`/`n=2`). A full
  spine-wide scan run the same day found **zero** `n==0` skills anywhere in the 322-skill spine —
  a corpus-wide condition (the prior batch's publish commit records "spine reaches 0 uncovered"),
  not a defect in this case's own skill selection. Flagged for the project owner in
  `LEARNING_GOALS.md`'s "new_coverage note" and `case.json.reinforcement_note`.
- **T1-16** — no `case_md_sha256` recorded before this run (expected on a first pass); resolved by
  this report's `qa` block, which records `f41709677a0d0c17dc7cdf07ece93ecd427c0916d86ce0982efa3975017fc13c`.

**POLISH (6, all "no `published/` directory yet"):** T1-07 (10 labels parsed, all from the
bulleted half), T1-15, T1-18, T1-19, T1-20, T1-21 — expected and correct, since `case-publish` was
intentionally not run this pass per instruction.

### Tier 2 — simulated play (6 of 7 probes; P7 out of scope per instruction)

The task instructions for this run scope Tier 2 to probes 1–6. **P7 (accessibility cold-read) was
not run** — its mechanical pre-screen requires a published `published/*.html` Interactive HTML
file, and `case-publish` was explicitly not run this pass. Recorded in `case.json.qa.tier2.P7` as
`"NOT RUN -- out of scope"`, not fabricated as a pass.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh, unbriefed subagent given only the leak-free packet reached a fully defensible position with correct arithmetic (every figure matched `sensitivity_model.py` to the exact cent: $15-15/16 post-referral proceeds, $6-5/16/unit and $252-1/2/month for A, $3-1011/1250 fulfillment fee and $5-6287/10000/unit and $225-37/250/month for B, $2,212-7/16 and $765-27/32 working capital). It chose **B**, having constructed its own "return on working capital" metric (monthly margin ÷ capital tied up) rather than raw monthly margin, and named that metric explicitly. Per this skill's own P1 pass criterion ("the solver reaches a defensible position, with correct arithmetic, and can name the metric it optimised" — not "reaches the case's own declared winner"), this is a genuine PASS, and is itself evidence the balance test is real: a fresh reader can build an equally rigorous, differently-optimized argument for the losing option using the case's own D5 data. |
| P2 both-sides | **PASS** | Both options genuinely defensible with real numbers; neither collapses on fake or unsupported arithmetic. Fresh subagent found FBM (A) wins on recurring monthly margin ($252-1/2 vs $225-37/250) while FBA (B)'s real strength — $1,446.59 in freed working capital — is a one-time effect; it computed the break-even point (~53 months) at which A's recurring margin advantage overtakes B's one-time capital advantage, correctly identifying B's argument as time-limited rather than fake. |
| P3 trap check | **PASS (after remediation)** | Fresh subagent's independently-predicted top trap — computing Option B's fulfillment fee by adding the raw surcharge number ($3.68+0.035=$3.715) instead of multiplying by (1+the surcharge fraction) ($3.68×1.035=$3.8088) — matched `FACILITATOR.md`'s stated trap exactly, down to both numbers. The same subagent flagged a second plausible trap (applying the 3.5% surcharge to the $18.75 item price instead of the $3.68 fulfillment fee) that `case.md`'s Appendix C text pre-empts but `FACILITATOR.md`'s "The trap" section had not named explicitly. **Fixed**: added as an explicit second trap, with both the correct ($0.129) and wrong ($0.656) surcharge amounts now recorded in `case.json.derived` for T1-14 continuity checkability. |
| P4 twist integrity | **PASS** | A second fresh subagent independently re-derived every figure in the case to the exact cent and confirmed all of it. Confirmed the twist — that the recommendation rests on Mia's own unverifiable packaging/postage estimate, not on Amazon's sourced, non-negotiable fees, and that a real (~22%) increase in that one figure flips the verdict — genuinely invalidates an unqualified "Amazon's fees are what decide this" room position, and survives every natural/defensible reading of `case.md`'s stated quantities and formulas (subtraction order, the multiplicative-vs-additive surcharge question is explicitly resolved as a trap not an ambiguity, and the shared $6.50 production cost cancels regardless of reading). |
| P5 sensitivity | **PASS (disclosed)** | Machine-run via `sensitivity_model.py` (`FLEX=["packaging_cost"]`). `packaging_cost` — Amber & Oak's own author-chosen, unverifiable per-unit cost, not a sourced platform fee — flips the verdict to B at +50% flex ($4.6875 vs. the stated $3.125) and breaks the SPEC §2 20% cap at -50% flex (margin 39.9%, A even further ahead). Both disclosed via `case.json.sensitivity_disclosure[]` as Category F. Separately confirmed (informational, not part of the default sweep): flexing the three real Amazon fee figures [S1][S2][S3] by ±50% does **not** flip the verdict in either direction — the case is robust to platform-fee uncertainty and fragile only to the one figure nobody outside the fictional business could verify, a real and pedagogically load-bearing finding reflected in `FACILITATOR.md`'s Twist. |
| P6 data decay | **PASS (after correction)** | A live re-fetch of all 3 cited URLs (2026-09-09): S1 (Amazon's own pricing page) and S2 (Goat Consulting's rate card) reachable, values confirmed present verbatim. **S3 was found to be imprecisely cited**: the original citation (Amazon's own Selling Partners corporate blog) confirms the 2026 fee-update program in general terms but does not itself state the 3.5% figure, the April 17 date, or the fee-vs-price mechanism anywhere on the page. **Corrected**: re-sourced to Digital Commerce 360's April 3, 2026 report, which explicitly quotes Amazon's own announcement for all three details; confidence downgraded HIGH → MEDIUM (reputable trade-press journalism citing a named tier-1 source, not a direct primary fetch); corroborated by CNBC, WeAreUncapped, DCL Logistics, and Novadata's independent 2026 coverage with zero numeric disagreement. Corrected in `case.json.sources[S3]`, `case.md` Appendix E, and `RESEARCH_LOG.md`. |

### Real defects found and fixed during this run

1. **A genuine, previously-unnamed second trap (P3).** See above — `FACILITATOR.md`'s trap section
   was incomplete (named only the additive-vs-multiplicative error) until a fresh adversarial read
   surfaced the wrong-base failure mode (surcharge applied to item price instead of the fulfillment
   fee). Same class of finding as `cases/the-special-order`'s own P3 remediation.
2. **An imprecise source citation (P6).** S3's 3.5% surcharge figure was attributed to a page that
   does not actually state it. Corrected to a source that does, with an honest confidence downgrade
   rather than a silent fix. Same class of finding as `the-special-order`'s own S4 characterization
   fix.
3. **A model/harness compatibility bug, found and fixed before probes ran, not a case defect:**
   `sensitivity_model.py`'s first draft stored `PARAMS` values as `fractions.Fraction` objects and
   returned `Fraction` results from `evaluate()`. `tier2_probes.py`'s P5 sweep only numerically
   flexes `isinstance(val, (int, float))` params, so `packaging_cost` (the declared `FLEX[]` dial)
   was silently skipped as "non-numeric," and its `round()`/`json.dumps()` handling crashed on raw
   `Fraction` values regardless. Fixed by storing `PARAMS` as plain floats (every dollar figure in
   this case is an eighths/quarters/halves mixed number, exactly representable in binary — no
   precision lost) and converting to `Fraction` immediately inside `evaluate()` via a `_frac()`
   helper, returning `float()` results at the end (same convention `cases/the-special-order`'s own
   model already uses). Verified: `python3 cases/the-referral-cut/sensitivity_model.py` reproduces
   the exact same fractions/mixed-number values before and after this fix.
4. **A first-run leak-avoidance check during authoring, not a defect:** the initial `case.md` draft
   placed the surcharge-application trap's wrong-answer framing loosely in Appendix C; confirmed
   before any Tier 1/2 run that no computed answer (post-referral proceeds, either option's margin,
   the margin percentage, or the packaging-cost flip point) appears anywhere in `case.md` — all such
   figures live only in `FACILITATOR.md` and `case.json`, consistent with the guard comment at the
   bottom of `case.md`.

### Balance and margin — real, computed numbers

`case.json.balance.margin_pct` = **10.83%**, inside the approved concept's 8-15% target band,
computed at Rivendell's actual guaranteed batch size of 40 units/month. Fulfilled by Merchant (A):
$6-5/16/unit ($252-1/2/month). Fulfilled by Amazon (B): $5-6287/10000/unit ($225-37/250/month). All
fee/margin arithmetic was carried in fraction/mixed-number form throughout (3/20, 17/20, 75/4,
255/16, 92/25, 207/200, 4761/1250, 56287/10000, etc.) via `sensitivity_model.py`'s exact
`fractions.Fraction` computation — no floating-point rounding at any intermediate step; only the
model's final return values and this report's prose use decimal approximations for readability.

### All 10 claimed skills — genuinely forced

Verified via `LEARNING_GOALS.md`'s bidirectional check (0 unmapped deliverables, 0 unreachable
skills) and independently confirmed by the P1/P2/P4 subagents' own worked solutions, all of which
performed genuine referral-fee simplification (D1), mixed-number × fraction multiplication (D1),
fraction × fraction multiplication for the surcharge (D3), fraction × whole-number multiplication
for the monthly scale-up (D4), and mixed-number × mixed-number multiplication for working capital
(D5) — without being told the skill names, i.e. the math was actually forced, not merely labeled.

### Next step

`Run the-referral-cut through case-publish` — but first, run Tier 2 P7 for real against the
published Interactive HTML (not done this pass, per instruction), since `case-publish`'s own gate
requires every probe recorded, not six of seven.
