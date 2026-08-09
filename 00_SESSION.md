# Session Instructions — Math Builder

**Independent project as of 2026-08-01.** This project was scoped, built, and initially governed
under `Best Practices` doctrine, then formally graduated to sit on its own — its own Claude/Cowork
project, its own instructions block, no longer counted against `Best Practices/PORTFOLIO_WIP.md`'s
ACTIVE-project cap. The block below is this project's complete, self-contained instructions —
paste it into a new Claude/Cowork project pointed at this folder. Nothing here defers to another
project's doctrine; every hard line below is this project's own, even where its origin (an "MCS-*"
id) traces back to lessons learned while it was still under Best Practices.

## Paste-ready block

```
Project: Math Builder · State: ACTIVE · Phase: 2 (Build)
Prime directive: Build and mechanically gate quantitative case studies for middle/high school
math — never fabricating a number, a URL, or a verdict — until at least one case reaches
VERIFIED with a real cohort.

Read first, in order:
1. README.md (what this is, folder map, how to open the dashboard)
2. SPEC.md (the contract — what a case study IS, the balance test, the hard lines)
3. DOCTRINE_LEDGER.md (every rule's lifecycle PROPOSED->CODIFIED->WIRED->VERIFIED; read the
   "Verification status" and "Change log" sections for current state, not just the table)
4. ROADMAP.md (current track priorities and the one blocking fact at the top)

Hard lines (this project's own, verbatim from SPEC.md §5 and DOCTRINE_LEDGER.md):
- Never fabricate a number. Every figure is either cited to a real source, or explicitly
  labeled a stated scenario assumption. There is no third category. Absent data is a
  first-class state, never quietly invented.
- No URL from memory (MCS-21). A fabricated URL is the worst failure available -- every
  external link must be actually fetched and confirmed before shipping.
- Machine drafts, human promotes (MCS-12). Nothing enters standards_spine.json,
  cases_index.json, submissions.json, or score_overrides.json without an explicit confirm
  step; snapshot to readmodel/_snapshots/ before every write to a frozen file (MCS-22).
- PUBLISHED is not VERIFIED (MCS-29). A case may only be marked VERIFIED -- and only then may
  it carry a checkmark in DOCTRINE_LEDGER.md -- with a filed, filled RUN_REPORT from a real
  cohort. No case in this system has reached VERIFIED yet.
- New rules go through a DOCTRINE_LEDGER row + critique pass (BLOCKER/GAP/POLISH) before being
  written in; name the mechanical enforcement point (a Tier 1 check id, a script) or the rule
  stays UNWIRED, which does not count as doctrine.

Session end: state what changed, what is staged (queue files, INTERIM scores), and what still
needs a human sign-off (a --confirm run, a guide's dry-run, a fetch this sandbox can't make).
```

## How to finish the graduation on your end

I can't create a Claude/Cowork project myself — that's a UI action. To complete it:
1. Create a new Project in Claude/Cowork.
2. Point it at this folder (`Math Builder`).
3. Paste the fenced block above into that project's instructions.
4. Future sessions in that project read only this project's own doctrine — they won't inherit
   `Best Practices`' reading list or hard lines unless this file says to.

## Phase note

Framework phases run 0-4 (a vocabulary this project keeps because it's useful, not because
`Best Practices` still governs). This project has shipped well past a Phase 1 PDR — a working
pipeline, a published case, a full dashboard app, and two tested QA modules — but has not cleared
the Phase 2->3 gate ("does the core loop work for a real user?") because no case has run with a
real cohort yet (Tier 3, `tier3_verify.py`). Phase is recorded as `2` for that reason, not `3`.

## Graduation note (superseded — kept for history)

Before 2026-08-01, this file flagged a real conflict: `Best Practices/PORTFOLIO_WIP.md` caps
ACTIVE projects at 3, and declaring this project ACTIVE would push an already-over-cap portfolio
further over. A survey at graduation time found the portfolio was carrying at least 8
already-declared-ACTIVE projects against that 3-cap, workspace-wide — a real, pre-existing
condition, not something this project caused. Graduating this project out from under
`Best Practices` governance resolves the conflict **for this project specifically**: it no longer
counts against that cap. It does not fix the portfolio's broader overage, which is a
`Best Practices`-side triage this file is not the place to resolve.
