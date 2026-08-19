# Guide Notes: Redrawing Lines

**Case:** Redrawing Lines · **Tier:** T4 · **Band:** HS · **Studio:** Heroes Academy
**Standards:** Discrete Mathematics / Combinatorics (the three remaining zero-coverage skills) +
Discrete Mathematics / Proof And Recursion (all seven) — see `case.json.standards[]` for the exact
ids.

Researched and margin-resolved 2026-08-12. Current `margin_pct` = **10.0** on county-line
crossings — The Kennebec Split 10, The Hancock Line 11 (`sensitivity_model.py`,
`case.json.derived`). This file is re-checked for drift at every readiness run.

**Read this before you run the room.** The margin is 10.0 percent under two stated conventions and
it is not convention-free under either.

- **MA2.** Count Kennebec in the southern district instead of the northern one and The Kennebec
  Split scores 12 against The Hancock Line's 11 — **B wins instead, by 9.1 percent.** Both
  readings stay inside SPEC §2's cap, so the case is close either way, but the winner is a choice
  the case made, not a fact it found.
- **MA5.** Drop the Hancock–Knox water boundary and The Kennebec Split falls to 9 while The
  Hancock Line stays at 11 — the margin widens to 22.2 percent, past the cap, in A's favour.

Both are printed in the open in Appendix H. If a Hero attacks either, they are right to, and the
correct response is "yes, and here is exactly what that does to the number," not a defence.

## Intro

Frame the format: this is a staff memo, not a worksheet. Name the opener — "You are the analyst.
The commission votes Monday, your name is on the recommendation, and both plans are legal."
Say out loud, once, that the case uses no election data and that neither plan is a party's plan.
Say it early so nobody spends the discussion looking for the hidden partisan angle.

## Launch

Show the two plans side by side with every number stripped off — two shapes and one county in the
middle. Ask for a gut read: "Which one looks fairer to you, before you know anything about it?"
Do not confirm or correct. The point is a commitment made on shape alone, so that the arithmetic
later has something to overturn.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the plan that cuts a county in half?" Show of hands,
both options, no discussion. Record the count — Close will ask for it again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'fair'?"**

Let confusion grow here; it is deliberate. Heroes will reach for a single fairness number and
there isn't one. There is a count of people out of place and a count of communities cut in half,
and they point opposite ways. Push: "Margo isn't ranking one thing. She's ranking two, and one of
them is measured in people and the other in county borders. Can those go in the same column?"
If the room lands on "these are different units" without being told, the case is working.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Make them name the steps before opening an appendix: count how many plans there could be (D1),
write the counting down as a rule that builds each row from the one before (D2), prove the count
is complete rather than merely large (D3), prove what is impossible before computing what is
possible (D4), and only then score the two plans in front of you (D5). Re-ask: "Is our question
still the right one now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Appendix H has five, and they are not equally dangerous. MA1 (a severed county is worth 1
crossing) is the numeric dial and it is stable — flexed either way by half, the ranking does not
move; the two plans tie only at a weight of 2. MA2 (a divided county is counted on the side
holding more of its people) is the one that decides who wins, and it cannot be flexed because it
is a convention, not a number. MA5 (a water boundary counts as a border) is the same kind of
choice and pushes the margin to 22.2 percent. MA3 (the staff shortlist rule, now "closest to equal
population") decides which plans are on the table at all, which is a bigger power than any of
them. Ask directly: "Which of these five would you most want a source for, and why can't you have
one?"

## Data Deep Dive

Now, and only now, the numbers.

**The counting (D1–D3).** 16 counties, each going to one of two districts, gives 65,536 by the
Fundamental Counting Principle — 65,534 once you drop the two that empty a district. The
size-breakdown row is C(16, j), and it reads 1, 16, 120, 560, 1820, 4368, 8008, 11440, 12870,
11440, 8008, 4368, 1820, 560, 120, 16, 1. Two things to draw out at the board: the row is a
palindrome, and it sums to 65,536. The palindrome is the same fact as Appendix F's two contiguity
rows — 1,734 assignments, 867 plans — because an assignment names which district is which and a
plan on a wall does not.

**The proof (D3), and why it is the point of the case.** Appendix F's first row is a claim about
how many plans exist; it is not evidence that any of them were checked. What licenses "we examined
every whole-county plan" is the induction: base case, then Pascal's rule inside the inductive step.
A Hero who quotes 65,534 as a credential has not noticed the difference between a big number and a
proof. That gap has its own section near the bottom of these notes; watch for it here first.

**The pigeonhole (D4).** 1,362,359 is odd, so no two districts can hold equal shares of it: one of
them must hold at least 681,180. That is worth saying slowly, because it reframes the whole
argument — The Kennebec Split is not "perfectly equal," it is off by 1, which is simply the least
Maine allows. Second claim: 16 counties into 2 districts forces at least 8 into one of them.
Third: the four largest counties into two districts forces at least two of them into the same
district. Note carefully what that does and does not say — pigeonhole proves a pair exists, not
which pair. The guaranteed consequence is therefore the *smallest* such pair, Penobscot and
Kennebec: at least 275,841 people from those four counties alone land in one district, whatever
the plan. The vivid instance is Cumberland and York, whose 515,041 people are most of a district
before anything else is placed — but a Hero who writes that pigeonhole *proves* the pair is
Cumberland and York has over-read the principle, and a Hero who quotes 515,041 as the guaranteed
floor has made the same error with a bigger number. That over-reading is worth catching out loud;
it is the same error as reading a count as an audit.

**The scorecard (D5).** The Kennebec Split runs along 9 county borders — Androscoggin–Cumberland,
Androscoggin–Sagadahoc, Cumberland–Oxford, Hancock–Knox, Kennebec–Lincoln, Kennebec–Sagadahoc,
Knox–Waldo, Lincoln–Waldo, Oxford–York — and through Kennebec, for 10. The Hancock Line runs along
11 — Androscoggin–Cumberland, Androscoggin–Sagadahoc, Cumberland–Oxford, Hancock–Penobscot,
Hancock–Waldo, Hancock–Washington, Kennebec–Lincoln, Kennebec–Sagadahoc, Knox–Waldo,
Lincoln–Waldo, Oxford–York — and through nothing, for 11. On population: 681,179 against 681,180
is a maximum deviation of 1, or 0.000147 percent; 683,062 against 679,297 is 3,765, or 0.5527
percent. Set that against Appendix E: Karcher struck 0.6984 percent, Tennant upheld 0.79 percent,
and The Hancock Line sits below both — so B's legal position is genuinely comfortable and A's
advantage on population, though enormous in ratio, is an advantage over a plan that is already
lawful. Cold-call for the percent conversion specifically; a Hero who can compute 3,765 out of
681,179.5 but cannot say what that means next to 0.79 has done the arithmetic and skipped the
argument.

**Watch the deviation basis.** Appendix E's percentages are *maximum
deviation*: larger district minus smaller district, over the ideal. The other natural reading —
one district's distance from the ideal — is exactly half: 1,882.5 people, 0.2764 percent, for The
Hancock Line. Half-size figures are not comparable to Karcher and Tennant, and the error is
invisible here because both readings clear both benchmarks. It stops being invisible at the twist:
Oxford's two figures are 8,363 (1.2277 percent) and 4,181.5 (0.6139 percent), and only the first
one is above Karcher's 0.6984. A Hero who quotes 0.6139 has proved the opposite of what they
think. Ask every pitch which of the two numbers it is quoting, before the twist lands.

## Twist — drop this at about 15 minutes into the discussion

Deliver slowly, with pauses.

"A commissioner has moved from the floor to strike the staff shortlist rule and swap Oxford County
in for Hancock. Look at Appendix D again with that motion in front of you: the Oxford version
splits the state 685,361 against 676,998."

"Recompute what you just argued. That plan runs along 9 county borders and through none. It beats
The Kennebec Split's 10 on Margo's own rubric — the whole-county side has just won the primary
metric, by 11.11 percent."

"And its maximum deviation is 8,363 people. That is 1.2277 percent — larger than the 0.79 percent
the Court upheld in Tennant, and larger than the 0.6984 percent it struck down in Karcher. The
whole-county plan is now the best plan on Margo's rubric and the only plan on the table that might
not survive a court. You have sixty seconds. Does that change your recommendation, or only your
reason for it?"

**Facilitator-only: what the numbers actually do.** `evaluate_twist()` in `sensitivity_model.py`
recomputes the pair as 10 against 9 — the winner flips from A to B on the primary metric, margin
11.11 percent the other way. Both popular positions break at once, which is the design: "A wins
the rubric too" dies for the A side, and "our plan is the legally comfortable one" dies for the B
side. Nobody's answer is handed to them. The strongest thing a Hero can say here is that the
substitution proves the argument was never really about which county gets added — it was about
MA3, the staff rule that ranked the shortlist on population and thereby kept the rubric's own
best plan off the table. The rubric and the rule disagree, and no number resolves that.

**If the room has already overturned MA2.** A room that adopted the minority convention was
already scoring The Kennebec Split at 12, so the whole-county side was already ahead and the
twist's metric flip is not a flip for them — it just widens the gap. The legal half still lands
with full force in that room, because Oxford is above both Appendix E benchmarks where Hancock was
below both. Lead with the deviation, not the crossings, if that is where the discussion has gone.

## Immediate recommit

Re-vote immediately, by name. "Did the motion change your vote, or just your confidence?" That
distinction is the transferable skill, not the vote.

## Deep conflict — three threads

1. **Two units, one column.** Crossings are borders; deviation is people. D5 asks for both and
   then asks for one recommendation. Is putting them in one ranking a judgement the analyst is
   entitled to make, or one she should hand up to the commission unresolved?
2. **A count is not an audit.** Appendix F says 65,534. D3 says why anyone should believe the
   commission looked at them. Which of those two would you put in a court filing, and what does
   the other one actually buy you?
3. **The rule nobody wrote down.** MA3 is staff practice. If a Hero goes looking outside it, there
   is a whole-county plan — Androscoggin, Cumberland, Oxford and York in the south — splitting the
   state 683,957 against 678,402 with only 5 crossings: a maximum deviation of 5,555, or 0.8155
   percent, and far better than either plan on the table on the primary metric. It also moves
   335,054 Mainers into a different district, which is the cost the staff rule exists to avoid,
   and its 0.8155 percent is above Tennant's 0.79. If somebody finds it, that is the best outcome
   of the night: reward it, then ask what the rule was protecting.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — two shapes, no numbers, cold-call for a gut read, stand/sit vote |
| 3:00–10:00 | Position defense — *"Convince us it's better, not just more legal"* |
| 10:00–15:00 | Pressure-test the models — *"Whose number is resting on an assumption?"* |
| **15:00** | **DROP THE TWIST** — the Oxford substitution, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (two units; count vs. audit; the rule nobody wrote down) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

**Primary trap — a count read as an audit.** As of the 2026-08-18 revision, `case.md`'s Appendix F no
longer prints 65,534 — a Hero has to derive it (D1, the Fundamental Counting Principle over the
Appendix A county list). That makes the trap *stronger*, not weaker: most Heroes will compute
65,536 (or 65,534 once the two empty-district assignments are dropped), feel the satisfaction of
having done real work to get there, and write "the commission examined every plan" straight into
the pitch anyway. Nothing in the packet examines anything: 65,534 is a count of how many plans
exist, not evidence that any were checked — deriving it yourself doesn't change what it proves. The
only thing that licenses the claim is the D3 induction proof, and a pitch that quotes the screening
count as a credential while skipping the base case has made exactly the mistake the case was built
to catch. Watch for it in the pitch, and watch for its cousin in discussion — treating "we
enumerated it" and "we proved it" as the same sentence.

**Second wrong path — the deviation basis.** Set out in full in the Data Deep Dive above. Most
learners will quote one district's distance from the ideal — the half-size figure — against
Karcher's and Tennant's maximum-deviation percentages, because "largest deviation from the ideal"
is the phrase that sounds right. It is harmless on the two plans on the table and decisive at the
twist, where it turns Oxford's 1.2277 percent into 0.6139 and reverses the legal conclusion.
Appendix E states the basis explicitly and D5 asks for both figures, so a Hero who does this has
skipped a line they were given — but they will still do it, and it will look like careful work.

## Socratic questions

1. The Kennebec Split is off by 1 person and The Hancock Line by 3,765 — but D4 proves no Maine plan can be exactly even. Does knowing that perfection was never available make the gap between 1 and 3,765 matter more, or less?
2. Karcher struck 0.6984 percent and Tennant upheld 0.79 percent, and The Hancock Line is at 0.5527 percent — below both. If B is already lawful, what work is A's extra precision actually doing?
3. Appendix H says a severed county is worth 1 crossing, and that number came from nowhere. The two plans tie at 2. At what weight would you change your recommendation — and does your answer mean the recommendation was ever really about crossings?
4. Appendix F says 65,534 plans and D3 asks you to prove a row of numbers adds up. Which of those two would convince you the commission looked at every plan, and why isn't it the bigger number?
5. Appendix D shows Oxford scores better on crossings than Hancock, and Hancock is on the table anyway because of a rule that is staff practice and not law. Who should be allowed to make that rule?
6. MA2 decides who wins: one convention gives A by 10.0 percent, the opposite gives B by 9.1 percent. If a stated convention picks the winner, is the recommendation a finding or a choice — and should Margo's memo say which?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing count to Anchor 1's. A room that did not
move after the twist is worth asking about directly: did the substitution not land, or did the
room already have the right structure built in before it arrived?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether the induction proof in D3 was where Heroes actually got stuck, or whether the pigeonhole
  claims in D4 were harder because they demand a proof with no computation at all.
- Whether the twist landed as new information or as a gotcha, and whether the room could name what
  broke rather than just changing its vote.
- Whether anybody went outside MA3's shortlist rule on their own, and what it took to get there.
- Whether the "no election data" framing held, or whether the room kept reaching for it anyway.

## Standards Touched On

Fundamental Counting Principle · Binomial Coefficient · Pigeonhole Principle · Recursive Formula ·
Base Case · Mathematical Induction · Inductive Step · Mean · How to apply the Fundamental Counting
Principle to count outcomes · How to compute a binomial coefficient · How to write a recursive
formula for a sequence · How to convert a recursive formula to an explicit formula · How to prove
a statement using mathematical induction · How to convert numbers to percents

## Facilitator note — sensitivity

Redistricting is politically charged in a way that has nothing to do with the math in this case.
The case is built entirely on population counts, county borders and case law — no election
results, no party registration — and neither option is a partisan position. If a learner steers
the discussion toward parties or candidates, redirect to the two numbers on the table and note
that both plans satisfy the same legal criteria. If a learner has family in a divided county and
takes it personally, that is legitimate material for the discussion, not a derailment: ask them to
put the harm in a unit the memo could carry.
