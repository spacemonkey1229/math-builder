# Guide Notes: Payroll

**Case:** Payroll · **Tier:** T2 · **Band:** MS-core · **Studio:** Heroes Academy
**Standards:** see `case.json.standards[]` for the exact ids (13 skills — percent, currency,
rounding, multi-digit addition/subtraction, bar graph, pie chart, comparison)

Legacy conversion, 2026-08-13, built from the original case study docx
(`source/Y1/Session 2/Payroll/Case Study_ Payroll.docx`) and its companion Guide Notes and
financial workbook (`Grampoline Annual Financial Report.xlsx`) onto the current 11-anchor ladder.
Grampoline LLC is a fictional small business invented by the original case materials — its
financial figures are the case's own stated dataset, not a real company's real numbers, so they
carry forward from the source workbook verbatim rather than being verified against an external
source (see `case.json.legacy_conversion_note`).

## Intro

Frame the format: this is not a "which number is bigger" problem. Both options, done correctly,
close the exact same $20,000 hole in Grampoline's budget. The room's real job is to decide who
should bear that $20,000, not to find the option that saves more of it — because neither does.

## Launch

Read Appendix A's five employee bios aloud, cold, before any dollar figures. Ask: "If you had to
guess, before you've seen a single number — who feels like the person Francesca lets go?" Do not
confirm or correct answers. Note who the room gravitates toward; it will matter at the Twist.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who stands with Operation Clean Break? Who stands with Operation Shared Weight?" Show of hands,
no discussion. Record the count — Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do we mean by 'closing the gap'?"**

Push on what "best" means for a founder who is also a person with a payroll to make, not a
spreadsheet to balance: dollars saved, whose life is most disrupted, and what happens to team
morale and customer relationships going forward are all real considerations — not just the $20,000
line item. Let it feel unresolved for a minute; that discomfort is doing real work.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has picked its deciding factor(s), ask them to name the actual steps: read
Appendix C's remaining-pay figures, decide who (Option A) or what percent (Option B), then check
the resulting dollar amount against the $20,000 target. Re-ask: "Is that still the right process
for the factor we picked?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the two real conventions this case states: (1) Francesca's own remaining pay is excluded
from the $20,000 target and from Option B's percentage base, because she has already gone without
pay and isn't one of "the five employees" the Dilemma is about; (2) the 2019 H1 actuals and H2
projections in Appendix B/C are Grampoline's own fictional dataset, not sourced externally. Ask
which one the room would push back on if they could ask Francesca a follow-up question.

## Data Deep Dive

Now, and only now, the numbers. Walk D1 (bar graph) and D2 (pie chart) together as a room, then
cold-call for D3 vs. D4's arithmetic specifically — this is where a Hero who computes Option B's
percent on the *wrong base* (all six people including Francesca, or just one employee's pay
instead of the $111,500 pool) will get a visibly wrong percent that doesn't actually close $20,000
when checked.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Francesca's phone rings. It's Grampoline's largest customer — a regional chain of senior-living
communities. 'I have to tell you,' they say, 'Irene's latest posts drove a wave of new signups at
our newest location. Honestly, she's a big part of why we keep coming back to Grampoline instead of
the bigger guys.'"

**Facilitator-only.** This is a disclosed scenario assumption for the Twist, not a real, sourced
figure (see `case.json.modeling_assumptions`): assume this customer's account is 15% of
Grampoline's 2019 H1 revenue — $127,000 × 15% = **$19,050** — and that losing Irene puts that
account at real risk of leaving within the following year.

If any Hero picked Operation Clean Break *specifically by letting Irene go*, ask them to recompute
live: the $20,000 saved in payroll is nearly wiped out by $19,050 of revenue put at risk — a real
net first-year benefit of only **$950** (95.25% of the "savings" disappears once the customer
relationship is priced in). This does not make Clean Break wrong — Tiago's remaining pay also
closes the $20,000 gap exactly, and nothing about Tiago's situation is touched by this twist — and
it does not make Shared Weight automatically right either; it still cuts five real paychecks.
It invalidates exactly one popular reasoning path ("let go of the newest hire") without resolving
the case for anyone.

**Soundness check (required before running this case live):** verified this twist holds under
both a sequential reading (state MA1, then MA2, then the twist's $19,050 figure, one at a time —
none contradicts an earlier one) and a simultaneous reading (apply all three at once: Francesca's
own pay is still excluded from both the $20,000 target and the 17.94% base; the H1/H2 figures are
still Grampoline's own stated dataset; the $19,050 at-risk figure is a separate, clearly-scoped
number that only ever modifies the Clean-Break-via-Irene branch and touches nothing else in the
case). No combination of the three produces a contradiction or a double-counted dollar.

## Immediate recommit

Re-vote immediately. Ask by name: "Did this change your position — or does it just mean if you
pick Clean Break, you pick Tiago instead of Irene?"

## Deep conflict — three threads (20–30 min)

1. **Concentrated vs. distributed pain.** Both options remove exactly $20,000 (`margin_pct = 0.0`
   — this is not a case where one option is secretly cheaper). Is it more defensible to put 100%
   of a $20,000 hit on one household, or 17.94% of a smaller hit on five households?
2. **Who gets picked, and on what basis.** If the room leans Clean Break, push on *why* that
   person and not another — tenure, family circumstance, sales performance, or the twist's
   customer-relationship risk are all real, disclosed factors in Appendix A, and they don't all
   point the same direction.
3. **What "fair" means to Francesca vs. to the team.** Martha is already stretched thin caring for
   her niece — does a distributed cut that still touches Martha's paycheck actually protect her,
   or does it just spread a hardship she's less equipped than the others to absorb right now?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — read Appendix A's bios aloud, cold-call a gut guess, no dollar figures yet |
| 3:00–10:00 | Position defense — *"Convince us your option is right for Grampoline's team specifically, not just 'it closes the gap'"* |
| 10:00–15:00 | Pressure-test the models — *"Which factor is actually deciding your vote — the dollars, or who it lands on?"* |
| **15:00** | **DROP THE TWIST** — the customer's call, delivered slowly |
| 15:00–20:00 | Immediate recommit — did the twist change anyone's answer, or just their target |
| 20:00–30:00 | Threaded deep conflict (concentrated vs. distributed pain; who gets picked and why; what "fair" means here) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

A Hero computes Option B's percent cut using the wrong base (all six people, or one employee's pay
alone, instead of the $111,500 five-employee pool) and either overshoots or undershoots the
$20,000 target without noticing — or a Hero picks Option A by tenure or "who's newest" alone,
without ever checking whether that person's remaining pay actually closes $20,000 at all (only
Tiago and Irene's do; every other single-employee cut over- or under-shoots the target, which the
case never tells a Hero directly — they have to check it themselves in D3).

## Socratic questions

1. Both options remove exactly $20,000 from the budget — so if the dollars are identical, what actual number or fact is doing the work in your recommendation?
2. If you picked Operation Clean Break, does your chosen employee's remaining pay close the $20,000 gap exactly, or did you have to explain an over- or under-shoot, and by how much?
3. Operation Shared Weight cuts every employee's pay by the same *percent*, not the same *dollar amount* — why does that distinction matter to someone earning $20,000 in H2 versus someone earning $28,000?
4. Now that you know about the customer relationship risk tied to Irene, does the math actually favor letting her go less than it first appeared — and by how much, in dollars?
5. Martha is already missing days of work to care for her niece — does a 17.94% pay cut protect her more than losing her job would, or does it just create a second, smaller crisis on top of the first one she's already living through?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that
gravitated toward Irene at the Launch and stayed there after the Twist is worth asking about
directly: did the $19,050 revenue-risk number not feel real to them, or did they weigh it and
still land on Irene for other reasons?

## Lessons Learned

*(Preserved and adapted from the original 2020 Guide Notes, which flagged: Heroes need to bring
their position and evidence with them; watch for misunderstanding the spreadsheet or "paydays";
consider having Heroes physically move to their position at the start of the discussion so they're
challenging each other, not just the discussion leader.)*

- Whether Heroes checked that their chosen Clean-Break employee's remaining pay actually closes
  $20,000 (only Tiago/Irene do exactly), or assumed any single firing works.
- Whether Heroes computed Option B's percent on the correct $111,500 base (five employees only) or
  mistakenly included Francesca's own remaining pay.
- Whether the Twist's $19,050 revenue-risk figure changed anyone's chosen employee, or just
  prompted a values discussion about whether that risk should matter at all.

## Standards Touched On

Bar Graph · Data · Percent · Rounding · Currency · Pie Chart · How to compare two or more values ·
How to add multi-digit numbers · How to subtract multi-digit numbers · How to convert numbers to
percents · How to find the percent of a number · How to round a number to a specified place value ·
How to create a pie chart given a set of data

## Facilitator note — sensitivity

This case touches money stress and family hardship directly (Francesca going without pay, Martha's
caregiving crisis, a real possibility of job loss) — SPEC.md §6 flags this for the discussion lead.
Keep the frame on the case's own disclosed numbers and each employee's stated circumstances in
Appendix A; steer away from personal financial-hardship anecdotes from the room, which can turn a
math discussion into something a facilitator isn't equipped to hold.
