# RESEARCH_LOG.md — Deluge Gun

One row per placeholder from `case-write`'s output (41 `{{NEEDS_SOURCE}}` tokens across 21
distinct facts, several repeated across Appendix D's cross-reference table and Appendix G's
table-cell-by-cell placeholders). Grouped by fact, not by raw token count, since most tokens are
the same fact referenced from more than one place.

## Fact 1 — Collapse zone standoff distance as a multiple of building height

**Searched:** "NIOSH firefighter collapse zone rule 1.5 times building height"; then fetched
NIOSH's own document directly.

**Found:** NIOSH's own PDF/HTML (`cdc.gov/niosh/docs/wp-solutions/2014-120/...`) returned HTTP 403
to the fetch tool on every attempt (both the PDF and the HTML landing page) — CDC appears to block
automated fetches. Fell back to a tier-2/3 trade-press source that names the same figure and cites
NIOSH's broader collapse-zone-establishment guidance: Christopher J. Naum, "Establishing Collapse
Zones At Building Fires," *Firehouse*, 2015-04-01. Fetched directly and confirmed the exact quote:
"This area is often defined by establishing a perimeter at a distance from the building that is
equal to 1.5 times the height of the structure."

**Outcome:** SOURCED as **S1** (HIGH — specific, quoted, dated, from an established fire-service
trade publication; widely repeated practice, no single formal code citation found for this exact
multiplier, which is the one honest caveat). **S2** records NIOSH's own document as supporting,
general context (MEDIUM — real, on-topic, but unquotable due to the 403).

## Fact 2 — Smoothbore discharge formula and standard operating pressure

**Searched:** "fire stream nozzle velocity formula 12.14 square root nozzle pressure"; then
"smoothbore master stream nozzle standard operating pressure 80 psi deck gun monitor."

**Found:** The "12.14" constant (a commonly-taught *velocity* shortcut) could not be traced to a
specific citable document — dropped rather than used. Found and fetched a strong direct
alternative: Joseph R. Polenzani, "Deck Guns: Know Your Flow," *Fire Engineering*, 2019-10-01,
which gives the real "Freeman Formula," $GPM = 29.71 d^2\sqrt{NP}$, and states "the standard
pressure is 80 psi" for master-stream nozzles.

**Outcome:** SOURCED as **S3** (HIGH). This let the case derive exit velocity from first
principles (continuity equation, $v=Q/A$) instead of relying on the unsourceable 12.14 constant —
a better outcome than the original plan, and it is now shown as the case's own derivation
(marked `derived: true` in spirit, explicitly labeled "not itself a directly published figure" in
Appendix C) rather than presented as if independently published.

## Fact 3 — Rated GPM for a specific smoothbore tip at 80 psi

**Searched:** direct follow-up on the deck-gun search results, then fetched Paul Shapiro, "Fixed
Master Stream Operations Using Smooth Bore Tips," *Fire Engineering*, 2011-06-24.

**Found:** A published stacked-tip table giving "1 3/8-inch  502 gpm" at 80 psi — matches (within
0.4%) the independently-derived Freeman-formula calculation for the same tip and pressure, and
also matches (within 0.4%) the real monitor's own 500 GPM rating (S6, below). Three independent
real sources converge on the same number — strong confidence.

**Outcome:** SOURCED as **S4** (HIGH). Tip diameter (1-3/8 in) is now itself a real, published
standard size rather than an arbitrary choice.

## Fact 4 — A real portable monitor with an elevation range wide enough for both solved angles

**Searched:** "portable master stream monitor elevation range degrees spec sheet Task Force Tips
Akron Brass," then fetched two Task Force Tips BlitzFire product pages directly.

**Found:** Standard BlitzFire portable monitors cap at 46° elevation — too low for this case's
solved High Arc angle (~70.8°). The **High Elevation (HE)** variant, model XX232A-HE, is real,
currently sold, and rated 10°–86° elevation, 500 GPM max flow — fetched and quoted directly from
`tft.com/product/xx232a-he/`.

**Outcome:** SOURCED as **S6** (HIGH). This was a genuine research finding, not a foregone
conclusion: if no real monitor's elevation range had covered both solved angles, the case would
have needed a redesign (a different assumed structure height, changing $R$ and therefore both
angles) to stay physically realizable by real equipment. It didn't need one — the HE BlitzFire's
real 10°–86° range comfortably covers ~19.2° and ~70.8°.

## Fact 5 — The projectile range formula and the complementary-angle fact

**Searched:** "OpenStax University Physics projectile motion range equation," then fetched the
specific section directly.

**Found:** OpenStax, *University Physics Volume 1*, §4.3, Equation 4.26: $R=v_0^2\sin(2\theta_0)/g$,
with the text explicitly stating: "It is interesting that the same range is found for two initial
launch angles that sum to 90°," backed by a worked 15°/75° example. This is the exact mathematical
fact the case's dilemma is built on, confirmed in a free, primary, open-license physics textbook.

**Outcome:** SOURCED as **S5** (HIGH).

## Fact 6 — Structure height for the scenario (MA1)

**Searched:** Not applicable — this is intentionally a fictional scenario detail (no real address
or incident to cite), like Ridgeview Fire Department itself.

**Outcome:** Declared as **MA1**, a stated Modeling Assumption (150 ft, a plausible height for a
mixed-use commercial mid-/high-rise), in the visible Modeling Assumptions block, not buried in a
table as though sourced. The real rule applied to that height (S1's 1.5×) is cited; the height
itself is not.

## Fact 7 — Wind-drift loss rate per second of flight (MA2)

**Searched:** Attempted "fire stream wind drift loss rate percent per second master stream" and
variants; found only qualitative statements (wind reduces reach/effectiveness of elevated
streams) in fire-hydraulics discussion, never a specific, citable numeric loss-rate-per-second for
a continuous master stream.

**Outcome:** Returned **NOT FOUND** for a specific numeric rate. Declared as **MA2**, a stated
Modeling Assumption (2% of rated flow lost per second of flight), explicitly flagged in the
Modeling Assumptions block as the case's single most load-bearing assumption, with a sensitivity
note (not a result) pointing a Hero at exactly this number if they want to argue for a different
answer. This is precisely the "exit 1: stated Modeling Assumption" path in `case-research`
SKILL.md §5, chosen over redesign because the qualitative wind-loss phenomenon is real and
central to the case's dilemma, and over dropping because it is the deliverable D4 exists to force.

## Verification pass

- `{{NEEDS_SOURCE}}` tokens remaining in case.md: **0** (started at 41).
- Every `[S1]`–`[S6]` citation marker in case.md has a matching `sources[]` row in case.json, and
  every `sources[]` row is cited at least once in case.md.
- No LOW-confidence source is load-bearing (none exist in this case — all six landed HIGH or
  MEDIUM).
- All arithmetic (exit velocity, both solved angles, apex heights, times of flight, effective GPM,
  margin) independently re-derived from the four hard inputs ($R$, $v$, $g$, $Q$) and the two
  Modeling Assumptions; matches the values recorded in `case.json.balance.computed_values` to
  within rounding.
- `case.json.status` → `"researched"`.

**Next step:** Run case-readiness on `deluge-gun` (Tier 1 structural checks, then the six Tier 2
probes).
