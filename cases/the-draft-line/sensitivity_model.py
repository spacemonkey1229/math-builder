#!/usr/bin/env python3
"""
Sensitivity model — The Draft Line.

CONTRACT (skills/case-readiness/SKILL.md, Tier 2 probe 5):
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is an ASSUMPTION
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the twist applied

Metric: net revenue per TEU actually carried (USD/TEU).
A = The Canal Passage. B = The Cape Diversion.

MODEL REVISION (2026-09-18, after Tier 2 probe 1's cold solve): the original
version of this model charged The Cape Diversion's fuel/operating cost only
for its "extra days" over The Canal Passage, treating the two routes' shared
baseline fuel/opex as common and cancelling out. A genuinely fresh cold-solve
subagent read case.md's D3 wording -- "calculate each route's total voyage
net revenue" -- the more natural way: every route burns its own fuel and pays
its own daily operating cost for its OWN full transit time, full stop,
regardless of route. That reading is also more realistic (a ship burns fuel
every day at sea, Suez transit or not) and removes a real, previously
undisclosed convention the case never stated. This version charges each
route its own full fuel + operating cost for its own transit time (Appendix D
figures apply per-day, per route); only The Canal Passage also pays the toll.
The winner and the approximate margin are preserved (previously A by 0.98%,
now A by 0.96%) -- this was a wording/convention fix, not a rebalancing.

FLEX scoping: distance (dist_suez, dist_cape, from S3) and freight revenue per
TEU (rev_per_teu, derived from S4) are real CITED data, not stated assumptions
-- they are NOT included in FLEX (Tier 2 probe 6, data decay, covers them
instead). The Suez charted draft limit (limit_m, from S1) is likewise cited,
real, and excluded. Only the eight genuinely-assumed scenario dials (MA1-MA8)
are swept by default.
"""

PARAMS = {
    # --- Appendix A, cited (S1) -- NOT in FLEX ---------------------------
    "limit_m": 20.1,          # Suez charted max draft, meters
    # --- Appendix B, MA1-MA4 ----------------------------------------------
    "teu_capacity": 18000,    # MA1
    "draft_m": 20.4,          # MA2
    "cm_per_teu": 0.15,       # MA3
    "speed_kn": 20.0,         # MA4
    # --- Appendix C, cited (S3) -- NOT in FLEX -----------------------------
    "dist_suez_nm": 10600.0,
    "dist_cape_nm": 13800.0,
    # --- Appendix D, MA5-MA8 -------------------------------------------------
    "toll_usd": 650000.0,       # MA5
    "fuel_price_per_ton": 600.0,  # MA6
    "fuel_tons_per_day": 200.0,   # MA7
    "opex_per_day": 25000.0,      # MA8
    # --- Appendix D, cited/derived (S4) -- NOT in FLEX ------------------------
    "rev_per_teu": 1813.0,
    # --- the Twist (FACILITATOR.md): expedited-carriage penalty --------------
    "twist_penalty_per_teu": 1800.0,  # disclosed scenario construction
}

FLEX = [
    "teu_capacity",      # MA1
    "draft_m",            # MA2
    "cm_per_teu",          # MA3
    "speed_kn",             # MA4
    "toll_usd",              # MA5
    "fuel_price_per_ton",     # MA6
    "fuel_tons_per_day",       # MA7
    "opex_per_day",              # MA8
]


def _metrics(p, twist_penalty=0.0):
    excess_cm = max(0.0, (p["draft_m"] - p["limit_m"]) * 100.0)
    offload = excess_cm / p["cm_per_teu"] if p["cm_per_teu"] else 0.0
    offload = min(offload, p["teu_capacity"])
    teu_a = p["teu_capacity"] - offload
    teu_b = p["teu_capacity"]

    t_suez_days = (p["dist_suez_nm"] / p["speed_kn"]) / 24.0
    t_cape_days = (p["dist_cape_nm"] / p["speed_kn"]) / 24.0
    extra_days = t_cape_days - t_suez_days

    # Each route pays its OWN fuel + daily operating cost for its OWN full
    # transit time. Only The Canal Passage also pays the toll. Only The
    # Canal Passage's cost is further reduced by the twist penalty (applied
    # to the offloaded TEU).
    cost_a = (p["toll_usd"]
              + p["fuel_tons_per_day"] * p["fuel_price_per_ton"] * t_suez_days
              + p["opex_per_day"] * t_suez_days
              + offload * twist_penalty)
    cost_b = (p["fuel_tons_per_day"] * p["fuel_price_per_ton"] * t_cape_days
              + p["opex_per_day"] * t_cape_days)

    rev_a = teu_a * p["rev_per_teu"]
    rev_b = teu_b * p["rev_per_teu"]
    net_a = rev_a - cost_a
    net_b = rev_b - cost_b

    rate_a = net_a / teu_a if teu_a else float("nan")
    rate_b = net_b / teu_b if teu_b else float("nan")

    return {"A": rate_a, "B": rate_b, "offload_teu": offload,
            "t_suez_days": t_suez_days, "t_cape_days": t_cape_days,
            "extra_days": extra_days, "cost_a": cost_a, "cost_b": cost_b,
            "net_a": net_a, "net_b": net_b}


def evaluate(params=None):
    """Returns EXACTLY {"A": metric, "B": metric} per the case-readiness
    contract. Deliberately does not surface _metrics()'s other diagnostic
    keys here -- Tier 2 probe 4's winner-detection does a naive
    max(dict, key=dict.get) over the WHOLE returned dict, so any extra key
    whose magnitude exceeds the A/B metric (net_a/net_b are ~$28M vs. A/B's
    ~$1,600/TEU) silently hijacks the winner computation. Use full_metrics()
    below for the walkthrough figures FACILITATOR.md and case.json.derived
    need."""
    p = dict(PARAMS)
    p.update(params or {})
    m = _metrics(p)
    return {"A": m["A"], "B": m["B"]}


def full_metrics(params=None):
    """All diagnostic fields -- for reporting/walkthrough use only. Never
    passed to Tier 2 probe 4."""
    p = dict(PARAMS)
    p.update(params or {})
    return _metrics(p)


def evaluate_twist(params=None):
    """A twist grounded in the shipping line's own customer-contract terms: any
    container that misses its booked sailing (the `offload_teu` containers left
    behind under The Canal Passage) triggers a stated expedited-alternate-carriage
    make-good penalty of `twist_penalty_per_teu` per container -- a real
    contractual mechanism (missed-sailing compensation), disclosed as a scenario
    construction since no public source publishes any one line's actual
    make-good rate. Returns EXACTLY {"A": metric, "B": metric}."""
    p = dict(PARAMS)
    p.update(params or {})
    m = _metrics(p, twist_penalty=p["twist_penalty_per_teu"])
    return {"A": m["A"], "B": m["B"]}


def full_metrics_twist(params=None):
    """All diagnostic fields, twist applied -- for reporting/walkthrough use only."""
    p = dict(PARAMS)
    p.update(params or {})
    return _metrics(p, twist_penalty=p["twist_penalty_per_teu"])


if __name__ == "__main__":
    base = full_metrics()
    tw = full_metrics_twist()

    def margin(m):
        lo, hi = min(m["A"], m["B"]), max(m["A"], m["B"])
        winner = "A" if m["A"] > m["B"] else ("B" if m["B"] > m["A"] else "TIE")
        return winner, 100.0 * (hi - lo) / lo if lo else float("nan")

    w, m = margin(base)
    print("BASE ", {k: round(v, 3) for k, v in base.items()}, "winner", w, "margin %.3f%%" % m)
    w, m = margin(tw)
    print("TWIST", {k: round(v, 3) for k, v in tw.items()}, "winner", w, "margin %.3f%%" % m)

    print("\n--- FLEX +-50% sweep ---")
    base_w, _ = margin(base)
    for name in FLEX:
        for factor, label in ((1.5, "+50%"), (0.5, "-50%")):
            p = dict(PARAMS)
            p[name] = p[name] * factor
            r = evaluate(p)
            w, m = margin(r)
            flip = " <-- FLIP" if w != base_w else ""
            breach = " <-- CAP BREACH (>20%)" if m > 20.0 else ""
            print(f"{name:20s} {label:5s} winner={w} margin={m:7.3f}%{flip}{breach}")
