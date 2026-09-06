# QA Report — The Custom Die

## case-readiness run — 2026-09-06

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

This run remediated two defects found by an earlier Tier 2 pass (Twist integrity, Accessibility
cold-read), and one additional defect Probe 6 found live during this run (a stale material price).
None of the three were papered over — each was fixed at its source (case-write-level text for the
first two, case-research-level re-sourcing for the third) and re-verified with fresh, unbriefed
subagents rather than assumed fixed.

### Tier 1 — structural (21 checks)

0 BLOCKERs, 0 GAPs on the substantive checks. T1-16 (QA hash currency) is mechanically stale
immediately after any edit by construction — resolved below via `resync_artifacts.py` as the very
last step of this run, after every other check below was confirmed against the final `case.md`
(sha256 `7d2f1a92bcdd5a1257be5e3f51aafb3a3d0917a6af06c7d428d9344df00bc02f`).

| id | result | note |
|---|---|---|
| T1-01..T1-13 | PASS | structure, boilerplate, appendices, sourcing, balance, standards binding, learning-goal reachability, tier load, facilitator guide/anchors/sensitivity |
| T1-14 | PASS | FACILITATOR.md's own derived numbers (including the twist's rejected 6,154-unit reading and the rounded 3.944 twist metric) are now present in `case.json.derived[]`, so nothing drifts silently |
| T1-15 | PASS (no `published/` yet) | nothing to drift |
| T1-16 | resolved via `resync_artifacts.py` after this report was written | see below |
| T1-17..T1-21 | PASS / advisory-clean | cohort bands, no `published/` HTML to check yet (T1-18/19/20/21 have nothing to check pre-publish) |

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh solver reached B (not the case's own D5-graded winner, A) via a transparent, arithmetically-correct route: it explicitly computed D5's metric, correctly found A wins it (4.30 vs 4.59), named that as "the strongest argument against my choice," and chose B anyway on a stated, reasoned preference for weighting the recurring dimensional-weight cost over the one-time tooling cost. Names the metric, shows correct arithmetic, reaches a defensible (if contested) position — exactly the kind of Anchor-2-style "is the graded number the right number?" reasoning the case is designed to provoke, not a leaked-answer or nonsense route. |
| P2 both-sides solve | PASS | Independently re-derived every D1-D5 table from the packet alone; both sides have a real quantitative argument, but B's collapses first and at a specific, named question: B's intuitive sales pitch ("almost no wasted space") is contradicted by its own D5 score at the stated 12,000-unit volume, and its rebuttal (the fulfillment center's actual $/cubic-inch billing rate) has no sourced figure anywhere in Appendix D/F to fall back on. A's case remains fully load-bearing at the given numbers; its only real vulnerability is the volume assumption itself (MA3), which the case already discloses as the most load-bearing figure. |
| P3 trap check | PASS | Fresh solver named a secondary, real but narrower trap (reusing the Wedge's own 3.00/3.00 legs instead of the clearance-added 3.25/3.25 legs when computing Option B's hypotenuse) before reading the guide; after reading FACILITATOR.md, agreed the guide's actual named trap (conflating wasted interior volume with net material area) is the one that will actually catch a room, because it is seeded from the Launch onward and survives even flawless arithmetic. Guide's trap is real, named, and judged to be the dominant one. |
| P4 twist integrity | PASS | Adversarial fresh audit confirmed the twist fix closes the gap: Appendix E's MA3 now explicitly defines the re-tooling horizon as "whatever order volume the team can confidently count on," which resolves to the full 40,000-unit annual guarantee (not a 6,154-unit conversion into the original 8-week window) because the twist's stated rate (40,000/year) and stated term (one year) are a 1:1 match with no ambiguity left in the conversion. The rule lives in `case.md` itself (not only in `FACILITATOR.md`), is self-contained, and explicitly forecloses the rival reading by name. No remaining blocker found under any defensible reading tested. |
| P5 assumption sensitivity | PASS (disclosed) | Verdict is unstable under ±50% flex of `tooling_b_usd` and `order_volume_units` (both flip the winner), but both are recorded in `sensitivity_disclosure[]` with a category and justification (MCS-26 disclosure-aware pass state), consistent with the case's own stated finding that MA3 is the most load-bearing assumption. Re-run against the corrected $2.37/sheet price; no flex newly breaches the 20% margin cap. |
| P6 data decay | PASS (with a live re-sourcing) | S1's Uline URL is reachable and still carries a real, current per-pad price at the 50-pad tier, structurally consistent with the case's claim — but the actual number had moved from $2.24 (recorded 2026-09-05) to $2.37 (re-verified via live browser fetch 2026-09-06), a genuine same-day price change on the retailer's own site. This is exactly the "resolves but no longer carries the recorded figure" case P6 exists to catch. Re-sourced rather than left stale: `case.json.sources[]`, Appendix D/F, `sensitivity_model.py`, and every downstream `case.json.derived[]` figure were updated and re-verified against the corrected price. The verdict does not flip; margins moved slightly (base 7.65%→6.39%, twist 12.01%→12.54%, crossover 17,183→16,230 units). |
| P7 accessibility cold-read | PASS | Round 1 (pre-fix) found 14 unglossed terms (see prior diagnosis). Round 2 (after the first remediation pass — inline glosses for die/die shop/net/score/tooling/amortizing/re-tooling/clearance/conveyor belt/fulfillment center/dimensional-weight billing/single-wall corrugated/200 lb test/rule footage, plus an expanded Appendix G and the disambiguated per-pad pricing) found 2-3 residual borderline terms (liner/medium construction detail, the 5/32 in thickness rating, and rule-footage-to-dollar conversion mechanics). Round 3 (after glossing white/kraft, "margin," purchase order, contract term, tooling lead time, and production window, and tightening the liner/medium and thickness glosses) found **zero** unexplained real-world terms. Mechanical pre-screen: no deliverable asks for a sketch/diagram/graph this case doesn't already support with a worked example, so 0 missing-visual findings. |

### Tier 3 — human dry-run

NOT RUN.

## Fixes applied this run

1. **Twist integrity (P4).** Appendix E's MA3 (case.md) now explicitly defines the re-tooling
   horizon as "whatever order volume Marcus's team can actually count on with confidence at the
   moment of the decision," and states the rule for what happens when a purchase order changes
   that: the confidently-known volume becomes the full guaranteed volume over the contract's own
   term, not a smaller figure obtained by converting that guarantee back into the original 8-week
   window. `FACILITATOR.md`'s live Twist reveal now states this same logic aloud (the manager's
   added line about the die shop and the annual renewal), so the resolution is not something the
   facilitator quietly assumes — it is said to the room and it is written in the case text every
   student can read. `case.json.derived[]` now also records the rejected 8-week-converted reading
   (6,154 units) and confirms it does not flip the verdict (Option A wins by an even larger margin,
   22.18%, under that rejected reading) — proof the horizon rule is doing real work, not decorative
   text.
2. **Accessibility (P7), three remediation rounds.** Added inline parenthetical glosses throughout
   case.md for: die, die shop, net (load-bearing — D2/D3 depend on it), score/scored, tooling,
   amortizing, re-tooling, clearance, conveyor belt, fulfillment center, dimensional-weight billing,
   single-wall corrugated cardboard (medium/liner), "200 lb test," rule footage, white/kraft finish,
   purchase order, contract term, tooling lead time, and production window; added a short note
   defining what "margin" means in Appendix E's Sensitivity column; expanded Appendix G (Learn More)
   with four new verified links (steel rule die, amortization, order fulfillment, corrugated box
   design — all confirmed HTTP 200 before adding); and disambiguated the "$2.24 per pad (50-pad
   bundle price)" phrasing into an unambiguous "$X per individual pad, sold in bundles of N" pattern
   (Appendix D, Appendix F, `case.json.sources[]`).
3. **Live price drift (P6), found during this run's own re-verification, not part of the original
   assignment but fixed under the same pass per house doctrine on stale figures.** A real browser
   fetch of Source S1's Uline product page found the 50-pad-tier price had moved from $2.24 (the
   value recorded 2026-09-05) to $2.37 (2026-09-06) — a genuine live-retailer price change, not a
   research error. Re-sourced and re-derived every dependent figure: `case.json.sources[]`,
   Appendix D/F in `case.md`, `sensitivity_model.py`'s `PARAMS`, and the full `case.json.derived[]`
   block. The verdict is unchanged (A wins the base case, B wins the twist); only the margins and
   the crossover volume moved slightly. See `RESEARCH_LOG.md`'s "Addendum" section.

## margin_pct

**6.39%** (was 7.65% before the S1 price re-verification; winner unchanged, Option A). Twist
margin: 12.54% (was 12.01%), winner unchanged, Option B.

## Next step

`case.json.qa.state` = `TIER2_PASS`. This case may proceed to `case-publish` when a human is ready
to run it (not run as part of this pass, per instruction). Recommend scheduling the Tier 3 dry-run
after publish.
