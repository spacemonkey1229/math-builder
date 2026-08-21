# Guide Notes: Feedback

**Case:** Feedback · **Tier:** T4 · **Band:** HS · **Studio:** Launchpad
**Standards:** Pre-Calculus / Polar And Parametric — the complete six-skill group, all
`new_coverage`. Exact ids in `case.json.standards[]`.

**Status:** drafted and researched 2026-08-19/20. Current `margin_pct` = **4.39** (House-Left
safer, pre-twist). Every figure quoted below resolves in `sensitivity_model.py`'s `evaluate()` /
`evaluate_twist()` output; this file is re-checked for drift at every readiness run.

## Intro

Frame the format before anything else. This is not a word problem with a microphone drawn on it —
it is a real job with a real, live consequence if it's wrong. Name the opener: *"You're the sound
engineer. One monitor amp channel just died, forty minutes to doors. Whichever wedge you pick,
you own the mix if it squeals."* Say plainly that both wedges are physically installable tonight
and both are defensible choices, and that the room's job is to decide which one they'd actually
commit to before the doors open.

## Launch

Play (or describe vividly) ten seconds of real feedback squeal — plenty of royalty-free examples
exist, or simply describe the sound and the sudden dead silence a house manager cuts the system
into. No numbers, no stage plot yet. Ask one question and take answers without correcting any of
them: *"If a monitor is closer to the mic but almost off to the side, and another is farther away
but almost straight ahead of it — which one worries you more?"* Let the gut reads stand. The Close
revisits them.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

*"Is anyone courageous enough to stand with Priya on House-Right — the close one?"* Stand-or-sit,
both options, no discussion permitted. Record the count; the Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'safer'?"**

Let confusion grow here; it is deliberate. The room will want to say "farther away is safer" —
distance-only thinking — and that is wrong in an interesting way. Push:

- *"Safer at what moment? The whole show, or one specific instant?"*
- *"The case says the mic rejects sound differently depending on direction. Rejects it how much,
  exactly — and does 'somewhat off to the side' mean a lot of rejection or a little?"*
- *"If a monitor were twice as far away but pointed straight at the mic's most sensitive angle,
  would that definitely be safer than a close one aimed at its least sensitive angle?"*

Do not resolve this. Say out loud: *"Huh — turns out 'closer is worse' isn't automatically true
here."* A room that leaves Anchor 2 still arguing about what "safer" even means is exactly where
it should be.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Make them name the steps before any appendix is opened. The chain they should arrive at, in some
form:

1. Turn each wedge's stage position into a distance and an angle off the mic's front (D1).
2. Find out how much the mic actually rejects sound at that angle (D2).
3. Combine distance and rejection into one safety score (D4).
4. Do that not just for the static verse, but for every moment the performer actually stands
   somewhere else (D3, D4).
5. Whichever wedge has the *worse* worst moment is the riskier choice, no matter how good its best
   moment looks (D5).

Re-ask: *"Is our question still the right question, now that we can see the steps?"* If someone
notices that step 5 means a wedge's best-looking number might not be the number that matters, that
is the whole case arriving early — do not step on it, but do not confirm it either.

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the honest gaps, all of which live in `case.md` Appendix E:

- The stage positions of both wedges (MA1) are the case's own fictional venue's numbers, not a
  real, published stage plot.
- The mic's aim is assumed to stay fixed the whole number, even while handheld (MA2) — a real
  performer might turn to face the crowd, which would change every angle in the case.
- The performer's blocking marks (MA3) are the case's own choreography, not a real script.
- Priya checks only the named blocking marks, not a continuous sweep (MA4).

Ask which of these changes the recommendation if it moves, and which merely changes the size of
the answer. The answer is worth withholding: MA1 and MA3 are both genuinely load-bearing — flex
either one and the recommendation can flip (see `sensitivity_model.py`'s flex sweep, several dials
flip the base verdict at ±50%). MA2 and MA4 change *how tractable* the case is, not *which wedge
wins*. A Hero who works that distinction out unprompted has understood the structure of the case.

## Data Deep Dive

Now, and only now, the numbers.

Work D1 → D5 as a room. Cold-call specifically on **D1's angle conversion**: this is where a Hero
who has memorized "θ = arctan(y/x)" without checking which axis is "on-axis" will get House-Right's
angle backwards (it is 90°, straight off to the side, not close to on-axis just because the wedge
is close). The sentence to fish for is some version of *"close doesn't mean in front of it."*

Two facilitator-only notes to hold in reserve:

- **The static verse is the least important number in the whole case, and it looks the most
  important.** House-Right's static-verse GBF (21.584 dB) is the single best number either wedge
  posts anywhere in the case — and it never governs the recommendation, because the bridge cross
  drives House-Right's mic much closer to it later in the song. A pitch that leads with the verse
  numbers and stops there has done real work and reached the wrong answer.
- **The angle can matter more than the distance.** House-Left's worst moment (16.246 dB) beats
  House-Right's worst moment (15.563 dB) even though House-Left is *farther* from the mic at every
  single checked moment. The pattern-rejection term is doing more work than the distance term at
  the moments that matter. Ask a room that's surprised by this to recompute House-Right's cross-end
  angle by hand.

Full worked figures — every checked moment, both wedges, the worst-case selection, and the margin
— are in the **Facilitator-only numbers** section below and reproduced by
`python3 cases/feedback/sensitivity_model.py`.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses.

*"The director just added one more mark. During the last few seconds of the song — the closing
tableau, right before blackout — Dana holds a pose at a new spot, further into the stage-left
wing, one nobody blocked when you did your math."*

*"Her mark is (1, 4), same reference frame as everything else you've already got. You have about
a minute. Does your recommendation still hold?"*

Then the follow-up, which is the actual point: **"What just broke in your original model? Were you
wrong — or were you missing information?"**

**Facilitator-only: what the numbers actually do.** At (1, 4), House-Left's GBF drops to
**14.235 dB** — worse than House-Left's previous floor of 16.246 dB, and now the *lowest* number
either wedge posts anywhere in the case. House-Right's GBF at that same point is **18.159 dB**,
comfortably above House-Right's own existing floor of 15.563 dB — so House-Right's worst moment is
still its bridge-cross-end number, unchanged. **The verdict flips.** House-Right becomes the safer
overall recommendation by **9.33%** — a margin thinner than the one it just overturned, and in the
opposite direction from the pre-twist recommendation.

The twist introduces exactly one new number — the tableau mark's coordinates — and reuses every
formula and every other figure already in the packet, which is why a Hero can genuinely price it
in the room without new appendices.

**One honest caveat, and hand it over if a Hero pushes.** The flip depends on the exact tableau
mark. A tableau mark anywhere reasonably close to House-Left (within a few feet, still well off
House-Left's on-axis heading) reproduces the flip; a tableau mark that instead lands *near
House-Right* would reinforce the pre-twist verdict instead of overturning it. This is disclosed,
not hidden — see `case.json.balance` and the sensitivity note below.

Do not hand the arithmetic over unprompted. A Hero who says *"I'd need to convert that new point to
polar relative to both wedges before I could answer"* has given the strongest possible answer and
should be told so.

## Immediate recommit

Re-vote at once, by name where the room is small enough. Ask: *"Did the tableau mark change your
vote, or only your confidence?"* That distinction is the transferable skill; the vote itself is
not.

## Deep conflict — two threads (20–30 min)

1. **The best number vs. the number that matters.** House-Right's static-verse number is the best
   single number in the whole case. Is a room wrong to be drawn to it? What does it mean to say a
   system is "only as safe as its worst moment" — and is that always the right way to grade a live
   show, or does it undervalue a wedge that's excellent most of the time and merely adequate once?

   **Guide: do not let the room settle for "worst-case thinking is obviously correct."** Ask
   directly: *"If House-Right's bad moment lasted one second and House-Left's bad moment lasted the
   whole first verse, would you still grade them the same way?"* The case's own MA4 assumption —
   checking only named blocking marks, not weighting by how long each moment lasts — is a real,
   debatable modeling choice, not an obvious one. A Hero who challenges MA4 has found a genuine
   soft spot in the case.
2. **Whose blocking is it, anyway?** The director set the choreography before Priya was consulted
   about monitor placement. Should blocking decisions account for the sound engineer's constraints,
   or is the sound engineer's job to make whatever blocking exists work safely? If the answer is
   "both should talk earlier," what would Priya need to know before rehearsal, and is that
   realistic on a community-theater schedule and budget?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — feedback squeal, cold-call gut reads, stand/sit vote, no explanation |
| 3:00–10:00 | Position defense — *"Convince us it's safer, not just closer or farther"* |
| 10:00–15:00 | Pressure-test the models — *"Which wedge's number is most fragile, and why?"* |
| **15:00** | **DROP THE TWIST** — the new tableau mark, delivered slowly, with pauses |
| 15:00–20:00 | Immediate recommit — who reverses, and was it the vote or the confidence that moved |
| 20:00–30:00 | Threaded deep conflict (best number vs. the number that matters; whose blocking is it) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes **will** compare the two wedges on distance alone — "House-Right is closer, so it must
be riskier" — and **will skip** converting each position into an angle off the mic's on-axis
heading before judging it. A wedge nearly off to the side of the pattern can be much safer than a
closer read suggests, because the pattern-rejection term can outweigh the distance term; a Hero
who never computes D1's θ column will confidently rank the two wedges by raw distance and get the
static verse backwards.

The second half of the same trap: **most will stop at the static verse** and never check the
bridge cross at all, because the verse numbers look decisive (House-Right wins by 14.06% on the
verse alone) — and the verse numbers never govern the actual recommendation. Watch for a pitch that
reports only Appendix A's static (r, θ) pair and never opens D3/D4.

Both halves produce a *confident* wrong-headed pitch that looks like real work — a conversion
table, a graph, a recommendation — which is exactly why it needs naming in advance. Watch for a
D5 table that only has one row of numbers per wedge instead of three.

**Trap 2, subtler and more dangerous because it produces a table that LOOKS complete: silently
reusing the static verse's (r, θ) for all three D4 rows instead of recomputing distance and angle
from Dana's actual mic position at each moment.** D1, D2, and D3 each read as self-contained
sub-tasks, so a Hero can satisfy each one locally and never notice that D4 requires re-deriving a
fresh (r, θ) pair — from the *fixed* wedge coordinates to Dana's *moved* mic position — at the
cross-start and cross-end moments, not copying D1's static numbers down the column. A pitch built
this way has three filled rows, a graph, and a recommendation — it looks identical in shape to
correct work. **The tell:** in a correctly-worked table, House-Left's angle strictly decreases
across the three moments (39.81° → 45.00° → 18.43°) and House-Right's does not move monotonically
either (90.00° → 111.80° → 90.00°) — a table where either wedge's θ column repeats the same value
three times in a row is this trap, not a coincidence. Cold-call a Hero on why the mic's position
relative to a *fixed* wedge changes even though the wedge itself never moves.

## Socratic questions

1. House-Right posts the single best number anywhere in this case, and it still isn't the recommended wedge. How can the "best" number and the "right" answer be different things?
2. Your D1 table says House-Right is closer to the mic than House-Left. Does that make it more dangerous, less dangerous, or does the answer depend on something the distance alone doesn't tell you?
3. Priya only checks gain-before-feedback at three named moments, not continuously through the whole song. What would you need to believe about the performer's motion in between those moments for that to be a safe simplification — and is it always true?
4. If you had to bet on which single number in this case is most likely to be wrong in the real world, which would you pick: a wedge's exact stage position, or the cardioid pattern equation itself? Why?
5. The director controls the blocking and Priya controls the mix. If their choices conflict, whose job is it to notice before the show, and how would they find out in time?

## Close

**VOTE AGAIN.** Then: *"Did we ask the right question at the start?"* and *"What math was new to
you tonight, and how did you actually attack it?"*

Compare the closing vote with Anchor 1's. A room that didn't move at all after the tableau mark is
worth asking about directly: did the twist not land, or did the room already have the right
structure built in and simply recompute?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether D1's angle conversion (rather than D3's parameter elimination) was genuinely where the
  room got stuck.
- Whether anyone caught, unprompted, that the static verse never governs the recommendation.
- Whether the twist produced real recomputation or only a change of mood.
- Whether "worst moment governs" as a grading rule was understood or quietly replaced with
  "average moment governs."

## Standards Touched On

Polar Coordinate · Parametric Equation · Parameter · How to convert a point between rectangular
and polar coordinates · How to graph a polar equation · How to eliminate the parameter to find a
rectangular equation

## Facilitator note — sensitivity

None required (SPEC §6). The stakes are professional and mildly comic (a live feedback squeal
mid-show), not personal, financial-hardship, illness, or death. No flag needed.

## Facilitator-only numbers

Every figure below is reproduced by `python3 cases/feedback/sensitivity_model.py`. Do not retype a
number here that script does not also print — the continuity check exists to catch exactly that.

**Base case (student-facing packet — three checked moments per wedge)**

| Moment | House-Left (r, θ) | House-Left GBF | House-Right (r, θ) | House-Right GBF |
|---|---|---|---|---|
| Static verse (mic at origin) | 7.810 ft, 39.81° | 18.923 dB | 6.000 ft, 90.00° | 21.584 dB |
| Cross-start (mic at (2,1)) | 5.657 ft, 45.00° | 16.427 dB | 5.385 ft, 111.80° | 24.677 dB |
| Cross-end (mic at (0,3)) | 6.325 ft, 18.43° | **16.246 dB** | 3.000 ft, 90.00° | **15.563 dB** |

**Worst-case per wedge:** House-Left **16.246 dB**, House-Right **15.563 dB**. **`margin_pct`
4.39**, House-Left the safer recommendation.

**The twist — fourth checked moment (facilitator-only, revealed at 15:00)**

| Moment | House-Left (r, θ) | House-Left GBF | House-Right (r, θ) | House-Right GBF |
|---|---|---|---|---|
| Tableau mark (mic at (1,4)) | 5.099 ft, 11.31° | **14.235 dB** | 2.236 ft, 116.57° | 18.159 dB |

**Worst-case per wedge, post-twist:** House-Left **14.235 dB** (now its own tableau moment, not
the cross-end), House-Right **15.563 dB** (unchanged). Margin **9.33%**, House-Right now the safer
recommendation. **The verdict flips.**

**Probe 5 sweep.** Flexing MA1's four wedge coordinates and MA3's four cross coordinates ±50%, one
at a time: the base verdict (House-Left, 4.39%) is **not stable** — `house_left_x` −50%,
`house_left_y` −50%, `house_right_y` +50%, and `cross_end_y` −50% each flip the winner to
House-Right, with flexed margins ranging from about 16% to 33%. This is a real, disclosed
instability, not an error: the base margin is thin (4.39%) precisely because the two wedges are a
genuinely close call, and MA1/MA3 are exactly the load-bearing assumptions `case.md` Appendix E
already names as sensitive. See `case.json.balance` and Appendix E's own Sensitivity column — no
Hero-facing text states the flip threshold or which direction it goes, only that the answer is
sensitive to these values.
