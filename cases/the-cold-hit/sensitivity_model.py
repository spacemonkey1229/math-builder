#!/usr/bin/env python3
"""
Sensitivity model -- The Cold Hit.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is an ASSUMPTION
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the twist applied

Metric: cold-hit cases closed per detective-and-lab hour. A = Refer on Match,
B = Hold for Corroboration.

FLEX scoping: RMP_locus (0.075, Appendix C / S3), N_state and N_national
(Appendix B / S1, S2) are REAL CITED figures, not assumptions the case author
chose -- they are stress-tested by Tier 2 probe 6 (data decay), not swept here.
Only the five disclosed Modeling Assumptions (Appendix F, MA1-MA5) are in
FLEX: annual caseload, the partial-profile share, and the three per-case time
costs. k_loci (8) is a scenario construction fixed by the case's evidence
description, not a dial a facilitator would plausibly flex in discussion --
excluded from FLEX for the same reason H/R/U were excluded in the Manifest
Split sibling model (it changes what case is being described, not a stated
uncertainty about a real quantity).
"""

RMP_LOCUS = 0.075          # Appendix C / S3 -- cited, not FLEX
K_LOCI = 8                  # Appendix C -- scenario construction, not FLEX
N_STATE = 3_368_310         # Appendix B / S1 -- cited, not FLEX
N_NATIONAL = 18_000_000     # Appendix B / S2 -- cited, not FLEX

PARAMS = {
    # --- Appendix D / Appendix F, MA1-MA2 -------------------------------
    "n_hits": 60,            # cold-hit cases reviewed this year
    "frac_partial": 0.6,     # share of this year's hits from a partial profile
    # --- Appendix E / Appendix F, MA3-MA5 -------------------------------
    "h_base": 6.0,           # base investigative review, hours/case, both policies
    "h_corrob": 3.0,         # Policy B corroboration step, hours/case
    "h_rework": 200.0,       # Policy A rework cost per false referral, hours
    # --- the Twist (FACILITATOR.md): grant-funded degraded-backlog sweep -
    "twist_frac_partial": 1.0,   # every hit this year comes from a partial profile
}

FLEX = [
    "n_hits",       # MA1
    "frac_partial", # MA2
    "h_base",       # MA3
    "h_corrob",     # MA4
    "h_rework",     # MA5
]


def _rmp(k=K_LOCI):
    return RMP_LOCUS ** k


def _dmp(n_database, k=K_LOCI):
    return n_database * _rmp(k)


def _details(n_hits, frac_partial, h_base, h_corrob, h_rework):
    """Full breakdown -- NOT the evaluate() contract return shape (that must be
    exactly {"A":.., "B":..}, see the 2026-09-18 fix note below). Used by
    __main__ and by evaluate()/evaluate_twist() internally."""
    dmp_national = _dmp(N_NATIONAL)
    n_false_A = n_hits * frac_partial * dmp_national
    total_A = n_hits * h_base + n_false_A * h_rework
    total_B = n_hits * h_base + n_hits * h_corrob
    a_rate = n_hits / total_A if total_A else float("nan")
    b_rate = n_hits / total_B if total_B else float("nan")
    return {"A": a_rate, "B": b_rate, "n_false_A": n_false_A,
            "total_A_hours": total_A, "total_B_hours": total_B,
            "dmp_state": _dmp(N_STATE), "dmp_national": dmp_national}


def evaluate(params=None):
    """CONTRACT: returns EXACTLY {"A": metric, "B": metric} -- no extra keys.
    Fixed 2026-09-18: tier2_probes.py's probe_sensitivity picks the winner via
    max(base, key=base.get)/min(...) over the WHOLE returned dict, not just
    'A'/'B'. An earlier draft of this file returned diagnostic extras
    (total_A_hours etc.) alongside 'A'/'B', and because those hour totals are
    numerically larger than the A/B rates, max()/min() silently picked
    'total_A_hours'/'total_B_hours' as the 'winner' and 'loser' instead of the
    real metric -- producing nonsense multi-million-percent margins. Use
    _details() (below) for the full breakdown; evaluate()/evaluate_twist() only
    ever return the two-key contract shape."""
    p = dict(PARAMS)
    p.update(params or {})
    d = _details(p["n_hits"], p["frac_partial"], p["h_base"], p["h_corrob"], p["h_rework"])
    return {"A": d["A"], "B": d["B"]}


def evaluate_twist(params=None):
    """A grant-funded cold-case initiative specifically clears the most
    degraded backlog first: every one of this year's cold hits (not just
    60%) comes from a partial (8-locus) profile. CONTRACT: returns exactly
    {"A": metric, "B": metric}, same as evaluate() -- see its docstring."""
    p = dict(PARAMS)
    p.update(params or {})
    p["frac_partial"] = p["twist_frac_partial"]
    d = _details(p["n_hits"], p["frac_partial"], p["h_base"], p["h_corrob"], p["h_rework"])
    return {"A": d["A"], "B": d["B"]}


if __name__ == "__main__":
    base = _details(**{k: PARAMS[k] for k in ("n_hits", "frac_partial", "h_base", "h_corrob", "h_rework")})
    tw_params = dict(PARAMS); tw_params["frac_partial"] = PARAMS["twist_frac_partial"]
    tw = _details(**{k: tw_params[k] for k in ("n_hits", "frac_partial", "h_base", "h_corrob", "h_rework")})

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
            print(f"{name:15s} {label:5s} winner={w} margin={m:6.2f}%{flip}{breach}")
