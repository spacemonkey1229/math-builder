# Research Log — The Gijon Rule

Every claim in the case, what was searched or fetched, what was found, and the outcome. Authored 2026-10-03.

| # | Item | Searched / fetched | Found | Outcome |
|---|---|---|---|---|
| P01 | Group 2 results (six matches) and all six first-round final tables | Wikipedia raw wikitext (`action=raw`) for 1982_FIFA_World_Cup_Group_1 to _Group_6; RSSSF https://www.rsssf.org/tables/82full.html | Group 2: 1-2, 0-1, 4-1, 0-2, 3-2, and (transcluded from Disgrace of Gijón) 1-0. Final tables parsed from the wikitext standings blocks. | **SOURCED**, S1/S2/S4-S8, HIGH. RSSSF corroborates every table; one discrepancy: RSSSF lists Peru's goals against as 5, the group page 6 (group page is internally consistent; Peru finished last either way; disclosed in Appendix D). |
| P02 | The 1982 tie-break ladder (points, goal difference, goals scored, lot) | Wikipedia 1982_FIFA_World_Cup raw wikitext; WebSearch for FIFA regulation text; RSSSF page (no rules text); Disgrace of Gijón article | Wikipedia's first-round section lists the ladder and cites a print Kicker special issue (May 1982, p. 3). The Disgrace article independently says "first tie-breaker is goal difference" and separates Austria/Algeria on goals scored. The Group 1 narrative (Cameroon out on goals scored with equal goal difference) is consistent. FIFA's own 1982 regulation text was not found online. | **SOURCED, MEDIUM** (S9). The ladder is secondary-sourced; the open item is resolved as MEDIUM, not HIGH. A primary FIFA regulation citation is still wanted. |
| P03 | Did the 1986 simultaneous rule cover only the final pair of matches? | Fetched raw wikitext for 1986_FIFA_World_Cup_Group_A to _Group_F; WebSearch | In all six 1986 groups the two final matches share a date and kickoff time, and no other pair of matches within a group does (checked by script over the six pages: consecutive matches 1-2, 2-3, 3-4, 4-5 never share a date and time; matches 5 and 6 always do). Wikipedia's Disgrace article says "the final two games in each group would be played simultaneously". | **SOURCED, MEDIUM** (S3, S10). Resolved: final pair only. |
| P04 | Three-point rule first used at a World Cup | Wikipedia Three_points_for_a_win and 1994_FIFA_World_Cup raw wikitext | 1994 text: "These finals were the first to award 3 points for a win in the group stage to motivate teams to play an attacking style." | **SOURCED, MEDIUM** (S11). |
| P05 | Option A's own cost (broadcast slot, fan access, scheduling) | Considered; no source located. | none | **DROPPED.** Not claimed anywhere in the case. The case says its cost is unsourced (Appendix F / FACILITATOR). |
| P06 | A match photograph | Commons imageinfo for "Germany v austria wc1982 01.jpg" (public-domain claim by a 2026 uploader of a 1982 magazine photo) and "Interior de El Molinón.JPG" | The match photo's public-domain claim is unverifiable (a 1982 press photograph, uploaded in 2026). The stadium photo is CC BY-SA 3.0, own work by HesselinK, uploaded 2013. | **Match photo REJECTED** (licence not defensible). **Stadium photo used** (S12), licence read from the Commons API, URL returns 200. |
| P07 | The twist's real-world analogue (2018 Japan-Poland, simultaneous matches) | Disgrace of Gijón wikitext | The article records the 2018 case, where a team changed play after watching the simultaneous match. | Facilitator note only; not a number, not load-bearing. Tie-breaks in 2018 differed and the case does not analyze them. |
| P08 | A source for the committee scene | none | No source documents how or when the 1986 rule was decided. | **Constructed scene, flagged** in Background and MA5. |

## Derivations (recomputed, not sourced)

All counts (39/49, 29/49, 11/21, 1/21, 42/49, 45/49, 5-2 unresolved, 6-3 Austria, Group 6 Scotland for USSR, groups 1/3/4/5 unchanged, 0 differences under three points) are recomputed by `sensitivity_model.py` and asserted in its `__main__`. The group-6 result was re-derived from the parsed standings of each of the six wikitext group pages (see model's GROUPS dict).

## Rejections worth recording

- Using a different group-page edition: the group pages were fetched 2026-10-03; Wikipedia can change.
- The "best scoreline" is 6-5 only inside the 0-6 window; it is (cap, cap-1) at every window tried (3 to 12).
- No FIFA 1982 regulation PDF was located; the ladder rests on secondary sources.
