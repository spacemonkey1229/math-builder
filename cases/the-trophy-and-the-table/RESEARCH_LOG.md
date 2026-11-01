# Research Log — The Trophy and the Table

Researched 2026-10-03. Seven placeholders SOURCED, two (MA1, MA2) NOT FOUND -> stated Modeling
Assumptions. No fourth outcome used.

| # | Placeholder | Searched | Found | Outcome |
|---|---|---|---|---|
| P01 | Final 2024/25 Premier League table | Fetched Wikipedia "2024-25 Premier League"; tried premierleague.com tables page (JS-rendered, no data returned); tried ESPN standings | Wikipedia table read in full: all 20 rows (W/D/L/GF/GA/GD/Pts), no deductions, bottom three relegated. Every GD and points value matches the bundle CSV (01_epl_2024_25_goal_difference_points.csv) | **SOURCED** S1, MEDIUM (transcription of the official table; official page not machine-readable). |
| P02 | Club record, 17th, lowest in 48 years, Europa League final facts | Wikipedia club-season page; Al Jazeera report; web search on the dismissal | Final: 21 May 2025, San Mames, Bilbao, 1-0 vs Manchester United. W11 D5 L22, GF64 GA65, 38 pts, "lowest top-flight finish in 48 years" | **SOURCED** S2, MEDIUM. Al Jazeera says the final was 25 May: wrong, rejected. |
| P03 | Europa League explainer; winner gets Champions League place | UEFA about page (did not state the rule); Wikipedia "UEFA Europa League" | Second-tier European club competition; winner qualifies for the next Champions League | **SOURCED** S3, MEDIUM. |
| P04 | Injury record | Fetched premierleague.com/en/news/4208927 | Dated 29 Dec 2024: all four senior centre-backs injured; a midfielder and 18- and 19-year-olds used in defence | **SOURCED** S4, HIGH. No points cost stated or claimed. Fan-site injury counts not used. |
| P05 | Free data terms | Fetched football-data.co.uk/data.php and /englandm.php; StatsBomb open-data README; Understat EPL page | Football-Data: private individuals only, no commercial/bot/scraper/AI use (on data.php; englandm.php lists season files but states no terms). StatsBomb: credit and logo on anything published. Understat: no terms on page | **SOURCED** S5 HIGH, S6/S7 MEDIUM. Link-only; nothing bundled or fetched by the case. |
| P06 | Relegation and goal-difference definitions (context) | Wikipedia pages | Definitions confirmed | **SOURCED** S8, S10 MEDIUM. |
| P07 | MA1: share of a miss that repeats next season | Initially judged not findable for one club. Then (coordinator request) derived from data: fetched Wikipedia action=raw wikitext for ten Premier League season pages (2015-16 to 2024-25, S14-S23), parsed W/D/L/GF/GA (every season: 20 clubs, 38 games each), fitted each season's own GD-to-points line (points = 3W+D, so Everton's 8-point and Forest's 4-point 2023/24 deductions are excluded), regressed next-season residual on this-season residual over the 17 clubs present in both seasons of each pair | Pooled 153 club-pairs: slope 0.109, SE 0.083, 95% range -0.054 to 0.273 (season-cluster bootstrap -0.014 to 0.230); per-pair slopes -0.15 to 0.38; excluding 2022-24 pairs 0.105 (n=119). Clubs missing their line by 5+ points (14): mean next-season residual +1.15, 8 of 14 above the line. Largest earlier miss: Manchester City 2019/20, -11.21; this club is -13.68 | **DERIVED (not sourced), USABLE but noisy.** Forecast slope 0.11, range about 0 to 0.27, labelled derived with the small-sample caveat; framed as a plain forecast (a club that missed by r misses by about 0.11 r next season), not a split into parts. Football-Data CSVs not used. |
| P08 | Reset cost of replacing a manager | No public study for one club | n/a | **NOT FOUND -> REDESIGN (2026-10-04).** The case no longer fixes a reset cost (earlier drafts used 6, then 2 points, which the coordinator rejected as tuning). It poses the break-even (0.11 x 14.40 = 1.58 points) and asks each student to choose and defend a range; 2 points is used only as the balance-test evaluation point (midpoint of a suggested 0-4 range). |
| P09 | Club statement and real outcome (facilitator only) | Fetched tottenhamhotspur.com club statement | Dated 6 June 2025, 16 days after the final; board "unanimously concluded" a change was in the club's best interests; cites poor league form (78 points from the last 66 league games) and acknowledges injuries and European-competition prioritisation | **SOURCED** S9, HIGH (via fetch summary; guide should read it directly). Kept out of case.md so the decision is not revealed. |

## Recomputed derived figures (labelled DERIVED, not sourced)

All recomputed by the author from S1 with sensitivity_model.py (n-2 residual SD):
full fit points = 52.35 + 0.666 x GD, R^2 = 0.941, residual SD 4.63; club predicted 51.68,
residual -13.68 (2.95 spreads below); next-worst Bournemouth -4.35; largest surplus Aston Villa
+8.99. Leave-one-out (other 19): 53.07 + 0.665 x GD, R^2 = 0.970, residual SD 3.34; club predicted
52.40, residual -14.40 (4.32 spreads below). These agree with the concept sheet's R1a figures.

## Rejections worth recording

- Football-Data CSVs were not downloaded or bundled; the persistence of club residuals across
  seasons is left as a student extension.
- FBref xG (discontinued 20 Jan 2026) never cited. ESPN's standings summary garbled the bottom
  three and was not used. Al Jazeera's 25 May final date rejected (Wikipedia: 21 May).
- "Lowest finish in 48 years" is carried from Wikipedia (MEDIUM); Al Jazeera's "worst since
  1976-77" is consistent but was not independently checked.

## Persistence derivation: honest limits

All figures are DERIVED by the author with a throwaway script (parse wikitext, fit lines, pooled regression, season-cluster bootstrap). The estimate is small (about 0.11) and noisy; it is an average over typical clubs and cannot say why a miss repeats, nor whether it would for a miss as large as this club's, which exceeds anything in the sample. It supports the direction (most of a miss does not repeat) more than the exact value.
