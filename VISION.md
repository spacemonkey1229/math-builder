# VISION — Math Builder

**Version 1.0 · 2026-10-19 · Status: PROPOSED (needs Manan's sign-off; see Open decisions in PRD.md)**
Trigger: first outside-user feedback (Anuj, 2026-10-17) — "evolve it from a tool to a product,
and eventually to a platform." This file turns that into a direction. It does not change the
contract: SPEC.md, RUBRIC.md and the hard lines in 00_SESSION.md still govern.

---

## One sentence

**A learner defends a real decision with evidence they can show — and a coach that asks good
questions (never gives the answer) helps them get there, then helps them see how they did.**

## Where we are, honestly

- **Tool (today).** A rigorous authoring pipeline that produces quantitative case studies, each
  with a self-checking interactive page, a facilitator guide, and a mechanical publish gate.
  A hosted guide app (Flask on Vercel + Neon, shared passcode) runs assign → submit → score →
  confirm → badge.
- **What has never happened:** a real cohort in a real room. Zero cases are `VERIFIED`
  (MCS-29). The first outside feedback (Anuj, using `phone-plan`) is the first signal from a
  user who is not us — and it found real defects the gates did not (an ambiguous twist
  instruction, a twist locked to a different scenario than the learner chose).
- **Implication:** the next stage is not "more features." It is *make the learner's moment
  inside one case excellent, prove it with real kids, then widen.*

## Three stages

| | **Tool** (now) | **Product** (next) | **Platform** (later) |
|---|---|---|---|
| Who it serves | An author-operator and one guide | Heroes, guides and parents in a cohort | Any Acton-style studio; any subject |
| Learner experience | Static case page; client-side "Check" buttons | Coach that hints and diagnoses; one-click Submit; fast, kind, rubric-anchored feedback; stars/badges | Same loop, subject-agnostic; richer recognition |
| What "done" means for a case | Passes the publish gate | Passes the gate **and** survives real learners (Tier 3) | Authored by a pipeline, verified by data |
| Grading | Machine first pass → guide confirms | AI-drafted, calibrated against human grades; guide confirms for badges | Per-subject graders (deterministic keys *and* rubric-judged writing) |
| Biggest risk | Quality we cannot see | Trust: a bot that leaks answers, mis-grades, or mishandles kids' data | Generalizing before the first subject is proven |

## Who we build for

- **Hero (learner), MS/HS.** Wants to be taken seriously, hates being stuck alone, hates being
  told the answer. Needs: unstick me without stealing the thinking; tell me honestly how I did.
- **Guide (facilitator).** Needs: see who is stuck *where* before the discussion, trust the
  score enough to confirm quickly, and keep the final say on badges.
- **Parent / sponsor.** Needs: evidence of growth that is not a single number. (Anuj is the
  prototype; he also volunteered to test with kids.)
- **Author (us).** Needs: real-use data flowing back into case quality, so each case gets
  better, not just published.

## Strategy — hypotheses to test, not conclusions

Everything below is a bet with a cheap way to find out. Nothing here is validated; the sources of
evidence are one outside user's email and our own pipeline.

**The bet.** In Acton-style studios the scarce thing is not worksheets — it is *guide time and
trustworthy feedback on reasoning*. Decision-based cases plus an AI coach and a calibrated grader
could let rigorous, discussion-based learning run beyond a room that happens to have an
exceptional guide.

**Customer, user, buyer — three different people.**
| | Who | Wants | Decides? |
|---|---|---|---|
| User | Hero (MS/HS learner) | Get unstuck without being told; be taken seriously | No |
| Buyer / champion | Guide, studio head, homeschool parent | Less prep and grading load; evidence of growth | Yes |
| Influencer | Parents (Anuj is the prototype) | Proof the kid is learning real reasoning | Shapes adoption |

**Wedge.** Quantitative cases for MS/HS in self-directed settings (Acton studios first, then
microschools, pods, co-ops): small, reachable through one champion, and Socratic discussion is
already the norm there. Not a general math-practice product.

**Why it could be defensible (honest: none of this is a moat yet).**
1. A case library with mechanical truth gates (never a fabricated number or URL) — *trust*.
2. Per-case misconception catalogs and step-level stuck data — a data flywheel a generic
   chatbot lacks. Only real once kids use it.
3. Guide-confirmed grading data that calibrates the AI grader.
4. A pipeline that can produce and verify new cases at quality.
Today the library is machine-verified but human-unproven (zero `VERIFIED`).

**Where it differs from the obvious alternatives.** Answer-practice and generic AI tutors reward
the right number; this rewards a *defended decision under ambiguity* and grades the reasoning.
To map, not assert: the adjacent landscape (AI tutors, adaptive practice, project/case curricula,
LMS/grading tools) — a Phase 0 research task, together with the marketing-tech comparisons Anuj
offered to share.

**Business model — open, decide after pilots.** Options: per-studio subscription · per-learner ·
case packs · free tool + paid coach/grading · open core + hosted · nonprofit/grant. AI cost is a
*variable per-learner cost*, so track cost per learner-case from the first pilot; it constrains
every option. Kids' data makes trust a prerequisite for any of them.

**Riskiest assumptions and the cheapest test for each.**
| # | Assumption | Cheapest test | Before |
|---|---|---|---|
| 1 | Kids use a hint coach to think, not to extract answers | Pilot with Anuj's kids; log hint ladder use vs. final answers | Building Coach v1 at scale |
| 2 | Guides trust AI-drafted grades enough to confirm quickly | Blind guide-vs-AI grading of the existing student work | Showing AI grades to learners |
| 3 | Guides/parents would adopt and pay | ~5 structured conversations (Anuj's network, Acton guides) | Any pricing or multi-tenant work |
| 4 | Case quality scales without the author in the loop | Measure pipeline throughput and gate-fail rate; step-level stuck data per case | Promising a catalog size |
| 5 | The engine generalizes to another subject | One science case prototype end to end | Any platform abstraction |
| 6 | Acton-system integration is worth building | Discovery with Anuj: what systems, what data, who owns it | Any integration work |

**Rings — learn from each before widening.** Ring 1: one household (Anuj's kids). Ring 2: one
studio cohort. Ring 3: several studios (accounts, multi-tenant, guide analytics). Ring 4: other
subjects and the platform.

**Quality is a system property, not a case fix.** Individual case defects (like the `phone-plan`
step instructions and undefined vocabulary the first outside reader hit) are symptoms. The
product answer is gates that catch the class — an instruction-clarity lint, a cold-read probe at
authoring time, step-level confusion data fed back from real use — so the next 190 cases don't
need the same repair. The `phone-plan` fix is the reference example, not the strategy.

## The experience, end to end (one Hero, one case)

1. **Assigned** — the guide assigns a case; the Hero opens a link (no account friction at first).
2. **Launch** — overview hook, background, the binary dilemma; first vote *before* any data.
3. **Work** — the notebook steps. Wrong answer → the coach says which *kind* of mistake it
   resembles; stuck → a hint ladder; never the answer. (Worked examples: PRD §3a.)
4. **Submit** — one click; numbers scored server-side; notes and pitch get rubric-language feedback,
   marked provisional.
5. **Discuss** — the live Socratic room is half the product: twist, re-vote, cold-calls. The guide
   arrives already knowing where the room got stuck.
6. **Grow** — stars toward a badge, what's still "Not Yet," next case recommended from the skills
   map. Parents see evidence, not a rank.

## How we'll know it works

- **North star (proposed):** *cases a Hero completes with a defended position and reflection, that a
  guide confirms* — per active Hero per month. Counts real finished reasoning, not logins.
- **Learning outcomes (not just engagement):** rubric criteria moving Not Yet → Proficient over
  successive cases; first-try-correct on a step after instruction fixes; transfer (a Hero applies
  a method from case N in case N+k without a hint).
- **Efficacy design:** the ~437-skill spine (as of 2026-09-06) gives a mastery map; define a simple
  pre/post on the skills a case claims before asserting any learning gain.
- **Guardrail metrics:** leak/injection failures (0), guide override rate, AI cost per learner-case,
  hint-dependence (a Hero who only advances via Level 3 hints is a coaching signal, not a score).

## When we'd change course (kill / pivot criteria)

Decide these *before* the pilots so the data can't be rationalized afterward.
- Hints are used mostly to extract answers after two design iterations → the coach is the wrong
  form; fall back to guide-facing diagnosis only.
- AI–guide agreement stays below the bar after calibration → keep AI as a guide-side draft tool;
  never learner-facing.
- No guide or studio outside Anuj's circle wants it in 5 conversations → stay a personal/portfolio
  tool; skip multi-tenant and pricing work.
- Cost per learner-case makes every business-model option negative → shrink the AI surface (more
  deterministic, less LLM).
- A science prototype needs a rewrite of the engine, not a content swap → the "platform" claim is
  premature; stay math-first.

## Operating model and constraints

Today this is one operator working with AI agents (model routing per 00_SESSION.md), plus Anuj's
offer to help and test. Implications: build only what a pilot needs; buy/borrow the hard commodity
parts (model API, auth, hosting) instead of building them; every phase must be shippable by one
person in weeks; the pipeline's gates are the leverage that lets one operator keep quality. What
we deliberately *stop* doing while Phases 0–1 run: broad new-case batches beyond what pilots
need (content track continues at a lower cadence).

## Risks specific to AI in learning

- **Answer-extraction and over-reliance** — mitigated by hint ladder, attempt-first, hint logging.
- **Authentic work** — a Hero can ask any chatbot to write the pitch. Design response, not
  detection: grade the *reasoning trail* (notes, step attempts, revisions), require the Hero's own
  numbers and a reflection on what they got wrong, and let the guide's discussion be the check.
- **Equity and access** — works on a shared phone/tablet; no reliance on paid add-ons.
- **Children's data** — see S3 and PRD R5.

## Principles

Existing (keep): defensible ambiguity · never fabricate a number or URL · machine drafts,
human promotes · published ≠ verified · derive counts, never hand-write them.

New for the product stage:

1. **The coach asks; it never tells.** Hints climb a ladder (nudge → pointer → worked analogue).
   The final answer is never emitted. Same spirit as MCS-37 (no answers in placeholders).
2. **Diagnose before you generate.** Most wrong answers in a well-built case are a *small
   set of predictable mistakes* (forgot tax, used total lines instead of lines beyond 2).
   Detect those in code first; use the language model to phrase the nudge and to handle the
   long tail. Cheaper, safer, testable.
3. **The server holds the key.** Anything that counts (a submitted grade) is computed server-
   side. Client-side checks stay as instant, formative feedback only.
4. **Mastery over rank.** RUBRIC.md already warns that scores "corrupt motivation the moment
   they become the point." Recognition (stars, badges, streaks) attaches to *what you
   demonstrated*, not to *where you rank against peers*. Leaderboards are parked, not rejected
   (see ROADMAP Parking lot).
5. **Humans stay in the loop until the data says otherwise.** AI grading starts as a draft the
   guide confirms. Autonomy is earned by measured agreement with human graders, not assumed.
6. **Kids' data is a design input, not a footnote.** Minimal data, no PII to model vendors,
   consent before launch, per-assignment identity before any bot ships.
7. **One real thing before the general thing.** Don't abstract the platform until a second
   subject forces the shape. Keep the seam clean; don't build the framework.

## What success looks like

- **Product (12-month horizon):** a cohort of real Heroes completes cases end-to-end without
  the author in the room; hint usage and stuck-points are visible per step; AI-drafted grades
  agree with guide grades closely enough that confirming takes seconds; at least one case
  reaches `VERIFIED`.
- **Platform (beyond):** a second subject (science first) ships through the same engine with
  its own deterministic keys; then one *subjective* subject (history/civics/book review)
  graded against a rubric with source-grounding requirements, calibrated like math was.

## Non-goals (for now)

- Replacing the guide or the Socratic discussion — the bot supports the written work, not the
  room.
- A public marketplace, open signups, or monetization.
- Public competitive rankings of children.
- Rewriting the case-authoring pipeline; it works and is gated. We add a learner-facing layer
  on top and feed data back into it.
