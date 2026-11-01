Case Study: The Trophy and the Table
MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

The trophy is still standing in the lobby when the board member arrives, and the glass case around it is covered in the fingerprints of people who wanted to touch it. It is the first major trophy the club has won in a very long time. Nobody has had the heart to wipe the glass.

Upstairs, the other piece of paper is already on the boardroom table. It is the final league table, printed on plain office paper, and the club's name sits far lower on it than anyone in the building is comfortable with. Somebody has circled a row in pencil. Somebody else has set a coffee cup on one corner to keep the page flat.

The board member takes the chair by the window and listens to the room divide, the way rooms do. One director says a trophy is the whole reason a football club exists. Another taps the table and says the table never lies. A third says that nobody present can actually say what the table is telling them, and asks the club's analyst to put the model on the screen.

The analyst's slide is a cloud of dots with a straight line running through it. Almost every dot hugs the line. One dot floats far below it, all by itself, and it is the club's own.

The chair slides a ballot sheet across the polished wood. It has two boxes and a single pen beside it. The board member picks up the pen.

---

## Background

This case puts you in a boardroom at a real club at a real moment, with one deliberate change: the decision point is **constructed**. The club is Tottenham Hotspur, a member of England's Premier League, the top division of English club football. The room is the club's board in the last days of May 2025. Which choice the club actually made is not part of this case; your guide will raise it at the close. The case uses only public record, does not guess at anyone's motives, and is **not a verdict on any person**: you are judging what a statistical model can and cannot tell a board, not whether a manager is good or bad.

The manager is Ange Postecoglou. In the 2024/25 season his team finished 17th of 20 in the Premier League, one place above the three clubs that are sent down to the second division (SEE APPENDIX A). Days earlier, the same team won the Europa League, a major European club trophy (SEE APPENDIX A, which explains the competition and the other football terms used here for readers who have never followed the sport). The board decides by secret ballot: each director marks one of two boxes, the majority wins, and you hold one vote. A board member must decide whether the league finish or the trophy should settle the manager's future.

The board's analyst has built a simple model on the final league table (SEE APPENDIX B): a straight line that predicts a club's points from its **goal difference**, the goals it scored minus the goals it conceded. The analyst's method is explained in Appendix F. Free public data for anyone who wants to go further is listed in Appendix C.

Your two options have memorable labels. **Keep the Winner** means the manager who won the Europa League trophy stays, and the 17th-place finish is not treated as a reason to change. **Change After 17th** means the manager is replaced after the 17th-place league finish, betting that the reset cost of a new manager is smaller than the shortfall it avoids, because the model says the club's points were far below what its goals should have earned.

To compare them, the board uses one number, **expected Premier League points in the 2025/26 season** under each option. Both options start from the same point: the club's **predicted points** from the model you build in Challenge 3, not the 38 actually earned, because the question is what happens next season. A club's **shortfall** in this case always means one thing: the positive number of points by which its actual total fell below the model's predicted total. Under Keep the Winner, the board forecasts the club's next-season shortfall from past data: across ten seasons of league tables, a club that finished r points below its season's line finished about 0.11 × r points below its line the following season (SEE APPENDIX E, where you can read this off a chart). Under Change After 17th, the case scores the club in the best light for a new manager: it assumes the new manager removes the forecast shortfall entirely (the club lands on its line), because the model cannot tell you how much of the shortfall was ever the manager's doing, and D5 asks you to say what that assumption costs. In exchange, the club pays a **reset cost**: the points a new manager costs while the squad adjusts to new tactics (SEE APPENDIX D for a concrete picture of how that happens). No public source gives that cost, so the case does not pick it for you: you choose and defend your own range for it (SEE APPENDIX D). Everything else is sourced in (SEE APPENDIX G). The vocabulary and "how to…" skills this case asks you to research are listed in Appendix H.

Injury reports from fan sites are not used as fact anywhere in this case. The league's own report on the club's injuries is cited in Appendix A [S4].

---

## Dilemma

You are a member of the club's board.

Do you:

**A.)** Keep the Winner — keep the manager who won the Europa League trophy; the 17th-place finish is not treated as a reason to change **OR**

**B.)** Change After 17th — replace the manager after the 17th-place league finish, betting that the reset cost is smaller than the shortfall it avoids

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:

- **D1 — A scatter plot and a line of best fit.** Using Appendix B, make a scatter plot of all 20 clubs (goal difference on the horizontal axis, points on the vertical axis). Fit a line of best fit (a spreadsheet or Desmos regression is allowed; show it in your appendix of work), draw it on your plot, and write its equation. Then (i) describe the correlation in direction and strength, (ii) say in one sentence what the slope means in points per goal of goal difference, and (iii) find the mean goal difference and the mean points of the 20 clubs, and say what you notice about where your line passes.
- **D2 — A residual table.** For every club, use your line to predict its points, and compute its residual (actual points minus predicted points). Report the club's residual, the next-largest shortfall among the other 19 clubs, and the largest surplus. Show that the 20 residuals average to about zero. Using the method in Appendix F, compute the residual spread of the 20 clubs, describe it with the term Variability, and state how many residual spreads below the line the club sits.
- **D3 — An outlier check.** Refit the line with the club's own row removed, so that it is fitted on the other 19 clubs only. Report the new equation, the club's residual against this new line, the residual spread of the other 19 clubs, and how many residual spreads below the new line the club sits. In two or three sentences, using the term Outlier, say whether the club's shortfall is an artifact of the club pulling the line toward itself.
- **D4 — A break-even comparison.** Using your D3 line as the model of record, compute the club's predicted points and its shortfall. Forecast the club's next-season shortfall under Keep the Winner (slope 0.11 from Appendix E times this season's shortfall) and its expected points. Then find the **break-even reset cost**: the reset cost at which Change After 17th and Keep the Winner tie. Change After 17th beats Keep the Winner only if the reset cost is smaller than that. Choose and defend your own range for the reset cost (Appendix D suggests 0 to 4 points; you may go beyond it), say whether it is plausible that the reset cost is smaller than the break-even, and give the winner and the percent margin at the low, middle and high ends of your range.
- **D5 — What the model leaves out (graded).** Write a short section on the limits of the model, graded on three things. (1) Name at least four distinct limits, each tied to a specific number or fact in this case, and use the terms Sample Size and Random. Your four must include that GD and points are mechanically linked (the line describes a pattern; it does not show a cause), and that a residual cannot separate luck from management. (2) For each limit, say whether it pushes the board toward A or toward B. (3) Name the single limit that would most change your recommendation, and say which free public data from Appendix C you would use to test it.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A — The Public Record

Referenced in Background and Challenge 3 (D5). Everything in this appendix is public record, cited to a named source. Nothing here is a claim about anyone's motives.

**The season.** In 2024/25 the club finished 17th in the Premier League with 38 points, from 11 wins, 5 draws and 22 losses, scoring 64 goals and conceding 65, for a goal difference of −1 [S2]. That was the club's lowest top-flight finish in 48 years [S2]. The three clubs that finished below it, Leicester City, Ipswich Town and Southampton, were relegated [S1].

**A few football terms, for readers new to it.** The *manager* is the head coach: the person who picks the team, sets the tactics and runs training, and who is hired and can be dismissed by the club's *board*, the group of directors that governs the club. In the league a win earns 3 points, a draw 1 and a loss 0 (check it against any row of Appendix B: 11 wins and 5 draws is 38 points). A *centre-back* is a central defender, one of the players whose main job is protecting the goal, and a *midfielder* is a player who works between the defenders and the attackers. **Relegation:** at the end of each season the bottom three of the league's 20 clubs drop to the second division, and three clubs from that division move up to replace them. Finishing 17th means finishing one place above that line [S8].

**The Europa League, in one paragraph for readers who have never followed it.** The UEFA Europa League is the second-tier European club competition, ranking below the Champions League, the top European club competition, which clubs are keen to qualify for. Clubs from many countries qualify through their domestic league finishes, and its games are played in midweek during the same months as the domestic league season, so a club plays both at once. Think of it as a separate tournament running alongside the regular season: winning it does not add a single point to a club's league record. Its winner earns a place in the next season's Champions League [S3]. The club beat Manchester United 1–0 in the Europa League final on 21 May 2025 at the San Mamés stadium in Bilbao, Spain [S2].

**The league's own report on injuries.** On 29 December 2024 the Premier League's website reported that all four of the club's senior centre-backs, the central defenders, were injured at the same time, and that a midfielder and two teenagers had been used in defence as a result [S4]. With the usual central defenders unavailable, other players had to cover their jobs. This is a documented fact about one period of the season. It does not say how many points the injuries cost, and this case does not use injury counts from fan or hobby sites as fact. How much a club values a European trophy against a league finish is for the board to argue; this case gives no figure for it.

---

## Appendix B — Final 2024/25 Premier League Table

Referenced in Background and Challenge 3 (D1, D2, D3). **Official final table**, as transcribed on the Wikipedia page for the season [S1]; no figure on this page is derived or computed by the case author. W, D, L = wins, draws, losses; GF, GA = goals for, goals against; GD = goal difference (GF − GA); Pts = league points. No club had points deducted. Some columns are not needed for every challenge.

| Pos | Club | W | D | L | GF | GA | GD | Pts |
|---|---|---|---|---|---|---|---|---|
| 1 | Liverpool | 25 | 9 | 4 | 86 | 41 | +45 | 84 |
| 2 | Arsenal | 20 | 14 | 4 | 69 | 34 | +35 | 74 |
| 3 | Manchester City | 21 | 8 | 9 | 72 | 44 | +28 | 71 |
| 4 | Chelsea | 20 | 9 | 9 | 64 | 43 | +21 | 69 |
| 5 | Newcastle United | 20 | 6 | 12 | 68 | 47 | +21 | 66 |
| 6 | Aston Villa | 19 | 9 | 10 | 58 | 51 | +7 | 66 |
| 7 | Nottingham Forest | 19 | 8 | 11 | 58 | 46 | +12 | 65 |
| 8 | Brighton & Hove Albion | 16 | 13 | 9 | 66 | 59 | +7 | 61 |
| 9 | AFC Bournemouth | 15 | 11 | 12 | 58 | 46 | +12 | 56 |
| 10 | Brentford | 16 | 8 | 14 | 66 | 57 | +9 | 56 |
| 11 | Fulham | 15 | 9 | 14 | 54 | 54 | 0 | 54 |
| 12 | Crystal Palace | 13 | 14 | 11 | 51 | 51 | 0 | 53 |
| 13 | Everton | 11 | 15 | 12 | 42 | 44 | −2 | 48 |
| 14 | West Ham United | 11 | 10 | 17 | 46 | 62 | −16 | 43 |
| 15 | Manchester United | 11 | 9 | 18 | 44 | 54 | −10 | 42 |
| 16 | Wolverhampton Wanderers | 12 | 6 | 20 | 54 | 69 | −15 | 42 |
| 17 | **Tottenham Hotspur** | 11 | 5 | 22 | 64 | 65 | −1 | 38 |
| 18 | Leicester City | 6 | 7 | 25 | 33 | 80 | −47 | 25 |
| 19 | Ipswich Town | 4 | 10 | 24 | 36 | 82 | −46 | 22 |
| 20 | Southampton | 2 | 6 | 30 | 26 | 86 | −60 | 12 |

---

## Appendix C — Where to Get More Data (Links Only)

Referenced in Background and Challenge 3 (D5). This packet does **not** include any file from these sites, and you should not pass files from them to anyone else. Download what you want yourself, as an individual, and read each site's own terms first.

- **Football-Data.co.uk** publishes free match-by-match results for every Premier League season back to 1993/94. Its data page states the data is for private individuals and not for commercial use or use by automated bots, scrapers or AI training, so you download the files yourself, by hand, for your own use [S5]. Season files for the Premier League are listed on its England page: [football-data.co.uk/englandm.php](https://www.football-data.co.uk/englandm.php).
- **Optional extension only, not required for any deliverable:** StatsBomb publishes free open event data and asks that anything you publish from it name StatsBomb as the source and use its logo [S6]. Understat shows expected-goals tables and states no terms of use on the page [S7]. Check each site's terms yourself before you use either.

---

## Appendix D — Modeling Assumptions

Referenced in Background and Challenge 3 (D4). MA1 is a figure the case author **derived** from public tables (Appendix E). MA2, MA3 and MA4 are **not sourced**: they are stated scenario assumptions chosen by the case author, because no public study measures them for one club in one season. A Hero may challenge any of them in discussion; that is a legitimate move, and the answer is sensitive to the first two.

| # | Assumption | Value used | Basis |
|---|---|---|---|
| MA1 | Forecast of next season's shortfall for a club whose goal difference stays the same: **0.11 × this season's shortfall** (slope 0.11; range about 0 to 0.27) | 0.11 | **Derived, not invented:** a fitted slope read off ten Premier League seasons of final tables (Appendix E). Each season has only 20 clubs, so the slope is uncertain; the range shows how much. It is an average over typical clubs and says nothing about why any one club finished where it did. |
| MA2 | The reset cost, in league points, of replacing the manager for one season: the points lost while players learn new tactics and routines (picture below) | **You choose.** The case asks you to consider the range 0 to 4 points (no cost at all, up to a little more than one lost match) and to defend your own range inside or outside it | **Unsourced scenario assumption.** No public figure applies to this decision, so the case does not fix one; Challenge 3 (D4) asks you to find the break-even and judge whether it is plausible. |
| MA3 | The club's goal difference next season, under either option | The same as in 2024/25 | Both options start from one baseline so that the comparison isolates the two choices. It leaves out transfers, injuries and the extra midweek matches that Champions League football brings. |
| MA3b | How the options are scored | Both options start from the model's predicted points for the club (not from the club's actual points). Expected points under Keep the Winner = predicted points − (MA1 × the size of the shortfall, taken as a positive number of points). Expected points under Change After 17th = predicted points − your chosen reset cost (MA2). The percent margin, for any reset cost you test, is the difference between the two, divided by the smaller of them | Stated so that every student scores the options the same way. |
| MA4 | Residuals are talked about in "residual spreads" (Appendix F), as if the other clubs' misses were ordinary, bell-shaped variation | Stated as a convenience | With only 20 clubs the bell shape cannot be checked; D5 asks you to say what that costs. |

**What a reset cost looks like on the pitch.** A new manager brings new tactics, new training routines and sometimes new signings, and players need weeks to learn them. In that time a few matches that the old set-up would have won may end as draws, and a few that would have been draws may end as losses. Because a win is worth 3 points, a draw 1 and a loss 0, **one win that becomes a draw costs 2 points, and one draw that becomes a loss costs 1 point.** So 1 point is one draw turning into a loss, 2 points is one win turning into a draw, and 4 points is a couple of matches slipping that way. The cost could also be zero, or even negative if a fresh voice lifts the squad and wins back points; you may argue for a range that goes below 0. Whether a new manager would really cost the club that much, or nothing, or even help, is exactly what no source can tell you. A board facing a number like this would not pretend to know it: it would test a range, ask where the answer flips, and judge whether the flip point is believable. That is what D4 asks you to do.

**The two scoring rules, in a picture.** Both options start from one line: the model's predicted points. Keep the Winner subtracts the forecast next-season shortfall (MA1 × this season's shortfall). Change After 17th subtracts only the reset cost you chose (MA2), because it assumes a new manager removes the forecast shortfall; that is the best case for replacing him, not a fact. Whichever subtracts less leaves the club with more expected points, so Change After 17th wins only if the reset cost is smaller than the forecast next-season shortfall. The picture is drawn without a scale and shows no figure from this case.

<svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Both options start from one horizontal line, the model's predicted points. Option A, Keep the Winner, drops down by the forecast next-season shortfall, MA1 times this season's shortfall. Option B, Change After 17th, drops down by the reset cost you choose, MA2. Whichever drop is smaller leaves more expected points. Drawn without a scale, no case figures." style="max-width:560px;width:100%;border:1px solid #999;background:#fafafa;font-family:sans-serif">
  <line x1="20" y1="40" x2="360" y2="40" stroke="#333" stroke-width="2" stroke-dasharray="6 4"/>
  <text x="20" y="30" font-size="12" fill="#333">Both options start here: the model's predicted points</text>
  <rect x="70" y="40" width="60" height="50" fill="#b03030"/>
  <text x="100" y="108" font-size="11" text-anchor="middle" fill="#333">Keep the Winner</text>
  <text x="100" y="122" font-size="10" text-anchor="middle" fill="#333">minus forecast next-season</text>
  <text x="100" y="134" font-size="10" text-anchor="middle" fill="#333">shortfall (MA1 x shortfall)</text>
  <rect x="250" y="40" width="60" height="30" fill="#1a3a5c"/>
  <text x="280" y="108" font-size="11" text-anchor="middle" fill="#333">Change After 17th</text>
  <text x="280" y="122" font-size="10" text-anchor="middle" fill="#333">minus the reset cost</text>
  <text x="280" y="134" font-size="10" text-anchor="middle" fill="#333">you choose (MA2)</text>
  <text x="190" y="175" font-size="10" text-anchor="middle" fill="#555">Shorter bar = more expected points. Bar lengths here are invented and not to scale.</text>
</svg>

---

## Appendix E — What a Miss Forecasts for Next Season (Derived)

Referenced in Background and Challenge 3 (D4, D5). **Every figure on this page is DERIVED by the case author**, not published by any source. Method: for each of ten seasons (2015/16 to 2024/25), the case author took the 20-club final table from its Wikipedia season page ([S14], [S15], [S16], [S17], [S18], [S19], [S20], [S21], [S22], [S23]), used each club's points from its results (3 per win, 1 per draw, so the two clubs' 2023/24 points deductions (penalties for breaking the league's financial rules) are left out), fitted that season's own line of points on goal difference, and computed every club's residual. Then, for every club that played in two consecutive seasons (153 club-pairs, 17 per season pair), the case author fitted a line of **next season's residual on this season's residual**. The slope of that line is the forecast: a club that missed its line by r points this season missed by about slope × r points the next season. **Read it off the chart:** take one club, say a club that finished 11 points below its season's line. Put a dot for it on the picture below, with that miss across and the same club's miss the following season going up. Do that for every club-pair. If a club's next-season miss simply copied this season's, the dots would climb along a line of slope 1. If this season's miss told you nothing about next season's, the dots would form a shapeless cloud with a flat line. The red line is the fitted slope: nearly flat.

| Season pair | Club-pairs | Slope: next season's miss per point of this season's miss |
|---|---|---|
| 2015/16 to 2016/17 | 17 | 0.13 |
| 2016/17 to 2017/18 | 17 | 0.14 |
| 2017/18 to 2018/19 | 17 | 0.22 |
| 2018/19 to 2019/20 | 17 | −0.04 |
| 2019/20 to 2020/21 | 17 | 0.09 |
| 2020/21 to 2021/22 | 17 | −0.13 |
| 2021/22 to 2022/23 | 17 | 0.29 |
| 2022/23 to 2023/24 | 17 | 0.38 |
| 2023/24 to 2024/25 | 17 | −0.15 |
| **All nine pairs pooled** | **153** | **0.11** |

**Reading it.** The pooled slope is about 0.11 (one ninth), with a 95% range of about −0.05 to 0.27 (a negative slope would mean misses tend to flip sign, which is hard to believe for a forecast, so read the range as roughly 0 to 0.27). The individual season pairs swing from −0.15 to 0.38, which is what small samples of 17 clubs look like. **Caveats the case author wants you to weigh:** (1) each season has only 20 clubs, so the estimate is noisy; (2) it averages over typical clubs, most of whose misses were under 8 points; (3) it forecasts next season's miss whatever the reason, and does not say whether a manager caused any of it; (4) the points-from-results choice and the one-season lag are the case author's choices. You can check one season pair yourself from the ten Wikipedia season pages in Appendix G.

<svg viewBox="0 0 380 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Scatter plot of 153 club-pairs from ten Premier League seasons. Horizontal axis: a club's miss from its season line one season. Vertical axis: the same club's miss the next season. The dots form a shapeless cloud and the fitted line is almost flat, rising only slightly. Derived by the case author from Wikipedia season tables." style="max-width:560px;width:100%;border:1px solid #999;background:#fafafa;font-family:sans-serif">
<line x1="60" y1="200" x2="340" y2="200" stroke="#333"/><line x1="60" y1="20" x2="60" y2="200" stroke="#333"/>
<line x1="200.0" y1="20" x2="200.0" y2="200" stroke="#ccc"/><line x1="60" y1="110.0" x2="340" y2="110.0" stroke="#ccc"/>
<circle cx="204.4" cy="101.3" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="240.6" cy="106.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="151.4" cy="67.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="183.8" cy="130.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="136.6" cy="127.3" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="274.9" cy="106.7" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="199.1" cy="106.3" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="155.0" cy="112.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="246.0" cy="106.9" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="197.0" cy="123.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="273.9" cy="106.7" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="168.9" cy="131.1" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="216.2" cy="88.3" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="167.2" cy="134.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="198.7" cy="83.4" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="203.9" cy="125.7" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="211.0" cy="94.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="213.5" cy="127.5" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="206.2" cy="100.3" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="175.7" cy="88.7" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="266.9" cy="91.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="168.0" cy="120.9" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="173.1" cy="79.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="205.2" cy="124.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="205.8" cy="139.1" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="195.9" cy="112.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="204.8" cy="84.7" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="178.8" cy="134.9" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="205.2" cy="103.7" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="233.7" cy="120.9" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="161.8" cy="100.4" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="241.4" cy="103.4" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="175.6" cy="142.4" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="224.9" cy="97.7" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="172.8" cy="96.5" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="201.6" cy="117.7" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="215.2" cy="106.9" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="233.1" cy="102.5" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="228.7" cy="92.5" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="183.1" cy="127.8" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="248.2" cy="135.8" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="228.8" cy="125.3" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="177.2" cy="129.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="154.7" cy="107.4" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="196.9" cy="119.8" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="239.3" cy="79.2" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="172.4" cy="135.8" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="161.2" cy="118.9" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="215.0" cy="112.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="210.3" cy="104.1" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="219.1" cy="107.3" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="221.0" cy="116.5" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="188.0" cy="124.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="204.8" cy="129.9" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="211.7" cy="77.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="227.3" cy="83.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="172.3" cy="99.4" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="159.8" cy="89.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="170.4" cy="142.9" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="204.1" cy="21.7" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="184.7" cy="173.1" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="247.9" cy="133.8" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="159.8" cy="90.4" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="186.1" cy="82.2" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="196.0" cy="119.7" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="209.2" cy="119.9" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="204.2" cy="141.9" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="225.4" cy="109.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="189.9" cy="121.9" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="182.9" cy="130.4" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="178.2" cy="155.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="250.4" cy="108.5" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="241.0" cy="109.8" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="216.5" cy="69.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="232.6" cy="71.8" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="148.8" cy="101.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="337.4" cy="112.9" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="101.9" cy="107.5" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="163.0" cy="95.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="230.5" cy="96.4" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="214.0" cy="122.8" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="243.3" cy="89.7" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="185.0" cy="141.5" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="150.3" cy="95.8" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="200.6" cy="96.4" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="181.5" cy="58.4" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="168.3" cy="146.5" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="130.0" cy="112.8" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="202.3" cy="149.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="200.4" cy="124.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="262.8" cy="148.4" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="259.4" cy="114.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="208.9" cy="76.5" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="214.1" cy="122.7" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="195.4" cy="100.9" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="203.9" cy="110.9" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="222.3" cy="79.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="221.1" cy="74.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="231.6" cy="105.9" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="151.0" cy="97.1" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="222.1" cy="119.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="221.1" cy="103.4" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="280.3" cy="92.3" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="143.2" cy="80.7" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="195.7" cy="124.4" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="181.1" cy="116.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="178.2" cy="126.9" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="140.3" cy="121.3" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="192.8" cy="122.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="252.1" cy="126.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="180.2" cy="155.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="214.2" cy="128.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="198.7" cy="120.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="247.2" cy="37.2" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="256.0" cy="130.2" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="206.4" cy="135.1" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="220.0" cy="93.3" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="186.0" cy="135.3" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="210.3" cy="80.3" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="227.5" cy="121.5" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="245.6" cy="77.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="177.6" cy="113.3" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="267.0" cy="92.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="189.8" cy="157.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="173.7" cy="101.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="182.4" cy="128.5" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="180.5" cy="99.5" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="183.3" cy="122.4" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="172.0" cy="102.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="183.5" cy="110.2" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="313.3" cy="66.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="168.6" cy="149.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="236.3" cy="142.8" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="225.9" cy="81.3" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="160.6" cy="66.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="246.1" cy="96.9" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="182.2" cy="119.4" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="251.4" cy="59.5" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="194.8" cy="87.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="227.1" cy="134.5" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="126.8" cy="123.2" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="213.0" cy="95.1" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="171.3" cy="106.3" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="216.3" cy="127.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="180.7" cy="100.7" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="212.4" cy="100.7" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="199.7" cy="110.1" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="267.5" cy="130.7" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="138.3" cy="111.9" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="149.0" cy="83.8" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="244.7" cy="187.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="267.5" cy="102.6" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<circle cx="220.4" cy="112.0" r="2.6" fill="#1a3a5c" fill-opacity="0.55"/>
<line x1="60.0" y1="120.0" x2="340.0" y2="100.3" stroke="#b03030" stroke-width="2"/>
<text x="200" y="228" font-size="11" text-anchor="middle" fill="#333">a club's miss this season (points; left = below its line)</text>
<text x="14" y="110" font-size="11" text-anchor="middle" fill="#333" transform="rotate(-90 14 110)">same club's miss next season</text>
<text x="200" y="244" font-size="10" text-anchor="middle" fill="#555">153 club-pairs, 2015/16 to 2024/25. Red line = the fitted slope. Derived by the case author.</text>
</svg>


---

## Appendix F — Method Notes

Referenced in Background and Challenge 3 (D2, D3, D4).

**Residual.** For a club, residual = actual points − predicted points, where predicted points come from your line. A negative residual means the club finished with fewer points than the line says its goal difference should have earned.

**Residual spread.** Square each club's residual, add up the squares, divide by (the number of clubs − 2), and take the square root. The result is in points. A club's miss, divided by this spread, tells you how many residual spreads it sits from the line. When you refit with a club left out in D3, the number of clubs is 19, and the same recipe divides by 17.

**What a residual is not.** A residual is a distance from a line fitted to a single season of 20 clubs. It is not a measurement of anyone's skill.

**An invented example, to show the shape of the idea.** The picture below uses made-up dots, with no numbers, from a different subject. It is not this case's data and shows nothing about any club. Dots above the line have positive residuals, dots below have negative residuals, and each short vertical segment is one residual.

<svg viewBox="0 0 320 210" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Illustrative scatter plot with a line of best fit and short vertical segments from each dot to the line, showing residuals. Invented example, not case data." style="max-width:520px;width:100%;border:1px solid #999;background:#fafafa;font-family:sans-serif">
  <line x1="40" y1="170" x2="300" y2="170" stroke="#333" stroke-width="1.5"/>
  <line x1="40" y1="170" x2="40" y2="15" stroke="#333" stroke-width="1.5"/>
  <text x="170" y="196" font-size="11" text-anchor="middle" fill="#333">hours practiced (invented)</text>
  <text x="14" y="95" font-size="11" text-anchor="middle" fill="#333" transform="rotate(-90 14 95)">test score (invented)</text>
  <line x1="55" y1="150" x2="290" y2="40" stroke="#1a3a5c" stroke-width="2"/>
  <line x1="85" y1="130" x2="85" y2="112" stroke="#b03030" stroke-width="2"/>
  <line x1="130" y1="108" x2="130" y2="127" stroke="#b03030" stroke-width="2"/>
  <line x1="180" y1="85" x2="180" y2="70" stroke="#b03030" stroke-width="2"/>
  <line x1="225" y1="64" x2="225" y2="82" stroke="#b03030" stroke-width="2"/>
  <line x1="270" y1="43" x2="270" y2="30" stroke="#b03030" stroke-width="2"/>
  <circle cx="85" cy="112" r="5" fill="#1a3a5c"/>
  <circle cx="130" cy="127" r="5" fill="#1a3a5c"/>
  <circle cx="180" cy="70" r="5" fill="#1a3a5c"/>
  <circle cx="225" cy="82" r="5" fill="#1a3a5c"/>
  <circle cx="270" cy="30" r="5" fill="#1a3a5c"/>
  <text x="215" y="150" font-size="10" fill="#b03030">red segment = one residual</text>
  <text x="95" y="60" font-size="10" fill="#1a3a5c">line of best fit</text>
</svg>

---

## Appendix G — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Final 2024/25 Premier League table (positions, W/D/L, GF/GA, GD, Pts); bottom three relegated; no deductions | Appendix B | Wikipedia — [2024–25 Premier League](https://en.wikipedia.org/wiki/2024%E2%80%9325_Premier_League) (transcription of the official table) | accessed 2026-10-03 | MEDIUM |
| S2 | The club's 2024/25 record, 17th place, lowest finish in 48 years; Europa League final 21 May 2025, San Mamés, Bilbao, 1–0 vs Manchester United | as stated | Wikipedia — [2024–25 Tottenham Hotspur F.C. season](https://en.wikipedia.org/wiki/2024%E2%80%9325_Tottenham_Hotspur_F.C._season) | accessed 2026-10-03 | MEDIUM |
| S3 | The Europa League's standing and that its winner qualifies for the next Champions League | as stated | Wikipedia — [UEFA Europa League](https://en.wikipedia.org/wiki/UEFA_Europa_League) | accessed 2026-10-03 | MEDIUM |
| S4 | All four senior centre-backs injured at once; midfielder and teenagers used in defence | 29 December 2024 | Premier League — [Spurs face injury crisis with all four senior centre-backs injured](https://www.premierleague.com/en/news/4208927) | 2024-12-29 | HIGH |
| S5 | Football-Data.co.uk free data is for private individuals, not commercial, bot, scraper or AI-training use | as stated | Football-Data.co.uk — [Data page](https://www.football-data.co.uk/data.php) | accessed 2026-10-03 | HIGH |
| S6 | StatsBomb open data requires crediting StatsBomb and using its logo on published work | as stated | StatsBomb — [open-data repository README](https://github.com/statsbomb/open-data) | accessed 2026-10-03 | MEDIUM |
| S7 | Understat publishes Premier League expected-goals tables and states no terms of use on the page | as stated | Understat — [EPL page](https://understat.com/league/EPL) | accessed 2026-10-03 | MEDIUM |
| S8 | Promotion and relegation: how clubs move between divisions | as stated | Wikipedia — [Promotion and relegation](https://en.wikipedia.org/wiki/Promotion_and_relegation) | accessed 2026-10-03 | MEDIUM |
| S14 | Final league table for the 2015–16 Premier League season (W/D/L, goals for and against), used to derive Appendix E | as stated | Wikipedia — [2015–16 Premier League](https://en.wikipedia.org/wiki/2015%E2%80%9316_Premier_League) (text available under CC BY-SA) | accessed 2026-10-03 | MEDIUM |
| S15 | Final league table for the 2016–17 Premier League season (W/D/L, goals for and against), used to derive Appendix E | as stated | Wikipedia — [2016–17 Premier League](https://en.wikipedia.org/wiki/2016%E2%80%9317_Premier_League) (text available under CC BY-SA) | accessed 2026-10-03 | MEDIUM |
| S16 | Final league table for the 2017–18 Premier League season (W/D/L, goals for and against), used to derive Appendix E | as stated | Wikipedia — [2017–18 Premier League](https://en.wikipedia.org/wiki/2017%E2%80%9318_Premier_League) (text available under CC BY-SA) | accessed 2026-10-03 | MEDIUM |
| S17 | Final league table for the 2018–19 Premier League season (W/D/L, goals for and against), used to derive Appendix E | as stated | Wikipedia — [2018–19 Premier League](https://en.wikipedia.org/wiki/2018%E2%80%9319_Premier_League) (text available under CC BY-SA) | accessed 2026-10-03 | MEDIUM |
| S18 | Final league table for the 2019–20 Premier League season (W/D/L, goals for and against), used to derive Appendix E | as stated | Wikipedia — [2019–20 Premier League](https://en.wikipedia.org/wiki/2019%E2%80%9320_Premier_League) (text available under CC BY-SA) | accessed 2026-10-03 | MEDIUM |
| S19 | Final league table for the 2020–21 Premier League season (W/D/L, goals for and against), used to derive Appendix E | as stated | Wikipedia — [2020–21 Premier League](https://en.wikipedia.org/wiki/2020%E2%80%9321_Premier_League) (text available under CC BY-SA) | accessed 2026-10-03 | MEDIUM |
| S20 | Final league table for the 2021–22 Premier League season (W/D/L, goals for and against), used to derive Appendix E | as stated | Wikipedia — [2021–22 Premier League](https://en.wikipedia.org/wiki/2021%E2%80%9322_Premier_League) (text available under CC BY-SA) | accessed 2026-10-03 | MEDIUM |
| S21 | Final league table for the 2022–23 Premier League season (W/D/L, goals for and against), used to derive Appendix E | as stated | Wikipedia — [2022–23 Premier League](https://en.wikipedia.org/wiki/2022%E2%80%9323_Premier_League) (text available under CC BY-SA) | accessed 2026-10-03 | MEDIUM |
| S22 | Final league table for the 2023–24 Premier League season (W/D/L, goals for and against), used to derive Appendix E | as stated | Wikipedia — [2023–24 Premier League](https://en.wikipedia.org/wiki/2023%E2%80%9324_Premier_League) (text available under CC BY-SA) | accessed 2026-10-03 | MEDIUM |
| S23 | Final league table for the 2024–25 Premier League season (W/D/L, goals for and against), used to derive Appendix E | as stated | Wikipedia — [2024–25 Premier League](https://en.wikipedia.org/wiki/2024%E2%80%9325_Premier_League) (text available under CC BY-SA) | accessed 2026-10-03 | MEDIUM |

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->

---

## Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Scatter Plot
- Correlation
- Line Of Best Fit
- Linear
- Slope
- Mean
- Outlier
- Variability
- Sample Size
- Random

**"How to…" questions**

- How to create a scatter plot given a set of data
- How to identify correlation given a scatter plot or set of data
- How to draw a line of best fit given a set of data
- How to write a linear equation given a set of data
- How to identify the slope of a line given a set of data, or a graph of a line of a set of data, or its linear equation
- How to find the mean of a set of data
- How to evaluate a variable expression (Substitution Property)
- How to find the percent of a number
- How to solve a one-step equation
