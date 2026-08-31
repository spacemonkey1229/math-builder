#!/usr/bin/env python3
"""
Sensitivity model — The Skin Pack Atlas.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the contract
and worked reference (Cold Chain).

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is a stated
                                                     Modeling Assumption
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better

The metric returned is `primary_metric` itself: the revenue-weighted percent
of active install base that renders the chosen atlas without a texture load
failure. Option B (the Anchor Atlas, 4096x4096) is fixed at 100% by
construction -- every device Tanager has ever tested loads it -- exactly as
case.json's balance.margin_note states. Option A (the Crest Atlas, 8192x8192)
is the number the case's whole D1-D5 matrix solve exists to produce.

Fixed (not in FLEX[]): India's and Nigeria's Value-tier device-share
percentages (47% / 50.7%) are cited, sourced current data (S1', S2'), not
stated scenario assumptions -- same treatment bioreactor-bid gives Column's
sourced fill fraction and both vessels' sourced costs.

MA3 (case.json.modeling_assumptions, case.md Appendix E): the model's
Value-tier hard cap describes the Mali-400 GPU (discontinued by ARM in 2015),
not the Mali-G52/G57-class GPUs that actually dominate India/Nigeria's
current budget segment -- so the model's blanket "every Value-tier install
fails to render the Crest Atlas" is disclosed as likely conservative. The
case states no replacement numeric cap (RESEARCH_LOG.md: "No current source
... could confirm an exact GL_MAX_TEXTURE_SIZE value for Mali-G52/G57"), so
this file represents MA3 as `value_tier_overcount_frac` -- the fraction of
"Value-tier"-proxy installs the model treats as a hard failure. Base = 1.0
reproduces the case's own all-or-nothing cap exactly (matching S4's Mali-400
figure); flexing it DOWN toward 0.0 approximates MA3's claim that fewer of
those installs are really incapable than the model's blanket cap assumes.
Values outside [0, 1] are clamped, so a +50% flex from the 1.0 ceiling is a
no-op by design -- the interesting direction is downward, same structure as
Cold Chain's `allocation_village_priority` dial.

Verified against case.json's balance object and FACILITATOR.md's worked
arithmetic (2026-08-30 recomputed pass):
    base    A = 85.1%  ·  B = 100%   margin 14.9%   (matches case.json.balance)
            device-count A = 51.8%                  (matches balance.margin_note)
"""

# --- Fixed: cited, sourced device-tier shares (S1', S2'), not stated
#     scenario assumptions -- same treatment bioreactor-bid gives sourced,
#     non-assumption dials.
INDIA_VALUE_SHARE = 0.47       # [S1'] -- MediaTek's India chipset share
NIGERIA_VALUE_SHARE = 0.507    # [S2'] -- Transsion-brand combined Nigeria share

PARAMS = {
    # --- MA1: Tanager's own invented install/revenue figures ----------------
    "india_installs": 40000.0,
    "nigeria_installs": 20000.0,
    "india_revenue_usd": 19780.0,
    "nigeria_revenue_usd": 9409.0,
    # --- MA3 proxy: see docstring. 1.0 = the model's own all-or-nothing hard
    #     cap (every "Value-tier"-proxy install fails the Crest Atlas), which
    #     is what case.json.balance.margin_note's 85.1%/14.9% figures assume.
    "value_tier_overcount_frac": 1.0,
}

# Probe 5 flexes THESE and only these -- the subset that is a stated Modeling
# Assumption (MA1, MA3), not cited/sourced device-tier share data (S1'/S2',
# fixed above). --flex-all overrides.
FLEX = [
    "india_installs",              # MA1
    "nigeria_installs",            # MA1
    "india_revenue_usd",           # MA1
    "nigeria_revenue_usd",         # MA1
    "value_tier_overcount_frac",   # MA3 -- the case's single most important
                                    # honest finding; see docstring.
]


def _solve(params):
    """Build M, solve r = M^-1 v, and return every intermediate the case's
    D1-D5 deliverables name, keyed the same way FACILITATOR.md's worked
    arithmetic is."""
    p = dict(PARAMS)
    p.update(params or {})

    india_flagship = p["india_installs"] * (1.0 - INDIA_VALUE_SHARE)
    india_value = p["india_installs"] * INDIA_VALUE_SHARE
    nigeria_flagship = p["nigeria_installs"] * (1.0 - NIGERIA_VALUE_SHARE)
    nigeria_value = p["nigeria_installs"] * NIGERIA_VALUE_SHARE

    # M (Appendix B): rows India/Nigeria, columns Flagship/Value.
    m00, m01 = india_flagship, india_value
    m10, m11 = nigeria_flagship, nigeria_value
    det = m00 * m11 - m01 * m10
    if det == 0:
        raise ValueError("det(M) is zero -- M is not invertible (D3 fails)")

    v0, v1 = p["india_revenue_usd"], p["nigeria_revenue_usd"]
    # r = M^-1 v (D4)
    r_flagship = (m11 * v0 - m01 * v1) / det
    r_value = (-m10 * v0 + m00 * v1) / det

    flagship_installs = india_flagship + nigeria_flagship
    value_installs = india_value + nigeria_value
    total_installs = flagship_installs + value_installs

    flagship_revenue = flagship_installs * r_flagship
    value_revenue = value_installs * r_value
    total_revenue = flagship_revenue + value_revenue

    return {
        "det": det, "r_flagship": r_flagship, "r_value": r_value,
        "flagship_installs": flagship_installs, "value_installs": value_installs,
        "total_installs": total_installs, "flagship_revenue": flagship_revenue,
        "value_revenue": value_revenue, "total_revenue": total_revenue,
        "p": p,
    }


def evaluate(params):
    """D5's decision table, as the case's own recommendation logic reads it:
    the revenue-weighted percent of active install base that renders the
    chosen atlas without a texture load failure. Higher is better."""
    s = _solve(params)
    p = s["p"]

    value_success_frac = 1.0 - p["value_tier_overcount_frac"]
    value_success_frac = max(0.0, min(1.0, value_success_frac))   # domain [0, 1]

    a_success_revenue = s["flagship_revenue"] + value_success_frac * s["value_revenue"]
    a_revenue_pct = 100.0 * a_success_revenue / s["total_revenue"]

    # Option B (Anchor Atlas, 4096): every device tier renders successfully,
    # by construction (case.md Appendix D / case.json balance.argument_b).
    b_revenue_pct = 100.0

    return {"A": a_revenue_pct, "B": b_revenue_pct}


def device_count_pct(params):
    """Not part of the Tier 2 contract -- the device-count (not
    revenue-weighted) success percentage, used only to reproduce
    case.json.balance.margin_note's 51.8% figure for verification. This is
    the number the case's own trap warns a Hero not to stop at."""
    s = _solve(params)
    p = s["p"]
    value_success_frac = max(0.0, min(1.0, 1.0 - p["value_tier_overcount_frac"]))
    a_success_installs = s["flagship_installs"] + value_success_frac * s["value_installs"]
    return {"A": 100.0 * a_success_installs / s["total_installs"], "B": 100.0}


if __name__ == '__main__':
    base = evaluate({})
    dev = device_count_pct({})
    margin = 100.0 * (base["B"] - base["A"]) / base["B"]
    print("base (revenue-weighted)", {k: round(v, 1) for k, v in base.items()},
          "margin %.1f%%" % margin)
    print("device-count            ", {k: round(v, 1) for k, v in dev.items()})

    # MA3 flexed to -50% (0.5): half of "Value-tier"-proxy installs are no
    # longer treated as a hard failure -- does the winner flip?
    flexed = evaluate({"value_tier_overcount_frac": 0.5})
    print("MA3 flexed to 0.5 (-50%)", {k: round(v, 1) for k, v in flexed.items()})

    # MA3 flexed all the way to 0.0: the model's own disclosed limit case --
    # every "Value-tier"-proxy install actually renders the Crest Atlas.
    flexed0 = evaluate({"value_tier_overcount_frac": 0.0})
    print("MA3 flexed to 0.0 (full)", {k: round(v, 1) for k, v in flexed0.items()})
