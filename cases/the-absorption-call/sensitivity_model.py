#!/usr/bin/env python3
"""
Sensitivity model — The Absorption Call.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is an ASSUMPTION
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the twist applied

Metric: "closeness score" = 1 - |ratio - 1|, where ratio is an option's achieved
RT60 divided by the target RT60 for the use it is built to serve (speech target
for A, music target for B). A perfect hit (ratio == 1) scores 1.0; the score
falls as the option misses its own target in either direction. Higher is
better, matching the contract.

Sabine's equation (SOURCED, S1/S2): RT60 = 0.161 * V / A_sabins.
Room geometry and baseline surfaces: Appendix A. Panel coefficients: Appendix B.
Targets: Appendix C. All non-FLEX constants below are either the sourced
Sabine constant, sourced absorption coefficients, or the fixed room-geometry
Modeling Assumption (MA1, which scales both options equally and is therefore
excluded from FLEX exactly as case-readiness/SKILL.md prescribes for a
constraint that cannot by itself change which option wins).
"""

FT_TO_M = 0.3048  # NIST SP811, S6 -- not flexed, exact constant

PARAMS = {
    # --- Appendix A, MA1 (room geometry -- NOT in FLEX, scales A and B equally)
    "room_length_ft": 40.0,
    "room_width_ft": 30.0,
    "room_height_ft": 16.0,
    # --- Appendix A, sourced Sabine constant (S1/S2) --------------------------
    "sabine_k": 0.161,
    # --- Appendix A, sourced baseline absorption coefficients (S3) -----------
    "alpha_floor": 0.09,
    "alpha_ceiling": 0.04,
    "alpha_walls": 0.07,       # side walls, stage wall, and rear-wall baseline
    # --- Appendix B, sourced absorptive-panel coefficient (S4) ---------------
    "alpha_absorptive": 1.05,
    # --- Appendix B, MA2: diffusive-panel coefficient (ASSUMPTION, FLEX) -----
    "alpha_diffusive": 0.48,
    # --- Appendix C: targets ---------------------------------------------------
    "target_speech": 1.05,     # sourced range midpoint (S5), NOT flexed
    "target_music": 1.6,       # MA3 (ASSUMPTION, FLEX)
}

FLEX = [
    "alpha_diffusive",   # MA2 -- the case's one load-bearing assumption
    "target_music",       # MA3
]


def _geometry(p):
    L = p["room_length_ft"] * FT_TO_M
    W = p["room_width_ft"] * FT_TO_M
    H = p["room_height_ft"] * FT_TO_M
    V = L * W * H
    floor = L * W
    ceiling = L * W
    side_walls = 2 * (W * H)
    stage_wall = L * H
    rear_wall = L * H
    return V, floor, ceiling, side_walls, stage_wall, rear_wall


def _rt60(V, sabins, k):
    return k * V / sabins if sabins else float("nan")


def _closeness(rt60, target):
    return 1.0 - abs(rt60 / target - 1.0)


def evaluate(params=None):
    p = dict(PARAMS)
    p.update(params or {})
    V, floor, ceiling, side_walls, stage_wall, rear_wall = _geometry(p)

    baseline = (floor * p["alpha_floor"] + ceiling * p["alpha_ceiling"]
                + side_walls * p["alpha_walls"] + stage_wall * p["alpha_walls"]
                + rear_wall * p["alpha_walls"])
    rear_baseline_sabins = rear_wall * p["alpha_walls"]

    sabins_A = baseline - rear_baseline_sabins + rear_wall * p["alpha_absorptive"]
    sabins_B = baseline - rear_baseline_sabins + rear_wall * p["alpha_diffusive"]

    rt60_A = _rt60(V, sabins_A, p["sabine_k"])
    rt60_B = _rt60(V, sabins_B, p["sabine_k"])

    score_A = _closeness(rt60_A, p["target_speech"])
    score_B = _closeness(rt60_B, p["target_music"])

    return {"A": score_A, "B": score_B}


def evaluate_twist(params=None):
    """The twist (FACILITATOR.md): a previously unconfirmed unamplified booking
    makes the acoustic/amplified calendar split roughly even. Modeled here as
    both options being judged against the SAME blended target -- the average
    of the speech and music targets -- rather than each against its own target,
    since "dominant use" no longer cleanly picks one target over the other."""
    p = dict(PARAMS)
    p.update(params or {})
    V, floor, ceiling, side_walls, stage_wall, rear_wall = _geometry(p)

    baseline = (floor * p["alpha_floor"] + ceiling * p["alpha_ceiling"]
                + side_walls * p["alpha_walls"] + stage_wall * p["alpha_walls"]
                + rear_wall * p["alpha_walls"])
    rear_baseline_sabins = rear_wall * p["alpha_walls"]

    sabins_A = baseline - rear_baseline_sabins + rear_wall * p["alpha_absorptive"]
    sabins_B = baseline - rear_baseline_sabins + rear_wall * p["alpha_diffusive"]

    rt60_A = _rt60(V, sabins_A, p["sabine_k"])
    rt60_B = _rt60(V, sabins_B, p["sabine_k"])

    blended_target = (p["target_speech"] + p["target_music"]) / 2.0
    score_A = _closeness(rt60_A, blended_target)
    score_B = _closeness(rt60_B, blended_target)

    return {"A": score_A, "B": score_B}


if __name__ == "__main__":
    base = evaluate()
    tw = evaluate_twist()

    def margin(m):
        lo, hi = min(m["A"], m["B"]), max(m["A"], m["B"])
        winner = "A" if m["A"] > m["B"] else ("B" if m["B"] > m["A"] else "TIE")
        return winner, 100.0 * (hi - lo) / hi if hi else 0.0

    w, m = margin(base)
    print("BASE ", {k: round(v, 4) for k, v in base.items()}, "winner", w, "margin %.2f%%" % m)
    w, m = margin(tw)
    print("TWIST", {k: round(v, 4) for k, v in tw.items()}, "winner", w, "margin %.2f%%" % m)

    print("\n--- FLEX +-50% sweep ---")
    base_winner, _ = margin(base)
    for name in FLEX:
        for factor, label in ((1.5, "+50%"), (0.5, "-50%")):
            p = dict(PARAMS)
            p[name] = p[name] * factor
            r = evaluate(p)
            w, m = margin(r)
            flip = " <-- FLIP" if w != base_winner else ""
            breach = " <-- CAP BREACH (>20%)" if m > 20.0 else ""
            print(f"{name:16s} {label:5s} winner={w} margin={m:6.2f}%{flip}{breach}")
