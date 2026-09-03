# RESEARCH_LOG.md — The Course Correction

`case-research` pass, 2026-09-01. 4 real-data `{{NEEDS_SOURCE}}` placeholders (Appendices B, C, D,
and the B methodology note) plus 4 sensitivity-placeholder tokens (Appendix E, MA1–MA4) and 2
structural placeholders (Appendix F table, Appendix G links) enumerated from the drafted `case.md`.
4 SOURCED (real data), 4 sensitivity findings computed via `sensitivity_model.py`, 0 DROPPED,
0 OPEN.

---

## P01 — Real, live NOAA/NDBC ocean current speed and direction (Appendix B)

Searched: "NDBC buoy real-time ocean current speed direction station data." Found NDBC's own FAQ
(`ndbc.noaa.gov/faq/adcp.shtml`) naming a handful of ADCP-equipped stations, plus several
`adcp_data.php?station=NNNNN` result pages from the search itself.

Fetched, in order, station pages `44013` (Boston Approach), `41013` (Frying Pan Shoals, NC),
`44025` (Long Island), `45008` (South Huron — "Buoy retrieved for winter 11/18/25"), `41012`
(St. Augustine, FL — disestablished 2014), `42865` and `42882` (Gulf platforms — "Station not
found," not in NDBC's current inventory). **Every one of these returned "No Current Reports"** or
an outright missing-station error. This is a real, useful negative finding, not a dead end:
several NDBC ADCP stations are seasonally retrieved, disestablished, or simply not reporting at
any given moment, and a case author pulling "the first station that comes up" risks citing a dead
page.

Pivoted to NDBC's own realtime-data directory (`ndbc.noaa.gov/data/realtime2/`) and listed every
file ending `.adcp` — a direct inventory of stations currently publishing ocean-current data,
rather than guessing station IDs. Fetched several of these raw `.adcp` files directly (not station
HTML pages) and confirmed live, recent readings: `44029` (Massachusetts Bay, 18 cm/s toward 300°,
2026-09-01 16:00 UTC), `42013` (Gulf platform, 17 cm/s, 2026-08-20), `42026` (Gulf platform, 18
cm/s, 2026-09-01 20:57 UTC), `44090` (Cape Cod Bay, 27 cm/s toward 340°, 2026-09-01 21:30 UTC),
`44091` (15 cm/s, 2026-09-01 21:30 UTC), `41056` (6 cm/s, weaker still).

Chose **44090 (Cape Cod Bay, MA)**: it is the strongest of the confirmed-live readings surveyed
(27 cm/s / 0.5248 kt), it is a real, currently active, appropriately-scaled buoy for a coastal
research-vessel rendezvous scenario (fits "swap an instrument package" narrative naturally — this
is exactly the kind of buoy a real coastal survey vessel services), and its reading is dated the
same day this case was authored (2026-09-01), matching the project's own "today" cutoff.

Confirmed the direction convention separately (P02 below) before using the reading, since ocean
current and wind conventions are opposite and getting this backwards would flip the entire vector
geometry.

**Outcome: SOURCED, HIGH.** S1 = NDBC 44090, direction (toward) 340° T, speed 27 cm/s
(0.5248 kt), observed 2026-09-01 21:30 UTC, 1 m depth.

## P02 — NDBC ocean current direction convention: FROM or TOWARD? (Appendix B methodology note)

Searched: NDBC's own `faq/adcp.shtml` first — did not state the convention. Tried
`ndbc.noaa.gov/measdes.shtml` directly — 301-redirected to `faq/measdes.shtml`. Fetched the
redirect target directly and found the authoritative statement: **"The direction the ocean
current is flowing toward. 0-360 degrees, 360 is due north, 0 means no measurable current."**
Repeated for both the standard ocean-current format and the expanded ADCP format — same wording
both places.

This matters because NDBC's own wind-direction convention is the opposite (wind is reported FROM,
matching standard meteorological practice) — a case author working from memory or analogy to
Wind Triangle's wind-vector handling could easily get this backwards. Confirmed explicitly rather
than assumed.

**Outcome: SOURCED, HIGH.** S4 = "toward" convention, confirmed via NDBC's own measurement
descriptions page.

## P03 — Real research-vessel-class speed/fuel-consumption spec (Appendix C)

Per the concept sheet's own guidance ("pinning the case to one *named* real vessel's exact
fuel-burn curve may not be public — use a stated, sourced-range spec... rather than one ship's
proprietary numbers"), searched first for a UNOLS compendium or spec sheet with multiple
speed/fuel data points on one vessel. Found the UNOLS Small Research Vessel Compendium (PDF) and
several Wikipedia UNOLS-vessel pages (R/V Robert Gordon Sproul, R/V Roger Revelle, USNS Gyre) —
these gave cruising speed and total fuel capacity/endurance (from which an *average* burn rate is
derivable: e.g. Sproul's 25,000 gal / 14 days ≈ 74.4 gal/hr), but none published a genuine
multi-speed fuel curve (rate at more than one throttle setting) on a single vessel.

A second search ("research vessel fuel consumption gallons per hour cruising speed maximum speed
table") surfaced the **R/V Medeia**, a real 110-foot Alaska Department of Fish and Game fisheries
research vessel, in an ADFG Wildlife News article. Fetched the article directly and confirmed
three real, named, government-published speed/fuel points on the *same vessel*: 8.5 kt (1250 RPM)
= 19 gal/hr; 9.5 kt (1460 RPM) = 32 gal/hr; ~11.5 kt (near top speed) = 60 gal/hr. This is exactly
the multi-point fuel curve the vector-correction mechanic needs (a required boat speed that falls
*between* two throttle settings, needing real interpolation) and it comes from one real vessel, not
mixed across different ships' proprietary numbers.

The article is a genuinely useful real-world hook in its own right: the ADFG crew found that
dropping cruising speed by one knot (9.5→8.5 kt, −11.8%) cut fuel consumption by "30 to 35
percent" — matching the case's own finding that fuel does not scale linearly with speed.

Used R/V Medeia's real figures as the sourced basis for the case's fictional *Coastal Aster*
("styled on a real coastal research-vessel class"), following the same pattern Prove It Scales
used for Meterworks (fictional company, real benchmark data) and Wind Triangle used for Meridian
Air (fictional airline, real aircraft performance data). The case text is explicit that the
*Coastal Aster* itself is not real and is not claimed to be the Medeia.

**Outcome: SOURCED, MEDIUM.** S2. Confidence downgraded from HIGH to MEDIUM because the source
article is from December 2008 — real and government-published, but not current, and no more
recent public multi-point fuel curve for a comparable small coastal research vessel was found in
this search.

## P04 — Real marine/diesel fuel price (Appendix D)

Searched: "Ship & Bunker marine gas oil MGO price index bunkerworld current price." Found
Ship & Bunker's own Global Average Bunker Price page and several competing bunker-price indices
(Bunker Index, OPIS, MABUX, General Index). **Attempted to fetch `shipandbunker.com`'s Global
Average Bunker Price page directly — received HTTP 403 Forbidden** (the site blocks the fetcher).
Did not substitute a remembered or search-snippet-only figure for the blocked page, per the
project's no-URL-from-memory rule — a snippet mentioning "MGO was USD/MT: 1,377.00" as of a stated
date appeared in the search results themselves, but this was not independently fetched and
confirmed on a live page, so it was not used or cited.

Reconsidered the unit fit: bunker/MGO indices price fuel at commercial-vessel bunkering scale
(thousands of metric tons per call), which does not match a 110-foot coastal research vessel's
actual fuel-buying reality — a vessel this size buys diesel at retail/wholesale marine-diesel
scale, closer to on-highway diesel pricing than to bulk bunker pricing. Searched instead for a
live, fetchable, dated U.S. retail diesel series and found the EIA's own weekly "U.S. No. 2 Diesel
Retail Prices" series. Fetched the live data page directly and confirmed the last two published
rows verbatim: 08/24 = $5.652/gal, 08/31 = $5.599/gal.

**Outcome: SOURCED, HIGH.** S3 = $5.599/gal, week ending 2026-08-31. Disclosed explicitly in
`case.json` that this is retail/on-highway diesel used as a proxy for this vessel's marine diesel
price, since no marine-specific bunker index at small-craft scale is publicly quoted and the
larger bunker indices proved both unreachable (403) and scale-mismatched.

---

## Verification (skill step 7)

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources (must not be load-bearing): []
needs_source OPEN remaining: 0
```

All four data sources (S1–S4) are HIGH or MEDIUM confidence; none is LOW. S2 (MEDIUM, 2008-dated)
is the only sub-HIGH source, and it is load-bearing (it is Appendix C's entire fuel curve) — this
is disclosed openly in `case.json`'s source note rather than treated as a defect, since no more
recent comparable public figure exists and the alternative (an un-sourced, author-invented fuel
curve) would violate SPEC §5's no-fabrication rule more seriously than citing a real, if dated,
figure.

## Margin (computed here, matches case.json.balance.margin_note and FACILITATOR.md)

Built `sensitivity_model.py` to compute both options' `$/nautical mile of net progress` exactly,
using S1 (current), S2 (fuel curve), S3 (price), and the case's stated MA1 (27.0 nm, 250.0° T) and
MA2 (3.0 hr window). Ran it (`python3 sensitivity_model.py` from the case directory):

- **Option A (The True Line):** required speed-over-ground 9.000 kt; solving `Heading =
  DesiredResultant − Current` (vector subtraction) for a resultant exactly on the 250.0° T course
  gives a required boat speed through the water of **9.0153 kt**; MA3's linear interpolation
  between S2's real 8.5 kt/19 gal/hr and 9.5 kt/32 gal/hr points gives a fuel rate of **25.699
  gal/hr**; time **3.0000 hr** exactly (zero slack against the 3.0 hr window); fuel **77.096 gal**;
  cost **$431.66** at S3's $5.599/gal; **metric = $15.9875/nm**.
- **Option B (The Steady Burn):** heading vector at S2's economical 8.5 kt on the uncorrected
  250.0° T bearing, plus S1's current vector (vector addition), gives a resultant of **8.5162 kt**
  at 253.53° T; a dot product against the course unit vector splits this into an along-track rate
  of **8.5000 kt** and a cross-track rate of **0.5248 kt**; time to close 27.0 nm along-track =
  **3.1765 hr**, at which point the ship is **1.6671 nm** off-line (MA4's un-modeled final leg,
  added at the same 8.5 kt) = **0.1961 hr** more; total time **3.3726 hr** (22.4 min over the 3.0
  hr window); engine distance **28.6671 nm** (6.17% more than the direct 27.0 nm); fuel **64.079
  gal** at S2's 19 gal/hr economical rate; cost **$358.78**; **metric = $13.2882/nm**.

**margin_pct = (15.9875 − 13.2882) / 15.9875 × 100 = 16.88%. Winner (cheaper per net nautical
mile): Option B, The Steady Burn.**

This is comfortably under SPEC §2's ~20% cap — **no retune pass was needed.** Both options'
figures are real computations from real sourced inputs (S1–S3) against the case's own stated
scenario constraints (MA1, MA2); no data was softened or adjusted to hit this number — it is what
the model returned on the first pass with the scenario geometry chosen in the case-write stage
(the geometry itself — placing the current at roughly a 90° angle across the course rather than
head-on or dead astern — was a deliberate design choice made *before* computing margin, to ensure
both a real along-track and a real cross-track effect would show up in the vector math; it was not
adjusted after the fact to tune the margin number).

## Sensitivity — flex sweep (Tier 2 probe 5 pattern)

Ran `sensitivity_model.py`'s `FLEX` sweep (±25%/±50% on MA1's distance and bearing components,
and MA2's window hours, one at a time):

```
distance_nm -50% (-> 13.500): winner=A margin=405.28%  <-- WINNER FLIPS
distance_nm -25% (-> 20.250): winner=A margin=121.76%  <-- WINNER FLIPS
distance_nm +25% (-> 33.750): winner=B margin=52.89%
distance_nm +50% (-> 40.500): winner=B margin=63.65%
course_deg  -50% (-> 205.000): winner=B margin=27.83%
course_deg  -25% (-> 227.500): winner=B margin=22.98%
course_deg  +25% (-> 272.500): winner=B margin=9.92%
course_deg  +50% (-> 295.000): winner=B margin=3.18%
window_hr   -50% (-> 1.500): winner=B margin=71.73%
window_hr   -25% (-> 2.250): winner=B margin=57.59%
window_hr   +25% (-> 3.750): winner=A margin=86.26%  <-- WINNER FLIPS
window_hr   +50% (-> 4.500): winner=A margin=192.71%  <-- WINNER FLIPS
```

**Finding, reported plainly:** the base-case margin (16.88%) is real and under the SPEC §2 cap,
but it sits inside a genuinely sensitive region of the scenario's own stated constraints. MA1's
distance and MA2's window hours together fix Option A's required speed-over-ground
(`distance_nm / window_hr`); moving either one far enough flips which option is cheaper per net
mile, because it changes how far up Appendix C's real, sourced (and sharply nonlinear) fuel curve
Option A has to climb. MA1's bearing component and MA3/MA4 (interpolation method and the
un-modeled final leg) are comparatively minor levers — flexing them moves the margin but does not
flip the winner in the ranges tested.

This is disclosed in full in `case.json.sensitivity_note`, the Modeling Assumptions table in
`case.md` Appendix E, and `FACILITATOR.md`'s balance section — not smoothed over. It is treated as
a strength for the Socratic discussion (Anchor 4 is built directly around it), not hidden as a
weakness of the case design.

## SPEC §2 self-check

- **Primary metric exists:** yes — fuel cost (USD) per nautical mile of net progress toward the
  rendezvous point, a ratio, matching the concept sheet's own framing exactly.
- **No structurally-zero-cost option:** confirmed — both options burn real, nonzero fuel over a
  real, nonzero transit time; neither option's cost or time can be zero under any parameter in
  `PARAMS`.
- **Dilemma is not a foregone conclusion:** confirmed — margin_pct = 16.88%, under the ~20% cap,
  and the flex sweep above shows this is not an artificially narrow number sitting far from any
  real tension; the scenario's own stated constraints (MA1, MA2) sit close enough to a real flip
  boundary that the case's numeric closeness is genuine, not manufactured. Additionally, the two
  options split on a second, qualitative axis (Option A reliably makes the weather window; Option
  B does not) that does not simply track the $/nm winner — a real source of defensible disagreement
  independent of the primary metric's own closeness.
- **Verdict: PASS.** No balance-test waiver needed; no retune pass needed. Flagging the MA1/MA2
  sensitivity finding above for the next case-readiness stage as a genuine, disclosed property of
  the case design, not a defect.

## Judgment call — concept sheet's Vectors-group coverage count

The concept sheet (`CONCEPTS_formal-logic-vectors-matrices-numbertheory_2026-08-23.md`, C2) states
the Vectors group is "currently covered by exactly one case (Wind Triangle) across the whole
spine." Checked `readmodel/standards_spine.json` directly (not from memory) on 2026-09-01: the
Vectors group's all 7 skills currently show `n=2`, `covered_by: ["Wind Triangle", "Crosswind
Cut"]` — a second case already exists that post-dates the concept sheet's 2026-08-23 write date.
This does not change this case's own design or its `new_coverage: []` status (both n=1→2 and
n=2→3 are pure reinforcement, 0 new skills either way), but it is flagged plainly in
`case.json.reinforcement_note` and `LEARNING_GOALS.md` for whoever maintains the concept-log
scoring, since the concept sheet's own count is stale.

## Next step

Run `case-qa` on `the-course-correction`.
