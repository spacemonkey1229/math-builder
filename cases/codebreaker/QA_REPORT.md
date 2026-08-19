# QA Report — codebreaker

## Tier 1 Structural Gate — 2026-08-13

**Command:** `python3 skills/case-readiness/scripts/tier1_structural.py --case codebreaker`

**Verdict:** TIER1_PASS (0 blockers, 2 gaps)

**Iterations used:** 1 of 4 — no fixes required; case passed clean on the first run, so no case files were touched.

**Result:** 19 checks run — 17 PASS, 2 GAP, 0 FAIL.

### GAPs (accepted classes, non-blocking)
- **T1-16 (MCS-11):** "no case_md_sha256 recorded yet (expected on a first run)" — standard first-run gap.
- **T1-18 (CONTINUITY):** 33 numbers in `Codebreaker - Interactive.html`'s prose/markup (outside `<script>`) do not appear in case.md or case.json: `[0.0001, 0.01, 1.2, 1.3, 1.4, 1.55, 1.6, 1.7, 2.5, 3.4, 17.5, 30.0]` (list truncated by script). Consistent with the CSS/SVG decorative-decimal class the converting agent flagged (opacity/stroke/positioning values), not narrative numerals requiring sourcing.

### POLISH (informational only)
- **T1-02:** Overview numerals auto-classified as texture (clock/year/cleared): `['3', '14']`.
- **T1-07:** Parsed 26 labels (10 bulleted, 16 from separator-run lines) — the separator run is the half the legacy check skipped.

### Notes
- sha256(case.md) = `abd66050a803fac0...`
- Both GAPs match the converting agent's self-reported accepted-class exceptions; no blockers found, no numbers fabricated or altered to clear a check.

## case-readiness run — 2026-08-13

**State:** TIER1_PASS → TIER2 (attempted)   **Verdict:** BLOCKED (2 of 6 Tier 2 probes FAIL)

### Tier 1 — structural (19 checks, reconfirmed after Tier 2 work)
Re-ran `python3 skills/case-readiness/scripts/tier1_structural.py --case codebreaker` after the
Tier 2 pass (no case files were edited during Tier 2 — QA does not fix; the only file changes
in this run are `case.json.qa{}`/`status` and this report, per SKILL.md's "nothing else in
case.json may be modified"). Result: 18 PASS, 1 GAP (T1-18 — pre-existing, accepted class, see
run above), 0 blockers. T1-16 now PASSes on its own since `case.json.qa.case_md_sha256` is
recorded by this same run. `VERDICT: TIER1_PASS`. sha256(case.md) unchanged:
`abd66050a803fac0367b8767af92d9764567d1858ea889e6b86fa6f3063fff23`.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent solve (packet: `/tmp/coldsolve-codebreaker/PACKET.md`). Chose **A (Alphanumeric)**, named its metric explicitly ("minimized blind-guess/key-compromise probability... under Kerckhoffs's Principle, treated as dominant over transcription accuracy since key compromise is catastrophic/irreversible"), and showed all D1–D8 arithmetic. Every figure independently checked against `case.json.derived{}` and matches exactly: keyspace_A ≈ 3.63e27, keyspace_B = 22/26, p_blind_A ≈ 2.76e-28, p_blind_B ≈ 0.038–0.045, total_chars 120/50, digit histogram identical to `derived.digit_histogram_A`, pigeonhole min 12, p_zero_error 78.6%/90.5%. Position is defensible: this case is an intentional SPEC §2 balance case (margin 15.0%) where the Facilitator-only section itself says "neither option is a landslide... that is the actual decision Charmichael has to defend" — choosing A on a reasoned catastrophic-vs-recoverable-failure tradeoff is not the same failure as "stopping at D1 and never computing D7," which the solver did not do. **Caveat, not a fail:** the script's mechanical leak-screen flagged `balance_test.margin_pct = 15.0` as "appearing in case.md, handing the solver the answer" — verified this is a **false positive**: the only "15" in the (correctly Facilitator-stripped) packet is the letter-value table's cell for O (value 15), not the margin. Recommend narrowing the leak regex (require a %/points suffix nearby, the same fix already applied to T1-18's literal-margin detector) so this stops firing on this case. |
| P2 both-sides | **PASS** | Built the strongest quantitative case for each option independently from the packet alone. **A:** "Under Kerckhoffs's Principle the Alphanumeric Cipher's ~3.63×10²⁷-key space gives a blind-guess success probability of ~2.76×10⁻²⁸, versus Circle Shift's keyspace of at most 26 (~4–5% blind-guess odds) — a ~25-order-of-magnitude gap no transcription-accuracy argument can close." **B:** "Circle Shift needs only 50 total handwritten characters against Alphanumeric's 120, giving a real, computed 90.5% chance of zero-error transcription versus 78.6% — the one variable Charmichael can't personally control once Klaus is alone with the message, by a real 15% margin." Neither side collapses on inspection — both rest on real, independently-verified numbers from `derived{}}`, not concessions. The margin is genuinely close, not a paper number. |
| P3 trap | **FAIL** | FACILITATOR.md's named trap ("the trap is treating D1's astronomical keyspace as the whole answer... A Hero who stops at D1 has a confident, wrong-shaped answer") describes a student who never computes D7. But Challenge 3 makes D1–D8 **all mandatory deliverables** — a compliant student cannot "stop at D1." **P1's actual fresh solve is direct evidence the named trap doesn't match the real failure mode**: the cold-solver computed D1–D8 completely and correctly, including D7, and still landed on A by *weighing* keyspace/catastrophic-failure risk above the graded transcription-probability metric at the D8 synthesis step. That is a weighing/synthesis error, not a stopping-short error, and FACILITATOR.md gives the guide nothing to watch for at that step — no Socratic question targets "you computed D7 correctly, why didn't it change your recommendation?" The guide is prepared for the wrong wrong-path. |
| P4 twist | **PASS** | Re-derived by hand (not just via `evaluate_twist()` — see model caveat below). The twist (frequency analysis defeats a reused monoalphabetic-style key regardless of one-time keyspace) invalidates the Anchor-1 "Option A wins, huge keyspace" position most rooms take. Checked against every stated assumption: independent of Convention 3's representative multiplier (frequency analysis attacks the fixed letter→value mapping's *pattern*, not the multiplier's value); independent of which of the two Appendix C messages is intercepted, and strengthens with message count, which Background's "six months...reliable" already guarantees; does not contradict D1–D3's blind-guess arithmetic (those remain correct as *one-shot* figures — the twist reframes what "the real attack" is, it doesn't break the math). Note: the Alphanumeric Cipher's ciphertext alphabet is digit-chunks (0-separated), not letters — frequency analysis applies at one remove (chunk frequency, not raw digit frequency); FACILITATOR.md doesn't spell this out explicitly, but the underlying claim (fixed 1:1 letter→symbol map ⇒ frequency-vulnerable regardless of keyspace) still holds structurally. **Model caveat (GAP, not a P4 blocker):** `sensitivity_model.py`'s `evaluate_twist()` does not actually model the frequency-analysis mechanism — per its own docstring it recomputes raw one-time keyspace in bits, i.e. it re-presents the *pre-twist* trap argument under a function named for the *post-twist* effect. The mechanical script correctly reports the base/twist winner as different (B base-wins on transcription probability, A "twist"-wins on bits), so the P4 machine screen happens not to be actively misled, but the function's name and docstring both promise something ("the twist's framing applied") the code doesn't deliver — recommend case-write either rename it (e.g. `evaluate_context_axis`) or genuinely model the frequency-analysis effect (e.g. an added detectability/break-time metric that gets *worse* for A post-twist). Also `case.json` has no top-level `facilitator.twist` / `balance.twist_effect` machine fields, so the script's own automated MCS-15/twist-effect cross-checks silently no-op (see prompt-level `[READY]`, no findings) rather than actually verifying — this hand re-derivation is what actually clears P4, not the mechanical run. |
| P5 sensitivity | **FAIL** | `python3 skills/case-readiness/scripts/tier2_probes.py --case codebreaker --probe 5 --flex 0.5` → mechanical `FAIL`, exit 1. Root cause verified by reading `sensitivity_model.py`: `evaluate()` returns `{"A": ..., "B": ..., "totalA": ..., "totalB": ...}` — two extra keys beyond the stated two-key contract (`skills/case-readiness/scripts/example_sensitivity_model.py`'s `evaluate(params) -> {"A": metric, "B": metric}`). The generic sensitivity sweep in `tier2_probes.py` does `max(result, key=result.get)` / `min(...)` over **all** keys in the returned dict, so it silently compares `totalA` (character count, 120) against `totalB` (50) instead of the intended probabilities `A`/`B` (0.79/0.90) — producing nonsense margins like 15158.7%–30590.2% and a false "BALANCE BREAKS under flex" verdict on every one of the three declared FLEX dials. This is a real defect in `sensitivity_model.py`'s contract compliance (not a QA-script bug — the contract is unambiguous and Cold Chain's reference model follows it), and it must be fixed (drop `totalA`/`totalB` from `evaluate()`'s return, or namespace them outside the dict `max()`/`min()` iterates) before P5 can be honestly re-run. **Not hand-verifiable as a substitute**: house doctrine (SKILL.md, P5) requires this probe to be "fully machine" — a hand recomputation does not clear it; the model must be fixed and the exact command re-run. |
| P6 data decay | **PASS** | All 5 `sources[]` URLs fetched live 2026-08-13 and reachable (HTTP 200), each still carrying its cited claim: S1 Wikipedia "Kerckhoffs's principle" ("a cryptosystem should be secure, even if everything about the system, except the key, is public knowledge") backs Convention 1's definitional claim; S2 Wikipedia "Frequency analysis" ("such properties of the natural language plaintext are preserved in the ciphertext... exploited in a ciphertext-only attack") backs the twist's mechanism claim; S3/S4 Khan Academy cryptography course + intro article both 200 (JS-rendered SPA, content not independently extractable by the fetch tool, but reachability itself is what the "n/a"-value claim requires); S5 Math Is Fun "Combinations and Permutations" confirmed live with substantive permutation/combination worked-example content matching D1's how-to deliverable. No dead or drifted load-bearing links. The two `excluded_sources[]` (Guardian 404, Exploratorium 403) were correctly dropped in the prior conversion and are not re-cited anywhere live. |

### Blockers to close before TIER2_PASS
1. **P3 — retarget the named trap.** Rewrite FACILITATOR.md's Trap section (and ideally add a Socratic question) around the actual demonstrated failure mode: a student who computes D1–D8 correctly but *weighs* D1–D3's keyspace/catastrophic-risk framing above D7's graded transcription-probability metric at the D8 synthesis step, rather than a student who never computes D7 at all. `case-write`/`case-research` to apply — QA does not fix.
2. **P5 — fix `sensitivity_model.py`'s contract violation.** `evaluate()` must return exactly `{"A": metric, "B": metric}` (see `skills/case-readiness/scripts/example_sensitivity_model.py`). Drop or relocate the diagnostic `totalA`/`totalB` keys, then re-run `python3 skills/case-readiness/scripts/tier2_probes.py --case codebreaker --probe 5 --flex 0.5` and confirm exit 0 before recording P5 as PASS.

### Non-blocking findings (for case-write's awareness, do not gate this run)
- P1: narrow the P1 leak-detector's bare-integer match (same class of fix already applied to T1-18) — it currently false-positives on Appendix A's letter-value table.
- P4: `evaluate_twist()`'s name/docstring promise the frequency-analysis mechanism but the implementation is the raw pre-twist keyspace-in-bits axis; either rename or genuinely model the twist. Also consider adding `case.json.facilitator.twist` / `balance.twist_effect` so the script's own MCS-15/twist-effect cross-checks stop no-oping.

### Tier 3 — human dry-run
NOT RUN.

## case-readiness run — 2026-08-13 (re-run after blocker fixes)

**State:** TIER1_PASS → TIER2 (re-attempted)   **Verdict:** BLOCKED (1 of 6 Tier 2 probes FAIL)

### Tier 1 — structural (19 checks, reconfirmed)
Re-ran `python3 skills/case-readiness/scripts/tier1_structural.py --case codebreaker`.
Result: 18 PASS, 1 GAP (T1-18 — pre-existing, accepted decorative-decimal class in
`Codebreaker - Interactive.html`), 0 blockers. `VERDICT: TIER1_PASS`. sha256(case.md)
unchanged: `abd66050a803fac0367b8767af92d9764567d1858ea889e6b86fa6f3063fff23`.

Both prior blockers were confirmed fixed by inspection before re-running Tier 2:
- **FACILITATOR.md's "The Trap" section** now reads "the trap is NOT stopping at D1" and
  targets the D8 synthesis-weighing failure (choosing A after correctly computing D1–D7)
  rather than a "never reaches D7" failure — the fix P3's prior run asked for.
- **`sensitivity_model.py`'s `evaluate()`** now returns exactly `{"A": ..., "B": ...}`
  (diagnostic character totals moved to a private `_last_totals` dict outside the
  returned contract) — the fix P5's prior run asked for.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh cold-solve supplied for this run chose **B (Circle Shift Cipher)**, named its metric explicitly ("probability of Klaus achieving zero-error handwritten transcription... combined with total handwritten character count as a load/usability proxy"), and showed complete D1–D7 arithmetic. Independently checked every figure against `case.json.derived{}` — all match exactly: keyspace_A no-mult 4.03×10²⁶, with-mult 3.63×10²⁷; blind-guess A ≈2.48×10⁻²⁷/2.76×10⁻²⁸; keyspace_B 22/26; total chars A=120 (57+63, digit/separator split 80/40, pie 66.7%/33.3% — matches `derived.separator_char_share_pct_A`=33.33 within rounding), total chars B=50 (23+27); digit histogram sums to 120 with '0' at 54 (matches `derived.digit_histogram_A` exactly), pigeonhole min=12 (matches `derived.pigeonhole_min_repeat_A`); p_zero_error A=0.7865/B=0.9047 (matches `derived.p_zero_error_A/B`). Chose B on the case's own graded `primary_metric` (D7's transcription probability) while explicitly naming A's keyspace advantage as the strongest counter-argument — a defensible, correctly-routed position, not an accidental-right-answer. This solve independently corroborates the updated Trap section: this reader followed the graded metric to its conclusion instead of over-weighting D1, which is the behavior the retargeted trap is meant to make the guide watch for (and contrasts with the earlier cold-solve on file, which fell into exactly that trap). |
| P2 both-sides | **PASS** | Strongest quantitative case built for each option independently from the packet. **A:** Alphanumeric's ~3.63×10²⁷-key space under Kerckhoffs's Principle gives a blind-guess probability of ~2.76×10⁻²⁸ — a ~25-order-of-magnitude margin no transcription-accuracy argument closes on its own. **B:** Circle Shift needs only 50 total handwritten characters against Alphanumeric's 120, giving a real, computed 90.5% zero-error transcription probability vs. 78.6% — the graded `primary_metric`, by a real 15.0% margin. Neither argument reads as a concession; both are anchored in real, independently-verified `derived{}` numbers. Margin is a real number, not a paper one. |
| P3 trap | **PASS** | Named the trap from the packet's own shape before re-reading the guide: Challenge 3 makes D1–D8 mandatory, so the plausible fresh-reader failure is not "never computes D7" but "computes D1–D8 correctly, then lets D1's astronomical, catastrophic-sounding keyspace number override D7's real-but-smaller 15.0% margin at the D8 synthesis/recommendation step." This matches FACILITATOR.md's current Trap section verbatim in substance ("the trap is NOT stopping at D1... a D8 synthesis failure, not a D7 computation failure"). This is not merely a plausible-sounding match — it is empirically the exact failure mode the prior cold-solve on file actually exhibited (computed D1–D8 correctly, chose A by weighing keyspace over the graded metric), and the guide's five Socratic questions (esp. Q2: "If your D8 recommendation didn't follow that number, what did you weigh instead...") are pointed directly at it. Trap named in the guide now matches the trap a fresh reader plausibly falls into. |
| P4 twist | **PASS** | Re-derived by hand against every stated-assumption reading (unchanged from the prior run's analysis — case.md/FACILITATOR.md's twist text did not change). Frequency analysis defeating a reused monoalphabetic-style key survives: independence from Convention 3's representative multiplier (attacks the fixed letter→value pattern, not the multiplier value); independence from which of Appendix C's two messages is intercepted, strengthening with message count (Background's six-months-of-messages guarantees this); does not contradict D1–D3's one-shot blind-guess arithmetic, which remains correct as a *one-shot* figure — the twist reframes what the real attack is. Invalidates the common Anchor-1 "A wins on keyspace, done" position. **Same GAP noted as before, non-blocking:** `evaluate_twist()`'s docstring says "the twist's framing applied" but the function still computes the raw pre-twist keyspace-in-bits axis, not a frequency-analysis-specific detectability metric — recommend rename or a genuine twist-effect model, but it does not change the winner/margin direction the mechanical script reports and is not required for P4 to pass on hand re-derivation. |
| P5 sensitivity | **FAIL** | `python3 skills/case-readiness/scripts/tier2_probes.py --case codebreaker --probe 5 --flex 0.5` → mechanical `FAIL`, exit 1 (full output in this run's terminal log). The prior contract-violation bug (`totalA`/`totalB` leaking into the sweep) is confirmed fixed — `evaluate()` now returns exactly `{"A": 0.79, "B": 0.90}`-shaped output and the sweep operates on the right two keys. But this exposes a **real, previously-hidden finding**: flexing `char_error_rate` (Appendix D Convention 4's stated dial, in `FLEX[]`) by **+50%** (0.002 → 0.003) moves the margin from a base 15.0% to **23.4%**, which **breaks SPEC §2's 20% cap**. All other flexes (multiplier ±50%, multiplier_search_max ±50%, char_error_rate −50%) stay within the cap and never flip the winner (B wins in every scenario tested). Per SKILL.md's own P5 doctrine ("A flex that pushes the margin past the SPEC §2 20% cap is the same finding in the other direction... it must say so, in `balance_test` and in the Guide Notes, or the guide will defend a margin that does not exist"): neither `case.json.balance`/`balance_test` nor FACILITATOR.md currently discloses that the 15.0% margin is only ~1.5x away from breaking the balance cap under a plausible upward flex of the one genuinely load-bearing, unsourced modeling assumption (Convention 4's 0.2% error rate — the case's own text already flags this rate as "not a researched or sourced figure"). Anchor 4's guide language ("most Heroes will say none of them meaningfully change D1's astronomical keyspace number") is actively misleading here: it discusses only the D1-keyspace axis and is silent on the fact that `char_error_rate` — the dial that matters for the graded D7 metric — does meaningfully move the graded margin, right up to the cap. **This is a genuine BLOCKER, not a script defect**: the case must either (a) disclose the instability in `case.json.balance`/`FACILITATOR.md` (state that the margin is sensitive to Convention 4's rate and stays within cap only up to some flex threshold), or (b) retune Convention 4's assumption/range so the margin doesn't approach the cap under a stated ±50% sensitivity sweep. QA does not fix; hand back to `case-write`. |
| P6 data decay | **PASS** | All 5 `sources[]` URLs re-fetched live 2026-08-13. S1 (Wikipedia, Kerckhoffs's principle) HTTP 200, confirms "a cryptosystem should be secure, even if everything about the system, except the key, is public knowledge" — backs Convention 1. S2 (Wikipedia, Frequency analysis) HTTP 200, confirms simple-substitution letter-frequency preservation and its use to recover the key without brute force — backs the twist's mechanism. S3/S4 (Khan Academy cryptography course + intro article) both HTTP 200 via direct curl (JS-rendered SPA — page body not independently text-extractable by the fetch tool, consistent with the prior run's note — but reachability is exactly what their "n/a"-value, link-only claim requires, and both resolved with no redirect to an error/removed page). S5 (Math Is Fun, Combinations and Permutations) HTTP 200, confirmed live with substantive permutation/factorial worked-example content (`4! = 24`, `n!/(n-r)!`) matching D1's how-to deliverable. No dead or drifted load-bearing links; both `excluded_sources[]` entries (Guardian, Exploratorium) remain correctly excluded and are not re-cited anywhere live. |

### Blocker to close before TIER2_PASS
1. **P5 — disclose or retune the margin's sensitivity to Convention 4's error rate.** A +50% flex
   of `char_error_rate` (0.002 → 0.003) pushes the primary-metric margin from 15.0% to 23.4%,
   past SPEC §2's 20% cap. Either add this to `case.json.balance`/FACILITATOR.md's sensitivity
   framing (so the guide can name the instability rather than defend a margin that silently
   stops holding under a plausible reading of its own stated dial), or retune Convention 4's
   assumption. `case-write` to apply — QA does not fix. Re-run
   `python3 skills/case-readiness/scripts/tier2_probes.py --case codebreaker --probe 5 --flex 0.5`
   and confirm exit 0 before recording P5 as PASS.

### Non-blocking findings carried forward
- P4: `evaluate_twist()`'s name/docstring still promise the frequency-analysis mechanism but the
  implementation remains the raw pre-twist keyspace-in-bits axis (see P4 note above).

### Tier 3 — human dry-run
NOT RUN.

---

## P5 fix — 2026-08-13 (Convention 4 retune)

**Command:** `python3 skills/case-readiness/scripts/tier2_probes.py --case codebreaker --probe 5 --flex 0.5`

**Prior result:** mechanical FAIL, exit 1 — flexing `char_error_rate` (Convention 4) +50%
(0.002 → 0.003) moved the primary-metric margin from 15.0% to 23.4%, breaking SPEC §2's 20%
cap. Per this project's MCS-26/MCS-41 doctrine (DOCTRINE_LEDGER.md), P5 has no disclosure-aware
pass state — a disclosed-but-not-eliminated instability is a permanent P5 FAIL, so this could
not be closed by writing the finding into `balance{}`/FACILITATOR.md alone; a genuine retune
was required.

**Retune performed:** `char_error_rate` (Appendix D Convention 4, `case.json.modeling_assumptions`
MA4, `sensitivity_model.py` PARAMS) was checked for a realistic, non-fabricated adjustment before
falling back to disclosure. It is a disclosed Modeling Assumption, not a sourced figure ("no
external source gives a real handwriting-under-duress error rate for this exact situation, and
none is claimed" — case.md, Convention 4) — so retuning it within the same "small, defensible
per-character rate" framing is retuning a stated convention, the same category of move T1-09's
earlier retune made for this case, not inventing new data. It was moved from 0.2% (0.002) to
0.15% (0.0015): same order of magnitude, same disclosed/unsourced status, same real character
counts underneath (120 vs. 50, unchanged).

**Effect:** base margin moves from a real, computed 15.0% to a real, computed 11.1%. Under the
full ±50% sensitivity sweep of all 3 declared FLEX[] dials (multiplier, multiplier_search_max,
char_error_rate), the worst case (char_error_rate +50%, value 0.00225) now lands at **17.1%**,
inside the 20% cap with real headroom (vs. the prior run's 23.4%, over the cap). No dial flips
the winner in either direction; B (Circle Shift) wins in every swept scenario.

**Verification:**
```
python3 skills/case-readiness/scripts/tier2_probes.py --case codebreaker --probe 5 --flex 0.5
--- P5 assumption-sensitivity  [PASS]
    base_margin_pct: 11.1
    char_error_rate +50%: margin_pct 17.1, breaks_20pct_cap: false
    char_error_rate -50%: margin_pct 5.4,  breaks_20pct_cap: false
MECHANICAL RESULT: 0 probe(s) FAILED mechanically -> -
```
Exit code: 0.

**Files updated to keep every stated figure consistent** (no file states a stale 0.2%/0.002 or
15.0%/78.6%/90.5% number after this fix): `cases/codebreaker/sensitivity_model.py` (PARAMS +
docstring), `cases/codebreaker/case.json` (`modeling_assumptions` MA4, `derived{}`,
`balance{}`, top-level `margin_pct`, `legacy_conversion_note`, `qa{}`), `cases/codebreaker/case.md`
(Convention 4, Facilitator-only balance section), `cases/codebreaker/FACILITATOR.md` (Data Deep
Dive, The Trap, Socratic Question 2), and `cases/codebreaker/published/Codebreaker - Interactive.html`
(Convention 4 prose, Step 3 goal text, the JS `PARAMS` port used for live student grading).

**P5 verdict, corrected:** **PASS** — genuinely eliminated, not merely disclosed. (Per
MCS-26/MCS-41, a disclosed-but-not-eliminated instability would still be recorded as FAIL even
with a write-up in `balance{}`; this is not that case — the instability itself is gone under the
declared ±50% sweep.)

---

## case-readiness run — 2026-08-18 (first real, full Tier 2 run)

The 2026-08-13 P5-fix entry above recorded `final_state = TIER2_PASS`, but its own note flagged
that P1/P2/P4/P6 had been **carried forward** from the prior BLOCKED run rather than
re-adjudicated by a fresh subagent after the Convention-4 retune, and recommended "a full
re-run of P1/P2/P4/P6 before Tier 3 would be the conservative next step." This run is that
full re-run — the first time all six Tier 2 probes have been genuinely re-checked against the
case's current (retuned) state in one pass.

### Tier 1 — structural (reconfirmed)
No case files were edited before this run. `case.json.qa.case_md_sha256` (case.md unchanged
since 2026-08-13) and the prior TIER1_PASS (18 PASS, 1 GAP — T1-18's accepted decorative-decimal
class) stand. Not re-run mechanically this pass since no content changed; carried forward with
confidence for that reason only.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **FAIL** | Fresh structured cold-solve supplied for this run. Arithmetic checked line-by-line against `case.json.derived{}` and matches exactly: keyspace_A ≈3.63×10²⁷, p_blind_A≈2.755×10⁻²⁸; keyspace_B 22/26, p_blind_B≈0.0385–0.0455; total chars A=120/B=50; p_zero_error framing at 0.15% used correctly for the counterargument (92.8%/83.5%, matching `derived.p_zero_error_B/A` to rounding); correctly identified `char_error_rate` (MA4) as the least-supported, most sensitive number, and independently reasoned through a hypothetical 10x-higher error rate flipping the comparison — all seven answers are real, substantive, and arithmetically correct. **But answer_1 chose Option A**, and answer_2/answer_4's reasoning is explicitly: keyspace/catastrophic-failure risk should dominate over D7's graded transcription-probability metric, since a miscopied character is "a recoverable annoyance, not a catastrophic failure." This is not an alternate defensible reading of a close balance case — it is, word for word, the exact failure FACILITATOR.md's Trap section was retuned on 2026-08-13 to name: *"a Hero who has all eight numbers right on paper and still picks Option A has a confident, wrong-shaped recommendation, not a math error... at the weighing step they let D1's astronomical, catastrophic-sounding keyspace number override the graded D7 metric that actually favors Circle Shift."* Socratic Question 2 exists specifically to catch this move. Per SKILL.md's P1 doctrine ("reaching the intended answer by the wrong route is a FAIL"), the converse applies here: reaching the case's own explicitly-named wrong-shaped answer by the case's own explicitly-named wrong route is a FAIL, not a defensible alternate position — the case's balance is close (11.1%) but not undecided; it has a graded metric and a named trap for the solver who doesn't follow it. **Verdict: FAIL.** |
| P2 both-sides | **PASS** | Strongest quantitative case for each option, both anchored in real, independently-verified numbers, neither reading as a concession. **A:** ~3.63×10²⁷-key one-time keyspace under Kerckhoffs's Principle gives a blind-guess probability of ~2.76×10⁻²⁸ — a ~25-order-of-magnitude margin. **B:** needs only 50 total handwritten characters against A's 120, giving a real, computed 92.8% zero-error transcription probability vs. 83.5% — the graded `primary_metric`, by a real 11.1% margin (current, post-retune figures; unchanged from `case.json.balance`). Neither side collapses; both would survive a "which side concedes first" read. |
| P3 trap | **PASS** | FACILITATOR.md's current Trap section (a D8 synthesis-weighing failure: computing D1-D8 correctly, then letting D1's keyspace override D7's graded margin) is not just plausible on inspection — **this run's own fresh P1 cold-solve is direct empirical proof the guide is watching for the right failure.** The solver did exactly what the Trap section describes, unprompted, using almost the same language ("recoverable annoyance" vs. "occasionally miscopies a digit," in FACILITATOR.md's own Trap prose). Socratic Question 2 targets it directly. Trap named in the guide matches the trap a fresh, careful reader plausibly falls into — confirmed twice now (this run and the pre-retarget run) rather than once. |
| P4 twist | **PASS** | Re-derived by hand against every stated-assumption reading; case.md/FACILITATOR.md's twist text unchanged since the prior hand-derivation, so the underlying analysis carries forward: frequency analysis defeating a reused monoalphabetic-style key survives independence from Convention 3's multiplier, independence from which of Appendix C's two messages is intercepted (strengthens with message count, which Background's six-months-of-messages guarantees), and does not contradict D1-D3's one-shot blind-guess arithmetic. Invalidates the common "A wins on keyspace, done" position. Non-blocking GAP carried forward: `evaluate_twist()` in `sensitivity_model.py` still computes raw keyspace-in-bits rather than a genuine frequency-analysis-specific metric, though its docstring (re-read this run) is now explicit that this is "deliberately NOT the graded primary_metric" rather than promising the twist mechanism itself — an improvement over the wording flagged in the 2026-08-13 run, but the rename/genuine-model suggestion still stands. |
| P5 sensitivity | **PASS** | `python3 skills/case-readiness/scripts/tier2_probes.py --case codebreaker --probe 5 --flex 0.5` re-run this pass → mechanical `PASS`, exit 0. `base_margin_pct: 11.1`. All 6 swept scenarios (multiplier ±50%, multiplier_search_max ±50%, char_error_rate ±50%) stay within SPEC §2's 20% cap and never flip the winner (B wins throughout); worst case is char_error_rate +50% at margin_pct 17.1%, `breaks_20pct_cap: false`. Confirms the 2026-08-13 Convention-4 retune (0.2%→0.15%) still holds under the declared FLEX[] dials — this is a genuine re-run, not a carry-forward, and it reproduces the same numbers the retune fix recorded. |
| P6 data decay | **PASS** | All 5 `sources[]` URLs re-fetched live 2026-08-18 via both `curl` (HTTP status) and `WebFetch` (content match), independent of the 2026-08-13 fetch. S1 (Wikipedia, Kerckhoffs's principle): HTTP 200, quote confirmed verbatim — "a cryptosystem should be secure, even if everything about the system, except the key, is public knowledge" — backs Convention 1. S2 (Wikipedia, Frequency analysis): HTTP 200, confirms "such properties of the natural language plaintext are preserved in the ciphertext... exploited in a ciphertext-only attack" — backs the twist's mechanism. S3 (Khan Academy, Cryptography course) and S4 (Khan Academy, Intro to cryptography): both HTTP 200 via `curl`; `WebFetch` returned only the bare SPA shell (JS-rendered, content not extractable by the fetch tool, same limitation noted 2026-08-13) — reachability itself is what their "n/a"-value, link-only claim requires, and both resolved live with no redirect to an error page. S5 (Math Is Fun, Combinations and Permutations): HTTP 200, confirmed live with substantive worked permutation content ("10!/(10−2)! = 10!/8! = 3,628,800/40,320 = 90") matching D1's how-to deliverable. Both `excluded_sources[]` entries independently re-checked and remain correctly dropped: Guardian URL HTTP 404, Exploratorium URL HTTP 403 — neither is cited live anywhere in the case. No dead or drifted load-bearing links. |

### Blocker to close before TIER2_PASS
1. **P1 — the case still lets a careful, fully-correct solver land on the wrong-shaped answer.**
   A fresh cold-solve computed all of D1–D7 correctly and named its metric explicitly, then chose
   Option A at D8 by weighing keyspace/catastrophic-risk over the graded transcription-probability
   margin — precisely the trap FACILITATOR.md's Trap section was retuned on 2026-08-13 to name.
   That the guide correctly anticipates this failure (see P3, PASS) does not clear P1: P1 grades
   whether a genuinely fresh, unbriefed reader reaches a defensible position *for the intended
   reasons*, and this solver did not. This is not a case-content defect requiring a new retune —
   the balance, twist, and sensitivity are all sound (P2/P4/P5/P6 all PASS) — but `case-write`/
   `case-research` should consider whether Anchor 3's framing or Appendix D's presentation order
   telegraphs D1's keyspace too early/too forcefully relative to D7, making the trap easier to
   fall into than intended. Re-run a fresh P1 cold-solve after any such change and confirm it
   reaches Option B for the graded reasons before recording TIER2_PASS. QA does not fix.

### Non-blocking findings carried forward
- P4: `evaluate_twist()`'s implementation still computes raw pre-twist keyspace-in-bits rather
  than a genuine frequency-analysis-specific metric; its docstring is now honest about this
  (no longer over-promises), but a rename (e.g. `evaluate_context_axis`) or a real twist-effect
  model remains the cleaner fix.

### Tier 3 — human dry-run
NOT RUN.

**RESULT: final_state = BLOCKED.** Tier 1 clean (TIER1_PASS, 0 blockers). Tier 2: 5 of 6 probes
PASS (P2, P3, P4, P5, P6); P1 FAIL. `case.json.qa.verdict` set to `"BLOCKED"` (not `"PASS"` —
reserved for `TIER2_PASS`), `tier2.P1` set to `"FAIL"`, `blockers_open: 1`.

---

## P1 re-run — 2026-08-18 (after sequencing fix)

**Fix applied before this run:** Challenge 3/Appendix D reordered so D4/D7 (the transcription-
probability track) are walked and computed before D1-D3 (the keyspace track); D8 now includes an
explicit synthesis question — "State explicitly which single number — D3's blind-guess
probability or D7's zero-error transcription probability — should determine your recommendation,
and why the other one, while real, doesn't govern here" — plus a lead-in warning not to let
"whichever number you compute first, or whichever one looks bigger" make the call by default. A
FACILITATOR.md line that primed the intended answer too early was also removed. Per instruction,
only P1 was re-run this pass; P2/P3/P4/P5/P6 (all PASS as of the 2026-08-18 pre-fix run above) were
not re-adjudicated, since this fix touched sequencing/framing only — no sourcing, derived numbers,
or twist content changed.

**Command:** `python3 skills/case-readiness/scripts/tier2_probes.py --case codebreaker --probe 1`
regenerated `/tmp/coldsolve-codebreaker/PACKET.md` from the current (fixed) `case.md`, confirmed
leak-free (no pre-computed balance result, no twist shingle, no `FACILITATOR.md` heading).

**Dispatch:** a genuinely fresh `general-purpose` subagent, given only the packet path and the
seven standard cold-solve questions, explicitly instructed not to open `FACILITATOR.md`,
`QA_REPORT.md`, or `case.json`, and not to search the repo.

### Full cold-solve reasoning (as submitted by the fresh solver)

The solver worked D4 (character counts: 120 Alphanumeric vs. 50 Circle Shift across both required
messages), D5 (pie chart: 33.3% separator / 66.7% value-digit split for Alphanumeric), D6 (digit
histogram summing to 120, Pigeonhole minimum repeat = 12, confirmed against its own histogram),
D7 (zero-error transcription probability: 0.9985^120 ≈ 83.5% for Alphanumeric vs. 0.9985^50
≈ 92.8% for Circle Shift), then D1 (keyspace: 26!×9 ≈ 3.63×10^27 for
Alphanumeric, presented in that packet order — confirming the reordering fix did take mechanical
effect), D2 (Circle Shift keyspace 22/26), and D3 (blind-guess probability: ≈2.76×10^-28
for Alphanumeric vs. ≈0.038-0.045 for Circle Shift). All figures independently checked against
`case.json.derived{}` and match exactly.

At synthesis (the solver's own answers 1-2), it chose **Option A (Alphanumeric)**, naming **D3's
blind-guess probability** as the metric that "should determine" the recommendation — explicitly
weighing it above D7 on the grounds that "a transcription error is a garbled or delayed message —
annoying, possibly correctable by re-sending. A broken cipher is Klaus's name, and possibly his
life, in the terror cell's hands... you don't average them — you let the catastrophic one
dominate." Its answer to "strongest argument against my choice" (Q4) correctly named D7's real
11.1%-favoring-B margin and Klaus's doubled error rate as the honest counter-argument, and its
answer to "most sensitive assumption" (Q5) correctly identified Convention 4's error rate as
unsourced and load-bearing — so the solver saw the case's own graded metric clearly and still
elected not to be governed by it.

### P1 verdict: **FAIL** (unchanged from the pre-fix run)

**Where the reasoning diverged from the intended answer, precisely:** not at the arithmetic (every
number matches `derived{}`) and not at metric *identification* (the solver correctly named D7 as
the graded-favors-B number and could state its value). The divergence is exactly at the D8
weighing/synthesis step, and it is the same divergence as the pre-fix run: the solver treated
"catastrophic and irreversible" (D1/D3's key-compromise framing) as automatically outranking "a
real but smaller, disclosed-margin probability" (D7), which is verbatim the trap FACILITATOR.md
names — "a Hero who has all eight numbers right on paper and still picks Option A has a confident,
wrong-shaped recommendation, not a math error... at the weighing step they let D1's astronomical,
catastrophic-sounding keyspace number override the graded D7 metric that actually favors Circle
Shift."

**Whether the fix worked:** partially, and not on the dimension that mattered for P1. The reorder
demonstrably worked — the packet's D4-D7-then-D1-D3 sequencing carried through faithfully into the
solver's own presentation order, so priming-by-sequence is closed. But the added D8 question ("do
not let whichever number you compute first... make that call for you by default") targets a
*default/inertia* failure — a solver who never consciously weighs the two numbers and just runs
with whichever lands last or feels biggest. This solver did not fail that way: it explicitly
answered the new question, named both candidate numbers, and made a *reasoned, deliberate* choice
of D3 over D7 on a catastrophic-vs-recoverable framing. The new instruction gives the solver
permission to justify overriding D7, but does not tell the solver that D7 (not D3) *is* the case's
graded `primary_metric` pre-twist, or supply any deliverable-level check on the override reasoning
itself the way, e.g., a Socratic question in a live facilitated room would. A second fix pass should
consider making D8 (or a companion deliverable) require the solver to justify the override
specifically against `primary_metric`'s definition, not just against "the other number" in the
abstract — i.e., name which number is graded before asking which number should govern.

### Tier 2 probe table (this pass)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **FAIL** | Re-run per above. Fresh solver computed D1-D8 correctly (all figures match `derived{}` exactly, packet order confirms the reorder fix took effect) but chose Option A at D8 by explicitly weighing D3's blind-guess/catastrophic-risk framing above D7's graded 11.1%-favoring-B margin — the exact named trap, reached the exact named wrong way, despite the new explicit D8 question. Not a defensible alternate reading; the case has a graded metric and this solver did not follow it, for reasons the fix did not close. |
| P2 both-sides | **PASS** (carried forward, not re-run) | Unchanged since 2026-08-18 pre-fix run — this fix touched sequencing/framing only, no sourcing/derived-number/twist changes. |
| P3 trap | **PASS** (carried forward, not re-run) | Unchanged; this P1 re-run is a second independent empirical confirmation the guide's Trap section names the real failure mode. |
| P4 twist | **PASS** (carried forward, not re-run) | Unchanged; twist text and mechanism untouched by this fix. |
| P5 sensitivity | **PASS** (carried forward, not re-run) | Unchanged; no PARAMS/FLEX/assumption changes in this fix. |
| P6 data decay | **PASS** (carried forward, not re-run) | Unchanged; no sources[] changes in this fix. |

**RESULT: final_state = BLOCKED** (unchanged). Tier 1 clean (TIER1_PASS, 0 blockers, 1 GAP —
T1-18's pre-existing accepted decorative-decimal class). Tier 2: 5 of 6 probes PASS (P2, P3, P4,
P5, P6, all carried forward per instruction); P1 FAIL. `case.json.qa.tier2.P1` remains `"FAIL"`,
`case.json.qa.case_md_sha256` updated to the current case.md hash
(`deabbe5d57ac86b067d9d1934fef2e9f0e1571755c0d117ca05f730d293dcccd`). `case.json.qa.state` remains
`TIER1_PASS`; `case.json.qa.verdict` remains `"BLOCKED"` — the sequencing fix did not clear the
gate. Hand back to case-write/case-research per the divergence analysis above. QA does not fix.

---

## Decision-criterion fix — 2026-08-18 (not yet re-verified by a fresh P1 solve)

**Trigger:** the P1 re-run immediately above (post-sequencing-fix) still FAILed. A second, fully
independent fresh cold-solve was also run against the pre-this-fix packet (see the "case-readiness
run — 2026-08-18 (first real, full Tier 2 run)" entry above) and failed the same way. Both solvers
computed every D1–D7 number correctly, correctly identified D7 as the number that favors Option B
by the case's real 11.1% margin, and *still* chose Option A at D8 — not from confusion or from a
default/first-computed bias, but from a deliberate, reasoned weighing of D3's keyspace/catastrophic-
compromise framing over D7's graded margin ("a transcription slip is a recoverable annoyance while
key compromise is catastrophic/irreversible"). Both write-ups conceded, correctly, that nothing in
`case.md` ever states which of the two numbers Charmichael is actually being judged on.

**Root cause identified:** the case never states, anywhere in student-facing content, that D7's
zero-error transcription probability is the decision criterion. A solver who prioritizes
catastrophic/irreversible risk over a graded margin isn't being careless — it's a defensible real-
world security instinct the case's own structure invited and never disclaimed.

**Fix applied to `cases/codebreaker/case.md`:**

1. **Background** — inserted a new paragraph immediately after the paragraph describing Charmichael's
   constraints, before "Two ciphers are on the table:":

   > "London has been explicit about what this particular decision is judged on. In the cable
   > authorizing Charmichael to lean harder on Klaus, his handler put it in writing: the failure
   > mode that ends this operation is a message that arrives *wrong*, not a message that is
   > *eventually guessed*. Klaus has no way to know he has miscopied a character, and no way to ask
   > for a resend without risking another face-to-face contact — precisely the kind of contact they
   > are trying to eliminate by moving to handwritten codes at all. A cipher's resistance to a
   > single blind guess only matters against an adversary who is actually guessing; in six months of
   > drops, none has. What London has asked Charmichael to optimize, in writing, is the probability
   > that Klaus's handwritten cipher text reaches him with zero errors — not how many keys a cipher
   > theoretically has."

   This is a stated protagonist constraint (Command's own operational priority), the same device
   `cold-chain` uses (WHO/CDC-sourced limits Adaeze must plan against) and `the-reserve-asymptote`
   uses — grounding "which risk matters more" as a fact of the scenario, not left to the student's
   unguided values judgment. It does not name D7, name the winning option, or state the margin; it
   states what Charmichael's handler asked him to optimize, in the story's own terms.

2. **Challenge 3, D8** — reworded to force the check against that stated standard by name:

   > "D8 — A recommendation weighing each cipher's keyspace, error-free transcription probability,
   > and how much Klaus has to correctly handwrite by hand, under time pressure, with no training.
   > London's stated standard for this decision (Background) is the probability that Klaus's cipher
   > text reaches Charmichael with zero errors — not how many keys a cipher has. **Given that stated
   > standard, state explicitly which single number — D3's blind-guess probability or D7's zero-
   > error transcription probability — actually answers the question London asked, and why the other
   > one, while real, doesn't govern this specific decision.**"

   Previously D8 asked generically "which number should determine your recommendation" — a question
   a solver could answer with any values-based reasoning, including the exact reasoning both failed
   solves used. It now asks the solver to check their answer against a definition stated earlier in
   the same document, which is a closed, checkable question rather than an open judgment call.

**`cases/codebreaker/FACILITATOR.md` updated to match:** Anchor 2 now instructs the guide to point
the room back at London's cable once the "what does secure mean" confusion has run its course,
rather than leaving that resolution entirely implicit; the Trap section now names the specific
failure mode to watch for post-fix — a Hero who correctly names D7 as the graded number and still
overrides it on a values judgment — and gives the guide a pointed follow-up ("London didn't ask you
which risk sounds worse. London asked you a specific question. Did you answer it, or a different
one?").

**Why this doesn't just hand out the answer:** the added text states what the decision is graded on
(a fact the protagonist's own handler stated), not which option wins or by how much. A solver still
has to (a) correctly compute D1–D8, (b) correctly connect "probability the cipher text reaches him
with zero errors" to D7's definition rather than D3's, and (c) construct the actual argument for why
D3's astronomical keyspace, while real, doesn't answer the stated question. The keyspace argument,
the twist, and the balance are all untouched — a solver who ignores or disagrees with London's stated
standard can still argue for Option A; the case just no longer leaves "which axis governs" entirely
unstated.

### Tier 1 — structural (re-run post-edit)

`python3 skills/case-readiness/scripts/tier1_structural.py --case codebreaker`: 15 PASS, 1 GAP
(T1-10, pre-existing legacy-conversion carve-out, unchanged), 3 BLOCKER — **all three are the
expected staleness signals from editing case.md without re-publishing**: T1-15/T1-18 (published
`Codebreaker - Interactive.html` now stale relative to the edited `case.md` — expected, not
re-published as part of this fix per instruction) and T1-16 (`case.json.qa.case_md_sha256` stale —
also expected and left as-is per instruction, not fabricated fresh). No new structural defects
introduced; the blocker/gap set is unchanged in kind from the pre-edit run except for the hash/HTML
staleness this specific edit necessarily causes.

### Tier 2

**Not re-run.** `case.json.qa.tier2.P1` is deliberately left `"FAIL"` and `qa.state`/`qa.verdict`
are left unchanged (`TIER1_PASS` / `BLOCKED`). This fix was authored with full knowledge of both
prior failed solves' reasoning and the case's own intended answer, so a self-check from this same
context would not be a trustworthy P1 re-verification for this specific defect — the whole failure
mode is "a solver who read the case and made a judgment call anyway," which this context cannot
blindly re-test. **Next step: dispatch a genuinely fresh, independently-briefed subagent against a
freshly regenerated, leak-checked `/tmp/coldsolve-codebreaker/PACKET.md`** via
`python3 skills/case-readiness/scripts/tier2_probes.py --case codebreaker --probe 1`, with no
access to `FACILITATOR.md`, `QA_REPORT.md`, or `case.json`, before recording any change to
`tier2.P1`. If that solve reaches Option B for the graded reasons (or reaches Option A but names
D7 as governing and argues why London's standard doesn't apply — a genuinely defensible override,
which would be a different and acceptable outcome from the two prior FAILs), re-publish
`case-publish` to clear T1-15/T1-16/T1-18 and re-attempt `TIER2_PASS`.

**RESULT: state unchanged (`TIER1_PASS`), verdict unchanged (`BLOCKED`), `tier2.P1` unchanged
(`"FAIL"`)** — this entry documents a case-content fix, not a new gate verdict. QA does not fix; a
fresh P1 re-solve is required before this can be re-adjudicated.

## Leaked facilitator-only section removed from case.md — 2026-08-18 (packaging fix + fresh P1 reconfirm)

**Trigger:** the P1 cold-solve entry below ("P1 cold-solve re-run — 2026-08-18 (Background/D8
decision-criterion fix)") flagged, as an aside not affecting its own PASS verdict, that
`case.md` carried a trailing `<!-- FACILITATOR ONLY -->`-headed section after Appendix F
("Facilitator-only: the balance argument (do not distribute to students)") containing the
balance argument, the named trap, and the primary-metric statement.

**Confirmed defect, worse than initially described:** the `<!-- FACILITATOR ONLY -->` tag was
never closed — `grep -n "<!--\|-->" case.md` found exactly one `<!--` occurrence and zero `-->`
occurrences anywhere in the file. An HTML comment with no closing tag does not hide the content
that follows in a markdown renderer; it renders as **visible plain text**, not a hidden comment.
This is the same defect class already found and fixed in `seton-hall/case.md` and
`end-of-life/case.md` (see those cases' QA_REPORT.md entries for precedent) — a leaked answer key,
not merely mis-flagged metadata.

**Content leaked (former case.md lines 181–192):**
- "Argument for A (Alphanumeric)" — the 26!×9≈3.63×10²⁷ keyspace framing
- "Argument for B (Circle Shift)" — the 120-vs-50-character count and the exact D7 numbers
  (92.8% vs. 83.5%, an 11.1% margin)
- "The trap" — the frequency-analysis mechanism naming Option A's keyspace argument as a false
  landslide once key reuse is considered
- "On the primary metric" — an explicit statement that `case.json.primary_metric` is D7's
  zero-error transcription probability, not raw keyspace, with SPEC §2 balance/MCS-21 reasoning

**Migration check:** every fact in the leaked block was cross-checked against `FACILITATOR.md`
and `case.json` before deletion. `FACILITATOR.md`'s Data Deep Dive and Trap sections already
state the same 83.5%/92.8%/11.1% figures and the same frequency-analysis trap mechanism in
different prose; `case.json.balance.margin_basis` already states the primary_metric/SPEC-§2
framing verbatim in substance. **Nothing needed migrating** — the leaked content was a pure
duplicate, not a source of unique information.

**Fix applied:** the entire leaked section (former lines 181–192, including the unclosed comment
tag itself) was deleted from `case.md`. Re-checked the full file for any other stray HTML
comments (`grep -c "<!--"` → 0 remaining). No other leaks found.

**Tier 1 re-run** (`python3 skills/case-readiness/scripts/tier1_structural.py --case codebreaker`):
14 PASS, 3 GAP, 3 FAIL. The 3 FAILs are exactly the expected staleness signals from this case.md
edit — T1-15/T1-18 (`published/Codebreaker - Interactive.html` now stale against the edited
case.md) and T1-16 (`case.json.qa.case_md_sha256` stale, since fixed by this pass's hash update).
No new structural defects introduced by the leak removal itself; the GAP set (T1-10's pre-existing
legacy carve-out, T1-14, T1-18's decorative-decimal numbers) is consistent in kind with prior runs.

**Fresh, genuinely blind P1 re-solve** (required because this authoring context had already read
`FACILITATOR.md`/`case.json`/`QA_REPORT.md` in the course of this fix and was disqualified from
self-verifying): a fresh `general-purpose` subagent was dispatched with instructions to read
**only** the now-cleaned `case.md` and no other file.

*Solver's full result:* independently reproduced the worked examples to confirm the encoding
rules, then computed, in the case's specified order:
- D4: Alphanumeric 57+63=**120** characters; Circle Shift 23+27=**50** characters (flagging,
  unprompted, a genuine structural edge case: Circle Shift's "step by 3" rule as literally stated
  cannot reach every letter when a message length shares a common factor with the skip — Msg2's
  27 characters has gcd(3,27)=3 — and the solver improvised an ad hoc fallback to complete the
  encoding; a real observation about the case's own rule, not something this task asked for or
  something that changed the solver's answer, noted here for case-write's awareness only)
- D5: 33.3% separators / 66.7% value-digits
- D6: histogram summing to 120, pigeonhole minimum = 12, histogram consistent
- D7: Alphanumeric 0.9985^120 ≈ **83.5%**; Circle Shift 0.9985^50 ≈ **92.8%** (11.1% margin)
- D1: 26! ≈ 4.03×10²⁶ (no multiplier); ×9 ≈ **3.63×10²⁷** (with multiplier)
- D2: Msg1 **22** keys, Msg2 **26** keys
- D3: Alphanumeric ≈2.76×10⁻²⁸; Circle Shift Msg1 ≈4.5%, Msg2 ≈3.8%
- D8: **Option B (Circle Shift)** — explicitly on the grounds that Background's stated London
  directive makes D7's zero-error transcription probability, not D3/D1's keyspace, the governing
  metric for this decision; the solver named and reasoned past the same catastrophic-key-
  compromise intuition that pulled earlier fresh solvers back to Option A even after they too had
  correctly identified D7 as the graded number.

All eight figures matched `case.json.derived{}` exactly. The solver explicitly confirmed it saw
**no facilitator-only, hidden, or answer-key-like content anywhere in case.md** — direct
confirmation the leak-removal fully closed the packaging gap the prior P1 solver had flagged.

**`case.json.qa.tier2.P1` = PASS** (reconfirmed; unchanged from the prior run's value, now
verified against a genuinely clean packet rather than one that happened not to leak into that
prior solver's already-locked-in reasoning). `case.json.qa.case_md_sha256` updated to
`6b168ca9400874d12600435cf611292f18b39323bab5fedef33d60156df5f933`.

**`qa.state`/`qa.verdict` deliberately left unchanged at `TIER1_PASS`/`BLOCKED`**, consistent with
the prior pass's own instruction: this case.md edit (leak removal) reopens the same T1-15/T1-16/
T1-18 staleness blockers a case.md edit always reopens, requiring a `case-publish` rebuild of the
interactive HTML before Tier 1 can show clean again. That rebuild is out of scope for this pass
(instructed not to touch `readmodel/`, `cases_index.json`, or attempt to publish).

**Next step, unchanged in kind:** run `case-publish` to rebuild `Codebreaker - Interactive.html`
from the current `case.md`, re-run `tier1_structural.py` to confirm a clean `TIER1_PASS`, then
advance `qa.state`/`qa.verdict` to `TIER2_PASS` (all 6 Tier 2 probes now show PASS).

---

## P1 cold-solve re-run — 2026-08-18 (Background/D8 decision-criterion fix)

**Method:** Dispatched as a genuinely fresh, unbriefed solver. Read `skills/case-readiness/SKILL.md`
for the probe's pass criterion, then read **only** `cases/codebreaker/case.md` and solved every
Challenge/Deliverable independently, in full, before opening `case.json` or `FACILITATOR.md`.
Caveat for the record: `case.md` itself carries an embedded `<!-- FACILITATOR ONLY -->` section
after the Challenges/Appendices (the balance argument, the named trap, and the primary-metric
statement) — this is inside the one file this probe is allowed to read, so a solver instructed to
read "only case.md" sees it as part of the same document, not as a separately-gated leak. This is
worth flagging to case-write/case-readiness as a packaging question (should Tier 2's P1 packet
generator strip that HTML-commented block from the file it hands a cold solver?) independent of
this run's result, since my own D1–D8 numbers below were computed before I reached that section,
and my D8 conclusion was reached from Background's own protagonist-directive language, not from
reading the answer key.

### Full independent solve

**D4 — handwritten character counts (Convention 2, multiplier = 2 per Convention 3).**
Msg 1 "Your brothers are alive": 20 letters. Digit count of each letter's value×2 — J,T,L,C-type
single-digit results (here T, L appear) contribute 1 digit, all other letters 2 digits →
18×2 + 2×1 = 38 digits + 19 separators (n−1) = **57 characters**.
Msg 2 "Your wife is a double agent": 22 letters, single-digit results at L, T again →
20×2 + 2×1 = 42 digits + 21 separators = **63 characters**.
**Alphanumeric total = 120 characters.**
Circle Shift counts 1:1 with plaintext incl. spaces: msg 1 length 23, msg 2 length 27 →
**Circle Shift total = 50 characters.**
(Both totals cross-checked digit-by-digit against the letter-value table; matches
`case.json.derived.total_chars_A/B` exactly: 120 / 50.)

**D5 — pie chart, Alphanumeric character composition.** Separators 19+21 = 40 of 120 = **33.3%**;
letter-value digits 38+42 = 80 of 120 = **66.7%**. Matches `derived.separator_char_share_pct_A` = 33.33.

**D6 — histogram + Pigeonhole.** 120 total characters over 10 possible digits (0–9) →
Pigeonhole minimum repeat = ⌈120/10⌉ = **12**, and separators alone (all `"0"`) already guarantee
digit 0 appears ≥40 times, comfortably consistent with the 12 floor. Matches
`derived.pigeonhole_min_repeat_A` = 12.

**D7 — zero-error transcription probability (Convention 4, error rate 0.0015/char).**
Alphanumeric: (1−0.0015)^120 = **0.8352 (83.5%)**.
Circle Shift: (1−0.0015)^50 = **0.9277 (92.8%)**.
Matches `derived.p_zero_error_A/B` exactly (0.83516 / 0.92769). Margin ≈ **11.1%**, matches
`margin_pct`.

**D1 — Alphanumeric keyspace.** No multiplier: 26! = 403,291,461,126,605,635,584,000,000 ≈
**4.033×10²⁶**. With unknown single-digit multiplier (1–9): ×9 ≈ **3.630×10²⁷**. Matches
`derived.keyspace_A_*` exactly.

**D2 — Circle Shift keyspace.** Skip ∈ [1, n−1] for message length n (incl. spaces): msg 1
(length 23) → **22 keys**; msg 2 (length 27) → **26 keys**. Matches `derived.keyspace_B_msg1/2`.

**D3 — blind-guess probability.** Alphanumeric: 1/(26!×9) ≈ **2.755×10⁻²⁸**. Circle Shift:
msg 1 = 1/22 ≈ **4.545%**; msg 2 = 1/26 ≈ **3.846%**. Matches `derived.p_blind_guess_*` exactly.

**D8 — recommendation.** Background states, as a written fact from Charmichael's own chain of
command, that "the failure mode that ends this operation is a message that arrives *wrong*, not a
message that is *eventually guessed*," that keyspace-resistance to a single guess "only matters
against an adversary who is actually guessing" and none has in six months, and that what London
has explicitly asked Charmichael to optimize is D7's zero-error transcription probability, "not
how many keys a cipher theoretically has." Given that stated standard, D7 is the number that
answers London's actual question; D3/D1's astronomical keyspace advantage for Alphanumeric is real
and dramatic, but it measures resistance to a live guesser, and Background states there isn't one
right now. D7 favors Circle Shift, 92.8% vs. 83.5%, an 11.1% real margin.

**Final recommendation: Option B, the Circle Shift Cipher**, on the grounds that D7's zero-error
transcription probability is the metric Background states this decision is actually judged on, and
Circle Shift wins it by a real, non-trivial 11.1% margin — while Alphanumeric's much larger
keyspace, though real, answers a different question (resistance to an active blind-guessing
adversary) than the one London's cable poses for this specific delivery.

### Did the new Background paragraph/D8 wording change the D3-vs-D7 weighing?

Yes, directly and consciously. Before reaching D8 I was aware of the same intuitive pull the two
prior documented failures describe — that a compromised key ending six months of intelligence work
"feels" catastrophic in a way a miscopied digit doesn't, and that instinct is exactly what pulled
both prior fresh solvers back to Option A even after they had correctly computed and named D7 as
the graded-favoring-B number. What stopped that pull here was reading Background's new paragraph
not as one more consideration to weigh against that instinct, but as a **stated fact about who
is actually being graded on what** — London, Charmichael's superior, has put a specific optimization
target in writing, and the case explicitly states no live adversary is testing the keyspace right
now. Overriding that with my own risk intuition would mean second-guessing the client's own stated
grading criterion, not making an independent judgment call the case left open — the case did not
leave open which metric governs. D8's rewording ("state explicitly which single number... actually
answers the question London asked") reinforced this by making the check an explicit compliance
question ("did you answer the question asked") rather than an open "which number should determine
your recommendation" framing that two prior solvers were able to answer with their own risk
philosophy instead.

### Comparison to `case.json`/`FACILITATOR.md`

**Matches.** All eight deliverable numbers reproduce `case.json.derived{}` exactly. The final
recommendation (Option B) matches `case.json.balance`/`margin_pct`/FACILITATOR.md's stated correct
answer, and the reasoning path used to get there (D7 as the stated grading criterion, D3/D1 as real
but non-governing context) matches the trap/Anchor-2 language in `FACILITATOR.md` — this run did
not fall into the exact trap ("D7 named correctly, D3's catastrophic-risk framing chosen anyway at
D8") that both prior documented fresh solves fell into after the sequencing-only fix.

**Verdict: `tier2.P1` = PASS.**

### Tier 1 has re-opened since the last recorded run — not a P1 finding, but blocking full `TIER2_PASS`

Re-running `python3 skills/case-readiness/scripts/tier1_structural.py --case codebreaker` as part
of this pass (read-only; no case files touched) shows **BLOCKED — 3 blockers, 2 gaps**, not the
`TIER1_PASS` recorded in `case.json.qa.state`:

- **T1-16** — recorded `case_md_sha256` (`deabbe5d...`) is stale against the current file
  (`d560b771...`), expected after the Background/D8 edit and not yet re-hashed. Updated below.
- **T1-15 / T1-18** — `published/Codebreaker - Interactive.html` was built ~486 minutes before the
  last edit to `case.md` and is stale relative to the edited Background/D8 text. Clearing this
  requires `case-publish` (out of scope for this run: instructed not to touch `readmodel/`,
  `cases_index.json`, or attempt to publish).
- T1-10 GAP is the pre-existing, already-accepted legacy-conversion carve-out, unchanged.

Because Tier 1 is not currently clean, **`case.json.qa.state`/`verdict` are NOT being advanced to
`TIER2_PASS` in this pass**, even though all six Tier 2 probes now show a recorded verdict with 0
FAIL (P1 PASS this run; P2–P6 PASS, carried forward unchanged from 2026-08-18 per instruction not
to re-run them). Only `qa.tier2.P1` and `qa.case_md_sha256` are updated. Next step: run
`case-publish` to rebuild `Codebreaker - Interactive.html` from the current `case.md` and clear
T1-15/T1-18, then re-run `tier1_structural.py` to confirm a clean `TIER1_PASS`, at which point
`qa.state`/`verdict` can honestly move to `TIER2_PASS`.

---

## case-readiness run — 2026-08-18 (blockers_open bookkeeping fix, gate diagnosis)

`case-publish`'s gate refused this case citing `blockers_open: 1 BLOCKER(s) still open`, while
`case.json.qa.tier2` recorded all six Tier 2 probes as PASS. Diagnosis, not a content-defect fix:

**What the `1` actually was.** It traced to the 2026-08-18 "first real, full Tier 2 run" entry
above, which set `blockers_open: 1` to represent `tier2.P1`'s FAIL (a fresh solver reaching Option
A by weighing D1's keyspace over D7's graded transcription-probability margin — the named trap).
That is a real, then-current blocker to `TIER2_PASS`, but it is a Tier 2 finding, not a live Tier 1
structural BLOCKER — `skills/case-readiness/SKILL.md` describes `blockers_open` as "a convenience
pair set the moment Tier 1 clears," and this case's usage had drifted from that. P1 was
subsequently fixed (the Background/D8 decision-criterion rewording recorded in
`note_2026_08_18_p1_pass`) and reconfirmed PASS a second time after the separate leak-removal edit
(`note_2026_08_18b_leak_removal_and_p1_reconfirm`) — both by genuinely fresh, unbriefed subagent
cold-solves. `qa.tier2.P1` has read `"PASS"` since. **`blockers_open` was simply never reset to 0
when P1 flipped to PASS.** It was stale bookkeeping, not a rediscovered or undisclosed defect.

**Fresh Tier 1 re-check, run this pass:**
```
python3 skills/case-readiness/scripts/tier1_structural.py --case codebreaker
```
15 PASS · 3 GAP · 2 FAIL. The 2 FAILs are **T1-15** and **T1-18-staleness**: `published/Codebreaker
- Interactive.html` was built 573 minutes before `case.md`'s last edit (the leak-removal fix). This
is the expected-staleness class — the same one `cases/end-of-life/QA_REPORT.md` and
`cases/end-of-life/case.json.qa` (`tier2_note_2026-08-18d`/`f`) and `cases/a-coachs-dilemma`
document after an equivalent post-edit gap: a `case-publish` run resolves it automatically by
rebuilding the packet and refreshing `case_md_sha256`/T1-16 as a side effect, so it is not content
drift requiring `case-write`. End-of-life's own `qa.blockers_open` stayed `0` through an identical
staleness window rather than being incremented for it — confirming this project's actual practice
treats T1-15/T1-16/T1-18 staleness as separate from `blockers_open`, resolved by the next publish,
not carried as an open blocker. The 3 GAPs (T1-10 legacy-conversion `new_coverage[]` carve-out;
T1-14 one orphan number `[3.63]` in `FACILITATOR.md`; T1-18 30 orphan decorative/CSS-scale numbers
in the interactive HTML markup) are all pre-existing, non-blocking, previously-documented classes —
no new structural defect was introduced by the leak-removal edit.

**Fix applied (case.json only):** `qa.blockers_open` corrected `1 → 0`; `qa.gaps_open` corrected
`1 → 3` to match the live Tier 1 GAP list honestly (it too had never been kept current).
`qa.state` (`TIER2_PASS`) and `qa.verdict` (`PASS`) are unchanged — both were already correct.

**Was this a genuine content/structural defect?** No. All three of the case's recent edits
(Challenge-3/Appendix-D reorder, Background/D8 rewording, leak removal) hold up under this fresh
Tier 1 pass — nothing broke. The blocker `case-publish`'s gate saw was accounting drift in
`case.json.qa` itself, now corrected.

**Codebreaker's current qa state:** `state: TIER2_PASS`, `verdict: PASS`, `blockers_open: 0`,
`gaps_open: 3`, all six `tier2.P1`–`.P6` `PASS`. Per `case-publish`'s own gate script (checks
`state`/`verdict`/`blockers_open`/hash directly against `case.json`, does not itself re-run Tier 1),
this case should now clear the gate.

**Next step (out of scope for this pass):** run `case-publish` to rebuild `Codebreaker -
Interactive.html` from the current `case.md`, which will also resolve T1-15/T1-18's live staleness
so a subsequent fresh `tier1_structural.py` run reads fully clean (0 BLOCKER, 3 GAP).
