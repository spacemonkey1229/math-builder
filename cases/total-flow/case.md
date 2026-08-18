Case Study: Total Flow
MS | Math | Case Study | 2026 | Launchpad

## Overview

The wind coming off the river keeps trying to turn the pages, so Nadia Brennan holds the binder
flat with her forearm and reads the same column again.

She is standing on the levee crown at the reach the district board has taken to calling the soft
spot, boots in wet crown gravel, watching a fisherman's truck idle on the access road below.
Behind her the town's water tower is close enough to read. In front of her the channel is running
low and brown and completely harmless-looking, which is the part she has never been able to get
the board to feel.

Nadia is the district's engineer of record. When the design certification goes out, her seal is
the one on it — not the board's, not the contractor's — and that certification says this levee
will hold what the river sends. She has one construction season and one appropriation, and she has
spent the better part of a month learning that the river does not send the same thing twice.

Two binders, flat on the tailgate. One holds a storm that arrived like a slammed door, up and over
and gone before the district's own crews had finished sandbagging the boat ramp. The other holds a
storm that never looked frightening on any single morning and simply refused to leave.

Her phone buzzes against the truck bed. The board chair. The bid package goes out at the end of
the week, and it can describe exactly one design.

Nadia looks at the channel, then at the binders, then at the channel again.

## Background

Nadia Brennan is the district engineer for the Marrow Bend Levee District, a small
special-purpose district responsible for a single leveed reach on Henderson Creek in western
Illinois. The board controls the appropriation; the design certification carries Nadia's
professional seal, and she is personally accountable for the standard she certifies to.

Henderson Creek is gaged continuously by the U.S. Geological Survey, which publishes a daily mean
discharge — the average rate of flow past the gage, in cubic feet per second — for every day of
record (SEE APPENDIX A). Two real floods from that record are the district's design storms this
season: **The Slammed Door**, a short, violent event, and **The Long Guest**, a flood that ran for
days (SEE APPENDIX A).

Below a certain discharge — the reach's **channel capacity** — the channel carries the creek
without loading the levee at all. Above that rate, every additional cubic foot per second is water
the district's works have to handle (SEE APPENDIX B). That water, and only that water, is what
this case calls **floodwater**: the volume above channel capacity. Flow at or below channel
capacity is not floodwater, and it never enters the board's number for either bid. Appendix B also
carries the gage's published flood-frequency record, which the district's engineering standards
require the certification to reference.

A design **safely manages** floodwater when that water is either carried inside the channel the
design provides or held in the storage the design provides. Floodwater that is neither is a
**shortfall**. Two bids are on the table and the appropriation pays for exactly one
(SEE APPENDIX C).

**The Crest Standard** raises and armors the levee crown so the channel itself carries a higher
discharge. It handles any flow at or below its design discharge for as long as the storm lasts —
duration is free — and everything above that design discharge is a shortfall, no matter how
briefly it lasts.

**The Basin Standard** leaves the crown where it was built and buys two upstream floodwater
detention structures. They absorb flow above channel capacity at any rate at all — peak is free —
but only until their storage is full; everything after that is a shortfall.

The board scores the two bids on one number, stated in the bid package: **acre-feet of floodwater
safely managed per one thousand dollars of appropriation, totalled across both design storms**
(SEE APPENDICES C AND D). Appendix D also carries the conversion the district's reports use to
turn a discharge rate into a volume, and the appropriation the board has voted.

Nadia may not change either bid's scope and may not change the river. Where a figure below is not
a matter of public record it is stated as an explicit modeling assumption (SEE APPENDIX F) rather
than guessed, and every sourced figure is listed in APPENDIX E. The vocabulary and the "how to…"
skills this case will ask of you are listed in APPENDIX H — that is where Challenge 1 sends you.
Curious what any of this looks like in the field, beyond the math? SEE APPENDIX G for further
reading.

## Dilemma

You are Nadia Brennan.
Do you:
A.) Certify The Crest Standard — raise and armor the levee crown so the channel carries a higher
discharge, for however long the storm lasts OR
B.) Certify The Basin Standard — leave the crown as built and buy upstream detention storage that
absorbs flow above channel capacity until it fills

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A Riemann sum for the total water volume that passed the gage during each design storm
    in APPENDIX A: state the interval width you used and where inside each day you placed that
    day's value (APPENDIX D says how to read the table as a function of time), show the sum,
    convert the result to acre-feet using the factor in APPENDIX D, and say in one sentence
    whether your sum over-estimates, under-estimates, or exactly reproduces the volume in the
    published record — and how you know which of the three it is.
    D2. For each design storm, a fitted discharge function Q(t) over the storm window, its
    indefinite integral written as a general antiderivative with the constant of integration
    shown, and the definite integral of Q(t) across the storm window evaluated by the
    Fundamental Theorem of Calculus — with that result compared, in acre-feet, against your D1
    Riemann sum for the same storm.
    D3. For each design storm, a shaded diagram and a computation of the area between your
    Q(t) curve and the horizontal channel-capacity line from APPENDIX B, over the interval where
    the storm exceeds capacity. State the limits of integration and show how you found them.
    This is the floodwater the district's works have to handle. Then state the same floodwater
    volume read straight off APPENDIX A's daily values, and account for the difference between
    the two figures.
    D4. A "floodwater safely managed" table for The Crest Standard and The Basin Standard across
    both design storms, in acre-feet and built from APPENDIX A's daily values, with each option's
    shortfall shown separately — then a final acre-feet-of-floodwater-safely-managed per one
    thousand dollars of appropriation figure for each option against APPENDIX C's bid prices, and
    your recommendation.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — The Gage and the Two Design Storms

| | Value |
|---|---|
| Gage name and USGS site number | Henderson Creek near Oquawka, Illinois — USGS 05469000 [S1] |
| Location | Henderson County, IL · 41.001425° N, 90.854308° W [S1] |
| Drainage area above the gage | 432 square miles [S1] |
| Gage altitude | 540.64 ft above NAVD88 [S1] |
| Regulation | Unregulated — no upstream reservoir controls the flow past this gage [S6] |

Both tables below are **daily mean discharge** in cubic feet per second, exactly as USGS
publishes them. Every value carries the USGS qualification code `A` — approved for publication,
review complete [S2, S3].

**Design Storm 1 — The Slammed Door** (February 2019)

| Date | Daily mean discharge (cfs) |
|---|---|
| 2019-02-22 | 413 |
| 2019-02-23 | 3,290 |
| 2019-02-24 | 8,060 |
| 2019-02-25 | 4,220 |
| 2019-02-26 | 1,130 |
| 2019-02-27 | 690 |
| 2019-02-28 | 490 |
| 2019-03-01 | 474 |

*(Source: [S2])*

**Design Storm 2 — The Long Guest** (April–May 2019)

| Date | Daily mean discharge (cfs) |
|---|---|
| 2019-04-28 | 225 |
| 2019-04-29 | 932 |
| 2019-04-30 | 3,000 |
| 2019-05-01 | 6,400 |
| 2019-05-02 | 6,700 |
| 2019-05-03 | 6,240 |
| 2019-05-04 | 3,980 |
| 2019-05-05 | 2,050 |
| 2019-05-06 | 1,490 |
| 2019-05-07 | 1,420 |

*(Source: [S3])*

## Appendix B — The Reach: Capacity and Flood-Frequency Record

| | Value |
|---|---|
| National Weather Service **minor flood stage** at this gage | 21.5 ft (action stage 20.0 ft; moderate and major flood stages are not defined for this gage) [S4] |
| **Channel capacity** — discharge at minor flood stage, from the gage's own rating | **1,934 cfs** [S5] |

**USGS stage-discharge rating 31.0 for site 05469000** (excerpt) [S5]

| Gage height (ft) | Discharge (cfs) |
|---|---|
| 20.00 | 1,415 |
| 21.50 | 1,934 |
| 22.00 | 2,147 |
| 23.00 | 2,663 |
| 24.00 | 3,290 |
| 25.00 | 4,117 |
| 26.00 | 5,927 |
| 26.50 | 7,049 |
| 27.00 | 8,337 |
| 28.00 | 11,488 |

**Published peak-flow frequency at this gage**, at-site estimates from 1924–2017 annual peaks [S6]

| Annual exceedance probability | Peak discharge (cfs) |
|---|---|
| 50% | 5,070 |
| 20% | 9,020 |
| 10% | 12,400 |
| 4% | 17,700 |
| 2% | 22,400 |
| 1% | 27,800 |
| 0.5% | 34,000 |
| 0.2% | 43,800 |

*These are **instantaneous** peak discharges. Every other discharge figure in this case is a
**daily mean**. The two quantities are not the same thing and are not directly comparable [S6, S7].*

## Appendix C — The Two Bids

Both bids came in at the appropriation ceiling in APPENDIX D — the board published the number, and
both contractors priced to it (SEE APPENDIX F, MA1).

| | Bid A: The Crest Standard | Bid B: The Basin Standard |
|---|---|---|
| Scope | Raise and armor 2.50 miles of levee crown by 4.50 ft | Two upstream floodwater detention structures |
| Discharge the channel then carries | **5,927 cfs** — the rating's value 4.50 ft above minor flood stage, at 26.00 ft [S5] | Unchanged at 1,934 cfs [S5] |
| Storage provided | None. The crest handles rate, not volume | **25,000 acre-feet** authorized — two structures at the 12,500 acre-foot per-structure ceiling in 16 U.S.C. 1002 [S8] |
| Usable storage at the start of a storm | — | **24,000 acre-feet** (SEE APPENDIX F, MA2) |
| Duration it can hold | Unlimited at or below its design discharge | Until the storage is full |
| Bid price | The full appropriation (SEE APPENDIX D) | The full appropriation (SEE APPENDIX D) |
| How its scope was priced | A comparable U.S. Army Corps of Engineers project raised a levee an average of 5 ft at a cost of $258 million across a 17-mile system [S9] | Detention pools are farmland; Illinois cropland averaged $9,850 per acre in 2025 [S10] |

**A levee is only as high as its lowest point.** Bid A raises the *whole* 2.50-mile reach or the
reach is not certified at all — the height in its scope line is the height it holds everywhere,
and it is what the contractor bid against the published appropriation, not a figure the district
derived (SEE APPENDIX F, MA1).

**Shortfall, per option.** Bid A's shortfall on a storm is the volume of flow above **5,927 cfs**.
Bid B's shortfall on a storm is the floodwater above channel capacity that its usable storage
cannot hold. The two design storms are ten weeks apart in the real record, and the detention
structures' outlet works draw a full pool down in far less time than that (SEE APPENDIX F, MA3),
so each storm meets the structures with their usable storage available.

## Appendix D — Units, Volume, and the Appropriation

| | Value |
|---|---|
| One cubic foot per second sustained for one day (one **cfs-day**) | 86,400 cubic feet = **1.98347 acre-feet** = 646,317 gallons [S7] |
| USGS on its own daily values | *"The daily mean discharges reported in the daily value data tables numerically are equal to the daily volumes in cfs-days, and the totals also represent volumes in cfs-days."* [S7] |
| District appropriation, this season | **$38,000,000** (SEE APPENDIX F, MA1) |
| Board's scoring number | **Acre-feet of floodwater safely managed per one thousand dollars of appropriation, totalled across both design storms** — *floodwater* being the volume above channel capacity, as defined in Background. Flow the channel would have carried anyway is not floodwater and is not scored for either bid. |

**Reading Appendix A as a function of time.** Every row of Appendix A is the mean discharge over
one whole day, not a reading taken at an instant. Let *t* be measured in days, with *t* = 0 at the
start of the first row's day; a storm of *n* rows then occupies the window 0 ≤ *t* ≤ *n* days, and
each row is the average value of Q on one one-day subinterval of it. Two things follow, and the
district's reports use both:

- Sum with Δ*t* = one day and **one subinterval per row**. Work out for yourself, from the USGS
  sentence above, what that sum returns and whether the choice of left, right or midpoint placement
  changes it — D1 asks you to say which, and why.
- A smooth curve fitted through the rows is a different object. Place each daily mean at the
  **midpoint** of its day (*t* = 0.5, 1.5, 2.5, …) if you fit one. Compare its integral against
  your sum, and be ready to say what any gap between the two is — and whether it is an error.

The district scores the bids on the published daily record, so every acre-foot in the D4 table
comes from Appendix A's daily values, not from a fitted curve.

## Appendix E — Sources

| id | Claim | Value | Source | Accessed | Confidence |
|---|---|---|---|---|---|
| S1 | Gage identity, location, drainage area, gage altitude | Henderson Creek near Oquawka, IL; USGS 05469000; 432 sq mi; 540.64 ft NAVD88 | U.S. Geological Survey, NWIS Site Service, expanded site record for 05469000 ([link](https://waterservices.usgs.gov/nwis/site/?format=rdb&sites=05469000&siteOutput=expanded)) | 2026-08-12 | HIGH |
| S2 | Daily mean discharge, Design Storm 1 | 413 / 3,290 / 8,060 / 4,220 / 1,130 / 690 / 490 / 474 cfs, 2019-02-22 to 2019-03-01, all code `A` | USGS NWIS Daily Values Service, site 05469000, parameter 00060, statistic 00003 ([link](https://waterservices.usgs.gov/nwis/dv/?format=rdb&sites=05469000&startDT=2019-02-15&endDT=2019-03-08&parameterCd=00060&statCd=00003)) | 2026-08-12 | HIGH |
| S3 | Daily mean discharge, Design Storm 2 | 225 / 932 / 3,000 / 6,400 / 6,700 / 6,240 / 3,980 / 2,050 / 1,490 / 1,420 cfs, 2019-04-28 to 2019-05-07, all code `A` | USGS NWIS Daily Values Service, same site and parameters ([link](https://waterservices.usgs.gov/nwis/dv/?format=rdb&sites=05469000&startDT=2019-04-24&endDT=2019-05-14&parameterCd=00060&statCd=00003)) | 2026-08-12 | HIGH |
| S4 | NWS flood-category stages for this gage | minor 21.5 ft; action 20.0 ft; moderate and major undefined | NOAA National Weather Service, National Water Prediction Service, gauge OQUI2 ([link](https://api.water.noaa.gov/nwps/v1/gauges/OQUI2)) | 2026-08-12 | HIGH |
| S5 | Stage-discharge rating for site 05469000 | rating 31.0: 21.50 ft = 1,933.91 cfs; 26.00 ft = 5,927.22 cfs (full excerpt in Appendix B) | USGS NWISWeb expanded rating table (`exsa`), site 05469000, rating retrieved 2026-07-02 ([link](https://waterdata.usgs.gov/nwisweb/get_ratings/?site_no=05469000&file_type=exsa)) | 2026-08-12 | HIGH |
| S6 | Peak-flow frequency quantiles and regulation status | 1% AEP 27,800 cfs (full table in Appendix B); `isRegulated: false` | USGS StreamStats GageStats service, station 05469000, peak-flow statistics, date range 1924–2017 ([link](https://streamstats.usgs.gov/gagestatsservices/stations/05469000?includeStats=true)) | 2026-08-12 | HIGH |
| S7 | Definition of a cfs-day, and that daily means equal daily volumes in cfs-days | 1 cfs-day = 86,400 cubic feet = 1.98347 acre-feet = 646,317 gallons | U.S. Geological Survey, *Water Resources Data — Definition of Terms* ([link](https://water.usgs.gov/ADR_Defs_2004.pdf)) | 2026-08-12 | HIGH |
| S8 | Statutory ceiling on a single watershed structure | no single structure above 12,500 acre-feet of floodwater detention capacity, or 25,000 acre-feet total capacity; watershed or subwatershed not above 250,000 acres | Watershed Protection and Flood Prevention Act, 16 U.S.C. § 1002 ([link](https://www.law.cornell.edu/uscode/text/16/1002)) | 2026-08-12 | MEDIUM |
| S9 | Cost of a comparable levee raise | $258 million for an average 5 ft raise, within a 17-mile, $529 million USACE project on the Kansas River | Giles Lambertson, *"USACE Begins Final Stage of $529M, 17-Mile Flood Protection Project in Kansas City,"* Construction Equipment Guide, 2022-08-31 ([link](https://www.constructionequipmentguide.com/usace-begins-final-stage-of-529m-17-mile-flood-protection-project-in-kansas-city/57707)) | 2026-08-12 | MEDIUM |
| S10 | Illinois cropland value per acre | $9,850 per acre, 2025 (up 3.1% from 2024) | USDA National Agricultural Statistics Service, *Land Values 2025 Summary*, August 2025, Cropland Average Value per Acre table ([link](https://www.nass.usda.gov/Publications/Todays_Reports/reports/land0825.pdf)) | 2026-08-12 | MEDIUM |

**Notes on the grades.** S8 is graded MEDIUM because the text was read from Cornell LII's
reproduction of the U.S. Code rather than from `uscode.house.gov`, which was not independently
fetched — the statute itself is not in doubt, the reproduction is what was checked. S9 is graded
MEDIUM because it is trade-press reporting of a Corps project rather than a Corps cost estimate,
and because the $258 million is attributed to the raising portion of a project that also included
floodwall work; it is used only to show that Bid A's scope is the right order of magnitude for the
appropriation, never as an input to the board's scoring number. S10 is graded MEDIUM for a
different reason: farmland values move every year, so this figure is a snapshot, not a constant
(SEE APPENDIX F, MA5).

## Appendix F — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, each with a real basis named below. A Hero may challenge any of them in discussion —
> that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | The district's appropriation, and that both bids come in at it | **$38,000,000**, both bids | The Marrow Bend Levee District is fictional and has no published budget. The figure is set so that each bid's scope is the right size of job against real unit costs: 2.50 miles of crest raise and armoring at the rate implied by S9 ($258M ÷ 17 mi ÷ 5,280 ft ≈ $2,874 per linear foot, for an average 5 ft raise across a 17-mile Corps program) is about $37.9M; two detention pools flooding roughly 3,100 acres of Illinois cropland at S10's $9,850 per acre is about $30.8M before embankments and outlet works. Public bodies publish a budget and bidders price a scope to it. The **4.50 ft** in Bid A's scope line is that bid's scope, not a height derived from S9's rate — a small district buying 2.50 miles of work does not get a 17-mile program's unit price, and this case does not claim it does. | **None on the recommendation.** Both options are divided by the same appropriation, so it cancels out of the comparison entirely. Flex it ±50% and satisfy yourself that the margin does not move. |
| MA2 | Share of authorized detention capacity unavailable when a storm arrives | **4.0%** of 25,000 acre-feet, leaving **24,000 acre-feet** usable | Detention structures lose capacity to sediment accumulation and may hold an antecedent pool at the onset of an event. These structures do not exist, so no measured figure can exist; 4% is a small, deliberately conservative reservation. | **The one genuinely load-bearing assumption in this case.** Flexed ±50% (2% to 6%) in the case's own sensitivity model: the recommendation does not change and the gap between the two options moves by about two percentage points. Note the ceiling this assumption sits under — 16 U.S.C. 1002 caps the authorized storage at 25,000 acre-feet [S8], so even a perfect 0% reservation cannot buy the Basin Standard more room than that. |
| MA3 | Time for the detention structures' outlet works to draw a full pool down | **10 days** | Standard practice sizes a flood-detention outlet to empty the pool within days, not weeks, so the storage is ready for the next event. | **None.** The two real design storms are 64 days apart at the gage, so any drawdown time from 5 to 15 days leaves the storage fully available for the second storm. |
| MA4 | The sustained-loading threshold used in Appendix F's projection | **4 consecutive days** on which the creek runs above channel capacity — "loading the levee" in the sense Background gives it, not the raised crown's own design discharge | The district's geotechnical report is a scenario device; no real report exists for a fictional reach. Sustained high water driving underseepage beneath an embankment is a real and well-documented levee failure mode. | Does not enter the base recommendation at all — it governs only the sustained-loading question, and nothing in the primary metric reads it. |
| MA5 | Data cutoff for every still-moving figure | **2026-08-12** | Illinois cropland values (S10), the USGS rating (S5, rating 31.0 as retrieved 2026-07-02), and the NWS flood-category stages (S4) all change over time. Every one of them is frozen at the date this case was researched, and none is refreshed independently of the others. | None on the arithmetic. It is what makes the case checkable: a future reader can re-fetch each source and see exactly what moved. |

**Two lines this case states rather than measures.** Neither is in the table above, because
neither is an estimate of an unknown quantity — each is a choice, made in the open, that the
arithmetic then obeys. Both move the answer further than anything in the table does.

1. **Channel capacity is taken to be the discharge at the National Weather Service's published
   *minor* flood stage** — 21.50 ft on Appendix B's rating. That is a choice of convention, not a
   measurement. Raising it shrinks both storms' floodwater volumes; lowering it grows them — and it
   does not grow the two storms' volumes at the same rate, which is something you can check and
   should. Every row of Appendix B's rating excerpt is a different convention, and moving one row is
   enough to move the recommendation.
2. **The height in Bid A's scope line is a bid's scope, not a property of the river.** It selects
   a second row of the same rating, and the discharge in Appendix C is whatever that row says. A
   different raise is a different bid, not a corrected number.

A Hero who wants to attack the recommendation should attack these two lines first, and should say
which row of Appendix B they are standing on when they do.

## Appendix G — Learn More

These are real, freely available resources for going beyond the required math — how streamgages
and levees actually work, and where the flood-control law behind Bid B comes from.

- [USGS Water Science School — How Streamflow is Measured](https://www.usgs.gov/special-topics/water-science-school/science/how-streamflow-measured) — the U.S. Geological Survey's own explanation of how a gage like the one on Henderson Creek converts stage (water height) into a discharge reading, the two-step process behind every number in Appendix A.
- [USGS Water Science School — Floods: Recurrence Intervals and 100-Year Floods](https://www.usgs.gov/special-topics/water-science-school/science/floods-and-recurrence-intervals) — a plain-language explanation of what an annual exceedance probability (like the 1% and 20% figures in Appendix B) actually means, and why a "100-year flood" is not a flood that happens once a century.
- [Wikipedia — Watershed Protection and Flood Prevention Act](https://en.wikipedia.org/wiki/Watershed_Protection_and_Flood_Prevention_Act) — background on the 1954 federal law (16 U.S.C. § 1002, cited as S8 in Appendix E) that caps the size of small-watershed detention structures like the ones in Bid B.
- [Construction Equipment Guide — USACE Begins Final Stage of $529M, 17-Mile Flood Protection Project in Kansas City](https://www.constructionequipmentguide.com/usace-begins-final-stage-of-529m-17-mile-flood-protection-project-in-kansas-city/57707) — a news account of the real Army Corps levee-raise project (cited as S9 in Appendix E) that Bid A's cost is benchmarked against, with photos and construction detail beyond the cost figure this case uses.

## Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Antiderivative
- Definite Integral
- Indefinite Integral
- Riemann Sum
- Area Between Two Curves

**"How to…" questions**

- How to find an antiderivative using the power rule
- How to evaluate a definite integral using the Fundamental Theorem of Calculus
- How to approximate area under a curve using a Riemann sum
- How to find the area between two curves

<!-- FACILITATOR ONLY -->

## Balance argument (facilitator only — never shipped to students)

**Argument for A (The Crest Standard).** Above channel capacity the two design storms carry
52,629 acre-feet of floodwater between them. The Crest Standard passes all but 7,323 acre-feet of
it — four days across the two storms, and never short by more than 2,133 cfs. It manages 45,306
acre-feet, ahead of the Basin Standard on the board's own number, and it does so without a single
acre of land taken out of production. Duration costs it nothing: The Long Guest ran six days above
capacity and the raised crown carried every one of them, clipping only the tops.

**Argument for B (The Basin Standard).** The Crest Standard's protection is a wall, and a wall has
an edge: on 2019-02-24 it was already 2,133 cfs short, and the published record at this gage says a
1% annual-exceedance peak is 27,800 cfs — several times the discharge the raised crown carries.
The Basin Standard has no such edge. Peak is free to it: it took all 19,374 acre-feet of The
Slammed Door, the very storm that beat the crest. What it ran out of was room, and only on the
second storm, where it held 24,000 of 33,255 acre-feet. It manages 43,375 acre-feet — behind by
less than the width of the one figure this case admits it invented (MA2), on a metric that counts
acre-feet and not the shape of the failure. And the line that decides it is a convention, not a
measurement: set channel capacity one row up Appendix B's own rating, at 22.00 ft instead of
21.50 ft, and the Basin Standard is the winner on the board's number.

**Margin.** Every figure is reproducible by hand from
Appendices A–D alone. See `case.json.margin_pct` and `case.json.derived`.

**Five Socratic questions (draft).**

1. Which of your two design storms carries more total water past the gage, and is that the same
   storm that reaches the higher peak discharge?
2. Your D1 Riemann sum and your D2 Fundamental-Theorem answer for the same storm are not the same
   number. Which one is closer to the truth, and how would you decide without being told?
3. The Basin Standard is described by a volume and the Crest Standard by a rate. What single
   mathematical operation converts one of those into the units of the other?
4. Each design fails somewhere — the Crest Standard on the four highest days, the Basin Standard
   on the back half of one storm. Whose failure is cheaper to be wrong about, and does the board's
   scoring number capture that at all?
5. Appendix F says channel capacity is a convention, not a measurement. If the district set it at
   a different flood stage, which option would gain?

**The trap.** A Hero compares the two storms' peak discharges, sees that 8,060 is bigger than
6,700, and treats that comparison as the answer — reading a hydrograph as a maximum instead of as
an accumulation. The Long Guest's lower peak sits above capacity for six days against The Slammed
Door's three, and carries 33,255 acre-feet against 19,374. Only integrating shows it.

**Sensitivity note (SPEC §6).** Flooding touches property and personal safety. This case is framed
entirely as protection — acre-feet safely managed, never damage inflicted or lives lost — but a
facilitator should check the room before running it.
