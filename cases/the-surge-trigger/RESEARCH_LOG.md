# RESEARCH_LOG.md — The Surge Trigger

One row per placeholder: what was searched, what was found or rejected, and why.

## P01 — Appendix A: true new cases in Eastgate on day 0 (I0)

Searched for any public source of a specific county's internal daily case counts for a fictional
scenario — by construction, no such source can exist (this is proprietary/fictional operational
data). **NOT FOUND, as expected.** Resolved as Modeling Assumption **MA1** (4 cases/day) — a
small, realistic starting count for an outbreak just beginning to accelerate.

## P02 — Appendix A: true daily growth-rate constant (k)

**Search 1:** "CDC MMWR early outbreak exponential growth rate doubling time days epidemic curve."
Returned several candidates: an early-COVID compendium citing a 7.4-day doubling time; a
pre-lockdown estimate of 1.30–4.34 days (median 2.59); Ebola doubling times of 15–40 days
depending on country.

**Chosen figure:** the 7.4-day doubling time, because it traces to a single, specific,
highly-cited peer-reviewed primary study (Li et al., NEJM 2020) rather than an aggregate/compendium
figure, and is independently re-quoted (with the same exact number) by a second, separately
peer-reviewed CDC journal article.

**Fetch attempts on the primary NEJM article:**
- `https://www.nejm.org/doi/full/10.1056/NEJMoa2001316` → HTTP 403 (paywall/bot-block).
- `https://www.nejm.org/doi/pdf/10.1056/nejmoa2001316` → HTTP 403.
- `https://pmc.ncbi.nlm.nih.gov/articles/PMC7313654` (a different Wuhan transmission-dynamics
  paper that cites Li et al.) → fetched successfully, but does NOT cite the doubling-time figure
  (only cites the incubation-period figure from the same paper). Rejected as confirmation source.
- `https://ncrc.jhsph.edu/research/...` (Johns Hopkins NCRC summary page) → HTTP 403.

**Successful confirmation:** `https://pmc.ncbi.nlm.nih.gov/articles/PMC7392464` (Muniz-Rodriguez et
al., "Doubling Time of the COVID-19 Epidemic by Province, China," *Emerging Infectious Diseases* —
a peer-reviewed CDC journal) — fetched successfully, quote-confirmed: "Li et al. covered cases
reported by January 22 and found a doubling time estimate of 7.4 (95% CI 4.2–14) days." This is a
secondary but primary-adjacent confirmation (a CDC peer-reviewed journal directly quoting and
citing the original study), graded HIGH per case-research's tier-2 rule (an institution that
republishes tier-1 with attribution).

**Recorded as [S1].** k = ln(2)/7.4 = 0.0937, rounded to **0.094/day**, used directly in Modeling
Assumption **MA2** — applied to this case's fictional county since no source publishes any real
county's actual real-time growth constant.

## P03 — Appendix C: testing capture-rate model (c0, m)

Searched for a citable, quantitative model of how testing/reporting capture rates decline during a
real outbreak surge. Found general qualitative discussion (testing-site strain, turnaround delays)
in secondary sources during earlier searches, but no single citable numeric curve that would apply
to this case's fictional scenario without overclaiming precision. **NOT FOUND as a numeric
figure — resolved as Modeling Assumption MA3** (c0 = 0.65, m = 0.015/day), with the basis stated
as a well-documented *qualitative* operational pattern (testing capacity strain during surges)
rather than a specific cited number, consistent with SPEC §5's rule against citing a number the
source doesn't actually support.

## P04 — Appendix D: True-Curve and Reported-Curve trigger thresholds

Searched implicitly alongside P01/P03 — internal department policy thresholds are, by construction,
not publishable for a fictional county. **NOT FOUND, as expected.** Resolved as Modeling Assumption
**MA4** (1.00 and 0.40 new cases/day, per day, respectively), set independently because the two
curves are measured on structurally different scales (Appendix C's capture rate keeps D(t) smaller
than I(t)).

## P05 — Appendix D: cost of Option A's mandatory verification protocol

**Search:** "mobile health clinic daily operating cost rural public health published budget."
Found several candidates (ResearchGate southern-US mobile-clinic cost study, Mobile Health Map,
BMC Health Services Research Oregon cost study). Chose Mobile Health Map's own aggregated figure
because it was directly fetchable and quote-confirmable.

**Fetch:** `https://www.mobilehealthmap.org/how-much-it-costs-to-run-a-mobile-clinic/` → fetched
successfully, quote-confirmed: "among the mobile clinics registered for Mobile Health Map, the
average annual operating cost is approximately $275,000." No external primary source or date is
cited on the page itself (Mobile Health Map's own aggregated data) — graded **MEDIUM**.

**Recorded as [S3].** $275,000/365 ≈ $753.42/day (derived). Used to *inform*, not literally set,
Modeling Assumption **MA5** ($1,700.00 — roughly 2 days' equivalent operating cost plus additional
senior-staff review time the case author added, since a model-verification protocol is a different
activity than routine mobile-clinic operation and no source publishes its exact cost).

## P06 — Appendix D: average cost per additional case if response is delayed

**Search:** "average cost per case infectious disease outbreak medical productivity loss CDC
economic burden per case." Found several candidates: measles outbreak-cost studies ($43,203.65
average cost/case; a 2025/2026 preprint), CDC MMWR Colorado measles case-investigation costs
($49,769 and $18,423 for two specific investigations), foodborne-illness per-case costs
($196–$4.6M by pathogen).

**Rejected:** the measles outbreak-cost studies — both the ScienceDirect article and the medRxiv
preprint returned HTTP 403 on direct fetch, and could not be independently quote-confirmed within
this research pass, so their headline figures are not used even though search-result summaries
repeated them.

**Fetched and confirmed:** `https://pmc.ncbi.nlm.nih.gov/articles/PMC5769785/` (Marx et al., CDC
MMWR, Nov 2017) — real, primary-publisher, quote-confirmed figures ($49,769 and $18,423 for two
real single-case measles investigations). **Recorded as [S2]**, but used only as *qualitative*
grounding (Background/Appendix B's framing that untimely detection carries real financial stakes
for a health department) — not as this case's own per-case dollar figure, because a full
individual-case-investigation cost of this scale is disproportionate to the "gap in a day's case
count" quantity this case actually needs to price.

**Second search:** "CDC average direct medical cost per case influenza outpatient visit dollars
published estimate." Found a Statista-aggregated figure: "$312 average ambulatory (outpatient)
visit cost due to an influenza infection, 2016–2017."

**Fetched and confirmed:** `https://www.statista.com/statistics/1111205/per-person-costs-of-treatment-for-influenza-in-the-us-by-treatment-type/`
→ fetched successfully, quote-confirmed exact figure and years. No underlying primary source named
on the page — graded **MEDIUM**. **Recorded as [S4]**, used DIRECTLY as this case's $312.00
cost-per-case figure in Appendix D and Challenge 3 (D4)'s arithmetic — applied to a different,
fictional respiratory illness in this case's fictional county, stated explicitly in case.md and
`case.json.sources[S4].note` as an application of real influenza-cost research to a different
scenario, not a claim that this case's own disease is literally influenza.

## Verification sweep

```
placeholders remaining: 0
citation markers with no source row: none
source rows never cited in text: none
LOW-confidence sources: none (S1, S2 = HIGH; S3, S4 = MEDIUM)
```

## Next step

Run `case-readiness` on `the-surge-trigger` — Tier 1 structural checks, then Tier 2's six
simulated-play probes (including `sensitivity_model.py` for P5).
