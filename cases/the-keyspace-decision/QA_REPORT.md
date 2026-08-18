# QA_REPORT — The Keyspace Decision

## case-readiness run — 2026-08-17 (Tier 2)
**State:** TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 reconfirmed
Re-ran `python3 skills/case-readiness/scripts/tier1_structural.py --case the-keyspace-decision`:
**TIER1_PASS, 0 blockers, 3 gaps** (T1-03, T1-14, T1-18 — same accepted/documented
false-positive classes as the 2026-08-15/08-17 runs above; unchanged). `sha256(case.md) =
85c0889fad2d846f931d841fbc4841806534d96846e0be524e20cf2eb2634113`.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent, packet-only, no `FACILITATOR.md`/`case.json` access. Chose **B (The Second Gate)**. Named the metric explicitly ("expected time-to-crack per dollar... the case's own D5 metric"). Showed FCP for D1 (70¹⁴, 70⁸, 36⁸, matching the packet's own worked check to the digit), the compound-unit conversion for D2, the D3 pigeonhole threshold (2,821,109,907,457 vs. 80 employees), a D4 breach-vector-weighted combination, and a D5 synthesis (≈2.08 yrs/$ for A vs. ≈123.2 yrs/$ for B — a different specific weighting from the facilitator's own 61/39 split, but an internally consistent, defensible route using D1–D5 as instructed, not a lucky guess at the label). Named the strongest counter-argument (2FA is not uniformly phishing-resistant; the AP legacy system's own login may not sit behind the 2FA gate), the most sensitive assumption (MA3, matching the case's own disclosure), an explicitly ignored figure (the narrower 13%/16%/31% Appendix C initial-vector splits, in favor of the 39% full-chain figure per the case's own stated reasoning), and the least-supported number (MA3's 0.008, explicitly flagged in Appendix E as "not sourced"). Reached the intended answer via the case's own structure, not by shortcutting to the label. |
| P2 both-sides | **PASS** | Strongest case for A: 70-char/14-length keyspace is brute-force-infeasible by any realistic measure (10¹³ yrs), modest mostly-one-time cost ($60/employee), no login friction. Strongest case for B: credential abuse appears in 39% of real breaches [S2] and password length does nothing against it; 2FA cuts that channel's takeover risk 98.56% even with a correct password [S3]; cheaper per employee ($36 vs $60). Neither side reads as a concession or as numbers-free — both are built from sourced, cited figures (D1–D4), and the case's own recorded margin is a genuine 10.1%, not a rout. Side A's real collapse point is D4 (the question "which channel do real attackers actually use"): its enormous D2 keyspace advantage is answered by the fact that channel length never touches the 39% credential-abuse share. Side B's real weak point (surfaced independently, matching P1's own counter-argument) is that 2FA is not perfectly phishing-resistant and the case never states whether the legacy AP login itself sits behind the 2FA gate. Neither side collapses outright before that question — this is a real, close balance test, consistent with T1-09's recorded 10.1% margin. |
| P3 trap | **PASS** | The trap a hurried, competent student would produce: divide D2's crack-time figures directly by cost, skipping D4's breach-vector weighting entirely — Option A "wins" by a factor of ≈70 billion (raw A ≈2.585×10¹¹ yrs/$ vs. raw B ≈3.66 yrs/$, reproduced exactly by `sensitivity_model.py`'s own `main()` trap block). `FACILITATOR.md`'s "The trap, quantified" section names this exact path, quantifies it with the same numbers, and states why it is wrong ("assumes brute force is the only attack that exists") — this is what a learner will actually do (stop at the astronomically larger keyspace and treat it as decisive), not merely a hard bit of arithmetic. The cold-solve run (P1) did not fall into it — it applied D4's weighting from the start — which is consistent with the guide's own framing of the trap as "the number a rushed pitch will report," not something every solver hits; the guide is watching for it (Twist section, Socratic question 1, Anchor 2). |
| P4 twist | **PASS** | (1) Invalidates a real position: the raw-D2-only conclusion ("Long Wall wins by ~70 billion") is the exact trap above, and a room that reaches it is invalidated once D4's weighting is applied — margin flips to a genuine, close B win (10.1%). (2) Survives the case's own stated assumptions read the most natural way: the twist's mechanism is built entirely from **sourced, cited data** — S2's 39% full-chain credential-abuse share and S3's 98.56% MFA block rate — neither of which is a flexed Appendix E assumption. `sensitivity_model.py`'s `evaluate()` confirms this: `w_credential_abuse` (0.39) and `mfa_block_rate` (0.9856) are in `PARAMS`, not `FLEX`; only MA3/MA4 are flexed by probe 5, and flexing them does not touch whether the twist's core logic (real attackers use credential abuse; length doesn't stop it) applies — it only touches the final margin's stability, which is a separate, already-disclosed P5 finding, not a twist-integrity defect. No convention the case fails to state is load-bearing for the twist itself. The AP legacy system's own capacity constraint (8-char, 36-symbol, applies to both drafts identically) does not change the twist's direction under either draft. |
| P5 sensitivity | **PASS (disclosed)** | `python3 skills/case-readiness/scripts/tier2_probes.py --case the-keyspace-decision --probe 5 --flex 0.5`: base A=5.34, B=5.94 yrs/$, margin 10.1%, winner B. Unstable under ±50%: `ma3_credential_theft_cadence` at −50% flips the winner to A (margin 78.8%, breaks the 20% cap); at +50% breaks the cap the other way (66.1%, no flip). `ma4_helpdesk_increment` at +50% breaks the cap alone (22.4%, no flip). Both parameters are recorded in `case.json.sensitivity_disclosure[]` (Category X — a real value exists at Bramwell but is not publicly measurable; both stated values are documented good-faith estimates anchored to the closest public analogue), each with a substantive justification, matching `FACILITATOR.md`'s "Tier 2 probe 5, disclosed" note. A genuine retune was attempted first (per the 2026-08-17 remediation entry above) and no setting keeps both the base margin and every ±50% flex result under the 20% cap simultaneously — the metric's reciprocal-of-a-weighted-rate structure is inherently this sensitive to its own most load-bearing dial, which is the case's intended pedagogical point (the trap, Socratic question 5). Reads PASS per the disclosure-aware pass state (2026-08-13 doctrine), not the stable-margin state — report it as such if this case is ever cited as "close and stable." |
| P6 data decay | **PASS** | All 5 `sources[]` URLs fetched live 2026-08-17 and reachable: **S1** (hivesystems.com/blog/are-your-passwords-in-the-green) — confirmed 138,675 H/s aggregate rate, bcrypt work factor 10, and the 132-year 8-character full-mix crack time verbatim. **S2** (verizon.com/business/resources/reports/dbir) — landing page reachable and confirms the 31% vulnerability-exploitation figure directly; the 39%/13%/16% credential-abuse figures sit behind the full PDF report as the case's own S2 confidence note (MEDIUM) already discloses, so cross-checked via one of the case's own cited secondary sources (descope.com/blog/post/verizon-dbir-2026), which confirms all three figures verbatim ("still on top at 39%", "credential abuse dropped to 13%... measured like last year... 16%", "31% of breaches... up 55% from 2025's 20%"). **S3** (arxiv.org/abs/2305.00945) — confirmed 98.56% (leaked-credential) and 99.22% (full population) verbatim in the abstract. **S4** (duo.com/editions-and-pricing) — confirmed Duo Essentials at $3/user/month. **S5** (bitwarden.com/pricing) — confirmed Bitwarden Teams at $4/user/month. No dead links, no drifted figures, no source older than 365 days (all accessed 2026-08-13/17). |

### case.json.qa
```
state: TIER2_PASS   verdict: PASS   blockers_open: 0   gaps_open: 3 (T1-03, T1-14, T1-18 — same
accepted/documented classes, unchanged)   tier2: {P1: PASS, P2: PASS, P3: PASS, P4: PASS,
P5: "PASS (disclosed)", P6: PASS}   case_md_sha256: 85c0889fad2d846f...2634113
```
`status` remains `"qa"`.

### Next step
`Run case-publish on the-keyspace-decision`.

## Remediation — 2026-08-17

Fixed two real, previously undisclosed defects per `skills/case-write/SKILL.md`'s 2026-08-13
Modeling-Assumptions rule and `skills/case-readiness/SKILL.md`'s Tier 2 probe 5 disclosure
mechanism:

1. **Answer-key leak in `case.md` Appendix E (student-facing).** MA3's and MA4's `Sensitivity`
   table cells stated the case's own `balance.margin_pct`/winner directly — MA3 gave the exact
   flip point (≈0.0072), the margin at the stated value and at two stress values ("at 0.008 the
   margin is 10.1%; at 0.02 it widens to 63.5%; at 0.05, to 84.9%"), and which option overtakes
   which; MA4 gave a precomputed comparative result ("moves from 5.34 to 5.71 years/$ — still
   short of Option B's 5.94"). Both are the answer key, handed to the student inside the appendix
   they are meant to use to solve the case. Rewrote both cells to state only WHAT was assumed and
   WHY it is load-bearing/uncertain, per the rule's wording ("the answer is sensitive to this
   value" — no size, direction, or threshold). Mirrored the same fix into
   `case.json.modeling_assumptions[]` (MA3/MA4 `sensitivity` fields), which had the identical
   leaked text. Confirmed `published/The Keyspace Decision - Interactive.html`'s own MA3/MA4 rows
   never carried this leak (they were already written result-free) — no change needed there.
   The full result (margin, winner, margin_basis) remains, correctly, in
   `case.json.balance`, `case.md`'s `<!-- FACILITATOR ONLY -->` Balance-argument section, and
   `FACILITATOR.md` — all facilitator-only per the rule.
2. **P5 FAILED and was undisclosed.** `tier2_probes.py --probe 5` mechanically FAILs: a ±50% swing
   on the two Appendix E assumptions that enter the primary metric
   (`ma3_credential_theft_cadence`, `ma4_helpdesk_increment`) flips the verdict (MA3 -50% → Option
   A wins, margin 78.8%) and breaks the SPEC §2 20% cap in three of the four swept directions (MA3
   -50%/+50%, MA4 +50%), with no `case.json.sensitivity_disclosure[]` entry recorded. **Attempted
   a genuine retune first**: swept MA3's base value from 0.008 up through 0.020 and MA4's base
   value from $12 up through $40 looking for a setting where both the base margin and every ±50%
   flex result stay under the 20% cap simultaneously — none exists. The primary metric is a
   reciprocal of a rate-weighted probability, so it is inherently steep in its most load-bearing
   input; damping that would require redesigning the metric, not tuning a constant, and would gut
   the case's own intended trap (MA3 is explicitly named in `case.md` as "the case's most
   load-bearing, least certain dial"). Added two `case.json.sensitivity_disclosure[]` entries,
   category **X** (a real value exists — Bramwell's true compromise rate and true help-desk cost —
   but neither is publicly measurable; both stated values are documented good-faith estimates
   anchored to the closest public analogue), each with a ≥20-character justification. Re-ran probe
   5: now reads `PASS (disclosed)`. Added a matching "Tier 2 probe 5, disclosed" note to
   `FACILITATOR.md` so a discussion lead knows the margin is not stable and can say so.
3. Refreshed `published/The Keyspace Decision - Interactive.html`'s mtime and `case.json.qa`
   (`case_md_sha256`, `run_on`) so `tier1_structural.py`'s T1-15/T1-16/T1-18 continuity checks read
   the current files — no content change was needed in the published HTML (verified it never
   carried the leaked MA3/MA4 text).

Re-ran `python3 skills/case-readiness/scripts/tier1_structural.py --case the-keyspace-decision`:
**TIER1_PASS, 0 blockers, 3 gaps** (T1-03, T1-14, T1-18 — the same accepted/documented
false-positive classes noted in the 2026-08-15 run below; unchanged by this remediation).

## case-readiness run — 2026-08-15
**State:** researched → TIER1_PASS   **Verdict:** TIER1_PASS

### Pre-checks (case-readiness runner, before Tier 1)
- Grepped `case.md` for `{{NEEDS_SOURCE}}` — **0 remaining**. All 16 placeholders enumerated in
  `RESEARCH_LOG.md` are closed (11 SOURCED, 2 ASSUMPTION-only rows resolved into MA1, 2 DROPPED
  with a documented reason, 1 the non-load-bearing remediation-deadline row).
- `case.json.standards[]` — all 5 spine ids resolve against `readmodel/standards_spine.json`.
  `new_coverage[]` = `["discrete-mathematics-pigeonhole-principle"]`, genuinely `n=0` at authoring
  time and forced by D3 (see `LEARNING_GOALS.md`'s forces test) — this is a fresh-authored case
  closing a real Discrete Mathematics spine gap, not a legacy conversion, so the T1-10
  legacy-conversion carve-out does not apply and was not invoked.
- **Found and fixed a real defect in `sensitivity_model.py`**: the file that shipped from
  case-research computed the case's own figures correctly but did **not** implement the Tier 2
  probe-5 contract at all — no `PARAMS` dict, no `FLEX` list, no `evaluate(params) -> {"A","B"}`
  function (see `skills/case-readiness/scripts/example_sensitivity_model.py`). Rewrote it to the
  contract shape. Verified the rewrite reproduces `case.json.derived`'s primary-metric figures
  exactly (`A=5.3419`, `B=5.9450`, margin `10.1%`) and the disclosed MA3 flip point
  (`≈0.007181`, matching Appendix E's stated `≈0.72%`).
- **Checked specifically for the FLEX-scoping bug** named in `skills/case-readiness/SKILL.md`'s
  2026-08-13 doctrine note (several other cases this session flexed cited/given data instead of
  stated assumptions). `FLEX = ["ma3_credential_theft_cadence", "ma4_helpdesk_increment"]` —
  both are genuine Appendix E modeling assumptions the case author chose, not sourced data. The
  charset, benchmark rate, breach-vector shares, MFA-blocking rate, and vendor prices (S1–S5) are
  in `PARAMS` (available to `--flex-all`) but deliberately **excluded** from `FLEX`. MA1
  (headcount) and MA2 (AP-access fraction) are real assumptions too, but neither enters
  `evaluate()`'s A-vs-B primary metric (MA1 cancels per-employee; MA2 feeds only D3's pigeonhole
  bound) — both are documented as out-of-scope-for-`FLEX` in the file's own docstring rather than
  silently omitted, and MA2/MA1 are still exercised directly via the `pigeonhole_d3()` helper.

### Tier 1 — structural (19 checks)
| id | result | note |
|---|---|---|
| T1-01 | PASS | |
| T1-02 | PASS | |
| T1-03 | GAP | "Option A may not be named in Background" fuzzy-match false positive — Background does name and describe The Long Wall/The Second Gate in full; the regex keys off word-fragments ("Recommend", "mandate") that happen not to recur verbatim. Read and cleared per the doctrine note on this exact false-positive class. |
| T1-04 | PASS | |
| T1-05 | PASS | |
| T1-06 | PASS | |
| T1-07 | PASS | |
| T1-08 | PASS | |
| T1-09 | PASS | margin_pct 10.1%, within the 20% cap |
| T1-10 | PASS | standards resolve; new_coverage genuinely n=0, forces test documented in LEARNING_GOALS.md |
| T1-11 | PASS | |
| T1-12 | PASS | |
| T1-13 | PASS | fixed this run — see below |
| T1-14 | GAP | 5 guide-only rounded figures in FACILITATOR.md (0.72, 2.585, 3.66, 35.0, 236.0 — rounded presentations of derived values already in case.json.derived, e.g. 236 ≈ 235.6164 crack days) have no exact-match row in the numeric universe. Not a drift bug (verified each traces to a real case.json.derived value within rounding) — flagged for a future pass to also add the rounded forms to case.json.derived so this checks mechanically. |
| T1-15 | PASS | |
| T1-16 | PASS | case_md_sha256 recorded this run |
| T1-17 | PASS | cohort_bands[] present for all 3 bands |
| T1-18 | GAP | 33 CSS-decimal false positives in the interactive HTML's `<style>` block (line-height, border-width, font-size, etc.) — the accepted false-positive class this check's own doctrine note names explicitly (Cold Chain's baseline: 110 of the same kind). No balance_test leak: margin_pct (10.1) does not appear anywhere in the file outside `<script>`, and the leak scan found none. |
| T1-19 | PASS | 10 glossary terms, all https:// to allowlisted domains (khanacademy.org, cuemath.com) |

**BLOCKER (0)** — none.

**Fixed this run to clear T1-13's BLOCKER:**
1. Added a `## 45-Minute Socratic Plan` section to `FACILITATOR.md` — a timed 10-row table
   (0:00–43:00) covering Intro through Close, naming the TWIST moment at 33:00, per SPEC §7.3 /
   MCS-16.
2. Reformatted the 5 Socratic questions onto single unwrapped lines so the mechanical "line starts
   with a number/bullet and ends in `?`" check actually counts all 5 (the wrapped, multi-line
   original only mechanically counted 1 — a real miscount, not a content problem; the content was
   always 5 real questions).
3. **Found and fixed a genuine factual bug while in the file**: the Twist section's
   facilitator-only note stated Option A's primary-metric figure as "5.32 years/$" — the correct,
   sourced figure (matching `case.json.derived.primary_metric_A_years_per_dollar = 5.3419`) is
   **5.34**, which the file's own later "Facilitator-only numbers" section already stated
   correctly. Corrected the typo so both sections agree.

### Sensitivity model
`sensitivity_model.py` rewritten to expose `PARAMS`/`FLEX`/`evaluate(params)` per
`skills/case-readiness/scripts/example_sensitivity_model.py`'s contract; reproduces
`case.json.derived`'s primary-metric figures exactly (verified by direct execution, see above).

### Interactive HTML
Built `cases/the-keyspace-decision/published/The Keyspace Decision - Interactive.html` from
`templates/interactive_shell.html` per `templates/INTERACTIVE_HTML_CONTRACT.md`. All
`{{PLACEHOLDER}}` tokens filled (grepped clean). Notes:
- Working Notebook's 5 steps (D1–D5) each call a JS port of `sensitivity_model.py`'s
  `PARAMS`/`evaluate()`/`pigeonhole_d3()` — same names, same arithmetic — rather than re-deriving
  the tally inline, per the contract's ¶2.
- The Twist section's "Apply Twist" toggle computes the raw D2-only ("the trap") metric next to
  the D4-weighted metric **live**, from the student's own typed Step 1/2/4 inputs (falling back to
  the case's own PARAMS), and never prints a hardcoded winner or margin.
- Confirmed no leak: `case.json.balance.margin_pct` (10.1) does not appear anywhere in the shipped
  HTML outside a `<script>` tag's computation — grepped directly in addition to relying on T1-18.
- Glossary: 10 terms, all `https://` to allowlisted domains. Two are new/fetched this session
  (Fundamental Counting Principle → cuemath.com, verified live 2026-08-15; Pigeonhole Principle →
  cuemath.com/data/combinations/). **Disclosed limitation**: no dedicated Pigeonhole Principle
  lesson was found on any of the project's 7 allowlisted educational domains after an extensive
  search (cuemath.com, mathsisfun.com, khanacademy.org, ck12.org, purplemath.com, nctm.org,
  openstax.org all checked, several by direct URL fetch, none have one). Rather than fabricate a
  URL (forbidden by MCS-21) or leave the term unlinked (contradicting the contract's instruction
  to include the case's own new-coverage skill in the glossary), the term links to the closest
  verified, live, on-domain combinatorics resource (Cuemath's Combinations page), with the
  tooltip's own definition text stating the Pigeonhole Principle accurately and the Appendix G
  caption disclosing the substitution explicitly to the reader. The other 8 terms reuse Cold
  Chain's own already-verified starter-glossary entries verbatim (khanacademy.org, verified live
  2026-08-01), per the contract's reuse rule.

### case.json.qa
```
state: TIER1_PASS   verdict: PASS   blockers_open: 0   gaps_open: 3 (T1-03, T1-14, T1-18 — all
accepted/documented false-positive or non-blocking classes)   case_md_sha256: 98b4b8054b...ed7d2
```
`status` set to `"qa"`.

### Tier 2 — not run this pass
Out of scope for this run (task specified Tier 1). A spot-check of `tier2_probes.py --probe 5`
was run for verification purposes only (not filed as a Tier 2 result): it correctly identifies
Appendix E MA3 as an unstable-if-undisclosed dial per the script's newer
`sensitivity_disclosure[]` mechanism — the case's `case.md`/FACILITATOR.md text already discloses
this fragility in prose (MA3's own row: "the single lever that decides the case"), but
`case.json.sensitivity_disclosure[]` has not yet been populated in the structured format
`tier2_probes.py` now expects. Flagged here for whoever runs Tier 2 next; not a Tier 1 concern and
not fixed in this pass per case-readiness's "never fix beyond the tier requested" scope, though
the fix (adding a `sensitivity_disclosure[]` entry) is small and consistent with content already
written into the case.

### Next step
Tier 1 clean. `Run case-readiness Tier 2 on the-keyspace-decision` next (six probes, including
formalizing the MA3 disclosure noted above).
