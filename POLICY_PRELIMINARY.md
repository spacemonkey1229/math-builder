# Data and AI Use Policy — PRELIMINARY v0.1

**Status: PRELIMINARY v0.2 · 2026-10-23 · not legal advice · not reviewed by counsel or a school.**
v0.2 folds in a fact-check by the R1b reviewer against FTC, Cornell LII (16 CFR 312), the US Dept. of Education and vendor terms pages.
**Purpose:** a simple set of working rules for the pilot (Phase 0–1) so the platform can move
forward. It is deliberately light: it does **not** restrict what the platform may become, and it
is meant to be revised after the pilot. Each rule says whether it is a *commitment now* or a
*pilot practice*.

---

## 1. What we collect (commitment now)

Collect the minimum needed to run a case and show a learner their own growth:
- A display name (first name or alias) and an internal opaque id. *An opaque id is still a persistent identifier, which COPPA treats as personal information; minimizing what we collect does not remove the consent duties in section 5.*
- Their work: step attempts, hint requests, notes, pitch, reflection, submission timestamps.
- Feedback they give on a case.
- Guide actions: confirmations, discussion notes, badges.
We do **not** collect: last names, birthdates, home address, school name, photos, government or
financial identifiers, or any precise location.

## 2. What goes to an AI model vendor (commitment now)

- Only the case step text, the learner's own input for that step or submission, and an opaque id.
- We never *send* a name, school, email, or other identifier ourselves. But learner **free text**
  (pitch, notes, chat) goes to the vendor as typed. The interface warns learners not to type personal
  details, and the server drops obvious personal details (emails, phone numbers) from free text before
  it is sent. Both are best-effort, not guarantees.
- **Vendor baseline.** Use a **paid API account only, never a free tier**, with terms that do not train
  on our data. Realistic baseline today: no training on customer content, and the vendor keeps inputs and
  outputs for up to about 30 days by default. Zero data retention is *not* self-serve (it needs a
  separate agreement or approval), so we do not rely on it. Re-check the vendor's current terms before
  any non-author child uses AI features.
- Learners are told, in plain words, when they are talking to an AI.

## 3. How AI is allowed to act (commitment now)

- The coach never gives the final answer to a graded step.
- AI feedback on writing is **provisional** until a guide confirms it. A badge is only ever awarded
  by a human.
- The AI never contacts anyone outside the platform and never sees another learner's work.

## 4. Who can see what (pilot practice)

- A learner sees their own work and history.
- Their guide sees their cohort's work and the AI drafts.
- A parent or guardian sees their own child's work and progress on request.
- Other learners see only what a learner chooses to show on the leaderboard (display name or alias,
  completed cases, depth-of-pitch measure). Never answers, notes, or drafts.
- Leaderboard participation is **opt-in**, and a learner can switch to an alias or leave at any time.

## 5. Consent (pilot practice)

- **Who is covered.** COPPA applies to children under 13, or to anyone we have actual knowledge is under
  13. FERPA generally applies only if a public, federally funded school is a partner; a private or
  household pilot is typically outside it. Neither is assumed away: treat every pilot child as covered.
- **Consent.** Because a child's text is sent to an AI vendor, plain "reply OK" consent is not enough.
  Before a child uses AI features, the parent or guardian replies to an email that names **the AI vendor
  and the types of data sent** (the child's answers, notes and pitch text), says who sees the work, and
  explains how to review it, delete it, and refuse further collection. Keep the reply. This is cheap and
  enough for a small family pilot; it is a pilot practice, not a legal conclusion.
- **Parent rights.** A parent can review their child's data, have it deleted, and refuse further
  collection at any time.
- Before any wider rollout, this section is reviewed by counsel against COPPA (16 CFR 312), any state
  student-privacy law, and the policies of any school or studio involved. **Open.**

## 6. Keeping and deleting (pilot practice)

- Work and history are kept while the learner is active, so their profile and journey are
  meaningful.
- On request from a learner's parent or guardian, we delete their data (the platform already has a
  learner-delete path), stop further collection if asked, and tell them when it is done.
- Raw prompts and model outputs are logged only to improve the coach and the grader, with the
  learner's id replaced by the opaque id. The retention period is an **open question** for the pilot.

## 7. Safety and incidents (pilot practice)

- If a learner's input suggests they or someone else is in danger, the coach stops the exercise
  and the guide is told. (Exact wording is an open item.)
- If we learn that data was exposed or an AI response was inappropriate, we tell the guide and
  the affected family promptly, fix it, and record what changed.
- Coach and grader failures never block a learner from saving or submitting their work.

## 8. Fairness and honesty (pilot practice)

- We tell learners what the grade or feedback is based on (the rubric).
- Guides can override any AI draft; overrides are kept and used to improve the grader.
- We track guide–AI agreement and publish it to the pilot families.

## 8a. API key and spend (pilot practice)

- The model account is a **paid** account owned by the operator personally (not a shared studio
  account), so it can be shut off by one person.
- The key lives only as a server-side environment variable, one per environment (dev/preview separate
  from production), marked sensitive, never in page code, logs, or the repository. Rotate on any
  suspected exposure and at the start of each pilot phase.
- A hard monthly spend limit is set in the vendor console, plus per-learner and per-day call caps and a
  kill switch in the app.

## 9. Open items

1. Retention period for logs and for learner work after a learner leaves (the vendor itself keeps data for up to about 30 days).
2. Who is the data owner when a studio or school is involved.
3. Final wording of the safety-escalation rule.
4. Legal review before any non-pilot use (COPPA, state student-privacy law, school agreements, a data-processing agreement with the vendor).
5. Whether to offer an "export my history" feature.
