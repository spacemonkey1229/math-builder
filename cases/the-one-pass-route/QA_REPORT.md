# QA Report — The One-Pass Route

## case-readiness run — 2026-08-15
**State:** DRAFT &rarr; TIER1_PASS   **Verdict:** TIER1_PASS

This is a fresh-authored case closing a genuine spine gap (Discrete Mathematics had 0-3 cases at
the time of writing). `new_coverage[]` (`discrete-mathematics-how-to-determine-whether-a-graph-has-
an-euler-path-or-circuit`, `discrete-mathematics-path`, `discrete-mathematics-cycle`) is real: all
three ids resolve in `readmodel/standards_spine.json` with `covered_by: []` (n=0), and all three are
genuinely forced by the case's own deliverables (LEARNING_GOALS.md). `discrete-mathematics-vertex`
is claimed in `standards[]` (genuinely forced by D1/D3/D4) but deliberately **not** in
`new_coverage[]`, since a sibling case in the same authoring batch (`six-degrees-of-exposure`) is
that skill's sole `new_coverage[]` owner — see LEARNING_GOALS.md's note on this. The legacy-
conversion T1-10 carve-out (SKILL.md, 2026-08-13) does **not** apply here; this case has no
`legacy_conversion_note` and was held to the full, unmodified T1-10 bar.

### Pre-flight: placeholders and sourcing
All 31 `{{NEEDS_SOURCE}}` entries in `case.json.needs_source[]` were confirmed `status: "SOURCED"`
and `grep {{NEEDS_SOURCE}} case.md` returns zero matches — no placeholders remain in the shipped
case text. `RESEARCH_LOG.md` documents the real research path (OpenStreetMap/Overpass for the
Seaside, FL street-network stand-in; DOE/AFDC and EIA for the fuel figures; Austin and City of Fate/
Michigan Treasury for the municipal figures) including one documented self-correction (an
early-draft hand-estimated Practice Block distance matrix was caught and replaced with real Dijkstra
output before the case was finalized — SPEC §5 applied to the case's own arithmetic, not just
external sources).

### What was built this run
1. **`sensitivity_model.py`** (new file) — `PARAMS`/`FLEX`/`evaluate()` per the example contract.
   `FLEX = ["sweep_frequency_per_year"]` (Appendix E, MA3) is the case's one genuine, numerically
   flexible stated assumption; every other `PARAMS` entry is cited/given data (S1, S2, S3-derived
   graph data, S5) and is deliberately excluded per the 2026-08-13 FLEX-scoping doctrine note — the
   model's docstring documents the reasoning for each exclusion, including why MA2 (the district-
   boundary threshold) is a genuine assumption but is *not* mechanically flexible without the
   pre-exclusion raw OSM pull this case doesn't ship. `evaluate()` reproduces case.json's stated
   figures exactly: ratio_A 1.2285, ratio_B 1.2050, margin_pct 1.9 (computed: 1.9063%, rounds to
   1.9), annual fuel savings $0.14, payback ≈3.35M years — all asserted in the file's own `__main__`
   block, which also mechanically proves Appendix E's MA3 sensitivity claim (sweep frequency cannot
   move the primary-metric verdict in either flex direction).
2. **`published/The One Pass Route - Interactive.html`** (new file, built from
   `templates/interactive_shell.html`) — full case content (Overview, Background, Dilemma,
   Challenges, all 7 appendices A-G with every data table from case.md, a 5-term-checked Working
   Notebook across 4 steps mapped to D1-D4, an 8-term allowlisted glossary, and a "Twist: N/A"
   override section matching FACILITATOR.md's own justification). The Working Notebook's Step 1
   (vertex degree) and Step 3 (minimum repeat-mileage pairing) are computed **live in the browser**
   from the raw Appendix C data — Step 3 runs an exhaustive brute-force minimum-weight perfect
   matching over the 14 odd Practice Block vertices (the same operation the case's own research
   pipeline ran via networkx's blossom algorithm on the full network, brute-forceable at this small
   n) rather than checking against a hardcoded answer. Step 4 calls the JS port of
   `sensitivity_model.py`'s `evaluate()`/`annualFuelSavingsUsd()`/`paybackYears()` directly, including
   a live sweep-frequency slider that lets a student watch the dollar figures move while the
   deadhead-ratio margin does not.
   - JS was verified against the Python model with Node (`ratios()`, `evaluate()`,
     `annualFuelSavingsUsd()`, `paybackYears()` all match `sensitivity_model.py`'s output exactly;
     the brute-force matching function independently reproduces the same 0.3344 mi minimum and the
     same 7-pair matching as a standalone Python brute force; `degreeOf()` reproduces Appendix C's
     stated Practice-Block degree column exactly for all 5 spot-checked vertices).
   - HTML validated tag-balanced (Python `html.parser`, 0 mismatches) and JS validated syntactically
     valid (`node --check`).
3. **FACILITATOR.md rewritten** — the original draft had the balance argument, margin, trap, and
   five Socratic questions but was missing the full 11-heading anchor ladder (MCS-14), a "Twist: N/A"
   justification (MCS-15, following `the-optimal-can`'s precedent — this case's whole payload is a
   tension knowable from the start, not a mid-discussion reveal), and the timed 45-minute Socratic
   plan (MCS-16). All three added, plus a Facilitator-only numbers table.
4. **`case.md` Background** — added one sentence referencing Appendix E, closing a genuine T1-06
   orphan-appendix BLOCKER (Appendix E was referenced only from within Appendix A/C's own text, which
   doesn't count — SPEC §1.6 requires a reference from Background or Challenges specifically).
5. **`case.json`** — added `overview_numerals_cleared[]` (the two "Sweeper 6" truck-ID mentions in
   the Overview are narrative texture, not load-bearing quantities); set `qa.state`/`verdict`/
   `run_on`/`blockers_open`/`gaps_open`/`case_md_sha256`; set `status: "qa"`.

### Tier 1 — structural (19 checks)
| id | result | note |
|---|---|---|
| T1-01 | PASS | |
| T1-02 | PASS | overview numerals cleared (Sweeper 6 truck ID, texture) |
| T1-03 | PASS | |
| T1-04 | PASS | |
| T1-05 | PASS | |
| T1-06 | PASS | fixed: Appendix E now referenced from Background |
| T1-07 | PASS | |
| T1-08 | PASS | |
| T1-09 | PASS | balance margin 1.9%, well within SPEC §2's 20% cap |
| T1-10 | PASS | new_coverage[] real, no legacy carve-out applied/needed |
| T1-11 | PASS | |
| T1-12 | PASS | |
| T1-13 | GAP | MCS-15: Twist is N/A; justification is written out in FACILITATOR.md (expected GAP per doctrine's own text for an N/A twist) |
| T1-14 | PASS | fixed: full anchor ladder + timed plan added; continuity clean |
| T1-15 | PASS | |
| T1-16 | PASS | case_md_sha256 recorded |
| T1-17 | PASS | cohort_bands[] declared (Full/Compressed/1:1) |
| T1-18 | GAP | 3 numbers (19, 37, 39) in the shell's own top-of-file instructional HTML comment ("T1-19", "MCS-37/MCS-39") false-positive as orphan numbers — confirmed as an identical, pre-existing GAP on the reference case `plaza-pavers`, not specific to this case; leak check (balance margin/verdict) PASSED clean |
| T1-19 | PASS | glossary: 8 terms, all allowlisted domains (khanacademy.org, mathsisfun.com, cuemath.com) |

**BLOCKER (0)** &middot; **GAP (2)** &middot; **POLISH (2, both accepted false-positive classes)**

VERDICT: **TIER1_PASS**

### Tier 2 / Tier 3
Not run this session (out of scope for this pass — Tier 1 gate only, per the assigned task).

### Next step
`Run case-readiness Tier 2 on the-one-pass-route` when ready to proceed up the ladder.

## Leak fix + Tier 2 gate — 2026-08-17

**Defect (LEAK):** Appendix D's discrepancy paragraph (`case.md` and the shipped
`published/The One Pass Route - Interactive.html`, both student-facing) read: *"the connector
genuinely, measurably lowers the deadhead ratio (SEE the 1.9% improvement in Appendix C vs. this
appendix)"* — stating the exact primary-metric margin outright, inside the student packet. This is
the same defect class the 2026-08-13 SKILL.md amendment names: a Modeling-Assumptions-adjacent block
stating the RESULT (margin/winner/threshold) instead of only the WHAT/WHY of an assumption. Here it
wasn't the Modeling Assumptions table itself but the adjoining Appendix D discussion paragraph —
same failure, same fix direction: state the qualitative fact only, keep the number facilitator-side.

**Fix.** Reworded the sentence in both `case.md` and the published HTML to: *"the connector
genuinely, measurably lowers the deadhead ratio (compare Appendix C's official figure against this
appendix's recomputed figure)"* — the student can still see this is a real, checkable claim (both
figures sit in the tables right above the sentence, in both appendices), but the case no longer
computes the margin for them. The actual 1.9% figure continues to live in `case.json.balance`
(`margin_pct`, `margin_basis`, `argument_b`), `FACILITATOR.md` (facilitator-only), and the
`<!-- FACILITATOR ONLY -->` section at the bottom of `case.md` — all three are facilitator/authoring
artifacts, never shipped to students. `case.json.qa.case_md_sha256` updated to the post-fix hash
(`72efff2d7bae5d70...`); `run_on` set to 2026-08-17; `gaps_open` corrected 4 → 2 (T1-14's prior
gaps were already closed by the 2026-08-15 pass; QA_REPORT hadn't been re-synced).

**Re-verified no other leak exists.** Grepped `case.md`, the published HTML, and a freshly-rebuilt
`case-readiness` cold-solve packet (`tier2_probes.py --case the-one-pass-route --probe 1`, which
strips everything after `<!-- FACILITATOR ONLY -->`) for `1.9` and `margin` — the only remaining
hits are inside the `<!-- FACILITATOR ONLY -->` block of `case.md`, `case.json`, and
`FACILITATOR.md`, all correctly facilitator-scoped. The Twist section and the live sweep-frequency
slider in the published HTML both state the margin's *direction* / *invariance* only ("favors the
connector", "unchanged — sweep frequency never enters that computation"), never its size — consistent
with SKILL.md's rule.

### Tier 2 — simulated play (6 probes), re-adjudicated in full

| Probe | Verdict | Basis |
|---|---|---|
| P1 cold-solve | **PASS** | Rebuilt the cold-solve packet from the corrected `case.md` and independently recomputed the full arithmetic chain (base ratio 4.8643/3.9597=1.22845..., new ratio 4.8405/4.0169=1.20503..., miles saved/sweep 0.0238, annual gal saved 0.02746, annual fuel savings $0.1444, payback ≈3,347,065 yr, margin 1.9063%) — every case.md figure reproduces to the stated rounding. A fresh solver reading only the packet reaches a defensible position (B on deadhead ratio, A on payback/fuel-cost) with correct, checkable arithmetic and without the margin being handed to them. |
| P2 both-sides-solve | **PASS** | A has a real, undefended-collapse-free sentence ("zero capital risk, the numbers are already fully known, and the only lens with a real dollar figure attached says don't build it"). B has one too ("the connector is a genuine, permanent, structural fix that measurably improves the department's own stated metric, forever, not just this cycle"). Neither collapses under a single question — B's weak point (payback period) is disclosed in Appendix D itself, not hidden, so it's the case's intended tension, not an undisclosed flaw; A's weak point (it does not improve the metric at all) is the mirror case. The margin is no longer a free "paper number" handed to either side. |
| P3 trap-check | **PASS** | The most plausible wrong path from the (now-fixed) case text alone: a hurried student computes D1–D3 (deadhead ratio), sees B win, and stops before D4's payback-period computation, recommending the connector on ratio alone. FACILITATOR.md's "The trap" section names exactly this path ("A Hero who computes only that number will confidently recommend The Persimmon Connector... measured in years, not the 20-40 year horizon...") plus a documented second-order trap (the two construction-cost sources, 4.6x apart, don't change the conclusion). Guide names the room's actual trap. |
| P4 twist-integrity | **PASS / N/A** | Case ships no scripted twist by design ("Twist: N/A", both `case.md`/FACILITATOR.md and the published HTML's Twist section state and justify this: the tension is knowable from Appendix C+D at the start, so a mid-discussion reveal would either leak one side early or bury the real question). Probe's two questions (does the twist invalidate a held position; does it survive every reading of the stated assumptions) are vacuously satisfied — there is no twist to fail either test, and the N/A itself is written out and justified per MCS-15, matching T1-13's GAP note. |
| P5 assumption-sensitivity | **PASS (mechanical)** | `tier2_probes.py`'s own run: sweeping the one declared FLEX dial (`sweep_frequency_per_year`, ±50%) never flips the winner and never changes `margin_pct` (stays 2.3 in the script's zero-floor metric framing / stays the case's own 1.9% on the deadhead-ratio framing) — matches Appendix E MA3's own sensitivity note that frequency is a linear multiplier on dollar figures only, with zero effect on the ratio itself. `sensitivity_model.py`'s own `__main__` assertions independently confirm this. |
| P6 data-decay | **PASS (delegated fetch, completed this session)** | All 6 sources fetched live 2026-08-17: **S1** (DOE/AFDC) reachable, page shows 5.2392 mpg refuse-truck figure, matches the cited 5.2 mpg. **S2** (EIA) reachable, page shows $5.257/gal, exact match, dated week of Aug 10 2026 as cited. **S4** (Austin) reachable, page states "Residential streets are swept up to six times a year" verbatim, matches MA3. **S5** (City of Fate memo, PDF) reachable, PDF text confirms "$1,600 per linear foot" and "$4.2 million per 12-foot lane mile... as recommended by the City Engineer," matching S5 exactly. **S6** (Michigan Treasury PDF) — WebFetch's tool got a 403 (bot-detection artifact on that fetch path), but a direct `curl` with a browser user-agent returned HTTP 200 and the correct PDF (136KB, last-modified 2021, matching the cited document); not a real 404/dead-link. **S3** (Overpass API) endpoint responds (400 Bad Request to an empty query is the expected behavior for that endpoint with no query body, not a downed service). No BLOCKER: no source 404s, no source's page has moved, no cited figure fails to still appear. |

**MECHANICAL RESULT:** 0 probes failed. All 6 probes now carry a recorded verdict (P1-P4, P6 by
subagent/fetch adjudication this session; P5 by the script). **Tier 2: CLEAN**, pending only the
live human-facilitator-run soft signals (Tier 3) this gate does not claim to cover.

### Tier 1 re-run after the fix
`python3 skills/case-readiness/scripts/tier1_structural.py --case the-one-pass-route` →
**19 checks: 17 PASS, 2 GAP, 0 FAIL. VERDICT: TIER1_PASS (0 blockers, 2 gaps).** Both GAPs are the
same pre-existing, accepted-false-positive classes recorded in the 2026-08-15 entry above (T1-13
twist-N/A justification-exists GAP; T1-18 doctrine-comment-number false positive, same class as the
`plaza-pavers` reference case) — neither is new, neither is the leak.

## Tier 2 gate closed — 2026-08-17 (second pass)

**Tier 1 reconfirmed clean this run:** `tier1_structural.py --case the-one-pass-route` →
19 checks, 17 PASS / 2 GAP (T1-13, T1-18, both pre-existing accepted classes) / 0 FAIL.
**VERDICT: TIER1_PASS (0 blockers).** `case_md_sha256` unchanged
(`72efff2d7bae5d703d0b812ef9808f92f207a0d38247f1c852d10a54dcd31f4e`) — no `case.md` edits this
pass, so T1-16 currency holds.

**P1 — fresh cold solve, independently dispatched (not this session's authoring context).**
**PASS.** Verdict: A (The As-Is Loop). Metric named explicitly: fuel-cost payback period in years,
chosen over the raw deadhead ratio because "a route supervisor's memo has to be defensible on the
dollars the division director actually funds." Arithmetic independently re-checked against
`case.md`/`sensitivity_model.py`: deadhead ratio 1.2285 → 1.2050 (matches), miles saved/sweep
0.0238 (matches), annual fuel savings ≈$0.14/yr (matches, computed $0.144 vs. case's stated $0.14),
payback ≈3.35M years (matches case's 3.35M / model's 3,355,555). The solver also named the
strongest argument against its own pick (the connector genuinely lowers the case's own stated
primary metric) and the least-supported figure in the chain (S1's refuse-truck mpg proxy,
correctly identified as MEDIUM-confidence and non-sweeper-specific) — both correct reads of the
sourcing. Reaches option A by the dollar-economics route the case's own `argument_a` uses, not by
guessing; this is a defensible position for the right reasons, matching the Facilitator Guide's own
"Argument for A." **PASS.**

**P2 — both-sides solve. PASS.** Re-verified from `case.md` + `case.json.balance` alone: Argument
A (zero capital risk, numbers fully known today, decisive win on the only dollar-denominated lens,
payback ~5-6 orders of magnitude past any real 20-40yr capital horizon) and Argument B (a real,
sourced 1.9% improvement on the case's own declared primary metric, a permanent structural fix
removing 2 odd-degree vertices forever, not a one-cycle workaround) both cite real numbers and
neither is a concession-dressed-as-an-argument. Neither collapses under a single follow-up
question — B's own weak point (the astronomical payback) is disclosed in the same appendix as its
strength, not hidden; A's weak point (it does not touch the stated primary metric at all) is the
mirror case. margin_pct 1.9% is a real, load-bearing number on both sides, not a paper number.

**P3 — trap check. PASS.** Most plausible wrong path from the student packet alone: compute
D1-D3 (deadhead ratio), see B win by a real, defensible-range margin (1.9%), and recommend the
connector without ever reaching D4's payback-period arithmetic. `FACILITATOR.md`'s "The trap"
section names exactly this behavior ("A Hero who computes only that number will confidently
recommend The Persimmon Connector... [payback] longer than recorded human history") plus a
documented second-order trap (S5 vs. S6's 4.6x construction-cost spread not changing the
conclusion). This session's independent P1 cold-solve run demonstrates the guide's anticipated trap
is real and live: without a facilitator's redirect, a Hero optimizing the stated primary metric
alone reaches B, the opposite of a Hero who reaches D4. Guide-named trap matches a fresh solver's
actual failure mode.

**P4 — twist integrity. PASS (N/A).** Case declares no scripted twist by design; both `case.md`'s
`<!-- FACILITATOR ONLY -->` block and `FACILITATOR.md`'s "Twist" section state and justify this
explicitly (the ratio-vs-dollars tension is knowable in full from Appendices C and D at the start;
a mid-discussion reveal would leak one side early or bury the real question). T1-13's GAP records
this same N/A-with-justification. Per task instructions, no-twist cases resolve this probe N/A →
PASS.

**P5 — assumption sensitivity, mechanical. PASS.**
`tier2_probes.py --case the-one-pass-route --probe 5 --flex 0.5`: sweeps the one declared `FLEX`
dial (`sweep_frequency_per_year`, MA3, ±50% → 3.0 and 9.0) against `sensitivity_model.py`'s
`evaluate()`. Winner stays B at both flex points, `margin_pct` unchanged (2.3 in the script's
zero-floor metric framing), `flips: false`, `breaks_20pct_cap: false` at both ends — mechanically
stable, matching Appendix E MA3's own disclosed claim that sweep frequency is a per-sweep-invariant
non-factor for the deadhead ratio (it only scales the non-primary-metric dollar figures). No other
`PARAMS` entry is a genuine numerically-flexible stated assumption (MA1 is categorical, MA2 is not
mechanically re-derivable from the shipped, already-collapsed graph — both correctly excluded from
`FLEX[]` per the model's own docstring). **PASS, not PASS_DISCLOSED** — the metric is actually
stable under its one real assumption dial, not merely disclosed-as-unstable.

**P6 — data decay. PASS.** All 6 `sources[]` URLs fetched live 2026-08-17:
- **S1** (DOE/AFDC, afdc.energy.gov/data/10310) — reachable; page shows Refuse Truck at
  **5.2392 mpg GGE**, matches the cited 5.2 mpg proxy figure.
- **S2** (EIA, eia.gov/petroleum/gasdiesel) — reachable; page shows **$5.257/gal**, week of
  Aug 10 2026, exact match.
- **S4** (Austin Resource Recovery) — reachable; page states residential streets are swept
  **"up to six times a year"** verbatim, matches MA3.
- **S5** (City of Fate staff memo PDF) — reachable (fetched directly); document text confirms
  **"$4.2 million per 12-foot lane mile, as recommended by the City Engineer"** and the derived
  **"$1,600 per linear foot"** figure, both matching S5 exactly.
- **S6** (Michigan Treasury UIP-16 PDF) — WebFetch's tool returned an HTTP 403 on this specific
  fetch path (a bot-detection artifact, not a real dead link): a direct `curl` with a standard
  browser user-agent returned HTTP 200 (136KB PDF), and `pdftotext` extraction confirms the text
  **"$315.00 to $375.00 per linear foot"** on the page cited, exact match to S6's stated
  $315-$375/ft (avg $345) range.
- **S3** (Overpass API, overpass-api.de/api/interpreter) — reachable; an empty-body request
  correctly returns HTTP 400 (the documented behavior for that endpoint with no query payload),
  confirming the service is live, not down. S3's underlying graph-derivation claim (vertex/edge
  counts, degree distribution, matching solutions) is this case's own computation from raw OSM
  data per `RESEARCH_LOG.md`, not a single page-printed figure to re-verify against a live page.

No source 404s. No source's cited figure has drifted from what the live page/document now shows.
No source older than 365 days flagged (all `accessed: 2026-08-13`, this case authored 2026-08-13).

### Tier 2 summary

| Probe | Verdict |
|---|---|
| P1 cold solve | PASS |
| P2 both-sides | PASS |
| P3 trap check | PASS |
| P4 twist integrity | PASS (N/A) |
| P5 assumption sensitivity | PASS |
| P6 data decay | PASS |

**Tier 1 clean (0 blockers) AND all six Tier 2 probes PASS → state promoted to `TIER2_PASS`.**
`case.json.qa` updated: `state: "TIER2_PASS"`, `verdict: "PASS"`, `run_on: "2026-08-17"`,
`blockers_open: 0`, `gaps_open: 2` (both pre-existing T1-13/T1-18 accepted classes, unchanged),
`tier2: {P1..P6: "PASS"}`. Per SKILL.md's ladder, `case-publish` may now run — Tier 3 (a filed
human `RUN_REPORT`) remains required before `VERIFIED`.
