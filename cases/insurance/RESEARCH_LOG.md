# Research Log — Insurance

One row per placeholder/figure. This case was converted and researched in a single continuous
pass (case-write immediately followed by case-research, both performed here); placeholders were
never left as literal `{{NEEDS_SOURCE}}` tokens in a separate drafting stage — each is documented
below as it was resolved.

| # | What was needed | What was searched/fetched | Result | Disposition |
|---|---|---|---|---|
| P01 | The friend's HDHP plan's real terms (premium, deductible, OOP max) | The only source is the original case's own Guide Notes.docx, which states the figures as relayed secondhand from Greg's friend's own plan — no plan name, insurer, or policy number given. No further public search is possible without an identifiable product. | NOT FOUND (no independent public source exists for this specific, unnamed, secondhand plan) | Stated Modeling Assumption (MA2), used as given, corroborated for legal plausibility against real 2021 IRS HDHP thresholds (S8) rather than invented or independently re-sourced. |
| P02 | Navigator Gold 2000's real 2021 net premium | The original case's own bundled `Plan Comparison.pdf` — extracted directly with `pypdf`, a real screen capture of the family's own yourhealthidaho.org plan-selection page, dated 2021-04-10 | FOUND: $694.00/mo net ($2,088.00 gross, $1,394.00 APTC) | SOURCED — S2, HIGH confidence, real primary-source screenshot bundled with the original source material. |
| P03 | Navigator Gold 2000's cost-sharing structure (deductible, OOP max, copays, coinsurance, pregnancy example) | The original case's own bundled SBC PDF (`Navigator Gold 2000_60597ID0360009-01 SBC.pdf`) — extracted directly with `pypdf` | FOUND: full SBC, including a real worked pregnancy coverage example ($12,700 total / $4,170 patient share) | SOURCED — S3, HIGH confidence, official plan document. |
| P04 | A reference cost for an "established patient" primary-care and specialist office visit, since neither plan's copay reveals the underlying bill | The original case's own bundled `sample-fees-list-ncal-en.pdf` (Kaiser Permanente 2021 Northern California Sample Fee List) — extracted directly | FOUND: established-patient level 3 visit $150, level 4 visit $215 — real, dated 2021, but a different U.S. region (Northern California, not Idaho), and not urology-specific | SOURCED with disclosed regional/specialty-proxy caveat — S4, MEDIUM confidence, used per MA3. |
| P05 | A reference cost for a VCUG (voiding cystourethrogram) imaging procedure | WebSearch: "average cost of VCUG voiding cystourethrogram procedure without insurance" | FOUND: MDsave (real cost-transparency platform) reports a $304-$845 range | SOURCED with disclosed proxy caveat — S5, MEDIUM confidence, midpoint ($500) used per MA4. Not 2021-specific; no dated 2021 figure was found in this search. |
| P06 | A reference cost for a self-pay urgent care visit | WebSearch: "average cost urgent care visit without insurance 2021 national average" | Search results skewed toward 2025-2026 current guidance; no clean 2021-specific national figure surfaced. Typical current range $125-$300, average ~$180 (GoodRx and similar aggregators) | SOURCED with disclosed proxy caveat — S6, MEDIUM confidence, $180 used per MA4. |
| P07 | A reference cost for an emergency-department visit, ideally 2021-dated to match the case's setting | WebSearch: "average cost emergency room visit without insurance 2021 national average stitches", then WebFetch on the AHRQ HCUP Statistical Brief #311 PDF directly | FOUND: a real 2021-dated federal statistic — $80.3 billion aggregate cost across 107.4 million treat-and-release ED visits = $748/visit average | SOURCED — S7, HIGH confidence (real, dated, federal), with a disclosed caveat that this measures hospital cost via cost-to-charge ratio, not necessarily patient billed charge. |
| P08 | Real 2021 IRS thresholds for HDHP qualification and HSA contribution limits, to check the friend's plan (P01) for plausibility | WebSearch: "2021 IRS HSA-qualified HDHP minimum deductible maximum out-of-pocket family Revenue Procedure 2020-32", then WebFetch on the IRS's own Rev. Proc. 2020-32 PDF directly | FOUND: family minimum deductible $2,800, family max OOP $14,000, family HSA contribution limit $7,200 | SOURCED — S8, HIGH confidence, primary federal source, fetched directly. Confirms the friend's plan (P01) is a legally real, rules-compliant HSA-qualified HDHP shape. |
| — | "Real Cost Of Healthcare Calculator" and "How Much Does Health Insurance Cost?" (original Appendix B optional links) | Not independently re-verified — these were optional resources in the original 2021 case, not load-bearing figures | Dropped from this conversion's Appendix B in favor of the two bundled, already-verified 2021-dated articles (HealthCare.gov, NerdWallet), which are decorative/optional research pointers, not cited data | DROPPED (decorative, not load-bearing; the two retained links are the ones already confirmed present and dated in the bundled source PDFs). |

## Rejections and dead ends

- Attempted to find a real, Idaho-specific, 2021-dated premium quote for a hypothetical HDHP plan
  matching the friend's stated terms exactly (to replace the LOW-confidence secondhand figure with
  a HIGH-confidence independent one). This is not findable after the fact — 2021 individual-market
  rate filings for specific plan designs are not retrievable via general web search, and the
  friend's plan is not named. Accepted as a genuine NOT FOUND; used as a disclosed Modeling
  Assumption instead (see P01 above), matching case-research's own worked example for exactly this
  situation (SKILL.md §"Worked example").
- Considered treating a possible 2021 pregnancy as a probability-weighted addition to the BASELINE
  expected-cost estimate (D2), using a stated probability for "considering trying." Rejected: this
  would have required assigning a specific numeric probability to a real family's real reproductive
  decision, which is both mathematically shaky (properly probability-weighting the two scenarios
  did not meaningfully change the raw-dollar landslide finding — verified by hand before rejecting)
  and needlessly sensitive for classroom material. The pregnancy is used instead as the Twist — a
  certain reveal at a fixed moment, exactly as the original Guide Notes' own "Lessons Learned"
  section suggested, using Navigator Gold 2000's own real SBC coverage example rather than an
  invented cost.

## Post-research fix, found by case-readiness Tier 2 probe 1 (cold solve)

A fresh cold-solve subagent, given only case.md, computed a different (lower) ordinary-year total
than this case's own canonical numbers, tracing back to an ambiguous sentence in Appendix D: the
original wording placed Tiffany and Greg's 3 routine 2020 PCP visits each in the same sentence as
the "used in D3" unplanned-incident framing, so a careful reader reasonably read those 6 routine
visits as D3-only data, not also as D2 recurring-care data. Fixed by splitting the sentence — see
QA_REPORT.md's P1 entry for the full trace. This was a real clarity defect in the case text, not a
sourcing defect, and is recorded here because it was found during the research/readiness pass in
this same session.

## Primary-metric redesign (the load-bearing finding of this research pass)

A raw combined premium-plus-out-of-pocket dollar comparison was computed by hand and cross-checked
with `sensitivity_model.py` under three scenarios (zero unplanned incidents, the family's real 2020
incident rate, and a full pregnancy year). In every scenario, Option A (HDHP) is cheaper by
39.5%-45.5% — a real, structural landslide driven by the $6,828/year real premium gap between the
two real, sourced premium figures (S1/S2), which no realistic combination of this family's own
documented care needs closes; the mathematical ceiling was checked explicitly (Option A's absolute
worst possible total, $14,300, is still below Option B's absolute best possible total, $8,328 plus
any nonzero utilization) confirming this is not scenario-dependent bad luck but a fixed relationship
between the two real numbers. Per SPEC.md §2 and case-research's own REDESIGN exit ("swap the
constraint for one with public data" / "usually the best answer"), the case's GRADED primary metric
was changed from raw total dollar cost to each plan's own real, stated, sourced out-of-pocket
maximum (S1/S3) — real, meaningful, needs no additional sourcing beyond what was already gathered,
and lands within 6.7%. The raw landslide is fully disclosed in case.md Appendix A and is the case's
central trap, not hidden. See `case.json.legacy_conversion_note` for the complete account.
