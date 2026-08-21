# QA Report — Insurance

## Preflight lint — 2026-08-20

1 advisory finding: the standard `<!-- FACILITATOR ONLY: ... -->` boilerplate comment line at the
end of case.md contains the word "facilitator." This is the same fixed boilerplate line used
across the corpus (e.g. `cases/family-trip/case.md`'s identical closing line) and is not a real
leak — it names where facilitator content lives, with no facilitator content following it in
case.md itself. Reviewed and accepted, not fixed (there is nothing to fix; the line is by design).

## case-readiness run — 2026-08-20

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (19 checks)

| id | result | note |
|---|---|---|
| T1-01 | PASS | |
| T1-02 | PASS | Overview contains no load-bearing numerals |
| T1-03 | PASS | Binary, opens "You are Greg and Tiffany Sanderson." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | |
| T1-06 | PASS | all 9 appendices referenced from Background/Challenges after fix |
| T1-07 | PASS | all 32 final-appendix lines verified verbatim against the spine |
| T1-08 | GAP | LOW-confidence source present (S1, the friend's HDHP terms) — see confirmation below |
| T1-09 | PASS | balance test: both arguments written, margin 6.7% ≤ 20% |
| T1-10 | GAP | new_coverage[] empty — legacy-conversion carve-out, project-owner-approved doctrine, not a per-case waiver |
| T1-11 | PASS | learning-goal mutual reachability, 0 unmapped / 0 unreachable |
| T1-12 | PASS | T3 numeric load (percent/coinsurance, probability, mean, algebraic expression) matches declared tier |
| T1-13 | PASS | facilitator guide: 5 Socratic questions, trap named, full anchor ladder, twist, timed 45-min plan |
| T1-14 | PASS | FACILITATOR.md numbers reconciled against case.json.derived |
| T1-15 | PASS | no published/ yet, nothing to drift |
| T1-16 | PASS | case_md_sha256 recorded and current |
| T1-17 | PASS | 3 cohort bands declared |
| T1-18 | PASS | no published/ yet |
| T1-19 | PASS | no published/ yet |

BLOCKER: none. GAP (2): T1-08, T1-10 (both addressed below). POLISH (4): all informational
(no `published/` directory yet; separator-run label parsing note).

**T1-08 confirmation (required by the GAP text):** S1 (the friend's HDHP plan terms — $125/mo
premium, $6,300 deductible, $6,500/$12,800 individual/family OOP max) is LOW confidence and DOES
underpin Option A's entire premise — it is not decorative. This is disclosed prominently, not
buried: it is flagged LOW in `sources[]`, restated as Modeling Assumption MA2 in both case.md
Appendix G and `case.json.modeling_assumptions[]`, and corroborated for real-world legal
plausibility against actual 2021 IRS HDHP thresholds (S8, HIGH confidence) in case.md Appendix F.
Per `skills/case-research/SKILL.md`'s own worked example, a real, unverifiable-origin figure that
cannot be independently re-sourced is handled exactly this way — declared, sourced as far as
possible, and checked for plausibility — not silently dropped or invented. Confirmed: this LOW
source does not carry the case's *graded* dilemma-flipping quantity (the primary metric, each
plan's OOP max, is B's real sourced figure vs. A's disclosed-LOW figure — already accounted for
in the balance test and margin), and its role as a real, disclosed constraint on Option A (not an
appendix-noise distractor) is exactly what SPEC intends for this class of legacy figure.

**T1-10 confirmation:** legacy-conversion carve-out applies per skills/case-readiness/SKILL.md
(2026-08-13 doctrine amendment) — "Health Insurance" is already credited in
`standards_spine.json`'s `covered_by[]` for every claimed skill; see `case.json.new_coverage_note`
and `LEARNING_GOALS.md`.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS (after one case.md fix) | Fresh subagent, packet only. Chose Option A, named "total 2021 cost, premium + expected out-of-pocket, checked in both an ordinary and a bad year" as its metric, showed full correct arithmetic, named the out-of-pocket-maximum/network-risk framing as the strongest counter-argument (independently rediscovering the case's actual graded angle), correctly flagged MA2 (the friend's secondhand premium) as its most sensitivity-loaded assumption, and named a real appendix item (Appendix F's IRS legal check) it chose to ignore as non-dollar-moving. Reached a defensible position via the right route. **Real finding, fixed before recording PASS:** the solver computed a $6,957.04/$10,776.00 ordinary-year total, not the case's own canonical $7,811.41/$10,896.00 (case.json.derived) — tracing the gap showed the solver reasonably read case.md Appendix D's original wording as bundling Tiffany and Greg's 3 routine PCP visits each into the D3 "unplanned incident" data only, since both were presented in the same sentence about their "2020 record... used in D3." That is a real, defensible reading of an ambiguous sentence, not a solver error — the case never explicitly said those routine PCP visits also recur in the D2 baseline. Fixed by splitting Appendix D's sentence so the 6 routine PCP visits are explicitly framed as recurring baseline care (same as Neri's and Greg's other appointments), and only the single 2020 urgent-care incident feeds the unplanned-incident count. case.md's sha256 updated accordingly (2022468e6098130b7cd5c6d92d8e29362f78c797dab9046e804e438fb6fefb08); case.json.derived/sensitivity_model.py were already using the intended (now-unambiguous) reading, so no other file needed to change. |
| P2 both-sides | PASS | Worked directly (mechanical pre-screen: no concession-only language flagged). Strongest sentence for A: real, guaranteed $6,828/yr premium savings that stays ahead by 39.5%-45.5% under every tested scenario. Strongest sentence for B: a real, sourced $800-lower worst-case cap plus fully predictable copays and confirmed network access, vs. A's disclosed-LOW plan terms and unconfirmed network. Neither side collapses to a bare concession — each has one deliverable-level question it structurally loses (A loses D2's raw-cost comparison at the 6.7%-margin metric; B loses D1's premium and average-cost comparison by a wide, real margin) but a real, quantified strength elsewhere. |
| P3 trap | PASS | Fresh subagent, packet only, predicted the trap BEFORE reading FACILITATOR.md: "premium tunnel vision — mistaking cheaper-on-average for cheaper-period, without separately checking worst-case exposure." This matches FACILITATOR.md's stated trap exactly. The subagent also independently flagged that the required deliverable D2 (report the OOP max "labeled separately") gives a careful student a structural escape hatch from the trap, and noted the Twist (pregnancy) functions as a well-constructed SECOND-order trap on top of the first, for students who correctly avoid the first one — a genuine strength, not anticipated by the author's own trap-naming but consistent with it. |
| P4 twist | PASS | Worked directly, cross-checked via sensitivity_model.py evaluate()/evaluate_twist() (mechanical pre-screen: READY, no auto-FAIL). (1) The twist invalidates the position that the out-of-pocket-maximum comparison is purely theoretical/irrelevant — a single real, plausible, already-discussed event (pregnancy) pushes realized spending to 69% of Option A's cap and 56% of Option B's cap. (2) Re-derived under both a sequential reading (pregnancy layered onto the rest of 2021's real care) and a standalone reading (pregnancy alone) of every stated Modeling Assumption, especially MA1 (the HDHP coinsurance rate the twist recompute depends on) — both readings hold, no unstated convention required. The twist does not flip the RAW-dollar landslide (A remains cheaper even with the pregnancy added, $10,351.41 vs $15,066.00) and does not need to — it targets the "the cap is theoretical" position, which it does invalidate. |
| P5 sensitivity | PASS | Fully machine (sensitivity_model.py). All 5 declared FLEX dials (hdhp_coinsurance_rate, pcp/specialist/vcug/urgent-care reference costs) swept ±50%: 0 flips, 0 cap breaches. The graded primary metric (each plan's own stated out-of-pocket maximum) is, by design, read directly from sourced plan data and does not depend on any of this case's Modeling Assumptions — it is unconditionally stable under every tested flex, a genuine, notable property of this case's metric choice (see case.json.sensitivity_note). |
| P6 data decay | PASS | S1-S4 are local bundled project files (Guide Notes docx, Plan Comparison PDF, Navigator Gold 2000 SBC PDF, Kaiser fee-list PDF) — all four confirmed readable and text-extracted successfully during research; not subject to URL decay. S5 (MDsave) re-fetched live 2026-08-20: reachable, still carries the $304-$845 range plus two additional real summary figures not originally captured (now added to sources[].S5.note) — case.md's own $500 midpoint proxy is unaffected and remains disclosed as a proxy, not MDsave's own headline average. S6 (GoodRx) 403'd to automated re-fetch (bot-blocked — the same failure mode seen on other cases' S1/S6/S3 in this project, not confirmed dead; the figure was independently corroborated across multiple aggregator sources during the original research pass). S7 (AHRQ HCUP Statistical Brief #311) and S8 (IRS Rev. Proc. 2020-32) both fetched directly and successfully during research, confirmed to carry their cited figures exactly. No dead links found; no figure found to have drifted from its cited value. |

**6/6 probes recorded, 0 FAIL.**

### Tier 3 — human dry-run

NOT RUN. `PUBLISHED` may be reached without this; `VERIFIED` requires a filed
`cases/insurance/runs/RUN_<date>_<guide>.md` from a real cohort before this case may be marked ✅
in the doctrine ledger.

---

**VERDICT: TIER2_PASS.** case-readiness stops here per instructions — case-publish was not run.
