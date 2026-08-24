# Research Log — Caribbean Internet Cafe

This case is unusual among the corpus's legacy conversions: its underlying source
(`source/Y2/Session 7/Caribbean Internet Cafe/998B02-PDF-ENG.PDF`) is not an in-house scenario
built for this pipeline but a real, professionally published Ivey Business School teaching case
(998B02, "Caribbean Internet Cafe," Michelle Theobalds, supervised by Professor Murray Bryant,
Richard Ivey School of Business, copyright 1998). Every dollar figure, percentage, and quantity
used in Appendices B–E (equipment costs, monthly operating costs, the JTL offer terms, the
exchange rate, the three market-research scenarios) is reproduced from this source, not invented —
the "sourcing" work for this case is verifying the source is real and current, and (per case-write
doctrine) explicitly declaring the two places the case's own deliverables need a number the source
document does not supply (Option A's financing rate; the historical grounding for the Twist).

## S1 — the source case itself is real and current

**Searched for:** whether "Caribbean Internet Café," Ivey case 998B02, is a real, still-available
published teaching case (not a fabricated or discontinued product), to establish that this case's
core dataset is genuine historical business-planning data rather than fiction dressed as fact.

**Found:** The case is commercially listed and available at Harvard Business Publishing's store
(store.hbr.org), product 998B02, confirming author, publisher, and subject matter match the PDF on
file in this project's `source/` tree. Cross-verified word-for-word between the legacy docx
(`Case Study_ Caribbean Internet Cafe.docx`) and the original PDF — same figures throughout.

**Outcome:** SOURCED as `S1`, confidence HIGH (primary source, live commercial listing,
cross-verified against the document on file). This is the backbone citation for Appendix A's "this
case is a formalization of a real, published Ivey Business School teaching case" claim and for
every case-given figure in Appendices B–E, none of which needed independent verification beyond
confirming the source itself is genuine.

## S2 — the case's own stated 1996 exchange rate (JA$35 = US$1), historical context

**Searched for:** independent corroboration that the Jamaican dollar's exchange rate against the
US dollar in the mid-1990s was broadly consistent with the case's own stated ~JA$35 = US$1 figure
(itself sourced to S1, the primary document's own footnote) — i.e., does the direction and rough
scale of Jamaican currency history in this period make the case's own number plausible, not just
internally asserted.

**Found:** Wikipedia's "Jamaican dollar" article confirms significant devaluation and elevated
inflation (roughly 25% in 1995, falling to single digits by 2000) through the period. This is
context only — it does not independently re-derive JA$35 = US$1 as an exact figure for 1996, and
is not used as if it did.

**Outcome:** SOURCED as `S2`, confidence MEDIUM (general secondary source, confirms the qualitative
trend, not the exact rate). The exchange-rate figure actually used anywhere in case.md is cited to
`S1` (the primary document), not to S2 — S2 is disclosed as broader corroborating context only, per
the note in `case.json.sources[]`.

## S3 — real-world grounding for the case's Twist

**Searched for:** whether "home Internet access became widespread within a few years of 1996,
eroding the market for paid public-access cafés" is a real historical pattern, not an invented
plot device, since FACILITATOR.md's Twist depends on it.

**Found:** Pew Research Center's "Americans' Internet Access: 2000–2015" confirms roughly half of
US adults were already online by early 2000, with broadband adoption accelerating through the
2000s — a real, fast home-access growth curve in the years immediately following the case's 1996
setting.

**Outcome:** SOURCED as `S3`, confidence HIGH (Pew Research, a reputable primary survey source).
Used only to ground FACILITATOR.md's Twist in a real historical trend — not cited anywhere in the
student-facing `case.md`, consistent with case-write's rule that Twist material stays
facilitator-only.

## Modeling Assumptions requiring no external source (Appendix F)

MA1 (Option A's financing rate, modeled at the case's own quoted 25% Jamaican mortgage rate, since
no independent lender quote for Option A is given anywhere in the source), MA2 (a shared
customer's Internet cost tracks paid computer-hours), MA3 (52⁄12 weeks per month), and MA4
(Appendix C's ambiguous staff-hours sentence, read as a total rather than a coverage multiplier)
are all genuine authorial choices about how to build the case's numbers, not claims about the real
world — per SPEC §5 these are declared as Modeling Assumptions in case.md Appendix F, not
presented as sourced fact, and are not logged here as research tasks.

## Verification sweep

```
placeholders remaining in case.md: 0
citation markers with no source row: none (all references resolve to case.json.sources[])
source rows never cited in text/facilitator material: none
LOW-confidence sources (must not be load-bearing): none — S1/S3 are HIGH, S2 is MEDIUM (context only)
```

Next step: none — this case already reached `qa.state: "TIER2_PASS"` (see `QA_REPORT.md`).
