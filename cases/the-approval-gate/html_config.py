CONFIG = {
    "strand_summary": "Formal Logic &middot; Truth Tables &middot; De Morgan's Laws",
    "protagonist": "Priya Nandakumar",
    "option_a_label": "The Compound Gate",
    "option_a_text": "Escalate whenever any one of the three safety conditions fails (&not;p &or; &not;q &or; r) -- the correct De Morgan negation of Compliance's approve rule.",
    "option_b_label": "The Streamlined Gate",
    "option_b_text": "Escalate only when all three unsafe conditions hold at once (&not;p &and; &not;q &and; r) -- the VP's proposed rewrite.",
    "challenge3_summary": "Include: <strong>D1</strong> the correct De Morgan negation and a full truth table for both rules; <strong>D2</strong> the rows where A and B disagree; <strong>D3</strong> each option's monthly escalation count; <strong>D4</strong> each option's expected false-approval loss cost; <strong>D5</strong> the total-cost comparison and recommendation.",
    "deliverables": [
        ["D1", "De Morgan negation and full truth table, both rules"],
        ["D2", "Rows where A and B disagree"],
        ["D3", "Monthly escalation count, each option"],
        ["D4", "Expected false-approval loss cost, each option"],
        ["D5", "Total monthly cost comparison and recommendation"],
    ],
    "notebook_steps_html": """
  <div class="stepbox">
    <h4>Step 1 &mdash; Monthly escalation count and cost (D3)</h4>
    <div class="goal">Using Appendix C's 8-row request-volume table, find how many requests each option escalates to a human reviewer per month (Option A escalates every row except p=T,q=T,r=F; Option B escalates only p=F,q=F,r=T), then multiply by Appendix D's per-escalation labor cost.</div>
    <div class="fieldrow"><label for="s1escA">Option A: requests escalated per month</label><input type="number" id="s1escA" step="1"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1costA">Option A: monthly escalation labor cost ($)</label><input type="number" id="s1costA" step="1"><span id="fb1b" class="fb"></span></div>
    <div class="fieldrow"><label for="s1escB">Option B: requests escalated per month</label><input type="number" id="s1escB" step="1"><span id="fb1c" class="fb"></span></div>
    <div class="fieldrow"><label for="s1costB">Option B: monthly escalation labor cost ($)</label><input type="number" id="s1costB" step="1"><span id="fb1d" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; Expected false-approval loss and total cost (D4&ndash;D5)</h4>
    <div class="goal">Option B auto-approves every row it doesn't escalate. Of those, only the p=T,q=T,r=F row is genuinely safe -- the rest are incorrectly approved. Multiply the incorrectly-approved count by Appendix D's fraud rate and average dollar value at risk to get the expected loss, then add it to Option B's escalation cost to get its true total. Compare to Option A's total (which never auto-approves anything unsafe).</div>
    <div class="fieldrow"><label for="s2incorrect">Option B: requests incorrectly auto-approved per month</label><input type="number" id="s2incorrect" step="1"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2loss">Option B: expected false-approval loss cost ($)</label><input type="number" id="s2loss" step="0.01"><span id="fb2b" class="fb"></span></div>
    <div class="fieldrow"><label for="s2totalA">Option A: total monthly cost ($)</label><input type="number" id="s2totalA" step="0.01"><span id="fb2c" class="fb"></span></div>
    <div class="fieldrow"><label for="s2totalB">Option B: total monthly cost ($)</label><input type="number" id="s2totalB" step="0.01"><span id="fb2d" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
  </div>
""",
    "twist_narrative_html": """
      <p>The VP pushes back one more time: "escalation cost is the number that actually shows up on my team's budget line every month -- the fraud loss is hypothetical." What happens to the recommendation if the true cost of an escalated review turns out to be 50% higher than Priya's estimate?</p>
""",
    "twist_apply_label": "Recompute at a 50% higher cost per escalation ($13.50 instead of $9.00)",
    "js_data_block": """
const PARAMS = {
  n_ttt: 40.0, n_ttf: 2000.0, n_tft: 30.0, n_tff: 430.0,
  n_ftt: 25.0, n_ftf: 850.0, n_fft: 15.0, n_fff: 210.0,
  cost_per_escalation: 9.0,
  fraud_rate: 0.1514,
  avg_value_at_risk: 66.0,
};
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  const total = p.n_ttt+p.n_ttf+p.n_tft+p.n_tff+p.n_ftt+p.n_ftf+p.n_fft+p.n_fff;
  const escA = total - p.n_ttf;
  const escB = p.n_fft;
  const approvedB = total - p.n_fft;
  const incorrectB = approvedB - p.n_ttf;
  const L = p.fraud_rate * p.avg_value_at_risk;
  const costA = escA * p.cost_per_escalation;
  const costB = escB * p.cost_per_escalation + incorrectB * L;
  return {A: -costA, B: -costB, costA, costB, escA, escB, incorrectB, lossB: incorrectB * L};
}
function evaluate_twist(params){
  return evaluate(Object.assign({cost_per_escalation: 13.5}, params||{}));
}
""",
    "notebook_check_functions": """
function checkStep1(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS, {cost_per_escalation: 13.5}) : PARAMS;
  const r = evaluate(p);
  fb('fb1a', near(parseFloat(val('s1escA')), r.escA, 0.5));
  fb('fb1b', near(parseFloat(val('s1costA')), r.costA, 1));
  fb('fb1c', near(parseFloat(val('s1escB')), r.escB, 0.5));
  fb('fb1d', near(parseFloat(val('s1costB')), r.escB * p.cost_per_escalation, 1));
}
function checkStep2(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS, {cost_per_escalation: 13.5}) : PARAMS;
  const r = evaluate(p);
  fb('fb2a', near(parseFloat(val('s2incorrect')), r.incorrectB, 0.5));
  fb('fb2b', near(parseFloat(val('s2loss')), r.lossB, 5));
  fb('fb2c', near(parseFloat(val('s2totalA')), r.costA, 1));
  fb('fb2d', near(parseFloat(val('s2totalB')), r.costB, 5));
}
""",
    "glossary_js": """{
  "Logical Statement": {def: "A sentence that is either true or false, used as a building block for logical rules like Priya's approval gate.",
    url: "https://www.khanacademy.org/math/geometry-home/geometry-logic"},
  "Conjunction": {def: "A compound statement joining two statements with AND, true only when both parts are true.",
    url: "https://www.mathsisfun.com/definitions/conjunction.html"},
  "Disjunction": {def: "A compound statement joining two statements with OR, true when at least one part is true.",
    url: "https://www.mathsisfun.com/definitions/disjunction.html"},
  "Negation": {def: "The opposite of a statement -- if the original is true, the negation is false, and vice versa.",
    url: "https://www.geeksforgeeks.org/dsa/mathematical-logic/"},
  "Conditional Statement": {def: "An if-then statement, such as \\"if p then q,\\" that is false only when p is true and q is false.",
    url: "https://www.mathsisfun.com/definitions/conditional-statement.html"},
  "Truth Table": {def: "A table listing every combination of true/false inputs to a logical statement and the resulting true/false output.",
    url: "https://www.geeksforgeeks.org/dsa/mathematical-logic/"},
  "Converse": {def: "The statement formed by swapping the if-part and then-part of a conditional statement (if q then p, from if p then q).",
    url: "https://www.geeksforgeeks.org/dsa/mathematical-logic/"},
  "Contrapositive": {def: "The statement formed by negating and swapping the parts of a conditional statement (if not q then not p, from if p then q) -- always has the same truth value as the original.",
    url: "https://www.geeksforgeeks.org/dsa/mathematical-logic/"}
}""",
    "howto_js": """[
  ["how to construct a truth table for a compound statement", "Truth Table"],
  ["how to determine the converse, inverse, and contrapositive of a conditional statement", "Conditional Statement"]
]""",
    "on_twist_toggle_js": """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
}
""",
}
