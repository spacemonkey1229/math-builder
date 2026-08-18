# RESEARCH_LOG — The Keyspace Decision

One row per placeholder enumerated from `case.md` at hand-off from `case-write` (16 tokens), plus
a note on the metric redesign this research pass required.

| # | Placeholder (abbreviated) | Searched | Found | Outcome |
|---|---|---|---|---|
| P01 | Charset composing the standard password policy | "Hive Systems 2026 password table" | Hive Systems' 2026 Password Table publishes a full-mix charset (lower/upper/digit/8 symbols = 70) as the standard it benchmarks against | SOURCED — S1. Adopted as Bramwell's own policy charset rather than inventing a separate one, so D1/D2 stay internally consistent with the benchmark rate in S1. |
| P02 | Total charset size | (same fetch as P01) | 70 | SOURCED — S1, arithmetic (26+26+10+8). |
| P03 | Legacy AP-system charset size | (derived from P01/P02) | 36 (26 lowercase + 10 digit, a subset of S1's own classes) | SOURCED — S1, recombination, not a separate external fact. |
| P04 | Fraction of employees with AP-system access | "accounts payable staff percentage of company headcount" — no company-specific or industry-average figure exists for a fictional firm | NOT FOUND (expected; Bramwell is fictional) | ASSUMPTION — MA2, 20%. |
| P05 | Offline guess rate benchmark | "Hive Systems 2026 password table time to crack GPU benchmark"; fetched hivesystems.com/password-table (landing page only, no rate) and hivesystems.com/blog/are-your-passwords-in-the-green (full figures) | 138,675 H/s aggregate, 16x RTX 5090 fleet, bcrypt cost 10, dated 2026-07-14 | SOURCED — S1. Cross-checked: recomputing the 8-char/70-charset crack time from this rate gives 131.8 years, matching Hive's own published "132 years" almost exactly — validates using this rate for the case's own derived figures (14-char and legacy-charset crack times), which Hive does not itself publish. |
| P06 | Share of breaches from credential theft/phishing/reuse | "Verizon 2026 DBIR credentials phishing percent initial access"; attempted direct fetch of the DBIR executive-summary PDF (returned only binary/encoded content, not usable); fetched three independent secondary summaries instead (Descope, Push Security, Tech Insider) | 39% full-chain credential abuse; 13% initial-vector (16% on prior-year category boundaries) | SOURCED — S2, MEDIUM confidence (Tier-3 corroboration, not a direct primary-document fetch). |
| P07 | Share attributable to direct password guessing / brute force, specifically | "DBIR 2026 hacking action varieties brute force percent"; "Verizon DBIR brute force initial access vector percentage 2025 2026" | The 2026 DBIR does not publish a standalone "brute force" percentage separate from "credential abuse" — Verizon's own category folds credential stuffing, reuse, phished, and guessed credentials together, and none of the secondary sources found could isolate a brute-force-only figure | **NOT FOUND, then REDESIGNED** (the important case). The original placeholder asked for a number that does not exist in the published literature, because real breach taxonomies do not track "an attacker who had zero prior information and had to guess" as its own category — in practice, attackers almost never do this against a live system (rate-limiting defeats it) and instead either crack stolen hashes offline (which D2 already models directly from the keyspace) or steal the credential outright (which is what "credential abuse" measures). Rather than invent a percentage, Appendix C and D4 were redesigned: D2's crack-time figures stand on their own as the "direct guessing" channel, and the sourced 39% full-chain credential-abuse share stands in for "the channel where the attacker already holds a credential, however obtained." This is a genuine redesign, not a workaround — see `case.json.needs_source[]` entry (status DROPPED) and the case.md Appendix C callout box. |
| P08 | MFA-blocking rate, correct-password case | "Microsoft 99.9% compromised accounts MFA"; then "Microsoft Digital Defense Report MFA blocks 99.9%"; then '"How effective is multifactor authentication at deterring cyberattacks" Microsoft Research 99.22' | Microsoft's 2019 blog post states "99.9%" with no stated methodology or dataset. A separate, later, authored Microsoft Research measurement study (Meyer et al. 2023, arXiv:2305.00945) states 99.22% across the full population and 98.56% specifically for accounts whose password had already leaked, with a named dataset (Azure AD) and named authors | SOURCED — S3. The 98.56% figure was chosen over the more commonly repeated 99.9% marketing claim specifically because it is methodologically documented (a named study, not a blog assertion) and matches D4's own framing (2FA blocking takeover *even when the attacker already has a correct password*) more precisely than the older figure. |
| P09 | Long Wall annual cost | "average cost per password reset help desk call Forrester Gartner 2026" | The commonly repeated "$70 per password reset" figure traces everywhere back to "Forrester Research" with no dated, primary, fetchable Forrester publication behind it — a pattern matching SPEC §5's own named precedent (the "50% of vaccines wasted" figure). Every hit was a secondary repetition of the same unlinked number. | **NOT FOUND, excluded.** Per SPEC §5, a widely repeated but unverifiable figure is excluded rather than used. Redesigned: the case instead prices a real, sourced business password-manager licence (S5, Bitwarden Teams, $48/employee/year — a genuinely necessary companion cost for a company-wide 14-character mandate, since employees cannot memorize compliant passwords without one) plus a small, explicitly stated Modeling Assumption (MA4, $12/employee/year) for the excluded help-desk effect, rather than presenting an unsourced industry number as if it were cited. |
| P10 | Second Gate annual cost | "Duo MFA pricing per user per month 2026"; fetched duo.com/editions-and-pricing directly | $3.00/user/month, "Essentials" tier | SOURCED — S4, HIGH (primary vendor page, fetched directly). |
| P11 | Remediation deadline | n/a — the placeholder itself instructed "record here only if found; otherwise omit" | Not searched separately; the placeholder was written at case-write time as explicitly non-load-bearing texture | DROPPED, as anticipated. No deadline appears anywhere in `case.md`'s calculations. |
| P12-P14 | MA1 (headcount) value/basis/sensitivity | "mid-size company employee count definition" | No public, citable, universally agreed numeric definition of "mid-size company" exists (conventions vary 100-999, 50-500, etc., by agency/purpose) | ASSUMPTION — MA1, 400 employees, stated basis (middle of the commonly used 100-999 band). |
| P15-P16 | Facilitator-only Balance argument (Argument for A / Argument for B) | n/a — drafted from D1/D2/D4's now-sourced figures | — | SOURCED (drafted), see case.md facilitator-only section and `case.json.balance`. |

## A note on the metric redesign — the actual finding of this research pass

The single most important result of this research session was not a number — it was discovering
that **the case's primary metric, taken completely literally, can never be close.**

D1's own arithmetic makes this a mathematical certainty rather than a modeling choice: on a fixed
70-character alphabet, a 6-character length difference (14 vs. 8) produces a keyspace ratio of
70⁶ ≈ 1.17 × 10¹¹, *independent of attack rate, hashing algorithm, or cost*. Dividing raw D2
crack-times by any realistic dollar-cost figure therefore makes Option A "win" the literal metric
by roughly seventy billion — a gap no amount of honest cost-tuning can close (verified directly:
matching Option A's raw metric to Option B's would require Option A's annual cost to be on the
order of **$3.5 trillion per employee**).

This is disclosed rather than hidden. The redesign adopted — combining D2's crack-time channel
with D4's breach-vector-weighted credential-abuse channel into a single "expected years to
compromise" figure per option (documented in full in `case.json.balance.margin_basis` and in
`sensitivity_model.py`) — produces a margin of **10.1%**, genuinely close and entirely dependent
on Appendix E MA3's stated (unsourced, explicitly flagged) annual attack-cadence assumption. The
raw, unweighted metric is preserved in the case as **the trap**: a Hero who reports D2's numbers
without doing D4's weighting will confidently recommend Option A by an astronomical, meaningless
margin. Flagged explicitly for whichever pass runs `case-qa` next: the case's balance rests on one
named, disclosed assumption (MA3), not on a robust structural feature of the underlying math.

## Verification (case-research SKILL.md step 7)

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
INCOMPLETE sources: none
LOW-confidence sources: none
```

See `sensitivity_model.py` for the reproducible computation of every derived figure in
`case.json.derived`.
