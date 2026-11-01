# QA Report — The Busiest Century

## case-readiness run — 2026-10-28
**State:** DRAFT → TIER1_PASS   **Verdict:** TIER2_INCOMPLETE (P7 FAIL; TIER2_PASS not recorded)   sha256(case.md) = ede2e7ae38228b464ca07f49081dfb7d4817d2ecebdd7c5b96d58dcfb230d390

### Tier 1 — structural (24 checks run)
All PASS except two GAPs: T1-10 (new_coverage empty; reinforcement carve-out, spine has no n=0 skill) and T1-16 (no hash on first run; now recorded). 0 BLOCKERs. Published-artifact checks T1-15, T1-18..T1-24 have nothing to check (case-publish not run, by instruction). Preflight lint clean.

### Tier 2 — simulated play (7 probes)
| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh solver chose B (Sites) with correct arithmetic: D1 10.1%/15.9%, D2 five-number summary 1/1/2/4/137, fences -3.5/8.5, 103 outliers, mean 4.19; D3 five cuts; D4 tie at s=0.389. Named the metric; strongest counter was the thin 5.8% Sites lead. Found ambiguities: no BP-to-CE wording rule for the wall sentence; no guidance for scaling a 1-to-137 axis; quartiles from a frequency table not shown; Appendix D "top three" lists four on a tie. |
| P2 both-sides | PASS | Both sides defensible with packet numbers; neither collapses; A buckles first at "half of all dates come from 103 outlier sites; is your century just where the most-dug sites are?"; mild tilt to B for a public wall. Neither dominated. |
| P3 trap | PASS | Solver predicted "bigger bar is the truth"; guide's trap 2 matches; guide also names dates-as-people. Missed by guide: quartiles taken from the frequency-table rows instead of the 863 sites; "readings always disagree"; D4 normaliser; wrong D3 denominator. GAP: add one line. |
| P4 twist | PASS | Both parts recomputed from the extract and reproduce. Part 1 (heaviest site out) flips the aligned Dates winner to 1200-1299; part 2 (sites with 10+ dates) puts both readings at 700-799 and flips the base blended winner. Caveats: part 1 holds only with centuries from 0 (guide says so); the guide's 9.73%/23.76% use a within-subset normaliser (case's Appendix B maxima give 10.1% and 31.1%); shifted-century twist figures are not reproducible from the packet's extract. Nothing depends on an unstated convention. |
| P5 sensitivity | PASS (disclosed) | s flips the verdict inside +/-50% (0.25: A by 3.79%; 0.75: B by 9.66%), disclosed (category F). Scope thresholds do not move it. |
| P6 data decay | PASS | All URLs reachable; claims present. Notes: Zenodo rights field names no CC0 (GitHub README is the CC0 authority; Zenodo/doi pages 403 to curl); Wikipedia "Calibration of radiocarbon dates" now titled "Radiocarbon calibration" (redirects); Sci Data article number 27 not extracted. |
| P7 accessibility | FAIL | Cold-reader named essentially no blocking real-world terms, BUT answered question 2 concretely: the Sites reading ("expected number of different sites with at least one dated sample") and a date as a probability smear over centuries cannot be pictured without a diagram. That alone is a FAIL. Mechanical pre-screen also FAIL: no published HTML with a visual (case-publish not run). The box-plot SVG was accepted as a comparable example for D2. P7 was run on case.md, not a published page, so hover glosses were not exercised. |

### Tier 2 detail — P1 full solve (recorded from the fresh solver)
D1: Dates top3 700-799 272.0; 1200-1299 244.4; 1100-1199 222.4. Sites top3 1200-1299 152.5; 1100-1199 143.6; 900-999 131.9. Cross values 700s 272.0/128.2; 1200s 244.4/152.5. Gaps: (272.0-244.4)/272.0 = 10.1%; (152.5-128.2)/152.5 = 15.9%.
D2: n=863, 3,616 dates; min 1, Q1 1, median 2 (432nd value), Q3 4, max 137; IQR 3; fences -3.5, 8.5; whiskers end 1 and 8; 103 outliers; mean 4.19.
D3: base 700-799/1200-1299 (10.1%, 5.8%) disagree; shifted 650-749/1150-1249 (13.6%, 7.7%) disagree; median 700-799/1200-1299 (7.0%, 5.8%) disagree; mean 800-899/1100-1199 (4.4%, 7.1%) disagree; mode 1100-1199/1100-1199 (10.2%, 14.1%) agree. Survives: the disagreement in 4 of 5 cuts; neither base winner survives all cuts.
D4: A scores 1.000/0.8407, B 0.8985/1.000; s=0.5 A 0.9203, B 0.9493; tie s=0.1015/0.2608=0.389; defended s=0.7 for B.
Metric: expected number of sites with dated activity (B). Strongest counter: Sites lead only 5.8% over 1100-1199 and the mean/mode cuts flip it. Most sensitive: M5, then M3. Ignored: the mode row. Least supported: 152.5 (M4 independence).

### Tier 2 detail — P2 full solve (recorded from the fresh solver)
A: dates are what the records contain; summed probability is the standard method (S4); 272.0 vs 244.4 is a 10.1% lead, holds under shifted bins (13.6%) and median (286 vs 266); blended A wins for s<0.389; the 700s has 84% of the sites peak while the 1200s has 90% of the dates peak. Weak spot: 103 outlier sites hold 1,829 of 3,616 dates (50.6%).
B: 152.5 vs 128.2 sites (15.9%); a site counts once so 137-date sites cannot inflate it; 700s has 2.1 dates per active site vs 1.6 for 1200s; Sites winner stays within 1100-1299 on all five cuts while the Dates winner wanders 650-1199; blended B wins for s>0.389 (0.949 vs 0.920 at 0.5). Weak spot: 5.8% lead over 1100-1199; M4 independence.

### Tier 3 — human dry-run
NOT RUN. Pueblo/Native community review: NOT DONE (case.json.community_review).

## Open items (hand back to case-write unless noted)
- BLOCKER: none.
- GAP: T1-10 reinforcement carve-out (expected; spine has no n=0 skill). T1-16 cleared by this run's hash.
- Tier 2 FAIL P7: add a diagram of a date as a probability smear over century bins with a two-date site merged into an "at least one" chance (and place near Appendix A); then re-publish and re-run P7 on the published HTML.
- GAPs from probes (case-write): add CE conversion rule for the wall sentence (1200-1299 cal BP = 651-750 CE); say how to read quartiles from a frequency table and how to scale the D2 axis; Appendix D tie wording; facilitator guide: add the frequency-table quartile slip to The Trap, and state the blend normaliser in Twist part 1.
- UNVERIFIED: IntCal20 licence text; Crema and Bevan and Bird et al. read at abstract level; Sci Data article number; site delineation in SiteID; Pueblo/Native community review.
