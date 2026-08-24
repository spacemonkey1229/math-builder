# Concept board — pipeline status

The lightweight tracker for concepts moving through `case-brainstorm → case-write →
case-research → case-readiness → case-publish`. One row per concept. Update the `Stage` column
as work lands; link to the concept sheet and, once a concept has a folder, to `cases/<id>/`.

Legend: 💡 concept only · ✍️ drafted (case-write) · 🔎 researched (case-research) · 🧪 in QA
(case-readiness) · ✅ published · ⏸️ paused, needs rework before continuing

| # | Concept | Target | Coverage | Quality | Stage | Notes |
|---|---|---|---|---|---|---|
| C1 | [Perimeter Protocol](cases/perimeter-protocol/case.md) | Formal Logic | 7.0 | 8/8 | 🧪 TIER2_PASS, publishing | Cleared all 6 Tier 2 probes. Caught and fixed a real leak (student-facing "trap" language) and a real trap-checker false-negative ("contrapositive" contains the substring "trap"). Margin unstable under 6/8 flexed assumptions — disclosed, not hidden. Building the publish packet now. |
| C6 | The Cold Start | Matrices (AI/streaming) | 0.0 | 7/8, sharpened | 💡 concept | Sharpened: dilemma now anchored to a named premiere show new subscribers signed up specifically to watch, which either gets buried (A) or costs onboarding completions (B) — not a generic metrics choice anymore. |
| C7 | The Rig Split | Matrices (oil & gas) | 0.0 | 7/8, sharpened | 💡 concept | Sharpened: Basin 1/2 renamed to real, named basins (Permian, Bakken — both separately tracked in the actual EIA/Baker Hughes data), plus a human cost (the veteran crew being relocated) that the spreadsheet can't price. |
| C8 | The Bot Farm | Matrices (AI/network) | 0.0 | 7/8, sharpened | 💡 concept | Sharpened: tied to a specific traffic-spike event 6 hours out, one-shot suspension action (no rollout), raising the cost of being wrong in both directions at once. |
| C2 | The Course Correction | Vectors | 0.0 | 6/8 | 💡 concept | Not started. Solid but generic — the fuel-vs-time tradeoff is real but not yet vivid; revisit before writing. |
| C4 | The Fret Board | Number-theory (music-acoustics) | 0.0 | 6/8 | ⏸️ paused | Drafted + researched — **real defect found**: Rule-of-18 deviation (~12.5 cents) is ~2.5× the stated 5-cent tolerance, not the close race the case needs. Needs a redesign (earlier fret, or reframe metric around cost/deadline vs. a known-larger accuracy cost) before re-entering the pipeline. See `cases/fret-board/case.json` `balance.margin_note`. |
| C5 | The Plaza Bid | Number-theory (tiling-pattern-art) | 0.0 | 6/8 | 💡 concept | Not started. |
| C3 | The Rig Budget | Matrices (gaming) | 0.0 | 5/8 | 💡 concept | Lowest quality in the batch — metric has no real counter-argument once computed (pure compute-cost count, no accuracy tradeoff). Deprioritized behind C6/C7/C8. |

**Right now:** C1 is the only concept in active drafting, moving through `case-readiness`. C4 is
paused pending a redesign, not dead. C6/C7/C8 are being sharpened before any of them starts
`case-write`. Nothing else in this batch has been written yet.
