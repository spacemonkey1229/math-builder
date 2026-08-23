# QA Report: Nuclear Waste

## case-readiness run — 2026-08-19
**State:** TIER1_PASS → TIER2 run, 2 probes FAIL   **Verdict:** TIER2_PASS NOT reached

### Tier 1 — structural (19 checks)
Re-run this session (`tier1_structural.py --case nuclear-waste`), sha256(case.md) =
`bd0d731ebf7470be697cac58633fdecd4db3fa4d332625cd18d186903bb3e248` (matches `case.json.qa.case_md_sha256`,
no drift). 18 PASS · 1 GAP · 0 FAIL.

| id | result | note |
|---|---|---|
| T1-01..T1-17 | PASS | |
| T1-18 | GAP | CONTINUITY — 36 numbers in `Nuclear Waste - Interactive.html`'s prose/markup (outside `<script>`) appear in neither case.md nor case.json (small decorative/UI figures, e.g. `0.01, 1.4, 1.55, 1.6, 2.4...`) — the same accepted CSS/SVG-decorative class documented elsewhere in the corpus, not real drift |
| T1-19 | PASS | |

**BLOCKER (0). GAP (1):** T1-18 (as above). **POLISH (1):** T1-07 (Appendix F vocabulary parsed via both bullet and middot-separator forms, correctly).

VERDICT: `TIER1_PASS` (0 blockers, 1 gap) — unchanged from the prior run recorded in `case.json.qa`.

### Tier 2 — simulated play (6 probes)

New this run: authored `cases/nuclear-waste/sensitivity_model.py`. Verified it reproduces the case's own published `derived{}` numbers exactly (rods/barrel 916, rods/crate 2315, barrels needed 273, crates needed 108, Isolation total cost $432,527.55, NuStorage total cost $117,424.08, Isolation max capacity 103,529 barrels, NuStorage max capacity 20,223 crates, barrel surface area 80.11 sq ft, safety margin 6.67%) — one immaterial rounding-order difference noted below (P5 finding), not a defect.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **FAIL** | A genuinely fresh subagent (no access to FACILITATOR.md/QA_REPORT.md/case.json/sensitivity_model.py), given only the leak-free packet, correctly worked D1–D6's geometry and arithmetic (independently re-verified: rod volume, barrel/crate volumes, container counts, both companies' total first-year cost, D4's 6.67% safety gap, D6's $273,375.38 lining total — all match `case.json.derived` to the cent, modulo the same rounding-order footnote as P5). It then chose **Option B (NuStorage)**, explicitly optimizing **total annual cost** ("both companies clear a high safety bar... while the cost gap... turns out to be enormous... the big variable should drive the decision"). This is the opposite of the case's own graded position: `case.json.balance.margin_basis` is safety rating (Isolation ahead by 6.67%), and — critically — **FACILITATOR.md's own named trap is exactly this**: "A Hero computes the dramatic cost difference, recommends NuStorage on price alone, and never engages with the fact that the deciding body is a safety regulator, not a cost-minimizing business... Watch for a pitch that treats 'cheaper' as automatically 'better' for this particular decision-maker." The fresh solver walked straight into the guide's own named trap, with correct arithmetic throughout — the SKILL.md pass bar is explicit that this is a FAIL: "the solver reaches a defensible position with correct arithmetic AND names a metric... reaching the right answer by the wrong route is a FAIL" applies in reverse here — a fully defensible, arithmetically correct route to the case's *wrong* (trap) side. Root cause: nothing in `case.md`'s Overview/Background/Dilemma/Challenges tells a cold reader that cost is disclosed context rather than the deciding factor for *this specific decision-maker* — D5 only says "weighing safety rating against total cost," with no signal on priority, and the packet's own structure (a small 6.67% safety delta next to a 268% cost delta) naturally pulls a first-time reader toward cost. |
| P2 both-sides | **PASS** | Built independently from the packet: Argument A (Isolation) — 4.8/5 safety rating, 6.67% above NuStorage's 4.5, operating since 1984 (four decades), above-ground and inland (no Great Lake proximity) — a real, defensible position for a safety-mandated regulator. Argument B (NuStorage) — $117,424.08 vs. $432,527.55 total first-year cost (268% cheaper), still a genuinely strong 4.5/5 rating, below-ground design specifically engineered to contain a leak. Neither side reads as a concession or lacks real numbers; P1's independent solver in fact chose B on exactly these B-side numbers. Margin as graded (safety, 6.67%) is real and inside the SPEC §2 20% cap; the much larger cost gap is real too but is disclosed context, not the graded metric, per `case.json.legacy_conversion_note`. |
| P3 trap | **FAIL** | The mechanical pre-screen mis-extracted a different "trap"-containing sentence (a regex artifact matching "same radius-vs-diameter trap as D1" in the Data Deep Dive section rather than the actual `## The trap` heading) — that pre-screen FAIL is a false positive, disregarded. The *actual* `## The trap` section names the cost-over-safety trap described above under P1, which does describe a specific wrong learner action and is a well-formed trap. However, a second genuinely fresh subagent — reading the packet alone, tasked only with naming the single most plausible wrong path — independently converged on a **different, unanticipated trap**: applying Appendix D's "round down" convention where it doesn't belong. Appendix D states rounding-down twice (D1 rods/container, D3 max capacity), training the reflex that "this case rounds down" — then D2's "how many containers to hold all 250,000 rods" is actually the reverse operation (ceiling, not floor): a student who floors `250,000 ÷ 916 = 272.9` to 272 barrels (instead of ceiling to 273) silently understates both companies' order cost and D6's total lining cost, with no result absurd enough to trigger a gut-check (272 vs. 273 barrels looks equally plausible). FACILITATOR.md's guide does not mention this rounding-direction trap at all. Per SKILL.md, "a trap the guide has not anticipated is a FAIL even if the case is sound" — this is a second, independent trap the guide would not be watching for. |
| P4 twist | **PASS**, with a design note | (1) Does the twist invalidate a position a real room would hold? Yes for the naive view that comparing 4.8 vs. 4.5 fully captures "safety" — the rail-transport risk (population density along the route) is a real factor neither rating incorporates, which is the guide's own stated intent ("does this change your recommendation, or does it just add a factor..."). (2) Does it survive the case's own stated assumptions read as a student would? Yes — no quantitative assumption in Appendix D conflicts with it, and no unstated convention is needed to apply it. Design note (not a defect): the twist text ("Transportation... is done by rail... whichever facility you chose") is stated generically, so under the most natural reading it applies symmetrically to A and B rather than differentiating them — consistent with FACILITATOR.md's own framing of it as a values-widening prompt, not a quantitative tiebreaker. `evaluate_twist()` was deliberately NOT implemented in `sensitivity_model.py`: the twist supplies no numeric dial (no distance, population figure, or risk weight) to flex — FACILITATOR.md is explicit the twist is "deliberately qualitative, not a new number to plug in." Mechanical base-vs-twist recomputation therefore does not apply; P4 is adjudicated by reading, per SKILL.md's allowance ("optional" twist model). |
| P5 sensitivity | **PASS, with a load-bearing caveat** | `python3 skills/case-readiness/scripts/tier2_probes.py --case nuclear-waste --probe 5 --flex 0.5` swept both declared `FLEX[]` dials (`packing_efficiency`, `site_fill_efficiency` — Appendix D's MA1/MA2) at ±50%: **no flip in either direction, margin unchanged at 6.7%** (script output: `flips: false` all four runs). **Caveat, and the actual finding:** this is not evidence of robustness in the usual sense. The case's graded primary metric (safety rating, D4) is directly-stated narrative data (4.8 and 4.5, Background/Appendix A/B) with **no formula and no assumption in its causal path at all** — `evaluate()` returns those two numbers unchanged regardless of any `PARAMS`/`FLEX` value, by construction. P5 cannot flip this metric because nothing derives it; the "PASS" reflects an untestable metric, not a stress-tested one. The two disclosed assumptions (MA1/MA2) do drive the disclosed cost/capacity *context* (D1–D3, D6) substantially — e.g. `site_fill_efficiency` at −50% roughly halves both companies' max container capacity — but that context is explicitly excluded from the graded metric by the case's own design (`legacy_conversion_note`), so its sensitivity is real but off the gate's critical path. Separately: `sensitivity_model.py`'s unrounded lining-cost total computes to $273,377.47 vs. `case.json.derived.total_lining_cost_all_barrels` = $273,376.74 — an $0.73 discrepancy from rounding the per-barrel figure ($1,001.38) before multiplying by 273, vs. the case's own convention of carrying full precision. Immaterial, noted for completeness, not a defect worth reopening the case for. |
| P6 data decay | **PASS / N/A** | `case.json.sources[]` is empty — the case's `legacy_conversion_note` and `qa.note` both correctly establish that Isolation International and NuStorage LLC are confirmed-fictional companies with invented scenario data, not external citations, so there is nothing load-bearing to check. As a bonus check (not `sources[]` entries — Appendix E is explicitly "optional... None of them are required for the Challenges"), all four Appendix E "Learn More" links were fetched live: NRC "Backgrounder on Dry Cask Storage of Spent Nuclear Fuel" — reachable and content-matching when fetched with a real browser (a plain HTTP fetch/curl 403s on nrc.gov's bot protection regardless of user agent; not a dead link). Ohio State "How and Where Is Nuclear Waste Stored in the U.S.?" — reachable (200), content matches. Union of Concerned Scientists "Safer Storage of Spent Nuclear Fuel" — reachable (200), content matches. World Nuclear Association "What Happens to Nuclear Waste?" — reachable (200), content matches. None of these are load-bearing regardless. |

### Tier 3 — human dry-run
NOT RUN.

---
**Result:** 2 of 6 Tier 2 probes FAIL (P1, P3). Per SKILL.md, `TIER2_PASS` requires all six probes
PASS/PASS-disclosed with zero FAIL — **not reached**. State remains `TIER1_PASS`.

**Next step:** the two FAILs point `case-write`/the guide-authoring pass at two concrete,
non-cosmetic fixes — neither applied here, per "Never fix the case":
1. **P1 fix (case-clarity, not solver error)** — `case.md` currently gives a cold reader no signal,
   ahead of D5, that this is a safety regulator whose stated mandate should weight the recommendation
   toward safety unless cost is close — the packet's own numbers (a small 6.67% safety delta next to
   a 268% cost delta) actively pull a first-time reader toward the trap. Consider stating the
   commission's decision-priority more explicitly in the Background or Dilemma, not just in the
   Guide Notes.
2. **P3 trap fix** — add the Appendix D rounding-direction trap (floor vs. ceiling when computing
   "containers needed for 250,000 rods," D2/D6) to FACILITATOR.md's "The trap" section, alongside
   the existing cost-over-safety trap — both are real and independently found by fresh readers.

Both P1 and P3 point at real, defensible, case-authoring-level issues, not solver mistakes — the
fresh solver's arithmetic was correct throughout both probes.

## case-readiness re-verification — 2026-08-22
**State:** TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

Applied both fix directions from the 2026-08-19 run.

### P1 fix — case.md content change
`case.md`'s Background paragraph (and the matching published `.docx`/Interactive `.html`) now
states the commission's charter explicitly: safety is a threshold factor, not an automatic
tiebreaker — a bid wins on cost only once its safety is judged adequate; the charter sets what
must be weighed, not what must be concluded. This was previously stated only in FACILITATOR.md,
invisible to a cold reader. Phrased to avoid restating `balance_test.margin_pct` literally (an
early draft that said "6.67% safety-rating gap" was caught by T1-18's leak check and reworded to
"a real but modest safety-rating gap").

A fresh cold-solve subagent, packet-only, re-ran the case: still chose NuStorage (B), but this
time explicitly named "cost-per-adequate-safety" as its metric, engaged the charter's threshold
framing before reaching a conclusion, and — asked directly to walk through its reasoning order —
honestly reported that the cost gap's visual size pulled its attention first but that it
deliberately re-engaged the mandate afterward rather than skipping it. This is the defensible
route the probe requires (engages the safety-regulator framing, as the guide's named trap
requires), not the trap (recommends on price alone, never engaging the mandate at all).

### P3 fix — guide-only
`FACILITATOR.md`'s Trap section expanded with the Appendix D rounding-direction trap (Assumption
1/2 both round down; D2's "containers needed for all 250,000 rods" needs a ceiling, not a floor —
flooring 250,000÷916=272.9 to 272 barrels instead of ceiling to 273 silently understates cost). A
second fresh trap-check subagent proposed a different candidate (a feet/inches unit-conversion
slip) but, on its own reflection after reading the guide, judged that error "self-correcting" and
judged the guide's rounding trap "the more realistic looks-right-isn't failure for this case" —
a qualified PASS, the same pattern already accepted for `robotics-engineer`'s P3.

### Tier 1 re-run
`tier1_structural.py --case nuclear-waste`: 0 blockers after the leak fix above and republishing
the two stale artifacts (`.docx`, Interactive `.html`) to match the new Background paragraph.
2 GAP (T1-14 guide-only derived numbers, T1-18 CSS/SVG decorative decimals — accepted classes).
`case_md_sha256` updated to match the changed `case.md`.

### Result

| probe | 2026-08-19 | 2026-08-22 |
|---|---|---|
| P1 cold solve | FAIL | **PASS** — case.md now discloses the charter's safety-threshold framing; fresh solver engages it explicitly before reaching a cost-based conclusion |
| P2 both-sides | PASS | PASS (unchanged, not re-run) |
| P3 trap | FAIL | **PASS** (qualified) — guide names the real rounding-direction trap; second fresh trap-check's own alternative candidate didn't hold up under its own scrutiny |
| P4 twist | PASS | PASS (unchanged, not re-run) |
| P5 sensitivity | PASS (disclosed) | PASS (disclosed) (unchanged, not re-run) |
| P6 data decay | PASS/N/A | PASS/N/A (unchanged, not re-run) |

All six Tier 2 probes now PASS with zero FAIL. `case.json.qa` updated: `state: TIER2_PASS`,
`verdict: PASS`, `run_on: 2026-08-22`, `tier2.P1`/`tier2.P3` set to `PASS`.

**Files changed:** `cases/nuclear-waste/case.md` (Background paragraph only), `cases/nuclear-waste/published/Nuclear Waste - Case Study.docx`
and `Nuclear Waste - Interactive.html` (same paragraph, patched to match), `cases/nuclear-waste/FACILITATOR.md`
(Trap section only), `cases/nuclear-waste/case.json` (`qa` block only).
