# Research log — Fixed Or Flex

Stage 3, run 2026-10-28. All NTD figures fetched live from the Socrata API and recomputed in Python (`sensitivity_model.py` reproduces the headline numbers).

| Placeholder / need | Searched / fetched | Found | Result |
|---|---|---|---|
| Opex, revenue hours, unlinked trips, revenue miles, passenger miles, fare revenue, WCTA MB and DR, RY2022-2024 | `https://data.transportation.gov/resource/ekg5-frzt.json?ntd_id=30044` (HTTP 200, 8 rows) | Appendix A rows copied cell-for-cell | SOURCED S1, HIGH |
| RY2025 rows (Twist only) | same call | MB 8,267,834 / 44,819 / 204,462; DR 6,981,124 / 76,918 / 164,014 | SOURCED S5 (facilitator-only; not cited in case.md) |
| Field definitions; passenger-miles caveat; licence | `https://data.transportation.gov/api/views/ekg5-frzt` (200) | Column descriptions, "Only Full Reporters report data on Passenger Miles", license Public Domain U.S. Government (usa.gov/government-works) | SOURCED S2, HIGH. Resolves the concept sheet's UNVERIFIED glossary note: the case quotes the dataset's own field descriptions. |
| Fixed-route count, Flyer routes, GO Westmoreland programs | WebFetch `https://www.westmorelandtransit.com` | 15 routes listed (1F,2F,3F,4,5,6,8,9,11,12,14,14F,15,16,17); Flyers 1F,2F,3F,14F; programs: Senior Shared-Ride, ADA Complementary Paratransit, Persons with Disabilities Transportation, Medical Assistance Transportation Program | SOURCED S3, HIGH. "15" is the site's menu count, not used in any calculation. |
| Senior Shared-Ride eligibility, funding, purposes | WebFetch `https://www.westmorelandtransit.com/senior-shared-ride` | 65 or older, proof of age; PA State Lottery; "any purpose". Booking lead time not stated on the page. | SOURCED S4, HIGH. Booking rules not used. |
| Official NTD glossary definition of unlinked trip | `transit.dot.gov/ntd/national-transit-database-ntd-glossary` via curl with browser UA | HTTP 403 Access Denied | NOT FOUND. Exit taken: use the dataset's own column descriptions (S2) instead. |
| DR trip split among programs | WCTA pages; dataset columns | Not published | NOT FOUND, load-bearing only through `w`. Exit: not assumed; carried by `w` (M5). |
| Date RY2024 rows first published | dataset metadata gives only rowsUpdatedAt (epoch 1791989479, i.e. 2026-10) | n/a | UNVERIFIED; case names no publication date, only M0. |
| WCTA passenger-mile sampling method | none found | n/a | UNVERIFIED; passenger-miles lens flagged soft in Appendix A. |
| rho_F, rho_D, w, $100,000, 520 convention | no public source exists | n/a | ASSUMPTION M1-M6 (visible block, ranges, bases). |

## Derivations (python)
cost/hr = opex / hours; trips/hr = trips / hours; trips per $100k = trips / opex x 1e5; hours bought = 1e5 / (cost/hr). RY2024: fixed 174.09, 4.698, 574.4 h, 2,698.4; vans 87.89, 2.218, 1,137.8 h, 2,523.7. Margin = (2,698.4 - 2,523.7)/2,698.4 = 6.475% -> 6.48%. rho_F* = 0.9352, w* = 1.0692, break-even trips/hr 4.393 (fixed) and 2.372 (vans). Signed gap D: +462.8, +160.3, -174.7; slope -318.76; RY2025 line value -493.5 (actual -123.6). Passenger-miles per $100k 34,344 vs 28,952 (A by 15.70%).

## Stale-data check
Pre-2022 NTD metrics live in a different table and were not fetched. RY2024-2025 are post-COVID recovery years (disclosed in FACILITATOR).
