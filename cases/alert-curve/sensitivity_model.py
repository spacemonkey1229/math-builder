#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Alert Curve.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic.

CONTRACT — two public names:

    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

The case's SPEC section 2 primary metric (case.json.balance.margin_basis) is
confirmed real incidents per false escalation, computed separately for the
Threshold Trip policy (Option A) and the Curve Check policy (Option B) from
Appendix D's 14-row historical log (MA6), classifying each row under each
policy's own rule: Threshold Trip escalates when the row's raw alert count
crosses Appendix C's threshold (MA4); Curve Check escalates when the row's
sign of dA/dt at confirmation is positive. Both rules are already "higher is
better" ratios, so evaluate() returns them unnegated.

Each row's raw alert count (MA6) is a genuine per-row authorial estimate and
is flexed here. Appendix C's threshold (MA4) is also flexed -- it is the
figure the case's own Modeling Assumptions table calls "the single most
flip-capable figure in the case." Each row's sign-of-dA/dt and
confirmed-incident outcome (also MA6) are categorical labels, not numeric
dials -- there is no principled "+/-50%" of a Yes/No outcome, so they are held
fixed here and are not in FLEX, the same way fret-board's sensitivity model
excludes MA2 (fret count) as a non-time-cost dial. A different LOG (different
row labels entirely) is a different case, not a flex of this one -- that
question belongs to case-write, not to this probe.

Verified against case.json.balance.margin_note:
    base    A (Threshold Trip) = 1.75  ·  B (Curve Check) = 2.0  ·  margin 14.3%
    (winner: B, matching case.json.margin_pct = 14.3 exactly)
"""

# --- Appendix D / MA6: raw alert count, past interval 1-14 (alerts/hour) ----
COUNTS = [610, 635, 730, 515, 410, 555, 675, 695, 545, 715, 585, 425, 655, 460]
# --- Appendix D / MA6: sign of dA/dt at confirmation, same 14 rows ----------
SIGN = ['+', '+', '+', '-', '+', '+', '+', '+', '-', '+', '+', '+', '+', '+']
# --- Appendix D / MA6: later confirmed a real incident?, same 14 rows -------
CONFIRMED = [True, True, True, False, True, False, True, True, False, True,
             False, False, True, False]

PARAMS = {"threshold": 500.0}
for _i, _c in enumerate(COUNTS, start=1):
    PARAMS[f"count_{_i}"] = float(_c)

# Probe 5 flexes THESE and only these: Appendix C's threshold (MA4) and each
# row's raw alert count (MA6) -- the numeric dials the case's own Modeling
# Assumptions table states and flags High sensitivity. SIGN[] and CONFIRMED[]
# are categorical row labels (also MA6), not numeric dials, so they are held
# fixed; see the docstring. Run with --flex-all to sweep the threshold-only
# subset differently if needed -- there is nothing else numeric to add.
FLEX = ["threshold"] + [f"count_{i}" for i in range(1, len(COUNTS) + 1)]


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    threshold = p["threshold"]
    counts = [p[f"count_{i}"] for i in range(1, len(COUNTS) + 1)]

    tt_true = tt_false = cc_true = cc_false = 0
    for count, sign, confirmed in zip(counts, SIGN, CONFIRMED):
        crossed = count >= threshold
        if crossed:
            if confirmed:
                tt_true += 1
            else:
                tt_false += 1
        if sign == '+':
            if confirmed:
                cc_true += 1
            else:
                cc_false += 1

    ratio_tt = (tt_true / tt_false) if tt_false else float('inf')
    ratio_cc = (cc_true / cc_false) if cc_false else float('inf')
    return {"A": ratio_tt, "B": ratio_cc}


if __name__ == '__main__':
    base = evaluate({})
    win = max(base, key=base.get)
    lo = min(base, key=base.get)
    margin = 100.0 * (base[win] - base[lo]) / (base[lo] or 1)
    print("base ratios ", {k: round(v, 3) for k, v in base.items()},
          "winner", win, "margin %.1f%%" % margin)
