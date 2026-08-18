# Case Study: Robotics Engineer

MS | Math | Case Study | 2026-27 | Heroes Academy

---

## Overview

Buzz, buzz, buzz. Spencer Tollson's phone vibrates across his bedside table. He wakes to red alarm-clock digits piercing the dark of the bedroom. Picking up the phone, he hears an urgent but familiar voice. "Spencer, it's Harriet — there's been a train crash and we need your team on site." Harriet Griggs is a FEMA agent Spencer's team has worked with before.

"There's an SUV outside your home. Your team's already begun loading Ultron." Spencer rubs his eyes. "What's the situation on the ground?"

"DOD has classified cargo they need recovered fast. No one's being allowed near the crash site until it's clear. We'll brief you on the plane — hurry."

By the time Spencer lands, his team has already reached the staging area. Ultron — seven feet of hazard-rated recovery robot — is powered up and waiting. Spencer pulls up the drone survey of the wreckage on his tablet: three sealed containers, scattered debris, and a decision he has to make before Ultron takes its first step.

He has already sent Ultron to the nearest container. Now, with two more still out there, he has to choose which one to reach first.

---

## Background

Spencer Tollson leads a six-engineer team at OBG Dynamics that built Ultron 2.0, a robot designed for hazardous disaster recovery. Ultron has completed five similar missions over the past two years. It is humanoid in design, able to withstand extreme temperatures, climb over obstacles under 4 feet tall, lift up to 2,300 lbs, and carry up to 100 lbs of equipment. It moves at 0.64 miles per hour over clear terrain and 0.06 miles per hour over rough terrain — the debris-covered ground of a wreckage site counts as rough terrain everywhere within it.

A Union Atlantic freight train derailed outside Benionsville, Iowa, scattering cargo across a debris field. Most of it is routine commercial freight. Three sealed containers are not: DOD-classified cargo the agency will not describe, only monitor. No human may approach until Ultron has moved each container into a sealed recovery bag.

Ultron has already reached **Recovery Site C** and secured that container. Two remain: **Recovery Site A** and **Recovery Site B**. The DOD's satellite feed gives structural-integrity readings for both — Container B's casing is intact but degrading fast; Container A's sensor feed cut out, so Spencer has no integrity reading for it at all (SEE APPENDIX B). The positions of all three sites, mapped from drone reconnaissance, are in **APPENDIX A**.

Spencer has to choose Ultron's next move. The exact ground rules for how to compute travel time and integrity loss — what counts as rough terrain, whether Ultron pauses to climb — are fixed in **APPENDIX C**; use them, or your numbers won't match anyone else's.

The vocabulary and the "how to…" skills this case will ask of you are listed in **Appendix E** — that is where Challenge 1 sends you. For real-world background on humanoid disaster-recovery robots and rail-freight derailments, SEE APPENDIX D.

---

## Dilemma

You are Chief Robotics Engineer Spencer Tollson, after navigating to Recovery Site C.

Do you:

**A.)** Navigate Ultron 2.0 to Recovery Site A, then Recovery Site B **OR**

**B.)** Navigate Ultron 2.0 to Recovery Site B, then Recovery Site A

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A coordinate-plane plot** of Recovery Sites A, B, and C, plotted from Appendix A's map.
- **D2 — The three pairwise distances** between C, A, and B (C-to-A, C-to-B, and A-to-B), computed with the distance formula and shown as a right-triangle/Pythagorean-theorem calculation, not just read off the grid.
- **D3 — Total travel time** for both possible route orders (C→A→B and C→B→A), using Ultron's stated rough-terrain speed, with your units converted and shown at every step.
- **D4 — Container B's structural integrity remaining** at the moment Ultron reaches it, computed separately for each route order using Appendix B's decay rate.
- **D5 — A one-sentence recommendation** stating which order is faster, and by how much.
- **D6 — Verify the three distances from D2 satisfy the Triangle Inequality Theorem** (no one side can be longer than the sum of the other two) — a real sanity check on the drone survey's coordinates before Ultron commits to a route through a debris field no human can enter.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A: Crash-Site Map

Positions read directly from the drone-reconnaissance map (1 grid unit = 1 meter), measured from an arbitrary origin at the corner of the debris field:

| Site | Coordinates (m) |
|---|---|
| Recovery Site A | (28, 25) |
| Recovery Site B | (33, 4) |
| Recovery Site C | (27, 13) — already recovered |

The entire mapped area is scattered debris and counts as rough terrain for Ultron's speed (SEE BACKGROUND). Debris under 4 feet tall is climbable, at a rate of 0.2 feet of height per minute; debris 4 feet or taller, and the derailed train cars themselves (6+ feet), are not passable and must be routed around.

---

## Appendix B: DOD Container Data

| | Container A | Container B | Container C |
|---|---|---|---|
| Contents | Classified | Classified | Classified |
| Size | 5-gallon barrel | 5-gallon barrel | 5-gallon barrel |
| Structural integrity | No data (feed lost) | 93%, falling 1.2% per hour | 32%, falling 0.3% per hour — already recovered |

"Structural integrity" is the DOD's own term for how sealed the casing remains; 0% means the casing has failed and its contents have leaked.

---

## Appendix C: Modeling Assumptions

**Assumption 1 — Uniform rough terrain.** The entire debris field is treated as rough terrain at Ultron's stated 0.06 mph rate for every leg of every route. This case does not ask you to model a faster shortcut through any locally clearer patch of ground — Appendix A's map is for plotting coordinates and distances, not for hand-routing around individual debris shapes.

**Assumption 2 — Straight-line travel.** Each leg of a route (C-to-A, C-to-B, A-to-B) is traveled in a straight line at the rough-terrain rate. Ultron does not pause to climb any individual obstacle under this assumption — Appendix A's climbing rate is given as real context for the site, not as a required step in D3's time calculation.

**Assumption 3 — Container A's integrity is not computable.** With no data feed, D4 only asks for Container B's integrity on arrival — there is no honest number to compute for Container A, and this case does not invent one.

---

## Appendix D: Learn More

Curious about the real technology and real disasters behind this case? These are real, freely available resources — none of them are required to complete the Challenges.

- [DARPA Robotics Challenge (Wikipedia)](https://en.wikipedia.org/wiki/DARPA_Robotics_Challenge) — overview of the real 2012–2015 competition that pushed humanoid robots like Ultron 2.0 toward disaster-recovery tasks.
- [Robonaut (Wikipedia)](https://en.wikipedia.org/wiki/Robonaut) — the story of NASA's real dexterous humanoid robot, built to work in environments too hazardous for people.
- [Atlas (Boston Dynamics)](https://bostondynamics.com/atlas/) — the official page for a real humanoid robot built for material handling in industrial settings, a close cousin of Ultron's fictional role.
- [National Transportation Safety Board](https://www.ntsb.gov/) — the real U.S. federal agency that investigates train derailments like the one this case is based on.
- [National Robotics Engineering Center](https://www.nrec.ri.cmu.edu/) — the real Carnegie Mellon lab that built CHIMP, one of the disaster-response robots pictured in this case's interactive version.

Links verified live 2026-08-18.

---

## Appendix E: "How To…" Math Questions To Research

**Vocabulary**

Coordinate Plane · Coordinate Pair (also Ordered Pair) · Right Triangle · Hypotenuse · Pythagorean Theorem · Triangle Inequality Theorem · Unit · Percent

**How to…**

- How to graph a coordinate pair on the coordinate plane
- How to find the distance between two coordinate pairs on a coordinate plane
- How to convert an amount from one unit to another unit
- How to find the percent of a number
- How to compare two or more values
