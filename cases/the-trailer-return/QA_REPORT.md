## case-readiness run — 2026-09-09 (remediation pass)
**State:** BLOCKED → TIER2_PASS   **Verdict:** PASS

Remediated the two Tier 1 BLOCKERs from the prior run, rebuilt `published/` to match, ran all six
scripted Tier 2 probes plus P7's cold-read. See fixes summary at the bottom.

### Tier 1 — structural (21 checks)
| id | result | note |
|---|---|---|
| T1-01 | PASS | |
| T1-02 | PASS | POLISH: overview numerals auto-classified as texture: ['5', '15', '4', '4'] |
| T1-03 | PASS | |
| T1-04 | PASS | Fixed — leaked `<!-- FACILITATOR ONLY: ... -->` HTML comment removed from Challenge 5 in case.md; no facilitator-only content remains in the student-facing document. |
| T1-05 | PASS | |
| T1-06 | PASS | |
| T1-07 | PASS | POLISH: parsed 8 labels (8 bulleted, 0 from separator-run lines) |
| T1-08 | PASS | |
| T1-09 | PASS | |
| T1-10 | GAP | SPEC §8 — new_coverage[] empty; `reinforcement_note` carve-out present (already recorded pre-fix) and stands — spine has zero true gaps left, this case thickens an n=1 cluster instead. |
| T1-11 | PASS | |
| T1-12 | PASS | |
| T1-13 | PASS | Fixed — FACILITATOR.md fully rewritten with real `##` headings for the full MCS-14 anchor ladder (Intro, Launch, Anchor 1-4, Data Deep Dive, Twist, Close, Lessons Learned, Standards Touched On), Anchor 2/3 both precede Data Deep Dive, a named Twist with soundness check, a 7-row timed 45-minute Socratic plan naming the twist moment, and 5 single-line Socratic questions each ending in `?`. |
| T1-14 | PASS | Orphan number (80.0, from the old fabricated "80% of budget committed" twist) resolved by rewriting the Twist around a real, already-disclosed case fact (S6's own sourcing note: the $115/day hauling-fee basis is a consumer-vehicle rate, not a heavy-duty quote) instead of an invented budget figure. |
| T1-15 | GAP | Published docx/xlsx rebuilt from the fixed case.md/FACILITATOR.md (node md_to_docx.js, build_xlsx_generic.py) so staleness cleared. Remaining GAPs are pre-existing shared-tooling artifacts, not case content: (a) Data.xlsx README!A2 carries "2026-27" (the generic builder's year-range boilerplate) whose "27" reads as an orphan number; (b) the Facilitator Guide docx's 45-Minute plan rows ("30:00–45:00" etc.) aren't clock-time-stripped by the docx checker the way FACILITATOR.md's own T1-14 sweep is — a known asymmetry in `tier1_structural.py`, not a real data drift. Left as-is; fixing either requires editing shared pipeline scripts, out of scope for a single-case remediation pass. |
| T1-16 | PASS | case_md_sha256 updated in case.json.qa to match the current case.md hash. |
| T1-17 | PASS | |
| T1-18 | GAP | Interactive HTML's leaked 80.0 (same fabricated twist number) fixed by rewriting the Twist narrative and rebuilding the file's twist section + JS note text to match FACILITATOR.md; sha256 comment updated. Remaining GAP: `max="300"` on the fee-slider `<input>` (a UI control default, not case data) is still flagged as an orphan number — cosmetic, not a leak, left as-is per scope.
| T1-19 | PASS | |
| T1-20 | PASS | POLISH: no image/chart/diagram/map found — advisory only |
| T1-21 | PASS | |

**BLOCKER (0).**

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Worked the case directly from `case.md` only (no Guide Notes). D2's full-grid classification (34 odd vertices ⇒ neither a closed Euler circuit nor a 2-endpoint Euler path) is a one-line read of Appendix A's given odd-vertex count — no full-scale computation required. D3/D4 are genuinely hand-tractable: the 26-vertex/14-odd-vertex Practice Block with Appendix C's full pairwise distance table supports a real greedy nearest-pair strategy a student can execute by hand (e.g. O-R and Q-S pair for free at 0.0000 mi, A-B free, E-V at 0.0099 mi, L-M at 0.0227 mi, then J-K at 0.0335 mi, leaving F-U at 0.1293 mi — a workable, non-optimal-but-close closed-circuit pairing in a few minutes of arithmetic). D5 then uses Appendix D's *official*, already-computed full-grid figures rather than asking the student to run the 68-vertex matching themselves. **Tractability verdict: real, not asserted** — the Practice Block is an honest scaffold, not a token gesture; a diligent HS-entry student can reach a defensible D1-D5 with correct arithmetic using only what's in the document. |
| P2 both-sides | **PASS** | Both options have a genuine, defensible one-sentence pitch from the document alone: A — "$10.07/day and nothing else, no new vendor, no realistic payback on Option B's ~12x total"; B — "a real, reproducible 3.70% cut in the case's own primary metric (deadhead ratio), achieved by correctly relaxing the closed-circuit requirement to an open path." Neither side collapses outright; B's defense only holds if the student explicitly commits to the ratio as the decision lens (exactly the move the case's own trap is testing for), which is a legitimate, arguable position, not a bluff. |
| P3 trap | **PASS** | The most plausible wrong path (build D5, see Option A win ~12x on dollars, stop, never engage Option B's ratio argument) is the exact trap FACILITATOR.md names verbatim under "The trap" in the Data Deep Dive section. |
| P4 twist integrity | **PASS** | Re-derived the twist (the $115 hauling fee's consumer-rate basis) against every stated Modeling Assumption. It does not contradict MA4's own sensitivity note (Appendix F: "even at half this value... Option A's dollar dominance is robust to plausible variation in MA4") — the twist is deliberately a *confidence* twist, not a *flip* twist, and says so explicitly in the Guide Notes; it invalidates the position "the $115 figure is a solid, sourced number" without requiring any convention the case never states. |
| P5 sensitivity | **PASS** | Ran `sensitivity_model.py` ±50% on `trailer_fee` (the sole declared FLEX dial): winner stays B, margin stays 3.70% at both -50% ($57.50) and +50% ($172.50) — the deadhead-ratio metric the case's balance test is built on is untouched by the dollar-side assumption, which is the correct, disclosed behavior (see MA4's own sensitivity note). No flip, no breach of the 20% cap. |
| P6 data decay | **PASS** | Live-fetched all 5 cited URLs. S1 (afdc.energy.gov/data/10310): reachable, shows 5.2392 mpg for refuse trucks. S2 (eia.gov/petroleum/gasdiesel): reachable, shows $5.967/gal for week of 2026-09-07. S5 (bls.gov OEWS 53-7081): reachable, shows $22.99/hr mean wage, May 2023. S6 (towingservicehub.com): reachable, shows $75-150 hookup + $3.50-7.00/mi for 2026. S3 (overpass-api.de/api/interpreter): returns HTTP 400 on a bare GET with no query — expected behavior for this API endpoint (it requires a POST with an Overpass QL body), not link rot; every S3-derived figure is reproduced in-document per the case's own stated policy (Appendix G). |
| P7 accessibility (cold read) | **PASS** | Built the packet from the *published* Interactive HTML (not case.md) and read it fresh. Real-world vocabulary (hopper, flatbed, single-stream recycling, dead end) is glossary-linked via STORY_GLOSSARY hover terms. One issue found and fixed during this pass: the newly-authored Twist originally used unglossed jargon ("rear-loader truck", "heavy-duty rotator service") with no hover definition — reworded to plain language already used elsewhere in the case ("a truck the size and weight of Truck 4," "a bigger, more specialized tow rig") and rebuilt into both FACILITATOR.md and the published HTML. Re-read after the fix: 0 remaining real-world concepts that block proceeding (a "blossom-algorithm" mention and OEWS/Overpass-API citation abbreviations appear only in methodology/citation asides, not required to complete Challenges 1-5). |

**Tier 2 verdict: 7/7 PASS.**

### Tier 3 — human dry-run
NOT RUN — no `RUN_REPORT` filed yet; out of scope for this remediation pass.

---

### Fixes applied this pass
1. **T1-04 BLOCKER** — removed the leaked `<!-- FACILITATOR ONLY -->` comment from `case.md` Challenge 5. Its substance (nothing new — it only pointed at FACILITATOR.md/case.json, which already carry the balance argument and margin) needed no separate home.
2. **T1-13 BLOCKER** — `FACILITATOR.md` fully rewritten: real anchor-ladder headings, a tractable Anchor-3 worked example (the O/R vs. O/M Practice-Block pairing), a Twist grounded in the case's own already-disclosed S6 sourcing caveat (no invented numbers), a 45-minute timed plan, and 5 single-line Socratic questions.
3. **T1-10 GAP** — left as-is; the pre-existing `reinforcement_note` carve-out already satisfies SPEC's anti-padding doctrine (spine has zero true n=0 gaps left).
4. **T1-14/T1-15/T1-18 GAPs** — resolved the two real content-drift instances (the fabricated "80% of budget committed" twist number, which existed in both FACILITATOR.md and the published HTML). Rebuilt `published/*.docx` and `*.xlsx` from the corrected sources (`md_to_docx.js`, `build_xlsx_generic.py`) and hand-patched the Interactive HTML's Twist section/JS note text plus its sha256 comment, since this case has no `html_config.py` for the generic HTML builder (authoring one was judged excessive rework for this pass). Two small GAPs remain and are documented above as out-of-scope shared-tooling artifacts, not case-content problems: the xlsx README's "2026-27" year-range boilerplate, the docx plan table's un-stripped clock times, and the HTML fee-slider's `max="300"` UI default.
5. Updated `case.json.qa` (state, verdict, blockers_open, gaps_open, tier2 block, case_md_sha256) and `published/MANIFEST.json` (hash, byte sizes, note) to match.

**Skipped (documented, not fixed):** the T1-15/T1-18 shared-tooling number-extraction false positives described above — fixing them means patching `tier1_structural.py`'s docx/xlsx checkers or the generic build scripts project-wide, which is out of scope for a single-case remediation pass and was judged excessive rework per task instructions.
