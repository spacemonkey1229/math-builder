# QA Report — Investment Portfolio

Legacy conversion from `source/Y3/Additional/Stock Market/` (case doc titled "Investment
Portfolio"; the pipeline board's folder-derived title is "Stock Market" — see
`case.json.legacy_conversion_note`). Already standards-tagged pre-conversion (74 skills under
"Investment Portfolio" in `standards_spine.json`), missing only the structural conversion.

## case-readiness run — 2026-08-22

### Tier 1 — structural (19 checks)
19 checks: 14 PASS, 5 GAP, 0 FAIL (re-run after the UAT pass below closed the T1-16 first-run gap
and, as a side effect of the twist-leak fix, shrank T1-18's unmatched-number count from 35 to 1).

- T1-10 — expected legacy-conversion carve-out: this title is already credited in
  `standards_spine.json`'s `covered_by[]` from the pre-pipeline corpus scan, so `new_coverage[]`
  is legitimately empty.
- T1-14 — 2 guide-only derived figures (43, 2012 — the Bitcoin-vs-CenturyLink launch-hook numbers
  in `FACILITATOR.md`'s Monday-launch material) not mirrored into `case.json`. Benign; flagged for
  a future `case.json.derived` backfill, not blocking.
- T1-15 — continuity GAPs on `published/*.xlsx` and the Facilitator Guide docx: raw allocation
  fractions (0.9, 0.1, 0.4, 0.075...) and per-holding-period return rows in the packet files don't
  string-match `case.md`'s percent-formatted prose (e.g. "90%" vs `0.9`). Same accepted
  false-positive class already carried by other published cases (see `cases/psychologist`'s
  T1-14 note) — the data itself was checked and matches (see P1 below, and the UAT section below).
- T1-18 — 1 number (0.5, the risk-free-rate slider's default midpoint) in the Interactive HTML's
  markup doesn't have a literal case.md match; inspected, not a graded answer.

**VERDICT: TIER1_PASS (0 blockers, 5 gaps)**

### Tier 2 — simulated play (6 probes)

**One real BLOCKER found and fixed during this run**: the Twist (Buffett's 90/10 allocation
originating as trust instructions for a lump-sum inheritance, contrasted with Benjamin's 30-year
recurring contributions) was pre-disclosed to students. `case.md`'s Appendix A and Appendix E
sources table, and the matching sections of the published Interactive HTML/docx/xlsx packet,
stated the allocation's origin as "Berkshire Hathaway's 2013 shareholder letter, instructions for
a trust set up for his wife's benefit" — an 8+ word near-verbatim overlap with `FACILITATOR.md`'s
Twist reveal text. A diligent student reading the appendix before discussion would already have
the twist's core fact, defeating the facilitator's timed reveal. **Fixed**: reworded the citation
in `case.md`, the Interactive HTML (both the Appendix-A side-note and the Sources footer), the
Case Study docx, and the Data xlsx (`Allocations!A6`, `Sources!B4/D4/E4`) to cite the allocation
neutrally ("a real, publicly documented allocation attributed to Warren Buffett [S1]") without the
trust/wife/inheritance/lump-sum/2013-letter framing. That framing now appears exactly once,
inside the Interactive HTML's gated `<section id="twist">` block (behind a "reveal" button,
facilitator-controlled) and in `FACILITATOR.md`'s own Twist section — the correct locations.
Re-verified clean by an independent fresh-context check after the fix (see P4 below).

| Probe | Verdict | Basis |
|---|---|---|
| P1 cold-solve | **PASS** | Fresh subagent, packet-only. Chose Buffett 90/10 on the 30-year projected terminal value (~$8.24M vs ~$5.30M for All-Weather), correctly noted the 20-year Sharpe ratio is a near-exact tie (0.66 vs 0.66) so risk-adjusted return doesn't discriminate, correctly named the -45.52% vs -20.58% max-drawdown gap and Benjamin's stated uncertainty about his own risk tolerance as the strongest counter-argument, and correctly flagged MA2 (trailing-30-year-return-as-forward-assumption) as the most sensitivity-critical input and MA1 (the un-cited 1.5% risk-free rate) as the least-supported number. Arithmetic independently reproduced and matches `case.json`. |
| P2 both-sides-solve | **PASS** | Fresh subagent built genuine, numeric cases for both options (A: wins every historical holding period, 1yr through 30yr; B: roughly half the volatility and less-than-half the drawdown, plus a real tax-drag argument on the taxable-account point). Verdict: A collapses first, under the drawdown/behavioral-risk question ("your own case says you don't know how you'd react to a 40% drop — how do you defend a -45.52% worst case?"), because A's defender has no textual counter to Benjamin's own stated uncertainty. Neither side is a rounding-error concession — both are real, substantiated arguments, matching the case's design intent (SPEC §2 balance test). |
| P3 trap-check | **PASS** | Fresh subagent's cold-read prediction — a room stops at the D4 30-year dollar total, declares Buffett the winner on "more money," and never seriously weighs the risk side — is essentially word-for-word `FACILITATOR.md`'s named trap, which additionally sharpens it: the case's primary graded metric (D6, the 20-year Sharpe ratio) is a near-exact tie, directly undercutting the ~55%-more-money story from D4. No divergence between the probe's blind read and the guide's anticipated trap. |
| P4 twist-integrity | **PASS** (after a real fix — see above) | Q1 (invalidates a real position): yes — undercuts a pure "good enough for Buffett, that settles it" appeal-to-authority stance without touching Appendix C/D's numbers. Q2 (survives the case's own stated assumptions): yes — the twist is an authority/context challenge, not a computational one; it doesn't depend on any unstated convention in MA1–MA4, unlike Cold Chain's original sequential-reading failure. Independently re-verified clean (no remaining leak in case.md, Interactive HTML outside the gated twist section, the Case Study docx, or the Data xlsx) after the citation rewrite. |
| P5 assumption-sensitivity | **PASS (disclosed)** | Mechanical script run (`tier2_probes.py --probe 5`) against `sensitivity_model.py`. Sweeping the one declared `FLEX[]` dial (risk-free rate, MA1) ±50%: base Sharpe ratio is a 0.2%-margin near-tie (A 0.66 / B 0.66); at -50% flex the winner flips to B (margin 5.5%); at +50% flex A widens to a 7.3% margin. SPEC §2 doesn't forbid an unstable margin, but it must be disclosed — it is, in `case.json.sensitivity_disclosure[]`, `balance_test`, and `FACILITATOR.md`'s sensitivity note (which explicitly flags MA1 as uncited and decisive to the Sharpe-ratio tie-break). No 20%-cap breach either direction. |
| P6 data-decay | **PASS** | Delegated fetch of all 4 cited URLs (S1 Yahoo Finance, S2/S2b LazyPortfolioETF Buffett + Dalio pages, S4 usinflationcalculator.com). All 4 reachable, no dead or moved links. S1/S2/S2b figures verbatim-verified matches on the live pages. S4's "~2.6% average 2000-2026" inflation figure is a derived computation from the page's year-by-year BLS data, not a number the page states directly — noted in `RESEARCH_LOG.md` as a derived figure, not re-cited as if quoted. |

**MECHANICAL RESULT:** 0 probes failed. All 6 probes carry a recorded verdict. One real BLOCKER
(P4's twist pre-disclosure) found and fixed during this run, independently re-verified against the
corrected packet files (case.md, Interactive HTML, Case Study docx, Data xlsx) by a second,
fresh-context adjudication pass — confirmed clean.

**Tier 1 clean (0 blockers, 5 gaps) AND all six Tier 2 probes PASS → state promoted to
`TIER2_PASS`.** `case.json.qa` updated: `state: "TIER2_PASS"`, `verdict: "PASS"`,
`run_on: "2026-08-22"`, `blockers_open: 0`, `gaps_open: 5`,
`case_md_sha256: "f9c9b949dc74144084d34095a85a41245142346b15923e58e4c626fa33b15de2"` (re-hashed
after the twist-leak fix above). Per `skills/case-readiness/SKILL.md`'s ladder, `case-publish` may
now run — Tier 3 (a filed human `RUN_REPORT`) remains required before `VERIFIED`. **This run does
not run `case-publish`**; `case.json.status` remains `"qa"` pending an explicit publish decision.

## Browser-based UAT — 2026-08-22

Beyond the readiness gate, both `investment-portfolio` and `caribbean-internet-cafe`'s published
Interactive HTML packets were loaded in a real browser (served over local HTTP, not `file://`, so
JS actually executes) and functionally exercised — not just read as static text.

**Investment Portfolio:**
- No console errors on load or during interaction.
- All 4 Working Notebook Check steps (D1 allocation split, D2 mean/range of 5-year returns, D3
  30-year projection with/without the Year-3 shock, D4/D6 Sharpe ratio) graded a correct answer
  ✓ and a deliberately wrong answer "try again" — grading is live, not decorative. Computed
  values matched the P1 cold-solve subagent's independent arithmetic exactly (Sharpe 0.6611 vs
  0.6599; 30-yr projections ≈$8.24M vs ≈$5.30M).
- The dilemma A/B pick widget updates state and persists correctly.
- The Twist reveal button works and un-hides its narrative.
- **Bug found and fixed during this pass:** `published/Investment Portfolio - Data.xlsx`,
  `Allocations!A6`, still carried the leaked "Berkshire Hathaway 2013 Shareholder Letter"
  citation text after the case.md/Interactive-HTML/docx leak fix above — the xlsx packet file had
  been missed. Reworded to a neutral citation, matching the other three files. Re-verified clean
  by a second fresh-context agent across all four packet files (case.md, Interactive HTML, Case
  Study docx, Data xlsx).
- All 12 unique external links (4 sourced citations + 8 glossary "how to" links) return HTTP 200.
- `published/MANIFEST.json` was stale after these edits (wrong byte counts, wrong `case_md_sha256`,
  and the Facilitator Guide docx was mislabeled `"audience":"student"` instead of `"facilitator"`
  — a real leak-risk mislabel, since that file contains the balance argument, the trap, and the
  full twist). All four fixed.

**Caribbean Internet Cafe** (already `TIER2_PASS`/published from a prior session — this pass was
verification, not a fix pass): no console errors; all 4 Working Notebook Check steps (Primary Sunk
Investment, monthly interest cost A/B, fixed costs + contribution margin, break-even visits A/B)
graded correctly against the case's own `PARAMS`-driven helper functions, both for correct and
deliberately-wrong input; the Twist reveal works; all 16 unique external links return HTTP 200.
**No bugs found** — this case's interactive artifact is clean as shipped.
