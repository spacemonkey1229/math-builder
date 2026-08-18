# Facilitator Guide — Phone Plans

Freshly authored for this conversion (the legacy source had no Guide Notes.docx and no
Socratic-question plan — see `case.json.legacy_conversion_note`).

---

## Argument for A (Verizon)

Verizon Plus is the name extended family already recommended, and its 30GB of mobile hotspot
data is a real, workable amount for a salesperson checking email and pulling account records
between clinic visits. Verizon also has the larger nationwide 4G LTE network by a real, sourced
margin — about 70% of U.S. land area covered versus AT&T's 68% (Appendix E) — an edge concentrated
in exactly the rural Oregon stretches (Burns, Astoria, Florence) Jake is about to start driving
through four days a week, where a cheaper plan and a bigger hotspot allowance do the family no
good if the signal itself isn't there.

## Argument for B (AT&T)

AT&T Extra 2.0 is cheaper than Verizon Plus at every phone-line count the family will actually
reach — today's 2 lines, the near-term 3rd line, and the eventual 4th — both before and after
tablets and Oregon's wireless tax are folded in. It also includes more mobile hotspot data
(50GB vs. 30GB), which speaks directly to Jake's stated need to hotspot a laptop from the road.

## The margin

Computed in `sensitivity_model.py` / `case.json.balance` — not restated here in words, per
`skills/case-write/SKILL.md`'s 2026-08-13 rule against handing the student the answer key inside
a facilitator document a Hero could stumble into. Run `python3 cases/phone-plans/sensitivity_model.py`
for the worked numbers.

---

## Guide Notes — the anchor ladder

### Intro

Frame the format: this is a real-world consumer decision, not a puzzle with one hidden right
answer. Name the opener — a family that just moved back to the U.S. with no working phone plan
and a job starting Monday.

### Launch

Read the Overview aloud, or project it. Stop at "Jake nods slowly, already reaching for his
laptop." Do not preview the Dilemma text yet — let the room sit with the moving-truck scene first.

### Anchor 1

TAKE A STAND AND VOTE. No reasoning yet, just commit. *"Is anyone courageous enough to stand with
Verizon? With AT&T?"* Record the initial split on the board — it becomes the baseline for the
re-vote at Close.

### Anchor 2

WHAT IS THE PROBLEM WE'RE SOLVING? *"Is this just 'which carrier is cheaper'? What do you mean by
cheaper — cheapest today, or cheapest once the family actually needs 4 lines?"* Deliberately let
confusion grow here: *"Wow, this is actually a harder question than it looked."*

### Anchor 3

WHAT IS THE PROCESS? *"If we go through Appendix A and B and find every price, how do we decide
which one to even compare?"* Re-ask: *"Is 'cheapest 1-line price' still the right question, given
what Jake actually needs his phone to do?"*

### Anchor 4

WHAT DON'T WE KNOW? *"Do we need to make any assumptions to finish this? Which ones actually
matter?"* Surface Appendix F's two modeling assumptions (tablet-line pricing, the blended tax
rate) here, before anyone has touched a calculator.

### Data Deep Dive

Now, and only now, the numbers. Work D1 (eligibility) as a group first, then let pairs build
D2/D3's cost tables independently.

### Twist

New information that breaks some models. See "The twist" below for the full narrative — it
concerns Verizon Plus's 30GB mobile hotspot cap against Jake's actual, stated usage pattern.

### Close

VOTE AGAIN. *"Did we ask the right question at the start?"* *"What math was new to you, and how
did you attack it?"* Name who moved from their Anchor 1 position and why.

### Lessons Learned

The recurring failure mode in this case is comparing the *cheapest* tier on each carrier instead
of the cheapest tier that actually meets Jake's stated hotspot requirement — a Hero who skips
straight to "which number is smaller" on Appendix A/B's top row never notices the hotspot column.
The second-order lesson, surfaced by the Twist, is that "cheaper" and "sufficient" are not the
same test, and a real family has to clear both.

### Standards Touched On

See Appendix G of `case.md` for the full verbatim spine list — percent, currency, rounding,
multiplication, addition, subtraction, and bar-graph reading/construction, all applied to a real
recurring monthly bill rather than a one-time purchase.

---

## Five Socratic questions

1. Your D1 eligibility table rules out both carriers' cheapest tier. What specific feature is missing from Verizon Welcome and AT&T Value 2.0 that Jake's job actually requires?
2. Once you're comparing Verizon Plus to AT&T Extra 2.0 instead of the cheapest tiers, does the winner from your first comparison stay the winner?
3. Your D3 table shows the bill at 2, 3, and 4 phone lines. Does the dollar gap between the two carriers grow, shrink, or stay about the same as lines are added?
4. Appendix C's tablet-line price is one of only two dials in this case that isn't taken straight off a carrier's own rate table. If that price were $10 lower on Verizon's side, would your recommendation change?
5. Jake hotspots his phone several days a week on the road. What would his actual monthly hotspot usage have to be for the 30GB-vs-50GB gap in Appendix A/B to matter more than the dollar difference in D2?

## The trap

Most Heroes will skip straight from the Overview to Appendix A and Appendix B, see Verizon
Welcome at $65/line and AT&T Value 2.0 at $50/line, and assume AT&T Value 2.0 is the obvious
cheap winner — without ever running D1's eligibility filter to check whether *either* tier
actually gives Jake the mobile hotspot data he explicitly needs for his work travel. Welcome
has none at all, and Value 2.0's 3GB (Appendix A) would be gone in a day or two of hotspotting
a laptop from the road. A learner who does this will build an entire pitch on the wrong pair of
plans and never notice, because $50/line genuinely is the cheapest number on the page — it is
just cheap for a plan that cannot do the job. The correct comparison is one tier up, between
Verizon Plus and AT&T Extra 2.0, where both the dollar figures and the mobile-hotspot allowances
are different from what the Welcome-vs-Value comparison suggested. Watch for a pitch that never
explains *why* it moved past Welcome/Value — that's the tell that the trap wasn't caught, just
walked past.

## The twist

Jake's hotspot habit is not a hypothetical. He is described as driving to hospitals and clinics
across Oregon at least four days a week, using his phone as his and Alyssa's home internet
connection, and needing the hotspot for his laptop specifically. Verizon Plus's 30GB of mobile
hotspot data (Appendix B) is a real, finite monthly cap — a working professional hotspotting a
laptop for email, video calls, and account software four days a week for a full month can
realistically approach or exceed 30GB, at which point Verizon throttles hotspot speed for the
rest of the billing cycle. AT&T Extra 2.0's 50GB cap (Appendix A) has meaningfully more headroom
for the identical use pattern. This doesn't change which plan is cheaper on paper — it changes
whether the cheaper plan on paper is actually the plan that reliably does the job Jake needs it
to do every single week, which is a real-world consideration D5 asks students to name explicitly.

**Soundness check.** Re-derived under both a *sequential* reading of the case (a Hero works D1
before D5, ruling out Welcome/Value on hotspot presence alone, then later weighs hotspot
*capacity* as a secondary factor in D5) and a *simultaneous* reading (a Hero reads all of Appendix
A/B at once and could, in principle, notice the capacity gap immediately during D1). Under either
reading the twist survives: it never contradicts Appendix A/B's stated GB figures, it never
requires assuming a specific hotspot-usage number in gigabytes (which the case does not state),
and it does not change D1-D4's dollar arithmetic — it only adds a real, sourced, non-dollar
consideration to D5 that a Hero who stopped at "AT&T is cheaper" would miss. No stated assumption
in Appendix F is required for the twist to hold, so there is no reading under which it silently
does nothing.

## Sensitivity note

`sensitivity_model.py`'s `FLEX[]` sweeps only Appendix F's two authored Modeling Assumptions
(MA1: flat per-tablet pricing; MA2: blended Oregon tax multiplier) at ±50%, per
`skills/case-readiness/SKILL.md`'s P5 scoping rule — the carrier per-line pricing in Appendices
A/B is sourced, given fact, not an authored dial.

- **`oregon_tax_rate` is STABLE** at ±50% either direction — a single multiplier applied to both
  options' pre-tax totals cannot change their ratio, so the margin is unchanged at both extremes.
- **`verizon_tablet_rate` and `att_tablet_rate` are NOT stable.** This case's real, sourced base
  margin is 18.8% (re-derived 2026-08-18 after correcting the Verizon tablet add-on rate from an
  untiered $20.00/mo to the live-verified, tier-matched Unlimited Plus rate of $25.00/mo), close
  enough to the SPEC §2 20% cap that a large enough swing in either carrier's tablet-line price
  pushes the margin past the cap in one direction, while the other direction narrows it to a thin
  single-digit margin without flipping the winner (see `case.json.balance.stability` for the exact
  figures). This is disclosed, not eliminated, per `DOCTRINE_LEDGER.md` MCS-26/MCS-41 — a
  facilitator running this case should know going in that the tablet-pricing assumption is
  genuinely load-bearing, not decorative, and be ready to field a Hero who challenges it directly.

No illness/death/family-hardship content. This is a straightforward consumer cost comparison; the
only real facilitation risk is treating the tablet-pricing assumption as more solid than it is.

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote — no explanation (Anchor 1). |
| 3:00–8:00 | Position defense: "Convince us why it's better, not just cheaper" (Anchor 2). |
| 8:00–13:00 | Pressure-test the models: "What process gets us to a real answer?" (Anchor 3). |
| 13:00–15:00 | Name the assumptions: tablet pricing, tax rate (Anchor 4). |
| 15:00–30:00 | Data Deep Dive: D1's eligibility filter as a group, then D2/D3 in pairs. |
| **30:00** | **DROP THE TWIST** — Verizon Plus's 30GB hotspot cap vs. Jake's actual usage pattern, delivered slowly, with pauses. |
| 30:00–38:00 | Immediate recommit: who reverses? "What just broke in your model?" |
| 38:00–45:00 | Close, re-vote, reflection, lessons learned, standards touched on. |

## Cohort bands

See `case.json.cohort_bands[]` — Full (12-20), Compressed (6-11), and 1:1/pair (1-2), each with a
band-specific note on how the anchors compress.
