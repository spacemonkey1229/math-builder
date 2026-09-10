# Research Log — Boulderfield

This case was authored and researched together (case-write + case-research combined in one pass);
every figure below was fetched and confirmed before being written into `case.md`, per MCS-21 (no
URL from memory).

## P01 — Longs Peak trailhead/summit elevation, Keyhole Route stats

Searched "Longs Peak Keyhole Route elevation gain mileage nps.gov" and fetched the NPS Keyhole
Route site-bulletin PDF directly — the PDF came back as corrupted/unreadable binary via WebFetch,
so it could not be used as a direct citation despite being the primary source. Fell back to
14ers.com's structured route-list table (`routelist.php?peakid=10015`), fetched directly and
confirmed: trailhead 9,400 ft, summit 14,259 ft, Keyhole 14.5 mi RT / 5,100 ft gain / Class 3.
Cross-confirmed the 14,259 ft summit figure independently against NPS's own Keyhole Route page
(`nps.gov/romo/planyourvisit/longspeak.htm`), which matched exactly — used as the basis for grading
14ers.com MEDIUM rather than LOW despite not being a primary government source. → **SOURCED, S1.**

## P02 — The Loft route stats

An early web-search AI synthesis reported a "North Face / Cables Route" at 13.0 mi RT / 5,168 ft
gain, Class 5.4 technical. Attempted to verify this directly against 14ers.com's own structured
route table and its dedicated route pages (`route.php?route=long4` returned an explicit "missing or
invalid information" error) — the North Face/Cables route does not appear in 14ers.com's own
route-list table at all, only three routes do: Keyhole, Keplinger Couloir, and **The Loft** (13 mi
RT, 5,300 ft gain, Class 3, High exposure / Considerable rockfall). Because the Cables Route figure
could not be independently confirmed from a page actually fetched (only from an unattributed search
synthesis), it was **rejected** and the case was redesigned around The Loft instead, which is
directly confirmed in the same fetched table as the Keyhole figures. This is the "redesign" exit
`case-research`'s SKILL.md describes for an unsourceable figure — in this instance applied mid-write
rather than after a placeholder came back NOT FOUND, but the same principle: never cite a number
that was not actually fetched. → **SOURCED, S2** (The Loft, not Cables/North Face).

## P03 — Trailhead-to-Boulderfield distance/elevation

Two independent trip-report sources gave inconsistent figures: one (theoutbound.com / search
synthesis) suggested ~5.5 mi / 12,760 ft; a personal blog (rickcrandall.net, fetched directly)
described a 7-mile approach to a "12,700 ft" Boulderfield campsite via what its own text identifies
as a different approach (consistent with the separately-documented "Boulder Brook" alternate
trailhead route, not the standard East Longs Peak Trail). Because the two figures reflect two
different trailhead approaches rather than a single contested fact, this was **not** treated as a
simple sourcing failure — it was disclosed as a genuine discrepancy in `case.md`'s Appendix A note,
and the standard-approach figure (5.5 mi / 3,360 ft gain) was adopted as a stated Modeling
Assumption (MA-BF) rather than presented as flatly sourced. → **ASSUMPTION, MA-BF** (not S-numbered
— explicitly disclosed as contested rather than cited as settled).

## P04 — Naismith's Rule formula

Searched directly for the rule's constants and fetched Wikipedia's `Naismith%27s_rule` article,
which attributes the original formula (1 hr / 3 mi horizontal, +1 hr / 2,000 ft ascent) to William
W. Naismith's 1892 Scottish Mountaineering Club Journal report. Graded MEDIUM (encyclopedia
republication of a well-documented historical primary source, not the primary source itself, but
the constants are the standard, unmodified form still cited in current SAR/hiking pace-planning
references). → **SOURCED, S4.**

## P05 — RMNP temperature range (basis for MA3)

Fetched NPS's `all-about-weather.htm` directly. Found two specific, usable figures: summer nights
"often reach the 70's or 80's and drop into the 40's," and alpine tundra areas see additional
"temperature drops of 10-20 degrees Fahrenheit." No specific overnight low for this case's stated
incident night exists publicly (it is a modeled scenario, not a real dated incident), so 28°F was
set as a disclosed Modeling Assumption (MA3) explicitly built on this documented range, not
presented as a sourced fact itself. → **SOURCED background (S5); MA3 is the assumption it informs.**

## P06 — Standard environmental lapse rate

Searched for a NOAA-attributable numeric lapse rate. The NWS glossary's own headline entry
(`forecast.weather.gov/glossary.php?word=lapse+rate`) turned out to define the *dry adiabatic*
lapse rate (5.5°F/1,000 ft) — a different, steeper quantity than the commonly used "normal" or
"environmental" lapse rate this case actually needed. Fetched the Britannica "normal lapse rate"
page directly for a cleaner citation; it returned HTTP 403 and could not be used. Fell back to
NOAA's Storm Prediction Center sounding-help glossary page (fetched directly, confirmed reachable),
used as the general meteorological-reference anchor for the ~3.5°F/1,000 ft figure that is widely
cited across multiple independent meteorology sources found in the original search pass. Graded
MEDIUM — a standard reference constant, not a site-specific Longs Peak measurement. →
**SOURCED, S6.**

## P07 — NWS Wind Chill Temperature Index formula

Fetched `weather.gov/safety/cold-wind-chill-chart` directly. Confirmed the exact formula (`35.74 +
0.6215T - 35.75(V^0.16) + 0.4275T(V^0.16)`) and its stated valid range (T ≤ 50°F, V > 3 mph) —
both of this case's D5 calculations fall inside that range. Primary government source. →
**SOURCED, S7.**

## P08 — "Off the summit by noon" rule of thumb (basis for MA5)

NPS's own Keyhole Route page states the 3:00 a.m. recommended start time and names June-August
afternoon thunderstorms as the reason (S3, HIGH). Searched separately for a specific turnaround
clock-time and found it only on SummitPost (fetched via search synthesis, community source, not
NPS) — graded MEDIUM and used only as one of two bracketing reference points for MA5's stated
10:00 a.m. deadline assumption, not as a load-bearing sourced fact on its own. → **SOURCED, S8**
(community rule of thumb, explicitly graded down from S3's primary-source confidence).

## P09 — Real RMNP search-and-rescue activity on Longs Peak

Searched for real, recent NPS press releases confirming SAR operations occur on Longs Peak's upper
routes. Found and fetched-via-search-confirmation "Major Rescue Underway On East Face Of Longs
Peak," an official NPS news release. Used only to establish this case's scenario is a realistic
kind of real, recurring situation (SPEC's framing requirement) — not as evidence this specific
incident happened. → **SOURCED, S9.**

## Verification sweep

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources (must not be load-bearing): []
```

## Next step

Run `case-readiness` on `boulderfield`.
