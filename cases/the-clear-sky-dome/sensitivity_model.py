"""Sensitivity model for Clear-Sky Dome (skills/case-readiness Tier 2, P5).

Contract required by tier2_probes.py:
    PARAMS   -- every dial the case STATES
    FLEX     -- the subset that is a genuine ASSUMPTION (swept +/-50% by default)
    evaluate(params) -> {"A": metric, "B": metric}          higher is better
    evaluate_twist(params) -> {"A": metric, "B": metric}    optional
"""
import math

PARAMS = {
    "R": 2.5,                     # m, drum/dome/cone base radius (real, Ash-Dome S4)
    "H_drum": 2.65,                # m, drum wall height (real, Ash-Dome S4)
    "mass_drum_std": 755.0,        # kg, real Ash-Dome drum-wall weight (S4)
    "mass_dome_std": 1193.0,       # kg, real Ash-Dome dome-cap weight (S4)
    "steel_density": 7850.0,       # kg/m^3 (S9)
    "h_cone": 1.2,                 # m, windscreen height (MA1)
    "b_foot": 3.0,                 # m, pier footing base side (MA3, identical both sites)
    "h_foot": 1.0,                 # m, pier footing height (MA3, identical both sites)
    "steel_price": 1.3228,         # $/kg (S6, derived, hot-rolled coil)
    "concrete_price": 235.37,      # $/m^3 (S7, derived)
    "formwork_price": 52.10,       # $/m^2 (S8, derived)
    "wind_std_mph": 70.0,          # HUD Wind Zone I (S5)
    "wind_reinf_mph": 100.0,       # HUD Wind Zone II (S5)
    "reinforcement_factor": 100.0 / 70.0,  # MA2 -- stated thickness-scaling assumption (the FLEX dial)
    "frac_A": 0.77,                # Vantage Mesa clear-sky fraction (S1)
    "frac_B": 0.626,               # Sable Hollow clear-sky fraction (S3, ground-based clear-night mean)
    "dark_hours": 9.0,             # avg usable dark hours/night, both sites (MA4, disclosed assumption)
}

# Only the wind-driven reinforcement factor is a genuine stated ASSUMPTION (MA2) --
# everything else is either real cited data or a fixed, non-wind-driven design choice
# (MA1's windscreen height, MA3's footing size) applied identically at both sites.
FLEX = ["reinforcement_factor"]


def _thicknesses(p):
    R, H = p["R"], p["H_drum"]
    SA_drum_lat = 2 * math.pi * R * H
    SA_dome_hemi = 2 * math.pi * R ** 2
    t_drum_std = p["mass_drum_std"] / (p["steel_density"] * SA_drum_lat)
    t_dome_std = p["mass_dome_std"] / (p["steel_density"] * SA_dome_hemi)
    t_cone_std = t_drum_std
    factor = p.get("reinforcement_factor", p["wind_reinf_mph"] / p["wind_std_mph"])
    return t_drum_std, t_dome_std, t_cone_std, factor


def _cyl_shell(R, H, t):
    return math.pi * H * (R ** 2 - (R - t) ** 2)


def _hemi_shell(R, t):
    return (2 / 3) * math.pi * (R ** 3 - (R - t) ** 3)


def _cone_shell(R, h, t):
    return (1 / 3) * math.pi * h * (R ** 2 - (R - t) ** 2)


def _pyr_vol(b, h):
    return (1 / 3) * b ** 2 * h


def _pyr_lateral_SA(b, h):
    l = math.sqrt(h ** 2 + (b / 2) ** 2)
    return 4 * (0.5 * b * l)


def _pyr_total_SA(b, h):
    return b ** 2 + _pyr_lateral_SA(b, h)


def _construction_cost(p, t_drum, t_dome, t_cone):
    R = p["R"]
    v_steel = (_cyl_shell(R, p["H_drum"], t_drum)
               + _hemi_shell(R, t_dome)
               + _cone_shell(R, p["h_cone"], t_cone))
    cost_steel = v_steel * p["steel_density"] * p["steel_price"]
    v_pier = _pyr_vol(p["b_foot"], p["h_foot"])
    cost_concrete = v_pier * p["concrete_price"]
    # Formwork prices only the four lateral (triangular) faces -- the base sits
    # directly against undisturbed soil in the excavation and needs no form.
    sa_pier_lateral = _pyr_lateral_SA(p["b_foot"], p["h_foot"])
    cost_formwork = sa_pier_lateral * p["formwork_price"]
    return cost_steel + cost_concrete + cost_formwork


def _hours(p, frac):
    return frac * p["dark_hours"] * 365


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    t_drum_std, t_dome_std, t_cone_std, factor = _thicknesses(p)

    std_total = _construction_cost(p, t_drum_std, t_dome_std, t_cone_std)
    reinf_total = _construction_cost(p, t_drum_std * factor, t_dome_std * factor, t_cone_std * factor)

    hours_A = _hours(p, p["frac_A"])
    hours_B = _hours(p, p["frac_B"])

    metric_A = hours_A / reinf_total
    metric_B = hours_B / std_total
    return {"A": metric_A, "B": metric_B}


def evaluate_twist(params):
    """Twist: the insurer imposes a uniform minimum wind rating -- both sites must
    now build to the reinforced (Vantage Mesa) spec. Removes the cost differential
    entirely; only the clear-sky fraction still differs."""
    p = dict(PARAMS)
    p.update(params or {})
    t_drum_std, t_dome_std, t_cone_std, factor = _thicknesses(p)

    uniform_total = _construction_cost(p, t_drum_std * factor, t_dome_std * factor, t_cone_std * factor)

    hours_A = _hours(p, p["frac_A"])
    hours_B = _hours(p, p["frac_B"])

    metric_A = hours_A / uniform_total
    metric_B = hours_B / uniform_total
    return {"A": metric_A, "B": metric_B}


if __name__ == "__main__":
    base = evaluate({})
    print("BASE:", base, "winner:", "A" if base["A"] > base["B"] else "B",
          "margin_pct:", abs(base["A"] - base["B"]) / max(base["A"], base["B"]) * 100)

    factor0 = PARAMS["wind_reinf_mph"] / PARAMS["wind_std_mph"]
    for label, f in [("-50%", factor0 * 0.5), ("+50%", factor0 * 1.5)]:
        r = evaluate({"reinforcement_factor": f})
        m = abs(r["A"] - r["B"]) / max(r["A"], r["B"]) * 100
        print(label, r, "winner:", "A" if r["A"] > r["B"] else "B", "margin_pct:", m)

    t = evaluate_twist({})
    mt = abs(t["A"] - t["B"]) / max(t["A"], t["B"]) * 100
    print("TWIST:", t, "winner:", "A" if t["A"] > t["B"] else "B", "margin_pct:", mt)
