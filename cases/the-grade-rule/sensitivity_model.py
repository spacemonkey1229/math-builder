"""Sensitivity model for Grade Rule (SPEC section 2 balance test,
case-readiness Tier 2 probe 5).

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py) -- exactly
these public names:

    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            the ASSUMPTION subset probe 5 sweeps
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher wins
    evaluate_twist(params)     same shape, twist applied

This case's primary metric is a COST (dollars per fully-fitting size) -- lower
is better, the opposite of the contract's "higher wins" convention. Same
device as The Fold Line's model: evaluate() returns the NEGATIVE of each
option's cost-per-fit, so "higher wins" still means "cheaper (per fit) wins."

PARAMS is split into SOURCED (case.md Appendix A/C, real cited ASTM/BLS
figures, not in FLEX) and ASSUMED (case.md Appendix D, an MA id in the
comment). FLEX lists only the ASSUMED scalars: tolerance_in (MA1) and the
three labor-time dials (MA2). The five real ASTM body measurements
(bust/waist/hip at 5 sizes) are cited data, not a scenario dial -- P5 sweeps
stated assumptions, not cited measurements, so they stay out of FLEX.

This case DOES have a twist (case.json facilitator.has_twist = true): the
tolerance tightens from 0.5in to 0.42in. evaluate_twist() lets case-readiness's
P4 probe recompute it mechanically.
"""

PARAMS = {
    # --- SOURCED (case.md Appendix A [S1]; not in FLEX) ---
    "base_size": 12,
    "sizes": (8, 10, 12, 14, 16),
    "bust":  {8: 36.25, 10: 37.25, 12: 38.75, 14: 40.375, 16: 42.125},
    "waist": {8: 29.5,  10: 30.5,  12: 32.25, 14: 34.0,   16: 36.0},
    "hip":   {8: 38.5,  10: 39.5,  12: 41.0,  14: 42.5,   16: 44.25},

    # --- SOURCED (case.md Appendix C [S2]; not in FLEX) ---
    "wage_per_hr": 30.05,

    # --- ASSUMED / FLEX (case.md Appendix D) ---
    "tolerance_in": 0.5,       # MA1
    "setup_min": 3.0,          # MA2 -- Uniform Dilation one-time setup
    "per_point_min_a": 0.4,    # MA2 -- Uniform Dilation per-point time
    "per_point_min_b": 1.2,    # MA2 -- Point-Specific per-point time

    # --- twist (not in FLEX; recomputed explicitly by evaluate_twist) ---
    "twist_tolerance_in": 0.42,
}

FLEX = ["tolerance_in", "setup_min", "per_point_min_a", "per_point_min_b"]

LANDMARKS = ("bust", "waist", "hip")


def _dilation_scale_factor(p):
    """Geometric mean of the full-range (min size -> max size) ratio across all
    three landmarks, taken to the 1/n_steps power. Matches RESEARCH_LOG.md."""
    lo, hi = min(p["sizes"]), max(p["sizes"])
    n_steps = (hi - lo) // 2
    ratios = [p[lm][hi] / p[lm][lo] for lm in LANDMARKS]
    avg_ratio = sum(ratios) / len(ratios)
    return avg_ratio ** (1.0 / n_steps)


def _predictions(p):
    s = _dilation_scale_factor(p)
    base = p["base_size"]
    out = {}
    for sz in p["sizes"]:
        n = (sz - base) // 2
        factor = s ** n
        out[sz] = {lm: p[lm][base] * factor for lm in LANDMARKS}
    return out


def _fits_a(p, tolerance):
    preds = _predictions(p)
    n_fit = 0
    for sz in p["sizes"]:
        ok = all(abs(preds[sz][lm] - p[lm][sz]) <= tolerance for lm in LANDMARKS)
        if ok:
            n_fit += 1
    return n_fit


def _costs(p):
    n_point_grades = (len(p["sizes"]) - 1) * len(LANDMARKS)
    wage_per_min = p["wage_per_hr"] / 60.0
    time_a = p["setup_min"] + n_point_grades * p["per_point_min_a"]
    time_b = n_point_grades * p["per_point_min_b"]
    return time_a * wage_per_min, time_b * wage_per_min


def evaluate(params=None):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Metric = NEGATIVE
    dollars-per-fully-fitting-size (see module docstring)."""
    p = dict(PARAMS)
    p.update(params or {})
    fits_a = _fits_a(p, p["tolerance_in"])
    fits_b = len(p["sizes"])  # Point-Specific always matches real data exactly
    cost_a, cost_b = _costs(p)
    cpf_a = cost_a / fits_a if fits_a else float("inf")
    cpf_b = cost_b / fits_b
    return {"A": -cpf_a, "B": -cpf_b}


def evaluate_twist(params=None):
    """The tolerance-tightening twist: MA1 tightens from 0.5in to
    twist_tolerance_in (0.42in) -- case.json balance.twist_effect /
    FACILITATOR.md's Twist section."""
    p = dict(PARAMS)
    p.update(params or {})
    fits_a = _fits_a(p, p["twist_tolerance_in"])
    fits_b = len(p["sizes"])
    cost_a, cost_b = _costs(p)
    cpf_a = cost_a / fits_a if fits_a else float("inf")
    cpf_b = cost_b / fits_b
    return {"A": -cpf_a, "B": -cpf_b}


def _detail(params=None, twist=False):
    p = dict(PARAMS)
    p.update(params or {})
    tol = p["twist_tolerance_in"] if twist else p["tolerance_in"]
    fits_a = _fits_a(p, tol)
    fits_b = len(p["sizes"])
    cost_a, cost_b = _costs(p)
    cpf_a = cost_a / fits_a if fits_a else float("inf")
    cpf_b = cost_b / fits_b
    return {"fits_a": fits_a, "fits_b": fits_b, "cost_a": cost_a, "cost_b": cost_b,
            "cpf_a": cpf_a, "cpf_b": cpf_b}


def _report(label, d):
    winner = "A" if d["cpf_a"] < d["cpf_b"] else "B"
    lo, hi = min(d["cpf_a"], d["cpf_b"]), max(d["cpf_a"], d["cpf_b"])
    margin = 0.0 if lo == 0 else 100.0 * (hi - lo) / lo
    print(f"{label}: A=${d['cpf_a']:.4f}/fit (fits={d['fits_a']})  "
          f"B=${d['cpf_b']:.4f}/fit (fits={d['fits_b']})  winner={winner}  margin={margin:.2f}%")
    return winner, margin


if __name__ == "__main__":
    base = _detail()
    winner, margin = _report("Base", base)
    assert winner == "A", f"Base model drifted from case.json's disclosed base (A wins): got {winner}"
    assert abs(margin - 10.77) < 0.5, f"Base margin drifted from disclosed 10.77%: got {margin:.2f}%"

    twist = _detail(twist=True)
    twist_winner, twist_margin = _report("Twist (tolerance -> 0.42in)", twist)
    assert twist_winner == "B", f"Twist expected to flip to B: got {twist_winner}"
    assert abs(twist_margin - 35.4) < 1.0, f"Twist margin drifted from disclosed ~35.4%: got {twist_margin:.2f}%"

    print("\n--- Probe 5: +/-50% sweep of FLEX[] (the case's stated assumptions) ---")
    base_winner = winner
    for key in FLEX:
        base_val = PARAMS[key]
        for pct, label in ((0.5, "+50%"), (-0.5, "-50%")):
            flexed = dict(PARAMS)
            flexed[key] = base_val * (1 + pct)
            d = _detail(flexed)
            w = "A" if d["cpf_a"] < d["cpf_b"] else "B"
            lo, hi = min(d["cpf_a"], d["cpf_b"]), max(d["cpf_a"], d["cpf_b"])
            m = 0.0 if lo == 0 else 100.0 * (hi - lo) / lo
            flips = w != base_winner
            cap_breach = m > 20.0
            flag = []
            if flips:
                flag.append("FLIPS")
            if cap_breach:
                flag.append("CAP-BREACH(>20%)")
            flagstr = (" <-- " + ", ".join(flag)) if flag else ""
            print(f"  {key:18s} {label:5s}  A=${d['cpf_a']:.4f} (fits={d['fits_a']})  "
                  f"B=${d['cpf_b']:.4f} (fits={d['fits_b']})  winner={w}  margin={m:7.2f}%{flagstr}")
