# Case Study: The Attribution Sample

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

Derek Okafor has four browser tabs open and one spreadsheet that won't stop recalculating.

It's Friday, 3:40 p.m., and the weekly attribution report is due in Driftline Games' inbox by Monday, 9:00 a.m. — the report that tells Driftline which of its ad channels actually delivered real players for *Emberfall Kingdoms*, and which ones delivered clicks that never became installs at all. Derek doesn't set Driftline's ad budget. He just supplies the number Driftline's marketing lead reads out loud in Monday's 9:15 stand-up, the number that decides which channels get funded next month and which ones get cut.

The pooled sample is already queued — one clean, randomized pull across every click Emberfall Kingdoms' campaigns generated this week, ready to run tonight. It's fast. It's the way Derek's team has always done it.

The other queue sits untouched: four separate pulls, one per ad channel, built so that not a single channel — not even the small one — goes unchecked.

Derek's cursor sits over the "Run" button on the first queue. Behind him, a Slack notification banner slides in from Driftline's marketing lead: something about "the influencer channel" and "board deck next week."

Derek doesn't open it yet.

---

## Background

Derek Okafor is a Performance Marketing Analyst at Verafly, an ad-tech install-attribution platform that mobile game studios plug into so they can tell which of their advertising channels are actually converting ad clicks into real, verified game installs, versus clicks that were never real users at all — the fraud, bots, and misattributed traffic that inflate a channel's apparent performance (*Verafly is a scenario construction for this case; there is no real company by this name*). Derek's client this week is Driftline Games, whose mobile title *Emberfall Kingdoms* runs paid user-acquisition campaigns across four kinds of ad placement (SEE APPENDIX A).

Verifying a single ad click's true install status — confirming a real device actually installed and opened the game, not a bot or a misattributed organic install claimed by a paid campaign — takes real analyst time: cross-referencing the click log against device-level install records, one click at a time (SEE APPENDIX E). Derek cannot verify every click Emberfall Kingdoms generated this week; he has to sample.

**The Pooled Random Sample** draws one simple random sample of clicks from the entire week's pooled click stream, ignoring which channel each click came from. It is fast to set up — one query against one unified log — and it verifies the same total number of clicks as the alternative (SEE APPENDIX B).

**The Channel-Stratified Sample** deliberately draws a separate random sample from each of the four ad-placement channels, with a guaranteed minimum sample size in the smallest channel, before combining the results. It requires building and reconciling four separate pulls — one per channel's own ad-network dashboard — instead of one pooled pull (SEE APPENDIX C).

The four channels do not carry equal weight or equal risk. One of them — the Influencer/Affiliate channel — generates only a small share of this week's total clicks, but Driftline's marketing lead has flagged it as a channel under particular scrutiny heading into next week's board deck (SEE APPENDIX A). Industry-wide, install-fraud rates vary sharply by channel type, and channels that route through affiliates and influencers run some of the least predictable rates of any channel category (SEE APPENDIX D and APPENDIX G). A channel this small, sampled at random alongside everything else, risks landing so few verified clicks that its estimated true-install rate is barely more than a guess (SEE APPENDIX E).

Derek has a fixed weekend verification budget before Monday's 9:00 a.m. deadline, and every hour spent verifying clicks is an hour that cannot be spent on anything else this weekend (SEE APPENDIX A). Neither of Derek's two options is a multistage design — both draw directly from clicks rather than first selecting a subset of ad placements or campaigns to sample within — but every fraud-rate figure behind this decision is grounded in real, published industry data, not invented for this case (SEE APPENDIX F). The full standards bridge for this case is in Appendix H.

---

## Dilemma

You are Derek Okafor.

Do you:

**A.)** Run **the Pooled Random Sample** — one simple random sample of clicks drawn from the entire week's pooled stream, fast to set up but liable to draw almost nothing from the small Influencer/Affiliate channel **OR**

**B.)** Run **the Channel-Stratified Sample** — four separate random samples, one guaranteed per channel including a real minimum for the small one, at the cost of more analyst setup time and a much tighter fit against Monday's deadline

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A Pooled Random Sample precision table.** Using Appendix E's per-channel expected sample counts under the Pooled Random Sample (Option A), compute the standard error (in percentage points) of each channel's estimated true-install rate. Identify which channel's estimate is too imprecise to trust, and explain why in terms of its sample size.
- **D2 — A Channel-Stratified Sample design.** Using Appendix C's minimum-floor-plus-proportional-remainder allocation method, compute each channel's stratified sample size (they must total the same 400 clicks as Option A) and the resulting standard error for each channel. Show how the small channel's precision changes compared to D1.
- **D3 — An analyst-hours cost table.** Using Appendix E's per-channel verification time and Appendix B/C's setup-time figures, compute total analyst-hours for each option (setup plus verification), and compare both totals against Appendix A's weekend verification-hours budget.
- **D4 — A primary-metric comparison.** Using D1/D2's channel-level standard errors, compute each option's pooled (whole-report) standard error in percentage points, then divide by D3's total hours to get each option's attribution error per analyst-hour. State which option wins on this metric and by what margin.
- **D5 — A recommendation memo.** Recommend Option A or Option B to Derek, defended with D4's primary-metric numbers, D1/D2's small-channel precision gap, and D3's hours-budget comparison — including whether the option that wins on D4 is still the option you'd recommend once the small channel's precision and the deadline risk are weighed in.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

## Appendix A: Verafly's Weekly Attribution Verification Constraints

| Quantity | Value |
|---|---|
| Report deadline | Monday, 9:00 a.m. (from Friday, 3:40 p.m.) [MA1] |
| Weekend analyst-hours available for verification before the deadline | 13 hours [MA2] |
| Total ad clicks generated by Emberfall Kingdoms' campaigns this week (all four channels, pooled) | 500,000 [MA3] |
| Number of ad-placement channels | 4 — Self-Attributing Networks (SAN), Programmatic/DSP Ad Networks, Owned & Boosted Media, Influencer/Affiliate [MA4] |
| Share of this week's clicks from the Influencer/Affiliate channel (the small, high-value one) | 2% [MA4] |

*Note: Verafly, Driftline Games, and Emberfall Kingdoms are scenario constructions for this case — none are real companies or products.*

---

## Appendix B: Option A — The Pooled Random Sample

| Spec | Value |
|---|---|
| Sampling method | Simple random sample, drawn from the entire week's pooled click stream (all channels combined, channel identity ignored at draw time) |
| Total sample size | 400 clicks [MA5] |
| Setup time | 0.5 hours — one query against one unified click log [MA6] |
| Expected per-channel draws (in expectation, proportional to each channel's share of total clicks) | SAN 248, DSP 104, Owned 40, Affiliate 8 (SEE APPENDIX A for channel shares) |

---

## Appendix C: Option B — The Channel-Stratified Sample

| Spec | Value |
|---|---|
| Sampling method | Stratified sample — one independent random draw per channel, with a guaranteed minimum sample size in the smallest channel |
| Minimum sample size, Influencer/Affiliate channel (the floor) | 40 clicks [MA7] |
| Remaining 360 clicks allocated proportionally among the other three channels, by their relative share (SAN : DSP : Owned = 62 : 26 : 10) | SAN 227, DSP 96, Owned 37 |
| Total sample size (all four channels) | 400 clicks — same total as Option A |
| Setup time | 1.4 hours — four separate pulls, one per channel's own ad-network dashboard, reconciled into one combined dataset [MA8] |

---

## Appendix D: Per-Channel True-Install-Rate Assumptions

| Channel | Fraud rate assumed | True-install rate used | Basis |
|---|---|---|---|
| Self-Attributing Networks (Meta, Google, TikTok, Apple Search Ads) | 5% | 95% | [MA9] — anchored to the real, published self-attributing-network fraud-rate range, 1–8% [S2] |
| Programmatic/DSP Ad Networks | 15% | 85% | [MA10] — anchored to the real, published Tier-1 DSP fraud-rate range, 12–20% [S2] |
| Owned & Boosted Media | 11% | 89% | [S3] — matches the real, directly reported figure for owned-media install fraud |
| Influencer/Affiliate (the small, high-value channel) | 15% | 85% | [MA11] — anchored to the real, published influencer/CPI-network fraud-rate range, 15–30% (low end used); this channel's real range is the widest of the four, meaning the true figure could plausibly run much higher [S2] |

---

## Appendix E: Sample Allocation, Verification Time, and Standard Error by Channel

*True-install rates from Appendix D. Standard error of a sampled proportion computed as
√(p(1−p)/n).*

| Channel | Share of clicks | Per-click verification time | Option A: n | Option A: SE (pp) | Option B: n | Option B: SE (pp) |
|---|---|---|---|---|---|---|
| SAN | 62% | 1 min [MA12] | 248 | 1.38 | 227 | 1.45 |
| DSP | 26% | 2 min [MA12] | 104 | 3.50 | 96 | 3.64 |
| Owned & Boosted | 10% | 2 min [MA12] | 40 | 4.95 | 37 | 5.14 |
| Influencer/Affiliate | 2% | 5 min [MA12] | 8 | **12.62** | 40 | **5.65** |
| **Total / verification time** | 100% | — | **400** | **9.6 hr** | **400** | **11.55 hr** |

*Per-click verification time is longer for Owned/Boosted and Influencer/Affiliate because those
channels lack the direct attribution-API access the two Self-Attributing/Programmatic channels
have, requiring manual log cross-referencing instead.*

---

## Appendix F: Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Global average mobile app install fraud rate, all channels pooled | 13.2% | AppsFlyer — ["Global exposure to app install ad fraud drops 30%"](https://www.appsflyer.com/company/newsroom/pr/global-exposure-install-ad-fraud/) | H1 2020 | HIGH |
| S2 | Install-fraud rate ranges by ad-channel type (self-attributing networks, Tier-1 DSPs, influencer/CPI networks) | SAN 1–8%; Tier-1 DSP 12–20%; Influencer/CPI networks 15–30% | RocketShip HQ, summarizing AppsFlyer's fraud data — ["AppsFlyer's fraud data disagrees"](https://www.rocketshiphq.com/appsflyer-mobile-fraud-report-2025-summary/) | 2026-03-22 | MEDIUM |
| S3 | Owned-media install-fraud rate, year-over-year | Rose 221% YoY, from 3.4% to 11% | AppsFlyer — ["Organic Traffic Is Now the Top Mobile Ad Fraud Channel"](https://www.appsflyer.com/company/newsroom/pr/organic-traffic-ad-fraud/) | 2026 (State of Fraud for Marketers 2026, YoY through Q1 2026) | HIGH |
| S4 | Share of all fraudulent installs coming from affiliate channels | "Nearly 40%" | AppsFlyer — ["Organic Traffic Is Now the Top Mobile Ad Fraud Channel"](https://www.appsflyer.com/company/newsroom/pr/organic-traffic-ad-fraud/) | 2026 | HIGH |
| S5 | iOS install-fraud rate, year-over-year | Fell from 17.5% (Q1 2025) to 11.7% (Q1 2026), a 33% YoY drop | AppsFlyer — ["Organic Traffic Is Now the Top Mobile Ad Fraud Channel"](https://www.appsflyer.com/company/newsroom/pr/organic-traffic-ad-fraud/) | Q1 2026 | HIGH |

---

## Modeling Assumptions

> These figures are **not sourced** from Verafly, Driftline Games, or Emberfall Kingdoms (all
> fictional) or, in most cases, from any external record at all. They are stated scenario
> assumptions chosen by the case author, several of them anchored to the real, published
> fraud-rate ranges in Appendix F. A Hero may challenge any of them in discussion — that is a
> legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Report deadline framing | Friday 3:40 p.m. → Monday 9:00 a.m. | Matches the Overview's Friday-afternoon framing. | None — flavor only, not load-bearing. |
| MA2 | Weekend analyst-hours budget | 13 hours | No public per-analyst weekend-verification-hours standard exists; chosen to be tight enough that Option B (12.95 hr, Appendix E/F) barely fits, while Option A (10.1 hr) leaves comfortable slack. | Directly shapes the deadline-risk argument in `balance.argument_a`/`argument_b`, but does not change which option wins the primary metric (D4) — see `case.json.balance.margin_note`. |
| MA3 | Total weekly pooled click volume | 500,000 clicks | Illustrative scale, consistent with a real mid-size mobile UA campaign's weekly volume; not load-bearing for any deliverable's math (both options' sample sizes are fixed at 400, independent of total population size, since both treat each channel as effectively unlimited relative to its sample). | None — flavor/scale only. |
| MA4 | Channel count, names, and click-volume shares (SAN 62%, DSP 26%, Owned 10%, Affiliate 2%) | As stated | Scenario design: four channel *types* match real, named categories from Appendix F's sources (S1–S5); the specific share split is chosen so the Influencer/Affiliate channel is genuinely small (2%) but not zero, matching the case's "small, high-value channel" premise. | **HIGH** — this is the split that makes Option A's Affiliate-channel sample (expected n=8) so imprecise (SE 12.62pp, Appendix E) in the first place. A larger Affiliate share would narrow the gap between the two options; see `sensitivity_model.py`. |
| MA5 | Option A total sample size | 400 clicks | Illustrative — a standard weekly SRS batch size for Derek's team. | Sets both options' total verification workload equal (400 clicks each), isolating the comparison to *allocation method*, not total effort. |
| MA6 | Option A setup time | 0.5 hours | One query against one already-unified click log — the fastest possible setup for any sampling design. | Small effect on Option A's total hours (10.1 hr); does not flip D4's winner on its own — see `sensitivity_model.py`. |
| MA7 | Option B minimum sample floor, Affiliate channel | 40 clicks | Chosen so the Affiliate channel's standard error (5.65pp, Appendix E) is tight enough to be useful for a budget decision, versus Option A's 12.62pp (barely better than a coin flip at that scale). | **HIGH** — this is the deliberate design choice that both (a) protects the small channel and (b) drives Option B's extra verification time. Raising the floor further would improve Option B's small-channel precision but cost more hours; see `sensitivity_model.py`. |
| MA8 | Option B setup time | 1.4 hours | Four separate pulls (one per channel's own ad-network dashboard/API), each requiring its own query and schema reconciliation into one combined dataset, versus Option A's single pooled query. | Meaningful driver of Option B's total hours (12.95 hr) and of how close Option B runs to MA2's 13-hour budget; see `sensitivity_model.py`. |
| MA9 | SAN fraud rate | 5% (true-install rate 95%) | Anchored to the real, published SAN fraud-rate range, 1–8% [S2]; 5% chosen near the middle of that range. | Low — SAN is the largest channel (62% share) and best-estimated under either option (Appendix E), so small changes here barely move the pooled SE. |
| MA10 | DSP fraud rate | 15% (true-install rate 85%) | Anchored to the real, published Tier-1 DSP fraud-rate range, 12–20% [S2]; 15% chosen near the middle of that range. | Low-moderate — DSP is the second-largest channel (26% share); moves the pooled SE more than SAN but less than the two smaller channels. |
| MA11 | Affiliate fraud rate | 15% (true-install rate 85%) | Anchored to the real, published influencer/CPI-network fraud-rate range, 15–30% [S2]; the **low end** of that range was chosen, meaning the true rate could plausibly be twice as bad — exactly the kind of uncertainty a badly-undersampled estimate (Option A, SE 12.62pp) cannot distinguish from noise. | **HIGH** for the qualitative argument (this is the channel whose real fraud rate is least certain industry-wide, per S2's own range), though it does not change `margin_pct` directly, since Appendix E's SE formula depends on n, not on which point within the real range was chosen. |
| MA12 | Per-click verification time by channel (SAN 1 min, DSP 2 min, Owned 2 min, Affiliate 5 min) | As stated | SAN and DSP have direct attribution-API access (fast, semi-automated cross-check); Owned/Boosted and Affiliate/Influencer traffic lacks that access and requires manual log cross-referencing. | Affiliate's 5-minutes-per-click figure is the single biggest driver of Option B's extra verification time (Appendix E) — Option B verifies 40 Affiliate clicks at 5 min each (200 min) versus Option A's 8 (40 min); see `sensitivity_model.py`. |

---

## Appendix G: Real-World Fraud-Rate Context

| Item | Value |
|---|---|
| Global average mobile app install fraud rate (all channels pooled, historical anchor) | 13.2% [S1] |
| Real, published range of install-fraud rates across self-attributing networks, Tier-1 DSPs, and influencer/CPI networks | 1% to 30%, a roughly 30x spread depending on channel type [S2] |
| Real, directly reported owned-media fraud-rate increase | 3.4% → 11% year-over-year [S3] |
| Real, directly reported share of all fraud coming from affiliate channels | Nearly 40% [S4] |
| Real, directly reported iOS install-fraud-rate trend | 17.5% (Q1 2025) → 11.7% (Q1 2026), a real industry-wide platform-level improvement — context for why this case's assumed channel-level rates (Appendix D) sit inside a moving, not static, real range [S5] |

*This appendix documents real, external, industry-wide benchmark figures — not figures reported
by Verafly, Driftline Games, or Emberfall Kingdoms, which are fictional. It supplies the real-world
scale and channel-to-channel spread that Appendix D's per-channel assumptions are anchored to.*

---

### Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Sample
- Population
- Sample Size
- Simple Random Sampling
- Stratified Sampling
- Percent

**"How to…" questions**

- How to find the percent of a number

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
