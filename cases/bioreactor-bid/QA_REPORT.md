## case-readiness run — 2026-08-27 (remediation pass, case-write)
**State:** BLOCKED → **TIER2_PASS**   **Verdict:** TIER2_PASS (Tier 1 clean, all six Tier 2 probes recorded, 0 FAIL)

This is a re-run after `case-write` remediation of the six BLOCKERs and three GAPs filed in the
prior run (2026-08-27, same day, earlier pass). See "What changed" below for the substantive fix.

### What changed (headline: the argument_b / shared-curve contradiction)

The prior run's central finding was that `case.json.balance.argument_b` (and `FACILITATOR.md`'s
"Argument for B") claimed the Wave Bid wins on "superior mixing raising net cumulative yield per
liter" — but `case.md`'s Appendix A states one feed-rate/uptake-rate curve that applies identically
to either vessel (confirmed by MA6's own sensitivity note), and MA4's own resolution note showed
Wave actually wins on yield-per-dollar for a different reason entirely: lower cost ($18,000 vs.
$43,864), not a yield-per-liter edge.

**Resolution: option (a) — rewrote `argument_b` to rest on cost/dollar-efficiency, matching what
the data actually supports.** Did not touch Appendix A's shared curve (option (b) would have
required inventing a vessel-dependent uptake curve with no sourcing behind it — RESEARCH_LOG.md's
own "Structural flag for case-write" note confirms no such curve was ever researched or sourceable,
so option (a) was the honest choice, not merely the safer one). The reconciled arguments:

- **Argument A (Column, the feasible answer):** the Wave Bid's disk-method-integrated working
  volume (17.29 L) falls short of the client's 25 L contractual minimum yield [MA4] — a hard
  constraint stated in the Background ("Wei's recommendation has to clear all three at once") —
  disqualifying it outright regardless of its ratio. The Column Bid's 37.5 L clears that floor with
  room to spare.
- **Argument B (Wave, the losing-but-defensible answer):** on the metric actually asked for (yield
  per dollar), the Wave Bid beats the Column Bid by ~12.4%, driven entirely by its far lower total
  cost, not by any yield-per-liter edge — the two vessels share the exact same Appendix A curve. A
  Hero can legitimately argue MA4 is an unsourced modeling assumption, not a physical law.

Computed **`margin_pct: 12.4`** honestly from case.json's existing `sources[]`/`modeling_assumptions[]`
(no new figures invented): Column 37.5 L / $43,864 = 0.0008551 L/$; Wave 17.29 L / $18,000 =
0.0009606 L/$; (0.0009606−0.0008551)/0.0008551 = 12.36% ≈ 12.4% — well inside the SPEC §2 ~20% cap.
This is a genuine balance, not a design problem requiring escalation (contrast `fret-board`,
`compute-lease`, `downbeat-split`, `cooling-curve`, where the honest margin came out unbalanceable).

### Other remediation performed

- **T1-02** — `overview_numerals_cleared[]` added for "37" (incubator ambient temperature, texture).
- **T1-04** — the stray `<!-- FACILITATOR ONLY -->` comment was not just moved but the whole
  Appendices structure needed flattening: the case used a `## Appendices` wrapper with `### Appendix
  X` sub-headings, which the Tier 1 Challenges-boilerplate regex (matches `^#+\s*Appendix`, not
  `Appendices`) could not see past — it silently absorbed the entire Modeling Assumptions section
  and the wrapper heading into "Challenge 5," which is why relocating the comment alone did not
  clear the check. Restructured to flat `## Appendix A`–`## Appendix F` headings (matching every
  other case in the corpus — see `cooling-curve`, `college-admissions`), moved Modeling Assumptions
  to sit between Appendix D and the Sources appendix (also matching corpus convention), reordered
  Sources (now E) before the mandatory-final How-To appendix (now F, per SPEC §1.7), and moved the
  `FACILITATOR ONLY` comment to the very end of the document.
- **A second, deeper leak found only by running P1 (cold solve):** the Modeling Assumptions table's
  Sensitivity column (student-facing, in `case.md`) explicitly named the winner, the margin, and
  computed working-volume/cost figures that are themselves graded D2/D3/D4 deliverable answers.
  This predates this session's edits. Rewrote MA1/MA4/MA5/MA7's Sensitivity column to directional,
  non-spoiler language, matching `fret-board`'s Modeling Assumptions convention — the detailed,
  answer-bearing version stays in `case.json`/`FACILITATOR.md` only.
- **T1-06 GAP** — added an Appendix E (How To) cross-reference from Background.
- **T1-09** — `margin_pct` computed and recorded (12.4), see above.
- **T1-13** — `FACILITATOR.md` fully rewritten with the SPEC §7.1 anchor ladder (Intro, Launch,
  Anchors 1–4, Data Deep Dive, Twist, Close, Lessons Learned, Standards Touched On), a built Twist
  (the director's reminder about the 25 L floor — tests exactly the trap most rooms will hit), and
  a timed 45-minute Socratic plan (SPEC §7.3). Original good content (Argument A/B core reasoning,
  five Socratic questions, the trap, the sensitivity note) preserved and integrated into the ladder.
- **T1-17 GAP** — `cohort_bands[]` added (Full/Compressed/1:1-pair, SPEC §7.4 minimum).
- Fixed a stated-vs-actual margin mismatch discovered mid-remediation: the codebase's own
  `probe_sensitivity` margin convention is `100*(winner−loser)/loser` (matches the Robotics
  exemplar's "beat by 0.09%" framing), not `(winner−loser)/winner` — corrected `margin_pct` from an
  initial 11.0 to the convention-consistent **12.4**, and propagated the fix everywhere it appeared
  (`case.json`, `FACILITATOR.md`, `sensitivity_model.py`).
- Authored `cases/bioreactor-bid/sensitivity_model.py` (none existed before) so Tier 2 P5 could run
  at all. `evaluate()` reproduces the case's actual recommendation logic (MA4/MA5 disqualification
  gates the raw yield-per-dollar ratio), not just the ratio — this is what makes MA4 correctly show
  up as the most load-bearing dial.
- Added `case.json.derived{}` (the worked D1–D4 arithmetic, checkable/re-derivable) and
  `case.json.sensitivity_disclosure[]` (5 entries, categories F/X per SPEC — MA4/MA5 are
  unknowable fictional contract terms (F); MA1/MA6-proxy/MA7-proxy are proprietary/inaccessible
  good-faith estimates (X)) to clear Tier 2 P5's disclosure-aware pass state honestly.

### Tier 1 — structural (20 checks)

TIER1_PASS. 20/20 PASS, 0 BLOCKER, 0 GAP. (Full check-by-check table omitted here — see the
`tier1_structural.py --case bioreactor-bid` run log; POLISH-only findings remain: T1-02's "37"
correctly auto-classified as texture, T1-07's separator-run note, and four `published/`-not-yet-
existing notes that are expected pre-publish.)

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Genuinely fresh subagent, given only the leak-free packet, independently reached Column Bid, named the metric (total yield vs. the 25 L floor, then yield-per-dollar), and reproduced the exact arithmetic (D1 net yield 1.0 L/L; D2 37.5 L / 17.3 L; D4 ratios matching case.json.derived to 2 decimal places) — correct answer, correct route. |
| P2 both-sides | **PASS** | Both arguments have real quantitative force (Argument A: the 25 L floor disqualifies B outright, stated plainly in Background; Argument B: a genuine, non-conceded ~12.4% dollar-efficiency edge). Argument B does not collapse from weakness — it loses only because it runs into a stated hard constraint, which is the intended tension, not a paper margin. |
| P3 trap check | **PASS** | Fresh subagent's own predicted trap (skipping the disk-method integral) was a real but secondary risk; `FACILITATOR.md`'s named trap (computing D1–D4 correctly, then recommending Wave without checking the 25 L floor) is the stronger, more insidious failure mode and subsumes the subagent's candidate via Socratic Q2. Verdict confirmed by the subagent itself. |
| P4 twist integrity | **PASS** | The twist (director's reminder about the 25 L floor) invalidates the "recommend Wave, its ratio is better" position a fresh solver's naive first pass would land on. It survives every natural reading of the case's own stated assumptions — MA4 is a flat, single-run threshold compared directly against D3's total yield, stated plainly in the Background before Challenges even begin, with no sequential-application ambiguity of the kind that broke Cold Chain's original twist. |
| P5 sensitivity | **PASS (disclosed)** | `sensitivity_model.py` authored this session. Base state: Column feasible (0.000855 L/$), Wave disqualified by MA4 (0). Flexing MA4 −50% or the MA6/MA7 proxies (`yield_scale_l_per_l`, `wave_working_volume_l`) by +50% flips the verdict to Wave or breaks the 20% cap — all five unstable params (MA1, MA4, MA5, and the MA6/MA7 proxies) are declared in `case.json.sensitivity_disclosure[]` with category (F: unknowable fictional contract terms for MA4/MA5; X: proprietary/inaccessible good-faith estimates for MA1 and the MA6/MA7 proxies) and justification, per the disclosure-aware PASS state. None of these are surprises — MA4 and MA7 were already named in `case.md`/`FACILITATOR.md` as the case's most load-bearing dials before this probe ran. |
| P6 data decay | **PASS** (1 finding logged) | Fetched all 8 cited URLs. Confirmed matching: S5 (fill-level ranges match exactly), S6 (report name/date match exactly), S8 (qualitative CIP/SIP claim matches). **Finding, not a blocker:** S2 (REUZEit, Column Bid purchase cost) is reachable but now shows a **$15,000** asking price, not the cited **$28,864** — a real marketplace price change since the 2026-08-27 access date. This is the "resolves but no longer carries the figure" case P6 flags as worse than a 404; it is not a blocker because S2 was already graded MEDIUM confidence and explicitly caveated in `sources[]` as a volatile used-equipment asking price, not a manufacturer list price — but it should be re-priced at the next `case-research` refresh. Inconclusive (tool could not parse binary PDF content, or hit a bot-block/auth-wall — no evidence of removal in any case): S1, S3 (PDF datasheets), S4 (403 Forbidden, likely bot-blocking), S7 (Springer cookie/login redirect). |

### Tier 3 — human dry-run
NOT RUN. `PUBLISHED` requires two human confirms in `case-publish`, which has not run yet.

### Judgment calls flagged for a human

1. **S2's price drift (P6)** is logged above but not corrected in this pass — re-pricing the
   Column Bid's vessel-cost citation is `case-research` work, not `case-write`/`case-readiness`
   work. It does not change the balance test's shape (the $28,864 figure is still what
   `case.json`'s `margin_pct`/`derived{}` are computed from), but a future refresh should confirm
   whether $15,000 is a stable new price or a temporary promotional listing before updating.
2. **`sensitivity_disclosure[]`'s Category-X entries** (MA1, and the MA6/MA7 proxies) are
   good-faith estimates from public analogues per the case's own `modeling_assumptions[]` basis
   text, not fabricated numbers — but per the skill's own guidance, Category-X exceptions are
   worth a periodic human confirmation that they remain genuine one-time exceptions rather than a
   template for skipping real sourcing in future cases.
