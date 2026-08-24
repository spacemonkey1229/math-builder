# Research Log — Investment Portfolio

Legacy conversion, 2026-08-22. The original source doc (`source/Y3/Additional/Stock Market/Case
Study_ Investment Portfolio.docx`) stated its own historical figures with "≈" (approximately) and no
citation — S&P 500 ≈10% return / ≈15% std dev / worst year ≈-37%; All-Weather ≈7-8% return / ≈8-10%
std dev / worst year ≈-13%. Per this project's constraint, these could not be carried forward
uncritically — they needed genuine re-sourcing or an explicit NOT FOUND. All of Benjamin's personal
financial facts ($100k income, 50% savings rate, debt-free, maxed retirement accounts, 40%-of-income
contribution plan) are case-given scenario data from the source doc, not real-world claims requiring
citation — no different from any other case's protagonist facts.

## P01 — Origin of Buffett's 90/10 allocation (Appendix A, and load-bearing for the Twist)

**Searched for:** confirmation and precise sourcing of the claim that Buffett's 90/10 allocation
originates from a specific, named, dated source (the original source doc didn't cite one at all).

**Found:** Buffett's 90/10 instruction (90% low-cost S&P 500 index fund, 10% short-term government
bonds) appears in Berkshire Hathaway's 2013 shareholder letter (published 2014), as instructions for
the trustee managing a testamentary trust for his wife's benefit — not a description of how Buffett
or Berkshire itself invests. Confirmed via WebSearch across multiple independent financial-press
sources (Yahoo Finance, others) all describing the same 2013/2014 letter and the same lump-sum,
no-further-contributions framing.

**Outcome:** SOURCED as `S1`, confidence MEDIUM (multiple consistent secondary sources describing a
real, dated primary letter; the primary letter itself was not directly fetched). Used in case.md
Appendix A (non-load-bearing framing) and load-bearing for FACILITATOR.md's Twist.

## P02–P16 — Backtested return, standard deviation, and maximum drawdown, both portfolios, all
holding periods (Appendix C)

**Searched for:** genuine, dated backtests of the two named portfolios' exact reference allocations
(not general "the stock market" statistics), at multiple holding periods, replacing the source doc's
uncited "≈" figures.

**Found:** LazyPortfolioETF.com — the same site the original 2021 source doc's own Appendix A/B
linked to — is still live and maintains a dated, methodology-documented backtest for both named
portfolios (90% VV / 10% SHY for Buffett; 30% VTI / 40% TLT / 15% IEF / 7.5% GLD / 7.5% DBC for
Dalio's All-Weather), current "as of 2026-07-31." Fetched full return, standard-deviation, and
Sharpe-ratio tables across 1/3/5/10/20/30-year and max (~156-year) horizons for both portfolios, plus
30-year maximum drawdown for each. Cross-checked internally: the site's own reported 20-year Sharpe
ratios (0.66 for both portfolios, independently) back-solve to an implied risk-free rate of
~1.50-1.52% for each — consistent with each other, which is reassuring evidence the site's own
Sharpe methodology is applied consistently across both portfolios, and became the basis for Appendix
D's MA1 assumption.

**Rejected:** Attempted `portfolioslab.com`'s equivalent pages for a second, independent data point —
both returned HTTP 403 (bot-blocked), not fetchable. Attempted `quantifiedstrategies.com` — both
pages returned only a bot-verification interstitial, no data retrievable. Did not pursue a primary
index-publisher source (e.g. S&P Dow Jones Indices' own published index return history) for the raw
S&P 500 alone, because the case needs the *blended, allocation-specific* portfolio return (90/10 with
bonds; the five-asset Dalio mix), which a raw index history cannot provide — this was a genuine
redesign decision: use a source that backtests the actual named allocations, not a proxy for one
piece of them.

**Outcome:** SOURCED as `S2`, confidence MEDIUM (transparent, documented backtest methodology —
real ETF prices where available, historical asset-class equivalents reconstructed for years before
each ETF's launch, dividends reinvested, annually rebalanced, no fees/taxes modeled — but a
third-party reconstruction, not each fund's own primary-published return history, and pre-2004/2005
data for both funds is reconstructed rather than the ETFs' own trading history). This single source
backs the entire Appendix C table.

**Redesign note (load-bearing):** the original source doc's "worst calendar year ≈-37%"
(S&P 500) / "≈-13%" (All-Weather) framing could not be re-sourced at that same level of specificity —
LazyPortfolioETF.com does not publish a discrete single-calendar-year worst-year row, only rolling
multi-period returns and peak-to-trough maximum drawdown. Rather than force an unsourceable "worst
calendar year" figure, this case substitutes **maximum drawdown** (a real, cited, arguably *better*
risk metric for exactly this decision, and one of the four options the source doc's own Challenge
list explicitly names: "Sharpe ratio, maximum drawdown, expense ratio, tax efficiency"). This is the
kind of redesign case-research/SKILL.md's worked example describes as "the right move."

**Also load-bearing:** primary_metric selection. The most obvious candidate metric (30-year projected
terminal portfolio value, D4) was computed and found NOT balanced — roughly a 55% margin favoring
Buffett 90/10, driven by compounding a real ~2.6-point trailing-return gap over 30 years. Rather than
force that metric to be the graded balance test (which SPEC §2 would reject) or manufacture
closeness by altering a real cited figure (never permitted), this case's primary_metric was set to
the 20-year Sharpe ratio instead, because the same Appendix C data genuinely, honestly lands the two
portfolios at an almost exact tie there (0.66 each) — a real property of the sourced data, not an
authored one. See `case.json.legacy_conversion_note` for the full reasoning.

## P17 — Description of Ray Dalio's All-Weather allocation (Appendix B)

**Searched for:** confirmation that the 40/30/15/7.5/7.5 allocation is still consistently described
as Dalio's All-Weather mix, and its commonly-cited origin.

**Found:** Consistently described the same way (and cited to Tony Robbins' 2014 book *Money: Master
the Game*, matching the original source doc's own citation) across the same S2 site and multiple
other financial-press sources returned by search.

**Outcome:** SOURCED as `S3`, confidence MEDIUM (secondary sources consistently describing a real,
dated primary book; the book itself was not directly fetched).

## P18 — Inflation-rate assumption for the D4/D5 salary-growth projection (Appendix D, MA3)

**Searched for:** a real, dated, citable average U.S. inflation rate to use as the basis for
Benjamin's stated plan that his income (and 40%-of-income contribution) grows with inflation over the
30-year projection.

**Found:** USInflationCalculator.com reports average U.S. CPI inflation of approximately 2.6% per
year over 2000-2026, citing BLS CPI data, via WebSearch.

**Rejected:** Did not pursue a direct BLS CPI table fetch for a marginally higher-confidence grade —
judged the aggregator's stated, dated average adequate for a Modeling Assumption's basis (this value
is not primary_metric-load-bearing; it only affects the D4/D5 projection deliverables, and MA3 is
explicitly labeled an assumption, not a sourced fact about the future).

**Outcome:** SOURCED as `S4`, confidence MEDIUM (aggregator site, but citing and consistent with
well-known BLS CPI trends over this period).

**P6 data-decay note (2026-08-22):** re-fetched during Tier 2. The live page carries year-by-year
CPI figures (e.g. 2025 = 2.6%, most recent 12-mo = 3.4%) but does not itself publish a single
"2000-2026 average" figure — the 2.6% used here is this case's own computed average of the page's
per-year data, not a number quoted verbatim from the source. Flagged here so a future reader
doesn't mistake it for a directly-quoted figure; it does not change S4's MEDIUM confidence grade.

## NOT FOUND count: 0

Every figure this case needed was either genuinely sourced (S1-S4, backing all of Appendix C's
return/stdev/drawdown table plus the allocation-origin and inflation claims) or is case-given
scenario data (Benjamin's personal finances) requiring no external citation. No figure was declared a
NOT-FOUND-driven Modeling Assumption in the case-research sense — Appendix D's MA1-MA4 are genuine
authorial/scenario conventions (risk-free rate for a hand computation; using trailing return as a
forward proxy; restating Benjamin's own stated plan; a rounding convention), not stand-ins for a
figure that could not be found.
