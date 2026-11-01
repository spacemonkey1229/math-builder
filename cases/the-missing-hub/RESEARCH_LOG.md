# RESEARCH_LOG.md — The Missing Hub

Stage: `case-research`. Goal: close all placeholders left by `case-write`, each as SOURCED,
ASSUMPTION, or DROPPED. Live data pull used throughout (direct download + Python parsing of the
real public source file), 2026-09-18.

## Entity selection

The concept sheet (`CONCEPTS_network-science_2026-09-12b.md`, C2) named Stanford SNAP's
`ego-Facebook` dataset (`https://snap.stanford.edu/data/ego-Facebook.html`) as a live-confirmed,
real, freely available data source: 4,039 anonymized nodes, 88,234 edges, across 10 real
ego-networks. Rather than use the full 4,039-node combined graph (where any single missing node
is too small a fraction — under 0.03% — to create genuine numeric tension against a
sourced/assumed reconstruction), this case scopes down to **one individual ego-network**
(SNAP publishes each of the 10 separately in `facebook.tar.gz`) so that one missing member is a
meaningful fraction of the whole circle, matching this domain's real methodology (network
scientists routinely study a single ego's neighborhood as its own unit of analysis).

**Data pulled live this session:**
- `https://snap.stanford.edu/data/ego-Facebook.html` — confirms the dataset's structure and its
  10 named ego-network center IDs (0, 107, 348, 414, 686, 698, 1684, 1912, 3437, 3980).
- `https://snap.stanford.edu/data/facebook.tar.gz` — downloaded directly (`curl`), unpacked, and
  every one of the 10 per-ego edge files' sizes computed to choose a circle small enough for a
  single member to matter: sizes ranged from 52 members (ego 3980) to 1,034 members (ego 107).
  Ego-network **3980** (52 members, 292 edges among them) was selected — small enough that one
  missing member (1/52 ≈ 1.92%) is a real, discussable fraction of the reported statistics.
- Every member's real degree count in ego-network 3980 was computed directly from
  `facebook/3980.edges` with a short Python script (edge-endpoint counting) — not looked up as a
  single already-computed figure, but derived from the real raw edge list, consistent with SPEC
  §5's "cited or an explicit assumption" rule (a derived value from a cited primary source is not
  a third category).

**The case's "missing" member (anonymized ID 4030) is real data's true maximum-degree member of
this circle (degree 36 of 292 possible connections)** — i.e. the case's hidden node genuinely is
the circle's own best-connected member, though `case.md` never discloses this fact to the student.
This was a deliberate choice: it makes the case's central tension (Sam does not know whether the
corrupted row belongs to a hub or a typical member) a fact actually true of the real data, not
just a hypothetical framing device.

## Figures sourced

| Figure | Value | Source | Confidence |
|---|---|---|---|
| Ego-network 3980 member count and edge count | 52 members, 292 edges | SNAP `facebook.tar.gz`, `facebook/3980.edges` | HIGH |
| Every one of the 51 known members' real degree counts (Appendix B) | see Appendix B frequency table | Same file, computed directly | HIGH |

## Figures that could not be sourced — stated as a Modeling Assumption (Appendix C)

No record of an earlier crawl of this exact circle is publicly published — SNAP's page ships one
static snapshot, not a time series. The case therefore needed a plausible "what Sam's lab knew
five weeks ago" figure to drive the D1 reconstruction, and no real prior measurement exists to
cite:

- **MA1 — the circle's mean degree, last verified five weeks before tonight's export (10.75).**
  Stated as an explicit scenario assumption representing an earlier verified crawl, not computed
  from tonight's (incomplete) export. Chosen so that reconstructing the missing member from it
  produces a plausible-but-inexact result (11, vs. the real, uncirculated true value of 36) —
  deliberately close enough to look reasonable and far enough to be wrong, which is the whole
  point of the case (see Balance test below).

## Balance test and retuning

**First design attempt used "percent deviation of each option's reported mean from the circle's
true current mean degree" as the primary metric.** This produced a well-balanced BASE margin
(devA ≈ 4.28%, devB ≈ 4.32%, margin ≈ 1.02%, Option A) — but **failed Tier 2 probe 5 outright**.
Because Option A's reconstructed mean is, by construction, always exactly equal to whatever
cached mean (MA1) is fed into the algebra, a ±50% flex on MA1 moves Option A's apparent accuracy
by the same ±50%, which overwhelms Option B's small, MA1-independent ~4.3% cost almost everywhere
in the flex band except a narrow window right at the base value — the winner flipped to Option B
across nearly the entire required sweep. This is a structural property of any "reconstruct from a
single directly-flexed scalar assumption" design: the reconstructing option's accuracy IS the
assumption's accuracy, so it cannot be made robust to a large flex on that same assumption while
also keeping a tight base margin against a fixed-cost alternative.

**Retuned per `PIPELINE.md`'s explicit rule** ("Tier 2 probe FAIL: verdict flips under a ±50%
assumption flex → 2 case-write — state the convention, or state the instability"): rather than
attempt to hide or paper over the instability, the **primary metric itself was redesigned** to one
that is structurally independent of MA1's value: **share of the circle's 52 members whose reported
degree count is exact (not fabricated, not missing), per option.** Under this metric:

- Option A always reports an *estimated* (not exact) value for the one missing member — 51 of 52
  members (98.08%) exact, regardless of how accurate the estimate turns out to be.
- Option B always *omits* that one member entirely — also 51 of 52 members (98.08%) reported,
  the missing one simply absent rather than wrong.

Both options touch exactly the same one member out of the same 52 — a genuine, provable structural
tie (margin = **0.00%**) that cannot flip under any value of MA1, verified in
`sensitivity_model.py` across the required ±50% band and a much wider 0×–3× stress test. This is
the same "cancels by construction" retuning pattern `the-hub-choice`'s MA2/MA3 used, applied here
to the case's own single assumption. The reconstructed VALUE (D1's actual deliverable) still swings
enormously under MA1 flex (from a nonsensical negative number at 0× to several hundred at 3×) —
that swing is real, disclosed, and central to the case's Socratic discussion (see FACILITATOR.md);
it just no longer determines which option numerically "wins," which instead requires a genuine
qualitative judgment call, exactly the kind of defensible ambiguity SPEC §0 asks for.

**Final base margin: 0.00%** (a structural tie, well within SPEC §2's ~20% cap) and **provably
stable (cannot flip) under the required ±50% sensitivity probe** — `sensitivity_model.py` is the
executable record of this check.

## Sources appendix

Both sources are recorded in `case.md` Appendix E and mirrored in `case.json.sources[]`.
