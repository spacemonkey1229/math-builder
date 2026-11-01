# QA Report: The Last Seat

## case-readiness run, 2026-10-28
**State:** DRAFT -> TIER1_PASS (Tier 2 not clean)   **Verdict:** BLOCKED on P7 (accessibility cold-read)
sha256(case.md) = f2213d8db1b02243796048f16ecb7a99e8b8712437a66ce8a4453d3617153765

### Tier 1 (24 checks): 0 BLOCKERs, 2 GAPs
- GAP T1-10: new_coverage[] empty. Every spine skill now has n>=1; reinforcement_note records what was checked (carve-out applies).
- GAP T1-16: hash recorded in this run (now current).
- No published/ directory (case-publish not run): T1-15, T1-18 to T1-24 had nothing to check; the interactive HTML and hover math glossary (MCS-37/39) remain to be generated at publish.
- Preflight advisory: FLEX contains house_size=435, which equals a cited value. Deliberate: the case treats 435 as statute, so the probe-5 sweep is a scenario question ("what if the House size also changed"), disclosed in sensitivity_disclosure[].

### Tier 2
| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh agent, packet only: chose A on the worst gap, correct arithmetic throughout (89, 1.8257/1.9009, 12.07/11.67). Ambiguity found and fixed: margin from rounded vs unrounded values (4.12/3.43 vs 4.11/3.50); Appendix C now says unrounded. Appendix B average corrected to 761,169 (was printing 761,168). |
| P2 both-sides | PASS | Both sides defensible with real numbers. B is the thinner side: it collapses first at "why is your yardstick right and why is it worth a law?" (rests on the contested bias claim). Not a paper margin. |
| P3 trap | PASS | Fresh agent's top trap (pick one yardstick, ignore that they disagree) matches the guide's trap; its second (arithmetic/convention slips) added to the guide. |
| P4 twist | PASS | 2010 data reverses the leader on both yardsticks (computed by evaluate_twist: B ahead by 1.50% on worst gap); invalidates two popular positions; no hidden convention. |
| P5 sensitivity | PASS (disclosed) | house_size -50% (218 seats) ties the methods; +50% (653) keeps A ahead at 7.99%; 300-600 sweep A 127 / B 6 (428-433) / tie 168. Disclosed in case.json and the guide. |
| P6 data decay | PASS | Fresh agent: all 13 URLs 200; values present for S1-S11. S12 uses n = seats already held (same formula, case defines n differently); S13 implies rather than states "nearest integer"; Li abstract page did not literally show the Webster recommendation in the agent's read (Crossref record agrees on citation). |
| P7 accessibility | FAIL | Round 1 named 9 unexplained items; after adding plain-words glosses (persons per representative, quota, divisor method, bias, the "sheet" in Appendix E) round 2 still named a few (meaning of "priority value", why the formula looks as it does, Dean's method, malapportionment, legal citations) and found the Overview's "rows" ambiguous until Appendix E. Both reads were of case.md, not published HTML, so the hover glossary was absent. |

### Remaining BLOCKER
- P7 FAIL: add a one-line plain-words meaning of "priority value" in Appendix A, drop or gloss "Dean" and "malapportionment", and make the Overview's "rows" read as seats (e.g. "two entries"); rerun P7 on the published HTML with the glossary. Or record a P7_waiver.

### Tier 2 detail: P1 full solve (condensed from the fresh solver)
D1 MN 8th: 5,709,752/sqrt(56)=762,997.7053; NY 27th: 20,215,751/sqrt(702)=762,994.3529; gap 3.3524; NY needs 20,215,839.82 so 20,215,840-20,215,751 = 89. D2 trials 750,000->440, 755,000->437, 760,000->435, 765,000->432, 770,000->431, 761,168->435; divisors ~758,100-761,300 work; Webster differs in Montana 2->1, Rhode Island 2->1, New York 26->27, Ohio 15->16. D3 current: Delaware 990,837 / Montana 542,703.5 = 1.8257; Webster: Rhode Island 1,098,163 / Wyoming 577,719 = 1.9009. D4 sums 12.0742 vs 11.6658; signed differences cancel to 0. D5 4.11% (A ahead) and 3.50% (B ahead). Chose A on the worst gap, naming Yardstick 1.

### Tier 2 detail: P2 full solve (condensed)
A: wins worst gap 1.8257 vs 1.9009 (4.11%); Webster pushes the largest district from 990,837 to 1,098,163; B's yardstick-2 edge is 0.41 seats from four states; already law, upheld 1992. B: yardstick 2 uses all 50 states, 11.67 vs 12.07 (3.50%); four states off by more than half a seat under current law, none under Webster (max 0.4987); small-state bias argument (Li; Young via CRS).

### Tier 3
NOT RUN.

## Honest gaps and UNVERIFIED
- Li (2022) full text not read; Ernst declaration not read (second-hand via CRS 2013).
- 2 U.S.C. 2a page shows no currency date; Census Table 1 footnote independently cites 2a/2b.
- Which committees hold census jurisdiction in 2027: not stated (generic wording).
- Interactive HTML and math glossary not built (case-publish out of scope).
