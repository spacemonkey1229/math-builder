# Research Log — Clear-Sky Dome

Case was drafted and researched in one continuous pass (2026-09-17/18): every figure was either
sourced live or marked as a disclosed Modeling Assumption before it was written into `case.md`, so
`case.md` never carried literal `{{NEEDS_SOURCE}}` tokens. This log records the search trail per
placeholder, in the order `case-research`'s own procedure calls for.

## P01 — Vantage Mesa (plateau) clear-sky fraction

- Searched: "ESO Paranal astroclimate photometric nights clear sky fraction percentage."
- Tier-1 attempt: ESO's own Astronomical Site Monitor / Sky Conditions page. Fetched directly:
  `eso.org/sci/facilities/paranal/astroclimate/Obsconditions.html`. Found a real, long-term
  (2014–2024), clearly dated, primary-publisher figure: 77% Photometric+Clear, 90% usable time,
  75%/80% seasonal split. **Used, HIGH confidence (S1).**
- A satellite-based secondary study (arXiv 1011.4815) reported an alternate 88% "clear nights" figure
  for 2007–2008 at Paranal — rejected in favor of S1's longer, more recent, primary-publisher figure,
  since using two different eras/definitions for the same site would itself be a contested-figure
  problem.

## P02 — average usable dark hours per night

- Searched: "average number of hours of darkness per night astronomical observing ESO Paranal annual
  average dark time." No single annual-average figure was found publicly stated.
- Found instead a real, peer-reviewed range: Patat et al., "The Dancing Sky" (arXiv 0801.2270),
  stating Paranal's shortest and longest astronomical nights as 7.4 h and 10.7 h.
- **Decision:** used the midpoint (9.05 h) as a derived estimate, applied identically to both sites
  (both are subtropical-latitude sites), disclosed as a derived average rather than a directly
  published annual mean. This is not a Modeling Assumption requiring sensitivity treatment because it
  is applied identically to both options and therefore cannot change the winner — same logic as
  Turbine Channel's MA2 (a factor shared across both options only rescales both answers together).

## P03 — Sable Hollow (sheltered) comparison site

- First attempt: Mauna Kea Weather Center (`mkwc.ifa.hawaii.edu`) — flagged as unreachable in the
  concept sheet; not attempted again.
- Second attempt: Kitt Peak National Observatory. Searched "Kitt Peak National Observatory clear
  nights per year statistics" — found conflicting secondary figures ("over 300 clear nights,"
  "260 nights of observing time") with no single clearly-dated primary source. Attempted to fetch
  NOIRLab's own Kitt Peak weather page directly (`kpno.noirlab.edu/.../kpno-weather`) —
  **HTTP 403 Forbidden**, could not verify live. Dropped Kitt Peak as unusable per SPEC §5 (do not
  cite a page you could not fetch).
- Third attempt: Roque de los Muchachos Observatory, La Palma (Isaac Newton Group). Searched
  "Isaac Newton Group La Palma Roque de los Muchachos percentage clear nights photometric" — found a
  real, peer-reviewed figure (70% clear annual average, 95% summer; 60% photometric annual average),
  attributed to published La Palma sky-clarity literature. **Used, MEDIUM confidence (S3)** — MEDIUM
  rather than HIGH because its "clear" category is not identically defined to Appendix A's
  "Photometric+Clear" category; this mismatch is disclosed directly in `case.md` Appendix A/B rather
  than smoothed over.

**CORRECTION, 2026-09-18 (Tier 2 P6 data-decay verification):** the "70% clear (95% summer), 60%
photometric" figures above were never directly confirmed against the cited paper at write time — they
came from a WebSearch AI-summary paraphrase, the same failure mode already caught once for S2 (see P02
above). Running the actual P6 probe (a live re-fetch of every `sources[].url`) included re-fetching this
exact paper directly and reading it. **The real paper does not state those figures.** Direct quotes from
della Valle, Maruccia, Ortolani & Zitelli, "Analysis of the fraction of clear sky at the La Palma and Mt
Graham sites," MNRAS 401(3), 2010:
- "At La Palma, we found a mean percentage of clear nights of 62.6 per cent from ground-based data"
- "71.9 per cent from satellite-based data"
- "the telescope operated for 70.8 per cent of the total nights"
- "the TNG is opened for the whole night and without interruption for more than 50 per cent of all of
  the nights considered"

None of these is "70%"/"95%"/"60%." **Corrected** `case.md` Appendix B, `case.json.sources[S3]`, and
every downstream figure to use the verified 62.6% ground-based clear-night mean (the closest
instrument-type match to Appendix A's ground-based ASM figure) — this is now the case's official Sable
Hollow clear-sky input. This single correction moved the case's margin from 14.85% to its final **4.79%**
(winner unchanged: Sable Hollow). Confidence upgraded S1/S3 relationship from MEDIUM to **HIGH** for S3,
since it is now a directly quoted, verified peer-reviewed figure, not a paraphrase.

This is the second time in this case's own research trail (after S2) that a search-engine AI summary
attributed a specific, plausible-looking, wrong figure to a real paper. Both were caught because
`case-research`'s own doctrine (SPEC §5, "a plausible number is not a true number") and `case-readiness`'s
P6 probe both require a direct fetch-and-quote, not a search-summary citation, before a figure ships.
Neither would have been caught by a Tier 1 structural check alone.

## P04 — dome enclosure geometry and standard-spec steel weights

- Searched: "observatory dome kit diameter price spec sheet fiberglass wind rating," then narrowed to
  "Ash-Dome Model R specifications shell thickness gauge steel weight PDF."
- Ash-Dome's own site (`ashdome.com`) and its distributor (`deepspaceproducts.com`) give diameter
  ranges (8'–16'6" Model R) and confirm Galvalume steel / 14-gauge skirt construction, but no
  itemized weight-by-size table was found on either page.
- Fetched a real, dealer-hosted as-installed spec page for a specific real Ash-Dome installation
  (Company Seven, "MCCM Astronomical Observatory Ash Dome Arrangement & Specs"):
  5.0 m (16'6") diameter, 2.65 m drum wall height, 755 kg drum-wall ("cylindrical foundation") weight,
  1,193 kg dome-cap weight. **Used, MEDIUM confidence (S4)** — MEDIUM because it is a dealer page, not
  the manufacturer's own primary spec sheet.
- **Cross-check performed, not just accepted:** back-calculated an effective shell thickness from
  S4's weight and area (mass ÷ (steel density × surface area)) — got ≈2.31 mm for the drum wall. This
  is consistent with Ash-Dome's own separately published claim (`ashdome.com`) that the skirt uses
  "14 Gauge galvanized steel" (nominal ≈1.9–2.0 mm) plus the added mass of welded stiffening angles —
  the two real, independent sources corroborate rather than contradict each other.

## P05 — reinforced vs. standard wind design

- Searched for a dome-specific wind rating or reinforced-gauge option: no manufacturer publishes a
  wind-zone-specific gauge chart for small (5 m class) dome kits. Returned **NOT FOUND**.
- Redesign considered and adopted (case-research's own "redesign" exit, per SKILL.md §5): rather than
  inventing a dome-specific reinforcement number, used a real, primary, federally regulated wind-speed
  standard as a stated stand-in — HUD's Basic Wind Zone Map (24 CFR §3280.305), Wind Zone I = 70 mph,
  Wind Zone II = 100 mph. **Used, HIGH confidence (S5).**
- The *scaling relationship* connecting those wind speeds to a shell-thickness multiplier (pressure ∝
  v², required thickness for constant bending stress ∝ √pressure, so thickness ∝ velocity ratio) is a
  standard structural-engineering simplification, disclosed as MA2, not itself an external citation.
- **First attempt used Wind Zone III (110 mph)** instead of Zone II — this produced a margin above 27%
  regardless of how the pier footing was sized, breaching SPEC §2's cap. **Rejected and retuned** to
  Zone II (100 mph), which is still a real, distinct, regulated tier and produces the case's final
  16.94% margin. This is the honest tuning SPEC §2 calls for: adjusting a real constraint choice
  (which real wind-zone tier to use), not inventing or hiding data.

## P06 — pier footing dimensions

- Searched IBC Table 1806.2 presumptive soil bearing values (real, public, government model-code
  table: 1,500–12,000 psf by soil type) as a candidate sizing basis. Computing footing size from pure
  bearing capacity against the enclosure's real total weight gives an implausibly small footing
  (well under 1 m² base) relative to how real telescope piers are actually built.
- Found instead that real observatory pier-design guidance (both professional and amateur) documents
  oversizing the footing for mass/stiffness (vibration damping at the optical axis) rather than sizing
  it to bearing capacity alone — a real, well-documented design principle, though not tied to one
  single citable numeric spec for this exact hypothetical scale.
- **Resolved as MA3**: a stated footing size (3.0 m × 3.0 m base, 1.0 m height), identical at both
  sites specifically because this design driver is not wind-dependent. Tried scaling the footing base
  with the same wind-based reinforcement factor in an earlier draft — this pushed the margin toward
  27% almost entirely on its own (footing volume scales with the square of a linear base-size factor)
  and was rejected in favor of holding it constant, both for margin balance and because the underlying
  engineering rationale (vibration mass, not wind resistance) genuinely supports treating it as
  site-independent.

## P07 — material unit prices (first pass, since corrected — see "Tier 2 P6 corrections" below)

- Steel: searched "structural steel plate price per pound 2026 hot rolled." Found a real, dated 2026
  range ($1.17–$1.24/lb) from two independent industry compilations (Leeco Steel, AGMetalMiner).
  **Used midpoint $1.20/lb = $2.6455/kg, MEDIUM confidence (S6, derived).**
- Concrete: searched "NRMCA average ready mix concrete price per cubic yard 2025 2026." A search-engine
  AI summary reported a $179.89/yd³ figure attributed to NRMCA. **Used, MEDIUM confidence (S7, derived,
  unit-converted to $235.29/m³).**
- Formwork: searched "concrete formwork cost per square foot 2026 construction estimate." Found a
  real, dated (May 2026) range ($4.35–$5.32/sq ft) from Homewyse's cost calculator. **Used midpoint
  $4.84/sq ft = $52.10/m², MEDIUM confidence (S8, derived)** — same source-class precedent as Turbine
  Channel's S7 (a cost-aggregator site, not a primary trade body, graded MEDIUM accordingly).
- Steel density: a standard, universally published physical constant (7,850 kg/m³ for carbon/Galvalume
  steel). **HIGH confidence (S9).**

## Tier 2 P6 (data-decay) corrections — 2026-09-18

Running the actual P6 data-decay verification (re-fetching every `sources[].url` directly rather than
trusting the original search-summary text) found and fixed three real problems, all before Tier 2 was
recorded as complete:

1. **S2 (Paranal night-length range, 7.4 h / 10.7 h) could not be verified.** A search-engine AI summary
   had attributed this range to Patat et al.'s "The Dancing Sky" paper. Both that paper and a second
   Patat et al. paper about Paranal twilight brightness were fetched directly and read — neither
   contains this figure. Per SPEC §5 ("a plausible number is not a true number"), the claim was
   **dropped, not kept on an unconfirmed attribution.** The average-usable-dark-hours input was
   redesignated as **MA4**, a disclosed 9.0-hour planning assumption applied identically at both sites
   (confirmed to leave `margin_pct` unchanged versus the earlier 9.05 h figure, since it cancels out of
   the ratio — see `case.json.modeling_assumptions[MA4]`).
2. **S6 (steel price) was re-fetch-tested and the original Leeco Steel URL now returns HTTP 403.** More
   importantly, re-examining the claim found that "structural steel plate" (heavy plate stock) is the
   wrong product category for this case's shell components, which are thin galvanized sheet steel (the
   real Ash-Dome installation uses 14-gauge sheet, not structural plate). Re-sourced to a real, directly
   fetched, dated hot-rolled-*coil* price ($1,200/short ton, week of 2026-08-25, General Steel citing
   Steel Market Update) — the correct product category, and meaningfully cheaper than the original plate
   price. This single correction dropped the case's margin from 16.94% to 12.78% (both winners
   unchanged, both comfortably inside SPEC §2's 20% cap) — see `case.json.excluded_sources[]`.
3. **S7 (concrete price) direct fetch found a different exact figure than the original search summary.**
   Concrete Network's own page states "$179.95 per cubic yard in 2025," not "$179.89" as an earlier
   AI-search summary had reported, and does not itself attribute the figure to NRMCA (it separately
   shows NRMCA data only through 2024). Corrected to the page's own exact, directly-quoted figure and
   attribution.

This is exactly the "fetch it yourself before citing it" discipline `case-research`'s own procedure
calls for; the first pass had leaned on search-summary text for three figures without a direct fetch
confirming each one, and P6 caught all three.

## Tier 2 P1/P2 (cold-solve / both-sides) corrections — 2026-09-18

Two independently dispatched fresh subagents (P1 cold-solve, P2 both-sides-solve), working only from
the case packet with no shared context, both computed the pier footing's formwork cost using only the
four triangular *lateral* faces' area rather than the pyramid's full total surface area (base + lateral)
— reasoning, unprompted, that a real footing's base sits against undisturbed soil in the excavation and
needs no formwork. This is a better real-world reading than the original draft's literal "total surface
area (for formwork cost)" wording, and both subagents reaching it independently is itself evidence it is
the more natural interpretation. Adopted as the case's official model: Challenge D4 now asks for both the
full total surface area (the complete, standard pyramid-surface-area computation) and the lateral-only
figure (the one actually used for formwork cost), with the real-world reasoning stated in Appendix E.
This changed the base-case margin from 12.78% to the case's final **14.85%** (winner unchanged: Sable
Hollow, still comfortably inside the 20% cap).

## Tier 2 P4 (twist-integrity) finding — MA5 added — 2026-09-18

An adversarial P4 review found that the case's Twist (an insurer-mandated uniform wind rating) flips the
recommendation entirely on the strength of treating Appendix A's 77% "Photometric + Clear" figure as
comparable to Appendix B's 70% "Clear" figure — a comparison the case's own Appendix A/B notes already
flagged as imperfect, but which had never been promoted to a formally documented Modeling Assumption
with its own sensitivity note, unlike MA1-MA4. Added **MA5** to Appendix G documenting this explicitly,
with a sensitivity note distinguishing its secondary role in the base case from its fully determinative
role once the twist is in play. `FACILITATOR.md`'s Twist section now points the guide to MA5 directly.

## Verification sweep (post-correction)

```
placeholders remaining: 0
citation markers with no source row: none
source rows never cited in text: none
LOW-confidence sources (must not be load-bearing): none
```

All nine sources (S1, S3–S9) are MEDIUM or HIGH confidence; none are LOW. The two most load-bearing
figures for the balance test — Appendix A/B's clear-sky fractions and Appendix D's wind-speed-driven
reinforcement factor — are HIGH (S1, S5) and a disclosed Modeling Assumption (MA2) respectively, not
LOW-confidence figures. Every source URL was directly fetched and its exact stated figure quoted (not
paraphrased from a search summary) as of 2026-09-18. Full margin arithmetic and the sensitivity sweep
are in `case.json.balance`, `case.json.sensitivity_disclosure`, and `sensitivity_model.py`.

Next step: `case-readiness` Tier 2 human-in-the-loop adjudication (P1–P4, P7) on `the-clear-sky-dome`.
