# Research Log — The Approval Gate

Stage 3 (`case-research`) run on `cases/the-approval-gate/`. 19 `{{NEEDS_SOURCE}}` placeholders
enumerated. Worked in load-bearing weight order: the two figures with a genuine chance of a real
public benchmark first (the return-fraud rate and the escalation cost-per-contact), then the
platform-realism grounding for Appendix A/B's structure, then the internal volume/threshold
figures (confirmed as non-public, proprietary-shaped before searching, since no company publishes
its own internal AI-agent request logs).

## P_APPD_FRAUD_RATE — Retail return-fraud rate

**Searched:**
- "NRF Appriss retail returns fraud percentage 2024 report customer returns"

**Fetched directly:**
- `https://apprissretail.com/news/appriss-retail-annual-research-fraudulent-returns-and-claims-cost-retailers-103b-in-2024/`
  — Appriss Retail's own 2024 annual research (with Deloitte), published 2024-12-30. Confirmed
  exact figures: **15.14% of all returns** were deemed fraudulent in 2024; fraudulent returns and
  claims cost retailers **$103 billion**. Methodology: data from 60+ leading US retailers, US
  Census Bureau statistics, a survey of 150 retail executives, and 1,000 consumers — the seventh
  consecutive annual report in this series.

**Outcome:** SOURCED as [S2], HIGH confidence (primary publisher, real stated methodology, dated,
industry-standard annual report, exactly the figure needed). Used **directly** in Appendix D and
this case's arithmetic — multiplied against Modeling Assumption MA4's average dollar value at risk
to compute the expected loss per incorrectly auto-approved refund request. This is the one figure
in the case used exactly as published, not merely informing an assumption's basis.

## P_APPD_COST_PER_ESCALATION — Cost per escalated (human-reviewed) request

**Searched:**
- "average cost per customer service contact ticket benchmark 2025"
- "Zendesk CX Trends Report 2025 average cost per ticket resolution benchmark"

**Fetched directly:**
- `https://www.zendesk.com/sg/blog/ai/productivity/cost-per-resolution/` — confirmed this page
  explains the cost-per-resolution (CPR) formula with only an illustrative example
  ($250,000 ÷ 50,000 = $5.00), no real industry benchmark figures. Rejected as a source for a real
  value.
- `https://www.ringly.io/blog/ecommerce-customer-service-cost-per-contact` — confirmed real figures
  aggregated from named third-party research: a Gartner-cited cross-industry "assisted channel"
  (human-handled) average of **$13.50** per contact (versus $1.84 for self-service); an
  Opensend-cited ecommerce ticket range of **$2.70–$5.60**; Ringly.io's own benchmark assessment of a
  small-ecommerce-store range of **$6–$12** per contact (informed by Gorgias ticket-volume/order-count
  data, but the $6-$12 dollar figure itself is Ringly.io's own assessment, not directly attributed to
  Gorgias on the page); a worked example computing $9.09/ticket for a mid-size Shopify
  store.

**Outcome:** NOT FOUND as a single, directly-citable exact figure for "cost of a manually reviewed
refund request" — no source measures this exact task. **Exit chosen: Modeling Assumption (MA3)**,
value $9.00, informed by [S4] (the Ringly.io page's Gartner- and Opensend-attributed figures, plus its own Gorgias-informed benchmark assessment),
set within the small-retailer $6–$12 range, toward its middle-upper part since a refund review
requires pulling order and customer history rather than a simple FAQ answer. [S4] graded MEDIUM
(a secondary vendor blog aggregating other firms' research, not its own primary methodology) —
disclosed as such in Appendix F.

## P_APPB_STRUCTURE / P_BACKGROUND_GATING_GUIDANCE — Real platform grounding

**Searched:**
- "Salesforce Agentforce approval workflow human-in-the-loop escalation rules documentation 2026"
- "ServiceNow AI Agent approval gate escalation condition documentation"
- "Microsoft Copilot Studio human in the loop approval agent actions documentation"

**Fetched directly:**
- `https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-advanced-approvals` — Microsoft
  Learn's own documentation for Copilot Studio's multistage/AI approvals feature, dated
  2025-09-04, updated 2026-06-30. Confirmed the page instructs builders to write rejection logic
  as an explicit list of conditions ("Reject the expense report if ANY of the following conditions
  are true") and shows a worked example using a $5,000 expense-amount threshold to route between
  automatic approval and manager escalation.
- `https://architect.salesforce.com/docs/architect/decision-guides/guide/determining-agentic-vs-traditional-workflow-automation`
  — Salesforce Architects' own decision guide. Confirmed the quote: "Agentic workflows operating
  at high density should incorporate explicit human approval or escalation gates for actions with
  irreversible consequences, such as financial transactions, regulatory submissions, or supplier
  commitments." No publication date visible on the page.

**Outcome:** SOURCED as [S1] (HIGH — dated, primary, directly fetched) and [S3] (MEDIUM —
primary but undated). ServiceNow's AI Agent governance documentation was found via WebSearch
(community guide/governance PDF attachments describing "approval gates," "evidence gates," and
policy-matrix-based action guardrails) but was **not** independently fetched and confirmed as a
primary page during this session, so it is named only in case.md's narrative prose (as a real,
named 2026 platform in this product category, per the approved concept's own framing) and is
**not** cited in Appendix F — per the rule against citing a URL not directly fetched.

## P_APPA_THRESHOLDS / P_APPC_VOLUME — Gate thresholds and monthly request-category volume

**Searched:** none attempted as a live web search — confirmed by direct reasoning before searching
that this class of figure (one specific, fictional company's internal AI-agent policy thresholds
and its own monthly request-volume breakdown by condition) cannot exist as a publishable external
dataset by definition: it is proprietary, day-to-day operational data for a company invented for
this case, the same category of "does not exist as a citable dataset" finding
`cases/the-overlap-send/RESEARCH_LOG.md` made explicit for its own CRM list sizes.

**Outcome: NOT FOUND, correctly not searched for.** **Exit chosen: Modeling Assumptions (MA1, MA2)**
— MA2 sets the $60 amount threshold, 1-year tenure threshold, and 90-day/2-request repeat-request
definition (informed by [S1]'s confirmation that real platforms use exactly this numeric-threshold
structure, though not by its specific $5,000 example, a different domain/scale). MA1 sets the
8-category monthly volume breakdown (total 3,600/month), chosen so the large majority of requests
are fully safe and the riskier categories shrink toward the rarest (all-conditions-unfavorable)
case — a realistic pattern for a mid-size retailer, and large enough that the reach-vs-cost trade
between the two gate designs is genuinely close (see `case.json.balance.margin_pct`).

## P_APPD_AVG_VALUE_AT_RISK — Average dollar value at risk per incorrectly approved request

**Searched:** considered searching for a published "average fraudulent refund amount" figure, but
[S2]'s own Appriss Retail report states only an aggregate percentage (15.14% of returns) and a
total industry-wide dollar loss ($103B) — not a per-incident average, and not broken out by
company size or product category. Computing a per-incident average by dividing $103B by an assumed
total-fraudulent-return count would require a return-count figure the report does not publish,
so that derivation was rejected as overreach rather than attempted.

**Outcome: NOT FOUND** as a directly citable per-incident figure. **Exit chosen: Modeling
Assumption (MA4)**, value $66.00, set as a company-specific figure near Appendix A's own $60
dollar threshold (risky requests cluster close to, and sometimes just past, the auto-approval
line), then multiplied directly by the sourced 15.14% fraud rate [S2] to produce the case's
expected-loss-per-incident figure ($9.99) used in Challenge 3 (D4).

## Summary table

| Placeholder | Resolution | Value | Confidence |
|---|---|---|---|
| Appendix A thresholds (p, q, r) | ASSUMPTION (MA2) | $60 / 1 year / 2nd+ in 90 days | n/a (assumption, informed by S1) |
| Appendix C, 8 category counts + total | ASSUMPTION (MA1) | see case.md, total 3,600/mo | n/a (assumption) |
| Appendix D, cost per escalation | ASSUMPTION (MA3) | $9.00 | n/a (assumption, informed by S4) |
| Appendix D, return-fraud rate | SOURCED (S2) | 15.14% | HIGH |
| Appendix D, average value at risk | ASSUMPTION (MA4) | $66.00 | n/a (assumption) |
| Appendix F Sources table | SOURCED (S1-S4) | — | 2 HIGH, 2 MEDIUM |

Sourced: 1 figure used directly ([S2]), plus 3 supplemental sources ([S1], [S3], [S4]) cited to
show their real, named provenance even though two of them inform rather than directly supply a
case value, and one ([S1]) grounds the case's structural realism. Assumption: 4 Modeling
Assumption records (MA1–MA4) resolve the remaining 15 placeholders. Dropped: 0. Open: 0.

## Next step

Run `case-readiness` on `the-approval-gate`.


## CORRECTION (during Tier 2 P6 data-decay verification)

A live re-fetch of `https://www.ringly.io/blog/ecommerce-customer-service-cost-per-contact` during
Tier 2 probe 6 found that the $6–$12 small-ecommerce-store cost-per-contact range — originally
written up in case.md/case.json as "Gorgias-cited" — is actually Ringly.io's own benchmark
assessment. The page attributes ticket-volume/order-count metrics to Gorgias ("Small stores...
expect 88 tickets per 100 orders") but states the $6–$12 dollar figure itself as its own analysis,
not a quote from Gorgias. The Gartner ($13.50 assisted-channel average) and Opensend ($2.70–$5.60
ecommerce range) attributions on the same page WERE independently confirmed as accurate on
re-fetch. Corrected in `case.md`'s Appendix F and Modeling Assumptions table, `case.json.sources[S4]`
and `modeling_assumptions[MA3]`, and this log, per the rule against citing a claim the fetched page
does not actually support. This does not change MA3's chosen $9.00 value or any downstream
arithmetic — it only corrects who is credited with the supporting range.
