## case-readiness run — 2026-08-31
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Preflight
`preflight_lint.py --case the-panel-layout` — clean, no advisory findings (run before
`sensitivity_model.py` existed; no `FLEX[]` leak possible to check yet at that point).

### Tier 1 — structural (20 checks)

First run found 3 BLOCKERs and 4 GAPs. All 3 BLOCKERs fixed; all 4 original GAPs closed except two
that are correct-as-is by design (see below).

| id | result | note |
|---|---|---|
| T1-01..T1-09 | PASS | |
| T1-10 | GAP (by design) | `new_coverage[]` empty; all four `standards[]` entries already sit at `n=2` (The Curve's Turn, The Optimal Can). `case.json.reinforcement_note` added, recording every adjacent uncovered Calculus skill checked (quotient rule; Taylor series) and why this case's actual D1 differentiation (chain rule on nested log2 terms, not a top-level quotient) doesn't force any of them. Downgraded BLOCKER→GAP per the 2026-08-17 reinforcement carve-out — this is the intended, non-fixable state for a genuine second-pass case. |
| T1-11..T1-12 | PASS | |
| T1-13 | PASS (was BLOCKER x2 + GAP) | Rewrote `FACILITATOR.md`: added real `## Intro/Launch/Anchor 1-4/Data Deep Dive/Twist/Close/Lessons Learned/Standards Touched On` headings (previously only bolded prose, not real headings — MCS-14 anchor-ladder check is mechanical on `#+` headings); authored a real Twist (previously `N/A` with a note deferring it) built from the case's own D1-D3 math (x* beats both named endpoints on raw time but has no tested miss-rate figure — no new invented fact); rewrote all 5 Socratic questions as single-line, question-mark-terminated items (previously wrapped across multiple lines, so the mechanical count read 0). |
| T1-14 | PASS (was GAP) | 7, then 6, orphan numbers in `FACILITATOR.md` not found in `case.md`/`case.json`. Fixed by moving every derived figure (T(0), T(1), T(x*), x*, E(Long Reach), E(Close Reach), the quadratic's coefficients, and the rounded x*≈0.43/43% figures used in the Twist) into `case.json.derived`, and by removing two spurious "SPEC §7.4"/"MCS-25" section-number literals from headings that the number-sweep regex was misreading as data. |
| T1-15..T1-20 | PASS | No `published/` yet — POLISH only (T1-15/18/19/20), nothing to block on. |

**BLOCKER list at first run (all resolved):**
- [T1-10] `new_coverage[]` empty, no `reinforcement_note` → fixed (see above).
- [T1-13] MCS-14 anchor ladder incomplete → fixed (real headings added).
- [T1-13] MCS-15 no Twist section → fixed (real Twist authored).

`case.json.qa.case_md_sha256` (this run) = `ffbc403f1eb8362d8016379c0c83933f54bb860b93f2df7672e00ad88fa671df`

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh subagent (no other context), given only the leak-free packet, independently built T(x), solved T'(x)=0 to the same 24x²−36x+11=0 / x*≈0.4273, correctly recognized D4 (miss-rate-weighted expected time) as the graded metric rather than raw T(x), and reproduced the case's own figures to 3-4 significant figures (T(0)=4.6253, T(1)=4.6111, E(Long Reach)=4.7776, E(Close Reach)=4.8949) — reached Option B for the right reasons, named MA8 as the most sensitive assumption (matches the case's own flagged lever). |
| P2 both-sides | PASS | Fresh subagent built a real quantitative argument for both options (A: raw-time edge of 4.611s vs 4.625s / 0.3%; B: miss-weighted edge of 4.778s vs 4.895s / 2.4%) and correctly identified that A collapses first, at exactly the "what's the expected time per successful actuation once you account for retries?" question — a real, structural collapse (not a debating-skill artifact), matching MA6/MA8/MA13's disclosed sensitivity. Machine pre-screen (numeric-density check on `balance.argument_a`/`argument_b`) also now passes after those fields were rewritten with real figures. |
| P3 trap | PASS | Fresh subagent, reading case.md only, independently named the "subtler" trap the guide calls out — mistaking the interior critical point x* (which wins on raw time) for an automatically-recommendable answer without checking it can be scored on the real (miss-rate-weighted) primary metric at all. This matches `FACILITATOR.md`'s "## The trap" section's second, subtler variant. Machine pre-screen also fixed: the trap-detector's leftmost-match regex was previously latching onto an earlier, unrelated use of the word "trap" in the Sensitivity note and Launch sections (reading as a difficulty-note, not a wrong-path description) — reworded those two mentions so the first "trap" occurrence in the file is the real heading. |
| P4 twist | PASS | Fresh subagent re-derived the twist under the case's own stated assumptions, specifically testing whether MA9's linear-interpolation license (for geometry) also licenses interpolating miss rate at x* — found the case explicitly forbids this twice, by name (Appendix C's closing note and Appendix D's MA9-referencing closing paragraph), and that the case's own D1-D3 math (linear inputs → nonlinear/log output via Fitts's Law) independently undercuts the analogy. Verdict: the twist does not depend on an unstated convention; it survives the most natural adversarial student reading. One polish note (not blocking): the *general principle* behind "don't interpolate an unmodeled empirical output the way you interpolate a modeled geometric input" is stated as a conclusion twice but never crystallized as one sentence. |
| P5 sensitivity | PASS (disclosed) | `sensitivity_model.py` authored and mechanically verifies the case's own claimed flip points for MA6 (≈118.07mm vs. claimed ≈118mm), MA8 (continuous threshold ≈2.365, i.e. flips between n=2/n=3, matching the claim exactly), and MA13 (≈4.12% vs. claimed ≈4.1%) — **no discrepancy found between the case's claimed and the mechanically re-derived thresholds**, unlike the Search Box case's earlier remediation this session, where the same check found the case's own claims were wrong. A ±50% sweep of all 12 numeric Modeling Assumptions additionally found 2 more params that flip the verdict beyond the case's own 3 disclosed ones — MA1 (Confirm width, Long Reach) at −50%, and MA5 (other-controls distance, Long Reach) at +50%. All 5 unstable params (MA1, MA5, MA6, MA8, MA13) now have a `case.json.sensitivity_disclosure[]` entry (category X — invented/proprietary device, good-faith estimate within a cited plausible range — with a real justification), so the probe passes as disclosed-not-eliminated, per the 2026-08-13 doctrine amendment. |
| P6 data decay | PASS (after correction) | Web-access subagent found S1's cited DOI (`10.1007/978-3-030-49282-3_9`) resolves but to the **wrong paper** — a different, later 2020 paper by the same three authors (LNCS 12188, HCII 2020, pp. 124-142), not the cited Fitts's-Law laptop study. This is the "resolves but doesn't carry the figure" case SPEC flags as worse than a dead link. **Fixed**: corrected `case.md` Appendix E and `case.json.sources[0]` to the true DOI (`10.1007/978-3-030-23563-5_20`) and the correct LNCS volume (11573, not 11572); the author's own mirror page (`yorku.ca/mack/hcii2019.html`) is reachable and independently corroborates the exact numeric coefficients (a=699.2ms, b=171.4ms/bit, r=.9124) against its own posted regression table — the underlying figures used throughout D1-D4 are unchanged and confirmed correct; only the citation URL/volume number needed repair. Logged in `RESEARCH_LOG.md`.

### Tier 3 — human dry-run
NOT RUN

### Verified MA6/MA8/MA13 flip thresholds — mechanical vs. claimed (per the parent task's specific ask)

| Assumption | Case's own claimed flip point | Mechanically verified (sensitivity_model.py) | Discrepancy? |
|---|---|---|---|
| MA8 (count of other required controls) | "flips between n=2 and n=3" | continuous threshold n* ≈ 2.365 → flips between the integers n=2 and n=3 | **None** — matches exactly |
| MA6 (Close Reach other-controls distance) | "≈118 mm" | ≈118.07 mm | **None** — matches to the mm |
| MA13 (Close Reach other-controls miss rate) | "≈4.1%" | ≈4.12% | **None** — matches to a tenth of a point |

Unlike the Search Box case earlier this session, where the mechanical check found the case's own
prose claims about flip points were wrong, this case's three self-reported dilemma-flipping
assumptions all check out under independent computation. The one genuinely new finding from this
run is that 2 additional assumptions (MA1, MA5) also flip the verdict under a full ±50% sweep —
these were not previously flagged in the case's own prose and are now disclosed in
`case.json.sensitivity_disclosure[]`.
