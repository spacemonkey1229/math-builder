# Research Log — The Skin Pack Atlas

Case-research pass, 2026-08-30. 18 open `{{NEEDS_SOURCE}}` placeholders enumerated from
`case.md` in document order (P01–P18). Recorded below: what was searched, what was found or
rejected, and the final disposition of each.

---

### P01 / P02 — Tanager Games' India / Nigeria active installs (invented studio figures)

No real "Tanager Games" or "Molt" exists (the case says so explicitly). No search performed —
this is a disclosed fictional business figure by design. **Disposition: ASSUMPTION (MA1).**
Chosen: India = 40,000 active installs, Nigeria = 20,000 active installs. Sized so the resulting
matrix M is well-conditioned (nonzero, non-degenerate determinant) and so revenue-per-install
rates solved via D4 land in a plausible mobile-game ARPU range (see P07/P08 below).

### P03 / P04 — Value-tier (Mali-400-class) GPU share, India / Nigeria

Search 1: `Android GPU vendor share by country India Nigeria Mali Adreno percent devices` —
surfaced DeviceAtlas's "Most used mobile GPUs in 2017" blog post as the strongest lead, matching
exactly the six-country set (India, Nigeria, Argentina, Poland, Spain, Germany) the concept sheet
asked for.
Direct fetch of `https://deviceatlas.com/blog/most-used-mobile-gpus-2017` (twice, second time
asking for verbatim quotes only, to rule out summarizer hallucination) confirmed the article
itself states: *"We noticed that the ARM Mali gets the largest share in developing markets, such
as Nigeria (53%), Colombia (45%), and India (42%)."* and *"Countries where Qualcomm's Adreno has
a significant share include Argentina (44%), Poland (40%), Spain (37%), and Germany (31%)."*
**Disposition: SOURCED (S2).** India = 42% Mali (Value-tier), Nigeria = 53% Mali (Value-tier).
Confidence MEDIUM — real named source (DeviceAtlas, a device-detection/analytics company) with a
specific date (Sept 2017 post, Q2 2017 web-traffic data), but (a) 9 years stale as of 2026, (b)
a web-traffic proxy for install base rather than a true install census, and (c) the category is
"Mali" broadly, not "Mali-400" specifically — see the note on P11 below for why this is used as a
proxy anyway, consistent with the case's existing MA2.

### P05 / P06 — Flagship-tier (complement) share, India / Nigeria

Derived, not separately searched: Flagship-tier share = 100% − Value-tier share, per the
case's own Appendix A structure (only two tiers modeled). India = 58%, Nigeria = 47%.
**Disposition: SOURCED (derived from S2).**

### P07 / P08 — Tanager Games' India / Nigeria monthly skin-pack revenue (invented studio figures)

No real studio, no search performed — disclosed fictional figure. **Disposition: ASSUMPTION
(MA1).** Chosen: India = $21,080/month, Nigeria = $9,110/month. These were reverse-engineered
from a target, plausible revenue-per-active-install split by tier ($0.80/month for Flagship-tier
installs, $0.15/month for Value-tier installs — consistent with the case's own narrative that
heavier-spending players cluster on newer devices) times each market's tier-split install counts
from P01–P06, then used as the case's stated total-revenue inputs. This keeps the invented
numbers internally consistent with the real, cited device-tier composition, per MA1's basis
statement in the original draft.

### P09 — Computed matrix M entries

Pure arithmetic once P01–P06 are filled: each entry = market's total installs × that market's
tier share (Appendix B's own stated definition). No search needed.
M = [[23200, 16800], [9400, 10600]] (rows India/Nigeria, columns Flagship/Value).
**Disposition: SOURCED** (derived; cites the same P01–P06 inputs, shown in full in case.md).

### P10 — Android GPU-maker share among Unity's own mobile players

Search: `Unity "Mobile Hardware Statistics" blog GPU share Qualcomm ARM Imagination NVIDIA`.
The canonical URLs (`blog.unity.com/technology/mobile-hardware-statistics-and-more`,
`unity.com/blog/technology/mobile-hardware-statistics-and-more`) both returned HTTP 403 to a
direct fetch in this environment (likely bot-blocking on unity.com's current CDN). Fell back to
two independent republications that quote the post directly: Game Developer (formerly Gamasutra)
at `gamedeveloper.com/programming/mobile-and-more-hardware-statistics`, and Aras Pranckevičius's
personal blog (a named ex-Unity graphics engineer) at
`aras-p.info/blog/2013/04/07/mobile-hardware-stats-and-more/`, mirroring the original 2013-04-07/08
Unity post. Both independently gave identical figures: Qualcomm 37%, ARM 32%, Imagination 22%,
NVIDIA 6%. **Disposition: SOURCED (S1).** Confidence MEDIUM: the claim is Unity's own, and two
independent mirrors agree verbatim, but the primary unity.com URL could not be directly verified
in this session (403), and the post itself is from April 2013 — 13 years stale, a material
caveat disclosed in the Sources appendix note.

### P11 — Mali-400-class share of ARM's Android footprint

Same source as P10. Verbatim quote recovered from both mirrors: *"ARM share is almost entirely
Mali 400. Strangely enough, almost no latest generation (Mali T6xx) devices."* No numeric
percentage is given in the original post — it is a qualitative claim ("almost entirely"), not a
percentage. **Disposition: SOURCED (S1)**, recorded as the qualitative claim it actually is
(no invented percentage substituted for the missing number).

### P12 / P13 — Regional Mali-vs-Adreno share, India / Nigeria

Same finding as P03/P04 — DeviceAtlas gives Mali share for these two markets directly (42% India,
53% Nigeria), which is the same figure used for the Value-tier row. **Disposition: SOURCED (S2).**

### P14 — Regional Mali-vs-Adreno share, comparison markets (Argentina, Poland, Spain, Germany)

Same DeviceAtlas post, same verbatim-quote fetch: Argentina 44% Adreno, Poland 40% Adreno, Spain
37% Adreno, Germany 31% Adreno (Mali share not separately broken out for these four in the
source; only their Adreno lead is stated). **Disposition: SOURCED (S2)**, recorded as Adreno
share since that is what the source actually reports for these four countries — not converted
into an invented Mali complement.

### P15 — Maximum 2D texture dimension per GPU generation tier (2048 / 4096 / 8192 / 16384)

Four separate primary-source lookups, one per tier:
- **2048 and 4096**: Apple's own (now-archived) *OpenGL ES Hardware Platform Guide for iOS*
  (`developer.apple.com/library/archive/.../OpenGLESPlatforms.html`), fetched directly. Table 1-2
  states `MAX_TEXTURE_SIZE` = 2048×2048 for the PowerVR SGX 535 generation (iPhone 3GS, iPhone 4,
  original iPad) and 4096×4096 for the SGX 543 generation (iPhone 4S, iPhone 5, iPad 2, iPad 3).
  **HIGH** confidence — Apple's own primary capability table, exact devices named, unambiguous
  units.
- **4096, corroboration for Mali-400 specifically**: searched
  `Mali-400 MP maximum texture size 4096 GPU specification`; found consistent citation across
  multiple independent search results of ARM's own FAQ (`ka13314`, "What is the maximum
  framebuffer and texture resolution supported by Mali-400 MP?") stating the max is 4096 along
  any axis, per TRM section 3.13.5. Direct fetch of `infocenter.arm.com/help/topic/.../ka13314.html`
  failed in this environment (TLS certificate mismatch against ARM's Akamai CDN), so this could
  not be independently re-verified by direct fetch. **MEDIUM** confidence — not directly
  fetched, but corroborates (does not solely carry) the already-HIGH-confidence Apple figure for
  the same 2011-era GPU generation.
- **8192**: Unreal Engine's own documentation,
  `dev.epicgames.com/documentation/en-us/unreal-engine/texture-format-support-and-settings-in-unreal-engine`,
  fetched directly: *"Unreal Engine supports texture resolutions from 1x1 up to 8192x8192."*
  **HIGH** confidence — engine's own current documentation.
- **16384**: Unity's own documentation,
  `docs.unity3d.com/ScriptReference/SystemInfo-maxTextureSize.html`, fetched directly: *"Unity
  only supports textures up to a size of 16384, even if `maxTextureSize` returns a larger size."*
  **HIGH** confidence — Unity's own current documentation, and directly relevant since Tanager
  Games is stated (Appendix D of the concept sheet / case background) to be a Unity-based studio.
**Disposition: SOURCED (S3, S4, S5, S6).**

### P16 / P17 — Minimum GPU tier required for the Crest Atlas (8192) / Anchor Atlas (4096)

Pure derivation from P15's ladder, no separate search: an 8192×8192 texture requires a GPU whose
`MAX_TEXTURE_SIZE` ≥ 8192 — i.e. a modern Flagship-tier GPU (per Appendix C/D's own two-tier
model, this is the Flagship tier). A 4096×4096 texture requires `MAX_TEXTURE_SIZE` ≥ 4096, which
the Value-tier (Mali-400-class, capped exactly at 4096) already satisfies. **Disposition:
SOURCED** (derived from S3/S4/S5/S6, cited in case.md).

### P18 — MA1 sensitivity language (final wording)

Written once P01/P02/P07/P08's actual values were chosen. Per the case-research skill's
placeholder-discipline rule, this states that the outcome is sensitive to the invented
install/revenue figures without disclosing size or direction of that sensitivity (the actual
margin and winning option are recorded in `FACILITATOR.md` and `case.json`'s `balance` object
only). **Disposition: ASSUMPTION (MA1, finalized).**

---

## Rejected / not used

- An AI-generated web-search summary (not a direct page fetch) initially returned country-level
  GPU shares for India/Nigeria/Argentina/Poland/Spain/Germany while, in the same breath, saying
  "I didn't find specific data for Mali in the search results" — an internally contradictory
  response that reads as a fabricated/hallucinated summary layered on top of real search
  snippets. Not used directly; instead, the actual DeviceAtlas source page it was drawing from
  was identified and fetched directly, with a follow-up fetch specifically requesting verbatim
  quotes (rather than a paraphrase) to confirm the numbers actually appear in the article before
  they were accepted. This is the reason P03/P04/P12/P13/P14 above were double-fetched rather
  than accepted from the first search result.
- `unity.com/blog/technology/mobile-hardware-statistics-and-more` and
  `blog.unity.com/technology/mobile-hardware-statistics-and-more` — both current canonical URLs
  for Unity's own post — returned HTTP 403 to direct fetch in this environment. Not used as the
  cited `url` for S1 as a result; two independent mirrors were used instead (see P10).
- ARM's own `ka13314` FAQ page — could not be fetched due to a TLS certificate mismatch in this
  environment (the host resolves to an Akamai edge whose certificate doesn't cover
  `infocenter.arm.com`). Not used as the sole citation for the Mali-400 4096 figure; downgraded
  to a MEDIUM-confidence corroborating citation alongside the directly-fetched, HIGH-confidence
  Apple SGX 543 table (same GPU generation, same 4096 cap).
- No attempt was made to invent a numeric percentage for "how much of ARM's share is Mali-400"
  (P11) since Unity's own post only ever states this qualitatively ("almost entirely"). The
  qualitative claim is cited as-is rather than manufacturing a false-precision percentage.

## Summary table

| P# | Value | Status | Source(s) | Confidence |
|---|---|---|---|---|
| P01 | India installs = 40,000 | ASSUMPTION | MA1 | — |
| P02 | Nigeria installs = 20,000 | ASSUMPTION | MA1 | — |
| P03 | India Value-tier share = 42% | SOURCED | S2 | MEDIUM |
| P04 | Nigeria Value-tier share = 53% | SOURCED | S2 | MEDIUM |
| P05 | India Flagship-tier share = 58% | SOURCED (derived) | S2 | MEDIUM |
| P06 | Nigeria Flagship-tier share = 47% | SOURCED (derived) | S2 | MEDIUM |
| P07 | India revenue = $21,080/mo | ASSUMPTION | MA1 | — |
| P08 | Nigeria revenue = $9,110/mo | ASSUMPTION | MA1 | — |
| P09 | M = [[23200,16800],[9400,10600]] | SOURCED (derived) | P01–P06 | — |
| P10 | Qualcomm 37% / ARM 32% / Imagination 22% / NVIDIA 6% | SOURCED | S1 | MEDIUM |
| P11 | ARM share "almost entirely" Mali-400 (qualitative) | SOURCED | S1 | MEDIUM |
| P12 | India Mali share = 42% | SOURCED | S2 | MEDIUM |
| P13 | Nigeria Mali share = 53% | SOURCED | S2 | MEDIUM |
| P14 | Argentina 44% / Poland 40% / Spain 37% / Germany 31% Adreno | SOURCED | S2 | MEDIUM |
| P15 | 2048 / 4096 / 8192 / 16384 px ladder | SOURCED | S3, S4, S5, S6 | HIGH (2048/4096/8192/16384), MEDIUM (Mali-400 corroboration) |
| P16 | Crest Atlas (8192) needs Flagship-tier | SOURCED (derived) | S3, S5 | HIGH |
| P17 | Anchor Atlas (4096) needs Value-tier | SOURCED (derived) | S3, S4 | HIGH/MEDIUM |
| P18 | MA1 sensitivity language | ASSUMPTION | MA1 | — |

**NOT FOUND count: 0.** Every placeholder resolved to either a cited source or a disclosed
Modeling Assumption. Zero placeholders remain OPEN.

Next step: `case-readiness`.

---

## Re-research pass, 2026-08-30 — staleness remediation

**Trigger.** Human reviewer flagged that two of the case's cited "real" sources were stale: S1
(Unity's own mobile hardware blog, April 2013 — 13 years old) and S2 (DeviceAtlas regional Mali/
Adreno blog, September 2017 — 9 years old). Instruction: do real, thorough re-research and
re-ground the case's entire data foundation in current (2024-2026) sources, not just patch the
footnotes. This section documents that pass. `case-research`'s original pass (above) is left
untouched as a historical record; this section supersedes S1 and S2 specifically.

### What was searched and found

**Unity's own current Gaming Report (2025 edition).** Searched and located
`unity.com/resources/gaming-report-2025` (published ~March 2025, GDC timing) as the direct
successor to the 2013 blog post the case originally cited. Direct fetch returned HTTP 403 (same
bot-blocking behavior unity.com showed for the 2013 post in the original pass). Search-result
summaries confirm the report covers "five high-level game development trends... backed by 30
interactive data charts" and survey data from "nearly five million Unity engine developers," but
none of the available secondary coverage (gamesmarket.global, unity.com/blog announcement post)
quotes a GPU-vendor or Android-hardware-tier breakdown from it — the 2025 report appears to have
moved on from the kind of raw device-hardware census the 2013 post did. Unity's legacy
`stats.unity3d.com` hardware-stats page (referenced in a search snippet as still being "updated
roughly once a month") no longer resolves (`ENOTFOUND` on direct fetch) — the page is gone.
**Disposition: NOT FOUND** as a direct replacement for S1's specific claim (Android GPU-maker %
breakdown). Unity itself does not appear to still publish this cut of data anywhere reachable.

**Statcounter GPU/device vendor share.** Statcounter (`gs.statcounter.com`) was checked directly;
it publishes mobile *vendor* (brand, e.g. Samsung/Tecno/Apple) and *OS* market share by country,
continuously updated, but does **not** publish a GPU-vendor or chipset breakdown at all — this is
a real, structural gap in what Statcounter tracks, not a research failure. **Disposition: NOT
FOUND** for GPU-specific data; Statcounter's brand-level Nigeria data was used instead as an input
to a chipset-vendor proxy (see S2' below, sourced via a republication that cites Statcounter as
its methodology).

**Google's official Android device/API distribution.** `developer.android.com/about/dashboards`
was fetched directly and is confirmed **live and actively maintained** — its footer states "Last
updated 2025-12-05 UTC," with a data snapshot for "the 7-day period ending on November 24, 2025."
It no longer publishes an API-level breakdown (a real, disclosed gap — Google now directs
developers to Play Console's "Reach and devices" for that cut), but it does publish current
OpenGL ES and Vulkan version distributions across all active Android handheld devices on Google
Play: **OpenGL ES 3.2, 98.24%; ES 3.1, 0.39%; ES 3.0, 0.86%; ES 2.0, 0.49%. Vulkan: none, 7.37%;
1.0.3, 3.86%; 1.1, 62.09%; 1.3, 26.01%; 1.4, 0.67%.** This is a genuinely current, first-party,
continuously-updated dataset. **Disposition: SOURCED (S8, new).** It is global, not
regional/India-Nigeria-specific — that regional gap is disclosed, not papered over.

**Academic/industry research on Android GPU/device fragmentation.** Searched arXiv and Google
Scholar-style queries for GPU/device-fragmentation research in mobile games specifically (per the
human's suggestion to check university/academic sources). Found and fetched
**arXiv:2504.20261, "An Empirical Analysis of Compatibility Issues for Industrial Mobile Games"**
(Song, Chen, Ma, Lu, Lin, Fan, Yang; ISSRE track; arXiv submission 2025-04-28) — a real empirical
study of four commercial mobile games' bug trackers (7M+ lines of code, 20,000+ commits). Direct
fetch of the full HTML confirmed: GPU-related issues account for **21 of 91 (23%)** studied
compatibility issues; the paper splits these into "Insufficient GPU" (11 cases — explicitly tied
to "older and low-configuration devices," causing display/lag failures) and "Incompatible GPU"
(10 cases — shader bugs on specific models regardless of tier). Direct quote: *"Different from
normal Android software, most compatibility issues in mobile games are caused by hardware rather
than software."* **Disposition: SOURCED (S7, new).** This is exactly the kind of current,
independent, peer-reviewed-track evidence the human asked for — it replaces S1's role (establishing
that GPU/hardware-tier mismatches are a real, load-bearing phenomenon in commercial mobile games)
with a 2025 empirical study instead of a 13-year-old vendor blog.

**Current regional chipset/device-vendor share, India and Nigeria.**
- **India:** Counterpoint Research, "India Smartphone Shipments Rise 8% YoY in Q2 2025..."
  (`counterpointresearch.com/en/insights/india-smartphone-market-q2-2025`, published 2025-07-30).
  Direct fetch confirmed: *"MediaTek led India's smartphone chipset market with a 47% share,
  followed by Qualcomm with a 31% share."* (Remaining ~22% is Unisoc/Samsung, not broken out by
  this source.) **Disposition: SOURCED (S1', replaces S2's India row).** Confidence HIGH — primary
  research firm, own website, directly fetched, current quarter.
- **Nigeria:** Intelpoint, "Tecno has the highest share among phone brands in Nigeria at 23.55% as
  of February 2025" (`intelpoint.co/insights/...`), citing Statcounter Global Stats as its
  underlying data source. Direct fetch confirmed: Tecno 23.55%, Infinix 21.73%, Itel 5.41%
  (Transsion Holdings' three brands combined: 50.69%); Samsung 12.36%, Apple 9.43%, Xiaomi 7.15%,
  Huawei 4.34%, Oppo 3.59%, Vivo 1.46%. **Disposition: SOURCED (S2', replaces S2's Nigeria row).**
  Confidence MEDIUM — Statcounter's methodology is web-traffic detection (a proxy for install base,
  not a census, same caveat class as the old S2), and this is a secondary republication of
  Statcounter's data rather than a fetch of Statcounter's own page (Statcounter itself does not
  publish a free, unauthenticated per-country historical vendor-share page in a form this session
  could fetch directly); the specific number is corroborated by the underlying Canalys Africa
  market coverage found in the same search pass, which independently describes Transsion's African
  share as "47-52%," bracketing the 50.69% figure.

**Chipset-to-GPU vendor mapping (needed to turn chipset share into a GPU/device-tier proxy).**
Confirmed via multiple industry sources (AndroidAuthority's MediaTek guide; ARM's own Mali product
pages, which state Mali IP is licensed to MediaTek, Unisoc, and Samsung Exynos SoCs) that MediaTek
and Unisoc chipsets integrate ARM Mali-family GPUs, while Qualcomm chipsets integrate Adreno GPUs.
Specific current budget chips used in the named Nigerian brands were checked directly: the Infinix
Hot 9 Pro (MediaTek Helio P22), Infinix Smart 5 (MediaTek Helio G25), and Itel P65 (Unisoc T615)
all confirmed via public spec-sheet aggregators. **Disposition: SOURCED** (industry-standard
vendor/architecture fact, MEDIUM-HIGH confidence, multiple independent corroborating pages).

### The load-bearing finding: the case's core hardware premise has partly dated out, not just its footnotes

This is the most important thing this pass turned up, and it would have been dishonest to bury it.
The original case's Value-tier definition — "Mali-400-class, capped exactly at 4096×4096" — described
a real GPU, but the Mali-400 MP was **discontinued by ARM in 2015** and has been architecturally
superseded twice over (Bifrost, then Valhall) in the chips that actually ship in India and Nigeria's
budget segment today. The Unisoc T612/T615 and MediaTek Helio-class chips found in current Infinix/
Itel/Tecno and Indian entry-tier devices use **Mali-G52/G57-class GPUs** (2018-2020 architecture),
which support OpenGL ES 3.2 and Vulkan 1.0/1.1 — modern APIs the ancient Mali-400 never supported at
all. Google's own current dashboard data (S8, above) shows **98.24% of all active Android handheld
devices today report OpenGL ES 3.2**, the same tier the budget chips in these two markets carry. No
authoritative current source states an exact `GL_MAX_TEXTURE_SIZE` value for Mali-G52/G57 (ARM's own
product pages do not publish it, and it could not be confirmed by direct fetch in this session — see
"Rejected / not used" below), but the surrounding evidence (modern API tier, modern architecture
generation, universal current-device Vulkan/ES3.2 support) points toward most of these chips clearing
the Crest Atlas's 8192 threshold with real headroom, not failing at it the way a genuine Mali-400
device would. **This is disclosed as a new Modeling Assumption (MA3, case.json/case.md Appendix E)**
rather than silently used to rewrite the case's premise out from under it: the case still uses
chipset-vendor share (MediaTek in India; Transsion-brand devices in Nigeria) as its Value-tier proxy,
because that is the best available *regional, current* data — but it now explicitly discloses that
this proxy likely **overstates** Option A's true 2026 failure rate, in a specific, named direction
(unlike the old MA2, which described undirected uncertainty). This makes Option B's already-favored
recommendation more conservative and defensible, not less — the case's answer does not flip, but the
honesty of how it gets there materially improves.

### Rejected / not used (this pass)

- Unity's `stats.unity3d.com` hardware-stats page — no longer resolves (DNS failure). Not used.
- `unity.com/resources/gaming-report-2025` and its mirrors (`create.unity.com`,
  `activation.unity3d.com`) — all either 403'd or, per available secondary coverage, do not publish
  a GPU-vendor/device-tier cut of data. Not used as a citation.
- ARM's own Mali-G52/Mali-G57 product pages — fetched directly; confirmed they do **not** publish a
  `GL_MAX_TEXTURE_SIZE`/`MAX_TEXTURE_SIZE` figure on the public marketing page (only a "download
  comparison PDF" link, not fetchable in this session). Not used as a numeric citation; the
  architecture-generation/API-tier evidence was used instead, disclosed as inference in MA3, not
  invented as a false-precision number.
- Several `electronics.alibaba.com/buyingguides/...` pages surfaced in search results describing
  Mali-400 and Mali-G52 "buying guides" — these read as SEO/content-farm material (one made an
  unverifiable, oddly specific claim about a "sharp uptick in listings" for Mali-400 educational
  tablets in "regional marketplaces" with no citation of its own). Not used as a source anywhere in
  this case; flagged here so a future pass does not accidentally pick them up.
- Global Q1 2026 AP-SoC vendor share (MediaTek 32%, Qualcomm 23%, Apple 19%, Unisoc 14%,
  Samsung 7% — Counterpoint's "Global Smartphone SoC Model Shipments Tracker," fetched directly)
  was considered as a substitute for India/Nigeria-specific data but rejected in favor of the
  India-specific Q2 2025 figure and the Nigeria-specific Feb 2025 figure, since country-specific
  data is what the case actually needs and both were available.

### Updated summary table (S1, S2 rows superseded; new rows added)

| id | Value | Status | Confidence | Replaces |
|---|---|---|---|---|
| S1' | India chipset share: MediaTek 47%, Qualcomm 31% (Q2 2025) | SOURCED | HIGH | S1 (India row) |
| S2' | Nigeria brand share: Transsion (Tecno+Infinix+Itel) 50.69% (Feb 2025) | SOURCED | MEDIUM | S2 (Nigeria row) |
| S7 | GPU-related issues = 23% of studied mobile-game compatibility bugs (arXiv, Apr 2025) | SOURCED | MEDIUM (normalized 2026-08-31, T1-08: was logged MEDIUM-HIGH, not a valid grade) | S1 (shape-of-claim role) |
| S8 | Android OpenGL ES/Vulkan version distribution, live (snapshot Nov 2025) | SOURCED | HIGH | new context, not a direct replacement |
| S3-S6 | Unchanged — retained as historical/current hardware capability specs, not market-share claims | SOURCED | HIGH/MEDIUM | unchanged |

**NOT FOUND, disclosed honestly:** an exact current `GL_MAX_TEXTURE_SIZE` value for Mali-G52/G57 or
Unisoc T612/T615 (the chips actually dominant in these markets today); an India/Nigeria-specific
OpenGL ES or Vulkan version distribution (Google's dashboard is global-only); and a 2025-or-later
Unity or third-party GPU-vendor-share breakdown comparable to the 2013 post's. All three are named
above rather than papered over with an invented number.

Next step: `case-readiness` (re-run, given the appendix/matrix changes below).
