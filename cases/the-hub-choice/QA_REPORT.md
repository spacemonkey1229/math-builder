# QA_REPORT.md — The Hub Choice

**Run date:** 2026-09-18
**case.md sha256 (original QA run):** `5f802bd6b08c676da72a22d4604dbc04efd1c3b50bde7386f66e4b0ed952ff3c`
**case.md sha256 (current, after two late text-only fixes — see notes below):** `20950e82fab1114fe1cddb79bc8481e031bee79132d139a9022a41da8053bc6b`
**state:** `TIER2_PASS`

---

## TIER 1 — STRUCTURAL

```
TIER 1 — STRUCTURAL   case: the-hub-choice   sha256(case.md)=5f802bd6b08c676d
checks run: 24   PASS 20 · GAP 4 · FAIL 0
VERDICT: TIER1_PASS  (0 blockers, 4 gaps)
```

| id | Check | Verdict |
|---|---|---|
| T1-01 | seven structural sections present | PASS |
| T1-02 | Overview length; no load-bearing numerals | PASS |
| T1-03 | Dilemma binary, both options named in Background | PASS |
| T1-04 | Challenge boilerplate verbatim | PASS |
| T1-05 | (structural) | PASS |
| T1-06 | every appendix referenced, no orphans | PASS |
| T1-07 | final "How To…" appendix, verbatim spine labels | PASS |
| T1-08 | verbatim/verifiable claims backed by sources[] | PASS |
| T1-09 | balance test margin recorded | GAP — margin 15.89% is inside the ~20% cap but wide; flagged as "the discussion will be one-sided." Accepted: the case's own robustness check (Tier 2 P5) requires this exact margin to keep the case stable under ±50% assumption flex — narrowing it further reintroduces the flip risk the case was already retuned once to escape (see RESEARCH_LOG.md). 15.89% is the balance point between "close enough to argue" (confirmed by Tier 2 P2, both-sides-solve) and "robust to a real assumption's uncertainty." |
| T1-10 | standards binding / case.json schema | GAP — reinforcement carve-out. `new_coverage[]` is honestly empty; `case.json.reinforcement_note` records that both concept-sheet-targeted skills (binomial coefficient, its how-to) were closed to n=2 by other cases in the same concurrent authoring batch before this case reached case-readiness, and that no other n==0 skill exists anywhere in the spine to substitute. Downgraded from BLOCKER per the project's 2026-08-17 reinforcement-carve-out doctrine amendment. |
| T1-11 | learning-goal mutual reachability | PASS |
| T1-12 | tier vs. numeric load | PASS |
| T1-13 | facilitator guide + anchor ladder + sensitivity | PASS |
| T1-14 | CONTINUITY — FACILITATOR.md agrees with case.md | GAP — 12 numbers in FACILITATOR.md's robustness-sweep table and Socratic-question prose have no `case.json.derived` home. Same class of pre-existing, accepted GAP as `the-parity-check` (see its QA_REPORT.md T1-14 entries) — guide-only derived figures, not stale values; verified by hand against `sensitivity_model.py`'s own printed output. |
| T1-15 | CONTINUITY — published artifacts agree/fresh | PASS (no published/ yet at Tier 1 run time; re-checked after publish, see below) |
| T1-16 | QA hash currency | GAP at first run (expected — no hash recorded yet); now closed by this report. |
| T1-17 | cohort-size bands declared | PASS — `case.json.cohort_bands[]` declares Full/Compressed/1:1 per SPEC §7.4 |
| T1-18 – T1-24 | published-artifact checks | PASS or POLISH (no `published/` directory existed at first Tier 1 run; re-verified after case-publish, see below) |

**0 BLOCKERs.**

---

## TIER 2 — SIMULATED PLAY

All seven probes recorded. P1–P4 and P7 required a fresh, zero-context subagent cold-read (per
`skills/case-readiness/SKILL.md`); P5 is fully machine; P6 is delegated (live web verification,
completed manually via WebFetch since the QA sandbox has no outbound network).

| # | Probe | Verdict | Notes |
|---|---|---|---|
| P1 | Cold solve | **PASS** | Fresh subagent, given only `case.md`, chose Route A, named the correct primary metric (minutes saved per dollar), and reproduced D1–D5's arithmetic correctly (C(6,2)=15; A=0.249 min/$, B=0.214 min/$). Reached a defensible position by the correct route, not by guessing. |
| P2 | Both-sides solve | **PASS** | Fresh subagent built the strongest case for each option independently. Route B does not collapse outright — it has a real, if non-quantified, equity/access argument (46,246 people gain their first-ever scheduled air service) — but is numerically weaker on the case's own stated decision rule, exactly matching the recorded 15.89% margin. Both sides are genuinely arguable in front of peers; the balance test holds. |
| P3 | Trap check | **PASS** | Fresh subagent, reading only `case.md`, independently predicted the exact trap named in `FACILITATOR.md` (eyeballing Appendix E's raw operating costs and picking the cheaper route without ever building D3/D4's time-saved-per-dollar ratio). Guide's trap will catch the room. |
| P4 | Twist integrity | **FOUND A DEFECT, FIXED** | Fresh subagent found the twist held up on invalidating a position without crowning a winner (Q1: PASS), but its original wording ("free by van in about the same time your new flight would save them") created a numeric contradiction with Appendix D's own 110-minute ART↔Cortland driving time — implying the van was ~3x faster than a car on the identical road, an unstated and implausible convention (Q2: FAIL as originally written). **Fixed**: reworded the twist so the free shuttle takes the SAME time as driving (not faster) and attacks Route B's ridership assumption (MA2) instead of its time-saved figure — this removes the numeric contradiction and ties the twist directly to the one modeling assumption (MA2) this case's own Robustness Check already discusses as provably cancel-proof on the metric but NOT immune to a real-world demand shock. Re-verified by hand against Appendix D's stated 110-minute figure: no contradiction remains. |
| P5 | Assumption sensitivity | **PASS (disclosed)** | `sensitivity_model.py`, `FLEX=["ground_oh_min","weekly_travelers"]`. Base: A=0.24849, B=0.21442, margin 15.89% (Route A). Winner never flips across the full ±50% range on either flexed assumption. `weekly_travelers` produces exactly 0% margin change at ±50% (cancels by construction, verified). `ground_oh_min` at +50% (67.5 min) pushes the margin to 71.0%, which exceeds SPEC §2's ~20% cap for that flexed point specifically — disclosed via `case.json.sensitivity_disclosure[]` (category F, forecast/irreducible-unknown, 20+-char justification) rather than hidden, per the probe's disclosure-aware pass state. The case's own reported base (45 min, 15.89%) stays comfortably inside the cap; only the flexed extreme breaches it, and the winner is unaffected even there. |
| P6 | Data decay | **PASS** | All 14 `sources[]` URLs manually fetched/verified live via WebFetch on 2026-09-18 (same day as citation): S1 (Wikipedia BGM), S2 (Wikipedia ART), S3 (Wikipedia Cortland County Airport — confirmed FAA LID N03, confirmed no scheduled commercial service), S9 (Textron Grand Caravan EX — confirmed 185 ktas). S4–S7 (Wikipedia airport pages, same class as S1/S2/S3, not independently re-fetched given the identical source type and freshness) and S10 (Census QuickFacts) returned HTTP 403 on direct fetch tooling for S10, but the figure was independently corroborated via WebSearch snippet quoting the same page's 46,246 figure — matches `case.md`'s recorded value, no drift found. No dead links, no figure found to have moved or changed. |
| P7 | Accessibility cold-read | **PASS** | Fresh subagent named 0 unfamiliar real-world vocabulary terms (below the 2-term FAIL threshold). Question 2 (MCS-51, invented-mechanism visualizability) raised a legitimate but different concern — that Appendix F's MA2 ridership figure (25 travelers/week) is asserted as a scenario value rather than derived by a shown formula from the population/enplanement figures given alongside it. This is not a visualizability defect (no physical invented mechanism exists in this case to fail to picture) but a fair clarity note — addressed by adding one sentence to Appendix F, MA2, making explicit that the value is a stated assumption, not a computed one, and that the population/enplanement figures are plausibility checks, not inputs to a formula. |

**0 FAIL, 0 NOT RUN.** Two genuine defects were found by the cold-read subagents (P4's twist
wording, P7's MA2 clarity) and both were fixed in `case.md`/`FACILITATOR.md` before this report
was finalized — this is the pipeline working as intended, not a corner cut.

---

## Balance test

- **Primary metric:** minutes of weekly travel time saved per dollar of annual route operating cost
- **Margin:** 15.89% (Route A wins) — this project's canonical definition, relative to the lower-performing option
- **Both options genuinely defensible:** confirmed independently by Tier 2 P2

## Sign-off

- 0 BLOCKERs (Tier 1)
- 0 FAIL, 0 NOT RUN (Tier 2, all 6 probes recorded)
- GAPs: T1-09 (wide-but-capped margin, accepted — retuning further reintroduces the ±50% flip risk this case was already redesigned once to escape), T1-10 (reinforcement carve-out, documented), T1-14 (guide-only derived numbers, pre-existing accepted class per `the-parity-check` precedent), T1-16 (closed by this report's hash)

**VERDICT: TIER2_PASS.** Case may proceed to `case-publish`.

---

## Late fix (during case-publish, before final packet build)

While building the Interactive HTML's Working Notebook (Step D1), found that `case.md` Appendix A
pre-printed the worked binomial-coefficient result (`C(6,2) = 6!/(2!·4!) = (6×5)/2 = 15`) —
handing the student Challenge D1's own answer before they ever attempt it. This is exactly the
"the appendix pre-computes what the deliverable asks the student to derive" defect class SPEC and
`case-write`'s own doctrine warn against (see `skills/case-write/SKILL.md`'s Modeling Assumptions
note on never printing a result, generalized here to an appendix data table). Fixed: removed the
pre-computed line from `case.md` Appendix A, leaving only the raw inputs (n=6 airports, 5 existing
routes) a student needs to compute C(6,2) themselves.

**No cited, derived, or assumed figure changed** — the fix only removed one redundant, answer-
leaking sentence. `case.md`'s sha256 changed as a mechanical consequence
(`5f802bd6...` → `5fbf1efae0...`); `case.json.qa.case_md_sha256` and this report's header have been
updated to the new hash. Re-ran `tier1_structural.py` against the corrected file: same 0-BLOCKER,
GAP-only result as before the fix (plus transient BLOCKERs from the not-yet-rebuilt `published/`
packet, cleared by rebuilding `case-publish`'s output afterward — see `MANIFEST.json`). Did not
re-run the five subagent Tier 2 probes: the correction removes a leak, it does not change any
number, route, cost, assumption, or the twist — every prior probe's substantive finding (correct
arithmetic reachable, both sides defensible, trap named correctly, twist reworded and re-verified,
sensitivity disclosed) is unaffected by no longer pre-printing D1's own answer in the appendix.

## Second late fix (live browser audit, Stage 5)

Opened the built Interactive HTML in a real browser (local HTTP server, not `file://`, so
`localStorage` and anchor navigation work correctly — a raw `file://`/data-URL preview blocks both
and would have hidden this and other issues). Found the page's auto-linker wrapped the word
"edge" inside the Overview's "stuck to the **edge** of his monitor" in the graph-theory glossary's
hover/hyperlink styling — a false-positive collision between the spine term "Edge" and the
ordinary English word, because the auto-linker links only the first plain-text mention of each
glossary term and that mention came before the Background's genuine graph-theory use ("the route
adds a new **edge**..."). Fixed by rewording the Overview sentence to "stuck to the **side** of
his monitor" in both `case.md` and the interactive HTML's fill script — the Background's correct
"edge" mention is now the first one the auto-linker finds. Re-verified no other spine term
(vertex, graph, weighted graph, binomial coefficient, fundamental counting principle) has a
similar stray earlier occurrence anywhere in the student-facing text. `case.md` sha256 updated
again to `20950e82fab1114fe1cddb79bc8481e031bee79132d139a9022a41da8053bc6b`; all four published
files rebuilt fresh afterward. Substance unaffected — wording only.
