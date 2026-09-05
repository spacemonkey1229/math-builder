# Case Study: The Two Offers

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

Two PDFs sit open in twin browser tabs, each headlined **ACCEPTANCE DEADLINE** in bold red. Maya Ortiz refreshes her inbox for no reason — nothing new is coming — and glances again at the offer letters she's had open since Tuesday. Her phone buzzes face-down on the kitchen table: a text from the Cascadia recruiter, then, thirty seconds later, one from Northwind. Both say some version of the same thing. *Just checking in — still good for Friday?*

She has read both letters enough times that she could recite the numbers in her sleep, and that's exactly the problem — she *has* memorized the numbers, and they still don't tell her who wins. Her roommate leans over the back of the couch, holding two mugs of coffee, and hands her one without a word. Maya sets her laptop flat on the table so both tabs show at once, side by side, cursor hovering between them.

Her mom already has an opinion. So does her academic advisor. So does the finance subreddit she posted in well after midnight last night. Nobody agrees, and nobody's plan matches how long Maya actually expects to stay in either job.

She opens a blank spreadsheet in a third tab, types a column header, deletes it, and types another. Somewhere in these two offer letters is a number that tells her which one is actually better — not on day one, but for as long as she's really going to be there. She just has to find it before Friday.

---

## Background

Maya Ortiz graduates this month with a degree in business analytics and has been offered the same kind of role — Junior Data Analyst — by two different companies, both of which she interviewed with over the past six weeks. She has no other offers on the table, no extensions available past this week, and a lease on her current apartment that ends in three months, so whichever offer she accepts will also decide where she's living.

The two offers are structured completely differently, and Maya and her friends have taken to calling them by shorthand: **the Steady Offer**, from Cascadia Robotics, and **the Frontloaded Offer**, from Northwind Analytics.

The Steady Offer is an on-site role at Cascadia Robotics' regional office. It carries a higher annual base salary and a smaller one-time signing bonus, paid in Maya's first paycheck (SEE APPENDIX A). Because the role is on-site, Maya would also take on a recurring monthly commuting and parking cost that the Frontloaded Offer does not carry (SEE APPENDIX A).

The Frontloaded Offer is a fully remote role at Northwind Analytics. It carries a lower annual base salary but a larger one-time signing bonus, plus an employer 401(k) match Cascadia does not offer (SEE APPENDIX B). Because the role is remote, Maya would keep working from her current apartment, avoiding the commuting and parking cost entirely and effectively banking that amount every month instead (SEE APPENDIX B).

Both companies require an answer by the same deadline this week, and neither will extend it. Maya cannot negotiate either offer's structure further — SEE APPENDIX C for the modeling assumptions her decision rests on. All figures in this case are sourced in (SEE APPENDIX E). For optional background reading on the math concepts involved, not required for any Challenge, SEE APPENDIX D.

The vocabulary and "how to…" skills this case will ask of you are listed in **Appendix F** — that is where Challenge 1 sends you.

---

## Dilemma

You are Maya Ortiz.

Do you:

**A.)** Accept the Steady Offer from Cascadia Robotics — higher base salary, smaller signing bonus, standard on-site benefits **OR**

**B.)** Accept the Frontloaded Offer from Northwind Analytics — lower base salary, larger signing bonus, employer 401(k) match, and remote-work commuting savings

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    - **D1 — A cumulative net value equation for each offer**, in the form V(t) = (net monthly value)(t) + (one-time signing bonus), where t is months on the job — with the slope and y-intercept identified and justified from the offer data in Appendices A and B for each offer.
    - **D2 — A graph plotting both offers' equations on the same axes** over a stated tenure horizon, with the crossover point clearly marked.
    - **D3 — The exact crossover point**, found by solving the two offers' equations together as a system of linear equations — the exact month (and dollar value) at which both offers have delivered the same cumulative net value, shown with full algebraic work.
    - **D4 — A recommendation naming which offer wins for two different assumed tenure lengths**: one shorter than the crossover point from D3, and one longer — using the equations from D1 (not the graph alone) to justify each answer.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A: The Steady Offer — Cascadia Robotics

| | Value |
|---|---|
| Role | Junior Data Analyst, on-site |
| Annual base salary | $96,250 [S1] |
| One-time signing bonus | $8,663 [S1][S2] (derived — see Appendix F note) |
| Employer 401(k) match | None offered |
| Monthly commuting + parking cost | $520 [MA1] (stated modeling assumption — see Appendix C) |

Cascadia's offer letter states the signing bonus is paid in full with Maya's first paycheck and is not prorated or repayable if she stays less than a year.

---

## Appendix B: The Frontloaded Offer — Northwind Analytics

| | Value |
|---|---|
| Role | Junior Data Analyst, fully remote |
| Annual base salary | $80,000 [S3] |
| One-time signing bonus | $12,000 [S3][S2] (derived — see Appendix F note) |
| Employer 401(k) match | 4.7% of base salary [S4] = $3,760/yr ($313/mo) (derived — see Appendix F note) |
| Monthly commuting + parking cost | $0 (fully remote) |

Northwind's offer letter states the signing bonus is paid in full with Maya's first paycheck and is not prorated or repayable if she stays less than a year. The 401(k) match is credited monthly, starting with Maya's first paycheck, with no vesting delay stated in the offer letter.

---

## Appendix C: Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case author. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Cascadia's monthly commuting + parking cost | $520/month | No public source publishes a single combined "commuting + parking" figure for a generic mid-size-metro office job — it depends on individual commute distance and city. This case assumes a 12-mile one-way commute (24 miles/day round trip, 21 workdays/month = 504 miles/month) costed at the IRS 2026 standard mileage rate of $0.725/mile [S5] ($365/month), plus a representative mid-size-metro monthly parking rate of $155/month, based on Denver, CO [S6]. The IRS rate bundles fuel, maintenance, depreciation, and insurance — costs a commuter partly bears regardless of the job — so $520/month is a deliberately conservative (high) estimate of Cascadia's true marginal commuting cost. | Every $200/month change in this assumption shifts the D3 crossover point by roughly 0.4–0.5 months, because it changes Cascadia's net monthly value directly. It does not change which offer eventually wins over a multi-year horizon (Cascadia's base-salary advantage is far larger), but it does move the exact crossover month a Hero calculates in D3, and it is the single most defensible number in the case for a Hero to push back on in Challenge 2. |

---

## Appendix D: Learn More

Want to go beyond the required math? These are real, freely available resources — not required for any Challenge, but useful if you want more background.

- [Linear Equation — Wikipedia](https://en.wikipedia.org/wiki/Linear_equation) — a reference on how linear equations work, including the slope-intercept form used in Challenge 3's D1.
- [System of Linear Equations — Wikipedia](https://en.wikipedia.org/wiki/System_of_linear_equations) — explains what it means to solve two equations together, the method Challenge 3's D3 (crossover point) relies on.
- [401(k) — Wikipedia](https://en.wikipedia.org/wiki/401(k)) — background on how an employer match works, for context on Appendix B.

## Appendix E — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Entry-level ("new to the role") base salary, Data Analyst — Technology sector, national | $96,250/yr | Robert Half — [Data Analyst — Technology Salary (2026 Salary Guide)](https://www.roberthalf.com/us/en/job-details/data-analyst-technology) | 2026 edition | MEDIUM — real, dated, national staffing-firm salary survey; "Technology" sector is a proxy for the robotics-company setting, and Robert Half's "low" tier means "new to the role," not strictly "first job out of college." |
| S2 | Sign-on bonus size as a percent of base salary, Data Science role category | Median 9% of base · 75th percentile 15% of base | Pave — [What Is a Sign-On Bonus? Benchmarks](https://www.pave.com/blog-posts/what-is-a-sign-on-bonus-benchmarks) (140,000+ accepted offers, 3,000+ companies, Pave × Greenhouse, trailing 18 months) | Updated 2026-09-02 | MEDIUM — real, dated, well-attributed compensation-data aggregator; "Data Science" is an adjacent role category to "Data Analyst," and the median/75th-percentile split used for Cascadia vs. Northwind (below) is this case's own modeling choice, not a reported on-site/remote split. |
| S3 | Entry-level Data Analyst base salary, United States, all industries/locations | Median $80,000/yr (25th pct $65,000, 75th pct $100,000) | [Levels.fyi — Entry Level Data Analyst Salary in United States](https://www.levels.fyi/t/data-analyst/levels/entry-level/locations/united-states) | Live data, accessed 2026-09-03 | MEDIUM — self-reported/crowdsourced panel; the reported figure is "total compensation," used here as a proxy for base salary since entry-level data-analyst pay is overwhelmingly base with minimal bonus/equity. |
| S4 | Average employer 401(k) match across recordkept plans | 4.7% of pay (record high) | Vanguard — [25th "How America Saves" report](https://corporate.vanguard.com/content/corporatesite/us/en/corp/who-we-are/pressroom/press-release-vanguards-twenty-fifth-how-america-saves-reveals-quiet-retirement-revolution-061626.html) | Published 2026-06-16, covers 2025 plan-year data | HIGH — primary source (the recordkeeper itself), dated, unambiguous units, nationally representative across Vanguard-administered plans. |
| S5 | Per-mile cost of operating a personal vehicle | $0.725/mile | IRS — [IRS sets 2026 business standard mileage rate at 72.5 cents per mile](https://www.irs.gov/newsroom/irs-sets-2026-business-standard-mileage-rate-at-725-cents-per-mile-up-25-cents) | Effective 2026-01-01 | HIGH — primary government source, dated, unambiguous; used here (see MA1) as an upper-bound proxy for commuting cost, since the rate also bundles depreciation and insurance a car owner incurs independent of commuting. |
| S6 | Representative monthly parking rate, mid-size US metro downtown | $155/month (Denver, CO) | [SpotHero — Denver, CO Monthly Parking](https://spothero.com/city/monthly/denver-parking) | Live pricing, accessed 2026-09-03 | MEDIUM — real marketplace pricing page, but undated/live rather than a fixed historical report; used only inside Modeling Assumption MA1, never as a standalone constraint. |

**Derivations shown:**
- Cascadia signing bonus [S1-D1] (Appendix A): $96,250 [S1] × 9% [S2, median] = $8,662.50 → rounded to $8,663.
- Northwind signing bonus [S3-D1] (Appendix B): $80,000 [S3] × 15% [S2, 75th percentile] = $12,000 exactly.
- Northwind 401(k) dollar value [S4-D1] (Appendix B): $80,000 [S3] × 4.7% [S4] = $3,760/yr = $313.33/mo, credited monthly per the offer letter.
- Cascadia commuting + parking cost (Appendix A, MA1): (24 mi/day × 21 days/mo × $0.725/mi [S5]) + $155/mo parking [S6] = $365.40 + $155 = $520.40/mo → rounded to $520/mo.

## Appendix F — "How To…" Math Questions To Research

**Vocabulary**

System Of Equations · Slope · Y-Intercept

**How to…**

- How to write a linear equation given a set of data
- How to identify the slope of a line given a set of data, or a graph of a line of a set of data, or its linear equation
- How to solve a system of linear equations
- How to draw a line of a set of data given its linear equation
