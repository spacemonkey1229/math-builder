# RESEARCH_LOG.md — Electoral College

72 `{{NEEDS_SOURCE}}` placeholders from `case-write`. All resolved: 62 `SOURCED`, 10 `ASSUMPTION`,
0 `OPEN`, 0 `DROPPED`. Zero placeholders remain in `case.md`.

## Group 1 — Electoral vote counts (51 placeholders: 37 contested states + 9 Peaken-locked + 5
Farnsworth-locked, plus the 270/538 threshold in Appendix A)

**Searched:** National Archives Electoral College allocation page.
**Found:** `archives.gov/electoral-college/allocation` — current apportionment (post-2020 Census,
in effect through the 2032 reapportionment), 538 total electoral votes, 270 to win. Fetched the
full state-by-state table and cross-checked every one of the 51 jurisdictions this case names.
**Result:** SOURCED, confidence HIGH, cited as **[S1]**.
**Integrity check:** the 37 contested-state EVs (450) + the 9 Peaken-locked (50) + the 5
Farnsworth-locked (38) sum to exactly 538 — confirms the original case source's own map matches
the real current apportionment exactly, including Nebraska at 5 (the pie chart's "(2)" label in
the source docx's embedded image appears to reference only Nebraska's 2 statewide electors, not
its full 5; this case treats Nebraska as winner-take-all like the other 49 states/DC, a stated
simplification noted in Appendix C, since Nebraska is one of only two states that splits electors
by congressional district in reality, and modeling that split is out of scope for this case's math).

## Group 2 — Challenge 1 resource links (video + article, Appendix A)

**Searched:** "How the Electoral College Works" video (matching the original source docx's own
named resource); "What Is the Electoral College?" article (same).
**Found:** CGP Grey's "How the Electoral College Works" (youtu.be/OUS9mM8Xbbw) — title corroborated
by multiple independent search listings, though a direct fetch of the creator's own blog page
(cgpgrey.com/blog/how-the-electoral-college-works.html) 404'd, so the YouTube URL is cited
directly and the source is graded MEDIUM rather than HIGH for that reason. The National Archives'
own "What is the Electoral College?" page (archives.gov/electoral-college/about) was fetched
directly and confirmed to match the original source's second named resource — graded HIGH.
**Result:** SOURCED, cited as **[S2]** and **[S3]**.

## Group 3 — Census Bureau demographic lookup tool (Appendix D)

**Searched:** current official US Census Bureau demographic data search tool, matching the
original source's own screenshot of a state/county/zip search bar.
**Found:** census.gov/quickfacts — real, matches the source's screenshot. A direct fetch of a
specific state's QuickFacts page returned an automated bot-protection block (HTTP 403); this is a
site access artifact, not a sign the tool doesn't exist, so the general QuickFacts landing page is
cited instead of a deep link.
**Result:** SOURCED, confidence MEDIUM, cited as **[S4]**.

## Group 4 — Campaign budget and travel-cost figures (Appendix E: total funds, ad-spend split,
remaining travel budget, flat per-state fee, per-half/full-day visit cost)

**Searched:** whether any real, dated, primary source could substantiate these exact dollar
figures for a *specific* fictional 2044 campaign. There is none — the scenario is fictional and
in the future, so by definition no primary source can exist for it.
**Result: NOT FOUND as citable facts.** Per SPEC §5, exit chosen: **stated Modeling Assumption**
(MA1, MA2), carried forward verbatim from the original case source document (these are the
scenario's own internal design numbers, not invented by this conversion).
**Grounding search performed anyway** (to check the *magnitude* is realistic, not to source the
figure itself): searched real 2024 presidential campaign final-stretch spending. Found NBC News
reporting that one real 2024 campaign spent $129M/month on media, $45.5M/month on event
production, and $2,626,110 in a single month on private flights alone. This confirms the case's
$19M-total/$16M-ad/$3M-travel weekly split and its ~$200K-$500K per-visit cost figures sit
comfortably inside real order-of-magnitude campaign spending, rather than being an arbitrary
invented number. Cited as grounding, not as the source of the figure, as **[S5]**.
**Result:** ASSUMPTION (MA1 total/ad-split/travel-budget; MA2 per-state/per-visit costs).

## Group 5 — Undecided-voter swing rate (Appendix E: 2 percentage points per half-day)

**Searched:** political-science research on the real persuasion effect of a presidential
candidate's in-person campaign visit on state-level polling.
**Found:** Wisconsin Public Radio's "Presidential candidate visits rarely gain votes," summarizing
academic research (including Christopher J. Devine's work) — real effects exist but are modest,
concentrated among undecided/independent voters, and **no research consensus gives a fixed
percentage-point figure**. This directly supports treating the case's own fixed "2 points per
half-day" as a deliberately clean, stated Modeling Assumption rather than a real, precisely
measured number — the honest finding from real research is that no such precise number exists.
**Result:** ASSUMPTION (MA3), grounded by **[S6]**, NOT presented as sourced fact.

## Group 6 — Contested-state and national demographic polling data (Appendices C, D)

**Searched:** n/a — a 2044 election has not happened, so by construction no real poll can be
found for it. This is the case's own fictional scenario data, extracted directly from the original
source docx's embedded pie-chart and table graphics (which are not machine-readable text, so were
extracted as images and read directly).
**Result:** ASSUMPTION (MA4), carried verbatim from source. **Data-integrity finding, disclosed
rather than corrected:** re-transcribing Appendix D's national demographic table, every column
reconciles to 99-101% except "White" (Farnsworth 49% + Peaken 55% + Not sure 12% = 116%). This is
most likely a transcription artifact on this conversion's part (the source image is a small,
compressed table) or an inherited error in the original source document itself — it could not be
resolved with certainty from the available image, so it is flagged in Appendix F rather than
silently adjusted to make the arithmetic work. A future editing pass with a higher-resolution
source scan should re-verify this one column.

## Balance / sensitivity verification

Built `sensitivity_model.py` to compute, for each of the two locked strategies (literal execution),
the electoral votes securable within the $3,000,000 travel budget. Base case: Strategy A reaches
296 EV ($3.0M spent), Strategy B reaches only 242 EV ($2.0M spent, falls short of 270) — **margin
18.24%**, inside SPEC §2's ~20% band. Ran the mandatory ±50% flex on the two most load-bearing
assumptions (MA2 per-visit cost, MA3 swing rate); margin ranged ~11%-18% across all four flexed
runs and Strategy A won every single run — the *direction* never flipped, only the margin's size,
which is the correct sensitivity signature (see FACILITATOR.md for the full table and the
"smart B" counter-example that does reach 270).

## Summary table

| Placeholder group | Count | Status | Confidence | Citation |
|---|---|---|---|---|
| Electoral vote counts + 270/538 threshold | 51 | SOURCED | HIGH | S1 |
| Video explainer | 1 | SOURCED | MEDIUM | S2 |
| Article explainer | 1 | SOURCED | HIGH | S3 |
| Census Bureau tool link | 1 | SOURCED | MEDIUM | S4 |
| Campaign budget / travel-cost figures | 7 | ASSUMPTION (MA1, MA2) | grounded MEDIUM | S5 |
| Undecided-voter swing rate | 1 | ASSUMPTION (MA3) | grounded MEDIUM | S6 |
| Contested/demographic polling data + rounding-check stub | 2 | ASSUMPTION (MA4) | n/a (fictional) | source docx |
| Appendix F meta-note | 1 | SOURCED (resolved by this log) | — | — |
| Sum-of-subtotal cells (9-state, 5-state) | 2 | SOURCED (derived from S1) | HIGH | S1 |

**Next step:** `Run case-readiness on electoral-college.`
