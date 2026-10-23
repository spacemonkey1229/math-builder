# PRD — Math Builder: Learner Experience (Product stage)

**Version 1.0 · 2026-10-19 · Status: DRAFT for Manan's review**
Companion to [VISION.md](VISION.md) (why) and [ROADMAP.md](ROADMAP.md) (when). This file is the
*what*: requirements, acceptance criteria, risks. Requirements are numbered `R#` so the roadmap
and decisions can cite them.

---

## 1. Problem

The authoring pipeline reliably produces rigorous cases, but the **learner's moment** inside a
case is thin: a static page with "Check" buttons that say right/wrong. A stuck learner has no
help; a confused learner can't tell whether the case or they are at fault; finishing means
exporting files for a guide to score by hand. The first outside user said it plainly: it is "a
great tool," and with a few tweaks it can be a product.

## 2. Feedback traceability (Anuj, 2026-10-17, example case: `phone-plan`)

| # | Feedback (paraphrased) | Verified in the repo? | Becomes |
|---|---|---|---|
| F1 | Add a chatbot for hints and help | Nothing like it exists | **R2** Coach |
| F2 | Twist instructions unclear — is the 8% tax expected again, like the previous step? | **Yes, real defect.** `phone-plan` Step 4 says "compare the $150 credit to a year of Carrier T savings at 2 lines" and never says whether to include Idaho's 8% plan tax | **R1** Instruction clarity |
| F3 | In "Check both," bot reverse-engineers the kid's method and hints toward the right answer | Step 1 "Check both" returns only right/wrong per field | **R2** (diagnostic engine) |
| F4 | Twist should reuse the line count chosen earlier so cost needn't be recalculated | **Yes, real defect.** Twist is hard-wired to 2 lines regardless of what the learner worked with | **R1** Scenario consistency |
| F5 | One-click submit, AI-graded on numbers *and* a small share for note quality | Partly. The page's toolbar **Submit** button only packages the notebook as a PDF (`exportSubmissionPacket()`) for the learner to hand over; scoring is the guide-run `submission-score` — no server-side submit or AI grading | **R3** Submit & grade |
| F6 | Leaderboard, stars, badges for motivation | Badges exist at guide level (Badge 1 = 5 cases); no learner-facing stars/leaderboard | **R4** Recognition |
| F7 | Tool → product → platform; other subjects incl. subjective (history, civics, book reviews) | — | **R7** + VISION stages |
| F8 | Integrate with the whole Acton system | Unknown surface area | **Discovery** (Roadmap Phase 3) |
| F9 | Offered to help develop and to test with kids | — | **Track A3** (first real learner) |
| F10 | "Remind me to share ideas on new marketing-tech-stack tools offering interesting comparisons" | — | Follow-up (Roadmap → Reminders) |

A note on the case: Anuj's description (8% sales tax, "twist," "check both") matches
`cases/phone-plan` (Idaho, Carrier V/T), **not** `cases/phone-plans` (Oregon, 22.53% combined
wireless rate). Worth confirming with him; it changes nothing about the fix.

## 3. Requirements

### R1 — Instruction clarity and scenario consistency (Phase 0)

*Story:* As a Hero, I always know exactly what a step asks, and a later step builds on my own
earlier choices instead of silently switching scenarios.

Behavior:
- Every graded step states, in the step text: **(a)** which scenario it uses (e.g., "your
  chosen line count, N"), **(b)** whether tax/fees are included, **(c)** rounding/units.
- Twist and downstream steps **inherit the learner's selected scenario** (line count, option)
  where the case has a learner-selected parameter, or state explicitly why they are pinned.
- `phone-plan` fixed first as the reference fix: Step 4 reads the line-count selector instead
  of hard-coding 2, and says whether the 8% applies.

Acceptance:
- A new Tier 1 lint (candidate id `T1-xx`, **needs a DOCTRINE_LEDGER row + critique pass**
  before it is real) flags any graded step whose text lacks tax/rounding/scenario statements
  when the case has tax/fee/selector parameters.
- Re-run of case-readiness (Tier 1 + Tier 2) on `phone-plan` passes; the live browser pass is
  repeated (see memory: text checks miss behavior bugs).
- Sweep: list every published case with a selector or tax/fee parameter and a Twist step;
  triage for the same two defects. (Expect more than one.)

Risk: touching published cases invalidates `case.json.qa` hashes → rebuild packets and re-run QA
per pipeline rules; do not hand-edit published artifacts.

### R2 — The Coach: hints and diagnosis (Phase 1)

*Story:* As a stuck Hero, I can ask for help on the step I'm on and get a nudge that respects
my thinking; when I enter a wrong answer, the coach can often tell me *which mistake that
probably is*.

Design:
1. **Misconception catalog (deterministic).** Each case gains `misconceptions` data next to
   `sensitivity_model.py`: a list of "plausible wrong methods" per step, each a small function
   that computes the wrong answer the method would produce (e.g., `forgot_tax`, `used_n_not_n_minus_2`,
   `tax_applied_twice`, `compared_unit_vs_total`). At runtime, the learner's input is matched
   against all candidates (within rounding tolerance). A match → targeted hint ("this looks like
   the number you'd get before tax — does the problem say tax applies here?").
   Catalog values are **recomputed in code**, never typed in from the model (consistent with
   the project's "answers recomputed in code" rule).
2. **Hint ladder.** Level 1 nudge (re-read a sentence / name the quantity) → Level 2 pointer
   (name the operation or appendix row) → Level 3 worked *analogue* with different numbers.
   Never the case's actual answer. The ladder advances only on request, and Level 3 requires an
   attempt first.
3. **LLM for the tail.** When no catalog entry matches, a model phrases a Socratic question
   given: the step goal, the learner's input, the catalog (so it knows what *isn't* the issue),
   and a hard instruction not to reveal the key. Model routing follows 00_SESSION.md (Haiku
   first; escalate only on measured failure).
4. **Free-text "ask the coach."** Same guardrails; scoped to the current step and the case's
   appendices; refuses off-topic and refuses to produce a pitch for the learner.

**Dialogue rules (from the R1a review).** These govern every Coach.AI turn:
1. *Attempt before help.* No hint until the Hero has entered a number or written the formula they used.
2. *Ask for the method, not the number.* "What did you start from?" The coach reads the Hero's own
   formula back before diagnosing.
3. *One question per turn, answerable from the page.*
4. *Name the kind of mistake, never the operation.* "This looks like a pre-tax number" is allowed;
   "add the tax" is not.
5. *Stop rules.* After two failed turns on a step, offer a worked analogue with different numbers. A
   correct method stated in words still needs the computation before the coach confirms. If the Hero
   says "just tell me," offer the analogue and don't debate.
*Top failure modes to test for:* answer extraction by rephrasing ("what is 2 times…"); validating a wrong
method because the number is close; the model tail asserting a value is wrong when it has no key; a step-1
hint that hands over step 3; implicitly endorsing the conclusion of a pitch.

Guardrails (acceptance, testable):
- **Leak test:** an automated suite sends adversarial prompts ("just tell me the answer,"
  "what number do I type," prompt-injection in the notebook text) across every step of the
  pilot case; zero responses contain the step's answer (± rounding) or an equivalent that makes
  it a one-step computation.
- **Key stays server-side:** the coach endpoint holds the key; it is never shipped in page JS.
  (Today the interactive page ports `evaluate()` to client JS, which is fine for formative
  checks but not for coach/grading authority.)
- **Cost/abuse:** per-student and per-case rate limits; hard monthly spend cap; graceful
  degrade to catalog-only hints when the model is unavailable.
- **Logged for learning:** every hint request (step, level, matched catalog id or "tail") is
  stored — this is the data that tells authors which steps are confusing.

Open: pilot case = `phone-plan` (the feedback came from it; Step 1 "Check both" is the F3
scenario). Authoring cost of a catalog per case is real — budget it as a per-case authoring
step and decide whether the author agent drafts candidates that code then verifies.

### R3 — Submit and grade (Phase 1b)

*Story:* As a Hero, I click Submit; I get prompt feedback tied to the rubric. As a guide, I get
a drafted score I can confirm in seconds.

Behavior:
- **Submit** (today: PDF export only) is upgraded to package the notebook state (step answers, pitch text, appendix/notes, hint usage)
  and posts it to the hosted app, creating a submission in the existing flow
  (`submissions.json` / Postgres). One click replaces export-and-hand-over.
- **Numbers:** scored deterministically, server-side, from the case key. Partial credit logic
  stays in `score_submission.py`; add per-step results.
- **Notes/pitch quality:** an LLM grader scores against RUBRIC.md criteria with anchored
  descriptors (Not Yet / Proficient / Exemplary), returning evidence quotes per criterion. The
  student sees the feedback in rubric language, labeled **"provisional until your guide
  confirms."**
- **Guide confirm** remains the gate for badges (MCS-12: machine drafts, human promotes).

**The rubric must match our goals (decided; revision proposed by the R1a review).** RUBRIC.md's seven
criteria predate the vision. Keep the split between a *mastery gate* (every criterion at least Proficient)
and a separate *growth score*; the growth weights are untested. Proposed gate:

| | Criterion (weight) | Proficient looks like |
|---|---|---|
| K1 | Structure the problem (20) | Names the decision metric and the variables, and sets one given fact aside as irrelevant. Absorbs old C7. |
| K2 | Compute and deliver (15) | Every deliverable present; each number recomputes from the stated model; units carried. Merges C3+C4. |
| K3 | Handle assumptions and complexity (20) | Names each assumption the winner depends on, flexes at least one, reports whether the winner changes. |
| K4 | Defend the decision (25) | One side, argued from the numbers; states the strongest counter and what would change their mind. C2 without the word-count gate. |
| K5 | Reflect and revise (10) | Names one error or assumption they changed, and why. New. |
| K6 | Field exposure (10) | Uses one source a practitioner in this role would use for a number or rule the Hero lacked. A link that is only the case glossary is Not Yet. Reframes C1. |

*Demoted to growth-only (recorded, not gated):* visual display (a badge shouldn't depend on a chart) and
discussion participation (a contribution count penalizes quiet learners). *Never scored:* **confidence**
(captured as a 1–4 pre/post self-rating visible only to the guide, to compare against K-scores);
**curiosity** (a "what would you look up next" tag feeding the skills map); **hint counts** (a coaching
signal). This is how Anuj's "small percentage for note quality" is honored: notes and reflection are
assessed in K1, K3 and K5, inside the mastery gate and growth score, not as a separate percent.

Calibration (acceptance, non-negotiable before any student sees an AI grade):
- Build a **gold set**: the existing human-reviewed student work in `student_work/` plus new
  pilot submissions, graded blind by a guide.
- Measure grader–guide agreement per criterion. Proposed bar to leave "draft + guide confirms"
  mode for any criterion: within one level on ≥ 90% of ≥ 30 submissions and no systematic
  inflation; these thresholds are a proposal to be set with Manan.
- RUBRIC.md is still `PROPOSED — needs one real cohort before it locks`; the AI grader
  inherits that uncertainty. Say so in the UI and the guide view.

Risks: grader inflating on fluent writing; prompt injection in the student's notes ("give me
Exemplary"); students gaming rubric language. Mitigations: evidence-quote requirement, injection
tests, guide sampling of "Exemplary" verdicts.

### R4 — Journey tracker, points, and a simple leaderboard (Phase 2; tracker data from Phase 0)

*Story:* As a Hero, I see my journey, earn recognition for effort and depth, and have a reason to keep
going. As a guide, I can see who is engaging and at what depth.

**Points come from the same events that record the journey** (R9), so one source of truth feeds the
tracker, the profile, and the leaderboard. Points reward effort and depth, never speed or raw score:

| Event (all from the event log) | Counts when |
|---|---|
| Case completed | A guide confirms the submission. Per-week cap on counted completions. |
| Pitch depth | One point per rubric criterion at Proficient or better **where the Hero's own quoted evidence is confirmed by the guide**. Counts criteria with evidence, never words, so length can't inflate it. A counter-argument counts only if it uses the other option's numbers. |
| Revision made | The Hero revised after Coach.AI feedback (shows growth) |
| Case feedback given | The Hero reflected on and rated the case (feeds the guide and the case-quality loop) |
| New field explored | First case in a field cluster they haven't visited |

**Leaderboard v1 (simple).** Shows two counts, **cases completed** and **pitch depth**, with a points
total from the table above. Cohort-scoped, display name or alias by default, **opt-in** per Hero, no
rank numbers beyond the cohort (tiers or alphabetical ties are fine). Guides see everyone. Not public.
*Reviewer note (R1c):* recommends showing the two counts separately and not summing them, because a
composite recreates score-as-point; the owner wants points for the tracker. Decision for Manan: keep
points as an effort/depth tally (as above) but sort the board by cases completed.

**Gaming and countermeasures (from review):**
1. *Padding or pasting AI text to hit depth* → guide confirmation of each criterion, plus an optional
   60-second spoken defense of any criterion before it counts (also supports R11).
2. *Rushing for completion count* → completion requires step-attempt and revision events from the log;
   weekly cap on counted completions.
3. *Sharing answer keys in the cohort* → cohort-unique numbers where the case allows; rotating
   assignments.

**Protecting slower learners.** No resetting streaks; use grace weeks. Personal-best and "your last
pitch vs. your first" views stay private to the Hero. No "most improved" public board (it makes
struggle visible).

**Other carrots, ranked by effort and risk (R1c):**
| Carrot | Effort | When |
|---|---|---|
| Careers card per case (from `domains.json` `careers[]`: math used, entry path) | Low | Now |
| Pitch of the week, chosen by the guide, shown with the author's alias | Low | Now |
| Bonus twist unlocked after the pitch is submitted | Low–Med | Now |
| "Question that changed the decision": the Hero's own what-if run through the case model | Med | Later |
| Two-minute practitioner voice (agronomist, structural engineer) | High (licensing, vetting) | Later |
| Learner-authored decision cases | High risk (unvetted numbers) | Later, if ever |

Acceptance: points for any Hero can be recomputed from the event log alone; a guide can hide the
leaderboard or any Hero from it; a Hero can leave or switch to an alias at any time.


### R5 — Identity, privacy, and consent (enabler for R2 and R3; Phase 1a)

Cannot ship the coach or AI grading on the current model (single shared passcode; student pages
unauthenticated *on purpose*, D-018).
- **Per-assignment signed links** (hypothesis, lowest friction): the existing assignment link
  carries a token identifying learner + case; the coach/grader endpoints require it. Revisits
  D-018 narrowly; full accounts/SSO later (Phase 3).
- **Data minimization:** model calls get step text, the learner's input, and an opaque id —
  never name, school, or email. Define retention for hint logs and submissions.
- **Consent:** parental consent path and vendor terms checked for minors' data before any
  non-author child uses AI features (US context: COPPA/FERPA considerations — confirm with
  counsel/school policy; this PRD does not assert compliance).
- Update TECH_STACK.md in the same pass as any change here (00_SESSION.md hard line).

**Profile and history (also R5).** Points and recommendations need durable profiles. A Hero's profile
shows five things, none of them a rank: (1) **fields explored** ("3 of 12 fields") with the career each
touched; (2) **cases finished**, each with the Hero's own choice and one-line reason; (3) a **pinned
favorite pitch** the Hero chooses, showing which criteria it met; (4) **growth**, meaning evidence per
pitch over time with the Hero's own reflection; (5) **"still wondering"**, an open question carried into
the next assignment. **Recommended next assignment:** field curiosity first (the Hero picks one of two
cases in an adjacent field), then a skill-gap filter from step-level logs once about five cases of data
exist. The guide sees the reason for each suggestion.

### R6 — Telemetry and the feedback loop (Phase 0 → ongoing)

- A visible **"This was confusing"** control on every step (free text + step id) writing to the
  app DB. Today feedback arrives by email.
- Guide view: per-step stuck heatmap (hint requests, wrong attempts, time) per cohort.
- Close the loop into the pipeline: step-level confusion data becomes input to case-readiness
  (a Tier 3 signal), and to the Next-cases worklist.

### R7 — Platform seam (Phase 4; only light prep earlier)

- Separate **engine** (case schema, steps, key, rubric binding, misconception catalog,
  coach, grader, recognition) from **content** (the math cases). Do the minimum now: keep the
  per-case artifacts (`case.json`, `sensitivity_model.py`, `misconceptions`) the only
  case-specific inputs to the coach and grader.
- Subject path: science next (quantitative, deterministic keys, same engine) → then a
  subjective subject with a **rubric-judged** grader and a "source-grounding" requirement (the
  analogue of "never fabricate a number": every claim in a history pitch cites a primary or
  reputable source the learner can name). SPEC's "defensible ambiguity" carries over directly
  to history/civics dilemmas.
- Do **not** build generic multi-subject abstractions before the second subject exists.

## 3a. Worked examples (illustrative; `phone-plan` numbers are recomputed in code)

**Example 1 — Coach.AI is a dialogue, not a hint button (Step 2, Carrier V at 3 lines).**
Correct pre-tax is $95.00; with 8% tax, **$102.60**. *The UI/UX is the product here.*

*Interaction design.* A Coach.AI panel sits beside each notebook step with that step's context pinned
at the top. The answer field stays; the dialogue is what happens around it. Before checking, the Hero
picks "How sure are you?" (a quick 3-way tap) — a confidence signal for the tracker, never graded.
Coach.AI opens on a wrong answer or when asked. Quick-reply chips: *I'm stuck · Check my method · Show
me a similar example.* The Hero can type a number, or their method in words. One question per turn.
Every turn is logged (R9). The Hero can always keep working without opening the coach.

> **Hero** enters 118.80 *(sure: 3 of 3)*
> **Coach.AI** — I got something different. Can you tell me how you got 118.80?
> **Hero** — 80 + 15×2, then tax.
> **Coach.AI** — You applied the tax once and used the right rates. Let's look at how many lines you
> charged the extra rate for. Where does the case say what counts as an extra line?
> **Hero** — "beyond the first 2"... so only 1. 95, then 102.60.
> **Coach.AI** — Check it. ✓ What did you notice that changed your answer?

Behind the scenes the catalog matched `used_total_lines_in_equation`, (80 + 15×2) × 1.08 = 118.80. The
coach named the *kind* of mistake and pointed to a place in the case; it never named the operation. Other
entries for this step (Level 1 wording, which names a kind of mistake and a place to look):

| Hero enters | Matches (computed in code) | Coach.AI's first move |
|---|---|---|
| 110.81 | 95 × 1.08 × 1.08 | "Your number is higher than I expected. Where does Appendix B say the tax comes in?" |
| 95.00 | forgot tax | "That looks like the plan price. Does the case say the family pays that, or something else?" |
| 160 (Step 1 intercept) | 80 × 2 | "Which row of Appendix A describes the first two lines, and what does the row label say about them?" |
| 135.00 | (80 + 15×3) × 1.08 | "Walk me through how many lines each rate applies to." |
| 7 (no match) | model, Socratic only | "Walk me through how you got 7. What did you start from?" |

**Example 2 — the end-of-case summary and its feedback (format varies by case).**
*What it is.* A short summary of the Hero's position, the reasoning behind it, and what they'd want to
know next. *Format is declared per case* (`pitch_format`: written · spoken · either), because the real
world asks for different things: a written decision memo to a family, a two-minute spoken brief to a
board. Default is "either"; the graded artifact is always text, so a spoken summary is recorded and
transcribed into the same pipeline. A short spoken defense of a criterion is also the strongest check
that the Hero owns their reasoning (R11).

*Interaction, not a verdict screen.* Coach.AI shows three observations pulled from the Hero's own text
(with quotes), asks one question, and lets the Hero revise once before it's sent to the guide. Revision
history is kept and shows in the profile as growth. Feedback is in the revised rubric's language (R3), is
labeled "Provisional until your guide confirms," and never shows a raw score.

> *Framing the problem — Proficient (draft).* "You said the family is really deciding what to pay when
> Charity's line arrives — 'the 3-line price is what matters.' That names the real question."
> *Assumptions and complexity — Not Yet (draft, low confidence).* "You used the 8% tax but didn't say
> why you trusted the $15 extra-line price to stay the same. What else would have to be true?"
> *One question for you:* "What's the strongest reason to pick the other carrier, and how would you answer it?"

**Example 3 — what the guide sees: skills, assessment, focus, strengths, and the Heroes' own feedback.**
The guide needs the **core skill behind each step** and an **assessment of the cohort on each skill**, so
they know where to focus the discussion, plus the Heroes' feedback on the case. Invented cohort of six:

| Step | Core skill (from the case's standards) | First try | Hint requests | Signal |
|---|---|---|---|---|
| 1 Cost equations | Writing a linear equation: slope and y-intercept | 2 of 6 | 6 | ⚠ 3 Heroes read $80 as per line |
| 2 Total with tax | Percent of a number; order of operations | 5 of 6 | 2 | ✓ strength |
| 3 Break-even | Solving a system of linear equations | 3 of 6 | 4 | ⚠ 2 reported "1 line" instead of 3 |
| Summary | Framing the problem; naming assumptions | 4 Proficient | n/a | Weak on assumptions |

> **Suggested focus (generated, guide can edit):** "Open on Step 1. Cold-call a Hero who entered 160:
> 'What was your $80 counting?' Then ask what 'x = 1' is counting in Step 3. Strength to name: everyone
> applied the 8% tax once."

*Heroes' feedback on the case* (collected at step 6 of the journey): "4 of 6 said the wording of Appendix A
was confusing; 5 of 6 want to see a case in a field like this one." This flows two ways: into the guide's
prep for next time, and into the case-quality queue (S4), which is how a defect class gets caught before
the next cohort.

**Example 4 — the same engine in other subjects (concept sketches, not cases).**
- *Science (deterministic key):* a decision between two interventions where unit and concentration
  conversions drive the answer. Catalog: `mL_vs_L`, `forgot_dilution_factor`, `mean_not_median`.
- *History/civics (rubric-judged):* a binary decision from a short primary-source packet. The grader checks
  that every claim cites a packet source, the strongest opposing argument is stated fairly, and evidence is
  separated from inference. Needs a calibrated gold set and source-grounding rules first.
- *Book review (rubric-judged):* "Would you recommend this to a skeptical friend?" Graded on a quoted
  passage as evidence and a fair statement of the best objection.
Same loop each time: Coach.AI dialogue, provisional feedback, guide confirms. Different key.

## 3b. Additional requirements surfaced by the strategy pass

**R8 — The room as a product surface (Phase 2).** Support the live Socratic discussion: the guide's
pre-discussion stuck summary (Example 3), a vote → twist → re-vote flow with a visible
before/after, a cold-call roster that tracks who has spoken (the existing "track who's actually
talking" backlog item), and a timer keyed to the facilitator's pacing table. Today the app logs
discussions after the fact (`discussions` table); this makes them live. Acceptance: a guide
runs a full session from one screen without notes.

**R9 — Event log foundation (Phase 0, before the coach).** Every learner action becomes a row:
`(learner, case, step, event_type, payload, ts)` — attempt, hint request and level, catalog match,
twist reveal, submit, confirm. Without it the coach, analytics, calibration, efficacy and cost
tracking each invent their own logging. Acceptance: any metric in VISION → "How we'll know"
can be computed from the log alone. Extends the existing Postgres schema
(`programs, learners, assignments, submissions, discussions, ratings, scores…`); update
TECH_STACK.md in the same pass.

**R10 — Author surface (Phase 4, the other half of "platform").** The platform is not only more
subjects; it is letting a guide or teacher author a case through the same gates: a guided case
builder, the cold-read and sensitivity probes run for them, and a publish gate they can't skip.
The pipeline's skills (brainstorm → write → research → context → readiness) are the engine;
the product question is how much of that a non-technical author can drive. Prototype with Anuj
or one Acton guide authoring a single case.

**R11 — Authentic-work design (Phase 1).** Grade the reasoning trail, not just the final text:
require step attempts and notes to precede the pitch, include a "what I got wrong and why"
reflection, and surface revision history to the guide. Acceptance: a pitch pasted whole from a
chatbot, with no matching step attempts, is flagged for the guide, not auto-failed.

## 4. Non-functional requirements

| Area | Requirement |
|---|---|
| Honesty | UI labels AI output as AI; grades are "provisional" until a guide confirms |
| Safety | Leak test and injection test suites are release gates for R2/R3 |
| Cost | Per-student/per-case limits; monthly cap; model routing per 00_SESSION.md |
| Reliability | Coach/grader failure must never block saving or submitting work |
| Accessibility | Keyboard-operable coach, readable at MS reading level, works on a phone/tablet (guide runs the loop "from any device") |
| Testing | The admin app currently has zero automated tests (ROADMAP Housekeeping); R2/R3 endpoints ship with tests |
| Verification | No feature is "done" on text checks alone — live browser pass required |

## 5. Decisions (updated 2026-10-23 after Manan's answers)

**Decided**
1. **Build a rubric that matches our goals.** Needed; see R3 (revision proposed by review).
2. **Simple leaderboard.** Yes; design in R4.
3. **Recommended assignments** that link week to week; see profile in R5.
4. **Pilot 3 cases**, from different fields. Candidates under review (ROADMAP).

**Being worked**
5. **Model vendor, budget, key:** reviewed by R1a/b/c, summary in ROADMAP §2.
6. **Preliminary data and AI policy:** drafted as POLICY_PRELIMINARY.md, reviewed by R1a/b/c; deliberately
   light and non-restrictive for now.

**Still open**
7. Acton-system integration surface (needs Anuj).
8. Final retention periods and legal review before any non-pilot use (POLICY_PRELIMINARY §9).

## 6. Metrics (proposed; baselines don't exist yet)

- Activation: % of assigned Heroes who open and complete ≥ 1 step unaided.
- Help: hint requests per step; % resolved by catalog vs. LLM tail; % of wrong answers matched
  to a known misconception (target coverage figure to be set after the first pilot).
- Learning: first-try-correct rate on a step before vs. after the instruction fixes (R1).
- Trust: guide–AI agreement per criterion; guide override rate (already tracked: "grading
  machine getting overridden").
- Safety: leak-test failures (target 0), injection-test failures (target 0).
- Delight (qualitative): learner and parent comments from the pilot.
