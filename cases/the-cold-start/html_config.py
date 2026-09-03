CONFIG = {
    "strand_summary": "Matrices &middot; Sparsity",
    "protagonist": "Priya Nakamura",
    "option_a_label": "The Popularity Path",
    "option_a_text": "Show every new user the same platform-wide popularity ranking immediately -- zero cold-start dropout, but no personalization.",
    "option_b_label": "The Ratings Gate",
    "option_b_text": "Require rating 10+ titles before showing personalized recommendations -- real dropout during the gate, but a real personalization lift once through it.",
    "challenge3_summary": "Include: <strong>D1</strong> the item-similarity and completer matrices' sparsity; <strong>D2</strong> Option A's identity-matrix framing; <strong>D3</strong> Option B's completers-only click-through rate; <strong>D4</strong> both options' clicks per 100 users exposed (the platform's own mandated per-100-starters metric, not per-100-completers); <strong>D5</strong> a recommendation memo.",
    "deliverables": [
        ["D1", "Item-similarity/completer matrix sparsity"],
        ["D2", "Option A's identity-matrix framing"],
        ["D3", "Option B's completers-only click-through rate"],
        ["D4", "Clicks per 100 users exposed, both options"],
        ["D5", "Recommendation memo"],
    ],
    "notebook_steps_html": """
  <div class="stepbox">
    <h4>Step 1 &mdash; Option B: completers and their clicks (D3)</h4>
    <div class="goal">Out of a cohort of 100 users who START the Ratings Gate, Appendix C's modeled dropout rate says some fraction never finish rating 10+ titles. Compute how many COMPLETE the gate, then apply the completers-only click-through rate (Appendix C) to get clicks among completers.</div>
    <div class="fieldrow"><label for="s1completers">Completers, out of 100 starters</label><input type="number" id="s1completers" step="0.1"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1clicksb">Clicks among completers</label><input type="number" id="s1clicksb" step="0.1"><span id="fb1b" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; The mandated metric: clicks per 100 STARTERS (D4)</h4>
    <div class="goal">Northline's analytics team mandated scoring both options per 100 users who START the funnel, not per 100 who complete it (case.md, Background). Compute Option A's clicks per 100 starters directly (Appendix B's click-through rate applies to everyone, no dropout). Then re-express Option B's Step-1 completer clicks as a rate per 100 <em>starters</em> &mdash; not per 100 completers.</div>
    <div class="fieldrow"><label for="s2clicksA">Option A clicks per 100 starters</label><input type="number" id="s2clicksA" step="0.1"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2clicksB">Option B clicks per 100 starters</label><input type="number" id="s2clicksB" step="0.1"><span id="fb2b" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
    <p class="side-note">Compare this to your Step 1 completer-only number for Option B. They are not the same claim &mdash; that difference is exactly the trap this case is built around.</p>
  </div>
""",
    "twist_narrative_html": """
      <p>One more real number, from the same 2002 MovieLens paper Appendix C's dropout model is anchored to (Appendix D, S2): the real, measured live-experiment dropout on that exact "rate 10+ before recommendations" gate was 13.96% &mdash; not the case's modeled 40%.</p>
      <p>Recompute Step 1/2 for Option B using 13.96% instead of 40% for the dropout rate. Does Option A still look better? Was the 40% figure a fair, honest scenario choice, or did it quietly stack the deck? (Both readings are defensible -- MovieLens's 2002 users were self-selected researchers, not a general 2026 mobile cohort arriving from a friend's text.)</p>
""",
    "twist_apply_label": "Recompute Step 1/2 using the real 2002 MovieLens dropout rate (13.96%) instead of 40%",
    "js_data_block": """
const PARAMS = { ctr_a: 0.20, dropout_b: 0.40, ctr_b_completer: 0.35, cohort: 100.0 };
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  const clicksA = p.cohort * p.ctr_a;
  const completersB = p.cohort * (1 - p.dropout_b);
  const clicksB = completersB * p.ctr_b_completer;
  return {A: clicksA, B: clicksB};
}
function evaluate_twist(params){
  return evaluate(Object.assign({dropout_b: 49.0/351.0}, params||{}));
}
""",
    "notebook_check_functions": """
function checkStep1(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS, {dropout_b: 49.0/351.0}) : PARAMS;
  const trueCompleters = p.cohort * (1 - p.dropout_b);
  const trueClicksB = trueCompleters * p.ctr_b_completer;
  fb('fb1a', near(parseFloat(val('s1completers')), trueCompleters, 0.5));
  fb('fb1b', near(parseFloat(val('s1clicksb')), trueClicksB, 0.3));
}
function checkStep2(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS, {dropout_b: 49.0/351.0}) : PARAMS;
  const r = evaluate(p);
  fb('fb2a', near(parseFloat(val('s2clicksA')), r.A, 0.3));
  fb('fb2b', near(parseFloat(val('s2clicksB')), r.B, 0.3));
}
""",
    "glossary_js": """{
  "Matrix": {def: "A rectangular array of numbers arranged in rows and columns.",
    url: "https://www.mathsisfun.com/algebra/matrix-introduction.html"},
  "Matrix Dimension": {def: "The size of a matrix, written rows x columns.",
    url: "https://www.mathsisfun.com/algebra/matrix-introduction.html"},
  "Determinant": {def: "A single number computed from a square matrix that reveals key properties like whether it has an inverse.",
    url: "https://www.mathsisfun.com/algebra/matrix-determinant.html"},
  "Identity Matrix": {def: "A square matrix with 1s on the main diagonal and 0s everywhere else -- multiplying by it changes nothing.",
    url: "https://www.mathsisfun.com/algebra/matrix-types.html"},
  "Percent": {def: "A ratio that compares a number to 100 -- literally \\"per hundred.\\"",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Ratio": {def: "A way of comparing two quantities by division, written a:b or a/b.",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Probability": {def: "A number between 0 and 1 describing how likely an event is to happen.",
    url: "https://www.khanacademy.org/math/statistics-probability/probability-library"},
  "Data": {def: "Facts or numbers collected for reference or analysis.",
    url: "https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-data-statistics"}
}""",
    "howto_js": """[
  ["how to add and multiply matrices", "Matrix"],
  ["how to find the determinant of a 2x2 matrix", "Determinant"],
  ["how to solve a system of equations using a matrix", "Matrix"]
]""",
    "on_twist_toggle_js": """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
}
""",
}
