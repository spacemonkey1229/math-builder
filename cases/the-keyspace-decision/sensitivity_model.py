"""
SENSITIVITY MODEL — The Keyspace Decision.

Reproduces every figure in case.json["derived"] and case.md's Balance argument, and
exposes the case-readiness Tier 2 probe 5 contract: PARAMS, FLEX, evaluate(params).

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):
    PARAMS   dict[str, number]   every dial the case STATES (sourced facts + assumptions)
    FLEX     list[str]           the SUBSET of PARAMS that is a stated ASSUMPTION
                                  (Appendix E), not cited/given data (Appendix A-D)
    evaluate(params) -> {"A": metric, "B": metric}   higher is better

FLEX-scoping note (doctrine 2026-08-13): the charset, benchmark rate, breach-vector
shares and MFA-blocking rate (S1-S3) and the vendor per-seat prices (S4/S5) are all
cited, sourced figures (Appendix B/C/D, Appendix F) — they belong in PARAMS so a run
with --flex-all can still stress-test them (that's what Tier 2 probe 6, data decay,
covers), but they must NOT sit in FLEX, which is reserved for genuine Appendix E
modeling assumptions the case author chose rather than looked up.

Only two Appendix E assumptions actually enter the primary metric's arithmetic:
  - MA3 (credential-theft annual cadence) — the case's own text names this "the
    single lever that decides the case."
  - MA4 (Long Wall's incremental help-desk cost) — adds linearly to Option A's cost.
MA1 (headcount) cancels out of the per-employee primary metric by construction (both
options scale identically) and MA2 (AP-system access fraction) feeds only D3's
pigeonhole bound, not the A-vs-B primary metric evaluate() computes — so neither
belongs in FLEX for probe 5, which flexes the metric this file's evaluate() returns.
Both are still real assumptions and are exercised directly by the D3 helper below.
"""

# ---- every dial the case states -------------------------------------------------
PARAMS = {
    # Appendix A: charset (S1)
    "charset_size": 70,
    "legacy_charset_size": 36,
    "long_wall_len": 14,
    "second_gate_len": 8,
    "legacy_len": 8,
    # Appendix B: offline benchmark rate (S1)
    "rate_hps": 138675,
    "seconds_per_year": 365 * 24 * 3600,
    # Appendix C: breach-vector weight (S2) and MFA block rate (S3)
    "w_credential_abuse": 0.39,
    "mfa_block_rate": 0.9856,
    # Appendix D: vendor per-seat costs (S4, S5)
    "cost_b_per_employee": 3.00 * 12,        # Duo Essentials, S4
    "cost_a_password_manager": 4.00 * 12,    # Bitwarden Teams, S5
    # Appendix E: modeling assumptions
    "ma1_headcount": 400,
    "ma2_ap_access_fraction": 0.20,
    "ma3_credential_theft_cadence": 0.008,
    "ma4_helpdesk_increment": 12.00,
}

# Probe 5 flexes THESE and only these — the case's own stated ASSUMPTIONS (Appendix
# E) that actually move the A-vs-B primary metric. Cited data (charset, benchmark
# rate, breach shares, MFA rate, vendor prices) is deliberately excluded; halving a
# vendor's published price or Hive Systems' benchmark rate is not a sensitivity test
# of this case's assumptions, it is a different case. Run with --flex-all to sweep
# everything anyway.
FLEX = [
    "ma3_credential_theft_cadence",   # Appendix E, MA3 — the case's own "single lever"
    "ma4_helpdesk_increment",         # Appendix E, MA4
]


def keyspace(charset_size, length):
    return charset_size ** length


def years_to_crack(keyspace_size, rate_hps, seconds_per_year):
    return (keyspace_size / rate_hps) / seconds_per_year


def evaluate(params):
    """{"A": years-to-crack per dollar, "B": years-to-crack per dollar} -- higher wins."""
    p = dict(PARAMS)
    p.update(params or {})

    k_a = keyspace(p["charset_size"], p["long_wall_len"])
    k_b = keyspace(p["charset_size"], p["second_gate_len"])
    t_a = years_to_crack(k_a, p["rate_hps"], p["seconds_per_year"])
    t_b = years_to_crack(k_b, p["rate_hps"], p["seconds_per_year"])

    w_credential = p["w_credential_abuse"]
    w_other = 1 - w_credential
    cadence = p["ma3_credential_theft_cadence"]

    # Option A (The Long Wall): no second factor, credential-theft channel unmitigated.
    p_brute_a = 1 / t_a
    p_cred_a = cadence
    years_a = 1 / (w_other * p_brute_a + w_credential * p_cred_a)

    # Option B (The Second Gate): 2FA on every login, credential-theft channel reduced.
    p_brute_b = 1 / t_b
    p_cred_b = cadence * (1 - p["mfa_block_rate"])
    years_b = 1 / (w_other * p_brute_b + w_credential * p_cred_b)

    cost_a = p["cost_a_password_manager"] + p["ma4_helpdesk_increment"]
    cost_b = p["cost_b_per_employee"]

    return {"A": years_a / cost_a, "B": years_b / cost_b}


def pigeonhole_d3(params=None):
    """D3 helper (not part of the probe-5 evaluate() contract): the legacy keyspace's
    guarantee threshold vs. Bramwell's actual AP-system headcount. Exercises MA1/MA2,
    which do not enter evaluate()'s primary metric -- see module docstring."""
    p = dict(PARAMS)
    p.update(params or {})
    k_legacy = keyspace(p["legacy_charset_size"], p["legacy_len"])
    guarantee = k_legacy + 1
    ap_employees = round(p["ma1_headcount"] * p["ma2_ap_access_fraction"])
    return {"guarantee_threshold": guarantee, "ap_employees": ap_employees,
            "ratio": guarantee / ap_employees}


def main():
    base = evaluate({})
    print(f"D1/D2 keyspaces & crack years (see case.json.derived for the full table)")
    d3 = pigeonhole_d3()
    print(f"D3 pigeonhole: guarantee threshold={d3['guarantee_threshold']:,}  "
          f"AP employees={d3['ap_employees']}  ratio={d3['ratio']:.3e}")

    print(f"D5 primary metric (yrs/$): A={base['A']:.4f}  B={base['B']:.4f}")
    winner = "B" if base["B"] > base["A"] else "A"
    margin = abs(base["B"] - base["A"]) / max(base["A"], base["B"]) * 100
    print(f"WINNER: {winner}  margin={margin:.1f}%")

    # THE TRAP -- raw/unweighted metric (D2 alone, no D4 breach-vector weighting).
    p = PARAMS
    k_a = keyspace(p["charset_size"], p["long_wall_len"])
    k_b = keyspace(p["charset_size"], p["second_gate_len"])
    t_a = years_to_crack(k_a, p["rate_hps"], p["seconds_per_year"])
    t_b = years_to_crack(k_b, p["rate_hps"], p["seconds_per_year"])
    cost_a = p["cost_a_password_manager"] + p["ma4_helpdesk_increment"]
    cost_b = p["cost_b_per_employee"]
    raw_a, raw_b = t_a / cost_a, t_b / cost_b
    print(f"\nTHE TRAP -- raw/unweighted metric (D2 alone, no D4 weighting):")
    print(f"  raw A={raw_a:.3e} yrs/$  raw B={raw_b:.4f} yrs/$  ratio A/B={raw_a/raw_b:.3e}")

    # Flip point for MA3, quoted in case.md/FACILITATOR.md.
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        r = evaluate({"ma3_credential_theft_cadence": mid})
        if r["B"] > r["A"]:
            hi = mid
        else:
            lo = mid
    print(f"MA3 flip point (B stops winning below this cadence): {hi:.6f}")


if __name__ == "__main__":
    main()
