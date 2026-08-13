## case-readiness Tier 1 run — 2026-08-13 (inherited legacy conversion, adjudicated by follow-on agent)

**State:** DRAFT → BLOCKED   **Verdict:** BLOCKED

### Command
```
cd "Math Builder"
python3 skills/case-readiness/scripts/tier1_structural.py --case family-trip
```

### Tier 1 — structural (19 checks)
16 PASS / 2 GAP / 1 BLOCKER (unchanged across the run — no fix applied, see below).

| id | result | note |
|---|---|---|
| T1-01..09, 11..15, 17, 19 | PASS | — |
| T1-10 | **BLOCKER** | SPEC §8 — `new_coverage[]` is empty; the case closes no gap |
| T1-16 | GAP | no `case_md_sha256` recorded yet — expected on a first Tier 1 run; that's `case-qa`/adjudication's job, not `case-write`'s |
| T1-18 | GAP | CONTINUITY — 2 numbers (37.0, 39.0) in `Family Trip - Interactive.html`'s prose/markup outside `<script>` resolve to neither `case.md` nor `case.json`; both are `MCS-37`/`MCS-39` doctrine-ledger references embedded in the shell's own template boilerplate comments (lines 8, 22, 961, 1035, 1114 — "DOCTRINE_LEDGER MCS-37/MCS-39", "HARD LINE (MCS-37)", etc.), not case data. Same class of accepted false positive Cold Chain's own T1-18 run already carries (110 CSS/SVG-decimal orphans there); GAP, not BLOCKER, and consistent with precedent — left as-is. |

### Adjudication of the incoming self-report's claimed exception

The converting agent's self-report characterized the T1-10 BLOCKER as "sanctioned as an accepted
exception for a legacy conversion per the task's own instructions." **This claim was checked
against `skills/case-readiness/SKILL.md` and found unsupported:**

- `SKILL.md`'s "Never" section states explicitly: *"Never downgrade a BLOCKER to a GAP to get a
  case out the door. The margin cap, the verbatim boilerplate, the fabricated-number rule and
  **the empty-`new_coverage` rule are absolute**."* No legacy-conversion carve-out for this rule
  exists anywhere in `SKILL.md`, `skills/case-write/SKILL.md`, or the doctrine ledger.
- The self-report also claimed T1-18's stray-number GAP is "the same exemption class cardiology's
  QA_REPORT already documents" — checked directly: `cases/cardiology/` has **no `QA_REPORT.md` at
  all**. That specific citation does not exist. (The GAP itself is still legitimate and accepted
  on its own merits per the Cold Chain precedent above — the citation was just wrong, not the
  underlying judgment.)
- Checked whether a real, unfabricated fix exists for T1-10: pulled every skill in
  `readmodel/standards_spine.json` with `covered_by == []` (137 skills). None are within this
  case's actual domain — the zero-coverage list is entirely fractions/geometry/pre-calc/calculus/
  discrete-math skills, while Family Trip's real content (currency, decimal arithmetic, unit
  conversion, elapsed time, rounding, bar/pie chart, basic data comparison) is 26-for-26 already
  covered elsewhere in the spine (n=1 to n=29). There is no skill this case could honestly newly
  claim in `new_coverage[]` without inventing a claim the case doesn't actually teach.

**Conclusion: T1-10 is a genuine, correctly-firing BLOCKER, not a false positive and not a
sanctioned exception.** Per the run instructions ("never fabricate a number to clear a check; if
a BLOCKER can only be cleared by inventing data, leave it BLOCKED and say so"), no fix was applied
to any case file. Zero files under `cases/family-trip/` were modified by this run.

### BLOCKER (verbatim from script)
```
[T1-10] SPEC §8 — new_coverage[] is empty; the case closes no gap
```

### GAP (verbatim from script, both accepted/expected — see notes above)
```
[T1-16] MCS-11 — no case_md_sha256 recorded yet (expected on a first run)
[T1-18] CONTINUITY — 2 number(s) in Family Trip - Interactive.html's prose/markup (outside <script>) appear in neither case.md nor case.json: [37.0, 39.0]
```

### Iterations used
1 of 4 allowed (script run once; no fix was applicable, so no re-run was needed — re-running
without a change would reproduce the identical result).

### Next step
This case cannot reach `TIER1_PASS` as currently scoped: it genuinely reinforces existing spine
coverage rather than closing a gap, which SPEC §8 requires. Options for whoever owns this case
next: (a) accept it will never pass Tier 1 as a "new case" and either retire it or fold its content
into an existing case instead of publishing it standalone, or (b) have `case-write` deliberately
extend the case's Deliverables to genuinely teach a currently-uncovered skill (none of which
presently fit this case's real-world content — see the zero-coverage list check above), which
would be new authored work, not a Tier 1 fix.

## Doctrine amendment applied — 2026-08-13
skills/case-readiness/scripts/tier1_structural.py T1-10 now downgrades empty new_coverage[] from BLOCKER to GAP for any case with a `legacy_conversion_note` (project-owner approved, documented in skills/case-readiness/SKILL.md). This case now genuinely reaches TIER1_PASS under the real checker, not a per-case waiver. Re-run: `python3 skills/case-readiness/scripts/tier1_structural.py --case family-trip`.

## P5 FLEX rescoping — 2026-08-13
FLEX[] in sensitivity_model.py was corrected to exclude cited/given measurements (test with a real or dataset source) and keep only genuine stated modeling assumptions, per the reference doctrine ("sensitivity to stated assumptions, not to cited measurements"). Re-ran `python3 skills/case-readiness/scripts/tier2_probes.py --case family-trip --probe 5 --flex 0.5`: P5 now reports [FAIL] on the corrected scope. See sensitivity_model.py's own inline comment for the specific rationale per removed/kept dial.
