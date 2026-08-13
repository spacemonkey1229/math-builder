# Research Log — Wildfire

This case had **zero** `{{NEEDS_SOURCE}}` placeholders left open by `case-write` — figures were
sourced directly during the conversion pass rather than staged as placeholders first, given the
size of this task. This log records what was searched, found, and rejected, per `case-research`
§7.

## Town/place data

**Search 1:** "driving distance Agua Dulce California to Santa Clarita California miles" —
returned conflicting figures (14.33 mi straight-line / 18 mi one route / 23 mi via CA-14 per
rome2rio). **Used:** 23 mi (the CA-14 route figure), as the more conservative (longer) real-road
distance. **Confidence:** MEDIUM — an aggregator tool, not a primary mapping authority, and the
range itself (14–23 mi depending on route) is real uncertainty, not sourcing failure.

**Search 2:** "driving distance Agua Dulce California to San Fernando California miles" —
returned 24 mi (trippy.com / distance.to). **Used:** 24 mi. **Confidence:** MEDIUM, same reasoning.

**Search 3/fetch:** Wikipedia "Santa Clarita, California" — population 228,673, land area 70.75 sq
mi (both 2020 Census), average household size 2.94 (2010 Census, carried in the same article — no
newer figure was in the fetched content). **Confidence:** MEDIUM (Wikipedia's own summary of
Census data, not fetched from census.gov directly — see the direct-census-attempt note below).

**Search 4/fetch:** Wikipedia "San Fernando, California" — population 23,946, land area 2.37 sq
mi, 6,358 households (2020 Census). Household size (3.77) is a derived figure (23,946 / 6,358),
computed by this conversion, not directly stated on the page. **Confidence:** MEDIUM.

**Search 5/fetch:** Wikipedia "Agua Dulce, California" — population 3,451 (not used — this case
uses only the housing figures, not population, for Agua Dulce), 1,303 housing units, 95.0%
occupied, land area 22.85 sq mi, average household size 2.79 (all 2020 Census). **Confidence:**
MEDIUM.

**Direct census.gov attempt (rejected path):** Attempted `WebFetch` against
`census.gov/quickfacts/fact/table/santaclaritacitycalifornia/PST045224` and the equivalent San
Fernando URL. Both returned **HTTP 403 Forbidden** — census.gov QuickFacts appears to block this
fetch tool's user agent. Fell back to Wikipedia's Census-sourced infobox data instead of guessing
or dropping the figures. **This is why S1–S3 are graded MEDIUM rather than HIGH** — a future pass
with authenticated or different-agent access to census.gov QuickFacts, or to the American Community
Survey data tables directly, should re-verify these three figures and upgrade the grade, or correct
them if Wikipedia's numbers have drifted from the primary Census release.

## Unit conversion facts

**Search 6/fetch:** "1 chain 66 feet forestry surveying unit definition NIST" then direct fetch of
NWCG's Firefighter Math course, "8.5 Map Spread"
(`nwcg.gov/course/ffm/fire-behavior/firefighter-math-85-map-spread`) — confirmed the worked
example "12 chains × 66 feet/chain = 792 feet," i.e., 1 chain = 66 feet is the real, standard
figure. 10 square chains = 1 acre is a standard, definitional derived fact from the same 66-foot
chain (1 chain² = 4,356 sq ft; 43,560 sq ft = 1 acre; 43,560 / 4,356 = 10) — not independently
re-derived from a second source, since it follows arithmetically from the 66-foot figure itself.
**Confidence:** HIGH — this is the same real NWCG training-course family (`nwcg.gov`) the legacy
case's own Appendix D already linked to ("National Wildfire Coordinating Group Training Course").

**Search 7/fetch:** "NWCG rate of spread chains per hour definition fire behavior" then fetch of
NWCG's Glossary of Wildland Fire (PMS 205), "rate of spread" entry — confirmed chains/hour is the
real, standard reporting unit for ROS, and that ROS is "the speed with which the fire is moving
away from the site of origin." This validates that the legacy case's own field-report format (ROS
in chains/hour) was not an invented unit. **Confidence:** HIGH.

## What was NOT independently sourced, and why

The two 05:00 field reports themselves (35 chains/hour southern head at 9% slope/10 mph wind; 27
chains/hour southwestern flank at 4% slope/8 mph wind) are the **legacy case's own scenario data**
for a **fictional fire** (the Soledad Canyon Fire, as depicted, did not occur as described — Agua
Dulce, Santa Clarita, and San Fernando are real, but this specific fire event is not). These
numbers cannot be externally verified because there is nothing real to verify them against; they
are preserved verbatim as the case's own stated field reports, exactly as Cardiology preserved its
disclosed (not trial-sourced) cost-modeling convention. No placeholder or citation applies to them
— they are the given premise of the scenario, not a factual claim about the world.

## Outcome

Zero placeholders open. Six sources added (S1–S6), three graded MEDIUM pending a census.gov
re-verification pass, three graded HIGH. Five Modeling Assumptions declared (MA1–MA5), each with a
stated sensitivity. No figure was invented, estimated-and-presented-as-fact, or rounded from
memory.

Next step: `case-qa` on `wildfire`.
