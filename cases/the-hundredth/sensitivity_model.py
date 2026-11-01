#!/usr/bin/env python3
"""
Sensitivity model -- The Hundredth.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS, FLEX, evaluate(params) -> {"A": metric, "B": metric}  (higher is better),
    evaluate_twist(params).

Metric: probability that the ruling instrument names the swimmer whose hand truly
reached the wall first, in a close finish whose true first-contact margin c is equally
likely anywhere in [-WINDOW, +WINDOW] seconds (WINDOW is a DEFINITION of "a close
finish" in the case, not a measurement).

Model (see FACILITATOR.md):
  * An instrument with an indecision band b (seconds) misorders any finish whose true
    margin has |c| < b about half the time and orders the rest correctly, so
        P_correct = 1 - b / (2 * WINDOW)         (b <= WINDOW)
  * A = pad ranks.        b_A = |delta_lag|   (the DIFFERENTIAL pad lag; a lag common
                          to both swimmers cancels and contributes nothing).
  * B = video ranks.      b_B = 1/fps + judge_band   (one frame period plus the band a
                          human judge needs to call "first contact" from the footage).

FLEX scoping: delta_lag, judge_band and fps are ASSUMPTIONS (no published lag figure
was found; the 2008 camera and the judge's reading band are not documented in any
source found). WINDOW is a definition and SPEED is a cited/derived figure, so neither
is swept. All three FLEX values are disclosed as "plausible range, not measured".
"""

SPEED = 100.0 / 50.58          # m/s, average speed, derived from the cited winning time

PARAMS = {
    "delta_lag": 0.010,        # s, assumed differential pad lag |l_Cavic - l_Phelps| scenario midpoint
    "judge_band": 0.005,       # s, assumed band for a judge reading first contact off the footage
    "fps": 240.0,              # frames per second of the review footage (scenario value)
    "window": 0.05,            # s, definition of a "close finish" (not flexed)
    # --- the Twist (FACILITATOR.md): only a slower feed clearly shows the wall
    "twist_fps": 60.0,
}

FLEX = ["delta_lag", "judge_band", "fps"]


def _p(band, window):
    return max(0.0, 1.0 - band / (2.0 * window))


def _metrics(delta_lag, judge_band, fps, window):
    a = _p(abs(delta_lag), window)
    b = _p(1.0 / fps + judge_band, window)
    return {"A": a, "B": b}


def evaluate(params=None):
    p = dict(PARAMS)
    p.update(params or {})
    return _metrics(p["delta_lag"], p["judge_band"], p["fps"], p["window"])


def evaluate_twist(params=None):
    """Only a 60 fps feed shows the wall clearly."""
    p = dict(PARAMS)
    p.update(params or {})
    return _metrics(p["delta_lag"], p["judge_band"], p["twist_fps"], p["window"])


def _margin(m):
    lo, hi = min(m["A"], m["B"]), max(m["A"], m["B"])
    w = "A" if m["A"] > m["B"] else ("B" if m["B"] > m["A"] else "TIE")
    return w, 100.0 * (hi - lo) / lo


if __name__ == "__main__":
    base, tw = evaluate(), evaluate_twist()
    print("BASE ", {k: round(v, 4) for k, v in base.items()}, *_margin(base))
    print("TWIST", {k: round(v, 4) for k, v in tw.items()}, *_margin(tw))
    print("speed m/s %.4f ; cm per 0.01 s %.3f" % (SPEED, SPEED * 1.0))
    for fps in (30, 60, 240, 1000):
        print("fps %4d  frame %.4f s = %.2f cm" % (fps, 1 / fps, SPEED * 100 / fps))
    print("break-even delta_lag = 1/fps + judge_band = %.5f s" % (1 / PARAMS["fps"] + PARAMS["judge_band"]))
    bw = _margin(base)[0]
    for name in FLEX:
        for f, lab in ((1.5, "+50%"), (0.5, "-50%")):
            p = dict(PARAMS); p[name] *= f
            w, m = _margin(evaluate(p))
            print(f"{name:10s} {lab:5s} winner={w} margin={m:6.2f}%" + (" <-- FLIP" if w != bw else ""))
