# Research Log — bioreactor-bid

33 `{{NEEDS_SOURCE}}` placeholders were opened by case-write. This log records what was searched,
what was found, what was rejected, and why — grouped by topic since most placeholders cluster into
a handful of underlying quantities.

## 1. Column Bid vessel geometry (nominal capacity, internal diameter, straight-side height) — SOURCED [S1]

Searched: "Sartorius BIOSTAT B stirred tank bioreactor vessel specifications working volume
diameter height" (found only bench-scale Univessel SU/Glass vessels, 1–10 L — too small for a
"production run" scaled up from a pilot suite) and "Cytiva Xcellerex XDR-50 wave rocking
bioreactor bag specifications nominal volume" (found the XDR *stirred-tank* line, not the wave
product — useful anyway since it's a real production-scale stirred tank).

Fetched the primary Cytiva datasheet PDF (`digi-23694-pdf`) directly. Table 1 gives XDR-50: max
working volume 50 L, min working volume 25 L, aspect ratio (H/D) 2.25:1 — but not a raw internal
diameter/height in cm. Derived diameter and height from the volume formula and the published
ratio (shown in-document in Appendix B). Confidence: HIGH for capacity (direct), MEDIUM for
diameter/height (a derivation from a published ratio, not a directly stated dimension).

## 2. Column Bid purchase cost — SOURCED [S2], MEDIUM

Checked Cytiva's and Sartorius's own eShop pages for a list price first (tier 1). Both required
login or a quote ("Login for price" / "Request a Quote") — confirmed no public new-unit price
exists, consistent with the skill's worked-example precedent for paywalled/quote-gated pricing.

Fell back to tier 3 (resale marketplace): searched used-equipment listings for the same product
(XDR-50) and found real, dated asking prices — $28,864 (REUZEit), $36,099 and $40,000 (other
REUZEit listings), consistent with a $27,990 Sartorius Biostat STR 50L listing on LabX. Used the
lowest/most specific listing with a resolvable product URL ($28,864, REUZEit). Graded MEDIUM: a
real, dated, public price, but a used-equipment asking price is a proxy for new-unit purchase
cost, not the thing itself.

## 3. Column Bid validation cost — NOT FOUND → Modeling Assumption [MA1]

Searched "single-use bioreactor validation cost benchmark CDMO facility qualification cost per
vessel." Found only qualitative discussion (Lab Manager TCO article, BioPharm International
qualification best-practices article) — no per-vessel dollar figure. BioPlan Associates' 22nd
Annual Report almost certainly tracks this, but its content is subscription-gated beyond the
table of contents. **Exit: Modeling Assumption** ($15,000), because a redesign that removes the
need for a validation-cost figure would also remove the yield-per-dollar metric the whole case is
built on, and dropping it isn't viable since Appendix D explicitly promises to anchor cost figures
to industry benchmarking. Documented with sensitivity in the Modeling Assumptions block.

## 4. Wave Bid vessel nominal capacity — SOURCED [S3]

Fetched the Sartorius Biostat RM datasheet PDF directly (all 8 pages read). The Flexsafe RM bag
family (page 6, ordering table) is offered in 1, 2, 10, 20, 50, 100, 200 L. Picked 50 L to match
the Column Bid's scale, so the yield-per-dollar comparison in D4 is apples-to-apples rather than
comparing a 50 L stirred tank to, say, a 200 L bag. HIGH confidence — this is a direct,
primary-source, dated (Feb 2026) figure.

## 5. Wave Bid purchase cost — SOURCED [S4], MEDIUM

Same paywall pattern as the Column Bid: Sartorius eShop shows "Request a Quote" for the Biostat RM
system, no public new-unit price. Searched used-equipment listings and found a real range
($4,500–$29,995 across six listings) for the Biostat RM 20/50 rocker + control tower. Picked the
$8,000 EquipNet listing (specific, resolvable URL). Noted explicitly that this is the *capital
rocker system* price and does not include the recurring per-batch Flexsafe bag consumable cost —
that's a real limitation of the figure, stated as a caveat rather than smoothed over.

## 6. Wave Bid validation cost — NOT FOUND → Modeling Assumption [MA2]

Same search as item 3; no quantitative benchmark found for single-use/wave systems specifically.
Used the qualitative finding (single-use systems reduce CIP/SIP validation burden) as directional
basis for setting MA2 below MA1, while being explicit that the dollar value itself is not sourced.

## 7. Wave Bid bag cross-sectional radius profile r(h) — NOT FOUND → Modeling Assumption [MA7]

Searched "Sartorius BIOSTAT RM rocking bioreactor bag specifications working volume cross section"
and "Sartorius Flexsafe RM bags datasheet schematic drawing dimensions length width filled."
Fetched the primary Biostat RM datasheet PDF directly and read every page — it gives bag *volume*
sizes and system dimensions, never a radius-vs-fill-height function. The datasheet itself says
"customized bag designs can be requested via engineered to order (ETO) process," confirming this
geometry is proprietary/made-to-order, not published for any standard configuration.

**Exit: Modeling Assumption**, not redesign, because there is no way to redesign around this
figure without eliminating the disk-method-integral challenge entirely (D2's core teaching point).
This is exactly the kind of assumption the skill calls "a feature, not a bug" — the case now says
so explicitly and gives the sensitivity band (this is the single most load-bearing assumption in
the case; see MA7 in case.md).

## 8. Appendix D — CDMO industry cost-benchmark survey name — SOURCED [S6]

Searched "BioPlan Associates annual report biomanufacturing benchmarking survey 2025 2026."
Confirmed the real, current, named report: *22nd Annual Report and Survey of Biopharmaceutical
Manufacturing Capacity and Production*, published April 2025, on the publisher's own page. HIGH
confidence for the name/date citation. Explicitly noted in Appendix D that the report's own dollar
tables are not the source of MA1/MA2's figures (those remain paywalled) — the survey name anchors
the *category* of figure, not the specific numbers, exactly as Appendix D's own lead-in text
promises.

## 9. Batch duration, client minimum yield, CRO budget cap — NOT FOUND → Modeling Assumptions [MA3, MA4, MA5]

These are contract-specific terms for a fictional client and a fictional CRO program; by
definition no public document reports them. Ran one confirming search each to document a genuine
attempt rather than assume unsourceability: "typical fed-batch mammalian cell culture production
run duration days mAb bioprocess" (found real industry range, 10–14 days, cited as [S7] and used
as the *basis* note for MA3, not as the value itself — Appendix A's pre-existing 6-row table
structure, days 0–5, forces the value to 5) and "typical minimum batch lot size liters monoclonal
antibody production contract manufacturing client requirement" (found only generic scale
categories — clinical 200–1,000 L, commercial 5,000+ L — wildly inconsistent with this case's 50 L
pilot-suite scale, confirming no useful public anchor exists at this scale).

Chose values deliberately to make the constraints load-bearing rather than decorative:
- MA4 (25 L minimum yield) sits between the two vessels' computed working-volume yields (Wave
  17.29 L, Column 37.5 L), so it actually disqualifies one option — see the Sensitivity column in
  case.md's Modeling Assumptions block for the full flip analysis.
- MA5 ($50,000 budget cap) sits above both total costs so it is not the binding constraint at the
  chosen value, keeping the dilemma centered on the yield floor and yield-per-dollar rather than
  raw affordability.

## 10. Appendix A feed-rate/uptake-rate table and conversion factor — NOT FOUND → Modeling Assumption [MA6]

Searched "CHO cell fed-batch culture published glucose feed rate lactate uptake rate g/L/day day 0
day 5" and "CHO cell fed-batch culture daily glucose consumption rate table day-by-day published
data study." Real published data exists (e.g., a 2017 metabolic-characterization paper on CHO
fed-batch phases), but only in cell-count-normalized or cell-volume-normalized units (µmol · 10⁶
cells⁻¹ · day⁻¹), never in g/L/day. Converting those units to g/L/day would require additional
unsourced assumptions (cell density, cell volume) — which would just relocate the fabrication
problem rather than solve it. **Exit: Modeling Assumption**, shaped like the qualitative pattern
of real Monod-style kinetics (feed roughly steady, uptake rising to meet it) but not claiming
citation to a specific published curve. The product-mass-to-volume conversion factor (0.05 L/g)
is likewise a stated assumption — no public source reports this unit for any real product.

## Structural flag for case-write (not corrected here)

`case.json`'s `balance.argument_b` describes the Wave Bid as achieving a *higher* net cumulative
yield per liter of working volume than the Column Bid (better mixing → larger area between the
feed/uptake curves). But `case.md`'s Background and Appendix A explicitly state the growth-kinetics
curves are shared and apply identically to either vessel once its working volume is known. These
two are in tension: as drafted, both vessels get the same per-liter net yield, and the entire
competitive difference comes from working-volume geometry and cost, not kinetics. I did not
resolve this by giving the two vessels different curves, since that would mean editing the
Background/Appendix A structure that belongs to case-write. Flagging it here for case-write's
attention; the case still produces a genuine, non-obvious dilemma under the shared-curve reading
(see MA4's sensitivity note), so this is not blocking, but the balance narrative in case.json
should be reconciled to what case.md actually says.

## Verification (skill step 7)

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources (must not be load-bearing): []
needs_source status counts: ASSUMPTION 27, SOURCED 8 (of 35 tokens — some tokens map many-to-one
  to a single source, e.g. all 12 feed/uptake-rate cells → MA6)
case.json status: researched
```
