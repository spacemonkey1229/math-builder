## case-readiness run — 2026-09-05
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Preflight lint
Not run as a separate step in this session; its two checks (Modeling-Assumptions leak, FLEX[]
scoping against sources[]) were applied by hand while authoring: the Appendix E "Sensitivity"
column states only "The answer is sensitive to this value" for every load-bearing assumption,
never the margin, winner, or threshold; `sensitivity_model.py`'s `FLEX[]` contains only the four
genuine stated assumptions (MA2-MA5) and excludes MA1 (constructed site geometry, the scenario
itself) and both sourced dollar inputs (S1 lumber price, S2 wage), consistent with the "Only
FLEX[] is swept" rule.

### Tier 1 — structural (21 checks)

First pass found one BLOCKER (T1-13, `FACILITATOR.md` missing) and two continuity GAPs (T1-14: five
numbers in a draft of `FACILITATOR.md` — 6.494, 120.0, 180.0, 620.0, 40000.0 — had no home in
`case.json`/`case.md`). Fixed: wrote `FACILITATOR.md` in full, and added
`octagon_hip_rise_ft`, `hexagon_known_angle_sum_deg`, `trap_incorrect_shortcut_deg`,
`angle_sum_formula_constant_deg`, and `matching_grant_usd` to `case.json.derived`.

Second pass, clean:

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview 267 words, zero digit numerals |
| T1-03 | GAP | Dilemma binary, opens "You are Tomas Reyes." Fuzzy Option-B-named-in-Background check misfires because "Site" (4 letters) and "Six" (3 letters) both fall under the checker's `len>4` word filter — read Background by hand: it names "The Site Six" explicitly, twice. Cleared deliberately, not a real defect. |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | numeral form `N.)` consistent |
| T1-06 | PASS | appendices A–H, lettered, ordered, no orphans (added an explicit Appendix C cross-reference to Background during authoring, before this run) |
| T1-07 | PASS | all 15 final-appendix lines verbatim spine labels (9 vocabulary + 4 how-to — corrected count after removing the ungrounded generic "Polygon" term and adding "Pythagorean Theorem") |
| T1-08 | PASS | every number cited (S1–S4) or a declared Modeling Assumption (MA1–MA5) |
| T1-09 | PASS | both arguments written, margin 11.35% ≤ 20% |
| T1-10 | GAP | `new_coverage[]` is honestly empty — a reinforcement/thickening pass on the Quadrilaterals And Polygons group (16/22 skills thin before this case), not a padded claim. `case.json.reinforcement_note` records that the only zero-coverage Geometry skill anywhere (`geometry-how-to-find-the-volume-of-a-sphere`) was checked and correctly ruled out. Downgraded from BLOCKER per the 2026-08-17 T1-10 reinforcement carve-out. |
| T1-11 | PASS | mutual reachability — 0 unmapped deliverables, 0 unreachable skills |
| T1-12 | PASS | T2 tier matches numeric load (interior-angle-sum theorem + Pythagorean rafter geometry + quadrilateral classification + weighted dollar comparison, two competing variables) |
| T1-13 | PASS | facilitator guide, anchor ladder, twist, timed plan, sensitivity note all present |
| T1-14 | PASS | continuity — FACILITATOR.md numbers all traced to case.json.derived |
| T1-15 | PASS | no published/ yet, nothing stale |
| T1-16 | PASS | hash current (`a0955fc9ff2f08ddfb20424f44d6bd07e79f35dd3f3a6f3920bbff3e7059ee7c`) |
| T1-17 | PASS | cohort_bands[] declared, 3 bands |
| T1-18/19/20/21 | PASS | no published/ yet (nothing to check — expected pre-publish) |

BLOCKER (0). GAP (2): T1-03 (fuzzy-match false positive, read and cleared), T1-10 (reinforcement
carve-out, honestly earned — see above). POLISH (6): all "no published/ yet" (expected pre-publish)
plus one informational T1-07 label-parsing note.

**VERDICT: TIER1_PASS**

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | A fresh, unbriefed subagent given only the leak-checked packet chose Option B, correctly named the graded metric (covered sq ft per dollar of frame+site-prep cost), independently reproduced the D2 angle arithmetic (interior angle sum 720° for the hexagon, 108+132+121+143+116=620°, sixth angle = 100°) and the D5 cost arithmetic (totals $665.74/$639.02, ratios 0.7168/0.7981 sq ft/$), correctly flagged the MA3 custom-cut premium as the least-supported figure, and correctly named MA4/MA5 (site-prep rates) as the assumption its answer was most sensitive to — independently converging on exactly the finding Tier 2 Probe 5 later confirmed mechanically. Reached the intended answer for the intended reason. |
| P2 both-sides | PASS | Mechanical pre-screen passed cleanly (no concession-pattern or low-numeric-density false trigger). Adjudicated: Option A's real floor is the twist-revealed shop-time win (1.5833 hr vs. 3.45 hr — batch-cutting eight identical hips in about half The Site Six's total setup-and-cut time), a genuine advantage when a single stamped-drawing deadline is the whole constraint, though its underlying setup-time estimates are facilitator-only and not independently sourced. Option B's real floor is the case's own graded-metric win (11.35%, sq ft/$), built entirely from Appendix D's official figures, fully priced with the real fabrication premium already included. Neither side collapses to zero — same asymmetric-win pattern as Roofline Call (graded metric vs. twist metric), not a paper margin. |
| P3 trap | PASS | A fresh subagent given only the packet, with no knowledge of the guide, independently predicted the exact trap: dividing the hexagon's 720° angle sum by 6 to get "120° each" (the regular-polygon shortcut, wrongly applied to an irregular polygon) instead of correctly subtracting the five known angles to get 100° — and named exactly why it's tempting (D2 teaches the regular shortcut immediately before the irregular case, inviting pattern-matching). `FACILITATOR.md`'s "The trap" section names this same path, independently and in matching detail. |
| P4 twist | PASS | (1) The twist (the truss shop's single batch-cut slot) invalidates the position "pick B because it wins the graded metric" — a real position Anchor 1's vote would produce, especially given the committee's own rendering favors B. (2) Re-derived under every stated Appendix E assumption exactly as written: the twist's setup-time dials (pattern/template) are entirely new information the twist introduces, not a re-reading of any stated assumption, so there is no ambiguous-convention risk of the Cold Chain kind; the two Appendix E assumptions the twist DOES reuse (MA2/MA3 cut times) are single unambiguous values with no sequential/simultaneous reading question. Cross-checked against `sensitivity_model.py`'s `evaluate_twist()`: A=1.5833 hr, B=3.45 hr, winner A, matching `FACILITATOR.md` exactly. The twist fully reverses the winner on a genuinely different metric (shop hours, not dollars), verified mechanically. |
| P5 sensitivity | PASS (disclosed) | `sensitivity_model.py` flexes all four declared assumptions (`simple_cut_min`, `custom_premium`, `site_prep_rate_a`, `site_prep_rate_b`) ±50%. MA2/MA3 (cut-time assumptions) move the margin only slightly (10.2%-12.5%) and never flip the winner or breach the 20% cap. MA4/MA5 (site-prep rates) genuinely DO flip the winner and breach the cap at multiple flex points (margins from 23.9% to 79.3%). This is a real, disclosed instability — not a scoping bug — recorded in `case.json.sensitivity_disclosure[]` (Category X: no real site-prep quote can exist for this constructed, non-real lot; both rates are good-faith point estimates anchored inside a sourced land-grading range). Machine result: `PASS (disclosed)` per the 2026-08-13 disclosure-aware pass state. |
| P6 data decay | PASS | All four sources freshly fetched THE SAME DAY as this run (2026-09-05), zero age. S1 (NAHB Framing Lumber Prices) — reachable, value confirmed verbatim ($521.35/1,000 board feet, week of August 28, 2026). S2 (BLS OOH Carpenters) — reachable, value confirmed verbatim ($60,580/yr, $29.12/hr, May 2025). S3 (EB3 Construction) — reachable, "30 to 60 percent" premium claim confirmed verbatim. S4 (Lawn Love land grading) — reachable; **a real transcription error was caught and fixed during this run**: an initial pass had recorded the page's figure as "$0.80 to $2.00/sq ft" from a web-search summary; a direct re-fetch of the page itself found the actual headline range is "$0.08 to $2.00/sq ft," broken into fine/finish grading ($0.40-$1.00/sq ft) and rough grading ($1.00-$2.00/sq ft) sub-ranges. Corrected in `case.json`, `case.md` (Appendix E/F), and `RESEARCH_LOG.md` before this Tier 2 run — both of the case's existing point estimates (MA4 $1.10, MA5 $0.95) already fell inside their correct, more specific sub-ranges once fixed, so no case numbers needed to change, only the citation. No URL dead, no figure still drifted after correction, all sources same-day fresh. |

**VERDICT: TIER2_PASS**

### Tier 3 — human dry-run
NOT RUN. `PUBLISHED` is reachable without it; `VERIFIED` is not. No `runs/` directory yet.

### Corrections made during this run
- Wrote `FACILITATOR.md` (was missing — Tier 1 BLOCKER, now resolved).
- Added five derived figures to `case.json.derived` to clear a Tier 1 T1-14 continuity GAP.
- Added `case.json.sensitivity_disclosure[]` (two Category-X entries, site_prep_rate_a/b) to move
  Tier 2 Probe 5 from mechanical FAIL to `PASS (disclosed)`, and extended `case.json.sensitivity_note`
  and `FACILITATOR.md`'s Anchor 4 with the same disclosure, facilitator-side only (never in
  `case.md`'s student-facing Modeling Assumptions column, which states only "the answer is
  sensitive to this value").
- **Caught and corrected a real sourcing error on S4** (land-grading cost range) between initial
  drafting and this Tier 2 run — see the P6 finding above and `RESEARCH_LOG.md`'s P04 correction
  note. This is exactly the kind of drift Tier 2 Probe 6 exists to catch, caught here before
  publish rather than after.
- Removed an ungrounded "Polygon" vocabulary line from Appendix H (not independently forced by any
  deliverable once the more specific octagon/hexagon/regular/irregular terms are already claimed)
  and added the genuinely-forced "Pythagorean Theorem" line, keeping Appendix H's final-appendix
  list exactly matched to `case.json.standards[]`.

**Next step:** human review, then `case-publish` on `the-bandstand-angle` (not run by this agent
per instruction — stopping here at `TIER2_PASS` for review).
