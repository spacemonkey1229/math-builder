# Guide Notes: Investment Portfolio

**Case:** Investment Portfolio (dashboard folder name: "Stock Market") · **Tier:** T4 · **Band:** MS-stretch / HS-entry · **Studio:** Acton Academy East Valley
**Standards:** see `case.json.standards[]` for the exact ids (43 skills — percent, decimal
arithmetic, ratio/proportion, negative numbers, mean/range, pie chart, bar graph, coordinate
plane, slope, y-intercept, comparison/rounding vocabulary)

Legacy conversion, 2026-08-22, reformatted from the original source Guide Notes
(`source/Y3/Additional/Stock Market/Guides Notes.docx`) onto the current anchor ladder. The
original recorded 5-6 named anchors plus a Monday launch hook (the real 2012 Bitcoin-vs-CenturyLink
story) and an Anchor 6 riff on crypto/art as "diversification or speculation." This guide keeps the
Monday launch hook and the OMAR-framework references from the source, and builds a new Twist
grounded in a real, sourced fact this case's own research turned up — not present in the original
source materials.

## Intro

Frame the format: this is not a worksheet about "the stock market" in the abstract — it's a real
decision Benjamin has to make with his own family's money, using two real, named, publicly
documented strategies from two real investors. Name the opener — "Benjamin has excess savings and
two shortlisted options. Tonight you build both cases before he has to."

## Launch — "Monday Case Study Launch" (from the original source Guide Notes)

Read this aloud, unchanged in spirit from the source doc: "Imagine it's 2012 and you just finished
your first year of employment with $10,000 saved. If you'd put all of it into Bitcoin at $7.50/coin,
you'd be sitting on a fortune today. If you'd put it into a struggling telecom stock instead, you'd
have lost most of it." Ask: with $10,000, would you (a) take a risk and invest in stocks, (b) put it
in a low-interest bank account, or (c) hide it under the mattress? Then: as a Hero with a few
thousand dollars saved, is it better to chase growth stocks (new, fast-rising, riskier) or value
stocks (established, slower, steadier)? Do not resolve this — it's priming for the real dilemma, not
part of it.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who's team Buffett — the simple 90/10? Who's team Dalio — the diversified All-Weather?" Show of
hands, no discussion yet. Record the count — Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'better'?"**

Let confusion grow deliberately. Heroes will want to jump straight to "which one made more money
historically" — push back: "Is it just as simple as picking the bigger number, or does it matter
*how* that number was earned — how much you'd have to survive along the way to get it?" If the room
lands on "we need to agree on what 'better' means before we can compare anything" on its own, that's
the case working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has a working sense that "better" needs a definition, ask them to name the actual
steps before touching Appendix C: what would you need to know about each portfolio's return, its
risk, and its worst case, to make this comparison fair? Encourage the OMAR framework (Options,
Metrics, Assumptions, Recommendation) as scaffolding, per the source doc's original reference. Push
specifically toward "risk-adjusted" language if it doesn't emerge on its own — "if one portfolio
returns more but also loses more in a bad year, how would you even compare them on one number?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix D's assumptions honestly. Ask directly: "Appendix C's numbers are real backtests —
but they're backtests of the *past*. What are we assuming when we use a portfolio's past return to
guess its future one (MA2)? What are we assuming about what counts as 'safe' when we pick a
risk-free rate to compute a Sharpe ratio (MA1)?" Both are real, defensible, and both are *choices*.

## Data Deep Dive

Now, and only now, the numbers. Walk D1 (allocation), D2 (return/risk table), and D3 (the
return-vs-holding-period chart) together as a room. This is where a Hero who plotted only the
30-year return (Buffett: 9.98%, All-Weather: 7.40% — a wide, obvious gap) will be surprised that the
gap narrows and narrows the shorter the window gets, and even more surprised once D6's Sharpe-ratio
computation lands.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"One more thing about Buffett's 90/10 rule. It didn't come from a book on how to build wealth over a
career. Buffett wrote it in his 2013 Berkshire Hathaway shareholder letter as an instruction for the
trustee managing his own wife's inheritance, after his death — a single lump sum, for someone who
would never add another dollar to it and would draw it down slowly for the rest of her life. Benjamin
is thirty, actively earning, and planning to add money to this account every single year for the next
three decades. Does 'good enough for Buffett's own wife' still mean 'good enough for Benjamin'?"

[S1] — see case.json sources[]. Real, dated, verifiable: the 2013/2014 Berkshire letter and its
"90% low-cost S&P 500 index fund, 10% short-term government bonds" instruction for a testamentary
trust are widely and consistently reported.

**Facilitator-only: what this does and doesn't change.** It changes nothing about Appendix C's
numbers — those are backtests of the fund allocations themselves, indifferent to *why* Buffett
proposed them. What it should invalidate is any Hero who has been leaning on "if it's good enough for
the single greatest investor alive, that settles it" as their entire argument, without separately
defending whether a lump-sum-for-a-widow recommendation actually transfers to a 30-year-old's
actively-growing, 30-year-horizon contribution plan. It does **not** settle the case either way —
Buffett's own reasoning for the 90/10 split (simplicity, low fees, faithful long-run exposure to
American business) is *also* a real argument that could still apply to Benjamin. The honest twist
question is "does the *origin* of this advice change how much weight it deserves here," not "the
advice is now wrong."

## Immediate recommit

Re-vote immediately. Ask by name: "Does knowing where this advice came from change your vote? Why or
why not?" That distinction — did the twist change the *math*, or just the *authority* you were
leaning on — is the transferable skill.

## Deep conflict — three threads (20–30 min)

1. **The risk-free-rate flip.** Appendix D's MA1 states a 1.5% risk-free-rate assumption for the
   Sharpe-ratio calculation. Ask the room to actually flex it (up and down) and watch what happens
   to the D6 comparison. Have them defend, with an actual number, whether 1.5% is the right
   assumption for a 30-year-old evaluating a decades-long hold — or whether a different, defensible
   risk-free rate would change their answer.
2. **The two metrics disagree.** The 30-year projected dollar total (D4) and the risk-adjusted
   Sharpe ratio (D6) do not tell the same story. Ask: if you had to pick just one of these two
   numbers to make Benjamin's decision for him, which one, and why? Is "more dollars" and "more
   efficient use of risk" actually the same goal, or two different ones Benjamin has to choose
   between?
3. **Benjamin's own stated fear.** He has explicitly said he doesn't know how he'd emotionally react
   to a severe drop. Does that admission change what "the right answer" even means here — is the
   math supposed to override his gut, or is his gut a legitimate input to the math problem?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — the 2012 Bitcoin-vs-CenturyLink hook, no scores yet, cold-call for a gut read on risk |
| 3:00–10:00 | Position defense — *"Convince us your portfolio is better, not just different"* |
| 10:00–15:00 | Pressure-test the models — *"Which of your numbers is most fragile if the assumption behind it moved a little?"* |
| **15:00** | **DROP THE TWIST** — the 2013 Berkshire letter, delivered slowly |
| 15:00–20:00 | Immediate recommit — did the vote move, and why |
| 20:00–30:00 | Threaded deep conflict (risk-free-rate flip; the two disagreeing metrics; Benjamin's own stated fear) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes will compute the 30-year projected dollar totals (D4), see Buffett 90/10 win by a wide
margin, and stop there — treating "more money at year 30" as the whole answer. The case's real
tension is that the *risk-adjusted* comparison (D6, the primary graded metric) is essentially a dead
heat, and that tie is itself sensitive to a single assumed input (the risk-free rate, MA1) that
nobody can look up — it has to be chosen and defended. Watch for a pitch that never builds D6 at all,
or that builds it but doesn't notice how close it lands, and calls the 30-year dollar gap the whole
story.

## Margin

Primary metric (`case.json.primary_metric`, 20-year Sharpe ratio): Buffett 90/10 = 0.6611, All-Weather = 0.6600, **margin_pct = 0.18** (Buffett fractionally ahead) — a real, sourced near-tie, well inside SPEC's 20% cap. This is the number of record; the D4 30-year-dollars reading (~55% margin, also Buffett-favored) is a different, non-primary metric — see `case.json.derived` and `case.json.balance` for both.

## Socratic questions

1. Buffett 90/10 projects to roughly 55% more money at year 30 than All-Weather under this case's assumptions (D4) — but the two portfolios post almost the exact same 20-year Sharpe ratio, a margin of only 0.18% (D6) — how can both of those be true at once, and which one should actually drive Benjamin's decision?
2. Appendix D's MA1 sets the risk-free rate at 1.5% for the Sharpe calculation — what would have to be true about the economy for a much higher risk-free rate to be the more defensible assumption, and does your D6 answer survive that change?
3. All-Weather's worst-case drawdown (-20.58%) is less than half of Buffett 90/10's (-45.52%) — but Buffett 90/10's 30-year return is also nearly 2.6 percentage points higher every single year — is a smaller worst case worth a permanently smaller average case, or not?
4. Buffett wrote his 90/10 instruction for his wife's inheritance — a lump sum, no further contributions, drawn down over her lifetime — while Benjamin is the opposite, actively contributing 40% of a growing income every year for 30 years — does that difference matter to which portfolio is right for him, and if so, in which direction?
5. Benjamin has said he doesn't know how he'd emotionally handle a 40% drop — if the risk-adjusted math really is a near-perfect tie, is that admission itself the tie-breaker, or is it a reason to distrust his own instincts and follow the higher-return option anyway?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight, and
how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that didn't move at
all after the twist is worth asking about directly: did the "whose advice is this really for"
question not land, or did the room already see both readings coming?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes built the D6 Sharpe-ratio comparison at all before committing to a position, or
  whether most groups stopped at the D4 dollar-total comparison and treated it as decisive.
- Whether the risk-free-rate flex (deep-conflict thread 1) produced a genuine debate about which
  assumption is defensible, or whether most groups treated 1.5% as a fixed fact rather than a choice.
- Whether the Buffett-letter twist changed anyone's vote, or whether Heroes correctly recognized that
  it doesn't settle the case either way and should have changed *how* they argued more than *what*
  they concluded.

## Standards Touched On

See `case.json.standards[]` for the full 43-id list (percent/decimal/negative-number arithmetic,
ratio & proportion, mean & range, pie chart & bar graph, coordinate plane & slope & y-intercept,
comparison and rounding vocabulary).

## Facilitator note — sensitivity

SPEC §6 applies: this case touches money stress (Benjamin's own worry about inflation and his
family's financial security) and an explicit personal admission of emotional uncertainty ("he does
not know how he would emotionally respond to a 40% drop"). Facilitators should be aware some Heroes
may have family members who have experienced real financial hardship or investment losses, and
should frame the discussion around Benjamin's specific, fictional decision rather than inviting
Heroes to disclose their own family's finances. No case-specific content changes are needed beyond
normal sensitivity to this topic.
