Case Study: The Eight-Percent Bet
MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

The sticky note is still on his monitor: *Call me back. He'll take it later if you add interest.*

Marcus Hale has been staring at it since the last home game ended. Below the window, the grounds crew drags the infield, and the smell of cut grass and fryer oil drifts up through a vent that never quite closes. Down the hall, a nameplate has been peeled off a locker that belonged to a player the club released this winter.

The club still owes that player the rest of his salary. Marcus can write the check this week and be done. Or he can say yes to the agent: let the money wait, let it earn interest on the player's side of the ledger, and bet that the club's own investments can outrun whatever the club will owe on the other side.

His owner doesn't care which. His owner cares that Marcus signs his name under it.

Two folders sit on the desk. One holds a check request form. The other holds a contract with a blank where an interest rate goes. Marcus pulls the cap off a pen and looks at the blank.

---

## Background

Marcus Hale is the finance director of the Harbor City Gulls, a professional baseball club. He does not choose the roster. His job is to tell the owner, in writing, what a money decision will cost the club and who has to cover it if it goes wrong.

The club released a veteran player but still owes him his salary for the season: $5,900,000 [MA1] (SEE APPENDIX A). The player's agent has offered Marcus a choice. The club can pay the full amount now, or it can defer it: the club pays nothing today, the unpaid amount earns interest at 8% [MA2] a year, and the club repays it in 25 [MA3] equal yearly payments, the first due 11 [MA4] years after signing (SEE APPENDIX A).

**The Clean Check** means paying the full amount owed today, so the club owes the player nothing afterward. **The Long Bet** means accepting the deferral, keeping the cash, and investing it under the club's investment policy (SEE APPENDIX C): 60% [MA6] in a broad index of large U.S. stocks and the rest in 10-year U.S. Treasury bonds, restored to those shares every January.

To keep the arithmetic on a single clock, this case treats every date as January 1. The cash is invested on January 1 of the signing year, the first payment is due on January 1 of the year the deferral names, and each later payment is due on January 1 as well. (Real contracts use other dates; the case simplifies.) The test of The Long Bet is a snapshot taken on the first payment date: is the invested pool worth at least what the club then owes? If the pool is short, the owner covers the gap out of the roster budget Marcus controls, in equal yearly amounts over the repayment years, at a funding rate you will choose in D6. If the pool is ahead, the club keeps the surplus. A club may not pay a player less than the league minimum, which in the first payment year was $414,000 [S1] (SEE APPENDIX C), so a yearly gap can be counted in roster spots.

The history of stocks and bonds is not a forecast, but it is the best evidence Marcus has. Appendix B lists the actual yearly return on each, year by year, for as long as the record goes back. Appendix D is a blank balance table to build the repayment work on. Appendix E lists the stated assumptions and the ones you must choose and defend, Appendix F lists every source, and Appendix G lists the "how to…" questions you will research.

---

## Dilemma

You are Marcus Hale.

Do you:

**A.)** Choose **The Clean Check** — pay the full salary owed today and owe the player nothing afterward **OR**

**B.)** Choose **The Long Bet** — defer the salary at the agent's interest rate and invest the cash under the club's policy to cover what the club will owe

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:

- **D1 — The debt on the first payment date.** Using Appendix A's amount owed, interest rate and number of years to the first payment, write and evaluate the exponential expression for what the unpaid salary will have grown to on the first payment date.
- **D2 — The repayment schedule, three ways.** (a) Using Appendix D's template, write the recursive formula for the deferred account's balance from one year to the next (interest added, then that year's payment subtracted), fill the table through the last payment, and find the level yearly payment that leaves the balance at exactly zero (a spreadsheet's goal-seek is allowed). (b) Convert the recursion into an explicit formula for the balance after any number of payments, and use it to solve for the same payment algebraically. (c) Write the payments as a sequence, write the sum of their discounted values term by term (at least the first three and the last two terms), and collapse the sum with the geometric-series formula. All three methods must agree with each other and with the payment in Appendix A.
- **D3 — The pool-to-debt ratio across history.** Using Appendix B, compute the value of the invested cash for the club's policy mix after every possible run of consecutive calendar years as long as the wait to the first payment (as many runs as the record allows). Divide each by D1's debt and show the full set of ratios as a box-and-whisker plot with the median and both quartiles labeled. State the share of runs in which the ratio is at least one.
- **D4 — The same record in non-overlapping blocks.** Cut Appendix B into back-to-back runs of that same length, with no year used twice, starting in a year you choose and state. Compute each run's ratio, the mean of those ratios, and how many are at least one. In two sentences, explain why overlapping runs make the evidence look stronger than it is, and how the count changes if you move the starting year.
- **D5 — What actually happened.** Using Appendix B, compute the ratio and the dollar net position for the real run that begins in the signing year named in Appendix A. State in one sentence whether The Long Bet was a bad decision or a bad outcome, and which evidence from D3 and D4 supports your answer.
- **D6 — The shortfall plan.** Choose the interest rate at which the club will fund a shortfall; state it and name a real source for what the club could earn or borrow at. Using D5's net position (or the surplus, if the pool is ahead), compute the yearly gap payment over the repayment years at your rate and at two other rates, using the same logic as D2. State who covers a shortfall and who keeps a surplus, and convert one yearly gap into roster spots using Appendix C's league minimum.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A — The Deal

Referenced in Background and Challenge 3 (D1, D2, D5). The terms of the deferral the agent has offered.

| Term | Value |
|---|---|
| Salary still owed to the released player (USD) | $5,900,000 [MA1] |
| Signing year (the cash is invested on January 1 of this year) | 2000 [MA4] |
| Annual interest rate on the deferred salary | 8% [MA2] |
| Number of equal yearly payments | 25 [MA3] |
| Years from signing to the first payment | 11 [MA4] |
| Yearly payment stated in the contract (USD) | $1,193,248.20 [MA5] |

---

## Appendix B — Historical Annual Returns

Referenced in Background and Challenge 3 (D3, D4, D5). One row per calendar year for as long as the record goes back. Each return is the total return for the year, dividends and interest included.

The table gives, for each calendar year from 1928 through 2025, the total return of the S&P 500 and of the 10-year Treasury bond.

| Year | S&P 500 total return (%) [S2] | 10-year Treasury bond total return (%) [S3] |
|---|---|---|
| 1928 | 43.81 | 0.84 |
| 1929 | -8.30 | 4.20 |
| 1930 | -25.12 | 4.54 |
| 1931 | -43.84 | -2.56 |
| 1932 | -8.64 | 8.79 |
| 1933 | 49.98 | 1.86 |
| 1934 | -1.19 | 7.96 |
| 1935 | 46.74 | 4.47 |
| 1936 | 31.94 | 5.02 |
| 1937 | -35.34 | 1.38 |
| 1938 | 29.28 | 4.21 |
| 1939 | -1.10 | 4.41 |
| 1940 | -10.67 | 5.40 |
| 1941 | -12.77 | -2.02 |
| 1942 | 19.17 | 2.29 |
| 1943 | 25.06 | 2.49 |
| 1944 | 19.03 | 2.58 |
| 1945 | 35.82 | 3.80 |
| 1946 | -8.43 | 3.13 |
| 1947 | 5.20 | 0.92 |
| 1948 | 5.70 | 1.95 |
| 1949 | 18.30 | 4.66 |
| 1950 | 30.81 | 0.43 |
| 1951 | 23.68 | -0.30 |
| 1952 | 18.15 | 2.27 |
| 1953 | -1.21 | 4.14 |
| 1954 | 52.56 | 3.29 |
| 1955 | 32.60 | -1.34 |
| 1956 | 7.44 | -2.26 |
| 1957 | -10.46 | 6.80 |
| 1958 | 43.72 | -2.10 |
| 1959 | 12.06 | -2.65 |
| 1960 | 0.34 | 11.64 |
| 1961 | 26.64 | 2.06 |
| 1962 | -8.81 | 5.69 |
| 1963 | 22.61 | 1.68 |
| 1964 | 16.42 | 3.73 |
| 1965 | 12.40 | 0.72 |
| 1966 | -9.97 | 2.91 |
| 1967 | 23.80 | -1.58 |
| 1968 | 10.81 | 3.27 |
| 1969 | -8.24 | -5.01 |
| 1970 | 3.56 | 16.75 |
| 1971 | 14.22 | 9.79 |
| 1972 | 18.76 | 2.82 |
| 1973 | -14.31 | 3.66 |
| 1974 | -25.90 | 1.99 |
| 1975 | 37.00 | 3.61 |
| 1976 | 23.83 | 15.98 |
| 1977 | -6.98 | 1.29 |
| 1978 | 6.51 | -0.78 |
| 1979 | 18.52 | 0.67 |
| 1980 | 31.74 | -2.99 |
| 1981 | -4.70 | 8.20 |
| 1982 | 20.42 | 32.81 |
| 1983 | 22.34 | 3.20 |
| 1984 | 6.15 | 13.73 |
| 1985 | 31.24 | 25.71 |
| 1986 | 18.49 | 24.28 |
| 1987 | 5.81 | -4.96 |
| 1988 | 16.54 | 8.22 |
| 1989 | 31.48 | 17.69 |
| 1990 | -3.06 | 6.24 |
| 1991 | 30.23 | 15.00 |
| 1992 | 7.49 | 9.36 |
| 1993 | 9.97 | 14.21 |
| 1994 | 1.33 | -8.04 |
| 1995 | 37.20 | 23.48 |
| 1996 | 22.68 | 1.43 |
| 1997 | 33.10 | 9.94 |
| 1998 | 28.34 | 14.92 |
| 1999 | 20.89 | -8.25 |
| 2000 | -9.03 | 16.66 |
| 2001 | -11.85 | 5.57 |
| 2002 | -21.97 | 15.12 |
| 2003 | 28.36 | 0.38 |
| 2004 | 10.74 | 4.49 |
| 2005 | 4.83 | 2.87 |
| 2006 | 15.61 | 1.96 |
| 2007 | 5.48 | 10.21 |
| 2008 | -36.55 | 20.10 |
| 2009 | 25.94 | -11.12 |
| 2010 | 14.82 | 8.46 |
| 2011 | 2.10 | 16.04 |
| 2012 | 15.89 | 2.97 |
| 2013 | 32.15 | -9.10 |
| 2014 | 13.52 | 10.75 |
| 2015 | 1.38 | 1.28 |
| 2016 | 11.77 | 0.69 |
| 2017 | 21.61 | 2.80 |
| 2018 | -4.23 | -0.02 |
| 2019 | 31.21 | 9.64 |
| 2020 | 18.02 | 11.33 |
| 2021 | 28.47 | -4.42 |
| 2022 | -18.04 | -17.83 |
| 2023 | 26.06 | 3.88 |
| 2024 | 24.88 | -1.64 |
| 2025 | 17.72 | 7.80 |

Returns are in percent, rounded to two decimals; each is the total return for that calendar year [S2] [S3].

---

## Appendix C — The Club's Investment Policy and the Roster

Referenced in Background and Challenge 3 (D6). The club's policy, stated as a rule rather than a forecast: the pool is held in the two investments in Appendix B, in the shares below, and restored to those shares every January.

| Item | Value |
|---|---|
| Share of the pool in stocks | 60% [MA6] |
| Share of the pool in 10-year Treasury bonds | 40% [MA6] |
| League minimum salary in the first payment year (USD) | $414,000 [S1] |

---

## Appendix D — Blank Balance Table

Referenced in Background and Challenge 3 (D2). Build the repayment schedule here, one row per year from signing through the last payment.

| Year | Opening balance | Interest added | Payment made | Closing balance |
|---|---|---|---|---|
| (one row for each year of the deferral) | | | | |

---

## Appendix E — Modeling Assumptions

Referenced in Background and Challenge 3 (D4, D6). This case is built so that you must decide a few quantities yourself, state them, and defend them. They are not given.

- **The funding rate (D6).** The yearly rate at which a shortfall is repaid out of the roster budget. State it, give a real source for what the club could earn or borrow at, and test two other rates.
- **The starting year of the blocks (D4).** The first year of your non-overlapping blocks. State it, and show how the count of successful blocks changes if you move it.

**Stated scenario assumptions.**

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case author. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Salary still owed to the released player | $5,900,000 | Chosen to mirror the size of a publicly reported professional-sports salary deferral (named in the facilitator guide); large enough to matter to a club's budget. The club and the player are fictional. | The answer to the dilemma is sensitive to this value. |
| MA2 | Annual interest rate on the deferred salary | 8% | Chosen to mirror the same reported deferral. It is the hurdle The Long Bet must clear. | The answer to the dilemma is sensitive to this value; D6 asks you to test other rates for the shortfall. |
| MA3 | Number of equal yearly payments | 25 | Chosen to mirror the same reported deferral. | The answer is sensitive to this value. |
| MA4 | Signing year, and years from signing to the first payment | Signing year 2000; first payment 11 years later (the case's all-January clock puts it on January 1 of the eleventh year after signing) | The signing year is fixed so that the real market run that begins in the signing year (D5) lies inside the historical record in Appendix B; the 11-year wait mirrors the reported deferral. | The answer is sensitive to the wait. |
| MA5 | Yearly payment stated in the contract | $1,193,248.20 | The level yearly payment the deferral implies at MA1-MA4; it is given so that D2 can check your three methods against it to the cent. | Not independent: it follows from MA1-MA4. |
| MA6 | The club's investment policy: shares in stocks and in 10-year Treasury bonds | 60% stocks, 40% bonds, restored to those shares every January | A common balanced allocation, chosen as a fixed club policy so that the allocation is a stated constraint and not a free choice. | The answer to the dilemma is sensitive to this policy; other mixes can be tested as an extension. |

---

## Appendix F — Sources

Referenced in Background. Every figure in this case is either sourced here or declared as a stated assumption in Appendix E.

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Major-league minimum salary in the first payment year (2011) | $414,000 | Baseball Prospectus (Maury Brown), citing the MLB Players Association annual report — Bizball: Inside the 2012-16 MLB CBA: Minimum Salaries, the Luxury Tax ([link](https://www.baseballprospectus.com/news/article/17225/bizball-inside-the-2012-16-mlb-cba-minimum-salaries-the-luxury-tax)) | 2011 season | MEDIUM |
| S2 | Annual total return of the S&P 500 including dividends, by calendar year | 98 annual values, 1928-2025 (Appendix B) | Aswath Damodaran, NYU Stern School of Business — Historical Returns on Stocks, Bonds and Bills (histretSP.xls) ([link](https://www.stern.nyu.edu/~adamodar/pc/datasets/histretSP.xls)) | through 2025 (page updated 2026-01-05) | HIGH |
| S3 | Annual total return of the 10-year U.S. Treasury bond, by calendar year | 98 annual values, 1928-2025 (Appendix B) | Aswath Damodaran, NYU Stern School of Business — Historical Returns on Stocks, Bonds and Bills (histretSP.xls) ([link](https://www.stern.nyu.edu/~adamodar/pc/datasets/histretSP.xls)) | through 2025 (page updated 2026-01-05) | HIGH |

The Gulls and Marcus Hale are fictional. The terms of the deferral are stated scenario assumptions (Appendix E). The two return series are real historical data. Two cautions on them: before 1957 the stock series is spliced from other large-company indices, and the bond series is a return Damodaran computes from Treasury yields for a bond of constant ten-year maturity, not the return of any bond you could have bought.

---

## Appendix G — "How To…" Math Questions To Research

Referenced in Challenge 1. The questions below are the skills this case asks you to use.

**Vocabulary terms**

- Recursive Formula
- Sequence
- Series
- Quartiles
- Box And Whisker Plot
- Median

**"How to…" questions**

- How to evaluate an exponential expression
- How to find the percent of a number
- How to write a recursive formula for a sequence
- How to convert a recursive formula to an explicit formula
- How to create a box and whisker plot given a set of data
- How to find the mean of a set of data
