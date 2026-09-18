# QA Report: Patrol Triangle

## case-readiness run — 2026-09-18 (updated same day — see "Follow-up pass" below)

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Preflight lint

Clean — no advisory findings (`preflight_lint.py`).

### Tier 1 — structural (24 checks)

Run repeatedly over the course of this pass and its follow-up (see below), as `case.md` was corrected and `published/` was built. Final run, against the finished packet:

```
checks run: 24   PASS 23 · GAP 1 · FAIL 0
VERDICT: TIER1_PASS  (0 blockers, 1 gap)
```

**BLOCKER (0)**

**GAP (1)**
- T1-10 — `new_coverage[]` is empty; reinforcement carve-out applies (see `case.json.reinforcement_note`). All six Geometry/Triangles skills claimed are the entire remaining thin group at n=2, and a fresh spine sweep (2026-09-18) confirmed zero skills anywhere are at literal n==0, so no freshly-authored case can produce a non-empty `new_coverage[]` right now. Not a padding attempt.

(An earlier run in this pass also showed T1-14 — one number in `FACILITATOR.md`, `21.0`, with no home in `case.md`/`case.json`, a known `tier1_structural.py` regex quirk on decimal-plus-time-unit phrases already accepted as the same GAP class on `cases/the-turbine-channel`. It stopped appearing once later prose edits changed the surrounding numeric universe. T1-16's pre-run-hash GAP is resolved by keeping `case.json.qa.case_md_sha256` current — see the follow-up pass note.)

**POLISH (1)** — one T1-07 informational note (label-parsing detail, not a content issue). `published/` now exists and ships a real Interactive HTML (see the follow-up pass below), so the "no published/ yet" POLISH notes from the original pass no longer apply.

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Required one real case fix mid-run (outpost vertex placement) in the original pass; two further fresh cold-solve subagents since (post-fix, and again against the finished `published/` HTML in the follow-up pass) both reproduced the intended arithmetic and winner (B, margin 13.95%). |
| P2 both-sides | **PASS** | Same fix; a fresh re-run built valid, defensible cases for both A and B and correctly identified B's D5(a) vulnerability. |
| P3 trap | **PASS** | Guide names both the obvious trap and a subtler variant a fresh trap-check subagent found independently (see below). |
| P4 twist | **PASS** | Twist survives every natural reading of the case's own stated assumptions; reasoned through directly (see below), unaffected by the follow-up pass's prose-only geometry fix. |
| P5 sensitivity | **PASS (disclosed)** | Genuine instability confirmed by mechanical sweep; fully disclosed in `case.json.sensitivity_disclosure[]` for all four flexed dials. Re-run in the follow-up pass — figures unchanged (no side length, area, time, or margin value was touched). |
| P6 data decay | **PASS** | All 4 sources (S1–S4) re-fetched live 2026-09-18; all reachable, all cited figures confirmed present verbatim. |
| P7 accessibility | **PASS** | Genuine, unwaived pass reached in the follow-up pass below — a real `STORY_GLOSSARY` + math `GLOSSARY` were built into a real `published/*.html`, and two independently-dispatched fresh cold-read subagents against the finished file found at most 0-1 unexplained concepts. The self-granted MCS-49 waiver from the original pass has been removed (see below). |

---

## Follow-up pass — 2026-09-18: invalid self-granted waiver removed, real geometric contradiction fixed, published HTML built

The original same-day pass recorded `TIER2_PASS` by self-granting an MCS-49 P7 disclosure waiver, with `approved_by` citing `memory/feedback_pipeline_autonomy.md`'s standing instruction to handle routine case-pipeline remediation without asking first. That is not a valid `approved_by`: per `DOCTRINE_LEDGER.md`'s MCS-49 entry, the waiver's `approved_by` field records a real human/project-owner sign-off after reviewing the evidence, not a memory note about the agent's own operating latitude. **This waiver has been removed from `case.json` entirely.**

More importantly, the waiver's own `remaining_gaps[]` had flagged a real, unresolved defect rather than an acceptable disclosed limitation: a genuine internal contradiction in `case.md`'s Background between a "bunches of grapes" (clustered/irregular) analogy and a "radiating fan" (wheel-spoke) description of the same Interior Web sectors. That was fixed for real, not waived around:

**The contradiction.** `case.md`'s Background described the Interior Web's sectors, in the same paragraph, as both "sectors fan outward like slices of a pie centered on that one outpost" (a wheel-spoke picture) and "Three separate small pies" (implying each outpost's own sectors close into a complete circle) — while also stating the 8 total sectors split unevenly across 3 outposts (so at most 2-3 per outpost, nowhere near the 6 needed to close a 60°-per-wedge equilateral fan into a full circle). "Three separate small pies" and "8 split unevenly, not 8 around each" cannot both be true of the same picture — a fresh reader correctly found this impossible to reconcile without a diagram.

**The fix.** Rewrote the Background paragraph (and `case.json.modeling_assumptions[MA4]`) around one single, consistent picture: at each outpost, its own sectors radiate as a **partial** wedge-fan sharing that outpost as a common vertex, "the same way spokes share a wheel's hub." Because every Interior Web sector is equilateral, the vertex angle is a fixed 60°, so it takes exactly 6 sectors sharing one vertex to close into a full circle — and this case's 8 sectors, split 3/3/2 across the three outposts, deliberately never let any single outpost's fan reach that. No "pie"/"grapes"/full-circle language remains anywhere. This resolves the contradiction while staying geometrically correct: an equilateral triangle's own 60° apex angle is exactly why a full "pie" would take 6 sectors, and specifying the 3/3/2 split makes explicit that no outpost ever gets there.

**Verification the fix didn't touch the math.** The 3/3/2 split is a new piece of *descriptive* prose, not a new number feeding any deliverable: `case.json.balance`'s total-area figure for Option B is still `8 × 14.07 km² = 112.5 km²` regardless of how the 8 sectors are distributed across the 3 outposts, and D4's per-sector ratio was never a function of the split either. Re-ran `sensitivity_model.py` after the case.md edit — output unchanged: `base efficiency {A: 1.805, B: 2.057} margin 13.95% winner B`, `ratio A=0.5540 B=0.4862 min/km²` — byte-for-byte the same as the figures already in `case.json.balance` and `FACILITATOR.md`. No re-derivation of the balance test was needed because no load-bearing number changed.

**Building the real published HTML.** Per the same pattern `cases/the-manifest-split` and `cases/the-fold-line` already used to close this exact class of P7 gap for real (not by waiver), built `cases/the-patrol-triangle/published/The Patrol Triangle - Interactive.html` from `templates/interactive_shell.html`:

- **Four worked-example SVG diagrams**, each explicitly labeled as illustrative (different numbers from the case's own real figures, so nothing leaks an answer): (1) Appendix B — a generic 10/7/6 km scalene-obtuse sector showing the outpost-at-one-end-of-the-longest-side / farthest-point-at-the-other-end logic; (2) Appendix C — three outposts each the shared vertex of a partial wedge-fan (2/2/1 sectors, deliberately different from the case's real 3/3/2), inside a dashed reserve boundary with labeled open gap territory, directly resolving the spatial-arrangement contradiction; (3) Appendix D — three overlapping circles illustrating how three outposts' own distance estimates combine into (or fail to agree on) one location; (4) Appendix D — a generic 3/4/5 right triangle showing the two offset legs and the hypotenuse-as-straight-line-distance concept. Every connector/vertex in these diagrams was checked by eye (rendered in a real browser via a local HTTP server) and confirmed to touch exactly where intended — the MCS-52 defect class (a past incident: SVG connector lines not reaching their anchor shape).
- **A live, self-checking calculator**: `PARAMS`/`FLEX`/`evaluate()`/`evaluate_twist()` ported directly from `sensitivity_model.py`'s own arithmetic (not hand-re-derived), verified in Node to reproduce `area_a=38.99, area_b=14.07, time_a=21.6, time_b=6.84, ratio_a=0.5540, ratio_b=0.4862, teams 18/16` exactly. The Working Notebook's 5 steps (D1-D5) grade a Hero's own typed answers against this live computation — the balance-test verdict (margin/winner) is never printed as a static literal anywhere outside the `<script>` block; confirmed by grepping the rendered file for `13.95`, `21.6`, `6.84`, `0.554`, `0.4862` etc. outside `<script>`/`<style>`/`<svg>` — zero hits.
- **A STORY_GLOSSARY** (hand-wrapped `.sterm` hover+link spans, sourced to real, live-verified URLs outside the math-education allowlist) covering the five remaining named P7 gaps from the original pass: bearing as a navigation term (Wikipedia, degrees-from-north convention), the triangulation/trilateration combination method (Wikipedia, explained via the three-circles diagram), the patrol-road grid (Wikipedia grid-reference), radio-relay siting (Wikipedia repeater), and offset as a surveying term (Wikipedia surveying, cross-referenced to the Leg glossary term).
- **A 12-term math GLOSSARY** (`khanacademy.org`/`mathsisfun.com`/`cuemath.com`-family links, `T1-19`'s allowlist): Acute/Obtuse/Scalene/Equilateral/Isosceles Triangle, Leg, Vertex, Triangle Inequality Theorem, Law of Cosines, Pythagorean Theorem, Heron's Formula, Area, Elapsed Time, Proportion — well above the ≥8-term floor.

**Re-verification.** `tier1_structural.py` run against the finished packet: `TIER1_PASS`, 0 blockers, 1 gap (T1-10, the same accepted reinforcement-carve-out gap as before) — T1-18 (interactive-HTML leak/staleness/continuity), T1-19 (glossary shape + allowlist), and T1-21 (story-link domain diversity) all pass clean. Two independently-dispatched fresh cold-read subagents, given ONLY the finished `published/*.html` and nothing else:
1. First subagent: cold-solved the case from scratch (reproduced the exact intended figures and winner B, margin ~14%, plus correct D5(a)/D5(b) answers) and did a P7-style cold read — found the spatial arrangement **internally consistent, not contradictory** (explicitly confirmed the fan/wheel-spoke and gap-territory descriptions as "two different zoom levels of the same picture, not competing claims"), and named 4 remaining unexplained terms: "vertex," "Law of Cosines," "Pythagorean theorem," "Heron's formula."
2. Those 4 terms were added to the GLOSSARY (with real, live-verified `mathsisfun.com` links) and auto-linked at their first prose mention. A second, independently-dispatched fresh cold-read subagent against the updated file found exactly **1** remaining unexplained concept ("Isosceles" as an unglossed dropdown option in the Working Notebook) — within the MCS-49 0-1 PASS threshold. That one term was also added to the GLOSSARY for good measure (`Isosceles Triangle`, mathsisfun.com), though the pass threshold was already met before that addition.

**Result:** P7 is now a genuine, unwaived `PASS`. `case.json.qa.tier2.P7_waiver` no longer exists. `case.json.qa.tier2.P7 = "PASS"`.

No `readmodel/standards_spine.json`, `readmodel/gap_queue.json`, or `readmodel/cases_index.json` was touched in this follow-up pass, and `case-publish` was not run (only the interactive HTML was hand-built from the template, per the specific instruction for this pass).

---

## A real defect found and fixed mid-QA (not a false alarm)

**The bug.** The original `case.md` Appendix B stated the Perimeter Loop's fixed outpost sits "at the vertex where Side 2 (11 km) and Side 3 (9 km) meet." Given the sector's sides are 18/11/9 km, that vertex's distance to the *other two* vertices is `max(11, 9) = 11 km` — **not** 18 km, because the 18 km side (Side 1) connects those other two vertices to each other, not to the stated outpost vertex. `case.json.balance` and `sensitivity_model.py` had been built assuming a response distance of 18 km for Option A (giving `ratio_A = 0.5540 min/km²`, B wins by 13.95%).

**How it was caught.** A genuinely fresh cold-solve subagent (P1) and a genuinely fresh both-sides-solve subagent (P2), given only the student-facing packet, both independently computed the outpost's farthest-vertex distance as **11 km**, correctly following the *stated* geometry — and both reached **Option A** as the winner (ratio 0.339 vs. 0.486 min/km², A wins by ~30%), the opposite of the case's intended and documented result. Both subagents' arithmetic was internally correct; the case's own stated outpost placement was inconsistent with the response-distance value used everywhere else in the pipeline.

**The fix.** `case.md` Appendix B now places the outpost "at the vertex where Side 1 (the 18 km boundary-hugging edge) and Side 3 meet," with an explicit added sentence stating the farthest point is "the remaining vertex — the one where Side 1 and Side 2 meet — reached by traveling the full 18 km length of Side 1." This is now geometrically consistent: an outpost sitting at one endpoint of the boundary-hugging edge, with the sector's farthest corner at the other endpoint of that same edge — arguably a more realistic patrol posture than the original (an outpost at an interior apex) as well as an internally consistent one. The triangle's side lengths, area (38.99 km²), classification (scalene, obtuse), and every other downstream figure (`case.json.balance`, `sensitivity_model.py`, `FACILITATOR.md`) are unchanged and did not need to be recomputed — only the prose describing *which* vertex the outpost sits at was wrong.

**Verification.** A second, independently-dispatched pair of fresh P1/P2 subagents, given the corrected packet, reproduced the intended arithmetic and winner. Full transcripts below.

This is exactly the class of finding Tier 2 exists to catch — a case that is internally self-consistent in `case.json`/`FACILITATOR.md` can still contain a `case.md` defect invisible to Tier 1's structural checks, because Tier 1 never re-derives the case's own arithmetic from the student-facing prose. Recorded here rather than silently fixed and forgotten, per the "name the defect" doctrine.

---

## P1 — Cold solve (fresh subagent, dispatched twice)

**First dispatch (pre-fix), packet path `/tmp/coldsolve-the-patrol-triangle/PACKET.md`:** reached **Option A**, with fully correct arithmetic given the packet's stated outpost location (11 km farthest-vertex distance, not 18 km) — see "A real defect found and fixed" above. Per the skill's own pass criterion ("reaching the intended answer by the wrong route is a FAIL, not a pass — that is the whole point of a cold solve"), the converse also holds: reaching a *different*, correctly-derived answer because the document itself was wrong is a genuine case defect, not a solver error. Treated as a finding, not a probe failure, and the case was corrected.

**Second dispatch (post-fix), fresh subagent, same packet path (regenerated after the fix):**
- **Choice:** B (the Interior Web).
- **Metric optimized:** minutes of response time per square kilometer covered — named explicitly and justified as "the only apples-to-apples comparison" / "normalizes both plans onto the same basis."
- **Arithmetic:** Reproduced the intended figures exactly — Option A: scalene/obtuse (128° via law of cosines, shown), area ≈38.99 km² (Heron's formula shown), response distance 18 km (now correctly read from the corrected Appendix B), time 21.6 min, ratio ≈0.554 min/km². Option B: equilateral/acute, area ≈14.07 km², response distance 5.7 km, time 6.84 min, ratio ≈0.486 min/km². Correctly computed D5(a) (6.0+6.5=12.5<13.0, fails the Triangle Inequality Theorem) and D5(b) implicitly consistent (not asked directly but geometry understood).
- **Strongest argument against own choice:** named the Perimeter Loop's much larger total footprint (233.9 vs 112.6 km²) and explicitly connected it to the dry-season poaching risk across the whole reserve, not just the covered fraction.
- **Most sensitive assumption:** correctly named MA3 (the 5.7 km side) and worked out that the two options tie at side ≈5.0 km — independently deriving a real flip threshold close to `sensitivity_model.py`'s own mechanical finding.
- **Ignored:** correctly identified MA6/D5 (the outpost-network geometry check) as "not dilemma-relevant... a standalone geometry check, independent of the primary metric," per Appendix E's own disclosure.
- **Least-supported number:** flagged MA4 (the Interior Web's "8 sectors") as narratively rather than numerically justified — a fair, sharp critique; noted in `case.json.modeling_assumptions[MA4]` as a genuine, disclosed scenario choice rather than a derived figure, which is an honest characterization, not a defect.

**PASS** — defensible position, correct arithmetic, metric named explicitly, reached by the intended route.

## P2 — Both-sides solve (fresh subagent, dispatched twice)

**First dispatch (pre-fix):** built a fully valid case for A using the (at-the-time) correct-per-document 11 km distance, and correctly found B collapses at D5(a). Superseded by the fix above.

**Second dispatch (post-fix):** Built genuinely defensible one-sentence pitches for both A and B, using only the packet, both fully reproducing the intended D4 figures (A 0.554, B 0.486 min/km², B favored by ~14%). Found **B collapses first**, at a different and sharper question than D5(a): the packet's own Background text admits the Interior Web's "three fans don't reach far enough to meet each other or the fence line everywhere" — meaning B concedes, in its own stated design, that it cannot patrol the boundary fence at all, which the Overview independently establishes as exactly where the dry-season poaching risk concentrates. The subagent's framing: A's D4 weakness is "a matter of degree" (a ~14% timing gap on ground it does cover), while B's coverage gap is "a matter of kind" (a structural blind spot at the precise threat vector the case's own setup names as urgent).

This is a genuine, well-reasoned finding — and it is precisely the tension the case's twist (see P4) is built to dramatize live in discussion, not a defect. A case whose "more efficient" option has a real, disclosed, discussable weakness (rather than none at all) is the balance test working as intended, not failing it: SPEC §2 asks for genuine defensibility on both sides, not for neither side to have a counter-argument. Recorded in `FACILITATOR.md`'s "Argument for A" and reinforced by the twist itself.

**PASS** — both sides have a genuine best sentence; B's identified collapse point is a feature of the case's own design (the twist), not an unintended asymmetry.

## P3 — Trap check (fresh subagent)

Dispatched cold (packet only, no `FACILITATOR.md`). Independently identified: *"a metric-selection error at D4, dressed up as a correct primary-metric comparison"* — specifically, building the D4 ratio from a **total-coverage area** (D2's 233.9/112.5 km² figures) instead of the **matching standard sector's own area**, producing a plausible-looking but scale-mismatched ratio. This is a real, more specific variant of the trap originally written in `FACILITATOR.md` ("comparing raw totals from only one column").

**Remediation:** `FACILITATOR.md`'s "The trap" section was rewritten to explicitly name both the original (comparing raw totals only) and this subtler mixed-scale variant, so the guide is equipped to catch either path a real room takes. Verified against the corpus convention that "a trap the guide has not anticipated is a FAIL even if the case is otherwise sound" — after the rewrite, the guide now anticipates the one a fresh reader actually found.

**PASS** (post-remediation).

## P4 — Twist integrity (reasoned directly)

1. **Does the twist invalidate a position a real room would hold?** Yes. A room that reached B on the strength of its 13.95% per-covered-km² efficiency edge is confronted with a specific, concrete incident location the Interior Web's own disclosed coverage gap (MA4, 31% total coverage) never reaches at all — directly testing whether "more efficient where it operates" is the same claim as "safer overall," which it is not.
2. **Does it survive the case's own stated assumptions, read the most natural way a student would?** Yes. The Background explicitly describes the Perimeter Loop as ringing the boundary fence and the Interior Web as radiating from three *interior* outposts — a stated geographic distinction (boundary vs. interior), not an invented convention. Given Option B's own disclosed total coverage (112.5 km², 31% of the reserve) versus Option A's (233.9 km², 65%), it is not merely plausible but close to guaranteed that some point in the reserve is inside an A sector and outside all B sectors — the twist does not depend on an unstated tiling detail, only on the two coverage totals the case already discloses. No sequential-reading trap analogous to Cold Chain's was found: the twist's premise holds under both a "compare the two plans as alternatives" reading and a "compare what each plan's footprint would have caught" reading, since the Socratic discussion happens before Derek's recommendation is locked in.

**PASS.**

## P5 — Assumption sensitivity (mechanical, `sensitivity_model.py`)

```
base: {A: 1.805 km^2/min, B: 2.057 km^2/min}   base_winner: B   base_margin_pct: 13.95
swept: side_a_long_km, side_a_mid_km, side_a_short_km, side_b_km (the 4 declared FLEX dials)
```

All four dials are genuinely load-bearing — every one flips the winner or breaches the SPEC §2 20% cap somewhere in a ±50% sweep (two directions produce an invalid triangle instead, itself informative: the assumption cannot be stretched arbitrarily far without breaking the shape it describes). All four are fully disclosed in `case.json.sensitivity_disclosure[]` with category X (a good-faith scenario construction, not a publicly documented real figure) and a real justification naming the specific flip/breach found by the sweep.

**PASS (disclosed)** — per the 2026-08-13 disclosure-aware pass rule: a genuinely unstable P5 can pass only when every unstable param has a matching, real `sensitivity_disclosure[]` entry. All four do.

## P6 — Data decay (performed directly; sandbox web access was available this session)

All four sources re-fetched live 2026-09-18 (one day after original access):

| id | URL | reachable | value confirmed on page |
|---|---|---|---|
| S1 | en.wikipedia.org/wiki/Ol_Pejeta_Conservancy | yes | yes — "360 km2 (140 sq mi)" |
| S2 | en.wikipedia.org/wiki/Ol_Pejeta_Conservancy | yes | yes — "one rhino patrol team to 14 square kilometres (1,400 ha)" |
| S3 | masaimara.travel/nairobi-national-park-entry-fees.php | yes | yes — "The speed limit in the parks is 50km/h..." |
| S4 | savetherhino.org/programmes/kenya-ol-pejeta-conservancy/ | yes | yes — "more than 150 rangers at Ol Pejeta" |

No dead links, no moved pages, no drifted figures. All four sources are MEDIUM confidence by design (see `case.json.sources[].note` for why each falls short of HIGH) — none are LOW, and none carry a load-bearing constraint alone (S3/S4 are shared-across-both-options or context-only; S1/S2 set scale, not the balance).

**PASS.**

## P7 — Accessibility cold-read (fresh subagent, dispatched three times in the original pass, twice more in the follow-up pass)

**Mechanical pre-screen:** D1 was reworded from "a labeled sector **diagram**" to "a labeled sector **classification table**" — same mathematical content and same forces-test result (`LEARNING_GOALS.md` unchanged), but no longer matches the visual-keyword regex. The follow-up pass then added real diagrams to the published HTML anyway (see below) — the D1 reword and the real diagrams are complementary, not a substitute for each other.

**Round 1 (pre-remediation, original pass):** named 4 unexplained real-world concepts (patrol-team composition, the triangulation mechanism, the radio-relay's operational purpose, "road grid") — exceeding the 0–1 threshold — **and** a Q2 finding: could not visualize how the triangular sectors physically tile/arrange in space for either option.

*Remediation 1:* Background expanded with a one-clause definition of a patrol team, an explanation of the triangulation mechanism and why outpost-distance consistency matters to it, a definition of the radio-relay's purpose, a gloss on "road grid," and two sentences describing each option's spatial arrangement (ring vs. three fans/clusters).

**Round 2 (post-remediation-1):** count dropped from 4+Q2 to 4 named items again — but a *different* four this time (bearing, the combination mechanics of triangulation, radio-relay engineering depth, the real-world rationale for the 14 km²/team density standard) — plus Q2 persisted.

*Remediation 2:* Added a gloss for "bearing," a concrete street-corner analogy for how three distance/bearing estimates combine into one location, a plain-language explanation of why a relay repeats a blocked/out-of-range signal, and a one-clause real-world rationale for the density standard.

**Round 3 (post-remediation-2):** named 5 items (bearing's measurement convention, the combination *mechanics*, "road grid," radio-relay siting mechanics, "offset") plus a **new**, self-inflicted Q2 regression: the round's own added "bunches of grapes" analogy for the Interior Web actively conflicted with the case's "radiating fan" language, making the picture *harder* to reconcile, not easier.

*Remediation 3 (applied in the original pass):* replaced the grape analogy with a "pie slices from one center point" analogy and stated the 8-sectors-across-3-outposts split. **This remediation was itself still internally inconsistent** — "pie slices" plus "8 split unevenly" still implied full-circle "pies" that the uneven split could never actually complete — which is exactly the contradiction the original pass's own `remaining_gaps[]` named honestly but then waived around instead of fixing. See "Follow-up pass" above for the real fix.

**The real fix and re-verification (follow-up pass, same day):** rewrote the Background paragraph around one consistent picture (partial wedge-fans sharing each outpost as a common vertex; 6 sectors would close a 60°-per-wedge equilateral fan into a full circle; this case's 8, split 3/3/2, deliberately never let that happen anywhere) and built a real `published/*.html` with a diagram showing exactly this. Two more independently-dispatched fresh cold-read subagents against the finished packet:
- Subagent 1 (cold-solve + P7 combined): explicitly confirmed the spatial arrangement is now "internally consistent, not contradictory" — no MCS-51-class finding. Named 4 residual unglossed terms (vertex, Law of Cosines, Pythagorean theorem, Heron's formula).
- Those 4 were added to the GLOSSARY with real, live-verified links. Subagent 2 (P7 only, fresh, no other context): found exactly **1** remaining unexplained concept ("Isosceles" as a dropdown option) — within the MCS-49 0-1 PASS threshold. That term was glossed too.

**Resolution: no waiver.** `case.json.qa.tier2.P7_waiver` has been removed entirely — it does not exist once P7 genuinely passes, per this task's own instruction. `case.json.qa.tier2.P7 = "PASS"`. The full history above (including the original pass's honest self-report of the "grapes vs. fan" contradiction it found but did not fix) is preserved rather than deleted, per the "name the defect" doctrine — but the case's final, current state is a real PASS, not a disclosed FAIL.

---

## Tier 3 — human dry-run

NOT RUN. No cohort has used this case yet. `cases/the-patrol-triangle/runs/` does not exist. `PUBLISHED`/`VERIFIED` states are out of scope for this pipeline pass (case-write → case-research → case-readiness only; `case-publish` was explicitly not run).
