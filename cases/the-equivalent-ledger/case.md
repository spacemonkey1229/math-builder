Case Study: The Equivalent Ledger
MS | Math | Case Study | 2026 | Adventure

## Overview

The overnight reconciliation run finished four minutes ago, and Priya Chandran is still staring at the diff (a side-by-side comparison showing exactly which lines of code changed between the old version and the new one). Two windows sit open side by side on her monitor: the pull request (a formal request to merge a proposed code change into the shared codebase, so other engineers can review it before it ships) an AI coding assistant opened last week, rewriting the ugly, decade-old formula that decides how many dollars get swept between two suspense accounts every time the ledger closes with unmatched line items — and the on-call engineer's (the engineer designated to be reachable and respond if something breaks during this shift) message from six minutes ago: "ran it against the last two real batches we had sitting around, numbers match exactly both times. approving now so we make the freeze window." Down the hall, the deployment freeze for quarter-end regulatory close starts before sunrise. If the rewritten formula isn't approved before then, it waits out the freeze, and Priya's team keeps hand-patching the old code's known quirks in the meantime. She has read the AI's rewrite twice. It is shorter, cleaner, and it produced the same number as the old formula on both of the two batches anyone actually tried it against. She has also spent eleven years around systems where "it matched on the data we happened to have" and "it is actually the same formula" turned out, more than once, to be two very different sentences. Her cursor sits over the Approve button. Behind her, the on-call engineer is already drafting the deployment ticket (the formal record, in the company's change-tracking system, that documents and authorizes this release into production).

## Background

Priya Chandran is the verification lead for the reconciliation engine at Ledgerline, a company that operates the overnight settlement ledger connecting a network of regional banks. Every night, Ledgerline's system tallies which transactions matched cleanly between partner banks and which did not; for every batch of unmatched line items, a dollar amount gets swept between two internal suspense accounts to keep both banks' books balanced until the mismatch is resolved by hand. That sweep amount has been computed, since before Priya joined the team, by a formula nobody fully trusts anymore — hand-derived years ago by an engineer who has since left, buried in code nobody wants to touch (SEE APPENDIX A).

Last week, as part of a broader effort to modernize that legacy module, an AI coding assistant proposed a rewritten version of the sweep formula. This kind of AI-assisted rewrite of deterministic financial code is a live, widely discussed tension in enterprise engineering right now — a system of record has to reconcile exactly, every time, while the tools being used to modernize it are built to be merely probably right (SEE APPENDIX A). The on-call engineer ran the rewritten formula against the two most recent real unmatched-item batches Ledgerline's own logs had on hand, and it produced the exact same dollar sweep as the original formula on both (SEE APPENDIX B).

Priya's team has narrowed the decision to two named paths. **The Regression Pass** means approving the rewritten formula for production now, on the strength of that two-batch match — fast, and it clears before the deployment freeze locks all changes out of the reconciliation engine ahead of quarter-end regulatory close (SEE APPENDIX C). **The Full Factor** means holding the deployment and spending the day having senior engineers fully factor both formulas by hand, to prove algebraically that they produce an identical dollar sweep for every possible batch size — not only the two batch sizes that happened to already get tested (SEE APPENDIX C).

The reconciliation engine is a system of record: every dollar it sweeps has to reconcile exactly, for every partner bank, every night, indefinitely — not only for the two nights someone happened to check. If the rewritten formula is wrong for batch sizes Ledgerline has not yet seen in production, it will not announce itself; it will simply mis-sweep dollars between suspense accounts, silently, until an auditor or a partner bank eventually notices the books don't balance (SEE APPENDIX D). The vocabulary and "how to…" procedures this case will ask you to research are listed in (SEE APPENDIX F); every priced, sourced, or stated figure is documented in (SEE APPENDIX E).

## Dilemma

You are Priya Chandran.
Do you:
A.) Approve The Regression Pass — ship the AI-rewritten formula now, because it produced identical results on both of the real batches QA (short for Quality Assurance — the practice of testing a product before it ships to catch defects before customers do) tested it against, clearing the deployment freeze OR
B.) Hold for The Full Factor — spend the day fully factoring both formulas by hand to prove they are the same expression for every batch size, not only the two already tested

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A complete factorization of the original formula, O(n), from Appendix A: find the
    greatest common factor of its coefficients using prime factorization — show a factor tree or
    repeated division for each coefficient, label every prime factor you find, and note any place
    an intermediate number turns out to be composite and needs further breaking down — then write
    O(n) as (greatest common factor) × (remaining expression).
    D2. The same complete factorization for the AI-rewritten formula, R(n), from Appendix A:
    find the greatest common factor of ITS coefficients using prime factorization, following the
    same process as D1, and write R(n) in fully factored form.
    D3. A sample-test table: evaluate O(n) and R(n) at all three batch sizes in Appendix B —
    the two batches QA already tested, and the one representative larger batch QA has not tested
    — showing every calculation, and state whether the two formulas still agree at each batch
    size, in dollars and as a percent.
    D4. A written proof verdict: using ONLY the fully factored forms from D1 and D2 (not D3's
    plugged-in numbers), determine whether O(n) and R(n) are the same expression for every
    possible batch size, or only coincidentally equal at the two batch sizes QA happened to test.
    Name the specific structural feature the factored form reveals — visible in the factored
    forms but invisible in D3's matching outputs — that answers the question.
    D5. A cost comparison table: using Appendix C's verification-labor figures and Appendix D's
    risk-exposure figures, calculate in dollars the cost of Option A (the expected cost of
    approving now, given the stated risk of an undetected error) versus Option B (the cost of
    paying for a full factoring verification today), and state which option is cheaper on paper,
    in dollars and as a percent.
    D6. A one-paragraph recommendation memo to Priya's engineering director: using BOTH D4's
    proof result and D5's cost comparison, state which option you recommend and defend it —
    including whether D4's result changes how much you trust the risk figure used in D5.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — The Two Formulas

The legacy formula in production, and the AI-rewritten formula proposed as its replacement, both computing the dollar sweep between suspense accounts for a batch of *n* unmatched line items. Referenced from Background and Dilemma; forces Challenge 3 (D1, D2, D3, D4).

| | Formula |
|---|---|
| Original formula, O(n) — in production today, no constant term | O(n) = 48n² + 180n (MA1) |
| AI-rewritten formula, R(n) — proposed replacement | R(n) = 54n² + 96n + 240 (MA2) |

## Appendix B — QA's Regression Sample

The batch sizes QA actually tested the rewritten formula against, plus one representative larger batch size drawn from a typical production night that QA has not yet tested. Referenced from Background; forces Challenge 3 (D3, D4).

| | Batch size, n (unmatched line items) |
|---|---|
| Most recent real batch QA tested | n = 4 (MA3) |
| Second real batch QA tested | n = 10 (MA3) |
| A representative larger batch from a typical production night, not yet tested by QA | n = 25 (MA4) |

## Appendix C — Verification Cost and the Deployment Calendar

What it would cost, in engineer-hours, to fully verify the rewritten formula today, and the deployment-freeze clock Priya is deciding against. Referenced from Background and Dilemma; forces Challenge 3 (D5).

| | Value |
|---|---|
| Hours from now until the deployment freeze begins | 6 hours (MA5) |
| How long the reconciliation engine stays locked from changes if the freeze window is missed | 6 weeks (MA6) |
| Senior engineers assigned to a full factoring verification | 2 (MA7) |
| Hours required per engineer for a full factoring verification | 8 (MA7) |
| Fully-loaded hourly cost of a senior verification/QA engineer | $48.94/hour [S1] |

## Appendix D — Risk Exposure If Deployed Unverified

The stated risk figures behind Option A's "expected cost" if the rewritten formula ships without a full proof. Referenced from Background; forces Challenge 3 (D5, D6).

| | Value |
|---|---|
| Estimated probability that an AI-rewritten code change which has already passed a small sample of regression tests still contains an undetected functional defect | 3.4% (MA8) |
| Estimated cost if an undetected reconciliation-sweep error reaches production and is later discovered (investigation across affected batches, manual correction, compliance/audit escalation) | $25,000 (MA9) |

## Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author/researcher, because a genuine multi-tier search found no public source publishing them
> for a private company's specific internal reconciliation formula or risk profile. A Hero may
> challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Original formula, O(n) | 48n² + 180n | A constructed, illustrative example of a two-term polynomial reconciliation-sweep formula. No real company's actual proprietary formula is used or implied; this is a disclosed stand-in built specifically so that its coefficients' greatest common factor (12) can be found by prime factorization. | The specific coefficients set which batch sizes coincidentally match R(n) (see MA2) and where the two formulas diverge — a Hero could construct a different pair of formulas and reach a different D3/D4 result, but the case's point (sample-testing is not proof) does not depend on these exact numbers. |
| MA2 | AI-rewritten formula, R(n) | 54n² + 96n + 240 | A constructed, illustrative example, chosen to model a realistic failure mode where an AI-rewritten formula matches the only data anyone has tested it against. No real company's actual formula is used or implied. | This is the case's central, deliberately-placed structural fact, not a flexed sensitivity dial — D1/D2/D4's factoring work is how you find out what it actually is; it is not swept in `sensitivity_model.py`. |
| MA3 | The two historical batch sizes QA tested | n = 4 and n = 10 | Protagonist-specific: whichever real unmatched-item batches Ledgerline's own logs happened to have on hand are not a publishable industry statistic. | Fixed by the case's construction (MA1/MA2 are built to agree exactly at these two values) — not an independent sensitivity lever. |
| MA4 | A representative larger, untested batch size | n = 25 | Protagonist-specific: a typical larger production night's batch size for this fictional company, not a publishable statistic. | The answer is sensitive to this value — a Hero arguing production batches are always small (near the two already-tested sizes) would weaken the case for The Full Factor. |
| MA5 | Hours until the deployment freeze begins | 6 hours | Matches the Overview's "before sunrise" narrative detail — not an independent estimate. | None — fixed by the narrative, not a sensitivity lever. |
| MA6 | Deployment freeze duration if missed | 6 weeks | Protagonist-specific banking practice: quarter-end regulatory close commonly triggers a change freeze on core financial-infrastructure systems industry-wide (see Appendix E supplemental source), but no public source publishes an exact freeze length for a specific company. Six weeks is a stated, disclosed scenario value in the middle of common industry practice. | Affects only the narrative stakes of missing the window, not the D5 cost comparison or D4's proof. |
| MA7 | Verification staffing and hours | 2 engineers x 8 hours each | Protagonist-specific: how many engineers and how much time Ledgerline would actually assign to this verification is an internal staffing decision, not a publishable fact. | Sets Option B's labor cost (D5) directly. The answer is sensitive to this value — a Hero arguing the verification would take meaningfully longer changes how close D5's two costs come out (see `case.json.sensitivity_disclosure`). |
| MA8 | Probability an AI-rewritten change that already passed limited testing still has an undetected defect | 3.4% | No public source publishes a defect-probability specific to a formula that has already passed two real-batch regression tests. Grounded in real, general evidence that AI-generated/AI-rewritten code carries materially elevated defect rates even after passing tests (CodeRabbit's "State of AI vs Human Code Generation" report, analyzing 470 real pull requests, found AI-authored changes carry 1.4-1.7x more critical/major defects than human-written code, with logic/correctness issues 75% more common — [S2]); 3.4% is chosen as a modest, non-zero residual-risk figure for a change that has already cleared some testing, not as a direct read-off of [S2]'s aggregate PR-level statistic. | The answer is sensitive to this value — a Hero arguing the real risk is lower or higher changes D5's comparison (see `case.json.sensitivity_disclosure`). |
| MA9 | Cost if an undetected reconciliation-sweep error reaches production | $25,000 | No public source publishes a cost specific to a systemic formula-level reconciliation error at a private financial-infrastructure company. General industry commentary on reconciliation-exception handling documents *routine* per-exception investigation costs around $9-$22 (a matched-item exception a human resolves in minutes); a *systemic*, formula-level error that recurs every affected night and requires investigation across multiple batches plus a compliance/audit escalation once discovered post-close is categorically more severe than a routine exception, so $25,000 is set well above that routine per-exception range as a disclosed scenario value, not derived arithmetically from it. | This is the case's single most load-bearing assumption in D5 — the answer is sensitive to this value, and a Hero who challenges it is making a legitimate move (see `case.json.sensitivity_disclosure`). |

**What "Sensitivity" means:** this column describes how much the final recommendation would change if this particular assumption's value turned out to be wrong — not whether the assumption itself is likely right or wrong. An assumption marked "the answer is sensitive to this value" is one where a meaningfully different number, plugged into the same math, would flip which option comes out cheaper; an assumption marked "not a sensitivity lever" is one where changing it would not change which option wins, even though the number itself is still an estimate.

## Appendix E — Sources

All sourced (non-assumption) figures in this case are cited here (SEE APPENDIX E).

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Median wage, Software Quality Assurance Analysts and Testers (SOC 15-1253) | $48.94/hour ($101,800/year) | U.S. Bureau of Labor Statistics — [Occupational Employment and Wage Statistics: Software Quality Assurance Analysts and Testers](https://www.bls.gov/oes/2023/may/oes151253.htm) | May 2023 | HIGH |
| S2 | AI-generated code carries materially more defects than human-written code, even after passing tests | 1.4-1.7x more critical/major defects; logic/correctness issues 75% more common | CodeRabbit — [State of AI vs Human Code Generation Report](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report) (analysis of 470 real-world open-source pull requests) | Published 2025-12-17 | MEDIUM |
| S3 | Enterprise/financial-system modernization requires deterministic verification; AI-assisted rewrites of legacy deterministic code are a live 2026 industry tension | qualitative, supplemental — establishes the narrative's real-world grounding, not a numeric figure | Allytics Tech Perspectives — [The End of the Legacy Rewrite Trap](https://allyticstechperspectives.com/the-end-of-the-legacy-rewrite-trap/) | Published 2026-07-02 | MEDIUM |

**What "Confidence" means:** a HIGH confidence figure comes from a primary, authoritative source measuring exactly the thing claimed (e.g. a government statistics agency reporting its own survey). A MEDIUM confidence figure is real and dated but comes from a less independent source (e.g. a company's own research report) or is a close-but-not-exact match to the claim. Neither rating says how big or small the number is — only how much to trust where it came from.

Notes:
- **S1 note:** the most specific, dated primary-government figure available for this exact occupation code (SOC 15-1253); a broader combined "Software Developers, Quality Assurance Analysts, and Testers" category on BLS's Occupational Outlook Handbook page reports a newer $104,300/year (May 2025) figure, corroborating the same general pay range, but is not broken out to the QA-specific code — S1 is used because it is the closer occupational match despite being from an earlier data year.
- **S2 note:** a software-tooling vendor's own primary research report (not independent academic peer review), but dated, methodologically disclosed (470 real pull requests), and specific — graded MEDIUM. Used only to ground the *qualitative existence and rough scale* of AI-code-defect risk (MA8); the exact 3.4% probability applied to this case's already-tested formula is a disclosed scenario assumption, not read directly from S2's PR-level aggregate statistic.
- **S3 note:** an industry analyst/trade blog, not primary data — used only as supplemental grounding that "AI rewriting legacy deterministic financial code" is a real, current (2026) conversation in enterprise engineering, per this case's sourcing brief. Carries no numeric figure used in any calculation.
- **Supplemental, not independently cited:** general commentary on reconciliation-exception handling costs (routine per-exception costs in the $9-$22 range) informed MA9's basis column but is not itself a load-bearing citation, since no source publishes a figure for the specific, more severe systemic-error scenario this case models — see `RESEARCH_LOG.md` P12 for the full search record.

## Appendix F — "How To…" Math Questions To Research

**Vocabulary terms**

- Factor
- Greatest Common Factor
- Prime
- Composite

**"How to…" questions**

- How to factor a number
- How to find the greatest common factor of a set of numbers
- How to find the percent of a number

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
