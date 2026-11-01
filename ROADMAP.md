# Roadmap — Math Builder

**Version 3.2 · 2026-10-24.** Purpose: students experience math in the real world; direction: **tool → product → platform** (see [VISION.md](VISION.md);
requirements in [PRD.md](PRD.md), cited here as R1–R7). Triggered by the first outside-user
feedback (Anuj, 2026-10-17). Full reasoning trail for older numbers lives in
[ROADMAP_HISTORY.md](ROADMAP_HISTORY.md).

This file has three parts: **(1)** the product roadmap — priorities, phases, parking lot;
**(2)** reminders and open questions; **(3)** the content-pipeline status carried forward from
v2.19, unchanged and dated 2026-09-06 (re-derive every count before trusting it — see
00_SESSION.md).

---

## 1. Product roadmap

### The ordering logic

**First deployment: The Humanist Academy.** The goal is to run the platform there, then take the guide out of
assigning, tracking and chasing so the guide can focus on hard concepts and getting Heroes started. That
makes **guide-free operations (R13)** a priority ahead of leaderboard polish.

Zero cases are `VERIFIED`; no real cohort has ever used the system. So the order is:
**fix what the first outside user hit → put real kids through it (with instrumentation) → add the
coach → add submit/grade → add recognition → harden → generalize.** Every phase ends with a gate
tied to real use, not to code being written.

### Strategic tracks (run alongside the feature phases)

Feature work below answers "what do we build." These answer "should we, for whom, and how do we
know" (see VISION.md → Strategy). Each has an owner-decision, not just tasks.

| Track | What | First step | Gate it informs |
|---|---|---|---|
| **S1 Discovery & demand** | **The Humanist Academy first:** program structure, cohort size, grade levels, how the guide runs assignment and tracking today, tools in use, what the guide wishes they had time for. Then ~5 conversations: Anuj, Acton guides/heads, 1–2 homeschool parents (what they'd switch for, what worries them about kids + AI) | Reply to Anuj; ask for an intro to the Humanist Academy lead | Guide-free operations design (R13), pricing, Acton integration |
| **S2 Landscape scan** | Map adjacent products and what Anuj saw in marketing-tech stacks; write one-page differentiation | Research task + Anuj's comparisons | Positioning; what *not* to build |
| **S3 Trust & safety foundation** | Data policy for minors, vendor terms, leak/injection test design, cost cap | Draft policy; pick vendor candidates | Any AI feature touching a child |
| **S4 Quality systems** | Turn one-off case defects into gates: instruction-clarity lint, cold-read at authoring time, step-level confusion data feeding case-readiness | Sweep published cases for the `phone-plan` defect classes; propose ledger rows | Scale of the library |
| **S5 Economics** | Track AI cost per learner-case from pilot 1; model unit economics for 2–3 business-model options | Instrument cost logging in Coach v1 | Business model |

**Status 2026-10-23:** `phone-plan` reference fix is done and re-verified (commit `7fe1a04`:
Step 4/twist follow the chosen line count, glossary + worked example added, all 7 Tier 2 probes
pass). It is the *template* for S4, not a roadmap item in itself; backlog rows 1–2 below are now
"sweep + lint," not "fix phone-plan."

### Prioritized backlog (Anuj's feedback + known gaps)

Score = value to a real learner/guide × confidence, against effort. S ≈ days, M ≈ 1–2 weeks,
L ≈ multi-week. (Estimates are rough; re-size at phase start.)

| Rank | Item | Req | Effort | Why this rank | Phase |
|---|---|---|---|---|---|
| 1 | ~~Fix `phone-plan` instructions~~ **Done 2026-10-23** (reference fix, `7fe1a04`) | R1 (F2, F4) | — | Template for the sweep below | 0 |
| 2 | Sweep all published cases for the `phone-plan` defect classes (unstated tax/scenario, pinned twist, undefined vocabulary) + wire the lint/cold-read as gates (**Track S4**) | R1 | M | Same classes likely elsewhere; gates stop recurrence (needs ledger rows) | 0 |
| 3 | **Run a real case with Anuj's kids** (Track A3) with "This was confusing" feedback control | F9, R6 | S | The #1 blocker for the whole project; Anuj volunteered | 0 |
| 3a | **Event log foundation** (every attempt, hint, reveal, submit as a row) | R9 | M | Everything after depends on it: coach, analytics, calibration, cost, efficacy | 0 |
| 4 | Identity + consent groundwork (signed assignment links, data policy) | R5 | M | Gate for any AI feature touching a child | 1a |
| 5 | **Coach.AI v1**: dialogue per step, misconception catalog + hint ladder; pilot on the 3 cases | R2 (F1, F3) | L | Highest learner value; deterministic-first keeps it cheap and safe | 1a |
| 5a | **Pilot readiness** for 3 cases (checklist in §2): fix data labeling, catalogs, skill tags | R1, R2 | M | R1b/R1a found blockers in each candidate | 0–1a |
| 5c | **Readiness on-ramp**: case-scoped warm-up + word-problem scaffold, pilot skills only | R12 | M | Sets Heroes up for the case; feeds the guide's skill view; test vs. no warm-up | 1a |
| 5b | **Revised rubric K1–K6** and a blind guide-graded gold set | R3 | M | Decided; must exist before AI feedback is shown | 1b |
| 6 | One-click **Submit** + server-side numeric scoring + per-step results | R3 (F5) | M | Replaces export-and-hand-over; unlocks guide time savings | 1b |
| 6a | **Guide-free operations**: auto-assign (build on `suggest_cases`), auto-track and remind, parent/guide digest, exception-first guide home | R13 | L | The primary goal of the Humanist Academy deployment | 1c |
| 6b | **Home and next step**: one action per screen, weekly rhythm, in-app nudges | R14 | M | Navigation, consistency and compliance without guide chasing | 1c |
| 7 | **AI feedback on notes/pitch** (provisional, guide confirms) + calibration against gold set | R3 (F5) | L | Needs gold set and RUBRIC calibration first; do after #6 | 1b |
| 8 | **Journey tracker, points, profile and a simple leaderboard** (completed cases + pitch depth); recommended next assignment | R4, R5 (F6) | L | Decided by Manan; points from the event log; effort and depth, not speed | 2 |
| 8a | **The room as a product surface**: stuck summary, vote/twist/re-vote, cold-call roster, timer | R8 | L | The Socratic discussion is half the product; guides are the buyers | 2 |
| 9 | Guide analytics: stuck-heatmap per step; feed into case-readiness | R6 | M | Closes the loop from kids to case quality | 2 |
| 10 | Per-user accounts, parent view, automated tests for the admin app | R5 | L | Real login is long-standing Housekeeping; tests are zero today | 3 |
| 11 | Acton integration discovery (what does "the whole Acton system" mean?) | F8 | S to scope | Can't size until Anuj describes the surface | 3 |
| 12 | Engine/content seam; science pilot; later a subjective subject | R7 (F7) | L | Only after the first product loop is proven with real kids | 4 |
| 13 | **Author surface**: guide-authored cases through the same gates | R10 | L | The other half of "platform"; prototype with Anuj/an Acton guide | 4 |
| 14 | Authentic-work design: reasoning-trail grading, paste-detection flag | R11 | M | Required before AI grading is trusted; ships with Phase 1b | 1b |

### Phases and exit gates

**Definition of done (applies to every phase item):** built, **tested** (automated: Tier 1/2 for cases, unit/integration for the app) and **UAT tested** (live browser, walking the real flow as each persona: Hero, guide, parent). A phase's exit gate is not met until all three are reported; anything not run is stated plainly.

**Phase 0 — Fix and observe (now → ~2 weeks)**
- Do: backlog #1–3, 3a, 5a. Event log; pilot-readiness fixes for the 3 pilot cases; instrument the case page so confusion is captured, not emailed.
- Exit gate: pilot cases pass their readiness checklist (ROADMAP §2) and Tier 1/2 **and a live browser pass**; sweep list produced;
  at least one real learner has attempted a case and their confusion points are logged. (This
  also satisfies Track A3's "first real learner.")

**Phase 1a — The Coach (~weeks 3–8)**
- Do: #4, #5. Per-assignment signed links; parent consent email naming the vendor and data; Coach.AI dialogue UI with misconception catalog + hint ladder; model for the long tail;
  leak and injection test suites; paid-account server-side key, spend cap and kill switch.
- Exit gate: leak test and injection test at **0 failures** on the pilot case; pilot learners
  use hints; catalog match rate and hint helpfulness measured (set targets from the pilot).

**Phase 1b — Submit and grade (~weeks 6–12, overlaps 1a)**
- Do: #5b, #6, #7. Revised rubric K1–K6; Submit; deterministic numeric scoring; end-of-case summary (written or spoken per case) with AI feedback (provisional);
  gold-set calibration.
- Exit gate: guide–AI agreement meets the bar agreed in PRD §R3 for the criteria being drafted;
  guide still confirms every badge. Until the bar is met, AI feedback is shown to the guide only,
  not to learners.

**Phase 1c — Run itself: guide-free operations (~weeks 8–14, overlaps 1b)**
- Do: #6a, #6b. Auto-assign from the journey with guide override; auto-track, in-app reminders, parent/guide
  digest; exception-first guide home; Hero home with one next step. **Run the Humanist Academy cohort.**
- Exit gate: for the cohort, assignment, tracking, reminders and reports run with no guide action; guide
  minutes on operations fall and minutes on concept help rise (measured from the event log); no exception
  missed in a two-week audit. If operations minutes don't fall, fix before widening.

**Phase 2 — Journey, incentives, and the room (~weeks 12–18)**
- Do: #8, #8a, #9. Journey tracker, profile and history; points (now including persistence and skill improvement) and the simple leaderboard (opt-in, cohort-scoped); guide skill view with suggested focus; Heroes' case feedback; per-step stuck data to guides and to the authoring side.
- Exit gate: depth of pitches does not fall as volume rises (leaderboard is driving depth, not just completions); return use up vs. Phase 0; at least one case revised because of step-level or Hero feedback.

**Phase 3 — Harden and connect (after a real cohort completes)**
- Do: #10, #11. Accounts/SSO, parent view, admin tests; Acton integration discovery with Anuj.
- Exit gate: first case reaches `VERIFIED` (filled RUN_REPORT from a real cohort, MCS-29).

**Phase 4 — Platform**
- Do: #12. Extract engine/content seam; science pilot; then a rubric-judged subjective subject
  with source-grounding rules.
- Exit gate: a non-math case runs end-to-end on the same engine, authored by the pipeline,
  graded with calibrated agreement.

### Parking lot

Ideas worth keeping, **not scheduled**. Each lists what would pull it forward.

| Idea | Source | Why parked | Pull-forward trigger |
|---|---|---|---|
| Peer-voted "best pitch" / hall of fame | spin-off of F6 | Needs a cohort and moderation | After first cohort completes 3+ cases |
| Adaptive next-case recommendation from skill spine | existing data | Needs mastery signal from real use | After Phase 2 data |
| Parent weekly digest | PRD persona | Needs accounts and consent | Phase 3 |
| Voice hints / read-aloud | accessibility | Nice, not core | Learner need observed in pilot |
| Per-character secret info forcing collaboration | existing Engagement idea | "Most interesting unexplored idea" — needs multi-learner session design | After the single-learner loop is proven |
| Tempting-wrong-answer design as a first-class case feature | existing Engagement idea | Synergy with the misconception catalog; could become an authoring input | After Coach v1 — author with the catalog in mind |
| Live-data cases | existing Engagement idea | Needs a deliberate decision (memory: prefer real, live, student-explorable data portals) | Independent track; revive with next content batch |
| LTI / Google Classroom export | possible Acton integration | Surface unknown | After Acton discovery (#11) |
| Marketing-tech-stack comparisons | Anuj's offer | Not yet received | When Anuj shares (see Reminders) |
| Multilingual cases/hints | not requested | No signal | Only if a cohort needs it |
| Printed-packet check, Drive publish | existing open items | Content track (below) | Content track |

---

## 2. Decisions, pilot, vendor and policy (updated 2026-10-23)

**First deployment (Manan, 2026-10-24):** run the platform at **The Humanist Academy**, then remove the guide from
assigning and tracking so the guide focuses on hard concepts and getting Heroes started. Second feedback round
weighed in PRD §2b (warm-up, independence, navigation, consistency, gamification, pitch shape adopted or adapted).

**Decided by Manan:** (1) build a rubric that matches our goals (K1–K6 proposed, PRD R3); (2) a simple
leaderboard (PRD R4); (3) recommended assignments linking week to week (PRD R5 profile); (4) pilot
**3 cases**; (5) a preliminary, non-restrictive policy (POLICY_PRELIMINARY.md v0.2).

### Pilot: 3 cases (recommendation, after R1a/b/c review)

No single trio came back clean. Findings by seat (full detail in the review notes):

| Case | Field | R1a (math/coach) | R1b (sources/data) | R1c (engagement/corpus) |
|---|---|---|---|---|
| `phone-plan` | Consumer finance | **Most coachable**; catalog drafts now | State tax stated as fact, 8% unsupported by the cited page; carrier prices are fictional | Anuj already used it; domain over-mined; keep as returning-user control |
| `field-watch` | Ag-tech / remote sensing | Hardest to coach; one-reading flip needs a probe | **Authored NDVI readings are presented as real satellite data** (blocking as written) | Strongest hook; zero existing remote-sensing cases |
| `creek-span` | Civil engineering | One option effectively dominant under any plausible labor value | Steel price will decay; table labeled "current" is a 1989 edition | Heavy reading load; teacher note on safety |
| `tide-window` *(R1c's swap)* | Oceanography | not checked | not checked | Zero existing cases, high data rating, "prediction published years ahead" hook |

**Recommended trio:** `phone-plan` (first coach catalog; returning-user control), `field-watch` (best
hook, after fixes below), and `tide-window` (new field; needs the same three checks). **Drop
`creek-span`** from the pilot: its balance is one-sided in substance. This is a recommendation for
Manan's call.

**Pilot-readiness checklist (per case, Phase 0–1a):**
- `phone-plan`: relabel the 8% as a stated assumption with the real-rate caveat (verify at
  tax.idaho.gov); label carrier prices as invented; draft misconception catalog (R1a listed 4 wrong
  methods with numbers).
- `field-watch`: relabel NDVI readings as modeled, or source a real series; fix the "every 5 days"
  wording (ESA: every spot on Earth); add a reading-flex sensitivity probe; define the buffer sign.
- `tide-window`: run the R1a coachability, R1b data, and R1c engagement checks before committing.
- All three: define the margin basis in each D-step (cases divide by different values); tag each step
  with its core skill (R1a: step_id, deliverable_id, primary_skill, process_tag, misconception_ids[]).
- None of these cases should be used to test the coach until its misconception catalog exists.

### Model vendor, budget, key (plain words)

- **Vendor:** the company whose model answers Coach.AI and writes feedback drafts.
- **Budget:** billed per token, so it needs a hard cap.
- **Key:** the secret credential that lets our server call the vendor and charges the account.
  Whoever holds it can spend money and read the traffic.
- **Cost is not the constraint.** From pricing pages R1b fetched on 2026-10-23: per learner-case about
  **$0.003–0.005** on Claude Haiku 5.5, **$0.065–0.10** on Sonnet 5.5 (assumptions: ~24k input and ~5k
  output tokens per case). A pilot month of 30 learner-cases is roughly **$0.10–0.15 on Haiku, $2–3 on
  Sonnet**, about five times that with testing. Re-check prices before launch.
- **Recommendation:** paid API account, owned by the operator personally (not a shared studio account);
  Haiku 5.5 for the coach, Sonnet for the grader only if tests show Haiku is too weak; one server-side
  env var per environment, marked sensitive, never in page code, logs or repo; hard monthly spend limit
  in the vendor console plus app-side per-learner and per-day caps and a kill switch; rotate on suspected
  exposure and at each phase. **Data terms matter more than price:** Anthropic does not train on
  commercial customer content and keeps data about 30 days by default; zero retention is not self-serve.
  Not verified by R1b: Anthropic's minimum cacheable prompt length, console spend-limit UI, and Vercel
  sensitive-variable behavior.
- **Decision for Manan:** who owns the account and holds the key (recommended: Manan personally for the
  pilot).

### Preliminary policy

POLICY_PRELIMINARY.md v0.2 is deliberately light and does not restrict the platform. R1b's fact-check
changed it: a parent's "OK" email is not enough because a child's text is sent to an AI vendor, so
consent must name the vendor and the data sent; zero retention is not self-serve; an opaque id is still
personal information; free text needs a warning and a scrub; parents can refuse further collection;
FERPA likely doesn't apply to a private pilot but COPPA does. Not legal advice; counsel review before
any non-pilot use.

### Reviewer flags worth your attention

- **Leaderboard:** R1c recommends showing the two counts separately rather than a summed score and
  keeping the pilot view to the cohort and guide (not public). PRD R4 adopts cohort-scoped, opt-in,
  alias-default, with points as an effort/depth tally. Your call on sorting and points.
- **Rubric:** R1a recommends demoting visuals and discussion to growth-only and never scoring
  confidence, curiosity, or hint counts (PRD R3).

**Reminders**
- **Find out about The Humanist Academy** (program, cohort, grade levels, current guide workflow, tools). The repo only lists it as a school in the Acton Survey case data.
- **Reply to Anuj:** thank him; the instruction issues are fixed; accept his offer to test with
  kids (this is Ring 1); ask what "integrate into the Acton system" means in practice; ask for 2
  introductions; ask for the marketing-tech comparison ideas he offered to share.
- Governance: new rules need a DOCTRINE_LEDGER row and critique pass; stack changes update
  TECH_STACK.md in the same pass; AI features touching children's work are D-021-class decisions.

---

## 3. Content-pipeline status (carried forward from v2.19, as of 2026-09-06)

> Numbers below are stale by construction; the ones that matter are re-derivable
> (`python3 app/build_pipeline.py --verify`, `python3 scripts/apply_publish_gate.py`). Content
> work continues in parallel with the product phases above, and per the *domain diversity*
> guidance, new batches should keep spreading across domains rather than re-mining a few.

**Last refreshed: 2026-09-06 (v2.19), against live scripts, not carried-forward numbers.**
For the full reasoning behind any line below — why a number moved, what broke, what was fixed —
see **[ROADMAP_HISTORY.md](ROADMAP_HISTORY.md)**, the complete narrative log. This file is just
the status page: what's done, what's not, what's next.

---

## Right now — the 5 things that matter most

| # | What | Why it's first |
|---|---|---|
| 1 | **Run the first real case with a real learner** (Track A3) | The single blocking fact — 0 cases have ever been run with a real learner, out of 134 now cleanly published (`python3 app/build_pipeline.py`, stage=promotion, TIER1_PASS, 0 blockers). Everything else is still a machine claim until this happens |
| 2 | **Push `app/student-moksh-atit.html` to the live site** | Currently local-only; his first assigned month can't actually be used until this ships |
| 3 | **Give `a-coachs-dilemma` its Tier 3 human dry-run** | Its long-standing blocker is now cleared: a genuine Tier 1 + Tier 2 re-run against the current NBA/Priya Shah content landed 2026-09-01 (`case.json.qa.run_on`, `case_md_sha256=fc3c53b5...`) — `tier1_structural.py --case a-coachs-dilemma` now shows 0 blockers, 3 disclosed non-blocking gaps (T1-10 reinforcement carve-out, T1-14/T1-15 known false-positive orphan-number matches), and all 6 Tier 2 probes PASS. Tier 3 (human dry-run) is the only remaining gate before `VERIFIED` — a natural pairing with item 1 above |
| 4 | **Decide the next coverage target** | Every true zero-coverage skill in the entire 437-skill standards spine is now closed (see 2026-09-06 note below) — this project has never been at `uncovered: 0` before. The next real backlog item is picking which of the remaining 162 thin (n=1/n=2) skill groups to thicken next, not closing a hard zero anymore. No batch is currently scoped — needs a fresh `case-brainstorm` pass against `standards_spine.json`'s live thin-group list |
| 5 | **Push a `case-publish` to Google Drive for the first time** | Every case published across recent sessions built its packet and promoted the read-model, but Drive upload has been held back pending separate approval every time — still an open step for all of them |

---

## What's actually ready to use right now

**Moksh Atit is set up and has his first month assigned** — 5 cases toward Badge 1, all genuinely
quality-checked: Phone Plans → Family Trip → Key Length → Field Watch → Apron Order. His page:
`app/student-moksh-atit.html`. Not yet pushed to the live site — still local only.

**124 cases** are genuinely ready to hand to any learner (passed every quality check this project
requires, live re-scan via `app/build_pipeline.py`, stage=promotion + TIER1_PASS + 0 blockers).
**1 case remains `BLOCKED`** — `the-locks-window`, intentionally: kept as a documented historical
record of a structurally one-sided dilemma, not revived (see its RESEARCH_LOG.md/FACILITATOR.md).
The previously-flagged batch of 10 mis-published cases (`archery-camp`, `baseball-lineup`,
`cardiology`, `catering`, `house-plans`, `lebron-vs-michael`, `nuclear-waste`, `phone-plan`,
`rent-vs-own`, `robotics-engineer`) remains remediated — each still carries a recorded
`TIER2_PASS` with all six Tier 2 probes passing; see their individual `QA_REPORT.md` files for the
per-case fix log.

**2026-09-05: the first life-skills batch — 10 cases — published.** The Two Offers, The Breakeven
Mile, The Deferred Repair, The Lease Break, The Bracket Bet (Roth vs. Traditional IRA), The
Minimum-Payment Trap, Deductible Roulette, Free Money With Strings (401k match), The Quiet Thief
(inflation), and How Long Can We Last (emergency fund sizing) — every true zero-coverage
*life-skills topic* the 2026-09-03 taxonomy identified (job offers, car ownership, Roth/Traditional,
car maintenance) plus 6 more, all reaching genuine `TIER2_PASS` (all 6 Tier 2 probes, 0 FAIL) before
publish, margins 5.1%–14.8%. Two real pre-existing defects were found and fixed during this batch,
not just authored around: `the-lease-break`'s original numbers showed one apartment cheaper in
*both* compared scenarios (no genuine dilemma — retuned against two independently-sourced real
termination-penalty figures) and `the-bracket-bet` had been recorded `TIER2_PASS` with one probe
(P5) `NOT RUN` — a real integrity gap, now closed with a genuine, disclosed sensitivity finding. See
each case's `QA_REPORT.md` for the full remediation trail. `readmodel/` promoted for all 10;
`app/dashboard.html` rebuilt same day. None yet pushed to Google Drive (see item 5).

**2026-09-06: the curriculum zero-coverage batch — 10 cases — published. `uncovered` reaches 0
for the first time in this project's history.** The Correction Window (Taylor Series ×2), The
Painted Gallon (sphere volume), The Marginal Call (quotient rule), The Deep End (`depth`/`digit`)
— the four true zero-coverage clusters `standards_spine.json` had flagged since 2026-09-02 — plus
The Bandstand Angle, The Overlap Send (full 8/8 Set Theory close), The Custom Die, The Sightline
Vote, The Mirror Cut, and The Special Order (full 8/8 Fractions close), thickening five of the
highest-severity thin clusters. All 10 reached genuine `TIER2_PASS` before publish, margins
6.4%–14.6%. Real defects found and fixed, not authored around: `the-painted-gallon`'s original
design had the Multi-Column tank winning every dollar metric with no genuine dilemma — fixed not
by retuning numbers but by adding a second real factor already present in the same cited
engineering memo (fabricator sole-sourcing risk), plus 3 bad citations (an unsupported claim, a
mis-cited CA Elections Code section, a dead USGS link) all replaced with verified sources;
`the-custom-die`'s Twist depended on an unstated convention (whether a signed annual contract
resets the tooling re-decision window) — now stated explicitly — and its accessibility probe found
14 unglossed real-world terms, closed for real over 3 remediation rounds. Also fixed in
`skills/case-readiness/scripts/tier2_probes.py`: a case-sensitive glossary-matching bug that let a
case pass its glossary structural checks (T1-19/T1-21) while the accessibility cold-read still saw
zero inline glosses for any term that only appears lowercase in prose — found independently on two
different cases the same day. `readmodel/` promoted for all 10; `app/dashboard.html` rebuilt same
day (the Calculus/Derivatives zero-coverage self-check failure that had stood since before
2026-08-24 is now gone, closed by The Marginal Call). None yet pushed to Google Drive.

**19 new cases published across two batches since 2026-08-30**, and `the-dosing-curve` /
`the-irregular-boundary` have since cleared readiness and promoted (see the 2026-09-01 note below
for the full batch list and the MCS-46/redesign detail). **4 cases remain in flight** — 3 at
readiness (`the-cheap-approximation`, `the-search-box`, `the-stake-out` — the last of these is
TIER1_PASS/0 blockers and TIER2_PASS-recorded (2026-09-01) but not yet promoted: it is in
`cases_index.json` but not yet credited in `standards_spine.json`'s `covered_by[]`, a pending
human-confirm step per MCS-12, not a defect) and 1 at research (`the-locks-window`, kept as a
documented historical record of a structurally one-sided dilemma, not revived) — live re-scan via
`app/build_pipeline.py`.

**0 concepts remain unwritten** (was 9 as of 2026-08-30). This is a corrected number, not just a
lower one: the pipeline-native concept board (`app/build_pipeline.py`'s `parse_concept_sheets()`)
was undercounting by 1 due to a genuine title-drift bug — concept C9 "Redrawing the Lines" had
already been written and published as `cases/redrawing-lines/` (case.json title "Redrawing Lines",
an internal "the" dropped) but the matcher only strips a *leading* "The ", so it never recognized
the match and kept showing the case as an unwritten concept. Fixed with a `CONCEPT_TITLE_ALIASES`
entry in `app/build_pipeline.py`, mirroring the existing `LEGACY_TITLE_ALIASES` pattern — this also
resolves the Housekeeping-table item "confusing near-duplicate case name needs a human check
(`redrawing-lines`)" below. All 9 previously-listed concepts from `CONCEPTS_pim-sector-gaps_2026-08-24.md`
and the rest of this session's batches are now written and published. Both remaining Pre-Calculus
gaps (Polar/Parametric, Trig Identities) stay closed.

---

## Status by area

Legend: ✅ done · 🔄 in progress · 🔜 next up · ⏳ open, not started · ⛔ blocked / needs a decision

### Quality — is any case actually good enough?

| Item | Status | What's left |
|---|---|---|
| Fix the flagship case (Cold Chain) | ✅ Done | — |
| Require a "stress test" before any case ships | ✅ Enforced by a script | 10 cases slipped through once; all 10 since remediated to TIER2_PASS |
| **Run the first case with real students** | ⛔ **Not started — the #1 blocker** | Pick any of the 80 clean cases, run it, fill in the results |
| Reusable case-page template | ✅ Done | Proven across many cases already |
| Facilitator "cohort size" guidance | 🔄 Only 1 case has it | Every case with facilitator notes needs its own |
| Fix the 10 mis-published cases | ✅ Done | All 10 now carry a recorded `TIER2_PASS` |

### Coverage — does the case library actually teach the whole curriculum?

| Item | Status | What's left |
|---|---|---|
| Tag old cases against the skill map | ✅ Done | Worked to its honest limit |
| Add Pre-Calculus / Calculus / Discrete Math to the skill map | ✅ Done | — |
| Give every case facilitator discussion notes | 🔄 In progress | 16 of 56 older cases still missing them |
| **Write/finish cases for Geometry & Pre-Calculus gaps** | ✅ Done | Pre-Calculus, Quadrilaterals & Polygons, Visual Perceptibility, Surface Area & Volume, Calculus/Derivatives, and Calculus/Series are all now fully closed (last three closed 2026-09-06 by The Painted Gallon/The Marginal Call/The Correction Window) — zero true zero-coverage skills remain anywhere in the spine |
| Some subject areas have almost no cases at all | ⏳ Not started | Number Theory is the thinnest |

**Geometry & Pre-Calculus gap tracker** (reprioritized ahead of other subjects per direct request):

| Subject | Topic | Gap | Status |
|---|---|---|---|
| Pre-Calc | Matrices | 7 skills | ✅ Published (`the-multiplier-recruit`) |
| Pre-Calc | Intro to Limits | 5 skills | ✅ Published (`the-reserve-asymptote`) |
| Pre-Calc | Polar & Parametric | 6 skills | ✅ Published (`feedback`) |
| Pre-Calc | Trig Identities | 5 skills | ✅ Published (`deluge-gun`) |
| Geometry | Fundamentals | 7 skills | ✅ Published (`roofline-call`) |
| Geometry | Quadrilaterals & Polygons | 0 of 22 uncovered | ✅ Closed |
| Geometry | Visual Perceptibility | 0 of 11 uncovered | ✅ Closed |
| Geometry | Surface Area & Volume | 1 of 10 uncovered | 🔄 9/10 covered — "How to find the volume of a sphere" remains |

### Interface — the dashboards and student-facing app

| Item | Status | What's left |
|---|---|---|
| Main dashboard (case library, coverage map, pipeline view) | ✅ Done | — |
| Shareable links to a specific view | ⏳ Open | Needs a technical decision about how the app is hosted |
| Students submit their work into the system | 🔄 Designed | Never actually tested with a real submission |
| "Which skills has this student actually practiced" view | ⏳ Open | Data already exists, just needs a screen |
| Broken data link (an old bug) | ✅ Fixed, verified 2026-08-19 | — |
| Pipeline status view (what's in progress, what's stuck) | ✅ Done | — |

### Delivery — getting a finished case into someone's hands

| Item | Status |
|---|---|
| Publish a case for real (not just locally) | ⏳ Open |
| Every case ships the same standard file bundle | ⏳ Open |
| Someone has actually printed a packet and checked it reads well on paper | ⏳ Open — nobody has yet |
| Clean up old cases' inconsistent file naming | ⏳ Open |

### Evaluation — grading and feedback quality

| Item | Status |
|---|---|
| Scoring rubric | ✅ Shipped, ⚠️ never calibrated against real student work |
| One scoring criterion ("framing the question") may be too hard | ⏳ Open |
| Track who's actually talking in discussions | ⏳ Open |
| Two facilitators independently score the same work, compare | ⏳ Open |
| Watch for the grading machine getting overridden a lot | 🔄 Ongoing |

### Engagement — making cases genuinely fun/compelling, not just correct

| Item | Status |
|---|---|
| Build in a deliberately tempting *wrong* answer | ⏳ Open |
| Give each "character" secret info that forces real collaboration | ⏳ Open, most interesting unexplored idea |
| Connect the math explicitly to the career that uses it | ⏳ Open |
| Use live/real-time data sources | ⏳ Open — needs a deliberate decision first |
| Cases about surprising subjects (drill team math, textile grading, etc.) | ⏳ Open |

### Housekeeping

| Item | Status |
|---|---|
| Automated tests for the admin app | ⏳ Open — currently zero |
| Real per-user login (currently one shared password for everyone) | ⏳ Open |
| ~~A confusing near-duplicate case name needs a human check (`redrawing-lines`)~~ | ✅ Fixed 2026-09-01 | It was not a duplicate — concept sheet C9 "Redrawing the Lines" and the published `cases/redrawing-lines/` ("Redrawing Lines") are the same case; `app/build_pipeline.py`'s title-matcher only stripped a leading "The ", not an internal "the", so it never recognized the match. Added a `CONCEPT_TITLE_ALIASES` entry (mirrors `LEGACY_TITLE_ALIASES`) |
| **`app/dashboard.html` is a static build artifact — goes stale after every `case-publish` unless someone manually reruns `python3 app/build_dashboard.py`** | ⚠️ **Process gap, not automated** | Rebuilt 2026-08-24 (had been stale since before Grant Reach/Perimeter Protocol published, meaning the live dashboard was missing 4 published cases for several sessions with nobody noticing). The page's own masthead shows `built <date>` once logged in — check that date against today before trusting what's on screen. No CI/git-hook enforces the rebuild yet; it's still a manual step someone has to remember after every publish |
| `build_dashboard.py --verify`'s 2 remaining failing self-checks | ⏳ Open, not investigated | (1) one zero-coverage cluster (Calculus/Derivatives) with no closing domain recorded, (2) tracker live exception queue not empty (`phone-plans`/Moksh Atit). Neither blocks a valid `dashboard.html` build; neither investigated further yet |
| **`readmodel/gap_queue.json` is stale and should not be used for coverage prioritization** | ⚠️ **Found 2026-09-02, not yet fixed** | Its per-group gap counts (e.g. Geometry/Quadrilaterals & Polygons "16 of 22 uncovered", Visual Perceptibility "10 of 11 uncovered") badly overstate the live gap — cross-checked directly against `standards_spine.json`'s own `covered_by[]` arrays, both groups have 0 skills at true n=0 coverage right now (consistent with this file's own "fully closed" claims above); `gap_queue.json` appears to predate a lot of coverage work and nothing in `app/` regenerates it (only `build_dashboard.py` reads it). The 20-case worklist below was built directly from `standards_spine.json`, not from this file. No script currently rebuilds `gap_queue.json` — either wire one up or retire the file so it stops being a plausible-looking trap for the next session |
| ~~`legacy_readiness` case count vs. `corpus_index` legacy count mismatch~~ | ✅ Fixed 2026-08-30 | Root cause was two compounding bugs: (1) `app/build_pipeline.py`'s `LEGACY_TITLE_ALIASES` didn't cover 4 legacy→published title renames (Movie Producer→Movie Executive, College Football Playoff Committee→Playoff Committee, Medical Statician→Medical Statistician, AirBnb→AirBnb Or Landlord), so those 4 published cases still showed as `legacy-untouched` "NEEDS A REAL DESIGN DECISION" cards on the pipeline board; (2) `corpus_index.json` never clears a row's `status: "legacy"` flag once that case is converted and published — true for all 43 already-converted legacy cases, not just the 4 with the title-alias bug (e.g. Payroll and Gerrymandering were also mislabeled, which is what caused the separate "legacy cases carrying `margin: 0` instead of `null`" self-check to fail too). Fixed both: added the 4 missing aliases, and flipped `status` to `"published"` on the 43 corpus_index.json rows for titles `build_pipeline.py` already recognizes as converted. `legacy_readiness.json`'s `n_legacy_cases` dropped from 45 to 2 (the two genuine remaining exceptions: `Castle Securtiy` — typo'd source folder name, and `Investing - Stock Market - Options (Jia)` — case doc is an .xlsx, not a .docx). Both self-checks now pass |

---

## Next 20 cases — prioritized coverage worklist (2026-09-02)

**Superseded 2026-09-06: #1–4 (every zero-coverage cluster), #6 (Set Theory, full 8/8),
and #10 (Fractions/Understanding Fractions, full 8/8) are now closed** — see the
2026-09-06 batch note above (The Correction Window, The Painted Gallon, The Marginal Call,
The Deep End, The Overlap Send, The Special Order). #5, #7, #8, #9 were also substantially
thickened by The Bandstand Angle, The Custom Die, The Sightline Vote, and The Mirror Cut
respectively, though none of those four groups reached a full close — re-run this worklist
against the live spine before drawing the next batch rather than trusting the table below,
which reflects 2026-09-02 numbers.

Built directly from `standards_spine.json`'s live `covered_by[]` arrays (not from the stale
`gap_queue.json`, see Housekeeping above). Rubric score = `3×(skills at n=0) + 2×(skills at n=1) +
1×(skills at n=2)` — i.e. a genuinely-uncovered skill outweighs five thinly-covered ones. The 4
zero-coverage clusters are ranked above their raw score because this project already tracks "skills
with zero coverage" as the one hard-zero metric (see numbers table). Every case still has to design
to SPEC §2's ~20% real-margin balance cap (or explicitly invoke the MCS-46 waiver for a genuine
physics/economics landslide) — that's a per-case design constraint to hit while writing, not
something computable from this table in advance.

| # | Priority | Domain / group | Gap (n=0 / n=1 / n=2 of total) | Score | Note |
|---|---|---|---|---|---|
| 1 | 🔴 zero-coverage | Calculus / Series | 2 / 2 / 1 of 5 | 11 | Taylor Series + evaluating a Taylor series at a point — both n=0 |
| 2 | 🔴 zero-coverage | Geometry / Surface Area & Volume | 1 / 5 / 3 of 10 | 16 | Sphere volume is the last n=0 skill in this cluster; the other 9 already have some coverage |
| 3 | 🔴 zero-coverage | Calculus / Derivatives | 1 / 2 / 1 of 9 | 8 | Quotient rule is the one n=0 skill |
| 4 | 🔴 zero-coverage | Number Sense / Measurement & Data + Place Value | 2 / 0 / 0 of 12 | 6 | "Depth" and "Digit" — two small, unrelated n=0 skills; likely one shared case or two very short ones |
| 5 | 🟠 thin | Geometry / Quadrilaterals & Polygons | 0 / 10 / 6 of 22 | 26 | Highest thin-severity group in the whole spine; already flagged "reprioritized ahead of other subjects" above |
| 6 | 🟠 thin | Discrete Mathematics / Set Theory | 0 / 8 / 0 of 8 | 16 | Every skill in the group sits at exactly n=1 |
| 7 | 🟠 thin | Geometry / Visual Perceptibility | 0 / 7 / 3 of 11 | 17 | |
| 8 | 🟠 thin | Geometry / Fundamentals of Geometry | 0 / 0 / 18 of 24 | 18 | All 18 gaps are n=2, not n=1 — lower urgency than its raw score suggests |
| 9 | 🟠 thin | Geometry / Transformations | 0 / 0 / 14 of 20 | 14 | Same n=2-only pattern as #8 |
| 10 | 🟠 thin | Fractions / Understanding Fractions | 0 / 4 / 4 of 11 | 12 | |
| 11 | 🟠 thin | Geometry / Triangles | 0 / 6 / 0 of 10 | 12 | |
| 12 | 🟡 thin | Advanced Operations / Scientific Notation, Factorial, Absolute Value | 0 / 4 / 1 of 8 | 9 | |
| 13 | 🟡 thin | Fractions / Addition & Subtraction of Fractions | 0 / 4 / 0 of 4 | 8 | Every skill in the group at n=1 |
| 14 | 🟡 thin | Discrete Mathematics / Formal Logic | 0 / 0 / 8 of 8 | 8 | All n=2 |
| 15 | 🟡 thin | Discrete Mathematics / Graph Theory | 0 / 1 / 6 of 8 | 8 | |
| 16 | 🟡 thin | Basic Operations / Factoring | 0 / 3 / 1 of 6 | 7 | |
| 17 | 🟡 thin | Fractions / Multiplication of Fractions | 0 / 3 / 1 of 4 | 7 | |
| 18 | 🟡 thin | Fractions / Division of Fractions | 0 / 3 / 1 of 4 | 7 | |
| 19 | 🟡 thin | Calculus / Integrals | 0 / 0 / 7 of 7 | 7 | All n=2 |
| 20 | 🟡 thin | Number Sense / Numbers & Counting | 0 / 3 / 0 of 4 | 6 | |

None of these 20 are scoped as concepts yet (concept backlog is genuinely at 0 — see numbers
table) — this is a *coverage-gap* ranking to draw the next concept batch from, not an existing
`CONCEPTS_*.md` sheet. #1–4 close every remaining true zero-coverage skill in the curriculum; #5–11
are the highest-severity thin clusters and mostly fall in Geometry, consistent with this project's
standing "Geometry & Pre-Calculus gaps reprioritized ahead of other subjects" direction above;
#12–20 round out the next batch. Fractions and Discrete Mathematics show up repeatedly and may be
worth a "some subject areas have almost no cases at all" look (see Coverage table above, which
separately flags Number Theory as thinnest overall).

---

## The numbers, for reference

| | |
|---|---|
| Cases that are genuinely ready to assign (published, live re-scan, `python3 app/build_pipeline.py`) | **134** |
| Cases at stage=promotion but genuinely `BLOCKED` (not force-passed) | **0** — `a-coachs-dilemma` cleared 2026-09-01, see item 3 above (`the-locks-window` is `BLOCKED` at stage=research, intentionally, a documented historical record, not a defect) |
| Total case directories under `cases/` (pipeline-authored corpus) | **138** (`ls -d cases/*/ \| wc -l`) |
| Concepts scoped but not yet written into a case | **0** (18 concept sheets in `cases/_concepts/`, all C-numbered concepts written) |
| Cases ever run with a real student | **0** |
| Skills in the curriculum map | 437 (`readmodel/standards_spine.json.totals.skills`) |
| Skills with zero coverage (n=0) | **0 — first time in this project's history**, closed 2026-09-06 (Taylor Series ×2, sphere volume, quotient rule, Depth, Digit) |
| Skills "thin" (1 ≤ n ≤ 2, the project's tracked thin-coverage threshold, `standards_spine.json.totals.thin_1_2`) | 162 |
| Distinct case titles credited in the spine (`standards_spine.json.totals.cases`) | 143 |
| Legacy source-corpus cases still un-triaged/exception (`readmodel/pipeline_status.json.legacy_exceptions`) | 2 (`Castle Securtiy`, `Investing - Stock Market - Options (Jia)`) |
| Concept-sheet backlog files (`cases/_concepts/CONCEPTS_*.md`) | 18 sheets, 0 unwritten C-numbered concepts remaining across all of them |
| `app/dashboard.html` last rebuilt | **2026-09-01** — must be rerun (`python3 app/build_dashboard.py`) after every future `case-publish`, or the live site keeps serving stale data even though the underlying case files are correct. `--verify` clean at 206 checks, 2 pre-existing documented failures (Calculus/Derivatives zero-coverage cluster; `phone-plans`/Moksh Atit tracker exception), 1080/1080 asset links resolved |
| `readmodel/domains.json` / `domain_coverage.json` | 40 domains, 12 clusters, `app/validate_domains.py` 28/28 checks passing |

**2026-08-30 note:** `bioreactor-bid`, `enclosure-call`, `fret-board`, `alert-curve`,
`compute-lease`, `cooling-curve`, `downbeat-split`, and `placement-test` — all 8 cases that were
in flight — reached `TIER2_PASS` and published this session (packet + interactive HTML +
read-model promotion). Google Drive upload was not pushed for any of them, held for separate
approval. `fret-board`, `alert-curve`, `compute-lease`, `cooling-curve`, `downbeat-split`, and
`placement-test` all required a genuine retune first (see the note above for what changed in
each).

**2026-09-01 note — staleness sweep + a 19-case batch's worth of pipeline/dashboard rebuild.**
Two things happened between the 2026-08-30 refresh and this one, across several concurrent
sessions working this repo: (1) 19 new cases were published in two batches — `prove-it-scales`,
`the-attribution-sample`, `the-bot-farm`, `the-bracket-cliff`, `the-cold-start`,
`the-contrapositive-claim`, `the-course-correction`, `the-dosing-curve`, `the-fee-ladder`,
`the-irregular-boundary`, `the-mainline-margin`, `the-peg-line`, `the-plaza-bid`,
`the-qubit-budget`, `the-repeat-match`, `the-rig-budget`, `the-rig-split`, `the-stake-out`,
`the-trial-size`; and (2) a 6-case Precal depth/redundancy batch (`the-tilt-decision`,
`the-crosswind-cut`, `the-skin-pack-atlas`, `the-search-box`, `the-clampband-margin`,
`the-late-run`) reached `TIER2_PASS`, alongside **two dilemma redesigns**: `the-locks-window`
(structurally one-sided, superseded by `the-late-run`, left in place as a documented historical
record rather than deleted) and `the-transfer-window` (chemical-vs-electric propulsion found to be
a structurally unfixable ~800x transit-time gap, superseded by `the-phasing-call`, a same-technology
direct-vs-phasing rendezvous rebuild). **MCS-46** (a narrow, project-owner-approved per-case waiver
of MCS-02's ~20% balance cap, for real dilemmas with a landslide margin driven by real
physics/economics where the *problem-solving process* is still genuinely hard) was added and used
to publish `the-phasing-call` (~1991% real margin, waived) and `the-transfer-window` (kept as
historical record, not revived under the waiver).

This session's own work, on top of that: found the corpus's live `--verify` state did **not**
match the task brief's premise — `the-stake-out` was not `BLOCKED`; it was already `TIER1_PASS`
(0 blockers) at stage=readiness (published packet built, `cases_index.json` entry present, not yet
promoted into `standards_spine.json.covered_by[]` — a pending human-confirm step, not a defect).
The real staleness sweep instead found **5 genuine `stage=promotion` `BLOCKED` cases**, all fixed
by rebuilding the actual broken artifact (never by weakening a check or fabricating a pass):
`deluge-gun`, `gerrymandering`, `redrawing-lines`, `speed-climbing`, and `the-keyspace-decision`
each had a Working Notebook `<input placeholder>` in its published Interactive HTML containing the
exact numeric answer the Check button grades against (MCS-37/T1-18) — every digit was replaced
with a format-only hint (e.g. `placeholder="e.g. 569068"` → `placeholder="whole number"`), and all
5 now re-verify `TIER1_PASS`/0 blockers. `a-coachs-dilemma` had a real, pre-existing, already
partly-diagnosed issue (its own `QA_REPORT.md`, dated 2026-08-21): case.md was edited to remove a
worked-answer leak, but `published/*.docx`/`*.xlsx`/`MANIFEST.json` were never regenerated and
`case.json.qa`'s hash/Tier-2 result still describe a *retired* NCAA-content version of the case.
The packet was mechanically rebuilt from the current case.md (clearing 3 of 4 blockers); the 4th
(`T1-16`, stale QA hash) was deliberately **left BLOCKED and reported, not forced green** — a real
Tier 1 + Tier 2 re-run against the current NBA/Priya Shah content is still owed and is now item 3
in "Right now" above. Also found and fixed a genuine title-drift bug in `app/build_pipeline.py`'s
concept-matcher (see the Housekeeping table) that was inflating the unwritten-concepts count by 1.
Full pipeline/dashboard/domains rebuild run clean afterward (`build_pipeline.py`,
`build_dashboard.py` + `--verify`, `build_legacy_readiness.py`, `build_domains.py` +
`validate_domains.py`) — see the numbers table above for every resulting figure and its source
command.

**2026-09-02 note — confirmed `a-coachs-dilemma`'s blocker is genuinely cleared, corrected the
case counts, and built the next coverage worklist.** A `git status` at session start showed
`case.json`, `QA_REPORT.md`, and `published/*` for `a-coachs-dilemma` already modified/regenerated
in the working tree but not yet reflected in this file. Re-ran `tier1_structural.py --case
a-coachs-dilemma` live: 0 blockers (T1-16 now PASS), 3 disclosed non-blocking gaps, matching
`case.json.qa` (`state: TIER2_PASS`, `run_on: 2026-09-01`, all 6 Tier 2 probes PASS, hash
`fc3c53b5...`) — this was real remediation from a concurrent session, not carried-forward-and-wrong.
Re-ran `app/build_pipeline.py` live: 114 promotion / 0 blocked (up from 111/1), 3 readiness (down
from 5 — `the-dosing-curve` and `the-irregular-boundary` have since promoted), 1 research, 0
concepts — updated throughout this file. Also cross-checked `readmodel/gap_queue.json` against
`standards_spine.json`'s live `covered_by[]` arrays while building the next-20-cases worklist below
and found it badly stale (see the new Housekeeping row) — the worklist was built from
`standards_spine.json` directly instead. No case content was written this session.

Full derivations, per-script commands, and the reasoning trail for every one of these numbers are
in [ROADMAP_HISTORY.md](ROADMAP_HISTORY.md).
