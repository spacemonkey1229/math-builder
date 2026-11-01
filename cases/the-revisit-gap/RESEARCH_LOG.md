# Research Log — The Revisit Gap

Concept sheet (`CONCEPTS_remote-sensing_2026-09-12.md`, C2) graded data feasibility MEDIUM and
flagged that no public, concrete commercial-imagery price figure had been confirmed (Planet's and
Sentinel Hub's public pricing pages returned no rendered numbers). This session's research
confirmed the free side remains HIGH feasibility and, on a second attempt with a different vendor
angle (reseller marketplaces rather than the primary vendors' own pages), found one concrete,
real, rendered commercial price.

| # | Searched for | Found | Outcome |
|---|---|---|---|
| P01 | Sentinel-2 revisit time and finest-band resolution | Copernicus Data Space Ecosystem documentation: 10 m resolution, 5-day revisit at the equator with 2 satellites | SOURCED — S1, HIGH |
| P02 | Commercial (Planet SkySat) imagery pricing, direct vendor pages | `planet.com/pricing/` returned only a page heading, no rendered dollar figures — matches the concept sheet's own finding exactly, confirmed again this session | NOT FOUND on the primary vendor page |
| P03 | Commercial imagery pricing, reseller/marketplace angle | SkyFi's "Planet Select" marketplace page: SkySat Archive from $6/km², SkySat Flexible Tasking from $12/km², confirmed via direct fetch | SOURCED — S5, MEDIUM (a reseller marketplace price, not Planet's own list price) |
| P04 | Minimum-mapping-unit rule of thumb tied to pixel size | Multiple secondary sources (ArcGIS Pro docs, Esri GIS Dictionary, search-result synthesis) converge on a "3×3 pixel" rule, with a concrete Landsat example (30 m pixels → ~0.81 ha minimum mapping unit); the original 2003 IEEE paper (Knight & Lunetta) could not be fetched directly (ResearchGate 403; a direct PDF mirror TLS-failed) | SOURCED — S6, MEDIUM (corroborated by secondary sources, primary paper unreachable this session) |
| P05 | Real, matched detection-lag data comparing a commercial and a free feed on the same events | No public program publishes this comparison for any specific reserve | NOT FOUND (load-bearing) — recommended exit: Modeling Assumption (MA1), constructed consistent with each feed's real revisit cadence |
| P06 | Annual illegal-clearing hectares for a specific small protected reserve | No public per-reserve figure found; this is not a real named reserve | NOT FOUND (load-bearing) — recommended exit: Modeling Assumption (MA5) |
| P07 | Share of tropical deforestation events too small for moderate-resolution sensors to detect | General remote-sensing literature (already used in `cases/pixel-snap/case.json`'s S9, Brinck et al. 2017, on tropical forest edge density) supports the *category* of finding (small-clearing prevalence is real and documented) but no single figure matches this case's specific reserve | NOT FOUND (load-bearing, exact figure) — recommended exit: Modeling Assumption (MA6), flagged HIGH sensitivity, swept in `sensitivity_model.py` |

## Redesign note

The concept sheet's original framing risked needing an unsourceable commercial per-km² price. This
session found one (S5, via a reseller marketplace rather than the primary vendor), which is why
this case was written with real dollar figures rather than treating the entire commercial cost side
as an assumption. The reserve's specific detection-lag data, annual clearing total, and small-
clearing share remain genuinely unsourceable for a real, undisclosed reserve — these are disclosed
Modeling Assumptions (MA1, MA5, MA6), consistent with `case-research`'s own worked-example guidance
for exactly this situation.

## Verification

All 7 `sources[]` entries (S1-S7) were fetched or searched live this session (2026-09-18); S3/S4
reuse two URLs independently fetched live in a prior session on this same project
(`cases/pixel-snap/case.json`, 2026-09-12) for the identical unchanged-infrastructure claim, per
this project's established practice of citing a previously-verified still-current source rather
than re-fetching. S6's primary source could not be fetched directly (two independent attempts
failed: a 403 and a TLS error) and is graded MEDIUM, corroborated by secondary sources, and used
only to justify a method (the 3×3-pixel rule), never as a Reserve-specific measured figure. S7 is
graded LOW (title/existence only) and used only as background context, never load-bearing.
