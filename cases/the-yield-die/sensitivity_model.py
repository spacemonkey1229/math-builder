#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Yield Die.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own D1-D5 arithmetic: gross
dies per wafer (wafer-geometry formula), the Seeds defect-density yield model
(D4), and revenue per wafer = net good dies x price per die (D5).

CONTRACT -- exactly two required public names:

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

evaluate() returns revenue per wafer (USD) for each option directly -- a
dollar amount where higher is genuinely better, no negation needed.

    Aw               = pi * (wafer_diameter_cm/2)^2                      (Appendix B)
    gross(A)         = Aw/A - (pi*wafer_diameter_cm)/sqrt(2*A)            (Appendix B, [S2])
    yield(A)         = 1 / (1 + defect_density_D0 * A)                   (Appendix D, Seeds model, [S5])
    good(A)          = floor(gross(A) * yield(A))
    transistors(A)   = transistor_density_per_mm2 * A_mm2                (Appendix C)
    price(A)         = dollars_per_transistor * transistors(A)           (Appendix E)
    revenue(A)       = good(A) * price(A)

Appendix B's wafer diameter [S1] and both die-option areas (Priya's own
design choices, grounded in S3) are cited/given data -- NOT flexed by default
(P6, data decay, covers cited URLs instead; see "Only FLEX[] is swept" in
skills/case-readiness/SKILL.md's P5 section). The transistor-density (MA1)
and pricing-benchmark (MA3) assumptions scale BOTH options by the same
factor and so never change which option wins -- only the absolute dollar
totals -- so flexing them would not test a real fragility; they are excluded
from FLEX for that reason, not because they aren't assumptions.

Only MA2 (the assumed defect density) is genuinely load-bearing for WHICH
option wins, because it enters the yield formula multiplied by a DIFFERENT
area for each option (1.00 cm^2 for A, 2.00 cm^2 for B) -- it does not cancel
out. No foundry discloses its live defect density for a specific, not-yet-
running process line: this is the one figure in the case that is genuinely
unknowable in advance, exactly like the-bracket-bet's future-tax-rate MA2.

MA4 (a flagship pricing premium applied to Option B only, beyond pure linear
per-transistor scaling -- grounded in real Nvidia L4 vs H100 pricing data,
S9) is what makes a genuine crossover possible at all: under pure linear
pricing (premium=1.0), Option A's larger gross-die-per-wafer count wins at
EVERY non-negative defect density (confirmed during Tier 2 P2/P4 review --
see QA_REPORT.md), which would make the case's central "assumption" (MA2)
unable to ever flip the verdict, contradicting D5's own prompt asking
readers to name the value that WOULD flip it. MA4 is deliberately NOT in
FLEX (it scales only Option B, and case-readiness's remediation fixed its
value once, rather than treating it as the swept dial) -- MA2 remains the
single swept assumption, consistent with "Only FLEX[] is swept."

Expected P5 finding: flexing defect_density_D0 by +/-50% (0.30 -> 0.15 or
0.30 -> 0.45) DOES flip the winner. At the base case (D0=0.30) and at +50%
(D0=0.45), Option A (Compact Die) wins. At -50% (D0=0.15), Option B (Full
Die) wins -- a genuine, disclosed bidirectional dependency, not a hidden
fragility: D5 already asks every reader to name the one figure their
recommendation depends on most and what value would flip it, and the real
crossover (~D0=0.157-0.16) is now a findable answer to that question.

Verified against case.json.balance / FACILITATOR.md (2026-09-09, revised
after Tier 2 P2/P4 remediation):
    base (D0=0.30)   A=$3,690,000.00  B=$3,409,350.00  A wins, margin  8.23%
    -50% (D0=0.15)   A=$4,170,000.00  B=$4,194,750.00  B wins, margin  0.59%  *** FLIPS ***
    +50% (D0=0.45)   A=$3,307,500.00  B=$2,873,850.00  A wins, margin 15.09%
"""
import math

PARAMS = {
    # --- Appendix B [S1], sourced wafer diameter -----------------------------
    "wafer_diameter_mm": 300.0,
    # --- Appendix B, Priya's own design-choice die areas (grounded via S3) --
    "die_area_A_mm2": 100.0,
    "die_area_B_mm2": 200.0,
    # --- Appendix C / Modeling Assumption MA1: transistor density -----------
    #     scales both options equally -- see module docstring for why this is
    #     excluded from FLEX despite being a stated assumption.
    "transistor_density_per_mm2": 2.0e8,
    # --- Appendix D / Modeling Assumption MA2: assumed defect density -------
    #     THE genuine free scenario dial -- no foundry discloses this for a
    #     specific, not-yet-running process line. Set to a "first tape-out,
    #     not-yet-mature line" figure (below Intel's real disclosed 18A
    #     ceiling of 0.40) rather than the "already-mature" 0.1 benchmark.
    "defect_density_D0_per_cm2": 0.30,
    # --- Appendix E / Modeling Assumption MA3: dollars-per-transistor -------
    #     derived from a real Nvidia H100 anchor; scales both options equally.
    "dollars_per_transistor": 3.75e-7,
    # --- Appendix E / Modeling Assumption MA4: flagship pricing premium -----
    #     applied to Option B ONLY; grounded in real Nvidia L4-vs-H100
    #     dollars-per-transistor gap (S9), a conservative 19% fraction of the
    #     real ~5x effect. This is what makes a genuine crossover possible --
    #     see module docstring.
    "flagship_premium_B": 1.19,
}

# Probe 5 flexes THIS and only this by default: the one genuinely free
# Modeling Assumption (MA2) that is load-bearing for WHICH option wins.
# MA1 and MA3 are real assumptions too, but scale both options by the same
# factor and so can never flip a verdict -- flexing them would not test a
# real fragility. The wafer diameter and both die areas are cited/given
# design data, stress-tested by P6 (data decay) instead. Run with
# --flex-all to sweep everything anyway.
FLEX = [
    "defect_density_D0_per_cm2",
]


def _gross_dies(wafer_diameter_cm, die_area_cm2):
    """Appendix B: the edge-loss-corrected gross-die-per-wafer formula [S2]."""
    Aw = math.pi * (wafer_diameter_cm / 2.0) ** 2
    return Aw / die_area_cm2 - (math.pi * wafer_diameter_cm) / math.sqrt(2.0 * die_area_cm2)


def _yield(defect_density_D0, die_area_cm2):
    """Appendix D: the Seeds defect-density yield model [S5]."""
    return 1.0 / (1.0 + defect_density_D0 * die_area_cm2)


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})

    wafer_diameter_cm = p["wafer_diameter_mm"] / 10.0
    area_A_cm2 = p["die_area_A_mm2"] / 100.0
    area_B_cm2 = p["die_area_B_mm2"] / 100.0

    gross_A = math.floor(_gross_dies(wafer_diameter_cm, area_A_cm2))
    gross_B = math.floor(_gross_dies(wafer_diameter_cm, area_B_cm2))

    yield_A = _yield(p["defect_density_D0_per_cm2"], area_A_cm2)
    yield_B = _yield(p["defect_density_D0_per_cm2"], area_B_cm2)

    good_A = math.floor(gross_A * yield_A)
    good_B = math.floor(gross_B * yield_B)

    transistors_A = p["transistor_density_per_mm2"] * p["die_area_A_mm2"]
    transistors_B = p["transistor_density_per_mm2"] * p["die_area_B_mm2"]

    price_A = p["dollars_per_transistor"] * transistors_A
    price_B = p["dollars_per_transistor"] * transistors_B * p["flagship_premium_B"]

    revenue_A = good_A * price_A
    revenue_B = good_B * price_B

    return {"A": revenue_A, "B": revenue_B}


if __name__ == '__main__':
    base = evaluate({})
    a, b = base["A"], base["B"]
    winner = "A (Compact Die)" if a > b else "B (Full Die)"
    lo, hi = min(a, b), max(a, b)
    margin = 100.0 * (hi - lo) / lo
    print("base (D0=%.2f)  A=$%.2f  B=$%.2f  winner=%s  margin=%.2f%%"
          % (PARAMS["defect_density_D0_per_cm2"], a, b, winner, margin))

    print("\n±50%% flex of defect_density_D0_per_cm2:")
    for mult, label in ((0.5, "-50%"), (1.5, "+50%")):
        d0f = PARAMS["defect_density_D0_per_cm2"] * mult
        r = evaluate({"defect_density_D0_per_cm2": d0f})
        ra, rb = r["A"], r["B"]
        w = "A (Compact)" if ra > rb else "B (Full)"
        lo3, hi3 = min(ra, rb), max(ra, rb)
        m3 = 100.0 * (hi3 - lo3) / lo3
        flip = " *** FLIPS ***" if w.startswith("B") else ""
        print("  D0 %s (rate=%.4f)  A=$%.2f  B=$%.2f  winner=%s  margin=%.2f%%%s"
              % (label, d0f, ra, rb, w, m3, flip))
