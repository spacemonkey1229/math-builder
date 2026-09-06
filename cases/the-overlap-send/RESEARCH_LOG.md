# Research Log — The Overlap Send

Stage 3 (`case-research`) run on `cases/the-overlap-send/`. 9 `{{NEEDS_SOURCE}}` placeholders
enumerated (P01–P09 below). Worked in load-bearing weight order: the broad-send conversion rate
first (the one figure with a real public benchmark report behind it, flagged HIGHEST priority at
write time), then the intersection-segment conversion rate and AOV, then the CRM list sizes, cost,
and budget (all confirmed as non-public, proprietary-shaped figures before searching, since no
company publishes its own internal list data).

## P06 — Broad-send (non-segmented) placed-order/conversion rate

**Searched:**
- "Klaviyo segmented email campaign conversion rate benchmark report 2025 2026"
- "Mailchimp average email marketing benchmarks by industry conversion click rate 2025"

**Fetched directly:**
- `https://www.klaviyo.com/products/email-marketing/benchmarks` — Klaviyo's own 2026 Email
  Marketing Benchmarks by Industry, aggregated from over 183,000 brands, published Feb 2026.
  Confirmed exact figures: campaign (broad broadcast) placed-order rate averages **0.16%** (top
  10%: 0.36%); automated flow (behavior-triggered) placed-order rate averages **2.11%** (top 10%:
  4.3%).

**Outcome:** SOURCED as [S1], HIGH confidence (primary publisher, own platform data, stated
methodology and sample size, dated, and the figure needed — a genuine purchase-conversion rate,
not a proxy metric like open/click rate). The 0.16% campaign figure is used directly as Appendix
C's broad-send (Option A) conversion rate. The 2.11% flow figure is **not** used directly for
Option B — flows are behavior-triggered automations (welcome series, abandoned cart, etc.), not a
static "customers in both lists" segment, so using it as-is would misrepresent what it measures.
It is cited only as one of three real inputs informing MA4's basis (see below).

## P07 — Intersection (multi-signal) segment conversion rate

**Searched:**
- "Mailchimp segmentation study 'segmented campaigns' click rate open rate increase percent"
- "HubSpot email segmentation benchmark conversion rate lift study"

**Fetched directly:**
- `https://mailchimp.com/resources/effects-of-list-segmentation-on-email-marketing-stats/` —
  Mailchimp's own segmentation study: ~2,000 accounts, ~11,000 segmented campaigns, ~9 million
  recipients. Confirmed: segmented campaigns show 14.31% higher opens, 100.95% higher clicks, lower
  bounces/complaints/unsubscribes than non-segmented campaigns. Confirmed the study does **not**
  measure conversion or purchase rate — engagement metrics only. Published/updated February 2017 —
  real and named-methodology, but old (9+ years as of this case).
- HubSpot's email-list-segmentation blog content (`blog.hubspot.com/marketing/email-list-segmentation`)
  states that a properly segmented send should outperform a broadcast send by "at least 20–30%,"
  framed as editorial guidance rather than a single controlled study with its own published dataset.

**Outcome:** Genuine search confirms **NOT FOUND** as a directly citable figure — no report
measures conversion rate for exactly "customers who are both a recent purchaser and a newsletter
subscriber." This two-list overlap segment is not a category any public benchmark tracks. **Exit
chosen: Modeling Assumption (MA4)**, value 0.60% (a 3.75x lift over the sourced 0.16% broad rate),
informed by three real cited findings (Klaviyo's own 13x flow/campaign gap at the high end,
HubSpot's 20–30% minimum-lift guidance at the low end, Mailchimp's +100.95% CTR study as
directional corroboration) without copying any of them directly — see `case.json.sources[S1-S3]`
and `modeling_assumptions[MA4]` for the full reasoning. Redesign (swapping the constraint) was
considered and rejected: the reach-vs-rate trade-off IS the reason this case exists per the
concept sheet, so removing the assumption would gut the case rather than repair it — same
reasoning `cases/the-deferred-repair` used for its own core unsourceable figure (MA1).

## P09 — Average order value (AOV)

**Searched:**
- "subscription box industry average order value AOV benchmark report"
- "Recharge State of Subscription Commerce report average order value benchmark"
- "Recharge subscription commerce report 2025 average order value AOV dollars"

**Found (initial pass):** WebSearch summaries attributed 2020 subscription-vertical AOV figures
($93 Beauty & Personal Care, $166 Health & Wellness) to Recharge's State of Subscription Commerce
data. Direct fetch of `https://getrecharge.com/glossary/aov/` (the page these figures were
initially cited to) confirmed the page discusses AOV generally and lists vertical names, but does
**not** actually state either dollar figure — a genuine over-claim from a secondary summary, not a
primary page. A second candidate (`ecommercegermany.com`'s Recharge-report summary) and a third
(`getrecharge.com/resources/physical-subscription-commerce-report-2020/`) were also fetched
directly and neither contains these figures either.

**CORRECTION (during Tier 2 P6 data-decay verification):** since the original citation could not
be confirmed against any page this session actually fetched, it was replaced before publication
rather than left in place. Fetched `https://www.shopify.com/blog/average-order-value` directly
(Shopify's own blog, dated September 18, 2025, citing Dynamic Yield's benchmark research) and
confirmed real, quotable AOV-by-category figures: beauty & personal care "$15 to $90," apparel &
accessories "$40 to $170," and a stated "global average AOV across industries... around $145." No
source publishes an AOV specifically for outdoor-gear or general lifestyle subscription boxes, and
no source publishes Basecamp Crate's own AOV (a fictional company).

**Outcome:** NOT FOUND as a direct citable figure for this specific vertical/company. **Exit
chosen: Modeling Assumption (MA5)**, value $58, informed by the confirmed Shopify/Dynamic-Yield
range (within the $15–$90 beauty/personal-care band, well below the ~$145 global baseline) but set
near the lower end of commonly observed public subscription-box price points (~$30–$70/month),
since an outdoor-gear/snack-style box is priced lower than premium beauty/wellness verticals.

## P01/P02/P03 — CRM list sizes (Set P, Set L, P ∩ L) and the reachable universe

**Searched:** none attempted as a live web search — confirmed by direct reasoning before
searching that this class of figure (one specific, fictional company's internal CRM list sizes and
their exact overlap) cannot exist as a publishable external dataset by definition: it is
proprietary, day-to-day operational data for a company invented for this case. No amount of
searching would find it, the same category of "does not exist as a citable dataset" finding
`the-deferred-repair`'s RESEARCH_LOG made explicit for its own coolant-failure-probability figures.

**Outcome: NOT FOUND, correctly not searched for.** **Exit chosen: Modeling Assumption (MA1)**,
values U = 90,000, P = 21,400, L = 38,600, P ∩ L = 6,900 — chosen to reflect a realistic relative
pattern (an all-time newsletter list larger than a rolling 90-day purchase list, partial but real
overlap between two vendor-built forms) and to keep the resulting union/intersection reach gap
(53,100 vs. 6,900, roughly 7.7x) large enough to make the reach-vs-rate trap genuinely tempting.

## P04/P05 — Flat per-recipient send cost, remaining quarterly budget

**Searched:**
- "average cost per email sent marketing ESP benchmark cost per thousand emails 2026"
- "SendGrid pricing per email 2026 official pricing page"
- `https://mailchimp.com/pricing/marketing/` (fetched directly) — confirmed Mailchimp prices by
  contact tier with a send multiplier (e.g., Standard: 12x contacts/month), not a literal flat
  per-recipient fee.

**Found:** Real published ESP pricing exists (Amazon SES ~$0.10 per 1,000 emails; SendGrid
overage pricing ~$0.85–$1.00 per additional 1,000 emails, i.e., roughly $0.001/email at typical
tiers), but this case's narrative cost is explicitly framed as coming out of an **ad budget** —
implying a coordinated email-plus-paid-distribution cost, not a bare transactional email send —
and no source publishes a blended per-recipient figure for that specific configuration.

**Outcome: NOT FOUND** as a directly citable figure for the case's specific "flat per-recipient,
ad-budget-funded send" framing. **Exit chosen: Modeling Assumption (MA2)**, value $0.06/recipient,
set above bare ESP marginal costs (~$0.001/email) and below typical third-party list-rental costs
(~$0.10–$0.40/name), reflecting a company mailing its own list at a coordinated rate. The remaining
quarterly budget ($4,000, MA3) is the approved concept's own stated scenario detail and was never
expected to resolve as an external citation — disclosed as a constructed scenario figure per the
concept-approval guidance that a subscription-box company's specific budget may be a disclosed,
realistic constructed detail.

## Summary table

| ID | Placeholder | Resolution | Value | Confidence |
|---|---|---|---|---|
| P01 | Set P size | ASSUMPTION (MA1) | 21,400 | n/a (assumption) |
| P02 | Set L size | ASSUMPTION (MA1) | 38,600 | n/a (assumption) |
| P03 | P ∩ L overlap | ASSUMPTION (MA1) | 6,900 | n/a (assumption) |
| P04 | Flat per-recipient send cost | ASSUMPTION (MA2) | $0.06 | n/a (assumption) |
| P05 | Remaining quarterly budget | ASSUMPTION (MA3) | $4,000 | n/a (assumption) |
| P06 | Broad-send conversion rate | SOURCED (S1) | 0.16% | HIGH |
| P07 | Intersection-segment conversion rate | ASSUMPTION (MA4) | 0.60% | n/a (assumption, informed by S1-S3) |
| P09 | Average order value | ASSUMPTION (MA5) | $58 | n/a (assumption, informed by S4) |
| — | Sources appendix | SOURCED (S1-S4) | — | mixed (1 HIGH, 3 MEDIUM/supplemental) |

Sourced: 1 figure used directly ([S1]), plus 3 supplemental sources ([S2]–[S4]) cited to show
their real, named provenance even though they inform rather than directly supply a case value.
Assumption: 5 Modeling Assumption records (MA1–MA5) resolve the remaining 7 placeholders (MA1
covers 3 placeholders as one CRM-snapshot record). Dropped: 0. Open: 0.

## Next step

Run `case-readiness` on `the-overlap-send`.
