#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Deluge Gun.

Reproduces the case's own arithmetic (range equation -> two complementary
elevation angles -> apex height / time of flight -> wind-drift-discounted
effective GPM) so Tier 2 probe 5 can flex the case's two stated Modeling
Assumptions (MA1: structure height: MA2: wind-drift loss rate) by +/-50% and
report whether either flips which option (A = Low Arc, B = High Arc) wins on
the primary metric (effective gallons-on-target per minute).

CONTRACT: PARAMS, FLEX, evaluate(params) -> {"A": metric, "B": metric}.

Verified against case.json.balance.computed_values / FACILITATOR.md:
    base   A (Low Arc)  = 477.93 GPM   B (High Arc) = 436.65 GPM   margin 9.45%
"""
import math

PARAMS = {
    # --- Appendix B, real cited figures (NOT flexed -- see FLEX below) ------
    "tip_diameter_in": 1.375,          # S4
    "nozzle_pressure_psi": 80.0,       # S3
    "rated_gpm": 500.0,                # S6
    "g_ft_s2": 32.2,                   # S5, standard constant
    "collapse_zone_multiplier": 1.5,   # S1, real cited rule -- NOT an assumption
    # --- Appendix F, Modeling Assumptions (the case's own stated dials) -----
    "structure_height_ft": 150.0,          # MA1
    "wind_loss_rate_pct_per_s": 2.0,       # MA2 (percent per second)
}

# SPEC §2 / MCS-26: flex STATED ASSUMPTIONS only, not cited measurements.
# collapse_zone_multiplier (S1), tip/pressure/rated_gpm (S3/S4/S6), and g (S5)
# are all real, sourced figures -- halving the collapse-zone rule is a
# different case, not a sensitivity test on this one. MA1 and MA2 are the two
# genuine stated scenario dials (see case.json.modeling_assumptions).
FLEX = [
    "structure_height_ft",       # MA1
    "wind_loss_rate_pct_per_s",  # MA2
]


def _exit_velocity_ft_s(p):
    d_ft = p["tip_diameter_in"] / 12.0
    area_ft2 = math.pi * (d_ft / 2.0) ** 2
    q_ft3_s = p["rated_gpm"] * 0.13368 / 60.0
    return q_ft3_s / area_ft2


def evaluate(params=None):
    p = dict(PARAMS)
    p.update(params or {})

    v = _exit_velocity_ft_s(p)
    g = p["g_ft_s2"]
    R = p["collapse_zone_multiplier"] * p["structure_height_ft"]

    ratio = R * g / (v ** 2)
    ratio = max(-1.0, min(1.0, ratio))          # domain guard: sin(2*theta) in [-1, 1]
    two_theta_low = math.degrees(math.asin(ratio))
    theta_low = two_theta_low / 2.0
    theta_high = 90.0 - theta_low

    vy_low = v * math.sin(math.radians(theta_low))
    vy_high = v * math.sin(math.radians(theta_high))
    t_low = 2 * vy_low / g
    t_high = 2 * vy_high / g

    loss_rate = p["wind_loss_rate_pct_per_s"] / 100.0
    eff_low = p["rated_gpm"] * max(0.0, 1 - loss_rate * t_low)
    eff_high = p["rated_gpm"] * max(0.0, 1 - loss_rate * t_high)

    # CONTRACT: exactly two keys, A and B. (Debug fields caused probe_sensitivity's
    # max()/min() over the whole dict to pick a non-A/B key as "loser" -- fixed by
    # not returning them here; use evaluate_debug() below for the printed detail.)
    return {"A": eff_low, "B": eff_high}


def evaluate_debug(params=None):
    p = dict(PARAMS); p.update(params or {})
    v = _exit_velocity_ft_s(p)
    g = p["g_ft_s2"]
    R = p["collapse_zone_multiplier"] * p["structure_height_ft"]
    ratio = max(-1.0, min(1.0, R * g / (v ** 2)))
    theta_low = math.degrees(math.asin(ratio)) / 2.0
    theta_high = 90.0 - theta_low
    t_low = 2 * v * math.sin(math.radians(theta_low)) / g
    t_high = 2 * v * math.sin(math.radians(theta_high)) / g
    r = evaluate(params)
    r.update({"theta_low_deg": theta_low, "theta_high_deg": theta_high,
              "t_low_s": t_low, "t_high_s": t_high})
    return r


if __name__ == '__main__':
    base = evaluate_debug({})
    print("base  A(Low Arc)=%.2f  B(High Arc)=%.2f  margin=%.2f%%  theta=%.2f/%.2f" % (
        base["A"], base["B"], 100 * (base["A"] - base["B"]) / base["A"],
        base["theta_low_deg"], base["theta_high_deg"]))

    for dial in FLEX:
        for pct, label in ((1.5, "+50%"), (0.5, "-50%")):
            flexed = dict(PARAMS)
            flexed[dial] = PARAMS[dial] * pct
            r = evaluate(flexed)
            winner = "A" if r["A"] > r["B"] else ("B" if r["B"] > r["A"] else "TIE")
            base_winner = "A" if base["A"] > base["B"] else "B"
            flip = " <<< FLIP" if winner != base_winner else ""
            print(f"{dial} {label}: A={r['A']:.2f} B={r['B']:.2f} winner={winner}{flip}")
