# Research Log — Driving Age

One row per placeholder that existed in the case-write draft. All seven resolved SOURCED; zero
DROPPED, zero remaining OPEN. One quantity (chauffeuring mileage) could not be sourced and is
recorded as Modeling Assumption MA1.

| # | What was needed | Searched | Found | Outcome |
|---|---|---|---|---|
| P01 | Arizona's current GDL minimum ages (permit / Class G / Class D) | "Arizona minimum driving age graduated license current law 2026"; "ADOT Arizona graduated driver license official age requirements class G class D azdot.gov" | azdot.gov's own Teen Driver Guide, directly fetched: permit 15y6m, Class G 16y, Class D eligible 18y | SOURCED — S1, HIGH |
| P02 | Real driver-age-vs-fatal-crash-rate dataset for the scatterplot deliverable | "IIHS state minimum licensing age teen fatal crash rate per 100,000 licensed drivers by age table"; "IIHS fatality facts teenagers 2023 chart deaths per 100,000 licensed drivers by age" | A state-by-state age-law table did not surface a usable multi-state crash-rate series. Pivoted to IIHS's own national age-by-age table (deaths per 100,000 people, 2024), directly fetched, full 13-row table captured | SOURCED — S2, HIGH. Redesign note: the original plan (state minimum-age law vs. state crash rate) was replaced with driver-age vs. crash-rate because a genuine multi-state dataset with both variables could not be located after two search framings; the age-based table is both more findable and more pedagogically direct for the D1-D3 scatterplot/linear-equation deliverables |
| P03 | Average insurance-premium cost of adding a 16-year-old driver | "average cost increase add teen driver 16 year old to car insurance policy 2026" | Forbes Advisor ($2,735/yr) blocked on fetch (403); MoneyGeek gave total-policy costs, not the increase; carinsurance.com directly fetched, gave a specific increase figure with an August 2026 update date | SOURCED — S3, MEDIUM (aggregator, not a named insurer's own filing) |
| P04 | A real per-mile cost figure to price the "extra chauffeuring miles" side | "AAA \"Your Driving Costs\" 2025 report average cost per mile sedan cents" | AAA's own newsroom PDF, fetched as a document (WebFetch's text extraction failed on the PDF binary; read directly as a PDF instead) | SOURCED — S4, HIGH |
| P05 | A real anchor figure for "how many miles does a family drive per year" (basis for the chauffeuring-mileage modeling assumption) | "average annual miles driven per vehicle United States FHWA 2023 2024" | DOE Alternative Fuels Data Center's mirror of FHWA Highway Statistics 2024 Table VM-1, directly fetched | SOURCED — S5, HIGH. Used only as the disclosed basis for MA1, not as a load-bearing figure in its own right |
| P06 | A second state with a later permit age than Arizona, for Appendix E context | "New Jersey minimum age learner permit 16 official MVC"; direct fetch of state.nj.us/mvc (301→nj.gov/mvc, then 404) | Official nj.gov MVC page unreachable; DMV.ORG's New Jersey teen-driver page confirms age 16 with several corroborating detail points | SOURCED — S6, MEDIUM (non-load-bearing context only) |
| P07 | Germany's minimum driving age (context, matches the original 2021 source's own claim) | "Germany minimum driving age 17 accompanied driving 18 unsupervised official law" | Germany's own federal administrative portal (verwaltung.bund.de), English-language page, directly findable and consistent with the original source | SOURCED — S7, HIGH |
| MA1 | How many extra miles per year a parent drives chauffeuring a non-driving 16-17-year-old | "National Household Travel Survey teens chauffeured miles per week parents driving trips to school"; "average distance students live from school miles NCES school commute average" | No public dataset isolates parent-chauffeuring mileage specifically. NHTS-based academic papers study GDL laws' effect on adolescent travel behavior in general terms, not a clean extractable per-week or per-year mileage figure suitable for direct citation | **NOT FOUND → Modeling Assumption.** Declared MA1 (6,000 mi/year, ~half the FHWA national average per-car mileage of 11,026 mi/year from S5) in the open, per case-research's three-exit rule. This is the case's one load-bearing, disclosed, unsourced dial — flagged in `sensitivity_note` and required to be swept by Tier 2 probe 5 |

## Post-Tier-2 fix (2026-08-20)

| # | What was needed | Searched | Found | Outcome |
|---|---|---|---|---|
| P08 | A real citation for the per-mile teen-crash-rate claim in Appendix B's context note, at a granularity closer to this case's real 15.5-vs-18 comparison | Tier 2 probe 4 (twist-integrity, fresh subagent) found the original claim ("16-19 crash several times higher than 20+") had NO citation anywhere in case.md or sources[], plus a granularity mismatch (16-19 vs 20+ doesn't speak to a 16-vs-18 comparison) and an internal tension (case.json's argument_a cited the population-rate table "still climbing" as a safety argument for A -- exactly the inference FACILITATOR.md's own Trap section calls invalid). Searched "IIHS teen driver fatal crash rate per mile driven 16-19 three times drivers 20 and older citation"; "NHTSA fatal crash involvement rate per 100 million vehicle miles traveled by driver age 16 17 18 19" | AAA Foundation for Traffic Safety's "Rates of Motor Vehicle Crashes, Injuries and Deaths in Relation to Driver Age, United States, 2014-2015" (published 2017), directly fetched: "The crash rate of drivers ages 16-17 years was nearly double that of drivers ages 18-19" -- a genuinely closer age-band match to 15.5-vs-18 than the original 16-19-vs-20+ framing | SOURCED — S8, HIGH. case.md's Appendix B context note, case.json's sources[]/balance.argument_a/argument_b, and FACILITATOR.md's Argument for A/Argument for B/Twist/Lessons Learned were all rewritten to (a) cite S8 explicitly, (b) rely on S8 rather than the population-rate "still climbing" reading as AYE's real safety argument, and (c) state plainly that S8's 16-17-vs-18-19 bands are the closest available real data, not an exact match for 15.5-vs-18 |

## Verification pass

```
placeholders remaining in case.md: 0
citation markers with no source row: none ([S1]-[S7] all present in sources[])
source rows never cited in text: none
INCOMPLETE source rows: none (all of claim/value/units/org/title/url/accessed/confidence present)
LOW-confidence sources: none
```

Next step: run `case-readiness` Tier 1 structural checks, then Tier 2's six probes.
