# Guide Notes: Kite Cut

**Case:** Kite Cut · **Tier:** T2 · **Band:** MS-core · **Studio:** Heroes Academy
**Standards:** Geometry / Quadrilaterals And Polygons — 3 singleton-reinforcement skills
(`geometry-parallelogram`, `geometry-rhombus`, `geometry-kite`, each currently at `n=1` in the
spine, not `n=0` — see `case.json.reinforcement_note`) + 8 reinforcement skills (11 total standards
in `case.json.standards[]`, `new_coverage[]` is empty per the reinforcement carve-out). See
`case.json.standards[]` for the exact ids.

Researched and margin-resolved 2026-09-09 (`margin_pct` = 2.16, see `sensitivity_model.py`).

## Intro

Frame the format: this is a real small-business cutting-floor decision with a deadline tonight,
not a worksheet about shapes. Name the opener — "You're the owner. Two sample frames are on the
mat. Two hundred fifty kites' worth of fabric budget rides on which one you cut tonight."

## Launch

Show both sample frames (or a photo/sketch of them) side by side, spine and spreader marked but
no measurements labeled. Ask: "Which one do you think uses more fabric, just from looking at it?"
Do not confirm or correct. Most rooms will guess the two shapes use noticeably different amounts
of sail cloth just because they *look* different — that gut read is the trap, worth recording out
loud before anyone touches a calculator.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Priya on The Eddy Flyer — the one that skips the tail
entirely?" Show of hands, both options, no discussion. Record the count for Close.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'better'?"**

Let confusion grow. Heroes will want to jump to "which one flies better" or "which one looks more
impressive at a festival" — real considerations, but not the graded metric. Push: "Priya's boss is
her own supply budget. What number does *she* actually need before five o'clock?" If the room
separates "which kite is the better flyer" from "which one costs less to build," the case is
working.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once separated, ask the room to name the steps before opening the appendices: classify each frame
correctly as a Rhombus or a Kite (D1), confirm both frames actually enclose the same sail area
(D2) — a genuine surprise most rooms won't predict — work out how efficiently each shape's panels
can be cut from the roll (D3, D4), and only then build the full cost table (D5).

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix E's three Modeling Assumptions honestly: MA1/MA2 (tail length and width) and MA3
(Option B's cutting-layout efficiency). Ask which one is load-bearing. The honest answer: MA3, by
far. A sharp Hero who runs the sensitivity math will find that Option B needs its real cutting
waste to land under roughly 1.89× raw sail area to win outright — and the case's stated value is
2.0×, uncomfortably close. Let them find this themselves before confirming it.

## Data Deep Dive

Now the numbers. Walk D1's rhombus/kite classification, D2's identical-area result, D3's
parallelogram-nesting proof, D4's yardage conversion, and D5's full cost table as a room,
cold-calling for D2 and D3 specifically — these are where a Hero who never actually ran the
diagonals-formula arithmetic, or never verified the nested parallelogram's sides are truly
parallel and congruent, will visibly struggle. That's useful information, not a moment to rescue.

**Facilitator-only geometry note.** Option A (crossing at 50%): all four sides =
√(18² + 18²) = 25.46 in — a rhombus. Option B (crossing at 19%, i.e. 6.84 in from the nose): two
sides = √(18² + 6.84²) = 19.26 in, the other two = √(18² + 29.16²) = 34.27 in — a kite, not a
rhombus. Both frames' sail area = 36 × 36 ÷ 2 = 648 sq in — *identical*, because the diagonals
formula doesn't care where along the diagonals they cross, only their full lengths and that
they're perpendicular. That equal-area result is the case's built-in "aha."

**Facilitator-only cost note.** Option A: 1,224 sq in of fabric/kite (648 sail + 576 tail) →
$4.505 fabric + $7.50 spar = **$12.005/kite**. Option B: 1,296 sq in of fabric/kite (MA3's
individually-boxed layout, no tail) → $4.77 fabric + $7.50 spar = **$12.270/kite**. Margin:
**2.16%**, Option A wins — a genuinely thin margin, in the spirit of this corpus's gold-standard
close calls.

## Twist

`N/A` for this case. The sensitivity itself (MA3's near-flip at 1.89× vs. the stated 2.0×) already
does twist-like work inside Anchor 4/Deep Conflict without needing a scripted reveal — introducing
a second, separate twist on top of that would crowd a T2 case. A future revision could add one
(e.g., "the festival cuts the order to half" or "a supplier discount only applies to one fabric
color") if a live run shows the discussion needs a jolt.

## Deep conflict — three threads (20–30 min)

1. **Same area, different fabric bill — how?** Both sails are exactly 648 sq in, yet the cheaper
   overall option isn't simply "the frame with less area" (they're tied) — it comes down entirely
   to how efficiently each *shape* cuts from a roll, plus one option's tail. Why does raw area not
   settle a manufacturing cost question by itself?
2. **The rhombus's symmetry is the whole reason D3 works.** Ask directly: what specific property
   of a rhombus (not a general kite) makes the zero-waste parallelogram pairing possible? What
   would have to be true about the Eddy sail's shape for the same trick to work on it?
3. **MA3 is one stated assumption away from flipping the case.** Is a case-author's stated
   assumption — even a reasoned, disclosed one — a fair thing to build a recommendation on, when
   the sensitivity math shows how close it is to changing the answer? What would Priya want to
   verify with her own cutting floor before committing to either option?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both sample frames, cold-call for a gut read, no formulas yet |
| 3:00–10:00 | Position defense — *"Convince us the number you're graded on is the number that matters"* |
| 10:00–15:00 | Pressure-test the models — *"Whose cost table is most fragile to a bad assumption?"* |
| 15:00–20:00 | Data Deep Dive walkthrough — D2's equal-area result, D3's parallelogram proof |
| 20:00–30:00 | Threaded deep conflict (area vs. cost; rhombus symmetry) — this is where the case's TWIST lands: reveal MA3's near-flip (1.89x vs. the stated 2.0x waste multiplier) and let the room sit with how thin that margin is |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes will look at the two visibly different frame outlines and assume the shape that
*looks* more different from a simple square must use noticeably more or less fabric — treating
outline shape as a direct stand-in for material quantity. Watch for a pitch that asserts one
option "obviously" uses less material without ever actually running D2's diagonals-formula
comparison — it hasn't done the geometry, and the geometry says the two raw sail areas are
identical. The real cost driver (cutting-layout efficiency, not raw area, plus the tail) is easy
to miss if a Hero stops at "I computed the area, so I'm done."

## Socratic questions

1. D2 shows both frames enclose exactly 648 square inches of sail fabric. If the shapes look this different, why is the raw area identical — and what does that tell you about judging material cost by eye?
2. D3 proves two rhombus panels nest into a parallelogram with zero waste. What single property of a rhombus makes that proof work, and why does the same construction fail to close cleanly for a kite that isn't also a rhombus?
3. MA3 assumes Option B's sail panels are cut with no pairing efficiency at all. What would a real cutting-floor test have to show about the Eddy sail's shape to change that assumption — and how far would it have to move before Option B actually wins?
4. Option A needs a tail and Option B doesn't. If tail material were free, would you still recommend Option A — and does that change what you'd tell Priya to research before committing the shop's budget?
5. The margin between the two options is thin. If you were Priya, what's the one number on this cutting floor you'd want to double-check with a real supplier invoice before signing off on 250 kites?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether the "equal area, different cost" finding in D2 landed as a genuine surprise or had to be
  told outright.
- Whether MA3's near-flip (1.89× vs. the stated 2.0×) generated real debate about trusting a
  stated assumption, or whether the room treated it as settled once stated.
- Whether the rhombus/kite classification in D1 was the easy warm-up it's designed to be, or a
  harder gate than expected.

## Standards Touched On

Parallelogram · Rhombus · Kite · Quadrilateral · Congruent · Perpendicular Lines · Parallel Lines
· Area

## Facilitator note — sensitivity

None required (SPEC §6) — the stakes here are a small business's production budget and a festival
deadline, not personal loss or hardship.
