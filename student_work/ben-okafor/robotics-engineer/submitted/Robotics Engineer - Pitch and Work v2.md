# Robotics Engineer — Ben Okafor

## Challenge 1 — Research

How to convert an amount from one unit to another unit:
https://www.basic-mathematics.com/units-of-speed.html

I used this for D3, converting Ultron's 0.06 mph rough-terrain speed into meters per hour so it
would match Appendix A's meter-based coordinates.

## Challenge 2 — The Pitch

**Revised after guide feedback on my first submission** — I had computed everything correctly but
never actually picked a side. Here's the recommendation the numbers support.

I recommend Route C-B-A. Send Ultron to Site B first, then Site A.

Site C is already recovered, at (27, 13). Site A is at (28, 25) and Site B is at (33, 4). Using the
distance formula, the distance from C to A is 12.042 meters, the distance from C to B is 10.817
meters, and the distance from A to B is 21.587 meters.

Converting Ultron's rough-terrain speed of 0.06 mph to meters per hour: 0.06 x 1609.34 = 96.56
meters per hour. Route C-A-B covers 12.042 + 21.587 = 33.629 meters total, which at 96.56 meters
per hour takes 20.896 minutes. Route C-B-A covers 10.817 + 21.587 = 32.404 meters total, which
takes 20.135 minutes.

Container B's integrity is falling at 1.2% per hour from a starting 93%. Going C-A-B, Ultron
reaches B after the full route time of 20.896 minutes, so integrity is 93 - 1.2 x (20.896/60) =
92.582%. Going C-B-A, Ultron reaches B directly from C, after only 10.817/96.56 hours = 0.1120
hours = 6.719 minutes, so integrity is 93 - 1.2 x (6.719/60) = 92.866%.

The strongest argument against my pick is that the gap is genuinely small — 45.66 seconds of
travel time and 0.284 points of integrity, out of a route that takes over twenty minutes either
way. Someone could reasonably say that's noise, not signal, and that Container A's completely
missing data feed is the real decision driver here, not a sub-minute difference between two
routes that both work.

I don't think "small" means "doesn't matter" in this case, though. Route C-B-A doesn't just win on
travel time — it wins on both numbers Spencer actually has, at no cost anywhere else. It's not a
trade-off where a small gain here costs something there; C-B-A is strictly better on the two
things this case actually measures. When one option dominates another on every real metric, taking
the free improvement is the right call even if the margin is thin, precisely because there's no
downside being traded away for it. That's different from the harder judgment call Spencer faces
about Container A's missing feed, which is a real, separate question this recommendation doesn't
try to resolve — routing order and the missing-data question are two different decisions, and
getting the free one right doesn't require solving the hard one first.

## Challenge 3 — The Work

### D1 — Coordinate-plane plot

Plotted all three recovery sites on the coordinate plane using Appendix A's coordinates: Site A at
(28, 25), Site B at (33, 4), Site C at (27, 13). C sits closest to the origin of the three, and a
straight line from A to B passes fairly close to C without going through it exactly — which is
part of why the D6 triangle-inequality check below is worth doing: A, B, and C form a real,
visibly thin-ish triangle on the plot, not degenerate points on a line. (Plot image in the appendix
submission folder — grid drawn by hand, axes 0–35.)

### D2 — Three pairwise distances

Distance C to A: 12.042 m
Distance C to B: 10.817 m
Distance A to B: 21.587 m

### D3 — Total travel time

Route C-A-B total time: 20.896 minutes
Route C-B-A total time: 20.135 minutes

### D4 — Container B integrity on arrival

Integrity via C-A-B: 92.582%
Integrity via C-B-A: 92.866%

### D5 — Recommendation

Route C-B-A: 20.135 minutes and 92.866% integrity, both strictly better than Route C-A-B's 20.896
minutes and 92.582% integrity. See Challenge 2 for the full argument and the strongest objection
to it.

### D6 — Triangle inequality check

C to A plus C to B: 12.042 + 10.817 = 22.858 m. Direct A to B: 21.587 m. Since 22.858 is greater
than 21.587, the triangle inequality holds — the coordinates describe a real, valid triangle, so
the drone survey data is internally consistent before Ultron commits to a route. The margin is
22.858 - 21.587 = 1.271 m.

### Original comparison (not in the case appendix)

I wanted to see the two routes' advantage in units that are easier to feel than minutes and
percentage points, so I converted both differences myself.

| Comparison | C-A-B | C-B-A | C-B-A's edge |
|---|---|---|---|
| Travel time (seconds) | 1253.76 | 1208.10 | 45.66 seconds faster |
| Container B integrity | 92.582% | 92.866% | 0.284 points more intact |

(20.896 minutes x 60 = 1253.76 seconds; 20.135 minutes x 60 = 1208.10 seconds; difference =
45.66 seconds.)

![Route comparison chart](route-comparison-chart.png)

## Challenge 4 — Appendix of work

Worked the distance formula by hand for all three pairs, then converted mph to m/hr before doing
any time calculations so the units would match. Checked the triangle inequality last since it uses
the same three distances from D2 and didn't require any new data.
