# Concept sheet — Cryptography & Cybersecurity (`cryptography-security`), 2026-10-27

Target: domain `cryptography-security` (cluster Digital Systems & Information). Existing cases avoided: Codebreaker (cipher
error rates), Key Length (toy RSA moduli), The Keyspace Decision (14-char password vs 2FA), The Bot Farm (graph/botnet),
The Cold Hit (DNA), plus Perimeter Protocol (KEV-based firewall AND/OR rules). Thin signature skills (n<=2) targeted:
digit, even, odd, permutation, permutation how-to. All figures below were recomputed in code on 2026-10-27/28 from live fetches.

| Rank | Concept | Skills closed (n<=2) | Tier | Data | Computed margin at operating point |
|---|---|---|---|---|---|
| 1 | C1 The Range Query | 1 term + thickens exponent | T2 | HIGH | 9.7% (A costs more) |
| 2 | C2 The Three-Day Clock | 0 thin (thickens logical-statement n=3) | T2 | HIGH counts / disclosed hours | 3.3% |
| 3 | C3 The Lock Screen | 2 (permutation + how-to) + digit | T2-T3 | MEDIUM | ~7.5% |

**Recommendation.** Write C1: cleanest live data, break-even is derived from the portal itself (the offline copy is exactly
16^5 range requests), both options provably win on either side of it. Kill nothing outright; C3 is the only one that
closes thin skills in the permutation pair, but needs a sourced entry-time figure before it clears R1b.

---

### C1 — The Range Query   ·   score ~0.6 + thickening   ·   tier T2
**Protagonist.** Priya Nair (constructed), platform engineer at a mid-size regional credit union's online-banking team,
who must wire a "reject known-breached passwords" check (NIST SP 800-63B-4 expects it) before the next audit.
**The dilemma.** A.) Call the free Pwned Passwords range API at every password set/login check (k-anonymity: send only the
first 5 hex digits of the SHA-1) OR B.) Mirror the entire dataset locally once a year (the official downloader just calls
every one of the 16^5 = 1,048,576 prefixes) and check offline.
**Primary metric.** Gigabytes transferred per year (lower wins), with the credit union's check volume as the disclosed
constructed input.
**Why it's close.** Measured mean range response is 77,478 B (n=200 random prefixes, sd 1,875 B, min 71,398, max 82,689).
Full mirror = 1,048,576 x 77,478 B = 81.2 GB; API cost = checks x 77,478 B. Break-even = 1,048,576 checks/yr per mirror
refresh. Below it A wins, above it B wins. At 1,150,000 checks/yr: A = 89.1 GB, B = 81.2 GB, B wins by 9.7%; at
900,000 checks: A = 69.7 GB, A wins by 14.2%. Operating point is set near the break-even so the argument is real
(B also removes third-party dependency and leaks no prefixes; A needs no 81 GB store and is always current).
**Would close.** `number-sense-numbers-and-counting-digit` (term, n=2; hex digits of a hash — stretch use of "digit", flag
for r1a). Thickens: `advanced-operations-how-to-evaluate-an-exponential-expression` (16^5), scientific notation. Raw ~0.6;
this is a thin-closer for one skill, so consider pairing with another crypto-security concept.
**Data feasibility: HIGH.** Fetched and confirmed:
- `https://api.pwnedpasswords.com/range/{5 hex}` (HTTP 200, no key, 200 live samples) and `https://haveibeenpwned.com/API/v3`
  (docs: free, no rate limit, never 404, Add-Padding header, offline downloader on GitHub).
- `https://haveibeenpwned.com/Passwords` (k-anonymity, "free and open source").
- Student-explorable: any student can hash a word, hit the URL in a browser, count the lines.
**Gaps / honesty.** The v3 docs say "typically about 800 per prefix" but live responses average 1,973 lines (~2.07 billion
hashes implied) — the case must use measured numbers and can make the stale-doc discrepancy a teachable moment. The offline
download size (81.2 GB) is computed (prefixes x measured mean), NOT read from a published figure; the downloader's GitHub
repo was not fetched (UNVERIFIED). Annual check volume is a constructed, disclosed assumption.
**Sensitivity (SPEC §6).** NONE (hash prefixes only; never use real passwords in the case).
**Split risk.** NONE.

---

### C2 — The Three-Day Clock   ·   score ~0.6   ·   tier T2
**Protagonist.** Marcus Oyelaran (constructed), IT operations lead for a 40-site county government who uses the CISA KEV
catalog as his patch trigger list.
**The dilemma.** A.) Staff a daily KEV triage (check every business day) OR B.) Run one weekly Thursday patch window.
**Primary metric.** KEV deadlines met per staff-hour.
**Why it's close.** Since BOD 26-04 (issued 2026-06-10) the live KEV feed carries 3-day, 14-day and 21-day due dates.
For the 47 KEV entries added 2026-06-10..2026-10-27 from ten enterprise vendors (Microsoft, Cisco, Fortinet, Ivanti, Citrix,
Palo Alto, SonicWall, VMware, Apple, Google): 37 had a 3-day clock, 10 a 14-day clock. Daily triage meets 47/47; a Thursday
window meets 36/47 (76.6%); Friday 40/47; Monday/Tuesday 15/47. With assumed 1.0 staff-hr per business day (99 business days)
vs 2.0 staff-hr per weekly window (19.9 weeks) plus e hours per item, break-even is e = 3.28 hr/item: at e = 2.63 B wins by
4.2%, at e = 3.94 A wins by 3.3%. Cheap patches favor the lean weekly window; expensive ones favor catching every deadline.
**Would close.** Thickens `discrete-mathematics-logical-statement` (n=3; "added <= window <= due"); no n<=2 skill closed.
Weak on thin-skill value; strong on student-explorable data. Possible honest add: `number-sense-even`/`odd` NOT claimed.
**Data feasibility: HIGH (counts) / assumption (hours).** Fetched: `https://www.cisa.gov/sites/default/files/feeds/
known_exploited_vulnerabilities.json` (catalogVersion 2026.10.27, 1,760 entries, fields dateAdded/dueDate/vendorProject/
forensicTriage); BOD 26-04 page `https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk`
(issued 2026-06-10, tiers from Table 1 which is an image — the 14/21-day tier numbers were NOT readable in text; use feed
dueDate values instead). NVD API `services.nvd.nist.gov/rest/json/cves/2.0?hasKev` confirmed matching count 1,760.
**Gaps.** Staff-hour inputs are constructed; BOD applies to federal agencies, county is using it voluntarily (disclose).
Overlaps data portal (not premise) with Perimeter Protocol. Entries with identical CVE ids appeared in the feed (e.g.
CVE-2026-109618 listed twice for PHP Group) — dedupe before counting.
**Sensitivity.** NONE. **Split risk.** NONE.

---

### C3 — The Lock Screen   ·   score ~2.2 (2 how-to/term thin skills + digit)   ·   tier T2-T3
**Protagonist.** Dr. Amara Singh (constructed), clinical informatics lead at a rural clinic issuing shared tablets.
**The dilemma.** A.) Android-style dot pattern, minimum 5 dots OR B.) 6-digit PIN.
**Primary metric.** Possible secrets (keyspace) per second of unlock time; NIST caps online guesses at 100 per authenticator
(SP 800-63B-4 §3.2.2, fetched), so a bigger keyspace per second of nurse time is the productive target.
**Why it's close.** Computed by exhaustive enumeration in code (not memory): valid patterns of length 4-9 = 389,112
(length 5: 7,152; 6: 26,016; 7: 72,912; 8: 140,704; 9: 140,704); length >=5 = 387,488; 6-digit PIN = 10^6; PIN without
repeats = 10P6 = 151,200. Keyspace/second: B = 10^6 / 2.4 s = 416.7k; A at 1.0 s = 387.5k (B wins 7.5%); A at 0.8 s = 484.4k
(A wins ~16%); break-even pattern time 0.93 s when PIN takes 6 taps x 0.4 s. Both win on either side of the entry-time line.
**Would close (n=2 each):** `statistics-and-probability-permutation` (term), `statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-permutation`
(how-to; the pattern count is ordered selections of distinct dots with a "no skipping an unvisited dot" rule — 10P6 PIN
variant is the clean permutation), `number-sense-numbers-and-counting-digit` (term).
**Data feasibility: MEDIUM.** Fetched: NIST SP 800-63B-4 `https://pages.nist.gov/800-63-4/sp800-63b.html` (100-attempt
limit, 15-char single-factor password minimum; the PIN activation-secret section was beyond the fetched text — UNVERIFIED).
Pattern counts are computed, student-reproducible by code. Entry-time figures (seconds) are UNVERIFIED/assumed — need a
citable HCI measurement or must be stated as a Modeling Assumption (this is why MEDIUM).
**Sensitivity.** NONE (not real-device hacking). **Split risk.** NONE. **Overlap check.** Different from The Keyspace
Decision (password length vs 2FA): this one is permutation counting under a movement rule, no 2FA, different artifact.
