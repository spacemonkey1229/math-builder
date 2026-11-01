# QA_REPORT.md — The Missing Hub

**Run date:** 2026-09-18
**case.md sha256:** `c367a1a9e97513ddac6672ef345fc72af1700893a6cfa6c6042e168c7b884d2c`
**state:** `TIER2_PASS`

---

## TIER 1 — STRUCTURAL

```
TIER 1 — STRUCTURAL   case: the-missing-hub   sha256(case.md)=c367a1a9e97513dd
checks run: 24   PASS 21 · GAP 3 · FAIL 0
VERDICT: TIER1_PASS  (0 blockers, 3 gaps)
```

| id | Check | Verdict |
|---|---|---|
| T1-01 | seven structural sections present | PASS |
| T1-02 | Overview length; no load-bearing numerals | PASS |
| T1-03 | Dilemma binary, opens "You are …" | PASS |
| T1-04 | Challenge boilerplate verbatim | PASS |
| T1-05 | Challenge numeral-form drift | PASS |
| T1-06 | every appendix referenced, no orphans | PASS |
| T1-07 | final "How To…" appendix, verbatim spine labels | PASS |
| T1-08 | every number cited or declared an assumption (visible Modeling Assumptions block) | PASS |
| T1-09 | balance test margin recorded, ≤20% cap | PASS (margin 0.00% — see Tier 2 P2/P5 for why this is a genuine, not manufactured, tie) |
| T1-10 | `case.json` schema + standards resolve in the spine | GAP — reinforcement carve-out. `new_coverage[]` is honestly empty; `case.json.reinforcement_note` records that both target skills were re-checked live at write time (still `n=1`, unraced by any concurrent session) and a whole-spine sweep found 0 skills at `n==0` anywhere — matching `the-hub-choice`'s and `the-parity-check`'s same-day findings. Downgraded from BLOCKER per the project's 2026-08-17 reinforcement-carve-out doctrine amendment. |
| T1-11 | learning-goal mutual reachability | PASS |
| T1-12 | tier vs. numeric load | PASS |
| T1-13 | facilitator guide + anchor ladder + twist + timed plan + sensitivity note | PASS |
| T1-14 | CONTINUITY — FACILITATOR.md agrees with case.md/case.json | GAP — 10 numbers in FACILITATOR.md's Robustness Check table and Socratic-question prose have no `case.json.derived` home (0.980769, 1.02, 5.375, 8.06, 11.0, 13.44, 16.13, 25.0, 128.8, 150.8). Same accepted class of pre-existing GAP as `the-hub-choice`'s and `the-parity-check`'s own T1-14 entries — guide-only derived figures (sensitivity-sweep outputs and Socratic-question arithmetic), verified by hand against `sensitivity_model.py`'s own printed output, not stale values. |
| T1-15 | CONTINUITY — published .docx/.xlsx agree and are not stale | GAP — same 10 numbers, same accepted class, now also present in the rendered Facilitator Guide docx (which renders FACILITATOR.md verbatim). Not a drift finding — the docx and the .md were rebuilt from the same source in the same pass. |
| T1-16 | QA hash currency | PASS |
| T1-17 | cohort-size bands declared | PASS — `case.json.cohort_bands[]` declares Full/Compressed/1:1 per SPEC §7.4 |
| T1-18 | interactive HTML present, fresh, leak-free | PASS |
| T1-19 | hover+hyperlink math glossary, verified domains | PASS |
| T1-20 | visual asset present | POLISH — no image/chart in the HTML; the live box-and-whisker plots (Step 3) are the case's visual, generated client-side, not a static image. Not required. |
| T1-21 | hover+hyperlink STORY-vocabulary glossary | PASS — `STORY_GLOSSARY` object, 5 real-world terms (ego-network, corresponding author, crawl, anonymized, network science), all links fetched and confirmed live (HTTP 200) this session, none on the math-glossary allowlist domains. |
| T1-22 | published HTML sections match case.md's | PASS |
| T1-23 | published HTML's inline `<script>` parses as JavaScript | PASS (`node --check` equivalent run manually via `new Function()`) |
| T1-24 | SVG connector lines reach their anchor shape | PASS |

**0 BLOCKERs.**

---

## TIER 2 — SIMULATED PLAY

P1–P4 and P7 were run as a genuinely fresh, zero-context subagent cold-read (given only
`case.md`, explicitly instructed not to open `FACILITATOR.md`, `case.json`, `QA_REPORT.md`, or
`RESEARCH_LOG.md`). P5 is fully machine (`sensitivity_model.py`). P6 (data decay) was verified
directly via live HTTP fetch this session (the QA sandbox note in the skill doc describes a
network-isolated environment; this session had live web access and used it directly).

| # | Probe | Verdict | Notes |
|---|---|---|---|
| P1 | Cold solve | **PASS** | Fresh subagent independently verified: known sum = 548, D1 reconstruction = 10.75×52−548 = 11 (plausible). Computed both options' mean/median/Q1/Q3 correctly using the median-of-halves method (A: mean=10.75, med=10, Q1=4, Q3=16; B: mean=10.745, med=10, Q1=4, Q3=16 — matching this case's own author-side computation exactly). Correctly determined neither dataset's max (34) exceeds the outlier fence (34), a non-obvious, correctly-derived result. Reached a defensible, reasoned recommendation (Option B, on the grounds that the numeric payoff of reconstruction is negligible while its risk is unverifiable) — a different but equally defensible position from Option A, exactly the intended "no single right answer" shape. Named the metric explicitly. |
| P2 | Both-sides solve | **PASS** | Fresh subagent built both arguments independently; neither collapsed. Specifically flagged that Option A's "reconstructed mean matches the last verified mean" argument is circular by construction (the formula solves for exactly that match) — a sharper, more precise version of this case's own named trap. Incorporated into FACILITATOR.md's Trap section verbatim as a strengthened trap description before this report was finalized. |
| P3 | Trap check | **PASS** | Fresh subagent, reading only `case.md`, independently named the trap: treating 34 (the visible max) as an "obvious" outlier without computing Q3+1.5×IQR, and/or treating Option A's tautological mean-match as proof of correctness. Both match/strengthen `FACILITATOR.md`'s recorded trap. |
| P4 | Twist-adjacent ambiguity check | **FOUND A DEFECT, FIXED** | No twist exists in `case.md` itself (twists are facilitator-only per this project's convention), so the probe instead checked for computational ambiguities in the student-facing data. Found one real ambiguity: the quartile method (Tukey/median-of-halves vs. linear-interpolation) was unspecified, and the outlier fence for this dataset sits razor-close to the max value (34 vs. fence 34.00) — a different quartile convention could change the outlier-plot answer entirely. **Fixed**: Challenge D2 now explicitly specifies the median-of-halves method. Also flagged two undefined jargon terms in Background ("corresponding author," "crawl") — **fixed** with brief in-line glosses, and both terms were also added to the published HTML's `STORY_GLOSSARY` (T1-21). |
| P5 | Assumption sensitivity | **PASS** | `sensitivity_model.py`, `FLEX=["cached_mean"]`. Base: A=0.980769, B=0.980769, margin 0.00% (structural TIE). Winner never flips across the full ±50% range (5.375–16.125) — confirmed by `tier2_probes.py`'s mechanical run (`flips: false` at both extremes) and by a wider 0×–3× stress test in the model's own `__main__` block. The metric is provably independent of `cached_mean`'s value by construction (see the model's module docstring for the earlier, failed design and the retuning that fixed it — recorded in `RESEARCH_LOG.md`). |
| P6 | Data decay | **PASS** | Both `sources[]` URLs fetched live this session: S1 (`https://snap.stanford.edu/data/ego-Facebook.html`) returns the dataset's stated structure (10 ego-networks, 4,039 total nodes). S2 (`https://snap.stanford.edu/data/facebook.tar.gz`) was downloaded directly (`curl`, HTTP 200) and `facebook/3980.edges` was parsed with Python to compute every figure in Appendices A–C directly from the raw file — the strongest possible P6 verification (not a cached page summary, the actual primary data file). The five `STORY_GLOSSARY` links (T1-21) were also each fetched and confirmed HTTP 200 this session (one candidate URL, `Ego_network`, 404'd during verification and was replaced with the confirmed-working `Social_network` article before shipping). No dead links, no figure found to have moved or changed. |
| P7 | Accessibility cold-read | **PASS (with fixes applied)** | Fresh subagent named 2 real jargon gaps ("ego-network" was already explained in-context; "corresponding author," "crawl," "program committee" were not) — addressed via in-line glosses (P4 above) and the `STORY_GLOSSARY`. Confirmed D3's box-and-whisker deliverable has sufficient given data (Appendix B's frequency table gives every raw value needed; min/max/quartiles all derivable). Confirmed the Overview carries zero load-bearing numbers and the case never reveals the "correct" answer, margin, or winning option anywhere in `case.md`. |

**0 FAIL, 0 NOT RUN.** Two genuine defects were found by the cold-read (P4's quartile-method
ambiguity, P7's jargon gaps) and both were fixed in `case.md`/the published HTML before this
report was finalized — this is the pipeline working as intended, not a corner cut. `case.md`'s
hash was re-verified current (`c367a1a9e9...`) after these fixes, before this report's Tier 1
re-run above.

---

## Balance test

- **Primary metric:** share of the friend circle's 52 members whose reported degree count is
  fabricated-or-missing (not an exact, known value), per option
- **Margin:** 0.00% — a genuine, provable structural tie (both options always compromise exactly
  1 of the circle's 52 members: an estimate vs. an absence), confirmed independently by Tier 2 P1
  and P2
- **Both options genuinely defensible:** confirmed independently by Tier 2 P1 (fresh solver chose
  B) and P2 (both sides hold up; A's naive "reconstruction confirms itself" argument is circular
  but its honest form — "we keep the true member count" — still stands)

## Sign-off

- 0 BLOCKERs (Tier 1)
- 0 FAIL, 0 NOT RUN (Tier 2, all 7 probes recorded)
- GAPs: T1-10 (reinforcement carve-out, documented), T1-14/T1-15 (guide-only derived numbers,
  pre-existing accepted class per `the-hub-choice`/`the-parity-check` precedent)

**VERDICT: TIER2_PASS.** Case may proceed to `case-publish` (packet-only, per task scope — the
shared read-model is deliberately not written by this batch).

---

## Live browser audit (Stage 5)

Opened the built Interactive HTML in a real browser via a local HTTP server (not `file://`, which
blocks `localStorage`). Clicked through every tab (Overview, Background, The Dilemma, Challenges,
Appendices, Working Notebook, Twist), exercised the Dilemma pick widget, the D1–D4 Check buttons
with both correct and slider-extreme inputs, the Twist reveal, and the Real-World Vocabulary
glossary hover/click. Found and fixed two real defects:

1. **The "Assumed cached mean" slider's live value label was rendering entirely off-screen** at
   narrow (mobile, ~436px) viewport widths. Root cause: `input[type=range]` carries a browser
   intrinsic minimum width that does not shrink under `flex:1` inside a narrow flex row without an
   explicit `min-width:0`, so the row overflowed its container and pushed the value span (and part
   of the slider itself) past the visible viewport edge — confirmed via `getBoundingClientRect()`
   (`.val` right edge at x=486 inside a 436px-wide viewport). **Fixed**: added `min-width:0` to the
   slider input, `flex-wrap:wrap` to the row, and `margin-left:auto` to the value label so it wraps
   to its own right-aligned line on narrow screens instead of clipping. Re-verified visible and
   correctly updating (0.00 → 52.00 across the full slider range) at the same narrow viewport width
   after the fix.
2. **The box-and-whisker plot used a fixed 0-based horizontal scale**, so an extreme (unrealistic
   but reachable) slider value — e.g. `cached_mean = 0`, giving a reconstructed value of −548 —
   produced whisker lines with negative x-coordinates that rendered off-canvas, clipped invisibly
   by the SVG `viewBox`. **Fixed**: the chart's scale is now domain-aware (computed from the actual
   min/max across both datasets, not assumed to start at 0), so the plot stays on-canvas — though
   still visually compressed — at any slider value, including deliberately extreme ones a curious
   Hero might try.

Both fixes are CSS/JS-only; no case data, source, or computed figure changed. `case.md`'s hash is
unaffected (`c367a1a9e9...`, unchanged) — only the published HTML was touched, and was rebuilt
fresh after both fixes. Re-ran `tier1_structural.py`: unchanged `TIER1_PASS`, same 3 accepted GAPs
as before the audit.

**Verified working correctly**, with real interaction (not just static read): D1's Check button
(entered `11`, got a green ✓ against the live-computed expected value); D2/D3's live-drawn box
plots matched hand-computed quartiles exactly (Q1=4, median=10, Q3=16 for both options at the base
assumption); D3's outlier dropdowns validated correctly against the computed outlier sets; D4's
comparison button reproduced this report's own hand-verified drift figures exactly (Option A:
0.000%, Option B: 0.046%); the Twist reveal button worked and disabled itself after use; the
Dilemma pick widget correctly highlighted the chosen card and updated the header pill
(`Current pick: A`); the Real-World Vocabulary glossary rendered all 5 terms with working
hover tooltips and click-through links; zero browser console errors throughout.
