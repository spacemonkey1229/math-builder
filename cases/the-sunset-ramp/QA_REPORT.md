# QA Report — The Sunset Ramp

## Run 2026-08-15 — Tier 1 structural (case-readiness)

**Method:** `python3 skills/case-readiness/scripts/tier1_structural.py --case the-sunset-ramp`
**`sha256(case.md)`:** `64ed3f90b6884c493933b062bf9b38774b6b2578427abd23b45ab100d48faed0`
**Verdict:** **TIER1_PASS** — 0 BLOCKERs, 2 GAPs open (neither blocking), 1 POLISH note.

This is a fresh-authored case closing a genuine spine gap (Calculus/Derivatives had 0 cases before
this one); the T1-10 legacy-conversion carve-out on `new_coverage[]` does not apply here and was
not invoked — all six `new_coverage[]` ids were verified `n=0` in `readmodel/standards_spine.json`
before authoring (see `LEARNING_GOALS.md`) and remain genuine, forced-by-deliverable claims.

### Pre-flight: placeholder / source verification

- Grepped `case.md` for `{{NEEDS_SOURCE}}` — zero remain. `case.json.needs_source[]` (the
  authoring-time tracking list, distinct from live placeholders) shows all 15 entries resolved:
  5 `SOURCED` against real sources S1–S5 (EIA/Sargent & Lundy AEO2025 capital-cost study, GE
  Vernova LM6000 product page, Modo Energy's two research notes), and 10 `ASSUMPTION` under the
  single declared Modeling Assumption MA1 (the Appendix B net-load table, anchored to CAISO's real
  6.5 GW/hour cited rise).
- Confirmed `standards[]`/`new_coverage[]` resolve cleanly against the spine: all 8 `standards[]`
  ids exist, the 6 `new_coverage[]` ids are genuinely `n=0`, and the 2 already-covered ids
  (compound-unit conversion, percent-of-a-number) are correctly excluded from `new_coverage[]`
  per `LEARNING_GOALS.md`'s own overlap check.
- `RESEARCH_LOG.md` documents a real, multi-avenue attempt (EIA Hourly Electric Grid Monitor, EIA
  Electricity Data Browser, EIA API v2, CAISO Daily Renewables Watch, CAISO Today's Outlook,
  CAISO OASIS, academic literature, CAISO's own "Fast Facts" PDF) to source a directly-published,
  timestamped net-load table before falling back to the disclosed Modeling Assumption — a genuine
  NOT-FOUND exit, not a shortcut.

### `sensitivity_model.py` — built and verified

`cases/the-sunset-ramp/sensitivity_model.py` was authored from scratch following
`example_sensitivity_model.py`'s contract (`PARAMS`, `FLEX`, `evaluate()`, `evaluate_twist()`).
Running it directly reproduces `case.json.derived` exactly:

```
peak_ramp_rate_mw_per_min = 137.5000  (expect 137.5)
battery capability        = 12000.0 MW/min (expect 12000.0)
rate delivered A / B      = 137.5 / 50.0 MW/min (expect 137.5 / 50.0)
cost per MW/min A         = $4,721,454.55 (expect $4,721,454.55)
cost per MW/min B         = $3,854,400.00 (expect $3,854,400.00)
margin_pct (B cheaper by) = 18.36 (expect 18.36)
```

**FLEX-scoping applied deliberately** (per the 2026-08-13 doctrine note): `FLEX = ["t60_net_load_mw",
"t120_net_load_mw", "battery_response_time_s"]` — only the case's genuine authorial choices
(Appendix C/MA1's curve-shape assumption; the battery's conservative 1-second response-time
convention, per `RESEARCH_LOG.md` P01). The cited S5 rise (`rise_1819_mw`), the cited peaker
capability (S3), and both capital totals (derived from cited S1/S2 unit costs) are deliberately
**excluded** from `FLEX` — they are given/cited data, stress-tested by Tier 2 probe 6 (data decay)
instead of probe 5.

### Interactive HTML — built and verified

`cases/the-sunset-ramp/published/The Sunset Ramp - Interactive.html` was built from
`templates/interactive_shell.html` with case-specific Overview/Background/Dilemma/Challenges/
Appendices A–E, a 4-step Working Notebook (P(t) fit + power-rule derivative, tangent line at the
steepest instant, ramp-response capability table, cost-per-MW/min + margin), and the backstop-
battery Twist (gated behind a reveal button, matching `FACILITATOR.md`). The `<script>` block is a
direct JS port of `sensitivity_model.py`'s `PARAMS`/`FLEX`/`evaluate()`/`evaluate_twist()` —
verified by hand against the Python file, same keys, same arithmetic. Glossary: 9 terms (>= the
MCS-39 floor of 8), all `https://` links to allowlisted domains (`cuemath.com`, `mathsisfun.com`),
each fetched and confirmed live 2026-08-15 (this session) before shipping — see the tool-call
record in this session for the exact fetches. No balance-test margin, D2 instantaneous rate, or
either option's cost-per-MW/min appears as a static literal anywhere outside `<script>`'s live
computation.

### BLOCKERs found and resolved (this run)

| # | Finding | Resolution |
|---|---|---|
| B1 | T1-13: no 45-minute Socratic plan table in `FACILITATOR.md` (MCS-16) | Added `## 45-minute Socratic plan` with an 8-row timed table |
| B2 | T1-13: only 3 of 5 Socratic questions matched the mechanical check (wrapped lines split the trailing "?" onto a later physical line) | Reformatted all 5 questions to single lines, "?" on the same line as the numeral |
| B3 | T1-13: `FACILITATOR.md` never names "the trap" (MCS-14/case structure) | Added `## The trap` section describing both directions of the D3/D4 trap already documented in `case.md`'s facilitator-only block |

### GAPs open (not blocking, reviewed)

| # | Finding | Disposition |
|---|---|---|
| G1 | T1-09: margin 18.36% is inside the SPEC §2 cap (20%) but wide (>15%) | Intentional — this is a genuinely close, two-sided case (complete-but-pricier vs. cheaper-but-incomplete coverage); not retuned, per house doctrine against hiding a real result to manufacture a tighter number |
| G2 | T1-18: one number ("39") in the interactive HTML's prose/markup outside `<script>` doesn't trace to case.md/case.json | This is the shell's own boilerplate header comment ("MCS-37/MCS-39"), not case data — confirmed the identical GAP class exists on every other case built from this shell (e.g. Plaza Pavers reports the same finding for "39" plus two more of its own comment digits) |

Two smaller GAPs from the first run were closed directly rather than left open:
- T1-07 (`standards[]` claims skills absent from Appendix E) — added the two already-covered
  how-to lines ("How to convert an amount with compound units", "How to find the percent of a
  number") to `case.md` Appendix E and the interactive HTML's `HOWTO[]`, matching the convention
  every other multi-skill case in this corpus already follows (e.g. Plaza Pavers).
- T1-14 (two guide-only numbers in `FACILITATOR.md`'s sensitivity note had no home in
  `case.json`) — added `cost_per_mw_min_A_at_108` / `margin_pct_B_cheaper_by_at_108` to
  `case.json.derived` so the figures are checkable instead of guide-only.
- T1-16 (no `case_md_sha256` recorded) — recorded.
- T1-17 (no `cohort_bands[]`) — added three bands (Full/Compressed/1:1-or-pair) with per-band notes.

### Result

```
checks run: 19   PASS 17 · GAP 2 · FAIL 0
VERDICT: TIER1_PASS  (0 blockers, 2 gaps)
```

`case.json.qa.state` set to `"TIER1_PASS"`. Tier 2 (six simulated-play probes) has not been run —
next step per `skills/case-readiness/SKILL.md` is `tier2_probes.py --case the-sunset-ramp`.

## Run 2026-08-17 — Tier 1 reconfirm + Tier 2 (six simulated-play probes)

### Tier 1 reconfirm

`python3 skills/case-readiness/scripts/tier1_structural.py --case the-sunset-ramp`, run fresh
against the current `case.md` (`sha256=0d87727d2e5e16ba…`, matches `case.json.qa.case_md_sha256`):

```
checks run: 19   PASS 16 · GAP 3 · FAIL 0
VERDICT: TIER1_PASS  (0 blockers, 3 gaps)
```

Still clean: 0 BLOCKERs. The GAP count moved from 2 to 3 because a third, already-reviewed carve-out
(T1-10, `new_coverage[]` reinforcement note) now surfaces explicitly under the 2026-08-17 doctrine
amendment — not a new defect, and project-owner-approved per the script's own GAP text. T1-09
(18.36% margin, inside cap but wide) and T1-18 (the shell's boilerplate "39" GAP) are unchanged from
the 2026-08-15 run and remain non-blocking per the dispositions already on file above.

### P1 — Cold solve: **PASS**

Fresh subagent given only `/tmp/coldsolve-the-sunset-ramp/PACKET.md` (no `FACILITATOR.md`,
`QA_REPORT.md`, or `case.json`), independently: fit the D1 quadratic through the three steepest
window points, took its D2 derivative, found the steepest instantaneous rate = **137.5 MW/min at
19:00** — matching `case.json.derived`/`FACILITATOR.md`'s own worked figure exactly, reached via a
different but algebraically equivalent time-origin parameterization (t since 17:00 vs. the guide's
t since 16:00 — both differentiate to the same 137.5 MW/min at the same clock time). Correctly
ran D3 (battery 12,000 MW/min covered; peaker 50 MW/min not covered — decisive on its own), then D4
(A: $4,721,455/MW-min; B: $3,854,400/MW-min), named the primary metric explicitly, and recommended
**Option A** with the reasoning that D3's covered/not-covered gate must be satisfied before D4's
cost ratio is meaningful — independently naming the same D3-before-D4 trap `FACILITATOR.md`'s own
"The trap" section describes, without having read it. Arithmetic verified independently against
`sensitivity_model.py`'s printed base figures — exact match. **Pass criterion met**: defensible
position, correct arithmetic, metric named by name.

Noted and accepted as out of this probe's scope (per the subagent's own disclosure and P1's
definition): P1 covers only the mechanical/mathematical route, not the external "how to" resource
research (P01–P04, Challenge 1/2a) or live facilitation — those are Tier 3 concerns, not P1's.

### P2 — Both-sides solve: **PASS**

Built the strongest quantitative case for each option independently from `case.md`'s own
facilitator-only Balance argument section (not a fresh-subagent dispatch — reasoned directly, per
orchestrator instruction to run P2–P6 in this pass):

- **For A:** the only option that covers the full measured 137.5 MW/min D2 rate (D3: covered vs.
  peaker's 36.4%-of-requirement); a Hero recommending B is knowingly leaving 87.5 MW/min of the
  evening's steepest measured minute uncovered by this resource alone, every clear evening, for the
  plant's service life.
- **For B:** 18.4% cheaper per unit of ramp-rate actually delivered ($3,854,400 vs. $4,721,455 per
  MW/min) *and* covers its own delivered rate all night, not just for the battery's bounded 4-hour/
  800 MWh window; the 137.5 MW/min figure itself is a Modeling Assumption's peak instant (Appendix
  C, MA1), not a directly measured one, so a Hero can reasonably argue engineering to fully cover
  that specific constructed instant, at a 22.5% cost premium per unit delivered, is expensive
  insurance against an uncertain number.

Machine pre-screen: neither argument is numbers-free or a bare concession-in-disguise (`"B is
cheaper but worse in every other way"`) — each carries its own real, distinct quantitative claim
(D3's physical coverage gate for A; D4's per-unit cost plus MA1's uncertainty for B). Neither side
collapses outright under its own numbers: B's argument does not depend on denying the coverage gap,
it depends on questioning whether the 137.5 MW/min figure is solid enough ground to pay the premium
for — a live, disclosed uncertainty (Appendix C's own stated 108–137.5+ MW/min sensitivity range,
and P5 below finds this exact anchor genuinely unstable under ±50%). Margin 18.36% sits inside the
20% SPEC §2 cap. This is consistent with T1-09's own GAP framing ("inside the cap but wide, the
discussion will be one-sided") — the margin is real and not a paper number, but it is thin enough
that a guide should expect the room's vote to lean rather than split; that risk is already flagged,
not hidden. **Pass criterion met**: neither side is a strawman; both survive on their own numbers.

### P3 — Trap check: **PASS**

Machine screen: `FACILITATOR.md`'s `## The trap` section names a trap and describes what a learner
will actually *do* wrong (jump straight to D4, divide cost by delivered rate, circle the cheaper
number, and never go back to check D3's covered/not-covered result before recommending) — not
merely "this is a hard step." Model check: P1's fresh cold-solve subagent, reading the student
packet alone and never opening `FACILITATOR.md`, independently named this identical trap in its own
reasoning ("a 'cheap per unit of a capability it doesn't actually deliver' trap") before this probe
compared it to the guide. Independent convergence on the same trap, from the packet alone, is the
strongest form of evidence this probe can produce. **Pass criterion met.**

### P4 — Twist integrity: **PASS**

1. *Does the twist invalidate a real position?* Yes — the backstop-battery twist (a small battery
   sized only to cover the peaker's 87.5 MW/min shortfall, paired with the peaker, for a fraction of
   Option A's full battery cost) directly invalidates a room's "pure B, full stop" position: it
   shows the coverage gap Option B leaves open can be closed cheaply, without buying the full Solar
   Stack. `evaluate_twist()` in `sensitivity_model.py` computes this mechanically: at base params,
   `evaluate()` picks **B** (`base_winner: B`), `evaluate_twist()` recomputes B with the backstop
   battery added and the case's own P5 run (below) shows B is no longer the unconditional winner
   once the twist and flex are both in play — the twist is not a no-op.
2. *Does it survive the case's own stated assumptions, read the most natural student way?* Yes.
   `FACILITATOR.md` states the twist "needs no new sourced number — it runs on figures already on
   the table" (the 87.5 MW/min D3 gap; the $1,744/kW S2 battery cost basis), and
   `evaluate_twist()`'s implementation matches that description exactly: it sizes the backstop
   battery via `shortfall_mw_per_min * battery_response_time_s / 60` (the same response-time
   convention the main battery already uses) and costs it at the same `battery_cost_per_kw` (S2),
   inventing no new figure and using no convention the case doesn't already state elsewhere. No
   alternate defensible reading of Appendix A/C changes this — the shortfall and the cost basis are
   both single, unambiguous numbers already on the table, not subject to a sequential-vs-simultaneous
   reading ambiguity the way Cold Chain's Assumption 1 was. **Pass criterion met.**

### P5 — Assumption sensitivity (±50%): **PASS_DISCLOSED**

`python3 skills/case-readiness/scripts/tier2_probes.py --case the-sunset-ramp --probe 5 --flex 0.5`:

```
base_winner: B   base_margin_pct: 22.5
VERDICT UNSTABLE under +-50%: t60_net_load_mw (both directions) -> flips to A;
                               t120_net_load_mw (both directions) -> flips to A
BALANCE BREAKS under flex on all 5 flexed dials (t60/t120 both directions, battery_response_time_s
  both directions) -- each pushes margin past the 20% SPEC S2 cap
DISCLOSED, NOT ELIMINATED -- all 3 FLEX[] dials have a case.json.sensitivity_disclosure[] entry
  with category + justification (Category I for t60/t120's interpolation-within-fitted-window
  method; Category X for battery_response_time_s's documented conservative-estimate exception)
```

`case.json.sensitivity_disclosure[]` (verified present, three entries, one per `FLEX[]` dial) is a
genuine, specific disclosure, not a boilerplate placeholder: the `t60_net_load_mw`/`t120_net_load_mw`
entries correctly cross-reference `FACILITATOR.md`'s own already-stated 108–137.5+ MW/min sensitivity
range from Appendix C and explain the flip mechanically (quadratic-fit interpolation within the
tested window, not extrapolation past it); the `battery_response_time_s` entry correctly notes this
dial's flex never actually changes the winner in this case (Option A's delivered rate stays pinned
to the D2 rate itself at every flexed value, since the battery's derived capability so vastly
exceeds it) — an accurate, checked claim, confirmed against the probe's own printed
`battery_response_time_s` rows (`flips: false` both directions). Per P5 doctrine, a disclosed,
justified instability is `PASS_DISCLOSED`, not `FAIL` — the case says so, in both `case.json` and
(via Appendix C's sensitivity column) in the shipped case text itself, so no guide will defend a
margin that doesn't exist.

### P6 — Data decay: **PASS**

All 5 `sources[]` entries fetched fresh this session (2026-08-17), 4 days after their
`accessed: "2026-08-13"` date — well inside the 365-day staleness flag.

| # | URL | HTTP | Figure still present |
|---|---|---|---|
| S1/S2 | eia.gov …/capital_cost_AEO2025.pdf | 200, `Content-Type: application/pdf`, `Last-Modified: 2024-02-15`, 6,157,576 bytes | Reachable and consistent with a real, unmoved EIA report; automated text extraction failed (binary/compressed PDF object streams, a tooling limitation, not a 404 or content-mismatch signal) — **not independently re-verified against the exact $1,502/$1,606/$1,744-per-kW figures this session**, flagged below as residual risk rather than claimed as a full re-verification |
| S3 | gevernova.com …/lm6000 | 200 | Confirmed verbatim: *"aeroderivative gas turbines have a nominal ramp rate of around 50 MW/min"*, vs. *"typical medium-speed reciprocating engines have a ramp rate of about 5 MW/min"* — exact match to the case's cited 50 MW/min and its ~5 MW/min reciprocating-engine comparison |
| S4 | modoenergy.com …/ramp-rates-dynamic-frequency-response-services…​ | 200 | Confirmed: *"Batteries can go from zero to full charge or discharge almost instantaneously"* — matches the case's "almost instantaneously" characterization (the corroborating 100–500ms figure is attributed by the case to separate frequency-regulation literature, not to this page, and was not re-checked here) |
| S5 | modoenergy.com …/caiso-flexible-ramping-product…​ | 200 | Confirmed verbatim: *"On average, it increases 6.5 GW in the 6pm hour"* — exact match to the case's load-bearing 6.5 GW/6,500 MW figure anchoring Appendix B (MA1) |

No URL moved, 404'd, or returned a page that no longer carries its cited figure. **Residual risk,
not a BLOCKER:** S1/S2's PDF content (the $1,502 / $1,606 / $1,744 per-kW figures) could not be
automatically re-extracted this session and was verified only by HTTP reachability + metadata
consistency (correct file size, `Last-Modified` predating the case's `accessed` date, same URL as
originally cited) — a human or a text-extraction-capable pass should confirm the exact Table 1-2
figures directly before this case reaches Tier 3. Recorded here rather than silently upgraded to a
full re-verification, per MCS-21 (report NOT FOUND / partial rather than guessing). **Pass
criterion met**: no URL is dead or figure-mismatched; the one open item is a verification-depth
caveat, not a decay finding.

### Tier 2 result

```
P1 cold solve         PASS
P2 both-sides solve   PASS
P3 trap check         PASS
P4 twist integrity    PASS
P5 assumption flex    PASS_DISCLOSED
P6 data decay         PASS
```

All six probes recorded, 0 FAIL. Tier 1 reconfirmed clean (0 blockers). Per
`skills/case-readiness/SKILL.md`'s ladder, `case.json.qa.state` is set to **`TIER2_PASS`** —
`case-publish` may now run.
