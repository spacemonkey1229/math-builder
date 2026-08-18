# Robotics Engineer — Jordan Reyes (revised)

## Challenge 1 — Research
Khan Academy, "Distance formula" — https://www.khanacademy.org/math/geometry/hs-geo-analytic-geometry/hs-geo-distance-and-midpoints/a/distance-formula-review

## Challenge 2 — Pitch (Route B: Site B first, then Site A)

I recommend **Route B**. Using the distance formula on the Appendix B grid coordinates and
Ultron's rated traverse speed (with Appendix C's terrain-band penalty applied to whichever leg
crosses it), Route B totals a lower travel time than Route A, by a margin of about 3.8% — close,
which is exactly why this decision needs real numbers, not a guess. Route A's first leg crosses
the rocky terrain band at full distance; Route B only crosses it on the shorter second leg, so
less total distance is spent at reduced speed, which is what tips the total time in Route B's
favor even though Route A's raw second-leg distance is shorter.

**Visual:** bar chart, Route A total minutes vs. Route B total minutes, with the terrain-band
portion of each route's bars shaded separately from the full-speed portion.

Strongest argument against my pick: the margin is close enough (under 5%) that if Ultron's actual
terrain-band speed penalty is smaller than Appendix C states, Route A could win instead — that's
the number I'd want double-checked before committing.
