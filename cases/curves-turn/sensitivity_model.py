"""Sensitivity model for The Curve's Turn (SPEC §2 balance test, case-readiness Tier 2 probe 5).

Every dial below is tagged SOURCED (cited in case.md Appendix E, citation id in the comment),
DERIVED (computed here from a SOURCED series, and published in case.md so a Hero can reproduce it),
or ASSUMED (stated in the open in case.md Appendix F, Modeling Assumptions, id in the comment).

FLEX lists the ASSUMED subset that is an *estimate of an uncertain real quantity*.  Probe 5 sweeps
only those, per case-readiness's own rule that cited measurements are stress-tested by probe 6
(data decay), not probe 5.

TWO DIALS ARE DELIBERATELY EXCLUDED FROM FLEX, and the reason is stated here so nobody has to
reverse-engineer it:

  * `board_closure_level_per_100k` (MA2).  This is not an estimate of anything.  It is the written
    trigger that *defines* Option B.  Halving it does not ask "what if we were wrong about the
    world", it asks "what if Option B were a different option" -- the same argument case-readiness
    itself makes for not halving a cited measurement.  The sweep is still run and still reported:
    see `disclosed_threshold_sweep()` below and the QA report.  At half the stated level the
    Tripwire fires in the same week as the Early Brake and B wins by exactly the screening removal
    rate; at 1.5x the stated level the model's forecast never reaches it inside the horizon and the
    Tripwire never fires at all.  Both are disclosed, neither is hidden.
  * `horizon_last_week` and `closure_len_weeks` (MA3, MA4) are integer week indices.  A +/-50% flex
    produces fractional weeks the week-indexed model cannot evaluate, and a 3-week or 9-week
    horizon is a different board rule, not a different estimate.

The published cubic coefficients are the ROUNDED four-decimal values printed in case.md Appendix A
and Appendix B.  The model uses exactly those, not the full-precision fit, so that every number
this file produces is reproducible by hand from the case document alone.
"""

# ---------------------------------------------------------------- parameters --
PARAMS = {
    # --- SOURCED ---
    "county_population": 163774.0,        # S2/S3 -- CDC, county_population (2019 Census estimate)

    # --- DERIVED (ordinary least squares on the S1 series; published in case.md) ---
    # Previous wave P(t), t = weeks from the week ending 2021-06-02 (Appendix A)
    "p3": -0.3348, "p2": 8.9975, "p1": -42.0177, "p0": 38.2994,
    # Current wave D(t), t = weeks from the week ending 2021-10-06 (Appendix B)
    "d3": 0.2174, "d2": -1.8006, "d1": 25.3255, "d0": 247.9597,
    # g = D'(11) / D(11), the model's own relative rate of change at the decision week.
    # Asserted against the coefficients above at import time -- see _check_g().
    "planning_growth_rate_g": 0.108070,

    # --- ASSUMED (case.md Appendix F) ---
    "board_closure_level_per_100k": 500.0,   # MA2 -- the Tripwire's written trigger, cases/100k/week
    "closure_len_weeks": 2,                  # MA3 -- the one closure the board authorised, in weeks
    "horizon_last_week": 17,                 # MA4 -- horizon runs t = 12..17 (six weeks)
    "in_school_coeff_k": 0.5,                # MA6 -- in-school transmissions per 1,000 students in an
                                             #        open week at a community rate of 100/100k/week
    "screening_removal_frac": 0.10,          # MA7 -- share of in-school transmission twice-weekly
                                             #        consent-based screening removes in an open week
}

FLEX = ["in_school_coeff_k", "screening_removal_frac", "planning_growth_rate_g"]

DECISION_WEEK = 11          # t index of the decision week (week ending 2021-12-22) in Appendix B
HORIZON_FIRST_WEEK = 12     # first week the board scores

# The reported weekly counts for the six horizon weeks.  REAL, from the same CDC series as the
# rest of the case (S1) -- these are the weeks the case document deliberately does NOT contain,
# because revealing them is the Twist.  They are never used by evaluate(); only by the twist.
TWIST_ACTUAL_WEEKLY_CASES = {12: 896, 13: 1732, 14: 3612, 15: 3220, 16: 2307, 17: 1325}


# ------------------------------------------------------------------ helpers --
def _poly(c3, c2, c1, c0, t):
    return c3 * t ** 3 + c2 * t ** 2 + c1 * t + c0


def _dpoly(c3, c2, c1, t):
    """Derivative of a cubic by the power rule -- the same three lines a Hero writes in D1."""
    return 3 * c3 * t ** 2 + 2 * c2 * t + c1


def current_model(p, t):
    return _poly(p["d3"], p["d2"], p["d1"], p["d0"], t)


def current_model_prime(p, t):
    return _dpoly(p["d3"], p["d2"], p["d1"], t)


def current_model_second(p, t):
    return 6 * p["d3"] * t + 2 * p["d2"]


def previous_model(p, t):
    return _poly(p["p3"], p["p2"], p["p1"], p["p0"], t)


def previous_model_prime(p, t):
    return _dpoly(p["p3"], p["p2"], p["p1"], t)


def rate_per_100k(p, t):
    """Step 1 of Appendix D."""
    return current_model(p, t) / p["county_population"] * 100000.0


def chain_multiplier(p, t):
    """Step 3 of Appendix D: finite geometric series ((1+g)^(H-t+1) - 1) / g."""
    g = p["planning_growth_rate_g"]
    H = p["horizon_last_week"]
    return ((1 + g) ** (H - t + 1) - 1) / g


def weighted_transmissions(p, t):
    """Step 4 of Appendix D, in chain-weighted transmissions per 1,000 students."""
    return p["in_school_coeff_k"] * rate_per_100k(p, t) / 100.0 * chain_multiplier(p, t)


def _horizon(p):
    return list(range(HORIZON_FIRST_WEEK, int(p["horizon_last_week"]) + 1))


def tripwire_week(p, rates=None):
    """First horizon week whose reported rate is at or above the board's written level.
    Returns None if the level is never reached inside the horizon -- a real state, not an error."""
    wk = _horizon(p)
    rates = rates or {t: rate_per_100k(p, t) for t in wk}
    return next((t for t in wk if rates[t] >= p["board_closure_level_per_100k"]), None)


# ------------------------------------------------------------------- core ----
def decision_table(p, rates=None, weights=None):
    """Step 5 of Appendix D.  Returns the number each plan LEAVES BEHIND -- chain-weighted
    in-school transmissions per 1,000 students over the horizon.  LOWER IS BETTER.

    Fully disclosed, single-pass: every line here is written out in case.md Appendix D, and a Hero
    can reproduce the whole table from Appendix B, C and D with a spreadsheet and no extra
    judgement call.  There is no hidden blend and no undisclosed constant.
    """
    wk = _horizon(p)
    n = int(p["closure_len_weeks"])
    rates = rates if rates is not None else {t: rate_per_100k(p, t) for t in wk}
    weights = weights if weights is not None else {t: chain_multiplier(p, t) for t in wk}
    X = {t: p["in_school_coeff_k"] * rates[t] / 100.0 * weights[t] for t in wk}
    total = sum(X.values())

    brake_weeks = [t for t in range(HORIZON_FIRST_WEEK, HORIZON_FIRST_WEEK + n) if t in X]
    brake_left = total - sum(X[t] for t in brake_weeks)

    tb = tripwire_week(p, rates)
    trip_weeks = [t for t in range(tb, tb + n) if t in X] if tb is not None else []
    e = p["screening_removal_frac"]
    trip_prevented = sum(X[t] for t in trip_weeks) + e * sum(X[t] for t in wk if t not in trip_weeks)
    trip_left = total - trip_prevented

    return {"A_left": brake_left, "B_left": trip_left, "total_no_action": total,
            "tripwire_week": tb, "brake_weeks": brake_weeks, "tripwire_weeks": trip_weeks,
            "X": X, "rates": rates, "weights": weights}


def _ceiling_transform(a_cost, b_cost):
    """CONTRACT: evaluate() returns {"A": metric, "B": metric} with HIGHER meaning better.
    This case's metric is transmissions LEFT, which is lower-is-better, and case.md states the
    margin as (worse - better) / worse.  Subtracting each cost from twice the worse cost keeps
    both values positive AND collapses the framework's generic (max-min)/min formula back to
    exactly (worse-better)/worse -- so probe 5 reports the case's own margin, not a different one.
    """
    ceiling = 2 * max(a_cost, b_cost)
    return {"A": ceiling - a_cost, "B": ceiling - b_cost}


def evaluate(p):
    d = decision_table(p)
    return _ceiling_transform(d["A_left"], d["B_left"])


def twist_decision_table(p):
    """The Twist (FACILITATOR.md): reveal what the county's reported series actually did in the six
    horizon weeks.  Nothing here is invented -- TWIST_ACTUAL_WEEKLY_CASES is the same real CDC
    series (S1) as Appendix A and B, continued past the decision week.

    Two things change together, and both are read off the real data rather than assumed:
      1. the rates become the observed rates, not the model's forecast;
      2. the chain multiplier becomes the REALISED one -- a transmission prevented in week t is
         credited with the chain the county actually went on to have, week-specific ratios and all,
         instead of a single planning growth rate.  After the real peak those ratios fall below 1,
         so late prevention is credited with almost nothing, exactly as it should be.
    """
    wk = _horizon(p)
    a = TWIST_ACTUAL_WEEKLY_CASES
    rates = {t: a[t] / p["county_population"] * 100000.0 for t in wk}
    ratio = {t: a[t + 1] / a[t] for t in wk[:-1]}
    weights = {}
    for t in wk:
        s, prod = 1.0, 1.0
        for u in range(t, wk[-1]):
            prod *= ratio[u]
            s += prod
        weights[t] = s
    return decision_table(p, rates=rates, weights=weights)


def evaluate_twist(p):
    d = twist_decision_table(p)
    return _ceiling_transform(d["A_left"], d["B_left"])


def disclosed_threshold_sweep(p):
    """MA2 is excluded from FLEX for the reason given in the module docstring.  It is swept here
    anyway, and the result is written into QA_REPORT.md.  Nothing about this dial is hidden."""
    out = []
    for mult in (0.5, 1.0, 1.5):
        q = dict(p)
        q["board_closure_level_per_100k"] = p["board_closure_level_per_100k"] * mult
        d = decision_table(q)
        lo, hi = min(d["A_left"], d["B_left"]), max(d["A_left"], d["B_left"])
        out.append({"multiplier": mult, "level": q["board_closure_level_per_100k"],
                    "tripwire_week": d["tripwire_week"],
                    "A_left": round(d["A_left"], 4), "B_left": round(d["B_left"], 4),
                    "winner": "A" if d["A_left"] < d["B_left"] else "B",
                    "margin_pct": round((hi - lo) / hi * 100, 2)})
    return out


def _check_g(p):
    """g is DERIVED, not stated: it must equal D'(11)/D(11) from the published coefficients.
    If someone edits a coefficient and forgets g, this fires instead of drifting silently."""
    want = current_model_prime(p, DECISION_WEEK) / current_model(p, DECISION_WEEK)
    assert abs(want - p["planning_growth_rate_g"]) < 5e-6, \
        f"planning_growth_rate_g drifted from the published cubic: {want:.6f} vs {p['planning_growth_rate_g']}"
    return want


_check_g(PARAMS)


# ------------------------------------------------------------------ report ---
if __name__ == "__main__":
    import math

    p = PARAMS
    print(f"D(t)  = {p['d3']}t^3 + {p['d2']}t^2 + {p['d1']}t + {p['d0']}")
    print(f"D'(t) = {3*p['d3']}t^2 + {2*p['d2']}t + {p['d1']}")
    print(f"D''(t)= {6*p['d3']}t + {2*p['d2']}   ->  zero at t = {-2*p['d2']/(6*p['d3']):.4f}")
    print(f"D(11) = {current_model(p,11):.4f}   D'(11) = {current_model_prime(p,11):.4f}   "
          f"g = {_check_g(p):.6f}")

    d = decision_table(p)
    print("\n  t   D(t)      R(t)      w(t)      X(t)")
    for t in _horizon(p):
        print(f" {t:2d} {current_model(p,t):9.2f} {d['rates'][t]:9.2f} "
              f"{d['weights'][t]:9.4f} {d['X'][t]:9.4f}")
    print(f"\n  no action              : {d['total_no_action']:.4f}")
    print(f"  A Early Brake (wk {d['brake_weeks']}) : {d['A_left']:.4f}")
    print(f"  B Tripwire    (wk {d['tripwire_weeks']}) : {d['B_left']:.4f}   fires at t={d['tripwire_week']}")
    lo, hi = min(d["A_left"], d["B_left"]), max(d["A_left"], d["B_left"])
    win = "A" if d["A_left"] < d["B_left"] else "B"
    print(f"  winner {win}, margin {(hi-lo)/hi*100:.2f}%")

    t = twist_decision_table(p)
    lo2, hi2 = min(t["A_left"], t["B_left"]), max(t["A_left"], t["B_left"])
    win2 = "A" if t["A_left"] < t["B_left"] else "B"
    print(f"\n  TWIST  no action {t['total_no_action']:.4f}  A {t['A_left']:.4f}  B {t['B_left']:.4f}"
          f"  fires at t={t['tripwire_week']}  winner {win2}, margin {(hi2-lo2)/hi2*100:.2f}%")

    print("\n  disclosed threshold sweep (MA2, excluded from FLEX by design):")
    for row in disclosed_threshold_sweep(p):
        print("   ", row)

    ev = evaluate(p)
    lo3 = min(ev, key=ev.get); hi3 = max(ev, key=ev.get)
    ev_margin = (ev[hi3] - ev[lo3]) / ev[lo3] * 100
    raw_margin = (hi - lo) / hi * 100
    assert hi3 == win and abs(ev_margin - raw_margin) < 0.05, \
        f"evaluate() contract transform drifted from decision_table(): {ev} margin={ev_margin:.2f}"
    print(f"\n  evaluate() contract check OK: winner={hi3}, margin={ev_margin:.2f}% "
          f"(matches the raw decision-table margin)")

    # D3 / D5 answers on the previous wave, for the guide notes
    a3, a2, a1 = 3*p["p3"], 2*p["p2"], p["p1"]
    disc = math.sqrt(a2*a2 - 4*a3*a1)
    roots = sorted([(-a2 + disc)/(2*a3), (-a2 - disc)/(2*a3)])
    print("\n  previous wave critical points:")
    for r in roots:
        kind = "local MIN" if (6*p["p3"]*r + 2*p["p2"]) > 0 else "local MAX"
        print(f"    t = {r:.4f}   P(t) = {previous_model(p,r):8.2f}   {kind}")
    print(f"    inflection at t = {-2*p['p2']/(6*p['p3']):.4f}")
