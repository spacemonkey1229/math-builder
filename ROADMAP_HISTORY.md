# Roadmap — Math Builder — full narrative history

> **This is the archive, not the working roadmap.** It's the complete version-by-version delta
> log — every decision, every correction, every "why," in full prose, oldest reasoning preserved
> per this project's append-only rule. It is long and it is not meant to be read top to bottom.
> **For "what's done / what's next," read [`ROADMAP.md`](ROADMAP.md) instead** — it's the short,
> table-based status page. Come here only when you need the reasoning behind an entry in that
> table, or the full story of how a number got to where it is.

---

**v2.13 · 2026-08-24.** Supersedes v2.12. **Delta: re-ran the live build scripts
(`app/build_pipeline.py`, `app/build_legacy_readiness.py`) rather than carrying forward v2.12's
numbers, and found the #1 flagged item from v2.12 already resolved.**

**0. The 10-mis-published-cases issue flagged in v2.12 is resolved.** `archery-camp`,
`baseball-lineup`, `cardiology`, `catering`, `house-plans`, `lebron-vs-michael`, `nuclear-waste`,
`phone-plan`, `rent-vs-own`, `robotics-engineer` all now carry `qa.state: "TIER2_PASS"` in their
`case.json`, each with an individual fix recorded in its own `QA_REPORT.md` (e.g. `archery-camp`'s
report shows a P3 probe re-run plus a `new_coverage[]` collision fix, both dated 2026-08-22). This
happened in a prior session not narrated here in detail — this entry records the state as found,
not the work of fixing it.

**1. `the-multiplier-recruit`, `the-reserve-asymptote`, and `roofline-call` have all cleared the
gate and published** since v2.12 — the three items that were "written, not yet promoted" or "not
yet written" in the last refresh's Geometry/Pre-Calc gap tracker. Pre-Calc Matrices and Intro to
Limits, and Geometry Fundamentals, are now closed.

**2. Live re-scan numbers, `2026-08-24`:** `stage_counts` from `readmodel/pipeline_status.json` —
`promotion: 80` (published), `drafting: 7` (`alert-curve`, `bioreactor-bid`, `compute-lease`,
`cooling-curve`, `downbeat-split`, `enclosure-call`, `placement-test` — all newly authored this
session, not previously tracked in this file), `research: 1` (`fret-board`, has a `RESEARCH_LOG.md`
started), `concepting: 9` (includes a fresh sheet, `CONCEPTS_pim-sector-gaps_2026-08-24.md`, a
14-item career/industry-gap batch scoped this session but not yet approved into a written case).
Polar & Parametric and Trig Identities remain unwritten — their concept sheets were touched this
session (minor edits) but no case directory exists for either yet.

**3. Two housekeeping items from the v2.12 table were stale and are now dropped:** the
"`build_dashboard.py` fix / `00_SESSION.md` note sitting uncommitted" line — both files were
committed in `a536a7a` and `5b4742a` respectively, well before this pass; there was nothing left to
decide.

**Not done in this pass:** the #1 blocker is unchanged — 0 cases have ever run with a real
learner, and `app/student-moksh-atit.html` is still local-only, not pushed to the live site. Both
carry forward as the top priorities into v2.13's `ROADMAP.md`.

---

**v2.12 · 2026-08-19.** Supersedes v2.11. **Delta: v2.11 was a numbers-only touch-up and the user
correctly called it inadequate — it never checked whether the tool producing those numbers was
telling the truth, and it left the file's own "current state" table nine days stale under a
heading that says otherwise.** Three real problems found and two fixed:

**0. The most important finding in this pass: 10 currently-`published` cases violate the
project's own publish gate (MCS-41/D-020) right now, live, undetected until this pass ran the
gate script that exists specifically to catch it.** `python3 scripts/apply_publish_gate.py`
(dry-run, the safe default — nothing written) reports `10 case(s) to demote`: `archery-camp`,
`baseball-lineup`, `cardiology`, `catering`, `house-plans`, `lebron-vs-michael`, `nuclear-waste`,
`phone-plan`, `rent-vs-own`, `robotics-engineer` — every one is `status: "published"` with
`qa.state: "TIER1_PASS"`, no `sensitivity_model.py`, no `QA_REPORT.md`. D-020's own rule, written
down after the *first* time this exact thing happened (the Aug 4–5 batch, ten different cases):
`published` requires `TIER2_PASS` or better, because a case with no sensitivity model has never
had its verdict tested against a ±50% swing of its own stated assumptions (MCS-26), and that is
the specific failure this pipeline exists to prevent a real cohort from receiving. **These ten are
currently assignable to a real learner in the live app right now** (`admin_core.py` gates on
`status in ('published', 'legacy')`, not on `qa.state`). Not caused by this pass — these are 10 of
the 49 in the `promotion` stage count every version since v2.10 has reported without anyone
running the one script that checks *why* a case is in that bucket. **Not demoted in this pass**:
running `--confirm` changes what a facilitator can currently hand a real student, which is a
live-app content decision, not a local build-script regen — flagged here for a human call, not
executed. See Sequencing → As of v2.12, now the #1 item, ahead of A3.

**1. `build_pipeline.py`'s concept-sheet parser was silently dropping 7 real, unwritten
concepts — a genuine tooling bug, not a stale-data problem.** `CONCEPT_HDR`'s regex required
exactly one space around each `·` separator (`" · score "`); `cases/_concepts/
CONCEPTS_next10-careers-gapclose_2026-08-18.md` — the sheet C1/C3/C5 (Grant Reach, The Multiplier
Recruit, The Reserve Asymptote) were written from — formats its headers with three spaces
(`"   ·   score   ·   tier"`), so every one of its ten `### C` headings failed to match and the
sheet's remaining 7 unwritten concepts (C2, C4, C6, C7, C8, C9, C10) were invisible to the
Pipeline tab's `concepting` count and to `pipeline_status.json.concepts[]` — verified by importing
`parse_concept_sheets()` directly and diffing its output against a manual read of the sheet.
**Fixed**: `CONCEPT_HDR` now tolerates `\s+` around each separator instead of a literal single
space ([app/build_pipeline.py:59](app/build_pipeline.py:59)). Re-ran `python3 app/
build_pipeline.py` (writes, not `--verify`, since the fix itself makes the cached file stale) —
`concepts (not yet written)` went **2 → 9**, `concepting` stage **25 → 32**. `python3 app/
build_dashboard.py --verify`: still 180 checks, same 3 pre-existing failures, nothing newly broken.

**2. Three concepts this file already told two sessions in a row to "write next" were written on
2026-08-18 and never recorded here.** `cases/grant-reach/`, `cases/the-multiplier-recruit/`, and
`cases/the-reserve-asymptote/` all exist, all carry `case.json.status: "researched"` with a real
`RESEARCH_LOG.md`, `authored_on: "2026-08-18"` — the same date as v2.10 itself, which nonetheless
still recommended writing them as if they hadn't started. Neither `DECISIONS.md` nor
`DOCTRINE_LEDGER.md`'s change log has an entry for this authoring — it happened in a session this
file's own append-only trail never captured. All three sit in the `research` stage now, next
action `case-readiness` (Tier 1) — genuinely the front of the queue, not "write C5 first" (which
v2.10 and v2.11 both still said).

**3. Not fixed, flagged for a human: `cases/_concepts/CONCEPTS_precalc-calculus-discrete_
2026-08-01.md`'s own C9, "Redrawing the Lines," may be the same case as the already-published
`cases/redrawing-lines/` under a near-identical title, or may be a legitimately separate second
redistricting case.** The two are not obviously the same: the published case's `new_coverage[]`
closed Discrete Mathematics / Proof And Recursion (per v2.10's own finding), while this concept's
own sheet entry targets Combinatorics (`fundamental-counting-principle`, a binomial-coefficient
how-to) — different skill group, so it is *not* mechanically redundant the way next10's own C9
("Prove It Scales," same sheet-collision pattern, already correctly marked moot in v2.10) was.
But a redistricting-analyst protagonist choosing between two districting standards is close enough
to what a case titled `redrawing-lines` would plausibly already be doing that this needs an actual
read of both `case.md`s before anyone authors it, not an assumption either way from this pass.

**Verified fixed, not just re-asserted: C5 ("fix the orphan override record") no longer
reproduces.** Checked `readmodel/score_overrides.json`'s 4 records against `readmodel/
submissions.json.scores[]` directly — the only one that fails to resolve is the file's own seeded
`_example: true` placeholder record (labeled as an example, not live data); all 3 real overrides
resolve cleanly. Track C's item is marked ✅ below. Caveat stated plainly: this checks the local
`readmodel/` mirror per `TECH_STACK.md`'s own boundary (only 4 docs are runtime-mutable in
Postgres, and this file suggests scores/overrides are among the local ones) — it does not query
the hosted Postgres store directly, so if the live app's own write path can produce an orphan this
check would not catch it.

**Also refreshed, not just re-derived a second time: `readmodel/domain_coverage.json`
regeneration from v2.11 is unaffected by any of the above** (concept-sheet parsing and domain
mapping are unrelated code paths) — its numbers stand as v2.11 reported them.

See the corrected **"Where things actually stand"** table and the new **"Current pipeline"**
section below (both dated 2026-08-19, both replacing what the stale versions were quietly
contradicting) for the full current numbers, and **Sequencing → As of v2.12** for the corrected
next-action order.

---

**v2.11 · 2026-08-19.** Supersedes v2.10. **Delta: no new case work since v2.10 — this pass is a
truthfulness refresh, not a content pass.** Re-derived every number in this file from a live script
run rather than trusting v2.10's snapshot (per `00_SESSION.md`'s own rule). Pipeline totals are
unchanged: `python3 app/build_pipeline.py --verify` → `concepting` 25, `drafting` 2, `research` 3,
`readiness` **0**, `promotion` **49**, `verified` **0** — matches v2.10's ending state exactly, so
the ten-case backfill that pass closed stayed closed.

**Closed the one open item v2.10's own sequencing named as next (#4): regenerated
`readmodel/domain_coverage.json`.** It had been flagged stale in v2.10 (`spine_skills_uncovered:
199` there vs. the spine's real 73) but not fixed, out of scope for that pass. Ran
`python3 app/build_domains.py` (dry-run first, 40 domains / 12 clusters / 154 URLs all still
fetched-live, 0 knowledge-only) then the real write; `python3 app/validate_domains.py`: 28/28.
`domain_coverage.json.totals.spine_skills_uncovered` now reads **73**, agreeing with the live
spine for the first time since B2. Side effect worth naming honestly: `uncovered_skills_still_
orphaned` moved from 92 to **51** purely from re-deriving against the corrected uncovered set, not
from any new domain-authoring work — the orphaned-skill *count* changed, the underlying skills
gap did not.

**Found, not caused, in the same pass: two files were already sitting modified in the working
tree from unfinished prior work, neither committed nor documented anywhere.** `app/
build_dashboard.py` carries a real fix — `build_data()`'s corpus-linking loop was resolving a
reconciled legacy case's `case.json`/`published/`/pipeline-doc links off the corpus record's
frozen original `path`, instead of the reconciled `cases_index.json` record's own (post-conversion)
path, so a legacy title reconciled into the pipeline could silently lose its own asset links; the
fix (and the matching `--verify` self-check) now prefers the reconciled path. Re-ran
`python3 app/build_dashboard.py --verify` to confirm: **180 checks, 3 failed** — down from the 4
pre-existing failures v2.10 recorded, because this fix closed the `derived skill ids match
cases_index standards_count` check without anyone touching it this pass. The 3 that remain are
the same pre-existing drift v2.10 already named and none are new: `legacy_readiness` case count vs.
`corpus_index` legacy count (45 vs. 63), the same 2-cluster B2 backlog (`Calculus`/`Derivatives`,
`Discrete Mathematics`/`Formal Logic`), and legacy cases carrying `margin: 0` instead of `null`.
Separately, `00_SESSION.md` carries an uncommitted addition declaring a `library` governance tier
(R34, dated 2026-08-18) — appears to be `Best Practices`-side work, not something this pass made or
verified. **Neither of these two files' changes were authored in this pass and neither is
committed** — flagged here so the next session doesn't mistake "sitting in the working tree" for
"done," and doesn't lose the `build_dashboard.py` fix to an accidental `git checkout`.

**The blocking fact is completely unchanged: no case is `VERIFIED`.** The pool of genuinely
`TIER2_PASS`/`published` candidates is still 15 (v2.10's close). This pass touched only the
read-model's own honesty (`domain_coverage.json`), not case content, case count, or coverage.

`readmodel/domain_coverage.json.totals`: `spine_skills` 437 (unchanged), `spine_skills_uncovered`
73 (was stale at 199), `uncovered_skills_now_reachable_from_a_domain` 22 (was stale at 107),
`uncovered_skills_still_orphaned` 51 (was stale at 92) — all now agree with the live
`standards_spine.json.totals` (`skills` 437, `cases` 71, `uncovered` 73).

---

**v2.10 · 2026-08-18.** Supersedes v2.9. **Delta: the ten cases sitting in the pipeline's
`readiness` stage were re-verified against the actual gate scripts rather than trusted at their
self-reported `case.json.qa` state, and all ten are now genuinely `TIER2_PASS`/`published`.** Five
had already reached that bar in a prior session (`a-coachs-dilemma`, `codebreaker`, `cold-chain`,
`end-of-life`, `seton-hall`) and were re-verified clean, not re-worked. The other five needed real
fixes before the claim was true, not just a status flip:

- **`airplane-manufacturer` and `family-trip`** were `BLOCKED` on live re-run (`T1-15`/`T1-18`
  CONTINUITY STALE — their `published/*.html` predated the last edit to `case.md`). Both were a
  genuine staleness, not a content defect: a prior session had moved facilitator-only content out
  of the student-facing `case.md` into `FACILITATOR.md` (correct, per the "never ship the answer in
  the student packet" rule) without regenerating the HTML afterward. Rebuilt/re-verified and both
  cleared `TIER1_PASS` (0 blockers) again. `family-trip` additionally had a stale `qa.case_md_sha256`
  (T1-16) and a real, small propagation bug caught while rebuilding its packet: the Overview still
  said Allegiant's lap-child policy is "one per adult" after Appendix D and `case.json` had already
  been corrected to the airline's real rule ("one per row") — the same class of single-line
  propagation miss `seton-hall`'s own QA history already named once. Fixed in `case.md` and the
  interactive HTML both.
- **`family-trip` itself was only `TIER1_PASS`** at the start of this pass — no full Tier 2 run had
  ever been recorded, just a standalone mechanical P5. Ran the other five probes for real (a
  genuinely fresh subagent for P1 and a second one for P3, direct work for P2/P4, live fetches of
  all 10 web sources for P6). P6 found two real, load-bearing defects: `S8`'s URL was a dead
  third-party mirror and the case's stated policy text was itself wrong (Allegiant's real rule is
  "per row," not "per adult" — the same fact as above, caught twice from two directions); `S12`
  resolved but backed the wrong IRS mileage-rate announcement (72.5¢, not the case's cited 76¢) —
  the 76¢ figure itself was correct, re-pointed to the announcement that actually states it. Both
  fixed. `family-trip` reached genuine `TIER2_PASS` with 0 real FAIL (P5 stays PASS-disclosed, the
  project's standing state for a stated-assumption instability that's written down rather than
  hidden — the same treatment `wildfire`/`airstrike` already use).
- **`airstrike`, `wildfire`, `redrawing-lines` were already genuinely `TIER2_PASS`** on arrival —
  their `QA_REPORT.md` files record real fresh-subagent P1/P3 runs, real live P6 fetches, and (for
  `airstrike` and `wildfire`) real defects that a prior pass found and fixed before the probes
  actually passed (a leaked trap-detector-defeating wording, a `FLEX` sweep that was a structural
  no-op and vacuously "passed" P4/P5 against parameters `evaluate()` never reads). No rework needed;
  re-verified live and left alone.
- **All four `qa`-status cases plus `family-trip` were promoted through `case-publish`**: built the
  missing packet files (student `.docx`, facilitator-guide `.docx`, `.xlsx` workbooks where the
  appendices warranted one, `MANIFEST.json`) for whichever were missing — `redrawing-lines` had
  **no `published/` directory at all** and needed its interactive HTML built from
  `templates/interactive_shell.html` from scratch, the project's first real proof that the A7
  scaffold works for a case authored after Cold Chain. Every rebuilt student `.docx` was rendered to
  PDF and read to confirm no facilitator content (the trap, the balance arguments, the margin)
  leaked across — 0 leaks found across all five packets. Promoted each to the read-model
  (`standards_spine.json`/`cases_index.json`/`gap_queue.json`) and flipped `case.json.status` to
  `"published"`.

**A real regression was found and fixed in the read-model itself, not in a case.** After all five
promotions, `standards_spine.json.totals.uncovered` read 76 — down only 5 from the 81 measured at
the start of this pass, when the eight individually-verified newly-closed skill ids
(`geometry-vertex`/`concave`/`irregular-polygon`/`quadrilateral` from `airplane-manufacturer`;
`discrete-mathematics-base-case`/`mathematical-induction`/`inductive-step`/its how-to from
`redrawing-lines`) should have moved it by 8. Diffing the promotion script's own
`readmodel/_snapshots/` (its safety net, working exactly as designed) found the cause: the
`family-trip` promotion's write — which should have been a pure no-op, since `family-trip`'s title
was already in `standards_spine.json.cases[]` from the original pre-pipeline corpus scan and its
own `case.json.new_coverage[]` is empty — instead **silently stripped `airplane-manufacturer` from
62 skills' `covered_by[]` and `wildfire` from 77**, cutting their broad legacy-scan-era tagging down
to only their narrow, freshly-curated `standards[]` claim (97→35 and 92→15 respectively). This
pattern — a legacy-converted case keeping both its old broad corpus-scan tag *and* its new curated
claim — is normal and matches every other legacy-converted case in the corpus (`codebreaker` is
26 curated vs. 42 total covered; `end-of-life` is 11 vs. 49); nothing else in the pipeline
documents or authorizes silently retiring the broad tag, so this was data loss, not a cleanup.
**Fixed by restoring `standards_spine.json` from the promotion script's own pre-write snapshot**
(`readmodel/_snapshots/standards_spine.20260818T220557.json`, the state immediately after
`redrawing-lines`'s correct promotion and immediately before `family-trip`'s), regenerating
`gap_queue.json` from the restored spine, and confirming `cases_index.json` was never touched by
the same bug (diffed clean against its own snapshot pair, only `family-trip`'s own row legitimately
changed). Root cause not fully diagnosed — the documented `case-publish` §2 script only ever
*appends* to `covered_by[]`, so this was very likely an ad hoc rewrite the promoting agent wrote
itself to handle the "title already in `cases[]`, still need to flip `status`" edge case the
documented script doesn't explicitly cover, not the script as written. Worth a real fix to
`case-publish`'s own promotion snippet (an explicit idempotent-but-still-flip-status path) so the
next case with this exact shape doesn't reopen the same hole; **not done in this pass**, filed
below.

**Where the chunk of ten ended up, all ten now genuinely `TIER2_PASS`/`published`:**

| case | starting `qa.state` / `status` | ending `qa.state` / `status` | what actually changed |
|---|---|---|---|
| `a-coachs-dilemma` | `TIER2_PASS` / `published` | unchanged | re-verified live, clean, no rework |
| `codebreaker` | `TIER2_PASS` / `published` | unchanged | re-verified live, clean, no rework |
| `cold-chain` | `TIER2_PASS` / `published` | unchanged | re-verified live, clean, no rework |
| `end-of-life` | `TIER2_PASS` / `published` | unchanged | re-verified live, clean, no rework |
| `seton-hall` | `TIER2_PASS` / `published` | unchanged | re-verified live, clean, no rework |
| `airplane-manufacturer` | `TIER2_PASS` (self-reported) / `qa` | `TIER2_PASS` / `published` | was `BLOCKED` on live Tier 1 (stale published HTML) — rebuilt; packet completed (docx/xlsx/facilitator guide/MANIFEST); promoted |
| `airstrike` | `TIER2_PASS` / `qa` | `TIER2_PASS` / `published` | live Tier 1/2 re-verify clean, no rework; packet completed; promoted |
| `wildfire` | `TIER2_PASS` / `qa` | `TIER2_PASS` / `published` | live Tier 1/2 re-verify clean, no rework; facilitator-guide docx + MANIFEST added; promoted |
| `redrawing-lines` | `TIER2_PASS` / `qa` | `TIER2_PASS` / `published` | had **no `published/` directory at all** — full packet built from scratch, including the interactive HTML from the A7 shell (case #2 proof); promoted |
| `family-trip` | `TIER1_PASS` / `qa` | `TIER2_PASS` / `published` | ran the 5 missing Tier 2 probes for real; fixed 1 propagation bug + 2 P6 citation defects; built the full packet; promoted |

`python3 app/build_pipeline.py`: `readiness` stage 10 → **0**, `promotion` stage 38 → **49**.
`python3 app/build_dashboard.py --verify`: 4 pre-existing, unrelated failures remain (down from 11
before this pass rebuilt the dashboard's cached page — the rebuild alone closed 7 of the original
11, which were the dashboard's own embedded coverage numbers having gone stale against the spine,
not real defects). The 4 that remain predate this session and are untouched by it:
`legacy_readiness` case count vs. `corpus_index` legacy count (45 vs. 63, a pre-existing corpus-
accounting drift), `derived skill ids match cases_index standards_count` (a pre-existing list of
cases whose `cases_index.json` cached `standards_count` has drifted from their live `case.json`),
the 2-cluster B2 backlog (`Calculus`/`Derivatives`, `Discrete Mathematics`/`Formal Logic` — already
documented, not newly found), and legacy cases carrying `margin: 0` instead of `null`. None are new
regressions from this pass; 0 self-checks newly broke.

**Coverage after the chunk closes:** `standards_spine.json.totals`: `skills` 437 (unchanged),
`cases` 71 (was 69), `uncovered` **73** (was 81 at the start of this pass), `thin_1_2` 196.
`readmodel/domain_coverage.json` was **not** regenerated in this pass (out of scope — the task
asked to run `build_pipeline.py`/`build_dashboard.py --verify`, not a domain-coverage rebuild) and
is now stale against the spine (`spine_skills_uncovered: 199` there vs. the live 73) — flagged
honestly, not silently trusted, the next time someone reads that file.

---

## Track B — major remaining skill gaps (2026-08-18 snapshot)

19 spine groups still carry at least one zero-coverage skill, 73 skills total. The ten highest by
raw zero-count, most recomputed after this pass's two closes above:

| zero | of | domain / group |
|---|---|---|
| 8 | 8 | Discrete Mathematics / Set Theory |
| 7 | 24 | Geometry / Fundamentals Of Geometry |
| 7 | 8 | Discrete Mathematics / Formal Logic |
| 7 | 7 | Pre-Calculus / Matrices |
| 6 | 6 | Pre-Calculus / Polar And Parametric |
| 6 | 6 | Calculus / Limits And Continuity |
| 5 | 5 | Pre-Calculus / Trigonometric Identities |
| 5 | 5 | Pre-Calculus / Introduction To Limits |
| 4 | 5 | Calculus / Series |
| 3 | 10 | Geometry / Surface Area And Volume |

`cases/_concepts/CONCEPTS_next10-careers-gapclose_2026-08-18.md` already scopes ten career-anchored
concepts against exactly these groups, ranked by skills-closed × feasibility. **Two of its ten need
re-checking before anyone writes them, because this pass's promotions moved the ground under them
without anyone intending to:** `redrawing-lines`'s `new_coverage[]` fully closed Discrete
Mathematics / Proof And Recursion (4 of 7 zero → 0 of 7) — **C9 "Prove It Scales" is now moot, its
entire target skill set already covered, drop it from the queue rather than write it.**
`airplane-manufacturer`'s closed Geometry / Fundamentals Of Geometry's `vertex` and Geometry /
Quadrilaterals And Polygons' `concave`/`irregular-polygon`/`quadrilateral` — **C7 "The Roofline
Call" now closes 7 skills instead of 8, and C8 "The Irregular Boundary" now closes 2
(`convex`/`parallelogram`) instead of 5**, which likely moves C8 below the write-worthiness bar the
concept sheet itself set (it was already the lowest-scored, MEDIUM-feasibility entry in the batch).
The other seven concepts (**C1** Grant Reach, **C2** The Contrapositive Claim, **C3** The
Multiplier Recruit, **C4** The Fan Formation, **C5** The Reserve Asymptote, **C6** The Tracker's
Angle, **C10** The Cheap Approximation) are untouched by anything in this pass. The concept sheet's
own recommendation stands and is now stronger: write **C5 (The Reserve Asymptote, score 12.2)**
first — it closes two full zero-coverage groups at once (Pre-Calculus Introduction To Limits +
Calculus Limits And Continuity, 11 skills, HIGH feasibility off public SOA/CDC mortality tables) —
then **C1** and **C3**, both HIGH-feasibility, both untapped careers, both still a clean one-group
fit.

**Correction, 2026-08-19 — this recommendation was already followed, same day, and nothing since
recorded it.** `cases/grant-reach/` (C1), `cases/the-multiplier-recruit/` (C3), and
`cases/the-reserve-asymptote/` (C5) all exist, all `authored_on: "2026-08-18"`, all `status:
"researched"`, sitting in the `research` pipeline stage with `case-readiness` (Tier 1) as next
action — see the "Current pipeline" table above. Two versions of this file (v2.10, v2.11) repeated
"write C5 next" after it was already written, because neither checked `cases/` directly. **The
seven concepts still genuinely unwritten** are C2, C4, C6, C7, C8, C10 from this same sheet, plus
this sheet's own C9 ("Prove It Scales," correctly held per the note above) — `pipeline_status.json`
only surfaced these as of this pass, after fixing the parser bug in v2.12's header finding #1.

**v2.9 · 2026-08-12.** Supersedes v2.8. **Delta: this file was eleven days stale, and the gap was
structural rather than clerical.** Between 2026-08-04 and 2026-08-12 the project shipped an entire
architecture that no roadmap track described — a local admin server (D-015), a hosted Flask app on
Vercel + Neon Postgres with passcode auth (D-016), an override-id fix (D-017), a public
student-facing case page (D-018), an Assign-a-Case redesign (D-019) — plus roughly fifteen more
authored cases. None of it appeared here, in README, in TECH_STACK or in DOCTRINE_LEDGER; a grep of
all six governance docs for `vercel|neon|postgres` returned zero hits. Corrected in this pass, with
five new doctrine rows (MCS-41→45).

**Three claims in v2.8 below are now false, and are corrected rather than deleted** (the v2.8 text
is left as written, per append-only discipline — read it as a 2026-08-01 snapshot):

1. **"Do not author case #2 until Cold Chain is `VERIFIED`"** (Track A's depth-before-breadth rule)
   — roughly fifteen more cases were authored. Tide Window was recorded as a deliberate stated
   exception; the Aug 4–5 batch of ten was not recorded as anything. The rule was not repealed, it
   was simply outrun. **What actually happened is more interesting than a rule violation:** the
   batch that ignored the rule produced ten cases at `TIER1_PASS` with no sensitivity model and no
   QA report, and the five cases authored 2026-08-12 — after the tooling matured — all clear
   `TIER2_PASS` with the full five-file packet. Depth-before-breadth was right about *why*, and the
   fix was better tooling rather than slower authoring. Track A's rule is hereby amended to the
   thing it was actually protecting: **do not mark a case `published` below `TIER2_PASS`** (MCS-41).
2. **A7 "no case #2 has used [the interactive shell] yet"** — every authored case now ships an
   `Interactive.html`. The scaffold is proven. What remains open is the narrower original point: no
   case's Working Notebook JS is a genuine *port* of its `sensitivity_model.py`, so the two can
   still silently drift (see `templates/INTERACTIVE_HTML_CONTRACT.md`).
3. **A2 "every future case needs its own `sensitivity_model.py`"** — stated as an open item, then
   not enforced for ten cases. Now mechanically swept by `scripts/apply_publish_gate.py` (MCS-41).

**The blocking fact is unchanged and is now the *only* blocker: no case is `VERIFIED`.** What has
changed is why. On 2026-08-01 there was no path to get a case to a learner and a score back. That
path now exists, is deployed, and has run the full assign → submit → machine-score → guide-confirm →
revise → resubmit → accept → complete cycle for real, repeatedly, with real submission files (see
`student_work/UAT_LOG.md`, `student_work/LIFECYCLE_SCRIPT.md`). **A3 is now a scheduling and
facilitation problem, not an engineering one.**

**New top-of-queue item — A8 · backfill the ten demoted cases.** D-020 demoted the Aug 4–5 batch
from `published` to `qa`, which makes them unassignable in the live app until each has a
`sensitivity_model.py` and a real Tier 2 run. Ten cases × (a declarative model + a probe run + a
QA report). This is now the largest single piece of open Track A work, and it is a direct,
quantified cost of having shipped past the gate — worth stating plainly rather than burying.

---

**v2.8 · 2026-08-01.** Supersedes v2.7. Delta: three roadmap items closed in one session —
**A7** (`templates/interactive_shell.html` + `INTERACTIVE_HTML_CONTRACT.md`, the case-agnostic
scaffold Cold Chain's hand-built interactive HTML never had), **B2** (spine extended into
Pre-Calc/Calculus/Discrete Mathematics, 322 → 437 skills, all three branches' `has_standards_rows`
flips true for the first time), and **C3** (Drive-folder submission intake designed against
`roster.json`/`submissions.json`/`case-track`, MCS-40). `build_domains.py`/`validate_domains.py`
(28/28) and `build_dashboard.py --verify` (140/140) all re-run clean, including three self-test
assertions that B2 made false and were fixed to test the real invariant rather than a
now-stale fact. Cold Chain itself was deliberately left untouched throughout. See
`DOCTRINE_LEDGER.md`'s 2026-08-01 change-log entries for each.

**v2.7 · 2026-08-01.** Supersedes v2.6. Delta: project renamed to Math Builder — folder physically renamed (`Math Case Studies/` → `Math Builder/`, 320 files verified intact) and every forward-facing title/reference updated to match (README, this file, DOCTRINE_LEDGER, TECH_STACK, DECISIONS, 00_SESSION, both skill docs with literal paths, the dashboard generator + regenerated dashboard.html/student.html, the Cold Chain interactive HTML footer). Historical changelog rows describing pre-rename events were left as written, per append-only discipline. `build_dashboard.py --verify`: 140/140 pass post-rename.

**v2.6 · 2026-08-01.** Supersedes v2.5. Delta: graduated to a fully independent project — `00_SESSION.md` is now this project's complete, self-contained instructions (no longer deferring to Best Practices' reading list or hard lines); `TECH_STACK.md` rewritten as this project's own authoritative record (no longer "reference + addendum"); the ACTIVE/WIP-3-cap conflict resolved by exit, not by triage — a workspace survey found 8+ other projects already over that cap, a pre-existing condition outside this project's scope. See `DOCTRINE_LEDGER.md`.

**v2.5 · 2026-08-01.** Supersedes v2.4. Delta: formally onboarded into the Best Practices governance system on request — added `00_SESSION.md` (per-project instructions block, `SESSION_PROTOCOL.md` template) and `TECH_STACK.md` (reference + addendum, not a copy); README.md now declares State/Phase in `PORTFOLIO_WIP.md` vocabulary. Flagged, not resolved: this project is honestly ACTIVE, and the portfolio was already known to be over the 3-ACTIVE cap — see `00_SESSION.md`.

**v2.4 · 2026-08-01.** Supersedes v2.3. Delta: verifying the already-shipped root-connections spine (rather than trusting the task list) caught real drift from the day's other changes — `domains.json` rebuilt fresh, a genuine two-skills-share-one-label gap fixed for Digit and Congruent (see `DOCTRINE_LEDGER.md`), `dashboard.html`/`student.html` rebuilt (were 1 day stale). `validate_domains.py` 28/28, `build_dashboard.py` 140/140, both clean. **v2.3 delta (superseded by this one):** RUBRIC.md C1 amended for MCS-39's tension with Challenge 1; B1 (`case-reconcile`) worked to its honest ceiling — 28 → 45 cases, 97 → 93 uncovered. Delta: RUBRIC.md C1 amended for the tension MCS-39 created (the case's own glossary now answers Challenge 1's "research it yourself" questions) and `score_submission.py` flags a byte-identical repost; B1 (`case-reconcile`) worked to its honest ceiling — a human read all 30 remaining 0-HIGH/0-MEDIUM cases, fixed a real plural-matching bug in the tool, and hand-confirmed 10 more cases with genuine evidence — `standards_spine.json.cases[]` 28 → 45, `uncovered` 97 → 93, 20 titles remain correctly untagged (2 revisions, 18 with no explicit math content). **v2.2 delta (superseded by this one):** MCS-39 (hover+hyperlink math glossary) shipped and locked into `case-readiness` as `T1-19`; B1 first pass confirmed 7 cases, 28 → 35. v2.1 delta (A1/A2/A5/A6 done, new A7) and v2.0 logic otherwise unchanged. v1.0 kept at the bottom as the shipped record.

Six tracks. They are **not** sequential — but there is a hard ordering rule inside two of them, and one fact blocks everything.

> **The blocking fact.** No case in this system is `VERIFIED`. Cold Chain was rewritten on 2026-07-31 to close the allocation ambiguity that first blocked it, and now reaches `TIER1_PASS` (0 blockers) with Tier 2 PASS-with-disclosed-findings on four probes (re-verified with fresh, uncontaminated subagents), a mechanical FAIL on the fifth (a real, disclosed sensitivity — not a defect), and the sixth — **attempted for real on 2026-08-01** with live network access — genuinely partial: 3 of 11 distinct cited URLs confirmed live and accurate, 1 real finding flagged for a human to check, 7 inconclusive because several source sites (UNICEF, CDC, medRxiv) block automated fetchers outright and one WHO PDF link now redirects to a JS app shell. Not a clean `TIER2_PASS` either way. That is real progress, and it is still not `VERIFIED` — no case has run with real learners. Until one does, every quality claim here is a machine claim. HIGH GRADE cleared thirteen structural checks and six simulated probes and still failed in a live room. Track A exists because of that sentence. **Resolved:** `case.json`/`cases_index.json` had both said Cold Chain's `status` was `"published"`, inconsistent with a `qa.state` that has never reached `TIER2_PASS`. User's rule: publish only on a confirmed QA-threshold pass. Corrected both to `status: "qa"` — the published files on disk are untouched, only the pipeline's own state flag moved to match reality. **Cold Chain is not currently assignable** (`case-track` requires `published` or `legacy`) until it genuinely clears `TIER2_PASS` and runs through `case-publish`.

---

## Where things actually stand — 2026-08-01 snapshot (historical; superseded below, kept per this file's own append-only rule)

**This table is nine version-deltas stale and several of its rows are now false as plain facts,
not just "as of" caveats — e.g. it still says 56 cases / 208 uncovered skills where the live spine
now says 71 / 73. Do not read anything below this line as current. See "Where things actually
stand — 2026-08-19" further down for the real numbers, derived live for this pass.**

| | |
|---|---|
| Case studies in the corpus | 56 (55 legacy + Cold Chain) — note: `case-reconcile`'s own docx-title accounting (which excludes `Best Of Studio` duplicates and reads each doc's real title) found 37 untagged titles against this corpus, not exactly `56 − standards_spine.cases`; the two counts use different methods and were never fully reconciled |
| Cases with a standards row (`standards_spine.json.cases[]`) | 45, up from 28 before `case-reconcile`'s two 2026-08-01 passes (7 automated HIGH/MEDIUM confirms, then 10 more from a human read-through of the LOW-only backlog) |
| Atomic skills | 437, up from 322 — B2 (2026-08-01) added 115 across three new Pre-Calc/Calculus/Discrete domains; all 437 ids globally unique |
| Skills with zero coverage | 208, up from 93 — the 115 new B2 rows all start at `n:0` honestly (no case exercises HS-stretch content yet); the pre-existing 93 is **still technically an upper bound** per the same caveat as before (20 read-by-hand untagged titles, 2 confirmed revisions, 18 genuinely name no math content) |
| Curriculum branches with no standards rows at all | **0**, down from 3 — Pre-Calc/Calculus/Discrete all now have real rows (B2, 2026-08-01) |
| Application domains mapped | 40, across 12 clusters, 121 live-verified sources |
| Uncovered skills now reachable from a domain | 116 of 208 — the pre-B2 93 stayed fully reachable; 92 of the 115 new B2 rows are not yet folded into a domain's `signature_skills[]` (disclosed, not hidden: `domain_coverage.json.totals.uncovered_skills_still_orphaned`) |
| Cases with Guide Notes | 40 of 56 |
| Cases with a timed Socratic plan | 2 of 56 |
| Cases `VERIFIED` by human dry-run | **0** |
| Cases currently passing the readiness gate | Cold Chain: `TIER1_PASS` (0 blockers) &middot; Tier 2 PASS-with-findings on 4 probes, mechanical FAIL on 1 (disclosed), 1 genuinely partial (3/11 URLs confirmed live 2026-08-01, 7 inconclusive/bot-blocked, 1 finding flagged) — not `TIER2_PASS`, and `status` corrected to `"qa"` (2026-08-01) to match — not currently assignable |
| Cases shipping a case-owned `sensitivity_model.py` | 1 of 1 pipeline cases (Cold Chain) |
| Cases shipping the MCS-37 interactive HTML | 1 of 1 pipeline cases (Cold Chain) — hand-built; a reusable scaffold now exists (`templates/interactive_shell.html`, A7, 2026-08-01) but no case #2 has used it yet |
| Cases shipping the MCS-39 hover+hyperlink math glossary | 1 of 1 pipeline cases (Cold Chain) — 15 terms, 14 how-to links, all urls fetched and confirmed live |

---

## Where things actually stand — 2026-08-19 (live, this pass)

Every number below was read directly from a live script run or a live `case.json` scan during
this pass (2026-08-19), not carried forward from a prior version's prose.

| | |
|---|---|
| Case dirs under `cases/` (`ls cases \| grep -v _concepts`) | 52 |
| — of those, `status: published` | 49 |
| — of those 49, **genuinely `qa.state: TIER2_PASS` or better** (`scripts/apply_publish_gate.py`) | **39** |
| — of those 49, **`qa.state: TIER1_PASS` — a live MCS-41 gate violation, not caught until this pass** | **10** (see finding #0 above: `archery-camp`, `baseball-lineup`, `cardiology`, `catering`, `house-plans`, `lebron-vs-michael`, `nuclear-waste`, `phone-plan`, `rent-vs-own`, `robotics-engineer`) |
| — of those 52, `status: researched` (in `research` stage, next action Tier 1) | 3 (`grant-reach`, `the-multiplier-recruit`, `the-reserve-asymptote`) |
| Cases tagged in `standards_spine.json.cases[]` | 71 (up from 45 as of the 2026-08-01 table above — includes the 52 pipeline dirs plus 19 legacy-only titles tagged by `case-reconcile` with no `cases/<id>/` dir of their own) |
| Atomic skills (`standards_spine.json.totals.skills`) | 437 |
| Skills with zero coverage (`standards_spine.json.totals.uncovered`) | **73** (the 2026-08-01 table's "208" is nine deltas stale) |
| Curriculum branches with no standards rows at all | 0 |
| Application domains mapped (`readmodel/domains.json`, regenerated this pass) | 40, across 12 clusters, 154 live-verified sources |
| Uncovered skills reachable from a domain (`domain_coverage.json`, regenerated this pass) | 22 of 73 reachable, 51 still orphaned |
| Legacy-corpus cases with Guide Notes (`corpus_index.json`, the original 56-doc scan — unchanged since 2026-08-01) | 40 of 56 |
| Legacy-corpus cases with a timed Socratic plan | 2 of 56 |
| Pipeline-authored cases (the 52 dirs) with a `FACILITATOR.md` | 48 of 52 (the 4 missing are the 3 `research`-stage cases pre-Tier-1 plus one gap not yet root-caused — not investigated further this pass) |
| Cases `VERIFIED` by a real human dry-run | **0** |
| Concept-sheet entries not yet written into a case (`pipeline_status.json.concepts[]`, after this pass's parser fix) | **9** — `C4` The Fan Formation, `C6` The Tracker's Angle, `C9` Redrawing the Lines *(precalc sheet — needs the human check in finding #3 above)*, `C2` The Contrapositive Claim, `C7` The Roofline Call, `C12` Reroute or Wait, `C10` The Cheap Approximation, `C8` The Irregular Boundary, `C9` Prove It Scales *(next10 sheet — already known-moot per v2.10, kept in the list because the parser doesn't encode "moot," a human does)* |

---

## Current pipeline — 2026-08-19 (case-by-case, `python3 app/build_pipeline.py`)

| stage | count | detail |
|---|---|---|
| `concepting` | 32 | 23 legacy-corpus cases whose dilemma isn't strictly binary and needs a design decision, plus 9 unwritten concept-sheet entries (see table above) |
| `drafting` | 2 | `legacy-caribbean-internet-cafe` (structurally sound, missing Guide Notes), `legacy-stock-market` (structurally sound, missing standards tagging) — both legacy-untouched, treated as near-ready once that one gap closes |
| `research` | 3 | `grant-reach`, `the-multiplier-recruit`, `the-reserve-asymptote` — all `status: researched`, all authored 2026-08-18, all next-action `case-readiness` (Tier 1). **This is the actual front of the authoring queue right now**, not "write C5" (which v2.10 and v2.11 both still said, not knowing it was already done) |
| `readiness` | 0 | nothing currently sitting mid-gate |
| `promotion` | 49 | all `status: published` — **but only 39 are genuinely gate-compliant; 10 are a live MCS-41 violation, see finding #0** |
| `verified` | 0 | unchanged — the one blocking fact |

Legacy corpus (separate accounting, `legacy_readiness.json`): 45 titles total, 2 named exceptions
(`Castle Securtiy` — missing core SPEC §1 sections; the Jia options case — case-doc asset is
misfiled as an `.xlsx` in `corpus_index.json`, D4 backlog item, unchanged since 2026-08-01).

---

# TRACK A · Quality — make one case actually trustworthy

**The rule for this track: depth before breadth. Do not author case #2 until Cold Chain is `VERIFIED`.** A pipeline that produces twelve cases carrying the same undisclosed-convention defect is worse than one that produces a single clean case slowly.

### A1 · Unblock Cold Chain ✅ *(done 2026-07-31 — re-verified with fresh subagents)*

Fixed by redesign, not disclosure: Order A rebuilt as 4 boxes ($408.84 of $420, 3 truck + 1 motorcycle, stated as Appendix F Assumption 0), so the allocation question the old design left ambiguous is now moot — there's no shortfall left to allocate. Re-ran the full ladder afterward with **fresh, uncontaminated subagents** for the four simulated-play probes: all four passed, and they found two smaller, real, previously-undisclosed sensitivities (the twist's `opening_cost_h ≥ ~2.65h` floor; Assumption 2's ±50% fragility) which are now disclosed in Guide Notes and `case.json` rather than hidden. See `cases/cold-chain/QA_REPORT.md` § *Rewrite + re-verification*. **P6 attempted for real 2026-08-01** (see § *Tier 2 probe 6 attempted for real*) — 3/11 URLs confirmed, 7 inconclusive due to site-side bot blocking, not something more network access alone fixes next time either. **Still open, and not something this pipeline can close alone:** A3 (the actual human dry-run) needs a real guide and room.

### A2 · Ship a `sensitivity_model.py` per case ✅ *(done for Cold Chain 2026-07-31)*

Tier 2 probe 5 returns `NOT RUN` without a declarative model. `cases/cold-chain/sensitivity_model.py` now ships as the case's own model (not the skill's reference model) — `PARAMS`, `FLEX = [opening_cost_h, in_spec_fraction]`, `evaluate()`, `evaluate_twist()`, verified to reproduce the published 8,200/7,000 base and the twist's tie. **Still open:** every future case needs its own; there is no scaffold/template yet that generates the boilerplate half of this file.

### A7 · Templatize the interactive-HTML generator (MCS-37) ✅ *(scaffold done 2026-08-01)*

Cold Chain's `published/*.html` was hand-built end to end — narrative markup, SVG diagrams, the self-checking calculator's JS, and (as of 2026-08-01) the MCS-39 math glossary were all authored bespoke for this one case. That does not scale past case #2. Built `templates/interactive_shell.html` (the crest/icon `<defs>`, CSS design system, nav/tab scaffolding, checklist/localStorage logic parameterized by `CASE_ID`, dilemma-pick widget, twist-reveal gating, and the `gtermHTML`/`renderGlossary` glossary render function — all case-agnostic, extracted verbatim from Cold Chain and marked with `{{PLACEHOLDER}}` tokens for every case-specific block) and `templates/INTERACTIVE_HTML_CONTRACT.md` (the `sensitivity_model.py` ↔ JS-port contract — same `PARAMS`/`FLEX`/`evaluate()`/`evaluate_twist()` names on both sides, which Cold Chain itself does *not* follow today, its JS tally being a hand-derived parallel rather than a port; the `T1-18`/`T1-19` gotchas, incl. the JS-data-object-wins-over-static-anchors precedence bug MCS-39 already found once; and a 14-term starter glossary reusing Cold Chain's own already-fetched-and-confirmed Khan Academy links verbatim, since MCS-21 treats a reused verified source as legitimate, not fabricated). `skills/case-publish/SKILL.md` §1 updated to point at the shell instead of a blank file, and its `MANIFEST.json` template now lists the `.html` (previously undocumented — case-publish doesn't build or verify it, but it should at least be recorded). **Still open:** this is a scaffold, not a generator — a human still authors each case's diagrams, narrative, and notebook logic by filling the shell; there is no code that emits a filled `.html` from `case.json` automatically. It has not yet been proven against a real case #2, because none has been authored since Cold Chain (Track A's own depth-before-breadth rule). Cold Chain's own file was deliberately left untouched rather than retrofitted onto the shell, to avoid risking regression in the one case closest to `VERIFIED`.

**Update, same day:** the shell shipped with a real bug — a nested HTML comment closed 20 lines early and mangled the raw file when opened in a browser (caught by the user actually opening it). Fixed and verified with a proper comment tokenizer. Also added `autoLinkGlossaryTerms()` on request: MCS-39 asks for hover+hyperlink "on any concepts that need explanation," which Appendix G alone doesn't deliver — the shell now auto-wraps the first mention of each glossary term wherever it actually appears in the case's own prose (Overview, Background, Appendices, Notebook, Twist), not just in a list at the bottom. Verified end-to-end against a filled test fixture (built and torn down inside the project folder so the browser preview actually ran the JS) — caught and fixed a second real bug in the process (the seeding step was counting Appendix G's own anchors as "already linked," silently defeating the whole feature). See `templates/INTERACTIVE_HTML_CONTRACT.md` §4 and DOCTRINE_LEDGER's 2026-08-01 entry.

### A3 · First human dry-run → first `VERIFIED` case

A guide runs Cold Chain with a real cohort and fills `templates/RUN_REPORT.md` **during** the session. Facts first. Use the **"can't tell"** column honestly. This is the only way to learn whether the twist lands, whether Anchor 2 keeps learners off the calculator, and whether 45 minutes is the right length.

**Correction, 2026-08-19 — a case run under A3 should not be picked from the raw "49 published"
count.** v2.12 found 10 of those 49 are only `TIER1_PASS`, a live violation of the gate this exact
track exists to enforce (see v2.12 header finding #0, and the new `A9` item below). Pick from the
39 that genuinely clear `TIER2_PASS`, or run `scripts/apply_publish_gate.py --confirm` first so
the unassignable ones stop showing up as candidates at all.

### A9 · Close the 10-case MCS-41 gate violation *(new, 2026-08-19)*

`scripts/apply_publish_gate.py` (dry-run) names 10 cases currently `status: published` with only
`qa.state: TIER1_PASS` — no sensitivity model, no QA report, exactly the shape D-020 wrote the gate
to stop: `archery-camp`, `baseball-lineup`, `cardiology`, `catering`, `house-plans`,
`lebron-vs-michael`, `nuclear-waste`, `phone-plan`, `rent-vs-own`, `robotics-engineer`. This is not
new — it is the same failure mode as the original Aug 4–5 batch D-020 already demoted once — it
just wasn't checked again since. Two moves, in order: **(1)** a human decides whether to
`--confirm` the demotion now (makes these 10 correctly unassignable again, matches every other
promoted case's real bar) or explicitly re-scope the rule; **(2)** whichever way that goes, decide
whether `apply_publish_gate.py` should run as part of `build_pipeline.py`/CI rather than by hand,
since this is the second time a real batch of cases slipped past the written rule undetected
between checks.

### A4 · Wire the last UNWIRED rules ✅ *(done — verified 2026-08-01)*

MCS-29 (`tier3_verify.py`), MCS-31 (`guide_confirm.py --audit --write` + the `demoted_criteria.json` overlay), and MCS-17 (`case-reconcile`, built in B1) are all genuinely `WIRED`. This item's real work turned out to be a ledger correction, not new code: `DOCTRINE_LEDGER.md` carried a stale, contradictory duplicate row for each of the three — left over from before the Tier 1/2/3 gate rebuild and `case-reconcile` — still claiming `CODIFIED`/`UNWIRED` alongside the later, correct `WIRED` row. Removed the stale duplicates so each rule has exactly one row, matching what the ledger's own UNWIRED queue had already (correctly) marked `CLOSED`. See DOCTRINE_LEDGER's 2026-08-01 "A4 closed" change-log entry.

### A5 · Fix the duplicate skill ids ✅ *(done 2026-07-31)*

Group-scoped the 2 colliding ids (`Digit` in Numbers-And-Counting, `Congruent` in Fundamentals) to `number-sense-numbers-and-counting-digit` / `geometry-fundamentals-of-geometry-congruent`, keeping the ids `domains.json` already referenced unchanged. 322 skills, 322 unique ids now, both pairs were n=0 so no case data moved. See MCS-36.

### A6 · Design cohort bands ✅ *(done 2026-07-31, applied to Cold Chain)*

Three named bands — Full (12–20), Compressed (6–11), 1:1 or pair (1–2) — each saying what compresses in the anchor ladder and which Deep Conflict threads survive. Transferred from the HIGH GRADE kit as process only. See MCS-25 and `case.json.cohort_bands[]`. **Still open:** only Cold Chain has bands; every other case with Guide Notes (B3) will need its own.

---

# TRACK B · Coverage — close the map

**Ordering rule: tag before you author.** The uncovered-skills figure was a 97-skill upper bound polluted by untagged cases; `case-reconcile` has now worked that backlog to its honest ceiling (see B1) and the real number is 93. Authoring against a wrong gap list wastes the most expensive resource here.

### B1 · `case-reconcile` — tag the untagged cases ✅ *(built, run, and worked to its honest ceiling — 2026-08-01)*

Built and run for real against the corpus (not the estimated 31 — **37** untagged cases actually found; source docs live under messy, inconsistent folder names, so the skill reads each doc's own title heading rather than trusting the folder). Every proposed skill carries a quoted evidence sentence and a HIGH/MEDIUM/LOW confidence grade. **First pass:** 7 cases carried a real vocabulary section and matched cleanly at HIGH confidence, confirmed automatically (College Football Playoff Committee, Driving Age, Fast Food, Life Insurance Agent, Medical Statistician, City Planner, Robotics Engineer). **Second pass — the human read the SKILL.md itself calls for:** all 30 remaining 0-HIGH/0-MEDIUM cases were read directly, source docx by source docx. That read (1) caught and fixed a real precision bug in the matcher (`match_term()`'s word-boundary regex didn't tolerate a plain plural, so "Histograms" never matched the "Histogram" skill), and (2) hand-confirmed 10 more cases via `--skills` where the actual sentence showed genuinely load-bearing math content rather than coincidental English — Acton Survey (a real sampling-methodology case), Biostatician, Caribbean Internet Cafe, Electoral College, Loan Officer, Medical Transport, Player Of The Year, Logic, Gerrymandering, Insurance Actuary. `standards_spine.json.cases[]`: 28 → 45, `uncovered`: 97 → 93. **Closed, not abandoned:** the remaining 20 titles were also read, not skipped — 2 are genuine revisions of already-tagged cases (Phone Plans/2.0 against "Phone Plan"; Which (Investment) Portfolio? against "Investment Portfolio" — same character, same premise, a rewrite), and 18 genuinely name no explicit math vocabulary anywhere in their source text. That is this corpus's real ceiling, not unfinished work.

### B2 · Extend the spine into Pre-Calc, Calculus, Discrete ✅ *(done 2026-08-01)*

Three branches had *no rows at all*. Added 115 skill rows across three new `standards_spine.json` domains — **Pre-Calculus** (41 skills / 6 groups: trig functions, identities, polar & parametric, vectors, matrices, intro to limits), **Calculus** (38 skills / 6 groups: limits & continuity, derivatives, applications of derivatives, integrals, applications of integrals, series), **Discrete Mathematics** (36 skills / 5 groups: set theory, formal logic, graph theory, combinatorics, proof & recursion) — following the existing id/group/`covered_by`/`n` conventions exactly (MCS-36's id-collision rule checked programmatically; 0 collisions). `curriculum_tree.json`'s three branches now carry `acton_domains: ["Pre-Calculus"]` / `["Calculus"]` / `["Discrete Mathematics"]`, so `has_standards_rows` flips to `true` for all three automatically. `readmodel/standards_spine.json.totals`: `skills` 322 → 437, `uncovered` 93 → 208 (every new row starts at `n:0`, honestly — no case exercises HS-stretch content yet). Snapshot taken before write (MCS-22). New spine ids also folded into 12 existing domains' `signature_skills[]` where the fit is real (not padding) — oceanography's tides (`pre-calculus-sine-function`/`amplitude`/`period-of-a-function`, `calculus-definite-integral`), aviation/surveying-geodesy's bearing math (`pre-calculus-vector`), spaceflight's rocket equation (`calculus-derivative`), computer-graphics' transforms (`pre-calculus-matrix`), cryptography-security/network-science/maritime-shipping/education-systems/tiling-pattern-art's counting and graph problems (`discrete-mathematics-*`), music-acoustics' waveforms (`pre-calculus-sine-function`). `build_domains.py`/`validate_domains.py` (28/28) and `build_dashboard.py --verify` (140/140) all re-run and pass — three of the 140 checks had hardcoded a now-false assumption (that these 3 branches would *always* render "unmapped," never a real 0%) and were fixed to assert the actual invariant (0% is never used to mean "no rows exist") rather than the stale fact. **Honestly disclosed, not closed:** only 116 of the 208 total uncovered skills are reachable from a domain's `signature_skills[]` today (`domain_coverage.json.totals.uncovered_skills_still_orphaned: 92`, almost all of them the newly-added rows) — B2 built the taxonomy; folding every new skill into a domain the way the original 93 were is B4-shaped follow-on authoring work, not done here.

### B3 · Backfill Guide Notes and Socratic plans

16 cases have no Guide Notes. 54 have no timed plan. The discussion is where the learning lands, so a case without facilitator scaffolding is half an artifact. Prioritize by actual use, not alphabetically.

### B4 · The authoring queue — gap-driven, domain-anchored

All 93 currently-uncovered skills are now reachable from a domain with named free data, so the queue writes itself. In priority order by skills closed:

| # | Case concept | Domain | Closes | Why |
|---|---|---|---|---|
| 1 | Tiling / pattern commission | `tiling-pattern-art` | **27** | Hits the polygon *and* transformation clusters at once; MIT Tiling Search gives real measurable patterns |
| 2 | Marching band drill design | `drill-choreography` | 14 | A football field is a painted coordinate grid. 14 of the 20 transformations. The surprising one |
| 3 | Sheet-metal nesting | `manufacturing-nesting` | 12 | Rotate-to-save-a-sheet — a transformation with money attached |
| 4 | Pattern grading | `textiles-pattern` | 12 | Grading *is* non-uniform dilation; FreeSewing exposes the formulas |
| 5 | Survey monument dispute | `surveying-geodesy` | 11 | Parallel lines and transversals; NGS datasheets let students check their own trig |
| 6 | Image registration | `remote-sensing` | 8 | Translation + dilation on free Landsat/Sentinel scenes |
| 7 | Key-length decision | `cryptography-security` | 8 | The only domain that closes the entire Factoring group, 6/6 |

**Addendum, 2026-08-01 — Pre-Calc/Calculus/Discrete queue.** The table above targets the original
MS-domain gaps; B2 (same day) opened a second, separate queue for the three branches that had no
standards rows at all until today. Six ranked concepts brainstormed against `gap_queue.json`
(regenerated first — see DOCTRINE_LEDGER) in
`cases/_concepts/CONCEPTS_precalc-calculus-discrete_2026-08-01.md`: **Tide Window** (Pre-Calc
Trig Functions, score 9.8, recommended first), **The Optimal Can** (Calculus Applications of
Derivatives, 7.7), **Wind Triangle** (Pre-Calc Vectors, 7.4), **Total Flow** (Calculus Integrals,
7.4), **The Keyspace Decision** (Discrete Combinatorics, 5.8), **Six Degrees of Exposure**
(Discrete Graph Theory, partial, 3.4, carries a SPEC §6 sensitivity note).

**Update, same day — C1 written.** User chose to write Tide Window now, a deliberate, stated
exception to the depth-before-breadth rule (Cold Chain is still not `VERIFIED`). `cases/tide-window/`
now has `case.md`/`case.json`/`LEARNING_GOALS.md`/`FACILITATOR.md`; bidirectional LEARNING GOAL
CHECK passes (4 deliverables, 11 skills, 0 unmapped, 0 unreachable); Tier 1 structural gate finds
exactly the two blockers expected at this stage (11 open `{{NEEDS_SOURCE}}` placeholders,
`margin_pct` null) and nothing else — see DOCTRINE_LEDGER for the real authoring defects that run
caught and fixed along the way.

**Update, same day — `case-research` run.** 9 of 11 placeholders sourced live (4 straight from
NOAA's own API — real station, real datum, real M2 constituent, real predicted water levels for a
real date), 2 honest `NOT FOUND`s became stated Modeling Assumptions with real industry figures as
their basis. Research forced a real finding before it forced a fake one: working the case's own
clearance-vs-policy arithmetic with real numbers showed the drafted Twist couldn't flip the
verdict without stretching the storm into hurricane territory the case's own narrative rules out —
rather than pick an assumption value to force a reversal, set it to the middle of a real range,
computed the honest result (margin erodes ~42%, doesn't flip), and rewrote the Guide Notes to argue
from that. Tier 1 re-run: 1 blocker left (`margin_pct`, correctly deferred to `case-qa`), 0 open
placeholders. **Next: `case-qa` / `case-readiness` on `tide-window`, then a `sensitivity_model.py`
before Tier 2 can run.** The other four concept-sheet options (C2/C3/C4/C6/C9, plus the C11+C12
pair) remain unwritten.

**Transformations — the largest hole at 20/20 — is closed by concepts 1–3 and 6 together.**

**Reprioritized, 2026-08-19 — Geometry and Pre-Calculus go first, ahead of Discrete Math and
Calculus.** User directive. Live counts from `standards_spine.json` (not the stale 2026-08-18
group table above — recomputed per-group directly this pass):

| domain | group | zero / of | closing concept | status |
|---|---|---|---|---|
| Pre-Calculus | Matrices | 7/7 | **C3** The Multiplier Recruit | **already written** — `cases/the-multiplier-recruit/`, `research` stage, needs Tier 1 |
| Pre-Calculus | Introduction To Limits | 5/5 | **C5** The Reserve Asymptote | **already written** — `cases/the-reserve-asymptote/`, `research` stage, needs Tier 1 (also closes 6 Calculus / Limits And Continuity skills as a bonus, not counted here) |
| Pre-Calculus | Polar And Parametric | 6/6 | **C4** The Fan Formation | unwritten |
| Pre-Calculus | Trigonometric Identities | 5/5 | **C6** The Tracker's Angle | unwritten |
| Geometry | Fundamentals Of Geometry | 7/24 | **C7** The Roofline Call | unwritten |
| Geometry | Quadrilaterals And Polygons | 2/22 | **C8** The Irregular Boundary | unwritten — closes only 2 now (`airplane-manufacturer` already took `convex`/`parallelogram`/etc.), re-check write-worthiness before starting |
| Geometry | Visual Perceptibility | 2/11 | **none yet** | no concept targets this group at all — a real gap in the concept queue itself |
| Geometry | Surface Area And Volume | 3/10 | **none yet** | same — no concept targets this group |

**The fast win, and the actual next step: promote what's already sitting written.** `the-
multiplier-recruit` (Matrices, 7/7) and `the-reserve-asymptote` (Intro To Limits, 5/5, +6
Calculus) only need `case-readiness` (Tier 1) run and the rest of the pipeline followed — no new
authoring. That alone fully closes 2 of Pre-Calculus's 4 zero-coverage groups. Write **C4** and
**C6** next (Polar And Parametric, Trig Identities) and Pre-Calculus has **zero** zero-coverage
groups left, full stop. Geometry is a longer road — **C7** closes 7 of Fundamentals Of Geometry's
remaining 7-of-24, but **C8** is now barely worth authoring on its own (2 skills), and two whole
Geometry groups (Visual Perceptibility, Surface Area And Volume, 5 skills between them) have no
concept at all yet — worth a dedicated Geometry-focused `case-brainstorm` pass rather than
stretching C8 to cover ground it wasn't scoped for. See Sequencing → As of v2.12 for where this
sits against the rest of the queue.

### B5 · Domain-starved branches

`number-theory` is both domain- and case-starved (4 domains, 4 cases) — the thinnest branch in the file. `precalc` / `calculus` / `linear-algebra` are *case*-starved but not domain-starved: the mapping exists, the cases don't. `calculus` has only two HIGH domains (oceanography, spaceflight) — the weakest pipeline.

---

# TRACK C · Interface

### C1 · Ship what was just built ✅

Cases open from the dashboard (283 links, all resolving on disk), a graph router with Back, global `/` search, a Root Connections tab over 40 domains, a Rubric & Scoring tab, and a separate role-locked `student.html`.

### C2 · Deep links

`pushState` with a URL throws on `file://` (opaque origin), so Back works but you cannot link someone to a view. Fix needs either hash-routing or serving over `http://`. Decide which — it still gates the "real upload form" option that C3 didn't take.

### C3 · Submission intake ✅ *(designed 2026-08-01 — unproven live)*

A Hero downloads a packet and submits… somewhere. The tracker had the schema; there was no path in. Chose **a per-learner Drive folder** over a watched local folder or a real upload form — the latter needs a server (C2 still gates that option specifically, not this one). `roster.json` gained `drive_folder_id`/`drive_folder_url` per learner; `submissions.json` gained `source` (`facilitator-dictated` | `drive-intake`) and `drive_artifacts{}` on `submissions[]`; `skills/case-track/SKILL.md` gained a full "Drive intake" operation reusing `case-publish`'s already-connected Drive MCP server, on its read/download side this time — locate-or-create the learner's folder (asked, not assumed), diff new files against what's already recorded, confirm before writing, download a local copy to `student_work/<learner>/<case>/submitted/` before recording anything. See DOCTRINE_LEDGER MCS-40. **This blocks the entire scoring loop from ever running at scale, and still does** — the mechanism is fully specified but has never touched a real Drive account; the honest next step is one real learner, one real folder, one real file, before trusting the diff logic in a live cohort.

### C4 · Per-learner standards heatmap

Student mode shows badge progress but not *which skills this Hero has actually exercised*. Probably the most motivating view in the system, and the data already exists.

### C5 · Fix the orphan override record ✅ *(verified fixed, 2026-08-19)*

`score_overrides.json` references a `score_id` present in no `scores[]` record. Currently surfaced in the UI rather than swallowed. Add referential integrity to the writer.

**Verified this pass, not just re-asserted:** checked all 4 records in `readmodel/
score_overrides.json` against `readmodel/submissions.json.scores[]` directly. The only one that
fails to resolve is the file's own seeded `_example: true` placeholder (labeled as an example, not
live data, by design); the 3 real overrides all resolve cleanly. Whatever fixed this happened in
an undated prior session — no matching entry in `DECISIONS.md` or `DOCTRINE_LEDGER.md`'s change
log — but the check itself now passes. **Caveat stated plainly, not swept under the ✅:** this
checks the local `readmodel/` mirror per `TECH_STACK.md`'s own local/hosted boundary, not the live
Postgres store directly — if the hosted app's own write path can still produce an orphan, this
check would not catch it.

### C6 · Pipeline view — where every case actually is ✅ *(done 2026-08-01)*

There was no single place to see "concepting vs. drafting vs. stuck in readiness" across the whole
corpus — `cases_index.json` only gains an entry at *publish* time, so a mid-pipeline case (Tide
Window, sitting in `research`→`readiness`) was invisible to it entirely. Built `app/build_pipeline.py`
(derives `readmodel/pipeline_status.json` by scanning `cases/*/case.json` directly and
`cases/_concepts/*.md`, live-re-running Tier 1 per case rather than trusting `case.json.qa`) and a
new **Pipeline** tab in the dashboard — six stage columns (concepting → drafting → research →
readiness → promotion → verified), a stat-tile summary, per-case gate-status cards with a
computed next-action, legacy corpus cases shown as an explicit separate bucket rather than
force-fit into a stage. `build_dashboard.py --verify`: 145/145 (5 new checks). **Real side effect
this surfaced**: `case.json.qa` was not even a consistent shape across the two real cases —
fixed both to match. **Still open:** the stage list is accurate to today's pipeline; if a stage's
actual mechanics change (e.g. case-readiness splits further), `build_pipeline.py`'s
`stage_for_case()` needs a matching update — it is not self-deriving from doctrine text.

**Update, same day — the 55 legacy cases scored too, on their own honest terms.** User asked to
review the existing corpus against the readiness gate. `tier1_structural.py` can't run against
them directly (wrong file shape — `case.md`/`case.json` vs. raw `.docx`), and a deeper look showed
a verbatim-boilerplate or exact-anchor-heading diff would fail all 55 for predating the doctrine,
not for being bad. Built `app/build_legacy_readiness.py` instead: structural shape (Overview/
Background/binary Dilemma/Challenges/Appendices, loosely matched — fair to ask of a pre-doctrine
doc) checked separately from current-doctrine artifacts (cohort bands/interactive HTML/glossary —
reported as "0/55, absent by construction," not a per-case defect list). Real findings: 20.4%
(11 cases) have a genuine third dilemma option, spot-checked against source text and confirmed
real (Pets: dog/cat/bird), predating SPEC's strictly-binary rule; 61.5% of Guide Notes mention a
twist somewhere despite only 2.6% using the literal "Standards Touched On" heading. Caught and
fixed two real bugs in the checker itself along the way (a case-sensitivity regex bug, a title-
escaping mismatch undercounting standards-tagged cases by one). Surfaced as a scorecard panel in
the same Pipeline tab, not a stage column — showing them "in" the pipeline would misrepresent them
the same way a verbatim diff would. `build_dashboard.py --verify`: 148/148. **Also found, not
fixed:** one legacy case (`Investing - Stock Market - Options (Jia)`) has an `.xlsx` misfiled as
its `case_doc` asset in `corpus_index.json` — a small pre-existing data bug, tracked, not touched
in this pass. See D4 (legacy packet normalization).

**Second update, same day — collapsed into one pipeline, per explicit user objection.** User: "i
reallly don't want two pipelines... let's put them in the right place." The scorecard-panel design
above was a genuine attempt to avoid misrepresenting pre-doctrine cases, but it built a second view
instead of placing them — not what was asked. Rewrote `build_pipeline.py` to triage all 55 using
`legacy_readiness.json`'s already-computed signal and fold each into the *same* six-column board:
not-strictly-binary lands in Concepting (23 cases — the same design decision a new concept needs);
structurally-sound-plus-Guide-Notes-plus-tagged lands in Drafting as `NEAR READY` (18); partial
signal lands `MODERATE WORK`/`MORE WORK` (7 + 5). 53 of 55 folded cleanly; the 2 that couldn't
(one misfiled `.xlsx`, one missing core sections) are named `legacy_exceptions[]`, not guessed at —
minimizing exceptions was the explicit ask. Dashboard's old scorecard panel replaced with legacy-
origin cards inside the real columns (effort-tier badge instead of a Tier-1 verdict) plus a small
callout naming just the 2 exceptions. `--verify`: 150/150 (was 148). Visually confirmed in-browser.
**Not done:** no legacy case has actually been converted yet — spot-checking Payroll (a "NEAR
READY" candidate) found 34 legacy-tagged standards skills, well past the ~8-15 healthy range
`case-brainstorm` itself guards against, meaning real curation is still required, not mechanical
transcription. Board structure now matches the instruction; sequencing the actual conversion of
the 18 NEAR READY cases toward `case-publish` is the next open decision.

---

# TRACK D · Download & delivery

### D1 · Drive publishing — one real run

`case-publish` has the step and has never executed against the connected account. Until it does, "publish" means "wrote a file locally."

### D2 · Packet standardization

Cold Chain's filenames don't follow the convention `case-publish` specifies. Every case should emit an identical bundle: case `.docx`, Guide Notes `.docx`, workbook `.xlsx`, RUN_REPORT, `MANIFEST.json`. HIGH GRADE's assembly-and-print checklist is the model — *print this / handwrite that / assemble in this order*.

### D3 · Print discipline

These get printed and handed out. **Nobody has printed one.** Check page breaks, whether appendix tables split across pages, whether the workbook fits one sheet, and whether a guide can hold the Socratic plan in one hand.

### D4 · Legacy packet normalization

55 legacy cases are loose `.docx` in session folders with inconsistent naming (`Guides Notes.docx`, `Castle Securtiy`). Normalize into the standard bundle so the tracker treats all 56 identically. Add to this backlog: `Investing - Stock Market - Options (Jia)`'s `corpus_index.json` entry lists an `.xlsx` as its `case_doc` asset (found running `app/build_legacy_readiness.py`, 2026-08-01) — `readmodel/corpus_index.json` needs the real case `.docx` identified and the asset entry corrected.

---

# TRACK E · Evaluation

### E1 · Calibrate the rubric ✅ shipped · ⚠ uncalibrated

`RUBRIC.md` v1.0 is **PROPOSED, not locked.** The weights assert that argument and correctness matter 4× the research link. Defensible, untested. One real cohort confirms or moves them.

### E2 · C7 needs a reality check

"Framing the question" has no legacy precedent — none of the 40 Guide Notes score it. It may be too hard at T1–T2. **If nearly everyone lands Not Yet, the criterion is wrong, not the Heroes.**

### E3 · Record discussion participation

C6 needs per-Hero contribution counts. The schema exists; the habit does not. Without it, one of seven criteria is unscoreable — and it is the one measuring the thing the whole format exists for.

### E4 · Inter-rater check

Two guides, one submission, compare. Until that has happened once, every Exemplary is one guide's opinion rather than a system verdict.

### E5 · Watch the override log

The machine's C1/C2/C7 detection is cue-phrase based and will miss unusual phrasing. Every override is a training signal. The 30% demotion rule needs enforcement (A4) and a real n before it means anything.

---

# TRACK F · Engagement

The brief asked for cases that *teach math and show applications* — engaging problems with real data. Tracks B and E make cases correct and gradeable. This track makes them worth doing.

### F1 · Engineer the herring

HIGH GRADE builds the *seductive wrong answer* first, with real supporting evidence, and constructs the truth around it. Cold Chain's trap was noticed during authoring, not designed. Invert it: `case-brainstorm` should ask "what is the plausible wrong path?" **before** "what is the answer?"

### F2 · The jigsaw variant *(the most interesting unexplored idea here)*

HIGH GRADE gives each character **information rights** — what they know, may reveal, must conceal. The analogue: different Heroes receive different appendices and must combine them to see the whole picture. Turns a solo case into a genuinely collaborative one and makes the discussion structurally necessary rather than merely scheduled.

### F3 · Career surfacing

`domains.json` carries 120 careers with the *specific computation* each uses — "fits dose-response curves and computes number-needed-to-treat," not "uses statistics." Surface it at the point of work: *the math you just did is what an epidemiologist does on a Tuesday.* Today it lives only in Root Connections; it belongs in the case packet.

### F4 · Live data

Several domains expose live feeds (GTFS transit, NOAA, USGS, FRED). A case whose appendix regenerates against this week's data is a different kind of artifact — and a maintenance burden, and a reproducibility problem for grading. Decide deliberately; don't drift into it.

### F5 · The surprising ones

Deliberately author the domains a teenager would not expect to be mathematical: marching-band drill, textile pattern grading, tiling, music acoustics, archaeology. `drill-choreography` sits at #2 on the authoring queue for exactly this reason.

---

## Sequencing

### As of v2.12 · 2026-08-19

**Now, in order — reordered from v2.11, whose #1 (A3) is demoted to #2 by a worse-severity finding
this pass surfaced:**
1. **A9 — resolve the 10-case MCS-41 gate violation.** `archery-camp`, `baseball-lineup`,
   `cardiology`, `catering`, `house-plans`, `lebron-vs-michael`, `nuclear-waste`, `phone-plan`,
   `rent-vs-own`, `robotics-engineer` are `status: published` at only `TIER1_PASS` — live,
   currently assignable to a real learner, in direct violation of the rule D-020 wrote after the
   *first* time this happened. A human decision (`apply_publish_gate.py --confirm`, or an explicit
   re-scope of the rule), not an engineering task. Goes first because it's a correctness violation
   in what's already live, not a "next thing to build."
2. **A3 — first `VERIFIED` case.** Still the actual blocking fact. Pick from the **39** cases that
   genuinely clear `TIER2_PASS` (not the raw 49), or resolve #1 first so "published" means what it
   says again.
3. **Run `case-readiness` (Tier 1) on `the-multiplier-recruit` and `the-reserve-asymptote`
   (C3/C5) first, ahead of `grant-reach` (C1).** Reordered per explicit user directive
   (2026-08-19): Track B now runs Geometry and Pre-Calculus ahead of Discrete Math and Calculus.
   `grant-reach` is Discrete Math (Set Theory) and drops behind these two, not off the queue —
   still the front of the authoring pipeline, just not first among the three.
4. **Write C4 (The Fan Formation, Pre-Calc Polar And Parametric, 6/6) and C6 (The Tracker's
   Angle, Pre-Calc Trigonometric Identities, 5/5) next.** Combined with #3 landing, this fully
   closes Pre-Calculus's zero-coverage list — 0 of 4 groups left with any zero-coverage skill. See
   Track B4's 2026-08-19 addendum for the live per-group counts this reordering is based on.
5. **Then Geometry: write C7 (The Roofline Call, Fundamentals Of Geometry, closes 7 of the
   remaining 7-of-24).** Re-check C8 (The Irregular Boundary) before starting it — it now only
   closes 2 skills (Quadrilaterals And Polygons), likely below write-worthiness on its own. Two
   Geometry groups (Visual Perceptibility 2/11, Surface Area And Volume 3/10) have **no concept
   at all** targeting them — a real gap in the concept queue, not just an authoring backlog; worth
   a dedicated Geometry `case-brainstorm` pass rather than stretching C8 to cover it.
6. **Fix `case-publish`'s promotion snippet for the "already in `cases[]`, still need to flip
   `status`" case.** Unchanged from v2.10 — the exact gap that produced that pass's 62/77-skill
   `standards_spine.json` regression is still open, and is now the *same shape* of bug as this
   pass's own #0/A9 finding (a promotion path nobody re-checks after the fact). Worth fixing both
   with the same discipline: a script that runs automatically, not one a human remembers to invoke.
7. **A9's gate violation resolved and the Geometry/Pre-Calc concepts landed, resume the general
   queue**: `cases/_concepts/CONCEPTS_precalc-calculus-discrete_2026-08-01.md`'s C9 ("Redrawing the
   Lines") needs a human read against the already-published `cases/redrawing-lines/` before anyone
   writes it (same-ish title, different stated skill target — not resolved by this pass); then C2
   (Discrete Formal Logic) and C10 (Calculus Series), the two remaining next10-sheet concepts
   outside Geometry/Pre-Calc.
8. **A regression net over the admin core.** Unchanged — `admin_core.py`, `store_postgres.py`,
   `admin_web/app.py` still have zero automated tests.
9. **Real auth (MCS-44).** Unchanged — one shared passcode still guards write access to real
   learner data with no per-user identity.
10. **Commit or discard the working-tree files this pass found already modified**, unchanged from
    v2.11: `app/build_dashboard.py`'s reconciled-path fix (real, verified) should be committed on
    its own; `00_SESSION.md`'s `library`-governance-tier note looks like it belongs to a different
    project and needs a human call.

**Done since v2.11 (same day, 2026-08-19):** fixed a real parser bug in `build_pipeline.py` that
was hiding 7 unwritten concepts (`concepting` 25 → 32); found and precisely quantified a live
10-case MCS-41 gate violation nobody had re-checked since D-020; found that C1/C3/C5 were already
written on 2026-08-18 and two prior roadmap versions never noticed; verified C5 (orphan override)
is actually fixed, not just claimed; replaced a nine-version-stale "current state" table and added
a real case-by-case pipeline view; reprioritized Track B's authoring queue to Geometry/Pre-Calculus
first per user directive.

**One line:** the roadmap itself was the thing most out of date — the pipeline's own scripts, run
for real instead of trusted, found a live gate violation, a mis-parsed concept queue, and three
already-finished cases this file kept telling people to start.

---

### As of v2.11 · 2026-08-19

**Now, in order — unchanged from v2.10 except item 4 is closed:**
1. **A3 — first `VERIFIED` case.** Still the single blocking fact, still untouched by this pass.
   15 genuinely `TIER2_PASS`/`published` candidates are available to run. Calendar work, not
   engineering work.
2. **Fix `case-publish`'s promotion snippet for the "already in `cases[]`, still need to flip
   `status`" case.** Unchanged from v2.10 — the exact gap that produced that pass's 62/77-skill
   `standards_spine.json` data-loss regression is still open; the next case with that shape (a
   legacy conversion, already spine-tagged, newly reaching `TIER2_PASS`) can reopen it.
3. **Write C5 (The Reserve Asymptote) next**, unchanged from v2.10 — highest-value item in the
   current concept queue, closes 11 skills across two full zero-coverage groups. Re-scope C7/C8
   first per v2.10's Track B note; C9 is moot, drop it.
4. ~~Regenerate `readmodel/domain_coverage.json`.~~ **Done in this pass** — see this version's
   header. `spine_skills_uncovered` now reads 73, matching the live spine.
5. **A regression net over the admin core.** Unchanged — `admin_core.py`, `store_postgres.py`,
   `admin_web/app.py` still have zero automated tests.
6. **Real auth (MCS-44).** Unchanged — one shared passcode still guards write access to real
   learner data with no per-user identity.
7. **New, found this pass — commit or discard the two files already sitting modified in the
   working tree.** `app/build_dashboard.py`'s reconciled-path fix (see this version's header) is a
   real, verified bug fix and should be committed on its own, not lost. `00_SESSION.md`'s
   `library`-governance-tier addition looks like it belongs to a different project's workflow
   (`Best Practices`) and needs a human decision, not an assumption, before it's committed here.

**Done since v2.10 (2026-08-18 → 2026-08-19):** `domain_coverage.json` regenerated and re-agrees
with the live spine (73 uncovered, was stale at 199) — the only work this pass did. Pipeline totals
(49 `promotion`, 0 `readiness`, 0 `verified`) confirmed unchanged by a live re-run, not assumed.

**One line:** nothing shipped this pass except making one read-model file stop lying about a number
— the project is exactly where v2.10 left it: 15 cases ready to run, zero run yet, and two
uncommitted files in the working tree worth a deliberate decision before the next session inherits
them silently.

---

### As of v2.10 · 2026-08-18

**Now, in order:**
1. **A3 — first `VERIFIED` case.** Still the single blocking fact — no case in this system has run
   with real learners. The pool of genuinely `TIER2_PASS`/`published` candidates just grew from 5 to
   **15** (the original five plus this pass's ten), so the choice of which case runs first is wider,
   not the blocker itself. This is calendar work, not engineering work, and remains the one thing
   nothing in this pipeline can do for itself.
2. **Fix `case-publish`'s promotion snippet for the "already in `cases[]`, still need to flip
   `status`" case** (new — see this version's header). The documented script's idempotent-stop path
   correctly does nothing when a title is already in `standards_spine.json.cases[]`, but a case in
   that exact shape (a legacy conversion, already spine-tagged, freshly reaching `TIER2_PASS`) still
   legitimately needs its `status` flipped to `published` — the gap between those two facts is
   exactly what produced this pass's 62/77-skill data-loss regression when an agent wrote ad hoc
   logic to bridge it. Write the explicit path into `SKILL.md`'s own script rather than leaving the
   next promoting agent to reinvent it.
3. **Write C5 (The Reserve Asymptote) next**, per the Track B update above — highest-value concept
   in the current queue, closes two full zero-coverage groups (11 skills) in one case, HIGH
   feasibility, untapped career (actuarial analyst). Re-scope C7/C8 first (see Track B) before
   anyone writes those two specifically — C9 is moot, drop it.
4. **Regenerate `readmodel/domain_coverage.json`.** Flagged stale in this pass (`199` uncovered
   there vs. the spine's real `73`) but not fixed — out of scope for what this pass was asked to do.
   Whoever picks up B4/the concept queue next should regenerate it first rather than read stale
   `uncovered_skills_still_orphaned` numbers.
5. **A regression net over the admin core.** Unchanged from v2.9 — `admin_core.py`,
   `store_postgres.py` and `admin_web/app.py` still have zero automated tests.
6. **Real auth (MCS-44).** Unchanged from v2.9 — one shared passcode still guards write access to
   real learner data with no per-user identity.

**Done since v2.9 (2026-08-12 → 2026-08-18):** the ten `readiness`-stage cases re-verified against
live gate scripts rather than trusted at self-report — 5 were already clean, 5 needed real fixes
(2 stale-published-artifact rebuilds, a full 5-probe Tier 2 run for `family-trip`, a real
propagation bug and two real P6 citation defects found and fixed, one case's packet built from
scratch including its first-ever case-#2 proof of the A7 interactive-HTML shell) — all ten now
genuinely `TIER2_PASS`/`published`; a real `standards_spine.json` data-loss regression found (via
the promotion script's own snapshot safety net) and fixed; `uncovered` 81 → 73.

**Ongoing:** E5 override watch · E3 discussion participation (still the least-instrumented of the
seven rubric criteria, and the one measuring the thing the format exists for).

**One line:** the ten-case backlog this pipeline itself created by outrunning its gate is now
actually closed, not just relabeled — every claim in the table above was checked against a live
script run, not a JSON field — and the project is back to the same one blocker it's had since
Cold Chain: no case has run with real learners yet.

### As of v2.9 · 2026-08-12

**Now, in order:**
1. **A3 — first `VERIFIED` case.** A real guide, a real room, a filled `RUN_REPORT`. The live app
   removed every technical excuse; this is calendar work now. Run it on one of the five
   `TIER2_PASS` cases (`plaza-pavers`, `company-front`, `vent-cap`, `apron-order`, `survey-corner`),
   not on Cold Chain — those clear a higher bar.
2. **A8 — backfill the ten demoted cases** (new; see the v2.9 header). Sensitivity model + Tier 2
   run + QA report each, then re-promote via `case-publish`. Until then they are correctly
   unassignable.
3. **Close MCS-41 at the gate.** `scripts/apply_publish_gate.py` sweeps after the fact;
   `case-publish` should refuse to stamp `published` below `TIER2_PASS` in the first place.
4. **A regression net over the admin core.** `admin_core.py`, `store_postgres.py` and
   `admin_web/app.py` have zero automated tests. Every production bug so far was caught by a human
   using the app (D-017, D-019, both MCS-45 failures). That has worked and does not scale.
5. **Real auth (MCS-44).** One shared passcode currently guards write access to real learner data,
   with no per-user identity — the audit trail records a typed name, not an authenticated actor.

**Done since v2.8 (2026-08-01 → 2026-08-12):** the local admin server (D-015) · the hosted
Vercel + Neon variant with a shared core across both transports (D-016) · the override-id collision
fix (D-017) · the public student case page (D-018) · the Assign-a-Case redesign (D-019) · the
publish gate written down and swept (D-020, MCS-41) · roughly fifteen more authored cases, the last
five at `TIER2_PASS` with full packets · A7's shell proven across every case · five doctrine rows
for the architecture that had none (MCS-41→45).

**Ongoing:** E5 override watch · E3 discussion participation (still the least-instrumented of the
seven rubric criteria, and the one measuring the thing the format exists for).

**One line:** the pipeline got good enough to outrun its own gate, the gate is now written down and
enforced, and the only thing left between this system and Phase 3 is putting one case in front of
real students.

### As of v2.8 · 2026-08-01 (historical)

**Now:** A3 (first VERIFIED case — needs a real guide and room, the one thing this pipeline cannot do for itself)
**Done since v2.7:** A1 · A2 · A7 (interactive-HTML scaffold) · B1 · B2 (spine extended) · C3 (Drive intake designed)
**Next:** prove A7's shell and C3's Drive intake against something real — either counts as case #2/first-real-submission groundwork — · E3 · D1
**Ongoing:** E5 override watch · A4 wiring

**One line:** fix the case the gate caught (done), tag the untagged cases (done), extend the spine and scaffold the tooling case #2 will need (done) — run one case with real learners is still the one blocker nothing in this session could close, and everything else now genuinely waits on it.

---

<details>
<summary><strong>v1.0 — shipped 2026-07-31 (historical record)</strong></summary>

| Deliverable | Notes |
|---|---|
| `SPEC.md` v1.0 | Case anatomy, balance test, 4 tiers, facilitator artifacts §7, Definition of Done |
| `standards_spine.json` | 322 atomic skills, 8 domains |
| `curriculum_tree.json` | 4 phases, 10 branches, prereq graph |
| `corpus_index.json` | 56 cases with asset manifests |
| Six pipeline skills | brainstorm → write → research → qa → publish → track |
| `dashboard.html` | 5 views, 46 self-checks |
| **Cold Chain** | First pipeline case. T3. Closed 3 zero-coverage skills |
| Doctrine | DOCTRINE_LEDGER (20 rules), DECISIONS, README |

Added later the same day: `domains.json` (40 domains, 121 live-verified sources) · `RUBRIC.md` · `case-readiness` (3-tier gate) · `submission-score` · `PROCESS_TRANSFER.md` · dashboard v2 (140 checks, 7 tabs, `student.html`) · DOCTRINE_LEDGER to 35 rules.

</details>
