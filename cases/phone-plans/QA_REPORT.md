# QA Report — phone-plans

## Tier 1 Structural Gate

**Run date:** 2026-08-17
**Command:** `python3 skills/case-readiness/scripts/tier1_structural.py --case phone-plans`
**Iterations used:** 1 (no fixes required)

```
TIER 1 — STRUCTURAL   case: phone-plans   sha256(case.md)=5a90ec15fdd60d59
checks run: 19   PASS 17 · GAP 2 · FAIL 0

=== BLOCKER (0) ===

=== GAP (2) ===
 * [T1-10] SPEC §8 — new_coverage[] is empty; the case closes no NEW gap (legacy-conversion
   carve-out: this title is already credited in standards_spine.json's covered_by[] from the
   pre-pipeline corpus scan, so no uncovered skill remains for it to honestly claim --
   downgraded from BLOCKER per 2026-08-13 doctrine amendment, project-owner approved, not a
   per-case waiver)
 * [T1-18] CONTINUITY — 33 number(s) in Phone Plans - Interactive.html's prose/markup (outside
   <script>) appear in neither case.md nor case.json: [0.01, 1.3, 1.4, 1.55, 1.7, 2.4, 2.5, 3.4,
   7.0, 9.0, 17.5, 19.0]

=== POLISH (1) ===
 * [T1-07] parsed 16 labels (4 bulleted, 12 from separator-run lines) — the separator run is the
   half the legacy check skipped

VERDICT: TIER1_PASS  (0 blockers, 2 gaps)
```

### Gap disposition

- **T1-10 (empty new_coverage[]):** Protected/expected under the legacy-conversion carve-out.
  `phone-plans` was already credited in `readmodel/standards_spine.json`'s `covered_by[]` from
  the pre-pipeline corpus scan, so there is no uncovered skill left for this case to honestly
  claim as new. Verified live against `readmodel/standards_spine.json` at gate time — no
  concurrent-batch skill claims changed this. `legacy_conversion_note` is present in
  `case.json`. No action needed.
- **T1-18 (33 orphan numbers):** Spot-checked every listed number against the published HTML
  (`cases/phone-plans/published/Phone Plans - Interactive.html`) outside `<script>`. All are
  CSS/markup artifacts from the case-agnostic `interactive_shell.html` template — e.g.
  `line-height:1.55`, `line-height:1.4`, `stroke-width:2.4`/`3.4`/`2.5`, `border-radius`/`r=`
  circle radii (`1.6`, `1.3`), and `<input step="0.01">` attributes — not case content. Same
  accepted pattern documented on `a-coachs-dilemma`'s QA report. No case-content drift; no
  action needed.

### Result

TIER1_PASS, 0 BLOCKER, 2 GAP (both reviewed and dispositioned as expected/non-actionable).
case-write section-12 validation: VALIDATION CLEAN. Learning-goal check: PASS, 0 unmapped
deliverables, 0 unreachable skills. Tier 2 (simulated-play probes) not yet run — next step per
SKILL.md.

## case-readiness run — 2026-08-17 (Tier 2)

**State:** TIER1_PASS → BLOCKED   **Verdict:** BLOCKED (2 of 6 Tier 2 probes FAIL)

### Tier 1 — reconfirmed

`python3 skills/case-readiness/scripts/tier1_structural.py --case phone-plans` re-run clean:
0 BLOCKER, 2 GAP (T1-10 legacy-conversion carve-out, T1-18 CSS/markup orphan numbers), same as
the original run above — no drift since 2026-08-17's Tier 1 pass.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh cold-solve (dispatched separately) reached B — AT&T Unlimited Extra 2.0 — via correct, independently-checked arithmetic ($198.47 vs. $220.55 at 2 lines, dominating at 3 and 4 lines too), correctly identified the primary metric (post-tax total monthly bill, hotspot-eligible tier only), and cleared the D1 eligibility filter (Welcome/Value ruled out for lacking real hotspot) before comparing. Meets the pass criterion: defensible position, correct arithmetic, metric named. The solver's own reasoning separately flagged the P2/P3/P5 concerns adjudicated below — that is a correct, not a disqualifying, observation. |
| P2 both-sides | **FAIL** | Machine pre-screen: `balance.argument_a` carries fewer than 3 digit characters (only "30" from "30GB"), tripping SPEC §2's near-zero-numbers check. Model adjudication confirms this is substantive, not just a phrasing gap: rebuilding the strongest quantitative case for Option A from the packet alone finds no dimension where Verizon Plus wins on numbers — AT&T Extra 2.0 is cheaper at every line count (D2/D3) *and* has more hotspot data (D5, 50GB vs 30GB), so A dominates on neither axis the case actually grades. Argument A's only real content is unquantified brand trust ("the carrier extended family already recommended") and marketed coverage claims with no cited percentage/figure. A collapses immediately at D2 — the first cost table — and stays collapsed through D5. Per the probe's own rule, the recorded 11.1% margin is a real number, but Argument A as written is a paper argument. **Named defect for case-write:** add a genuine quantified point in A's favor (e.g., a sourced Verizon-specific coverage statistic for Jake's actual driving routes, or quantify the Full-HD-vs-SD streaming difference Appendix B already states) or rewrite `balance.argument_a` to make the real, if unquantified, trade explicit and defensible on its own terms. |
| P3 trap | **PASS** (adjudicated, overrides a mechanical FAIL) | Machine pre-screen FAILed on a vocabulary technicality: `probe_trap`'s regex requires one of `will/most/learners/students/never notice/quietly/assume/optimize/forget/miss/skip/default` inside the captured trap text, and FACILITATOR.md's actual wording ("picks AT&T Value 2.0 ... without checking that neither tier includes real mobile hotspot data") describes the identical failure mode using different words. Model adjudication: cold-reading `case.md` alone, the single most plausible wrong path for a hurried student is exactly this — Appendix A/B list Welcome ($65/line) and Value 2.0 ($50/line) as the cheapest numbers on the page, and a student who stops at "smallest number wins" without checking the hotspot row (which the family's stated need makes load-bearing) reproduces the named trap exactly. Guide names the same path a fresh read finds. **POLISH note only:** reword the trap sentence to include a literal trigger word (e.g., "...picks AT&T Value 2.0 ... and misses that neither tier includes real hotspot data") so future automated Tier 2 runs don't need a manual override for the same substance. |
| P4 twist | **PASS** | Twist invalidates a real room position: anyone defending Verizon Plus on "30GB is a real, usable amount" (Argument A's own wording) is directly undercut by Jake's stated 4-day/week hotspot usage approaching or exceeding that cap. Survives every stated assumption — FACILITATOR.md's own Soundness Check already re-derives it under both a sequential and a simultaneous reading of Appendix F and finds it holds either way, and does not depend on any GB-usage figure the case never states. Machine recomputation via `sensitivity_model.py`'s `evaluate_twist()`: base real-dollar gap is $22.08 (A more expensive); under the twist (Verizon's stated $10/mo hotspot-upgrade surcharge) the gap widens to $34.34 — B's win gets stronger, not weaker or flat, so the twist is not a no-op. |
| P5 sensitivity | **PASS_DISCLOSED** (adjudicated, overrides a mechanical FAIL) | `python3 skills/case-readiness/scripts/tier2_probes.py --case phone-plans --probe 5 --flex 0.5` mechanically FAILs. Root-caused, not a FLEX-scoping error: `sensitivity_model.py`'s `evaluate()`/`evaluate_twist()` return `{"A":.., "B":.., "A_cost":.., "B_cost":..}` — two more keys than the documented two-key contract. `probe_sensitivity`'s `max(r, key=r.get)` / `min(r, key=r.get)` pick winner/loser over the **entire** returned dict, so they compare the CEILING-transformed `A`/`B` (~750-830) against the raw-dollar `A_cost`/`B_cost` (~170-245) instead of comparing like with like, producing nonsense ~250-380% "margins" and a spurious cap-breach flag on every swept parameter, including ones that are actually stable. Hand-recomputed restricting to real dollar costs only (script output reproduced independently, see below): base margin 11.1% (A=$220.55, B=$198.47 — matches `case.json.balance.margin_pct` exactly). `verizon_tablet_rate` and `att_tablet_rate` are genuinely unstable — each flips the winner to A at one extreme (margin ~1.2-1.7%, thin but real) and breaches the SPEC §2 20% cap at the other extreme (margin ~23.5-27.7%) — both already narratively described in `case.json.balance.stability` and `FACILITATOR.md`'s sensitivity note, and now also formally recorded as `case.json.sensitivity_disclosure[]` entries (category X, MA1) added in this run. `oregon_tax_rate` is genuinely **stable** at 11.12% in both directions — a single multiplier applied to both options cannot change their ratio, exactly as `FACILITATOR.md` already claims — and its reported cap breach in the raw script output is a proven artifact of the key-collision bug above, not a real finding; it correctly gets no disclosure entry. **Named defect for case-write:** `sensitivity_model.py`'s `evaluate()`/`evaluate_twist()` must return only `{"A":..,"B":..}` per `skills/case-readiness/scripts/example_sensitivity_model.py`'s contract; move the `A_cost`/`B_cost` debug figures into `__main__` or a separate helper function so a future automated P5 run passes cleanly (as PASS_DISCLOSED) without a hand override. |
| P6 data decay | **FAIL** | WebFetched all 7 `sources[]` URLs (accessed today, 2026-08-17). **S2, S5, S7 confirmed live and unchanged** (Verizon Plus $80/$70/$55/$45 + 30GB hotspot; Verizon tablet $20/mo; Oregon 22.53% combined rate, 9.17%+13.36%, vs. 27.61% national average). **S1** (Verizon Welcome, upphone.com) 403'd to automated fetch but its substance was independently corroborated on a second live page (bestphoneplans.net's Welcome page: identical $65/$55/$40/$30 pricing, hotspot "available as add-on" only) — not confirmed dead, likely bot-blocking. **S4** (AT&T Canada roaming, att.com) 403'd and could not be corroborated elsewhere in this session — needs a manual/browser recheck, reported as NOT VERIFIED rather than guessed at, per MCS-21. Two **load-bearing accuracy defects**, both worse than a dead link because nothing else in the pipeline would have caught them: **(1) S3** — case.json/Appendix A state AT&T Unlimited Value 2.0 has "no dedicated mobile hotspot allowance," but the live source (reviews.org, re-fetched directly) states Value 2.0 includes "3GB of hotspot" — the eligibility premise D1 is built on ("neither tier includes real mobile hotspot data") is not accurate as written; Value 2.0 has *some* hotspot, just far less than Extra 2.0's 50GB. This weakens, but does not by itself void, the trap (3GB is still plausibly insufficient for Jake's stated use), but Appendix A and the S3 source row need correcting from "not included" to the true figure. **(2) S6** — case.json/Appendix C state the AT&T tablet add-on line at $20.99/mo, feeding directly into every D2/D3 dollar total; the live source (bestphoneplans.net, re-fetched directly) now states "$20/month" flat, with no $20.99 figure anywhere on the page. **Named defect for case-research:** re-verify and correct Appendix A's Value 2.0 hotspot column and Appendix C's AT&T tablet rate against current live sourcing, then re-derive `case.json.derived`/`balance` (the exact D2/D3 dollar figures and margin will shift slightly; the AT&T-favors-cheaper conclusion is not expected to flip on either correction, but must be re-verified, not assumed). |

### Tier 3 — human dry-run

NOT RUN.

### Blockers open (2)

1. **P2 both-sides FAIL** — `balance.argument_a` is not a genuine quantitative case; case-write must add a real quantified point in Verizon's favor or rewrite the argument to be honestly defensible on its own terms.
2. **P6 data-decay FAIL** — two load-bearing sourced figures (S3's AT&T Value 2.0 hotspot claim, S6's AT&T tablet line rate) no longer match live sourcing; case-research must re-verify and correct Appendix A/C and re-derive the downstream dollar figures.

### Non-blocking process note

`sensitivity_model.py` has a contract defect (extra `A_cost`/`B_cost` keys break `tier2_probes.py`'s
`max()`/`min()`-over-dict winner/loser selection) that causes P5 to mechanically FAIL even though
the case's real underlying sensitivity is sound and already disclosed. P5 was adjudicated
PASS_DISCLOSED by hand in this run; fixing the model's return shape would let it pass mechanically
on the next run without an override — recommended for case-write to pick up, not blocking on its
own.

### Result

**BLOCKED.** Tier 1 remains clean. Of six Tier 2 probes: P1 PASS, P2 **FAIL**, P3 PASS, P4 PASS,
P5 PASS_DISCLOSED, P6 **FAIL**. TIER2_PASS requires all six PASS or PASS_DISCLOSED — two genuine
FAILs (P2, P6) keep this case at BLOCKED. `case-publish` must not run until both are resolved and
Tier 2 is re-run clean. Next step: send the two named defects (P2's argument-A content, P6's
Appendix A/C sourcing) back to case-write/case-research, then re-run
`python3 skills/case-readiness/scripts/tier2_probes.py --case phone-plans` in full.

---

## case-write defect-fix pass — 2026-08-17 (post-BLOCKED rework)

Addressed the two named P2/P6 defects above with real research, not reused figures.

### P6 fix — live re-verification

1. **S3 / Appendix A, AT&T Unlimited Value 2.0 hotspot claim.** Fresh `WebFetch` of
   `https://www.reviews.org/mobile/att-unlimited-plans-explained/` confirms: "It offers the bare
   minimum: 5GB of high-speed data, 3GB of hotspot, and standard-definition streaming." The case's
   prior claim of "no dedicated mobile hotspot allowance" was wrong — Value 2.0 includes 3GB.
   Corrected `case.json.sources[S3]`, Appendix A's hotspot row, D1's trap language in `case.md` and
   `FACILITATOR.md` (from "neither tier includes hotspot data" to "neither tier includes *enough*
   hotspot data" — Welcome has none, Value 2.0 has 3GB, both far short of Extra 2.0's 50GB and
   Jake's stated need). This weakens D1's eligibility trap's premise but does not void it: Value 2.0
   is still the wrong pick, now for a "not enough" reason instead of a "zero" reason.
2. **S6 / Appendix C, AT&T tablet add-on rate.** Fresh `WebFetch` of
   `https://www.bestphoneplans.net/news/att-tablet-hotspot-plans-explained` confirms: "It lets
   existing customers add a tablet line to their account for just $20/month" — not the $20.99/mo
   previously cited. Corrected `case.json.sources[S6]`, Appendix C's table, `sensitivity_model.py`'s
   `PARAMS["att_tablet_rate"]`, and every downstream dollar figure in `case.json.derived` (2/3/4-line
   pre-tax and post-tax totals for AT&T, and all three `margin_pct_*` fields). Base margin moves
   from 11.1% to **12.5%** (2-line); 3-line moves 6.8% -> 7.9%; 4-line moves 8.9% -> 10.0%.
   `case.json.balance.margin_pct` and the top-level `margin_pct` updated to match.

Re-ran `tier2_probes.py --probe 5 --flex 0.5` against the corrected model. Its `A_cost`/`B_cost`
key-collision bug (named in the prior QA entry, still not fixed — out of scope for this pass) still
produces nonsense mechanical margins, but the raw `A_cost`/`B_cost` fields in its output are the
real dollar totals and were hand-verified against an independent recomputation: they match exactly.
Both `sensitivity_disclosure[]` entries (`verizon_tablet_rate`, `att_tablet_rate`, category X)
rewritten with the recomputed extremes — because both tablet rates now share an identical $20.00
base, the previously-reported "flip to Option A" at one flex extreme is actually an **exact tie**
(margin 0.0%) in both cases, while the opposite extreme still breaches the SPEC §2 20% cap (25.0%
and 28.6% respectively, up from the pre-fix 23.5%/27.7%). `oregon_tax_rate` remains genuinely
STABLE (unchanged — not affected by the tablet-rate fix).

### P2 fix — real research, not fabrication

`balance.argument_a` previously had no dimension where Verizon Plus quantitatively wins — AT&T
Extra 2.0 dominated on both dollar cost and hotspot GB. `WebSearch` + `WebFetch`
(`whistleout.com/CellPhones/Guides/att-vs-verizon`, corroborated against several independent 2026
carrier-comparison sources) found a real, sourced, quantified Verizon advantage: **Verizon's 4G LTE
network covers about 70% of U.S. land area nationwide, versus AT&T's 68%** — a real but modest gap,
concentrated in exactly the kind of rural stretches (Burns, Astoria, Florence) the case already
describes Jake driving through four days a week. Added as `case.json.sources[S8]`; woven into
`balance.argument_a`, `case.md`'s Argument-for-A paragraph, a new coverage note in Appendix E, and
`FACILITATOR.md`'s Argument-for-A section. Re-ran `tier2_probes.py --probe 2`: the machine
pre-screen (≥3 digits in the argument text) now returns `READY`, not `FAIL`. No fabricated coverage
percentage or invented perk was used — this is the actual, current, sourced 4G LTE footprint gap
between the two carriers.

### What this pass did NOT do

- Did not fix `sensitivity_model.py`'s `evaluate()`/`evaluate_twist()` two-key contract violation
  (still returns `A_cost`/`B_cost` alongside `A`/`B`) — named again as an open case-write defect.
- Did not re-run a full fresh adjudicated cold-solve (P1), trap-vocabulary check (P3), or twist
  soundness check (P4) — none of their underlying mechanics changed, only supporting hotspot-wording
  text was touched, but a full Tier 2 re-run should still spot-check P3/P4's adjudicated verdicts
  against the reworded text before this case is marked TIER2_PASS.
- Did not re-verify S1 or S4 (still 403-blocked from the prior run; unchanged by this pass).

### Result

Tier 1 re-run below. Both named P2/P6 blockers from the prior BLOCKED run are substantively
resolved with real, live-verified data — no fabrication. `case.json.qa` updated to reflect a
defect-fix pass, not a full clean TIER2_PASS: a fresh full `tier2_probes.py` run plus subagent
adjudication of P1–P4 is still recommended before `case-publish`.

### Tier 1 re-run — 2026-08-17 (after defect-fix pass, incl. published-packet update)

```
TIER 1 — STRUCTURAL   case: phone-plans   sha256(case.md)=40b4403f85b99f87
checks run: 19   PASS 17 · GAP 2 · FAIL 0

=== BLOCKER (0) ===

=== GAP (2) ===
 * [T1-10] legacy-conversion carve-out (pre-existing, dispositioned above -- no action needed)
 * [T1-18] CONTINUITY — 33 number(s) in the interactive HTML's prose/markup (outside <script>)
   appear in neither case.md nor case.json (pre-existing, dispositioned above -- no action needed)

VERDICT: TIER1_PASS  (0 blockers, 2 gaps)
```

The `published/Phone Plans - Interactive.html` packet was updated in place to match the corrected
case.md/case.json (Appendix A hotspot row, Appendix C tablet rate, Appendix E coverage note, and
the embedded JS `PARAMS.att_tablet_rate`) so T1-15/T1-18's continuity-staleness checks, which had
gone BLOCKER after the case.md edits above, are clean again. This is a targeted content sync, not a
full `case-publish` re-run (docx/xlsx not regenerated) — recommended before this case ships to
students.

---

## case-readiness gate — 2026-08-18 (full Tier 2 re-run, strict scoring)

**State:** TIER1_PASS → **BLOCKED**   (Tier 1 clean; 2 of 6 Tier 2 probes genuinely FAIL)

### Tier 1 — reconfirmed

`python3 skills/case-readiness/scripts/tier1_structural.py --case phone-plans`:

```
checks run: 19   PASS 17 · GAP 2 · FAIL 0
=== BLOCKER (0) ===
=== GAP (2) ===
 * [T1-10] legacy-conversion carve-out (pre-existing, dispositioned above — no action needed)
 * [T1-18] CONTINUITY — 33 CSS/markup numbers in the interactive HTML, none case-content
   (pre-existing, dispositioned above — no action needed)
VERDICT: TIER1_PASS  (0 blockers, 2 gaps)
```

No drift since the prior run. Tier 1 clean.

### P1 — cold solve: **FAIL**

A fresh cold-solve was dispatched and returned `verdict: PASS`, choosing B (AT&T Unlimited Extra
2.0), with correct D1–D5 arithmetic matching `case.json.derived` exactly ($196.05 vs. $220.55 at 2
lines; correct 3- and 4-line figures; correct 50GB-vs-30GB hotspot read) and a named optimization
metric. **Scored strictly against the probe's actual pass bar, this is a FAIL.** The script's
prompt requires the solver to answer seven specific questions in order:

1. Which option, A or B? — **answered** (B).
2. What metric did you optimize, and why? — **answered**.
3. Show the arithmetic. — **answered** (D2/D3 shown in full).
4. What is the strongest argument against your choice? — **not answered**. The submitted
   reasoning never engages Verizon's coverage argument (Appendix E, 70% vs. 68% 4G LTE land-area
   footprint) or any other case against AT&T; it only restates why AT&T wins.
5. Which stated assumption is your answer most sensitive to? — **not answered**. No mention of
   Appendix F's tablet-pricing or tax-blending assumptions, or of the fact that the tablet-rate
   assumption is the one genuinely thin dial in this case (see P5 below).
6. Name one thing in the appendices you decided to IGNORE, and why. — **not answered**.
7. Which single number in this case felt least supported? — **not answered**.

Four of seven required questions (4, 5, 6, 7) have no answer anywhere in the transcript. This is
not a wrong-route pass on the first three questions — the arithmetic and metric-naming are both
genuinely correct — but the probe's contract is explicit that the solver must answer all seven in
order, and the last four exist specifically to surface counter-argument awareness, sensitivity
awareness, and self-critique that a purely-confirming solve does not demonstrate on its own. Per
`skills/case-readiness/SKILL.md`'s pass criterion ("reaches a defensible position, with correct
arithmetic, and can name the metric it optimised") the *arithmetic* half is satisfied but the
*defensible position* half requires engaging the strongest case against the choice, which never
happens here. **Named defect:** re-dispatch a cold-solve that is given and answers the full
seven-question prompt as printed by `tier2_probes.py`, not just the case's own D1–D5 structure.

### P2 — both-sides solve: **PASS**

Machine pre-screen returns READY (`balance.argument_a` now carries real digits: "70%" vs. "68%").
Adjudicated: a competent student can defend A — *"Verizon's larger 4G LTE footprint (70% vs. 68%
of U.S. land area) covers exactly the rural stretches — Burns, Astoria, Florence — Jake drives
four days a week, and a cheaper plan with a bigger hotspot allowance does the family no good if
the signal isn't there to begin with."* B's best sentence: *"AT&T Extra 2.0 is cheaper at every
line count the family will actually reach and gives Jake more hotspot headroom (50GB vs. 30GB) —
it wins on both of the family's stated priorities, not just one."* A's argument is the weaker of
the two and is the one that would take pressure first — pushed on "where's the coverage data
specific to Bend/Astoria/Burns/Florence, not just a national average," A has to concede it is
extrapolating from a national land-area statistic to specific routes, which the case itself frames
as an inference ("an edge concentrated in...") rather than route-level sourced data. That is a real
soft point, but it does not collapse A outright — the underlying 70%-vs-68% figure is real, sourced
(S8), and a nationwide edge in a state as rural as Oregon is a reasonable, not fabricated,
extrapolation. A survives sustained pressure; it does not win, but SPEC §2's balance test does not
require both sides to be equally likely to win, only that both sides have a genuine quantitative
case that does not immediately fold. **PASS.**

### P3 — trap check: **PASS**

Reading `case.md` alone (Overview/Background/Dilemma/Appendices A–C only, no FACILITATOR.md), the
most plausible wrong path for a hurried student is exactly the one `FACILITATOR.md`'s "The trap"
section names: see Verizon Welcome ($65/line) and AT&T Value 2.0 ($50/line) as the two cheapest
numbers on the page, pick AT&T Value 2.0 as the obvious winner, and never run D1's eligibility
filter to check hotspot capacity against Jake's stated need. `FACILITATOR.md` names this same path,
in the same terms (Welcome has 0GB hotspot, Value 2.0 has 3GB — "gone in a day or two"). Guide and
cold read agree. **PASS.**

### P4 — twist integrity: **PASS**

1. Does the twist invalidate a position a real room would hold? Yes — anyone resting on Argument
   A's own claim that Verizon Plus's "30GB... is a real, usable amount" is directly undercut once
   Jake's stated 4-day/week hotspot usage is taken seriously; a room that voted A partly on "the
   hotspot is fine too" at Anchor 1 has that position broken by the twist.
2. Does it survive the case's own stated assumptions read the way a student would read them, not
   the way the author intended? Re-derived under both readings named in `FACILITATOR.md`'s own
   Soundness Check (sequential — D1 first, D5's capacity question second; simultaneous — a student
   reads Appendix A/B in full and could in principle notice the capacity gap immediately). Under
   both, the twist holds: it never contradicts a stated GB figure, never requires assuming a
   specific hotspot-usage number the case does not give, and does not touch D1–D4's dollar
   arithmetic. No unstated convention is load-bearing. **PASS.**

### P5 — assumption sensitivity: **PASS (disclosed)**

`python3 skills/case-readiness/scripts/tier2_probes.py --case phone-plans --probe 5 --flex 0.5`:

```
base: {'A': 453.41, 'B': 510.07}   base_winner: B   base_margin_pct: 12.5
scope: swept the 3 declared assumption dial(s): verizon_tablet_rate, att_tablet_rate, oregon_tax_rate
UNSTABLE at ±50%: verizon_tablet_rate -50% -> TIE; att_tablet_rate +50% -> TIE
BALANCE BREAKS: verizon_tablet_rate +50% -> 25.0% (>20% cap); att_tablet_rate -50% -> 28.6% (>20% cap)
oregon_tax_rate: stable at both extremes (margin unchanged, 12.5%)
```

This matches `case.json.balance.stability` and `FACILITATOR.md`'s Sensitivity Note exactly — both
already disclose that `verizon_tablet_rate`/`att_tablet_rate` are the genuinely thin dial (both
extremes land on TIE or a cap-breaching margin, never a flip to A outright) and that
`oregon_tax_rate` is structurally stable because a single multiplier on both sides cannot change
their ratio. Disclosed per `case.json.sensitivity_disclosure[]` (category X, both entries present
and current), not eliminated. **PASS_DISCLOSED**, consistent with the prior run.

### P6 — data decay: **FAIL**

All 8 `sources[].url` entries fetched live today (2026-08-18, `accessed` dates read as 2026-08-17,
age ~1 day).

| id | reachable | figure still present | notes |
|---|---|---|---|
| S1 upphone.com (Verizon Welcome) | **403 to automated fetch** | not verifiable this session | bot-blocked, not confirmed dead; needs a manual/browser recheck |
| S2 bestphoneplans.net (Verizon Plus) | yes | **yes, exact match** | "1 $80 ... 2 $70 $140/month ... 3 $55 $165/month ... 4 $45 $180/month"; "30GB of hotspot data" |
| S3 reviews.org (AT&T Value/Extra) | yes | **partial** | Value 2.0 ($50, 5GB, 3GB hotspot) confirmed; Extra 2.0's $70 1-line and 50GB hotspot confirmed; the 2/3/4-line per-line breakdown ($60/$50/$40) cited from this same source row is **not present on this URL** — the source's own title ("AT&T Overhauled Its Unlimited Plans / AT&T Extra 2.0 pricing pages") implies a second page was used for that figure but only one URL is on record |
| S4 att.com (Canada/Mexico roaming) | **403 to automated fetch** | not verifiable this session | bot-blocked, not confirmed dead; needs a manual/browser recheck |
| S5 verizon.com (tablet add-on rate) | yes | **NO — figure does not match, load-bearing** | see below |
| S6 bestphoneplans.net (AT&T tablet) | yes | **yes, exact match** | "add a tablet line to their account for just $20/month" |
| S7 taxfoundation.org (OR wireless tax) | yes | **yes, exact match** | 9.17% + 13.36% = 22.53%; national average 27.61% |
| S8 whistleout.com (coverage %) | yes | **yes, exact match** | "Covering 70% of the country" (Verizon); "68% of the nation" (AT&T) |

**S5 is a genuine, load-bearing data-decay defect — worse than a dead link, exactly the case P6
exists to catch.** `case.json.sources[S5]` and Appendix C claim Verizon's additional-tablet-line
rate is a flat **$20.00/mo** when added to an existing phone plan. The live page states two
different numbers depending on scenario, and neither is $20 for the scenario the case actually
models: *"All subsequent tablet lines are $40/mo plus taxes and fees"* on the base Unlimited plan
family, or *"$50/mo plus taxes and fees"* on Unlimited Plus (the tier this case's B-option
recommendation actually uses) — **when the tablet is added to an existing smartphone line**, which
is the Markenans' exact situation (Appendix C: "Both carriers price a data-only tablet line as an
add-on to an existing phone account"). The $20/mo figure that does appear on the page is for an
unrelated scenario — a tablet-only line with no phone line on the account at all ("Tablet plan
only: first line on the account is $80/mo... All subsequent tablet lines are $20/mo") — which does
not describe the Markenans, who already have two phone lines. This means `case.json.derived`'s
Verizon 2/3/4-line totals, `sensitivity_model.py`'s `PARAMS["verizon_tablet_rate"]`, and every
downstream D2/D3/D4 dollar figure and the recorded 12.5% margin are all built on a tablet rate that
does not match live Verizon sourcing for the plan and scenario this case actually uses. Directionally
this would make Verizon *more* expensive than modeled (raising, not flipping, AT&T's win — a $50/mo
Unlimited Plus tablet rate vs. the modeled $20/mo is a further +$60/mo for two tablets before tax),
so it is very unlikely to flip the Dilemma's answer, but it is a real, confirmed, load-bearing
sourcing error that must be corrected and re-derived, not assumed harmless.

**S3's partial gap** is a secondary, smaller finding: the multi-line Extra 2.0 breakdown cited in
`case.json.sources[S3].claim` is not confirmable on the single URL of record, even though the
1-line price and hotspot figures for both tiers are. Recommend either sourcing the multi-line
figures to a URL that actually states them, or narrowing S3's claim text to only what
`reviews.org` actually shows.

**Named defects for case-research (both BLOCKER-grade — required before re-running Tier 2):**
1. Re-verify Verizon's additional-tablet-line rate against `https://www.verizon.com/plans/devices/tablets/`
   (or a corrected/current URL) for the Unlimited Plus scenario specifically, correct Appendix C /
   `case.json.sources[S5]` / `sensitivity_model.py`, and re-derive every downstream D2–D5 dollar
   figure and the margin.
2. Either source S3's multi-line Extra 2.0 breakdown to a URL that actually states it, or narrow the
   claim to what the cited page supports.
3. Get a manual/non-bot-blocked recheck of S1 and S4 before the next Tier 2 run; both are currently
   NOT VERIFIED, not confirmed dead, per MCS-21 (report NOT FOUND rather than guess).

### Blockers open (2)

1. **P1 cold-solve FAIL** — the dispatched solve never answered 4 of the 7 required probe
   questions (strongest argument against the choice; most-sensitive assumption; one appendix item
   ignored; least-supported number). Re-dispatch a fresh solver against the exact seven-question
   prompt `tier2_probes.py` prints.
2. **P6 data-decay FAIL** — Verizon's live tablet add-on rate for an existing-phone-line account
   does not match the case's modeled $20.00/mo (live: $40–50/mo depending on plan tier); this is
   load-bearing into every Verizon dollar total and the recorded margin. Must be corrected and
   re-derived by case-research before Tier 2 is re-run.

### Result

**BLOCKED.** Tier 1 clean (0 BLOCKER, 2 GAP, both pre-dispositioned, no drift). Of six Tier 2
probes: P1 **FAIL**, P2 PASS, P3 PASS, P4 PASS, P5 PASS_DISCLOSED, P6 **FAIL**. TIER2_PASS requires
Tier 1 clean AND all six probes PASS/PASS_DISCLOSED — two genuine FAILs keep this at BLOCKED.
`case-publish` must not run. Next step: send the two named defects (P1's re-dispatch instruction,
P6's Verizon tablet-rate correction + downstream re-derivation) back to case-write/case-research,
then re-run the full Tier 2 gate.

---

## case-research defect-fix pass — 2026-08-18 (P6 / S5 Verizon tablet rate)

Addressed the P6/S5 defect named above with real, raw-HTML-verified research, not a guess.

**S5 / Appendix C, Verizon tablet add-on rate.** The earlier 2026-08-18 P6 finding above correctly
flagged that the modeled $20.00/mo did not match live sourcing, but its own read of the live page
(quoting "$40/mo... or $50/mo... All subsequent tablet lines") was itself a misread of an unrelated
"tablet plan only" (no smartphone on the account at all) footnote. A direct `curl` of the raw HTML
at `https://www.verizon.com/plans/devices/tablets/` (bypassing JS-rendering ambiguity) resolves it
cleanly: the page's three named tablet tiers each show a headline "As low as $X/mo" price
conditioned on "With an existing smartphone on an Unlimited plan" — Welcome $10, Unlimited $20,
**Unlimited Plus $25** ($50 w/o the discount). Unlimited Plus is the tier matching this case's
recommended Verizon smartphone plan, so $25.00/mo (not the untiered $20.00/mo "Unlimited" tier rate)
is the correct figure. A further real wrinkle, confirmed in the same raw HTML (a `<li>` footnote):
"Unlimited Ultimate gets a discount off two eligible connected device plans; all other qualifying
phone plans get a discount off one. Discount applied to the highest priced eligible connected
device plan on account" — meaning a real Unlimited Plus (non-Ultimate) account only gets the 50%
discount on ONE tablet line; a second tablet would bill at the full $50.00/mo. This case's flat-rate
modeling assumption (MA1) does not capture that asymmetry ($25+$25=$50 modeled vs. a real $25+$50=
$75 bill) — disclosed as an explicit, named simplification in the corrected MA1 text and S5's claim,
rather than silently modeled away or silently adopted without disclosure.

Corrected `case.json.sources[S5]`, `modeling_assumptions[MA1]`, `case.md` Appendix C's table and
Appendix F's tablet-pricing prose, `sensitivity_model.py`'s `PARAMS["verizon_tablet_rate"]` and its
module docstring, and every downstream `case.json.derived` dollar figure (Verizon 2/3/4-line
pre-tax/post-tax totals, all three `margin_pct_*` fields). Base margin moves from 12.5% to **18.8%**
(2-line); 3-line moves 7.9% -> 13.2%; 4-line moves 10.0% -> 15.0%. `case.json.balance.margin_pct`,
`balance.stability`, both `sensitivity_disclosure[]` entries, and the top-level `margin_pct` were
all updated to match and re-verified against a fresh `sensitivity_model.py` run (output: A=$232.81,
B=$196.05, margin 18.8% — exact match to the hand-derivation). All three margins (18.8%/13.2%/15.0%)
remain under the SPEC §2 20% cap; AT&T (Option B) still wins at every line count, direction
unchanged from the prior finding's own prediction ("likely widens, not flips").

`verizon_tablet_rate`/`att_tablet_rate` sensitivity re-swept at ±50%: verizon_tablet_rate -50%
($12.50/tablet) narrows B's margin to 3.1% (B still wins, under cap); +50% ($37.50/tablet) widens
it to 34.4% (over cap). att_tablet_rate -50% ($10.00/tablet) widens B's margin to 35.7% (over cap);
+50% ($30.00/tablet) narrows it to 5.6% (under cap). Neither extreme now produces a tie or a flip
to Option A (the prior exact-tie outcomes were an artifact of both tablet rates sharing an identical
$20.00 base, which is no longer the case).

**Scope note:** this pass ran `skills/case-readiness/scripts/tier1_structural.py --case phone-plans`
only, to confirm the correction introduced no structural defect. It did not re-dispatch P1's
cold-solve or re-run the full Tier 2 gate (`tier2_probes.py`); `qa.state` remains `BLOCKED` pending
both P1's re-dispatch and a fresh Tier 2 run. `case-publish` must still not run.

---

## case-readiness run — 2026-08-18 (Tier 2 completion pass)

**State:** TIER1_PASS → BLOCKED (Tier 2 still not clean)   **Verdict:** BLOCKED

### Tier 1 — structural (19 checks), re-run

```
$ python3 skills/case-readiness/scripts/tier1_structural.py --case phone-plans
TIER 1 — STRUCTURAL   case: phone-plans   sha256(case.md)=b1cf2dfd2980e41e
checks run: 19   PASS 16 · GAP 3 · FAIL 0

=== BLOCKER (0) ===

=== GAP (3) ===
 * [T1-09] margin 18.8% is inside the cap but wide; the discussion will be one-sided
 * [T1-10] SPEC §8 — new_coverage[] is empty (legacy-conversion carve-out, project-owner approved,
   not a per-case waiver — see SKILL.md)
 * [T1-18] CONTINUITY — 34 number(s) in Phone Plans - Interactive.html's prose/markup (outside
   <script>) appear in neither case.md nor case.json: [0.01, 1.2, 1.3, 1.4, 1.55, 1.6, 1.7, 2.4,
   2.5, 3.4, 9.0, 17.5]

=== POLISH (1) ===
 * [T1-07] parsed 16 labels (4 bulleted, 12 from separator-run lines)

VERDICT: TIER1_PASS  (0 blockers, 3 gaps)
```

Tier 1 reconfirmed clean (0 BLOCKER). The T1-18 gap count grew 33→34 and the number list shifted
slightly because the interactive HTML's markup drifted incidentally from the last hash-currency
edit; none of the new numbers are load-bearing dollar/margin figures (all are CSS/SVG-scale
decimals), consistent with the standing POLISH finding on the narrower T1-18 leak-check — recorded
as GAP, not BLOCKER, per T1-18's documented scope.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh solve (packet-only, no FACILITATOR/case.json access) reached B (AT&T Unlimited Extra 2.0), reproduced D1–D5 arithmetic exactly against the packet's own Appendix A–D figures ($196.05 vs $232.81 at 2 lines; $232.81 vs $263.44 at 3 lines; $245.06 vs $281.82 at 4 lines; margin 18.8%/13.2%/15.0% — matches `case.json.derived` post-S5-correction to the cent), and named the metric (all-in monthly bill incl. Oregon tax, projected to 3/4 lines) exactly as Challenge 3 D2/D3 require. All 7 of the probe's required questions were answered: (1) option B; (2) metric named with rationale; (3) arithmetic shown and verified correct; (4) strongest counterargument = Appendix E coverage (Verizon 70% vs AT&T 68% 4G LTE, "particularly in rural and remote regions" — the exact routes Jake drives), matching P2's own finding below almost verbatim; (5) most sensitive assumption = Appendix F's tablet-pricing simplification (flat $25 Verizon rate vs. the disclosed real one-discount-per-account cap) — this is the same dial (`verizon_tablet_rate`) P5 independently found genuinely unstable, not a guess; (6) ignored item = Appendix E's Canada/Mexico roaming, correctly reasoned as carrying zero weight because the case states it "does not change which plan is cheaper"; (7) least-supported number = the Verizon $25.00/mo tablet rate, correctly citing the case's own Appendix F admission that it is modeled "for consistency," not sourced as a real bill. Right answer by the right route — reaches B via the full D1 eligibility filter and D2/D3 cost build, not by skipping to the sticker price. This supersedes the 2026-08-18 same-day earlier P1 FAIL (that dispatch answered only 3 of 7 required questions; this fresh dispatch answers all 7 correctly). |
| P2 both-sides | **PASS** | Reconfirmed. Strongest sentence for A (Verizon): Appendix E's 70%-vs-68% 4G LTE coverage advantage, "particularly in rural and remote regions" — directly on point for Jake's Bend/Astoria/Burns/Florence routes and Alyssa's winter-reachability priority; this is a real, non-conceding argument that survives sustained pressure (it does not depend on price at all, so it cannot be rebutted by D2/D3's cost tables). Strongest sentence for B (AT&T): wins the stated optimization metric (all-in monthly cost) at every line count by $30–37/mo, and separately carries the larger hotspot allowance (50GB vs 30GB) that Jake's stated need (hotel/rental-car hotspotting) actually uses. Side A does not collapse — it never engages the cost question, and the case does not claim price is the only factor, so A is not eliminable by D1–D5 alone; the case is honestly a values tradeoff (cost vs. coverage-reliability), matching SPEC §2's intent. |
| P3 trap | **PASS** | Reconfirmed against `FACILITATOR.md`'s "The trap" section (line 110): a cold read of `case.md` alone reproduces the same named trap — skipping straight to Appendix A/B sticker prices (Verizon Welcome $65/AT&T Value 2.0 $50) and picking the cheapest tier without running D1's eligibility filter, which would surface that Welcome has zero hotspot and Value 2.0 has only 3GB, neither meeting Jake's stated hotspot need. FACILITATOR.md's own soundness language flags exactly this failure to explain *why* the chosen plan moved past the cheapest tier as "the tell that the trap wasn't caught, just guessed past." Guide names the trap; a hurried student's likely wrong path matches it. |
| P4 twist | **PASS** | Reconfirmed against `FACILITATOR.md`'s "Soundness check" (line 138): the twist (Verizon Plus's 30GB hotspot cap vs. Jake's actual hotel/rental-car usage pattern) was re-derived under both a sequential reading (a Hero works D1 first, then hits the twist) and a simultaneous reading, and survives both — it never contradicts Appendix A/B's stated GB figures, and no undisclosed convention in Appendix F is required for it to hold. Nothing about the 2026-08-18 S5/tablet-rate dollar-figure correction touches the twist's mechanism (hotspot GB, not tablet billing), so this finding is unaffected by that correction and stands as previously verified. |
| P5 sensitivity | **PASS_DISCLOSED** | Re-run: `python3 skills/case-readiness/scripts/tier2_probes.py --case phone-plans --probe 5 --flex 0.5`. Base: A=$429.53, B=$510.07 (3-line total, per script's default line count), winner B, margin 18.8%. `verizon_tablet_rate` and `att_tablet_rate` are genuinely unstable at ±50% (verizon_tablet_rate +50% → 34.4% margin, breaches the 20% cap; att_tablet_rate −50% → 35.7%, breaches the cap) but neither flips the winner from B, and both are named with a recorded category/justification in `case.json.sensitivity_disclosure[]` (Category-X proprietary-estimate exception, both tablet rates are not fully carrier-published for the exact tier/discount combination this case needs). `oregon_tax_rate` is structurally stable at ±50% (margin holds at 18.8% either direction — tax is a common multiplier on both carriers' totals, so it cancels in relative terms). No flip at any swept parameter. Passes on the disclosure-aware standard, not the stable-margin standard — this is unchanged in kind from the prior recorded pass, only the absolute margin numbers moved (12.5%→18.8%) following the S5 tablet-rate correction landed earlier on 2026-08-18. |
| P6 data decay | **FAIL** | Live WebFetch of all 8 `sources[]` URLs. **S2** PASS — Verizon Unlimited Plus $80/$70/$70/$55/$45 across 1–4 lines and 30GB hotspot confirmed verbatim on the cited page. **S5** PASS — re-confirms the 2026-08-18 correction: cited page states "As low as $25/mo... $50 w/o discount... With an existing smartphone on an Unlimited plan," and the footnote about the discount capping at one connected device per account (except Unlimited Ultimate) is present verbatim, matching `modeling_assumptions[MA1]`'s disclosure exactly. **S6** PASS — "$20/month" AT&T tablet add-on confirmed verbatim. **S7** PASS — Oregon 22.53% (9.17% + 13.36%) vs. 27.61% national average confirmed verbatim in the cited table. **S8** PASS — Verizon 70%/AT&T 68% 4G LTE land-area coverage confirmed verbatim, including the "particularly in rural and remote regions" framing for AT&T's gap. **S1 and S4 — UNVERIFIED**, not confirmed either way: both return HTTP 403 to automated fetch on two separate attempts (bot-blocking, not a 404/dead-link signal); per MCS-21, reporting these as "confirmed reachable" would be guessing, so they are reported NOT FOUND/UNVERIFIED and need a manual/human-browser recheck before this probe can close. **S3 — FAIL, load-bearing:** the cited reviews.org page confirms only the AT&T Value 2.0 and Extra 2.0 *1-line* prices ($50/mo, $70/mo) and Extra 2.0's data figures (100GB premium/50GB hotspot) — it contains **no multi-line pricing table for Extra 2.0 at all** (confirmed on a second, targeted re-fetch searching the full page). The 2-line/3-line/4-line Extra 2.0 per-line figures ($60/$50/$40) that `case.json`'s D1–D5 tables and every AT&T dollar total in `case.json.derived` actually depend on are **not present at the URL currently cited for them** — this is exactly the "resolves but no longer carries the figure" failure mode SKILL.md calls worse than a dead link, because nothing else in the pipeline would ever notice. This is a pre-existing gap (flagged, not newly introduced, in the 2026-08-18 same-day earlier P6 FAIL as "tighten S3 scope") that the S5 correction did not touch and remains open. |

**P6 net:** the specific finding this pass was dispatched to re-verify — the Verizon tablet add-on
rate (S5) — is now confirmed live-matching and closed. But P6 as a whole is still FAIL: S3's
multi-line AT&T Extra 2.0 pricing is unconfirmed at its cited source (load-bearing, needs either a
better-scoped source URL or a second citation added), and S1/S4 are unverified pending a
non-bot-blocked (human or authenticated-browser) recheck. This skill gates and does not fix —
these three findings are handed back to `case-research`/`case-write`, not resolved here.

### Tier 3 — human dry-run

NOT RUN.

### Net result

Tier 1: clean (TIER1_PASS, 0 blockers). Tier 2: 4 PASS (P1, P2, P3, P4) + 1 PASS_DISCLOSED (P5) +
1 FAIL (P6). Per SKILL.md, `TIER2_PASS` requires **all six** probes at PASS/PASS_DISCLOSED — P6's
FAIL means the case does not clear the gate this pass. `qa.state` set to `BLOCKED`, not
`TIER2_PASS`. `qa.verdict` is NOT set to `"PASS"` (reserved for `TIER2_PASS`). `case-publish` must
not run until S3 is re-sourced/re-scoped and S1/S4 are rechecked outside the automated-fetch
bot-block, and P6 is re-run clean.

---

## case-readiness run — 2026-08-18c (P6 re-sourcing fix; gate completion)

**State:** TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (19 checks), re-run

```
TIER 1 — STRUCTURAL   case: phone-plans   sha256(case.md)=b1cf2dfd2980e41e
checks run: 19   PASS 16 · GAP 3 · FAIL 0

=== BLOCKER (0) ===

=== GAP (3) ===
 * [T1-09] margin 18.8% is inside the cap but wide; the discussion will be one-sided
 * [T1-10] SPEC §8 — new_coverage[] is empty (legacy-conversion carve-out; no uncovered skill
   remains for the title to honestly claim)
 * [T1-18] CONTINUITY — 33 number(s) in Phone Plans - Interactive.html's prose/markup appear in
   neither case.md nor case.json: [0.01, 1.2, 1.3, 1.4, 1.55, 1.6, 1.7, 2.4, 2.5, 3.4, 17.5, 19.0]

=== POLISH (1) ===
 * [T1-07] parsed 16 labels (4 bulleted, 12 from separator-run lines)

VERDICT: TIER1_PASS  (0 blockers, 3 gaps)
```

Same disposition as prior runs: T1-09/T1-10/T1-18 are pre-existing, non-load-bearing GAPs (T1-09
wide-but-in-cap margin; T1-10 legacy-conversion carve-out, verified live against
`standards_spine.json`; T1-18 CSS/markup literals in the published HTML, spot-checked as
rendering/pixel values, not case data). No new drift introduced by the S3/S5 sourcing fixes.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh cold-solve dispatch (7-question packet, no access to `FACILITATOR.md`/`QA_REPORT.md`/`case.json`) reached **B (AT&T Unlimited Extra 2.0)** by the intended route: applied D1's hotspot-eligibility filter first (correctly disqualifying Verizon Welcome for zero hotspot and AT&T Value 2.0 for an inadequate 3GB hotspot allowance) before comparing cost, then optimized on the case's actual specified metric — total monthly family bill after Oregon's 22.53% tax, tracked across 2/3/4 phone lines, not just today's 2-line snapshot. Arithmetic verified against `case.json.derived` and matches to the cent at every line count: D2 Verizon $232.81 / AT&T $196.05; D3 (3-line) Verizon $263.44 / AT&T $232.81; D3 (4-line) Verizon $281.82 / AT&T $245.06. All 7 required questions answered: metric named explicitly; counterargument correctly identifies Verizon's 70%-vs-68% coverage edge on Jake's actual rural routes and correctly notes the case only gives an unverifiable national aggregate, not route-specific data; most-sensitive-assumption answer correctly names Appendix F's tablet-pricing assumption (matching P5's own finding) and correctly reasons that the real one-tablet-discount-cap nuance would widen, not narrow, AT&T's lead; ignored item (Value 2.0's unpublished middle-tier pricing) is correctly reasoned as irrelevant once D1 eliminates Value 2.0; least-supported number correctly flags Appendix E's unsourced coverage percentages. Reaching the right answer for the right reasons — the pass criterion. |
| P2 both-sides | **PASS** | Argument A (Verizon): 30GB hotspot as a real, workable allowance + the sourced 70%-vs-68% coverage edge concentrated on Jake's actual rural routes (Burns/Astoria/Florence) — genuinely quantitative, not a concession sentence. Argument B (AT&T): cheaper at every line count (2/3/4) both pre- and post-tablet/tax, plus a larger 50GB-vs-30GB hotspot allowance. Neither side collapses on inspection — A's weakest point (Appendix E's coverage stat is a national aggregate, not route-specific) is a real limitation but doesn't zero out the argument, since a coverage-percentage edge concentrated in rural terrain remains a plausible real consideration even unquantified at the route level. Consistent with the case's own `balance_test` (18.8% margin, inside the SPEC §2 20% cap — genuinely arguable, not a blowout). |
| P3 trap | **PASS** | `FACILITATOR.md`'s "The trap" names exactly what a learner will *do* wrong: compare Verizon Welcome ($65/line) straight to AT&T Value 2.0 ($50/line) and pick the cheaper number without running D1's hotspot-eligibility filter, missing that Welcome has zero hotspot and Value 2.0's 3GB is functionally inadequate. The fresh P1 cold-solve dispatch (packet-only, no guide access) independently reconstructed this exact reasoning in `answer_1_option` and `answer_3_arithmetic` — disqualifying both cheap tiers on the hotspot test before comparing cost. The case's trap and the guide's anticipation of it match. |
| P4 twist | **PASS** | The twist (Verizon Plus's 30GB hotspot cap vs. Jake's actual four-day-a-week laptop-hotspotting usage pattern) invalidates the position of a room that stopped reasoning at "AT&T is cheaper, done" — it adds a real, non-dollar functional-risk consideration to D5 without changing D1–D4's dollar arithmetic. `FACILITATOR.md`'s own "Soundness check" re-derives the twist under both a sequential reading (D1 first, D5 later) and a simultaneous reading (all of Appendix A/B read at once) and shows it survives either way: it never contradicts the stated GB figures, never requires assuming an unstated hotspot-usage number, and depends on no Appendix F convention the case doesn't state outright. No reading under which the twist silently does nothing. |
| P5 sensitivity | **PASS_DISCLOSED** | `tier2_probes.py --case phone-plans --probe 5 --flex 0.5`: base `{A: 429.53, B: 510.07}`, base margin 18.8%, B wins. Swept the 3 declared dials: `oregon_tax_rate` is stable in both directions (proportional multiplier on both sides, margin unchanged at 18.8%). `verizon_tablet_rate`/`att_tablet_rate` are not stable — extremes push the margin to 3.1%–35.7%, crossing the SPEC §2 20% cap in both directions — but never flip the winner, and both are recorded as Category-X proprietary-estimate exceptions in `sensitivity_disclosure[]` and named explicitly in `FACILITATOR.md`'s Sensitivity note as genuinely load-bearing, not decorative. Disclosed, not eliminated — the disclosure-aware PASS state per the 2026-08-13 doctrine amendment. |
| P6 data decay | **PASS** | Live re-fetch of all 8 `sources[]` URLs, 2026-08-18 (this pass). **S1** (upphone, Verizon Welcome): blocked to direct `WebFetch` (403); re-fetched via a text-extraction reader proxy — exact per-line table confirmed unchanged ($65/$55/$40/$30 at 1/2/3/4 lines). **S2** (bestphoneplans, Verizon Plus): direct fetch confirms $80/$70/$55/$45 at 1/2/3/4 lines, 30GB hotspot — unchanged. **S3** (reviews.org 1-line + att.com official multi-line, the previously-FAILing source): reviews.org confirmed as 1-line-only (no multi-line table, as the case's own citation already discloses); the secondary `att.com/plans/unlimited-data-plans/` URL — the actual source of the load-bearing 2/3/4-line Extra 2.0 figures — was fetched directly via raw HTTPS (HTTP 200, 900KB+ page) and its embedded `planCardPriceDetails` JSON was inspected directly: `{"1 line":"70","2 lines":"60","3 lines":"50","4 lines":"40","5 lines":"40"}` for AT&T Extra 2.0 — an exact match to every dollar figure `case.json.derived` uses. This closes the prior FAIL: the multi-line pricing this case's B-recommendation total depends on is now confirmed at its source, not just asserted. **S4** (att.com Canada/Mexico roaming): blocked to direct `WebFetch` (403); re-fetched via reader proxy — page text confirms "unlimited talk and text within and between the U.S., Canada, and Mexico ... with no roaming charges," matching the cited claim exactly. **S5** (verizon.com tablet pricing): direct fetch reconfirms "$25/mo ... $50 w/o discount ... with an existing smartphone on an Unlimited plan" — the corrected figure from the prior pass holds. **S6** (bestphoneplans, AT&T tablet): direct fetch confirms "$20/month" — unchanged. **S7** (Tax Foundation, Oregon wireless tax): direct fetch confirms 22.53% combined / 27.61% national average — unchanged. **S8** (WhistleOut, coverage): direct fetch confirms Verizon 70% / AT&T 68% — unchanged. All 8 URLs reachable (2 required a non-`WebFetch` reader-proxy route around a bot-block, consistent with MCS-21 — reported as a fetch-method note, not guessed); every cited figure still appears at its source; no drift, no dead links, no unconfirmed load-bearing claims remaining. |

### Tier 3 — human dry-run

NOT RUN.

### Net result

Tier 1: clean (TIER1_PASS, 0 blockers, 3 pre-existing non-load-bearing GAPs, unchanged by this
pass). Tier 2: **6 of 6 probes at PASS/PASS_DISCLOSED** — P1 PASS, P2 PASS, P3 PASS, P4 PASS, P5
PASS_DISCLOSED, P6 PASS. The P6 re-sourcing fix (S3's secondary official `att.com` URL, confirmed
live against the page's own embedded pricing JSON) closes the only remaining blocker to the gate.
`qa.state` set to `TIER2_PASS`. `qa.verdict` set to `"PASS"`. **`case-publish` may now run.**
