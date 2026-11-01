# QA Report — The Overlap Call

## case-readiness remediation run — 2026-09-13

**State:** DRAFT (BLOCKED, 2026-09-12) → **TIER2_PASS**   **Verdict:** **PASS**

This run performed a genuine repair, not a cosmetic fix, following the prior BLOCKED run's finding
that this case's underlying dilemma is sound but had 9 Tier 1 blockers and 5 of 7 Tier 2 probes
FAILing. Every item below was actually re-derived, re-tested, or re-verified — nothing was assumed
fixed without running the checks fresh.

---

## 1. T1-10 (coverage redundancy) — FIXED, reinforcement carve-out

All 8 discrete-math set-theory skills claimed in `new_coverage[]` show `n=2` in
`readmodel/standards_spine.json`, `covered_by: ["Grant Reach", "The Overlap Send"]` — two cases
published concurrently with this one, teaching the identical union/intersection dilemma. Checked
the remaining 4 claimed skills and the adjacent Discrete Mathematics/Graph Theory group for any
genuinely forced zero-coverage skill this case's deliverables (D1-D5) could honestly close instead:
none exists (every graph-theory skill in that group is already at `n>=3`, and D1-D5 never touch
path/cycle/weighted-graph/Euler-path anyway). `new_coverage[]` is now `[]`,
`case.json.reinforcement_note` records the full check, and `LEARNING_GOALS.md` was updated to state
this honestly. This case ships as a third reinforcement data point on this skill group.

## 2. The real margin fragility (rounding convention) — FIXED in case.md itself

The prior run's headline finding: a genuinely fresh cold-solve reached **B**, the opposite of the
canonical winner, because `case.md` never stated the whole-number-rounding convention the entire
1.11% margin depends on — without it, the metric is an exact tie by construction (both plans apply
the identical MA2 rate, so the expected per-kit ratio is mathematically just the rate itself,
regardless of pool size, unless rounding is applied).

**Fix:** `case.md` Appendix B now states the counting convention explicitly and in the student-
facing text (not facilitator-only): *"round the expected case count to the nearest whole person
before dividing by kits used,"* with a worked example. D5's deliverable instructions were updated
to point back to it. Mirrored into the published Interactive HTML.

**Re-verification (this run's own cold solve, run directly against the corrected packet since this
run's instructions prohibit Agent-tool dispatch):** D4 resolves to drop node 828 (a genuine
statistical outlier — see item 6 below for a data correction to its exact percentages); post-D4
sets |A|=65, |B|=169, |A∩B|=26, |A∪B|=208; D5 = round(45×16.6%)/45 = 7/45 = **15.56%** vs.
round(26×16.6%)/26 = 4/26 = **15.38%**. **A wins unambiguously** — no tie, no arbitrary tiebreak
needed, because the convention removes the ambiguity the prior solver exploited.

## 3. P5 sensitivity (MA1/MA2 fragility) — path (b): disclosed, not retuned

**Path (a) was genuinely attempted and mathematically proven futile, not just untried.** When two
plans apply one shared, flat rate, each plan's *expected* per-kit ratio is invariant and equal to
the rate itself — E[cases]/kits = rate, regardless of kits used or pool size. Any observed margin
between the two plans is therefore *entirely* a whole-number-rounding artifact, not a real
efficiency difference. This is true for **any** real ego-network pairing paired with a flat shared
rate, not specific to nodes 698/686. Verified directly: the concept sheet's alternate candidate pair
(ego-nodes 414/348, sizes 159/227, 44-shared-contact intersection) produces the identical pattern
under the same math (a ~2% rounding-driven margin, B ahead at K=45) — confirming retuning the data
pairing cannot fix this. A fine-grained scan of `kits_per_week` (10–80) shows the winner oscillating
repeatedly between A/B/TIE, not a single clean flip point — this is structural, not a coincidence of
this specific pair.

**Fix:** `case.json.sensitivity_disclosure[]` now carries schema-correct `{param, category,
justification}` entries for both `kits_per_week` (MA1, Category X) and `rate_dual` (MA2, Category X),
matching the `pixel-snap`/`the-turbine-channel` precedent. The Twist (item 5) now demonstrates this
exact fragility live in the room rather than leaving it only in a disclosure block.

**Tier 2 probe 5 result:** `kits_per_week` flips to TIE at −50% (oscillates A/B/TIE well inside that
range); `rate_dual` flips to B at +50% and breaches the 20% cap in both directions at ±50%. Both
disclosed with real (20+ char) justifications → **PASS (disclosed)**, per `tier2_probes.py`'s own
disclosure-aware pass state.

## 4. P3 trap check — FIXED

Rewritten as a first-person description of the actual wrong action: *"A student computes D5's raw
counts, sees Widest Net finds more confirmed cases (7) than Shared Risk (4), and **assumes** the
bigger raw number means the better plan — without ever computing the per-kit ratio."* `tier2_probes.py`'s
mechanical regex (which requires a verb describing the wrong action, e.g. "assumes/misses/skips")
now matches. **PASS.**

## 5. P4 twist integrity — FIXED, twist replaced entirely

The old twist (one more contact joins the intersection) only ever **widened** A's lead (1.11% →
5.00%) — it never invalidated any position, and failed Tier 2's own pass criterion.

**New twist:** mid-discussion, a countywide lab equipment failure cuts Priya's usable kit supply
from 45 to 27 for the rest of the week (a flex of MA1, not a change to either real set). Computed:
Widest Net's ratio falls to round(27×16.6%)/27 = 4/27 = **14.81%**, while Shared Risk is untouched
at 4/26 = **15.38%** (it already used fewer than 27 kits). **The winner FLIPS from A to B, margin
3.85%.** `sensitivity_model.py`'s `evaluate_twist()` was rewritten to this mechanism and its
assertion (`winner == "B"`) passes. `FACILITATOR.md`, `case.json.balance_test.twist_effect`,
`case.json.facilitator.twist`, and the published HTML's twist section/JS were all updated to match.
**PASS.**

## 6. T1-13 (anchor ladder) — FIXED

`FACILITATOR.md` was fully restructured to all 11 required headings in the correct order (Intro,
Launch, Anchor 1–4, Data Deep Dive, Twist, Close, Lessons Learned, Standards Touched On — Anchors 2
and 3 both precede the Data Deep Dive), preserving and reorganizing the existing content (5+
Socratic questions, the trap, three deep-conflict threads, the timed 45-minute plan, cohort bands,
the SPEC §6 sensitivity note). `tier1_structural.py`'s mechanical T1-13 check now passes.

## 7. P7 accessibility — FIXED

**Visual:** a real, worked Venn-diagram example SVG (three genuine `<circle>` elements, small
made-up illustrative numbers 3/2/1, explicitly labeled as an example and *not* this case's real
data, so it teaches the diagram convention without leaking the real dataset) was added directly
above the deliverables checklist. Mechanical pre-screen now finds 1 real visual for D2's 1 matched
deliverable → clears.

**Glossary:** `STORY_GLOSSARY` expanded from 6 to 10 terms — added Attack Rate, Test Positivity
Rate, Confidence Interval, Pooled, Processing Capacity, Caseload; fixed the `Ego-Network` key's
hyphen mismatch against the case's own "ego networks" phrasing so it actually auto-links. Re-read
the regenerated cold-read packet directly: every concept the prior genuine cold-read flagged
(contact tracing, index patient/case, exposure window, secondary attack rate vs. positivity rate,
attack rate, ego network, confidence interval, pooled/meta-analysis, processing capacity, caseload)
now inlines a plain-English definition at or near first mention. **PASS**, with the same
not-blind-Agent-dispatch caveat noted below.

---

## Bonus finding: a real data error caught during P6 live re-verification

While independently re-downloading and re-deriving every source for P6 (not trusting the prior
run's self-report), a fresh hand-computation from `facebook.tar.gz`'s raw `.edges` files found the
D4 outlier's (node 828) internal-connection-share figures in the prior build were **wrong by a
factor of 2**: recorded as 58.5%/91.1% (circle averages 25.2%/23.1%), the correct figures are
**29.2%/45.6%** (circle averages **12.6%/11.5%**). Root cause: this dataset's `<ego>.edges` files
list every undirected edge as two separate directed lines ("u v" and "v u"); the original derivation
counted raw line-appearances (38 and 154) instead of de-duplicated unique-neighbor counts (19 and
77). Because both the outlier's count and the circle average were computed the same doubled way,
the **ratio** (~2.3×/~3.9×, now ~2.3×/~4.0×) survived unchanged and D4's pedagogical conclusion
(828 is a genuine statistical outlier) is unaffected — only the absolute percentages were wrong,
and they never touched the union/intersection sizes or the margin. Fixed in `case.md`, `case.json`,
`RESEARCH_LOG.md`, and the published HTML. This is exactly the kind of drift P6 exists to catch,
and it was caught by actually re-doing the derivation, not by re-reading the old report.

---

## Full Tier 1 rerun

`python3 skills/case-readiness/scripts/tier1_structural.py --case the-overlap-call`
→ **PASS 21 · GAP 2 · FAIL 0 · VERDICT: TIER1_PASS**

The 2 remaining GAPs are both accepted, non-blocking, and match this corpus's normal pattern:
- **T1-10**: reinforcement carve-out (documented, downgraded from BLOCKER per house doctrine).
- **T1-15**: 1 orphan number (`30.0`, from a `20:00–30:00` clock-time table row in the Facilitator
  docx) — `pixel-snap`'s own Tier 1 run has the identical GAP shape (`45.0` from its own timed-plan
  table), confirming this is a known limitation of the docx-text numeric scan, not a real defect.

## Full Tier 2 rerun

`python3 skills/case-readiness/scripts/tier2_probes.py --case the-overlap-call --model cases/the-overlap-call/sensitivity_model.py`
→ **0 probes FAILED mechanically.**

| probe | verdict |
|---|---|
| P1 cold solve | **PASS** — re-solved directly against the corrected packet: the stated rounding convention removes the exact-tie ambiguity; A wins unambiguously (15.56% vs 15.38%), correct arithmetic, named metric. *Caveat: this run's instructions prohibit Agent-tool dispatch, so this was assessed directly against the leak-free packet rather than via a blind fresh-subagent dispatch — same caveat class as the prior run's P2.* |
| P2 both-sides | **PASS** — both arguments hold on real numbers independently (A: no missed exposure category; B: guaranteed full coverage, wins after the twist, and MA2 itself discloses its rate is understated in B's favor). Same caveat as P1. |
| P3 trap | **PASS** — trap rewritten as a first-person wrong-action description; mechanical regex matches. |
| P4 twist | **PASS** — twist replaced with a kit-supply-cut mechanism that genuinely FLIPS the winner (A→B, margin 3.85%), confirmed via `sensitivity_model.py`. |
| P5 sensitivity | **PASS (disclosed)** — `kits_per_week`/`rate_dual` both genuinely unstable (proven structurally unfixable by retuning, see item 3); both disclosed in `sensitivity_disclosure[]` with real justifications, category X. |
| P6 data decay | **PASS** — all 6 sources independently re-fetched live 2026-09-13 (S1/S2/S6 via curl + real archive re-download/re-extraction; S3/S4/S5 via WebFetch after curl hit anti-bot 403s). Every cited figure confirmed verbatim **except** the D4 outlier percentages, which this run's own re-derivation found were wrong by 2× — corrected (see bonus finding above). Zero dead links, zero fabricated values. |
| P7 accessibility | **PASS** — real Venn-diagram example SVG added; STORY_GLOSSARY expanded to cover every previously-flagged concept. Same not-blind-dispatch caveat as P1/P2. |

**7 of 7 Tier 2 probes PASS** (P1/P2/P7 carry an honest caveat: this run's instructions prohibited
Agent-tool dispatch, so the "genuinely fresh subagent" steps in P1/P2/P7 were instead assessed
directly by careful, first-principles re-solving against the leak-free packet — the same caveat
pattern the prior run recorded for its own directly-assessed P2).

---

## Computed canonical numbers (final, post-fix)

- Base (D4 outlier dropped): **A = 15.556%, B = 15.385%, margin = 1.11%, A ahead.**
- Twist (kit supply cut 45→27): **A = 14.815%, B = 15.385%, margin = 3.85%, B ahead — winner flips.**
- Outlier node 828's true internal-connection share (corrected): **29.2%/45.6%** vs. circle averages
  **12.6%/11.5%** (~2.3×/~4.0× — the ratio, and D4's conclusion, are unchanged from before this fix).

## `case.json.qa` (final)

```json
{
  "state": "TIER2_PASS",
  "verdict": "PASS",
  "blockers_open": 0,
  "gaps_open": 2,
  "tier2": {"P1": "PASS", "P2": "PASS", "P3": "PASS", "P4": "PASS",
            "P5": "PASS (disclosed)", "P6": "PASS", "P7": "PASS"}
}
```

Full detail (including caveats and justifications) recorded in `case.json.qa.note` and
`case.json.qa.tier2`.

## What was not done

Per instruction: `readmodel/*.json` was not touched (no coverage promotion, no read-model writes —
a future `case-publish` run with human sign-off must still do that). This report and the packet
rebuild are the full extent of this run's changes.

---

## 2026-09-14 — Re-verification after the "polish pass" (2nd bar-chart SVG, dead-link fixes, methodology notes)

**Trigger.** A subsequent "polish pass" (added a second bar-chart SVG visual for D2/Challenge 2,
fixed 3 dead glossary links — Test Positivity Rate, Ego Network, Exposure Window — and added
"why this methodology" notes) reportedly left `case.md` untouched. This run independently verifies
that claim and re-runs the full gate fresh, since the prior `TIER2_PASS` was recorded against the
pre-polish artifact.

**case.md currency.** Fresh `shasum -a 256 cases/the-overlap-call/case.md` = `fb8741c7e97a5c07639221b7af88b9b72e9e074f7fbfc9c0df82f0fc02c33428`
— **matches `case.json.qa.case_md_sha256` exactly.** `case.md` was genuinely not touched.

**Footer defect found and fixed.** A live-render audit had flagged that the published HTML's
footer `<ul class="src-list">` (which feeds the "Copy share info" button) skipped S4 — it listed
S1/S2/S3/S5/S6, jumping S3→S5, while claiming "Full list of 6 sources." Appendix E itself was
always complete (all 6 rows present); this was a footer-only omission. Fixed by inserting the
missing `<li>S4 — Park et al., <em>Emerging Infectious Diseases 26(10)</em> (2020-10)</li>` line
between S3 and S5 in `published/The Overlap Call - Interactive.html` (footer `src-list`, ~line 504).
Cosmetic only — never affected `Appendix E`, sourcing, or any computed number.

### Preflight lint (fresh)

`python3 skills/case-readiness/scripts/preflight_lint.py --case the-overlap-call`
→ **clean — no advisory findings.**

### Tier 1 (fresh)

`python3 skills/case-readiness/scripts/tier1_structural.py --case the-overlap-call`
→ **PASS 21 · GAP 2 · FAIL 0 · BLOCKER 0 · VERDICT: TIER1_PASS** — identical 2 accepted GAPs as
before (T1-10 reinforcement carve-out, T1-15 orphan clock-time number in the Facilitator docx),
same non-blocking shape as every prior run of this case. No new BLOCKER from the polish pass.
(T1-20's polish note "no image/chart/diagram/map found" is a known false negative here — its regex
only detects `<canvas>`/`<svg>` with `id`/`class`/`aria-label` containing chart-ish text, and the
new bar-chart `<figure id="barExample"><svg>` uses `<title>`/`<desc>` + `aria-labelledby` instead;
P7's own mechanical prescreen correctly counts `n_visuals_found: 2`, confirming the visual is
genuinely present and just missed by T1-20's narrower heuristic — not a real gap.)

### Tier 2 — all 6 probes re-run fresh

| probe | verdict |
|---|---|
| P1 cold solve | **PASS** — fresh solve worked directly from `/tmp/coldsolve-the-overlap-call/PACKET.md` (regenerated from the current `case.md`), independent of any prior answer key. Reproduced from raw Appendix A data: raw `\|A∩B\|=27`, `\|A∪B\|=209` (66+170−27); post-D4-drop (node 828 removed as the flagged outlier) `\|A\|=65`, `\|B\|=169`, intersection=26. Applying Appendix B's stated whole-number-rounding convention (`round(kits × rate)`, then divide): Widest Net 45 kits × 16.6% = 7.47 → 7 → 7/45 = **15.556%**; Shared Risk 26 kits × 16.6% = 4.316 → 4 → 4/26 = **15.385%**. A wins by **1.11%** — matches the case's own canonical numbers exactly, correct arithmetic, metric named explicitly (confirmed cases per kit used, not raw count). Confirms the rounding convention still reliably resolves the margin with no tie and no ambiguity. |
| P2 both-sides | **PASS** — both sides independently defensible on real numbers. A's best sentence: nobody exposed to either index patient is left off the list, and under the base assumptions it also wins the case's own headline per-kit metric. B's best sentence: the intersection is the one certain double-exposure population, and testing it fully never depends on how many kits are left this week — confirmed by the twist (B survives; A's edge is a rounding artifact that evaporates and reverses). A is the side that collapses first, precisely at the "how big is your margin really" question — 1.11% off two rounded integers, not a structural efficiency gap. |
| P3 trap | **PASS** — mechanical regex matches (0 fails). Re-read `FACILITATOR.md`: it names the identical trap the mechanical prescreen extracts from `case.json` (raw-count-over-ratio, D5's 7 vs. 4) almost verbatim, plus a documented second-order variant (never checking Appendix A's Data Note before computing). The guide is watching for the trap that will actually catch the room. |
| P4 twist | **PASS** — `sensitivity_model.py` confirms mechanically: base `{A: 0.15556, B: 0.15385}`, twist (kit cut 45→27) `{A: 0.14815, B: 0.15385}`. Winner genuinely flips A→B, margin 3.85%, reproduced by this run's independent hand re-derivation (Widest Net at 27 kits: 27×16.6%=4.482→4→4/27=14.815%; Shared Risk unaffected at 26/26 kits since 26≤27). |
| P5 sensitivity (disclosed) | **PASS** — re-ran `sensitivity_model.py` fresh: `kits_per_week` −50% → winner **TIE** (base A); `rate_dual` +50% → winner **B** (base A); `rate_dual` ±50% both breach the 20% margin cap (48.4%/102.2%). Both instabilities are recorded in `case.json.sensitivity_disclosure[]` (Category X, real justification ≥20 chars each) — same disclosure, unchanged since the prior run, still resolves to the disclosure-aware PASS state. |
| P6 data decay | **PASS** — all 6 `sources[]` URLs plus the 3 newly-replaced glossary links independently re-fetched live 2026-09-14. S1 (snap.stanford.edu/data/ego-Facebook.html): HTTP 200, "4039"/"88234" figures present verbatim. S2 (facebook.tar.gz): HTTP 200; **re-downloaded the real archive and re-derived every cited number from scratch** — `698.feat`/`686.feat` give `\|A\|=66`, `\|B\|=170`, `∩=27`, `∪=209` exactly as cited; node 828's internal-connection share re-derived from the raw `.edges` files as **29.230769…% ≈ 29.2%** (19/65) and **45.562…% ≈ 45.6%** (77/169), circle averages **12.587…% ≈ 12.6%** and **11.528…% ≈ 11.5%** — all four figures match Appendix A verbatim, to the tenth of a percent. S3 (jamanetwork.com): 403 to curl (anti-bot), reachable via WebFetch, page states "16.6% (95% CI, 14.0%-19.3%)" verbatim, 54-study/77,758-participant pooled estimate confirmed. S4 (wwwnc.cdc.gov): HTTP 200 via curl, all four cited figures present verbatim (11.8%, 10,592, 1.9%, 48,481). S5 (cdc.gov/mmwr): 403 to curl (anti-bot), reachable via WebFetch, median 29 contacts/tracer and 31 cases/investigator both confirmed verbatim for the June 25–July 24, 2020 period. S6 (papers.nips.cc): HTTP 200, title "Learning to Discover Social Circles in Ego Networks" confirmed verbatim. **3 newly-replaced glossary links**: Test Positivity Rate → en.wikipedia.org/wiki/COVID-19_testing, HTTP 200, "positivity rate" content confirmed live. Ego Network → arxiv.org/abs/2101.00863, HTTP 200; the abstract page itself doesn't say "ego network" (it's a broad network-science textbook, "The Atlas for the Aspiring Network Scientist"), so this run went further and downloaded the full linked PDF directly — it contains 46 occurrences of "ego network," a substantive treatment, confirming the link is genuinely on-topic once a reader goes past the abstract. Exposure Window → pmc.ncbi.nlm.nih.gov/articles/PMC7832466/, HTTP 200, a real Mayo Clinic contact-tracing paper discussing the infectious/communicable period concept the term names. Zero dead links, zero fabricated values, zero figures that failed to reproduce. |

**6 of 6 requested Tier 2 probes PASS** (P7 accessibility was also re-run as a mechanical
prescreen only, confirming `n_visuals_found: 2` post-polish-pass — not one of the 6 probes this
run was scoped to adjudicate, so no verdict is recorded for it here; the last recorded P7 verdict
remains the 2026-09-13 PASS in the section above). P1/P2 caveat: this run's instructions did not
call for Agent-tool dispatch, so both were assessed directly via careful first-principles
re-solving against the regenerated leak-free packet, same caveat class as every prior run of this
case.

## `case.json.qa` (updated 2026-09-14)

```json
{
  "state": "TIER2_PASS",
  "verdict": "PASS",
  "run_on": "2026-09-14",
  "blockers_open": 0,
  "gaps_open": 2,
  "tier2": {"P1": "PASS", "P2": "PASS", "P3": "PASS", "P4": "PASS",
            "P5": "PASS (disclosed)", "P6": "PASS", "P7": "PASS (2026-09-13, unchanged)"}
}
```

Case remains `TIER2_PASS`. No regression from the polish pass; one real cosmetic defect (footer S4
omission) found and fixed in this run.
