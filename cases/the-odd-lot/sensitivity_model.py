#!/usr/bin/env python3
"""
Sensitivity model -- The Odd Lot.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is an ASSUMPTION
    evaluate(params) -> dict   EXACTLY {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the twist applied

Metric: dwelling-unit-years delivered within the stated planning horizon.
A = Plat As-Is, B = Replat & Consolidate.

FLEX scoping: the parcel geometry (Appendix C/D areas and rear-lot-line lengths),
FAR (3.44, cited S2), and average unit size (714 sq ft, cited S5) are fixed
givens -- the geometry is a constructed scenario (MA1) but not a single scalar
dial a facilitator would plausibly flex in discussion, and FAR/unit size are
real cited figures, stress-tested by Tier 2 probe 6 (data decay), not swept
here. Only the three scalar Modeling Assumptions that are genuinely dials
(MA3's two lead times, MA4's planning horizon) are in FLEX.
"""

FAR = 3.44                  # Appendix B / S2 -- cited, not FLEX
UNIT_SIZE = 714.0           # Appendix E / S5 -- cited, not FLEX
YARD_DEPTH = 30.0           # Appendix B / S3 -- cited, not FLEX

# Appendix C -- Option A's three "as-is" parcels (MA1/MA2, fixed geometry, not FLEX)
L1_AREA, L1_REAR = 11000.0, 40.0
L2_AREA, L2_REAR_EDGES = 7900.0, [80.0, 60.0, 64.0]   # rear + two concave notch edges
L3_AREA, L3_REAR = 11100.0, 80.0

# Appendix D -- Option B's consolidated lot (fixed geometry, not FLEX)
B_AREA, B_REAR = 30000.0, 200.0

PARAMS = {
    # --- Appendix E / Appendix F, MA3 ------------------------------------
    "lead_A": 6.0,        # months to construction start, Plat As-Is
    "lead_B": 18.0,       # months to construction start, Replat & Consolidate
    # --- Appendix E / Appendix F, MA4 ------------------------------------
    "horizon": 120.0,     # months, the stated planning horizon
    # --- the Twist (FACILITATOR.md): a shortened housing-production deadline
    "twist_horizon": 60.0,
}

FLEX = ["lead_A", "lead_B", "horizon"]


def _buildable_A():
    yard_L1 = L1_REAR * YARD_DEPTH
    yard_L2 = sum(L2_REAR_EDGES) * YARD_DEPTH
    yard_L3 = L3_REAR * YARD_DEPTH
    build = (L1_AREA - yard_L1) + (L2_AREA - yard_L2) + (L3_AREA - yard_L3)
    return build


def _buildable_B():
    yard = B_REAR * YARD_DEPTH
    return B_AREA - yard


def _units(buildable_sqft):
    return buildable_sqft * FAR / UNIT_SIZE


def _unit_years(units, lead_months, horizon_months):
    remaining = max(0.0, horizon_months - lead_months)
    return units * remaining / 12.0


def _metrics(lead_A, lead_B, horizon):
    units_A = _units(_buildable_A())
    units_B = _units(_buildable_B())
    a = _unit_years(units_A, lead_A, horizon)
    b = _unit_years(units_B, lead_B, horizon)
    return {"A": a, "B": b}


def evaluate(params=None):
    p = dict(PARAMS)
    p.update(params or {})
    return _metrics(p["lead_A"], p["lead_B"], p["horizon"])


def evaluate_twist(params=None):
    """A shortened housing-production deadline: the city's planning horizon
    drops from 10 years to 5 years (120 -> 60 months), penalizing Option B's
    longer lead time more heavily since fewer of its extra units are
    delivered within the now-shorter window."""
    p = dict(PARAMS)
    p.update(params or {})
    return _metrics(p["lead_A"], p["lead_B"], p["twist_horizon"])


if __name__ == "__main__":
    base = evaluate()
    tw = evaluate_twist()

    def margin(m):
        lo, hi = min(m["A"], m["B"]), max(m["A"], m["B"])
        winner = "A" if m["A"] > m["B"] else ("B" if m["B"] > m["A"] else "TIE")
        return winner, 100.0 * (hi - lo) / lo

    w, m = margin(base)
    print("BASE ", {k: round(v, 2) for k, v in base.items()}, "winner", w, "margin %.2f%%" % m)
    w, m = margin(tw)
    print("TWIST", {k: round(v, 2) for k, v in tw.items()}, "winner", w, "margin %.2f%%" % m)

    print("\n--- FLEX +-50% sweep ---")
    base_winner = margin(base)[0]
    for name in FLEX:
        for factor, label in ((1.5, "+50%"), (0.5, "-50%")):
            p = dict(PARAMS)
            p[name] = p[name] * factor
            r = evaluate(p)
            w, m = margin(r)
            flip = " <-- FLIP" if w != base_winner else ""
            breach = " <-- CAP BREACH (>20%)" if m > 20.0 else ""
            print(f"{name:10s} {label:5s} winner={w} margin={m:6.2f}%{flip}{breach}")

    print("\n--- geometry check (buildable areas, units) ---")
    print("buildable_A", _buildable_A(), "units_A", _units(_buildable_A()))
    print("buildable_B", _buildable_B(), "units_B", _units(_buildable_B()))
