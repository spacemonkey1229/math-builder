"""Sensitivity model for Feedback (SPEC §2 balance test, case-readiness Tier 2 probes 4 and 5).

WHAT THIS FILE IS FOR
----------------------
Reproduces, from the case document alone, every number the case claims: each wedge's rectangular
position converted to polar coordinates relative to the mic's on-axis heading; the cardioid
pattern-rejection dB at that angle; the inverse-square-law distance-term dB; the combined
gain-before-feedback (GBF) score at every checked blocking moment (static verse, cross-start,
cross-end); each wedge's worst (minimum) GBF across those moments; the margin; and the Twist
(a fourth checked moment, the closing tableau mark, revealed only during the Socratic discussion,
not present in the student packet).

WHAT IS SOURCED AND WHAT IS ASSUMED
------------------------------------
Cardioid polar equation g(theta)=0.5(1+cos theta) ... SOURCED  case.md Appendix B  [S1]
Distance-term formula 20*log10(r) (inverse sq law) .. SOURCED  case.md Appendix D  [S2]
PAG calculation shape (corroboration only) .......... SOURCED  case.md Appendix D  [S3]
Wedge positions (House-Left, House-Right) ........... ASSUMED  case.md Appendix E  MA1
Mic orientation held fixed throughout ............... ASSUMED  case.md Appendix E  MA2 (structural, non-numeric, not swept)
Bridge-cross start/end/duration ..................... ASSUMED  case.md Appendix E  MA3
Checked-moments-only, identical room/PA/mic-count ... ASSUMED  case.md Appendix E  MA4 (structural, non-numeric, not swept)
Twist tableau mark (facilitator-only) ............... ASSUMED  FACILITATOR.md only, disclosed there

FLEX[] lists only the ASSUMED numeric dials (MA1's four wedge coordinates, MA3's four cross
coordinates), per case-readiness's rule that probe 5 stress-tests stated assumptions while probe 6
stress-tests cited/sourced facts. The cardioid equation and the distance-term formula are SOURCED,
not swept here.

THE TWIST
---------
evaluate_twist() adds a fourth checked moment -- a closing tableau mark at (1, 4) ft, held for the
last several seconds of the number -- revealed only during the Socratic discussion, not part of
the student packet's own Challenge 3 deliverables. It flips the base verdict: House-Left's worst
moment becomes this new tableau mark (14.234 dB), which is now *worse* than House-Right's floor
(15.563 dB, unchanged), so the recommendation flips from A to B.
"""
import math

# --- SOURCED: cardioid polar equation, case.md Appendix B [S1] ---------------------------------
def cardioid_gain(theta_deg):
    """Normalized cardioid gain g(theta) = 0.5*(1+cos(theta)), theta measured off on-axis (0-180)."""
    return 0.5 * (1 + math.cos(math.radians(theta_deg)))


def pattern_rejection_db(theta_deg):
    """SOURCED [S1]: -20*log10(g(theta)). theta=180 (null) is a true math singularity; not swept."""
    g = cardioid_gain(theta_deg)
    if g <= 0:
        return math.inf
    return -20 * math.log10(g)


def rect_to_polar(x, y):
    """Standard rectangular -> polar conversion. +x axis = mic on-axis heading (case.md Appendix A)."""
    r = math.hypot(x, y)
    theta = abs(math.degrees(math.atan2(y, x)))
    return r, theta


def distance_term_db(r_ft):
    """SOURCED [S2]: 20*log10(r), r relative to a 1 ft reference (cancels in every A-vs-B comparison).
    r_ft <= 0 is a degenerate case (a flex that puts the monitor exactly on the mic's own position)
    and is reported as -inf: physically, a monitor coincident with the mic gives no gain-before-
    feedback headroom at all, which is the correct (if pathological) reading, not a bug to hide."""
    if r_ft <= 0:
        return -math.inf
    return 20 * math.log10(r_ft)


def gbf_score(monitor_xy, mic_xy):
    """Combined GBF score (case.md Appendix D) for a monitor at monitor_xy, mic at mic_xy."""
    dx = monitor_xy[0] - mic_xy[0]
    dy = monitor_xy[1] - mic_xy[1]
    r, theta = rect_to_polar(dx, dy)
    return distance_term_db(r) + pattern_rejection_db(theta)


# --- ASSUMED: case.md Appendix E ----------------------------------------------------------------
PARAMS = {
    "house_left_x": 6.0,   # MA1
    "house_left_y": 5.0,   # MA1
    "house_right_x": 0.0,  # MA1
    "house_right_y": 6.0,  # MA1
    "cross_start_x": 2.0,  # MA3
    "cross_start_y": 1.0,  # MA3
    "cross_end_x": 0.0,    # MA3
    "cross_end_y": 3.0,    # MA3
    "cross_duration_s": 4.0,  # MA3 (does not affect GBF scores; kept for the parametric-equation deliverable)
}

FLEX = [
    "house_left_x", "house_left_y",
    "house_right_x", "house_right_y",
    "cross_start_x", "cross_start_y",
    "cross_end_x", "cross_end_y",
]

# Facilitator-only twist point (revealed only during discussion; NOT in PARAMS/FLEX,
# because it is new information dropped at the twist, not a stated case assumption a Hero
# ever sees or could flex against).
TWIST_TABLEAU = (1.0, 4.0)


def _checked_moments(params):
    verse = (0.0, 0.0)
    start = (params["cross_start_x"], params["cross_start_y"])
    end = (params["cross_end_x"], params["cross_end_y"])
    return {"verse": verse, "cross_start": start, "cross_end": end}


def evaluate(params):
    """Base case: worst-case GBF per option across the three student-facing checked moments.
    Returns {"A": gbf_dB, "B": gbf_dB} -- higher is better (safer)."""
    A = (params["house_left_x"], params["house_left_y"])
    B = (params["house_right_x"], params["house_right_y"])
    moments = _checked_moments(params)
    worst_a = min(gbf_score(A, mic) for mic in moments.values())
    worst_b = min(gbf_score(B, mic) for mic in moments.values())
    return {"A": worst_a, "B": worst_b}


def evaluate_twist(params):
    """Twist: add the closing tableau mark as a fourth checked moment (facilitator-only, revealed
    mid-discussion). Returns {"A": gbf_dB, "B": gbf_dB} under this expanded moment set."""
    A = (params["house_left_x"], params["house_left_y"])
    B = (params["house_right_x"], params["house_right_y"])
    moments = _checked_moments(params)
    moments["twist_tableau"] = TWIST_TABLEAU
    worst_a = min(gbf_score(A, mic) for mic in moments.values())
    worst_b = min(gbf_score(B, mic) for mic in moments.values())
    return {"A": worst_a, "B": worst_b}


def _margin(result):
    a, b = result["A"], result["B"]
    hi, lo = max(a, b), min(a, b)
    winner = "A" if a > b else ("B" if b > a else "TIE")
    margin_pct = 100.0 * (hi - lo) / lo if lo else float("inf")
    return winner, margin_pct


if __name__ == "__main__":
    base = evaluate(PARAMS)
    w, m = _margin(base)
    print("BASE  A={:.4f} dB  B={:.4f} dB  winner={}  margin={:.2f}%".format(base["A"], base["B"], w, m))

    twist = evaluate_twist(PARAMS)
    wt, mt = _margin(twist)
    print("TWIST A={:.4f} dB  B={:.4f} dB  winner={}  margin={:.2f}%".format(twist["A"], twist["B"], wt, mt))

    print("\n--- +/-50% flex sweep on FLEX[] (one at a time) ---")
    for key in FLEX:
        for sign, label in ((0.5, "-50%"), (1.5, "+50%")):
            p = dict(PARAMS)
            p[key] = PARAMS[key] * sign
            r = evaluate(p)
            fw, fm = _margin(r)
            flips = (fw != w) and w in ("A", "B") and fw in ("A", "B")
            print(f"  {key:16s} {label:5s} -> A={r['A']:.3f} B={r['B']:.3f} winner={fw} margin={fm:.2f}%"
                  f"{'  *** FLIPS ***' if flips else ''}")
