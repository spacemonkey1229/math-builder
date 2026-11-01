# QA Report: The Tap Date

## case-readiness run: 2026-10-28
**State:** DRAFT -> TIER1_PASS -> TIER2_PASS   **Verdict:** TIER2_PASS (0 BLOCKERs; GAPs and caveats below)
sha256(case.md) = bebce901f8b2d4bab32d3949794475b9b570894a47e902d953f2c19f2c761ec8

### Design note (the central finding)
The sheet's balance claim fails at the natural freeze-thaw definition. Re-derived from GHCN-Daily USW00014742 (fetched 2026-10-28, runs to 2026-10-24, sha256 55228514...32fb), Early Tap = Feb 20 (A), Late Tap = Mar 1 (B), 42-day window, margin = |A-B|/larger. Winner by rule and record:

| Rule (high at least / low at most) | 1950-79 | 1991-2020 | 1996-2025 | 2006-25 | 1950-2025 |
|---|---|---|---|---|---|
| Primary 35/27 (pre-committed) | B 12.0 | A 1.8 | **A 4.7** | A 5.3 | B 2.6 |
| Plain Freeze-Thaw 32/32 | B 9.7 | B 4.5 | B 1.4 | A 1.0 | B 5.2 |
| Warm Day, Any Frost 35/32 (Tmin <= 32) | B 14.2 | B 8.1 | B 5.0 | B 3.0 | B 8.9 |

A wins 4 of these 15 cells. A 48-rule sweep (Tmax 32/33/35/37 x Tmin 25/27/30/32 x window 35/42/49 d), Early Tap wins: 1950-79 4/48; 1991-2020 24/48; 1996-2025 33/48; 2006-25 35/48 (2 ties); 1950-2025 16/48. Largest margin anywhere 17.6%. The case is built so the student discovers and defends this: pre-committed scope (station, 42 d, two dates, Primary Rule, judged on 1996-2025, margin 4.7%), then D3 (records) and D4 (rule-by-record map). Rounding temperatures to whole F first leaves the three 1996-2025 winners unchanged.

### Tier 1: structural (24 checks, `tier1_structural.py`)
23 PASS, 0 BLOCKER, 1 GAP: T1-10 (new_coverage[] empty; reinforcement carve-out: the spine has no skill at n == 0; `reinforcement_note` records the adjacent skills considered). T1-15, T1-18 to T1-24: POLISH "no published/ directory" (case-publish not run). Fixed during the run: T1-14 (guide-only numbers moved into `case.json.derived`), T1-06 (Appendix F not named in Background), Background over 500 words after clarity edits (trimmed to 499).

### Tier 2: simulated play
Probes were run by fresh agents given only the student packet, in batches of at most 3. case.md was edited three times after probes (P7 findings: explain sugarbush/evaporator/spout, no re-drilling, hole drying, freeze-thaw mechanism, "run-day rule" wording, Appendix A rows). P1, P2, P3 and P7 were re-run on the final packet (sha above). P4 and P6 ran on earlier packets; the edits did not touch the twist, rules, windows or sources (P4 inputs: Appendix B, C and the twist text unchanged; P6 checked the same source list).

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Final fresh solver chose A (Early), metric: mean Primary-Rule run days 1996-2025; all D1-D4 arithmetic matches the author's: means 12.667 / 12.067, margin 4.74%, lines Early 0.00275x + 7.21 (+0.03 per decade, r 0.02), Late -0.03411x + 80.80 (-0.34 per decade, r -0.24), crossing 1996.8; D4 map reproduced for all 12 cells and the 3 rules' slopes and crossings (2022.6, 2038.6). Named the reversing cell (Primary 1950-2025 / Plain 1996-2025). Ambiguities reported: ties, correlation cut-offs, "one cell" meaning, crossing year rounding. |
| P2 both-sides | PASS (soft) | Both sides survive. A: pre-committed rule/record, 17 of 30 seasons, recent windows, falling Late line. B: Late wins full record under all three rules and 1996-2025 under 2 of 3 rules, Primary edge t = 1.46. B cracks first at "why may you change the rule or record Ansel fixed before looking?"; A cracks at "is 0.6 run days real, and does it survive a 32 F night threshold?" (it does not). A solver judged: A stronger if the pitch stands on the pre-committed cell, B stronger if it stands on robustness. |
| P3 trap | PASS (guide amended) | Blind wrong paths: (1) stop at the pre-committed 4.7%; (2) override with the full record; (3) crossing year as forecast; (4) ties/denominator/per-decade slips; (5) S6 as tie-break; (6) rule treated as measurement. Guide covered 1 to 4; forms 5 and 6 added to FACILITATOR.md. |
| P4 twist | PASS (soft twist) | Adversarial reviewer recomputed 2026 from the CSV: Primary 15/15 (tie), Plain 26/24 (A), Warm Day 20/22 (B); tie robust to rounding and to strict vs non-strict only in that the strict-inequality reading changes counts but not the Primary tie (15/15) or the two other winners; the only reading that changes the Primary result is counting the 42 days from the day after the tap (14/15), now pre-empted in the guide. Wording error fixed ("rich year" holds under the Primary Rule only). Reviewer called it a soft twist: it pressures rather than refutes. |
| P5 sensitivity | PASS (disclosed) | `sensitivity_model.py`, +/-50% of window length, day margin and night margin. window_len -50% (21 d) flips the winner to B (5.57 vs 6.63); night margin -50% is a near tie (15.97 vs 15.93); other flexes keep A. Flexed margins all <= 19.2% by the script's gap/loser convention (16.1% by the case's convention). Window disclosed as Category X in `sensitivity_disclosure[]`. The rule and record dependence is the case's central finding. |
| P6 data decay | PASS (notes) | 28 URLs HTTP 200. S1 first row 1940-12-01, last 2026-10-24, 2025-02-20 row present; S3 version 3.35, tenths of C, DOI 10.7289/V5D21VHZ; S4 line matches; S5 title and date match (exact phrase "freezing nights and thawing days" not on the page; page supports freeze-thaw); S6 contains the mid-April passage; S7 PDF matches. S8 and S9 do not contain the words evaporator/spout (S10 does and is the cited source for them). S2 DOI redirects to the AMS page (script gets 403; body not checked). |
| P7 accessibility | PASS (judged) | Round 1 FAIL (central tap-hole mechanism and sugarbush/evaporator/spout unexplained); fixed. Final zero-context read: BLOCKING none; about a dozen MINOR items (evaporator purpose, why holes clog, appendix data jargon, reporting-precision consequence, leap-year wording). Run on case.md, not published HTML. The mechanical visual pre-screen reports FAIL by absence (D1 asks for a plot, no published/ HTML exists); it cannot be resolved until case-publish. |

### Tier 2 detail: P1 full solve (final run, condensed to the load-bearing numbers)
D1: Primary Rule, 1950-2025: Early r = +0.022, Late r = -0.243. D2: Early y = 0.002748 x + 7.210 (+0.027 per decade); Late y = -0.034108 x + 80.803 (-0.341 per decade); crossing 0.036856 x = 73.593, x = 1996.78. D3 (Early / Late means, margin, seasons ahead E/L/ties): 1950-79 12.200 / 13.867 Late 12.02% 8/17/5; 1991-2020 13.033 / 12.800 Early 1.79% 15/12/3; 1996-2025 12.667 / 12.067 Early 4.74% 17/9/4; 2006-25 12.150 / 11.500 Early 5.35% 11/7/2; 1950-2025 12.671 / 13.013 Late 2.63% 34/32/10. D4: Plain 1991-2020 L 4.50, 1996-2025 L 1.45, 2006-25 E 0.98, 1950-2025 L 5.16; Warm Day L 8.15, L 5.01, L 2.98, L 8.85; slopes per decade Plain +0.184 / -0.191 (cross 2022.6), Warm Day +0.438 / +0.062 (cross 2038.6). Stand: Primary Rule, 1996-2025; reversing cells: Primary 1950-2025 and Plain 1996-2025. Strongest counter: the edge is 0.6 run days (t about 1.46) and holds under one of three rules. Most sensitive: MA2/MA3, then MA5. Least supported: 42 days (MA1).

### Tier 2 detail: P2 full solve (final run, condensed)
A: Primary Rule, 1996-2025: 12.67 vs 12.07 (4.74%), 17 seasons to 9 (4 ties); 2006-2025 +5.35%; last 10 seasons 12.0 vs 10.7; Late slope -0.34 per decade vs Early flat; lines at 2025 12.77 vs 11.73; rule fixed in advance. B: 1950-2025 13.01 vs 12.67 (2.63%); Plain 1996-2025 25.33 vs 24.97; Warm Day 21.97 vs 20.87 (every Warm Day cell favors B, 2.97% to 8.85%); B wins 11 of 15 rule-by-record cells (8 of 12 in D4); A's paired edge +0.60, SE 0.41, t 1.46; 1991-2020 margin only 1.79%.

### Tier 3: human dry-run
NOT RUN.

## Open items
- **G1 (T1-10):** new_coverage[] empty under the reinforcement carve-out.
- **G2 balance shape:** the pre-committed cell favors A (4.7%) but B wins 11 of 15 rule-by-record cells; a cold solver saw both sides survive, with A needing to concede fragility. Confirm at the Tier 3 Anchor 1 split that the room does not collapse to B.
- **G3 not built:** interactive HTML (hover/hyperlink `math_glossary`, `context_glossary`), docx, xlsx, visual; P1/P7 should be re-run against the published HTML after case-publish, and the P7 mechanical visual pre-screen resolved then.
- **G4 UNVERIFIED assumptions:** 42-day tap-hole life (MA1) and all three run-day rules (MA2, MA3) are stated assumptions, not published figures (two search framings plus fetches found none). The cause of the 2013 change in reporting precision is not established. NCEI reuse wording not stated (case cites, does not assert public domain). AMS DOI body not verified.
- **G5 polish:** Background says the Early window ends April 2 while Appendix C notes it ends a day earlier in a leap year (a P7 reader flagged the apparent conflict with "42 days"); P4 called the twist soft; P7 minor jargon items (evaporator purpose, appendix data terms).
