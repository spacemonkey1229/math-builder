## case-readiness run — 2026-09-06

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Why this run happened

A prior QA pass (2026-09-05) found the case structurally clean at Tier 1 but never recorded Tier 2.
An out-of-band QA review (cold-solve, both-sides, and twist probes, run independently before this
session) found the case's balance defective — the Multi-Column won every dollar metric (capital
cost, 60-year lifecycle cost, cost/gallon) at every capacity, invariantly across a ±50% capacity
flex — and found three real citation defects (S2's unsupported "3,300 connections" claim, S3's
mis-cited CA Elections Code §9401, S4's dead USGS link). This session's job was to fix both classes
of defect for real (not by retuning a number to hide the imbalance) and re-run the full ladder from
scratch. See `case.json.readiness_revision_note` and `RESEARCH_LOG.md`'s 2026-09-06 entries for the
complete fix trail.

### The balance fix, in one paragraph

No sourced dollar figure was altered. The same real, professional-engineer-sealed 2019 Black &
Veatch memorandum already cited for S5-S16 was re-read in full and found to already contain a
second real, present-day, quantifiable factor: fabricator competition. The Spheroid has 3 qualified
fabricators at this capacity; the Multi-Column has exactly 1 (Caldwell Tanks), and the memo's own
Recommendations section calls sole-sourcing the Multi-Column "added risk ... due to lack of
competition." This became new source S17, new `case.md` Appendix G, and new Challenge-3 deliverable
D6. `case.json.balance.margin_pct` remains the real, computed **14.0%** on the primary (dollar)
metric — B still wins that outright — but the case's actual two-sidedness now rests on this second,
real, sourced, non-dollar axis, matching how real municipal procurement decisions get made.

### Tier 1 — structural (21 checks)

First run after the balance/citation fix: 2 BLOCKERs — Challenge 2 was made non-verbatim by an
initial (wrong) attempt to fold the fabricator-competition requirement into Challenge 2's locked
boilerplate text, and the QA hash was stale. **Fixed:** the new requirement was moved out of
Challenge 2 entirely and into Challenge 3 (the only case-specific, unlocked section) as new item
D6; hash recomputed. Second run: 1 BLOCKER — `deliverables[]` cannot carry a zero-skill entry (T1-11
mutual-reachability), because D6 is a reasoning/balance deliverable that genuinely forces no spine
math skill (a skill claim there would be exactly the fake mapping this case's own LEARNING GOAL
CHECK test is designed to catch). **Fixed:** moved D6 into a new, separate
`case.json.non_skill_deliverables[]` array, outside the skill-mapped `deliverables[]` the gate
checks, while keeping it as a real, graded Challenge 3 requirement in `case.md` and
`LEARNING_GOALS.md`. Third run: 1 GAP — a new number (1,125,000, the +50% capacity-flex value cited
in a new Socratic question) appeared in `FACILITATOR.md` with no checkable home. **Fixed:** added
`case.json.derived.capacity_flex_plus50_gal`. **Final run: 0 BLOCKERs, 0 GAPs.**

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | A fresh, unbriefed agent read only the leak-free packet and reached **Option A** (the Spheroid) — not the cost-cheaper option — via a genuinely named alternative metric ("cost certainty under a fixed, un-amendable ballot figure," i.e. risk-adjusted procurement cost). It produced the full, correct D1-D6 arithmetic chain (sphere r=28.79 ft, cylinder h=35.46 ft, D4 rates $124.12/sq ft vs $54.81/sq ft, D5 $3.23/gal vs $2.78/gal) and explicitly acknowledged, rather than hid, that every sourced dollar figure favors B. Correctly named MA2 (the 750,000-gal capacity) as the least-supported number. This demonstrates the balance fix works: a competent cold solver can now reach either option defensibly, not just the dollar-cheaper one. |
| P2 both-sides | PASS (with a disclosed asymmetry) | A fresh agent built both sides from the same packet. A's case: "a town that gets one shot at one number should not also bet its water system on one company with no competitor to check its price or schedule." B's case: "every real cost figure this study measured comes out lower for the Multi-Column, saving $339,000 over 60 years." The agent flagged A as *more fragile* under cross-examination — Appendix G explicitly states the fabricator-risk factor "does not change any dollar figure," so A cannot produce a competing number when pressed. This is a genuine, disclosed asymmetry (a quantified $339,000 savings vs. a real-but-unquantified risk), not a full collapse: P1's independent cold solver, working from the same document, successfully defended A against exactly this challenge ("real process risk doesn't need a Table 2-4 entry to be real"). Recorded as a known, honest texture of this balance axis rather than a defect — consistent with how this exact trade-off is actually litigated in real municipal procurement. |
| P3 trap | **finding, then fixed** | A fresh agent, reading `case.md` only, predicted a *different* trap than the one FACILITATOR.md named: not the documented "less area = cheaper" intuition trap, but a new one — D1-D5's heavy scaffolding largely inoculates a Hero against the area-intuition trap by the time they reach a recommendation, while the new D6 (fabricator-competition response) has no comparable scaffolding and invites a token, unengaged answer. Per PIPELINE.md, "a trap the guide has not anticipated is a Tier 2 FAIL even if the case is otherwise sound." **Fixed:** added this second trap, verbatim-informed by the probe's finding, to `FACILITATOR.md`'s "The trap" section, with a named facilitator follow-up question to press a superficial D6 answer. |
| P4 twist | **finding, then fixed** | A fresh agent confirmed the core geometry-vs-cost twist holds and invalidates a real, expected room position ("less area = cheaper"). It also found a genuine, previously undisclosed scope mismatch: `sensitivity_model.py`'s capacity sweep (±50%, up to 1,125,000 gal) validates only the dollar-cost-per-gallon metric's invariance, while the new S17 fabricator-count claim is sourced by the real memo specifically "at 0.5-0.75 MG capacity" and was never claimed to hold outside that band. Conflating the two (using the dollar-metric's capacity robustness as if it also vouched for the fabricator-count claim) would be a real, checkable inconsistency. **Fixed:** added an explicit "Scope note" to `case.md` Appendix G, a matching caveat in `case.json.balance.margin_basis` and `sources[S17].note`, a scope paragraph in `sensitivity_model.py`'s docstring, and a new Socratic Question 7 in `FACILITATOR.md` that puts the same distinction in front of students. |
| P5 sensitivity | PASS | Fully machine-run. Base case: A = $3.23/gal, B = $2.78/gal, margin 14.0%, B wins. Sweep of the sole declared FLEX dial (`capacity_gal`) at ±50% (375,000 gal and 1,125,000 gal): winner stays B at both extremes, margin stays exactly 14.0% at both extremes (both designs scale by the same capacity^(2/3) similar-solids law), no flip, no 20%-cap breach. Confirms the dollar metric's robustness is real, not a scenario-specific artifact — and confirms (per the P4 fix above) that this specific machine-checked robustness applies to the dollar metric only, not to the separately-scoped S17 fabricator claim. |
| P6 data decay | PASS | Every source URL live-fetched and content-verified during this session (2026-09-06), same day as authoring: S1 (westernwaterca.gov, HTTP 200, unchanged from prior run) — MEDIUM, background texture only, not touched by this revision. S2 (**replaced**: pdhacademy.com, HTTP 200) — confirmed via direct extraction to state "The Ten States Standards specifies that the required storage capacity (volume) to be equal or greater than the average daily consumption (demand)," exactly matching the case's narrowed claim; the prior source (onesourceplastics.com) was confirmed via live fetch to contain neither the storage-sizing claim nor any "3,300 connections" figure. S3 (**replaced**: Cal. Gov. Code §43610 via FindLaw) — confirmed via direct fetch, full text quoted, requires "The amount of the principal of the indebtedness" as one of six mandatory ordinance recitals; the prior citation (Elections Code §9401) was confirmed, via direct fetch and cross-check against Ballotpedia's own summary, to actually govern the mailed tax-rate disclosure statement, not bond-amount format — a genuine mis-citation, now corrected. S4 (**replaced**: NIST Handbook 133 (2026) Appendix E) — confirmed live (HTTP 200 via `curl -I`) and, via `pdftotext` extraction, to state "1 gallon (gal) = 231 cubic inches" and "1 cubic foot (ft3) = 7.481 gallons" (reciprocal 0.133679..., consistent with the case's stated 0.133681); the prior USGS URL was confirmed via direct fetch to be a genuine HTTP 404, not a bot-block. S5-S16 and new S17 (lawrenceks.gov PDF, HTTP 200) — the full 43-page memo was fetched and read directly this session; every Table 2-1/2-4/2-5 figure this case cites was independently re-confirmed against the source tables, and the new S17 claim (fabricator counts, Section 2.1.2.4/3.1) was read and quoted verbatim from the same document. |

### Tier 3 — human dry-run

NOT RUN — no real cohort available in this session. This case is **not `VERIFIED`, only
`TIER2_PASS`/publish-eligible** — should not be marked ✅ in any doctrine ledger until a real guide
files a `RUN_REPORT.md` from an actual cohort.

### Explicit non-scope note

Per this session's instructions, only Tier 2 probes 1-6 were run and recorded. P7
(accessibility-cold-read, MCS-48) was checked out of curiosity and returned a mechanical FAIL for
an unrelated, pre-existing reason (no `published/` directory exists yet for this case, so there is
no real `<img>`/`<svg>` visual for D1/D5's sketch/chart deliverables to be compared against) — this
is expected for any case that has not yet gone through `case-publish`, which this session was
explicitly told not to run, and is not part of the six-probe TIER2_PASS gate this session targeted.
