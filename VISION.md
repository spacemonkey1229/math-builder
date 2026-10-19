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
