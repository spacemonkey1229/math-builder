"""Sensitivity model for The Overlap Call (SPEC section 2 balance test, case-readiness Tier 2
probe 5).

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py, templates/
INTERACTIVE_HTML_CONTRACT.md section 2) -- exactly these public names:

    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            the ASSUMPTION subset probe 5 sweeps
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the case's own twist applied

Canonical (D4-resolved, outlier node 828 dropped from both real sets, matching case.json's
balance_test/FACILITATOR.md): |A|=65, |B|=169, |A intersect B|=26, |A union B|=208 -- real,
sourced ([S2], derived from the raw SNAP ego-Facebook archive), NOT flexed here; probe 6 (data
decay) stress-tests the underlying dataset, not probe 5.

This case states exactly two Modeling Assumptions (case.json.modeling_assumptions):
  MA1 -- kits_per_week (45), an invented order-of-magnitude scenario constant.
  MA2 -- rate_dual, the choice to REUSE the sourced single-exposure rate [S3] (16.6%) for the
         intersection group specifically, because no dual-exposure-specific rate was found.
`rate_single` (Appendix B / [S3]) is sourced and stays fixed -- it is the value the union group's
yield is computed from, and MA2 never touches it. `rate_dual` is a SEPARATE dial from
`rate_single` even though they are set to the same 0.166 value at baseline: MA2's actual, honest
content is "we don't know the true dual-exposure rate, so we reuse the single-exposure one" --
flexing rate_dual in isolation is what actually tests whether that specific, disclosed guess is
load-bearing. (An earlier draft of this file collapsed both rates into one shared parameter,
which was a MODELING BUG, not a design choice -- scaling both plans' rates together mostly
cancels out in the ratio and would have hidden exactly the fragility this probe exists to find.
Fixed here; do not re-merge them.)

Base evaluate(PARAMS) reproduces case.json's canonical balance_test exactly: A = 7/45 = 15.556%,
B = 4/26 = 15.385%, margin ~= 1.11%, A ahead.

evaluate_twist(PARAMS) reproduces FACILITATOR.md's CURRENT twist (rewritten 2026-09-13 remediation
pass -- see QA_REPORT.md): a countywide lab equipment failure cuts Priya's usable kit supply for
the rest of the week from 45 to 27, mid-discussion. This is a flex of MA1 (kits_per_week), not a
change to either real set. Widest Net's ratio falls to round(27x0.166)/27 = 4/27 = 14.815% while
Shared Risk is unaffected (it was already using fewer than 27 kits) at 4/26 = 15.385% -- the winner
FLIPS from A to B, margin 3.85%. (An earlier draft of this twist added one contact to the
intersection instead -- that version only ever WIDENED A's lead, 1.11% -> 5.00%, and so failed
case-readiness Tier 2 probe 4's "does the twist invalidate a position" check. Replaced, not
patched, because the underlying math -- both plans applying the identical MA2 rate means each
plan's per-kit ratio is the rate itself in expectation, and the observed margin is a pure whole-
number-rounding artifact of kits_per_week and pool size -- makes kits_per_week, not intersection
size, the only genuinely twist-able lever that can flip this case's winner.)
"""

# Canonical real set sizes (post-D4 outlier drop) -- [S2], NOT flexed (probe 6 covers the raw data).
UNION_SIZE = 208
INTERSECTION_SIZE = 26
TWIST_KITS_PER_WEEK = 27.0  # FACILITATOR.md twist: countywide lab equipment failure cuts supply 45->27

PARAMS = {
    # --- SOURCED (fixed; not in FLEX) ---
    "rate_single": 0.166,    # Appendix B / [S3] -- sourced household close-contact secondary attack rate

    # --- ASSUMED (case.md Appendix C -- the two stated Modeling Assumptions) ---
    "kits_per_week": 45.0,   # MA1 -- Priya's weekly test-kit allotment
    "rate_dual": 0.166,      # MA2 -- reused rate applied to the intersection group specifically
}

FLEX = ["kits_per_week", "rate_dual"]


def _plan_yield(kits_available, pool_size, rate):
    """A plan tests min(kits_available, pool_size) people from its pool at `rate`; the number of
    confirmed secondary cases found must be a whole number of people, so the expected count is
    rounded before the per-kit ratio is taken -- the case's own stated arithmetic
    (case.json balance_test.argument_A/argument_B: 'round(45x0.166)=7', 'round(26x0.166)=4')."""
    kits_used = min(kits_available, pool_size)
    if kits_used <= 0:
        return 0.0, 0, 0.0
    cases = round(kits_used * rate)
    return kits_used, cases, cases / kits_used


def evaluate(params, union_size=UNION_SIZE, intersection_size=INTERSECTION_SIZE):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Metric = confirmed secondary cases
    found per test kit used (this case's own primary_metric). A (Widest Net) is tested at the
    sourced single-exposure rate; B (Shared Risk) is tested at the separately-flexed MA2 rate."""
    p = dict(PARAMS)
    p.update(params or {})
    _, _, yield_a = _plan_yield(p["kits_per_week"], union_size, p["rate_single"])
    _, _, yield_b = _plan_yield(p["kits_per_week"], intersection_size, p["rate_dual"])
    return {"A": yield_a, "B": yield_b}


def evaluate_twist(params):
    """FACILITATOR.md's twist: a countywide lab equipment failure cuts Priya's usable kit supply
    for the rest of the week from 45 to 27, mid-discussion -- a flex of MA1 (kits_per_week), not
    a change to either real set. Any kits_per_week the caller passes in `params` is overridden
    for this call, matching how the twist is presented in the room (an external event, not a
    dial the room chooses)."""
    p = dict(params or {})
    p["kits_per_week"] = TWIST_KITS_PER_WEEK
    return evaluate(p)


def _state(ev):
    """(winner-or-"TIE", margin_pct), computed against the base's own possible tie state -- not
    an arbitrary max()-on-ties pick. margin_pct is 0.0 on a tie, not undefined."""
    a, b = ev["A"], ev["B"]
    if a == b:
        return "TIE", 0.0
    hi_key, lo_key = ("A", "B") if a > b else ("B", "A")
    lo = ev[lo_key]
    margin = 0.0 if lo == 0 else 100.0 * (ev[hi_key] - lo) / lo
    return hi_key, margin


def _report(label, ev):
    state, margin = _state(ev)
    print(f"{label}: A={ev['A']*100:.3f}%  B={ev['B']*100:.3f}%  state={state}  margin={margin:.2f}%")
    return state, margin


if __name__ == "__main__":
    base = evaluate(PARAMS)
    winner, margin = _report("Base", base)
    assert winner == "A" and abs(margin - 1.11) < 0.05, \
        f"Base model drifted from case.json's disclosed canonical base (A wins by 1.11%): got {winner} {margin:.2f}%"

    twist = evaluate_twist(PARAMS)
    t_winner, t_margin = _report("Twist (lab equipment failure cuts kits_per_week 45->27)", twist)
    assert t_winner == "B" and abs(t_margin - 3.85) < 0.05, \
        f"Twist should FLIP the winner to B by ~3.85% per FACILITATOR.md, got {t_winner} {t_margin:.2f}%"

    print("\n--- Probe 5: +/-50% sweep of MA1 (kits_per_week) and MA2 (rate_dual) ---")
    print(f"Base state: {winner}  margin={margin:.2f}%\n")
    for key in FLEX:
        base_val = PARAMS[key]
        for pct, label in ((0.5, "+50%"), (-0.5, "-50%")):
            flexed = dict(PARAMS)
            flexed[key] = base_val * (1 + pct)
            ev = evaluate(flexed)
            state, margin_v = _state(ev)
            flips = state != winner
            cap_breach = margin_v > 20.0
            flag = []
            if flips:
                flag.append("FLIPS/TIES" if state == "TIE" else "FLIPS")
            if cap_breach:
                flag.append("CAP-BREACH(>20%)")
            flagstr = (" <-- " + ", ".join(flag)) if flag else ""
            print(f"  {key:14s} {label:5s}  A={ev['A']*100:7.3f}%  B={ev['B']*100:7.3f}%  "
                  f"state={state:4s}  margin={margin_v:6.2f}%{flagstr}")

    print("\n--- Fine-grained kits_per_week scan (this is the base's real fragility) ---")
    print("  (every value 10..80; the flex probe above only samples +/-50%, which happens to")
    print("   miss most of these regime changes)")
    prev_state = winner
    for k in range(10, 81):
        ev = evaluate({"kits_per_week": float(k)})
        state, m = _state(ev)
        if state != prev_state:
            pct_from_base = 100.0 * (k - 45) / 45.0
            print(f"  kits_per_week={k:3d} ({pct_from_base:+.1f}% from base): "
                  f"state changes {prev_state} -> {state}  (A={ev['A']*100:.3f}%, B={ev['B']*100:.3f}%)")
            prev_state = state

    print("\n--- Fine-grained rate_dual scan (isolating MA2's own fragility) ---")
    prev_state = winner
    for pct in [x / 100 for x in range(-50, 51, 1)]:
        flexed = dict(PARAMS)
        flexed["rate_dual"] = PARAMS["rate_dual"] * (1 + pct)
        ev = evaluate(flexed)
        state, m = _state(ev)
        if state != prev_state:
            print(f"  rate_dual flex {pct*100:+.0f}% (={flexed['rate_dual']*100:.2f}%): "
                  f"state changes {prev_state} -> {state}  (A={ev['A']*100:.3f}%, B={ev['B']*100:.3f}%)")
            prev_state = state
    print("  (scan complete)")
