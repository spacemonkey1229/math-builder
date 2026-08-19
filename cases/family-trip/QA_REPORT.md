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

## case-readiness Tier 2 run — 2026-08-18
**State:** TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (re-checked, not the object of this run)
Case entered this run at `TIER1_PASS` (0 blockers, verified live). Two real Tier-2 defects were
found and fixed directly in `case.md`/`case.json` (see P6 below), which — as an expected,
mechanical side effect of editing `case.md` — re-triggers `tier1_structural.py`'s continuity
checks until the published artifact is regenerated: T1-15/T1-16/T1-18 now correctly fire STALE
against `published/Family Trip - Interactive.html`, which still contains the pre-fix text
("one lap child per adult", the old IRS URL). This is not a new content defect — it is the
expected, honest consequence of fixing case.md mid-pipeline, and it is what `case-publish` exists
to resolve next (it rebuilds the interactive HTML from the current case.md). `case.json.qa.state`
below reflects the Tier 2 content verdict per this skill's ladder; the published HTML must be
rebuilt via `case-publish` before this case is truly current for learners.

### Tier 2 — simulated play (6 probes)
| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Genuinely fresh subagent (packet only) chose B (drive), optimizing "real out-of-pocket cash cost against the stated $1,300 budget." Arithmetic matched `sensitivity_model.py`'s base case exactly: A=$1,940.80, B gas-only=$602.50, B fully-loaded=$1,754.88. Correctly named MA4 (cost-definition choice) as its most sensitive assumption, correctly ignored Appendix C's non-representative $58 low-demand fare, and correctly flagged MA1's 2-year-old fare projection as the least-supported number. Defensible position, correct arithmetic, named metric — clean pass. |
| P2 both-sides | PASS | Built directly from case.md. A's strongest line: real cash cost $1,940.80 (blows the $1,300 budget by $640.80) but buys ~3 more days in Gilbert on the same 5 vacation days and cuts family transit from ~29 hours to a few hours with two infants. B's strongest line: real cash cost $602.50 — under half the budget, $697.50 left for gifts — and B still wins even under the Twist's fully-loaded IRS-rate lens (10.6% margin), not just the naive gas-only one. Neither side collapses to concession-only: A's pure-cost defense weakens hardest at D5 (dollars-remaining goes negative), but its rebuttal (extra days, less transit time) is itself quantified from the case's own numbers, not hand-waved. |
| P3 trap | PASS | Independent fresh subagent (case.md only, before FACILITATOR.md) predicted a different trap than the guide names: it expected a fare-doubling misread of Appendix C's "one-way fare (round-trip purchase)" column header, vs. FACILITATOR's actual trap (defaulting to 6 paid tickets instead of 4, missing the lap-child exemption). On review this is a near-miss, not a guide gap: Appendix H's MA1 already hands students the correct $474/passenger round-trip figure precomputed, and Challenge D1 explicitly directs attention to "how many of the six family members actually need a paid ticket" — both structurally shield against the subagent's predicted misread while directly inviting the guide's actual trap. FACILITATOR's named trap remains the case's single most probable failure mode; the subagent's alternate is a real but lower-probability path, not an unanticipated one. |
| P4 twist | PASS | Re-derived mechanically via `sensitivity_model.py`'s `evaluate()`/`evaluate_twist()`: pre-Twist gas-only reading is a landslide (B $602.50 vs A $1,940.80, 222% margin); post-Twist fully-loaded reading narrows to B $1,754.88 vs A $1,940.80, 10.6% margin — winner unchanged (B) but the "landslide" position a real room would hold going in is invalidated. Checked against every stated assumption (MA1–MA6) and Appendix G's calendar/vacation-day limits under both a sequential and a simultaneous reading; the arithmetic (1,888 round-trip miles × $0.76/mi + $320 hotel) requires no unstated convention and is unambiguous either way. |
| P5 sensitivity | PASS (disclosed) | Carried forward unchanged from the prior mechanical run (not re-run, per instructions): base A=$1,940.80/B=$1,754.88, margin 10.6%, B wins. Genuinely unstable under ±50% flex on `fare_per_leg_usd` and `hotel_rate_per_night_usd` (a -50% fare flex flips the winner to A); both dials carry matching `sensitivity_disclosure[]` entries in case.json and Guide Notes — disclosed, not eliminated, per the project's disclosure-aware PASS doctrine. |
| P6 data decay | PASS (2 defects found and fixed) | Fetched all 10 live URLs (S1–S4, S6, S7, S8, S10–S12; S5/S9 are local docx image references, non-fetchable, noted as such). **S2** (fueleconomy.gov) confirmed exact: 19/27/22 mpg, 21.0 gal. **S4** (allegiantair.com) confirmed: $58 low-demand fare still shown. **S7** (allegiantair.com/baggage-1) confirmed: personal item free, carry-on/checked dynamic. **S11** (gasprices.aaa.com) confirmed: $4.0654/gal, consistent with the cited $4.04. **S1** (trippy.com) and **S6** (tsa.gov) returned HTTP 403 to automated fetch (bot-blocked, not confirmed dead — both are long-stable, low-volatility figures: a fixed interstate route distance and a statutory federal fee unchanged in years). **S3** (skyscanner.com) is a JS-rendered SPA that returned no fetchable content — inconclusive via automated fetch. **S10** (lvcva.com/research/) does not show the specific cited $208.02 Strip figure on that landing page (shows a different, broader $183.52 2025 metro-wide ADR instead); already disclosed as MEDIUM/"via aggregated search," and the $208.02 figure is independently corroborated by web search as a real reported Jan–Jun 2026 Strip ADR — noted, not fixed, since it was already flagged as unfetched. **S8** (intercom.help) 404s — DEAD LINK. Re-sourced to Allegiant's own official page (allegiantair.com/traveling-with-children), which surfaced a real, load-bearing wording defect: Allegiant's actual policy is "one lap child **per row**, due to the number of oxygen masks per row" — not "one lap child per adult" as case.md stated. Fixed in `case.md` Appendix D, the Sources table, and `case.json`'s S8 entry; the blockquote now tells the family they must book two separate rows to get both free lap-child slots. The D1 math (4 of 6 need a paid ticket) is unchanged. **S12** (irs.gov) resolves but backs the WRONG figure: the cited URL only supports the January 2026 rate (72.5¢/mile), not the $0.76/mile the case actually uses — confirmed via independent search that a real mid-year IRS Announcement 2026-11 (Internal Revenue Bulletin 2026-29) did raise the rate to 76¢/mile effective July 1, 2026, so the $0.76 figure itself is correct, only the citation was wrong. Fixed: S12's URL re-pointed to `irs.gov/irb/2026-29_irb`, which verbatim states "The revised standard mileage rates are: (1) Business 76 cents per mile." |

### Tier 3 — human dry-run
NOT RUN.

### Overall
**TIER2_PASS.** All six Tier 2 probes recorded by name, 0 real FAIL (P5 is disclosed-unstable, the
project's standing PASS state for that condition). Two genuine P6 citation defects found and fixed
this run (S8 dead link + real policy-wording error; S12 URL backing the wrong rate). `case.json.qa`
updated: `state` → `TIER2_PASS`, `tier2` block recorded, `case_md_sha256` re-stamped to the
post-fix hash. **`published/Family Trip - Interactive.html` is now stale** (still shows the
pre-fix lap-child/IRS text) and must be regenerated by `case-publish`, which this skill does not
run.
