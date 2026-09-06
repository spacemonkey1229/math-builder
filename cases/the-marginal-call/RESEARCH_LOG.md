# Research Log — The Marginal Call

One row per `{{NEEDS_SOURCE}}` placeholder from `case-write`. 11 placeholders total.

---

### P01 — Appendix A: Fixed cost per kiln-drying run

**Searched:** "custom kiln drying lumber service cost per board foot sawmill"; fetched WoodWeb's
"Rates for sawmilling/kiln-drying" (dated June 2000 — too stale to use), Kitsap Dry Kiln's pricing
page, and Timms Sawmill's pricing guide.

**Found:** every real kiln-drying operator found prices **per board foot** (Kitsap: $0.59–$1.21/bf;
Timms: a small flat $6.00 processing fee, no material cost) or with **volume-discount percentages**
off a per-bf rate (Timms: 5%/10%/15% off at 1,000/2,000/4,000+ bf) — none publishes a separate flat
"run-booking" or "scheduling" fee of the kind this case needs as its fixed cost term.

**Disposition: ASSUMPTION (MA1).** No source exists for this specific line item at any confidence
grade. Set to $1,800 (a kiln-scheduling fee plus roughly a day of shop changeover/setup labor). See
`case.json.modeling_assumptions[MA1]`.

---

### P02 — Appendix A: Variable cost per board foot at standard capacity

**Searched:** "black walnut lumber price per board foot kiln dried 2026"; fetched
customwoodquote.com/wood-prices/ directly. Searched "'labor cost' per board foot furniture
manufacturing OR woodworking BLS wage furniture worker"; fetched bls.gov/ooh/production/woodworkers.htm
directly.

**Found:**
- Lumber: customwoodquote.com states surfaced (S2S/S4S) hardwood-dealer walnut runs $10–$18/bf as
  of early 2026 (page updated March 2026). **SOURCED [S1]**, midpoint $14.00/bf used.
- Kiln-drying: Kitsap Dry Kiln's own posted price page states $0.59–$1.21/bf for 1"–2" lumber
  (species-dependent), current as of access. **SOURCED [S2]**, midpoint $0.90/bf used.
- Labor: BLS OOH states Woodworkers' median wage is $21.79/hour (May 2025). **SOURCED [S3]**. No
  public per-board-foot labor-hour production-rate standard exists for furniture-grade walnut, so
  converting $21.79/hr into a $/bf figure required an assumed processing rate (~8.7 bf/hour →
  $2.50/bf). **Disposition for the rate itself: ASSUMPTION (MA2)**, layered on top of the sourced
  wage.

**Combined value used:** $14.00 + $0.90 + $2.50 = **$17.40/bf**, recorded as `derived: true` on
S1–S3 in `case.json.sources[]`.

---

### P03 — Appendix A: Overtime-labor cost coefficient

**Searched:** "overtime wage premium capacity-constrained marginal cost small manufacturer" (no
distinct search transcript beyond the general labor-cost searches above — no source publishes a
cost-scaling *coefficient* for any manufacturer, let alone furniture-specific).

**Found:** nothing publishes a numeric coefficient for how per-unit cost rises with batch size
beyond standard capacity for a small manufacturer. The only real, citable anchor is the *structural*
fact that federal law (FLSA) requires 1.5× pay for overtime hours — real and well documented, but
not itself a $/bf² coefficient.

**Disposition: ASSUMPTION (MA3).** Set to k = 0.0001 $/bf², a smooth continuous approximation
grounded in the FLSA 1.5× logic. See `case.json.modeling_assumptions[MA3]`.

---

### P04 — Appendix B: The Steady Order's board footage

**Searched:** not independently searchable — this is Renata's own shop's specific order-history
figure, not a publishable industry statistic.

**Disposition: ASSUMPTION (MA4).** Protagonist-specific, set to 2,000 bf.

---

### P05 — Appendix B: The Full Kiln's board footage

**Searched:** same kiln-drying-operator sources as P01/P02 (Kitsap, Timms, WoodWeb) checked for any
published "minimum batch for deep-discount run" figure. Timms's own volume-discount tiers exist
(1,000/2,000/4,000+ bf) but are this specific mill's real numbers, not the fictional mill Renata
uses, and no source publishes a "minimum for the LAST slot of the season" figure — that is
inherently protagonist- and scenario-specific.

**Disposition: ASSUMPTION (MA5).** Set to 3,000 bf. See `case.json.modeling_assumptions[MA5]` —
flagged as the case's single most load-bearing protagonist-specific figure.

---

### P06 — Appendix C: This quarter's sellable limit

**Searched:** not independently searchable — depends on the specific fictional hotel order's size
plus Renata's specific shop's existing account load, neither of which is a published statistic.

**Disposition: ASSUMPTION (MA6).** Set to 2,700 bf. Tier 2 P5 later confirmed this is the case's
dilemma-flipping dial (see `case.json.sensitivity_disclosure`).

---

### P07 — Appendix C: Carrying cost per unsold board foot

**Searched:** "inventory carrying cost rate percent of inventory value per year small manufacturer";
attempted to fetch apqc.org's benchmark page directly (HTTP 403, inaccessible); fetched
finaleinventory.com's carrying-cost guide (redirected, general 15–30% ranges, no manufacturing
breakout) and vndly.io's "20% Inventory Carrying Costs: 2026 Data" page directly.

**Found:** vndly.io states "about 20% of inventory cost per year" as a common benchmark, attributed
to AccountingTools, with "20% to 30% as a practical rule of thumb" attributed to Fit Small Business.
General inventory-management benchmark, not furniture- or hardwood-specific — no source was found
breaking this out by manufacturing sub-industry.

**Disposition: SOURCED [S4]**, MEDIUM confidence (general benchmark, not industry-specific).
Applied at one-quarter of the annual rate (5%/quarter) to match this case's one-quarter planning
horizon — that conversion is this case's own derivation, disclosed in the source note, not part of
the cited figure itself.

---

### P08 — Appendix D: Ship deadline

**Searched:** not applicable — this restates the Background's own narrative-fixed detail ("a firm
five-week ship date"), not an independently sourceable fact.

**Disposition: ASSUMPTION (MA7)**, matching the Background verbatim, per the same pattern as
`cases/the-breakeven-mile/case.md`'s MA3.

---

### P09 — Appendix D: Existing business line-of-credit / available headroom

**Searched:** "average small business line of credit limit typical amount 2026"; fetched multiple
aggregator pages (Bankrate, Lendio, LendingTree) via search summary — found general ranges
($10,000–$500,000 depending on lender and revenue) but nothing specific to a nine-person furniture
shop's actual credit-line balance, which is inherently protagonist-specific and not a publishable
fact regardless of search depth.

**Disposition: ASSUMPTION (MA8).** Set to $25,000 of available headroom (the line's total limit is
unstated; the shop's ongoing payroll/materials draw already uses part of it).

---

### P10 — Appendix D: Deposit percentage

**Searched:** "custom furniture manufacturer order deposit percentage upfront typical"; fetched
lukesfurniturecompany.com's deposit article directly.

**Found:** "50% upfront, 50% at delivery or completion" is called the custom-furniture industry
standard (dated 2026-05-18); 30/70 also cited as common. This describes a furniture **buyer's**
deposit to a furniture **maker** — not a mill's wholesale kiln-drying deposit terms, which no public
source publishes (confirmed by the same P01/P05 mill-pricing search: none of Kitsap, Timms, or
WoodWeb states a deposit-percentage policy).

**Disposition: SOURCED [S5]**, MEDIUM confidence, used as a disclosed proxy — the note on S5 in
`case.json.sources[]` states plainly that this is a buyer-to-maker norm applied by analogy to a
shop-to-mill relationship, not an exact match.

---

### P11 — Appendix D: Bank turnaround time

**Searched:** "bank line of credit increase approval time small business days"; fetched
crestmontcapital.com's business-loan-approval-time article directly.

**Found:** "Traditional banks and credit unions typically take 1 to 3 weeks" for business
line-of-credit approval, versus 1–5 business days for online lenders.

**Disposition: SOURCED [S6]**, MEDIUM confidence (industry-blog aggregation, not a regulator or
bank-association survey, but a specific, attributable, dated claim).

---

## Summary

| Placeholder | Status | Resolved by |
|---|---|---|
| P01 (fixed cost) | ASSUMPTION | MA1 |
| P02 (variable cost) | SOURCED (+ MA2 for labor-rate conversion) | S1, S2, S3 |
| P03 (overtime coefficient) | ASSUMPTION | MA3 |
| P04 (Steady Order bf) | ASSUMPTION | MA4 |
| P05 (Full Kiln bf) | ASSUMPTION | MA5 |
| P06 (sellable limit) | ASSUMPTION | MA6 |
| P07 (carrying cost) | SOURCED | S4 |
| P08 (ship deadline) | ASSUMPTION | MA7 |
| P09 (credit-line headroom) | ASSUMPTION | MA8 |
| P10 (deposit %) | SOURCED | S5 |
| P11 (bank turnaround) | SOURCED | S6 |

**0 remaining OPEN. 0 NOT FOUND left unresolved** — every placeholder is SOURCED or ASSUMPTION, per
SPEC §5. No redesign was needed: the case's core mechanism (average cost minimized by the quotient
rule, then penalized by a real carrying cost against a real sellable-demand ceiling) survives
entirely on the sourced lumber/kiln/wage/carrying-cost figures, with the protagonist-specific batch
sizes and demand ceiling — inherently unpublishable for a fictional shop — carried openly as
Modeling Assumptions.

Next step: `case-readiness` — Tier 1 structural checks, then Tier 2's six simulated-play probes.
