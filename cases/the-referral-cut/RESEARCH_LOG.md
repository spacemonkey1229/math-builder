# Research Log — The Referral Cut

Stage 3 (`case-research`) run on `cases/the-referral-cut/`. 3 `{{NEEDS_SOURCE}}` placeholders
enumerated from `case.md`. Worked in load-bearing order: Appendix B's referral fee first (drives
both options' post-referral proceeds), then Appendix C's base FBA fulfillment fee, then Appendix
C's fuel-and-logistics surcharge.

## P01 — Amazon referral fee, Home & Kitchen category (Appendix B)

**Searched:** "Amazon referral fee percentage Home category 2026 seller central fee schedule."

**Fetched directly:** `https://sell.amazon.com/pricing` — Amazon's own public seller-pricing page
states directly: Home and Kitchen referral fee is 15%, with a $0.30 minimum per item.
Cross-checked against `feedvisor.com/university/referral-fee/`, `eightx.co`, and `fbalytic.com`'s
2026 referral-fee guides, all independently reporting the identical 15% figure for this category
with no disagreement, and all noting Amazon froze referral fees (no change) for 2025 and 2026.

**Outcome:** SOURCED as [S1], value 15% (+ $0.30 minimum), HIGH confidence — a direct fetch of
Amazon's own public pricing page, corroborated by every independent secondary source checked. At
this case's $18-3/4 list price, 15% ($2.8125) is well above the $0.30 minimum, so the minimum
never binds and plays no further role in this case's arithmetic.

## P02 — Base FBA per-unit fulfillment fee, small standard-size, 8-10 oz, $10-$50 band (Appendix C)

**Searched:** "Amazon FBA fulfillment fee schedule 2026 standard size small item per unit,"
"2026 US FBA fulfillment fee changes."

**Attempted direct fetches of Amazon's own pages** (all gated behind Seller Central login, no fee
table returned):
- `https://sell.amazon.com/fulfillment-by-amazon/pricing` — HTTP 404.
- `https://sell.amazon.com/blog/fba-fees-guide` — overview only, directs to "the FBA costs help
  page" and the Revenue Calculator tool, no dollar table.
- `https://sellercentral.amazon.com/help/hub/reference/external/G201411300` — redirected to a
  login/homepage shell.
- `https://sellercentral.amazon.com/help/hub/reference/external/GABBX6GZPA8MSZGW` (linked
  directly from Amazon's own 2026 fee-update forum post as "2026 US FBA fulfillment fee changes")
  — also redirected to a login/homepage shell, no fee table content returned.
- `https://sellingpartners.aboutamazon.com/update-to-u-s-referral-and-fulfillment-by-amazon-fees-for-2026`
  (Amazon's own Selling Partners corporate blog) — confirms the 2026 fee-update program exists and
  states an average $0.08/unit increase, but explicitly defers the actual per-item table to the
  gated Seller Central link above rather than publishing it on the page itself.

**Fetched two independent secondary reconstructions of the gated table:**
- `https://www.goatconsulting.com/amazon-fulfillment/amazon-fba-fee-changes-for-2026` — a detailed,
  dated (effective 2026-01-15 through the October 2026 non-peak period) multi-tier table. For the
  8-10 oz weight tier in the $10-$50 price band: **$3.68**. The article explicitly directs readers
  to Seller Central's own Fee Preview as "the official source of truth," and its adjacent-tier
  values step up in a pattern ($2.77 under $10 → $3.68 at $10-$50 → $3.94 over $50; 10-12 oz:
  $2.82 → $3.78 → $4.04) consistent with Amazon's known tiering structure.
- `https://amzprep.com/amazon-fba-fees/` — reports **$3.48** for the identical weight tier and
  price band, a real, disclosed discrepancy of $0.20 between two independent secondary
  reconstructions of a table neither could fetch primary.

**Outcome:** The exact authoritative figure is genuinely gated behind Amazon's own Seller Central
login — confirmed by three separate direct-fetch attempts against Amazon's own domains, and by
Goat Consulting's own text explicitly naming Seller Central's Fee Preview as the place to verify.
**SOURCED as [S2]**, value $3.68 (Goat Consulting's fuller, internally-consistent multi-tier
table), **MEDIUM confidence** per this skill's own criterion for a secondary source with a
disclosed range (here, disagreement between two independent secondary readings rather than one
source's stated range) — matching the treatment `cases/the-special-order`'s S4 gave a
forum-synthesized rate. The $3.48 figure is disclosed here and in `case.json.sources[S2].note`
rather than silently discarded.

## P03 — Fuel-and-logistics surcharge on FBA fulfillment fees (Appendix C)

**Searched:** same searches as P02 surfaced this figure directly and consistently.

**Fetched directly:** `https://sellingpartners.aboutamazon.com/update-to-u-s-referral-and-fulfillment-by-amazon-fees-for-2026`
(Amazon's own corporate Selling Partners blog) confirms the 2026 fee-update program. The specific
3.5% figure and April 17, 2026 effective date are corroborated identically — with no numeric
disagreement found anywhere — across Goat Consulting, AMZ Prep, Sellersnap, JayGroup, and
MapMyChannel's independent 2026 fee-change summaries. AMZ Prep's article states the mechanism
explicitly: "a product with a $5 fulfillment charge would incur an additional $0.18 per unit"
($5 x 0.035 = $0.175, rounding to $0.18 — confirms multiplicative, not additive, application).

**Outcome:** SOURCED as [S3], value 3.5% (applied to the fulfillment fee, not to item price),
**HIGH confidence** — although Amazon's own most detailed page is behind the same Seller Central
login gate as P02, every independent secondary source checked agrees on both the percentage and
the effective date with zero disagreement, unlike P02's conflicting dollar figures.

## Verification pass

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources: []
```

All 3 placeholders resolved: 3 SOURCED (S1-S3), 0 Modeling Assumptions needed — matching the
project instruction that no assumption should be required for the core fee figures. Two of three
(S1, S3) are HIGH confidence; S2 is MEDIUM because Amazon's own authoritative per-item dollar
table sits behind a Seller Central login wall that could not be crossed, and two independent
secondary reconstructions of that table disagree by $0.20 for the identical tier — disclosed
rather than silently resolved in either source's favor. No figure was invented, rounded from
memory, or presented as sourced without a fetched, checkable URL.

## Author-owned figures (not sourced, not needing external citation)

Per `case-write`'s own convention (matching `cases/the-special-order`'s treatment of its cut-list
widths), the following are Amber & Oak's own business data — the fictional shop's operational
choices, not claims about a real, externally-verifiable entity — and were fixed at `case-write`
time, then retuned once to land the balance margin inside the approved concept's 8-15% band:
list price ($18-3/4), packaging/postage cost ($3-1/8, retuned from an initial $2-3/8 once S1-S3
landed — see below), production cost ($6-1/2), guaranteed monthly order quantity (40 units), weeks
of inventory held per option (6-1/2 / 2-1/4), and weekly production cost ($340-3/8).

**Retuning note:** the first pass (packaging cost $2-3/8) produced a 17.06% margin, above the
20% SPEC §2 unbalance ceiling only marginally but above the concept's stated 8-15% target band.
Per pipeline doctrine ("Margin > 20% — unbalanced... retune a constraint. Never fix a margin by
hiding data"), and by extension applied here to stay inside the *concept's* tighter target band
rather than only SPEC's outer ceiling, the packaging/postage cost (an author-owned constraint, not
a sourced figure) was retuned to $3-1/8, landing the margin at a genuine, computed **10.83%**, with
Option A (FBM) winning under the current sourced figures. No sourced Amazon fee figure was altered
to hit this band.

## Tier 2 Probe 6 (data decay) correction — 2026-09-09

A live re-fetch of all three cited URLs during `case-readiness`'s Tier 2 P6 check found S1 and S2
reachable with their recorded values still present verbatim. **S3 was imprecisely cited**: the
original source, Amazon's own Selling Partners corporate blog
(`sellingpartners.aboutamazon.com/update-to-u-s-referral-and-fulfillment-by-amazon-fees-for-2026`),
confirms the 2026 fee-update program exists in general terms but does **not** itself state the
3.5% figure, the April 17, 2026 effective date, or the "calculated on fulfillment fees, not sale
price" mechanism anywhere on the page — attributing this specific number to that exact URL
overstated what the page actually carries. **Corrected**: re-sourced to Digital Commerce 360's
April 3, 2026 report (`digitalcommerce360.com/2026/04/03/amazon-to-add-fuel-and-logistics-surcharges/`),
which explicitly quotes Amazon's own Seller Central announcement for all three details. Confidence
downgraded from HIGH to MEDIUM (reputable trade-press journalism citing a named tier-1 source, per
this skill's own tier-3 criterion, rather than a direct fetch of Amazon's own primary page).
Cross-corroborated with identical figures from CNBC, WeAreUncapped, DCL Logistics, and Novadata's
independent 2026 coverage — no numeric disagreement found anywhere on the percentage, date, or
fee-not-price mechanism. Updated in `case.json.sources[S3]` and `case.md` Appendix E.

Next step: `Run case-readiness on the-referral-cut.`
