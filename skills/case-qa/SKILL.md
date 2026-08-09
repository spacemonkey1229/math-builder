---
name: case-qa
description: "SUPERSEDED — do not invoke. The case-quality publish gate is now skills/case-readiness/, which adds Tier 2 simulated-play probes and a Tier 3 human dry-run on top of the structural checks that used to live here. If a request would have reached case-qa (\"QA the case\", \"run the gate\", \"is this case ready\", \"can we publish this\"), use case-readiness instead. This file exists only so the supersession is visible; the original text is preserved verbatim at skills/case-qa/SKILL.superseded.md."
---

# case-qa — SUPERSEDED by `case-readiness`

**Do not run this skill.** It has no procedure. Use **`skills/case-readiness/`**.

Per MCS-22, *nothing is superseded silently.* The original skill is preserved verbatim at
`skills/case-qa/SKILL.superseded.md` rather than deleted, because the reasons it was replaced are
worth reading: its inline script had three defects that let real drift through, and a future
author who finds only the replacement will not know what to avoid.

## What changed

| | `case-qa` (superseded) | `case-readiness` |
|---|---|---|
| Structural checks | 12, inline in the SKILL.md | 17, in a versioned script with a regression test |
| Continuity | none | Guide Notes, workbook and published packet cross-checked against `case.md` |
| Simulated play | none | six probes: cold solve · both-sides · trap · twist integrity · assumption sensitivity · data decay |
| Human dry-run | none | Tier 3 `RUN_REPORT` with design-vs-delivery attribution |
| States | `PASS` / `BLOCKED` | `DRAFT → TIER1_PASS → TIER2_PASS → PUBLISHED → VERIFIED` |

## The three defects, named

1. **Challenge numeral form broke the whole diff.** The regex required `N.)` exactly, so a case
   written `**1.**` matched nothing and a *rewritten* Challenge 2 passed clean.
2. **The Appendix-G verbatim check skipped 14 labels.** It read only `- ` bullets, so the
   middot-separated Vocabulary run was never checked against the spine at all.
3. **The orphan-appendix check exempted anything titled "how to".** `if 'how to' in title: continue`
   silently exempted any appendix mentioning "how to", not just the mandatory §1.7 one.

All three are fixed in `case-readiness` Tier 1 and covered by
`skills/case-readiness/scripts/selftest_tier1.py`, which mutates a copy of a real case and asserts
each check fires. The superseded script fails all three mutations; the replacement catches all three.
