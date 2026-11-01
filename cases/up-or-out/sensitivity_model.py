"""Sensitivity model for Up or Out (SPEC section 2 balance test, case-readiness Tier 2 probe 5).

CONTRACT: evaluate(params) -> {"A": metric, "B": metric}, higher wins.
Option A = The Tall Plan (vertical), B = The Wide Plan (horizontal).
The case's primary metric is expected declared cost (lower wins). To keep the probe's margin formula
equal to the case's margin convention (gap divided by the winner's value), the metric returned is
1e9 / expected_cost: (1/lo - 1/hi) / (1/hi) = hi/lo - 1 = (hi - lo) / lo.

MEDIANS[half_width][size] = (Tall median $/sq ft, Wide median $/sq ft) of the cleaned NYC DOB filings
(dataset ic3t-wcy2, pulled 2026-10-28; see data_pull.py), for filings within +/- half_width sq ft of
size. The window itself (half_width) is flexed by using the 25 / 50 / 75 tables.
"""
MEDIANS = {
    25: {100: (1178.571, 604.167), 125: (894.309, 485.353), 150: (697.658, 547.734), 175: (535.368, 484.162), 200: (999.809, 373.547), 225: (897.284, 448.605), 250: (740.741, 420.197), 275: (649.819, 409.197), 300: (548.173, 468.764), 325: (312.692, 439.883), 350: (296.791, 370.44), 375: (294.165, 339.153), 400: (316.655, 360.952), 425: (324.006, 390.698), 450: (318.415, 407.981), 475: (318.665, 436.283), 500: (396.677, 376.569), 525: (322.841, 333.056), 550: (249.455, 368.492), 575: (269.36, 333.333), 600: (267.571, 280.776), 625: (304.338, 324.675), 650: (245.558, 309.598), 675: (215.208, 300.041), 700: (208.343, 243.75), 725: (201.351, 252.0), 750: (202.703, 280.374), 775: (200.799, 269.028), 800: (201.981, 244.2)},
    50: {100: (1092.748, 557.594), 125: (888.489, 575.146), 150: (850.342, 481.837), 175: (905.0, 451.151), 200: (776.467, 451.807), 225: (901.142, 401.152), 250: (718.802, 421.464), 275: (667.272, 437.098), 300: (454.468, 434.406), 325: (312.692, 426.078), 350: (304.878, 373.848), 375: (300.797, 364.205), 400: (311.213, 364.205), 425: (314.814, 390.717), 450: (318.665, 418.502), 475: (332.298, 407.981), 500: (318.665, 397.624), 525: (304.72, 373.691), 550: (291.466, 333.333), 575: (266.819, 318.474), 600: (274.163, 317.494), 625: (265.781, 304.348), 650: (243.986, 316.431), 675: (219.13, 293.071), 700: (202.703, 285.584), 725: (202.703, 272.758), 750: (201.948, 267.789), 775: (202.703, 258.17), 800: (201.441, 258.94)},
    75: {100: (894.309, 564.146), 125: (899.654, 505.378), 150: (906.411, 487.805), 175: (888.489, 460.2), 200: (863.428, 421.941), 225: (675.676, 435.991), 250: (740.741, 419.786), 275: (636.704, 436.92), 300: (481.944, 421.908), 325: (337.407, 391.988), 350: (312.692, 384.948), 375: (314.814, 376.676), 400: (304.878, 386.039), 425: (314.814, 386.364), 450: (329.596, 390.717), 475: (318.665, 392.778), 500: (317.164, 391.356), 525: (291.871, 368.421), 550: (291.12, 338.889), 575: (287.343, 320.603), 600: (265.781, 316.591), 625: (249.819, 314.465), 650: (221.0, 293.071), 675: (216.216, 301.72), 700: (213.904, 283.65), 725: (202.655, 280.541), 750: (202.703, 252.774), 775: (202.115, 258.17), 800: (202.115, 271.808)},
}

PARAMS = {
    "range_lo": 250.0,      # MA2: low end of the architect's range, sq ft
    "range_hi": 450.0,      # MA2: high end, sq ft
    "half_width": 50.0,     # MA4: comparable-filings window, +/- sq ft
    "savings": 150000.0,    # MA1: reported in the memo (D4); does not enter the primary metric
}
STEP = 25  # sizes 25 sq ft apart (MA2/MA3); a convention, not flexed

# Probe 5 flexes the case's stated assumption dials. savings is excluded because it enters no verdict
# (only D4's list of sizes over budget).
FLEX = ["range_lo", "range_hi", "half_width"]


def _table(p):
    hw = int(min((25, 50, 75), key=lambda h: abs(h - p["half_width"])))
    return MEDIANS[hw]


def sizes(p):
    lo = int(round(p["range_lo"] / STEP) * STEP)
    hi = max(lo, int(round(p["range_hi"] / STEP) * STEP))
    return list(range(lo, hi + 1, STEP))


def expected_costs(p):
    t = _table(p)
    s = sizes(p)
    return (sum(x * t[x][0] for x in s) / len(s), sum(x * t[x][1] for x in s) / len(s))


def evaluate(p):
    cv, ch = expected_costs(p)
    return {"A": 1e9 / cv, "B": 1e9 / ch}


def evaluate_twist(p):
    """Twist (FACILITATOR.md): the survey comes back and the addition is exactly 300 sq ft."""
    q = dict(p)
    q["range_lo"] = q["range_hi"] = 300.0
    return evaluate(q)


if __name__ == "__main__":
    cv, ch = expected_costs(PARAMS)
    lo, hi = min(cv, ch), max(cv, ch)
    print(f"expected cost  Tall ${cv:,.0f}  Wide ${ch:,.0f}  winner {'Tall' if cv < ch else 'Wide'}  margin {100*(hi-lo)/lo:.1f}%")
    assert abs(100 * (hi - lo) / lo - 3.2) < 0.1
    print("twist:", {k: round(v, 3) for k, v in evaluate_twist(PARAMS).items()})
    for name in FLEX:
        for m in (0.5, 1.5):
            q = dict(PARAMS); q[name] = PARAMS[name] * m
            e = evaluate(q); w = max(e, key=e.get); l = min(e, key=e.get)
            print(f"{name} x{m}: winner {w} margin {100*(e[w]-e[l])/e[l]:.1f}%")
