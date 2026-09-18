"""Sensitivity model for The Fold Line (SPEC section 2 balance test,
case-readiness Tier 2 probe 5).

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py) -- exactly
these public names:

    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            the ASSUMPTION subset probe 5 sweeps
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher wins

This case's primary metric is a COST (dollars per panel) -- lower is better, the
opposite of the contract's "higher wins" convention. To stay contract-compliant
without inverting the case's own meaning, evaluate() returns the NEGATIVE of each
option's total cost: A's metric = -total_cost_A, B's metric = -total_cost_B. The
option with the smaller cost has the larger (less negative) metric, so "higher
wins" still means "cheaper wins," exactly matching case.json's balance object
(Fold Cut / A wins at the base case).

PARAMS is split into SOURCED (a citation id in the comment; case.md Appendix
B/C/G, real cited figures) and ASSUMED (case.md Appendix E, an MA id in the
comment). FLEX lists only the ASSUMED scalars that are genuine dials the case
chose -- t_fold_min (MA2's labor-time base, which also fixes t_open_min at
exactly double) and the two marker-efficiency point-values (MA3) -- per
case-readiness's default-scope rule: P5 sweeps stated assumptions, not cited
measurements. width_in/length_in (MA1) are deliberately left OUT of FLEX: MA1
scales both options' fabric use by the same factor and is not the kind of
scenario dial this case asks a Hero to challenge (see case.json's
modeling_assumptions, MA1 flippable: false) -- flexing it would mostly just
rescale both totals together rather than test a real fragility.

This case DOES have a twist (case.json facilitator.has_twist = true): the
fabric-price twist raises price_per_yd from 3.70 to 6.50. `evaluate_twist()`
is defined to let case-readiness's P4 probe recompute it mechanically.
"""

PARAMS = {
    # --- SOURCED (case.md Appendix B/C/G; not in FLEX) ---
    "seam_allowance_in": 0.625,     # Appendix A/G [S1] -- 5/8in standard seam allowance
    "bolt_width_in": 44.0,          # Appendix B [S2] -- standard 44/45in bolt
    "price_per_yd": 3.70,           # Appendix B [S4] -- real, live fabric price
    "wage_per_hr": 17.61,           # Appendix C [S5] -- real BLS median wage

    # --- panel geometry (MA1, case.md Appendix E; NOT in FLEX -- see docstring) ---
    "finished_width_in": 8.375,     # MA1
    "finished_length_in": 23.25,    # MA1
    "hem_allowance_in": 1.5,        # MA1

    # --- ASSUMED / FLEX (case.md Appendix E) ---
    "t_fold_min": 0.8,              # MA2 -- Fold Cut marking+cutting minutes per panel
    "eff_fold": 0.78,               # MA3 -- Fold Cut marker efficiency
    "eff_open": 0.88,               # MA3 -- Open Cut marker efficiency

    # --- twist (not in FLEX; recomputed explicitly by evaluate_twist) ---
    "twist_price_per_yd": 6.50,
}

FLEX = ["t_fold_min", "eff_fold", "eff_open"]


def _totals(p):
    """Return (total_cost_fold, total_cost_open) in USD per panel."""
    cutting_width = p["finished_width_in"] + p["seam_allowance_in"]
    cutting_length = (p["finished_length_in"] + p["hem_allowance_in"]
                       + p["seam_allowance_in"])
    area_in2 = cutting_width * cutting_length

    fabric_in2_fold = area_in2 / p["eff_fold"]
    fabric_in2_open = area_in2 / p["eff_open"]

    fabric_yd_fold = (fabric_in2_fold / p["bolt_width_in"]) / 36.0
    fabric_yd_open = (fabric_in2_open / p["bolt_width_in"]) / 36.0

    price = p.get("_price_override", p["price_per_yd"])
    fabric_cost_fold = fabric_yd_fold * price
    fabric_cost_open = fabric_yd_open * price

    t_fold = p["t_fold_min"]
    t_open = 2.0 * t_fold  # MA2's stated fixed 2:1 ratio

    labor_cost_fold = (t_fold / 60.0) * p["wage_per_hr"]
    labor_cost_open = (t_open / 60.0) * p["wage_per_hr"]

    total_fold = fabric_cost_fold + labor_cost_fold
    total_open = fabric_cost_open + labor_cost_open
    return total_fold, total_open


def evaluate(params):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. A = Fold Cut, B = Open Cut.
    Metric is NEGATIVE cost (see module docstring) -- less negative/higher = cheaper = wins.
    """
    p = dict(PARAMS)
    p.update(params or {})
    total_fold, total_open = _totals(p)
    return {"A": -total_fold, "B": -total_open}


def evaluate_twist(params=None):
    """The fabric-price twist: price_per_yd rises from 3.70 to 6.50 (FACILITATOR.md).
    Everything else held at its base value unless the caller overrides it."""
    p = dict(PARAMS)
    p.update(params or {})
    p["_price_override"] = p.get("twist_price_per_yd", 6.50)
    total_fold, total_open = _totals(p)
    return {"A": -total_fold, "B": -total_open}


def _report(label, ev):
    hi_key = max(ev, key=ev.get)
    lo_key = min(ev, key=ev.get)
    cost = {"A": -ev["A"], "B": -ev["B"]}
    margin = 0.0 if cost[hi_key] == 0 else 100.0 * (cost[lo_key] - cost[hi_key]) / cost[hi_key]
    # hi_key is the WINNER (higher metric = lower cost); margin = how much more the loser costs
    winner = hi_key
    loser = lo_key
    margin = 0.0 if cost[winner] == 0 else 100.0 * (cost[loser] - cost[winner]) / cost[winner]
    print(f"{label}: A(Fold)=${cost['A']:.4f}  B(Open)=${cost['B']:.4f}  "
          f"winner={winner}  margin={margin:.2f}%")
    return winner, margin


if __name__ == "__main__":
    base = evaluate(PARAMS)
    winner, margin = _report("Base", base)
    assert winner == "A", f"Base model drifted from case.json's disclosed base (A/Fold wins): got {winner}"
    assert abs(margin - 17.1) < 1.0, f"Base margin drifted from case.json's disclosed 17.1%: got {margin:.2f}%"

    twist = evaluate_twist()
    twist_winner, twist_margin = _report("Twist (fabric price -> $6.50/yd)", twist)
    assert twist_winner == "A", f"Twist unexpectedly flips the winner: got {twist_winner}"
    assert abs(twist_margin - 6.8) < 1.5, f"Twist margin drifted from FACILITATOR.md's disclosed ~6.8%: got {twist_margin:.2f}%"

    print("\n--- Probe 5: +/-50% sweep of FLEX[] (the case's stated assumptions) ---")
    for key in FLEX:
        base_val = PARAMS[key]
        for pct, label in ((0.5, "+50%"), (-0.5, "-50%")):
            flexed = dict(PARAMS)
            flexed[key] = base_val * (1 + pct)
            # keep efficiencies in (0, 1]
            if key.startswith("eff_"):
                flexed[key] = min(flexed[key], 0.999)
            ev = evaluate(flexed)
            hi_key = max(ev, key=ev.get)
            cost = {"A": -ev["A"], "B": -ev["B"]}
            lo_key = min(cost, key=cost.get)  # cheaper option
            m = 0.0 if cost[lo_key] == 0 else 100.0 * (cost[hi_key if hi_key != lo_key else lo_key] - cost[lo_key]) / cost[lo_key]
            # recompute margin cleanly: winner = cheaper option
            winner_flexed = min(cost, key=cost.get)
            loser_flexed = max(cost, key=cost.get)
            m = 0.0 if cost[winner_flexed] == 0 else 100.0 * (cost[loser_flexed] - cost[winner_flexed]) / cost[winner_flexed]
            flips = winner_flexed != winner
            cap_breach = m > 20.0
            flag = []
            if flips:
                flag.append("FLIPS")
            if cap_breach:
                flag.append("CAP-BREACH(>20%)")
            flagstr = (" <-- " + ", ".join(flag)) if flag else ""
            print(f"  {key:12s} {label:5s}  A=${cost['A']:.4f}  B=${cost['B']:.4f}  "
                  f"winner={winner_flexed}  margin={m:6.2f}%{flagstr}")
