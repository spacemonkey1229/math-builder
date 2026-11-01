# Research Log — The Point Cloud Match

Stage 3 (`case-research`) run on `cases/the-point-cloud-match/`. 29 `{{NEEDS_SOURCE}}` placeholders
were enumerated from `case.json.needs_source[]`. Worked in load-bearing weight order: the real
Stanford Repository statistics first (they anchor D1 and Appendix A), then the marker-coordinate
appendix (the case's central geometric evidence, D2–D4), then the documented-failure-mode note,
then the time/deadline/tolerance figures (D5).

## P01–P08 — Stanford Bunny / Dragon / Happy Buddha scan-pass, vertex, triangle, format counts

**Searched:** Direct `WebFetch` of `http://graphics.stanford.edu/data/3Dscanrep/` with two
independently-worded prompts, both returning identical figures.

**Fetched directly:** the repository's own page. Then, for independent verification, downloaded
`http://graphics.stanford.edu/pub/3Dscanrep/bunny.tar.gz` directly via `curl` (the page's own
download link resolves to `graphics.stanford.edu/pub/...`, a different subpath than the summary
page) and parsed it locally:

- `bun.tar.gz` extracts to exactly the real dataset: 10 raw range-scan `.ply` files
  (`bun000/045/090/180/270/315.ply`, `chin.ply`, `ear_back.ply`, `top2.ply`, `top3.ply` — matching
  "Number of scans: 10" exactly) plus the `reconstruction/` folder's `bun_zipper.ply`.
- `bun_zipper.ply`'s own PLY header reads `element vertex 35947` / `element face 69451` — an exact
  match to the summary page's stated 35,947 vertices / 69,451 triangles.
- Summing each raw scan file's own `element vertex` count (40256+40097+30379+40251+31701+38298+
  36023+35336+37738+32193) gives **362,272** — an exact match to the summary page's stated
  "Total size of scans: 362,272 points."

This double-checks the primary source against itself (not just trusting a rendered summary page)
and is the strongest possible confirmation short of a second independent publisher.

**Outcome:** SOURCED as **[S1]** (page) and **[S1b]** (direct file verification), **HIGH**
confidence for both — primary publisher, dated data (README states August 1996 acquisition,
though the page itself carries no separate "last updated" date — noted as such rather than
invented), unambiguous units, exactly the figures needed, and independently cross-checked against
the raw files themselves. Used directly in Appendix A's table (Bunny/Dragon/Happy Buddha rows) and
in a new Appendix A sub-table giving the Bunny's real per-pass point breakdown, needed for D1's
"percent of total scanned vertices belonging to the suspect pass" calculation — `bun315.ply`
(35,336 of 362,272 points, ≈9.75%) was picked as the real, published stand-in for "the pass Priya
suspects is mirrored," since Priya's own (fictional) prop has no published per-pass data of its
own.

## P09 — A citable documented description of a mirrored/reflected registration reported as "converged"

**Searched, in order:**
1. `"photogrammetry point cloud registration mirrored reflected alignment converged documented failure mode"`
2. `"ICP iterative closest point local minimum symmetric object mirror flip ambiguity point cloud registration"`
3. `"Metashape RealityCapture documentation chirality reflection alignment error symmetric object misalignment"`
4. `""symmetry ambiguity" OR "mirror ambiguity" point cloud registration ICP converge wrong local minimum symmetric shape"`
5. `"registration" OR "alignment" 3D scan symmetric prop "mirrored" turntable photogrammetry known issue markers fix"`

**Fetched directly (to verify, not just trust search-summary text) and rejected as not matching the specific claim:**
- `arxiv.org/abs/2506.14771` ("Empirical Studies of Large Scale Environment Scanning by Consumer
  Electronics") — a search-result summary implied this paper discussed objects "flipped upside
  down." Direct fetch of the abstract confirms it does **not** — it is a Matterport-Pro3-vs-iPhone
  accuracy benchmark with no symmetry-ambiguity content. Rejected.
- `arxiv.org/abs/2312.02985` (FocalPose++) — same false lead, checked and rejected; no symmetry
  discussion in the available content.
- `pmc.ncbi.nlm.nih.gov/articles/PMC5580094` (an ICP-with-geometric-features paper) — a
  search-summary implied a specific "box symmetric under 180° rotation, one solution 0 RMSE, one
  high RMSE" claim. Direct fetch found **no such passage** in this paper. Rejected as
  unverifiable — the search engine's own summarization, not the source, appears to have
  synthesized/conflated content across multiple abstracts. This is exactly the kind of
  AI-summary drift `case-research` is supposed to catch by fetching primary text rather than
  trusting a search snippet.
- `arxiv.org/abs/2505.13088` (CoFF, cross-modal point cloud registration) — abstract confirms only
  a general mention of "symmetric similarity" as a challenge category, not the specific
  converge-to-a-mirrored-pose claim. Rejected as too generic to cite for the specific claim.

**Found and confirmed real:** `photogrammetrycommunity.github.io/metashape-expert-manual/...` —
the Metashape Expert Manual (a community-maintained technical manual for Agisoft Metashape, one of
the industry's major photogrammetry pipelines). Fetched directly; confirmed it states, verbatim:
"Symmetries and repetitive patterns: building façades, tiled floors, agricultural row crops, brick
walls" as a named alignment-failure cause, and "Repetitive-feature scenes can defeat dozens of
markers. When the false matches in the existing tie-point graph reinforce the wrong pose, even many
manual markers may not override" — i.e., a real, documented case of automatic alignment settling
into a self-consistent-but-wrong pose, with markers as the (imperfect) real-world remedy. This
directly parallels the case's own two options (trust the solver vs. manually recheck against known
points).

**Outcome:** SOURCED as **[S2]**, **MEDIUM** confidence — real, on-topic, and fetched directly, but
it does **not** use the words "mirrored," "reflected," or "converged," so it does not verbatim-match
the placeholder's exact composite claim. Per SPEC §5 and the skill's own rules, this gap is
disclosed rather than papered over: Appendix E's **MA6** states plainly that this case's specific
"reflection across an axis" framing is a modeling choice built for the coordinate-plane Challenges,
grounded in — but not a verbatim quote of — a real documented failure class.

## P10 — Manual marker/tie-point placement as a real per-point task (basis for technician-minute assumptions)

**Searched:** `"manual tie point marker placement time per point photogrammetry Metashape RealityCapture workflow minutes"`.

**Fetched directly:** `agisoftmetashape.com/how-to-place-markers-in-agisoft-metashape-a-step-by-step-guide/`
(Agisoft's own published guide, dated 2025-09-13). Confirms markers are placed by hand and refined
across "several different images where the same feature is visible" — a genuine per-point,
multi-photo manual task.

**Outcome:** SOURCED as **[S3]**, MEDIUM confidence (vendor's own guide, real and dated, but gives
no minutes-per-marker figure for any studio — no such figure appears to exist publicly). This
grounds, but does not fully source, Appendix E's **MA2** (7 min/marker) and **MA3** (12 min
re-export/re-check) — both remain disclosed Modeling Assumptions, not sourced facts.

## P11 — A citable registration/scan-to-CAD tolerance in millimeters, at VFX/photogrammetry specificity

**Searched:** `"photogrammetry registration accuracy tolerance millimeters reverse engineering scan-to-CAD industry standard"`.

**Fetched (via search-result synthesis, cross-checked against the Novedge article's own stated
figures):** no source states a general "acceptable VFX prop registration tolerance in mm." Real,
citable figures exist at both ends of a range — precision optical-metrology parts (~0.005–0.03 mm,
CMM-inspected, not photogrammetry-based) and formed sheet-metal/plastic scan-to-CAD tolerances
(~0.030in ≈ 0.8 mm) — with an explicit statement that "photogrammetry should not be used as the
basis of a tolerance-critical CAD rebuild."

**Outcome:** NOT FOUND at the case's exact specificity → **Modeling Assumption**. SOURCED the
*range* as **[S4]**, MEDIUM confidence, and used it as the disclosed basis for **MA1**: 1.0 mm RMS,
picked at the loose (non-precision-metrology) end of the real range, appropriate to a VFX prop
replica rather than a machined or optical part. Sensitivity stated: below ~0.55 mm the tolerance
would also fail Option B's own corrected residual.

## Marker-coordinate methodology (Appendix B) — real Bunny vertex data as basis

Rather than inventing marker coordinates outright, four real 3-D vertices were pulled directly from
the downloaded `bun_zipper.ply` (the same file behind [S1]/[S1b]): the mesh's own extreme vertices
in +x, −y, −x, and +y. Their (x, y) components (z dropped) were converted from meters to
centimeters and rounded to two decimals, giving the four "expected" marker coordinates:

| Marker | Real Bunny vertex used | Expected (cm) |
|---|---|---|
| 1 | max-x vertex | (6.10, 6.23) |
| 2 | min-y vertex | (−5.38, 3.30) |
| 3 (suspect) | min-x vertex | (−9.47, 12.42) |
| 4 | max-y vertex | (−1.75, 18.73) |

"Actual" coordinates were then built by disclosed, computable transforms, not invention:
- Markers 1 & 2: a single real rigid translation, (Δx, Δy) = (+3.00, +2.00) cm — verified to
  preserve Distance(1,2) exactly (11.848 cm both expected and actual), confirming a genuine
  rigid motion.
- Marker 3: reflected across the rig's local y-axis (x → −x), no translation — the case's central
  mirrored-pass defect. Verified: predicting Marker 3 under the Markers-1&2 translation instead
  gives (−6.47, 14.42), a 160.65 mm gap from its actual (9.47, 12.42) — confirming reflection, not
  translation, explains it.
- Marker 4: reflected across the rig's local x-axis (y → −y) instead — a *different* mirror axis,
  deliberately inconsistent with Marker 3's, to ground the Twist ("it doesn't match either... not
  the same way... differently") in an actual, different, computable geometric fact rather than a
  vague narrative beat.

All of this — the base coordinates, the translation, both reflections, and every distance derived
from them — is arithmetic on disclosed real data and disclosed transforms; none of it required an
external citation, per the task's own framing that a mirroring error is "a computable geometric
form... derivable mathematically... once real coordinates are chosen."

## Scenario/assumption figures (Appendix C, and the rig's/manual-correction error figures)

Six figures are disclosed Modeling Assumptions (MA1–MA6 in `case.md` Appendix E and
`case.json.modeling_assumptions[]`), each with a stated basis and a mandatory sensitivity note per
SPEC §5 and the skill's rules: MA1 (1.0 mm tolerance), MA2 (7 min/marker), MA3 (12 min
re-export/re-check), MA4 (0.40 mm rig self-report), MA5 (0.55 mm manual-correction residual), MA6
(the reflection framing itself). Appendix C's time-of-day figures (4:40 PM converged, 5:30 PM
deadline) and the re-shoot cost ($8,500) are stated scenario constraints, disclosed as such in
`case.md`'s own existing note, not claimed to be sourced.

## margin_pct

Computed from the real/assumption numbers above: face-value ratio A (0.40 mm / 90 min = 0.004444
mm/min) vs. face-value ratio B (0.55 mm / 123 min = 0.004472 mm/min) → **margin_pct = 0.61%**, well
under SPEC §2's ~20% cap, and deliberately razor-thin (in the spirit of the Robotics Engineering
exemplar's 0.09%) because the case's entire point is that this tight, defensible-looking margin is
built on one unverified number (MA4). Substituting the D2–D4-derived real error (160.65 mm) for
MA4 gives a true ratio ~400x worse for Option A — recorded as `balance.true_reveal_ratio_note` in
`case.json`, facilitator-only, not written into `case.md`.

## NOT FOUND summary

| Placeholder | Outcome |
|---|---|
| Documented "mirrored, reported as converged" description at exact specificity | NOT FOUND verbatim → cited the closest real, on-topic documentation ([S2]) at MEDIUM confidence, and disclosed the exact gap as **MA6** rather than overstating the match. |
| VFX/photogrammetry registration tolerance in mm at case's exact specificity | NOT FOUND → **Modeling Assumption MA1** (1.0 mm), grounded in a real, sourced range ([S4]). |
| Minutes per manual marker registration, minutes to re-export/re-check | NOT FOUND (no studio publishes this) → **Modeling Assumptions MA2/MA3**, grounded in real documented per-point manual-marker practice ([S3]). |

All other placeholders (Stanford scan/vertex/triangle/format counts, all four marker coordinates,
the rig's self-reported error, the manual-correction residual, all Appendix C time/cost figures)
are now either real sourced data ([S1]/[S1b]) or disclosed scenario figures/Modeling Assumptions,
per SPEC §5 — zero remain as invented-but-unlabeled numbers.

## Next step

Run `case-qa` on `the-point-cloud-match`. (Not run as part of this pass, per instruction — this
case-research run leaves `case.json.qa.verdict` as `null`.)

---

## 2026-09-12 addendum — S4 data-decay fix (case-readiness Tier 2 P6)

A subsequent `case-readiness` run (see `QA_REPORT.md`) live-re-fetched all 5 sources during Tier 2
probe P6 (data decay) and found the original S4 (Novedge, "Scan-to-CAD Workflows...") had rotted:
the URL is still reachable (HTTP 200, stable across two fetches) but its live content (28,846
chars stripped) is now a *different*, generic scan-to-CAD pipeline article (FPFH/SHOT, ICP,
pose-graph optimization, VDI/VDE 2634) that contains none of the figures originally cited from
it — no 0.005mm, no 0.0002in, no 0.030in/0.8mm, no "CMM," no "tolerance-critical CAD rebuild."
`case-readiness` correctly downgraded S4 to LOW confidence rather than leaving a stale citation,
and flagged it as the one open blocker to `TIER2_PASS`.

**Re-research performed for this fix:**

1. **Checked whether the content simply moved.** Web-searched the exact phrases ("tolerance-critical
   CAD rebuild", the 0.005mm/0.8mm figures) to see if the Novedge article had migrated to a new
   URL or a mirror. Two candidate pages surfaced in search-engine AI summaries
   (phillipscorp.com/india/3d-scanning-reverse-engineering-accuracy and
   3d-scantech.com/reverse-engineering-manufacturing-scan-to-cad) that appeared, in the search
   summary text, to carry the same figures. **Both were fetched and grepped directly** (not
   trusted from the search summary) — neither page's actual text contains the 0.005mm, 0.0002in,
   0.030in, or 0.8mm figures. (phillipscorp.com does carry a very similar sentence — "Use it for
   context and scale; do not use it as the basis of a tolerance-critical CAD rebuild" — but not
   the numeric range.) **Rejected**: search-engine AI summaries can blend in memorized/training
   content that isn't actually on the live page; only the directly-fetched, grepped text counts.
   Conclusion: the original figures are not verifiably live anywhere. No replacement found by this
   route.
2. **Searched for a real manufacturer/standard spec sheet for the tight end of the range**
   (precision optical metrology). Found and verified live: Creaform's own HandySCAN 3D BLACK
   Series technical-specifications page (creaform3d.com) states "HandySCAN BLACK™ Elite Accuracy
   0.025 mm (0.0010 in)," acceptance-tested per VDI/VDE 2634 part 3 — a real, current, directly
   fetched vendor spec (confirmed via direct `curl` + grep of the live page, not a summary). This
   would have worked as a tight-end replacement but was set aside once a better-fitting source
   (below) was found.
3. **Searched for a source that measures the actual quantity MA1 approximates** (photogrammetric
   registration accuracy in mm, not a manufacturing scan-to-CAD tolerance analogy). Found
   Kenely, Bugeja, Grima, Pullicino, Pullicino, Seychell, "Large-Scale Photogrammetric
   Documentation of St. John's Co-Cathedral: A Workflow for Cultural Heritage Preservation"
   (arXiv:2604.24316, v2 posted 2026-05-14) — a primary, dated academic paper. **Downloaded the
   actual PDF and grepped the extracted text directly** (not a search summary) to confirm the
   figures verbatim: "mean point error reached 1.3mm with a maximum of 3.2mm at peripheral scan
   pairs," "[core-area] registration (28 scans) achieved tighter results: 0.9mm mean point error,"
   and "Target-based registration between scan clusters yielded a mean distance error of 5.8mm" —
   all present exactly as quoted, on p.9 and in the results table on p.11.

**Decision: replaced S4** with the arXiv paper. This is a better fit than the original Novedge
source, not just a substitute — it reports the actual measured quantity (photogrammetric
multi-scan registration point error, mm) rather than a manufacturing-tolerance analogy, it is
HIGH confidence (primary, dated, unambiguous units, directly the thing the case needs), and MA1's
1.0mm value already sits inside its real 0.9–1.3mm measured range, so **no numeric value changed**
— `MA1` stays at 1.0 mm RMS, and it remains a disclosed Modeling Assumption in Appendix E (a
*measured error* is not the same claim as a stated *client acceptance threshold*, so promoting it
to a directly-sourced fact would overclaim). No downstream `margin_pct`, `balance`, or derived
figures required any change.

Updated: `case.json.sources[]` S4 (full replacement, confidence LOW → HIGH); `case.md` Appendix D
note, Appendix E MA1 basis cell, Appendix G S4 row; published HTML's matching MA1 row, S4 sources
row, and Sources list entry. Docx/xlsx rebuilt from the updated `case.md`/`case.json`;
`MANIFEST.json` updated with new file sizes, new `case_md_sha256`, and a build note.
