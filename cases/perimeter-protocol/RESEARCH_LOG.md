# Research Log — Perimeter Protocol

Stage 3 (`case-research`). Seven `{{NEEDS_SOURCE}}` placeholders were opened by `case-write`.
Two resolved to real, directly-fetched primary sources. Five resolved to stated Modeling
Assumptions (three distinct assumption values, since the analyst-hour placeholder appeared twice
in the document for the same figure).

| # | Placeholder | Location | Searched | Found | Outcome |
|---|---|---|---|---|---|
| P1/P2 | Total weekend analyst-hours available to the skeleton crew | Background, Appendix A | Searched for any public benchmark on hospital-network SOC weekend/on-call staffing levels. No public dataset reports a specific organization's SOC staffing schedule — this is operational security information organizations do not publish, for the same reason firewall logs aren't published. | NOT FOUND (expected — no such figure is or should be public) | **Modeling Assumption MA1** — 20 analyst-hours, stated scenario constraint for a two-person weekend on-call crew. |
| P3 | Date of KEV catalog snapshot | Appendix B | Fetched the CISA KEV catalog live JSON feed directly (`cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json`) rather than relying on the HTML catalog page, which returned HTTP 403 on direct fetch. | FOUND — `dateReleased: 2026-08-21T17:46:43.60Z`, `catalogVersion: 2026.08.21` | **SOURCED [S1]**, HIGH confidence — primary source, directly fetched. |
| P4 | Current total entries in the CISA KEV catalog | Appendix B | Same fetch as P3. Cross-checked against a secondary aggregator (axis-intelligence.com) that independently reported "1,665 entries as of catalog version 2026.08.11" — an earlier, smaller count consistent with the catalog having grown by 9 entries between 2026.08.11 and 2026.08.21 (plausible at CISA's typical weekly addition rate; see the several "CISA Adds N Known Exploited Vulnerabilities" alert pages found in the same search). | FOUND — `count: 1674` | **SOURCED [S1]**, HIGH confidence — primary JSON feed, directly fetched, and independently corroborated in trend/direction by a secondary aggregator's slightly earlier count. |
| P5 | The Weekend Traffic Sample (20-request table with p, q, and ground-truth-threat flags) | Appendix C | This was never expected to resolve to a real source — no public per-hospital firewall log exists, and none should. Confirmed no such dataset exists via search; none was seriously expected. | NOT FOUND (expected, by design) | **Modeling Assumption MA2** — hand-built 20-row sample. Built deliberately (not randomly) so the classification produces a genuine, defensible margin: Rule Set A (disjunction) blocks 10 of 11 true threats at a cost of 6 false positives (ratio 1.667); Rule Set B (conjunction) blocks 4 of 11 true threats at a cost of 2 false positives (ratio 2.0) — a 16.7% margin favoring B on the stated primary metric, within SPEC §2's 20% cap, while A still blocks more than double B's raw threat count. This arithmetic is recorded here and in `case.json`'s `balance` object — **not** in `case.md`, which only carries the raw, unclassified sample rows so students do the classification themselves. |
| P6 | Average cost/time to triage a single false-positive alert (IBM/Ponemon Cost of a Data Breach or comparable vendor SOC report, cited as a survey average) | Appendix D | Searched for "Ponemon false positive cost," "IBM Cost of a Data Breach false positive," "average time to investigate a security alert." Found two real, named Ponemon Institute surveys: (1) Ponemon/Exabeam SIEM Productivity Report (Aug 2019) — 25% of analyst time spent on false positives; (2) Ponemon/Damballa *The Cost of Malware Containment* (2015) — $1.3M/year and ~21,000 hours/year investigating inaccurate alerts, out of 16,937 weekly alerts with only 19% deemed reliable. Neither converts cleanly to a single "cost per false positive" figure — the 2019 survey reports a rate, not a per-alert time, and the 2015 survey's totals explicitly conflate false negatives and false positives ("analyzing false negatives and/or false positives"), so deriving a per-alert dollar figure from it (e.g. dividing $1.3M by an assumed false-positive count) would require an unstated extra assumption this case is not going to launder as a measured figure. Attempted to reach the original Ponemon/Exabeam PDF and a more recent (2020-2021) Ponemon "Economics of the SOC" report directly (businesswire.com press release, msspalert.com) for a cleaner per-alert figure; the businesswire fetch timed out and msspalert.com returned HTTP 403 — could not verify a cleaner number this session. | PARTIALLY FOUND — real, dated, named survey data establishing scale and direction, but no clean per-alert figure | **SOURCED [S2] [S3]** for the underlying real research (both MEDIUM confidence — real Ponemon surveys, but accessed via secondary write-ups rather than original PDFs, and S3 is dated 2015). **Modeling Assumption MA3** for the actual value used in calculations — 15 analyst-minutes per false positive, anchored to S2/S3's real scale, not a literal transfer of either figure. |
| P7 | Sources table | Appendix F | N/A — populated as each placeholder above resolved. | — | **SOURCED** — table built with S1, S2, S3. |

## Rejected leads (for the next person's benefit)

- **A precise "$ per false positive" figure from a recent (2023-2025) IBM Cost of a Data Breach
  report.** IBM's Cost of a Data Breach report reports breach-response costs, not false-positive
  triage costs, in the editions checked via search snippets — it measures a different quantity
  (cost of an actual confirmed breach) and was not pursued further once that mismatch was clear.
  Worth a direct fetch of the current edition if a future revision of this case wants to add or
  swap this figure.
- **A more recent Ponemon "Economics of the Security Operations Center" report (2020-2021,
  various sponsors: ServiceNow, Devo).** Multiple press releases referencing this report were
  found (businesswire.com, PR Newswire, Security Magazine) with adjacent figures ($2.86M average
  annual SOC spend; "70 minutes average alert investigation time" from an unrelated secondary
  source), but two direct fetch attempts (businesswire.com timeout; msspalert.com HTTP 403) did
  not resolve within this session. If revisited, try fetching the PR Newswire or Security Magazine
  copies directly, or the original Ponemon Institute library page (ponemon.org/research).
- **A derived "$1.3M / assumed annual false-positive count" per-alert dollar figure.** Computable
  from S3's own numbers by assuming the 81%-unreliable share of the 16,937 weekly alerts are all
  false positives, but this stacks an unstated assumption (unreliable = false positive, not false
  negative or duplicate) on top of an already-dated source. Rejected as a load-bearing number for
  exactly the reason SPEC §5 exists — it would look sourced while actually being invented.

## Summary

- **Placeholders opened:** 7
- **Resolved SOURCED (real citation):** Appendix B date + count (2), Appendix F sources table (1) — 3 tokens, 1 underlying fact (the KEV catalog snapshot)
- **Resolved as stated Modeling Assumption:** Background/Appendix A analyst-hour pool (2 tokens, 1 assumption — MA1), Appendix C traffic sample (1 token — MA2), Appendix D false-positive cost (1 token — MA3)
- **Dropped:** none
- **NOT FOUND, by design (no real source should exist):** the per-hospital weekend staffing figure and the per-hospital traffic log — both correctly became Modeling Assumptions, exactly as predicted in the concept sheet (`CONCEPTS_formal-logic-vectors-matrices-numbertheory_2026-08-23.md`, C1's "Sources I am NOT confident about" note).

Next step: `Run case-qa on perimeter-protocol` (a later, separate stage — not run in this pass per
instructions).
