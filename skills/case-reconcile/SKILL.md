---
name: case-reconcile
description: "Tag untagged legacy math case studies against the standards spine (MCS-17/MCS-38). Use when the user says \"reconcile the legacy cases\", \"tag the untagged cases\", \"run case-reconcile\", \"close the 31 untagged cases\", \"what skills does the Pets case cover\", or asks whether the coverage/gap numbers on the dashboard are trustworthy. Machine PROPOSES spine-skill matches with a quoted evidence sentence for every candidate; nothing is written into standards_spine.json or cases_index.json until a human runs --confirm by name. This skill cannot invent a match with no textual evidence, and it will not silently confirm a low-confidence guess."
---

# case-reconcile — close the tagging gap without fabricating one

Track B1. The 97-uncovered-skills figure on the dashboard is an upper bound polluted by cases
that were never tagged against the spine at all — not because they don't touch those skills, but
because nobody has looked. This skill looks, honestly, and says when it can't tell.

> House doctrine: **Machine drafts, human promotes (MCS-12).** This skill has exactly the same
> shape as `gap-close`/`cbc-gap-close` in the sibling portfolio projects: propose with evidence,
> stage, never touch the frozen file until an explicit confirm.

## What it does

```
python3 skills/case-reconcile/scripts/reconcile.py --propose --project .
```

Walks `source/Y1`, `source/Y2`, `source/Y3` for every `Case Study*.docx`, extracts the real title
from the document's own first heading (not the folder name — they disagree constantly: "Movie
Producer" the folder, "Movie Executive" the doc), and compares that title against
`standards_spine.json`'s `cases[]` list. Anything not already there is untagged.

**Excludes `source/Best Of Studio/` entirely.** Those are student submissions of already-tagged
cases (e.g. "Audrey Case Study - Airstrike" is a kid's answer to the existing `Airstrike` case),
not new case sources. Confusing the two would double-count a case as if it were two.

For every untagged case, it proposes spine-skill matches with a quoted evidence sentence, and
grades its own confidence rather than presenting every hit as equally solid:

- **HIGH** — the label appears as its own bare line, the way Cold Chain's Appendix G lists
  vocabulary verbatim. Real evidence: someone put "Bar Graph" on its own line on purpose.
- **MEDIUM** — a multi-word label (e.g. "Simple Random Sampling") found inside running prose.
  Specific enough that a coincidental match is very unlikely.
- **LOW** — a single generic word (e.g. "Time", "Even", "Range", "Side", "Term", "Degree") found
  only in running prose. These are common English words as often as they are math vocabulary.
  Presence is not evidence of use.

**A real, load-bearing finding from the first run:** most of the Y1–Y3 corpus does NOT carry an
explicit vocabulary appendix the way Cold Chain and a handful of others do (Fast Food, Medical
Statistician). For those cases, the matcher correctly returns mostly LOW-confidence noise — that
is the honest answer, not a bug to paper over with a looser threshold. A case with 0 HIGH/MEDIUM
matches needs a human to actually read it, not a smarter regex.

**2026-08-01 — that human read actually happened.** All 30 remaining 0-HIGH/0-MEDIUM cases were
read directly (source docx, not just the LOW-match snippets). Two outcomes: (1) fixed a real bug
in `match_term()` — the word-boundary regex didn't tolerate a plain plural, so "Histograms" never
matched the "Histogram" skill even as a bare word — and (2) hand-confirmed 10 cases via `--skills`
where the sentence showed genuinely load-bearing math content (a real given figure, a named
methodology, an explicit deliverable), not coincidental English ("Time" from "long-term", "Age"
from "age 45"). 18 of the 30 were read and correctly left untagged — the source text names no
math content explicitly, which is a real property of that era of case, not a gap in the tool.

## Confirming one case

```
python3 skills/case-reconcile/scripts/reconcile.py --confirm "Fast Food"
```

Confirms **HIGH + MEDIUM confidence proposals only**, by default — LOW-confidence matches never
ride along silently. Override with `--skills id1,id2,...` to hand-pick an exact set (including
specific LOW matches a human has actually read and agrees with), or `--include-low` to accept
every LOW match too (not recommended without reading the case first).

Confirming: snapshots `standards_spine.json` and `cases_index.json` to `readmodel/_snapshots/`
(MCS-22), appends the case title to `covered_by[]` for each accepted skill, recomputes `n`, adds
the title to `standards_spine.json.cases[]`, and adds a new `legacy` entry to
`cases_index.json.cases[]` with `standards_count` set to exactly how many skills were actually
confirmed (never the proposed count — those are different numbers on purpose).

## What this skill refuses to do

- **Never writes to the frozen read-model on `--propose`.** Only `readmodel/reconcile_queue.json`
  changes.
- **Refuses to confirm a title flagged `possible_revision_of`.** Two Phone Plans docs, a Payroll
  2.0, a Navigation duplicate, an "Investment Portfolio" vs. "Which (Investment) Portfolio?" — the
  fuzzy title check catches these and stops rather than guessing whether it's a new case or a
  revision of an existing one. A human resolves it by hand (edit the queue file, or confirm the
  other title instead).
- **Never infers a skill from what a case is "about."** A case about fast food finance is not
  automatically tagged `Percent` just because restaurants have percentages somewhere in their
  business model — it's tagged only if "Percent" (or evidence of the *how-to*) actually appears in
  the document text, with the sentence quoted so a human can check the machine's work in five
  seconds.

## Enforcement

MCS-38 (`DOCTRINE_LEDGER.md`): every confirmed case must trace to a `reconcile_queue.json` record
naming the exact evidence sentence used, or the confirm script refuses to run.
