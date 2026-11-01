"""Sensitivity model for The Retirement State (SPEC section 2 balance test, case-readiness Tier 2 probes 4 and 5).

CONTRACT: evaluate(params) -> {"A": metric, "B": metric}, higher wins.
Option A = Florida (The Crude Map finalist), B = Georgia (The Adjusted Map finalist).

The case's two readings of the primary metric are each a plain rate comparison:
  crude basis        Florida 971.4 vs Georgia 798.2      -> Florida higher, gap/higher = 17.8%
  age-adjusted basis Georgia 793.7 vs Florida 672.1      -> Georgia higher, gap/higher = 15.3%
Neither is an assumption: all four rates are cited or derived (data_pull.py), so they are NOT in FLEX.

The only free dial is how much weight the Fund's charter puts on each reading. The case does not state a
weight (the charter names no rate); the dilemma IS that choice. To make the choice machine-testable, the
model scores each state by a blended burden index, relative to the U.S. on each basis:

    index(state, w) = w * crude(state)/crude(US) + (1 - w) * aadr(state)/aadr(US)      (1.0 = the U.S.)

w = 1 is the pure crude reading, w = 0 the pure age-adjusted reading, w = 0.5 an equal split. The state with
the higher index is the one the blend points the award at (A or B). FLEX = ["w_crude"] is therefore the one
dial Probe 5 sweeps, standing in for the board's judgment. It is a facilitator-only construct: students are
never given w, and nothing in case.md depends on it.

Margin note: Probe 5 reports gap / LOWER index (its fixed convention). The case's own convention (SPEC 2
margin = gap / HIGHER value, stated once in FACILITATOR.md) is what __main__ prints for the two pure readings.
The two differ: the pure crude reading is 17.8% by the case's convention and 21.7% by Probe 5's (the pure
age-adjusted reading is 15.3% and 18.1%). The swept points w = 0.25 and 0.75 are 7.7% and 11.3% on Probe 5's
convention, so the sweep itself never touches the cap; only the w = 1 endpoint would, and it is not swept.
"""

PARAMS = {
    # 2017 rates per 100,000 (crude derived from NCHS deaths / Census July 1 estimate; aadr NCHS-published)
    "crude_fl": 971.4, "crude_ga": 798.2, "crude_us": 865.7,
    "aadr_fl": 672.1, "aadr_ga": 793.7, "aadr_us": 731.9,
    # the board's weight on the crude reading (the dilemma itself); 0.5 = equal split
    "w_crude": 0.5,
}
FLEX = ["w_crude"]


def index(p, state):
    w = min(1.0, max(0.0, p["w_crude"]))   # clamp: +50% of 0.5 stays inside [0, 1]
    return (w * p["crude_" + state] / p["crude_us"]) + ((1 - w) * p["aadr_" + state] / p["aadr_us"])


def evaluate(p):
    return {"A": index(p, "fl"), "B": index(p, "ga")}


# Twist (FACILITATOR.md): CDC provisional COVID-19 death rates by jurisdiction of residence, cumulative
# 2020-01-01 to 2026-09-12, data as of 2026-09-17 (data.cdc.gov mpx5-t7tu). Crude and age-adjusted, per 100,000.
TWIST = {"crude_fl": 399.6, "crude_ga": 360.4, "crude_us": 374.5,
         "aadr_fl": 270.1, "aadr_ga": 342.0, "aadr_us": 311.4}


def evaluate_twist(p):
    q = dict(p)
    q.update(TWIST)
    return evaluate(q)


def tie_weight(p):
    """w at which Florida and Georgia have the same blended index."""
    a = (p["crude_fl"] / p["crude_us"] - p["aadr_fl"] / p["aadr_us"])
    b = (p["crude_ga"] / p["crude_us"] - p["aadr_ga"] / p["aadr_us"])
    c0 = p["aadr_ga"] / p["aadr_us"] - p["aadr_fl"] / p["aadr_us"]
    return c0 / (a - b)


if __name__ == "__main__":
    P = PARAMS
    cm = 100 * (P["crude_fl"] - P["crude_ga"]) / P["crude_fl"]
    am = 100 * (P["aadr_ga"] - P["aadr_fl"]) / P["aadr_ga"]
    print(f"pure crude  : Florida {P['crude_fl']} vs Georgia {P['crude_ga']}  margin (gap/higher) {cm:.2f}%")
    print(f"pure aadr   : Georgia {P['aadr_ga']} vs Florida {P['aadr_fl']}  margin (gap/higher) {am:.2f}%")
    assert abs(cm - 17.8) < 0.1 and abs(am - 15.3) < 0.1
    print(f"tie weight on crude: {tie_weight(P):.4f}")
    for w in (0.0, 0.25, 0.4536, 0.5, 0.75, 1.0):
        q = dict(P); q["w_crude"] = w
        e = evaluate(q); win = max(e, key=e.get); lo = min(e, key=e.get)
        print(f"w={w:<6} A(FL)={e['A']:.4f} B(GA)={e['B']:.4f} winner {win} gap/lower {100*(e[win]-e[lo])/e[lo]:.1f}%")
    t = evaluate_twist(P); tw = max(t, key=t.get); tl = min(t, key=t.get)
    print(f"twist (w=0.5): A(FL)={t['A']:.4f} B(GA)={t['B']:.4f} winner {tw} gap/lower {100*(t[tw]-t[tl])/t[tl]:.1f}%")
    tc = 100 * (TWIST["crude_fl"] - TWIST["crude_ga"]) / TWIST["crude_fl"]
    ta = 100 * (TWIST["aadr_ga"] - TWIST["aadr_fl"]) / TWIST["aadr_ga"]
    print(f"twist pure crude margin (gap/higher) {tc:.2f}% ; pure aadr margin {ta:.2f}%")
