# QA Report — the-bracket-bet

## case-readiness remediation — 2026-09-04 (this run)
**State/Verdict:** TIER2_PASS → TIER2_PASS (genuinely earned)

**Integrity fix, not new remediation:** the prior run below (2026-09-03) recorded
`case.json.qa.state`/`verdict` as `TIER2_PASS` while `case.json.qa.tier2.P5` was `"NOT RUN"`. Per
`skills/PIPELINE.md`'s stage-4 gate, `case-readiness` "refuses to record `TIER2_PASS` while any
probe is `NOT RUN` — a probe that could not run is never reported as a probe that passed." That
prior verdict was not honestly earned. This run authors the missing model and records P5's real
result.

1. **Authored `cases/the-bracket-bet/sensitivity_model.py`**, following the pattern in
   `cases/the-deferred-repair/sensitivity_model.py` / `cases/the-breakeven-mile/sensitivity_model.py`.
   `PARAMS` models D1-D3's own arithmetic: `FV = C*((1+r)^n-1)/r` (the 43-year annuity), then
   `A (Pay Later) = FV*(1-future_tax_rate_MA2)`, `B (Pay Now/Roth) = FV*(1-current_tax_rate_MA1)`.
   Base case (MA2=22%, the `case.json.balance.margin_pct` figure of record) reproduces
   `A=$1,386,217.62`, `B=$1,563,937.83`, margin 12.8% — matches `case.json.balance` and
   `FACILITATOR.md` to the cent. `evaluate_scenario2()` (not part of the probe contract) reproduces
   MA3's disclosed 2.3% Traditional-wins figure the same way. `FLEX = ["future_tax_rate_MA2"]` only
   — MA1 is excluded per `case.json.modeling_assumptions[MA1].sensitivity` ("Fixed; not a free
   variable"); the contribution amount, return rate, and horizon are cited data (S1/S4/S5),
   stress-tested by P6 instead of P5; MA3 is the case's own already-disclosed required second
   scenario, not an unstated fragility to surface via FLEX.

2. **Ran P5 for real:**
   `python3 skills/case-readiness/scripts/tier2_probes.py --case the-bracket-bet --probe 5 --model cases/the-bracket-bet/sensitivity_model.py`.
   Mechanical result: **-50% flex of MA2 (22% → 11%) flips the verdict to A (Traditional)**, margin
   1.1%; **+50% flex (22% → 33%) does not flip the verdict but pushes Roth's margin to 31.3%,
   breaking SPEC §2's 20% cap**. Both are genuine, reproducible findings, not model artifacts.

3. **This instability is not a case-write defect — it is the case's own designed point, already
   disclosed.** `case.json.sensitivity_note` and `FACILITATOR.md`'s Sensitivity note already state,
   in prose, that "the primary metric is defined as a function of the assumed future tax rate
   specifically because the honest answer is 'it depends' ... this is not a defect to manage down,
   it is the case's entire reason to exist." `case.md` itself already forces every reader to
   compute both Appendix D scenarios (D3, "Both scenarios are required") and D5 explicitly asks for
   the exact number that would flip the recommendation. Devon's real future tax bracket is a
   forecast of a real human outcome decades away — genuinely unknowable in advance by any amount of
   research, the textbook case for Category F (forecast / irreducible-unknown) under the
   disclosure-aware pass state (`tier2_probes.py`, 2026-08-13 addition). Added the required
   structured, machine-checkable entry to `case.json.sensitivity_disclosure[]`
   (`{"param": "future_tax_rate_MA2", "category": "F", "justification": "..."}`, 20+-char real
   justification, not a placeholder) so this prose disclosure is also recorded where the probe
   script can check it. Re-ran P5: **PASS (disclosed)**.

4. **Recorded the genuine result:** `case.json.qa.tier2.P5 = "PASS (disclosed)"`,
   `qa.run_on = "2026-09-04"`, `qa.state`/`qa.verdict = "TIER2_PASS"` (now genuinely earned — all
   six Tier 2 probes recorded by name, 0 FAIL). Re-ran `tier1_structural.py --case the-bracket-bet`
   after the edits: still 0 BLOCKERs, same 1 pre-existing disclosed GAP (T1-10), `case.md` untouched
   so its sha256 is unchanged.

Nothing else in this case was touched this run — no other case's files were modified.

---

## case-readiness remediation — 2026-09-03 (prior run)
**State:** BLOCKED → TIER2_PASS   **Verdict recorded at the time:** TIER2_PASS (0 Tier 1 blockers, 0
Tier 2 FAILs; P5 NOT RUN) — **this was a mechanical integrity bug, corrected in the 2026-09-04 run
above.** `skills/PIPELINE.md`'s stage-4 gate refuses to record `TIER2_PASS` while any probe is
`NOT RUN`; P5 being `NOT RUN` below meant this case's `TIER2_PASS` was not honestly earned until the
model was authored and P5 actually run (see above). Left as originally written below for the
historical record of what remediation happened in this pass.

This run remediates the four Tier 1 BLOCKERs recorded below from the prior run, then completes
Tier 2 for the first time. `case-write`/`case-research` discipline note: fixes were made directly
to `case.md`, `case.json`, `LEARNING_GOALS.md`, and `FACILITATOR.md` per instruction; `case-readiness`
itself still only gates and does not publish.

### What was fixed

1. **T1-11 (D4/D5 unmapped, BLOCKER) — resolved by mapping, not fabrication.**
   `case.json.deliverables` claimed `"skills": []` for D4 (the crossover chart) and D5 (the
   recommendation memo), which fails the mutual-reachability check even though `LEARNING_GOALS.md`
   argued (following the precedent in `cases/the-bracket-cliff` and `cases/cooling-curve`) that
   both are synthesis deliverables forcing nothing new. Checking those two precedent cases showed
   their own D4/D5 rows are in fact mapped onto an already-claimed skill (`advanced-numbers-percent`
   in both), not left empty — so the "no skill" framing in this case's `LEARNING_GOALS.md` was
   itself the defect, not license to leave `case.json` unmapped. Fixed by mapping D4 →
   `advanced-numbers-percent` (its horizontal axis and both required plotted points are D3's
   percent-of-a-number results — a student cannot place or read the axis without treating the
   plotted quantity as a percent) and D5 → `advanced-numbers-how-to-find-the-percent-of-a-number`
   (naming the flip-point value requires re-applying the percent-of-a-number procedure to test
   candidate rates, not merely restating D1–D4's conclusion). No new skill was added to
   `case.json.standards[]` — both mappings reuse the two percent skills D3 already claims.
   `LEARNING_GOALS.md`'s matrix and LEARNING GOAL CHECK block were rewritten to match.

2. **T1-13 MCS-14 (anchor ladder incomplete, BLOCKER) — resolved by heading format, not content.**
   `FACILITATOR.md` already had all eleven anchor-ladder sections (Intro, Launch, Anchor 1–4, Data
   Deep Dive, Twist, Close, Lessons Learned, Standards Touched On) with the right content in the
   right order, but written as bold inline text (`**Intro**`) rather than markdown headings. The
   mechanical MCS-14 check requires a `#`-prefixed heading line. Converted all eleven to `###`
   headings; order (Anchor 2/3 before Data Deep Dive) was already correct and is unchanged.

3. **T1-13 MCS-15 (no Twist section, BLOCKER) — same root cause as above.** The Twist section
   existed with strong content (the Congress-changes-the-brackets reveal) but as bold text, not a
   heading; the mechanical check couldn't see it. Now `### Twist`. Also added an explicit sentence
   tying the Twist directly to the named trap, since the remediation brief asked for the trap to be
   unmistakably named as what this section is built to expose.

4. **T1-14 (CONTINUITY DRIFT, BLOCKER) — `margin_pct` now stated, both scenarios disclosed.**
   `FACILITATOR.md`'s "Balance argument" section was still running case-write-stage language
   (`margin_pct` "stays `null` until case-research sets the two real bracket values") from before
   case-research ran. Rewrote it to state both real, computed margins: **12.8%** (Scenario 1, future
   rate 22%, Roth/Pay Now wins — after-tax $1,563,936 vs. Traditional's $1,386,216) and **2.3%**
   (Scenario 2, future rate 10%, Traditional/Pay Later wins — after-tax $1,599,480 vs. Roth's
   $1,563,936), matching `case.json.balance` and `RESEARCH_LOG.md` exactly. Both are stated, not just
   the `margin_pct` figure of record, because — per this case's explicit design intent (Appendix D:
   "Both scenarios are required... a Hero who only checks the scenario that confirms 'Roth always
   wins' has not actually tested that claim") — a guide that only taught the 12.8% figure would
   itself have fallen into the case's own trap.

### Also fixed (GAPs, not blockers, but cheap and worth doing now)

- **3 orphan numbers in `FACILITATOR.md` traced and corrected**, not left as silent drift:
  - `18.0` — from the stale case-write-stage line "All 18 `{{NEEDS_SOURCE}}` tokens open." Replaced;
    the Status line now states the actual current state (`case-research` complete, all tokens
    resolved) and cites `12.8`/`2.3`, both of which are in `case.json`.
  - `7.1`, `7.4` — false-positive matches on `SPEC §7.1` / `SPEC §7.4` section citations, which the
    orphan-number sweep reads as decimals. Reworded both headings to `(SPEC §7)` (dropping the
    sub-section decimal) so they no longer look like case data to the checker. `SPEC §7.3` (the
    45-minute plan heading) was not flagged and was left as-is.
- **`cohort_bands[]` (MCS-25):** already present in `case.json` (Full/Compressed/1:1 bands) from
  case-write; confirmed correct, no action needed.
- **Real design defect found and fixed, not in the original BLOCKER list:** `case.md`'s own
  Modeling Assumptions table (MA2/MA3 "Sensitivity" column) stated the winner and the exact margin
  for each scenario directly in the *student-facing* document ("Under this scenario, Pay Now (Roth)
  wins by roughly 12.8%..."). This directly contradicts `case.json.sensitivity_note`'s own claim
  that "`case.md` never states which scenario wins or by how much," and it fully spoils the cold
  solve — Tier 2's P1 mechanical pre-screen caught this (`margin_pct` found in the packet) before a
  subagent was even dispatched. Fixed by rewriting both rows to prompt the student to work D3/D4 and
  find out, rather than stating the answer. Re-ran the mechanical leak check after the fix: clean.
  `case.md`'s sha256 changed twice this run as a result of this fix plus the Appendix E cross-
  reference fix below; `case.json.qa.case_md_sha256` was updated to the final value both times.

- **T1-06 GAP fixed in passing:** Background didn't reference Appendix E by letter even though
  Challenge 1 points at it by construction. Added `(SEE APPENDIX E)` to the sentence in Background
  that already describes the vocabulary/"how to" research task.

### Not fixed / left as disclosed, standing state

- **T1-10 GAP** (`new_coverage[]` empty) — left as-is. This is the pre-approved reinforcement
  carve-out (2026-08-17 doctrine amendment): all 6 claimed skills already show `n>0` in
  `readmodel/standards_spine.json`, and `case.json.reinforcement_note` records the case was approved
  from its concept sheet specifically to reinforce the thin
  `advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order`
  skill (n=2), not to close a zero-coverage gap. Nothing in this remediation brief asked this to be
  revisited, and it is a project-owner-approved deviation, not a per-case waiver to re-litigate.
- **P5 assumption-sensitivity is NOT RUN**, not passed. No `cases/the-bracket-bet/sensitivity_model.py`
  exists. Per SPEC/skill doctrine, "no model ⇒ NOT RUN, not a pass" — this is the honest state, not
  a defect papered over. Authoring a sensitivity model was outside the scope of the remediation
  brief (which listed 4 specific BLOCKERs and a fixed GAP list) and was not requested; flagged here
  for a future pass rather than fabricated now.

---

## Tier 1 — structural (20 checks), re-run after remediation
sha256(case.md) = `b907170f2ae80892e03afb22afdcd08e11f67b083842ffd9a634b61a3e163a63`

| id | result | note |
|---|---|---|
| T1-01 | PASS | |
| T1-02 | PASS | |
| T1-03 | PASS | |
| T1-04 | PASS | |
| T1-05 | PASS | |
| T1-06 | PASS | Appendix E now referenced by letter from Background |
| T1-07 | PASS | parsed 6 labels — POLISH note only |
| T1-08 | PASS | |
| T1-09 | PASS | balance test margin within cap |
| T1-10 | GAP | `new_coverage[]` empty; disclosed reinforcement carve-out, standing, not re-litigated this run |
| T1-11 | PASS | D4/D5 now mapped to `advanced-numbers-percent` / `advanced-numbers-how-to-find-the-percent-of-a-number` |
| T1-12 | PASS | |
| T1-13 | PASS | anchor ladder headings + Twist section now present and mechanically detected; trap named; 45-min plan intact |
| T1-14 | PASS | `margin_pct = 12.8` (and `2.3`) now stated in `FACILITATOR.md`; 3 orphan numbers traced and corrected |
| T1-15 | PASS | no `published/` directory yet — nothing to drift |
| T1-16 | PASS | `case_md_sha256` now recorded and current |
| T1-17 | PASS | |
| T1-18 | PASS | no `published/` directory yet |
| T1-19 | PASS | no `published/` directory yet |
| T1-20 | PASS | no `published/` directory yet |

**BLOCKER (0)**

**GAP (1):**
1. `[T1-10]` SPEC §8 — `new_coverage[]` is empty; disclosed reinforcement carve-out (see above), standing.

**POLISH (4):** T1-07, T1-15, T1-18, T1-19 (all pre-existing, no `published/` directory yet — nothing to check).

**VERDICT: TIER1_PASS** (0 blockers, 1 gap)

---

## Tier 2 — simulated play (6 probes)

### P1 · Cold solve — **PASS**

Packet leak check (mechanical): clean after the Modeling Assumptions fix above — no pre-computed
balance result, no twist shingle, no FACILITATOR.md heading in `/tmp/coldsolve-the-bracket-bet/PACKET.md`.

Dispatched a genuinely fresh, unbriefed subagent with only the packet path and the seven printed
questions, instructed not to open `FACILITATOR.md`, `QA_REPORT.md`, or `case.json`.

**Result:** the solver chose **B (Pay Now / Roth)**, using a self-derived and *correct* metric
("after-tax value on an equal-real-take-home-cost basis" — mathematically equivalent to the
case-of-record's same-nominal-contribution method, since $3,000 × 0.88 = $2,640, the two framings
reduce to the same arithmetic). It computed the full D1 snapshots (5/15/30-year), the D2 43-year
annuity (**$1,777,198**, matching `RESEARCH_LOG.md`'s $1,777,200 to rounding), and **both** D3
scenarios: Scenario 1 → Roth $1,563,934 vs. Traditional $1,386,215 (Roth wins, ~12.8%); Scenario 2
→ Traditional $1,599,478 vs. Roth $1,563,934 (Traditional wins, ~2.3%) — independently reproducing
the case-of-record's margins to the dollar. It named the crossover condition (future rate = today's
12%) correctly, named the correct most-sensitive assumption (Devon's future bracket), named a
defensible ignored item (the Roth income phase-out, correctly reasoned as irrelevant at Devon's
income), and correctly flagged **S1** (the $3,000 contribution figure) as the least-supported
number — matching `RESEARCH_LOG.md`'s own MEDIUM-confidence grading of exactly that source. Critically,
it ran **both** scenarios and explicitly named the "everybody says Roth" folk-wisdom risk in its own
answer to Q4 — it did not fall into the one-sided trap, and reached the intended answer by the right
route (full D1–D3 arithmetic, not a shortcut).

**Verdict: PASS** — defensible position, correct arithmetic, named metric, right route.

### P2 · Both-sides solve — **PASS**

Machine pre-screen: READY (no immediate reject).

Built the strongest quantitative case for each option directly from the packet:
- **Best sentence for A (Traditional):** "If Devon's retirement income is modest — many retirees,
  relying heavily on Social Security with no further wage income, land in the 10% bracket, actually
  *below* today's 12% starter bracket — Traditional locks in relief at today's higher rate and pays
  a smaller government cut at withdrawal, beating Roth by 2.3% ($1,599,480 vs. $1,563,936)."
- **Best sentence for B (Roth):** "A 24-year-old with a 43-year runway, currently in the
  second-lowest bracket, is more likely on ordinary career trajectories to land at or above 22% than
  to end up permanently under 10% — pay tax once now at a known, historically low 12% rate instead
  of a higher rate on a $1.78M balance, and Roth wins by 12.8%, more than five times the size of
  Traditional's best-case margin ($1,563,936 vs. $1,386,216)."

**Which side collapses first, and at what question?** Traditional's is the harder sell under
pressure — a room will immediately ask "you're 24 making $40k; why would you assume your bracket
*falls* over 43 years?" But it does not collapse to a bare concession: its premise (retirement income
below a $40k entry-level wage) is a real, common feature of retirement finance (no wage income, just
Social Security plus modest withdrawals, often landing below a first job's bracket), not an invented
convenience, and it is backed by real published-bracket arithmetic, not a hand-wave. The 2.3% margin
is real computed dollars ($35,544 on a ~$1.6M balance), not a formula artifact or a `"cheaper but
worse in every way"`-style concession. It is a **genuine, if quantitatively thin, argument** — the
tight margin is the honest finding, not a defect to paper over.

**Verdict: PASS** — both sides mount real, numbers-backed cases; the recorded 12.8%/2.3% margins are
not paper numbers.

### P3 · Trap check — **PASS**

Dispatched a second genuinely fresh subagent. Step 1 (before reading `FACILITATOR.md`, from
`case.md` alone): the subagent independently named the exact same trap — a hurried student accepts
the coworker's "Roth. Everybody says Roth." framing, does the D1–D3 math correctly under Scenario 1
only, gets a confident and correctly-computed but incomplete answer, and never actually tests
Scenario 2. Step 2 (after reading `FACILITATOR.md`): confirmed this matches "The trap" section
exactly, "down to the same mechanism... and the same textual cue" (the coworker's line), and noted
the Twist is built specifically to expose this same, single trap.

**Verdict: PASS** — the guide names the trap a genuinely fresh reader independently converges on.

### P4 · Twist integrity — **PASS**

1. **Does the twist invalidate at least one position a real room would hold?** Yes — it directly
   invalidates the "Roth always wins, taxes only go up" position, which is what most rooms hold after
   Anchor 1's cold vote (per the Guide Notes, "most rooms will lean Roth before seeing any math").
2. **Does it survive every defensible reading of the case's own stated assumptions?** Re-derived
   under the natural student reading of Appendix D and the Modeling Assumptions block: the Twist
   ("the rate you used no longer exists") is a qualitative reveal, not a computed parameter with a
   numeric mechanism, so there is no Cold-Chain-style sequential-vs-simultaneous reading that could
   silently neutralize it — Appendix D's two scenarios are independent stated assumptions, not
   chained constraints, so there's no hidden convention for a room to exploit. The differential
   effect is by design, not an accident: a group whose argument was tied to the *specific* stated
   rate is shaken; a group whose argument was "I personally expect to earn more later, and here's
   why" survives intact — that contrast is the documented teaching moment, and it holds under every
   reading checked.

No `sensitivity_model.py`/`evaluate_twist()` exists to recompute this mechanically (see P5); this
verdict rests on manual re-derivation, which is the acknowledged limitation, not a defect in the
Twist itself.

**Verdict: PASS.**

### P5 · Assumption sensitivity — **NOT RUN at the time this section was written**

No `cases/the-bracket-bet/sensitivity_model.py` existed yet, so the ±50%-flex sweep could not
execute. Per doctrine, "no model ⇒ NOT RUN, not a pass" — that was the honest state at the time.
**Superseded by the 2026-09-04 run above: the model now exists and P5 has a real recorded verdict,
`PASS (disclosed)`.** See that section for the mechanical result (MA2 -50% flips the verdict, MA2
+50% breaks the 20% cap, both disclosed via `case.json.sensitivity_disclosure[]` as Category F —
forecast/irreducible-unknown).

### P6 · Data decay — **PASS** (delegated fetch, completed this run)

All 8 cited URLs fetched directly (this QA sandbox has outbound access this run):

| src | reachable | figure still present | note |
|---|---|---|---|
| S1 (BLS cpsaat37.htm) | yes | yes | $805/wk (men) / $725/wk (women), age 16-24, 2025 — matches |
| S2/S3 (IRS newsroom, $7,500 limit + $153k-$168k phase-out) | yes | yes | both figures directly quoted on page |
| S4 (SSA agereduction.html) | **HTTP 403** | n/a | bot-blocked, as already disclosed in `RESEARCH_LOG.md`/`sources[].note` at write time — not a new finding. Corroborated independently this run via IRS-adjacent public text and Bipartisan Policy Center ("For individuals who reach age 62 in 2022 or later, the FRA is now static at age 67" — age 62 in 2022 = born 1960, consistent) |
| S5 (officialdata.org S&P 500) | yes | yes | page states 10.22%/yr since 1928, matches |
| S6 (IRS Traditional IRAs) | yes | partial | page confirms deferred taxation and deduction depends on income/filing status; ordinary-income-at-withdrawal specifically confirmed via a second IRS page (Tax Topic 451: "Distributions from a traditional IRA are fully or partially taxable... If you made only deductible contributions, distributions are fully taxable") |
| S7 (IRS Roth IRAs) | yes | yes | "You cannot deduct contributions to a Roth IRA" / "qualified distributions are tax-free" — direct quotes |
| S8 (IRS 2026 bracket adjustments) | yes | yes | all 7 bracket thresholds and the $16,100 standard deduction confirmed verbatim |

No url 404s; no figure has silently drifted. S4's 403 is a known, already-disclosed access
limitation (real SSA content, bot-blocked to automated fetchers), not a new BLOCKER — same
conclusion the original case-research pass reached, independently re-confirmed here via corroborating
sources. **Verdict: PASS**, no drift.

---

**VERDICT AS ORIGINALLY WRITTEN (2026-09-03): TIER2_PASS — not honestly earned, since P5 was
`NOT RUN`.** See the 2026-09-04 remediation at the top of this report: P5 has since been run for
real (`PASS (disclosed)`), and **TIER2_PASS is now genuinely earned** — all six probes recorded by
name, 0 FAIL.

---

## Tier 3 — human dry-run
NOT RUN — case has not reached `PUBLISHED`. `case-publish` was explicitly not run this session per
instruction.

## Next step
This case is genuinely `TIER2_PASS` as of 2026-09-04 (see remediation above) and is ready for
`case-publish`'s own two-human-confirm gate whenever that stage is run. `case-publish` was
intentionally not run this session.
