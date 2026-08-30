## case-readiness run — 2026-08-27 (P5/P6 close-out pass #2 — TIER2_PASS)
**State:** TIER1_PASS → **TIER2_PASS**   **Verdict:** TIER2_PASS (Tier 1 clean, 0 blockers/0 gaps;
Tier 2 fully recorded, all six probes PASS)

This run closes out the two Tier 2 FAILs left by the prior pass (preserved below). Per the
instruction that drove this remediation, P5 was resolved by **correction/disclosure**, not by
silently retuning MA1's geometry, and P6 was resolved by **re-sourcing** the decayed/blocked
citations — no figure was invented.

### P5 — assumption sensitivity (±50%) — now PASS (disclosed)

`MA1.sensitivity` (case.json.modeling_assumptions[] and case.md's Modeling Assumptions table) was
factually wrong: it claimed the frustum/sphere dimensions do "not by itself flip the
recommendation." The prior pass's mechanical run showed that claim is false — flexing
`horn_base_r_in`, `horn_top_r_in`, `horn_height_in` (each at −50%) and `orb_r_in` (at +50%)
individually flips the winner from B (Orb) to A (Horn), and several of those same flexes (plus
`horn_packing_efficiency` and `horn_tooling_cost_usd`) also breach SPEC §2's 20% balance cap
without necessarily flipping. Fixed by:

1. **Correcting MA1's and MA6's `sensitivity` text** in both `case.json` and `case.md` to state the
   real, mechanically-confirmed instability instead of the prior (wrong) stability claim. MA4's
   text was left substantively as-is (its own claim — "does not by itself flip the recommendation"
   — is actually true) but updated to reference the re-sourced S8 language (see P6) and to note the
   20%-cap breach at its low end.
2. **Adding `case.json.sensitivity_disclosure[]`** — six entries, each with a `param`, a
   `category` (F or X per the harness's documented disclosure-aware pass state, 2026-08-13
   doctrine), and a 20+-character justification: `horn_base_r_in`, `horn_top_r_in`,
   `horn_height_in`, `orb_r_in` are Category **F** (fictional-prototype dimensions no amount of
   research could ever recover a real value for); `horn_packing_efficiency` and
   `horn_tooling_cost_usd` are Category **X** (a real value exists in principle but isn't publicly
   accessible for this fictional part, so the case used a documented good-faith estimate anchored
   to a public analogue — S8's fill-rate guidance and S7's tooling-cost range, respectively).
3. **Reviewed the ±50% flex range itself** for physical plausibility, per the instruction to check
   whether it was unreasonably wide before accepting the finding: base radius 1.75–5.25 in, top
   radius 1.0–3.0 in, height 3–9 in, sphere radius 1.75–5.25 in are all still plausible dimensions
   for a fictional portable-speaker enclosure. Judged reasonable — not retuned, not widened or
   narrowed.

Re-running `tier2_probes.py --case enclosure-call --probe 5` against the unchanged
`sensitivity_model.py` (geometry inputs were never touched) now returns:

```
--- P5 assumption-sensitivity  [PASS (disclosed)]
base_winner: B   base_margin_pct: 8.9
! DISCLOSED, NOT ELIMINATED: horn_base_r_in, horn_height_in, horn_packing_efficiency,
  horn_tooling_cost_usd, horn_top_r_in, orb_r_in — each has a recorded category and justification
  in sensitivity_disclosure[]. This PASSES per the disclosure-aware pass state (2026-08-13), not
  the stable-margin state.
```

The same 6 params are still mechanically unstable (unchanged, since no input values were altered)
— what changed is that the instability is now honestly documented instead of contradicted by the
case's own text, which is exactly what the harness's disclosure-aware pass state is for.

### P6 — data decay — now PASS

Re-sourced or re-verified all 9 `sources[]` URLs on 2026-08-27:

| id | prior finding | resolution |
|---|---|---|
| S1, S2, S5, S9 | PASS (unchanged) | Re-fetched again today for a genuinely fresh P6 run; all four still show their exact cited figures. |
| S3 (ABS resin price) | FAIL — ProcurementResource showed only EUR/Europe figures | **Re-sourced** to BusinessAnalytiq's live ABS North America price index: "North America: US$1.94/KG" (≈$0.88/lb), August 2026. |
| S4 (ABS density) | INCONCLUSIVE — MatWeb 403-blocked | **Re-sourced** to AmesWeb's published density table: ABS, Extrusion Grade, 1.052 g/cm³ / 0.038 lb/in³ — within a hair of the old 1.05 g/cm³ figure. |
| S6 (derived material cost) | FAIL — inherited S3's decay | **Re-derived** from the new S3 × S4 × MA5: $0.88/lb × 0.038 lb/in³ × 0.0925 in ≈ **$0.0031/in²** (was $0.0029/in²). |
| S7 (tooling-cost benchmark) | FAIL — Formlabs' own figures drifted | **Same URL, re-verified claim**: the page now states "$5,000 to $100,000" for complex-geometry/10,000+-unit molds, plus a $20,000 example for a 100,000-unit steel mold. Both MA6 tooling figures ($32,000, $58,000) still fall inside this range. |
| S8 (packing-efficiency benchmark) | FAIL — DHL-study framing gone | **Same URL, re-verified claim**: the page now reads "above 85% achievable... below 75% suggests a problem," with no study attribution. MA4's basis/sensitivity text updated to match. |

All 9 URLs were fetched live on 2026-08-27 via WebFetch and confirmed to carry their currently-cited
figures — see `cases/enclosure-call/RESEARCH_LOG.md` for the fetch-by-fetch record.

### Margin recompute (S3/S4 re-sourcing changed a load-bearing input)

Re-sourcing S3 ($0.83→$0.88/lb) and S4 (0.0379→0.038 lb/in³) moved the derived material cost per
sq in from $0.0029 to $0.0031, which changes total cost per unit for both options:

| | Project Horn | Project Orb |
|---|---|---|
| Material cost/unit | $0.4579 → **$0.4895** | $0.4464 → **$0.4772** |
| Total cost/unit | $0.8305 → **$0.8621** | $0.7612 → **$0.7920** |

**`margin_pct`: 9.11% → 8.85%** (Project Orb/B still wins, still comfortably inside SPEC §2's 20%
cap). The twist's illustrative Horn-favoring margin moved from 13.32% to **12.75%** along with it.
Updated honestly in `case.json.balance`, `case.json.derived`, `case.json.margin_pct`, `case.md`
(Appendix B material-cost row, Modeling Assumptions table), and `FACILITATOR.md` (Data Deep Dive
table, both Argument sections, Five Socratic Questions, the Twist section) — no document was left
teaching the stale 9.11%/$0.83/$0.0029 figures.

### P1–P4 re-confirmed

- **P1 cold-solve — PASS.** Dispatched a genuinely fresh subagent with access to only the current
  student packet (`/tmp/coldsolve-enclosure-call/PACKET.md`, regenerated by this run). It
  independently reached **B (Project Orb)** with correct arithmetic matching the recomputed
  $0.862/$0.792-per-unit figures, correctly named the metric, and named **MA1** (the geometry
  dimensions) as its most-sensitivity-critical assumption — a reasonable independent read, since
  MA1's disclosed instability is now explicit in the text; it also, unprompted, named MA6's tooling
  gap as the least-supported number, matching the case's own named trap (see P3).
- **P2 both-sides — PASS.** `case.json.balance.argument_a`/`argument_b` were updated with the new
  figures; both remain genuine, quantitative, non-collapsing arguments.
- **P3 trap-check — PASS.** The guide's named trap (stopping at the mold-tooling-cost comparison
  without opening the shipping appendix) matches the fresh cold-solver's independent answer to
  "which number felt least supported" (MA6's tooling-cost gap) — unchanged from the prior run.
- **P4 twist-integrity — PASS.** The twist's structure and independence from every stated Modeling
  Assumption are unchanged; only its illustrative margin moved (13.32% → 12.75%) along with the
  base recompute.

### Final verdict

```
P1 PASS · P2 PASS · P3 PASS · P4 PASS · P5 PASS (disclosed) · P6 PASS
```

Tier 2 is now fully recorded and fully clean (0 FAIL). Per `skills/case-readiness/SKILL.md`'s
ladder, the case advances to **`TIER2_PASS`**. `case.json.qa.state`/`verdict` set to `TIER2_PASS`;
`case.json.qa.blocker_detail` carries the full remediation record. Tier 3 (human dry-run) is now
reachable but NOT RUN — that remains the next, human-only step before `case-publish`.

**Human judgment calls worth a second look, not blockers:** (1) S3's region label reads "North
America" where the case's claim says "USA" — read as materially equivalent for this purpose, but a
human may want to confirm; (2) both Category-X disclosure entries (`horn_packing_efficiency`,
`horn_tooling_cost_usd`) are legitimate one-time exceptions per the harness's own doctrine, but are
worth revisiting if this case is ever revised, since a Category-X estimate is weaker than a real
citation.

---

## case-readiness run — 2026-08-27 (P5/P6 close-out pass #1)
**State:** TIER1_PASS → TIER1_PASS (unchanged)   **Verdict:** TIER1_PASS (Tier 1 clean, 0
blockers/0 gaps; Tier 2 now FULLY RECORDED — P1-P4 PASS, **P5 FAIL, P6 FAIL** — not TIER2_PASS)

This run closes out the two Tier 2 probes left `NOT RUN` by the prior remediation pass (below):
P5 (assumption sensitivity, ±50%) and P6 (data decay on every `sources[].url`). Both probes now
have real, mechanically-run verdicts — and both came back genuine `FAIL`, not `PASS`. Per instruction,
neither is marked PASS because it "isn't genuinely run" would be false either way — they ran, and
they found real problems.

### P5 — assumption sensitivity (±50%) — FAIL

Authored `cases/enclosure-call/sensitivity_model.py` following the contract in
`skills/case-readiness/scripts/example_sensitivity_model.py` (`PARAMS`, `FLEX`, `evaluate()`,
`evaluate_twist()`). It reproduces the case's own published arithmetic to within a tenth of a cent
(Horn $0.8306/unit vs. case.json's $0.8305; Orb $0.7612/unit exact match; base margin 9.11%; twist
margin 13.32% — both exact matches to `case.json.derived`). Since the case's real metric (cost) is
lower-is-better and the Tier 2 harness picks a winner via `max()`, `evaluate()` returns
`1/total_cost_per_unit` per option so the harness's winner-selection stays correct; this is a
scoring-scale choice only and does not change which option wins or by how much in real terms.

`FLEX[]` scopes the sweep to the case's 9 real assumption dials, tracing to MA1 (4 dims), MA2, MA4,
MA5, and MA6 (2 tooling costs) — cited/fixed figures (S1-S4 raw values, and Project Orb's
74.05% Kepler-conjecture packing ceiling, a proven mathematical fact rather than an authored
assumption) are deliberately excluded from `FLEX[]` and left to P6 instead, per SPEC §2 and the
FLEX-scoping doctrine in `skills/case-readiness/SKILL.md`. `preflight_lint.py`'s FLEX-scoping check
ran clean (no cited-value-in-FLEX false positive).

Running `tier2_probes.py --case enclosure-call --probe 5`:

```
base: Horn=1.20 (inverted), Orb=1.31 (inverted)   base_winner: B   base_margin_pct: 9.1%
```

**Verdict: FAIL.** Flexing MA1's four geometry dials (`horn_base_r_in`, `horn_top_r_in`,
`horn_height_in`, `orb_r_in`) and MA6's `horn_tooling_cost_usd` individually by ±50% (holding all
other dials at base) flips the winner from B (Orb) to A (Horn) in 6 of 18 flex rows, and 9 of 18
rows push the margin past SPEC §2's 20% balance cap:

| dial | flex | new winner | margin | flips base (B)? |
|---|---|---|---|---|
| horn_base_r_in | −50% | A | 34.6% | yes |
| horn_top_r_in | −50% | A | 5.6% | yes |
| horn_height_in | −50% | A | 23.1% | yes |
| orb_r_in | +50% | A | 112.2% | yes |
| horn_tooling_cost_usd | −50% | A | 6.5% | yes |
| horn_base_r_in / top_r_in / height_in (opposite direction), orb_r_in −50%, horn_packing_efficiency −50%, horn_tooling_cost_usd +50% | — | B (unchanged) | 24.4%–215.9% | no, but breaks 20% cap |

MA4 (Project Horn's packing efficiency — the case's own named "single most dilemma-sensitive
assumption") and MA2 (target production volume) do **not** flip the verdict under ±50%, matching
`case.json.sensitivity_note` and `MA4`/`MA2`'s own stated sensitivity language exactly. The
newly-discovered instability is somewhere the case's own documentation does not currently flag it:
`MA1.sensitivity` states flexing the frustum/sphere dimensions "does not by itself flip the
recommendation" — that claim is false under an honest per-dial ±50% flex (each of the 4 dims is
independently listed as its own `needs_source`/`ASSUMPTION` entry resolving to MA1, so flexing each
independently is a legitimate reading, not a model artifact). `tier2_probes.py` also flags all 6
unstable dials as **UNDISCLOSED** — `case.json` has no `sensitivity_disclosure[]` entry covering
any of them.

**This is a genuine finding, left for a human**, not remediated in this pass: either (a) add a
disclosure/caveat to `MA1`'s and `MA6`'s `sensitivity` text and to `balance`/Guide Notes admitting
the geometry- and tooling-cost fragility, or (b) retune MA1's dimension picks so the case is less
geometry-fragile at ±50%. Neither is a mechanical fix within this pass's scope (it requires editorial
judgment about how the case should read, not just data entry).

### P6 — data decay — FAIL

Fetched all 9 `sources[].url` entries via WebFetch on 2026-08-27, one day after their recorded
`accessed: "2026-08-26"` date.

| id | verdict | finding |
|---|---|---|
| S1 | PASS | bws.net still shows "Capacity: 76 cbm" — matches cited 2,683 cu ft / ~76 m³ |
| S2 | PASS | freightos.com still shows exactly $3,570.80 for the current FBX spot rate |
| S3 | **FAIL** | procurementresource.com no longer shows any USA/USD figure — only EUR/MT figures for Europe (EUR 1,696–1,838/MT for June/July 2026). The cited $0.83/lb USA figure does not appear on the page any more. |
| S4 | **INCONCLUSIVE** | matweb.com returned HTTP 403 to automated fetch (both WebFetch and a direct `curl` with a browser UA) — typical MatWeb bot-blocking, not a confirmed dead page. Could not verify the 1.05 g/cm³ density figure either way. Reported as NOT FOUND rather than guessed, per MCS-21. |
| S5 | PASS | protolabs.com still shows exactly "0.045 in. - 0.140 in." |
| S6 | **FAIL** | derived from S3 (identical URL) — inherits S3's decay; its basis figure is no longer present on the cited page |
| S7 | **FAIL** | formlabs.com now shows a different range: "$5,000 to $100,000" for complex-geometry/10,000+-unit molds, and ~$20,000 for a 100k-unit steel-mold example — not the cited "$25,000-100,000+" for 100k+-unit production |
| S8 | **FAIL** | 3dloadcalculator.com now shows "85%+ achievable... below 75% suggests a problem," with no DHL-study citation found anywhere on the page — not the cited "76-85%" DHL-attributed range |
| S9 | PASS | audioxpress.com still discusses PC/ABS blends for speaker enclosures; qualitative claim holds |

**Net: 4 PASS, 4 FAIL, 1 INCONCLUSIVE of 9.** S3/S6 (the material-cost basis) and S7/S8 (the
tooling-cost and packing-efficiency bases) have decayed since the 2026-08-26 access date — these
are exactly the "worse" case the skill warns about (the URL resolves, but no longer carries the
figure, so nothing else in the pipeline would ever have noticed). These need either re-sourcing or
an updated `as_of`/`confidence` note before publish; not remediated in this pass, since re-sourcing
a live figure is itself a `case-research`-stage judgment call, not a QA fix.

### The Twist's $45,000 figure — re-confirmed consistent

Re-checked per instruction: `case.md` contains **zero** mentions of "45,000", "45000", or "recert"
(confirmed by direct grep — no matches). The figure lives only in `FACILITATOR.md`'s "## Twist"
section (explicitly marked "illustrative for the discussion only... not a `sources[]`-backed
figure") and in `case.json.derived.twist_illustrative_*` keys, never in `case.json.balance` (which
stays the honest, sourced 9.11% figure) and never in the graded student-facing `case.md`. This
remains the correct, intentional design — no adjustment needed.

### Net effect on `case.json.qa`

Tier 2 is now **fully recorded** (all six probes have real verdicts; none is `NOT RUN` any more),
but it is **not clean** — 2 of 6 probes FAIL. Per `skills/case-readiness/SKILL.md`'s ladder
("`TIER2_PASS` requires all six Tier 2 probes recorded, 0 FAIL"), the case **remains at
`TIER1_PASS`**, not `TIER2_PASS`. `case.json.qa.tier2` updated to `{P1: PASS, P2: PASS, P3: PASS,
P4: PASS, P5: FAIL, P6: FAIL}`; `case.json.qa.blocker_detail` carries the full detail above.
**Not ready for `case-publish`** until a human resolves the P5 disclosure/retune judgment call and
the P6 source refresh.

---

## case-readiness run — 2026-08-27 (remediation pass)
**State:** BLOCKED → TIER1_PASS   **Verdict:** TIER1_PASS (Tier 1 clean, 0 blockers/0 gaps; Tier 2
partially run — P1-P4 PASS, P5/P6 NOT RUN)

This is a re-run after `case-write`-stage remediation of the four BLOCKERs found in the prior run
(see the original findings preserved at the bottom of this file). Summary of what changed:

1. **T1-09 (margin_pct)** — computed the total-cost-per-unit comparison honestly from the on-file
   MA1/MA2/MA4/MA6 assumptions and S1/S2/S6 sourced figures. Project Horn = $0.8305/unit, Project
   Orb = $0.7612/unit. **`margin_pct` = 9.11%, Project Orb (B) wins**, comfortably inside SPEC §2's
   ~20% balance cap. Recorded in `case.json.balance`, `case.json.margin_pct`, and
   `case.json.derived` (full arithmetic walkthrough in the latter's `computation_2026_08_27` note).
2. **T1-13 (x3)** — `FACILITATOR.md` rewritten in full: the complete SPEC §7.1 anchor ladder
   (Intro/Launch/Anchor 1-4/Data Deep Dive/Twist/Close/Lessons Learned/Standards Touched On), a
   genuine Twist section (a contractual acoustic-certification requirement that adds a
   $45,000/250,000-unit = $0.18/unit cost to Project Orb, illustrative-only figure, flipping the
   *illustrative* recommendation to Horn by ~13.32% without making either side obviously correct),
   and a timed 45-minute Socratic plan (SPEC §7.3, 7 timed rows, twist drop named at 15:00). The
   original write-time content (Argument for A/B, five Socratic questions, the trap, the "no SPEC §6
   sensitivity" note) was preserved and folded into the rewritten guide rather than discarded.
3. **T1-06 GAP** — Appendix E ("Sources") was undeclared in `case.json.appendices[]` and sat out of
   letter order in `case.md`. Fixed by relettering: Sources is now **Appendix D**, the mandatory
   "How To…" standards-bridge appendix is now **Appendix E** (last, as SPEC §1.7 requires), both in
   `case.md` and in `case.json.appendices[]`. Background's two APPENDIX cross-references were
   updated to match.
4. **T1-17 GAP** — `case.json.cohort_bands[]` declared: Full (16-24), Compressed (8-12), 1:1/pair
   (1-2), per SPEC §7.4's three-band floor.
5. **T1-13 GAP (regex false-positive)** — the prior run's 5-Socratic-questions miscount was
   confirmed to be a line-wrap artifact of `tier1_structural.py`'s regex, not a content defect (per
   the prior report). Reformatted each of the 5 questions onto a single line in the rewrite so the
   mechanical check now counts them correctly (5/5) — this is a formatting improvement, not a
   change of substance, and the underlying regex-maintenance suggestion for multi-line questions
   still stands as a `tier1_structural.py` improvement for other cases.

**Judgment call flagged for a human:** the Twist's $45,000 recertification-cost figure is
deliberately *not* a `sources[]`-backed number — it is a facilitator-only illustrative device (SPEC
§7.2 twists are introduced information, not appendix data), recorded only in `case.json.derived` and
`FACILITATOR.md`, never in `case.md`. This is consistent with how twists work elsewhere in the
corpus, but flagging it explicitly since it is the one number in this remediation that is invented
rather than computed from cited/assumed inputs — it is scoped to stay out of the graded, student-
facing balance test, which remains the honest 9.11% figure computed from real sourced/assumed data.

### Tier 1 — structural (20 checks)
sha256(case.md) = `206068853e129446bf4d2e611782eed59a1d2510cb317fdd318a9856c436f483`

All 20 checks PASS. 0 BLOCKER, 0 GAP.

| id | result |
|---|---|
| T1-01 … T1-20 | all PASS |

**POLISH (5, none gate anything):** T1-07 (parse note only — 9 labels, 9 bulleted, 0 from
separator-run lines); T1-15/T1-18/T1-19/T1-20 (no `published/` directory yet, nothing to check).

### Tier 2 — simulated play (6 probes)

Mechanical pre-screens for P2 (both-sides) and P3 (trap) were re-run after rewriting
`case.json.balance.argument_a`/`argument_b` with real quantitative figures (the write-time drafts
had zero digits, which is why they mechanically FAILed the "strongest quantitative argument" check
the moment `margin_pct` stopped being null) and after removing an accidental early mention of the
word "trap" in `FACILITATOR.md`'s Data Deep Dive section that was hijacking the trap-detection
regex before it reached the real "## The trap" section.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Dispatched a genuinely fresh subagent with no access to `FACILITATOR.md`/`case.json`/`QA_REPORT.md`, only the leak-checked student packet. It reached **B (Project Orb)** with correct, independently-derived arithmetic ($0.831 vs $0.761/unit, ~8-9% gap), correctly named the optimized metric (total cost per unit), and correctly identified **MA4 (Horn's 80% packing efficiency)** as the most sensitivity-critical assumption — matching the case's own `sensitivity_note` exactly, unprompted. |
| P2 both-sides | **PASS** | Mechanical pre-screen clean (each argument now carries real numbers, no concession-only phrasing). Both A and B have genuine, defensible quantitative cases in `FACILITATOR.md`/`case.json.balance`; neither collapses — the 9.11% margin holds up as a real balance, not a paper number. |
| P3 trap check | **PASS** | `FACILITATOR.md`'s named trap (a Hero who stops at the tooling-cost comparison and never opens Appendix C) matches what the independent cold-solve subagent found unprompted: its own answer to "which number felt least supported" named the $26,000 Horn-vs-Orb tooling gap as *the* decisive, weakest-evidenced factor in the whole case — the guide's anticipated trap is the room's actual trap. |
| P4 twist | **PASS** | The Twist (a contractual acoustic-certification cost, not a market figure) is independent of every stated Modeling Assumption, so it survives any natural reading of MA1-MA6 without contradiction. It invalidates the "case closed at 9.11% for Orb" position a room would reach after the Data Deep Dive, and does not make either side obviously correct (Horn only wins by ~13.32% under the twist, still inside a defensible range). |
| P5 sensitivity | **NOT RUN** | No `cases/enclosure-call/sensitivity_model.py` exists to flex MA1-MA6 ±50% mechanically. Authoring one is out of scope for this remediation pass (which was scoped to the 4 named BLOCKERs); flagged here as the one remaining Tier 2 gap, and as a genuine judgment call — a human should decide whether to invest in a sensitivity model now or accept `NOT RUN` as this case's honest, documented state per house doctrine ("absent data is a first-class state"). |
| P6 data decay | **NOT RUN** | 9 `sources[]` URLs on file (S1-S9), all listed in the Tier 2 script's worklist, but the URL-liveness fetch was not performed in this remediation pass. Recommend running before `TIER2_PASS`/publish. |

**Tier 2 is not yet fully clean** (P5 and P6 outstanding) — the case sits at `TIER1_PASS`, not
`TIER2_PASS`, per the ladder in `skills/case-readiness/SKILL.md` ("all six Tier 2 probes recorded, 0
FAIL"). P1-P4 give strong, independently-corroborated confidence the case plays correctly; P5/P6 are
the honest remaining work before publish.

### Tier 3 — human dry-run
NOT RUN. Not reachable until `TIER2_PASS`.

### Next step
Author `cases/enclosure-call/sensitivity_model.py` (P5) and run the data-decay fetch on the 9
`sources[]` URLs (P6) to close out Tier 2 and reach `TIER2_PASS`. Everything else in this case —
structure, balance test, facilitator guide, cohort bands — is now clean and consistent.

---

## Prior run — 2026-08-27 (original, superseded by the remediation above)

**State:** DRAFT → BLOCKED   **Verdict:** BLOCKED (Tier 1 did not clear; Tier 2 not run)

Preflight lint (`preflight_lint.py --case enclosure-call`) ran first: 1 advisory finding, an
HTML comment in `case.md` (`<!-- FACILITATOR ONLY: ... -->`) that names "FACILITATOR" in the
student-facing file. Reviewed and judged not a real leak — it is an HTML comment, invisible in
rendered output, and names no balance figure, margin, or twist content, only the word
"facilitator" itself. Not escalated as a BLOCKER; noted here for the record since preflight is
advisory-not-blocking by design. (Still true on the remediated case — same finding, same
judgment, re-confirmed 2026-08-27.)

### Tier 1 — structural (20 checks)
sha256(case.md) = `0d3316769690b075064c2d17e3a059022c210c70de2b68c52b4464e303de8e08`

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview length; no load-bearing numerals |
| T1-03 | PASS | Dilemma binary, opens "You are Nina Odom." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no Challenge numeral-form drift |
| T1-06 | GAP | appendices out of order: `['A', 'B', 'C', 'E', 'D']`. `case.json.appendices[]` only declares A, B, C, D — `case.md`'s "Appendix E — Sources" is an undeclared fifth appendix. **FIXED — see remediation above.** |
| T1-07 | PASS | 9 vocabulary labels parsed (9 bulleted, 0 from separator-run lines), all resolve to the spine |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | **FAIL / BLOCKER** | SPEC §2 — `margin_pct` not recorded. **FIXED — see remediation above.** |
| T1-10 | PASS | `new_coverage[]` = `["geometry-cone", "geometry-sphere"]`, both genuinely zero-coverage before this case |
| T1-11 | PASS | learning-goal mutual reachability |
| T1-12 | PASS | tier (T2) vs. numeric load consistent |
| T1-13 | **FAIL / BLOCKER (3 findings)** | `FACILITATOR.md` write-time partial draft. **FIXED — see remediation above.** |
| T1-14 | PASS | continuity — no `case.json.derived` rows yet to check against `FACILITATOR.md` (nothing to drift) |
| T1-15 | PASS | no `published/` directory yet — nothing to drift |
| T1-16 | GAP | MCS-11 — no `case_md_sha256` recorded yet (expected on a first run; recorded now) |
| T1-17 | GAP | MCS-25 — `case.json` declares no `cohort_bands[]`. **FIXED — see remediation above.** |
| T1-18 | PASS | no `published/` directory — MCS-37 has nothing to check yet |
| T1-19 | PASS | no `published/` directory — MCS-39 has nothing to check yet |
| T1-20 | PASS | no `published/` directory — advisory, nothing to check yet |

### Tier 2 — simulated play (6 probes)
NOT RUN in the original pass. See the remediation run above for the current Tier 2 state.

### Tier 3 — human dry-run
NOT RUN.
