# Research Log — The Custom Die

`case-research`, 2026-09-05. This case was authored with one real, load-bearing figure needed
(the raw cardboard material price) and three figures identified up front as needing a stated
Modeling Assumption, because the concept itself is about a single company's private die quotes and
internal demand forecast — neither of which is ever a published figure.

## P01 — Corrugated cardboard price, per square inch

**Need:** a real, dated price for the single-wall corrugated stock both box options are cut from,
so Appendix D's material cost is not invented.

- Searched: `corrugated cardboard sheet cost per square foot 2026 custom box supplier price` —
  returned mostly low-quality aggregator/blog pages (polyflute.com, suneco.net, lansbox.com) citing
  a wide, inconsistent $0.18–$0.38/sq ft range with no primary attribution for any single figure.
  **Rejected as load-bearing** — no named, dated, checkable primary source behind any of these
  pages; this matches the SPEC section 5 "contested figure" pattern.
- Searched again: `Uline corrugated sheets price list per sheet 200 lb test` — surfaced Uline's own
  product catalog for corrugated pads. Fetched product S-15058 (24 in x 36 in, 200 lb test,
  white/kraft, single-wall) directly: **$2.24 per pad**, sold in 50-pad bundles.
- **Outcome: SOURCED**, confidence **HIGH** (a primary retailer's own current, dated-by-access
  price for a real, specified product — species/grade, dimensions, and basis weight all
  unambiguous). This is flat corrugated pad stock rather than a die-cut box shipped from a
  packaging converter, so it is a proxy for "raw single-wall corrugated material," not a
  converter's finished-box price — noted in `case.json.sources[].note`. Since both options are cut
  from the identical raw stock, this proxy affects both sides of the comparison identically and
  does not bias the verdict either direction.
- Recorded as **S1** in `case.json.sources[]`, cited in Appendix D. Derived: $2.24 / 864 sq in =
  $0.0025926/sq in, shown as the derivation in-document per the case-research skill's own rule that
  derived figures show their arithmetic.

## MA1 / MA2 — Steel-rule die cost, simple vs. complex net

**Need:** a one-time tooling cost for (a) a simple 6-panel rectangular box die and (b) a more
complex triangular-prism die with angled panels.

- Searched: `custom box steel rule die cost simple vs complex tooling packaging 2026` — returned
  several packaging-industry blog posts (customboxmakers.com, packagetheworld.com, gmsindustries.com)
  broadly agreeing that die cost scales with rule footage and design complexity, citing ranges from
  roughly $250 (simple structural dies) to $3,500 (complex, multi-piece, or heavily creased dies),
  with "most folding carton dies" cited around $800–$2,000 by one source. No two sources agreed on
  a specific number for a specific complexity level, and none disclosed a primary methodology
  (survey, industry index, or a named supplier's own published rate card).
- Followed up directly on a die-cutting supplier's own pricing page
  (customshapepros.com/custom-die-pricing) via a direct fetch, hoping for a real published rate
  schedule. **Outcome: the page names the same three qualitative cost drivers (die type/size, rule
  footage, complexity) but publishes no actual price table or numbers** — it routes every visitor
  to a custom quote form instead. (Note: an earlier automated search-summary attributed a specific
  $400–$3,500 range to a named "Paperboard Packaging Council 2024 survey"; the direct fetch of the
  cited page found no such attribution anywhere in its content, so that claim is NOT used anywhere
  in this case — treated as an unverifiable summarization artifact, not a real citation.)
- **Outcome: NOT FOUND (as a specific, defensible dollar figure for either complexity level) →
  Modeling Assumption.** This is exactly the SPEC section 5 "contested figure, poorly sourced,
  conflates categories" situation: real qualitative agreement (more rule footage and complexity
  cost more), but no single number defensible enough to cite as fact, and a specific company's die
  quote is not the kind of thing that is ever publicly indexed regardless. Exit taken: **stated
  Modeling Assumption** (exit 1 of the three allowed exits) for both MA1 ($450, the simple end of
  the researched range) and MA2 ($1,450, roughly a 3.2x multiplier consistent with the qualitative
  complexity pattern every source agreed on, without adopting any single source's specific number).
- The rejected, inconsistent blog range is **not** reproduced anywhere in `case.md` as if it were a
  citation — per SPEC section 5's contested-figure rule, the dispute and the range are named here in
  the research log, not laundered into the case.

## MA3 — Expected order volume for amortization

**Need:** how many units of The Wedge the bakery expects to ship before the next possible
re-tooling decision, since the die's one-time cost has to be spread across *some* volume for the
comparison to mean anything.

- This is not a figure that exists anywhere to search for — it is a single fictional bakery's own
  internal demand forecast for a single new product, tied to the concept's own stated growth
  narrative (40 local orders/week to 12,000 nationwide). No search was attempted; a genuine
  external search would return nothing relevant, and pretending otherwise would misrepresent the
  research process.
- **Outcome: Modeling Assumption by design**, not a NOT FOUND. Recorded as **MA3**: 12,000 units,
  with the stated basis that it represents roughly one week of the bakery's own current nationwide
  order volume — a plausible, disclosed forecast basis rather than an arbitrary number. Flagged as
  the single most load-bearing figure in the case for Tier 2 probe 5 (the crossover point where the
  two options tie sits well within the range this bakery could plausibly reach), and it is the
  figure the case's Twist directly revises.

## Summary

| Placeholder | Outcome | Confidence | Case location |
|---|---|---|---|
| Cardboard material price | SOURCED (S1) | HIGH | Appendix D |
| Simple-die cost (MA1) | ASSUMPTION | — | Appendix E |
| Complex-die cost (MA2) | ASSUMPTION | — | Appendix E |
| Order volume for amortization (MA3) | ASSUMPTION | — | Appendix E |

Zero placeholders remain `OPEN`. Zero figures were invented, rounded from a remembered number, or
laundered from a contested or unverifiable source (including the unverified "Paperboard Packaging
Council" attribution surfaced by an automated search summary and explicitly not used). Both product
and box dimensions in Appendices B/C are the case's own authored scenario design (a real,
fixed-shape product a bakery could plausibly bake), consistent with the Roofline Call / Vent Cap
precedent for an authored-design case where the geometry itself is the case's own creation.

Next step: run `case-readiness` on `the-custom-die`.

## Addendum — Tier 2 Probe 6 re-verification (2026-09-06)

`case-readiness` Tier 2 Probe 6 (data decay) re-fetched S1's live Uline product page
(https://www.uline.com/Product/Detail/S-15058/Corrugated-Pads/24-x-36-200-lb-Cardboard-Corrugated-Pads-White)
via a real browser fetch (the page's price is JS-rendered, so a bare `curl` did not surface it — a
rendered browser session was required). The page is reachable and the claimed figure's *structure*
still checks out (a "PRICE PER PAD" column, sold in bundle quantities starting at 50), but **the
actual number had moved**: the 50-pad-tier price is now **$2.37/pad**, not the $2.24/pad recorded
the day before (2026-09-05). This is a real, live retailer SKU price, not a fixed constant, and it
had genuinely changed within roughly 24 hours.

**Outcome: RE-SOURCED**, not treated as a dead link (the URL and the figure's basis are both still
good) but as exactly the "resolves but no longer carries the recorded figure" case Probe 6 exists
to catch, per `skills/case-readiness/SKILL.md`'s Probe 6 section ("worse [than a 404], because
nothing else in the pipeline would ever notice"). Updated `case.json.sources[].value/units/accessed`,
Appendix D and Appendix F in `case.md`, and every downstream `sensitivity_model.py` and
`case.json.derived[]` figure that depends on the cardboard price. The verdict does not flip
(Option A still wins the base case, Option B still wins the twist) — only the margins move
slightly: base 7.65% → 6.39%, twist 12.01% → 12.54%, crossover 17,183 → 16,230 units. No
modeling assumption changed; only the one real sourced figure did.
