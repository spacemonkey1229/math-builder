# Research Log — Psychologist

Legacy conversion, 2026-08-20. This case's core dataset (27 applicants × 5 test scores, Appendices
A and B) is the case's own given fictional/scenario data, carried over verbatim from
`source/Y3/Additional/Psychologist/Case Study_ Psychology.xlsx` — it is not a real-world fact
requiring external citation, the same way Baseball Lineup's spring-training statistics or Cold
Chain's fictional facility circuit are given data, not sourced data. Only two real-world claims in
this case needed sourcing.

## P01 — court reporter professional speed/accuracy standard (Background paragraph 1)

**Searched for:** NCRA (National Court Reporters Association) RPR certification exam speed
requirements, to verify the "up to 225 words per minute" figure the original source docx asserted
in its Background section as a real, general claim about court reporters.

**Found:** NCRA's RPR skills exam has three legs — Literary (180 WPM), Jury Charge (200 WPM), and
Testimony/Q&A (225 WPM) — each graded to a 95%+ accuracy standard. Confirmed via WebSearch and a
direct WebFetch of LegalClarity's "RPR Certification Requirements and Exam Structure" article
(published 2026-05-18), which describes NCRA's own certification structure with specific
wpm/accuracy figures per leg.

**Rejected:** Attempted to fetch NCRA's own certification page directly
(`ncra.org/certification/getting-certified/rpr`) for a tier-1 primary source — returned HTTP 404 (page
moved or restructured). Did not chase down NCRA's current URL structure further; LegalClarity's
recent (2026-05), specific, multi-figure description of NCRA's exam structure was judged a
reasonable tier-3 secondary source for a piece of scene-setting texture that is not load-bearing to
any calculation in this case (nothing in Challenge 3's deliverables uses the 225 WPM figure).

**Outcome:** SOURCED as `S1`, confidence MEDIUM (secondary source, but specific, dated, and
unambiguous in units). Cited `[S1]` in Background; row added to case.md Appendix D and
case.json.sources[].

## P02 — equal weighting as the default composite-scoring method (Appendix C, MA2)

**Searched for:** whether equal ("unit") weighting is a real, recognized default methodology for
combining multiple test scores into one composite score, to back Appendix C's Modeling Assumption
MA2 (the case weights all five test categories equally in its composite score) as a defensible
real-world convention rather than an arbitrary author choice.

**Found:** "Individual Psychometrics" (an open psychometrics coursebook, rbind.io), section 13.4.1
"Calculating a Weighted Composite Score," describes unit-weighted composites as the simplest and
most transparent method of combining scores, and equal weighting as a neutral default that does not
privilege any one dimension absent domain-validated weights. Confirmed via WebFetch, quoting the
relevant passage directly.

**Rejected:** Did not pursue the more authoritative but paywalled/non-fetchable "Standards for
Educational and Psychological Testing" (AERA/APA/NCME) — the standard professional reference on
this topic, but not available as a live, fetchable URL within this research pass. A secondary
academic-coursebook source was judged adequate for a case-internal Modeling Assumption's basis
(SPEC does not require a MA's citation to be tier-1, only that the case not present an unsourced
number as though it were sourced fact — MA2 is explicitly labeled a modeling assumption, not a
fact, and S2 only backs *why the assumption is a defensible default*, not the assumption's value
itself).

**Outcome:** SOURCED as `S2`, confidence MEDIUM (no author/date on the page; secondary academic
source). Cited `[S2]` in Appendix C, MA2; row added to case.md Appendix D and case.json.sources[].

## Supplemental appendix materials (not placeholders, SPEC §1.6/case-research §6)

Two real, live, verified-resolving links were added to Appendix D "Further Reading" to establish
the case's central tension (specialist vs. generalist selection) is a real kind of tension, not an
invented one:

- IvyWise, "The Myth of the Well-Rounded Student: Colleges Want Specialists" (updated 2025-11-20) —
  verified live via WebFetch; confirms the specialist-vs-well-rounded debate is a real, current
  topic in a different (college admissions) selective-admissions context.
- Khan Academy, "Percentages" hub page — verified live via WebSearch; a free, general resource on
  the percent-conversion skill this case's D1 deliverable requires (not the answer to Challenge 1's
  research task, since Challenge 1 requires a Hero's *own* researched resource, but a legitimate
  supplemental resource for anyone who wants one).

## Verification sweep

```
placeholders remaining in case.md: 0
citation markers with no source row: none ([S1], [S2] both resolve to case.json.sources[])
source rows never cited in text: none
LOW-confidence sources (must not be load-bearing): none — both S1 and S2 are MEDIUM
```

Next step: run `case-readiness` on `psychologist`.
