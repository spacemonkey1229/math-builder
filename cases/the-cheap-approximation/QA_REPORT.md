# QA_REPORT.md — The Cheap Approximation

## case-readiness run — 2026-08-31

**State:** DRAFT → TIER1_PASS → (Tier 2: 5/6 PASS, P1 pending reconfirmation)
**Verdict:** TIER1_PASS. NOT YET TIER2_PASS — see P1 below.

Context: this case was redesigned this session (RESEARCH_LOG.md, "CASE-FIX PASS — 2026-08-31").
The original margin (99.86%, Option B winning by ~730x) was fixed by (a) correcting Appendix A's
operating range to the datasheet's real accuracy-guaranteed range (0–70°C, not the originally
spliced −80/150°C), and (b) tightening the flash-budget Modeling Assumption (MA3) from 64 to 6
bytes. New margin: 13.97%, Option B (Table Path) still wins, much more narrowly. This case had
**not** previously been through the FACILITATOR.md-anchor-ladder / Socratic-questions / orphan-
number remediation the rest of this batch received — it was written directly to Tier-2 quality
expectations. This run is the first full pass through the gate.

---

### Preflight lint

Found one Modeling-Assumptions leak: `case.md`'s MA3 Sensitivity column stated the actual
computed margin ("the D5 margin is ~14%") and named specific alternative-budget margins ("a
~60% margin," "the ~99% landslide"), not just the assumption's basis. **Fixed**: rewrote MA3's
(and MA2's, which had the same defect plus a stale "~99.86%" reference to the pre-fix margin)
Sensitivity cells to state direction only, matching house style (see `curves-turn`/`downbeat-
split` precedent). Mirrored the same fix into `case.json.modeling_assumptions[MA2/MA3].sensitivity`.
Re-run: clean.

### Tier 1 — structural (20 checks)

| id | result | note |
|---|---|---|
| T1-01 – T1-08 | PASS | |
| T1-09 | PASS (after fix) | a **stale top-level `case.json.margin_pct: 99.86`** (never updated during the case-fix pass — only the nested `balance.margin_pct` had been updated to 13.97) was making T1-09 report the case as unbalanced. Fixed: top-level field corrected to 13.97. |
| T1-10 | PASS | `new_coverage` correctly non-empty (`calculus-taylor-series`, `calculus-how-to-find-the-taylor-series-of-a-function-at-a-point`) — confirmed both still show `n=0`, `covered_by: []` in `readmodel/standards_spine.json`. No `reinforcement_note` added; none needed. |
| T1-11 | PASS (after fix) | deliverable D5 had `skills: []` — an orphan deliverable. Fixed: added `calculus-taylor-series` (matching D3/D4's mapping, since D5 combines D3's Taylor-derived error into the recommendation). |
| T1-12 | PASS | |
| T1-13 | PASS (after full rewrite) | Originally missing the entire anchor ladder (Intro/Launch/Anchor 1–4/Data Deep Dive/Twist/Close/Lessons Learned/Standards Touched On), no Twist section, no timed 45-minute Socratic plan, and 0 machine-countable Socratic questions (existing 5 were line-wrapped so the question mark fell on a different line than the numeral). **Fixed**: rewrote FACILITATOR.md in full, using `cases/cooling-curve/FACILITATOR.md` as the structural template. Authored a new Twist (see below) grounded entirely in numbers already in the case (MA3's 6-byte reservation vs. the MCU's sourced 16 KB total flash — no invented figures). Collapsed the Socratic-questions list to single-line items so the mechanical check counts them. |
| T1-14 | PASS (after fix) | continuity sweep initially found 11 guide-only numbers with no home in case.md/case.json. Fixed: added `case.json.derived` (D3/D4/D5 intermediate figures, matched to the same rounding used in FACILITATOR.md's arithmetic note) and recorded the Kelvin-Celsius offset constant (273.15). |
| T1-15 | PASS | no `published/` yet |
| T1-16 | GAP (expected) | no `case_md_sha256` recorded before this run — now set: `465a02786476d0a91a40c22a605c82980d539fba7065c32bb4bd8ed03be2466b` |
| T1-17 | PASS (after fix) | no `cohort_bands[]` declared. Fixed: added 3 bands (12–18 full / 6–9 compressed / 1–2 pair), matching cooling-curve's structure. |
| T1-18 – T1-20 | PASS / advisory | no `published/` directory yet (case not yet built to interactive HTML) |

**BLOCKER (0). GAP (1, expected first-run T1-16).**

**Additional fix found during Tier 2, not by Tier 1:** Appendix A never stated the Steinhart-Hart
equation itself, and Challenge D1 ("Derive the 2nd-order Taylor series of the sensor's response
function") did not specify which variable to expand in — R or ln(R). This is exactly the kind
of ambiguity Tier 1's mechanical checks cannot catch (it is a math-content-clarity issue, not a
structural one) but Tier 2's cold-solve probe is designed to surface. See P1 below. **Fixed**:
Appendix A now states the equation (`1/T = A + B·ln(R) + C·[ln(R)]³`) and explicitly instructs
that D1's expansion is with respect to u = ln(R), not R. Re-ran Tier 1 after this fix: still
clean, TIER1_PASS, same 0 blockers / 1 expected GAP.

### Sensitivity model

Authored `cases/the-cheap-approximation/sensitivity_model.py`. Reproduces the case's real physics
from scratch (numerically inverts the Steinhart-Hart equation for the true response, derives the
2nd-order Taylor expansion symbolically, scans a dense piecewise-linear interpolation of an
N-node table) rather than using a canned lookup. Verified against RESEARCH_LOG.md's own MA3 sweep
table: reproduces every row (N=2/3/4/6/8/32 entries) to 3 significant figures, and reproduces
the case's documented D3 (0.169°C / −0.667°C), D4 (5/9 cycles, 0.156/0.281 µs) and D5 (4.27/3.68
°C/µs) figures essentially exactly. One documented caveat: `case.json`'s own margin convention
(divide by the *losing* option's raw metric, 13.97%) differs from `tier2_probes.py`'s harness
convention (divide by the *winning* option's raw metric via the reciprocal transform the contract
requires, 16.2%) — both are standard conventions, both agree on the winner, both land under the
20% cap; this is documented in the model's own docstring, not a modeling error.

**Flash-budget (MA3) sensitivity — the specific finding requested.** MA3 is confirmed
**dilemma-flipping**: a −50% flex (6 → 3 bytes, which floor-divides to the same 2-entry table as
an even smaller budget) **flips the winner to the Series Path (A)**. A +50% flex (6 → 9 bytes,
4 entries) does **not** flip the winner — it widens the Table Path's (B's) existing lead sharply.
The flip happens on the downward side of the swing at this base value, not the upward side. This
matches and mechanically confirms RESEARCH_LOG.md's own hand-computed MA3 sweep table exactly.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **FAIL (original) → root cause fixed → mechanically re-verified, live re-run pending** | A fresh subagent, given only the student-facing packet, reached the correct **winner** (B) but via **wrong arithmetic**: it expanded the response function in R directly instead of in u = ln(R), producing wildly inflated errors (≈+39.9°C at 0°C, ≈−17.5°C at 70°C, vs. the case's real ≈+0.17°C/−0.67°C) and separately assumed an unstated table-node-placement convention that produced near-zero table error. Root cause: case.md never stated the Steinhart-Hart equation itself, and D1 did not specify the expansion variable — exactly the "reaching the right answer by the wrong route" failure this probe exists to catch. **Fixed** in Appendix A (see Tier 1 above). Re-verification: with u = ln(R) as now explicitly instructed, I recomputed the D3 arithmetic directly and got +0.1689°C at 0°C and −0.6670°C at 70°C — matching the case's documented figures to 4 significant figures, and matching a second, independent fresh subagent (dispatched for P2, working from the case before this fix) which inferred u = ln(R) on its own from general Steinhart-Hart knowledge and got the same close match (+0.159°C/−0.686°C). This shows the ambiguity is real but not universally fatal, and that the fix directly targets and closes the specific gap the failing solver fell into. **Recommend one more live fresh cold-solve subagent run post-fix before this is called a clean PASS** — I have not treated my own arithmetic check as a substitute for that. |
| P2 both-sides | PASS | Mechanical prescreen initially FAILed (`argument_b` carried almost no numbers — 1 digit). Fixed: rewrote `argument_b` with concrete figures (6 bytes/2 bytes-per-entry, 9 vs. 5 cycles, ~1.8x). A fresh subagent built the strongest case for each option independently: Argument A is genuinely strong (Series Path wins on BOTH raw sub-metrics — less error AND less time, at this specific 6-byte budget — a real, striking finding neither I nor the original case text had surfaced this precisely). Argument B is real but attackable (wins only the case's actual graded ratio metric, and only because of MA3's specific value). Neither side reads as a hollow concession. Collapse point for A: when pressed on the case's literal primary-metric definition (error *per microsecond*, not raw error or raw time alone). Collapse point for B: when pressed on MA3's realism. Both collapse points are real and distinct — a legitimately close, well-built dilemma. |
| P3 trap | PASS | Mechanical prescreen initially FAILed twice: (1) the word "trap" appeared earlier in FACILITATOR.md's own preamble disclaimer and in the Launch section, so the regex's "first trap mention" check never reached the real "## The trap" section. Fixed: rephrased both earlier mentions to avoid the literal word. (2) Once it reached the real section, the trap text read as a difficulty note ("the case forces a *specific* table resolution... can end up defending a table that is either not accurate enough...") without a DO-verb describing what a learner actually does wrong. Fixed: rewrote to explicit learner-action language ("Most learners will... assume... skip... misses... defaults to..."). Independently, my own read of the case (and the P2 both-sides finding above) confirms the guide's named trap: a hurried student who computes D3/D4 separately finds the Series Path superior on *both* raw numbers and stops there, never computing D5's actual ratio — the guide names this correctly, and my analysis shows it is if anything a sharper trap than the guide's text states (both raw sub-metrics favor A, not just compute time). |
| P4 twist | PASS | A fresh subagent, given `case.md`, `FACILITATOR.md`, and `case.json`, checked the Twist (MA3's 6-byte flash reservation is under 0.04% of the MCU's sourced 16 KB total flash — is that realistic, or contrived to manufacture a close margin?) against the Cold Chain precedent (a twist that did nothing under one reading of an assumption). Verdict: **PASS**. The twist's core arithmetic (6/16384 ≈ 0.037%) is invariant — it depends on no other assumption, reading order, or convention, so it cannot fail the way Cold Chain's did. It genuinely undercuts unearned confidence in "B wins, case closed" (the case's own history — 64 bytes was scoped down specifically to manufacture a genuine dilemma — makes this a fair, not a strawman, provocation). It does not mechanically flip the recommendation on its own (FACILITATOR.md is explicit about this), though the door to a real flip is open via MA3's own disclosed −50% instability (Probe 5) if a Hero constructs and defends a specific alternative. |
| P5 sensitivity | PASS (disclosed) | Mechanical run (`tier2_probes.py --probe 5`) initially FAILed: `flash_read_cycles`, `flash_budget_bytes`, and `bytes_per_entry` all break the 20% cap or flip the winner under ±50%, with no `sensitivity_disclosure[]` entries. Fixed: added 4 disclosure entries (MA1/MA2 as Category X — real silicon facts, inaccessible from public docs; MA3/MA4 as Category F — facts about a fictional firmware project's own memory map, unresearchable in principle), each with a real justification citing the specific instability found. Re-run: **PASS (disclosed)**. MA3 (flash budget) confirmed as the load-bearing, dilemma-flipping dial (see Sensitivity model section above). |
| P6 data decay | PASS | Live-fetched the Omega Engineering 44000 Series datasheet (`assets.omega.com/spec/44000_THERMIS_ELEMENTS.pdf`) directly — **the crux claim is confirmed verbatim**: "We list two basic accuracy/interchangeability specifications for our thermistors, ±0.10°C and ±0.20°C from 0 to 70°C (32 to 158°F)" and "The accuracy specification of ±0.1% or 0.2% means that each thermistor's resistance will fall within these limits between 0 and 70°C." The document's own "To Order" table confirms "Interchangeability @ 0 to 70°C" is a column distinct from "Maximum Working Temp" (150°C) and "Storage and Working Temp for Best Stability" (−80 to 120°C) — directly confirming RESEARCH_LOG's finding that the original −80/150°C scoping spliced two different, non-accuracy columns. Also confirmed live: Table 1's Model 44004 row (R25°C=2252 Ω, A=1.468×10⁻³, B=2.383×10⁻⁴, C=1.007×10⁻⁷ — exact match) and Table 2's tolerance values (±0.20°C at both 0°C and 70°C for the 44004/±0.20°C class). Live-fetched the Arm Cortex-M0+ Technical Reference Manual (`keil.com/dd/docs/datashts/arm/cortex_m0p/r0p0/ddi0484b_cortex_m0p_r0p0_trm.pdf`) — confirmed Table 3-1's exact text ("cycle counts are based on a system with zero wait-states"), `ADDS Rd, Rn, Rm` = 1 cycle, `MULS Rd, Rm, Rd` = "1 or 32", `LDR` = "2 or 1b" — all match case.md exactly. Independently re-confirmed by a second live-fetch pass (matching text quoted verbatim from both fetches). Minor precision note, not a defect: footnote (b) on `LDR`'s "2 or 1" reads "2 if to AHB interface or SCS, 1 if to single-cycle I/O port" — MA2's basis text uses the "2 cycles" baseline, which is the physically correct selection for a flash-memory read specifically (flash is accessed via the AHB interface, not a single-cycle I/O port), so this is not an oversimplification for this case's actual use, just worth recording that the TRM's own figure is conditional rather than a flat constant. S8/S9 (ST's STM32L011F4 product page) could not be re-fetched directly this pass (60s timeout on two independent attempts, plus a failed curl), consistent with RESEARCH_LOG.md's own documented note about repeated st.com bot-protection/timeouts — not a new finding. A WebSearch-indexed snippet of ST's own datasheet text independently corroborates Cortex-M0+, 32 MHz max, and 16 Kbyte flash. MEDIUM confidence stands, unchanged. |

### Tier 3 — human dry-run

NOT RUN.

---

## Disposition

- **BLOCKER count: 0.** Tier 1 is clean and stable across both the structural remediation and the
  post-Tier-2 Appendix A fix (re-run confirmed 0 blockers both times).
- **Tier 2: 5 of 6 probes PASS.** P1 found a real, now-fixed defect and is mechanically
  re-verified but not yet reconfirmed by a second live fresh cold-solve subagent.
- `case.json.qa.state` set to `TIER1_PASS`; `status` set to `"qa"`. Tier 2 is recorded probe-by-probe
  in `case.json.qa.tier2` per house doctrine (six probes, six verdicts, by name — P1's verdict is
  recorded honestly as "FAIL (original run) -> defect fixed -> PENDING reconfirmation", not
  papered over as a clean PASS).

## Next step

**Run one more fresh, blind cold-solve subagent against the corrected `case.md`** (regenerate the
packet via `tier2_probes.py --case the-cheap-approximation --probe 1`, dispatch a genuinely new
subagent with no context from this run, packet only). If it reaches the documented D3 figures
(≈+0.17°C / −0.67°C) via u = ln(R) without being told to, record P1 as a clean PASS and set
`case.json.qa.state` to `TIER2_PASS`. `case-publish` should not run until then.

## Never

This report names defects and the exact fixes applied; it does not itself publish, does not
touch `readmodel/`, and does not write `cases_index.json`.
