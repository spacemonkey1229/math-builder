---
name: submission-score
description: "Auto-score a Hero's case-study submission against RUBRIC.md and produce a complete machine first-pass verdict on all seven criteria. Use when the user says \"score this submission\", \"grade Avery's Cold Chain work\", \"run the rubric\", \"first pass on these submissions\", \"is this badge eligible\", \"what's their growth score\", \"confirm the score\", \"I disagree with C3\", \"log an override\", \"how did the cohort do\", \"which criteria did the group struggle with\", or after case-track records a submission. Ingests docx / pdf / md / xlsx plus the case.json it answers; recomputes the Hero's numbers against the case appendix data; checks whether the visual's data is copied from the case or original; and emits BOTH the mastery gate (badge_eligible = all seven at least Proficient) and the weighted 0-100 growth score, never averaged together. Writes student_work/<learner>/<case>/SCORE.md and appends to readmodel/submissions.json scores[] with status machine-first-pass. A guide-confirm step flips it to confirmed and logs every override to readmodel/score_overrides.json. NEVER final: the machine drafts, a human promotes."
---

# submission-score — the machine first pass

The only skill that forms an opinion about a Hero's work, and it is never allowed to be the last
word. `case-track` records *state* and deliberately has no scoring field; this skill produces the
*draft verdict* that a guide starts from.

> **The point is scale.** A guide reviewing twenty submissions should start from a filled-in form,
> not a blank one. That is why the machine emits all seven criteria even where it is guessing —
> but every guess carries a confidence flag, and every LOW-confidence verdict is surfaced first,
> not buried.

## Contract

| | |
|---|---|
| **Reads** | the submission files, `cases/<id>/case.json`, `cases/<id>/case.md`, `readmodel/submissions.json`, `readmodel/roster.json`, `RUBRIC.md` |
| **Writes** | `student_work/<learner>/<case>/SCORE.md` · `readmodel/submissions.json` → `scores[]` · `readmodel/score_overrides.json` |
| **Never writes** | `assignments[]`, `submissions[]`, `discussions[]` (those are `case-track`'s), `standards_spine.json`, `cases_index.json`, anything under `cases/` |

Write ownership in `submissions.json` is **split by array**: `case-track` owns three, this skill
owns `scores[]`. No skill writes an array it does not own.

---

## The three hard limits

These come from `RUBRIC.md` and they are binding. They are enforced in code, not just documented —
`score_submission.py` asserts limit 2 before it will write, and `guide_confirm.py` is the only
script that can set `status: confirmed`.

**1 · A machine BLOCKER on C3 is advisory, not final.**
When recomputation disagrees with the Hero, the Hero may be right and the check may be wrong —
especially where the Hero declared their own assumption. Every disagreement is rendered as
*CHECK THIS*, never as *wrong*, and never surfaced to the learner as an error. The guide
adjudicates. This is not politeness; on the Cold Chain fixture the machine's 7,771 and the Hero's
8,200 were **both correct** under different allocation readings, because the case never states an
allocation rule. A scorer that said "wrong" would have been wrong.

**2 · The machine may never mark C7 Exemplary.**
Recognising that someone reframed the question well requires reading an argument, not scanning
one. `_c7()` clamps the ceiling to Proficient and asserts it. Only a guide override can set C7
Exemplary, and that override is logged.

**3 · Every verdict is `machine-first-pass` until a guide confirms.**
Unconfirmed verdicts do not count toward a badge and render as INTERIM on the dashboard. Machine
drafts, human promotes — the same rule as everywhere else in this system.

---

## The two outputs, and why they are never averaged

```bash
python3 skills/submission-score/scripts/score_submission.py \
    --learner <id> --case <id> --file <path> [--file <path>] [--write]
```

**Mastery gate** — `badge_eligible = all(criterion >= Proficient)`. No partial credit, no
compensation, no "three Exemplaries cover one Not Yet."

**Growth score** — 0–100, weighted C1…C7 at **5 / 20 / 20 / 15 / 15 / 15 / 10**, with
Not Yet = 0, Proficient = 70, Exemplary = 100. All-Proficient scores 70.

They answer different questions. The gate is blind to trajectory; the score is blind to readiness.
Averaging them produces a number that means nothing and reads like a grade. **If a learner asks
what their score is, the answer is that it is a tool for their guide, and the number that matters
is which criteria are still Not Yet.**

## What the machine can actually see

| Criterion | Signal | Typical confidence |
|---|---|---|
| C1 research | link present; "how to…" phrasing; cues that the skill was *learned* (a false start, a correction); **MCS-39 (2026-08-01)** — flags LOW if the submitted link is byte-identical to a URL already embedded in the case's own interactive-HTML glossary, since that doesn't by itself show independent research | MEDIUM, LOW at Exemplary or on a glossary-repost |
| C2 pitch | word count (prose only, tables and appendix excluded); position-statement detection; hedge detection; self-counter-argument cues | HIGH at the 250-word floor, MEDIUM above it |
| C3 correctness | **recomputation** of every case quantity against `case.json.derived` and `balance_test` | LOW — advisory by rule |
| C4 deliverables | checklist from `case.json.deliverables[]`, by id and by keyword overlap | MEDIUM |
| C5 visual | image/chart presence; **originality** of the underlying data | MEDIUM, LOW when the data cannot be extracted |
| C6 discussion | contribution count and engagement cues from `submissions.json.discussions[]` | MEDIUM, LOW at zero |
| C7 framing | metric-named and alternative-metric cues | **always LOW** |

### Recomputing the Hero's numbers

The machine builds a value table from `case.json.derived` and `balance_test`, finds each quantity
by label in the submission, and compares. Three outcomes, and the third matters:

- **AGREES** — within 0.5% relative. A Hero who rounds 8,571.43 to 8,571 has not made an error.
- **CHECK** — a plausibly-same-quantity figure that differs. *Advisory.*
- **NOT ADDRESSED** — the Hero never stated this figure. **Absence is not disagreement**, and it is
  not a zero.

Two scoping rules keep this honest, both learned from false positives during build: the search
window is the **line** containing the label (a character radius spills across spreadsheet rows and
"finds" the next container's cold life), and the reported figure is the candidate nearest **in the
text**, restricted to within an order of magnitude — "a margin of 17.1%" reports 17.1, not
whichever number in the sentence happens to sit closest to the expected value.

### Originality of the visual (C5)

> "Original" means the Hero built it. Re-typing Appendix A into a table is not a visual display.

The machine extracts the visual's **underlying data** — chart series ranges from `.xlsx`, or the
tables adjacent to the image — and measures what fraction appears **verbatim** in `case.md`.

| copied fraction | reading |
|---|---|
| ≥ 80% | the visual re-displays the case's own appendix data → **Not Yet** |
| ≤ 50% | the majority of plotted values are the Hero's own → **Proficient** |
| in between | mixed; LOW confidence, the guide decides whether the derived part carries the argument |
| data not extractable | **UNDETERMINED**, reported as such — never scored as absent |

A visual the machine cannot read (a photo of paper, a Desmos link) is a **false negative** and the
report says so. Check the appendix link before acting on a C5 Not Yet.

### Tier adjustment

Read from `case.json.tier`. It changes what Proficient **requires**; it does **not** scale the
score — a Proficient T1 and a Proficient T4 both score 70, because the score tracks *this Hero's*
growth, not cross-tier comparison.

| Tier | Additional requirement | Gates |
|---|---|---|
| T1 | — | — |
| T2 | the trade-off between the two competing variables is named explicitly | C2 |
| T3 | some case data is correctly identified as irrelevant and set aside | C3 |
| T4 | at least one assumption stated, justified, and its sensitivity tested | C3 |

Detection is by cue phrase and is therefore fallible; a tier cap is always applied at LOW
confidence and is a prime override candidate. A guide may move which criterion the tier note gates.

---

## Guide confirm — and why overrides are the point

```bash
python3 skills/submission-score/scripts/guide_confirm.py \
    --learner <id> --case <id> --by "<name>" \
    --override C3=Proficient --reason "<why>" [--override ... --reason ...] --write
```

Flips `machine-first-pass` → `confirmed`, records **who** confirmed and **what** they overrode,
recomputes both outputs, and appends every override to `readmodel/score_overrides.json`.

- An override with no `--reason` is **refused**. An unexplained override is not a training signal,
  it is noise.
- There is no "reject" state. A guide who disagrees overrides the criterion and confirms, so the
  disagreement is *captured* rather than discarded.
- The log is append-only. A correction to an override is a new row — the wrong call is part of the
  signal.

### The 30% rule

```bash
python3 skills/submission-score/scripts/guide_confirm.py --audit
```

**A criterion the machine gets wrong more than ~30% of the time should be demoted to "guide
only"** — removed from the machine first pass entirely, rather than left emitting a verdict a
guide has to undo. Tolerating a 40%-wrong criterion is worse than not scoring it, because a wrong
first-pass verdict *anchors* the guide who reads it. Rates on fewer than 8 confirmed records are
noise and the audit reports counts instead of percentages.

The audit also reports the **direction** of every override, which is the actual bias measurement:

- consistently **raised** → the machine reads *harsh*; a cue-phrase detector cannot see reasoning
  that is present but phrased unusually. Fix: widen the detector.
- consistently **lowered** → the machine reads *generous*; presence was detected and quality was
  not. Fix: demote the criterion.

Expected hot spots, documented in `score_overrides.json` so nobody mistakes them for bugs: **C7**
(the machine is guessing entirely and is clamped below Exemplary), **C3** (advisory by rule — an
override is the system working), and **C6** (almost always a *recording* gap, not a scoring
defect; fix the habit before touching the scorer).

---

## Cohort roll-up — feedback on the CASE

```bash
python3 skills/submission-score/scripts/cohort_rollup.py --case <id> [--cohort <name>]
```

Which criteria did the *group* struggle with? A criterion where most of a cohort lands Not Yet is
**feedback on the case, not on the learners**, and the roll-up ends by naming what to hand back to
`case-readiness`:

| criterion fails cohort-wide | what it implicates in the case |
|---|---|
| C2 | the dilemma may not feel like a real fork — re-run Tier 2 probe 2 (both-sides solve) |
| C3 | ambiguous appendix data, or an unstated convention forcing different answers — re-run Tier 2 probes 1 and 5 |
| C4 | Challenge 3's deliverables are under-specified. The most directly fixable defect on the list |
| C5 | the case never modelled what an original visual looks like |
| C6 | a recording gap, not a learner gap. Check the guide's habit first |
| C7 | either the case gave no reason to question the metric, or — per RUBRIC's own open question — C7 is too hard at this tier and *the criterion is wrong, not the Heroes* |

Unconfirmed scores are **excluded** by default: a roll-up built on machine drafts measures the
machine, not the cohort. Zero confirmed records prints "nothing to roll up" rather than a
misleading table of zeros.

---

## Peer and self review

Every submission carries `templates/SELF_REVIEW.md` and `templates/PEER_REVIEW.md` — three
questions each, one page each. **Neither sets the verdict**; both are visible to the guide and to
the Hero, and the guide sees them *before* the machine's first pass. They are rehearsal for the
Socratic discussion and the cheapest way to raise C2 and C5 across a cohort.

## Report back

The seven criteria with levels and confidence flags; the mastery gate and the growth score, stated
separately and never combined; the LOW-confidence list to read first; the recomputation table with
CHECK items called out as advisory; and the exact `guide_confirm.py` command.

## Never

- **Never present a C3 disagreement as an error.** "Check this," always. The Hero may be right.
- **Never mark C7 Exemplary.** Hard limit, asserted in code.
- **Never write `confirmed`** from the scorer. Only `guide_confirm.py`, only with a named human.
- **Never average the mastery gate and the growth score**, and never show the score to a learner
  as a grade.
- **Never report an unreadable file as an empty one.** `files_unreadable[]` is printed under a
  NOT READ heading; nothing is scored against a file the machine could not open.
- **Never read zero discussion records as zero participation.** It means *not recorded*.
- Never award a badge. That is a human act, recorded by `case-track` in `roster.json`.
