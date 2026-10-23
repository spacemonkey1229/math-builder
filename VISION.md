# VISION — Math Builder

**Version 2.0 · 2026-10-23 · Status: PROPOSED (needs Manan's sign-off)**
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
| Guide experience | Hand scoring | Skill-level view per step and per case; suggested focus; Heroes' feedback folded in | Same, plus authoring tools |
| Grading | Machine first pass → guide confirms | AI-drafted against a rubric built for our goals; guide confirms | Per-subject graders |
| Biggest risk | Quality we cannot see | Trust: answer leaks, mis-grading, children's data | Generalizing before one subject is proven |

## The Hero's journey

The journey tracker is the spine of the product. Each stop writes to the Hero's profile and history.

1. **Pick an assignment.** The Hero chooses from recommended cases that follow from their journey
   (fields explored, skills being built, what they asked to see more of), so one week links to the next.
2. **Kickoff.** Part of the assignment itself: just enough to explain the problem and its world,
   before any data. First vote, committed before reasoning.
3. **Work the steps with Coach.AI.** The notebook steps are a dialogue, not a form. The Hero enters
   an answer or a method; Coach.AI replies, asks, and probes. A wrong answer names the kind of
   mistake; being stuck gets a hint; the final answer is never given.
4. **Summary and feedback.** The Hero gives a summary pitch of their position. Coach.AI responds in the
   language of the rubric, provisional until the guide confirms.
5. **Discuss.** The live Socratic room: twist, re-vote, cold-calls. The guide arrives already knowing
   where the room got stuck, which skills to focus on, and where the strengths are.
6. **Reflect and give feedback on the case.** What was new, what was confusing, what they want to
   explore. This feeds the guide's workflow and the case's quality loop.
7. **Points, profile, history.** Completion and depth of work earn points. The profile shows the
   Hero's journey (fields touched, cases finished, a favorite pitch, growth over time), not just a score.
8. **Recommended next assignment**, which returns to step 1.

## What the guide needs

The guide is the buyer and the person in the room. Per case they need: the **core skill behind each
step**, an **assessment of how the cohort did on each skill**, **suggested focus** ("three of six
Heroes treated $80 as per-line; cold-call them"), **named strengths**, and the **Heroes' own feedback**
on the case. This is a first-class surface, not an afterthought (PRD R8).

## Incentives: the carrot

Aimed at the right behavior: **effort and depth**, not speed or raw score.
- **Simple leaderboard, v1.** Based on completed cases and the depth of pitches. Cohort-scoped to
  start. Design details and anti-gaming rules are in PRD R4.
- **Other carrots** (PRD R4): stars toward badges, personal bests, streaks, "most improved," fields
  explored, a peer-voted favorite pitch.
- **Integrated into the journey tracker,** so points come from the same events that record the
  journey. That requires **profiles and history** (PRD R5, R9), which also make the experience feel
  humane rather than like a scoreboard.

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

**Wedge.** Quantitative real-world cases for MS/HS in self-directed settings (Acton studios first,
then microschools, pods, co-ops): small, reachable through one champion, Socratic discussion already
the norm. Pilot on three cases from different fields.

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

**Rings: learn from each before widening.** Ring 1: one household (Anuj's kids), 3 pilot cases.
Ring 2: one studio cohort. Ring 3: several studios. Ring 4: other subjects and the platform.

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
- **Guardrails:** leak and injection failures stay at 0; guide override rate; AI cost per
  learner-case; whether the leaderboard drives depth, not just volume.

## When we'd change course

Decided *before* the pilot so the data can't be rationalized afterward.
- Coach.AI is used mostly to extract answers after two redesigns → it becomes guide-facing only.
- AI–guide agreement stays under the bar → AI stays a guide-side draft tool.
- The leaderboard produces volume without depth after two tuning rounds → drop points for volume;
  keep personal best and profile only.
- No one outside Anuj's circle wants it → stay a personal tool; skip pricing.
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
4. **Recognition rewards effort and depth.** Points reflect what a Hero did and showed, not speed.
   Raw score is never the ranking.
5. **Humans stay in the loop until the data says otherwise.** AI feedback starts as a draft a guide
   confirms; autonomy is earned by measured agreement.
6. **Children's data is a design input.** Minimal data, no identifiers to model vendors, consent
   before launch (POLICY_PRELIMINARY.md).
7. **One real thing before the general thing.** No platform abstraction before a second subject
   forces its shape.

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
