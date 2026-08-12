# Robotics Engineer — Jordan Reyes

## Challenge 1 — Research
Khan Academy, "Distance formula" — https://www.khanacademy.org/math/geometry/hs-geo-analytic-geometry/hs-geo-distance-and-midpoints/a/distance-formula-review (used to check my leg-distance math below).

## Challenge 2 — Pitch (Route B: Site B first, then Site A)

I recommend **Route B — navigate Ultron 2.0 to Recovery Site B first, then Site A**. Total travel
time is the only thing that matters here, since both containers have to come home regardless of
order and the rover's battery margin doesn't change with route order — the entire decision is
which leg sequence produces the lower total minutes.

I computed both leg distances from the grid coordinates in Appendix B using the distance formula
(how-to researched above), converted each distance to minutes using Ultron's rated traverse speed
in Appendix A, and summed. Route A (Site A then Site B) comes out higher than Route B because the
first leg of Route A crosses the rockier terrain band described in Appendix C, which the case
states cuts effective speed — Route B's first leg avoids that band entirely and only picks it up
on the shorter second leg, so less total time is spent at the reduced speed.

**Visual:** see attached grid diagram (bar chart of Route A vs Route B total minutes, with the
terrain-band overlap highlighted on each route).

Strongest argument against my pick: Route A's second leg is measurably shorter in raw distance, so
if the terrain-speed penalty were smaller than stated, Route A could still win — that's the
assumption I'd want double-checked first.
