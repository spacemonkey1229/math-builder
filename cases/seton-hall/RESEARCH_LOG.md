# Research Log — Seton Hall

Legacy conversion research pass, 2026-08-13. Every `{{NEEDS_SOURCE}}` avoided at write time by
sourcing directly during the conversion (case-write and case-research run together for this
legacy conversion, matching the cardiology/tide-window precedent).

## What was searched, and why

| # | What was needed | Searched | Found | Confidence | Rejected |
|---|---|---|---|---|---|
| P1 | Whether the legacy case's live-committee-vote framing is a real event | "Seton Hall basketball 2019-20 record 21-9 NCAA tournament canceled COVID Big East champion" | **The 2020 NCAA Tournament was canceled outright, March 12, 2020 — no bracket was ever finalized or made public.** This is the single most important finding of the conversion; it forced a full reframe of case.md's Background (disclosed reconstruction, not a transcript). | HIGH (independently confirmed by two more searches below) | — |
| P2 | Whether the legacy data workbook is real season data | "Virginia basketball 2018-19 record 23-7 offensive rating defensive rating KenPom" | Virginia's 35-3 2018-19 record does NOT match the workbook's 23-7 row for "Virginia" — but this ruled out 2018-19, not the workbook's authenticity. Led to re-checking against 2019-20 instead (P1's season), where Virginia (defending champs, mediocre title defense before the season froze) plausibly sits around 23-7. | — | Initial 2018-19 guess rejected once P1 confirmed the real season is 2019-20. |
| P3 | Confirm Bernadette McGlade is a real committee member | "Bernadette McGlade Atlantic 10 commissioner NCAA men's basketball selection committee 2020" | Real: McGlade was literally sequestered with the committee in Manhattan in March 2020 when the shutdown happened. Confirmed a real 5-year term on the committee. | HIGH | — |
| P4 | Confirm the 353-team field size the legacy case claims | "2019-20 NCAA Division I men's basketball 353 teams tournament canceled selection committee" + "2019 NCAA Division I men's basketball 353 teams" | 353 Division I teams, consistent across the 2018-2021 seasons. Matches the workbook's own row count (353) exactly after removing the blank rows. | MEDIUM | — |
| P5 | A real bracketology reconstruction, to see how outside analysts read Seton Hall's case | "Joe Lunardi final bracketology 2020 Seton Hall seed reconstruction canceled tournament" | Lunardi's projections through early March 2020 consistently had Seton Hall on a top-4-seed line (top 16). Useful corroborating color, but **not cited as a source** — Lunardi's projections were never "final" (the season kept moving after each snapshot), and no single authoritative "last" bracketology could be pinned down with a clean date the way the AP poll and NET rank could be. Excluded from case.json.sources for that reason, not because it was wrong. | — | Excluded: no single citable "final" snapshot; used only to sanity-check that the direction of this case's real sources (AP/NET both "in") is not an outlier reading. |
| P6 | A real, dated, national ranking to serve as the case's genuinely close primary metric | "Seton Hall basketball 2019-20 record 21-9 NCAA tournament canceled COVID Big East champion" (P1) then Wikipedia fetch | **Final AP media poll: No. 15**, released March 16, 2020 — the last complete national ranking of the season. This became `primary_metric` (S3, S4). | HIGH (S4 is a primary athletic-department source; Wikipedia S3 independently agrees) | — |
| P7 | A second, opponent-adjusted real ranking to corroborate/contrast with AP | "Seton Hall NET ranking March 2020 NCAA basketball final NET number 12 or 16" | **NET rank No. 12**, final tracked week (WarrenNolan.com, a well-established public NET/RPI history aggregator). Used as FACILITATOR.md's Twist and case.json S5. | MEDIUM (secondary aggregator; the NCAA does not itself publish a historical NET archive) | — |
| P8 | A widely-repeated claim that the real committee was "leaning" one way on Seton Hall specifically | General search during drafting | Only found in unattributed forum/blog commentary, no named source or date. | LOW | **Excluded** per SPEC.md §5 — logged in `case.json.excluded_sources` rather than used. |

## Data-quality finding (not a placeholder, a disclosed defect)

While building Appendix B/C from the legacy workbook, 83 of 353 rows' win-loss column had been
silently corrupted by spreadsheet auto-date-formatting (a text value like `12-15` became the
calendar date December 15, 2020). Confirmed by inspecting the underlying cell values directly
(`data_only=False`, cell number_format `m-d`) — the original text is not recoverable from the file.
Per MCS-21, this is reported as `CORRUPTED` in the companion CSV (`data/team_stats_2019-20_full_field.csv`)
and disclosed in case.md Appendix C, rather than guessed at or silently dropped. None of the 25
teams used in Appendix B's curated bubble field are affected.

## What did NOT need sourcing

The legacy case's own methodology text (Team/Opponent Offensive and Defensive Rating definitions)
was kept verbatim from the legacy docx's Appendix B key — these are definitions, not factual claims
requiring a citation, and they accurately describe a standard opponent-adjusted efficiency metric.

## Outcome

Zero `{{NEEDS_SOURCE}}` placeholders remain — every load-bearing number in case.md is either cited
(S1-S7) or disclosed as a Modeling Assumption (MA1-MA3) or a data-quality defect (Appendix C).

Next step: run `case-qa` on `seton-hall`.
