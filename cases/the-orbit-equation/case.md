Case Study: The Orbit Equation
MS | Math | Case Study | 2026-27 | Launchpad

---

## Overview

The render preview freezes mid-orbit, and Devon Achebe's cursor is still hovering over the keyframe timeline when the lead animator leans into the doorway: "Blocking locks tomorrow morning. Whatever camera path you hand off, that's the one riding into playtest."

Two candidate camera rigs sit open in adjacent viewport tabs. One drifts around the boss on a perfect, unwavering circle — smooth, cheap, predictable. The other tightens its orbit at the exact moment the boss winds up its telegraphed attack, swinging in close enough that the room should genuinely flinch, then easing back out. It looks incredible in the dramatic clip Devon just scrubbed through frame by frame. It also runs more math every single frame of the fight, not just the one dramatic beat — and the boss arena's stone wall sits close enough on the tight side of that curve that clipping into it during a cutscene would be the kind of bug a lead notices in the very first playtest.

Devon has checked the numbers for the flashy moment. Devon has not checked them for the whole fight.

The animator is still standing in the doorway. Devon minimizes both viewport tabs and opens a blank spreadsheet instead.

---

## Background

Devon Achebe is the gameplay camera engineer on Launchpad Games' boss-fight cutscene team, responsible for authoring the camera path that runs during the game's climactic boss encounter. Devon does not choose how the boss animates or attacks; Devon chooses how the camera tracks it, and that choice has to survive both the animation team's blocking review tomorrow and the engine's own frame-time budget once it ships. Camera engineers commonly build orbit and "always face the target" behavior by describing an orbiting camera's position with a radius and an angle relative to the thing it's tracking — a polar description — rather than hand-authoring raw on-screen coordinates frame by frame. Unity's own Cinemachine camera system, one of the most widely used camera toolkits in commercial game engines, implements exactly this convention (SEE APPENDIX A) — because that really is the natural way to reason about "how far from the boss, and at what point around it" as the camera moves.

Devon has narrowed the boss-fight camera to two rigs, both authored around the same boss position at the arena's center. **The Fixed-Radius Orbit** holds the camera at one constant distance from the boss for the entire encounter, computed each frame from a simple radius-and-angle rule — cheap, predictable, and comfortably clear of the arena's stone collision wall, but it frames the boss the same way whether or not anything dramatic is happening. **The Variable-Radius Push-In** instead drives the camera along a polar curve whose distance from the boss actually changes with the orbit angle, tightening in specifically during the boss's telegraphed attack for a bigger, more dramatic frame — at the cost of evaluating one more term of math every single frame of the fight, not only during the dramatic beat, and at the cost of coming closer to the arena's collision wall than the fixed orbit ever does (SEE APPENDIX B for both rigs' governing equations and Option A's authored waypoints, APPENDIX C for the arena's clipping limit, and APPENDIX D for the compute-cost and framing figures each rig actually requires).

Every figure in this case is either cited to real, published camera-engineering documentation (SEE APPENDICES A AND F) or disclosed as a stated production Modeling Assumption (SEE APPENDIX E). The vocabulary and "how to…" skills this case will ask you to research are listed in Appendix G — that is where Challenge 1 sends you.

---

## Dilemma

You are Devon Achebe.

Do you:

**A.)** Ship The Fixed-Radius Orbit — a constant-radius circular camera path around the boss, computed in polar coordinates, cheap to run and comfortably clear of the arena wall **OR**

**B.)** Ship The Variable-Radius Push-In — a polar curve whose radius shrinks during the boss's telegraphed attack for a more dramatic frame, at a higher per-frame compute cost and a tighter clearance from the arena wall

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:

- **D1 — A rectangular-to-polar conversion table confirming Option A's authored waypoints.** Using the eight camera waypoints Devon authored in rectangular (x, y) level coordinates for The Fixed-Radius Orbit (Appendix B), convert each waypoint to polar coordinates (r, θ) centered on the boss. Show your conversion work for at least two waypoints, and state whether every waypoint really does lie at the same radius — confirming (or disproving) that this rig is genuinely a fixed-radius orbit.
- **D2 — A graph of both rigs' governing polar equations.** Using Appendix B's equations for The Fixed-Radius Orbit (r = constant) and The Variable-Radius Push-In (r as a function of θ), plot r versus θ over one full 360° orbit for each rig — by hand or with a graphing tool (e.g., Desmos). Identify the minimum radius The Variable-Radius Push-In ever reaches, and compare it to the arena's clipping radius in Appendix C. Show whether the rig clears the wall, and by how much.
- **D3 — A framing-and-compute-cost comparison table.** Using Appendix B's equations, compute the percent of the frame the boss occupies at each of the eight sampled orbit angles for both rigs (Appendix D gives the framing formula), then find each rig's average percent-of-frame over the full orbit. Using Appendix D's per-frame compute-cost figures, compute each rig's primary metric — average percent-of-frame occupied per millisecond of per-frame computation — and the percent margin between the two rigs. State which rig wins on tonight's numbers.
- **D4 — A camera-facing check using the unit circle.** At each of the eight sampled orbit angles, use the unit circle to find the exact sine, cosine, and tangent of that angle (not decimal approximations) — these describe the direction the camera's position vector points relative to the boss at that instant, which Devon's look-at code needs in order to keep the camera aimed correctly. Identify every angle where the tangent is undefined, and explain in one paragraph what that means for a camera system that computes facing direction from tan θ — why the code needs a special case there, and what a "vertical" position vector physically represents in this orbit.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A — Real Camera-Engineering Technique: Polar Camera Rigs

Referenced in Background.

Both of Devon's candidate rigs use a real, documented technique: describing an orbiting camera's position by a radius and an angle relative to the thing it's tracking (a polar description), and keeping the camera aimed at that target with a dedicated "look-at"/aim behavior, rather than hand-authoring raw on-screen coordinates frame by frame. Unity's Cinemachine camera system — one of the most widely used camera toolkits in commercial game engines — implements exactly this: its Orbital Follow component positions a camera using "3 axis values: horizontal, vertical, and radius," where radius "controls the scale, allowing the camera to move towards or away from the target" [S1], and its Rotation Composer component continuously "rotates the camera to face the Look At target" [S2]. Unity's own default camera field of view is also a real, standard convention — a new Camera component defaults to 60 degrees — establishing "how much frame is there to fill" as a real production quantity, not an invented one [S3]. Neither of Devon's two rigs is an unusual or invented approach; this is the standard way a real production camera system is built. The question in front of Devon is only which of the two specific curves to ship.

---

## Appendix B — Governing Equations and Option A's Authored Waypoints

Referenced in Background and Challenge 3 (D1, D2, D3).

Both rigs are defined with the boss at the pole (origin) of a polar coordinate system, and θ = 0° set at the orbit angle where the boss's telegraphed attack is at its most visible to the camera (SEE APPENDIX C).

| Rig | Governing polar equation |
|---|---|
| A — The Fixed-Radius Orbit | r = 18 (constant, all θ) |
| B — The Variable-Radius Push-In | r(θ) = 18 − 6 cos θ |

Devon separately authored The Fixed-Radius Orbit as eight rectangular (x, y) waypoints in level-coordinate space — one every 45° around the boss — the way the animation team's blocking tool actually stores camera keyframes:

| Waypoint | Design angle | x (game-units) | y (game-units) |
|---|---|---|---|
| W0 | 0° | 18 | 0 |
| W1 | 45° | 12.73 | 12.73 |
| W2 | 90° | 0 | 18 |
| W3 | 135° | −12.73 | 12.73 |
| W4 | 180° | −18 | 0 |
| W5 | 225° | −12.73 | −12.73 |
| W6 | 270° | 0 | −18 |
| W7 | 315° | 12.73 | −12.73 |

Challenge D1 asks you to convert these back to polar form to confirm they really do describe a fixed-radius orbit. Challenges D2–D4 use both rigs' full set of eight sampled orbit angles: 0°, 45°, 90°, 135°, 180°, 225°, 270°, 315°.

---

## Appendix C — The Arena's Clipping Radius

Referenced in Background and Challenge 3 (D2).

The boss arena is a circular stone room. Devon's camera rig is not allowed to come closer to the boss's position than a minimum distance — the **clipping radius** — or the camera passes through the arena wall's collision mesh, a visible rendering bug that a playtester would spot immediately.

| Quantity | Value |
|---|---|
| Clipping radius (minimum allowed camera distance from the boss) | 8.5 game-units |
| θ = 0°, the boss's telegraph angle | The orbit angle at which the boss's telegraphed attack animation is at its most readable. Both rigs in Appendix B are authored relative to this same reference angle. |

The clipping radius is a disclosed Modeling Assumption — SEE APPENDIX E, MA1.

---

## Appendix D — Framing Formula and Per-Frame Compute Cost

Referenced in Challenge 3 (D3).

**Framing formula.** Over the camera distances both rigs use, the percent of the vertical frame the boss's model occupies is modeled as inversely proportional to the camera's current polar radius:

percent of frame ≈ 300 ÷ r

where r is the camera's polar radius in game-units at a given orbit angle. This is a stated simplification of real perspective-camera framing (a closer camera makes a fixed-size subject fill a larger fraction of the frame), scaled so that Rig A's constant orbit gives a stated baseline frame percentage — SEE APPENDIX E, MA2.

**Per-frame compute cost.** Every frame, the camera system has to evaluate its rig's governing equation to find the camera's next position.

| Rig | What it evaluates each frame | Per-frame compute cost |
|---|---|---|
| A — The Fixed-Radius Orbit | one sine and one cosine (radius is constant) | 0.020 ms/frame |
| B — The Variable-Radius Push-In | one sine, one cosine of the orbit angle, and a subtraction (radius changes with θ) | 0.022 ms/frame |

Both figures are disclosed Modeling Assumptions — SEE APPENDIX E, MA3 and MA4. For scale: a cutscene running at a 60-frames-per-second target gives the whole engine roughly 16.67 ms per frame total, shared across rendering, animation, AI, and everything else the game does at once — SEE APPENDIX E, MA5.

---

## Appendix E — Modeling Assumptions

> These figures are **not sourced from an external publisher**. No public dataset reports a specific game's arena collision geometry, its camera system's per-operation compute cost, or its own screen-framing convention — that information is internal to a specific studio's own engine and content. They are stated scenario assumptions chosen by the case author. A Hero may challenge any of these numbers in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Arena clipping radius | 8.5 game-units | No public source states a specific game's arena collision geometry. Set smaller than Option A's 18-unit radius (so Option A is never at risk) but large enough to be a real, checkable constraint on Option B's tighter approach. | This value decides whether Option B's closest approach clears the wall at all — see Challenge D2. The case's numbers are sensitive to this figure. |
| MA2 | Framing constant (percent of frame ≈ 300 ÷ r) | 300 | No public source publishes a formula converting a specific game's camera distance into an exact on-screen boss-size percentage. This is a stated simplification of the real optical principle that on-screen size scales inversely with distance, scaled so Option A's baseline orbit gives a plausible, stated boss-frame percentage. | This constant scales both rigs' frame percentages by the same factor, so on its own it does not favor either option — the two rigs' relative percentages are what actually decides the comparison. |
| MA3 | Per-frame compute cost, Option A | 0.020 ms/frame | Reflects two trigonometric evaluations per frame. No public source publishes a specific studio's own per-operation timing (this varies by hardware and engine); set as a stated relative baseline. | The comparison depends on Option B's cost relative to this baseline, not on this value alone. |
| MA4 | Per-frame compute cost, Option B | 0.022 ms/frame | Reflects one additional cosine evaluation and a subtraction beyond Option A's cost, matching the extra term in Option B's governing equation. No studio-specific figure is public. | The case's whole comparison is highly sensitive to this figure — a smaller extra cost lets Option B's better framing win outright; a larger one could push Option A's win past the SPEC 20% balance cap. |
| MA5 | Target frame rate / per-frame time budget | 60 frames per second → 16.67 ms/frame | A commonly used real target frame rate for real-time gameplay and cutscenes (not universal — some productions target 30 fps). The 16.67 ms/frame figure is arithmetic derived directly from 60 fps (1000 ms ÷ 60), not an independent figure. | Context only — this case's compute-cost comparison (MA3/MA4) does not depend on the total frame budget, only on the two rigs' cost relative to each other. |
| MA6 | Push-in amplitude, Option B (the "6" in r(θ) = 18 − 6 cos θ) | 6 game-units | A production/animation choice: how dramatically the camera pushes in during the telegraph. No public source sets this value for any specific game. | The case's whole comparison is highly sensitive to this figure — a larger push-in amplitude increases Option B's average framing advantage and its per-frame margin, and also brings the camera closer to the arena wall on every orbit. |

---

## Appendix F — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Real orbiting-camera systems commonly describe camera position with a radius-and-angle (polar) axis system relative to a tracked target | "3 axis values: horizontal, vertical, and radius"; "Radius controls the scale, allowing the camera to move towards or away from the target" | Unity Technologies — [Orbital Follow, Cinemachine 3.1 Manual](https://docs.unity3d.com/Packages/com.unity.cinemachine@3.1/manual/CinemachineOrbitalFollow.html) | Cinemachine 3.1, accessed 2026-09-18 | HIGH |
| S2 | Real camera systems keep an orbiting camera continuously aimed at ("looking at") a tracked target via a dedicated rotation/aim behavior | "rotates the camera to face the Look At target" | Unity Technologies — [Cinemachine Rotation Composer component, Cinemachine 3.1 Manual](https://docs.unity3d.com/Packages/com.unity.cinemachine@3.1/manual/CinemachineRotationComposer.html) | Cinemachine 3.1, accessed 2026-09-18 | HIGH |
| S3 | A new camera in a real game engine defaults to a 60-degree (vertical) field of view | 60 degrees | Unity Technologies — [Camera component manual](https://docs.unity3d.com/Manual/class-Camera.html) and [Camera.fieldOfView scripting reference](https://docs.unity3d.com/ScriptReference/Camera-fieldOfView.html) | accessed 2026-09-18 | HIGH (context only — not load-bearing in this case's arithmetic) |

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->

---

## Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Polar Coordinate
- Unit Circle
- Tangent Function

**"How to…" questions**

- How to convert a point between rectangular and polar coordinates
- How to graph a polar equation
- How to find the sine, cosine, and tangent of an angle using the unit circle
