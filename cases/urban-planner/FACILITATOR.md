# Guide Notes: Urban Planner

**Case:** Urban Planner · **Tier:** T4 · **Band:** MS-stretch/HS-entry · **Studio:** Heroes Academy
**Standards:** see `case.json.standards[]` for the exact ids (28 skills — coordinate-plane
geometry and distance, area/proportion-based capacity estimation, cost arithmetic, and a
weighted-criteria decision matrix)

Legacy conversion, 2026-08-20, built from the original case study docx
(`source/Y3/Session 5/Urban Planner/Case Study_ City Planner.docx` and its Guide Notes,
`Urban Planner.docx`) onto the current 11-anchor ladder. Ordinance 322b, Paul Cordon's role and
deadline, and the site list are preserved from the source. The dilemma is narrowed from the
original's 3 sites to 2, per `cases/_concepts/LEGACY_DILEMMA_LOCKS_2026-08-20.md` — see
`case.json.legacy_conversion_note` for the full account. The original case had almost no
load-bearing math (its site appendices were empty except for each site's name); this conversion
builds the entire quantitative spine from real, cited data.

**A note on content (SPEC §6 — read before running this case).** This case is built on a real,
still-live policy question — where a city sites services for its unhoused population — and it is
reasonable for a Hero to have a strong personal reaction to it. Keep the discussion anchored to the
math and the disclosed assumptions, not to a debate about whether homelessness itself is a
personal failing or a systemic one, and not to characterizing either neighborhood's residents.
Both options are framed here exactly as factual tradeoffs (closer-but-higher-income vs.
farther-but-less-neighborhood-opposition) — present both without editorializing either side, and
redirect a Hero who starts arguing from ideology back to "what does your weighted score say, and
why did you weight it that way?" If a Hero or their family has a personal connection to
homelessness or housing insecurity, be attentive — this is a live, real-world topic, not a
hypothetical one.

## Argument for A (Westmoreland–Eastmoreland Site)

A wins decisively on accessibility — 3.61 miles from City Hall versus B's 6.69 miles, a real
distance advantage computed from each site's real coordinates, not an estimate. That distance
matters concretely: every resident's medical, legal and social-service appointment downtown is a
shorter, cheaper, more reliable trip. A's cost per resident is essentially tied with B's (both land
near $191,600), so A's proximity is not being bought with worse economics — it's close to free.
The honest gap in A's favor is that it sits in a higher-income residential neighborhood, which is
real context (case.md Background) but not something the graded weighted score measures directly —
push a Hero who leans on "less opposition" for B to say which criterion in their own matrix that
opposition actually shows up in, if any.

## Argument for B (Hayden Island Nature Preserve)

B wins decisively on capacity — an estimated 217 residents housed versus A's 73, a real three-fold
difference that traces directly to B's much larger sourced acreage (540.80 ac vs. A's 181.59 ac).
Under the case's stated assumption that a comparably modest fraction of each site's total acreage
gets developed (MA1), that acreage difference alone is B's whole capacity advantage — cost per
resident does not offset it (see Argument A). If the city's actual goal is serving as many of its
unhoused residents as possible with one site, B is the site that does that.

## The margin

`margin_basis` (case.json.balance): using the author's example weighting (40% accessibility / 35%
capacity / 25% cost-efficiency, Appendix F MA6) and Appendix E's scoring method, **Score_A = 7.68,
Score_B = 8.16 — B wins by 6.3%.** This is a real but thin margin, and it is *weighting-dependent
by design* — see Sensitivity below. A Hero who weights accessibility more heavily than capacity
will land on A; one who weights capacity more heavily will land on B; both are legitimate,
defensible positions under Challenge D4, which explicitly asks each Hero to choose and justify
their own weights rather than use the case's example. The case works precisely because there is no
single "correct" weighting — the discussion is about which criterion a city should actually
prioritize when it can only build one site, not about who did the arithmetic correctly.

## Five Socratic questions

1. "Your accessibility score for Site A is almost twice Site B's. Your capacity score for Site B is almost three times Site A's. Which of those two gaps is bigger, and does your weighting actually reflect which one you think matters more?"
2. "Cost per resident came out almost identical for both sites. If the case's cost data had come out clearly favoring one site, would that have changed your weights — or only the arithmetic?"
3. "You assumed the city would only develop about 1% of each site's total acreage. What happens to your recommendation if that number is wrong — say, the city actually plans to develop 2%, or only half a percent?"
4. "Site A is in a higher-income neighborhood and Site B draws less opposition. Neither of those shows up as a number in your weighted matrix — should it? If yes, how would you actually score it without inventing a number?"
5. "If you could only pick one criterion — accessibility, capacity, or cost — and had to throw out the other two, which one would you keep, and does the site you'd recommend change?"

## The trap

Most Heroes will compute all three criterion scores correctly and then default to an even
equal-thirds split across the three criteria (or copy the case's own 40/35/25 example) without
genuinely defending *why* — turning
Challenge D4's central ask (justify your own weights) into a rubber stamp on the author's example.
A Hero who does this has done the arithmetic but skipped the actual decision the case is testing.
Cold-call on this specifically: "Why 40/35/25 and not 60/20/20? What would have to be true about
Portland's real situation for you to weight it that way?" A Hero with no answer beyond "that's what
the example used" has not actually made the call themselves.

## Sensitivity note (SPEC §6 / T4)

This case is unusually sensitive to its own stated assumptions, and that is disclosed, not hidden
(`case.json.modeling_assumptions[].sensitivity`, `sensitivity_note`). Running
`sensitivity_model.py`'s ±50% sweep: **the developed-footprint percent (MA1) and the criteria
weights (MA6) both flip the winner** at a ±50% flex — the outreach-shuttle frequency (MA4) barely
moves the answer at all, since transportation cost is a small fraction of total cost either way.
Tell the room this directly if it comes up: a case where the "right" answer moves when a reasonable
person's assumption changes is not a broken case — for a T4 case built on stated, disclosed
assumptions layered onto real data, that is the intended lesson.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch, 30-second commitments, stand/sit vote — no explanation |
| **3:00–10:00** | Position defense: "Convince us why it's better, not just closer / not just bigger" |
| **10:00–15:00** | Pressure-test the models: "Whose recommendation is most fragile to a weight change?" |
| **15:00** | **DROP THE TWIST** — delivered slowly, with pauses |
| **15:00–20:00** | Immediate recommit: who reverses? "What just broke in your model?" |
| **20:00–30:00** | Threaded deep conflict — two named threads: (1) accessibility-to-services vs. capacity-served; (2) whose weighting scheme is actually defensible vs. convenient |
| **30:00–45:00** | Close, re-vote, reflection, lessons learned |

## Intro

Frame the format: this is a real Portland city-planning decision, built from a real 2021 ordinance
and real city data, not a worksheet with a story stapled on. Name the opener — "One city planner,
two weeks to recommend a site, and a decision that genuinely can't make everyone happy. How do you
even decide what 'best' means here?"

## Launch

Read the Overview aloud, then Background's site descriptions (Westmoreland–Eastmoreland vs. Hayden
Island) with no Appendix B/C/D numbers shown yet. Ask: "Just from what you've heard — which site
sounds like the obvious choice, and why does it stop sounding obvious once you think about it for
ten more seconds?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who's recommending the Westmoreland–Eastmoreland Site? Who's recommending Hayden Island?" Show of
hands, no discussion yet. Record the count — Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'best site'?"**

Push on what "best" even means here — closest? biggest? cheapest per person? least opposed? Let the
room sit in the ambiguity: "Is anyone courageous enough to define 'best' before we've computed
anything?"

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has a working definition of "best," ask them to name the actual steps: how far is
each site, how many people can each site hold, what does each site cost per resident, and how do
you combine three different numbers into one decision. Re-ask: "Given how we just defined 'best' —
is that still the right process?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix F's six modeling assumptions as a group, out loud, before anyone computes final
scores — especially the developed-footprint percent (MA1) and the criteria weights (MA6, which
each Hero sets for themselves in D4). Ask which one the room thinks matters most.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's distance map, D2's capacity table, and D3's cost table
together as a room, then let Heroes build and compare their own D4 weighted matrices.

**The trap:** see above — Heroes copy the case's example weighting instead of defending their own.
Cold-call: "Why that split, specifically?"

## Twist — drop this at roughly the 15-minute mark

Deliver slowly, with pauses:

"Paul Cordon just got a call from the city's environmental review office. The northwest half of
Hayden Island the plan was counting on turns out to sit mostly within the Columbia River's active
floodplain and existing levee-protected wetland habitat — the same land conservation groups have
been fighting to preserve for years. Building on it isn't off the table, but the buildable footprint
just got cut in half again. You now have 60 seconds. Does your recommendation still hold — or did
it just flip?"

Run `python3 sensitivity_model.py` (the `evaluate_twist()` function halves Site B's developed-
footprint assumption, MA1) to check the real effect for this case's numbers, and report the real
answer to the room — do not assert an outcome here that the model doesn't confirm. (For the record:
this twist does flip the winner back to Site A under the case's example weighting — B's capacity
advantage shrinks enough that A's accessibility edge takes over. Confirm this live rather than
stating it from memory, since a Hero's own weights may not flip the same way.)

## Close — vote again

VOTE AGAIN. "Did we ask the right question? What math was new to you today, and how did you attack
it?"

## Lessons Learned

- How would you rank this case study in terms of difficulty, 1–5?
- What was the hardest single step — the distance formula, the capacity proportion, or building
  your own weighted matrix?
- What math concepts were new to you, and how did you take on that challenge?
- If given a similar case next time, what would you do differently?

## Standards Touched On

Share the standards checklist from `case.json.standards[]`.
