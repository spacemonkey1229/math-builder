Case Study: The Keyspace Decision
MS | Math | Case Study | 2026 | Launchpad

## Overview

The dashboard on Renata Cho's second monitor is still counting. Nine hundred and forty login
attempts against the same account in the last six minutes, all from different IP addresses, all
failing, all aimed at a mid-level accounts-payable clerk named in the alert as `d.ferreira`. The
coffee she poured before the page went off is still too hot to drink. Somewhere down the row a
teammate's headset mic clicks on and off — a normal Tuesday call, nothing wrong in his corner of
the floor.

Renata is Bramwell Analytics' security operations analyst, and the identity policy on her screen
carries her name in the change log, not the CISO's. Two draft policies sit open in adjacent tabs.
One would make every employee's password longer. The other would leave passwords short and bolt a
second factor onto every login. Both drafts are dated for the board meeting where the fiscal-year
security budget gets signed, and both are dated before the auditor's follow-up visit that flagged
the current policy as a finding last quarter — a finding with her name on the remediation line.

The clerk's account survives the attempt; the credential-stuffing tool moves on to the next name on
its list within the hour. It is not this attack Renata is actually worried about. It is the one
that doesn't show up on a dashboard at all — a password typed once into a fake login page, months
before anyone notices.

Her manager's message is still sitting unread in the corner of the screen: *Which one are we
bringing to the board Thursday?*

Renata pulls both drafts onto one monitor and starts reading them side by side.

## Background

Renata Cho is the security operations analyst at Bramwell Analytics, a mid-size firm whose
employees each hold a single directory account used to sign into email, finance systems, and the
firm's client-data platform. She does not own the budget and cannot compel the board, but she
authors the password-and-authentication standard that the whole company runs on, and the
remediation plan for the auditor's finding is filed under her name (SEE APPENDIX D). If the finding
recurs at the next audit, the follow-up escalates to her director.

Two draft standards are under consideration, each meant to fully replace Bramwell's current
password policy (SEE APPENDIX A):

**The Long Wall** would require every account password to be at least 14 characters, drawn from a
stated character set, with no second authentication factor required at login.

**The Second Gate** would allow account passwords as short as 8 characters, drawn from the same
character set, but would require a second authentication factor — a phone app or hardware key — on
every login, for every account, with no exceptions.

Both standards would apply to the same population of employee accounts (SEE APPENDIX E, MA1).
Both must also satisfy one constraint neither draft can avoid: Bramwell's accounts-payable system
is a legacy platform that Bramwell does not control the code of, and it has never been updated to
accept anything past its original design — it stores only the first 8 characters of whatever
password it is given, drawn only from lowercase letters and digits, no matter how long or how
complex the password an employee actually types (SEE APPENDIX A). Whatever the company-wide
standard becomes, the accounts-payable system's real, effective password protection is capped at
that smaller keyspace, for every employee who touches it.

An attacker who wants into a Bramwell account has more than one way in. One path is to guess the
password directly, at a rate a modern offline cracking rig can sustain (SEE APPENDIX B). The other
path is to steal or phish the password from the employee, or to reuse one leaked from a breach of
some other site the employee also used it on. Public breach research measures how often real
account takeovers happen by each of these routes, and separately measures how much a second
authentication factor actually blocks — even when the attacker already has a correct password
(SEE APPENDIX C).

Each draft standard carries its own annual cost to implement and support across Bramwell's whole
employee population (SEE APPENDIX D). Where a needed figure is not a matter of public record, it is
stated as an explicit modeling assumption (SEE APPENDIX E) rather than guessed, and every sourced
figure is listed in **APPENDIX F**. A curious Hero who wants to go beyond the required math will
find further real-world reading on password security and multi-factor authentication in
**APPENDIX G** (SEE APPENDIX G). The vocabulary and the "how to…" skills this case will ask of
you are listed in **APPENDIX H** — that is where Challenge 1 sends you.

## Dilemma

You are Renata Cho.
Do you:
A.) Recommend The Long Wall — mandate 14-character passwords, no second factor OR
B.) Recommend The Second Gate — allow 8-character passwords, but require 2FA on every account

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A keyspace table (SEE APPENDIX A) for The Long Wall's nominal password, The Second
    Gate's nominal password, and the accounts-payable system's reduced effective password —
    character-set size, password length, and total possible passwords computed by the
    Fundamental Counting Principle, with the full application of the principle shown in writing
    for at least one row.
    D2. A time-to-crack table (SEE APPENDIX B) converting each of the three keyspaces from D1
    into an expected time to crack, in years, at the sourced offline guessing rate — with the
    full compound-unit conversion (guesses per second to guesses per year) shown for at least one
    row.
    D3. A collision-bound analysis of the accounts-payable system's reduced keyspace (SEE
    APPENDIX A): using the Pigeonhole Principle, find the minimum number of employees who would
    have to share that reduced keyspace before two of them are *guaranteed* to hold the identical
    accounts-payable password, and compare that number to Bramwell's actual employee count (SEE
    APPENDIX E, MA1) to state, with your reasoning shown, whether an accidental password
    collision is a real risk at Bramwell's size.
    D4. A breach-vector table (SEE APPENDIX C) showing the share of real-world account
    takeovers attributable to credential theft/phishing versus direct password guessing, and the
    published rate at which a second authentication factor blocks account takeover even when the
    attacker already holds a correct password — combined into a single expected-annual-takeover
    figure for The Long Wall and for The Second Gate.
    D5. A cost-per-dollar synthesis table (SEE APPENDIX D) combining D2's time-to-crack figures,
    D4's breach-vector-weighted takeover figures, and each standard's annual implementation and
    support cost into the case's own metric — expected time-to-crack, in years, per dollar of
    implementation and support cost — computed for The Long Wall and for The Second Gate, with
    the full arithmetic shown.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — Password Policy Specification

**The Long Wall (Option A)**

| | Value |
|---|---|
| Minimum password length | 14 characters |
| Allowed character set | Lowercase letters (26), uppercase letters (26), digits (10), symbols (8: `^ * % $ ! & @ #`) [S1] — a policy definition fixed once for both draft standards |
| Total character-set size | **70** (26 + 26 + 10 + 8) [S1] |

**The Second Gate (Option B)**

| | Value |
|---|---|
| Minimum password length | 8 characters |
| Allowed character set | Same character set as The Long Wall — **70** [S1] |
| Second factor required | Yes, on every login, every account |

**The Accounts-Payable Legacy Constraint (applies under either draft)**

| | Value |
|---|---|
| Characters actually stored | First 8 characters of whatever password is entered |
| Allowed character set actually stored | Lowercase letters and digits only |
| Character-set size | **36** (26 lowercase + 10 digits) — the same character classes tabulated in [S1], recombined |
| Employees whose accounts touch this legacy system | **80** (see Appendix E, MA2) |

## Appendix B — Offline Attack Benchmark

| | Value |
|---|---|
| Sustained guess rate, modern offline attack against the company's stored password hashes | **138,675 hashes/second** — a rented 16× Nvidia RTX 5090 GPU fleet (two racks of eight) cracking bcrypt at work factor 10, the 2026 benchmark rig [S1] |
| Seconds per year (for the compound-unit conversion in D2) | 31,536,000 (365 × 24 × 60 × 60) |

**Worked check.** At this rate, an exhaustive search of the Second Gate's nominal 8-character, 70-symbol keyspace (576,480,100,000,000 combinations) takes 576,480,100,000,000 ÷ 138,675 s⁻¹ = 4,157,053,470 s ÷ 31,536,000 s/yr ≈ **131.8 years** — matching Hive Systems' own published figure of **132 years** for an 8-character password drawn from the full character mix [S1], to within rounding. This is the same benchmark rate used for every crack-time figure in this case (SEE Challenge 3, D2).

## Appendix C — Breach-Vector Data

| | Value |
|---|---|
| Share of real-world breaches in which credential abuse — stolen, phished, or reused credentials — appears anywhere in the attack chain | **39%** [S2] |
| Share of real-world breaches whose *first* known access vector was credential abuse | 13% under the 2026 report's revised category boundaries, or **16%** on the prior year's category boundaries (comparable to earlier editions) [S2] |
| Share of real-world breaches whose first known access vector was vulnerability exploitation — a vector neither draft standard defends against | **31%** [S2] |
| Rate at which a second authentication factor blocks account takeover, even when the attacker already holds a correct, un-phished password | **98.56%** (risk reduction measured specifically on accounts whose password had already leaked) [S3] |

**A figure this case does *not* use, and why.** Published breach research does not isolate "pure brute-force guessing against an unknown password" as its own, separately measured category — Verizon's own 2026 report folds credential stuffing, password reuse, and brute-force guessing together with phished and stolen credentials into one "credential abuse" bucket, and states plainly that it cannot separate them further (SEE RESEARCH_LOG.md). Rather than invent a brute-force-only percentage that does not exist in the source, D4 uses the **39% full-chain credential-abuse share** as the case's stated allocation of "the channel where the attacker holds a valid credential, however obtained," and treats the complementary **61%** as the channel where the case's D2 crack-time figures are what actually governs the outcome (SEE APPENDIX E, MA3, for how the two channels are combined).

## Appendix D — Cost of Implementation and Support

| | Value |
|---|---|
| Bramwell's employee headcount used to scale both standards | **400** (see Appendix E, MA1) |
| The Long Wall — annual cost per employee | **$60.00** = **$48.00** business password-manager licensing, needed because a company-wide 14-character minimum is not practical to remember without one [S5], **+ $12.00** assumed incremental help-desk cost from a higher forgotten-password rate (see Appendix E, MA4) |
| The Long Wall — annual cost, full headcount | **$24,000.00** (400 × $60.00) |
| The Second Gate — annual cost per employee | **$36.00** — Duo Essentials MFA, the entry-level paid tier that supports company-wide enforcement [S4] |
| The Second Gate — annual cost, full headcount | **$14,400.00** (400 × $36.00) |
| Auditor's remediation deadline this policy responds to | Texture only — not load-bearing in any calculation. No dated figure is stated. |

**A widely repeated figure this case excludes.** Industry articles commonly cite "$70 per help-desk password reset," usually attributed to Forrester Research. No dated, primary Forrester publication stating that figure could be located and fetched in this session — every citation found was a secondary repetition of the same unlinked number (SEE RESEARCH_LOG.md). Per this project's sourcing standard, an unverifiable widely repeated figure is excluded rather than used; Appendix E, MA4 states a smaller, explicitly unsourced assumption in its place.

## Appendix E — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author. A Hero may challenge them in discussion — that is a legitimate move, and APPENDIX H
> names the skills a Hero would need to test one.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Bramwell's employee headcount | **400 employees** | Bramwell is fictional. 400 sits in the middle of the commonly used 100–999 employee band for "mid-size company." | Scales both options' total dollar cost identically (D5's per-employee metric is unaffected) and scales D3's pigeonhole comparison headcount proportionally. Does not change which option wins D5's per-employee metric. |
| MA2 | Fraction of Bramwell's employees whose accounts touch the accounts-payable legacy system | **20% (80 employees)** | No real company's finance-system access list is public; 20% is a plausible finance/accounts-payable-adjacent share for a mid-size firm. | Directly sets the headcount D3 compares against the pigeonhole guarantee threshold. Because that threshold (2,821,109,907,457) exceeds any plausible employee count by nine to eleven orders of magnitude, no realistic value of MA2 changes D3's conclusion. |
| MA3 | Annual rate at which a given employee account experiences a *successful* credential-theft or phishing-based compromise attempt (used to combine Appendix B's crack-time channel with Appendix C's credential-abuse channel in D5) | **0.008 (0.8% of employee accounts per year)** | No public source states an annual per-account success rate for this specific event. Deliberately conservative — well below commonly cited employee phishing-*susceptibility* rates, which describe click-throughs rather than completed credential theft. This is the case's most load-bearing, least certain dial, stated openly rather than buried in D5's table. | The primary metric weights the credential-abuse channel directly by this rate, so **the final comparison is sensitive to this value.** A Hero who argues Bramwell's employees are meaningfully more or less phishing-prone than this assumption has found the case's real fault line — that argument is worth making with numbers, not just intuition. |
| MA4 | The Long Wall's incremental annual help-desk cost per employee, beyond password-manager licensing, from a higher forgotten-password rate under a 14-character minimum | **$12.00 per employee per year** | No independently verifiable per-employee figure exists (SEE APPENDIX D — the commonly repeated "$70 per reset" figure is excluded as unsourced). $12 is a stated, modest placeholder scenario value, deliberately small relative to the sourced $48 password-manager cost it sits beside. | Adds linearly to The Long Wall's per-employee cost ($48 + MA4). **The final comparison is sensitive to this value**, since it moves Option A's cost denominator directly; a Hero who thinks Bramwell's actual help-desk load would run higher or lower than this placeholder has a legitimate lever to pull on. |

## Appendix F — Sources

| id | Claim | Value | Source | Accessed | Confidence |
|---|---|---|---|---|---|
| S1 | Offline password-cracking benchmark rate, hashing algorithm, and the character-set composition used to build it | 138,675 H/s aggregate, 16× RTX 5090 fleet, bcrypt cost factor 10; charset = 26 lower + 26 upper + 10 digit + 8 symbol = 70; 8-char full-mix crack time 132 years | Hive Systems, *2026 Password Table* ([landing page](https://www.hivesystems.com/password-table)) and *"The 2026 Password Table Is Here: How Fast Can a Hacker Crack Your Password?"* ([article](https://www.hivesystems.com/blog/are-your-passwords-in-the-green)) | 2026-08-13 | HIGH — a named, dated, primary benchmark publisher; this case's own from-scratch recomputation of the 8-character full-mix crack time from the stated rate and charset (131.8 years) matches Hive Systems' own published 132-year figure to within rounding, an independent cross-check |
| S2 | Share of breaches involving credential abuse (full chain and initial-vector), and share whose initial vector was vulnerability exploitation | Credential abuse in the full breach chain: 39%; initial-vector credential abuse: 13% (16% on prior-year category boundaries); initial-vector vulnerability exploitation: 31% | Verizon, *2026 Data Breach Investigations Report* (verizon.com/dbir) — figures corroborated identically across three independent secondary summaries: Descope ([link](https://www.descope.com/blog/post/verizon-dbir-2026)), Push Security ([link](https://pushsecurity.com/blog/verizon-dbir-2026-review)), and Tech Insider ([link](https://tech-insider.org/verizon-dbir-2026/)) | 2026-08-13 | MEDIUM — this case could not directly fetch readable text from Verizon's own PDF (binary/encoded response); the figures are used on the strength of three independent secondary sources reporting the same numbers from the named primary report, which is the case-research procedure's Tier-3 standard, not Tier-1 |
| S3 | Reduction in account-compromise risk from multi-factor authentication, measured specifically on accounts whose password had already leaked | 98.56% risk reduction (and 99.22% across the full population) | Meyer, L.A., Romero, S., Bertoli, G., Burt, T., Weinert, A., Lavista Ferres, J. (Microsoft Research), *"How effective is multifactor authentication at deterring cyberattacks?"*, May 2023 ([arXiv:2305.00945](https://arxiv.org/abs/2305.00945)) | 2026-08-13 | HIGH — a named, authored measurement study of Azure Active Directory accounts, not a marketing claim; independently corroborated by a secondary summary ([securityscientist.net](https://www.securityscientist.net/blog/how-effective-is-mfa/)) quoting the identical figures |
| S4 | The Second Gate — per-seat price of the entry-level paid MFA tier suitable for company-wide enforcement | $3.00 per user per month ($36.00/year) | Cisco, *Duo Editions and Pricing*, "Essentials" tier ([link](https://duo.com/editions-and-pricing)) | 2026-08-13 | HIGH — primary vendor pricing page, fetched directly |
| S5 | The Long Wall — per-seat price of a business password manager | $4.00 per user per month ($48.00/year) | Bitwarden, *Pricing*, "Teams" plan ([link](https://bitwarden.com/pricing/)) | 2026-08-13 | HIGH — primary vendor pricing page, fetched directly |

## Appendix G — Learn More

These are real, currently-live resources for a Hero who wants to go beyond this case's required
math and read more about password security, credential theft, and multi-factor authentication in
the real world. They are optional background, not graded content.

- [NIST Special Publication 800-63B — Digital Identity Guidelines: Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html) — the U.S. government's own current technical standard for password length, composition, and multi-factor authenticator requirements, the real-world rulebook both draft standards in this case are trying to satisfy.
- [Have I Been Pwned](https://haveibeenpwned.com/) — a free, widely used breach-notification service where anyone can check whether an email address or password has appeared in a known data breach, the same kind of leaked-credential data that fuels the credential-stuffing attack Renata is watching.
- [Krebs on Security — "Credential Stuffing" coverage](https://krebsonsecurity.com/tag/credential-stuffing/) — ongoing reporting by security journalist Brian Krebs on real credential-stuffing incidents and the forced password resets companies use to respond to them.
- [Microsoft Security Blog — "One simple action you can take to prevent 99.9 percent of account attacks"](https://www.microsoft.com/en-us/security/blog/2019/08/20/one-simple-action-you-can-take-to-prevent-99-9-percent-of-account-attacks/) — Microsoft's own accessible summary of the multi-factor-authentication research this case draws on in Appendix F, S3.
- [Computerphile — "Password Cracking"](https://www.youtube.com/watch?v=7U-RbOKanYs) — a short video from the University of Nottingham's Computerphile channel explaining, in plain terms, how real offline password-cracking attacks like the one in Appendix B actually work.

## Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Fundamental Counting Principle
- Pigeonhole Principle

**"How to…" questions**

- How to apply the Fundamental Counting Principle to count outcomes
- How to convert an amount with compound units
- How to find the percent of a number

<!-- FACILITATOR ONLY -->

## Balance argument (facilitator only — never shipped to students)

**The trap, stated up front.** D2 alone makes this look like the least close case imaginable.
The Long Wall's nominal keyspace (70¹⁴ ≈ 6.78 × 10²⁵) takes an expected **1.55 × 10¹³ years** to
exhaust at the sourced benchmark rate; The Second Gate's nominal keyspace (70⁸) takes **131.8
years**. Divided naively by cost, The Long Wall "wins" by a factor of roughly **70 billion** — a
number so large it is meaningless, and any Hero who stops at D2 will report exactly that number
with total confidence. **This is the wrong answer, and finding out why is the case.**

**Argument for A (The Long Wall).** A fourteen-character password drawn from a 70-character set is
brute-force-infeasible by any realistic measure: even at a modern GPU-cracking rig's rate, exhausting
its keyspace takes trillions of years. The cost is modest and mostly one-time (a $4/seat/month
password manager plus a small assumed support increment), with no ongoing per-login friction for
employees. If the threat that matters is an attacker who has stolen a copy of the password hashes
and is guessing offline, The Long Wall ends the conversation before it starts.

**Argument for B (The Second Gate).** Real account takeovers overwhelmingly do not happen this way.
Credential abuse — stolen, phished, or reused passwords — appears somewhere in the chain of **39%**
of real-world breaches [S2], and none of that channel cares how long the password is: an attacker
who phishes the actual password walks in regardless of whether it was 8 characters or 40. A second
factor is the one control in this case that defends that channel directly, cutting the risk of a
successful takeover **even when the attacker already has a correct password** by **98.56%** [S3].
Weighting each option's protection by how real attackers actually get in — not by an idealized
offline-guessing scenario — The Second Gate comes out ahead on the case's own primary metric,
**and does so at a lower dollar cost per employee** ($36/year against The Long Wall's $60/year).

**Margin.** `margin_pct` = **10.1**. `margin_basis`: for each option, combine (a) the annual
probability of compromise via direct password guessing (1 ÷ D2's crack-time figure) and (b) the
annual probability of compromise via the credential-abuse channel (Appendix E MA3's stated annual
attempt rate, un-mitigated for Option A, reduced by [S3]'s 98.56% for Option B), weighted 61%/39%
by [S2]'s vulnerability-exploitation/credential-abuse split; invert the combined annual probability
to get expected years to compromise; divide by each option's annual per-employee cost (Appendix D).
Computed: Option A ≈ **320.5 years** combined expected time to compromise ÷ **$60.00** = **5.34
years per dollar**. Option B ≈ **214.0 years** ÷ **$36.00** = **5.94 years per dollar**. The Second
Gate wins by **10.1%** — genuinely close, and entirely dependent on Appendix E MA3's stated
attack-rate assumption, disclosed there as the case's single most load-bearing dial.

**Sensitivity note (SPEC §6).** None required. The stakes are professional and organizational (an
audit finding, a security-operations analyst's remediation record) — not personal loss or family
hardship.
