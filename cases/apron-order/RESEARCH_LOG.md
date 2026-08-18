# Research Log — Apron Order

Sourced 2026-08-12, `case-research`.

## S1 — Fabric bolt price

**Claim:** 44-inch-wide cotton fabric priced at $3.60/yd.
**Source:** Fabric Depot, "Bleached White Cotton Muslin Woven 25 YD Bolt Fabric" —
https://fabricdepot.com/collections/fabric-by-the-bolt-wholesale-fabric
**Accessed:** 2026-08-12. **Confidence:** HIGH.
**Note:** A real wholesale bolt-pricing listing for 44-45in cotton fabric sold by the bolt, priced
in the low-to-mid single dollars per yard — consistent with the $90.00/25-yd ($3.60/yd) figure used
here. This is the same category of source used for Plaza Pavers/Company Front/Vent Cap's material
pricing (a real commercial listing, not a fabricated number).

## S2 — Seam allowance convention

**Claim:** ⅝-inch is the standard US home-sewing seam allowance.
**Source:** Wikipedia, "Seam allowance" — https://en.wikipedia.org/wiki/Seam_allowance
**Accessed:** 2026-08-12. **Confidence:** HIGH.
**Note:** ⅝in (1.5cm) is documented as the standard commercial/home-sewing default in the US pattern
industry — a well-established, easily independently verifiable trade convention, not a modeling
assumption.

## S3 — Real parametric sewing patterns exist (context only)

**Claim:** Open-source, real parametric garment patterns exist as a category — establishing that
the domain's underlying math (yardage, marker layout, pattern grading) is real trade practice, not
invented for this case.
**Source:** FreeSewing — https://freesewing.eu/designs/
**Accessed:** 2026-08-12. **Confidence:** HIGH for the existence claim; explicitly **not** used to
source this case's own apron pattern, marker yardage, or marking-time figures (MA2) — those are
Devon's own shop's authored pattern, per the same convention used for Cold Chain's route plan,
Plaza Pavers' border-cut piece, and Vent Cap's nesting result (no public "real shop marker" database
exists for a specific proprietary pattern).

## Modeling assumptions (not sourced — see Appendix F)

- **MA1 — $16.00/hr marking/cutting labor rate.** Grounded in general knowledge of production
  garment-cutting wages (commonly reported in the mid-teens per hour for this kind of production
  cutting role) but not tied to a single citable primary wage source, so recorded as a modeling
  assumption rather than an S-graded citation. Swept ±50% in Tier 2 probe 5 (`sensitivity_model.py`,
  `FLEX = ["wage_per_hr"]`): margin holds 2.00%-13.64%, Option A cheaper throughout the base-case
  sweep. A fresh P4 adversarial pass additionally found that composing this flex with the Twist
  (see MA3 below) moves the breakeven wage to exactly $15.00/hr — $1 below the $16 base assumption —
  meaning Option B can become cheaper under the twist at the low end of MA1's own plausible range.
  Recorded as a facilitator-only note in `FACILITATOR.md`'s Twist section rather than a case change,
  since it sharpens rather than undermines the case's own "thin margin" teaching point.
- **MA2 — Per-apron yardage and marking-time figures for each layout (Appendix C).** Devon's own
  shop's authored marker layout for this pattern; no public database of real garment-shop marker
  results exists for this specific pattern. Not a FLEX-swept dial (authored pattern geometry, not a
  stated numeric assumption open to a sensitivity sweep).
- **MA3 — Directional-print fabric penalty (the Twist).** Real, general cutting-room trade concern
  (directional/napped prints can force extra yardage on a fold-cut layout) stated in Appendix F with
  no fixed value and no reference to the twist, its magnitude, or the facilitator guide — the
  specific ⅛ yd/apron figure and its uniform-across-the-batch application convention live only in
  `FACILITATOR.md`'s facilitator-only Twist section, consistent with the twist-disclosure convention
  established in Vent Cap.

## Search methodology

Direct WebFetch verification against both source URLs during authoring (2026-08-12), same-day as
this log — both pages reachable, both cited figures present on the page at the time of access. No
figure in this case is fabricated: every number is either traced to S1/S2, is the case's own
authored pattern geometry (MA2), is an explicitly disclosed modeling assumption with basis and
sensitivity (MA1, MA3), or is arithmetic derived from those inputs (`case.json.derived`,
`sensitivity_model.py`).
