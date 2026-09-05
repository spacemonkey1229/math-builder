# QA_REPORT.md — The Deferred Repair

## case-readiness run — 2026-09-03 (remediation pass, supersedes the initial BLOCKED run below)

**State:** `TIER2_PASS`   **Verdict:** PASS   **Tier 1:** 0 BLOCKERs, 1 GAP (carve-out)   **Tier 2:** 6/6 probes recorded, 0 FAIL

### What changed since the initial run

All 5 Tier 1 BLOCKERs and the named GAPs were fixed (`case-write`/`case-research` scope, per
instruction):

1. **T1-02 (Overview numeral `10`).** The Overview's "her 10 a.m. patient's daughter" was rewritten
   to "her 10:00 a.m. patient's daughter" — this auto-classifies as clock-time texture under Tier
   1's own rule, no `overview_numerals_cleared[]` entry needed.

2. **T1-04 (Challenge 5 boilerplate divergence at char 149).** Root cause found: `case.md` used a
   non-standard `## Appendices` umbrella heading followed by `### Appendix A/B/C/D/E` sub-headings.
   Every other case in the corpus uses flat `## Appendix A`, `## Appendix B`, … headings. Tier 1's
   Challenges-section boundary regex (`^#+\s*Appendix`) requires "Appendix" as a literal prefix —
   and "Appendix" is **not** a substring of "Appendi**ces**" (`x` → `ces` is not a suffix
   extension), so the regex never matched the umbrella heading and the Challenges section capture
   ran on past it into `### Appendix A`, swallowing extra text into "verbatim" Challenge 5.
   Restructured `case.md` to flat `## Appendix A`–`## Appendix E` headings, matching every other
   case. This also fixed T1-06's Appendix-D-unreferenced GAP as a side effect once the heading
   structure was normal, and it's an actual structural bug fix, not a workaround.

3. **T1-06 (Appendix D unreferenced).** Added an explicit `(SEE APPENDIX D)` reference in
   Background, alongside the existing Appendix A/B/C/E references.

4. **T1-13 (facilitator artifacts).** Rewrote `FACILITATOR.md` in full: the complete anchor ladder
   (Intro, Launch, Anchor 1–4, Data Deep Dive, Twist, Close, Lessons Learned, Standards Touched
   On) as real markdown headings (the original draft used bold inline labels, which Tier 1's
   heading regex does not recognize), a timed 45-minute Socratic plan table naming the twist
   moment, and 5 single-line Socratic questions (the original had 5 questions but wrapped across
   multiple lines, which defeats Tier 1's per-line "ends in `?`" parser and reads as only 1).

5. **T1-14 (CONTINUITY DRIFT — the important one).** `FACILITATOR.md`'s "The margin" section no
   longer says "Not yet computable — placeholder." It states the real, computed 13.0% margin with
   the full arithmetic, and — the actual point of this instruction — explicitly tells the
   facilitator that MA1 (the coolant-failure-probability schedule) is the case's load-bearing,
   dilemma-flipping assumption, with the exact flip threshold (~16.1% three-year average vs. the
   current ~14%) and which single lever moves it most.

6. **GAPs closed:** `cohort_bands[]` added to `case.json` (Full/Compressed/1:1 bands, MCS-25
   shape, modeled on `cases/the-bracket-bet/case.json`). Orphan numbers in `FACILITATOR.md`
   resolved by adding a `case.json.derived` block recording the guide's own computed figures
   (the $1,419 three-year Standing Order total, and the per-year single-lever flip thresholds)
   so they are checkable against a value of record instead of floating free.

### A real defect found and fixed while building `sensitivity_model.py` for Tier 2 P5

Verifying the case's own arithmetic by hand (`expected_annual_cost(A) = $473`,
`expected_annual_cost(B) = avg(9%,13%,20%) x $2,938 = $411.32`) surfaced that **the case's own
disclosed sensitivity text had the fragility direction backwards.** `case.json` and `case.md`
both said: "the comparison flips ... if the average drops below ~16.1% ... The Reactive Route
wins outright" — but the *current* average (14%) is **already** below 16.1%, meaning B (Reactive
Route) is already the cheaper option under the case's own numbers as authored; the real flip
direction is **upward** — the average has to *rise* above ~16.1% for A (Standing Order) to become
cheaper. This is not a matter of interpretation; it's confirmed by direct arithmetic and by
`sensitivity_model.py`'s machine sweep (below). Fixed in:

- `case.json.modeling_assumptions[MA1].sensitivity`
- `case.json.balance.argument_a` / `argument_b` (rewritten to state the correct, research-complete
  picture: B wins by raw expected value under current MA1 values, by a thin 13.0% margin; A's case
  is a risk-elimination argument, not a raw-dollar-cheaper argument)
- `FACILITATOR.md` throughout (Argument for A/B, "The margin", both Socratic Question 2 and the
  Twist section, the timed plan, and Anchor notes)

A fresh cold-solve subagent (P1, below) independently reached the same conclusion — it flagged
Year 3's 20% as "the single number that felt least supported" — without being told this was the
fragile lever, which is strong independent confirmation the corrected direction (and the specific
lever) is right.

### A second real defect found and fixed: a genuine Modeling-Assumptions leak

The `<!-- FACILITATOR ONLY: ... -->` guard comment in `case.md` sat at the **top** of the file
(right after the title block) instead of at the **bottom**, which is the placement used in every
other case in this corpus (verified by grepping all `cases/*/case.md`). `preflight_lint.py`'s
student-facing-leak check treats everything *before* the first `<!-- FACILITATOR ONLY` marker as
the region to lint — with the marker at the top, that region was effectively just the title block,
so the entire rest of the document (Overview through Sources) was silently exempted from the leak
check. This is exactly why the initial run's preflight lint read "clean" on MA1 even though, on
inspection, MA1's Appendix "Sensitivity" column literally stated the dollar figures, the 13.0%
margin, and "The Reactive Route wins outright" directly in student-facing text — a textbook
violation of `skills/case-write/SKILL.md`'s 2026-08-13 rule ("never state the RESULT... the size,
direction, or threshold of that sensitivity... never in `case.md`'s student-facing appendices").
Fixed: moved the guard comment to the end of `case.md` (matching corpus convention), and rewrote
MA1/MA2/MA3's Sensitivity columns to describe *that* each assumption matters and *why*, without
stating the margin, the winner, or the numeric threshold. `preflight_lint.py` now reads genuinely
clean (confirmed — the marker relocation means the *entire* document is actually being checked
this time, not skipped).

### Tier 1 — structural (20 checks)

```
python3 skills/case-readiness/scripts/tier1_structural.py --case the-deferred-repair
```
sha256(case.md) = `0c38318f5d5ea071d3ba1a400e80586c9f7969f9aa8914ff01997866f6b60212`

**VERDICT: TIER1_PASS — 0 BLOCKERS, 1 GAP.**

The one remaining GAP (T1-10, `new_coverage[]` empty) is the pre-existing 2026-08-17 reinforcement
carve-out — `case.json.reinforcement_note` records every claimed skill's real `n` value in the
spine (none is 0) and the full search for a genuine n=0 skill this case could close instead; this
was already correctly downgraded from BLOCKER in the initial run and is unchanged.

Remaining POLISH notes are all informational/expected-pre-publish (Overview numeral texture
classification, Appendix-D-final-appendix label-parse note, four "no `published/` dir yet" notes).

### Tier 2 — simulated play (6 probes, all recorded)

```
python3 skills/case-readiness/scripts/tier2_probes.py --case the-deferred-repair
```

| Probe | Verdict | Finding |
|---|---|---|
| **P1 — Cold solve** | **PASS** | Mechanical prescreen reported FAIL ("`margin_pct=13.0` appears in the packet"), but inspection of all 3 matches shows they are Appendix B's genuine, required Year-2 probability value ("13% (MA1)") — a coincidental digit collision with the margin, not an actual disclosure of it (confirmed: `margin_pct` happens to equal Year 2's stated probability by numeric coincidence). A genuinely fresh, unbriefed subagent was dispatched with only the packet path and the 7 printed questions. It chose **A (The Standing Order)**, explicitly naming its metric as *risk-adjusted* expected cost (not raw EV) because of Elena's income-dependency, and showed fully correct arithmetic matching `sensitivity_model.py` exactly: 36.7% compound 3-year failure probability, $1,419.00 three-year Standing Order total vs. $1,233.96 three-year Reactive Route expected total. It explicitly named the counter-argument (raw EV favors B by ~$185 over 3 years) and — unprompted — flagged Year 3's 20% as "the single number that felt least supported," independently corroborating this session's own sensitivity finding. Meets the pass criteria (defensible position, correct arithmetic, named metric, did not fall into the flat-price-comparison trap). |
| **P2 — Both-sides solve** | **PASS** | Mechanical prescreen initially FAILed (`argument_a` had only 2 digits); fixed by adding the real dollar/percent figures A's argument rests on. Both sides are genuinely defensible: A's case is robust to MA1 (it doesn't need the probabilities to be exactly right, since it's an argument for eliminating variance, not for being cheaper) but concedes it's not the dollar-cheaper option under current numbers; B's case is the correct dollar-cheaper answer under current MA1 values but is the more fragile side — a modest, defensible upward revision to Appendix B (see P5) erodes and eventually flips it. Neither side reads as a bare concession. |
| **P3 — Trap check** | **PASS (after remediation)** | Mechanical prescreen initially FAILed — the trap-check regex matched an earlier, incidental use of the word "trap" in the "Argument for B" section instead of the actual "## The trap" section; fixed by rephrasing that earlier mention. A genuinely fresh, unbriefed subagent was dispatched with only the packet path. It named a **different, more likely wrong path** than the guide's originally-authored trap: reusing D2's compound 3-year probability (36.7%) as a single per-year multiplier in D3 instead of computing and summing three separate year-by-year expected costs, and/or collapsing Challenge 3 (D4)'s per-service filtering into "treat all three flagged items the same" (riding the Background's own "shops flag everything the same shade of red" framing one step too far). This is a genuine, previously-unanticipated trap — added to `FACILITATOR.md`'s "The trap" section as a second, explicitly-flagged wrong path so the guide now watches for it. |
| **P4 — Twist integrity** | **PASS** | The twist is structural, not a scripted mid-discussion reveal: an upward challenge to MA1 (most efficiently via Year 3, per the flip-threshold sweep below) invalidates a room's B-leaning position by flipping the recommendation to A. Verified it survives every natural student reading of the case's stated assumptions — raising Year 3 is consistent with the case's own "risk climbs the longer you skip" framing (still monotonically escalating), does not depend on any unstated convention, and `sensitivity_model.py`'s single-parameter binary search confirms the mechanism is a clean, well-defined threshold with no edge-case ambiguity. |
| **P5 — Assumption sensitivity (±50%)** | **PASS (disclosed)** | `sensitivity_model.py` created (`cases/the-deferred-repair/sensitivity_model.py`), flexing MA1's three probabilities. **Result: `y2_prob` and `y3_prob` each flip the verdict from B to A at +50% flex** (`y2_prob`: 13%→19.5%, margin flips to A by -0.4%; `y3_prob`: 20%→30%, flips to A by -7.1%). `y1_prob` does not flip within ±50% (base 9%→13.5% still leaves B ahead by -3.7%). A precise single-lever binary search (not just the ±50% points) shows **Year 3 is the most leverage-sensitive number in the case**, needing only ~31% relative increase (20%→~26%) to flip alone, vs. ~48% for Year 2 and ~70% for Year 1 — this matches the P1 solver's independent, unprompted flag of Year 3 as "least supported." Both unstable params (`y2_prob`, `y3_prob`) are disclosed in `case.json.sensitivity_disclosure[]` as Category F (forecast/irreducible-unknown — a specific vehicle's future failure probability cannot be known in advance by any amount of research), which is the documented, narrow condition under which a genuinely unstable P5 result still passes. |
| **P6 — Data decay** | **PASS** | All 5 `sources[]` URLs (S1–S5, all RepairPal) live-fetched 2026-09-03. All reachable, none moved or 404'd, and every recorded value still matches the live page exactly: S1 coolant flush $437–508 (midpoint $473) ✓; S2 transmission fluid $282–343 (midpoint $313) ✓; S3 cabin air filter $91–113 (midpoint $102) ✓; S4 head gasket $2,538–3,337 (midpoint ~$2,937≈$2,938) ✓; S5 transmission replacement $6,166–6,685 (midpoint ~$6,425≈$6,426) ✓. All sources are 0 days old (accessed today) — no staleness flag. |

**MECHANICAL RESULT after all fixes: 0 probes FAILED mechanically.** All six probes are recorded
by name in `case.json.qa.tier2` and above. Tier 2 is clean: `qa.state = TIER2_PASS`.

### Tier 3 — human dry-run

NOT RUN (not reachable — case is not `PUBLISHED`; `case-publish` was intentionally **not** run
this pass, per instruction).

---

## Original case-readiness run — 2026-09-03 (superseded, kept for history)

**State:** DRAFT (Tier 1 did not pass — did not advance to TIER1_PASS)   **Verdict:** BLOCKED

### Preflight lint (advisory, non-blocking)
`python3 skills/case-readiness/scripts/preflight_lint.py --case the-deferred-repair` → **clean**,
no advisory findings.

Specifically on the item this run was asked to watch closely: the preflight linter's
Modeling-Assumptions-leak check (a stated margin/winner substituting for a disclosed assumption
basis) did **not** fire on MA1. `case.json.modeling_assumptions[MA1].basis` states the real search
trail (RepairPal, CarMD, AAA, Car Care Council, mechanic-trade press — no per-year schedule found)
and the escalating-risk rationale for 9%/13%/20%, and `case.json.balance.margin_basis` explicitly
flags "this margin is a designed property of the assumption's chosen values, not an empirical
finding." No `sensitivity_model.py` `FLEX[]`/`sources[]` collision was found either. The linter's
clean read on this specific risk looks correct on inspection — the assumption's basis is shown,
not just a margin/winner asserted.

**This "clean" read was itself wrong, for a reason not visible at the time** — see "A second real
defect found and fixed" above. The guard-comment placement bug meant the linter was not actually
scanning the section it reported clean on.

### Tier 1 — structural (20 checks)
`python3 skills/case-readiness/scripts/tier1_structural.py --case the-deferred-repair --json /tmp/t1.json`
sha256(case.md) = `21003698f581c33020e15019819e4bd812bd84959a114cb3b8ecd024a162b25e`

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | **FAIL (BLOCKER)** | Overview contains numeral `10` not classified as clock time/year and not cleared in `case.json.overview_numerals_cleared[]` |
| T1-03 | PASS | dilemma binary, opens "You are &lt;X&gt;." |
| T1-04 | **FAIL (BLOCKER)** | Challenge 5 not verbatim boilerplate — diverges at char 149 |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | GAP | final standards Appendix D not referenced by letter in Background/Challenges |
| T1-07 | PASS | Appendix labels parsed (9 bulleted) |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | PASS | balance test: both arguments written, margin 13.0% ≤ 20% |
| T1-10 | GAP | `new_coverage[]` empty — reinforcement carve-out applies |
| T1-11 | PASS | learning-goal mutual reachability |
| T1-12 | PASS | tier vs numeric load |
| T1-13 | **FAIL (BLOCKER)** | anchor ladder incomplete; no timed 45-minute Socratic plan; only 1 of 5 Socratic questions parsed |
| T1-14 | **FAIL (BLOCKER)** | CONTINUITY DRIFT — `FACILITATOR.md` margin section still said "Not yet computable — placeholder" |
| T1-15–T1-20 | PASS/GAP (pre-publish expected) | no `published/` dir yet |

**BLOCKER (5):** T1-02, T1-04, T1-13 (×2), T1-14 — see full detail in the original report text
(superseded, all fixed — see "What changed" above).

**GAP (6):** T1-06, T1-10 (carve-out), T1-13 (Socratic question count), T1-14 (orphan `6.0`),
T1-16 (no sha recorded yet), T1-17 (no `cohort_bands[]`).

### Tier 2 — simulated play
NOT RUN (gated behind TIER1_PASS, which had not been reached).

### Tier 3 — human dry-run
NOT RUN (not reachable — case is not yet `PUBLISHED`).
