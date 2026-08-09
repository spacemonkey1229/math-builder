# Robotics Engineer — Ben Okafor

## Challenge 1 — Research

How to convert an amount from one unit to another unit:
https://www.basic-mathematics.com/units-of-speed.html

I used this for D3, converting Ultron's 0.06 mph rough-terrain speed into meters per hour so it
would match Appendix A's meter-based coordinates.

## Challenge 2 — The Pitch

Both orders get Ultron to both remaining sites, and the numbers for each are close enough that
either could work depending on what Spencer values most. Route C-A-B and route C-B-A both recover
both containers safely. It really comes down to what Spencer wants to prioritize.

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

So C-B-A is a little faster (20.135 minutes vs 20.896 minutes) and preserves a little more of
Container B's integrity (92.866% vs 92.582%) since it reaches B sooner. But the difference is
small either way — under a minute of travel time and under a third of a percentage point of
integrity — so both options are valid and Spencer could reasonably choose either one.

## Challenge 3 — The Work

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

See Challenge 2 above — either route is defensible.

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
