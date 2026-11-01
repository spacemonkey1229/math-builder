# QA Report — Up or Out

## case-readiness run — 2026-10-28
**State:** DRAFT -> TIER1_PASS (Tier 2 NOT clean)   **Verdict:** BLOCKED for TIER2_PASS (P7 FAIL)   sha256(case.md) = f047d97d7118637690409718db2ff3e6db0a0a2c3f177ce09da5951b3fc22d0f

### Tier 1 — structural (24 checks)
0 BLOCKERs. GAPs (2): T1-10 empty new_coverage under the reinforcement carve-out (no spine skill has n==0; reinforcement_note on file); T1-14 two guide-only rounded figures ($44,910, $74,325, the packet-rounded regrets; stated in the guide's grading note). Published-artifact checks T1-15/18-24 have nothing to check (no published/; case-publish not run, by instruction). preflight_lint: clean.

### Tier 2 — simulated play
| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh solver (packet only) did D1-D5 correctly, chose Tall on the stated metric, named regret as the counter-argument and MA3 as the sensitivity; arithmetic matches the guide within rounding |
| P2 both-sides | PASS | Neither side collapses; Tall's closest-to-collapse question is the small-survey outcome (answer rests on Appendix E); Wide concedes it loses the average |
| P3 trap | PASS | Solver's wrong path (trust pooled gap + thin average) matches the guide's trap; added the averaging-$/sq-ft slip and the Appendix E bin misreading to the guide |
| P4 twist | PASS | Twist (exactly 300 sq ft) overturns the Tall-by-average position; Wide wins by 4.6% under every reading tested; no unstated convention |
| P5 sensitivity | PASS (disclosed) | window half-width stable; range_lo and range_hi flips/cap breaches disclosed as category F in sensitivity_disclosure[] |
| P6 data decay | PASS | All 7 URLs reachable; 71,003 count reproduced exactly; dictionary strings, Admin Code and ZR quotes present |
| P7 accessibility | FAIL | Mechanical: D1/D2 ask for plots and there is no published visual yet (box_plot_anatomy.svg exists in context/ but nothing is published). Cold-read named well over 2 unexplained setting concepts: Alteration Type 1/egress/occupancy, PW1/declared cost, pre-filed/signed off, 1-2-3 family, the survey, two-family house layout, stories, accessible bathroom |

TIER2_PASS is NOT recorded.

### Remaining work for P7 (hand back to case-write / case-context)
Add story-glossary terms with sourced links for survey, PW1, pre-filed / signed off, 1-2-3 family building, egress/occupancy, stories, two-family house; one sentence in Background saying who lives upstairs and what "partial floor" means; embed the box-plot and scatter examples in the published HTML; re-run P7 against the published HTML. Optional: say in Background what a filing is (one real project's paperwork).

### Tier 2 detail — P1 full solve
Solver output (summary of every figure; full text held in the session transcript): D1 five-number summaries (median of halves): 250 Tall n66 58/277/719/1250/1935, no outliers; 250 Wide n194 24/200/421.5/857/1911, outlier 1911; 450 Tall n67 27/170/319/548/1534, 5 outliers 1159-1534; 450 Wide n167 59/226/419/600/1773, 13 outliers 1162-1773; boxes overlap in both windows. D2 slopes Tall -5.286 and +0.138, Wide +0.258 and +0.447; both non-linear; crossing 303.8 sq ft. D3 pooled gap 30.5%. D4 costs Tall 179,700 / 183,508 / 136,350 / 101,628 / 106,715 / 112,800 / 124,480 / 133,790 / 143,415, Wide 105,375 / 120,202 / 130,320 / 138,482 / 130,830 / 136,575 / 145,680 / 166,048 / 188,325; averages 135,821 vs 140,204, gap 4,384 = 3.23%; over savings Tall 250, 275, Wide 425, 450. D5 regrets Tall 74,325, Wide 44,910. Metric: average cost over nine sizes; strongest counter: minimax regret favors Wide; most sensitive: MA3; ignored: pooled Appendix D; least supported: Tall 718.8 at 250. Ambiguities flagged: interpolate on $/sq ft vs total (3.8 vs 3.5 sq ft apart, immaterial), which size to compare in D3.

### Tier 2 detail — P2 full solve
A (Tall): wins average (135,821 vs 140,204), 6 of 9 sizes (325-450), plateau about 300-319 $/sq ft, Wide exceeds savings at 425/450; small-size spike probably other work (totals 159,190 vs 121,255; 28% add stories). B (Wide): smallest worst case (44,910 vs 74,325), $364-437 per sq ft across the range, n 167-194 vs 57-70, cheaper at 250/275/300, a 4.4% probability shift to 250/275 flips the average, range 250-400 favors Wide by about $5.4k.

### Tier 3 — human dry-run
NOT RUN.

## Margin and break-even
Margin 3.2% (gap / winner). Break-even job size about 304 sq ft. Winner is a statistical coin flip (bootstrap 52%).
