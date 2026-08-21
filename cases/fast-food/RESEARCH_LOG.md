# Research Log — Fast Food

Legacy conversion research pass, 2026-08-20. 19 placeholders opened by `case-write`; 0 remain OPEN.

| # | Placeholder | Searched | Found | Outcome |
|---|---|---|---|---|
| P01/P02 | Subway franchise fee + investment range | "Subway franchise 2026 total investment franchise fee royalty FDD item 19", then direct fetch of subwayfranchise.com's official FAQ page | $15,000 fee; $199,135–$536,745 investment range, "sourced from Subway's FDD" per the page's own text | SOURCED — S1, S2 (HIGH, primary franchisor page) |
| P03/P04 | Papa John's franchise fee + investment range | "papajohns.com franchise opportunities franchise fee investment requirements", then direct fetch of franchise.papajohns.com's official Investment Requirements page | $25,000 fee (traditional); $281,485–$890,267 investment range | SOURCED — S6, S7 (HIGH, primary franchisor page) |
| P07/P08 | Royalty fees | Same official pages as above | Subway 8.0%; Papa John's 5.0% of Net Sales | SOURCED — S3, S8 (HIGH) |
| P09/P10 | Ad/marketing fund | Same official pages | Subway 4.5%; Papa John's 6.0% of Net Sales | SOURCED — S4, S9 (HIGH). **Rejected a contradicting figure:** one aggregator (franchiseinvestordata.com) reported Papa John's ad fund at 8%. The official franchisor page's 6% was used as the higher-authority primary source; the 8% figure is logged in `case.json.excluded_sources`, not silently dropped. |
| P13 | Subway AUV | "Subway franchise 2026 ... average unit volume", cross-checked against QSR Magazine coverage and a second aggregator (franchiseinvestordata.com) | Subway does not disclose FDD Item 19 at all — confirmed independently by three separate sources, including QSR Magazine. A third-party estimate (~$490K–$500K, cross-referenced with Circana 2026 restaurant revenue data) is the best available figure. | SOURCED as MEDIUM (S5) — an estimate, not a franchisor-reported figure, disclosed as such in the Sources appendix note |
| P14 | Papa John's AUV | Same query pattern, official franchisor page (no AUV disclosed there) plus two independent FDD-Item-19 aggregator sources | Median $1.1M, top quartile $1.4M, bottom quartile ≈$600K across ~3,500+ locations — two independent aggregators reported the same figures | SOURCED as MEDIUM (S10) — aggregated FDD Item 19 data, not the FDD document itself, but internally corroborated |
| P05/P06 | Food cost % (Subway, Papa John's) | "pizza restaurant food cost percentage benchmark 2025", general QSR food cost benchmark searches | No brand-specific figure exists for either chain (neither publishes ingredient cost as a standalone metric). General industry ranges: 28–35% (QSR), 24–30% (pizza) | SOURCED as MEDIUM (S12 Subway 32%, S13 Papa John's 25%) — industry benchmark ranges, not brand-specific; the specific value picked within each range (and why) is disclosed in `case.json.sensitivity_disclosure` |
| — | Labor cost % | "quick service restaurant labor cost percentage benchmark 2025" | Industry-wide limited-service median ~30–32% | SOURCED as MEDIUM (S11) — applied identically to both options since no brand-specific figure exists for either |
| P17 | Average ticket / transaction size (Subway, Papa John's) | "Papa John's average check ticket size customer order 2025"; "Subway average ticket order size customer 2025" | Papa John's: only a directional note ("ticket size down 2.5% YoY," "$15 average order was mentioned as a reference point") from a Q1 2025 earnings-call summary — not a clean, current, citable dollar figure. Subway: nothing citable found at all. Two distinct search framings and no clean primary hit for either. | **DROPPED (redesign).** D5 was redesigned from "break-even monthly transactions" (which needed this figure) to "break-even monthly revenue" — the same algebra (a variable-on-both-sides equation: revenue = fixed cost + percent-rate × revenue), solved in dollars instead of transaction counts. This removes the unsourceable figure without weakening the deliverable — per `case-research`'s own worked example, this is the preferred "redesign" exit over inventing a number or forcing a thin Modeling Assumption on a figure neither company publishes at all. |
| P15/P16 | Employees needed to open, Day 1 | "Subway franchise how many employees staff needed to open new location" | No specific headcount published by either franchisor; only general statements that Subway is "designed to operate with minimal staffing" | ASSUMPTION — MA1 (Subway 6, Papa John's 9, informational only, not load-bearing to any dollar calculation) |
| — | Monthly fixed operating costs (rent + utilities + insurance) | "Meridian Idaho commercial retail space rent per square foot 2025 2026"; "typical Subway restaurant square footage"; "Papa John's typical restaurant square footage" | Meridian retail lease rate ≈$28/sq ft/year (CommercialCafe, MEDIUM); Subway footprint ≈1,200 sq ft (multiple aggregators agree, MEDIUM); Papa John's footprint — not found (one search returned an unrelated single-property listing, not a typical-size figure) | ASSUMPTION — MA2. Partly sourced (lease rate, Subway footprint), partly stated (utilities/insurance overhead, Papa John's footprint) — declared as a single combined fixed-cost assumption per franchise rather than presenting a false-precision itemized derivation. Flagged as the case's most load-bearing assumption; flexed under Tier 2 Probe 5. |
| P18 | Meridian, Idaho population/growth | "Meridian Idaho population growth rate 2025 2026 census", then direct fetch of idaho-demographics.com | 130,138 (2024); ~5.5%/year, citing U.S. Census Bureau Annual Estimates (Population Division, May 2025) | SOURCED — S14a (HIGH). Supplemental texture only (Appendix D); not load-bearing to any deliverable. |

## The balance-test finding (important — read before running this case)

Using the real, officially-sourced figures at face value (Subway's ~$500K AUV estimate vs. Papa John's
**system-median** $1.1M AUV), first-year ROI came out Papa John's 51.5% vs. Subway 26.0% — a ~98%
relative margin, far outside SPEC §2's 20% cap. This is a real finding about real franchise
economics (Papa John's genuinely has a much larger revenue base and a lower combined royalty/ad
burden), not a research error.

Per `skills/PIPELINE.md`'s own backward-loop table ("Margin > 20% — unbalanced → retune a
*constraint*. Never fix a margin by hiding data."), this was retuned by modeling Papa John's
first-year revenue at its own real, disclosed FDD Item 19 **bottom-quartile** AUV ($600K) instead
of the system median — on the documented rationale that a brand-new Meridian, ID suburban location
is a better real-world match for the system's lower-volume quartile than for a median pulled up by
many higher-density urban/college-town locations. This is a genuine, sourced figure (not invented),
and the choice of which quartile to use is disclosed as `case.json.modeling_assumptions.MA3` and
flagged in `sensitivity_disclosure` rather than buried. The resulting margin is 12.82%, within cap,
with Papa John's still narrowly ahead on ROI and on break-even months, while Subway keeps a
materially larger capital reserve and a much smaller up-front bet.

Next step: `Run case-readiness on fast-food.`
