# Research Log — The Two Offers

Stage: `case-research`. Six `{{NEEDS_SOURCE}}` placeholders enumerated from `case.md` at start.
Worked in order of load-bearing weight: the two base salaries first (they set the slope of each
`V(t)` line and dominate the D3 crossover), then the two signing bonuses (y-intercept), then the
401(k) match (a smaller slope contributor), then the commute/parking cost last (also a slope
contributor, but the case narrative tolerates it being the "soft" figure a Hero can challenge).

---

## P01 — Cascadia (Steady Offer) annual base salary

**Placeholder:** `entry-level data analyst annual base salary, USD, on-site role at a mid-size robotics/tech company, US, 2026 or most recent`

- Tier-1 attempt: searched BLS OEWS for a "Data Analyst" SOC code. Rejected — BLS has no distinct
  "Data Analyst" occupation code; the nearest code (15-2051, Data Scientists) returned a median
  annual wage of $120,230 (2025), which is a poor proxy (data scientist pay runs well above data
  analyst pay) and BLS's public OOH/summary pages don't expose the 10th-percentile ("entry")
  breakout without a raw-file download this session could not parse cleanly. Rejected as too poor
  a proxy to use for a load-bearing figure.
- Tier-2 attempt: Robert Half's 2026 Salary Guide publishes a "Data Analyst — Technology" role
  with an explicit low/mid/high band ($96,250 / $117,250 / $138,500), where "low" is defined as
  "new to the role." This is a real, dated, national staffing-firm compensation survey — used the
  "low" figure. **Found. SOURCED as S1, confidence MEDIUM** (proxy: "Technology" sector broadly,
  not robotics specifically; "new to the role" is not identical to "first job out of college").

## P04 — Northwind (Frontloaded Offer) annual base salary

**Placeholder:** `entry-level data analyst annual base salary, USD, fully remote role at a mid-size analytics company, US, 2026 or most recent`

- Needed a genuinely distinct, independently-sourced figure (not just picking a different tier off
  the same Robert Half page — that would launder one methodology into looking like two).
- Searched Levels.fyi's "Entry Level Data Analyst" page for the United States: median total
  compensation $80,000 (25th pct $65,000, 75th pct $100,000), crowdsourced/self-reported, live
  data. **Found. SOURCED as S3, confidence MEDIUM** (self-reported panel; "total compensation"
  used as a proxy for base salary, since entry-level data-analyst pay is overwhelmingly base).
- Rejected: general Glassdoor "entry-level data analyst" average ($63,153) — considered but not
  used, since Levels.fyi gave a more specifically-labeled "entry level" cut with visible
  percentiles and a clearer methodology statement.

## P02 — Cascadia one-time signing bonus

**Placeholder:** `typical entry-level tech signing bonus, USD, on-site role, US, 2026 or most recent`

- Searched WorldatWork, NACE, SHRM, and Indeed Hiring Lab for a dollar figure. All four report
  *prevalence* (% of employers offering bonuses) but not dollar amounts in their free/public
  content. Rejected — no usable number.
- Found Poets&Quants for Undergrads' 2026 report: average 2025 signing bonus across 110 ranked
  undergraduate business schools = $7,328. This is real, dated, and specific to Maya's exact
  population (undergraduate business-analytics grad) — but it is a single population-wide average,
  not split by industry or on-site/remote, so it can't independently source *two different*
  bonuses for the two offers without laundering one number into two.
- Better resolution found: Pave's Sign-On Bonus Benchmarks (140,000+ accepted offers, Pave x
  Greenhouse), which reports sign-on bonus size *as a percent of base salary* by role category,
  including "Data Science": median 9%, 75th percentile 15%. Applying the median rate to Cascadia's
  sourced base ($96,250 x 9%) gives a bonus of $8,663 that is smaller in a way consistent with the
  case's own narrative (see P05). **Found. SOURCED + DERIVED as S1-D1 (inputs S1, S2), confidence
  MEDIUM.**
- The $7,328 Poets&Quants figure was not used in the final case.md table (it doesn't
  differentiate the two offers), but is worth noting for a future facilitator sanity-check: $8,663
  sits reasonably close to it, which is a good cross-check that the derived figure isn't wildly
  off from real undergraduate bonus norms.

## P05 — Northwind one-time signing bonus

**Placeholder:** `typical entry-level tech signing bonus, USD, fully remote role, US, 2026 or most recent`

- Same search effort as P02; no public source splits bonus dollar amounts by remote-vs-onsite.
- Resolved the same way as P02, using Pave's *75th-percentile* Data Science sign-on-bonus rate
  (15%) against Northwind's sourced base ($80,000 x 15% = $12,000 exactly). Choosing the 75th
  percentile (vs. Cascadia's median) is disclosed explicitly in case.md and case.json as this
  case's own modeling choice — it is what makes Northwind's bonus "larger" as the narrative
  requires, and it is built on a real, cited rate distribution rather than an invented number.
  **Found. SOURCED + DERIVED as S3-D1 (inputs S3, S2), confidence MEDIUM.**

## P06 — Northwind employer 401(k) match

**Placeholder:** `typical employer 401(k) match, expressed as annual USD or percent of salary matched, US private-sector entry-level role, 2026 or most recent`

- Tier-1/2 attempt: Vanguard's "How America Saves" report (25th edition, published 2026-06-16,
  covering 2025 plan-year data across Vanguard-administered plans) — a primary source, since
  Vanguard is the recordkeeper reporting on its own book of plans. Reports the average employer
  match reached a record 4.7% of pay. **Found on first tier-1/2 attempt. SOURCED as S4, confidence
  HIGH.** Dollar value ($3,760/yr = $313/mo against Northwind's $80,000 base) shown as a derived
  line (S4-D1).
- Not used: a "most common match formula" figure (e.g., "50% of the first 6% of pay") — the
  Vanguard press release mentioned formula prevalence in passing but a WebFetch of the full press
  release did not surface a citable formula breakdown; the average-match-percent figure alone was
  sufficient and cleaner for this case's needs.

## P03 — Cascadia monthly commuting + parking cost

**Placeholder:** `average monthly commuting plus employer-area parking cost, USD, for a mid-size-metro on-site office job, US, 2026 or most recent`

- Searched for a single published "commuting + parking" composite figure. Found several
  candidates, all rejected as insufficiently clean for a load-bearing sourced figure:
  - Chamber-of-Commerce–branded "$8,000+/year commuting cost" figure (chamberofcommerce.org, a
    private lead-gen site, not the U.S. Chamber of Commerce) — fetched directly and confirmed it
    measures *lost wages from commute time* (a wage-loss/opportunity-cost calculation off Census
    ACS data), not out-of-pocket expense. Explicitly the wrong quantity. Rejected.
  - A separate "$5,748/year direct commuting cost, 170 cities" figure attributed to the same site
    was found only in a search-result AI summary, with no direct-fetch confirmation of
    methodology or that it isolates parking specifically. Rejected — could not verify provenance
    directly (SPEC's "never cite a search-results page" rule).
  - AAA's 2025 "Your Driving Costs" fact sheet: a genuine tier-1-adjacent source (AAA, a national
    organization, publishes an annual cost-per-mile study), but the PDF could not be parsed for
    text by the fetch tool, and a secondary site's cents-per-mile breakdown (fuel 11.13c +
    maintenance 11.91c for a medium sedan) could not be independently re-confirmed via a second
    fetch. Rejected as unverifiable to the standard this case needs.
  - SpotHero's live monthly-parking pricing pages: real marketplace data, city-specific, but
    undated/live rather than a fixed historical report — usable only as one input to an assumption,
    not as a load-bearing standalone figure.
- **Conclusion: NOT FOUND as a single, cleanly-sourced composite figure.** No public source
  publishes "commuting + parking cost" as one number for a generic, unnamed mid-size metro — it is
  inherently dependent on an individual's commute distance and city, which this fictional case
  does not specify beyond "mid-size metro." Exit chosen: **(a) Stated Modeling Assumption (MA1)**,
  not a redesign — the case's narrative structurally needs Cascadia to carry a real recurring cost
  that Northwind (remote) avoids, so dropping the figure isn't viable, and a redesign that removed
  it would gut the case's central comparison.
  - MA1 basis: IRS 2026 standard business mileage rate ($0.725/mile, S5 — primary, government,
    dated, verified by direct fetch) applied to an assumed 12-mile one-way commute (504 mi/month),
    plus SpotHero's Denver, CO monthly parking rate ($155/month, S6) as a representative mid-size
    metro (deliberately not NYC/SF/Chicago). Total: $520.40/month, rounded to $520/month.
  - Disclosed explicitly in case.md Appendix C as not sourced, with a Sensitivity column, per the
    skill's requirement that a dilemma-flippable assumption must be presented as a feature the
    Hero can challenge, not buried in the data table.

---

## Verification

Ran the skill's verification script after all edits:
- Placeholders remaining in case.md: **0**
- Citation markers with no matching Sources row: **none**
- Source rows never cited in text: **none**
- LOW-confidence sources: **none** (no LOW-confidence figure was used at all, let alone
  load-bearing)
- All 9 `sources[]` entries in case.json (6 primary + 3 labeled derivations) carry claim, value,
  units, org, title, url, accessed, and confidence.

## Balance/margin note for the next stage

Computing `V(t) = mt + b` for each offer with the sourced figures:

- Cascadia: net monthly value = $96,250/12 − $520 (commute) = $7,500.83/mo; b = $8,663 (bonus).
- Northwind: net monthly value = $80,000/12 + $313.33 (401k) = $6,980.00/mo; b = $12,000 (bonus).

Solving `7500.83t + 8663 = 6980t + 12000` gives a crossover at **t ≈ 6.4 months**. This is
mathematically usable for Challenge 3 (D3 solves cleanly; D4 has room to pick a "shorter" tenure,
e.g. 3 months, and a "longer" one, e.g. 24 months), but the crossover is dominated almost entirely
by the ~$16,250/year base-salary gap between the two sourced figures (S1 vs. S3) — the bonus,
401(k), and commute-cost differences are comparatively minor levers. Flagging this for whoever
runs `case-qa` / the facilitator margin check: Cascadia wins by an increasingly large margin for
any tenure beyond about half a year, which may make Argument B (the Frontloaded Offer) feel
under-powered in discussion unless the facilitator leans on the "what if you leave before month 6"
framing explicitly.
