Case Study: The Overlap Send
MS | Math | Case Study | 2026 | Launchpad

## Overview

Jess Okafor has the CRM export open in one tab and the board deck open in the other, and the cursor won't stop blinking in the "Send To" field. Two lists sit side by side on the screen: one column of everyone who bought a Basecamp Crate box in the last ninety days, another column of everyone who ever checked the newsletter box at checkout. Nobody on this three-person marketing team has ever actually compared them.

A Slack message from the CEO is still pinned at the top of the channel: *"Board meeting Friday. Need to see the plan for the number by then."* The quarter is behind, and this send is the last one the ad budget can cover before the quarter closes. Jess has already dragged the two lists into a spreadsheet twice and closed it twice, because both times the honest next step was a diagram, not a guess.

The office is empty except for the hum of the space heater under the desk and a half-cold oat-milk latte. Jess pulls up a blank circle-and-circle sketch, types the two list sizes into the corners, and stops with the cursor hovering between "Send to everyone" and "Send to just the middle."

The file has to go out today. One list. One send. One number to bring to the board on Friday.

## Background

Jess Okafor is the sole growth marketer at Basecamp Crate, a small outdoor-gear subscription box company. Marketing owns the CRM, the newsletter signup form, and the paid-send budget, and Jess is the only person who touches all three — there is no one else to double check the math before Friday's board meeting.

Basecamp Crate's CRM currently holds two separate customer lists, built by different tools at different times (SEE APPENDIX A): **Set P**, everyone who purchased a box in the last 90 days, and **Set L**, everyone who has ever opted into the email newsletter. The purchase-tracking form and the newsletter signup form were built by two different vendors two years apart, and nobody on the current team has ever run the two lists against each other to see how much they overlap.

This quarter's remaining paid-send budget is fixed and cannot be exceeded (SEE APPENDIX B): whatever list Jess chooses, the total cost of the send — every name on the list, billed at the same flat per-recipient rate regardless of whether that person ever opens the email — must fit inside it. There is no partial-send option and no way to add more budget before Friday.

The two options on the table are named plainly on Jess's whiteboard: **Cast The Net**, mailing every name that appears in *either* list (the union of P and L), or **Mail The Middle**, mailing only the names that appear in *both* lists (the intersection of P and L). A published industry benchmark report gives a real, sourced conversion-rate figure for what a broad, undifferentiated send typically achieves, and that same body of published research informs — without directly measuring — how much better a tightly-overlapping segment is likely to convert (SEE APPENDIX C). The vocabulary and "how to…" procedures needed to work through the two sets are listed in (SEE APPENDIX D), and every sourced or assumed figure in this case is documented in (SEE APPENDIX E).

Jess has to recommend one list, defend the expected revenue math behind it, and file it before the office closes today.

## Dilemma

You are Jess Okafor.
Do you:
A.) Cast The Net — mail everyone in the union of Set P and Set L, the widest possible reach OR
B.) Mail The Middle — mail only the names in the intersection of Set P and Set L, the smallest, most tightly-overlapping list

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A two-circle Venn diagram, drawn inside a rectangle representing Basecamp Crate's full
    reachable email universe, showing Set P and Set L with all four region counts labeled from
    Appendix A's data (only-P, only-L, both, and neither) — including an explicit check of
    whether any one of those four regions is the empty set (∅), and a sentence stating what it
    would mean for this case if it were.
    D2. A written set-notation summary stating |P|, |L|, |P ∩ L|, and |P ∪ L|, showing the
    inclusion-exclusion arithmetic used to compute |P ∪ L| from |P|, |L|, and |P ∩ L|, plus a
    subset determination — using ⊆ or ⊄ notation — for whether P is a subset of L, or L a subset
    of P, defended with the actual counts from Appendix A.
    D3. A reach-and-cost table comparing Option A (mail P ∪ L) and Option B (mail P ∩ L):
    recipient count, total send cost at Appendix B's flat per-recipient fee, and how each
    compares to Appendix B's fixed remaining budget.
    D4. An expected-net-revenue calculation for each option — reach × conversion rate × average
    order value, minus total send cost — using Appendix C's benchmark conversion-rate figures,
    shown step by step for both options.
    D5. A one-paragraph written recommendation, using correct set notation (∩, ∪, ⊆, ⊄, ∅)
    throughout, that names which option's expected net revenue is higher and explicitly
    addresses why comparing raw reach alone, without the conversion-rate difference, would have
    been misleading.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — CRM List Snapshot

Referenced in Background and Challenge 3 (D1, D2). Basecamp Crate's two customer lists, exported
the same afternoon so both counts are from the same moment in time.

| Set | Definition | Count |
|---|---|---|
| Full reachable email universe (U) | All active, mailable contacts in Basecamp Crate's ESP (Email Service Provider — the platform, such as Klaviyo or Mailchimp, that a company uses to send and track its marketing emails) | 90,000 (MA1) |
| P | Customers who purchased a Basecamp Crate box in the last 90 days | 21,400 (MA1) |
| L | Customers who have ever opted into the Basecamp Crate email newsletter | 38,600 (MA1) |
| P ∩ L | Customers who appear on BOTH lists | 6,900 (MA1) |

**RESEARCH FLAG RESOLVED:** no public company publishes the exact size or exact overlap of its own
CRM lists — this is proprietary, day-to-day operational data specific to one company's customer
database, and it does not exist anywhere as a citable external dataset, not merely as a
hard-to-find one. All four counts (including the total reachable universe, needed to draw
Challenge 3's Venn diagram inside a bounded rectangle) are therefore a stated, disclosed **Modeling
Assumption (MA1)** — see the Modeling Assumptions section below for the full basis and sensitivity.

## Appendix B — Send Cost & Remaining Budget

Referenced in Background and Challenge 3 (D3).

| Item | Value |
|---|---|
| Flat cost per recipient, any send (regardless of whether the recipient opens it) | $0.06 (MA2) |
| Basecamp Crate's remaining paid-send budget this quarter | $4,000 (MA3) |

## Appendix C — Conversion & Order-Value Benchmarks

Referenced in Background and Challenge 3 (D4).

| Metric | Value | Source type |
|---|---|---|
| Placed-order (conversion) rate, a broad, undifferentiated send to a full customer file | 0.16% [S1] | sourced benchmark report |
| Placed-order (conversion) rate, a tightly-overlapping, multi-signal segment (customers who show two independent signals of interest) | 0.60% (MA4) | stated modeling assumption, informed by [S1], [S2], [S3] |
| Average order value (AOV), Basecamp Crate box purchase | $58 (MA5) | stated modeling assumption, informed by [S4] |

**What "conversion" means here:** a "placed-order (conversion) rate" of 0.16% means that out of every
1,000 people who receive the send, 1.6 of them go on to complete a purchase — place an actual order,
not just open the email or click a link. Challenge 3 (D4) multiplies this rate by reach and by AOV to
turn "how many people saw the email" into "how much revenue the send is expected to generate."

**RESEARCH FLAG RESOLVED:** a genuine search for a published conversion-rate figure specific to
"customers appearing in both a recent-purchase list and a newsletter opt-in list" turned up no
such report — no industry source measures exactly this two-list overlap segment; it is not a
publishable figure at any confidence grade. The broad-send rate **is** a real, sourced figure
[S1]. The intersection-segment rate is a stated Modeling Assumption (MA4), informed by — but not
copied directly from — three real, cited pieces of published research on targeting/segmentation
lift [S1]/[S2]/[S3]. See the Modeling Assumptions section below.

## Modeling Assumptions

> These figures are **not sourced from an external publisher**. They are stated scenario
> assumptions chosen by the case author because Basecamp Crate's own list sizes, overlap, budget,
> and per-recipient cost are internal operational data no public company publishes, and because no
> industry report measures the exact "recent-purchaser-and-newsletter-subscriber" segment's
> conversion rate. A Hero may challenge these numbers in discussion — that is a legitimate move,
> and the sensitivity column shows exactly where the challenge would matter.
>
> The Basis columns below cite real research from Klaviyo, HubSpot, and Mailchimp (all companies
> that make email marketing software) and Shopify (an ecommerce platform) — see Appendix E for
> what each company is and how each figure is used.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Full reachable email universe (U), Set P size, Set L size, and overlap P ∩ L | U = 90,000; P = 21,400; L = 38,600; P ∩ L = 6,900 | No source publishes any specific company's internal CRM list sizes. Chosen to reflect a realistic relative pattern for a small subscription-box company: an all-time newsletter list (built from every checkout since launch) larger than a rolling 90-day purchaser list, built by two different signup forms with only partial overlap. | This case's numbers are close enough that several of these counts, if challenged, could change which option comes out ahead — work the comparison yourself with a different plausible set of counts rather than taking 21,400 / 38,600 / 6,900 as unchallengeable fact. |
| MA2 | Flat per-recipient send cost | $0.06 | No source publishes an exact blended figure for a coordinated email-plus-paid-sync send (a send where the same customer list is also uploaded to a paid ad platform, like Facebook or Google, so the ads and the email reinforce each other) charged against an "ad budget" (rather than a bare transactional email send). Set well above published bare email-service-provider marginal costs (roughly $0.001 per email at typical ESP overage pricing) and well below typical third-party list-rental costs (the per-name fee a company pays to temporarily rent someone else's mailing list for a single send, roughly $0.10–$0.40 per name), reflecting a company mailing its own list at a coordinated, ad-budget-funded rate rather than a raw send-only rate or a rented list. | A Hero who challenges this figure changes both options' total cost and how much of Appendix B's budget each option consumes — redo Challenge 3 (D3) and (D4) with a different value before assuming the recommendation is unaffected. |
| MA3 | Remaining quarterly paid-send budget | $4,000 | This is the case's own stated scenario detail — Basecamp Crate's specific remaining ad budget is a constructed, disclosed detail of this fictional company, not a figure any public source could publish. | Does not change which option's expected net revenue is higher on its own (both options fit under $4,000 in this case), but a smaller stated budget could rule Option A out entirely — check whether Appendix B's cost figures still fit before assuming both options remain on the table. |
| MA4 | Placed-order rate for the intersection (multi-signal) segment | 0.60% | No source measures conversion rate for exactly "recent purchaser AND newsletter subscriber." Informed by three real, cited findings: Klaviyo's own 2026 benchmark data shows automated, behavior-triggered sends convert at 2.11% versus 0.16% for broad campaign sends [S1] — roughly a 13x gap for the most targeted category Klaviyo measures; HubSpot's published guidance states a properly segmented send should outperform a broadcast send by "at least 20–30%" [S2]; and Mailchimp's own list-segmentation study (2,000 accounts, ~11,000 campaigns, ~9 million recipients) found segmented campaigns generate a 100.95% higher click-through rate than non-segmented campaigns [S3], though that study does not measure purchase conversion directly. 0.60% (a 3.75x lift over the sourced 0.16% broad rate) is chosen as a deliberately moderate point within the real range these sources bracket — well below Klaviyo's most extreme measured gap, since a static two-list overlap segment and a fully behavior-triggered flow are not the same mechanism. | This is the single assumption the case's recommendation is most sensitive to. A modest, defensible challenge to this value in discussion could change which option comes out ahead once Challenge 3 (D4)'s expected-revenue comparison is redone with that changed value — work the comparison yourself rather than taking 0.60% as unchallengeable fact. |
| MA5 | Average order value (AOV) | $58 | No source publishes Basecamp Crate's own AOV. Informed by Shopify's own 2025 AOV benchmark figures (citing Dynamic Yield's benchmark research): beauty & personal care $15–$90, apparel & accessories $40–$170, global ecommerce baseline ~$145 [S4]. Basecamp Crate is modeled as a lower-price-point outdoor-gear box rather than a premium vertical, so $58 sits within the lower beauty/personal-care band and well below the global baseline, consistent with commonly observed public subscription-box price points (roughly $30–$70/month). | A Hero who challenges this figure changes the expected-revenue gap between the two options proportionally on both sides — redo Challenge 3 (D4) with a different value before assuming the recommendation is unaffected. |

## Appendix D — "How To…" Math Questions To Research

**Vocabulary terms**

- Set
- Subset
- Union
- Intersection
- Empty Set
- Venn Diagram

**"How to…" questions**

- How to find the union and intersection of two sets
- How to represent a set relationship using a Venn diagram

## Appendix E — Sources

All sourced (non-assumption) figures in this case are cited here. Sources marked "supplemental"
are not directly quoted for a value used in this case's arithmetic; they inform the basis column
of a Modeling Assumption (see above) and are cited for transparency about what real research
shaped that assumption.

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Placed-order rate, broad ecommerce email campaign sends (all industries), vs. automated/behavior-triggered flow sends | Campaigns 0.16% / Flows 2.11% | Klaviyo — [2026 Email Marketing Benchmarks by Industry](https://www.klaviyo.com/products/email-marketing/benchmarks) | Feb 2026 | HIGH |
| S2 | Guidance that a properly segmented email send should outperform a broadcast send by at least 20–30% | 20–30% minimum expected lift | HubSpot Blog — [Email List Segmentation: 30 Ways to Earn Higher Engagement and Revenue](https://blog.hubspot.com/marketing/email-list-segmentation) | 2026 | MEDIUM (supplemental — informs MA4's basis, not directly used as the case's value) |
| S3 | Effect of list segmentation on campaign click-through rate | Segmented campaigns: 100.95% higher click-through rate than non-segmented | Mailchimp — [Effects of List Segmentation on Email Marketing Stats](https://mailchimp.com/resources/effects-of-list-segmentation-on-email-marketing-stats/) | Published Feb 2017 | MEDIUM (supplemental — dated study, measures clicks not purchases; informs MA4's basis, not directly used as the case's value) |
| S4 | Average order value benchmarks by product category, general ecommerce | Beauty & personal care $15–$90; apparel & accessories $40–$170; global baseline ~$145 | Shopify (citing Dynamic Yield benchmark research) — [Average Order Value benchmarks by industry](https://www.shopify.com/blog/average-order-value) | Sep 2025 | MEDIUM (supplemental — informs MA5's basis, not directly used as the case's value) |

**Who these sources are:** Klaviyo, HubSpot, and Mailchimp are all companies that make email
marketing software — the tools businesses use to build, send, and track email campaigns like the
one Jess is planning — and each publishes its own benchmark research from the campaigns run on its
platform. Shopify is an ecommerce platform companies use to run their online stores; Dynamic Yield
is a personalization technology company (now part of Mastercard) whose benchmark research Shopify
cited in S4.

S1 is the only figure used directly as a value in this case's arithmetic (the 0.16% broad-send
conversion rate, Appendix C). S2–S4 are real, dated, named-source figures that inform Modeling
Assumptions MA4 and MA5's chosen values without being the values themselves — see the Modeling
Assumptions table above for exactly how each is used. See `RESEARCH_LOG.md` for the full search
trail, including sources consulted and rejected for the CRM list sizes, per-recipient cost, and
budget figures (now Modeling Assumptions MA1–MA3 above).

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
