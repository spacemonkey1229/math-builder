"""
sensitivity_model.py — The Deep End

Contract (see skills/case-readiness/SKILL.md, Tier 2 Probe 5):
    PARAMS: dict[str, number]      every dial the case STATES
    FLEX:   list[str]              the subset that is an ASSUMPTION (all four here — see
                                    case.json.modeling_assumptions MA1/MA2)
    def evaluate(params) -> {"A": metric, "B": metric}     higher is better
    def evaluate_twist(params) -> {...}                    N/A for this case (Twist: N/A,
                                    see FACILITATOR.md) — omitted on purpose.

primary_metric: supervised swim-hours accessible to the facility's actual user base, per
square foot of pool footprint. Higher is better for both A and B.
"""

PARAMS = {
    "total_weekly_hours": 63.0,     # MA1 — facility's total weekly scheduled supervised-swim hours
    "reserved_hours_a": 18.0,       # MA1 — Deep-End Design's exclusive swim-team practice block
    "footprint_a": 2700.0,          # MA2 — Deep-End Design pool basin footprint, sq ft
    "footprint_b": 3500.0,          # MA2 — Zero-Entry Ramp Design pool basin footprint, sq ft
}

# All four PARAMS are stated Modeling Assumptions (case.json.modeling_assumptions MA1/MA2),
# not cited/given data — so all four are legitimately swept by Tier 2 Probe 5's default sweep.
FLEX = ["total_weekly_hours", "reserved_hours_a", "footprint_a", "footprint_b"]


def evaluate(params):
    """Return {'A': rate, 'B': rate} in supervised swim-hours per square foot. Higher wins."""
    accessible_hours_a = params["total_weekly_hours"] - params["reserved_hours_a"]
    rate_a = accessible_hours_a / params["footprint_a"]
    rate_b = params["total_weekly_hours"] / params["footprint_b"]
    return {"A": rate_a, "B": rate_b}


if __name__ == "__main__":
    base = evaluate(PARAMS)
    winner = "A" if base["A"] > base["B"] else ("B" if base["B"] > base["A"] else "TIE")
    lo = min(base.values())
    margin_pct = 0.0 if lo == 0 else 100.0 * abs(base["A"] - base["B"]) / lo
    print("base:", base, "winner:", winner, "margin_pct: %.2f" % margin_pct)
