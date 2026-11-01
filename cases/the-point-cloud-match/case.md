# Case Study: The Point Cloud Match

MS | Math | Case Study | 2026 | Adventure

---

## Overview

The progress bar fills all the way and the word **CONVERGED** turns green on Priya Kessler's second monitor.

She doesn't move. Behind her, the scan rig's turntable ticks as it cools — six hours of range-image passes, forty-one gigabytes of raw point cloud, all of it now folded down into one aligned mesh sitting in the export queue. On her first monitor, the client's reference model rotates slowly, waiting for the file that's supposed to sit exactly on top of it.

Priya zooms into the mesh's left flank, where pass four met pass five. Something about the seam bothers her. She pulls up the three calibration markers taped to the physical prop before the scan — three known points, logged by hand, that should land in the same place on both the reference model and her scan if the alignment actually worked. Two of them look right. The third one doesn't look wrong, exactly. It looks like it's on the wrong side of the object.

Her phone buzzes, face-down, next to the keyboard. She already knows who it is. The client needs the file by end of day, and if it comes back from their pipeline mis-registered, the studio eats the cost of the whole re-shoot — camera rig, turntable time, her Saturday.

The software says converged. Her eyes say something got mirrored.

Priya picks up the phone without answering it, and opens the marker log.

---

## Background

Priya Kessler is a 3-D scanning and photogrammetry technician at a small VFX digitization studio. Her job is to turn a physical object into a clean, aligned 3-D mesh that matches a client-supplied reference model closely enough for the client's own pipeline to accept it without manual correction. She is accountable for the file she ships — if it fails the client's own registration check after delivery, the studio pays for the re-shoot, not the client.

The scan rig captures the object in multiple passes from different camera positions and stitches them into one point cloud automatically. Its alignment software reports a single word when it's done: **converged** or **failed**. It does not report *how* it converged, and it cannot, on its own, tell the difference between two mesh sections that are related by an ordinary rotation and two that are related by a **reflection** — a mirror flip. This is a known, documented failure mode in multi-pass photogrammetry: if a camera pass is oriented backward relative to the others, the matching algorithm can pair up mirrored surface features and report a low, "converged" error anyway, because the *shape* still looks similar even though it is no longer the same object traced through space (SEE APPENDIX A).

To catch this, the studio always logs the physical position of **three known marker points** stuck to the object before scanning starts, and records where the client's reference model says each marker *should* land ("expected") versus where the finished scan says each marker actually *is* ("actual") (SEE APPENDIX B). If the actual markers are a rotation and translation of the expected markers, the scan is trustworthy. If one marker's actual position looks like a reflection of its expected position instead, part of the scan is mirrored — and the rig's own reported error number cannot be trusted to say so.

Two paths are open to Priya:

**Option A — Ship As Converged.** Accept the rig's report and export the file now. Costs no additional technician time, but any mirrored region ships uncorrected.

**Option B — The Marker Recheck.** Manually re-register the scan against the three known marker points by hand, correcting any reflection before export. Catches a real mirroring defect, but the client's end-of-day deadline is fixed, and the manual pass has to fit inside the technician time Priya has left (SEE APPENDIX C).

Every registration decision at the studio is judged by the same yardstick: how much point-to-point mismatch, in millimeters, is left in the file relative to how many technician minutes it cost to get there (SEE APPENDIX D). Any figure in this case that is not a real, sourced number is disclosed plainly as a stated Modeling Assumption (SEE APPENDIX E), and every source used to ground this case is listed in full in **APPENDIX G**. The vocabulary and "how to…" skills this case will send you to research are listed in **APPENDIX F**.

---

## Dilemma

You are Priya Kessler.

Do you:

**A.)** Accept the scanning rig's automatic alignment, which the software reports as converged, and ship the file **OR**

**B.)** Manually re-register the scan by hand against the three known marker points, correcting any reflection before you export

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A scan-scale note in scientific notation.** Using the real vertex and triangle counts for the Stanford scans in Appendix A, write each count in scientific notation, and calculate what percent of the total scanned vertices belong to the pass Priya suspects is mirrored. *Why this approach: the real counts here span tens of thousands to over a million, and scientific notation is the tool built for comparing figures at that different a scale without losing track of zeros — the percent-of-total step then puts one single pass in proportion to the whole scan, the same proportional reasoning Priya needs before she can say how much of the finished mesh even sits inside the suspect pass.*
- **D2 — A congruence-or-similarity audit.** Using the coordinate-pair distance formula, find the marker-to-marker distances within the "expected" (reference) set and within the "actual" (scanned) set from Appendix B. Decide, and justify with your numbers, whether the expected and actual marker triangles are **congruent** (same size and shape — a valid rotation/translation) or only **similar** (same shape, different scale — a sign the scan drifted), or neither. *Why distances first: the distance formula measures how far apart two points are, which is exactly what tells you whether the marker triangle kept its size (ruling out scale drift) — but distance alone can't tell you which way a shape is facing. A rotation and a reflection both preserve every distance in a triangle, so confirming congruence here is a necessary first step, not a final answer — it's exactly why D3 exists to test orientation specifically.*
- **D3 — A reflection test and quadrant map.** Plot all expected and actual marker coordinates from Appendix B on a coordinate plane in the rig's local axes, and label the **quadrant** each point falls in. For the marker Priya suspects is mirrored, compute where it *would* land if it were reflected across the rig's y-axis instead of rotated, and compare that predicted position to its actual scanned position. *Why a reflection prediction, not just a plot: reflecting a point across the y-axis has one precise algebraic signature (x flips sign, y stays the same) — computing that specific prediction and comparing it to a marker's actual scanned position is a direct, checkable test for orientation, which is the one thing D2's distance check can't see.*
- **D4 — A translation check.** Using only the two markers you determined in D2/D3 are *not* mirrored, set up and solve a system of two equations for the (Δx, Δy) translation offset between the expected and actual marker sets. Use that offset to predict where the third, suspect marker *should* land under a pure translation (no mirror) — and show how far off its actual scanned position really is. *Why only the two non-mirrored markers: a translation offset is only meaningful if it's built from points that actually moved by translation alone — including a mirrored point would corrupt the (Δx, Δy) you solve for. Two independent expected/actual coordinate pairs give you two equations for two unknowns, the standard way to pin down an unknown shift; applying that same offset to the third marker turns "translation fits these two" into a testable prediction you can compare against what actually happened.*
- **D5 — A registration-error-per-minute comparison, and a deadline check.** For Option A and Option B, state the registration error left in the file (in millimeters, from D2–D4) and the technician minutes each option costs (Appendix C), then compute the ratio of millimeters of error to minutes spent for each option. State whether Option B's manual pass finishes before the end-of-day deadline in Appendix C, showing your unit conversions. *Why a ratio rather than comparing error or time alone: the studio's real decision is whether the extra accuracy an option buys is worth the extra time it costs, which a millimeters-per-minute ratio expresses directly — and that ratio only matters if the option can actually be finished in time, which is why the deadline check has to run alongside it, not instead of it.*

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A: The Stanford 3D Scanning Repository

The reference geometry in this case comes from a real, live, publicly downloadable archive of laser-range-scanned 3-D models: the **Stanford 3D Scanning Repository**, hosted by the Stanford Computer Graphics Laboratory at **http://graphics.stanford.edu/data/3Dscanrep/**. It has published raw multi-pass range-scan data — the actual point clouds and reconstructed meshes researchers use as the standard test case for point-cloud registration and alignment algorithms — since the 1990s, and it remains online and downloadable today. Go to the link directly; do not rely only on the table below.

| Scan | Number of range-image passes | Total vertices in reconstructed mesh | Total triangles in reconstructed mesh | File format available |
|---|---|---|---|---|
| Stanford Bunny | 10 [S1] | 35,947 [S1] | 69,451 [S1] | .ply [S1] |
| Stanford Dragon | ~70 [S1] | 566,098 [S1] | 1,132,830 [S1] | .ply [S1] |
| Happy Buddha (for comparison only) | ~60 [S1] | 543,652 [S1] | 1,087,716 [S1] | .ply [S1] |

**Priya's studio is scanning a prop of comparable complexity to the Bunny — not the Bunny itself — but uses the Bunny's own published multi-pass structure as the documented example of exactly how a range scan is assembled from separate passes, and where a single flipped pass can enter the pipeline.** The Happy Buddha row is included only so you have a second real object's scale to compare against; you do not need it to complete any Challenge.

> *Source: Stanford Computer Graphics Laboratory, "The Stanford 3D Scanning Repository," graphics.stanford.edu/data/3Dscanrep/. This is a live, actively hosted academic data repository — go to the link and look at the actual files, not just this table, before you calculate anything.*

**D1 worked numbers — the Bunny's own real individual passes.** The Bunny's raw scan archive (the actual files behind the "10" in the row above) breaks down into these real per-pass point counts, which sum exactly to the repository's published raw total of **362,272 points** [S1]:

| Pass file | Raw points in this pass |
|---|---|
| bun000.ply | 40,256 |
| bun045.ply | 40,097 |
| bun090.ply | 30,379 |
| bun180.ply | 40,251 |
| bun270.ply | 31,701 |
| top2.ply | 38,298 |
| top3.ply | 36,023 |
| **bun315.ply (this case's stand-in "suspect pass")** | **35,336** |
| chin.ply | 37,738 |
| ear_back.ply | 32,193 |
| **Total** | **362,272** [S1] [S1b] |

Priya's own prop is not the Bunny, so no per-pass breakdown for *her* scan is published anywhere — it can't be, it isn't a real object. For D1, use **bun315.ply** as the real, published stand-in for "the pass Priya suspects is mirrored": a real Stanford Bunny range-scan file containing a real number of points, out of the Bunny's own real published total.

**On documented mirrored/symmetric-alignment artifacts:** Automatic point-cloud and photo alignment solvers are documented to settle into a self-consistent but geometrically wrong registration when a scene or object has symmetric or repetitive structure — the solver's own error metric can look fine while the pose is actually wrong, because the mismatched-but-similar-looking geometry still satisfies the metric. The Metashape Expert Manual, a community-maintained technical manual for one of the industry's major photogrammetry pipelines, documents this class of failure directly: symmetric and repetitive scenes are named as a root cause of alignment error, and manual markers/reference points are the documented remedy, though a badly-affected scene can defeat even many manual markers if the underlying match graph has already reinforced the wrong pose [S2]. That source does not use the specific words "mirrored" or "reflected," or the word "converged" — this case's own framing of the failure as a *reflection* specifically (rather than, e.g., a repeated-pattern 180°-rotation ambiguity, which is the form most directly documented) is a modeling choice, disclosed in Appendix E, made because reflection is the transformation this case's Challenges are built to test.

---

## Appendix B: Marker Point Log

Four markers were taped to the object before scanning began. Marker 4 was logged as a matter of studio routine and is not needed for any Challenge — the studio logs every marker on every job, whether or not that job turns out to need it.

| Marker | Expected coordinates (client reference model, rig's local axes, cm) | Actual coordinates (finished scan, same axes, cm) |
|---|---|---|
| Marker 1 | (6.10, 6.23) | (9.10, 8.23) |
| Marker 2 | (-5.38, 3.30) | (-2.38, 5.30) |
| Marker 3 (the suspect marker) | (-9.47, 12.42) | (9.47, 12.42) |
| Marker 4 (logged, not required) | (-1.75, 18.73) | (-1.75, -18.73) |

**Rig's own reported alignment error at export ("converged"):** 0.40 mm RMS.

> *Note: marker coordinates in this appendix are a scenario construction built for this case, positioned to be consistent with a real, documented photogrammetry failure mode (see Appendix A). They are not measurements from an actual client job. Methodology: each marker's **expected** coordinate is a real 3-D vertex pulled directly from the Stanford Bunny's actual reconstructed mesh data (`bun_zipper.ply`, the same 35,947-vertex file cited in Appendix A) — specifically, the mesh's extreme vertex in +x, −y, −x, and +y respectively, with only the (x, y) components kept (z dropped) and converted from meters to centimeters, rounded to two decimals, to give this case's 2-D rig-axes marker log. Markers 1 and 2's **actual** coordinates were then built by applying one real, consistent rigid translation, (Δx, Δy) = (+3.00, +2.00) cm, to their expected coordinates — a valid registration offset. Marker 3's actual coordinate was built instead by reflecting its expected coordinate across the rig's local y-axis (x → −x), with no translation — the mirrored-pass error this case is about. Marker 4's actual coordinate was built by reflecting its expected coordinate across the rig's local x-axis (y → −y) instead — a different mirror axis than the one applied to Marker 3. The rig's own reported 0.40 mm figure is a stated scenario value representing a plausible, misleadingly low self-reported error (SEE APPENDIX E for why it cannot be trusted at face value).*

---

## Appendix C: Studio Time and Deadline Constraints

| Quantity | Value |
|---|---|
| Time of day the rig reported "converged" | 4:40 PM |
| Client's end-of-day delivery deadline | 5:30 PM |
| Estimated technician time to manually re-register one marker by hand | 7 minutes |
| Estimated technician time to re-export and re-run the client's own registration check after a manual correction | 12 minutes |
| Technician time already spent on this job before the "converged" result | 90 minutes |
| Studio's estimated cost of a full re-shoot if a delivered file fails the client's downstream check | $8,500 |

> *Note: all figures in this appendix are stated scenario constraints for this case, disclosed as such — they set the studio's real-world time pressure without claiming to be a specific real company's numbers. The two per-marker/per-task minute figures are Modeling Assumptions grounded in real documented practice: manual marker placement in professional photogrammetry pipelines genuinely is a per-point task requiring the technician to locate and confirm the same marker's projection across multiple separate photos by hand (SEE APPENDIX E for the sourced basis) — no publicly published figure states exactly how many minutes this takes per marker for any studio, so a plausible value is assumed and disclosed rather than invented as fact.*

---

## Appendix D: Registration-Error Tolerance

| Quantity | Value |
|---|---|
| Client's stated maximum acceptable registration error for pipeline acceptance (mm) | 1.0 mm RMS — **MA1**, see Appendix E |

> *Note: `case-research` could not find a single publicly citable figure for "acceptable VFX/reverse-engineering photogrammetry registration tolerance in mm" at this exact specificity — but a real, published large-scale photogrammetric documentation project reports actual multi-scan registration point error in almost exactly this range: 0.9–1.3 mm mean point error across the project (up to 3.2 mm at the worst peripheral scan pairs), with cross-cluster target-based registration averaging 5.8 mm [S4]. This case's 1.0 mm client tolerance sits inside that real, measured range for professional photogrammetric work, rather than being invented from nothing — but a measured *error* is not the same thing as a stated client *acceptance threshold*, so it remains a disclosed Modeling Assumption — see Appendix E.*

---

## Appendix E: Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case author or by `case-research`, after a genuine search failed to find a publicly citable figure at the specificity this case needs. A Hero may challenge any of them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Client's maximum acceptable registration error | 1.0 mm RMS | No single public source states a general "VFX prop scan" registration *tolerance* (the maximum a client would accept). But a real, published large-scale photogrammetric reconstruction project (LIDAR + photogrammetry documentation of a cathedral interior) measured actual multi-scan registration point error of 0.9–1.3 mm across the project (up to 3.2 mm at the worst peripheral scan pairs) [S4] — this case's 1.0 mm client tolerance sits inside that real, measured range for professional photogrammetric registration work, rather than being invented from nothing. | If the tolerance were tightened below ~0.55 mm, even Option B's corrected residual (0.55 mm) would fail client acceptance — the manual recheck would not just catch the mirror, it would also reveal that "close enough by eye" isn't automatically "close enough for the client." Above ~0.55 mm, Option B passes comfortably; Option A's real (marker-derived) error of ~160.6 mm fails at any tolerance a client could plausibly state. |
| MA2 | Technician time to manually re-register one marker | 7 minutes | Manual marker placement in professional photogrammetry pipelines is a genuine, documented per-point task: the technician locates and confirms the same marker's projection across multiple separate photos by hand for each marker (Agisoft Metashape's own published guide: "adjust the marker position in several different images where the same feature is visible" [S3]). No public source states a minutes-per-marker figure for any studio, so a plausible value is assumed. | At 3 markers, this feeds directly into Option B's total minutes (Appendix C). If the true per-marker time were, say, 15 minutes instead of 7, Option B's minutes would rise from 33 to 57 task-specific minutes (123 → 147 total), which still fits Appendix C's 50-minute window only if some of that time overlaps or the deadline slips — a live classroom discussion point. |
| MA3 | Technician time to re-export and re-run the client's registration check | 12 minutes | Same basis as MA2 — a real, disclosed estimate for a real task, not a published figure. | A larger figure here tightens the Appendix C deadline check directly; the 50-minute window becomes the binding constraint before the ratio does. |
| MA4 | Rig's own self-reported "converged" error | 0.40 mm | Stated scenario value representing a plausible, misleadingly low self-reported error — a number the studio's software reports on its own, without checking it against the ground-truth markers. | Whatever a student's D5 ratio for Option A comes out to, it rests entirely on this one unverified number being trustworthy — worth asking what changes if it isn't. |
| MA5 | Manual-correction residual error after Option B | 0.55 mm | Stated scenario value for the small, real imprecision remaining after a careful hand-registration against three ground-truth markers — hand-placed markers are not perfectly precise even when they correctly catch a reflection. | See MA1's sensitivity note: this value sits just above the tolerance in MA1 only by design margin; if MA1 and MA5 were reversed in size the case would flip. |
| MA6 | Documented failure-mode framing (reflection specifically) | — | The Metashape Expert Manual [S2] documents symmetric/repetitive-pattern alignment failure and the marker-based remedy in a real, actively used photogrammetry pipeline, but does not use the words "mirrored," "reflected," or "converged." This case names the failure mode as a *reflection* because that is the transformation this case's Challenges are built to test (Appendix F); the general phenomenon (a solver settling into a self-consistent but wrong pose on ambiguous/symmetric geometry) is real and documented, but the specific "reflection across an axis" framing is this case's own modeling choice, not a verbatim-sourced claim. | N/A — this is a framing choice, not a numeric assumption, so it has no dilemma-flipping sensitivity of its own. |

---

## Appendix F: "How To…" Math Questions To Research

**Vocabulary**

Congruent · Similar · Quadrant · Coordinate Pair (also Ordered Pair) · Transformation · Translation · Rotation · Reflection · Scientific Notation · Ratio · System Of Equations

**How to…**

- How to reflect a figure across the Y-Axis
- How to find the distance between two coordinate pairs on a coordinate plane
- How to write a number in scientific notation given its standard notation
- How to find the percent of a number

---

## Appendix G: Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Stanford Bunny / Dragon / Happy Buddha scan-pass counts, reconstructed vertex/triangle counts, raw per-pass point counts, file format | Bunny: 10 scans, 35,947 vertices, 69,451 triangles, 362,272 raw points (bun000=40,256; bun045=40,097; bun090=30,379; bun180=40,251; bun270=31,701; top2=38,298; top3=36,023; bun315=35,336; chin=37,738; ear_back=32,193); Dragon: ~70 scans, 566,098 vertices, 1,132,830 triangles; Happy Buddha: ~60 scans, 543,652 vertices, 1,087,716 triangles; all distributed as .ply | Stanford Computer Graphics Laboratory — "The Stanford 3D Scanning Repository" ([link](http://graphics.stanford.edu/data/3Dscanrep/)) | page undated, actively maintained; range-scan data itself dated August 1996 per its own README | HIGH |
| S1b | Independent verification of S1's Bunny figures by direct download and parse of the primary data file (not just the summary page) | Downloaded `bunny.tar.gz` from the repository's own file server and parsed `bun_zipper.ply`'s header (35,947 vertices, 69,451 triangles — exact match) and all 10 raw `data/*.ply` file headers (point counts sum to exactly 362,272 — exact match) | Stanford Computer Graphics Laboratory ([link](http://graphics.stanford.edu/pub/3Dscanrep/bunny.tar.gz)) | accessed 2026-09-12 | HIGH |
| S2 | Documented alignment-failure class: automatic photogrammetric alignment can be defeated by symmetric/repetitive scene geometry, with manual markers as the standard remedy (used to ground, but not verbatim-match, this case's "mirrored pass reported as converged" framing — see Appendix E, MA6) | "Symmetries and repetitive patterns: building façades, tiled floors, agricultural row crops, brick walls" cause alignment problems; "Repetitive-feature scenes can defeat dozens of markers. When the false matches in the existing tie-point graph reinforce the wrong pose, even many manual markers may not override." | Photogrammetry Community — "Helping alignment when photos don't align: markers, references, and what to use when," Metashape Expert Manual ([link](https://photogrammetrycommunity.github.io/metashape-expert-manual/workflow/alignment/helping-alignment/)) | undated community-maintained manual | MEDIUM |
| S3 | Manual marker placement in a professional photogrammetry pipeline is a genuine per-point, multi-photo manual task (basis for MA2/MA3's technician-minutes assumptions) | "Place the marker across multiple photos – To improve accuracy, adjust the marker position in several different images where the same feature is visible." | Agisoft Metashape — "How to Place Markers in Agisoft Metashape: A Step-by-Step Guide" ([link](https://www.agisoftmetashape.com/how-to-place-markers-in-agisoft-metashape-a-step-by-step-guide/)) | published 2025-09-13 | MEDIUM |
| S4 | Real, measured multi-scan photogrammetric registration point-error figures from a professional large-scale reconstruction project, used as the sourced basis for MA1's 1.0 mm registration-tolerance assumption (no single figure exists at this case's exact specificity of a stated client *tolerance*) | Full-project mean point error 1.3 mm (max 3.2 mm at peripheral scan pairs); tighter core-area registration (28 scans) 0.9 mm mean point error; target-based cross-cluster registration mean distance error 5.8 mm | Kenely, Bugeja, Grima, Pullicino, Pullicino, Seychell — "Large-Scale Photogrammetric Documentation of St. John's Co-Cathedral: A Workflow for Cultural Heritage Preservation," arXiv:2604.24316 ([link](https://arxiv.org/abs/2604.24316)) | v2 posted 2026-05-14, accessed 2026-09-12 | HIGH |

*Every marker coordinate in Appendix B, every minute/time/cost figure in Appendix C, and the tolerance in Appendix D are either directly derived from S1/S1b (the Bunny's real mesh data) per the methodology note under Appendix B, or are disclosed Modeling Assumptions in Appendix E grounded in S2/S3/S4 — never invented outright.*

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
