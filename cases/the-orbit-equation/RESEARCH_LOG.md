# Research Log — The Orbit Equation

`case-write` left zero blank numbers as `{{NEEDS_SOURCE}}` placeholders that could actually resolve
to a public figure; per the concept sheet's own feasibility call (MEDIUM — "no specific external
dataset applies... what is real and checkable: Unity's and Unreal Engine's published documentation
on camera-rail/orbit and look-at conventions... not confident about, and necessarily a Modeling
Assumption: the specific arena radius, boss hitbox size, and target framing percentage"), every
production/engineering number in this case was written directly as a disclosed Modeling Assumption,
and only the underlying *technique* was researched for a real citation. This log records what was
searched for each research target.

| # | What was needed | Searched | Found | Outcome |
|---|---|---|---|---|
| P01 | A real, documented example of a game camera system describing an orbiting camera's position with a radius-and-angle (polar) axis system | "Unity Cinemachine Orbital Follow camera radius angle documentation"; fetched the page directly | Unity's Cinemachine 3.1 manual, Orbital Follow component: "The exact position of the camera on the surface is determined by 3 axis values... horizontal, vertical, and radius" | **SOURCED** — S1, HIGH confidence. Confirms Appendix A/B's polar-rig convention is real industry practice, not invented. Context, not load-bearing in the arithmetic. |
| P02 | A real, documented example of a camera system keeping an orbiting camera continuously aimed at ("looking at") a tracked target | "Cinemachine Rotation Composer aim component always look at target documentation"; fetched the page directly | Unity's Cinemachine 3.1 manual, Rotation Composer component: "rotates the camera to face the Look At target" | **SOURCED** — S2, HIGH confidence. Confirms the always-face-the-boss convention behind Challenge D4. Context, not load-bearing. |
| P03 | A real, documented default field of view for a game-engine camera, to establish "how much frame there is to fill" as a real production quantity | "Unity Camera component default field of view 60 degrees manual" | Unity's own Camera manual/scripting reference: a new Camera component defaults to 60 degrees (vertical) | **SOURCED** — S3, HIGH confidence. Context only in Appendix A; the case's actual framing formula (Appendix D) is a stated simplification (MA2), not built from this FOV figure directly, so this does not carry the arithmetic. |
| — | A real, documented Unreal Engine example of a Camera Rig Rail (or similar actor) orbiting 360° around a tracked actor while continuously facing it | "Unreal Engine camera rig rail orbit around actor documentation"; fetched the official Camera Jibs and Dollies page and the Fortnite Camera Rig Rails/Crane page directly | Both official pages describe the Camera Rig Rail as a **linear dolly system** along a spline (used for tracking shots and flyovers) — one explicitly states that with "Lock Orientation to Rail" off, the camera "swivels... pointing at the same position as it started," which is a fixed-point look, not a continuously-orbiting-and-facing behavior. Neither official page actually describes a built-in 360° orbit-while-facing convenience the way Unity's Cinemachine Orbital Follow + Rotation Composer combination does. | **NOT USED.** Rejected as a citation for the orbit-while-facing convention specifically — using it would have overstated what the fetched pages actually say. Unity's Cinemachine (S1, S2) already sourced that exact convention with a direct quote, so the case does not need a second, weaker engine citation for the same point. |
| — | A public figure for a specific game's boss-arena collision/clipping radius | Not searched as a load-bearing figure — this is internal level-design/collision data no studio publishes for a specific title, and the concept sheet's own feasibility note anticipated this | **NOT FOUND, as expected.** Became MA1, a disclosed scenario assumption. |
| — | A public formula converting camera distance to on-screen subject-size percentage for a specific game | Not searched as a load-bearing figure — camera-framing conventions are studio-internal design choices, not published data; the underlying optical principle (apparent size ∝ 1/distance) is a well-established fact of perspective geometry, not something requiring a citation search | **NOT FOUND / not applicable as a citation target.** Became MA2, a disclosed simplification of a well-established optical principle. |
| — | A public, studio-specific per-frame compute-cost figure (in milliseconds) for evaluating a trigonometric camera path | Not searched as a load-bearing figure — per-operation timing depends on hardware, engine, and implementation and is not published by any studio for a specific camera system | **NOT FOUND, as expected.** Became MA3 and MA4, disclosed relative-cost assumptions. |
| — | A public figure for how far a specific real game's boss-fight camera pushes in during a telegraphed attack | Not searched as a load-bearing figure — this is a scene-specific animation/production choice, not published data | **NOT FOUND, as expected.** Became MA6, a disclosed production assumption, and the basis of the Twist. |

## Rejections

The Unreal Engine Camera Rig Rail candidate source (see table above) was found and explicitly
rejected as a citation for "orbit continuously around and face a target" — the two official pages
fetched directly describe a linear dolly-along-a-spline system with an optional fixed look-at point,
not a built-in orbit-and-track convenience. Citing it for that specific claim would have
overstated what the source says. Unity's Cinemachine Orbital Follow + Rotation Composer combination
(S1, S2) was kept as the case's sourcing for the polar-orbit-with-tracking convention because both
were confirmed with a direct quote from the fetched page, not just a search-result summary.

## Status

All real-world technique claims in `case.md` are cited (S1–S3). All production/engineering numbers
(clipping radius, framing constant, per-frame compute costs, push-in amplitude, target frame rate)
are disclosed Modeling Assumptions (MA1–MA6), per the concept sheet's own MEDIUM feasibility call —
this domain has real, checkable *technique* but no public dataset for a specific game's own
production numbers. Zero `{{NEEDS_SOURCE}}` placeholders remain. `case.json.status` set to
`"researched"` (superseded by `"qa"` once case-readiness runs).
