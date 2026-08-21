# Research Log — AirBnb Or Landlord

Legacy conversion. The source docx (`Case Study_ AirBnb Or LandLord.docx`) itself contained no
`{{NEEDS_SOURCE}}` placeholders in the pipeline sense — it referenced two market-data appendices
(Boise Airbnb market, Boise traditional rental market) that existed only as embedded screenshots
and attached PDFs, none of it machine-readable text, and all of it 2–3+ years stale by 2026. This
log covers what was re-researched to make the case's actual numbers (D1/D2 in case.md) real,
current, and cited, per SPEC.md section 5 ("a case citing a still-changing real entity states a
fixed 'as of' cutoff").

## P01 — Boise short-term (Airbnb) rental market: current ADR and occupancy rate

**Searched:** "Boise Idaho Airbnb short term rental market 2026 average daily rate occupancy
rate." Multiple aggregators returned different figures (AirDNA, Rabbu, AirROI) — a real,
disclosed disagreement between data providers, not smoothed over.

**Found:** AirROI's Boise report (fetched directly, 2026-08-19): ADR $195/night, occupancy 47.8%,
1,268 active listings, $25,127 average annual revenue, period Aug 2025–Jul 2026. Rabbu's search
snippet (not directly fetchable — 403) reported ADR $167–$186 and occupancy 51–67% for a similar
period.

**Decision:** Used AirROI's figures (S1) because it was the one page that actually fetched with a
clear, dated, sourced breakdown. The disagreement with Rabbu's snippet is disclosed in case.md
Appendix B rather than hidden — this is exactly the "contested figure" case SPEC.md section 5
calls out (the "50% of vaccines wasted" precedent): rather than picking whichever number favors
one option, the case states that real providers disagree and shows which one it used and why.

## P02 — Boise traditional (long-term) rental market: current 3BR rent

**Searched:** "Boise Idaho average rent 2026 3 bedroom house rental market report."

**Found:** Zumper's Boise rent-research page (fetched directly, 2026-08-20): 3-bedroom houses at
$2,197/month, dated August 2026. Multiple other aggregators (RentCafe, RentHop, apartments.com)
reported figures from $1,800–$2,600 for 3BR depending on methodology (house vs. apartment,
different sample windows).

**Decision:** Used Zumper (S2) — directly fetched, clearly dated, with a clean per-bedroom
breakdown. Chosen over RentHop's higher figure and RentCafe's lower blended figure because it was
the one page that actually resolved on fetch with an unambiguous 3BR-specific number.

## P03 — Furnished-rental premium (percent over unfurnished)

**Searched:** "furnished rental premium percentage more than unfurnished apartment house 2026."

**Found:** Multiple sources converge on a real range: long-term furnished rentals typically
command 15%–30% more per month than an identical unfurnished unit (furnishedunfurnished.com,
fetched directly), with short-term/luxury furnished rentals reaching 40–50% — not applicable here
since Option B is a 1–2 year lease, not a short-term furnished stay. A national dataset (Nomad)
cited in the same search showed a real but smaller ~5-point gap for long-term furnished vs.
unfurnished in early 2026.

**Decision:** Used the 15%–30% range (S3) as the real sourced basis for Modeling Assumption MA1.
The source case's own original figure (25%–35%) sits mostly outside this real range's upper
bound, and at its own 25% midpoint the case's margin came out to 37.2% — over SPEC.md section 2's
20% balance cap. Rather than hide this and keep the source's number, the case was retuned: MA1
now uses 15%, the real sourced low end, which brings the margin to a defensible, disclosed 18.5%.
See case.json.legacy_conversion_note for the full account of this retuning decision.

## P04 — Airbnb host service fee (2026)

**Searched:** "Airbnb host service fee percentage 2026."

**Found:** Airbnb's own Help Center page (airbnb.com/help/article/1857, fetched directly,
2026-08-20) confirms Airbnb has migrated most hosts to a single host-only service fee of 15.5%
(range 14%–16% depending on host, 16% for Brazil/Mexico listings), deducted from the host's
payout, applied to the nightly rate plus any host-set fees (including the cleaning fee) but not
taxes. This is a **material structural change** from the split-fee model (3% host + ~14–16.5%
guest) that existed when the source case was originally written — the source predates this
migration entirely, so its implicit fee assumptions (if any) would be wrong for 2026 regardless.

**Decision:** Used the "most hosts pay 15.5%" figure (S4) directly from Airbnb's own official
page — HIGH confidence, primary source, directly fetched.

## P05/P06 — Historical screenshots and PDF (source folder)

The two AirDNA dashboard screenshots (Apr 2023) and the We Know Boise PDF (Q4 2022 data) that
shipped with the original case were extracted and are reproduced in case.md Appendices B and C as
labeled historical color — real primary evidence of what the Daltons themselves would have seen
when researching this decision originally — but explicitly **not** used in any D1/D2 computation,
which relies entirely on the fresh 2026 figures (S1/S2) above. This mirrors the precedent set by
`cases/family-trip`'s handling of its own stale embedded screenshots.

## Not researched / not needed

- **Mortgage ($1,092/mo), utilities ($225/mo), maintenance ($490/yr), household income/expenses
  ($8,200 / $4,000 / $2,300):** these are the Daltons' own fixed scenario facts (like a family's
  stated budget in any other case in this corpus) — not externally verifiable market claims, so
  T1-08 does not require a `sources[]` row for them.
- **Boise short-term-rental lodging/occupancy tax (Idaho 6% sales + 2% travel/convention tax +
  local auditorium-district tax):** real, and briefly considered, but Idaho's 2025 marketplace-
  facilitator law (House Bill 583) has Airbnb itself collect and remit state/local taxes on
  behalf of hosts in most cases — a guest-side pass-through that does not change either option's
  actual profit calculation. Dropped as a decorative constraint per case-write's "no decorative
  constraints" rule rather than forced into the case just because it's real.
- **Boise long-term rental vacancy rate:** considered for a vacancy-adjusted Option B, but the
  source case's own framing already treats a signed 1-2 year lease as providing "guaranteed
  monthly income during the lease," and modeling a vacancy-and-turnover cycle would push this T2
  case toward T3-level multi-period modeling. Left out; the historical 3.21% single-family
  vacancy figure (S6) is reproduced as color only in Appendix C.

## Verification pass (post-write)

```
placeholders remaining in case.md: 0
citation markers with no source row: none
source rows never cited in text: none
```

All 6 `sources[]` entries carry `claim`, `value`, `units`, `org`, `title`, `url`, `accessed`,
`confidence`. Zero LOW-confidence sources. `status: "researched"` — case handed to case-readiness.
