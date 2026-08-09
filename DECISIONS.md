# Decision Log — Math Builder

**Append-only.** Never edit or delete a row; supersede it with a new one.

---

### D-001 · 2026-07-31 · Standards spine is inherited, not invented
Extracted the school's own 8-sheet standards workbook into `standards_spine.json` (322 atomic skills) rather than authoring a new taxonomy. **Why:** the school's coverage matrix already encodes years of judgment about what belongs; replacing it would orphan 27 cases of tagging. **Cost:** the spine has real gaps — no Pre-Calc, Calculus, or Discrete rows. Accepted; extending it is Phase 2.

### D-002 · 2026-07-31 · Both skills-pipeline AND tracker app
User chose both rather than either. **Why:** authoring and operating are different jobs on different cadences. Skills produce; the app observes. **Cost:** two artifacts to keep in sync — mitigated by making the app a pure derived view (`build_dashboard.py`), never a source of truth.

### D-003 · 2026-07-31 · Gap-driven authoring, MS + HS
Target zero-coverage skills rather than deepening covered ones. **Why:** 100 of 322 skills had no case at all; badge volume can come later from cases that also close gaps.

### D-004 · 2026-07-31 · Cold Chain chosen as the proof case
Picked to close Geometry `Prism` and Advanced Operations `Absolute Value` / `How to evaluate an absolute value expression`. **Why over a Transformations case** (the larger 20/20 hole): the WHO PQS catalogue offers five real containers whose surface-area-to-volume ratio maps monotonically onto published cold life — a genuine empirical finding, not a contrived setup. Transformations remains the #1 authoring gap and is the next pick.

### D-005 · 2026-07-31 · Dry ice excluded from the Cold Chain case
Research surfaced good dry-ice data, but dry ice is for −70 °C ultra-cold chain, not +2–8 °C routine vaccine. **Why:** using it would have been physically wrong and a knowledgeable reader would catch it. Kept out entirely rather than as a distractor.

### D-006 · 2026-07-31 · "Up to 50% of vaccines wasted" excluded, not caveated
Widely repeated; traces only to a UNEP secondary attribution and conflates open-vial and expiry wastage with temperature failure. **Why excluded rather than footnoted:** a caveated bad number still ends up in student pitches. Replaced with the concrete sourced framing that a $128 box protects $3,200–$4,000 of vaccine. Codified as MCS-18.

### D-007 · 2026-07-31 · Two modeling assumptions stated in the open
No published source gives a per-lid-opening cold-life penalty or a °C/hour warming curve. Rather than quietly picking numbers or abandoning the case, both are declared in Appendix F with their reasoning, and students are invited to disagree and show what changes. **Why:** this *is* the HS-band skill — modeling under missing data.

### D-008 · 2026-07-31 · Case rebalanced by changing a constraint, not hiding data
First construction had Order B winning by 22.5% — outside the balance threshold. Fixed by setting the container budget at $320 (which lets Order A buy three boxes, not two) and adding the cold-life opening penalty. Margin fell to 11.0%. **Why this way:** SPEC forbids fixing balance by withholding data from students.

### D-009 · 2026-07-31 · Mid-session: corpus is 55 cases, not 27
Y1–Y3 uploads revealed the standards matrix tracks only 27 of 55 real cases; 31 have no standards row and 5 matrix columns have no source folder. **Consequence:** the "uncovered skills" count is an upper bound, and reconciliation is now a distinct backlog from authoring. Codified as MCS-17. **Open:** no skill owns reconciliation yet.

### D-010 · 2026-07-31 · Facilitator artifacts promoted into SPEC after the corpus arrived
The Y1–Y3 Guide Notes (39 of them) revealed a consistent five-anchor Socratic ladder and a Twist mechanic that the six exemplars alone did not show. SPEC §7 was written from them and the Definition of Done extended. **Why it matters:** the written case is only half the artifact; the discussion is where the learning lands.

### D-011 · 2026-07-31 · Curriculum tree added as a second spine
User supplied a four-phase MS→university Tree of Thought mid-session. Stored as `curriculum_tree.json` and joined to the legacy spine through `acton_domains[]` rather than merged. **Why kept separate:** the tree is a *pedagogical sequence* with prerequisites; the spine is an *atomic skill inventory*. Merging them would lose the dependency edges. The join exposed that three branches have no standards rows at all.

### D-012 · 2026-07-31 · The 3-item `intersections[]` is superseded, not deleted
Phase 4 of the curriculum tree ("Root Connections") shipped as three lines — Physics, Computer Science, Finance — which is not an input to brainstorming, it is a decoration. Replaced with `readmodel/domains.json`: 40 first-class application domains across 12 clusters, each carrying validated spine skill ids, curriculum branch ids, verified free data sources, decision archetypes and a career layer with specific mathematics named. **Why 40 and not 3:** the brief for a case is "a binary decision under constraint with real cited data" — that requires knowing, before writing, whether the data exists and which uncovered skill the domain forces. Three abstractions cannot answer either question. **Why superseded rather than deleted:** `curriculum_tree.intersections[]` is read by `build_dashboard.py`; it now holds 40 derived pointers into `domains.json`, and the original three survive verbatim as `legacy_intersections[]`. Codified as MCS-22.

### D-013 · 2026-07-31 · Every source URL was fetched before it was written down
121 unique URLs across the 40 domains were retrieved and their rendered content inspected before being recorded; each carries a machine-readable verification state. Eleven candidates failed on first attempt — FAOSTAT and USDA Quick Stats are JavaScript-only, IAEA PRIS now redirects behind registration, OxCal's web version wants a login, `freesewing.org` moved to `.eu`, Stooq blocks scripted access, the Universal Robots UR5 page was withdrawn — and each was either replaced with a verified alternative or downgraded and flagged in that domain's `data_availability.note`. **Why this mattered enough to be a rule:** a fabricated URL in an authoring input propagates into a student-facing appendix and is discovered by the student. Codified as MCS-21, enforced by `app/validate_domains.py`.

### D-014 · 2026-07-31 · Data availability is graded honestly, including down
Ten of the 40 domains are graded MEDIUM rather than HIGH, and the reason is stated per domain rather than smoothed over. The pattern is consistent: the *geometry* is free and the *cost* leg is not. Manufacturing nesting has benchmark instances and sheet-stock sizes but no public library of real factory parts; drill choreography has the exact field grid and public DCI scores but no obtainable drill chart; construction has permits and design loads but RSMeans unit costs are paid; tiling has public-domain pattern imagery but no central tile pricing. **Why grade down rather than pad the source list:** MEDIUM tells the case author to plan for a declared modelling assumption. A padded HIGH sends them looking for a dataset that does not exist. No paid source (IFR World Robotics, RSMeans, Ethnologue, Clarksons) is listed as a source anywhere — they are named in notes as paid, so nobody re-discovers the dead end.

### D-015 · 2026-08-08 · A local-only admin server, for writes only
"Managing students" (assign a case, record a submission, log discussion participation, run the
machine scorer, confirm a guide review, mark complete, award a badge) requires real writes to
`readmodel/roster.json`/`submissions.json` and real subprocess calls to `score_submission.py` /
`guide_confirm.py`. A static `file://` page — the entire rest of this stack — cannot do either.
Added `app/admin_server.py`: a stdlib-only Python HTTP server, binding to `127.0.0.1` only, serving
one page with a JSON API that is a thin, direct wrapper over the exact rules already documented in
`skills/case-track/SKILL.md` and `skills/submission-score/SKILL.md` (same eligibility checks on
assign, same state machine, same "never auto-grade, never auto-award a badge" limits) — no new
policy, just a UI for policy that already existed and was previously only executable by an agent
editing JSON by hand. **Why this doesn't violate TECH_STACK.md's "no server" line:** that line was
about the guide/student *dashboards* needing no install, no login, no deploy to be opened by
anyone. This server is local-only, single-operator, no auth (same as the rest of the stack has no
auth), nothing is hosted, and it changes nothing about how `dashboard.html`/`student.html` work —
they remain pure derived views, generated from the same JSON this server writes to. **Cost:** a
second thing to run (`python3 app/admin_server.py`) instead of just opening a file; accepted, since
the alternative was either no self-serve student management at all, or reinventing multipart file
upload and subprocess execution inside a browser sandbox, which isn't possible. **Open:** still no
non-technical-facilitator-friendly packaging (a double-clickable app, a background launchd job) —
today it's a command run from a terminal, same operator-comfort bar as everything else in this
project.
