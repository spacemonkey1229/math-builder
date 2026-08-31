#!/usr/bin/env python3
"""
Sensitivity model -- The Crosswind Cut.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the contract
and worked reference (Cold Chain).

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is a stated
                                                     Modeling Assumption
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better

The metric is net forward-progress thrust per amp (case.json.balance.margin_basis):
for each configuration, sum thrust and current across MA3's motor count at the
route's throttle setting (Appendix A), resolve the crosswind into a
course-perpendicular component that must be cancelled (Appendix B, MA1/MA2),
take the dot product of the remaining thrust vector with the delivery-heading
unit vector (D3), and divide by total current draw (D4). Configuration A is
Sparrow (high-KV/small prop), Configuration B is Albatross (low-KV/large prop).

Fixed (not in FLEX[]): Appendix A's per-motor thrust/current/RPM figures at 90%
throttle and the 40%-throttle advertised-efficiency figures -- these are T-Motor's
own published test data (sources[] S1/S2), not stated scenario assumptions.
Only Appendix D's seven Modeling Assumptions (MA1-MA7) are stated conventions,
and only the five that actually reach D3/D4 are swept by default (MA5/MA6/MA7
feed only the separate D5 reserve check and are NOT part of this metric, exactly
as case.json's own MA5/MA6/MA7 sensitivity notes say -- flexing them is
mechanically a no-op on evaluate(), which is itself the finding, not a bug).

Verified against case.md and FACILITATOR.md (2026-08-31 remediation):
    base    A (Sparrow) = 121.21 g/A  ·  B (Albatross) = 119.07 g/A
            margin = (121.21-119.07)/119.07 * 100 = 1.8%   (matches case.json.margin_pct)
    MA1 flexed +/-50% (7.5 mph, 22.5 mph): margin UNCHANGED at 1.8% -- the
            wind-correction cosine is common to both configurations and cancels
            out of the ratio. This is the case's real Twist finding, reproduced
            here mechanically, not asserted.
    Only a change to the underlying Appendix A thrust/current data (NOT a
            Modeling Assumption, so not in FLEX[] -- see --flex-all) can move
            the winner, because the ranking is decided by which side of
            T-Motor's ~70-80% throttle efficiency crossover the modeled
            throttle setting falls on.
"""
import math

# --- Fixed: cited data (sources[] S1/S2), not stated modeling assumptions ---
# Per-motor figures at the route's 90% throttle setting, T-Motor's own test data.
THRUST_PER_MOTOR_G = {"A": 2782.0, "B": 3909.0}
CURRENT_PER_MOTOR_A = {"A": 20.60, "B": 29.46}

PARAMS = {
    # --- MA1: crosswind speed, mph -------------------------------------------
    "crosswind_mph": 15.0,
    # --- MA2: crossing angle between corridor heading and crosswind, degrees -
    "crossing_angle_deg": 80.0,
    # --- MA3: number of motors on the airframe -------------------------------
    "motor_count": 4,
    # --- MA4: commanded cruise groundspeed, mph ------------------------------
    "groundspeed_mph": 33.5,
    # --- MA5: route length, mi (D5 reserve check only, not D3/D4) -----------
    "route_length_mi": 4.0,
    # --- MA6: battery pack capacity, Ah (D5 reserve check only) -------------
    "battery_capacity_ah": 22.0,
    # --- MA7: mandatory reserve fraction at touchdown (D5 reserve check only)
    "reserve_fraction": 0.25,
}

# Probe 5 flexes THESE and only these -- the subset that is a stated Modeling
# Assumption reaching D3/D4 (the graded ranking). MA5/MA6/MA7 are included so
# --flex is complete, but they provably cannot move evaluate()'s A/B metric
# (see reserve_check() instead) -- Appendix A's sourced thrust/current data is
# NOT a Modeling Assumption, so it is excluded here; --flex-all overrides.
FLEX = [
    "crosswind_mph",       # MA1
    "crossing_angle_deg",  # MA2
    "motor_count",          # MA3
    "groundspeed_mph",      # MA4
    "route_length_mi",      # MA5 (D5 only)
    "battery_capacity_ah",  # MA6 (D5 only)
    "reserve_fraction",     # MA7 (D5 only)
]


def _wind_correction_cos(p):
    """cos(theta), theta = the crab angle needed to cancel the crosswind's
    course-perpendicular component. Domain-invalid (crosswind's cross-corridor
    component exceeds groundspeed) returns None -- the route is not flyable
    under a simple crab-angle correction at all, which is itself a finding."""
    sin_arg = p["crosswind_mph"] * math.sin(math.radians(p["crossing_angle_deg"])) / p["groundspeed_mph"]
    if abs(sin_arg) > 1.0:
        return None
    theta = math.asin(sin_arg)
    return math.cos(theta)


def evaluate(params):
    """Net forward-progress thrust per amp for each configuration. Higher wins."""
    p = dict(PARAMS)
    p.update(params or {})
    cos_t = _wind_correction_cos(p)
    n = p["motor_count"]
    out = {}
    for k in ("A", "B"):
        total_thrust = THRUST_PER_MOTOR_G[k] * n
        total_current = CURRENT_PER_MOTOR_A[k] * n
        if cos_t is None:
            # Crosswind cannot be cancelled by a simple crab angle at all --
            # net forward progress is undefined/zero, not merely small.
            out[k] = 0.0
        else:
            net_thrust = total_thrust * cos_t
            out[k] = net_thrust / total_current
    return out


def reserve_check(params):
    """D5: percent of the mandatory reserve remaining at touchdown for each
    configuration. Not part of the Probe 5 A/B metric (D3/D4 alone decide the
    recommendation) -- reported separately because MA5/MA6/MA7 only ever reach
    this check, never evaluate()'s ranking, which is itself part of the case's
    documented sensitivity story."""
    p = dict(PARAMS)
    p.update(params or {})
    n = p["motor_count"]
    time_hr = p["route_length_mi"] / p["groundspeed_mph"]
    out = {}
    for k in ("A", "B"):
        total_current = CURRENT_PER_MOTOR_A[k] * n
        used_ah = total_current * time_hr
        remaining_pct = 100.0 * (p["battery_capacity_ah"] - used_ah) / p["battery_capacity_ah"]
        out[k] = {
            "used_ah": used_ah,
            "remaining_pct": remaining_pct,
            "legal": remaining_pct >= 100.0 * p["reserve_fraction"],
        }
    return out


if __name__ == '__main__':
    base = evaluate({})
    print("base per-amp", {k: round(v, 2) for k, v in base.items()},
          "margin %.2f%%" % (100 * (base["A"] - base["B"]) / base["B"]))

    for wind in (7.5, 22.5):
        r = evaluate({"crosswind_mph": wind})
        m = 100 * (r["A"] - r["B"]) / r["B"] if r["B"] else float('nan')
        print(f"crosswind={wind} mph  per-amp", {k: round(v, 2) for k, v in r.items()},
              "margin %.2f%%" % m)

    print("reserve check (base)", {k: {kk: round(vv, 3) if isinstance(vv, float) else vv
                                          for kk, vv in v.items()}
                                     for k, v in reserve_check({}).items()})

    # A crosswind at NWS gust range (S3, 46-57 mph) -- the crab angle correction
    # this case's model relies on stops having a solution well before that.
    gust = evaluate({"crosswind_mph": 46.0})
    print("crosswind=46 mph (NWS gust floor)", gust, "(0.0/0.0 => undefined crab angle)")
