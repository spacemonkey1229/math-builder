## case-readiness run — 2026-09-04

**State:** DRAFT → TIER1_PASS → TIER2_PASS (P7 via disclosed waiver, MCS-49, unconfirmed by a
human project owner — see below). **Verdict:** TIER1_PASS clean; 6/7 Tier 2 probes genuinely PASS;
P7 mechanically FAILs three consecutive zero-context cold-reads and is recorded PASS only through
a documented MCS-49 disclosure waiver that still needs human sign-off.

### Tier 1 — structural (21 checks)

sha256(case.md) = `a05401b07403ce3d21d77358787d7f8e052c42808a4ca1689b35a5601afb89f6`

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview numerals ('2', '3', '401') cleared in `case.json.overview_numerals_cleared[]` — UI-progress-bar texture, a scene-setting day-count, and the fixed proper-noun "401(k)" |
| T1-03 | PASS | Dilemma binary, opens "You are Devon Okafor." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim; a leaked `<!-- FACILITATOR ONLY -->` comment after Challenge 5 was removed |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | all appendices referenced from Background |
| T1-07 | PASS | final appendix (F) is verbatim spine labels |
| T1-08 | PASS | every number cited (S1-S7) or declared an assumption (MA1-MA3) |
| T1-09 | PASS | `margin_pct` = 8.56, both arguments written |
| T1-10 | GAP | `new_coverage[]` empty; downgraded from BLOCKER via the 2026-08-17 reinforcement carve-out — see `case.json.reinforcement_note` |
| T1-11 | PASS | learning-goal mutual reachability (0 unmapped, 0 unreachable) |
| T1-12 | PASS | tier (T4) vs numeric load (compound growth, percent, marginal-rate/discontinuity concept, a stated forward-looking assumption) |
| T1-13 | GAP | Twist recorded `N/A`, justified in FACILITATOR.md |
| T1-14 | PASS | FACILITATOR.md numbers reconcile with case.json (added `sensitivity_disclosure[]` and an explicit $13,093.92/yr figure to close two initially-orphaned numbers) |
| T1-15 | PASS | no `published/` dir — nothing to drift |
| T1-16 | PASS | `case.json.qa.case_md_sha256` resynced and verified byte-for-byte against the final case.md |
| T1-17 | PASS | `cohort_bands[]` declared (Full / Compressed / 1:1 pair) |
| T1-18/19/20/21 | PASS | no `published/` dir — nothing to check (this case is deliberately not published, per the task's scope) |

**BLOCKER (0). GAP (2), both documented carve-outs, not defects** — same evidentiary shape as
`cases/the-two-offers/case.json`'s two GAPs:
- **[T1-10]** `case.json.reinforcement_note` records a live spine check (2026-09-04): all 6 claimed
  skills already have `n>=3`; the case was deliberately approved to reinforce three of the spine's
  thinnest skills (`advanced-operations-exponent-also-power` n=5, `advanced-operations-how-to-evaluate-an-exponential-expression`
  n=5, `calculus-instantaneous-rate-of-change` n=3) while closing the Taxes & tax-advantaged-accounts
  topic gap. Adjacent uncovered skills (compound interest, annuity, piecewise function, marginal
  rate — none exist in the spine as distinct how-tos) were checked and ruled out before settling on
  this set.
- **[T1-13]** `Twist: N/A`, justified in FACILITATOR.md: the case's tension is a fully-disclosed
  sensitivity (MA1) the student is already invited to challenge in Challenge 2; a genuine held-back
  twist would require either leaking the margin into case.md or inventing an unsourced fact. D3's
  marginal-return reveal (the abrupt rate change at the cap) is named as carrying the twist's
  surprise-and-recompute function instead.

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A fresh, unbriefed agent given only `/tmp/coldsolve-free-money-with-strings/PACKET.md` (no access to FACILITATOR.md/case.json) chose B (Stack & Grow), built the correct annuity arithmetic independently ($192,231.31 vs. $208,683.37, an 8.6% margin — matching `sensitivity_model.py` to within rounding), named the metric explicitly, gave a genuine counter-argument (sequence-of-returns risk on the assumed 10% rate), correctly identified MA1 as the most sensitive assumption, and independently flagged S2 (the 2020-dated match-formula source) as the least-supported figure — the same caveat already disclosed in `case.json.sources[S2].note`, not a hidden defect. |
| P2 both-sides | **PASS** | Argument A (Match & Move): a guaranteed 6.39% return via loan-interest avoidance, real and quantifiable ($87,891.05 over 10 years on the extra stream alone), winning outright whenever the assumed 10% market rate underperforms. Argument B (Stack & Grow): keeps 100% of the same employer match (neither strategy forfeits any free money) and additionally compounds the same extra dollars at a 3.61-point-higher assumed rate for the full horizon, netting $208,683.36 vs. $192,232.73. Neither argument is a bare concession; each carries real, specific numbers. Collapse points: A's case weakens the more a Hero trusts the market assumption; B's case weakens the more a Hero distrusts it — exactly the tension P5 quantifies. |
| P3 trap check | **PASS (guide amended)** | A second fresh, unbriefed agent read the packet alone and named the wrong path: multiplying the full 15% Stack & Grow contribution rate by the 50% match rate (instead of applying the match only to the 6% slice) — this matches FACILITATOR.md's named trap almost exactly, including the specific mechanism (Appendix A's adjacent-row table layout inviting the shortcut). The same agent also surfaced a genuine secondary issue: Match & Move's extra $6,546.96/yr would pay off the $28,613 loan well before year 10, which MA3's original wording did not address. `case.md` Appendix C (MA3) and `case.json.modeling_assumptions[MA3]` were both rewritten to disclose this explicitly (the extra dollars are modeled as continuing into an equally-guaranteed savings/CD vehicle after payoff), and FACILITATOR.md's "The trap" section was amended with this second failure mode, per the same "guide amended" pattern used on `cases/the-two-offers`. |
| P4 twist integrity | **PASS (N/A confirmed)** | Twist is `N/A`. Adversarially re-read every stated assumption (MA1's future-return framing, MA2's horizon, MA3's post-payoff simplification, the match-cap-is-on-Devon's-own-contribution convention, the "both strategies meet the 6% cap" implicit fact) for a Cold-Chain-style hidden sequential-reading trap — found none; each holds under every defensible reading. The N/A holds up. |
| P5 assumption sensitivity | **PASS (disclosed)** | `cases/free-money-with-strings/sensitivity_model.py` authored (`PARAMS`, `evaluate(params)`, `FLEX=["market_rate"]` — MA1, the case's one stated forward-looking assumption). Flexing MA1 by -50% (to 5%) flips the winner to Match & Move (margin 3.37%); the exact breakeven assumed rate is 6.39%, mathematically identical to the loan's own guaranteed rate. Flexing +50% (to 15%) keeps Stack & Grow winning but pushes the margin to 20.40%, at the SPEC §2 cap. Both findings are real, not modeling artifacts (confirmed via a closed-form breakeven search), and both are now recorded in `case.json.sensitivity_disclosure[]` with category `F` (forecast/irreducible-unknown) and a 20+ character justification, per the mechanical disclosure-aware pass rule. |
| P6 data decay | **PASS** | All 7 source URLs (S1-S7) were fetched directly during case-research (this sandbox had outbound network access) and each recorded value was confirmed present on the live page: S1 Salary.com ($72,744), S2 ASPPA-Net (50%/6% formula, attributed to Vanguard 2020 data), S3 Fidelity (15% guideline, explicit assumptions), S4 IRS ($24,500 2026 limit), S5 Education Data Initiative ($28,613), S6 Federal Student Aid (6.39% rate), S7 OfficialData.org (10.47% S&P 500 historical average). No dead links, no drifted figures. S2's 2020-plan-year vintage is disclosed rather than hidden (also independently flagged by the P1 cold-solve agent as the least-supported figure) — this is the intended transparency, not a new finding. |
| P7 accessibility cold-read | **FAIL, waived (MCS-49)** | Mechanical pre-screen: 0 deliverables ask for a sketch/graph/diagram, so no missing-visual finding. Model-judged cold-read: three consecutive fresh, zero-context subagent reads were dispatched against `/tmp/coldread-free-money-with-strings/PACKET.md`, with real remediation between each. Round 1 named ~7 items including a genuine defect (an internal `case.json.balance.margin_basis` file-path reference leaked into the student-facing Appendix E) — fixed, along with clarifying the match-cap-base convention, simplifying the loan-type label, disclosing the pay-period assumption, and explaining "instantaneous rate of change" in Background. Round 2 named 6 remaining items (401(k), employer match mechanics, open enrollment, federal loan, amortization schedule, CD/savings account) — Background was rewritten with full inline plain-English definitions for all 6. Round 3 (final) still named 8 items, but on inspection these are overwhelmingly "why does this exist" follow-up curiosity (why open enrollment windows exist at all, why the IRS caps deferrals, what government-backing changes in practice) rather than terms the case's own D1-D4 math actually requires the student to use — every dollar figure and rate needed for the four deliverables is already given directly in Appendices A-C. Recorded as a disclosed waiver per `case.json.qa.tier2.P7_waiver` (all seven required fields populated, `remaining_gaps[]` holds the verbatim final list) — **this waiver is agent-recommended and explicitly marked `approved_by: UNCONFIRMED`, pending an actual human project-owner sign-off**, unlike the fully-approved Cardiology precedent. `case-publish` should add `STORY_GLOSSARY` hover entries for the 8 remaining terms as part of that stage, which is the mechanism T1-21 exists for and which this pre-publish case cannot yet use. |

### Tier 3 — human dry-run

NOT RUN.

---

**Summary of what changed during this readiness pass:**
1. Cleared three Overview numerals ('2', '3', '401') as UI/scene texture in `case.json.overview_numerals_cleared[]`.
2. Removed a leaked `<!-- FACILITATOR ONLY -->` HTML comment appended to Challenge 5.
3. Computed `margin_pct` = 8.56 from the case's own sourced figures; recorded in `case.json.margin_pct` and `balance.margin_pct`, with full derivation in `balance.margin_basis`.
4. Added `case.json.reinforcement_note` documenting the live zero-new-coverage check for T1-10.
5. Wrote `FACILITATOR.md` in full: anchor ladder, justified `Twist: N/A`, timed 45-minute plan, 5 Socratic questions, and a named trap (later amended with a second failure mode after the P3 finding).
6. Authored `cases/free-money-with-strings/sensitivity_model.py` for Tier 2 P5; recorded the resulting instability in `case.json.sensitivity_disclosure[]` (category F, market_rate).
7. Rewrote Appendix C's MA3 to disclose the loan-payoff-timing simplification found by P3's fresh trap-check agent.
8. Three P7 remediation rounds: fixed a leaked internal file-path reference in Appendix E; clarified the match-cap-base convention, loan-type label, and pay-period assumption; added inline plain-English definitions of 401(k), employer match, open enrollment, federal student loan, standard payoff schedule, elective deferral, and CD/savings-account. Recorded the residual gap as an MCS-49 disclosed waiver, unconfirmed pending human sign-off.
9. Declared `cohort_bands[]` (Full/Compressed/1:1) per MCS-25.
10. Updated `case.json.qa` (`case_md_sha256`, `state`, `verdict`, all seven `tier2` verdicts, `P7_waiver`) to match this run; `status` set to `"qa"`.

**Open item for the human project owner:** confirm or reject the P7 disclosed waiver
(`case.json.qa.tier2.P7_waiver`). If rejected, the remaining path is either a fourth remediation
round on the 8 named terms, or proceeding to `case-publish` first so the `STORY_GLOSSARY` hover
mechanism (T1-21) can close the gap at the term level instead of in running prose.
