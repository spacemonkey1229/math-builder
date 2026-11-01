#!/usr/bin/env python3
"""
Sensitivity model -- The Eight-Second Tour.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS, FLEX, evaluate(params) -> {"A": metric, "B": metric} (higher is better),
    evaluate_twist(params).

Options: A = commit to the aero-bar position; B = ride the conventional position at full power.
Metric: predicted average speed over the 24.5 km, km/h, from the aero-only cube-law
approximation. Hindsight-scenario stand-in: the rival's expected stage time is Fignon's real
27:55 (1675 s). LeMond's conventional-position speed is Fignon's speed times a SOURCED
baseline ratio b taken from the three earlier 1989 Tour individual time trials (prologue
1.0000, stage 5 1.0095, stage 15 1.0109; Wikipedia). B's speed = Fignon speed * b.
A's speed = B's speed * ((1 - y) / (1 - x)) ** (1/3), where x = fractional cut in drag
area (CdA) and y = fractional loss in sustainable power in the aero position.
b cancels in the A-vs-B speed comparison; it matters only for the 50 s bar (follow-on).
Ratios only: this model never claims LeMond produced any particular wattage.

FLEX scoping: x and y are the two scenario assumptions (a SENSITIVITY RANGE, x 10-15%,
y 3-14%; base = midpoints 12.5% / 8.5%). The stage distance, the real times (cited) and the
50 s deficit (cited) are fixed givens and are NOT in FLEX (Tier 2 P6 covers cited data).
"""
DIST_KM = 24.5
RIVAL_TIME_S = 1675.0        # Fignon 27:55, cited (Wikipedia)
DEFICIT_S = 50.0             # cited
LEMOND_TIME_S = 1617.0       # 26:57, cited (used only by the model-mismatch check)
# bundle scenario parameters (a model, not data), used only by full_model_*
RHO, CDA0, MASS, CRR, G = 1.225, 0.32, 78.0, 0.004, 9.81

# Observed LeMond/Fignon speed ratios, earlier 1989 Tour ITTs (Wikipedia, whole-second results)
B_PROLOGUE = 1.0                         # 7.8 km, both +6 s on the winner
B_STAGE5 = 5948.0 / 5892.0               # 73 km; LeMond used triathlon bars (per Wikipedia)
B_STAGE15 = 4346.0 / 4299.0              # 39 km mountain ITT
B_LOW, B_HIGH = B_PROLOGUE, B_STAGE15

PARAMS = {
    "cda_cut": 0.125,          # x, midpoint of the 10-15% sensitivity range (MA)
    "power_loss": 0.085,       # y, midpoint of the 3-14% sensitivity range (MA)
    "twist_power_loss": 0.14,  # the twist: a lab estimate at the top of the y range
    "baseline_ratio": (B_LOW + B_HIGH) / 2.0,   # b: midpoint of the observed range (cited-derived, not FLEX)
}
FLEX = ["cda_cut", "power_loss"]


def conv_speed_kmh():
    return DIST_KM / (RIVAL_TIME_S / 3600.0)


def speed_ratio(x, y):
    return ((1.0 - y) / (1.0 - x)) ** (1.0 / 3.0)


def _metrics(x, y, b=None):
    b = PARAMS["baseline_ratio"] if b is None else b
    v0 = conv_speed_kmh() * b
    return {"A": v0 * speed_ratio(x, y), "B": v0}


def evaluate(params=None):
    p = dict(PARAMS); p.update(params or {})
    return _metrics(p["cda_cut"], p["power_loss"], p["baseline_ratio"])


def evaluate_twist(params=None):
    p = dict(PARAMS); p.update(params or {})
    return _metrics(p["cda_cut"], p["twist_power_loss"], p["baseline_ratio"])


# ---- derived figures of record (checked against FACILITATOR.md / case.json) ----
def needed_ratio():
    return RIVAL_TIME_S / (RIVAL_TIME_S - DEFICIT_S)


def cube_break_even(x, b=1.0):
    """max power loss y for the aero position to still reach the 50 s bar, given baseline b."""
    return 1.0 - (needed_ratio() / b) ** 3 * (1.0 - x)


def _power(v, cda):
    return 0.5 * RHO * cda * v ** 3 + CRR * MASS * G * v


def full_break_even(x, b=1.0):
    v0 = DIST_KM * 1000.0 / RIVAL_TIME_S * b
    v1 = DIST_KM * 1000.0 / RIVAL_TIME_S * needed_ratio()
    return 1.0 - _power(v1, CDA0 * (1 - x)) / _power(v0, CDA0)


def box_share(b, model="cube", n=400):
    """share of the x 10-15% by y 3-14% box where the aero position reaches the 50 s bar"""
    hit = 0
    for i in range(n):
        x = 0.10 + 0.05 * (i + 0.5) / n
        for j in range(n):
            y = 0.03 + 0.11 * (j + 0.5) / n
            lim = cube_break_even(x, b) if model == "cube" else full_break_even(x, b)
            hit += y <= lim
    return hit / float(n * n)


def conv_gain_s(b):
    """seconds the conventional position gains on Fignon's 27:55 from the baseline alone"""
    return RIVAL_TIME_S - RIVAL_TIME_S / b


def model_power_at_lemond_speed():
    return _power(DIST_KM * 1000.0 / LEMOND_TIME_S, CDA0)


def margin(m):
    lo, hi = min(m.values()), max(m.values())
    return ("A" if m["A"] > m["B"] else "B" if m["B"] > m["A"] else "TIE"), 100.0 * (hi - lo) / lo


if __name__ == "__main__":
    print("needed ratio %.4f cubed %.4f" % (needed_ratio(), needed_ratio() ** 3))
    print("baselines: prologue %.4f stage5 %.4f stage15 %.4f stage21(not used) %.4f" % (B_PROLOGUE, B_STAGE5, B_STAGE15, 1675 / 1617.0))
    for b in (B_LOW, B_STAGE5, B_HIGH):
        print("b=%.4f aero needs ratio %.4f cubed %.4f; B gains %.1f s; box share cube %.3f full %.3f" % (b, needed_ratio() / b, (needed_ratio() / b) ** 3, conv_gain_s(b), box_share(b), box_share(b, "full")))
        for x in (.10, .14, .15, .20):
            print("   x=%2d%%  cube y<=%.2f%%  full y<=%.2f%%" % (x * 100, 100 * cube_break_even(x, b), 100 * full_break_even(x, b)))
    print("model power at 26:57: %.1f W" % model_power_at_lemond_speed())
    b = evaluate(); t = evaluate_twist()
    print("BASE", {k: round(v, 3) for k, v in b.items()}, margin(b))
    print("TWIST", {k: round(v, 3) for k, v in t.items()}, margin(t))
    bw = margin(b)[0]
    for n in FLEX:
        for f in (1.5, .5):
            p = dict(PARAMS); p[n] *= f
            r = evaluate(p); w, m = margin(r)
            print(n, f, round(p[n], 4), w, round(m, 2), "FLIP" if w != bw else "")
    # time-gain view (seconds) at the base and the grid corners, for FACILITATOR only
    for x, y in ((.10, .03), (.15, .03), (.10, .14), (.15, .14), (.125, .085)):
        r = speed_ratio(x, y)
        print("x=%.3f y=%.3f ratio %.4f time %.1f s gain %.1f s" % (x, y, r, RIVAL_TIME_S / r, RIVAL_TIME_S - RIVAL_TIME_S / r))
