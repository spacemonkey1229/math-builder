CONFIG = {
    "strand_summary": "Graph Theory &middot; Vertices &amp; Edges &middot; Weighted Paths",
    "protagonist": "Priya Nair",
    "option_a_label": "The Card Bridge",
    "option_a_text": "Keep every reorder-agent transaction on the existing card-network settlement path (Issuing Bank &rarr; Card Network Hub &rarr; Acquiring Processor &rarr; Merchant Bank Account).",
    "option_b_label": "The Coin Rail",
    "option_b_text": "Migrate every reorder-agent transaction to the stablecoin settlement path (Agent Wallet &rarr; Stablecoin Ledger &rarr; Custodian &rarr; Merchant Bank Account).",
    "challenge3_summary": "Include: <strong>D1</strong> a labeled drawing of the settlement network as a weighted graph; <strong>D2</strong> the shortest path and whether the graph has an Euler path/circuit; <strong>D3</strong> each rail's total fee percentage and flat cost per $1,000 processed; <strong>D4</strong> each rail's expected fraud/dispute loss; <strong>D5</strong> the net-revenue-retained comparison and recommendation.",
    "deliverables": [
        ["D1", "Settlement network as a weighted graph"],
        ["D2", "Shortest path; Euler path/circuit determination"],
        ["D3", "Fee percentage and flat cost per $1,000, each rail"],
        ["D4", "Expected fraud/dispute loss, each rail"],
        ["D5", "Net revenue retained comparison and recommendation"],
    ],
    "notebook_steps_html": """
  <div class="stepbox">
    <h4>Step 1 &mdash; Total fee and expected-loss percentage per rail (D3&ndash;D4)</h4>
    <div class="goal">Using Appendix B/C's fee tables and Appendix D's fraud-incidence assumption, compute each rail's total fee percentage (interchange + assessment for the Card Bridge; the off-ramp fee for the Coin Rail) and its expected fraud/dispute-loss percentage (fraud probability &times; the rail's own loss share &mdash; 20% recoverable for the Card Bridge, 100% unrecoverable for the Coin Rail).</div>
    <div class="fieldrow"><label for="s1feeA">Card Bridge: total fee percentage</label><input type="number" id="s1feeA" step="0.0001"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1lossA">Card Bridge: expected loss percentage</label><input type="number" id="s1lossA" step="0.0001"><span id="fb1b" class="fb"></span></div>
    <div class="fieldrow"><label for="s1feeB">Coin Rail: total fee percentage</label><input type="number" id="s1feeB" step="0.0001"><span id="fb1c" class="fb"></span></div>
    <div class="fieldrow"><label for="s1lossB">Coin Rail: expected loss percentage</label><input type="number" id="s1lossB" step="0.0001"><span id="fb1d" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; Net revenue retained per $1,000 processed (D5)</h4>
    <div class="goal">Using Appendix D's average transaction value, find each rail's per-transaction flat-cost drag, then combine with Step 1's percentages to find net revenue retained per $1,000 processed for each option, and the percent margin between them.</div>
    <div class="fieldrow"><label for="s2netA">Card Bridge: net revenue retained per $1,000</label><input type="number" id="s2netA" step="0.01"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2netB">Coin Rail: net revenue retained per $1,000</label><input type="number" id="s2netB" step="0.01"><span id="fb2b" class="fb"></span></div>
    <div class="fieldrow"><label for="s2margin">Margin between the two rails (percent)</label><input type="number" id="s2margin" step="0.1"><span id="fb2c" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
  </div>
""",
    "twist_narrative_html": """
      <p>A board member asks the question everyone in the room is thinking: "the Coin Rail's fee is obviously smaller &mdash; why are we even discussing this?" Priya's answer depends on one number nobody has directly measured: the fraud/dispute incidence rate for AI-agent-initiated purchases (Appendix D). Toggle the switch below to see what happens if that assumed rate is 50% higher than Priya's estimate.</p>
""",
    "twist_apply_label": "Recompute at a 50% higher fraud/dispute-incidence rate (0.0135 instead of 0.0090)",
    "js_data_block": """
const PARAMS = {
  interchange_pct: 0.0189, assessment_pct: 0.0014, card_flat_fee: 0.10,
  loss_share_a: 0.20,
  coin_flat_fee: 0.01, offramp_pct: 0.0005,
  avg_txn_value: 1.30,
  fraud_prob: 0.0090,
};
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  const txnCount = 1000.0 / p.avg_txn_value;
  const feeA = p.interchange_pct + p.assessment_pct;
  const flatA = txnCount * p.card_flat_fee;
  const lossA = p.fraud_prob * p.loss_share_a;
  const netA = 1000.0 * (1.0 - feeA - lossA) - flatA;
  const feeB = p.offramp_pct;
  const flatB = txnCount * p.coin_flat_fee;
  const lossB = p.fraud_prob * 1.0;
  const netB = 1000.0 * (1.0 - feeB - lossB) - flatB;
  return {A: netA, B: netB, feeA, lossA, feeB, lossB};
}
function evaluate_twist(params){
  return evaluate(Object.assign({fraud_prob: 0.0135}, params||{}));
}
""",
    "notebook_check_functions": """
function checkStep1(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS, {fraud_prob: 0.0135}) : PARAMS;
  const r = evaluate(p);
  fb('fb1a', near(parseFloat(val('s1feeA')), r.feeA, 0.0005));
  fb('fb1b', near(parseFloat(val('s1lossA')), r.lossA, 0.0005));
  fb('fb1c', near(parseFloat(val('s1feeB')), r.feeB, 0.0005));
  fb('fb1d', near(parseFloat(val('s1lossB')), r.lossB, 0.0005));
}
function checkStep2(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS, {fraud_prob: 0.0135}) : PARAMS;
  const r = evaluate(p);
  const lo = Math.min(r.A, r.B), hi = Math.max(r.A, r.B);
  const margin = lo ? 100.0*(hi-lo)/lo : 0;
  fb('fb2a', near(parseFloat(val('s2netA')), r.A, 0.5));
  fb('fb2b', near(parseFloat(val('s2netB')), r.B, 0.5));
  fb('fb2c', near(parseFloat(val('s2margin')), margin, 0.3));
}
""",
    "glossary_js": """{
  "Graph": {def: "A structure of vertices (points) connected by edges (lines) -- used here to model the settlement network's institutions and the connections between them.",
    url: "https://www.mathsisfun.com/sets/graph-theory.html"},
  "Vertex": {def: "A point in a graph, usually representing an object or place (here, an institution in the settlement network).",
    url: "https://www.mathsisfun.com/sets/graph-theory.html"},
  "Edge": {def: "A connection between two vertices in a graph.",
    url: "https://www.mathsisfun.com/sets/graph-theory.html"},
  "Path": {def: "A sequence of edges connecting a start vertex to an end vertex without repeating a vertex.",
    url: "https://www.mathsisfun.com/sets/graph-theory.html"},
  "Cycle": {def: "A path that starts and ends at the same vertex without repeating any other vertex.",
    url: "https://www.mathsisfun.com/sets/graph-theory.html"},
  "Weighted Graph": {def: "A graph where each edge carries a number (a weight), such as a cost or a fee, rather than just a connection.",
    url: "https://www.mathsisfun.com/sets/graph-theory.html"}
}""",
    "howto_js": """[
  ["how to find the shortest path between two vertices in a weighted graph", "Weighted Graph"],
  ["how to determine whether a graph has an Euler path or circuit", "Graph"]
]""",
    "on_twist_toggle_js": """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
}
""",
}
