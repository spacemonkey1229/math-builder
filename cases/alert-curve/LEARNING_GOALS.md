# Learning Goals — The Alert Curve

Bidirectional deliverable ↔ skill matrix. `case-write`, 2026-08-24.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — chain-rule derivation of dS/dt | `calculus-how-to-use-the-chain-rule-to-differentiate-a-composite-function` |
| D2 — product-rule derivation of dA/dt (uses D1) | `calculus-how-to-use-the-product-rule-to-differentiate-a-product-of-functions` |
| D3 — differentiability justification (raw count vs. continuous model) | `calculus-differentiable` |
| D4 — tangent line at t0 and its next-interval prediction | `calculus-tangent-line` |
| D5 — confirmed-incidents-per-false-escalation ratio and margin | `calculus-tangent-line` (reinforced) |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 4    new_coverage: 2
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Forcing test applied to each claimed skill** (*could a competent Hero produce the deliverable
correctly without ever performing this skill?*):

- `calculus-how-to-use-the-chain-rule-to-differentiate-a-composite-function` (new_coverage) — D1
  explicitly requires identifying S(t) = f(g(t))'s outer function f(x) = c·√x and inner function
  g(t) = k·t + m separately, then combining f'(g(t))·g'(t). There is no route to a correct dS/dt
  without performing the chain rule — S(t) is not a simple polynomial a student could differentiate
  by the power rule alone.
- `calculus-how-to-use-the-product-rule-to-differentiate-a-product-of-functions` (new_coverage) —
  D2 requires differentiating A(t) = V(t)·S(t), a genuine product of two non-constant functions of
  t. Differentiating V and S separately and simply multiplying the two derivatives together (the
  common wrong shortcut) produces a different, incorrect expression — only the product rule
  (V'·S + V·S') gives the correct dA/dt, which D5's escalation classification then depends on.
- `calculus-differentiable` (already covered, n=2) — D3 requires an explanation grounded in the
  actual definition of differentiability: why a step function (the raw alert count) has no
  instantaneous rate of change at its jump points, and why a product/composition of functions that
  are each differentiable everywhere (V and S) is itself differentiable everywhere. A student who
  does not know what differentiable means cannot produce this argument — restating "the count goes
  up in steps" without connecting it to the definition does not satisfy D3.
- `calculus-tangent-line` (already covered, n=2) — D4 requires the actual equation of a line
  through (t0, A(t0)) with slope dA/dt from D2 — not just stating the slope's value. D5 then
  requires applying the *sign* of that same slope, interval by interval, to classify each row of
  Appendix D's historical log under the Curve Check policy; a student cannot produce D5's ratio
  correctly without having built a real tangent line (or at minimum its slope) for each classified
  interval.

No skill here is claimed on the strength of "the case is about calculus generally" — each one
traces to a specific verb in a specific deliverable, using the exact operation (differentiate a
composite vs. differentiate a product vs. justify differentiability vs. build and apply a tangent
line) each spine skill actually names. No quotient-rule claim is made: A(t) is built as a single
product of two functions (Appendix A), not a quotient, so only the chain rule and product rule are
forced — a second, unrelated composite function was deliberately not introduced just to also claim
the quotient-rule how-to (per the approved concept).
