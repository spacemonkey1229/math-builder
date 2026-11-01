"""Sensitivity model for Constellation Bid (SPEC section 2 balance test,
case-readiness Tier 2 probe 5).

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py) -- exactly
these public names:

    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            the ASSUMPTION subset probe 5 sweeps
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher wins
    evaluate_twist(params)     same shape, twist applied

Primary metric is satellites-correctly-placed-per-dollar for each option (higher
wins, contract-compliant with no inversion needed).

PARAMS is split into SOURCED (case.md Appendix A/D/E, real cited figures) and
ASSUMED (case.md Appendix F, an MA id in the comment). FLEX lists only the
ASSUMED scalars that are genuine scenario dials the case chose: altitude_km
(MA1), wet_mass_kg (MA3), and propellant_allowance_kg (MA4) -- per
case-readiness's default-scope rule, P5 sweeps stated assumptions, not cited
measurements (rideshare/Electron prices, Isp, are all SOURCED and swept
instead by P6's data-decay check). MA2 (the choice to model a RAAN change with
the single-burn combined plane-change formula) is a MODELING convention, not a
numeric dial, and is not something a +/-50% flex applies to meaningfully.

This case DOES have a twist (case.json facilitator.has_twist = true): the
rideshare price rises from 7,000 to 9,000 USD/kg. evaluate_twist() lets
case-readiness's P4 probe recompute it mechanically.
"""

import math

PARAMS = {
    # --- SOURCED (case.md Appendix D/E; not in FLEX) ---
    "isp_s": 2150.0,                 # Appendix D [S3] -- real BIT-3 Isp
    "g0_ms2": 9.80665,               # Appendix D -- standard physical constant
    "rideshare_base_usd": 350000.0,  # Appendix E [S4]
    "rideshare_base_kg": 50.0,       # Appendix E [S4]
    "rideshare_rate_usd_per_kg": 7000.0,  # Appendix E [S4]
    "electron_price_usd": 7500000.0,  # Appendix E [S5]

    # --- fixed constellation structure (not FLEX -- structural, not a scenario dial) ---
    "n_satellites": 60,
    "n_planes": 6,
    "sats_per_plane": 10,
    "mu_km3s2": 398600.4418,         # standard gravitational parameter

    # --- ASSUMED / FLEX (case.md Appendix F) ---
    "altitude_km": 550.0,            # MA1
    "wet_mass_kg": 15.0,             # MA3
    "propellant_allowance_kg": 4.0,  # MA4

    # --- twist (not in FLEX; recomputed explicitly by evaluate_twist) ---
    "twist_rideshare_rate_usd_per_kg": 9000.0,
}

FLEX = ["altitude_km", "wet_mass_kg", "propellant_allowance_kg"]

# Minimum angular separation (degrees) and satellite count per group, from Appendix B.
GROUPS = [(0.0, 10), (60.0, 10), (120.0, 10), (180.0, 10), (120.0, 10), (60.0, 10)]


def _orbital_speed_ms(p):
    r_km = 6371.0 + p["altitude_km"]
    v_kms = math.sqrt(p["mu_km3s2"] / r_km)
    return v_kms * 1000.0


def _propellant_per_ms(p):
    return p["wet_mass_kg"] / (p["isp_s"] * p["g0_ms2"])


def _option_a(p, rideshare_rate=None):
    """Return (correctly_placed, total_cost_usd) for the Consolidated Launch."""
    v = _orbital_speed_ms(p)
    prop_per_ms = _propellant_per_ms(p)
    placed = 0
    for theta_deg, n in GROUPS:
        dv = 2.0 * v * math.sin(math.radians(theta_deg / 2.0))
        prop_needed = dv * prop_per_ms
        if prop_needed <= p["propellant_allowance_kg"]:
            placed += n
    total_mass = p["n_satellites"] * p["wet_mass_kg"]
    rate = p["rideshare_rate_usd_per_kg"] if rideshare_rate is None else rideshare_rate
    cost = p["rideshare_base_usd"] + rate * max(0.0, total_mass - p["rideshare_base_kg"])
    return placed, cost


def _option_b(p):
    """Return (correctly_placed, total_cost_usd) for the Distributed Launch."""
    placed = p["n_satellites"]  # every dedicated launch succeeds by construction
    cost = p["n_planes"] * p["electron_price_usd"]
    return placed, cost


def evaluate(params=None):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Metric = sats correctly
    placed per dollar for each option. Exactly two keys, per the probe-5 contract
    (skills/case-readiness/scripts/example_sensitivity_model.py) -- extra debug
    keys break the generic winner-detection logic in tier2_probes.py, which reads
    every key in the returned dict as a candidate option."""
    p = dict(PARAMS)
    p.update(params or {})
    placed_a, cost_a = _option_a(p)
    placed_b, cost_b = _option_b(p)
    return {"A": placed_a / cost_a, "B": placed_b / cost_b}


def evaluate_twist(params=None):
    """The rideshare-price twist: rate rises to twist_rideshare_rate_usd_per_kg
    (case.json balance.twist_effect / FACILITATOR.md's Twist section)."""
    p = dict(PARAMS)
    p.update(params or {})
    placed_a, cost_a = _option_a(p, rideshare_rate=p["twist_rideshare_rate_usd_per_kg"])
    placed_b, cost_b = _option_b(p)
    return {"A": placed_a / cost_a, "B": placed_b / cost_b}


def evaluate_detail(params=None, twist=False):
    """Non-contract helper (debug/report use only): returns the full detail
    dict including placed counts and raw costs, for _report()/RESEARCH_LOG-style
    printing. Never passed to tier2_probes.py."""
    p = dict(PARAMS)
    p.update(params or {})
    if twist:
        placed_a, cost_a = _option_a(p, rideshare_rate=p["twist_rideshare_rate_usd_per_kg"])
    else:
        placed_a, cost_a = _option_a(p)
    placed_b, cost_b = _option_b(p)
    return {"A": placed_a / cost_a, "B": placed_b / cost_b,
            "placed_a": placed_a, "cost_a": cost_a,
            "placed_b": placed_b, "cost_b": cost_b}


def _report(label, ev):
    winner = "A" if ev["A"] > ev["B"] else ("B" if ev["B"] > ev["A"] else "TIE")
    lo, hi = min(ev["A"], ev["B"]), max(ev["A"], ev["B"])
    margin = 0.0 if lo == 0 else 100.0 * (hi - lo) / lo
    print(f"{label}: A={ev['A']:.4e} (placed={ev['placed_a']}, cost=${ev['cost_a']:,.0f})  "
          f"B={ev['B']:.4e} (placed={ev['placed_b']}, cost=${ev['cost_b']:,.0f})  "
          f"winner={winner}  margin={margin:.2f}%")
    return winner, margin


if __name__ == "__main__":
    base = evaluate_detail()
    winner, margin = _report("Base", base)
    assert winner == "A", f"Base model drifted from case.json's disclosed base (A wins): got {winner}"
    assert abs(margin - 19.05) < 0.5, f"Base margin drifted from case.json's disclosed 19.05%: got {margin:.2f}%"

    twist = evaluate_detail(twist=True)
    twist_winner, twist_margin = _report("Twist (rideshare -> $9,000/kg)", twist)
    assert twist_winner == "B", f"Twist expected to flip to B: got {twist_winner}"
    assert abs(twist_margin - 6.67) < 0.5, f"Twist margin drifted from disclosed ~6.67%: got {twist_margin:.2f}%"

    print("\n--- Probe 5: +/-50% sweep of FLEX[] (the case's stated assumptions) ---")
    base_winner = winner
    for key in FLEX:
        base_val = PARAMS[key]
        for pct, label in ((0.5, "+50%"), (-0.5, "-50%")):
            flexed = dict(PARAMS)
            flexed[key] = base_val * (1 + pct)
            ev = evaluate_detail(flexed)
            w = "A" if ev["A"] > ev["B"] else ("B" if ev["B"] > ev["A"] else "TIE")
            lo, hi = min(ev["A"], ev["B"]), max(ev["A"], ev["B"])
            m = 0.0 if lo == 0 else 100.0 * (hi - lo) / lo
            flips = w != base_winner
            cap_breach = m > 20.0
            flag = []
            if flips:
                flag.append("FLIPS")
            if cap_breach:
                flag.append("CAP-BREACH(>20%)")
            flagstr = (" <-- " + ", ".join(flag)) if flag else ""
            print(f"  {key:26s} {label:5s}  A={ev['A']:.4e} (placed={ev['placed_a']:2d})  "
                  f"B={ev['B']:.4e} (placed={ev['placed_b']:2d})  winner={w}  margin={m:6.2f}%{flagstr}")
