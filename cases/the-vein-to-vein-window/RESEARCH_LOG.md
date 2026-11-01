# Research Log — The Vein-to-Vein Window

One row per placeholder from `case-write`'s pass. `case.md` and `case.json` (`sources[]`,
`modeling_assumptions[]`, `needs_source[]`) are already updated; this log documents what was
searched, what was found, and what was rejected and why.

## P01 / P03 (Appendix A background) — real published vein-to-vein and manufacturing-turnaround figures

**Searched:** `CAR-T therapy "vein-to-vein time" typical weeks manufacturing turnaround`;
`"vein-to-vein" CAR-T median days 2024 2025 real-world Yescarta commercial`.

**Found:** A CIBMTR (Center for International Blood and Marrow Transplant Research — a real,
independent U.S. patient-outcomes registry) analysis, described in a Kite Pharma/Gilead press
release (2022-12-11), gives a real-world median vein-to-vein time of 27 days for Yescarta
(axicabtagene ciloleucel), inclusive of apheresis, pre- and post-manufacturing transport,
manufacturing, and hospital scheduling/pre-conditioning. A separate Kite press release
(2024-01-30) documents an FDA-approved manufacturing process change that reduced Yescarta's median
manufacturing turnaround (leukapheresis to product release) from 16 days to 14 days.

**Disposition:** SOURCED as S1 (27-day vein-to-vein median) and S3 (14-day manufacturing
turnaround). Both graded MEDIUM: each is a company press release describing/announcing the
underlying fact rather than an independently republished or peer-reviewed primary source. Neither
is load-bearing — both are background-only, establishing why the "last mile" this case is actually
about happens after weeks of irreversible process are already sunk. Considered but rejected:
searching for the underlying CIBMTR conference abstract or peer-reviewed manuscript directly to
upgrade S1 to HIGH — not pursued further within this research pass since the figure is
non-load-bearing and MEDIUM confidence is an accurate, honest grade for a press-release-sourced
registry figure.

## P02 (Background) / Appendix B — the FDA-label hard cutoff

**Searched:** `Yescarta OR Kymriah package insert thawed product infuse within hours stability`.
**Fetched directly:** the FDA structured product labeling XML at accessdata.fda.gov (the primary
regulatory document), and separately attempted drugs.com's dosage page as a secondary
cross-check (returned HTTP 403 — inaccessible to this fetch, not used).

**Found:** The FDA-approved Yescarta (axicabtagene ciloleucel) prescribing information states the
thawed product "may be stored at room temperature (20°C to 25°C) for up to 3 hours," and separately
that the entire bag must be infused within 30 minutes once infusion begins (a separate, narrower
operational constraint this case does not use, to keep the case's single hard cutoff clean and
unambiguous — see "Rejected" below).

**Disposition:** SOURCED as S2, confidence HIGH — a primary FDA regulatory document, unambiguous
unit, current labeling for the product as marketed. This is the case's one load-bearing
real-world figure: it sets the 180-minute cutoff (3 hours × 60 minutes/hour, arithmetic, not
independently sourced) used in every one of D1–D4's calculations.

**Rejected:** using the label's separate "infuse within 30 minutes of starting" constraint as a
second cutoff. Two hard cutoffs in the same case would either be decorative (if only one is ever
binding) or would force a compound piecewise function beyond this case's intended scope — the case
is built around one clean, unambiguous, real hard boundary (the 3-hour post-thaw window), and the
30-minute infusion-duration figure is not needed by any deliverable, so per SPEC's "no decorative
constraints" rule it is omitted from the case entirely rather than stated and left unused.

## Appendix C route timings (Options A/B nominal elapsed time) — NOT FOUND, resolved as Modeling Assumptions

**Searched:** hospital-internal cell-therapy thaw-to-infusion timing benchmarks, on-site vs.
central-pharmacy CAR-T logistics timing comparisons. This is exactly the outcome the concept
sheet's own feasibility note anticipated ("exact per-patient/per-manufacturer figures will likely
need disclosed Modeling Assumptions grounded in published typical ranges").

**Found:** No public, institution-specific data exists for the internal minute-level timing of a
hospital's own thaw-to-bedside-infusion workflow — this is operational, internal-to-each-hospital
information, not published anywhere. Two distinct search framings were tried (general "on-site vs.
central pharmacy CAR-T thaw timing" and "cell therapy bedside infusion workflow minutes"), neither
surfaced anything beyond generic process-step descriptions with no timing figures attached.

**Disposition:** NOT FOUND → **stated Modeling Assumption** (the correct exit per
`skills/case-research/SKILL.md` — never invented as if sourced). Recorded as MA1 (On-Site Rapid
Thaw, 45 minutes nominal) and MA2 (Central Pharmacy Courier, 150 minutes nominal), both built from
realistic, disclosed process-step reasoning (thaw time, identity/product verification, transport or
its absence, bedside intake) rather than from any specific institution's real data, and stated
openly in Appendix E with basis and sensitivity, not buried in a data table as though sourced.

## Appendix C delay scenarios and probabilities — NOT FOUND, resolved as Modeling Assumptions

**Searched:** hospital courier/transport on-time performance rates, internal workflow delay-rate
statistics for time-critical specimen or drug transport.

**Found:** No public institution-specific delay-rate data exists for hospital-internal courier or
workflow delays of this kind (elevator waits, identity-verification callbacks, traffic on an
internal campus route). This class of data is not publicly tracked or published at the level of
specificity this case would need.

**Disposition:** NOT FOUND → **stated Modeling Assumption**. Recorded as MA3 (a shared two-tier
delay model: +20 minutes minor / +50 minutes major) and MA4 (a shared probability distribution:
70% no delay / 20% minor / 10% major), applied identically to both routes so the comparison
isolates the two routes' elapsed-time difference rather than assuming one route is inherently more
delay-prone than the other — a deliberate modeling choice disclosed in Appendix E, not a
convenient number chosen to force a particular verdict (see `case.json.balance.margin_basis` and
`sensitivity_model.py` for the resulting, honestly-computed 10.00% margin).

## Appendix D — the worked algebra contrast function `S(x)`

**Disposition:** Not a research item. `S(x) = (x²+5x)/x` is disclosed in-document as a standalone
teaching construct (a hypothetical staffing-cost-savings model), explicitly labeled as such and
not presented as a real hospital figure. No search was performed or needed; this complies with
SPEC §5 because the function is never presented as sourced or as a real-world fact.

## Verification sweep

```
placeholders remaining in case.md: 0
citation markers with no source row: none ([S1], [S2], [S3] all resolve)
source rows never cited in text: none
LOW-confidence sources: none (S1 MEDIUM, S2 HIGH, S3 MEDIUM — none LOW, none load-bearing at LOW)
```

## Next step

Run `case-readiness` on `the-vein-to-vein-window`.
