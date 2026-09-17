# Research Log — FlowState

Stage 3 (`case-research`) run on `cases/flow-state/`. This case was drafted and researched in a
single combined pass rather than starting from literal `{{NEEDS_SOURCE}}` tokens in a saved
intermediate file; the log below documents the same search-and-cite discipline `case-research`
requires, organized by the figure each entry resolves. Worked in load-bearing weight order: the
two directly-quoted channel benchmarks first (SEO CPC/CVR, magazine CPM — both used as real values,
not just assumption-basis), then the wide-range channel benchmarks (TV CPM, radio), then the
funnel-conversion benchmarks (site conversion, trial-to-paid), then the harder-to-source
company-specific figures (budget, segment skew, awareness/interest rates).

## P01 — SEO / paid search cost-per-click and conversion rate (Health & Fitness category)

**Searched:** "Google Ads benchmark 2026 average CPC health fitness industry"

**Fetched directly:** `https://ppcchief.com/google-ads-benchmarks/health-fitness` — confirmed
exact figures: average CPC $5.00, average CTR 7.2%, conversion rate 6.8%, CPL $62.80, "expected
CPC typically falls between $3.75 and $6.75," updated 18 Feb 2026, methodology stated as "£20M+ in
managed Google Ads spend and 200K+ leads generated across 15+ years and 200+ accounts."

**Outcome:** SOURCED as [S1], MEDIUM confidence (a paid-search agency's own benchmark report from
its own managed spend — real and dated, but not a primary platform-published figure). CPC $5.00
used directly for SEO reach (Appendix A). CVR 6.8% used directly as SEO's own trial-conversion rate
(Appendix D), distinct from the generic DTC site-conversion rate (S6) applied to every other
channel, since a paid-search click carries meaningfully more purchase intent than a passive
broadcast/print impression.

## P02 — Cable TV CPM and per-spot cost range

**Searched:** "average cost 30-second national cable TV ad 2026 CPM sports network"

**Fetched directly:** `https://vidico.com/news/how-much-does-a-30-second-commercial-cost/` —
confirmed: "CPM range: $10 to $30 for cable TV, with prime-time slots on major networks commanding
premium rates." Niche cable channels: $1,000–$20,000/spot. Premium networks (ESPN, TNT):
$20,000–$150,000/spot. The article does **not** separately break out a sports/fitness-network CPM
from a general-broadcast-network CPM — both are lumped under the same cable/broadcast range.

**Also fetched (404, not cited):** `https://mountain.com/blog/tv-advertising-cost/` (MNTN's guide —
URL returned HTTP 404, page not retrievable; not cited anywhere in this case per the "never cite a
URL you did not fetch" rule).

**Outcome:** SOURCED as [S2], MEDIUM confidence. Since no source distinguishes a sports/fitness
package's CPM from a general daytime/primetime package's CPM, two specific point-values were chosen
*within* this one real range rather than treated as two independently sourced figures: $14.00 for
TV Sports/Fitness (MA2, toward the low end — niche/targeted inventory), $24.00 for TV General
(MA3, toward the high end — broader, primetime-adjacent inventory). Both disclosed as Modeling
Assumptions in Appendix E, not presented as two separately sourced numbers.

## P03 — Radio drive-time advertising cost

**Searched:** "radio drive time ad cost CPP 2026 average spot price"; "radio advertising CPM
average cost per thousand listeners 2026"

**Fetched directly:**
- `https://www.radioadvertisinghome.com/radio-advertising-cost-rates-cpm-what-to-pay/` — confirmed
  explicit statement: "There is no national price list for radio. A rate is assembled from market,
  audience, daypart, length, season and how much unsold inventory a station is holding that week."
  No usable CPM/CPP number found on this page.
- `https://www.adresultsmedia.com/news-insights/how-much-do-radio-ads-cost/` — confirmed a table of
  average 60-second ad costs across the 15 largest U.S. radio markets (e.g. New York $795.15,
  Boston $1,168.60, Philadelphia $500.55, Detroit $503.38, Seattle-Tacoma $600.00, Miami-Ft.
  Lauderdale $90.77) and a CPP range of $3–$525. No reach/audience-size figure accompanies these
  spot costs, so they could not be converted into a CPM directly.
- `https://www.radioadvertisinghome.com/radio-advertising-rates-glossary-cost-benchmarks/` —
  confirmed CPM/CPP definitions only, no numeric range. Cited as [S9], supplemental/vocabulary.
- `https://www.audiogo.com/blog/podcast-advertising-cost-and-rates` — confirmed, dated 10 Aug 2026:
  "Traditional radio ads typically run $900 to $2,000 a week in small markets, $2,500–$5,000 in
  medium markets, and $5,000–$8,000+ in large markets," plus podcast CPM "$12 to $55... most
  advertisers paying $15–$30 CPM."

**Rejected (not cited):** a WebSearch-synthesized claim of a "commonly cited $5–$15 radio CPM"
could not be traced to any page this session actually fetched with that number on it — per the
"never cite a URL you did not fetch" rule, it is not used anywhere in this case.

**Outcome: NOT FOUND** as a direct, citable, drive-time-specific CPM. **Exit chosen: Modeling
Assumption (MA4)**, value $10.00 CPM, cross-checked for plausibility against the real, dated
weekly-package figures in [S3] (a $10 CPM at a medium-market weekly budget in the low thousands of
dollars implies an audience size broadly consistent with a real medium-market weekly package cost)
rather than invented outright. [S3] (AudioGo) also supplies the podcast CPM shown in Appendix A as
a real, priced-out, decorative/unused channel.

## P04 — Magazine (health/fitness) advertising rate

**Searched:** "health fitness magazine full page ad rate 2026 rate card"; "Men's Health OR Shape OR
Runner's World magazine media kit full page ad rate 2026"; "fitness magazine full page ad rate
$10,000 OR $4,300 circulation media kit"; "consumer magazine average full page ad cost circulation
2026 rate benchmark"

**Fetched directly (rejected):**
- `https://www.themediaant.com/magazine/mens-health-magazine-advertising` — no rate quoted, Indian
  edition, directs to contact sales. Not cited.
- `https://www.gaebler.com/Muscle+&+Fitness-magazine-advertising-costs++29366` — quoted a specific
  $36,145 full-page estimate for Muscle & Fitness, but the page itself explicitly states this
  estimate "may be completely incorrect." Rejected as LOW confidence per the "a LOW figure may
  never carry a constraint" rule — not used.
- `https://www.webfx.com/digital-advertising/pricing/cost-to-advertise-in-national-magazines/` —
  confirmed a "$250,000 to $700,000" typical national-magazine range, but this describes
  large-circulation flagship titles, not a mid-size specialty health/fitness magazine; too far
  outside this case's scale to use directly.

**Fetched directly (used):** `https://mediamaxnetwork.com/industry-insights/magazine-advertisement-rates-how-to-get-the-best-deal/`
— confirmed two specific, attributed CPM figures: "A full-page ad in a million-circulation
magazine costs around $22 per thousand impressions (CPM)... a 100,000 circulation magazine charges
$63 CPM," attributed to the Association of Magazine Media (the print-magazine industry's own trade
association). No publication date is shown on the page itself — disclosed as such in
`case.json.sources[S4].as_of`.

**Outcome:** SOURCED as [S4], MEDIUM confidence — the one channel-cost figure in this case used
directly as a real, quoted, attributed value rather than only informing an assumption's basis. The
100,000-circulation tier was chosen as representative of a mid-size specialty health/fitness title,
since no source gave a circulation-specific rate for a magazine of that description by name.

## P05 — Startup launch advertising budget (Solstice Labs' own figure)

**Searched:** "early stage hardware startup product launch marketing budget benchmark"; "seed stage
hardware startup product launch marketing budget dollars site:techcrunch.com OR
site:crunchbase.com"

**Outcome, without a further fetch:** Solstice Labs' own budget cannot exist as a citable external
figure — it is a fictional company. This is the same category finding documented for
`the-fee-route`'s MA3 (Fernbrook's own transaction value) and `the-overlap-send`'s MA1 (CRM list
sizes): correctly not chased further as a direct search once confirmed.

**Fetched directly for grounding:** `https://www.gtm8020.com/blog/startup-marketing-budget-statistics`
— confirmed: "Seed-stage startups spend 10-20% of their funding on marketing," "Seed startups
typically work with $50,000-$250,000 annually for marketing," "Early-stage companies average
$5,000 to $10,000 monthly in marketing spend."

**Outcome: Exit chosen: Modeling Assumption (MA1)**, value $60,000, set within the real, sourced
$50,000–$250,000 annual seed-stage marketing range [S5] as a launch-specific slice of the annual
figure rather than the full year.

## P06 — Interested-visitor-to-trial-signup conversion rate (non-SEO channels)

**Searched:** "DTC hardware subscription funnel conversion rate benchmark awareness to purchase
2026"

**Fetched directly:** `https://topgrowthmarketing.com/dtc-ecommerce-benchmarks/dtc-site-conversion-rate-2026/`
— confirmed: median site conversion rate 1.17% (middle 50%: 0.92%–1.52%), across 19 DTC store
properties, ~17.0 million sessions, ~235,000 transactions, "transactions ÷ sessions in GA4"
methodology, trailing 12 months ending June 2026.

**Outcome:** SOURCED as [S6], HIGH confidence (a stated, dated methodology and a real sample size —
the strongest-sourced figure in this case). Used directly as the interested-visitor-to-trial-signup
conversion rate for every channel except SEO (which uses its own, higher, directly-sourced rate
from [S1] instead, since a search click already carries more intent than a generic DTC site
visitor).

## P07 — Trial-to-paid adoption rate, by segment

**Searched:** "direct to consumer subscription trial to paid conversion rate benchmark 2026"

**Fetched directly:** `https://blog.cleeng.com/subscription-conversion-benchmarks` — confirmed
trial-to-paid conversion: Leaders 66.1%, Average 52.0%, Followers 35.8%, described as applying to
"D2C subscription brands" generally (streaming, sports, wellness, creators, gaming, memberships),
derived from "millions of subscription conversion touchpoints across Cleeng's global client base."

**Outcome:** SOURCED as [S7], MEDIUM confidence (real, dated, named methodology, but not
hardware-specific and not FlowState-specific by construction). **Assignment to segment is MA9**: the
Followers tier (35.8%) assigned to Segment 1 (student athletes, shorter/more price-sensitive
subscription horizon), the Average tier (52.0%) assigned to Segment 2 (working professionals,
steadier discretionary spending) — the values are real; which segment receives which value is a
disclosed modeling choice, not itself sourced.

## P08 — TV awareness/recall rate

**Searched:** "average TV ad recall rate percent benchmark advertising awareness study"

**Fetched directly:** `https://adwave.com/resources/tv-brand-awareness-effectiveness` — confirmed:
"TV generates 23% brand awareness lift vs. 9% for digital advertising" attributed to Nielsen, 2025;
"TV delivers a 2.5x advantage over digital for brand awareness building."

**Outcome:** SOURCED as [S8], MEDIUM confidence (supplemental — informs MA6's basis rather than
supplying a direct value). MA6 (TV awareness rate, 22%) set just under the real 23% lift figure to
reflect that S8's figure describes lift for advertisers generally, while FlowState is a brand-new,
previously-unadvertised product with no existing baseline awareness to lift from.

## P09 — Radio awareness rate; interest rate (aware → visits site), all passive channels;
## channel-by-segment audience skew

**Searched:** none attempted as further live web searches — confirmed by direct reasoning, the
same category finding made explicit above for MA1, that a per-channel awareness-to-website-visit
rate and a channel-by-two-fictional-segment audience skew for this specific hypothetical campaign
cannot exist as citable external datasets. A general search for a radio-specific recall/awareness
benchmark comparable to S8's TV figure did not surface a usable, fetchable source distinct from the
CPM/CPP searches already run in P03.

**Outcome: NOT FOUND, correctly not searched further. Exit chosen: Modeling Assumptions (MA5, MA7,
MA8)**, disclosed in Appendix E with their basis and sensitivity. MA8 (interest rate) is
deliberately left **unresolved for the print channel only** in `case.md` Appendix D — this is the
case's SPEC §3 T4 requirement ("at least one quantity the student must assume and justify") made
concrete: the case supplies the reasoning pattern for the other four channels, and Challenge D1
explicitly requires the student to produce and justify their own print-channel value using that
same pattern, rather than being handed one.

## Revision pass — 2026-09-11: deepen Appendix B and Appendix D market/behavioral grounding

Requested by the case author after the researched draft: Appendix B (the two segments) and Appendix D
(funnel rates) leaned on 9 sources doing double duty, several supplemental. Goal: add real, live-fetched,
cited data specific to youth vs. adult wearable/wellness engagement and category market sizing, and find a
tighter, more category-specific real source for a funnel-rate Modeling Assumption if one exists — a strict
improvement per SPEC §5, not padding.

## P10 — Smart water bottle / hydration-tech category market sizing

**Searched:** "smart water bottle market size 2026 growth rate"

**Fetched directly:** `https://www.fortunebusinessinsights.com/smart-water-bottle-market-115917` —
confirmed: "The smart water bottle market size was valued at USD 550.99 million in 2025," "projected to
grow from USD 585.65 million in 2026 to USD 1,043.88 million by 2034, exhibiting a CAGR of 7.49%," and
"North America dominated the smart water bottle market with a market share of 37.79% in 2025" (~$208.22
million).

**Other results not fetched:** Straits Research, MarketResearchFuture, market.us, IndustryARC,
TowardsPackaging, ResearchNester, FutureMarketInsights, MarkWideResearch, IndustryResearch.biz all returned
materially different market-size and CAGR figures for the same category (ranging $195M–$3.2B and
7.5%–20.2% CAGR) — a classic market-research-firm methodology spread. Not fetched or cited; only the one
directly-fetched, directly-quoted figure (Fortune Business Insights) is used, consistent with the "never
cite a URL you did not fetch" rule and to avoid presenting a cherry-picked number from an unfetched page.

**Outcome:** SOURCED as [S10], MEDIUM confidence, supplemental — real category-level market context added
to Appendix B, not an input to any of this case's arithmetic.

## P11 — Wearable-device ownership by age

**Searched:** "Gen Z vs adults fitness wearable ownership percent by age 2026 survey"

**Fetched directly:** `https://www.sonarhealth.co/blog/wearable-adoption-2026/` — confirmed, citing a 2026
Pew Research Center survey: "37% of U.S. adults have a smartwatch," rising to "44%" among "adults ages 18
to 49." No further age-bracket breakdown (e.g. a separate 13–22 or 45+ split) is present on this page.

**Outcome:** SOURCED as [S11], MEDIUM confidence, supplemental — used in Appendix B to note that the
18–49 ownership-rate gap overlaps the older half of Segment 1 and all of Segment 2. Not a hardware- or
hydration-specific figure, and not an input to case arithmetic.

## P12 — Wellness spending share by generation

**Searched:** "sports nutrition hydration supplement spending by age group survey Gen Z millennials"

**Fetched directly:** `https://www.emarketer.com/content/gen-z--millennials-spend-more-on-wellness-products-than-older-cohorts`
— confirmed, citing McKinsey's Future of Wellness survey (9,000+ consumers across the US, UK, Germany, and
China, published 18 Jun 2025): "Gen Z and millennials comprise approximately 36% of the US adult
population but account for around 41% of annual wellness spending," while "consumers 58+ make up nearly
35% of the population yet drive only 28% of US wellness spending." The article states younger consumers
spend disproportionately on discretionary wellness items (wearables, mindfulness apps, self-massage
tools) versus older generations' focus on essentials — no specific dollar figure for hydration-tech or
smart bottles by name.

**Outcome:** SOURCED as [S12], MEDIUM confidence, supplemental — used in Appendix B to support that
younger generations (overlapping Segments 1 and 2) spend disproportionately on discretionary wellness
categories generally. Not a hydration-specific figure and not an input to case arithmetic.

**Also searched, not cited:** "student athletes youth sports nutrition product spending statistics 2026"
surfaced real findings (e.g. Aspen Institute's $1,016 average family youth-sports spend, NFHS
participation counts, supplement-usage rates among student-athletes) but nothing specific to hydration
wearables/smart bottles or directly relevant to the funnel/segment figures already in the case; not
fetched or used, to avoid padding Appendix F with decorative citations that don't inform any claim.

## P13 — Category-specific subscription trial-to-paid benchmark (search for a tighter MA9 cross-check)

**Searched:** "connected fitness hardware subscription trial to paid conversion rate benchmark wearable"

**Fetched directly:** `https://adapty.io/blog/health-fitness-app-subscription-benchmarks/` — confirmed,
from Adapty's State of In-App Subscriptions 2026 report (16,000+ apps, $3B+ subscription revenue
analyzed, published 27 Mar 2026): Health & Fitness weekly subscriptions with a free trial convert
trial-to-paid at 42.2%; install-to-trial conversion is 9.5% globally and 14.5% in North America.

**Evaluated as a replacement for S7/MA9, decided against full replacement:** Adapty's figure is
app-subscription data (not hardware-plus-cartridge-subscription specific) and is a single blended
Health & Fitness figure, not broken out by age/segment the way S7's Leaders/Average/Followers tiers are —
replacing S7 outright would lose the segment-level differentiation Appendix D's adoption-rate step depends
on, and would require recomputing every downstream total for a swap that is not clearly *more* correct,
only differently-scoped. **Exit chosen: supplemental cross-check.** [S13] is cited in Appendix D and
Appendix E (MA9) as a real, dated, category-specific data point that falls between the two tier values
already in use (35.8% and 52.0%), corroborating both rather than replacing either. This is disclosed as a
supplement, not presented as if it changed the underlying computation — no case.md funnel number, no
case.json margin_pct, and no FACILITATOR.md figure changed as a result of this addition.

## Summary table

| ID | Placeholder | Resolution | Value | Confidence |
|---|---|---|---|---|
| P01 | SEO CPC and CVR | SOURCED (S1) | $5.00 CPC; 6.8% CVR | MEDIUM |
| P02 | TV cable CPM range | SOURCED (S2), point-values are MA2/MA3 | $10-$30 range; $14/$24 chosen | MEDIUM |
| P03 | Radio CPM | ASSUMPTION (MA4, cross-checked vs. S3) | $10.00 | n/a (assumption) |
| P04 | Magazine CPM | SOURCED (S4) | $63.00 (100k-circ tier) | MEDIUM |
| P05 | Total launch budget | ASSUMPTION (MA1, informed by S5) | $60,000 | n/a (assumption) |
| P06 | Site conversion rate (non-SEO trial step) | SOURCED (S6) | 1.17% | HIGH |
| P07 | Trial-to-paid rate, by segment | SOURCED (S7); assignment is MA9 | 35.8% / 52.0% | MEDIUM |
| P08 | TV awareness rate basis | SOURCED, supplemental (S8); MA6 uses it | 22% (MA6, informed by 23%) | MEDIUM (supplemental) |
| P09 | Radio awareness; interest rates; segment skew | ASSUMPTION (MA5, MA7, MA8) | see Appendix E | n/a (assumption) |
| P10 | Smart water bottle category market size/CAGR | SOURCED (S10), supplemental | $585.65M (2026), 7.49% CAGR | MEDIUM (supplemental) |
| P11 | Wearable ownership by age | SOURCED (S11), supplemental | 37% all adults; 44% ages 18-49 | MEDIUM (supplemental) |
| P12 | Wellness spending share by generation | SOURCED (S12), supplemental | GenZ+Mill. 36%/41%; 58+ 35%/28% | MEDIUM (supplemental) |
| P13 | Health & Fitness trial-to-paid benchmark (MA9 cross-check) | SOURCED (S13), supplemental | 42.2% trial-to-paid | MEDIUM (supplemental) |

Sourced: 5 figures used directly as real numeric values (S1's CPC+CVR, S2's range informing two
point-picks, S4, S6, S7). Supplemental: 6 sources (S3, S8, S10, S11, S12, S13) inform an assumption's
basis or add real market/behavioral context without being a value used directly in case arithmetic;
S9 is vocabulary-only. Assumption: 9 Modeling Assumption records (MA1–MA9) resolve every figure that
could not be directly sourced, one of them (MA8's print-channel portion) deliberately left open for
the student rather than resolved by the case author. Dropped: 0. Open: 0.

**2026-09-11 revision pass total:** 4 new sources fetched and cited (S10-S13), all live-confirmed;
0 dead ends requiring citation (P10's alternative market-sizing pages and P12's youth-sports-spending
search were reviewed but correctly not cited, per the notes under P10/P12 above, since either the
figures conflicted without a way to arbitrate among them or nothing found was relevant to a claim
already in the case). No case.md funnel number, case.json margin_pct/options/balance field, or
FACILITATOR.md figure changed as a result of this pass — see the P13 note for why S13 was used as a
corroborating cross-check rather than a replacement value.

## Revision pass — 2026-09-11 (second pass): tighten Appendix A channel-cost sourcing

Requested by the case author after the market-research deepening pass above: Appendix A (Channel Cost
Benchmarks) and its supporting Modeling Assumptions (MA2, MA3, MA4) rested on 3 sources doing a lot of
work with wide real ranges ($10-$30 cable CPM covering both TV rows; radio had no exact CPM source at
all). Goal: find more specific real sources for (1) sports/fitness-category cable TV cost, (2) general
broadcast/daytime TV cost, (3) drive-time radio cost, and (4) SEO/paid-search cost specific to a
wearables/connected-fitness or consumer-hardware category — replacing a Modeling Assumption's range
where a genuinely tighter real source exists, corroborating (not replacing) where it doesn't.

## P14 — Sports/fitness-specific cable TV CPM

**Searched:** "sports network cable TV advertising cost CPM ESPN 2026"

**Fetched directly:**
- `https://www.designrush.com/agency/ad-agencies/trends/tv-advertising-cost` — confirmed: "Cable TV
  Ads average $23.30 CPM," no ESPN- or sports-network-specific CPM broken out. Published 21 Jan 2025,
  updated 9 Dec 2025.
- `https://www.hohumproductions.com/espn-advertising-sales/` — an ad-sales agency page claiming to
  represent ESPN; quotes only vague marketing copy ("starting at under $5.00 an ad," "under $1.00 per
  ad" for national radio/TV) with no verifiable CPM methodology or rate card. Rejected — not a usable
  or credible figure, and internally inconsistent with every other TV-cost source found in this case.
- `https://www.vibe.co/blog/how-to/tv-advertising-cost` — confirmed a real, distinct figure for
  **live sports (streaming)**: "$40-$80+ CPM," attributed to "category and event premium." This prices
  streaming inventory, not the cable package this case's TV Sports/Fitness row models. Published 10 Jun
  2026.

**Outcome: no sports-cable-specific CPM found; exit chosen: corroboration, not replacement.** MA2 stays
$14.00 within S2's existing $10-$30 cable range. The Vibe.co live-sports-streaming figure is cited as
[S14] (supplemental) — it corroborates that sports content commands a real premium in at least one other
ad format, but streaming and cable are bought and priced on different models, so it does not replace
MA2's cable-sourced value. This mirrors the discipline the prior pass used for S13 (Adapty): a real,
dated, on-topic source that corroborates rather than replaces.

## P15 — General broadcast/daytime TV CPM

**Searched:** "daytime broadcast TV advertising cost CPM 2026"

**Fetched directly:**
- `https://www.vibe.co/blog/how-to/tv-advertising-cost` — confirmed, published 10 Jun 2026: "Linear
  national broadcast: $25-$40 CPM," distinct from "Linear local broadcast: $5-$15 CPM" and the live-sports
  streaming figure above. This is the first source found in this case's research that prices broadcast
  separately from cable, rather than lumping both under one range the way S2 does.
- `https://www.designrush.com/agency/ad-agencies/trends/tv-advertising-cost` — confirmed: "Broadcast TV
  Ads average around $47.14 CPM for a 30-second spot," also distinct from its own cable figure ($23.30
  CPM). Published 21 Jan 2025, updated 9 Dec 2025.
- `https://adwave.com/resources/how-much-does-tv-advertising-cost` — confirmed only a blended "$20-$50
  CPM" range for connected TV generically; not broadcast-specific enough to use over the two sources
  above. Not cited.

**Outcome: SOURCED as [S14] (primary value) and [S15] (corroboration) — MA3 narrowed, a strict
improvement per SPEC §5.** Both S14 and S15 independently and specifically distinguish broadcast TV
pricing from cable TV pricing, and both put broadcast meaningfully above the $10-$30 cable range this
case's MA2/MA3 previously shared. **MA3 retuned from $24.00 to $30.00** — chosen in the lower-middle of
S14's $25-$40 national-linear-broadcast range (more recent, 2026, and specifically labeled "broadcast"
rather than a blended average), corroborated directionally by S15's higher $47.14 figure. This is not a
Solstice-Labs-specific assumption being replaced by another assumption — it is one real range (undifferentiated
cable/broadcast, S2) being replaced by a tighter, broadcast-specific real range (S14), the exact kind of
improvement SPEC §5 calls a "plausible number is not a true number."

## P16 — Drive-time radio CPM

**Searched:** "radio drive time advertising CPM rate 2026"

**Fetched directly:**
- `https://www.radioadvertisinghome.com/radio-advertising-cost-rates-cpm-what-to-pay/` — confirmed the
  publisher's own explicit statement: "Berk Marketing does not publish rate estimates, because a rate is
  only real once a specific station returns availability for specific dates." Confirms drive-time
  commands "premium rates" qualitatively, no number given. This is the same finding the original P03 pass
  already made via a sibling page from the same publisher (cited as S9) — not re-cited as a separate
  Appendix F entry to avoid a redundant citation for the same non-finding.
- `https://www.amraandelma.com/radio-show-marketing-statistics/` — confirmed, citing Westwood One's 2026
  Cost-Efficiency Analysis and Arbitron's 2026 In-Car Audio Report: "Westwood One's 2026 analysis pegs
  radio's average CPM at $4.78 across the top 50 U.S. markets," and "commuters aged 18-54 spend 91.3% of
  in-car audio time on radio," averaging "52 minutes per day" in-vehicle. No drive-time-specific CPM
  given — $4.78 is a cross-daypart average.

**Outcome: still NOT FOUND as a direct, citable, drive-time-specific CPM; exit chosen: corroboration, not
replacement.** MA4 stays $10.00. [S16] (Amra & Elma / Westwood One) is cited as supplemental corroboration:
its $4.78 average sits *below* MA4's $10.00 figure, which could look like grounds to lower the assumption
— but the same source's own drive-time-captivity data (91.3% in-car radio share, 52 min/day) and a second,
independent radio-industry page (Berk Marketing, above) both confirm drive-time is a premium daypart priced
above the blended average, so $10.00 remains a plausible above-average assumption. Replacing it with the
lower blended figure would have been a regression, not an improvement — the disclosed reasoning that keeps
MA4 unchanged is itself the finding.

## P17 — Wearables/connected-fitness-hardware-specific SEO CPC

**Searched:** "smartwatch fitness tracker wearable device Google Ads CPC cost per click consumer
electronics benchmark"; "wearables Google Shopping Ads CPC benchmark category 2026"

**Fetched directly:**
- `https://www.webtonic.io/blog/e-commerce-google-ads-statistics` — confirmed, published 18 Jul 2026,
  updated 4 Sep 2026: "Sports & Fitness" Search CPC $1.45, "Electronics & Tech" Search CPC $1.85 — no
  wearables- or connected-fitness-hardware-specific line item.
- `https://foundrycro.com/blog/google-shopping-benchmarks-by-category-2026/` — confirmed, published 30
  Apr 2026: Electronics/Consumer Tech Shopping CPC $1.42, also no wearables-specific breakout. Fetched
  and reviewed but not separately cited in Appendix F — it would only restate the same "no
  wearables-specific number exists, and the figures that do exist conflict with S1" conclusion Web Tonic
  already supports, and citing both risks padding Appendix F with a second source for one finding (the
  same discipline P10 used when it fetched but did not cite 9 conflicting market-sizing pages).

**Outcome: NOT FOUND as a wearables/hardware-specific SEO CPC; exit chosen: corroboration considered and
explicitly rejected as a replacement.** S1's $5.00 Health & Fitness CPC (PPC Chief) stays the value used.
Web Tonic's own Sports & Fitness figure ($1.45) conflicts with PPC Chief's Health & Fitness figure ($5.00)
by more than 3x for what are adjacent, largely overlapping categories — a cross-publisher spread of the
same kind this case already flagged for S10's smart-water-bottle market sizing (9 sources ranging
$195M-$3.2B for the same category). Given that spread, and that neither Web Tonic's Electronics & Tech
figure ($1.85) nor Foundry CRO's Shopping-network Electronics figure ($1.42) isolates wearables or
connected-fitness hardware as its own category, replacing S1's more specific Health & Fitness figure with
either would trade a directly-relevant, single-category number for a broader, conflicting, and less
relevant one — not a strict improvement. Cited as [S17], supplemental, with the rejection reasoning stated
in Appendix A/E rather than left implicit.

## Math recomputed after MA3's retune

Because MA3 (TV — General broadcast CPM) is used directly in D1's reach calculation (reach =
budget ÷ CPM × 1,000) and its retune from $24.00 to $30.00 changes only the audience reached, not any
funnel conversion rate, the following were recomputed and updated in `FACILITATOR.md` and `case.json`:

- TV — General subscribers: Plan A 91.00 → **72.80**; Plan B 30.33 → **24.27**
- Plan A total: 348.04 → **329.83**; Plan B total: 292.57 → **286.50**
- Margin: 15.9% → **15.1%** (still comfortably inside SPEC §2's ~20% balance cap)
- Cost per acquisition: Plan A $172.39 → **$181.92**; Plan B $205.08 → **$209.42**
- D4 broadcast-bucket yield: 0.006102 → **0.005722** subscribers/dollar; precision-bucket yield unchanged
  (0.004385, since SEO and print are untouched by this pass). Break-even split: x≈$17,166/y≈$42,834 →
  **x≈$17,498/y≈$42,502**; reallocation needed to tie: $30,834 → **$30,502**
- **Twist effect materially changed:** at the same disclosed +50% seasonal TV-CPM premium, the higher
  baseline MA3 value pushes Plan A's TV-General exposure high enough that the twist now **flips the
  winner** (Plan B pulls ahead by ~1.3%, A≈259.82 vs B≈263.16), where the identical +50% premium
  previously only narrowed the margin to ~1.8% without flipping it. The algebraic crossover point itself
  moved from ~+57% to ~+44.8% CPM premium. This is disclosed in `case.json`'s `balance.twist_effect` and
  `sensitivity_disclosure[]`, and in `FACILITATOR.md`'s twist section and Deep Conflict Thread 2 — never
  in `case.md` or any student-facing text.

No other case.md figure, Modeling Assumption value, or funnel-conversion rate changed. `standards[]` and
`new_coverage[]` are untouched — this pass is about sourcing quality and one constrained retune, not new
math content.

## Summary table (this pass)

| ID | Placeholder | Resolution | Value | Confidence |
|---|---|---|---|---|
| P14 | Sports/fitness-specific cable TV CPM | NOT FOUND — corroboration only (S14, live-sports-streaming) | MA2 unchanged, $14.00 | n/a (assumption) |
| P15 | General broadcast/daytime TV CPM | SOURCED (S14), corroborated (S15) — MA3 narrowed | $30.00 (was $24.00) | MEDIUM |
| P16 | Drive-time radio CPM | NOT FOUND — corroboration only (S16) | MA4 unchanged, $10.00 | n/a (assumption) |
| P17 | Wearables/hardware-specific SEO CPC | NOT FOUND — corroboration considered and rejected (S17) | S1 unchanged, $5.00 CPC | n/a (kept sourced) |

**2026-09-11 second revision pass total:** 4 new sources fetched and cited (S14-S17), all live-confirmed;
2 dead ends reviewed but correctly not cited (hohumproductions.com's uncredible ESPN sales-page figures,
and Foundry CRO's Shopping-CPC page, redundant with Web Tonic's already-cited finding). 1 genuine
replacement (MA3, TV-General CPM, $24.00 → $30.00) and 3 corroboration-only additions (MA2, MA4, and S1's
SEO CPC all kept unchanged with their "considered and rejected as replacement" reasoning stated
explicitly). Downstream math recomputed and kept internally consistent across case.md, case.json, and
FACILITATOR.md — see "Math recomputed after MA3's retune" above.

## Next step

Run `case-readiness` on `flow-state`.
