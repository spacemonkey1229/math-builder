#!/usr/bin/env python3
"""
Sensitivity model for The Last Bench (Tier 2 probe 5).

Metric: life-of-pit cash margin, undiscounted, USD million (higher is better).
  A = ore_res*(v - proc) - (ore_res + waste_res)*mining
  B = A + pipe_t*(v - proc) - shell_t*mining - capital
  v = grade * recovery / g_per_oz * price      (recovered gold value per tonne of ore)

Cited data (NOT flexed): price_2024 (USGS MCS 2026), oz_per_tonne conversion.
Everything else is a scenario assumption (Appendix C) and is in FLEX.
The Twist price (USGS 2025 estimate, MCS 2026) is cited and lives only in evaluate_twist().

Also exposes pv_margins() for the optional discounting test (mid-period convention).
"""
import math

PARAMS = {
    "price_2024": 2388.0,        # cited, USGS MCS 2026
    "oz_per_tonne": 32150.7,     # cited, USGS MCS 2026 footnote 1 (troy oz per metric tonne)
    "twist_price": 3300.0,       # cited, USGS MCS 2026 (2025 estimate); Twist only
    "grade_gpt": 1.0,
    "recovery": 0.88,
    "mining_cost": 3.0,
    "proc_cost": 22.0,
    "capital_m": 60.0,
    "ore_res_mt": 25.0,
    "waste_res_mt": 50.0,
    "density": 2.6,
    "floor_radius": 180.0,
    "depth_cur": 300.0,
    "push_depth": 60.0,
    "wall_angle_deg": 42.0,
    "pipe_radius": 140.0,
    "throughput_mt": 20.0,
    "discount": 0.08,
}

FLEX = ["grade_gpt", "recovery", "mining_cost", "proc_cost", "capital_m", "ore_res_mt",
        "waste_res_mt", "density", "floor_radius", "depth_cur", "push_depth",
        "wall_angle_deg", "pipe_radius"]


def _geom(p):
    t = math.tan(math.radians(p["wall_angle_deg"]))
    fr = p["floor_radius"]
    hs = fr * t
    vols = []
    for d in (p["depth_cur"], p["depth_cur"] + p["push_depth"]):
        R = fr + d / t
        H = d + hs
        vols.append(math.pi / 3.0 * (R * R * H - fr * fr * hs))
    shell_m3 = vols[1] - vols[0]
    pipe_m3 = math.pi * p["pipe_radius"] ** 2 * p["push_depth"]
    return shell_m3 * p["density"] / 1e6, pipe_m3 * p["density"] / 1e6   # Mt, Mt


def _value_per_t(p, price):
    # grams of gold per tonne -> troy oz per tonne via oz per metric tonne (1e6 g / oz_per_tonne = g per oz)
    g_per_oz = 1e6 / p["oz_per_tonne"]
    return p["grade_gpt"] * p["recovery"] / g_per_oz * price


def _margins(p, price):
    shell_t, pipe_t = _geom(p)
    pipe_t = min(pipe_t, shell_t)           # ore cannot exceed the rock in the shell
    v = _value_per_t(p, price)
    A = p["ore_res_mt"] * (v - p["proc_cost"]) - (p["ore_res_mt"] + p["waste_res_mt"]) * p["mining_cost"]
    B = A + pipe_t * (v - p["proc_cost"]) - shell_t * p["mining_cost"] - p["capital_m"]
    return A, B


def evaluate(params=None):
    p = dict(PARAMS); p.update(params or {})
    A, B = _margins(p, p["price_2024"])
    return {"A": A, "B": B}


def evaluate_twist(params=None):
    p = dict(PARAMS); p.update(params or {})
    A, B = _margins(p, p["twist_price"])
    return {"A": A, "B": B}


def breakeven_price(params=None):
    p = dict(PARAMS); p.update(params or {})
    lo, hi = 500.0, 20000.0
    f = lambda P: (lambda ab: ab[1] - ab[0])(_margins(p, P))
    if f(lo) * f(hi) > 0:
        return None
    for _ in range(80):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def pv_margins(price, params=None, mid_period=True):
    """Discounted margins. Rock is moved at throughput_mt per year: reserve first, then the
    pushback; each year's cash is taken at the middle of the year (part-years prorated);
    capital is paid when the pushback begins."""
    p = dict(PARAMS); p.update(params or {})
    shell_t, pipe_t = _geom(p); pipe_t = min(pipe_t, shell_t)
    v = _value_per_t(p, price); r = p["discount"]; thr = p["throughput_mt"]
    res_rock = p["ore_res_mt"] + p["waste_res_mt"]
    a_net = p["ore_res_mt"] * (v - p["proc_cost"]) - res_rock * p["mining_cost"]
    push_net = pipe_t * (v - p["proc_cost"]) - shell_t * p["mining_cost"]

    def stream(segments):
        t0 = 0.0; total = 0.0
        for rock, net in segments:
            rem = rock; start = t0
            while rem > 1e-12:
                frac_in_year = 1.0 - (start % 1.0) if (start % 1.0) > 1e-12 else 1.0
                step = min(frac_in_year, rem / thr)
                share = step * thr / rock
                when = start + step / 2.0 if mid_period else start + step
                total += net * share / (1 + r) ** when
                start += step; rem -= step * thr
            t0 += rock / thr
        return total
    pv_a = stream([(res_rock, a_net)])
    pv_b = stream([(res_rock, a_net), (shell_t, push_net)]) - p["capital_m"] / (1 + r) ** (res_rock / thr)
    return pv_a, pv_b


def stake(params=None, crew=180):
    p = dict(PARAMS); p.update(params or {})
    shell_t, pipe_t = _geom(p)
    la = (p["ore_res_mt"] + p["waste_res_mt"]) / p["throughput_mt"]
    lb = la + shell_t / p["throughput_mt"]
    return la, lb, crew * la, crew * lb


if __name__ == "__main__":
    b = evaluate(); t = evaluate_twist()
    print("2024  A %.1f  B %.1f  winner %s  margin %.2f%%" % (b["A"], b["B"], "A" if b["A"] > b["B"] else "B",
          100 * abs(b["A"] - b["B"]) / max(b["A"], b["B"])))
    print("twist A %.1f  B %.1f  winner %s  margin %.2f%%" % (t["A"], t["B"], "A" if t["A"] > t["B"] else "B",
          100 * abs(t["A"] - t["B"]) / max(t["A"], t["B"])))
    print("break-even price %.1f" % breakeven_price())
    for P in (1801, 1802, 1945, 2388, 3300):
        a, bb = _margins(dict(PARAMS), P)
        print(P, round(a, 1), round(bb, 1), "gap/winner %.1f%%" % (100 * abs(a - bb) / max(a, bb)))
    print("PV 2024", [round(x, 1) for x in pv_margins(2388)], "PV twist", [round(x, 1) for x in pv_margins(3300)])
    print("PV end-period 2024", [round(x, 1) for x in pv_margins(2388, mid_period=False)])
    print("stake", stake())
    print("--- +/-50% flex (2024 anchor) ---")
    for k in FLEX:
        row = []
        for f in (0.5, 1.5):
            e = evaluate({k: PARAMS[k] * f})
            row.append("%s %.0f%%" % ("A" if e["A"] > e["B"] else "B", 100 * abs(e["A"] - e["B"]) / max(e["A"], e["B"])))
        print("%-16s -50%%: %-8s +50%%: %s" % (k, row[0], row[1]))
