const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, AlignmentType, LevelFormat,
} = require("docx");

const PAGE = { size: { width: 12240, height: 15840 } };
const NAVY = "1a3a5c";
const GOLD = "c9a227";
const GREY = "5b6472";
const BOXBG = "FBF8EE";

function h1(text) {
  return new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 260, after: 160 }, children: [new TextRun({ text, bold: true, color: NAVY, size: 32 })] });
}
function h2(text) {
  return new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 220, after: 120 }, children: [new TextRun({ text, bold: true, color: NAVY, size: 26 })] });
}
function p(text, opts = {}) {
  return new Paragraph({ spacing: { after: 140 }, children: [new TextRun({ text, ...opts })] });
}
function pMulti(runs, opts = {}) {
  return new Paragraph({ spacing: { after: 140 }, ...opts, children: runs });
}
function bullet(text, opts = {}) {
  return new Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { after: 100 }, children: [new TextRun({ text, ...opts })] });
}
function numbered(text, opts = {}) {
  return new Paragraph({ numbering: { reference: "numbers", level: 0 }, spacing: { after: 120 }, children: [new TextRun({ text, ...opts })] });
}
function cell(text, { width, header = false, shade = null, bold = false } = {}) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: shade ? { type: ShadingType.CLEAR, fill: shade } : undefined,
    margins: { top: 80, bottom: 80, left: 100, right: 100 },
    children: [new Paragraph({ children: [new TextRun({ text, bold: header || bold, color: header ? "FFFFFF" : "000000", size: 20 })] })],
  });
}
function dataTable(headerRow, rows, widths) {
  return new Table({
    width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    columnWidths: widths,
    rows: [
      new TableRow({ tableHeader: true, children: headerRow.map((t, i) => cell(t, { width: widths[i], header: true, shade: NAVY })) }),
      ...rows.map((r, ri) => new TableRow({ children: r.map((t, i) => cell(String(t), { width: widths[i], shade: ri % 2 === 1 ? "F7F9FB" : null })) })),
    ],
  });
}
function boxed(children) {
  return new Table({
    width: { size: 9500, type: WidthType.DXA },
    columnWidths: [9500],
    rows: [new TableRow({ children: [new TableCell({
      width: { size: 9500, type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, fill: BOXBG },
      margins: { top: 160, bottom: 160, left: 200, right: 200 },
      children,
    })] })],
  });
}

const doc = new Document({
  numbering: {
    config: [
      { reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 260 } } } }] },
      { reference: "numbers", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 260 } } } }] },
    ],
  },
  sections: [{
    properties: { page: { size: PAGE.size, margin: { top: 1080, bottom: 1080, left: 1080, right: 1080 } } },
    children: [
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: [new TextRun({ text: "Facilitator Guide: Prove It Scales", bold: true, size: 40, color: NAVY })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [new TextRun({ text: "FACILITATOR-ONLY — do not distribute to students", bold: true, size: 20, color: "a3312a" })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 300 }, children: [new TextRun({ text: "MS | Math | Case Study | 2026-27 | Adventure", size: 20, color: GREY, italics: true })] }),

      p("Case: Prove It Scales · Tier: T2 (MS-core) · Studio: Adventure", { bold: true }),
      p("Standards: Discrete Mathematics/Proof And Recursion — Mathematical Induction, Base Case, Inductive Step, and How to prove a statement using mathematical induction."),

      // SPEC 1c: sensitivity note box at top
      boxed([
        p("Facilitator note — sensitivity (SPEC §6)", { bold: true, color: NAVY }),
        p("NONE. This is routine software-engineering correctness-vs-performance math — no subject-matter sensitivity flag applies."),
      ]),

      h2("Real-World Grounding (facilitator background)"),
      bullet("Oren Eini (Ayende Rahien), founder of RavenDB — \"Production postmortem: Your math is wrong, recursion doesn't work this way\" (ayende.com/blog/197637-A). A real recursive map-reduce billing-aggregation function silently violated its own inductive assumption once already-reduced intermediate results were fed back into it across cluster nodes, producing real divergent per-account billing totals. This is the real-world precedent for Appendix E and for Background's \"Meterworks has shipped a bug of this shape before\" line — the Meterworks incident is fictional scenario detail modeled on this real failure shape; the two are not the same incident, and the case should never claim they are."),
      bullet("Felipe Dutra Tine e Silva, \"Iterative vs Recursive vs Tail-Recursive in Golang\" — real, reproducible Go benchmark: iterative 16.4 ns/op, tail-recursive 33.3 ns/op, plain (non-tail) recursive 394 ns/op. This is the real ~2x (TCO honored) vs. ~24x (TCO not honored) gap Appendix D scales from."),
      bullet("pope/go_recursive_benchmark (GitHub) — real extreme-case benchmark: a naive exponential-recursion Fibonacci at ~312,238,250 ns/op vs. a tail-call-optimized rewrite at ~35.36 ns/op — roughly an 8.8-million-times gap. This is the real anchor for Appendix E's extreme-case row, and for the Twist."),
      bullet("AWS TLA+ on DynamoDB/S3 (Newcombe et al., CACM 2015) and seL4 / DARPA HACMS (Klein et al.) — real, named engineering-culture anchors for \"prove it, don't just argue it informally,\" useful for Intro framing and for pressure-testing whether Devon's stakes justify a proof at all."),

      h2("Intro"),
      p("Frame the format: this is a real ship/no-ship engineering decision the night before a release freeze, not a worksheet. Name the opener — \"You are the engineer whose name is on this function. One version is proven correct. The other version is proven fast. You don't get both, and you have to pick tonight.\" Mention, once, that companies like AWS have used formal proof methods (TLA+) to catch real bugs before shipping — this is a real professional practice, not an academic exercise invented for the case."),

      h2("Launch"),
      p("Show the two branches side by side exactly as the Overview describes them — the proof, and the climbing red chart on Devon's second monitor — with no runtime numbers yet. Ask: \"Which one would you ship, just from what you see here?\" Do not confirm or correct. Most rooms will split; record the split, Close will re-ask it."),

      h2("Anchor 1 — Take a Stand and Vote"),
      p("TAKE A STAND AND VOTE. No reasoning yet, just commit.", { bold: true }),
      p("\"Is anyone courageous enough to stand with the Guaranteed Floor — the version with no proof on file?\" Show of hands, both options, no discussion yet. Record the count."),

      h2("Anchor 2 — What Is The Problem We're Solving?"),
      p("\"Is this the right question?\" · \"What do you mean by 'proven correct'?\"", { bold: true }),
      p("Let confusion grow here on purpose. Heroes will want to jump straight to \"which one is faster,\" but push on what \"proven correct\" buys you that \"tested and it looked fine\" doesn't: \"If the Guaranteed Floor's tests all pass at depth 6, and Meterworks' real account trees never nest past depth 6, does the Provable Path's proof matter at all? What would have to be true about Meterworks' actual account hierarchies for that proof to matter?\" If the room lands on \"a proof covers depths nobody has tested yet, a test suite only covers the depths someone thought to try,\" the case is working as designed."),

      h2("Anchor 3 — What Is The Process?"),
      p("\"If we go through this process and find the data, how will we decide?\"", { bold: true }),
      p("Once the room separates \"which one is faster\" from \"which one's correctness guarantee is worth trusting,\" ask them to name the actual steps before touching the appendices: write the induction proof itself, base case and inductive step (D1); trace it on a real sample hierarchy (D2); connect the inductive step to why runtime scales with depth (D3); build the six-cell runtime table across both TCO scenarios and three depths (D4); and decide, using all of that, which version ships (D5). Re-ask: \"Is our question still the right one, now that we can see the steps?\""),

      h2("Anchor 4 — What Don't We Know?"),
      p("\"Do we need to make assumptions? Which ones are critical?\"", { bold: true }),
      p("Surface the real gap honestly: Meterworks' own traffic volume, its own maximum real account-hierarchy depth, and which language runtime the release actually ships to are all scenario figures — Meterworks is fictional, so none of these can be independently verified the way the shape of the recursive/iterative cost gap can (that part is anchored to a real, published benchmark). Ask which of the open figures is actually load-bearing for the recommendation. The honest answer: the target-runtime TCO fact (Appendix B) is the single most load-bearing item in the whole case — it is the variable that decides whether Option A costs ~2x or ~24x-1,000x+ more than Option B, which is a materially different question than \"is recursion slower.\""),

      h2("Data Deep Dive"),
      p("Now, and only now, the numbers. Walk D1's proof, D2's trace, D3's interpretation, and D4's six-cell table together as a room, cold-calling for D4 specifically — this is where a Hero who wrote a correct D1 proof but never connects it to D4's actual runtime numbers will visibly struggle to answer \"so is the proof worth it, here, tonight.\""),

      h2("Twist — Drop at ~15 Minutes Into the Discussion"),
      p("Deliver slowly, with pauses: \"There's a real company — not Meterworks, a real one — whose recursive billing-aggregation function looked exactly like the Provable Path. It was proven correct on paper. It shipped anyway. And in production, it silently violated its own inductive assumption once an already-computed result got fed back into it one level down — two customer accounts' billing totals came out on opposite sides of zero for the same real numbers.\""),
      p("\"If a proof like the one you wrote for D1 can still fail in production when the implementation doesn't actually match the proof's own assumptions at every call site — does that make you trust the Provable Path more, or less, than you did five minutes ago? What exactly would you have to check, beyond writing the proof itself, to be sure this doesn't happen to Devon's version?\""),
      p("Facilitator-only: what this does and doesn't change. This is the real Ayende/RavenDB postmortem — it does not change D4's runtime numbers, and it is not proof that Option A is wrong. It is proof that \"I wrote an induction proof\" and \"the shipped code provably matches every premise the proof assumed at every call site\" are two different claims, and a Hero who conflates them has not fully reckoned with what D1 does and doesn't guarantee.", { italics: true }),

      h2("45-Minute Socratic Plan (SPEC §7.3)"),
      dataTable(["Time", "Move"], [
        ["0:00–3:00", "Cold-call launch (Intro/Launch above), 30-second commitments, stand/sit vote (Anchor 1) — no explanation."],
        ["3:00–10:00", "Position defense: \"Convince us why it's better, not just fair\" (Anchor 2 — what does \"proven correct\" actually buy you?)."],
        ["10:00–15:00", "Pressure-test the models: process and open assumptions (Anchors 3–4) — name the D1-D5 steps, surface which figures are real vs. stated."],
        ["15:00–25:00", "Data Deep Dive — D1-D5 together; cold-call D4's six-cell table specifically."],
        ["25:00", "DROP THE TWIST — the real RavenDB/Ayende postmortem, delivered slowly, with pauses."],
        ["25:00–30:00", "Immediate recommit: who reverses? \"What just broke — the proof, or your trust in what the proof covers?\""],
        ["30:00–40:00", "Threaded deep conflict — see the three named threads below."],
        ["40:00–45:00", "Close, re-vote, reflection, Lessons Learned."],
      ], [1600, 7900]),

      h2("Deep Conflict — Threads (20–30 min)"),
      numbered("A proof about the function is not automatically a proof about the deployed system. D1's induction proof is airtight given its own stated assumptions — but the RavenDB twist shows a real case where the code silently stopped matching those assumptions at one call site. Push: \"What would you need to check, beyond D1 itself, to be sure Devon's implementation actually satisfies D1's inductive step at every real call site?\""),
      numbered("\"Recursive is slower\" is not one fact, it's a fact that depends on one switch. A Hero who treats Appendix D as \"recursion costs more\" without noticing the TCO column has missed the entire secondary lever the case is built around. Push: \"If Meterworks' target runtime honored TCO, would this still be a hard decision?\""),
      numbered("Correct-forever vs. fast-right-now. The Provable Path's guarantee holds for every depth, including depths Meterworks doesn't have yet. Push: \"Is a guarantee about hierarchy depths that don't exist yet worth paying for today — and does your answer change if Meterworks is growing?\""),

      h2("The Trap"),
      p("Heroes will treat \"recursive is slower\" as a flat, universal fact and recommend the Guaranteed Floor on that basis alone, without ever checking Appendix B's TCO fact — missing that the real size of the gap (Appendix D) depends entirely on whether the target runtime honors tail-call optimization, which is the actual analytical fork this case is built around. A second, related trap: treating D1's induction proof as a guarantee about the deployed system rather than a guarantee about the function as specified — the RavenDB twist exists specifically to catch a Hero who has not distinguished \"I proved the recurrence is correct\" from \"I verified the shipped code actually satisfies every premise the proof assumed at every call site.\""),

      h2("Socratic Questions"),
      numbered("Your D4 table has two very different numbers for the recursive version — one under a TCO-honoring runtime, one without. Which of those two numbers should actually drive Devon's recommendation, and why does it matter which one you pick?"),
      numbered("Your D1 proof shows the recursive version is correct for a hierarchy of any depth. Does that proof, by itself, tell you anything about how fast the function runs? Why or why not?"),
      numbered("The twist describes a real company whose recursive aggregation function was proven correct on paper and still produced wrong billing totals in production. Does that mean D1's proof was worthless — or does it mean something more specific about what a proof does and doesn't cover?"),
      numbered("If Meterworks' maximum real account-hierarchy depth turned out to be much shallower than the \"Deep\" row in Appendix D, which parts of your D4/D5 argument would still hold, and which wouldn't?"),
      numbered("Appendix A lists a target language/runtime for the release as a still-open figure. If you had to recommend a version before that runtime is finalized, would you recommend differently than if you already knew whether it honors tail-call optimization? What does that tell you about how much of this decision is actually a math question versus an infrastructure question?"),

      h2("Close"),
      p("VOTE AGAIN.", { bold: true }),
      p("\"Did we ask the right question at the start?\" \"What math was new to you tonight, and how did you actually attack it?\" Compare to Anchor 1's vote — a room that moves after the twist should be pressed to explain the move using D1/D4, not just the twist's emotional weight."),

      h2("Balance Argument (SPEC §2)"),
      p("Argument for A (the Provable Path).", { bold: true }),
      p("The induction proof (D1) is airtight for every hierarchy depth Meterworks will ever have, including depths that don't exist in its account base yet — a real, permanent asset for billing-critical code, and the exact kind of guarantee AWS's own engineers have said they wished they'd had before shipping DynamoDB/S3-critical code informally. If the target runtime honors TCO (Appendix B), the real Go-benchmark-anchored cost gap at the Shallow depth is only 0.333 ms vs. 0.164 ms per 10,000 rollups (S1) — a real but modest 50.8% difference — making the correctness guarantee nearly free at the depths (up to 5 levels, S5) Meterworks actually has today."),
      p("Argument for B (the Guaranteed Floor).", { bold: true }),
      p("Its per-call cost (0.164 ms/10,000 rollups at Shallow, S1) never depends on a runtime detail Devon does not control. Under Go — the case's actual named target, which does not honor TCO (S4) — the recursive version costs 3.94 ms/10,000 at the same depth, a real, sourced 95.8% gap, and the real extreme-case benchmark (S2) shows non-tail-callable recursion can reach a ~8.8-million-times gap at depth 40. Meterworks has already shipped one production bug of exactly the shape a real, documented 2022 postmortem describes (S3, –67,343 vs +67,329 on the same account)."),

      p("Margin — 95.8%. Winner: Option B, The Guaranteed Floor (iterative).", { bold: true }),
      p("At the Shallow depth (closest to Appendix A's real max hierarchy depth, 5 levels, AWS Organizations FAQ), under Go — Appendix A's target runtime, which Appendix B/S4 confirms does not guarantee or reliably apply TCO — Option A (recursive) costs 3.94 ms per 10,000 rollups and Option B (iterative) costs 0.164 ms, both real, directly-measured figures from the Felipe Dutra Tine e Silva Go benchmark (S1). margin_pct = (3.94 − 0.164) / 3.94 × 100 = 95.8%."),

      boxed([
        p("MCS-46 waiver on file", { bold: true, color: NAVY }),
        p("This margin is wide, well past SPEC §2's ~20% guideline, and it is not softened. The counterfactual was checked: even under a TCO-honoring runtime instead of Go, the same Shallow-row real data gives (0.333 − 0.164) / 0.333 = 50.8% — still far over 20%. This is not an artifact of picking Go as the target runtime (MA7): the real, cited D4 numbers show iterative beating recursive decisively under both runtime regimes at every measured depth. No available Modeling Assumption is a lever that would bring the margin under ~20% without contradicting real, cited benchmark data (S1, S2) — retuning is not available here the way it is on other cases, because the gap is real, not a modeling artifact. Approved per MCS-46 (DOCTRINE_LEDGER.md), scoped narrowly to this case's own researched figures — not a general relaxation, and not retroactive to any other case. Approved by manan.atit@gmail.com, 2026-09-01."),
      ]),

      p("What this means for facilitation.", { bold: true }),
      p("The case's genuine tension is not a close numeric race on D4 — it's the qualitative one argument_a/argument_b are already built around: D1's permanent, depth-independent correctness guarantee vs. D4's decisive, real, sourced performance cost. Treat this the way a T1-tier case with a clean, lopsided winner is treated: the room's real work is arguing whether the correctness guarantee is worth paying a large, real cost for — not disputing whose number is bigger."),

      h2("What a Strong Defense Sounds Like"),
      p("This case has no single right answer, so there is no answer key to grade against — but a strong defense has a recognizable shape regardless of which option a Hero ultimately recommends. It states D1's base case and inductive step precisely enough that a reader could check them independently, not just gesture at \"it works by induction.\" It reads D4's six-cell table correctly — naming which of the two recursive columns (TCO-honored vs. not) actually governs Devon's real decision, and why the target-runtime fact in Appendix A is what selects it, rather than treating \"recursive is slower\" as a single flat number. It engages the Twist honestly: a strong defense of Option A explains what would have to be independently checked, beyond the proof itself, to trust that the deployed code matches every premise D1 assumed — it does not wave the postmortem away, and it does not treat the postmortem as disqualifying either. And it closes with a recommendation that is actually defended by D1's proof status, D4's numbers, and Appendix A's target-runtime fact together, not by only one of the three."),

      h2("Skills Exercised"),
      bullet("Mathematical Induction — constructing and defending a full induction proof (base case, inductive step, closing generalization) for a recursive function."),
      bullet("Base Case — identifying and stating the base case of a recursive definition precisely."),
      bullet("Inductive Step — identifying and stating the inductive step, and using it to reason about per-call cost."),
      bullet("How to prove a statement using mathematical induction — applying the general induction proof technique to a concrete, real engineering artifact."),
      bullet("Reading and interpreting a multi-column, multi-row data table under a stated modeling assumption (MA7) that changes which column applies."),
      bullet("Distinguishing a proof about a specification from a proof about a deployed system — a correctness-scope reasoning skill surfaced by the Twist."),
    ],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync("cases/prove-it-scales/published/Prove It Scales - Facilitator Guide.docx", buf);
  console.log("wrote Prove It Scales - Facilitator Guide.docx", buf.length, "bytes");
});
