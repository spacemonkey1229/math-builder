# RESEARCH_LOG — The Bracket Cliff

Case-research pass, 2026-09-01. 21 `{{NEEDS_SOURCE}}` placeholders enumerated from `case.md`
(Appendices A–E). All 21 resolved: 17 sourced to real, cited figures (S1–S16; some sources cover
more than one placeholder, e.g. Household 1/2's income and premium came from the same KFF article),
4 disclosed as Modeling Assumptions (Appendix E — Priya's state is deliberately not a real named
state, per Background).

---

## Appendix A — FPL threshold and the $128,600 vs. $132,600 discrepancy

**P01 — 2026 federal poverty guideline basis.** Searched "HHS 2026 federal poverty guidelines,"
found the ASPE guidelines page and multiple secondary aggregators. The aggregators disagreed on
which vintage governs "2026 coverage" — this is exactly the discrepancy the case brief flagged.
Fetched ASPE's own detailed-guidelines PDFs directly for both 2025 and 2026 (tier-1 primary,
`aspe.hhs.gov`). **2025 guidelines** (published following the Jan. 17, 2025 Federal Register
notice): household of 1 = $15,650, household of 4 = $32,150 (100% FPL). **2026 guidelines**
(published following the Jan. 15, 2026 notice): household of 4 = $33,000 (100% FPL). Confirmed via
`obamacarefacts.com` and `healthinsurance.org` that ACA marketplace subsidy eligibility for a given
plan year is fixed by statute to whichever HHS poverty guidelines were *most recently published
before that year's open enrollment begins* — because the coverage year's own guidelines aren't
published until January of that year, after enrollment has already started, there is a built-in
one-year lag. For 2026 coverage this means the **2025** guidelines govern.

**P02/P03 — 400% FPL thresholds.** Single filer: 400% × $15,650 = $62,600. Family of four:
400% × $32,150 = $128,600. Both read directly off ASPE's own published percentage table (the PDF
includes a 400% column), so no arithmetic error is possible here — HIGH confidence, primary source.

**Resolving the discrepancy.** $128,600 (400% of the 2025 guideline) is the figure that actually
governs 2026 ACA plan-year eligibility. $132,000 (400% of the 2026 guideline, sometimes rounded to
$132,600 in secondary sources) is arithmetically correct for the *2026* guideline vintage, but that
vintage does not govern ACA 2026-coverage subsidy determination — it governs 2026-dated programs
without the one-year lag (e.g., Medicaid/SNAP eligibility periods tied to calendar year). This is a
real, sourced explanation for the discrepancy, not a coin flip — both case.md and case.json state
it explicitly rather than silently picking one number.

**Rejected:** A handful of blog aggregators (`ustax.tools`, `benefitsusa.org`,
`federalpovertylevelcalculator.com`) stated the $132,000/$132,600 figure as "the" 2026 ACA
threshold with no acknowledgment of the vintage-lag rule — these were not used as sources; they are
exactly the kind of undated/un-attributed conflation the discrepancy note calls out.

---

## Appendix B — KFF worked examples

**P04–P07 — Household 1/2.** Searched for the specific KFF figures named in the case brief
($62k→$64k, ~$8,756 swing). Found and directly fetched KFF's "A Steep Subsidy Cliff Looms for Older
Middle-Income Enrollees" (Quick Takes, Oct. 8 2025). It gives, for a 60-year-old: $62,000 income =
396% FPL, subsidized premium $6,175/yr; $64,000 income = 409% FPL, unsubsidized premium
$14,931/yr. $14,931 − $6,175 = $8,756 — matches the case brief's named figure exactly, confirming
this is the correct primary source rather than a coincidentally similar one. HIGH confidence, tier-1
primary (KFF's own analysis with a clear publication date).

**P08/P09 — Couple's second example.** Found KFF's companion piece ("ACA Marketplace Premium
Payments Would More than Double..."), Sept. 30 2025, with a 60-year-old-couple example: $85,000
combined income (402% FPL), premium payments rise "by over $22,600" once enhanced credits expire,
described elsewhere in the article as going from ~8.5% to ~25% of income. Attempted to get an exact
dollar premium figure via a second, more targeted fetch — the article states the percentages and
the $22,600 rise but never states the absolute dollar premium outright. Derived ≈$21,250/yr (25% ×
$85,000) as an approximation. **Graded MEDIUM, not HIGH**, and explicitly flagged as not
load-bearing: the $22,600 figure appears to blend the subsidy-cliff effect with a separate ~18%
2026 premium-inflation effect the article discusses elsewhere, so treating it as a clean "cliff-only"
number would overstate precision the source doesn't actually have. Household 1/2 (S3) remains the
only load-bearing pair for D1's limit computation.

---

## Appendix C — ARP/IRA 8.5% cap and benchmark premium

**P10 — 8.5% affordability cap.** Well-documented, low-effort search: multiple sources
(healthinsurance.org, Congress.gov CRS Report R48290) independently confirm the ARP/IRA
enhancement's defining mechanism was capping the benchmark premium at 8.5% of income with no upper
income cutoff (as opposed to the pre-ARP formula, which capped at higher percentages that rose with
income and then cut off entirely at 400% FPL). HIGH confidence — this is essentially undisputed
policy fact, corroborated by a nonpartisan CRS product.

**P11 — 2026 benchmark premium for the Appendix B household.** Initially searched for a
stand-alone benchmark premium figure. Re-read the KFF Quick Takes methodology note: the $14,931
figure *is* the 2026 hypothetical benchmark premium for this exact enrollee (18% national median
premium increase applied to the 2025 benchmark) — at 409% FPL with $0 subsidy, a household's full
premium and the benchmark premium are the same number by definition (no subsidy to net out).
Rather than treat this as a separate NOT-FOUND item, recorded it as identical to S3 with a note
explaining why — avoids inventing a second number that would coincidentally have to match the first
anyway.

---

## Appendix D — Cost of closing the gap

**P11 (CBO) — $350B estimate.** Searched directly for the CBO figure named in the case brief.
Found consistent reporting across AHLA, Becker's Payer Issues, and the House Budget Committee, all
citing the same CBO/JCT score: ≈$350 billion, FY2026–FY2035. Did not manage to directly fetch the
CBO's own cost-estimate letter (not indexed by the search tool in a directly fetchable form) —
graded HIGH on strength of multiple independent, named-source republications of the same specific
number rather than a raw search-engine summary, per the skill's tier-2 guidance, but noted the caveat
in the source record rather than silently treating it as a tier-1 fetch.

**P12 — State count.** Found two different KFF-published counts: 10 states (Sept. 29 2025 FAQ,
pre-expiration) vs. 11 states (Jan. 9 2026 article, post-expiration, adds Oregon). Rather than pick
one, reported both with dates and the explanation that they reflect different points in time as
states reacted to the federal enhancement's expiration — same treatment as the FPL discrepancy,
just lower-stakes since this number isn't load-bearing for any Challenge computation.

**P13 — New Mexico.** Directly fetched the Governor of New Mexico's own press release (primary,
Jan. 6 2026): $21.5M (regular Jan. 2025 session) + $17.3M (Oct. 2025 special session) ≈ $38.8M
combined, through June 30, 2026, fully backfilling the lost federal enhancement up to 400% FPL —
NM is reported to be the only state doing a *full* backfill. Corroborated by KSFR (NM public
radio). HIGH confidence.

**P14 — Massachusetts.** Directly fetched Mass.gov's own press release on Gov. Healey's Jan. 8 2026
announcement: $250M in new state funding, bringing total ConnectorCare funding to $600M for plan
year 2026. Corroborated by GBH News and CommonWealth Beacon coverage of the same announcement. HIGH
confidence, primary source.

**P15 — California.** The case brief named a $190M→$300M progression. Found $190M in Covered
California's own Feb. 26 2026 press release (2026 plan year, up to 165% FPL) — primary source. The
$300M figure initially appeared only as a *proposed* May Revision budget item (per KFF Health News,
June 12 2026, still under negotiation) — did not treat this as settled until finding CalMatters'
June 29 2026 reporting on the *signed* FY2026–27 budget explicitly listing "$300 million to
subsidize private healthcare... a Newsom priority" as included in the final deal. Recorded as
finalized for plan year 2027 (up to 200% FPL) rather than as a live-negotiation figure, since it was
confirmed passed before this research pass.

**P16 — National share above 400% FPL.** Found two figures: CMS's own 2025 QHP Premiums and Choice
Report states 5% of APTC-eligible enrollees had income over 400% FPL (describing PY2024 data) —
primary federal source, HIGH confidence. A narrower, more directly useful proxy for "how many
households are actually close to the line" is the 400–500% FPL band specifically, cited at 3% of
2025 plan selections via secondary reporting on the same CMS data — graded MEDIUM (a proxy
quantity, secondary attribution) and used as the basis for Modeling Assumption MA2 rather than the
broader 5% figure, since "close enough to cross" is a narrower claim than "any income above 400%."

---

## Appendix E — Priya's state (Modeling Assumptions, not sourced)

**P17–P20.** Background states explicitly that Priya's state and exchange are illustrative, not a
real named state — so none of these four figures are publicly sourceable by design, and all four
were always going to resolve as Modeling Assumptions per the skill's "NOT FOUND → three exits"
procedure (exit 1, stated assumption) rather than genuine research failures.

- **MA1 (enrollment, 480,000):** rather than pull a number from nowhere, anchored it to a real,
  comparably-sized state marketplace — Pennsylvania's Pennie, reported at ≈486,000 total enrollees
  at the close of 2026 open enrollment (PHIEA/agency.pennie.com press release, corroborated by
  Pennsylvania Office of Rural Health reporting). Rounded to 480,000 and disclosed the anchor
  explicitly rather than implying it's Pennsylvania's actual figure.
- **MA2 (share near threshold, 3%/≈14,400 households):** applied the S15 national 400–500% FPL
  band share to MA1's enrollment figure. Disclosed as a Modeling Assumption specifically because
  compounding one real national percentage onto one illustrative state population is itself an
  assumption, even though each input is separately sourced or estimated.
- **MA3 (discretionary line item, $8M one-time):** set deliberately well below any real per-state
  wraparound program's *annual* cost (Appendix D range: $38.8M–$300M), because Background specifies
  this is a one-time discretionary item, not an ongoing appropriation — a same-scale figure would
  have quietly erased the funding-mechanism tension the case is designed to surface in D5.
- **MA4 (21 days):** pure narrative-urgency figure, not derived from any real legislative calendar;
  disclosed as such with no attempt to dress it up as sourced.

All four carry a **Sensitivity** entry per the skill's requirement for assumptions that can affect
the dilemma. MA1 and MA2 turn out to be *inert* with respect to the actual A-vs-B margin (they
cancel out of the per-household ratio — see FACILITATOR.md) — this was verified algebraically, not
assumed, and is called out explicitly in both `case.md`'s Modeling Assumptions block and
`FACILITATOR.md`, since it is a genuinely useful thing for a Hero to discover mid-discussion. MA3 is
the assumption that actually matters for D5's practical recommendation.

---

## Verification

Ran the skill's standard verification script after all edits: 0 placeholders remaining, all
`[S<n>]` citation markers have a matching `sources[]` row and vice versa, no source row is
missing a required field, zero LOW-confidence sources (so none is at risk of carrying a
constraint), `case.json.status` = `"researched"`.

## Computed margin (facilitator-only; not written into case.md per skill instructions)

Per-household: D1/D2 discontinuity $8,756 (S3) vs. Build The Bridge's real cost $9,491 (S3 + S5
combination) → **margin_pct = 7.74%, winning option = A (Hold The Cliff)**. This is a genuinely
close, non-landslide margin (well under SPEC §2's ~20% flag threshold), and it is
population-independent — MA1/MA2's state-scale assumptions cancel out of the ratio algebraically,
so the margin does not depend on the case's least-defensible number. Full derivation recorded in
`FACILITATOR.md` and `case.json.balance.margin_pct`.

**Next step:** Run `case-readiness` on `the-bracket-cliff`.
