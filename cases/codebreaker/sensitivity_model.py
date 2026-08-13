#!/usr/bin/env python3
"""
Sensitivity model — Codebreaker.

Reproduces case.json's derived{} numbers and gives Tier 2 probe 5 ("flex each stated
assumption by +/-50%, report which flips the verdict") a runnable model to work against.

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            subset of PARAMS probe 5 perturbs
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the twist's framing applied

The graded primary_metric (case.json) is Appendix D Convention 4's zero-error transcription
probability: the probability Klaus copies an entire cipher text by hand with NO character
errors, given a stated 0.15%-per-character error rate (a disclosed Modeling Assumption, not
a sourced figure -- no external source gives a real handwriting-under-duress error rate for
this exact scenario). Fewer characters written -> higher success probability, so evaluate()
returns that probability directly ("higher is better" already holds).

evaluate_twist() switches to the OTHER real axis this case discloses (case.md's
"Facilitator-only" section, case.json.balance) -- raw one-time keyspace, in bits of
security (log2 of the keyspace) -- to make the FACILITATOR's trap concrete: Option A wins
by a landslide on THIS metric while Option B wins the graded metric by a real, close 11.1%.
Neither call is the "real" verdict alone; the case's balance is genuinely two-axis, which
is why case.json documents both directions.

Verified against cases/codebreaker/case.json's derived{} block:
    base (P[zero errors], higher better)   A = 0.8352  ·  B = 0.9277   (margin 11.1%)
    twist (security bits, higher better)   A = 91.55   ·  B = 4.46     (margin 1953.0%)

Retuned 2026-08-13: char_error_rate moved from 0.002 to 0.0015 (see PARAMS comment and
case.json.legacy_conversion_note) after Tier 2 probe 5 found the original 0.002 broke
SPEC section 2's 20% balance cap under a +50% flex.
"""
import math

# --- Appendix A: the letter -> value table, verified against Appendix A's own worked
#     example (NEED EXTRACTION NOW) -- see legacy_conversion_note for the one worked
#     example that did NOT reproduce and was dropped rather than guessed at.
LETTER_VALUES = {
    "A": 20, "B": 17, "C": 4, "D": 8, "E": 10, "F": 22, "G": 11, "H": 16, "I": 14,
    "J": 1, "K": 9, "L": 3, "M": 12, "N": 23, "O": 15, "P": 5, "Q": 25, "R": 7,
    "S": 13, "T": 2, "U": 21, "V": 18, "W": 26, "X": 24, "Y": 6, "Z": 19,
}

# --- Appendix C: the two required messages -----------------------------------------
MESSAGES = ["Your brothers are alive", "Your wife is a double agent"]

PARAMS = {
    # Appendix D, Convention 3: the representative multiplier used for D4-D6.
    "multiplier": 2,
    # Appendix D, Convention 1: the assumed upper bound on a "single-digit multiplier"
    # the terror cell must search over for the Alphanumeric Cipher's keyspace (D1).
    "multiplier_search_max": 9,
    # Appendix D, Convention 4 (Modeling Assumption, D7's dial): probability Klaus
    # miswrites any single character under field conditions. THIS IS THE LOAD-BEARING
    # DIAL for the graded primary_metric -- flex it and watch the 11.1% margin move.
    # Retuned 2026-08-13 from 0.002 (0.2%) to 0.0015 (0.15%) -- Tier 2 probe 5 found
    # that 0.002 flexed +50% (to 0.003) pushed the margin to 23.4%, breaking SPEC
    # section 2's 20% cap. 0.0015 is still a small, defensible field-error rate (same
    # order of magnitude, same disclosed-not-sourced status -- no real source gives a
    # handwriting-under-duress error rate for this exact scenario, and none is claimed
    # for 0.0015 either) and it leaves real headroom under the cap even at +50% flex
    # (margin goes 11.1% -> 17.1%, not 15.0% -> 23.4%). See case.json.legacy_conversion_note
    # and QA_REPORT.md for the full accounting of this retune.
    "char_error_rate": 0.0015,
    # Kerckhoffs's Principle (Appendix E) is a fixed assumption, not a dial -- not
    # included here; flexing "does the adversary know the algorithm" is a different
    # case, the same way Cold Chain's docstring excludes cited measurements from FLEX.
}

# Probe 5 flexes THESE and only these -- all three are explicit, stated modeling
# conventions (Appendix D), not cited external measurements.
FLEX = ["multiplier", "multiplier_search_max", "char_error_rate"]


def _encode_A_length(message, multiplier):
    """Total handwritten characters for the Alphanumeric Cipher (Appendix A + D Conv. 2)."""
    letters = [c for c in message.upper() if c != " "]
    total = 0
    for i, ch in enumerate(letters):
        # The written symbol is always an integer (Appendix A's value times the
        # integer multiplier) -- cast explicitly so a float multiplier (e.g. from
        # probe 5's +/-50% flex, which multiplies by 1.5/0.5 and can round-trip
        # through a float even at whole-number values like 1.0/3.0) doesn't pick
        # up a spurious ".0" from str(), which would silently inflate the
        # handwritten-character count this function exists to measure.
        total += len(str(int(round(LETTER_VALUES[ch] * multiplier))))
        if i != len(letters) - 1:
            total += 1  # the "0" separator
    return total


def _encode_B_length(message):
    """Total handwritten characters for the Circle Shift Cipher (Appendix B + D Conv. 2)."""
    return len(message)  # 1:1 with plaintext incl. spaces-as-underscore, always


def _keyspace_A(params):
    return math.factorial(26) * params["multiplier_search_max"]


def _keyspace_B(message):
    n = len(message)
    return n - 1  # skip in {1, ..., n-1}; Appendix D Convention 1


# Diagnostic character-count totals from the most recent evaluate() call, kept OUT of
# the returned dict so the contract stays exactly {"A": metric, "B": metric} -- the
# generic Tier 2 probe 5 sweep picks up every key in the returned dict and compares it,
# so any extra key pollutes the sweep with numbers that aren't the graded metric.
_last_totals = {}


def evaluate(params):
    """Primary (graded) metric: probability of a zero-character-error transcription
    of both required messages combined (Appendix D Convention 4). Higher is better."""
    total_A = sum(_encode_A_length(m, params["multiplier"]) for m in MESSAGES)
    total_B = sum(_encode_B_length(m) for m in MESSAGES)
    _last_totals["A"] = total_A
    _last_totals["B"] = total_B
    p_ok = 1.0 - params["char_error_rate"]
    return {"A": p_ok ** total_A, "B": p_ok ** total_B}


def evaluate_twist(params):
    """Disclosed context metric: raw one-time keyspace, in bits (log2). Higher is better.

    This is deliberately NOT the graded primary_metric -- see module docstring and
    case.json.balance. Included so Tier 2 probe 5 can show both axes move in opposite
    directions under the same FLEX dials, which is the actual shape of this case's
    balance, not a bug to be tuned away.
    """
    kA = _keyspace_A(params)
    kB = min(_keyspace_B(m) for m in MESSAGES)  # weakest (smallest) circle-shift keyspace
    return {"A": math.log2(kA), "B": math.log2(kB)}


if __name__ == "__main__":
    base = evaluate(PARAMS)
    twist = evaluate_twist(PARAMS)
    print("base (P[zero transcription errors], higher better):", base)
    print("  margin (B over A): {:.1f}%".format((base["B"] - base["A"]) / base["A"] * 100))
    print("twist (security bits, higher better):", twist)
    print("  margin (A over B): {:.1f}%".format((twist["A"] - twist["B"]) / twist["B"] * 100))
