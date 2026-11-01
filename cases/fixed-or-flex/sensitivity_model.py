#!/usr/bin/env python3
"""
Sensitivity model -- Fixed Or Flex.

Contract per skills/case-readiness/scripts/example_sensitivity_model.py:
    PARAMS, FLEX, evaluate(params) -> {"A","B"} (higher is better), evaluate_twist(params).

Metric: weighted trips bought per year by the $100,000 =
        (average trips per $100k of that mode) x rho x w.
A = More Fixed (rho_F, w=1 by definition); B = More Flex (rho_D, w).

Cited NTD figures (RY2024 expenses and trips) are NOT in FLEX -- SPEC 2 asks for
sensitivity to stated assumptions; cited data is stress-tested by P6.
Margin convention: (winner - loser) / winner.
"""

# --- cited, NTD ekg5-frzt, ntd_id 30044, RY2024 (S1) -- NOT flexed -------------
PARAMS = {
    "mb_expense": 7617684.0, "mb_trips": 205556.0, "mb_hours": 43758.0,
    "dr_expense": 6265961.0, "dr_trips": 158133.0, "dr_hours": 71297.0,
    # --- stated assumptions (Appendix C) -- the dials FLEX sweeps --------------
    "rho_F": 1.00,   # M3
    "rho_D": 1.00,   # M4
    "w": 1.00,       # M5
    # --- Twist only (RY2025 NTD rows, withheld from the student packet) --------
    "mb_expense_25": 8267834.0, "mb_trips_25": 204462.0,
    "dr_expense_25": 6981124.0, "dr_trips_25": 164014.0,
}

FLEX = ["rho_F", "rho_D", "w"]


def _per100k(trips, expense):
    return trips / expense * 100000.0


def evaluate(params):
    p = dict(PARAMS); p.update(params or {})
    a = _per100k(p["mb_trips"], p["mb_expense"]) * p["rho_F"]
    b = _per100k(p["dr_trips"], p["dr_expense"]) * p["rho_D"] * p["w"]
    return {"A": a, "B": b}


def evaluate_twist(params):
    """Twist: RY2025 arrives. Marginal productivity RY2024->RY2025 replaces the
    'added hour = average hour' assumption (one year, agency-wide, not causal)."""
    p = dict(PARAMS); p.update(params or {})
    d_exp_f = p["mb_expense_25"] - p["mb_expense"]
    d_trip_f = p["mb_trips_25"] - p["mb_trips"]
    d_exp_d = p["dr_expense_25"] - p["dr_expense"]
    d_trip_d = p["dr_trips_25"] - p["dr_trips"]
    a = _per100k(d_trip_f, d_exp_f)            # about -168.3
    b = _per100k(d_trip_d, d_exp_d) * p["w"]   # about +822.3 x w
    return {"A": a, "B": b}


if __name__ == "__main__":
    import json
    for name, f in (("base", evaluate), ("twist", evaluate_twist)):
        r = f({})
        hi, lo = max(r.values()), min(r.values())
        print(name, {k: round(v, 1) for k, v in r.items()},
              "margin (gap/winner) %.2f%%" % (100 * (hi - lo) / abs(hi)))
    pa = PARAMS["mb_trips"] / PARAMS["mb_expense"] * 1e5
    pb = PARAMS["dr_trips"] / PARAMS["dr_expense"] * 1e5
    print("rho_F* = %.4f   w* = %.4f" % (pb / pa, pa / pb))
