#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- Driving Age.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. This is that
model, for cases/driving-age.

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):

    PARAMS                             dict[str, number]  every dial the case states
    FLEX                               list[str]          subset of PARAMS probe 5 flexes
    evaluate(params) -> dict           {"A": metric, "B": metric}
    evaluate_twist(params) -> dict     same shape, with the twist's own lens applied

IMPORTANT -- metric direction: this case's primary metric is a two-year COST in
USD, so LOWER is better here (unlike Cold Chain's in-spec-dose count, where
higher is better). Callers comparing A vs B for "the winner" should take the
smaller value, not the larger one.

evaluate() returns the case's graded PRIMARY metric: net two-year dollar cost
per family (case.json.primary_metric). Option A (raise to 18) = chauffeuring
cost only. Option B (keep 15.5) = insurance cost only. Matches case.json
balance (A=$7964.40, B=$8100.00, margin 1.70%, A cheaper).

evaluate_twist() returns the same two dollar totals but tags on the naive,
per-100,000-population fatality-rate reading a room reaches for before
FACILITATOR.md's Twist reframes it as a per-mile-vs-per-population confound.
The Twist does not change the dollar arithmetic -- it changes whether Option
A's *safety* argument (not its cost argument) is defensible. evaluate_twist()
therefore returns the same {"A", "B"} cost dict as evaluate() PLUS a
"twist_note" key naming which age's rate is used as the naive read.

Verified against case.md / case.json:
    evaluate({})        A = 7964.40  B = 8100.00   margin (B-A)/A = 1.70%   (A cheaper)
"""

PARAMS = {
    # --- Appendix F, MA1: disclosed chauffeuring-mileage assumption ---------
    "chauffeuring_miles_per_year": 6000,
    # --- Appendix A, S1: real, current AZ law -- years HB 3320 would delay
    #     independent driving (16 -> 18) ---------------------------------------
    "delay_years": 2,
    # --- Appendix C, S4: real, current AAA fully-loaded per-mile cost --------
    "cost_per_mile_usd": 0.6637,
    # --- Appendix C, S3: real, current average insurance-premium increase ----
    "insurance_increase_per_year_usd": 4050.00,
    # --- Appendix B, S2: real IIHS fatal-crash rate per 100,000 people, by
    #     driver age -- used only by evaluate_twist() for the naive safety read
    "rate_age_16": 3.5,
    "rate_age_18": 7.0,
    "rate_age_19": 8.8,
}

# Probe 5 flexes THESE and only these -- the case's one genuine, disclosed,
# author-chosen scenario dial (MA1). delay_years, cost_per_mile_usd and
# insurance_increase_per_year_usd are real, cited, sourced figures (S1, S4,
# S3) -- cited measurements, not assumptions -- and are stress-tested by the
# data-decay probe (P6) instead, per the "only FLEX[] is swept" rule.
FLEX = [
    "chauffeuring_miles_per_year",   # Appendix F, MA1
]


def _option_a_cost(p):
    """Raise the age to 18: no insurance cost, full chauffeuring cost."""
    return p["chauffeuring_miles_per_year"] * p["delay_years"] * p["cost_per_mile_usd"]


def _option_b_cost(p):
    """Keep 15.5: full insurance cost, no chauffeuring cost."""
    return p["insurance_increase_per_year_usd"] * p["delay_years"]


def evaluate(params=None):
    """Primary graded metric: net two-year dollar cost, lower is better."""
    p = dict(PARAMS)
    p.update(params or {})
    return {"A": _option_a_cost(p), "B": _option_b_cost(p)}


def evaluate_twist(params=None):
    """Same dollar totals; the Twist attacks Option A's SAFETY argument, not
    its cost. Reports the naive per-100,000-population reading (age 16 vs. 18)
    alongside the unchanged cost dict, so a caller can see both moved parts."""
    p = dict(PARAMS)
    p.update(params or {})
    out = evaluate(p)
    out["twist_note"] = (
        "naive safety read: rate climbs from %.1f (age 16) to %.1f (age 18) to "
        "%.1f (age 19) per 100,000 people -- NOT a per-mile risk rate, and does "
        "not fall with a higher minimum age" % (p["rate_age_16"], p["rate_age_18"], p["rate_age_19"])
    )
    return out


if __name__ == "__main__":
    base = evaluate({})
    tw = evaluate_twist({})
    margin = 100 * (base["B"] - base["A"]) / base["A"]
    cheaper = "A" if base["A"] < base["B"] else "B"
    print("evaluate()       A=$%.2f  B=$%.2f  (B-A)/A=%.2f%%  -> %s cheaper" %
          (base["A"], base["B"], margin, cheaper))
    print("evaluate_twist() A=$%.2f  B=$%.2f  %s" % (tw["A"], tw["B"], tw["twist_note"]))
