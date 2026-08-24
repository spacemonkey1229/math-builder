# FACILITATOR.md — The Alert Curve

**Facilitator-only. Do not distribute to students.** Balance argument, margin, and the trap live
here and in `case.json`'s `balance` object — never in `case.md`.

## Argument for A — The Threshold Trip

The raw hourly alert count crossing the threshold is available immediately, with zero additional
delay. For any interval where a true accelerating attack does trip the threshold, the Threshold
Trip policy escalates it exactly one sampling interval sooner than the Curve Check policy ever
could, since Curve Check requires waiting for that next interval before its derivative
confirmation even exists. Every real incident Curve Check would eventually confirm, Threshold Trip
already caught earlier — the only open question is how many additional, non-incident alerts also
crossed the threshold alongside those real ones.

## Argument for B — The Curve Check

Because A(t) is a product of traffic volume and threat score, a pure volume spike with a flat or
falling threat score can push the raw count over the threshold without dA/dt ever turning
positive. Curve Check's chain-and-product-rule confirmation filters exactly that case out, so
every interval it does escalate carries a real, computed acceleration signal that Threshold Trip's
raw count alone cannot distinguish from noise. If a large share of Threshold Trip's threshold
crossings turn out to come from volume-only spikes, Curve Check's confirmed-incidents-per-false-
escalation ratio beats Threshold Trip's by a wide margin — even after accounting for every real
incident Curve Check catches one sampling interval late.

## Margin

`margin_basis` (see `case.json.balance.margin_basis`): compare confirmed real incidents per false
escalation for the Threshold Trip policy versus the Curve Check policy, both computed from
Appendix D's historical interval log (classified under each policy's own rule — Appendix C's
threshold for Threshold Trip, the sign of dA/dt at confirmation for Curve Check), once Appendix A's
function coefficients and Appendix C's threshold and sampling-interval figures are sourced or
accepted as Modeling Assumptions. `margin_pct` is `null` until then — this case is designed so
Threshold Trip's speed advantage and Curve Check's precision advantage pull against each other on
the same ratio; the actual margin is not yet known and must not be guessed at write time.

## Five Socratic questions

1. Your D2 gives you dA/dt at t0 as a single signed number — what does its sign alone tell you
   that the raw alert count at t0 by itself cannot?
2. Suppose two different intervals both cross the threshold in Appendix D — one where traffic
   volume is spiking and threat score is flat, another where both are rising together. Does your
   D2 derivative treat those two intervals the same way, and should it?
3. Your D5 ratio for the Curve Check policy has no entry for an interval where a real attack got
   exactly one sampling interval longer to run before anyone was paged — how do you weigh that
   cost against the false escalations Threshold Trip is racking up in the same log?
4. If Appendix C's sampling interval were cut in half, what happens to Curve Check's disadvantage
   of "waiting one more interval" — and does that change which policy your D5 ratio favors?
5. D3 argues the raw alert count itself isn't truly differentiable. If Jordan tried to eyeball "is
   this accelerating" straight off the raw count, without ever building the continuous model A(t),
   what mistake would D3's own argument predict he'd make?

## The trap

A Hero notices that the Threshold Trip policy always catches every real incident at least as early
as the Curve Check policy — since Curve Check can't even evaluate a derivative until it waits a
full sampling interval — and concludes Threshold Trip must therefore also have the better
confirmed-incidents-per-false-escalation ratio, because "catching it sooner is strictly better."
This conflates *speed* with *precision*. The primary metric counts every alert a policy raises, not
just the real ones it catches, and a policy that reacts to any volume spike crossing the threshold
racks up false escalations exactly where the threat score never actually moved. A Hero who never
sorts Appendix D's log by whether dA/dt was genuinely positive at the moment of escalation will
overstate Threshold Trip's real advantage — and miss the whole reason Appendix A built A(t) as a
product in the first place.

## Sensitivity note

Financial-services SOC framing — keep the discussion strictly on the escalation-policy decision
itself. Never let it drift into treating this as a real breach, a named institution, or an actual
security incident; the stakes are a training/operations decision about *when to escalate*, not a
depiction of a real compromise. Routine register, comparable to this project's Key Length case — no
illness, death, or financial hardship to a person is involved, so SPEC §6's stronger sensitivity
handling does not otherwise apply here.
