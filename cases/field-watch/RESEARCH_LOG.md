# Research Log — Field Watch

Sourced 2026-08-12, `case-research`.

## S1 — Sentinel-2 revisit interval

**Claim:** Sentinel-2's two-satellite constellation revisits the same ground every 5 days at the
equator.
**Source:** European Space Agency (Copernicus), "Sentinel-2 images the globe every 5 days" —
https://sentinels.copernicus.eu/web/success-stories/-/sentinel-2-images-the-globe-every-5-days
**Accessed:** 2026-08-12. **Confidence:** HIGH.
**Note:** Cross-checked against a second independent search result (ESA/eoPortal facts-and-figures
pages, same figure) before use. This is the real, published revisit cadence — the case's 5-day gaps
between Pass 1→2 and Pass 2→3 in Appendix B are not invented spacing.

## S2 — NDVI thresholds are not universal

**Claim:** NDVI is a real, standard vegetation index; burn/vegetation-stress NDVI thresholds used
in real practice are not a single fixed value — they are calibrated by region and vegetation/crop
type.
**Source:** US Geological Survey, Burn Severity Portal glossary —
https://burnseverity.cr.usgs.gov/glossary
**Accessed:** 2026-08-12. **Confidence:** HIGH.
**Note:** A targeted web search for a specific "standard" NDVI burn/stress threshold (tried values
around 0.3-0.4) returned no single universal figure — the literature is consistent that operational
thresholds are regionally calibrated, not a fixed constant. This finding is used directly: it is
the honest reason this case states its own 0.40 threshold as a disclosed Modeling Assumption (MA1)
rather than presenting it as if it were a sourced, universal figure — doing the latter would have
been exactly the kind of fabricated-precision SPEC §5 exists to prevent.

## Modeling assumptions (not sourced — see Appendix F)

- **MA1 — NDVI damage threshold (0.40 = 0.37 base + 0.03 calibration allowance).** Grounded in S2's
  real finding that thresholds are calibrated, not universal; the case states its own calibrated
  value honestly rather than inventing a fake "industry standard." The 0.03 calibration allowance is
  the FLEX-swept dial in `sensitivity_model.py` (±50%, effective threshold 0.385-0.415): margin
  ranges 12.02%-17.09%, Model B stays the winner throughout.
- **MA2 — The three passes' specific NDVI values (Appendix B) and the filing deadline (Appendix D).**
  This field's own authored claim data — no public database of real per-field, per-claim satellite
  readings exists (same convention as every prior case's authored domain data: Cold Chain's route,
  Plaza Pavers' border cut, Vent Cap's nesting result, Apron Order's marker layout, Survey Corner's
  field notes).

## Search methodology

Direct WebFetch/WebSearch verification against both sources on 2026-08-12, same day as authoring —
both reachable, both figures confirmed present. The NDVI-threshold search additionally surfaced,
and ruled out, several candidate "standard" values (0.2 for bare-vegetation presence, 0.3-0.5 range
cited inconsistently across burn-severity literature) — none rose to the level of a single citable
universal figure, confirming S2's own claim rather than contradicting it. No figure in this case is
fabricated: every number is either traced to S1/S2, is the field's own authored claim data (MA2,
explicitly disclosed), is an explicitly disclosed modeling assumption with basis and sensitivity
(MA1), or is arithmetic derived from those inputs (`case.json.derived`, `sensitivity_model.py`).
