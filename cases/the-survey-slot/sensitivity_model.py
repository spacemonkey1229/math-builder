#!/usr/bin/env python3
"""
Sensitivity model -- The Survey Slot.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is an ASSUMPTION
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the twist applied

Metric: expected confirmed transit detections per hour of telescope time.
A = The Candidate Watch, B = The Twelve-Field Sweep.

FLEX scoping: slot_hours (4), n_fields (12), n_flagged (5) and n_followup (2)
are stated scenario/schedule parameters (Appendix B/D, MA1/MA4/MA5) that shape
the D4 combinatorics deliverable but are NOT swept here -- they are structural
scenario choices, not uncertain real-world dials the primary-metric comparison
turns on. Only the two probability assumptions that directly drive the
A-vs-B rate comparison (MA2, MA3) are in FLEX, per the "Only FLEX[] is swept"
rule -- both are irreducible scenario estimates informed by, but not equal to,
a real cited statistic (S1, S2 in case.json.sources).
"""

PARAMS = {
    # --- Appendix B, MA1 (NOT in FLEX -- structural schedule, not an uncertain dial) ---
    "slot_hours": 4.0,
    "n_fields": 12,
    # --- Appendix C, MA2: The Candidate Watch --------------------------------
    "p_success_candidate": 0.7479,   # informed by S1 (565/2241 TESS TOI false-positive rate)
    # --- Appendix C, MA3: The Twelve-Field Sweep -----------------------------
    "p_field_detection": 0.10,       # informed by S2 (Kepler DR25 ~2.1% per-star yield)
    # --- Appendix D, MA4/MA5 (NOT in FLEX -- feeds D4 combinatorics only) ----
    "n_flagged": 5,
    "n_followup": 2,
    # --- the Twist (FACILITATOR.md): background-contamination alert ---------
    "twist_p_success_candidate": 0.55,
}

FLEX = [
    "p_success_candidate",   # MA2
    "p_field_detection",     # MA3
]


def _metrics(slot_hours, n_fields, p_success_A, p_field_B):
    p_success_A = min(max(p_success_A, 0.0), 1.0)
    p_field_B = min(max(p_field_B, 0.0), 1.0)
    p_atleast1_B = 1.0 - (1.0 - p_field_B) ** n_fields
    a_rate = p_success_A / slot_hours
    b_rate = p_atleast1_B / slot_hours
    return {"A": a_rate, "B": b_rate,
            "p_success_A": p_success_A, "p_atleast1_B": p_atleast1_B}


def evaluate(params=None):
    p = dict(PARAMS)
    p.update(params or {})
    return _metrics(p["slot_hours"], p["n_fields"],
                     p["p_success_candidate"], p["p_field_detection"])


def evaluate_twist(params=None):
    """An archival cross-match flags a faint background star nearly blended
    with the candidate's target star -- exactly the kind of blended-object
    false-positive cause Appendix A already names -- dropping the candidate's
    false-positive-survival probability from the base MA2 value to
    `twist_p_success_candidate`. The Sweep side (B) is unaffected -- its
    fields are unrelated stars, and the twist is entirely about A."""
    p = dict(PARAMS)
    p.update(params or {})
    return _metrics(p["slot_hours"], p["n_fields"],
                     p["twist_p_success_candidate"], p["p_field_detection"])


if __name__ == "__main__":
    base = evaluate()
    tw = evaluate_twist()

    def margin(m):
        lo, hi = min(m["A"], m["B"]), max(m["A"], m["B"])
        winner = "A" if m["A"] > m["B"] else ("B" if m["B"] > m["A"] else "TIE")
        return winner, 100.0 * (hi - lo) / lo

    w, m = margin(base)
    print("BASE ", {k: round(v, 5) for k, v in base.items()}, "winner", w, "margin %.2f%%" % m)
    w, m = margin(tw)
    print("TWIST", {k: round(v, 5) for k, v in tw.items()}, "winner", w, "margin %.2f%%" % m)

    print("\n--- FLEX +-50% sweep ---")
    base_winner = margin(base)[0]
    for name in FLEX:
        for factor, label in ((1.5, "+50%"), (0.5, "-50%")):
            p = dict(PARAMS)
            p[name] = p[name] * factor
            r = evaluate(p)
            w, m = margin(r)
            flip = " <-- FLIP" if w != base_winner else ""
            breach = " <-- CAP BREACH (>20%)" if m > 20.0 else ""
            print(f"{name:22s} {label:5s} winner={w} margin={m:6.2f}%{flip}{breach}")
