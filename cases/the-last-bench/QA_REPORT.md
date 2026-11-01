# QA REPORT: The Last Bench

## case-readiness run: 2026-10-28
**State:** DRAFT -> TIER1_PASS (Tier 2 not clean)   **Verdict:** BLOCKED (2 Tier 2 FAILs: P2, P7)   **sha256(case.md):** b9b1ca64f2c3f1ca00a987393060351f8501b97b3ce88b82dc3dea501158e0f3

### Tier 1: structural (24 checks, tier1_structural.py)
0 BLOCKERs, 2 GAPs, all other checks PASS (T1-15 and T1-18 to T1-24 are POLISH "no published/ yet": case-publish not run by instruction).
- GAP T1-10: new_coverage[] is empty. All 10 claimed skills already have n>=2 in the spine; reinforcement carve-out invoked with a written case.json.reinforcement_note (adjacent n<=1 skills checked and not reachable). Needs a human to accept the carve-out; the concept sheet's claim that cone and cylinder volume are "true holes" refers to n=2, which the checker does not treat as new.
- GAP T1-16: hash first recorded by this run (now recorded).
Mechanical repairs made during the run (all in the case's own files): placeholder table, FACILITATOR numbers moved into case.json.derived (T1-14c), Background tightened, sensitivity_disclosure[] entries, argument A reworded (P2 pre-screen).

### Tier 2: simulated play
| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh agent (packet only) chose A on gap/winner 6.78%; every number matches the case of record; named metric correctly; break-even 2,616.2; flagged ambiguities (pipe inside shell not stated, mining order, whether throughput counts ore plus waste), all since stated in Appendix B/C. |
| P2 both-sides | FAIL | Fresh agent: A is "easily" defensible; B survives only as a values/option-value pitch or by attacking the scenario assumptions. B collapses at the peer challenge "name one year in the USGS series where B beats A" (none does; break-even 2,616 is above all four) and at "what is the break-even stripping ratio" (6.57-12.11 vs 14.26). B's quantitative pillars (9.6% price move erases the gap; leverage 0.979 vs 0.707 USD M per USD/oz; 1,319 extra crew-years at about 47,010 USD each; 271.8 koz) are real but the agent judged B "legitimate but not strong". Recorded FAIL: the 6.8% margin is a paper number on the cash metric alone. The concept deliberately balances on cash vs stake; a human must decide whether that design is accepted (waiver) or the case is retuned (e.g. a constraint that brings the break-even inside the plotted years). Readiness does not retune. |
| P3 trap | PASS | Fresh agent named the same trap as the guide (ore-only accounting). It also found traps the guide had not named; six added to FACILITATOR.md (cone heights vs depths, pipe double-count, capital omitted, 50-degree wall pick, live gold price, deferred-not-prevented closure and early stripping). |
| P4 twist | PASS (after repair) | Fresh adversarial agent first returned FAIL: the discounted twist claim depended on an unstated mining order (pushback-first reverses the result). Repaired by stating "planned reserve first, then pushback; capital when the pushback begins" in MA7 (Appendix C). Undiscounted twist (A 1,559.1 vs B 1,745.0, B by 10.7%) survived every reading tested (pipe double-counted, cost on waste only, zero capital, g/oz vs oz/t conversion). NOT independently re-run after the repair; the agent's own table shows all reserve-first readings (mid-period, end-of-year, capital at t=0 or 3.75) keep A at 2,388 and B at 3,300. |
| P5 sensitivity | PASS (disclosed) | sensitivity_model.py swings 13 scenario dials +/-50%. The verdict is NOT stable: B wins at grade or recovery +9.6%, mining cost -14.1%, processing cost -29.3%, floor radius -22.2%, current depth -12.0%, wall angle +7.9%, pipe radius +6.9%; capital never flips it (A still leads by 2.0 USD M at zero capital); price flips at 2,616. Several +/-50% flexes break the 20% cap. Disclosed in FACILITATOR.md, balance.sensitivity and sensitivity_disclosure[]. JUDGMENT CALL for a human: the script only accepts categories F/X/I; the 8 dials are authored scenario values with no public analogue, so Category X is the closest bucket but is a stretch (X expects a good-faith estimate from a public analogue). The script reports base margin 7.3% (gap/loser); the case uses gap/winner = 6.78%. |
| P6 data decay | PASS | Fresh agent fetched all 7 URLs (S1-S6 plus Wikipedia Strip_ratio): all HTTP 200, no redirects to new addresses, values present (USGS 1,801/1,802/1,945/2,388; 32,150.7 oz per metric ton; bench, pushback, head grade, waste rock, 31.1034768 g, stripping ratio). Note: USGS MCS 2026 has versions 1.0 to 1.3 (Feb-May 2026); PDF footer says February 2026. |
| P7 accessibility | FAIL | (a) mechanical: D5 asks for a graph and published/ has no visual (case-publish not run; a figures/pit_cross_section.svg schematic exists and is referenced from Appendix B but is not yet in any published artifact). (b) First cold read (packet before repairs): bench and pushback unexplained, stripping ratio partial, pit geometry (large cone minus small cone, shell) not picturable. After adding inline explanation of the apex, the shell and the pipe: 0 hard-stop terms, but Q2 (central invented object) still YES: the shell geometry (apex fixed while floor and rim drop). The figure should fix it once published. Re-run P7 on the published HTML (with hover glosses and the figure) before TIER2_PASS. |

### Tier 2 detail: P1 full solve (condensed; every number from the fresh solver)
Constants: value per ore tonne = 1.0 g/t x 0.88 x 32,150.7 oz/t / 1e6 x P = 0.028293 oz/t x P; at 2,388 = 67.56 USD/t.
D1: current pit (1/3)pi[513.18^2 x 462.07 - 180^2 x 162.07] = 127.431 - 5.499 = 121.932 Mm3; pushback pit 183.799 - 5.499 = 178.300 Mm3; shell 56.368 Mm3 = 146.557 Mt (second check 183.799 - 127.431; small cone cancels).
D2: pipe pi x 140^2 x 60 = 3.6945 Mm3 = 9.6057 Mt = 271,771 oz; waste in shell 136.951 Mt; stripping ratio 14.26.
D3: A = 25(67.56-22) - 75 x 3 = 914.07; B = 852.06; gap 62.01; margin 62.01/914.07 = 6.78% (A). A(P) = 0.70732P - 775; B(P) = 0.97909P - 1,485.997; tie at P = 710.997/0.27177 = 2,616.2 USD/oz (9.6% above 2,388). Each year (A/B): 1801 498.9/277.3; 1802 499.6/278.3; 1945 600.7/418.3; 2388 914.1/852.1.
D4: mine life 3.75 / 11.078 yr; crew-years 675 / 1,994.0; extra 1,319; 62.007/1,319 = 0.047 USD M (about 47,000 USD); crew 180/2,100 = 8.57%.
D5: lines A and B above, 4 plotted points, crossing at (2,616.2, about 1,075.4).
Extensions: break-even SR 6.57 / 6.58 / 7.93 / 12.11 vs 14.26; discounted (8%, mid-year, reserve first) A 793.8, B 747.7.
Strongest counter-argument (A): thin 6.8% margin, break-even only 9.6% above planning price, B has more upside and 1,319 jobs-years. Most sensitive: gold price, then grade x recovery, mining cost, capital. Ignored: the 38/50-degree table. Least supported: 1.0 g/t at 88%.

### Tier 2 detail: P2 full solve (condensed)
Argument A: pushback ore pays 437.7 vs 439.7 USD M of mining before 60 USD M capital; B finishes 62.0 USD M (6.8%) behind; tie needs 2,616, above every year in the series; B more price-exposed (slope 0.979 vs 0.707); at 2021 prices B is 44% below A; best sentence: "At the board's own 2024 price, the pushback's ore pays only 437.7 USD M against 439.7 USD M of mining before a dollar of its 60 USD M capital, so B finishes 62 USD M (6.8%) behind and needs gold at 2,616 just to tie."
Argument B: 6.8% rests on labelled assumptions that flip with 10-14% changes; gold rose 22.8% in 2023-24 and 32.6% in 2021-24; B is the leveraged position; mine life 3.75 -> 11.08 yr; 1,319 crew-years at about 47,010 USD each; closure and reclamation liabilities are deferred (excluded, MA6). Best sentence: "For a 6.8% haircut on a 914 USD M margin, which one 9.6% gold move erases, B keeps 180 people working 7.3 more years."
Collapse: B first, as above.

### Tier 3: human dry-run
NOT RUN.

### Open items
- BLOCKER-class: P2 FAIL (B collapses on cash alone); P7 FAIL (needs published HTML with figure and glossary).
- GAP: T1-10 reinforcement carve-out; P5 Category X mapping; P4 not re-run after repair.
- UNVERIFIED: all geometry, grade, recovery, cost, throughput, crew and town figures (scenario assumptions by design); the math-glossary hover/hyperlink layer (T1-19) is generated at publish, not yet exercised; context_glossary[] links fetched and confirmed 2026-10-28 and ready for render_context.py.
- Concept-sheet discount figures (794.0/747.9, 1,354.3/1,450.2) differ from this case's reproducible 793.8/747.7, 1,354.0/1,449.8 by 0.2-0.4 (part-year treatment); winners and margins agree.
