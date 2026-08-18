# RESEARCH LOG — Reroute Or Wait

Stage 3, `case-research`. Run 2026-08-12. Every URL below was fetched in this session and
confirmed to carry the figure cited against it (MCS-21: no URL from memory). Rejections are
recorded because they are the part that stops the next person re-running a dead search.

**Placeholders opened by `case-write`:** 69. **Remaining OPEN:** 0.
SOURCED 52 · ASSUMPTION 13 · DROPPED 4.

---

## 1. What the concept sheet promised, and what actually held up

The C12 concept sheet flags **Transitland (GTFS), gtfs.org and OpenStreetMap** as the intended
data basis, and grades data feasibility HIGH. Verified rather than assumed, and the finding is
mixed:

| Named source | Verdict |
|---|---|
| Transitland | **Not usable as cited.** Its REST API is key-gated, and a GTFS feed is a zip of CSVs — not fetchable or checkable inside this pipeline, and not something a Hero can open either. A case built on it would carry figures nobody downstream could re-verify. **Rejected.** |
| gtfs.org | Real and live, but it is the *specification*, not data. It publishes no running time, no headway and no ridership. **Not a source for any figure in this case.** |
| OpenStreetMap | Real, but it carries geometry, not scheduled running times, and its road speeds are not agency-published. Using it would have meant deriving edge weights from distance and an assumed speed — replacing sourced numbers with an assumption in the load-bearing position. **Rejected on purpose.** |

**What replaced them.** The agency publishes everything the case actually needs, in HTML and PDF,
with no key: per-timepoint clock times (`trimet.org/schedules/w/...`), per-route weekday ridership
with passenger miles and average trip length (`Route Ridership Report`), and per-station weekday
ons/offs (`MAX Light Rail Passenger Census`). This is a **stronger** basis than the concept sheet's
own, because a Hero can open every one of them. Recorded here as a correction to the concept sheet
rather than a silent substitution.

The concept sheet also names **Census data**. Nothing in the final case uses it: the ridership
question is answered directly by the agency's own counts, and pulling in tract-level population
would have added a number nobody in the room could tie to a bus trip. **Dropped, deliberately.**

---

## 2. Placeholder-by-placeholder

| Placeholders | What was searched / fetched | Outcome |
|---|---|---|
| Appendix A "served by" column (14 rows) | Fetched the published weekday schedules for Line 20 (`t1020_1.htm`), MAX Blue (`t1100_1.htm`), MAX Red (`t1090_1.htm`), Line 77 (`t1077_1.htm`). Read the timepoint headers directly. | **SOURCED** S2, S3, S4, S10. |
| Appendix B, Line 20 clock times (36 cells → 3 trip rows) | Same Line 20 page, midday block. Took three consecutive trips so a Hero can confirm the headway and confirm each segment repeats. All eleven segment times are identical across all three trips. | **SOURCED** S2. |
| Appendix B, MAX Blue RQ→PSN | `t1100_1.htm`, five consecutive midday trips: 11:50→11:59, 12:05→12:14, 12:20→12:29, 12:35→12:44, 12:50→12:59. **Nine** minutes, five times. | **SOURCED** S3. **Corrected 2026-08-12 — see §6.** |
| Appendix B, MAX Red RQ→PSN | `t1090_1.htm`, three consecutive midday trips: 12:28→12:37, 12:43→12:52, 12:58→1:07. Nine minutes. | **SOURCED** S4. Agrees with the Blue Line exactly; there is no disagreement between the two services over this pair. |
| Appendix B, headways | Read off the printed trip rows, plus the agency's own frequency sentence. | **SOURCED** S2, S3, S4, and S5 for the published statement. S5 graded MEDIUM: "every 15 minutes **or less**" is a floor, not a figure, so it is not what the arithmetic uses. |
| Appendix D, Line 20 ridership block (6 cells) | Fetched the `Route Ridership Report — Weekdays, Spring 2024` PDF and read the rendered pages. Route 20: 9,530 boarding rides, 35.2 rides/revenue hour, 28.5 rides/vehicle hour, $5.01/ride, 32,726 passenger miles, 9.0 passenger miles per revenue mile, 3.4 mi average trip. | **SOURCED** S1. |
| Appendix D, neighbouring routes (8 cells) | Same report, same pages: routes 12, 15, 19, 77. | **SOURCED** S1. Deliberately over-complete — none of it is needed for the answer. |
| Appendix D, MAX station counts (15 cells) | Fetched `max_station_passenger_census_report.pdf` (Spring 2025) and read the rendered pages. | **SOURCED** S7. Also over-complete: Skidmore Fountain and Old Town/Chinatown are on neither option's path. |
| Background, the closure itself | Fetched the county's own "Recommended Traffic Option During Construction" page. Confirms the recommendation is a **"full closure"** with traffic diverted to neighbouring bridges. | **SOURCED** S6, graded MEDIUM — see the NOT FOUND section below. |
| Appendix F, the whole sources table | Assembled from the fetches above. | **SOURCED**. |
| Appendix G, the whole assumptions table | See §3. | **ASSUMPTION** ×6 (MA1–MA6). |

---

## 3. NOT FOUND, and which of the three exits each one took

**3.1 Bus running time over the detour route — NOT FOUND.**
Two search framings (agency detour notices; neighbouring-line timetables covering the detour
streets) and a direct fetch of the county project page. No agency or county document publishes an
estimated added transit running time for the Burnside detour, and no published timetable covers the
exact streets a detoured Line 20 would use. The county's own page states no delay figure of any
kind.
→ **Exit 1, stated Modeling Assumption (MA2)** — but derived rather than guessed. The case prices
the extra distance at *the closed segment's own published pace* (S2), so the assumption is a
distance, not a speed. Swept ±50% in Tier 2 probe 5.

**3.2 One-way route length of Line 20 — NOT FOUND from any citable publisher.**
Transit-blog and trip-planner pages publish route-length figures with no methodology and no agency
attribution. All rejected as LOW; a LOW figure may never carry a constraint, and this one would
have carried the crossing share, which is the case's most load-bearing quantity.
→ **Exit 2, redesign.** The case now *derives* route length from four figures the agency does
publish (boarding rides, rides per revenue hour, passenger miles, passenger miles per revenue mile)
plus the timetable's one-way running time. The derivation is written into Appendix E as student
work. This is the single best outcome of the research pass: an unsourceable number became a
computation a Hero performs, and the result — 26.86 miles for a Beaverton-to-Gresham route — is
sane on its face.

**3.3 An origin-and-destination table for Line 20 — NOT FOUND.**
The agency publishes stop-level ons and offs, but no O-D matrix for a bus route, and the
stop-level census is a single several-hundred-page PDF covering every route in the system.
→ **Exit 1, stated Modeling Assumption (MA6)**, with its direction of error stated: the closed
edge sits nearer the middle of the route and in its densest segment, so the true crossing share is
probably *higher* than the stated method returns. That pushes against the option the arithmetic
ends up favouring, not toward it, and Appendix G says so.

**3.4 Walking and street distances at the two transfer points — NOT FOUND as published figures.**
→ **Exit 1, stated Modeling Assumptions (MA3, MA4).** Both are stated as *distances* and converted
to minutes using a real cited standard (MUTCD 3.5 ft/s, S8) or the line's own published pace (S2).

**3.5 Confirmed detour bridge for buses — NOT FOUND in a fetched document.**
A search summary asserted that buses would be detoured across the Steel Bridge. The county page
that the summary pointed at, when actually fetched, **does not say this** — it names no bridge at
all. The claim was therefore **dropped** rather than cited: the case says only "the next bridge
north," which is a property of the case's own Option A, not a claim about the county's plan.
This is exactly the failure MCS-21 exists to prevent, caught before it shipped.

**3.6 Current construction start date — CONTESTED, and the case says so.**
The county's own recommended-option page prints construction as "scheduled to start in 2024 and
last four to five years," which its own newsroom contradicts (a later release cites federal
funding uncertainty and a pushed-back start). Rather than pick a year, the case **does not use a
start date at all**. It uses only the closure *length*, takes the top of the county's own printed
range, and pins every figure to a stated vintage in MA5 (SPEC §5's "as of" rule). The contradiction
is named in Appendix F's S6 note instead of being smoothed over.

**3.7 Dropped outright (4 placeholders).**
The Appendix C "crosses the closed edge?" column was left as student work rather than filled — it
is D2/D3 output, not data. Nothing was invented to fill it.

---

## 4. Sources that were rejected

| Rejected | Why |
|---|---|
| Transitland REST API | API-key gated; not re-checkable downstream. |
| A GTFS `stop_times.txt` feed | Not fetchable as a document, not openable by a Hero. |
| Third-party transit apps' station-to-station times | No provenance, no publication date. LOW, and this figure is load-bearing. |
| Transit-blog "route length" pages | Same: LOW, load-bearing, rejected. See 3.2. |
| A search-result summary asserting the bus detour bridge | Never confirmed by fetching the document it named. See 3.5. |
| Census tract population | Real and fetchable, but nothing in the decision consumes it. Adding it would have been decoration. |

---

## 5. Live-data note (SPEC §5)

TriMet's schedules, its route ridership report and its station census are all still-moving
quantities, and they move on three different cycles. The case does not average them and does not
refresh any of them independently. **MA5 pins each figure to the vintage printed beside it** —
Spring 2024 route ridership, Spring 2025 station census, schedules as retrieved 2026-08-12 — and
states that no number is updated without the others. Tier 2 probe 6 re-checks every URL.

---

---

## 6. Correction pass, 2026-08-12 (stage 4 re-verification, MCS-21)

Before Tier 2, **all ten URLs were re-fetched from scratch and every recorded figure re-checked
against the fetched document**, rather than trusting §2 above. Nine of ten came back clean. One
did not, and it was load-bearing.

**6.1 The MAX Blue Line running time was wrong — 8 minutes recorded, 9 minutes published.**

The original §2 row recorded five Blue Line trips as `11:57→12:05, 12:12→12:20, 12:27→12:35,
12:42→12:50, 12:57→1:05` — an eight-minute segment. Re-fetching `t1100_1.htm` and parsing the
schedule table **by column index** (Rose Quarter TC = column 5, stop ID 8377; Pioneer Square North
= column 6, stop ID 8383) shows this is a column mis-read:

- `12:05pm`, `12:20pm`, `12:35pm`, `12:50pm`, `1:05pm` are the **Rose Quarter** values, not the
  Pioneer Square North values. The original row used them as PSN times and paired them with the
  *previous* trip's RQ time, manufacturing an 8-minute segment out of a 15-minute headway.
- Across **all 72 timed rows** on the page the RQ→PSN segment is 9 or 10 minutes. Every midday row
  is **9**.

**Consequences, all applied:**

1. `case.md` Appendix B's Blue Line table replaced with the five real midday rows.
2. `sensitivity_model.py` `max_rq_to_psn_min` 8.0 → 9.0.
3. Option B's transfer penalty 24.107 → **25.107** min; Option B's ledger 29,079.5 → **30,285.8**
   rider-min/weekday; the margin 7.70% → **11.38%**. Option A still wins and the case is still
   inside the SPEC §2 cap, so the design survives — but every published figure had to move.
4. **A claim in the case was retracted, not just a number.** §2 previously asserted that Blue and
   Red "really do publish different times over the same pair of stations," and Appendix A's
   parallel-edge convention ("keep the faster published running time") was presented as resolving
   that disagreement. **There is no disagreement.** Both lines publish 9 minutes. The convention
   sentence is still correct and still needed for a parallel-edge graph, so it stays — but it no
   longer pretends to adjudicate a conflict that does not exist.

This is the second MCS-21 catch on this case (§3.5 was the first, caught pre-ship). The lesson is
the same both times, and it is worth stating plainly: **a figure that was "fetched" once and
written down is not verified.** Nothing downstream of §2 would ever have caught this — the
8-minute figure was internally consistent, plausible for three downtown rail stops, and produced a
balanced case with a clean 7.70% margin. Only re-reading the source column-by-column found it.

**6.2 Everything else re-verified clean.** S1 (Route 20 row and all four neighbouring routes,
against the extracted PDF text layer), S2 (all 12 timepoint headers and all three trip rows), S4,
S5, S6, S7 (all five station rows), S8, S9, S10 — all reachable, all values still present. Two
minor quotation fixes: S9's page prints `Aug. 2-29`, not `August 2-29`, and S6's page says traffic
is detoured to "other bridges" rather than "neighbouring bridges". Both corrected in `sources[]`.

**6.3 `case.json` had never been written back.** Independently of the data error, stage 3 updated
`case.md` but left `case.json` at `sources: []`, all 69 `needs_source[]` rows `OPEN`,
`modeling_assumptions: []` and both balance arguments `null`. The document and its record had
diverged completely. All of it is now populated.

---

**Next step:** `case-readiness` Tier 2 adjudication is recorded in `QA_REPORT.md`.
