CONFIG = {
    "strand_summary": "Scientific Notation &middot; Factorial &middot; Absolute Value",
    "overview_banner_svg": '<figure style="margin:0 0 20px">\n<svg class="diagram" viewBox="0 0 720 250" role="img" aria-labelledby="bnT bnD" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;background:#fff;border:1px solid var(--line);border-radius:8px">\n  <title id="bnT">Two views of Priya\'s decision</title>\n  <desc id="bnD">Left: Aurora-7 and a piece of debris on paths that pass within a 5 kilometer screening range. Right: one propellant supply of 0.024 kilograms with a disposal-reserve rule line at 0.0100 kilograms; only the part above the line can be spent on avoidance maneuvers.</desc>\n  <text x="20" y="26" font-size="14" font-weight="700" fill="#1a3a5c">Two paths, one close pass</text>\n  <circle cx="170" cy="140" r="70" fill="none" stroke="#c9a227" stroke-width="1.5" stroke-dasharray="5 4"/>\n  <text x="170" y="228" font-size="12" text-anchor="middle" fill="#5b6472">screening range: 5 km</text>\n  <path d="M30 200 Q170 90 310 80" fill="none" stroke="#1a3a5c" stroke-width="3"/>\n  <path d="M40 60 Q170 150 300 205" fill="none" stroke="#a3312a" stroke-width="3" stroke-dasharray="2 5"/>\n  <circle cx="165" cy="137" r="7" fill="#1a3a5c"/>\n  <circle cx="176" cy="148" r="6" fill="#a3312a"/>\n  <text x="48" y="188" font-size="12" fill="#1a3a5c" font-weight="700">Aurora-7</text>\n  <text x="212" y="64" font-size="12" fill="#a3312a" font-weight="700">tracked debris</text>\n  <text x="190" y="118" font-size="11" fill="#5b6472">closest approach</text>\n  <line x1="360" y1="20" x2="360" y2="236" stroke="#dfe4ea" stroke-width="2"/>\n  <text x="385" y="26" font-size="14" font-weight="700" fill="#1a3a5c">One tank of bookkeeping, not two tanks</text>\n  <rect x="400" y="60" width="90" height="150" fill="#e6f4ec" stroke="#1f7a4d" stroke-width="2"/>\n  <rect x="400" y="140" width="90" height="70" fill="#fbeceb" stroke="#a3312a" stroke-width="2"/>\n  <line x1="390" y1="140" x2="500" y2="140" stroke="#122943" stroke-width="2.5" stroke-dasharray="6 3"/>\n  <text x="510" y="64" font-size="12" fill="#1f7a4d" font-weight="700">total on board: 0.024 kg</text>\n  <text x="510" y="100" font-size="12" fill="#1f7a4d">above the line: free to spend</text>\n  <text x="510" y="116" font-size="12" fill="#1f7a4d">on avoidance maneuvers</text>\n  <text x="510" y="144" font-size="12" fill="#122943" font-weight="700">rule line: 0.0100 kg</text>\n  <text x="510" y="178" font-size="12" fill="#a3312a">below the line: kept for the</text>\n  <text x="510" y="194" font-size="12" fill="#a3312a">final de-orbit burn</text>\n</svg>\n<figcaption class="side-note" style="margin-top:6px">Illustration drawn for this case, not to scale. The line is a flight rule on one shared supply of propellant, not a physical wall. Figures: Appendices D and E.</figcaption>\n</figure>',
    "protagonist": "Priya Nakamura",
    "option_a_label": "De-Orbit Now",
    "option_a_text": "End Aurora-7's data collection immediately, with a guaranteed-compliant disposal burn and zero further fuel risk.",
    "option_b_label": "Fly The Season",
    "option_b_text": "Keep Aurora-7 collecting data through the debris-conjunction season, spending reserve propellant on real avoidance maneuvers only when a conjunction's predicted collision probability actually crosses the industry threshold.",
    "skip_appendix_letters": ["F", "I"],
    "glossary_letter": "Appendix F",
    "challenge3_summary": "Include: <strong>D1</strong> a conjunction-count table (factorial-based combinations); <strong>D2</strong> a probability-notation screening table (scientific &harr; standard notation, absolute-value margin to the real threshold); <strong>D3</strong> a propellant-budget table (kilograms per m/s, then total cost of every threshold-crossing maneuver); <strong>D4</strong> a decision memo comparing Option A's certain outcome to Option B's computed outcome.",
    "deliverables": [
        ["D1", "Conjunction-count table (factorial-based combination formula; factorial expression shown before simplifying)"],
        ["D2", "Probability-notation screening table (both notations + absolute-value margin to the threshold, in scientific notation)"],
        ["D3", "Propellant-budget table (kg per m/s of delta-v, then total propellant for every threshold-crossing event)"],
        ["D4", "Decision memo (recommendation with the arithmetic that supports it)"],
    ],
    "notebook_steps_html": """
  <div class="stepbox">
    <h4>Step 1 &mdash; Counting the pairs (D1)</h4>
    <div class="goal">Appendix B says 36 objects share Aurora-7's altitude band (Aurora-7 included). Every pair of objects is one close-approach check the screening system must run. Count the unique pairs with a factorial-based combination formula, C(n, 2) = n! / (2! &times; (n &minus; 2)!), then count how many of those pairs include Aurora-7 herself.</div>
    <div class="fieldrow"><label for="s1total">Total unique pairs among the 36 objects</label><input type="number" id="s1total" step="1"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1aurora">Pairs that involve Aurora-7</label><input type="number" id="s1aurora" step="1"><span id="fb1b" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; Screening one event against the threshold (D2)</h4>
    <div class="goal">Pick an event from Appendix C. Write its maximum collision probability in standard (decimal) notation, then find the absolute-value margin |Pc &minus; threshold| against the real 1 &times; 10<sup>&minus;4</sup> threshold and write it in scientific notation (mantissa between 1 and 10, times a power of 10). Finally decide whether the event crosses the threshold.</div>
    <div class="fieldrow">
      <label for="s2event">Event</label>
      <select id="s2event"></select>
    </div>
    <div class="fieldrow"><label for="s2dec">Pc in standard notation</label><input type="number" id="s2dec" step="0.0000001"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2man">Margin &mdash; mantissa (1 to 10)</label><input type="number" id="s2man" step="0.01"><span id="fb2b" class="fb"></span></div>
    <div class="fieldrow"><label for="s2exp">Margin &mdash; power of 10</label><input type="number" id="s2exp" step="1"><span id="fb2c" class="fb"></span></div>
    <div class="fieldrow"><label for="s2cross">Does it cross the threshold?</label>
      <select id="s2cross"><option value="">choose&hellip;</option><option value="yes">Yes &mdash; maneuver recommended</option><option value="no">No &mdash; no action</option></select><span id="fb2d" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 3 &mdash; Propellant per maneuver (D3)</h4>
    <div class="goal">Exhaust velocity = Isp &times; g<sub>0</sub>. Propellant per m/s of delta-v = wet mass &divide; exhaust velocity. Enter it as a mantissa times 10<sup>&minus;4</sup> kg per m/s, then total the propellant for <em>every</em> event that crosses the threshold in the season you are currently working.</div>
    <div class="fieldrow"><label for="s3kg">kg per m/s &mdash; mantissa (&times; 10<sup>&minus;4</sup>)</label><input type="number" id="s3kg" step="0.001"><span id="fb3a" class="fb"></span></div>
    <div class="fieldrow"><label for="s3tot">Total propellant for all crossing events (kg)</label><input type="number" id="s3tot" step="0.00001"><span id="fb3b" class="fb"></span></div>
    <button onclick="checkStep3()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 4 &mdash; What is left, and the cushion (D4)</h4>
    <div class="goal">Option B can only spend what is left after the mandatory disposal reserve. Compute the propellant available for avoidance (reserve propellant minus disposal minimum), subtract the Step 3 total, and express what remains (or the shortfall, as a negative number) in kilograms. Then give that remainder as a percent of the available propellant.</div>
    <div class="fieldrow"><label for="s4left">Remaining after maneuvers (kg; negative = shortfall)</label><input type="number" id="s4left" step="0.000001"><span id="fb4a" class="fb"></span></div>
    <div class="fieldrow"><label for="s4pct">Cushion as % of available propellant</label><input type="number" id="s4pct" step="0.01"><span id="fb4b" class="fb"></span></div>
    <button onclick="checkStep4()">Check</button>
    <p class="side-note">The notebook checks your arithmetic. It does not tell you which option to recommend &mdash; that's your D4 memo.</p>
  </div>
""",
    "twist_narrative_html": """
      <p>New SOCRATES screening result, just in. A previously uncataloged fragment &mdash; debris from an unrelated collision two weeks ago &mdash; has been tracked for the first time and screened against Aurora-7. Time of closest approach: day 44, one day before the season ends. Maximum predicted Pc: 6.0 &times; 10<sup>&minus;4</sup>. Required avoidance delta-v: 5.5 meters per second.</p>
      <p>Use the same threshold rule you applied to the first six events. Tick the box below and re-run Steps 2&ndash;4 with the seventh event included. What just broke in your original plan &mdash; were you wrong, or just missing information nobody could have had? And does that change how much cushion you would want built in next time?</p>
""",
    "twist_apply_label": "Add the seventh event (E7) and re-run Steps 2&ndash;4",
    "js_data_block": """
const PARAMS = {
  isp_s: 2150.0,
  g0: 9.80665,
  wet_mass_kg: 12.0,
  reserve_propellant_kg: 0.024,
  disposal_reserve_kg: 0.0100,
  threshold_pc: 0.0001,
  n_objects: 36,
  twist_pc: 0.0006,
  twist_dv_ms: 5.5,
  season_days: 45.0,
};
const FLEX = ["wet_mass_kg", "reserve_propellant_kg", "disposal_reserve_kg"];
// Appendix C, as reported: [label, max Pc, avoidance delta-v if maneuvered (m/s) or null]
const EVENTS = [
  ["E1", 0.000027, null],
  ["E2", 0.00034, 3.5],
  ["E3", 0.000081, null],
  ["E4", 0.00019, 6.0],
  ["E5", 0.00052, 7.0],
  ["E6", 0.00011, 4.5],
];
function currentEvents(){
  return window.__TWIST_APPLIED__ ? EVENTS.concat([["E7", PARAMS.twist_pc, PARAMS.twist_dv_ms]]) : EVENTS;
}
function crosses(pc, p){ return pc >= p.threshold_pc; }
function kgPerMs(p){ return p.wet_mass_kg / (p.isp_s * p.g0); }
function requiredKg(events, p){
  let dv = 0;
  events.forEach(e => { if (crosses(e[1], p) && e[2] !== null) dv += e[2]; });
  return dv * kgPerMs(p);
}
function leftoverKg(events, p){
  return (p.reserve_propellant_kg - p.disposal_reserve_kg) - requiredKg(events, p);
}
function choose2(n){
  let f = 1;
  for (let i = 0; i < 2; i++) f *= (n - i) / (i + 1);
  return Math.round(f);
}
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  const left = leftoverKg(EVENTS, p);
  return {A: 0, B: left >= 0 ? p.season_days : -1, leftover_kg: left};
}
// Twist: a seventh event, E7, discovered late in the season
function evaluate_twist(params){
  const p = Object.assign({}, PARAMS, params||{});
  const ev = EVENTS.concat([["E7", p.twist_pc, p.twist_dv_ms]]);
  const left = leftoverKg(ev, p);
  return {A: 0, B: left >= 0 ? p.season_days : -1, leftover_kg: left};
}
(function(){
  const sel = () => document.getElementById('s2event');
  window.refreshEventSelect = function(){
    const s = sel(); if (!s) return;
    const keep = s.value;
    s.innerHTML = currentEvents().map(e => '<option value="'+e[0]+'">'+e[0]+'</option>').join('');
    if (keep) s.value = keep;
  };
  document.addEventListener('DOMContentLoaded', window.refreshEventSelect);
})();
""",
    "notebook_check_functions": """
function checkStep1(){
  const n = PARAMS.n_objects;
  fb('fb1a', near(parseFloat(val('s1total')), choose2(n), 0.5));
  fb('fb1b', near(parseFloat(val('s1aurora')), n - 1, 0.5));
}
function checkStep2(){
  const lab = document.getElementById('s2event').value;
  const e = currentEvents().find(x => x[0] === lab);
  if (!e) return;
  const pc = e[1];
  const margin = Math.abs(pc - PARAMS.threshold_pc);
  const exp = Math.floor(Math.log10(margin) + 1e-9);
  const man = margin / Math.pow(10, exp);
  fb('fb2a', near(parseFloat(val('s2dec')), pc, 0.0000001));
  fb('fb2b', near(parseFloat(val('s2man')), man, 0.02));
  fb('fb2c', near(parseFloat(val('s2exp')), exp, 0.5));
  fb('fb2d', document.getElementById('s2cross').value === (crosses(pc, PARAMS) ? 'yes' : 'no'));
}
function checkStep3(){
  const kg = kgPerMs(PARAMS);
  fb('fb3a', near(parseFloat(val('s3kg')), kg * 1e4, 0.01));
  fb('fb3b', near(parseFloat(val('s3tot')), requiredKg(currentEvents(), PARAMS), 0.00002));
}
function checkStep4(){
  const avail = PARAMS.reserve_propellant_kg - PARAMS.disposal_reserve_kg;
  const left = leftoverKg(currentEvents(), PARAMS);
  fb('fb4a', near(parseFloat(val('s4left')), left, 0.00001));
  fb('fb4b', near(parseFloat(val('s4pct')), 100 * left / avail, 0.2));
}
""",
    "glossary_js": """{
  "Standard Notation": {def: "A number written the ordinary way, digit by digit, e.g. 0.00034 -- as opposed to scientific notation.",
    url: "https://www.mathsisfun.com/definitions/standard-notation.html"},
  "Scientific Notation": {def: "A compact way to write very large or very small numbers: a number from 1-10 times a power of 10.",
    url: "https://www.mathsisfun.com/numbers/scientific-notation.html"},
  "Factorial": {def: "The product of a whole number and every positive whole number below it, written n! -- e.g. 5! = 5 x 4 x 3 x 2 x 1.",
    url: "https://www.mathsisfun.com/numbers/factorial.html"},
  "Combination": {def: "A selection of items where order does not matter; the number of ways to pick r of n items is n! / (r! x (n - r)!).",
    url: "https://www.mathsisfun.com/combinatorics/combinations-permutations.html"},
  "Absolute Value": {def: "How far a number is from zero on the number line -- always zero or positive.",
    url: "https://www.mathsisfun.com/numbers/absolute-value.html"},
  "Order of Magnitude": {def: "A power of 10; two numbers differ by one order of magnitude when one is about ten times the other.",
    url: "https://www.mathsisfun.com/definitions/order-of-magnitude.html"},
  "Rate": {def: "A ratio that compares two quantities with different units, such as kilograms per meter/second.",
    url: "https://www.mathsisfun.com/definitions/rate.html"},
  "Ratio": {def: "A way of comparing two quantities by division, written a:b or a/b.",
    url: "https://www.mathsisfun.com/numbers/ratio.html"},
  "Probability": {def: "A number between 0 and 1 describing how likely an event is to happen.",
    url: "https://www.mathsisfun.com/data/probability.html"},
  "Percent": {def: "A ratio that compares a number to 100 -- literally \\"per hundred.\\"",
    url: "https://www.mathsisfun.com/percentage.html"}
}""",
    "howto_js": """[
  ["how to write a number in standard notation given its scientific notation", "Standard Notation"],
  ["how to evaluate a factorial expression", "Factorial"],
  ["how to write a number in scientific notation given its standard notation", "Scientific Notation"],
  ["how to convert an amount with compound units", "Rate"]
]""",
    "on_twist_toggle_js": """
function onTwistToggle(){
  // Adds E7 to the event picker and makes Steps 2-4 grade against the
  // seven-event season. Prints no verdict -- the Check buttons still compute.
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
  if (window.refreshEventSelect) window.refreshEventSelect();
}
""",
}
