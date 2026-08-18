# QA Report — Cinema

## case-write conversion run — 2026-08-17
**State:** DRAFT -> TIER1_PASS   **Verdict (Tier 1):** TIER1_PASS

### Tier 1 — structural (19 checks)
Run via `python3 skills/case-readiness/scripts/tier1_structural.py --case cinema`.

18 PASS, 1 GAP, 0 BLOCKER.

| id | result | note |
|---|---|---|
| T1-01..T1-17, T1-19 | PASS | all clean after two fix passes (see below) |
| T1-18 | GAP | `[37.0, 39.0]` appear in the interactive HTML's prose/markup outside `<script>` with no home in case.md/case.json. Traced to the literal substrings "MCS-37" and "MCS-39" in the shared `templates/interactive_shell.html` boilerplate comments (the checker's number regex matches a hyphen-prefixed number, `-37`/`-39`, as a bare literal). This is not case-specific content — the same GAP is already accepted precedent on `cases/a-coachs-dilemma`'s own TIER1_PASS (see that case's `case.json.qa.note`: "1 GAP [T1-18 orphan number 39.0 in the published Interactive HTML]"). Not fixed here, consistent with precedent. |

**POLISH:** T1-07 parsed 19 vocabulary/how-to labels (11 bulleted, 8 from the middot-separated vocabulary line) — informational only.

**Fixes applied during this run** (all now PASS):
- T1-06 BLOCKER (Appendix D orphan) — added an explicit `**Appendix D**` cross-reference from Challenge 3's D3 deliverable.
- T1-07 GAP (`Addition`/`Subtraction` claimed in `standards[]` but absent from the final appendix) — added both terms to case.md's Appendix E vocabulary line.
- T1-13 GAP (0 Socratic questions detected) — the five questions were originally hard-wrapped across two lines each, so the question mark never landed on the same line as the numbered marker the checker's regex requires; reflowed each question onto a single line.
- T1-14 GAP (FACILITATOR.md's twist margin `3.21` had no home in case.json) — added `derived.twist_option_a_total`, `derived.twist_option_b_total`, `derived.twist_margin_pct` to case.json.
- T1-16 BLOCKER (stale sha256) — recomputed and updated `case.json.qa.case_md_sha256` after the case.md edits above.

### Tier 2 — simulated play (6 probes)
Run via `python3 skills/case-readiness/scripts/tier2_probes.py --case cinema`.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | NOT RUN | mechanical packet build succeeds (`/tmp/coldsolve-cinema/PACKET.md`, leak-free); requires dispatching a genuinely fresh subagent, not done in this conversion session |
| P2 both-sides | NOT RUN | mechanical pre-screen passes (packet ready); requires model adjudication, not done in this conversion session |
| P3 trap | READY (mechanical pre-screen PASS) | FACILITATOR.md's "The trap, named explicitly" section now describes a real wrong-path BEHAVIOR (leaning on review score/runtime, missing the D1 scheduling constraint) rather than a difficulty note — the mechanical screen initially FAILED twice (once because an earlier, unrelated use of the word "trap" in the Close section was matched instead of the real trap section; once because the real trap section lacked a required wrong-path verb) and both are fixed. Full adjudication (comparing an independent solver's self-named trap against the guide's) not done in this session. |
| P4 twist | NOT RUN | mechanical recompute of `evaluate()` vs `evaluate_twist()` confirms both return well-formed, differently-valued results (base B=$68,673.05 margin 2.86%; twist B=$67,873.05 margin 3.21%, same winner) — full adversarial re-derivation under every assumption-reading is written up in FACILITATOR.md's "Twist Soundness Check" but not independently re-verified by a fresh pass in this session |
| P5 sensitivity | **PASS** (fully mechanical) | `concession_top_band_estimate` (the case's one genuine stated assumption) flexed +/-50% ($25 / $75): winner stays B in both directions, margin stays 2.86% (rounds identically at 1 decimal), no 20% cap breach. No disclosure entry needed — this is a clean stable PASS, not a disclosed-instability pass. |
| P6 data decay | N/A | `sources[]` is empty by design — this case is entirely fictional scenario data (Majesty Cinemas, Emily Carlin, all six films are invented; see `case.json.legacy_conversion_note`), so there are no external URLs to check for decay. |

**Tier 2 is NOT yet TIER2_PASS** — P1, P2, P4, P6 need explicit verdicts recorded by name (P1/P2/P4 need a dispatched fresh subagent or model adjudication pass; P6 is vacuously satisfied by an empty source list but should still be recorded explicitly by a future gate run) before `case.json.qa.state` can advance past `TIER1_PASS`. This report is filed honestly at the point this conversion session's work stopped, per house doctrine (absent data — here, absent adjudication — is a first-class state, not silently assumed passing).

### Tier 3 — human dry-run
NOT RUN.

## Tier 1 gate verification run — 2026-08-17 (independent re-check)
Re-ran `python3 skills/case-readiness/scripts/tier1_structural.py --case cinema` fresh (as the gating step for the "just converted" self-report) to confirm the structural gate independently of the authoring session's own claim.

Result matches the self-report exactly, byte-for-byte on the verdict:

```
TIER 1 — STRUCTURAL   case: cinema   sha256(case.md)=62487d771d17cdf2
checks run: 19   PASS 18 · GAP 1 · FAIL 0
=== BLOCKER (0) ===
=== GAP (1) ===
 * [T1-18] CONTINUITY — 2 number(s) in Cinema - Interactive.html's prose/markup (outside <script>) appear in neither case.md nor case.json: [37.0, 39.0]
=== POLISH (1) ===
 * [T1-07] parsed 19 labels (11 bulleted, 8 from separator-run lines) — the separator run is the half the legacy check skipped
VERDICT: TIER1_PASS  (0 blockers, 1 gaps)
```

No BLOCKERs found; no fixes were needed this run. The single GAP (T1-18) matches the accepted `cases/a-coachs-dilemma` precedent already documented above and was left as-is per that precedent — GAPs are not blocking for TIER1_PASS. State confirmed: **TIER1_PASS**. 1 iteration used (0 fix iterations required).

## Tier 2 gate run — 2026-08-17

**State:** TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — reconfirmed clean
Re-ran `python3 skills/case-readiness/scripts/tier1_structural.py --case cinema` fresh before
opening the Tier 2 gate. Identical result to the run above, byte-for-byte:
`checks run: 19   PASS 18 · GAP 1 · FAIL 0`, 0 BLOCKER, GAP = T1-18 (same accepted
`a-coachs-dilemma` precedent, shared-template `MCS-37`/`MCS-39` boilerplate literal, not
case-specific). `sha256(case.md)=62487d771d17cdf2b0586bf34d3a6126a79b7441d3bd7dee9aff124c437dd054`
— unchanged since the last run; case.json's `qa.case_md_sha256` was already current.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh-subagent cold solve (dispatched outside this gating session) reached Option B ("The Revengers House") via the correct metric — "Projected weekend net profit (D5: [ticket revenue + concession revenue] − exhibition cost), per the case's own D3→D4→D5 chain and Emily's stated mandate to keep the cinema profitable" — matching the case-of-record's own `derived{}` winner and margin. Right answer, right route: the solver named the D3-D4-D5 chain, not review score or runtime (the trap). |
| P2 both-sides | **PASS** | Built each side independently from the packet's Appendix A/B/C/D data alone, then checked against `sensitivity_model.py`'s exact per-day breakdown. **Argument A** (Unicorn House): Lizzie needs only 4 daily showings vs. Revengers' 5, so Lizzie skips the single worst-attendance slot (10:30 AM) every day, and its higher $325/showing cost is partly offset by running one fewer showing/day than a naive 5-showing comparison would suggest ($1,300/day actual vs. $1,625/day naive) — a real, numbers-driven position. **Argument B** (Revengers House): Revengers costs $220/showing vs. Lizzie's $325 on every single showing, all weekend, and multiplying that gap by the large theater's 150 seats compounds it; verified directly against the model: Revengers nets **more** in the identical large theater than Lizzie would ($47,154.93 vs. $41,949.62 — a $5,205.31 gap), which is the real reason B wins, not just a cost-per-showing artifact. Neither side is a concession-phrased non-argument; both cite real dollar figures from Appendix A/B. **Where A collapses:** at the question "does Lizzie actually out-earn Revengers in the identical large theater?" — no, by $5,205.31 — which is the exact point Argument A has no rebuttal for. This matches the case's own recorded 2.86% margin: real, not a paper number. |
| P3 trap | **PASS** | Independently named the trap from the packet before reading `FACILITATOR.md`: leaning on Revengers' higher review score (9.6/10 vs. 8.4/10) and longer runtime as an implicit "deserves the big room" argument, when review score is Appendix-A data that never enters Majesty Cinemas' own attendance-capacity table (Modeling Assumption D-3) and is irrelevant to the D3-D5 arithmetic. This is exactly the trap `FACILITATOR.md`'s "The trap, named explicitly" section describes, including its second half (the D1 discovery that Revengers' 164-minute runtime plus the 90-minute complex-wide cadence requirement plus turnaround overhead make a single-theater-only schedule for Revengers' 5 required daily showings a live scheduling problem, not just a revenue one — flagged explicitly and non-hidden by case.json's `modeling_assumptions[MA1]`/case.md Appendix D-1 as a simplification D3-D5 doesn't need to reconcile with D1). Guide's named trap matches the independently-derived trap. |
| P4 twist | **PASS** | (1) The twist invalidates a real, plausible room belief — that the co-op fee "doesn't structurally favor one plan over the other by design" means it affects both plans equally; it doesn't, because the two confined movies aren't symmetric (Revengers confined = 20 fee-bearing showings all weekend at $50 each = $1,000; Lizzie confined = 16 showings = $800), so Option A's cost side gets hit harder. (2) Re-derived under both a sequential and a simultaneous reading of Appendix D's D-1 through D-5 (and case.json MA1-MA5): the twist is a flat per-showing fee added strictly after D3-D5's revenue computation and strictly on top of D-5's fixed showing counts — it never touches D-1 (five-slot model), D-2 (pricing), D-3 (uniform capacity), or D-4 (concession estimate) under any reading, sequential or simultaneous. Re-ran `evaluate()` then `evaluate_twist()` on the shipped `PARAMS` independently: base `{"A": 66764.08, "B": 68673.05}` (2.86%, B), twist `{"A": 65764.08, "B": 67873.05}` (3.21%, B) — winner unchanged, margin widens, both dicts well-formed. No reading of the stated assumptions (including the "most natural student reading" — e.g. a student who assumes the D1-actual showing count, possibly higher than the D5-modeled minimum if Revengers needs a second theater to satisfy the 90-minute cadence) produces an undefined or contradictory result; that ambiguity is itself pre-empted by MA1's explicit disclosure that D1 and D3-D5 are not required to reconcile. |
| P5 sensitivity | **PASS** (mechanical) | `python3 skills/case-readiness/scripts/tier2_probes.py --case cinema --probe 5 --flex 0.5`: base `{"A": 66764.08, "B": 68673.05}`, margin 2.9%, winner B. Sweeping the case's one declared `FLEX[]` dial, `concession_top_band_estimate` ($50, Modeling Assumption D-4, the only genuinely author-estimated number — every other `PARAMS` entry is Appendix A/B/C given data and is correctly excluded from `FLEX[]`, confirmed by inspection — no FLEX-scoping bug found): at −50% ($25.00) → `{"A": 65319.76, "B": 67188.1}`, margin 2.9%, winner B, no flip, no 20%-cap breach; at +50% ($75.00) → `{"A": 68208.41, "B": 70158.0}`, margin 2.9%, winner B, no flip, no 20%-cap breach. Genuinely STABLE — no `sensitivity_disclosure[]` entry needed, this is a clean mechanical PASS, not PASS_DISCLOSED. |
| P6 data decay | **PASS** | `case.json.sources[]` is `[]`. Confirmed by inspection this is by design, not an oversight: `legacy_conversion_note` documents that Majesty Cinemas, Emily Carlin, and all six films (with their review scores, running times, and per-showing costs) are entirely fictional — no claim in the case is a claim about a real theater, distributor, or box-office figure, the same way a word problem's numbers don't need external citation. T1-08's BLOCKER-level check (does a legacy case's "verbatim"/"publicly verifiable" claim have unbacked `sources[]`) already confirms mechanically that this case makes no such real-world-verifiable claim. Zero URLs to fetch; zero dead links; vacuously PASS, not NOT RUN. |

**All six Tier 2 probes: PASS.** Tier 1 reconfirmed clean (0 BLOCKER). **State: TIER2_PASS.**
`case-publish` may now run.

### Tier 3 — human dry-run
NOT RUN. (Not required for `TIER2_PASS`; required before the case may be marked ✅ in
`DOCTRINE_LEDGER.md`.)
