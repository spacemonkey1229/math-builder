Case Study: The Tap Date
MS | Math | Case Study | 2026 | Adventure

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->

---

## Overview

The sugarhouse is cold enough that Ansel Pelletier can see his breath over the evaporator pan, a long steel tray he has scrubbed twice since Christmas and that has not yet held a drop. Outside, the January snow squeaks under his boots all the way down the sap line, a blue tube strung from maple to maple like a clothesline for giants, carrying the sap down to the sugarhouse. He walks it end to end, thumbing ice off the fittings, listening to nothing. In a few weeks the whole woods will start to tick and drip, and the family will be at the pan until their eyes burn.

His cousin Corinne is waiting at the door when he comes back, one glove off, stamping her boots. She has already told her boss she is taking the season unpaid, and so has her brother. What neither of them has told the boss is the day. Ansel's father tapped when the calendar said it was time and never once explained why that day. Corinne reads weather records for fun and calls the calendar a habit. Ansel has promised her a day by tonight, and the records she means are sitting unopened on his kitchen table.

Corinne zips her coat up to her chin. "So," she says. "Which day do I tell them?"

---

## Background

Ansel Pelletier runs a family sugarhouse near Burlington, Vermont, where sap from the sugarbush (the family's stand of maple trees) is boiled down in an evaporator pan (a long shallow pan over a fire) into maple syrup. (The people and the sugarbush are invented; the weather is real.) Each year he picks the tap day: drilling a hole in each tree and setting a spout (a small tube) in it to carry the sap away. Each tree is tapped once a season; there is no re-drilling. Two relatives take unpaid leave for the whole season.

**The two options.** The **Early Tap** starts the season on February 20. The **Late Tap** starts it on March 1. The relatives' employers grant leave for one block only, and the forms are due this week, so there is no third date (a scenario input). A drilled hole dries and clogs after some weeks as microbes grow in it [S6], so each tap hole is assumed to stay productive for 42 [MA1] days counting from the day it is drilled (a scenario input); the leave covers exactly that window. A season is that window: February 20 through April 2 for the Early Tap and March 1 through April 11 for the Late Tap (SEE APPENDIX D).

**What counts.** Maple sap runs when freezing nights are followed by thawing days: a freeze draws water into the wood and the thaw pushes sap out of the tap hole [S5][S7] (SEE APPENDIX E). The case counts **run days**, a stand-in for sap flow that nobody measured in this bush; more run days means more days when sap is likely to flow. A day is a run day when its high is at least 35 [MA2] degrees Fahrenheit and its low is at most 27 [MA2] degrees Fahrenheit. Call this the **Primary Rule**. Two other rules are on the table, **Plain Freeze-Thaw** (high at least 32 [MA3], low at most 32 [MA3]) and **Warm Day, Any Frost** (high at least 35 [MA3], low at most 32 [MA3]); all three are defined in (SEE APPENDIX B), with every season's run days in (SEE APPENDIX C).

**What Ansel fixed before he looked.** On January 26, 2026, before counting anything, Ansel fixed: the Burlington airport weather station (SEE APPENDIX A), the window above, the two dates, and the Primary Rule. He judges the dates by **mean run days over the 30 most recent complete seasons, 1996 through 2025 [MA5]** (higher wins). The **margin** is the difference of the two means divided by the larger, as a percent. The airport is the longest nearby record, but an open airfield is not a wooded hillside (SEE APPENDIX D). You may test Ansel's run-day rule against the others, but your pitch must take a stand and say which run-day rule and which record you stand on.

**In this packet.** Seasons through 2025 and nothing later; other figures are sourced or declared in (SEE APPENDICES D AND E). Skills to research: (SEE APPENDIX F).

---

## Dilemma

You are Ansel Pelletier.

Do you:

**A.)** Tap on February 20 (the Early Tap) **OR**

**B.)** Tap on March 1 (the Late Tap)

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:

- **D1 — Both dates on one scatter plot.** A scatter plot of run days against season year, 1950 through 2025, under the Primary Rule (Appendix C), with the Early Tap and the Late Tap each as its own set of points and a line of best fit drawn through each set. One sentence per line saying whether the correlation between year and run days is positive, negative or close to none, and how strong it is.
- **D2 — The two lines as equations.** For each line, a linear equation (run days = slope × year + intercept) with the slope also written in run days per decade, and the season year at which the two lines meet, found by solving the two equations together. Say what the crossing year means for Ansel's choice and what you would not trust it to say.
- **D3 — The baseline table.** Under the Primary Rule, for the records 1950–1979, 1991–2020, 1996–2025, 2006–2025 and 1950–2025: the mean run days for each date, the winner, the margin as a percent, and the number of seasons in which each date had more run days than the other.
- **D4 — The rule-by-record map.** For the records 1991–2020, 1996–2025, 2006–2025 and 1950–2025, repeat the means, winner and margin under each of the three rules (Appendix B), and give each rule's two slopes per decade and its crossing year from the lines fitted to 1950–2025. Show the result as a table or chart that marks, for every rule and record, which date wins and by how much. Then name the rule and record you stand on, and the one cell on your map that would reverse your pick.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

## Appendix A — The Station and the Record

Referenced in Background and in Challenges (D1 to D4).

| Item | Value | Note |
|---|---|---|
| Station | Burlington International Airport, Vermont (GHCN-Daily ID USW00014742); latitude 44.4683, longitude -73.1500, elevation about 101 m [S1][S4] | NOAA NCEI GHCN-Daily, described in Menne et al. 2012 [S2] |
| Variables used | Daily maximum and minimum temperature (TMAX, TMIN) | Stored in tenths of a degree Celsius [S3]; converted to Fahrenheit exactly, with no rounding |
| Seasons in Appendix C | 1950 through 2025 (76 seasons) | A season is labeled by the year of its tap date |
| Missing days | None in any season window used | Every day of every window has both a high and a low |
| Days NOAA's quality checks flagged as errors, February to April | None | No flagged day appears in these windows |
| Reporting precision | From 2013 on, between about 12% and 27% each year [S1] of the daily highs and lows are recorded to a finer fraction of a degree than before | Before 2013 every value is a whole degree Fahrenheit once converted; the reason for the change is not established here. A finer value can move a day across a threshold, so treat this as a caveat on the data, not something to correct |
| What the station is not | An airport, not a sugarbush | Temperatures in a woods differ from an airfield (Appendix D, MA4) |

---

## Appendix B — The Three Rules

Referenced in Background and in Challenges (D4). A day is a run day when both conditions hold. All temperatures are degrees Fahrenheit.

| Rule | Day's high is at least | Night's low is at most |
|---|---|---|
| Primary Rule (fixed by Ansel before he looked) | 35 [MA2] | 27 [MA2] |
| Plain Freeze-Thaw | 32 [MA3] | 32 [MA3] |
| Warm Day, Any Frost | 35 [MA3] | 32 [MA3] |

(SEE APPENDIX D) for how the thresholds were chosen.

---

## Appendix C — Run Days per Season, 1950 through 2025

Referenced in Background and in Challenges (D1 to D4). Each cell counts the run days inside the season's window of 42 [MA1] days counted from the tap date. Derived by the case author from the station's daily highs and lows (SEE APPENDIX A) and the three rules (SEE APPENDIX B). Early Tap = February 20 start; Late Tap = March 1 start. In a leap year the Early window ends a day earlier.

| Season | Primary Rule: Early Tap | Primary Rule: Late Tap | Plain Freeze-Thaw: Early Tap | Plain Freeze-Thaw: Late Tap | Warm Day, Any Frost: Early Tap | Warm Day, Any Frost: Late Tap |
|---|---|---|---|---|---|---|
| 1950 | 10 | 14 | 20 | 25 | 15 | 20 |
| 1951 | 12 | 10 | 26 | 24 | 23 | 21 |
| 1952 | 11 | 9 | 26 | 22 | 20 | 20 |
| 1953 | 8 | 5 | 23 | 17 | 20 | 16 |
| 1954 | 18 | 18 | 30 | 27 | 24 | 21 |
| 1955 | 11 | 11 | 27 | 28 | 19 | 22 |
| 1956 | 10 | 11 | 22 | 27 | 14 | 19 |
| 1957 | 18 | 19 | 31 | 33 | 26 | 29 |
| 1958 | 15 | 14 | 36 | 36 | 28 | 29 |
| 1959 | 14 | 14 | 21 | 22 | 18 | 20 |
| 1960 | 7 | 12 | 17 | 22 | 10 | 17 |
| 1961 | 15 | 14 | 29 | 30 | 22 | 23 |
| 1962 | 16 | 17 | 31 | 33 | 25 | 27 |
| 1963 | 12 | 16 | 24 | 32 | 14 | 22 |
| 1964 | 13 | 18 | 24 | 29 | 18 | 23 |
| 1965 | 14 | 17 | 22 | 27 | 18 | 23 |
| 1966 | 16 | 13 | 23 | 26 | 19 | 22 |
| 1967 | 10 | 13 | 17 | 24 | 14 | 20 |
| 1968 | 10 | 13 | 19 | 25 | 18 | 24 |
| 1969 | 12 | 18 | 21 | 25 | 16 | 23 |
| 1970 | 14 | 19 | 21 | 28 | 18 | 25 |
| 1971 | 6 | 11 | 22 | 27 | 10 | 16 |
| 1972 | 9 | 16 | 17 | 23 | 13 | 20 |
| 1973 | 10 | 12 | 21 | 26 | 20 | 25 |
| 1974 | 15 | 15 | 29 | 29 | 21 | 21 |
| 1975 | 17 | 16 | 30 | 30 | 24 | 22 |
| 1976 | 13 | 13 | 26 | 26 | 20 | 22 |
| 1977 | 10 | 15 | 22 | 24 | 20 | 22 |
| 1978 | 8 | 13 | 16 | 21 | 13 | 18 |
| 1979 | 12 | 10 | 21 | 23 | 20 | 21 |
| 1980 | 13 | 12 | 21 | 20 | 18 | 19 |
| 1981 | 9 | 7 | 22 | 22 | 18 | 18 |
| 1982 | 11 | 13 | 21 | 25 | 16 | 20 |
| 1983 | 16 | 13 | 30 | 26 | 25 | 22 |
| 1984 | 12 | 16 | 21 | 24 | 17 | 20 |
| 1985 | 16 | 13 | 26 | 26 | 21 | 21 |
| 1986 | 13 | 13 | 19 | 20 | 17 | 19 |
| 1987 | 15 | 12 | 27 | 24 | 24 | 23 |
| 1988 | 14 | 11 | 21 | 16 | 18 | 14 |
| 1989 | 14 | 15 | 25 | 26 | 22 | 23 |
| 1990 | 14 | 13 | 20 | 22 | 18 | 19 |
| 1991 | 16 | 14 | 25 | 24 | 21 | 21 |
| 1992 | 14 | 12 | 24 | 23 | 18 | 21 |
| 1993 | 14 | 17 | 23 | 29 | 22 | 27 |
| 1994 | 12 | 13 | 27 | 33 | 21 | 26 |
| 1995 | 14 | 17 | 23 | 27 | 21 | 24 |
| 1996 | 18 | 18 | 25 | 27 | 24 | 26 |
| 1997 | 13 | 14 | 23 | 25 | 17 | 20 |
| 1998 | 11 | 8 | 23 | 20 | 19 | 19 |
| 1999 | 12 | 11 | 20 | 22 | 18 | 20 |
| 2000 | 9 | 7 | 28 | 27 | 23 | 23 |
| 2001 | 15 | 14 | 27 | 31 | 21 | 25 |
| 2002 | 15 | 14 | 28 | 30 | 22 | 23 |
| 2003 | 13 | 12 | 21 | 26 | 18 | 19 |
| 2004 | 13 | 16 | 23 | 25 | 20 | 24 |
| 2005 | 18 | 18 | 23 | 24 | 20 | 23 |
| 2006 | 9 | 11 | 21 | 24 | 17 | 22 |
| 2007 | 14 | 15 | 20 | 26 | 17 | 22 |
| 2008 | 18 | 17 | 27 | 28 | 20 | 23 |
| 2009 | 12 | 12 | 24 | 23 | 18 | 20 |
| 2010 | 13 | 11 | 33 | 24 | 30 | 23 |
| 2011 | 10 | 13 | 28 | 31 | 19 | 25 |
| 2012 | 13 | 7 | 21 | 16 | 18 | 14 |
| 2013 | 10 | 11 | 32 | 31 | 22 | 24 |
| 2014 | 12 | 13 | 21 | 24 | 19 | 22 |
| 2015 | 12 | 13 | 20 | 26 | 17 | 24 |
| 2016 | 13 | 11 | 26 | 26 | 24 | 22 |
| 2017 | 11 | 9 | 22 | 20 | 20 | 18 |
| 2018 | 9 | 14 | 31 | 34 | 27 | 30 |
| 2019 | 17 | 14 | 30 | 31 | 26 | 27 |
| 2020 | 11 | 8 | 24 | 21 | 21 | 18 |
| 2021 | 14 | 13 | 24 | 20 | 20 | 18 |
| 2022 | 13 | 9 | 20 | 18 | 16 | 15 |
| 2023 | 12 | 11 | 30 | 30 | 25 | 25 |
| 2024 | 9 | 7 | 26 | 24 | 26 | 24 |
| 2025 | 11 | 11 | 28 | 26 | 22 | 21 |

---

## Appendix D — Modeling Assumptions

Referenced in Background and in Challenges (D2 to D4).

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case author. A Hero may challenge them in discussion; that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Productive life of a tap hole | 42 days | No single published figure was found. Sugarmakers report that holes drilled too early can dry out by mid-April [S6]; the case fixes one length for both dates so the windows are comparable. | The answer to the dilemma is sensitive to this value. |
| MA2 | The Primary Rule as a stand-in for sap flow | High at least 35, low at most 27 | Sap flow needs freezing and then thawing [S5][S7]; no authority publishes one agreed temperature rule, and the case author chose a clearly-below-freezing night and a clearly-above-freezing day. | The answer to the dilemma is sensitive to these thresholds. |
| MA3 | The two other rules | Plain Freeze-Thaw: high at least 32, low at most 32; Warm Day, Any Frost: high at least 35, low at most 32 | Plain Freeze-Thaw is the literal reading of "freezing night, thawing day"; the other keeps the Primary Rule's day and loosens only the night. | The answer to the dilemma is sensitive to the choice of rule. |
| MA4 | The airport stands in for the sugarbush | Station daily highs and lows | The sugarbush has no long record. A university specialist notes that one location's air temperature does not capture variation across a sugarbush [S7]. | The sugarbush may differ from the airfield in ways this case cannot measure. |
| MA5 | The judging record | The 30 most recent complete seasons, 1996 through 2025 | Fixed by Ansel before results, with the scope in Background; other records are D3's work. | The answer to the dilemma is sensitive to which seasons are used. |
| MA6 | Only two dates, same window length | Early Tap and Late Tap, equal windows | The relatives' leave covers one block (Background). | A third date is outside this case. |
| MA7 | What run days leave out | Sap sugar content, how much sap a run day yields, labor, tap-hole health | Not measured in public data. | Run days count how often conditions are right, not how much syrup results. |

---

## Appendix E — Sources

Referenced in Background and in Challenges (D1 to D4). Dates are the dates the pages were fetched (2026-10-28).

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Daily maximum and minimum temperature, Burlington International Airport; the three rules' run-day counts in Appendix C are derived from it | Station file USW00014742, daily values from 1940-12-01 to 2026-10-24 (seasons 1950-2025 used) | NOAA NCEI, GHCN-Daily station file ([link](https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/USW00014742.csv)) | fetched 2026-10-28 | HIGH |
| S2 | How GHCN-Daily is built and how to cite it | Menne et al. 2012, J. Atmos. Oceanic Technol. 29, 897-910 | Menne, Durre, Vose, Gleason, Houston, "An overview of the Global Historical Climatology Network-Daily Database" ([doi](https://doi.org/10.1175/JTECH-D-11-00103.1)) | 2012 | HIGH |
| S3 | Units of TMAX and TMIN; version and citation request | Tenths of degrees Celsius; GHCN-Daily Version 3.35 | NOAA NCEI, GHCN-Daily README ([link](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt)) | fetched 2026-10-28 | HIGH |
| S4 | Station name, coordinates and elevation | USW00014742, BURLINGTON INTL AP, VT, 44.4683, -73.1500, 101.2 m | NOAA NCEI, ghcnd-stations.txt ([link](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt)) | fetched 2026-10-28 | HIGH |
| S5 | Sap flow follows a cycle of freezing nights and thawing days | Qualitative; no temperature thresholds given | Science Friday, "How The Sap Runs", April 5, 2019 ([link](https://www.sciencefriday.com/segments/how-the-sap-runs/)) | 2019-04-05 | MEDIUM |
| S6 | Tap holes drilled too early can dry out by mid-April | Qualitative; no number of days given | Chuck Wooster, "Keeping Tap Holes Clean", The Outside Story, Northern Woodlands ([link](https://northernwoodlands.org/outside_story/article/keeping-tap-holes-clean)) | 2011-03-14 | MEDIUM |
| S7 | Freezing and thawing drive sap flow; air temperature at one location does not capture the variation across a sugarbush | Qualitative; no agreed thresholds given | Tim Wilmot, University of Vermont Extension, "Temperatures in the Sugarbush", Maple Syrup Digest, June 2006 ([link](https://www.uvm.edu/d10-files/documents/2024-10/temperaturesinsugarbush2006.pdf)) | 2006-06 | HIGH |

**A figure left out.** No published single figure for how many days a tap hole stays productive was found, so the case states it as an assumption (MA1) instead of citing one. No published, agreed temperature rule for a "run day" was found either, so the three rules are stated assumptions (MA2, MA3).

---

## Appendix F — "How To…" Math Questions To Research

Referenced in Challenge 1. The questions below are the skills this case asks you to use.

**Vocabulary terms**

- Scatter Plot
- Correlation
- Line Of Best Fit
- Slope
- System Of Equations
- Mean

**"How to…" questions**

- How to create a scatter plot given a set of data
- How to identify correlation given a scatter plot or set of data
- How to draw a line of best fit given a set of data
- How to identify the slope of a line given a set of data, or a graph of a line of a set of data, or its linear equation
- How to write a linear equation given a set of data
- How to solve a system of linear equations
- How to find the mean of a set of data
