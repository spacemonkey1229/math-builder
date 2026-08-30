# Research Log — placement-test

Case-research pass, run 2026-08-26. Five `{{NEEDS_SOURCE}}` placeholders were found in
`case.md` (the task brief mentioned six; only five exist in the file and in `case.json`'s
`needs_source[]` — verified by grep, see below).

```
grep -n "NEEDS_SOURCE" cases/placement-test/case.md
126: Appendix A — production weeks remaining
132: Appendix B — total fixed ad-spend budget
140: Appendix C — Meta/Google minimum recommended spend or conversions
146: Appendix D — industry benchmark conversion rate range
147: Appendix D — industry benchmark CPM range
```

---

## P01 — Production weeks remaining before quarter-end (Appendix A)

**Load-bearing check:** Feeds only D1's permutation calculation (`P(weeks, 3)`). Does not
affect the A/B statistical-attribution recommendation as long as ≥3 weeks are available.

**Search attempted:** This is not a real-world fact — it is a fictional detail internal to
Jaylen Ortiz's (fictional) company's fictional production calendar. No search framing applies;
there is no publisher of "how many production weeks a fictional DTC brand has left in a
fictional quarter." Tier 1–4 sources do not exist for this quantity by construction.

**Outcome:** NOT FOUND (correctly — nothing to find). **Exit chosen: Stated Modeling
Assumption (MA1).** Value set to 5 weeks, chosen deliberately greater than the 3 required cuts
so D1 requires the full `nPr` permutation formula (order matters, not every week is used)
rather than a trivial `3!` — this matches the standard "how to determine the number of outcomes
of a permutation" more precisely than a same-count trivial case would.

---

## P02 — Total fixed ad-spend budget for the quarter (Appendix B)

**Load-bearing check:** HIGH. This is the number that actually drives the A vs. B
recommendation once compared against the Appendix C threshold (see P03/P04 below) — it is not
decorative.

**Search attempted:** Same problem as P01 — this is Jaylen's fictional employer's specific,
already-locked internal budget figure. No public filing, price list, or schedule could ever
carry this number for a fictional company. Confirmed no search framing applies.

**Outcome:** NOT FOUND (correctly). **Exit chosen: Stated Modeling Assumption (MA2).** Value
set to $18,000 — picked so it divides evenly by 6 variants ($3,000/variant, clean division for
D2) and so it sits below the derived Appendix C threshold (see P03), which is what creates the
real pedagogical tension this case is built around (SEE case.json `balance.argument_b`).
**This is the single most dilemma-sensitive number in the case — sensitivity is documented in
Appendix E, MA2, and flags the flip point explicitly.**

---

## P03 — Meta/Google minimum recommended spend or conversions per ad variant (Appendix C)

**Load-bearing check:** HIGH — gates whether Full Rotation's per-variant budget counts as
statistically usable in D3/D4.

**Search 1:** `Meta ads learning phase 50 optimization events per week minimum` — returned only
tier-3/4 SEO blogs (Code3, adlibrary.com, growwithsakib.com, etc.), all restating "~50
optimization events per 7 days" without their own primary sourcing.

**Search 2 (tier-1 attempt):** `site:facebook.com OR site:business.facebook.com learning phase
50 optimization events help center` — located Meta's own page, "About learning limited"
(`https://en-gb.facebook.com/business/help/269269737396981`). The search-result snippet quotes
the page directly: *"An ad set becomes Learning limited when it is unlikely to receive around 50
optimisation events in the week after your last significant edit."*

**Direct fetch attempt:** `WebFetch` was tried on four separate Meta Business Help Center URLs
(`.../269269737396981`, `.../112167992830700/`, `.../139628083350822`, plus an
`archive.org` mirror, which is blocked entirely for this environment). All four returned no
retrievable body text — Meta's help center appears to serve a JS-rendered shell to the fetch
tool with no crawlable content, a **tooling limitation, not a nonexistence of the source.** The
figure is Meta's own stated guidance (confirmed twice via independent search snippets from
Meta's own domain) but could not be independently verified by this session via direct fetch.

**Search 3 / fetch (Google side):** `WebFetch` on
`https://support.google.com/google-ads/answer/6268633?hl=en_us_us` ("Tips on measuring Smart
Bidding performance," Google's own domain) succeeded and returned: *"assessing Smart Bidding
performance over longer periods of time, like a month, or at least 50 conversions, for a
clearer perspective."* A second Google Ads Help page
(`support.google.com/google-ads/answer/7065882`, "About Smart Bidding") was also fetched and
returned a consistent figure: *"at least 30 conversions... a month or longer (50 conversions for
Target ROAS)."*

**Outcome: SOURCED**, with caveats on both legs:
- **S1 (Google, MEDIUM):** ~30 conversions/month minimum recommended for reliable Smart Bidding
  read (50 for Target ROAS). Google Help pages carry no explicit publication date, which is why
  this is graded MEDIUM rather than HIGH despite being a primary, directly-fetched page.
- **S2 (Meta, MEDIUM):** ~50 optimization events per 7-day window to exit "Learning limited."
  Confirmed via search snippet from Meta's own domain; direct fetch of the page body failed
  (tooling limitation), and the page itself carries no explicit date — both push this to MEDIUM.

Neither platform publishes an official **dollar** minimum-spend threshold (only conversion-count
thresholds) — Appendix C's row asks for "spend or conversions," so the sourced figures are
reported in conversions directly. Converting to a dollar figure for use in D3 required an
additional stated assumption (see MA3 below) — that dollar conversion is disclosed as derived,
not sourced.

---

## P04 — Industry benchmark conversion rate range, paid-social/influencer video (Appendix D)

**Load-bearing check:** MEDIUM — feeds D4's conversions-per-dollar comparison, but (per the
numbers chosen) applies identically to both options, so it does not independently flip A vs. B;
the flip is driven by P02/P03.

**Search 1:** `2026 paid social conversion rate benchmark report by industry average percent` —
returned wildly inconsistent tier-4 SEO/aggregator content: quoted figures spanning 0.7%–14.29%
depending on which site and which funnel definition, no two sites agreeing.

**Search 2 (tier-1/2 attempt):** `eMarketer paid social benchmarks report 2026 conversion rate
CPM` and a direct fetch of `https://www.emarketer.com/industry-kpis/social-ad-cpm` (the
placeholder specifically asked for IAB or eMarketer). The fetch returned a 404 — eMarketer's
industry-KPI data is subscription-gated and not available to an unauthenticated fetch. This
matches the SKILL.md worked example precedent ("metals pricing is largely paywalled — expect
this to fail").

**Search 3:** `IAB paid social advertising benchmark report 2026` — returned only spend-forecast
figures (ad-spend growth %, market share), not conversion-rate data; no free, dated, point
conversion-rate figure from IAB was found either.

**Outcome: NOT FOUND as a clean sourced figure.** The publicly visible numbers are a genuinely
**contested figure** (SPEC §5's "50% of vaccines wasted" precedent applies directly): dozens of
SEO blogs cite non-comparable numbers with no shared primary source, and the two publishers the
case explicitly asked for (IAB, eMarketer) either don't publish a free point figure or gate it
behind a paywall. **Exit chosen: Stated Modeling Assumption (MA4)** — a declared range (1%–3%,
using 2% in worked arithmetic), explicitly flagged in the case as not a cited statistic.

---

## P05 — Industry benchmark CPM range, paid-social video (Appendix D)

**Load-bearing check:** Same as P04 — feeds D4 symmetrically across both options.

**Search 1:** `2026 CPM benchmark paid social video ads Meta average cost per thousand
impressions report` — again wildly inconsistent: quoted figures from $6.83 to $30+ depending on
objective/industry, no authoritative convergence.

**Search 2:** Same eMarketer fetch attempt as P04 (paywalled/404).

**Outcome: NOT FOUND as a clean sourced figure**, same contested-figure situation as P04.
**Exit chosen: Stated Modeling Assumption (MA5)** — declared range ($10–$20, using $15 in worked
arithmetic).

---

## Derived assumption required by P03 (not a placeholder, but disclosed for transparency)

**MA3 — assumed cost per attributable conversion, $20.** Neither platform publishes an official
dollar minimum-spend threshold (see P03). To make Appendix C's threshold usable in dollar terms
for Challenge D3 (which explicitly asks for a "spend threshold" comparison against budget in
dollars), this case combines the sourced conversion-count threshold (Meta: 50 events/week × 5
weeks [MA1] = 250 events) with a stated, clearly-labeled cost-per-conversion assumption of
$20/conversion, giving a derived $5,000/variant threshold. This is disclosed as `derived: true`
built on one sourced input (S2) and one stated assumption (MA3) — never presented as a directly
sourced dollar figure.

---

## Summary

| Placeholder | Resolution | Confidence |
|---|---|---|
| P01 production weeks remaining | ASSUMPTION (MA1) | — |
| P02 total ad-spend budget | ASSUMPTION (MA2) | — |
| P03 min. recommended spend/conversions | SOURCED (S1, S2) + derived assumption (MA3) | MEDIUM |
| P04 benchmark conversion rate range | ASSUMPTION (MA4) | — |
| P05 benchmark CPM range | ASSUMPTION (MA5) | — |

Zero placeholders left OPEN. Zero silently invented numbers. `case.json.status` → `"researched"`.
