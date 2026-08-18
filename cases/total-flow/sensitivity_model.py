"""Sensitivity model for Total Flow (SPEC §2 balance test, case-readiness Tier 2 probe 5).

Every number below is either SOURCED (a figure cited in case.md Appendix E, citation id in the
comment) or ASSUMED (a row of case.md Appendix F, Modeling Assumptions, id in the comment).
FLEX lists the ASSUMED subset — probe 5 sweeps only those, per case-readiness's rule that cited
measurements are stress-tested by probe 6 (data decay), not probe 5.

WHY THE SOURCED DIALS ARE NOT IN FLEX. Three quantities decide this case: the channel capacity
(1,934 cfs), the Crest Standard's design discharge (5,927 cfs), and the Basin Standard's
authorized detention (25,000 acre-ft). None is an authorial estimate:

  * 1,934 cfs is the USGS stage-discharge rating's own value at 21.50 ft, and 21.50 ft is the
    National Weather Service's published minor flood stage for this gage.
  * 5,927 cfs is the same rating's value 4.50 ft higher, at 26.00 ft — the height in Bid A's
    scope. A different raise is a different bid, and every row of the rating is a different case;
    case.md Appendix F says so on the page rather than hiding it in this file.
  * 25,000 acre-ft is two structures at the statutory per-structure ceiling in 16 U.S.C. 1002.

Halving any of the three is a different case, not a sensitivity test — the same reason Cold
Chain's reference model keeps WHO-rated cold lives out of FLEX. The case does NOT hide that these
three are decisive: case.md Appendix F states the computed effect of moving the channel-capacity
convention, and so do case.json.balance.stability and FACILITATOR.md.

CONTRACT: PARAMS, evaluate(params) -> {"A": metric, "B": metric} (higher wins), evaluate_twist().
"""
import datetime

# --- The real record ---------------------------------------------------------------------------
# USGS 05469000 Henderson Creek near Oquawka, IL — daily mean discharge, cubic feet per second,
# fetched from USGS NWIS (S2, S3). These are scenario structure, not dials: they are what the
# river did. Probe 6 (data decay) is what re-checks them.
STORM1 = [                                     # "The Slammed Door" — Feb 2019
    (datetime.date(2019, 2, 22), 413.0),
    (datetime.date(2019, 2, 23), 3290.0),
    (datetime.date(2019, 2, 24), 8060.0),
    (datetime.date(2019, 2, 25), 4220.0),
    (datetime.date(2019, 2, 26), 1130.0),
    (datetime.date(2019, 2, 27), 690.0),
    (datetime.date(2019, 2, 28), 490.0),
    (datetime.date(2019, 3, 1), 474.0),
]
STORM2 = [                                     # "The Long Guest" — Apr/May 2019
    (datetime.date(2019, 4, 28), 225.0),
    (datetime.date(2019, 4, 29), 932.0),
    (datetime.date(2019, 4, 30), 3000.0),
    (datetime.date(2019, 5, 1), 6400.0),
    (datetime.date(2019, 5, 2), 6700.0),
    (datetime.date(2019, 5, 3), 6240.0),
    (datetime.date(2019, 5, 4), 3980.0),
    (datetime.date(2019, 5, 5), 2050.0),
    (datetime.date(2019, 5, 6), 1490.0),
    (datetime.date(2019, 5, 7), 1420.0),
]

PARAMS = {
    # --- SOURCED (case.md Appendix B/C/D; see the docstring for why these are not flexed) -------
    "channel_capacity_cfs": 1934.0,          # S5 — USGS rating 31.0 at 21.50 ft (S4, NWS minor flood stage)
    "crest_design_discharge_cfs": 5927.0,    # S5 — same rating at 26.00 ft (21.50 + a 4.50 ft raise)
    "authorized_detention_af": 25000.0,      # S8 — 2 structures x 12,500 acre-ft, the 16 U.S.C. 1002 ceiling
    "cfsday_to_acreft": 1.98347,             # S7 — USGS Definition of Terms

    # --- ASSUMED (case.md Appendix F, Modeling Assumptions) ------------------------------------
    "appropriation_usd": 38000000.0,         # MA1 — the district's single appropriation; both bids sit at it
    "unavailable_storage_frac": 0.04,        # MA2 — sediment + antecedent pool, unavailable at storm onset
    "basin_drawdown_days": 10.0,             # MA3 — outlet-works drawdown time for a full pool
    "twist_max_loading_days": 4.0,           # MA4 — sustained-loading limit revealed by the Twist
}

# Probe 5 flexes THESE and only these.
FLEX = [
    "appropriation_usd",           # MA1 — both options share the denominator, so this is margin-invariant
    "unavailable_storage_frac",    # MA2 — the one genuinely load-bearing assumption in the set
    "basin_drawdown_days",         # MA3
    "twist_max_loading_days",      # MA4 — twist-only; evaluate() does not read it, by design
]


# --- Mechanics ---------------------------------------------------------------------------------
def _excess_cfsdays(series, floor_cfs):
    """Volume, in cubic-foot-per-second-days, of the region between the daily-mean discharge
    curve and the horizontal line Q = floor_cfs, over the days where discharge exceeds it.

    Delta-t is exactly one day and the values are daily MEANS, so this sum is not an
    approximation of the published record — USGS's own Definition of Terms says the daily mean
    discharges 'numerically are equal to the daily volumes in cfs-days'. That is the point
    deliverable D1 is built around."""
    return sum(q - floor_cfs for _, q in series if q > floor_cfs)


def _days_above(series, floor_cfs):
    """Longest run of consecutive days with discharge above floor_cfs."""
    best = run = 0
    prev = None
    for d, q in series:
        if q > floor_cfs and (prev is None or (d - prev).days == 1):
            run += 1
        elif q > floor_cfs:
            run = 1
        else:
            run = 0
        prev = d
        best = max(best, run)
    return best


def _tail_excess_cfsdays(series, floor_cfs, keep_days):
    """Excess volume the Crest Standard LOSES under the Twist: everything above channel capacity
    that arrives after `keep_days` consecutive days of loading, within one storm."""
    run = 0
    lost = 0.0
    prev = None
    for d, q in series:
        if q > floor_cfs:
            run = run + 1 if (prev is not None and (d - prev).days == 1 and run) else 1
            if run > keep_days:
                lost += q - floor_cfs
        else:
            run = 0
        prev = d
    return lost


def _separation_days():
    """Days between the last above-capacity day of storm 1 and the first of storm 2 — a fact of
    the real record, used to decide whether the basins are empty again when storm 2 arrives."""
    qc = PARAMS["channel_capacity_cfs"]
    last1 = max(d for d, q in STORM1 if q > qc)
    first2 = min(d for d, q in STORM2 if q > qc)
    return (first2 - last1).days


def breakdown(p):
    """Every figure case.md and FACILITATOR.md quote, derived in one place."""
    conv = p["cfsday_to_acreft"]
    qc = p["channel_capacity_cfs"]
    qa = p["crest_design_discharge_cfs"]

    e1 = _excess_cfsdays(STORM1, qc) * conv          # acre-feet above channel capacity, storm 1
    e2 = _excess_cfsdays(STORM2, qc) * conv          # acre-feet above channel capacity, storm 2
    total = e1 + e2

    # Option A — rate-limited. Shortfall is the region above its own design discharge.
    short_a = (_excess_cfsdays(STORM1, qa) + _excess_cfsdays(STORM2, qa)) * conv
    managed_a = total - short_a

    # Option B — volume-limited. Usable storage, less anything still impounded from storm 1.
    usable = p["authorized_detention_af"] * (1.0 - p["unavailable_storage_frac"])
    stored1 = min(usable, e1)
    undrained = stored1 * max(0.0, 1.0 - _separation_days() / max(p["basin_drawdown_days"], 1e-9))
    stored2 = min(max(usable - undrained, 0.0), e2)
    managed_b = stored1 + stored2

    per_1000 = p["appropriation_usd"] / 1000.0
    return {
        "excess_storm1_af": e1, "excess_storm2_af": e2, "total_excess_af": total,
        "shortfall_a_af": short_a, "managed_a_af": managed_a,
        "usable_storage_af": usable, "managed_b_af": managed_b,
        "shortfall_b_af": total - managed_b,
        "A_per_1000": managed_a / per_1000, "B_per_1000": managed_b / per_1000,
        "days_above_storm1": _days_above(STORM1, qc), "days_above_storm2": _days_above(STORM2, qc),
        "peak_storm1_cfs": max(q for _, q in STORM1), "peak_storm2_cfs": max(q for _, q in STORM2),
        "separation_days": _separation_days(),
    }


def twist_breakdown(p):
    """The Twist: the raised crown may only be loaded for a limited number of consecutive days
    before underseepage takes the reach out of service. Option B is untouched."""
    b = breakdown(p)
    qc = p["channel_capacity_cfs"]
    keep = p["twist_max_loading_days"]
    lost = (_tail_excess_cfsdays(STORM1, qc, keep) +
            _tail_excess_cfsdays(STORM2, qc, keep)) * p["cfsday_to_acreft"]
    managed_a = b["managed_a_af"] - lost
    per_1000 = p["appropriation_usd"] / 1000.0
    return {"lost_af": lost, "managed_a_af": managed_a, "managed_b_af": b["managed_b_af"],
            "A_per_1000": managed_a / per_1000, "B_per_1000": b["managed_b_af"] / per_1000}


def _contract(a, b):
    """CONTRACT: {"A": metric, "B": metric}, higher wins.

    Total Flow's metric (acre-feet managed per $1,000) is already higher-is-better, but the case
    states its margin the SPEC §2 way — (better - worse) / better — while the probe framework's
    generic formula is (max - min) / min. Mapping the winner to 2*better - worse and the loser to
    better makes the generic formula collapse to exactly the case's own definition, so the probe
    and case.json can never report two different margins for the same run. Ordering is preserved.
    """
    better, worse = max(a, b), min(a, b)
    if better == worse:
        return {"A": better, "B": better}
    hi, lo = 2 * better - worse, better
    return {"A": hi if a > b else lo, "B": hi if b > a else lo}


def evaluate(params=None):
    p = dict(PARAMS); p.update(params or {})
    d = breakdown(p)
    return _contract(d["A_per_1000"], d["B_per_1000"])


def evaluate_twist(params=None):
    p = dict(PARAMS); p.update(params or {})
    t = twist_breakdown(p)
    return _contract(t["A_per_1000"], t["B_per_1000"])


def _margin(a, b):
    return 100.0 * (max(a, b) - min(a, b)) / max(a, b)


if __name__ == "__main__":
    b = breakdown(PARAMS)
    for k in ("peak_storm1_cfs", "peak_storm2_cfs", "days_above_storm1", "days_above_storm2",
              "separation_days", "excess_storm1_af", "excess_storm2_af", "total_excess_af",
              "shortfall_a_af", "managed_a_af", "usable_storage_af", "managed_b_af",
              "shortfall_b_af", "A_per_1000", "B_per_1000"):
        print(f"  {k:22s} {b[k]:,.2f}")
    base_margin = _margin(b["A_per_1000"], b["B_per_1000"])
    base_win = "A" if b["A_per_1000"] > b["B_per_1000"] else "B"
    print(f"\nBASE   A {b['A_per_1000']:.5f}  B {b['B_per_1000']:.5f}  af per $1,000 "
          f"-> winner {base_win}, margin {base_margin:.2f}%")

    t = twist_breakdown(PARAMS)
    tw_margin = _margin(t["A_per_1000"], t["B_per_1000"])
    tw_win = "A" if t["A_per_1000"] > t["B_per_1000"] else "B"
    print(f"TWIST  A {t['A_per_1000']:.5f}  B {t['B_per_1000']:.5f}  "
          f"(A loses {t['lost_af']:,.2f} af) -> winner {tw_win}, margin {tw_margin:.2f}%"
          + ("   <-- THE TWIST FLIPS THE WINNER" if tw_win != base_win else ""))

    ev = evaluate()
    gen = 100.0 * (max(ev.values()) - min(ev.values())) / min(ev.values())
    assert abs(gen - base_margin) < 0.01, f"contract transform drifted: {ev} -> {gen:.2f}"
    print(f"\ncontract check OK: generic (max-min)/min on evaluate() = {gen:.2f}% "
          f"= case margin {base_margin:.2f}%")

    print("\n--- probe 5 preview: FLEX +/-50% ---")
    for name in FLEX:
        for lbl, mult in (("-50%", 0.5), ("+50%", 1.5)):
            p = dict(PARAMS); p[name] = PARAMS[name] * mult
            d = breakdown(p)
            m = _margin(d["A_per_1000"], d["B_per_1000"])
            win = "A" if d["A_per_1000"] > d["B_per_1000"] else "B"
            flag = "  <-- FLIP" if win != "A" else ("  <-- CAP" if m > 20 else "")
            print(f"  {name:26s} {lbl}  winner {win}  margin {m:5.2f}%{flag}")
