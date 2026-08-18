#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Tide Window (owned by this case, per MCS-26 / A2).

Authored 2026-08-12 to close P5 NOT RUN and give P4's twist-integrity finding a
mechanical backstop. This case is a THRESHOLD-vs-FLOOR shape, not a two-option
apples-to-apples ratio like Cold Chain's dose count: Option B (Slack Tide) is
structurally always far safer than Option A (Dawn Transit) by raw under-keel
clearance, so a naive "return each option's clearance margin" model would have
B trivially "win" under every parameter setting and P5's flip-detection would
never fire on anything meaningful.

Instead this model returns the two numbers the case's OWN graded `margin_pct`
is actually built from (see `case.json.balance.margin_basis`): "A" is the Dawn
Transit's achieved clearance (ft), "B" is the Pilots' Association's required
policy floor (ft). `evaluate()`'s generic `100*(A-B)/B` then equals exactly
this case's real, GRADED margin -- 19.33%, matching `case.json.derived` and
`case.json.margin_pct` exactly -- rather than a meaningless number from
forcing a dollar-valued win/lose encoding through a generic ratio. "A wins"
means the transit clears the floor and is legally authorizable; if a flexed
parameter pushes the achieved clearance below the floor, the winner flips to
B, correctly signaling PROHIBITED. MA2's dollar penalty does not enter this
metric (it never moves the safety margin) and is FLEXed separately below only
so probe 5 exercises every stated assumption dial, per MCS-26, even though
this particular metric can't reflect a cost-side flip -- see `margins()` for a
by-the-numbers report, including MA2's role, that doesn't depend on this
ratio-based reduction.

FIXED 2026-08-17 (real defect, not a per-case workaround): this file used to
put the PRE-twist (predicted, no storm) figure in `evaluate()` and the POST-
twist (storm-adjusted) figure in `evaluate_twist()`. That is backwards for
what `evaluate()` is actually used for: `skills/case-readiness/scripts/
tier2_probes.py`'s probe 5 always flexes and grades `model.evaluate()` --
never `evaluate_twist()` -- against the SPEC section 2 20% cap. But this
case's OWN stated margin_basis (case.json.balance) establishes that the 20%
cap applies to the POST-twist margin (19.33%), not the pre-twist one (47.07%,
which is *supposed* to be wide -- that is the whole premise the twist erodes).
With the old (pre-twist-in-evaluate) wiring, probe 5 was grading the wrong
number two ways at once: (1) it swept `setdown_ft` -- MA3's own headline
assumption -- through a function that hardcoded `setdown_ft=0`, so the sweep
had *zero* effect on the metric it was supposedly testing sensitivity of, and
(2) the 47.07% base margin it did compute is well outside the 20% cap by
design, so the probe "mechanically reports FAIL" every run (see the stale
`case.json.balance.stability` note this replaces) even though the case's real
graded scenario (19.33%) is fine. `evaluate()` now IS the case's real graded
primary_metric (post-twist); `evaluate_twist()` now returns the pre-twist
predicted baseline as a disclosed CONTEXT metric only (not graded) -- the same
pattern `cases/codebreaker/sensitivity_model.py` uses for its non-graded axis.

CONTRACT — exactly two public names (see skills/case-readiness/scripts/
example_sensitivity_model.py for the full spec this follows):

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     optional; same shape, non-graded context metric

Verified against cases/tide-window/case.json.derived (2026-08-17, post-fix):
    evaluate()       (GRADED, post-twist): A legal, margin +0.634 ft, 19.33%
                     of the 3.28 ft floor -- matches case.json.margin_pct
    evaluate_twist() (context, pre-twist, predicted/no-storm): A legal,
                     margin +1.544 ft, 47.07% of the floor
    setdown_ft that zeroes the graded margin: 1.544 ft (well within S10's
    real ~4 ft documented range for wind-driven setdown -- see
    RESEARCH_LOG.md)
"""
import math

PARAMS = {
    # --- Appendix B / MA4: which real, sourced depth governs -----------------
    "governing_depth_ft": 54.0,
    # --- Appendix A, S4: real NOAA tide predictions (not an authored assumption,
    # excluded from FLEX the same way cold-chain excludes its sourced cold-life
    # ratings) ------------------------------------------------------------------
    "dawn_low_ft": -0.176,
    "slack_high_ft": 5.831,
    # --- Appendix B, S5/S7: real sourced vessel draft and policy floor --------
    "draft_ft": 49.0,
    "policy_floor_ft": 3.28,
    # --- Appendix E, MA3: the Twist's wind-driven setdown ----------------------
    "setdown_ft": 0.91,
    # --- Appendix E, MA2: the late-delivery penalty, expressed as A's "value"
    # when Option A is legally authorized -------------------------------------
    "late_penalty_usd": 18000.0,
}

# Probe 5 flexes these two -- the case's actual stated, author-chosen Modeling
# Assumptions (MA2, MA3). governing_depth_ft (MA4) is deliberately NOT in FLEX:
# it is a disclosed choice between two real, equally-sourced figures (S6), not
# an authored scenario magnitude -- SPEC section 2's +/-50% sweep is the wrong
# tool for a binary either/or. See the __main__ block below for the discrete
# 52 ft check instead. late_penalty_usd (MA2) does not move evaluate()'s A/B
# (see docstring) -- it is included in FLEX anyway so probe 5's sweep touches
# every stated assumption per MCS-26; its 0%-movement result is itself the
# honest, correct finding (MA2 is a schedule/dollar dial, not a safety dial).
FLEX = ["setdown_ft", "late_penalty_usd"]


def _dawn_clearance_ft(p, setdown_ft=0.0):
    actual_depth = p["governing_depth_ft"] + p["dawn_low_ft"] - setdown_ft
    return actual_depth - p["draft_ft"]


def _slack_clearance_ft(p):
    actual_depth = p["governing_depth_ft"] + p["slack_high_ft"]
    return actual_depth - p["draft_ft"]


def evaluate(params):
    """GRADED primary_metric (matches case.json.margin_pct = 19.33%): post-
    twist, MA3's wind-driven setdown applied to the Dawn Transit's achieved
    clearance -- the Slack Tide happens hours later, outside the twist's
    modeled window, so only A is affected. A = achieved clearance (ft), B =
    the policy floor (ft) -- see module docstring for why this pair, not a
    literal Option A vs Option B comparison. This is the function probe 5
    flexes and grades against the SPEC section 2 20% cap, so it MUST be the
    case's real graded scenario, not the pre-twist one (see 2026-08-17 fix
    note in the module docstring)."""
    p = dict(PARAMS)
    p.update(params or {})
    return {"A": _dawn_clearance_ft(p, setdown_ft=p["setdown_ft"]), "B": p["policy_floor_ft"]}


def evaluate_twist(params):
    """CONTEXT metric only, NOT graded (see case.json.balance.margin_basis):
    the pre-twist, predicted/non-adjusted water level with no wind-driven
    setdown applied -- the wide, comfortable margin the twist goes on to
    erode. Included so a reader can see both numbers side by side; probe 5
    never sweeps this one. A = achieved clearance (ft), B = the policy floor
    (ft)."""
    p = dict(PARAMS)
    p.update(params or {})
    return {"A": _dawn_clearance_ft(p, setdown_ft=0.0), "B": p["policy_floor_ft"]}


def margins(params=None, setdown_ft=None):
    """Reporting helper -- clearance-over-floor margins in ft, including
    Option B (Slack Tide), for cross-checking against case.json.derived. Not
    used by evaluate()/evaluate_twist() -- MCS-26's contract needs exactly two
    named metrics, this gives the fuller picture for a human reader."""
    p = dict(PARAMS)
    p.update(params or {})
    sd = p["setdown_ft"] if setdown_ft is None else setdown_ft
    floor = p["policy_floor_ft"]
    return {
        "dawn_pretwist_margin_ft": round(_dawn_clearance_ft(p, setdown_ft=0.0) - floor, 3),
        "dawn_posttwist_margin_ft": round(_dawn_clearance_ft(p, setdown_ft=sd) - floor, 3),
        "slack_margin_ft": round(_slack_clearance_ft(p) - floor, 3),
    }


if __name__ == '__main__':
    print("margins (base params):", margins())

    print("\nFLEX sweep +/-50%, setdown_ft (MA3, base 0.91):")
    for sd in (0.455, 0.6825, 0.91, 1.365):
        m = margins(setdown_ft=sd)
        print(f"  setdown_ft={sd:.4f}  dawn_posttwist_margin_ft={m['dawn_posttwist_margin_ft']:+.3f}"
              f"  {'LEGAL' if m['dawn_posttwist_margin_ft'] > 0 else 'PROHIBITED'}")

    print("\nWhere does the margin actually zero?")
    m = margins(setdown_ft=1.544)
    print(f"  setdown_ft=1.544  dawn_posttwist_margin_ft={m['dawn_posttwist_margin_ft']:+.3f}"
          f"  (vs. S10's real ~4 ft documented Tampa Bay event -- well inside the real range)")

    print("\nMA4 discrete check -- the 52 ft alternate reading (NOT in FLEX, see docstring):")
    m52 = margins({"governing_depth_ft": 52.0}, setdown_ft=0.0)
    print(f"  governing_depth_ft=52  dawn_pretwist_margin_ft={m52['dawn_pretwist_margin_ft']:+.3f}"
          f"  {'LEGAL' if m52['dawn_pretwist_margin_ft'] > 0 else 'PROHIBITED -- pre-twist, before any storm'}")

    print("\nverdict check (evaluate = GRADED post-twist, evaluate_twist = context pre-twist) --"
          " A=achieved clearance ft, B=policy floor ft:")
    graded, context = evaluate({}), evaluate_twist({})
    g_margin_pct = 100 * (graded['A'] - graded['B']) / graded['B']
    c_margin_pct = 100 * (context['A'] - context['B']) / context['B']
    print(f"  evaluate()       (GRADED, post-twist)  A={graded['A']:.3f}  B={graded['B']:.3f}"
          f"  winner={'A' if graded['A'] > graded['B'] else 'B'}  margin_pct={g_margin_pct:.2f}%"
          f"  (case.json's graded margin_pct: 19.33%)")
    print(f"  evaluate_twist() (context, pre-twist)  A={context['A']:.3f}  B={context['B']:.3f}"
          f"  winner={'A' if context['A'] > context['B'] else 'B'}  margin_pct={c_margin_pct:.2f}%")
