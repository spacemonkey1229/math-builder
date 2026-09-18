#!/usr/bin/env python3
"""
Sensitivity model — The Manifest Split.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is an ASSUMPTION
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the twist applied

Metric: containers cleared per inspector-hour. A = The Combined Lane, B = The
Split Lanes.

FLEX scoping: H, R and U (Appendix B) are disclosed Modeling Assumptions (MA1)
but are NOT included in FLEX. They are constrained to each other (a valid set
system requires max(H,R) <= U <= H+R); an independent +/-50% sweep of any one
of them alone produces mathematically invalid negative intersections for three
of the six combinations (H-50%, R-50%, U+50%), which are reported as a CAVEAT,
not a real sensitivity finding — the same treatment case-readiness/SKILL.md
prescribes for a zero-baseline margin-formula artifact. Only the five
per-container timing assumptions (MA2-MA6) are swept by default; they are
independent dials that do not have this validity constraint.
"""

PARAMS = {
    # --- Appendix B / Appendix D, MA1 (NOT in FLEX -- see docstring) --------
    "H": 90,     # hazmat-flagged containers
    "R": 130,    # reefer-flagged containers
    "U": 195,    # total distinct flagged containers (H union R)
    # --- Appendix C / Appendix D, MA2-MA3: The Combined Lane -----------------
    "t_hazmat_combined": 8.0,   # minutes/container
    "t_reefer_combined": 7.0,   # minutes/container
    # --- Appendix C / Appendix D, MA4-MA5: The Split Lanes --------------------
    "t_hazmat_split": 6.0,      # minutes/container
    "t_reefer_split": 5.0,      # minutes/container
    # --- Appendix C / Appendix D, MA6: re-handle cost -------------------------
    "t_rehandle": 11.0,         # minutes/container, intersection only
    # --- the Twist (FACILITATOR.md): lithium-battery reclassification --------
    "twist_new_hazmat": 30,     # containers moved from R-only into H (subset of R)
}

FLEX = [
    "t_hazmat_combined",   # MA2
    "t_reefer_combined",   # MA3
    "t_hazmat_split",      # MA4
    "t_reefer_split",      # MA5
    "t_rehandle",          # MA6
]


def _metrics(H, R, U, tHA, tRA, tHB, tRB, tmove):
    x = H + R - U  # intersection, by inclusion-exclusion
    total_A_min = tHA * H + tRA * R
    total_B_min = tHB * H + tRB * R + tmove * x
    a_rate = 60.0 * U / total_A_min if total_A_min else float("nan")
    b_rate = 60.0 * U / total_B_min if total_B_min else float("nan")
    return {"A": a_rate, "B": b_rate, "x": x,
            "total_A_hours": total_A_min / 60.0, "total_B_hours": total_B_min / 60.0}


def evaluate(params=None):
    p = dict(PARAMS)
    p.update(params or {})
    return _metrics(p["H"], p["R"], p["U"],
                     p["t_hazmat_combined"], p["t_reefer_combined"],
                     p["t_hazmat_split"], p["t_reefer_split"], p["t_rehandle"])


def evaluate_twist(params=None):
    """A supplemental compliance bulletin reclassifies `twist_new_hazmat`
    previously reefer-only containers as also hazmat (lithium-ion cells shipped
    refrigerated). Those containers are a SUBSET of R, so U is unchanged and H
    rises by exactly that count -- which, by inclusion-exclusion, means the
    intersection x rises by the same amount."""
    p = dict(PARAMS)
    p.update(params or {})
    p["H"] = p["H"] + p["twist_new_hazmat"]
    return _metrics(p["H"], p["R"], p["U"],
                     p["t_hazmat_combined"], p["t_reefer_combined"],
                     p["t_hazmat_split"], p["t_reefer_split"], p["t_rehandle"])


if __name__ == "__main__":
    base = evaluate()
    tw = evaluate_twist()
    def margin(m):
        lo, hi = min(m["A"], m["B"]), max(m["A"], m["B"])
        winner = "A" if m["A"] > m["B"] else ("B" if m["B"] > m["A"] else "TIE")
        return winner, 100.0 * (hi - lo) / lo

    w, m = margin(base)
    print("BASE ", {k: round(v, 3) for k, v in base.items()}, "winner", w, "margin %.2f%%" % m)
    w, m = margin(tw)
    print("TWIST", {k: round(v, 3) for k, v in tw.items()}, "winner", w, "margin %.2f%%" % m)

    print("\n--- FLEX +-50% sweep ---")
    for name in FLEX:
        for factor, label in ((1.5, "+50%"), (0.5, "-50%")):
            p = dict(PARAMS)
            p[name] = p[name] * factor
            r = evaluate(p)
            w, m = margin(r)
            flip = " <-- FLIP" if w != margin(base)[0] else ""
            breach = " <-- CAP BREACH (>20%)" if m > 20.0 else ""
            print(f"{name:20s} {label:5s} winner={w} margin={m:6.2f}%{flip}{breach}")
