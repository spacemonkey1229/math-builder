Case Study: The Skin Pack Atlas
MS | Math | Case Study | 2026 | Adventure

## Overview

The fan on Alicia Tran's laptop is loud enough to hear over the Discord call, and nobody has said
anything for eleven seconds. On her second monitor sit two renders of the same character, side by
side, wearing the same new skin. On the left, every scale on the tail is crisp enough to count. On
the right, the same scales blur slightly the moment the camera zooms in — not broken, just softer,
the kind of soft a player notices without being able to say why.

Alicia is the only technical artist at Tanager Games, seven people total, and she is the one who
has to explain — again — why a texture that looks perfect on her own phone can make a stranger's
phone refuse to draw it at all. The community manager shares her screen too: support tickets from
the last skin pack, sorted by country, most of them from India and Nigeria — Tanager's two
fastest-growing markets, where, per current chipset-market data (SEE APPENDIX C), a large share of
new phones still ship with budget-tier silicon rather than the flagship chips Alicia's own test
device runs. "Players are saying their skins are just... gray," she says. "Some are asking for
refunds."

The build for tonight's release is sitting in two branches, one for each atlas, and Alicia has
maybe twenty minutes before she has to pick one and merge it. She pulls up her spreadsheet of
device data instead of picking by feel this time. Somewhere in these two columns of numbers is an
answer that isn't just "which one looks better in a screenshot."

She opens both branches side by side, uncaps a marker for the whiteboard, and starts drawing a
grid.

## Background

Alicia Tran is the sole technical artist at Tanager Games, a seven-person indie studio that makes
*Molt*, a collectible-creature idle RPG (SEE APPENDIX D). *Molt*'s revenue comes almost entirely
from character skin packs, and Alicia is responsible for the technical decision of how each pack's
new art gets packed into the game before it ships — and accountable to the rest of the small team
for making sure this week's pack does not silently break the game for players who already paid for
it. Two packaging options are on the table for tonight's release, and only one can ship:

**The Crest Atlas** — pack the new character art into a single **8192×8192** texture atlas. This
is the sharpest possible version of the new skins, and it is what Alicia's own flagship test
device renders (SEE APPENDIX D).

**The Anchor Atlas** — pack the same art into a single **4096×4096** texture atlas instead. This
requires compressing the source art harder to fit, which visibly softens fine detail like scale
edges and fur, but every device Tanager has ever tested has been able to load a 4096×4096 texture
without failure (SEE APPENDIX D).

The failure mode that matters is not gradual: a mobile GPU either supports a texture at a given
dimension or it does not. If a device's GPU cannot handle a texture at the atlas's dimension, that
texture does not load — the character shows up untextured, or the game refuses to draw that screen
at all. This is a hard pass/fail, tied to a real, published mobile-GPU texture-size capability
ladder (SEE APPENDIX C), not a matter of the art simply looking a little worse on older phones.

Tanager's two fastest-growing markets, by new installs, are India and Nigeria (SEE APPENDIX A).
Both markets skew toward budget-tier Android hardware: in India, MediaTek — whose chips run ARM
Mali-family GPUs rather than Qualcomm's Adreno — is the single largest smartphone chipset vendor,
and in Nigeria more than half of all phones sold are one of three Transsion-made brands (Tecno,
Infinix, Itel) built almost entirely on the same budget MediaTek/Unisoc silicon (SEE APPENDIX C).
A real, current, peer-reviewed-track study of commercial mobile games found that GPU-related
problems — specifically devices too old or low-tier to render what a game asks of them — account
for close to a quarter of all the compatibility bugs those games' own developers had to fix (SEE
APPENDIX C). A metric that only counts *devices* running budget silicon, though, is not the whole
picture: not every install is worth the same to the studio, because heavier-spending players tend
to cluster on newer, higher-tier devices. Tanager's own analytics dashboard reports total monthly
skin-pack revenue by country, but does not break that revenue out by device tier — a real
limitation many small studios operate under. Alicia has to reconstruct that missing breakdown
herself, using India and Nigeria's known device-tier composition and each market's known total
revenue as a system of two linear equations (SEE APPENDICES A AND B), built on top of a small set
of disclosed modeling assumptions and proxies where Tanager's own real business data does not
exist to source (SEE APPENDIX E).

Alicia's recommendation must be judged on one number: **the revenue-weighted percent of Tanager's
active install base that can render the chosen atlas without a texture load failure**, found by
building a 2×2 system of linear equations from Appendices A and C and solving it using matrix
algebra (SEE APPENDICES A, B, C AND D). Every sourced and assumed figure in this case is listed in
**APPENDIX F**, and the vocabulary and "how to…" skills this case will ask of you are listed in
**APPENDIX G** — that is where Challenge 1 sends you.

## Dilemma

You are Alicia Tran.
Do you:
A.) Ship tonight's skin pack packed into an 8192×8192 texture atlas — The Crest Atlas OR
B.) Ship tonight's skin pack packed into a 4096×4096 texture atlas — The Anchor Atlas

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A labeled 2×2 install-base matrix **M** (SEE APPENDIX B): rows are Tanager's two named
    growth markets, columns are the two device tiers, every entry defined in words, with the
    matrix's dimensions stated.
    D2. The identity matrix **I** and the computed inverse matrix **M⁻¹**, with a verification
    step showing the full arithmetic of **M · M⁻¹** entry by entry, confirming it equals **I** —
    not just asserting that it does.
    D3. The determinant of **M**, computed by hand using the 2×2 determinant formula, with a
    one-sentence explanation of why a nonzero determinant is required before **M** can be inverted
    at all.
    D4. The solved revenue-per-active-install vector **r = M⁻¹v** for the reported total-revenue
    vector **v** (SEE APPENDIX A), showing the full matrix arithmetic used to solve the system —
    not just the final numbers.
    D5. A final decision table (SEE APPENDICES C AND D): for the Crest Atlas and the Anchor
    Atlas, the device-count percent of the install base that renders successfully, the
    revenue-weighted percent that renders successfully (using D4's per-tier revenue rates), and
    your recommendation stated and defended using that last column.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — Growth-Market Revenue and Install Data

|  | India | Nigeria |
|---|---|---|
| Tanager's reported active installs, this market, most recent month | 40,000 [MA1] | 20,000 [MA1] |
| Share of this market's installs on a Value-tier GPU (SEE APPENDIX C) | 47% [S1'] | 50.7% [S2'] |
| Share of this market's installs on a Flagship-tier GPU (SEE APPENDIX C) | 53% [S1'] | 49.3% [S2'] |
| Tanager's reported total skin-pack revenue, this market, most recent month (USD) | $19,780 [MA1] | $9,409 [MA1] |

India and Nigeria are Tanager's two fastest-growing markets by new installs this year (SEE
APPENDIX E, MA1). Tanager Games and *Molt* are both fictional; the studio's own install and
revenue figures above are disclosed as stated business assumptions (MA1), built on top of the
real, cited regional chipset-vendor-share figures in Appendix C (SEE APPENDIX E). India's
Value-tier share is MediaTek's current chipset market share (the complement, 53%, is everyone
else — Qualcomm, Unisoc, Samsung); Nigeria's Value-tier share is the combined current market share
of the three Transsion-made brands (Tecno, Infinix, Itel), whose phones run the same budget
MediaTek/Unisoc chipset families (SEE APPENDIX C, MA3).

## Appendix B — The Install-Base Matrix M

Alicia's model treats each of Tanager's two growth markets as a row and each of two device tiers
as a column:

- **Column 1 — Flagship-tier**: GPUs capable of rendering an 8192×8192 texture without failure.
- **Column 2 — Value-tier**: GPUs found in budget-oriented chipsets (MediaTek in India;
  Transsion-brand devices — Tecno, Infinix, Itel — in Nigeria, predominantly MediaTek/Unisoc
  chipsets), used here as the best available current, region-specific proxy for devices at
  meaningful risk of a texture-size failure at 8192×8192 (SEE APPENDIX C, MA3).

$$M = \begin{bmatrix} \text{India, Flagship-tier installs} & \text{India, Value-tier installs} \\ \text{Nigeria, Flagship-tier installs} & \text{Nigeria, Value-tier installs} \end{bmatrix}$$

Each entry equals that market's total reported active installs (Appendix A) multiplied by its
Flagship-tier or Value-tier share (Appendix A, sourced from Appendix C). **M** is a **2×2 matrix**
— 2 rows (markets) by 2 columns (device tiers) — once every entry is filled in. Its exact numeric
entries are:

$$M = \begin{bmatrix} 40{,}000 \times 0.53 & 40{,}000 \times 0.47 \\ 20{,}000 \times 0.493 & 20{,}000 \times 0.507 \end{bmatrix} = \begin{bmatrix} 21{,}200 & 18{,}800 \\ 9{,}860 & 10{,}140 \end{bmatrix}$$

(India, Nigeria installs and shares from Appendix A [MA1, S1', S2']).

## Appendix C — Real GPU Hardware and Texture-Cap Reference Data

This appendix is real, published hardware data, reproduced here so the device-tier split in
Appendices A and B can be checked against it.

| Claim | Value | Source |
|---|---|---|
| Current (2025) smartphone chipset market share, India | MediaTek 47%, Qualcomm 31%, other (Unisoc/Samsung) 22% [S1'] | Counterpoint Research, "India Smartphone Market Q2 2025" |
| Current (2025) smartphone brand market share, Nigeria | Tecno 23.55%, Infinix 21.73%, Itel 5.41% (Transsion combined 50.69%); Samsung 12.36%, Apple 9.43%, Xiaomi 7.15%, Huawei 4.34%, Oppo 3.59%, Vivo 1.46% [S2'] | Statcounter Global Stats, via Intelpoint republication |
| Which GPU family each named chipset vendor's silicon uses | MediaTek and Unisoc chips run ARM Mali-family GPUs; Qualcomm chips run Adreno GPUs [S1', S2', chipset-vendor mapping] | ARM Mali product licensing pages; AndroidAuthority MediaTek chip guide; public device spec sheets (Infinix Hot 9 Pro/Smart 5, Itel P65) |
| Share of studied commercial mobile-game compatibility bugs that are GPU-related, and which device population they concentrate on | 21 of 91 (23%) of studied bugs are GPU-related; "Insufficient GPU" (11 of 91) explicitly tied to older/low-configuration devices [S7] | Song et al., "An Empirical Analysis of Compatibility Issues for Industrial Mobile Games" (arXiv, 2025) |
| Current, live distribution of GPU rendering-API capability across all active Android devices | OpenGL ES 3.2: 98.24%; ES 3.1: 0.39%; ES 3.0: 0.86%; ES 2.0: 0.49%. Vulkan: none 7.37%, 1.0.3 3.86%, 1.1 62.09%, 1.3 26.01%, 1.4 0.67% [S8] | Google, Android Developers "Distribution dashboard" (live, snapshot ending 2025-11-24) |
| Maximum supported 2D texture dimension by mobile GPU generation (historical hardware capability specs — older/budget Mali-400-class and PowerVR SGX generations, modern flagship Android/iOS, top-tier mobile/desktop-class) | 2048 px (older/budget, e.g. PowerVR SGX 535 — iPhone 3GS/iPhone 4/original iPad) [S3]; 4096 px (Mali-400-class, discontinued by ARM in 2015 [S4]; also PowerVR SGX 543 — iPhone 4S/iPad 2+) [S3]; 8192 px (modern flagship, per Unreal Engine's own supported ceiling) [S5]; 16384 px (top-tier, Unity's own engine-wide cap) [S6] | Apple OpenGL ES Hardware Platform Guide; ARM Mali-400 MP specification; Unreal Engine texture documentation; Unity SystemInfo documentation |

## Appendix D — Atlas Packaging Options

|  | Option A — The Crest Atlas | Option B — The Anchor Atlas |
|---|---|---|
| Atlas dimensions | 8192 × 8192 px | 4096 × 4096 px |
| Minimum device GPU generation required to render without a load failure (SEE APPENDIX C) | Flagship-tier (a modern GPU whose maximum texture dimension is ≥ 8192 px) [S3, S5] | Value-tier (budget chipset-family GPU, capped at 4096 px or below in this model, or better) [S3, S4] |
| Can a Value-tier device render this option? | Fails to load, per this model (SEE APPENDICES C, E — MA3 discloses this is likely conservative for current budget silicon) | Loads successfully (SEE APPENDIX C) |
| Visible art quality on a device that can render it | Full detail; the source art's native resolution | Visibly softened; source art compressed harder to fit the smaller atlas |

*Molt* and Tanager Games are both fictional, invented for this case (SEE APPENDIX E).

## Appendix E — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, disclosed here rather than presented as real studio data. A Hero may challenge them in
> discussion — that is a legitimate move.

| # | Assumption | Basis | Sensitivity |
|---|---|---|---|
| MA1 | Tanager Games and *Molt* are fictional; the studio's reported active-install and revenue figures for India and Nigeria (Appendix A) are the case's own invented business figures. | No real seven-person studio matching this description exists to source install or revenue figures from. The invented figures (India: 40,000 installs, $19,780/month revenue; Nigeria: 20,000 installs, $9,409/month revenue) were built so that each market's device-tier composition matches the real, cited current regional chipset-vendor-share data in Appendix C (India 47%/53% Value/Flagship from S1', Nigeria 50.7%/49.3% Value/Flagship from S2'), even though the specific install and revenue totals are not real. | The final revenue-weighted percentage in the Challenge 3 decision table — and therefore which atlas is defensible — is sensitive to these invented install and revenue totals. A different but still device-tier-consistent set of numbers could shift that percentage. A Hero may reasonably challenge these figures and re-run the matrix solve with their own numbers, as long as the device-tier composition still matches Appendix C. |
| MA2 | Chipset-vendor share (MediaTek in India; Transsion-brand devices in Nigeria) is used as a proxy for "Value-tier, capped below 8192×8192," even though not every device from these vendors is actually capped there, and the reverse complement (Qualcomm/Samsung/other) is treated as uniformly Flagship-tier even though it also contains some lower-tier devices. | MediaTek and Unisoc chipsets integrate ARM Mali-family GPUs; Qualcomm chipsets integrate Adreno GPUs (SEE APPENDIX C). Chipset-vendor share is real, current, and region-specific (S1', S2') — a meaningfully better-grounded proxy than a global GPU-brand blog — but it is still a proxy, not a direct device-capability census. | Two compounding, disclosed directions of possible error, same structure as before: (1) some devices in the "Flagship" complement may still be older/lower-tier hardware this proxy doesn't count, and (2) some MediaTek/Transsion-brand devices may run modern silicon well above the 4096 px cap this proxy assumes (see MA3, which argues this second error is now the dominant one). |
| MA3 | The Value-tier's assumed hard cap at 4096×4096 was set by the Mali-400 GPU, which ARM discontinued in 2015. The budget chipsets that actually dominate India and Nigeria's device-tier proxy today (Unisoc T612/T615, MediaTek Helio-class) use newer Mali-G52/G57-class GPUs supporting OpenGL ES 3.2 and Vulkan — APIs the Mali-400 never supported at all. | Public spec sheets confirm the Infinix Hot 9 Pro, Infinix Smart 5, and Itel P65 (three of Nigeria's best-selling models) run MediaTek Helio or Unisoc T-series chips with Mali-G52/G57-class GPUs, not Mali-400. Google's own live Android distribution data shows 98.24% of all active Android handheld devices today report OpenGL ES 3.2 (SEE APPENDIX C, S8) — the tier these budget chips carry, not the Mali-400's tier. No current source in this research pass could confirm an exact `GL_MAX_TEXTURE_SIZE` value for Mali-G52/G57, so this is disclosed as a reasoned inference, not an invented number. | This pushes in one specific, named direction (unlike MA2's two-sided uncertainty): it means the model's Value-tier failure assumption is very likely **conservative** — Option A's true 2026 failure rate among "Value-tier"-proxy devices is probably smaller than this case models, not larger. That makes Option B's already-favored recommendation more conservative, not less; it does not flip the case's answer, and a Hero who raises this point should be credited for catching a real, current limitation of the model, not treated as having broken it. |

## Appendix F — Sources

| id | Claim | Value | Source | Accessed | Confidence |
|---|---|---|---|---|---|
| S1' | Current (Q2 2025) smartphone chipset market share, India | MediaTek 47%, Qualcomm 31%, remainder ~22% (Unisoc/Samsung, not broken out by this source) | Counterpoint Research — ["India Smartphone Shipments Rise 8% YoY in Q2 2025..."](https://counterpointresearch.com/en/insights/india-smartphone-market-q2-2025) | 2026-08-30 | HIGH |
| S2' | Current (Feb 2025) smartphone brand market share, Nigeria | Tecno 23.55%, Infinix 21.73%, Itel 5.41% (Transsion combined 50.69%); Samsung 12.36%, Apple 9.43%, Xiaomi 7.15%, Huawei 4.34%, Oppo 3.59%, Vivo 1.46% | Statcounter Global Stats, via [Intelpoint republication](https://intelpoint.co/insights/tecno-has-the-highest-share-among-phone-brands-in-nigeria-at-23-55-as-of-february-2025/) | 2026-08-30 | MEDIUM |
| S3 | Maximum 2D texture dimension by iOS GPU generation | 2048×2048 (PowerVR SGX 535 — iPhone 3GS/4, original iPad); 4096×4096 (PowerVR SGX 543 — iPhone 4S/5, iPad 2/3) | Apple — [OpenGL ES Hardware Platform Guide for iOS (archived)](https://developer.apple.com/library/archive/documentation/OpenGLES/Conceptual/OpenGLESHardwarePlatformGuide_iOS/OpenGLESPlatforms/OpenGLESPlatforms.html), Table 1-2 | 2026-08-30 | HIGH |
| S4 | Maximum 2D texture dimension, ARM Mali-400 MP | 4096 px along any axis (Technical Reference Manual §3.13.5); Mali-400 MP discontinued by ARM in 2015 | ARM — ["What is the maximum framebuffer and texture resolution supported by Mali-400 MP?"](http://infocenter.arm.com/help/topic/com.arm.doc.faqs/ka13314.html) | 2026-08-30 | MEDIUM |
| S5 | Maximum supported texture resolution in Unreal Engine | 8192×8192 | Epic Games — [Texture Format Support and Settings in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-format-support-and-settings-in-unreal-engine) | 2026-08-30 | HIGH |
| S6 | Maximum supported texture size in Unity | 16384 px (Unity's own engine-wide cap, regardless of what the GPU itself reports) | Unity Technologies — [SystemInfo.maxTextureSize documentation](https://docs.unity3d.com/ScriptReference/SystemInfo-maxTextureSize.html) | 2026-08-30 | HIGH |
| S7 | Share of studied commercial mobile-game compatibility bugs that are GPU-related, and the device population they concentrate on | 21 of 91 (23%) of studied bugs are GPU-related; "Insufficient GPU" (11 of 91) explicitly tied to older/low-configuration devices; "most compatibility issues in mobile games are caused by hardware rather than software" (verbatim) | Song, Chen, Ma, Lu, Lin, Fan, Yang — ["An Empirical Analysis of Compatibility Issues for Industrial Mobile Games"](https://arxiv.org/abs/2504.20261), arXiv, submitted 2025-04-28 (ISSRE track) | 2026-08-30 | MEDIUM |
| S8 | Current, live distribution of GPU rendering-API capability across all active Android handheld devices | OpenGL ES: 3.2 (98.24%), 3.1 (0.39%), 3.0 (0.86%), 2.0 (0.49%). Vulkan: none (7.37%), 1.0.3 (3.86%), 1.1 (62.09%), 1.3 (26.01%), 1.4 (0.67%) | Google — [Android Developers, "Distribution dashboard"](https://developer.android.com/about/dashboards), snapshot ending 2025-11-24, last updated 2025-12-05 | 2026-08-30 | HIGH |

**Notes on confidence and staleness.** This case originally cited a 2013 Unity blog post and a
2017 DeviceAtlas blog post for its GPU-vendor-share figures; both were flagged as stale in review
and have been superseded here by S1', S2', S7, and S8 (SEE `RESEARCH_LOG.md` for the full
remediation trail, including what was searched and rejected). S2' is a secondary republication of
Statcounter's own data (Statcounter does not publish a free, directly fetchable historical
per-country vendor-share page); its web-traffic-detection methodology carries the same
proxy-not-census caveat the original S2 disclosed, now on 2025 rather than 2017 data. S4 could not
be independently re-verified by direct fetch in this session (a TLS certificate mismatch on ARM's
CDN); it is retained only as corroboration for the already-HIGH-confidence Apple SGX 543 figure
(S3), which covers the same GPU generation and reports the identical 4096 px cap — and, per S4's
own updated note, that generation (and the Mali-400 specifically) has been out of production since
2015 (SEE APPENDIX E, MA3, for what that means for this model's Value-tier assumption).

## Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Matrix
- Matrix Dimension
- Determinant
- Identity Matrix

**"How to…" questions**

- How to add and multiply matrices
- How to find the determinant of a 2x2 matrix
- How to solve a system of equations using a matrix
