# Research Log — Heist

Legacy conversion, 2026-08-20. This case is fiction/probability-driven, not a real-world
statistics case — per the task brief, no real-world "odds of capture" data exists to search for,
and none was searched for as if it might. What follows is the log for the placeholders that
*were* real, geographic facts requiring verification, plus an explicit account of why the risk
percentages were routed to Modeling Assumptions instead of a search.

## P01 — Zions Bank Idaho Headquarters, real street address

Original source docx states "800 W Main St. Boise, Idaho 83702" directly in the Background text.
Verified via WebSearch: Downtown Boise Association's business directory, the Better Business
Bureau's Zions Bank profile, a Yelp business listing, and the Boise Chamber of Commerce directions
page all independently confirm 800 W Main St, Boise, ID 83702 (the "Eighth & Main" building).
**Found, HIGH confidence, no drift from the original source.** → S1.

## P02 — Heroes Academy, real address

The original source's own Challenge 3 text names "Heroes Academy in Boise, Idaho" as the literal
getaway swap-lot destination — the same name as this project's own real Acton Academy campus.
Searched to confirm this is a real, findable location rather than assuming it. Found: Acton
Academy's own campus directory, a Niche.com school profile, a BBB listing, and a Yelp listing all
independently agree on 5771 N Discovery Way, Boise, ID 83713, next to the West Boise YMCA.
**Found, HIGH confidence.** → S2.

## P03 — Real driving distance/time, Zions Bank to Heroes Academy

Neither the original source (screenshot-only map appendices, not machine-readable) nor a plain
WebSearch/WebFetch returned a route distance (Google Maps and MapQuest both require a JS-rendered
map that a text fetch can't read). Used the Browser tool to load Google Maps' own directions page
live and read the rendered route panel directly: fastest route is 8.9 miles / 21 minutes via
downtown Boise streets onto W Chinden Blvd and US-20 W/US-26 W (a real signed U.S. highway). A
close second alternate (9.2 mi / 23 min) was also shown; this case uses the fastest option, the
plan a real getaway crew would pick. **Found, HIGH confidence, live-fetched.** → S3.

Google's routing tool reports one combined distance/time, not a road-type-by-road-type mile
breakdown — there is no public API that would supply "how many of these 8.9 miles are 3+ lane
city road vs. state highway." This case makes its own defensible category split (2.0 mi city
road / 6.4 mi state highway / 0.5 mi neighborhood road) based on the real named roads in the
route, disclosed as Modeling Assumption MA1 rather than presented as sourced.

## P04 — Boise Police Department headquarters, real address and distance

Searched for Boise PD's real headquarters address (needed for Appendix C's police-proximity risk
check, D4). Found: Yelp and countyoffice.org business listings both independently confirm 333 N
Mark Stall Pl, Boise, ID 83704. A second Boise PD facility (6140 W Corporal Ln) also appeared in
search results but was not used — Appendix C's rule is framed around "a police station" generally,
and headquarters is the department's primary, most-cited facility, so it's the one this case
checks against. Used the Browser tool to fetch a live Google Maps route from Zions Bank to this
address: 6.3 miles via I-184 W — a materially different corridor than the Chinden Blvd getaway
route. **Found, HIGH confidence, live-fetched.** → S4. This real fact is what makes D4's answer
("no, the proximity penalty does not apply to this route") a genuine finding rather than an
assumed one.

## The risk-model numbers (road-type-per-mile risk, stoplight/stop-sign increments, per-minute
risk, proximity-radius bumps, and the speeding formula) — NOT searched, and why

These are the original source's own "Four's Calculations" — the protagonist's stated, in-story
expertise, not a real-world statistical claim. Per SPEC §5 and `skills/case-research/SKILL.md`,
the test for whether a number needs a citation is whether it is presented as a real, externally-
verifiable fact. No public dataset reports "the percent chance of an active pursuit forming per
mile of freeway driven" or "the percent increase in capture risk per stoplight" — this is not
information that exists to be found, and searching for it would only risk laundering an invented
statistic behind a plausible-sounding citation (exactly what SPEC §5 and this skill's "Never"
section prohibit). Per case-research's three legitimate exits for an unsourceable figure — stated
Modeling Assumption, redesign, or drop — this case takes the first: every one of these figures is
reused verbatim from the original source and reframed explicitly as Four's own disclosed
professional judgment in `case.md` Appendix C's Modeling Assumptions block, never presented as
sourced fact. **Zero placeholders were silently filled; zero were left OPEN.**

## Verification pass

```
placeholders in case.md at case-write handoff: 4 (Zions Bank address, Heroes Academy address,
  route distance/time, police station address/distance)
placeholders SOURCED: 4 (S1-S4)
placeholders left OPEN: 0
citation markers [S1]-[S4] all resolve to a sources[] row: yes
source rows never cited in text: none
LOW-confidence sources used for a load-bearing figure: none (all 4 sources are HIGH)
```

Next step: run `case-readiness` on `heist`.
