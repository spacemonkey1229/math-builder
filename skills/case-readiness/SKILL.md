---
name: case-readiness
description: "The publish gate for CASE QUALITY. Run a math case study up a three-tier readiness ladder before it can be published or verified. Use when the user says \"QA the case\", \"run the gate\", \"is this case ready\", \"check the Fermenter case\", \"review the case study against the spec\", \"can we publish this\", \"run the probes\", \"cold-solve this case\", \"is the twist sound\", \"has this been dry-run yet\", or after case-research reports all placeholders closed. TIER 1 is nineteen mechanical structural checks against SPEC.md plus continuity checks that the Guide Notes, the workbook, the published interactive HTML and its math glossary all still agree with case.md. TIER 2 is six simulated-play probes: cold solve, both-sides solve, trap check, twist integrity, assumption sensitivity at plus/minus 50 percent, and data decay on every cited URL. TIER 3 is a human dry-run with real learners, filed as a RUN_REPORT. Emits DRAFT / TIER1_PASS / TIER2_PASS / PUBLISHED / VERIFIED to cases/<id>/QA_REPORT.md. This skill CANNOT publish and CANNOT fix. It only gates. Supersedes case-qa."
---

# case-readiness — the three-tier gate

Stage four. The only skill in the pipeline whose output is a **verdict**. It gates and nothing
else: it does not fix, does not source, does not publish. If it finds problems it names them and
hands the case back.

> House doctrine: *The critique pass is not optional. BLOCKER/GAP/POLISH before any build begins.*
> Here it is before any publish begins. **Every BLOCKER must be resolved. No exceptions.**

**Supersedes `case-qa`.** The legacy skill is preserved at `skills/case-qa/SKILL.superseded.md`
per MCS-22 — nothing is superseded silently. Its inline script had three defects that let real
drift through; they are named and fixed in Tier 1 below, and the fixes are regression-tested.

---

## Why three tiers

The sibling HIGH GRADE murder-mystery kit cleared **all thirteen of its structural checks and all
six of its simulated-play probes** — and then failed in front of a real room. Worse, the
post-mortem could not tell whether the *artifact* or the *facilitation* was at fault, because
nobody had written down what happened when.

That is the whole argument for Tier 3, and it is why Tier 3 cannot be skipped and why
`templates/RUN_REPORT.md` demands facts before impressions and forces a design-vs-delivery
attribution. A machine gate can prove a case is *consistent*. It cannot prove it *works*.

## The ladder

```
DRAFT ──T1──▶ TIER1_PASS ──T2──▶ TIER2_PASS ──human confirm──▶ PUBLISHED ──T3──▶ VERIFIED
                   │                  │                                            │
              0 BLOCKERs        6 probe verdicts                          a filed RUN_REPORT
              (mechanical)      written by name                           from a real cohort
```

| State | Requires | What it licenses |
|---|---|---|
| `DRAFT` | — | nothing |
| `TIER1_PASS` | Tier 1 clean: 0 BLOCKERs | Tier 2 may start |
| `TIER2_PASS` | all six Tier 2 probes recorded, 0 FAIL | `case-publish` may run |
| `PUBLISHED` | Tier 1 + Tier 2 clean **and** two human confirms in `case-publish` | the case may be assigned to learners |
| `VERIFIED` | a filed `cases/<id>/runs/RUN_*.md` with no unresolved artifact-attributed defect | **only now may the case be marked ✅ in `DOCTRINE_LEDGER.md`** |

`PUBLISHED` is deliberately reachable without Tier 3 — you cannot dry-run a case you have not
published. But `VERIFIED` is not, and per the ledger's own rule (*no ✅ without a QA report naming
the case it was verified against*) an unverified case is never doctrine evidence.

Write the state to `case.json.qa.state`.

---

# TIER 1 — STRUCTURAL (machine, blocking)

```bash
cd "$PROJECT"
python3 skills/case-readiness/scripts/tier1_structural.py --case <id>
python3 skills/case-readiness/scripts/tier1_structural.py --case <id> --json /tmp/t1.json
```

Exit 0 = `TIER1_PASS`. Exit 1 = `BLOCKED`. Nineteen checks:

| id | Check | Authority |
|---|---|---|
| T1-01 | seven structural sections present | SPEC §1 |
| T1-02 | Overview length; no load-bearing numerals | SPEC §1.2 |
| T1-03 | Dilemma binary, opens "You are <X>." | SPEC §1.4 |
| T1-04 | Challenges 1/2/4/5 verbatim boilerplate | SPEC §1.5, MCS-04 |
| T1-05 | Challenge numeral-form drift | SPEC §1.5 |
| T1-06 | appendices lettered, ordered, **no orphans** | SPEC §1.6, MCS-08 |
| T1-07 | final-appendix lines are verbatim spine labels | SPEC §1.7, MCS-05 |
| T1-08 | every number cited or declared an assumption; every legacy case claiming "verbatim"/"publicly verifiable" real data has a sources[] entry backing it | SPEC §5, MCS-06 |
| T1-09 | balance test: both arguments written, margin ≤ 20% | SPEC §2, MCS-02 |
| T1-10 | `case.json` schema + standards resolve in the spine | SPEC §4 |
| T1-11 | learning-goal **mutual** reachability | MCS-10 |
| T1-12 | tier vs numeric load | SPEC §3 |
| T1-13 | facilitator guide, anchor ladder, twist, timed plan, sensitivity note | SPEC §6/§7, MCS-14/15/16/19 |
| T1-14 | **CONTINUITY** — `FACILITATOR.md` agrees with `case.md`/`case.json` | MCS-23 |
| T1-15 | **CONTINUITY** — published `.docx`/`.xlsx` agree and are not stale | MCS-23 |
| T1-16 | QA hash currency | MCS-11 |
| T1-17 | cohort-size bands declared | MCS-25 |
| T1-18 | interactive HTML present, fresh, leak-free | MCS-37 |
| T1-19 | hover+hyperlink math glossary, verified domains | MCS-39 |

## The three defects this fixes

A verification pass found three ways the legacy `case-qa` script let real drift through. Each is
fixed and each fix is covered by `scripts/selftest_tier1.py`, which mutates a copy of a real case
in a tempdir and asserts the check fires.

**1 · Challenge numeral form broke the whole diff.** The old regex required `N.)` exactly. A case
written with `1.` or `**1.**` matched nothing, so the boilerplate diff silently examined zero
sections and a *rewritten* Challenge 2 passed clean. This is not hypothetical — it is BLOCKER B3
in the Cold Chain report. Tier 1 now accepts `N.)`, `N.`, `N)`, bold or not, still diffs the text,
and reports the numeral drift **separately as T1-05** so the deviation stays visible instead of
being normalised away. Markdown-bullet rendering of the `a.)`/`b.)` sub-lines is likewise reported
as rendering drift, not silently accepted and not called a rewrite.

**2 · The Appendix-G verbatim check skipped 14 labels.** The old check read only lines starting
`- ` or `* `. Cold Chain's Vocabulary half is a single middot-separated run —
`Volume · Surface Area · Prism · …` — so MCS-05 was only ever enforced on the "How to…" half, and
fourteen labels were never checked against the spine at all. Tier 1 now parses separator runs
(`·`, `•`) as well as bullets. Verified: corrupting one vocabulary label to `Prisms` is caught by
Tier 1 and is **not** caught by the legacy script.

**3 · The orphan-appendix check exempted anything titled "how to".** The old code did
`if re.search('how to', title): continue`, which silently exempted *any* appendix whose title
mentions "how to" — not just the mandatory §1.7 standards appendix. Tier 1 now identifies the
final standards appendix by its full §1.7 title, treats a missing reference to it as a GAP (it is
referenced by Challenge 1 by construction), and runs the full orphan check on everything else.
Verified: an unreferenced `Appendix H: How To Read The Circuit Table` is caught by Tier 1 and is
**not** caught by the legacy script.

## Two more defects found in later use (2026-08-04)

A simulated-classroom QA pass (5 cold-solve runs + a real-world fact-check on each of 4
`TIER1_PASS` legacy conversions) found that Tier 1 clean does not mean the case's real-world
claims are true — Cardiology cited a real clinical trial (real NCT id, real sponsors) with a
fabricated mortality table, and LeBron vs. Michael froze a still-active player's stats at an
undisclosed, incomplete partial season. Both passed all nineteen Tier 1 checks. Two structural
gaps let this through, and both are fixed now:

**4 · T1-08 never required a legacy case's "verbatim"/"publicly verifiable" claim to have
anything backing it.** A case's own `legacy_conversion_note` can say its Appendix A is "used
verbatim" from a real source while `sources[]` sits empty, and the old T1-08 had no rule against
that — it only checked that *explicit* `[S1]`-style citation markers resolve to a `sources[]` row,
which a case with zero markers trivially satisfies. T1-08 now treats an empty/unbacked
`sources[]` on a legacy case making this exact class of claim as a BLOCKER (see
`tier1_structural.py`, T1-08, `REAL_CLAIM_RE`). Verified against the corpus: 0 regressions on the
4 already-`TIER1_PASS` cases, and 5 other still-unconverted legacy cases with the identical
unbacked "verbatim" claim now correctly gain this BLOCKER too — a real, pre-existing risk this
check surfaced, not a false positive.

**5 · `case-publish`'s gate checked `qa.verdict`, which Tier 1 alone already sets to `"PASS"`.**
case-readiness's own ladder always said `TIER2_PASS` — all six probes recorded, 0 FAIL — is
required before publish. Nothing enforced it: `qa.verdict`/`qa.blockers_open` are a convenience
pair set the moment Tier 1 clears, and `case-publish`'s gate checked those, not `qa.state`. All 10
of this project's first-wave legacy conversions reached `published` on `TIER1_PASS` alone, Tier 2
never run. Fixed in `skills/case-publish/SKILL.md`'s gate: it now requires `qa.state == "TIER2_PASS"`
explicitly. This is a hard stop for any future publish, including re-publishing an already-shipped
case, until Tier 2 genuinely runs.

**T1-18 also had a live bug, not a missing check:** the leak-detector that blocks a case from
printing its own `balance_test.margin_pct` as a literal answer used a bare-digit regex, so a small
round margin (e.g. `5.0`) false-positived against CSS pixel values, SVG path coordinates, and
ordinary phrases like "5-year" or "Year 5". Narrowed to exclude `<style>`/`<svg>` blocks and, for
`margin_pct` specifically, require the match to actually be stated as a percent/points figure
nearby — verified the narrower check still catches a genuine literal leak.

## The continuity checks (new)

The analogue of the Murder Mystery continuity bug — where the killer changed at v1.2 and three
documents kept convicting the old suspect — is a case whose numbers change while `FACILITATOR.md`,
the workbook and the published docx quietly keep teaching the old ones.

- **T1-14a keyed cross-check.** Every row of `case.json.derived` must appear, with the same
  values, in the corresponding `FACILITATOR.md` table row. A guide teaching a different SA:V from
  the one in the case of record is a BLOCKER.
- **T1-14b balance continuity.** `balance_test.A_*`, `B_*` and `margin_pct` must appear in
  `FACILITATOR.md`. If the guide's arithmetic and the case's arithmetic have diverged, the guide
  will defend a number that no longer exists.
- **T1-14c orphan-number sweep.** Any number in the Guide Notes with no home in `case.md` or
  `case.json` is a GAP. It is either a guide-only derived figure — fine, but it will drift
  silently, so move it into `case.json.derived` — or it is already stale.
- **T1-15 published-artifact staleness.** Each artifact is paired with the source it is generated
  from (`Guide Notes*` ← `FACILITATOR.md`, everything else ← `case.md`) and flagged BLOCKER if it
  was built more than 120 s before its source's last edit. Plus a number sweep of every `.xlsx`
  cell and `.docx` paragraph against the same universe.
- **T1-16** re-checks the MCS-11 hash: a stale hash means every other finding may describe a
  different file, so it is reported first.

## Two behaviours that are intentional

- **Overview numerals** are BLOCKER-for-confirmation per SPEC §1.2. Clock times (`4:40`) and
  4-digit years are auto-classified as texture and downgraded to POLISH. Anything else must be
  read by a human and the clearance **recorded** in `case.json.overview_numerals_cleared[]` as
  `{"numeral": "...", "why": "..."}`. A clearance that is not written down is not a clearance.
- **Option-named-in-Background** is a fuzzy word match and will occasionally misfire. Read the
  Background and clear it or keep it deliberately.

## Regression test

```bash
python3 skills/case-readiness/scripts/selftest_tier1.py --project "$PROJECT"
```

Copies a real case into a tempdir, applies three mutations, and asserts Tier 1 catches each.
Run this after any edit to `tier1_structural.py`. **A gate with no test is a gate you trust for
no reason.**

---

# TIER 2 — SIMULATED PLAY (machine + model, blocking)

```bash
python3 skills/case-readiness/scripts/tier2_probes.py --case <id>
python3 skills/case-readiness/scripts/tier2_probes.py --case <id> --probe 5 --flex 0.5
```

Six probes, modelled on the HIGH GRADE kit's six simulated-play probes. The script runs the
mechanical half of each, builds the packets and prompts, and **prints what a model or a subagent
must do**. A probe with no recorded verdict is `NOT RUN`, which is a real state and not a pass.

### P1 · Cold solve

The script writes the student-facing packet to `/tmp/coldsolve-<id>/PACKET.md` and proves it is
leak-free (no balance result pre-computed in `case.md`; no six-word shingle of the twist; no
`FACILITATOR.md` heading). Then:

> **Dispatch a genuinely fresh subagent.** Not this conversation, not a subagent you have briefed.
> Give it the packet path, the seven questions the script prints, and an explicit instruction not
> to open `FACILITATOR.md`, `QA_REPORT.md` or `case.json`.

**Pass criterion: the solver reaches a defensible position, with correct arithmetic, and can name
the metric it optimised. Reaching the intended answer by the wrong route is a FAIL.** That is the
Cold Solve packet's whole point in the sibling project: can fresh readers convict the right person
*for the right reasons*, and get past the planted trap.

### P2 · Both-sides solve

Build the strongest quantitative case for *each* option, independently, from the packet alone.
Machine pre-screen: an argument with almost no numbers, or one that reads as a concession
(`"B is cheaper but worse in every other way"`), fails before a model sees it. Then a model
answers: which side collapses first, and at exactly which question?

**If one side collapses, the recorded margin is a paper number and the SPEC §2 balance test has
not really been passed** — regardless of what `margin_pct` says.

### P3 · Trap check

Does the case contain a plausible wrong path, and does the guide *name* it? The machine screen
checks that `FACILITATOR.md` names a trap and that the trap describes what a learner will actually
*do* wrong rather than merely noting a hard bit. Then a model names the trap from the packet
alone, before reading the guide, and compares.

**A trap the guide has not anticipated is a FAIL even if the case is sound**, because the guide
will not be watching for it.

### P4 · Twist integrity

Two questions, and the second is the one that gets skipped:

1. Does the twist invalidate at least one position a real room would hold?
2. **Does the twist survive the case's own stated assumptions, read the most natural way a
   *student* would read them — not the way the author intended?**

Cold Chain's twist originally failed (2): under a sequential reading of Assumption 1 it did
nothing at all, and the case shipped that way until an adversarial pass caught it. Re-derive the
effect under every defensible reading of every stated assumption **and under the case's own stated
capacity limits**. If the effect depends on a convention the case never states, that is a BLOCKER.

When the case ships a sensitivity model with `evaluate_twist()`, the script recomputes base vs.
twist mechanically and fails the probe if the winner and the margin are both unmoved.

### P5 · Assumption sensitivity — fully machine

Flex each stated assumption ±50% and report which flips the verdict.

Requires `cases/<id>/sensitivity_model.py`. The contract is two public names:

```python
PARAMS   = {...}                       # every dial the case STATES
FLEX     = ["...", "..."]              # the subset that is an ASSUMPTION (optional but expected)
def evaluate(params) -> {"A": metric, "B": metric}     # higher is better
def evaluate_twist(params) -> {...}                    # optional
```

`skills/case-readiness/scripts/example_sensitivity_model.py` is the worked reference (Cold Chain),
kept inside the skill so it can be executed and diffed without touching a published case.

Two rules that keep this honest:

- **Only `FLEX[]` is swept by default.** SPEC §2 asks for sensitivity to *stated assumptions*, not
  to cited measurements. Halving a WHO-rated cold life is a different case, not a sensitivity
  test. Cited data is stress-tested by P6 instead. `--flex-all` overrides, and the report says so.
- **No model ⇒ `NOT RUN`, not a pass.** Absent data is a first-class state (house doctrine); a
  probe that could not run is never reported as a probe that passed.

**A case whose answer is unstable under a ±50% assumption swing is not forbidden — but it must say
so**, in `balance_test` and in the Guide Notes, or the guide will defend a margin that does not
exist. A flex that pushes the margin past the SPEC §2 20% cap is the same finding in the other
direction.

### P6 · Data decay

The QA sandbox has no outbound network, so the script emits the fetch worklist (every
`sources[].url`, its `accessed` age, its confidence grade) and the probe is **delegated** to a
subagent with web access. For each URL report: reachable / moved / dead; whether the recorded
`value` still appears; and the new URL if it moved.

A URL that 404s while its figure is load-bearing is a BLOCKER. **A URL that resolves but no longer
carries the figure is worse**, because nothing else in the pipeline would ever notice. Sources
older than 365 days are flagged automatically. Per MCS-21, report NOT FOUND rather than guessing —
a fabricated URL is the worst failure available.

---

# TIER 3 — HUMAN DRY-RUN (blocking for VERIFIED, not for PUBLISHED)

A guide runs the case with real learners, once, and files
`templates/RUN_REPORT.md` → `cases/<id>/runs/RUN_<date>_<guide>.md`.

The form is in the Beta Host Report's voice and its order is load-bearing:

- **Sections 1–6 are facts.** Cohort size and the band used; the *actual* clock time of every
  anchor and of the twist; who voted what at Anchor 1 and at the close; who moved; which anchors
  were reached; where the room stalled and for how long; an A/T/I engagement mark per learner per
  act.
- **Sections 7–9 are impressions**, and they come after.

The pivotal question in section 2 is whether the numbers reached the room before Anchors 2 and 3
were done — the equivalent of the beta report's early-leak question, and the same logic: *an early
leak explains more about a disappointing night than any opinion about the plot.*

**Section 8 is the design-vs-delivery attribution.** Every defect gets checked as *the case was
weak here* (artifact) or *I lost the room here* (delivery) or *can't tell* — and "can't tell" asks
what you would need to observe to decide. This section exists because the sibling project's
post-mortem could not make that separation and therefore could not fix anything.

Findings attributed to the **artifact** re-open the gate at Tier 1 or Tier 2. Findings attributed
to **delivery** go to guide coaching and do **not** block the case. Two artifact-attributed
findings across two independent runs means the case goes back to `case-write`, not to the guide.

**Cohort bands (MCS-25).** `case.json.cohort_bands[]` declares the discussion sizes the case is
tuned for and what changes at each — the analogue of the HIGH GRADE kit scaling 19–23 / 16–18 /
12–15 players. The RUN_REPORT records which band was actually used, so a case that works at 10 and
dies at 22 becomes visible instead of becoming a guide's private impression.

---

## Write the report

Append to `cases/<id>/QA_REPORT.md` (append — do not overwrite an earlier run; the history is the
evidence):

```markdown
## case-readiness run — <date>
**State:** DRAFT → TIER1_PASS → ...   **Verdict:** <state reached>

### Tier 1 — structural (17 checks)
| id | result | note |
...
BLOCKER / GAP / POLISH lists, verbatim from the script.

### Tier 2 — simulated play (6 probes)
| probe | verdict | finding |
| P1 cold solve | PASS/FAIL | did the fresh solver reach a defensible position for the right reasons? |
| P2 both-sides | PASS/FAIL | which side collapses, at which question |
| P3 trap | PASS/FAIL | the trap the case contains vs. the trap the guide names |
| P4 twist | PASS/FAIL | does it survive the case's own assumptions |
| P5 sensitivity | PASS/FAIL/NOT RUN | which dial flips the verdict |
| P6 data decay | PASS/FAIL | dead links, drifted figures, refresh dates |

### Tier 3 — human dry-run
NOT RUN / filed at cases/<id>/runs/RUN_<date>.md / <n> artifact-attributed findings
```

Then set `case.json.qa`:
`{"state": "...", "verdict": "...", "run_on": "...", "blockers_open": n, "gaps_open": n,
"tier2": {"P1": "...", ..., "P6": "..."}, "tier3_runs": [...], "case_md_sha256": "..."}`
and `status: "qa"`. **Nothing else in `case.json` may be modified by this skill.**

## Report back

The state reached, the BLOCKER list verbatim, the six probe verdicts by name, the report path, and
the next step: `Fix the N blockers and re-run` / `Run case-publish on <id>` / `Schedule the Tier 3
dry-run`.

## Never

- **Never fix the case.** QA that edits its own subject cannot be trusted. Name the defect and the
  exact fix; let `case-write` or `case-research` apply it.
- Never publish, never touch `readmodel/`, never write `cases_index.json`.
- Never downgrade a BLOCKER to a GAP to get a case out the door. The margin cap, the verbatim
  boilerplate, the fabricated-number rule and the empty-`new_coverage` rule are absolute.
- Never mark `TIER2_PASS` with a probe recorded as `NOT RUN`. Six probes, six verdicts, by name.
- Never mark a case ✅ in the doctrine ledger without a filed RUN_REPORT. `PUBLISHED` is not
  `VERIFIED`, and the ledger has been wrong about exactly this before.
- Never accept "the number is plausible". SPEC §5: QA rejects plausible.
