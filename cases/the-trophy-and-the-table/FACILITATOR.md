# Guide Notes: The Trophy and the Table

MS/HS | Guide Notes | Adventure | 2026-27
**Tier:** T3 (MS-stretch / HS-entry) · **Primary metric:** expected 2025/26 Premier League points · **Margin:** 0.82% (fragile — see the sensitivity note before Lessons Learned)

---

## Teacher note (required — read before the room fills)

**Students are judging a model, not a person.** This case involves a living manager and a real club's
real decision. It is not a verdict on the manager, and it must not become one. The case uses public
record only, quotes no one, and speculates on no one's motives; hold the room to the same rule. If a
Hero starts arguing about what a real person "really" wanted or deserved, redirect: *"What can the
line tell us, and what can it not tell us?"* The real decision is withheld from the student
document on purpose and is raised only at the Close.

Sports-fan heat is a feature here, not a risk, as long as the question stays on the evidence.

---

## Intro

Heroes, you are on a board that has two pieces of evidence it cannot weigh against each other: a
trophy and a league table. A line through the whole league says one thing about this club. The
trophy says another. I do not have the answer; the numbers narrow the question, they do not close it.

## Launch

Show the final 2024/25 table (Appendix B) on screen and ask only: *"Where is this club? Does that
match what you would expect from its goal difference?"* Then show the trophy photo or a one-line
headline of the Europa League final. Let the room feel the clash before any arithmetic.

> **Hero name — Keep the Winner, or Change After 17th? Commit out loud.**

---

## Anchor 1 — Take a stand and vote

Keep the Winner (A) or Change After 17th (B). No reasoning yet. Write the split on the board.

*"Is anyone courageous enough to stand with ______?"*

## Anchor 2 — What is the problem we're solving?

Do **not** let them start regressing yet.

- Is the question "did the club underperform?" or "whose fault is it, and will it persist?" Those
  sound the same. They are not: the first is about **detection**, the second about **attribution**.
- Push: *"If the line says the club is far below where its goals should put it, have we learned
  anything about the manager yet?"*
- Is that the right question?

> Let the confusion grow: *"A far-below-the-line dot has a lot of possible parents."*

**The trap to let them walk into:** most learners will compute the club's residual (and in D3, the
4.32 spreads below the line), decide that an extreme number is proof of management failure, and stop. They treat *detection* of a
shortfall as *attribution* of it to the manager. The data cannot do that: a residual is a distance
from a line fitted to 20 clubs in one season, and luck, injuries, tactics and the manager all sit
inside it. A third trap, seen in the cold solve: in D4 students start from the club's actual 38 points or add the residual with the wrong sign instead of starting both options from the model's predicted points. A second, quieter trap: students who fit the line with the club included (D2) and
decide that 2.95 spreads is "not that extreme" never run D3, where the club's own pull on the line
is removed.

## Anchor 3 — What is the process?

- How do we turn a residual into a decision? What would we need to believe, and how much?
- If we compare two numbers, expected points under each option, what two quantities does the
  comparison really depend on? (Answer: the forecast next-season shortfall under Keep, and the cost of a reset under Replace. The decision is a break-even question.)
- Is our question still the right question?

## Anchor 4 — What don't we know?

- Appendix D separates what is derived from what the student must choose. The forecast slope
  (0.11, range about 0 to 0.27) is **derived** from ten seasons of Wikipedia tables (Appendix E): a
  club that missed its line by r points missed by about 0.11 × r next season. The reset cost (MA2) has
  no source and the case does not pick it: each Hero chooses and defends a range. Which would you
  trust less? Could a student redo Appendix E for one season pair? (Yes: ten Wikipedia season pages
  are linked. Football-Data files are an optional extension: link-only, each Hero downloads them
  personally.)
- What is the line itself leaving out? (n = 20, one season, GD and points mechanically linked.)
- What are we assuming stays fixed? (This is the case's opening for the twist; do not tip it.)

---

## Data Deep Dive

All figures below are **DERIVED** by the author from the official table (S1) and recomputed in
`sensitivity_model.py`. They are not sourced; students compute them in D1-D4.

**Step 1 — the 20-club line (D1, D2).**

| Quantity | Value |
|---|---|
| Intercept | 52.35 |
| Slope | 0.666 points per goal |
| R squared | 0.941 |
| Residual spread (n - 2 formula) | 4.63 points |
| Club predicted points | 51.68 |
| Club residual | -13.68 |
| Spreads below the line | 2.95 |
| Next-worst residual (AFC Bournemouth) | -4.35 |
| Largest surplus (Aston Villa) | 8.99 |

The intercept equals the mean points (52.35) because mean goal difference is 0 — a neat D1 (iii)
observation. Spurs' 38 points are 13.68 below what its goal difference of −1 predicts; the next-worst
club is 4.35 below. Make sure Heroes see that the gap to the next-worst club is about three times its size.

**Step 2 — the outlier check (D3).**

| Quantity | Value |
|---|---|
| Intercept (other 19 clubs) | 53.07 |
| Slope | 0.665 points per goal |
| R squared | 0.970 |
| Residual spread | 3.34 points |
| Club predicted points | 52.40 |
| Club residual | -14.40 |
| Spreads below the line | 4.32 |

Removing the club makes the fit tighter and the club's miss bigger. The "it is just pulling the
line down" objection fails. Lesson: an outlier can hide by dragging the line toward itself.

**Step 3 — the break-even (D4).** L = 52.40, shortfall = 14.40.

- Forecast next-season shortfall under Keep: 0.11 × 14.40 = **1.58** points, so E_A = 52.40 − 1.58 = **50.82**.
- **Break-even reset cost = 1.58 points.** Change After 17th beats Keep the Winner only if the reset
  cost is smaller than that. The case does not fix a reset cost. For the balance test only, the
  model is evaluated at a **test point of 2 points** (the midpoint of the 0 to 4 range the case
  suggests): E_B = 52.40 − 2 = **50.40**, so Keep wins by **0.82%**. Over the whole suggested range
  Replace wins for reset costs below 1.58, about 40% of it. Do not present the test point as the
  case's claim.

Sit on the break-even: *"Is it plausible that a new manager costs the club less than a point and a
half next season?"* Heroes choose their own ranges: accept any defended range, and ask what it
implies at the low, middle and high ends. A Hero who works D4 with the full-fit numbers (51.68 and
−13.68) lands near the same place (break-even about 1.5); accept it and note the line of record was D3's.

---

## Twist — drop this at ~15 minutes into the discussion

Deliver it slowly. Let each piece land.

> *"The analyst adds one fact. In the ten seasons behind the forecast slope, no club ever finished
> as far below its own season's line as this club did."*
>
> (pause)
>
> *"The slope was fitted on typical clubs. Not on a miss this size."*
>
> (pause)
>
> *"Suppose, just for the next five minutes, that for a miss this size the slope is the top of the
> range: zero point two seven, not zero point one one. Change After 17th still pays only its reset cost."*

Say the number aloud, and say aloud that Option B pays only its reset cost, exactly as Appendix D
(MA3b) states; an earlier adversarial read found that if a Hero charges the slope-based shortfall to
B as well, the twist does nothing, which contradicts MA3b. The largest earlier miss was Manchester
City in 2019/20, about 11.2 points below that season's line, against 13.68 for this club on the
20-club line. If a Hero says the club's miss is "not in the data": yes, that is the extrapolation
worry. The what-if is a stress test of a disclosed range, never a measured fact.

**Facilitator only — do not read aloud.** With slope 0.27, the forecast next-season shortfall is
0.27 × 14.40 = **3.89** points, so the break-even reset cost rises from 1.58 to **3.89** and Replace
now wins for reset costs below 3.89 (about 97% of the suggested 0 to 4 range). At the test point
(2 points): E_A = 52.40 − 3.89 = **48.52** against E_B = **50.40**, so **the winner flips to Change
After 17th, by 3.89%.** Position invalidated: *"the data says the next-season miss is small, so Keep
is safe"*. Position NOT rescued: Replace is not now obviously right, because 0.27 is the top of a
range centred on 0.11, nothing says a new manager would repair a real problem, and a reset cost above
3.89 still favours Keep.

Now: **"Sixty seconds. Are you changing your vote — or not?"**


## Immediate recommit

- Who is not changing? Why?
- **What just broke in your original model?** Were you wrong — or were you missing information?
- Who built their whole case on the extreme residual and never asked how much of it sticks?

---

## Deep conflict — threads (20–30 min)

**Thread 1 — Detection versus attribution.** *"We are certain the club missed its points. How certain
are we about whose miss it was? What would it take to find out?"* Push toward: a residual is a
symptom, and one season of 20 clubs cannot separate Random variation, injuries and management.

**Thread 2 — Fragility to one chosen number.** The forecast slope is derived but uncertain, the reset cost is the Hero's own. At the 2-point test point, flexing either by 50%
flips the winner (see case.json `sensitivity_disclosure[]`; do not read aloud). *"Which option
would you still defend if the board's analyst had picked a different reset cost?"*

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. *"Thirty seconds — keep, or change?"* Stand/sit vote, no explanation. |
| **3:00–10:00** | Position defense. *"Convince us it is better, not just louder."* · *"What is your expected-points number, not a guess?"* |
| **10:00–15:00** | Pressure-test. *"Which option depends most on a number nobody can check?"* |
| **15:00** | **DROP THE TWIST.** Slowly, with pauses. Finish with: *"Sixty seconds. Are you changing your vote — or not?"* |
| **15:00–20:00** | Immediate recommit. Who reverses? *"What just broke?"* |
| **20:00–30:00** | The two threads: detection vs attribution · fragility to one invented number. |
| **30:00–45:00** | Close (including the real decision, below), re-vote, reflection, lessons learned. |

### Five Socratic questions

1. Your D3 line puts the club 4.32 residual spreads below it. If luck alone had produced that, how surprised should we be, and does being surprised tell us whose fault it was?
2. Your break-even reset cost is about 1.58 points. What single piece of evidence would move your own reset-cost range above or below it?
3. If the real reset cost were 1 point instead of 3, what would your recommendation be, and what does that say about trusting any one chosen number?
4. The next-worst club is 4.35 points below the line and the club is 13.68 below. Does a gap of that size prove a cause, or only that something unusual happened?
5. Which of the four limits you named in D5 would most change your vote if you could remove it with one more season of data?

---

## Close

- **Vote again.** Compare to the Anchor 1 board. Who moved?
- **Only now, bring in the real decision.** Public record: the club announced the manager's
  departure on 6 June 2025, 16 days after the final. Its statement said the board unanimously
  concluded a change was in the club's best interests, pointed to the league finish and the points
  from the last 66 league games, and also acknowledged injuries and the demands of European
  competition [S9: tottenhamhotspur.com/news/2025/june/club-statement-ange-postecoglou-departs/]. Read
  the statement yourself before paraphrasing. Ask: *"Did the club's reasoning match anything your
  model could and could not see?"* Do not assign or discuss motives beyond what the statement says.
- We asked ______ as our key question. Was it the right one?
- What math was new to you here, and how did you attack it?

## Lessons Learned

A line of best fit can tell a board, with real confidence, that something unusual happened, and ten
past seasons say that a club's miss one season forecasts only a small miss the next (slope about
0.11). The club sits 4.32 residual spreads below the line, and that survives removing the club from
the fit. The model cannot say what happened or whose it was. The decision comes down to a
break-even: Replace pays off only if a reset costs less than about 1.58 points, and nobody can pin
that cost down for one club. At the case's 2-point test point Keep the Winner leads by 0.82%, which
is real but fragile: the top of Appendix E's range flips it, and so does a reset cost below 1.58. Say that plainly: both
things are true, and naming both is stronger than choosing one.

---

## Standards Touched On

**Scatter Plot · Correlation · Line Of Best Fit · Linear · Slope · Mean · Outlier · Variability ·
Sample Size · Random · How to create a scatter plot given a set of data · How to identify correlation
given a scatter plot or set of data · How to draw a line of best fit given a set of data · How to
write a linear equation given a set of data · How to identify the slope of a line given a set of
data, or a graph of a line of a set of data, or its linear equation · How to find the mean of a set
of data · How to evaluate a variable expression (Substitution Property) · How to find the percent of
a number · How to solve a one-step equation.**

See `LEARNING_GOALS.md` and `case.json.reinforcement_note`.

---

## Facilitator note — sensitivity

SPEC Section 6 applies lightly: a living manager and a real club's real decision. Students judge a
model, not a person. Public record only; no motive speculation; no injury counts from fan sites;
real decision withheld until the Close. If any Hero is a fan with strong feelings, name that at the
start and ask them to argue the side they do not hold for the first round.

## Facilitator note — data terms

The Football-Data.co.uk files may be downloaded by individuals for private use only (S5). Do not
distribute them in class packets and do not run bots or scripts against the site. StatsBomb open
data (S6) must be credited with its logo if anything is published; Understat states no terms (S7).
Both are optional extensions only. FBref expected-goals data was discontinued in January 2026 and
is not used.

## Facilitator note — where the forecast slope comes from (and its limits)

The 0.11 slope was derived on 2026-10-03 by regressing each club's next-season residual on its
this-season residual across nine consecutive-season pairs (2015/16 to 2024/25; 153 club-pairs;
Wikipedia tables S14-S23; points from results so 2023/24 deductions are excluded). Pooled slope
0.109, standard error about 0.083, 95% range about -0.05 to 0.27; season-by-season slopes range
-0.15 to 0.38. Of the 14 club-seasons that missed their line by 5 or more points, the average
next-season residual was about +1.15 (8 of 14 were above the line the next year). Say plainly to the
room that these are small samples, that the slope is an average over typical clubs, and that it does
not say whether a manager caused anything. The reset cost is NOT fixed by the case: the earlier
draft fixed it at 6 and then 2 points, which the coordinator rejected as tuning; it is now a break-even
the Heroes judge, with 2 points used only as the balance-test evaluation point.
