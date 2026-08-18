"""Sensitivity model for Redrawing Lines (SPEC section 2 balance test, case-readiness Tier 2 probe 5).

Every number below is either SOURCED (a citation id from case.md Appendix G, in the comment) or
ASSUMED (a Modeling Assumption id from case.md Appendix H). FLEX lists the ASSUMED subset only --
probe 5 sweeps those, because SPEC section 2 asks for sensitivity to STATED ASSUMPTIONS. The
county populations and the county adjacency list are U.S. Census Bureau data; halving a Census
count is not a sensitivity test, it is a different state. Cited data is stress-tested by probe 6.

The primary metric is COUNTY-LINE CROSSINGS and it is LOWER-is-better, while the probe-5 contract
is higher-wins. evaluate() therefore returns (a_score + b_score - score) for each plan, computed
fresh inside the call. That keeps both values positive and collapses the framework's generic
(max-min)/min margin formula back to exactly (worse-better)/better -- the same definition case.md
states -- rather than silently reporting a different margin. _selftest() asserts this every run.

Run directly to reproduce every derived figure in the case:
    python3 cases/redrawing-lines/sensitivity_model.py
"""
import itertools
import math

# --- SOURCED: 2020 Census P.L. 94-171 resident population by county [S2] ------------------
COUNTY_POP = {
    "Androscoggin": 111139, "Aroostook": 67105, "Cumberland": 303069, "Franklin": 29456,
    "Hancock": 55478, "Kennebec": 123642, "Knox": 40607, "Lincoln": 35237,
    "Oxford": 57777, "Penobscot": 152199, "Piscataquis": 16800, "Sagadahoc": 36699,
    "Somerset": 50477, "Waldo": 39607, "Washington": 31095, "York": 211972,
}

# --- SOURCED: U.S. Census Bureau County Adjacency File 2025, Maine rows [S4] ---------------
ADJACENCY = {
    "Androscoggin": ["Cumberland", "Franklin", "Kennebec", "Oxford", "Sagadahoc"],
    "Aroostook":    ["Penobscot", "Piscataquis", "Somerset", "Washington"],
    "Cumberland":   ["Androscoggin", "Oxford", "Sagadahoc", "York"],
    "Franklin":     ["Androscoggin", "Kennebec", "Oxford", "Somerset"],
    "Hancock":      ["Knox", "Penobscot", "Waldo", "Washington"],
    "Kennebec":     ["Androscoggin", "Franklin", "Lincoln", "Sagadahoc", "Somerset", "Waldo"],
    "Knox":         ["Hancock", "Lincoln", "Waldo"],
    "Lincoln":      ["Kennebec", "Knox", "Sagadahoc", "Waldo"],
    "Oxford":       ["Androscoggin", "Cumberland", "Franklin", "York"],
    "Penobscot":    ["Aroostook", "Hancock", "Piscataquis", "Somerset", "Waldo", "Washington"],
    "Piscataquis":  ["Aroostook", "Penobscot", "Somerset"],
    "Sagadahoc":    ["Androscoggin", "Cumberland", "Kennebec", "Lincoln"],
    "Somerset":     ["Aroostook", "Franklin", "Kennebec", "Penobscot", "Piscataquis", "Waldo"],
    "Waldo":        ["Hancock", "Kennebec", "Knox", "Lincoln", "Penobscot", "Somerset"],
    "Washington":   ["Aroostook", "Hancock", "Penobscot"],
    "York":         ["Cumberland", "Oxford"],
}
BORDERS = sorted({tuple(sorted((a, b))) for a, ns in ADJACENCY.items() for b in ns})

# --- ASSUMED (case.md Appendix H MA5): the one Maine county-to-county boundary that a Hero may
# argue is not a border, because it runs through water. The Census file [S4] lists it like any
# other and assigns it a boundary length; this case counts it, and MA5 states what excluding it
# would do instead.
WATER_BORDERS = {("Hancock", "Knox")}

# The five counties wholly inside the southern district in both plans (MA3's staff rule).
CORE = ("Cumberland", "Knox", "Lincoln", "Sagadahoc", "York")

PARAMS = {
    # --- ASSUMED (case.md Appendix H) ---
    "severance_weight": 1.0,                 # MA1 -- crossings charged for a county the line runs through
    "split_county_assignment": "majority",   # MA2 -- non-numeric; "majority" or "minority"
    "shortlist_rule": "closest-to-equal",    # MA3 -- non-numeric; which Appendix D column picked Option B
    "water_boundaries": "counted",           # MA5 -- non-numeric; "counted" or "excluded"
    "whole_county_addon": "Hancock",         # MA3's output -- the whole-county plan on the table
    "twist_addon": "Oxford",                 # the fewest-crossings plan a floor motion puts back on

    # --- SOURCED (case.md Appendix G) ---
    "state_resident_pop": 1362359,           # S2 -- Maine 2020 Census resident population
    "seats": 2,                              # S1 -- U.S. House seats apportioned to Maine
    "kennebec_south_share": 53595,           # S3 + S5 -- the 12 statutory municipalities, cross-checked to S6
    "enacted_south_pop": 681179,             # S6 -- Maine SOS, enacted CD-1
    "enacted_north_pop": 681180,             # S6 -- Maine SOS, enacted CD-2
}

FLEX = ["severance_weight", "split_county_assignment", "shortlist_rule", "water_boundaries"]


# ----------------------------------------------------------------- geometry helpers ----
def crossings(south_counties, p, severed=None):
    """County-line crossings for a plan, per case.md Appendix B + Appendix H MA1/MA2.

    south_counties -- the set of whole counties in the southern district, ALREADY resolved for a
                      divided county under MA2 (use plan_kennebec_split() rather than passing a
                      divided county here by hand).
    severed        -- name of the county the line runs through, or None.
    """
    south = set(south_counties)
    if p.get("water_boundaries", "counted") == "excluded":
        border_list = [e for e in BORDERS if e not in WATER_BORDERS]
    elif p.get("water_boundaries", "counted") == "counted":
        border_list = list(BORDERS)
    else:
        raise ValueError("water_boundaries must be 'counted' or 'excluded'")
    along = [f"{a}-{b}" for a, b in border_list if (a in south) != (b in south)]
    score = len(along) + (p["severance_weight"] if severed else 0.0)
    return {"score": score, "borders_along": along, "n_borders_along": len(along),
            "severed": severed}


def plan_kennebec_split(p):
    """Option A -- Maine's enacted plan [S5]. Kennebec is divided; MA2 assigns it, for the border
    count only, to whichever district holds more of its people."""
    south_share = p["kennebec_south_share"]
    north_share = COUNTY_POP["Kennebec"] - south_share
    if p["split_county_assignment"] == "majority":
        ken_side = "south" if south_share > north_share else "north"
    elif p["split_county_assignment"] == "minority":
        ken_side = "north" if south_share > north_share else "south"
    else:
        raise ValueError("split_county_assignment must be 'majority' or 'minority'")
    south = set(CORE) | ({"Kennebec"} if ken_side == "south" else set())
    c = crossings(south, p, severed="Kennebec")
    c.update({"south_pop": p["enacted_south_pop"], "north_pop": p["enacted_north_pop"],
              "kennebec_south": south_share, "kennebec_north": north_share,
              "kennebec_counted_in": ken_side, "counties_divided": 1})
    return c


def plan_whole_county(p, add_on):
    """A whole-county plan: the five-county core plus exactly one more whole county."""
    south = set(CORE) | {add_on}
    sp = sum(COUNTY_POP[c] for c in south)
    c = crossings(south, p, severed=None)
    c.update({"south_pop": sp, "north_pop": p["state_resident_pop"] - sp,
              "kennebec_south": 0, "kennebec_north": COUNTY_POP["Kennebec"],
              "counties_divided": 0, "add_on": add_on})
    return c


def ideal_district(p):
    return p["state_resident_pop"] / p["seats"]


def deviation(plan, p):
    """Deviation from the ideal, per district and as the total range, in people and percent."""
    ideal = ideal_district(p)
    per = abs(plan["south_pop"] - ideal)
    rng = abs(plan["south_pop"] - plan["north_pop"])
    return {"per_district": per, "per_district_pct": 100.0 * per / ideal,
            "total_range": rng, "total_range_pct": 100.0 * rng / ideal}


# ----------------------------------------------------------- the two plans on the table ----
def scoreboard(p):
    a = plan_kennebec_split(p)
    b = plan_whole_county(p, p["whole_county_addon"])
    return {"A": a, "B": b}


def evaluate(p):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. See module docstring for the transform."""
    s = scoreboard(p)
    tot = s["A"]["score"] + s["B"]["score"]
    return {"A": tot - s["A"]["score"], "B": tot - s["B"]["score"]}


def evaluate_twist(p):
    """The twist (FACILITATOR.md): counsel rules that the whole-county option may be swapped for
    the land-only alternative, Oxford. Every figure comes straight from Appendix A and Appendix B
    -- nothing new is assumed. Option A is untouched."""
    a = plan_kennebec_split(p)
    b = plan_whole_county(p, p["twist_addon"])
    tot = a["score"] + b["score"]
    return {"A": tot - a["score"], "B": tot - b["score"]}


# --------------------------------------------------- Appendix F: the screening count ----
def screening_counts():
    """Reproduces Appendix F. 2^16 assignments by the Fundamental Counting Principle; 65,534 once
    the two empty-district assignments are dropped; and the number in which BOTH districts are one
    connected piece on the Appendix B border list."""
    names = sorted(COUNTY_POP)
    n = len(names)

    def connected(S):
        S = set(S)
        if not S:
            return False
        stack = [next(iter(S))]
        seen = {stack[0]}
        while stack:
            x = stack.pop()
            for y in ADJACENCY[x]:
                if y in S and y not in seen:
                    seen.add(y)
                    stack.append(y)
        return seen == S

    contig = 0
    for m in range(1, 2 ** n - 1):
        A = {names[i] for i in range(n) if m >> i & 1}
        if connected(A) and connected(set(names) - A):
            contig += 1
    return {"fcp_total": 2 ** n, "non_empty": 2 ** n - 2,
            "contiguous_unordered": contig // 2, "contiguous_labelled": contig,
            "binomial_row": [math.comb(n, j) for j in range(n + 1)]}


# ------------------------------------------------------------------------- selftest ----
def _selftest():
    p = dict(PARAMS)
    s = scoreboard(p)
    a_sc, b_sc = s["A"]["score"], s["B"]["score"]
    raw_margin = 100.0 * (max(a_sc, b_sc) - min(a_sc, b_sc)) / min(a_sc, b_sc)
    ev = evaluate(p)
    win = max(ev, key=ev.get)
    lose = min(ev, key=ev.get)
    ev_margin = 100.0 * (ev[win] - ev[lose]) / ev[lose]
    assert win == "A", f"expected A to win the crossings metric, got {win}"
    assert abs(ev_margin - raw_margin) < 0.01, f"transform drift: {ev_margin} vs {raw_margin}"
    assert s["A"]["south_pop"] + s["A"]["north_pop"] == PARAMS["state_resident_pop"]
    assert sum(COUNTY_POP.values()) == PARAMS["state_resident_pop"], "county sum != state total"
    assert sum(COUNTY_POP[c] for c in CORE) == 627584
    assert len(BORDERS) == 34
    assert abs(raw_margin - 10.0) < 0.05, f"stated margin is 10.0%, model says {raw_margin}"
    # MA2 flipped: B wins, and the case is still inside SPEC section 2's 20% cap either way.
    q = dict(p); q["split_county_assignment"] = "minority"
    sq = scoreboard(q)
    assert sq["A"]["score"] == 12 and sq["B"]["score"] == 11
    # MA5 flipped: the ranking holds but the margin goes past the cap, in A's favour.
    r = dict(p); r["water_boundaries"] = "excluded"
    sr = scoreboard(r)
    assert sr["A"]["score"] == 9 and sr["B"]["score"] == 11
    return raw_margin


if __name__ == "__main__":
    p = dict(PARAMS)
    ideal = ideal_district(p)
    print(f"Maine resident population {p['state_resident_pop']:,}   seats {p['seats']}   "
          f"ideal district {ideal:,.1f}")
    print(f"five-county core {sum(COUNTY_POP[c] for c in CORE):,}   "
          f"short of ideal by {ideal - sum(COUNTY_POP[c] for c in CORE):,.1f}")
    print(f"distinct county borders: {len(BORDERS)}\n")

    for label, plan in (("A  The Kennebec Split", plan_kennebec_split(p)),
                        ("B  The Hancock Line", plan_whole_county(p, p["whole_county_addon"]))):
        d = deviation(plan, p)
        print(f"{label}")
        print(f"    south {plan['south_pop']:,}  north {plan['north_pop']:,}")
        print(f"    deviation/district {d['per_district']:,.1f} ({d['per_district_pct']:.6f}%)   "
              f"total range {d['total_range']:,.0f} ({d['total_range_pct']:.4f}%)")
        print(f"    borders along ({plan['n_borders_along']}): {', '.join(plan['borders_along'])}")
        print(f"    counties divided {plan['counties_divided']}   CROSSINGS {plan['score']:g}\n")

    margin = _selftest()
    print(f"PRIMARY METRIC margin (county-line crossings): {margin:.2f}%  -- A wins\n")

    print("Appendix D — one-county add-ons to the core:")
    for c in sorted({y for x in CORE for y in ADJACENCY[x] if y not in CORE}):
        pl = plan_whole_county(p, c)
        d = deviation(pl, p)
        print(f"    +{c:13s} south {pl['south_pop']:>9,}  north {pl['north_pop']:>9,}  "
              f"range {d['total_range']:>8,.0f} ({d['total_range_pct']:6.4f}%)  "
              f"crossings {pl['score']:g}")

    tw = evaluate_twist(p)
    ob = plan_whole_county(p, p["twist_addon"])
    do = deviation(ob, p)
    print(f"\nTWIST (substitute {p['twist_addon']} for {p['whole_county_addon']}): B crossings "
          f"{ob['score']:g}, total range {do['total_range']:,.0f} ({do['total_range_pct']:.4f}%)")
    print(f"    evaluate_twist winner: {max(tw, key=tw.get)}  (base winner: A)")
    print("\nMA1 tie point: A = 9 + w, B = 11, so the two plans tie at severance weight w = 2;")
    print("    below 2 The Kennebec Split scores better, above 2 The Hancock Line does.")
    for w in (0.0, 0.5, 1.0, 1.5, 2.0, 2.5):
        q = dict(p); q["severance_weight"] = w
        sq = scoreboard(q)
        a_, b_ = sq["A"]["score"], sq["B"]["score"]
        win = "A" if a_ < b_ else ("B" if b_ < a_ else "TIE")
        print(f"    w={w:.1f}  A={a_:5.1f}  B={b_:5.1f}  winner {win}  "
              f"margin {abs(a_-b_)/min(a_,b_)*100:5.1f}%")

    for label, key, val in (("MA2 counter-check (count Kennebec on the minority side instead)",
                             "split_county_assignment", "minority"),
                            ("MA5 counter-check (drop the Hancock-Knox water boundary)",
                             "water_boundaries", "excluded")):
        print(f"\n{label}:")
        q = dict(p); q[key] = val
        sq = scoreboard(q)
        a_, b_ = sq["A"]["score"], sq["B"]["score"]
        win = "A" if a_ < b_ else ("B" if b_ < a_ else "TIE")
        print(f"    A crossings {a_:g}  B crossings {b_:g}  winner {win}  "
              f"margin {100.0*(max(a_,b_)-min(a_,b_))/min(a_,b_):.1f}%")

    sc = screening_counts()
    print(f"\nAppendix F: FCP total {sc['fcp_total']:,}   non-empty {sc['non_empty']:,}   "
          f"both districts contiguous {sc['contiguous_labelled']:,}")
    print(f"    binomial row C(16,j): {sc['binomial_row']}")
    print(f"    row sum {sum(sc['binomial_row']):,} == 2^16 {2**16:,}")
