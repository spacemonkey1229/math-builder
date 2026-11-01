# VISION — Math Builder

**Version 2.1 · 2026-10-24 · Status: PROPOSED (needs Manan's sign-off)**
v1.0 (2026-10-19) opened with principles. This version opens with the purpose and moves the
guiding principles to their own section near the end. It does not change the contract: SPEC.md,
RUBRIC.md (under revision, see PRD R3) and the hard lines in 00_SESSION.md still govern.

---

## The vision

**Students experience math in the real world.** Each case is a real decision with real numbers, so
that a learner:

1. **Solidifies math concepts** by needing them to defend a choice, not by practicing them in isolation.
2. **Learns to structure real-world problems and complexity**: to decide what the question really is,
   what to ignore, what to assume, and what they still don't know.
3. **Gains exposure to fields and careers**: an insurer's actuary, a satellite crop analyst, a bridge
   engineer. And finds something they want to be curious about.

Underneath all three is the deeper goal: **confidence in complex problem solving.** A Hero should
finish a case believing "I can take a messy, unfamiliar problem and make progress on it," and have
evidence in their own history that it's true.

Product and platform are how this reaches more learners and more subjects. They serve the purpose;
they are not the purpose.

**Terms.** *Guide* is the human (the person the platform's feedback calls "the coach"). *Coach.AI* is the AI
that works with a Hero inside a case. This file uses those two words only.

## First deployment, and the guide's role

The goal is to get the platform **up and running with The Humanist Academy**, then **remove the guide from
the blocking and tackling**: assigning, tracking, chasing, reporting. The guide's time then goes where a
person matters most: **helping Heroes with the math concepts that are hard, and getting started on a case.**

| Today the guide does | The platform should do | The guide keeps |
|---|---|---|
| Picks and assigns the next case | Recommends and assigns from the Hero's journey (`suggest_cases()` already ranks cases from interests, grade and branch) | Override and approve |
| Tracks who is behind or stuck | Tracks, reminds, and reports automatically; surfaces **exceptions** only (the app's exception queue already flags OVERDUE, STALE, NO OPEN WORK) | Acting on an exception |
| Chases late work, writes progress updates | Nudges the Hero in-app; sends a parent/guide digest | Conversations that need a person |
| Confirms every score and badge | AI drafts, calibrated; guide confirms (a light check, then sampled as agreement is proven) | Final say on badges |
| (the part we want more of) Explaining hard concepts, unsticking a Hero at the start | Tells the guide *which Hero is stuck on which concept*, with what they tried | **This is the job** |

What is known about The Humanist Academy so far: it appears as a school in the Acton Survey case data.
Its program structure, cohort size, grade levels, current guide workflow and tools are **not yet known**
and are the first discovery item (Roadmap S1). Acton-system integration remains a later idea from Anuj.

## Where we are, honestly

- **Tool (today).** A rigorous authoring pipeline that produces quantitative case studies, each
  with a self-checking interactive page, a facilitator guide, and a mechanical publish gate. A hosted
  guide app (Flask on Vercel + Neon) runs assign → submit → score → confirm → badge.
- **Not yet happened:** a real cohort in a real room. Zero cases are `VERIFIED` (MCS-29). The first
  outside feedback (Anuj, using `phone-plan`) found real defects the gates missed.
- **Implication:** make the learner's experience inside a case excellent, prove it with real kids on
  a few cases, then widen.

## Three stages

| | **Tool** (now) | **Product** (next) | **Platform** (later) |
|---|---|---|---|
| Who it serves | An author-operator and one guide | Heroes, guides, parents in a cohort | Any studio; any subject |
| Learner experience | Static page; client-side "Check" | Coach.AI dialogue per step; end-of-case summary with feedback; journey tracker, profile, points | Same loop in other subjects and fields |
| Guide experience | Hand scoring and assigning | Skill-level view per step and per case; suggested focus; Heroes' feedback folded in | Same, plus authoring tools |
| Guide's time goes to | Operations: assign, track, chase, score | Hard concepts and getting started; exceptions only | Same, across more cohorts |
| Grading | Machine first pass → guide confirms | AI-drafted against a rubric built for our goals; guide confirms | Per-subject graders |
| Biggest risk | Quality we cannot see | Trust: answer leaks, mis-grading, children's data | Generalizing before one subject is proven |

## The Hero's journey

The journey tracker is the spine of the product. Each stop writes to the Hero's profile and history.
Every screen shows **one clear next step**.

1. **Pick (or be assigned).** Recommended cases that follow from the Hero's journey (fields explored,
   skills being built, what they asked to see more of), so one week links to the next. Once the platform
   runs the operations, assignment is automatic, with guide override.
2. **Warm-up, as needed.** A short, case-scoped readiness check on the foundational skills this case
   needs. It finds gaps and strengths and gives early wins. Strong Heroes skip it. Where a gap shows up,
   the Hero gets a few targeted drills, and if the problem is translating words into steps, a short
   word-problem lesson (PRD R12). This sets the Hero up for the case; it is not a separate course.
3. **Kickoff.** Part of the assignment: just enough to explain the problem and its world, before any
   data. First vote, committed before reasoning.
4. **Work the steps with Coach.AI.** A dialogue, not a form. Wrong answer names the kind of mistake;
   stuck gets a hint; the final answer is never given. When a step gets tough, the coach breaks it into
   smaller pieces and checks in rather than letting momentum die.
5. **Summary.** The Hero pitches their position using a five-part shape (below). Coach.AI responds in the
   rubric's language, provisional until the guide confirms.
6. **Discuss.** The live Socratic room: twist, re-vote, cold-calls. The guide arrives already knowing
   where the room got stuck, which concepts need help, and where the strengths are.
7. **Reflect and give feedback on the case.** What was new, what was confusing, what they want to explore.
8. **Points, profile, history.** Effort, depth, and persistence earn points; the profile shows growth.
9. **Next assignment**, which returns to step 1.

**The summary pitch has a shape** (this also teaches a Hero to talk about a solution, its implications,
its method and its assumptions): (1) *the underlying problem and why it matters*; (2) *the position, in
plain language*; (3) *a simple, relatable example of how it works*; (4) *what makes this option better than
the other*, and what would change the Hero's mind; (5) *the outcomes and implications, with the method and
assumptions underneath*. This maps onto rubric K1, K3 and K4 (PRD R3).

## What the guide needs

Once operations are automated, the guide is the **concept coach**. Per case they need: the **core skill
behind each step**, an **assessment of how each Hero did on each skill**, **who is stuck on what and what
they already tried**, **who hasn't started**, **suggested focus**, **named strengths**, and the **Heroes' own
feedback** on the case. The guide's home screen is an exception list (who needs a person today), not a
spreadsheet to scan. This is a first-class surface (PRD R8, R13).

## Incentives: the carrot

Aimed at the right behavior: **effort and depth**, not speed or raw score.
- **Simple leaderboard, v1.** Based on completed cases and the depth of pitches. Cohort-scoped to
  start. Design details and anti-gaming rules are in PRD R4.
- **Reward persistence, mastery and improvement, not activity.** Points also recognize coming back after
  a hard step, moving a skill from Not Yet to Practiced, and finishing a case that got tough. Streaks use
  grace weeks (no punishing resets).
- **Other carrots** (PRD R4): stars toward badges, levels and milestones, personal bests, fields explored,
  a peer-voted favorite pitch.
- **Integrated into the journey tracker,** so points come from the same events that record the
  journey. That requires **profiles and history** (PRD R5, R9), which also make the experience feel
  humane rather than like a scoreboard.

## Building independence: the learning workout

The platform's job is to make a Hero **less dependent on the guide over time**. The feedback pointed to
models that do this well: **Duolingo** (bite-sized lessons, immediate feedback, streaks, progression),
**Omada** (behavioral coaching, personal goals, accountability) and **workout apps** (routines, progressive
challenges, milestones). What we take, and what we don't:

| Take | Adapt | Don't take |
|---|---|---|
| Immediate feedback; progress you can see; milestones | Bite-sized **practice around the case** (warm-up, drills, step-sized wins), not a replacement for the case, which is a deep 2–3 hour decision | Loss-aversion mechanics (hearts, shame streaks) |
| Personal goals and a weekly rhythm (Omada-style) | A weekly goal the Hero sets with the platform; a parent/guide digest as the accountability loop | Rewards for raw volume of activity |
| Progressive difficulty (workout-style) | Difficulty ramps across cases and within a case's warm-up, matched to the Hero's skill grid | Leaderboards on raw score |

The case stays the main event. The workout wraps it: warm up, do the work, cool down with a reflection, and
keep momentum **especially when the case gets tough**.

## Who we build for

| | Who | Wants | Decides? |
|---|---|---|---|
| User | Hero (MS/HS learner) | Get unstuck without being told; be taken seriously; see their own growth | No |
| Buyer / champion | Guide, studio head, homeschool parent | Less prep and grading; know where to focus; evidence of growth | Yes |
| Influencer | Parents (Anuj is the prototype) | Proof the child is learning real reasoning and finding interests | Shapes adoption |
| Author | Us, then other guides | Real-use data flowing back into case quality | n/a |

## Strategy: hypotheses to test, not conclusions

Nothing here is validated. Evidence so far: one outside user's email and our own pipeline.

**The bet.** Building confidence in complex problem solving needs three things at once: *real*
problems (so the stakes feel real), *structure* (a repeatable way to break a messy problem down), and
*support at the moment of struggle* (so struggle produces progress, not quitting). A guide can't give
that moment-by-moment support to every Hero; Coach.AI plus a skill-aware guide surface can.

**What "deeper than a math tool" means for the strategy.**
- The product teaches a *method* (frame → assume → compute → defend → revise) that transfers across
  fields. The case library is the vehicle; the method is the point.
- Confidence is built by *evidence the Hero can see*: a history of problems worked and positions
  defended. The profile is therefore a core feature, not an add-on.
- Exposure to fields is a *designed* part of recommendation, not a side effect of case topic.

**Wedge and first deployment.** Quantitative real-world cases for MS/HS in self-directed settings, starting
with **The Humanist Academy** as the first live deployment (then other Acton-style studios, microschools,
pods, co-ops): small, reachable through one champion, Socratic discussion already the norm. Pilot on three
cases from different fields, then run the Humanist Academy cohort with the guide's operations automated.

**Positioning.** The feedback frames this as moving beyond a tutoring platform to a *personalized,
habit-forming* learning experience that combines skill development, real-world problem solving,
behavioral motivation and measurable progress. We adopt that **in service of the purpose**, not as a
repositioning: we are not a daily math-practice app or a tutor. Habit and motivation features exist to get a
Hero through real problems with less help.

**Why it could be defensible (none of this is a moat yet).** (1) A case library with mechanical truth
gates: trust. (2) Misconception catalogs plus step-level stuck data per case: a flywheel a generic
chatbot lacks. (3) Guide-confirmed grading data that calibrates the grader. (4) Hero journey data
(fields, skills, growth) that makes recommendations better over time.

**Where it differs from alternatives.** Practice products and generic AI tutors reward the right
number. This rewards a *defended decision under ambiguity*, grades the reasoning, and does it in
real-world fields. To map, not assert: the adjacent landscape, plus the marketing-tech comparisons
Anuj offered to share (Roadmap S2).

**Business model: open, decide after pilots.** Per-studio, per-learner, case packs, free tool + paid
coach/grading, open core + hosted, nonprofit/grant. AI is a *variable per-learner cost*, so cost per
learner-case is tracked from pilot one.

**Riskiest assumptions and the cheapest test for each.**
| # | Assumption | Cheapest test | Before |
|---|---|---|---|
| 1 | Heroes use Coach.AI to think, not to extract answers | Pilot; log dialogue and hint levels against final answers | Coach at scale |
| 2 | Guides trust AI-drafted feedback enough to confirm fast | Blind guide-vs-AI grading of existing student work | AI feedback shown to Heroes |
| 3 | Points for completed cases and pitch depth drive effort, not gaming | Pilot leaderboard; compare depth before/after; review outliers | Widening the leaderboard |
| 4 | Heroes' confidence actually rises | Short before/after self-rating plus guide observation | Claiming the outcome |
| 5 | Guides and parents would adopt and pay | About 5 structured conversations | Pricing, multi-tenant |
| 6 | The engine generalizes to another subject | One science case end to end | Platform abstraction |
| 7 | Acton-system integration is worth building | Discovery with Anuj | Any integration |
| 8 | A guide's operations can be automated without losing oversight | Run one cohort with auto-assign, tracking and reminders; measure guide minutes on operations vs. concept help; count missed exceptions | Removing the guide from assignment and tracking |
| 9 | A short case-scoped warm-up helps Heroes start and persist, rather than adding friction | Warm-up vs. no warm-up on pilot cases: completion, first-try on step 1, drop-off | Building drills for the whole library |
| 10 | Heroes become more independent over time | Share of steps resolved without a human, per Hero over successive cases | Claiming independence |

**Rings: learn from each before widening.** Ring 1: one household (Anuj's kids), 3 pilot cases. Ring 2:
**The Humanist Academy cohort**, with the guide's operations automated and the guide refocused on concept
help. Ring 3: other studios. Ring 4: other subjects and the platform.

**Quality is a system property, not a case fix.** The defects the first outside reader hit in
`phone-plan` are symptoms. The answer is gates that catch the class: an instruction-clarity lint, a
cold-read probe at authoring time, step-level confusion data from real use. `phone-plan` is the
reference example, not the strategy.

## How we'll know it works

- **North star (proposed):** cases a Hero completes with a defended position and reflection,
  confirmed by a guide, per active Hero per month.
- **Outcomes tied to the vision:** can structure an ambiguous problem (a rubric criterion, PRD R3);
  concept transfer (applies a method from case N in case N+k without a hint); breadth of fields
  explored; **self-reported confidence** before and after, tracked as a signal, not graded.
- **Independence and scalability (the feedback's goal):** share of steps resolved without a human; guide
  minutes per Hero per week on operations (target: falling) versus on concept help (target: rising);
  operations automated (assign, track, remind, report); a Hero's drop-off at hard steps.
- **Guardrails:** leak and injection failures stay at 0; guide override rate; AI cost per
  learner-case; whether the leaderboard drives depth, not just volume.

## When we'd change course

Decided *before* the pilot so the data can't be rationalized afterward.
- Coach.AI is used mostly to extract answers after two redesigns → it becomes guide-facing only.
- AI–guide agreement stays under the bar → AI stays a guide-side draft tool.
- The leaderboard produces volume without depth after two tuning rounds → drop points for volume;
  keep personal best and profile only.
- No one outside Anuj's circle wants it → stay a personal tool; skip pricing.
- Guide minutes on operations don't fall after the automation phase → the automation isn't working; fix it before widening.
- Habit mechanics raise activity but depth falls → strip them back to persistence and improvement only.
- Cost per learner-case sinks every model → shrink the AI surface.
- A science case needs an engine rewrite → the platform claim is premature; stay math-first.

## Design principles

The rules that shape *how* we build toward the vision.

Existing: defensible ambiguity · never fabricate a number or URL · machine drafts, human promotes ·
published ≠ verified · derive counts, never hand-write them.

For the product stage:
1. **Coach.AI asks; it never tells.** Hints climb a ladder; the final answer is never emitted.
2. **Diagnose before you generate.** Detect common mistakes in code; use the model to phrase the
   response and handle the long tail.
3. **The server holds the key.** Anything that counts is computed server-side; client checks are
   formative only.
4. **Recognition rewards effort, depth and persistence.** Points reflect what a Hero did and showed, not
   speed or volume. Raw score is never the ranking.
5. **Humans stay in the loop until the data says otherwise.** AI feedback starts as a draft a guide
   confirms; autonomy is earned by measured agreement.
6. **Children's data is a design input.** Minimal data, no identifiers to model vendors, consent
   before launch (POLICY_PRELIMINARY.md).
7. **One real thing before the general thing.** No platform abstraction before a second subject
   forces its shape.
8. **Automate operations; keep humans for judgment.** Assigning, tracking, reminding and reporting are
   the platform's job; concept help, getting started, and badge calls are the guide's.
9. **One next step.** Every screen tells a Hero and a guide exactly what to do next, with minimal navigation.

## Operating model and constraints

One operator working with AI agents (model routing per 00_SESSION.md), plus Anuj's offer to help and
test. Build only what a pilot needs; buy the commodity parts (model API, hosting, auth); every phase
shippable by one person in weeks; the pipeline's gates are the leverage. While Phases 0–1 run,
content batches slow to what the pilots need.

## Risks specific to AI in learning

- **Answer-extraction and over-reliance:** hint ladder, attempt-first, dialogue logging.
- **Authentic work:** a Hero can ask any chatbot to write the pitch. Design response: grade the
  reasoning trail (step attempts, revisions, reflection) and let the discussion be the check.
- **Gaming the leaderboard:** depth measures that can't be met by length alone; guide review of outliers.
- **Equity and access:** works on a shared phone or tablet.
- **Children's data:** POLICY_PRELIMINARY.md; Roadmap S3.

## Non-goals (for now)

- Replacing the guide or the Socratic discussion.
- A public marketplace, open signups, or monetization.
- Rankings on raw score.
- Rewriting the authoring pipeline; we add a learner-facing layer and feed data back.
