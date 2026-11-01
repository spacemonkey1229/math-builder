// Facilitator Guide .docx for The Gijon Rule. Body is converted from FACILITATOR.md (shared renderer in
// build_docx.js); the publish-time run-of-show (SKILL 1c) and the boxed framing/sensitivity note are added on top.
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
  AlignmentType, BorderStyle,
} = require("docx");
const { mdToChildren, inlineRuns, styles, numbering, footer, NAVY, GOLD, CONTENT_W } = require("./build_docx.js");

const caseJson = JSON.parse(fs.readFileSync(path.join(__dirname, "case.json"), "utf8"));
const fac = fs.readFileSync(path.join(__dirname, "FACILITATOR.md"), "utf8");

// Split off the closing sensitivity section: it is moved into the boxed note at the top.
const MARK = "## Facilitator note — sensitivity";
const mi = fac.indexOf(MARK);
if (mi < 0) throw new Error("sensitivity section not found in FACILITATOR.md");
const sensText = fac.slice(mi + MARK.length).trim();
let bodyMd = fac.slice(0, mi).replace(/\n---\s*\n\s*$/, "\n");
// Drop the guide's own title/meta lines (replaced by this document's title block) but keep the Tier/metric line.
const bl = bodyMd.split("\n");
const tierLine = bl.find((l) => l.startsWith("**Tier:**"));
bodyMd = bl.slice(bl.findIndex((l) => l.startsWith("---"))).join("\n");

function box(titleText, paras, { fill = "FBF4DC", edge = GOLD, titleColor = "7a4a00" } = {}) {
  const border = { style: BorderStyle.SINGLE, size: 12, color: edge };
  const borders = { top: border, bottom: border, left: border, right: border };
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W],
    rows: [new TableRow({ children: [new TableCell({
      width: { size: CONTENT_W, type: WidthType.DXA }, borders,
      shading: { type: ShadingType.CLEAR, color: "auto", fill },
      margins: { top: 120, bottom: 120, left: 180, right: 180 },
      children: [
        new Paragraph({ spacing: { after: 100 }, children: [new TextRun({ text: titleText, bold: true, size: 24, color: titleColor })] }),
        ...paras.map((t) => new Paragraph({ spacing: { after: 100 }, children: inlineRuns(t) })),
      ],
    })] })],
  });
}

const b = caseJson.balance;
const sensParas = sensText.split(/\n\s*\n/).map((s) => s.replace(/\n/g, " ").trim()).filter(Boolean);

const children = [
  new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: "Facilitator Guide: The Gijon Rule", bold: true, size: 44, color: NAVY })] }),
  new Paragraph({ spacing: { after: 160 }, children: [new TextRun({ text: "FACILITATOR ONLY — contains the balance argument, the margin, the trap and the twist. Do not distribute to Heroes.", bold: true, color: "a3312a" })] }),

  box("Read first: framing and sensitivity note", [
    "**This is an incentive-structure story, not an accusation.** " + sensParas[0],
    ...sensParas.slice(1),
  ]),
  new Paragraph({ spacing: { after: 160 }, children: [] }),

  new Paragraph({ spacing: { after: 100 }, children: inlineRuns(tierLine) }),
  new Paragraph({ spacing: { after: 100 }, children: inlineRuns("**Case:** The Gijon Rule  ·  **Studio:** Adventure  ·  **Source files:** case.md, FACILITATOR.md, case.json.balance / derived, sensitivity_model.py") }),

  new Paragraph({ heading: "Heading1", children: [new TextRun("The Balance Argument (Answer Key, Facilitator Only)")] }),
  new Paragraph({ spacing: { after: 120 }, children: inlineRuns("**Argument for A (Same-Clock Only).** " + b.argument_a) }),
  new Paragraph({ spacing: { after: 120 }, children: inlineRuns("**Argument for B (Same-Clock, Goals First).** " + b.argument_b) }),
  new Paragraph({ spacing: { after: 120 }, children: inlineRuns("**Margin.** " + b.margin_basis + " On the stated primary number Option A wins; the case is two-sided because the committee has not said whether the ceiling or the average counts for more.") }),
  new Paragraph({ spacing: { after: 120 }, children: inlineRuns("**The trap.** Heroes count the 1-0 grid, see Option B shrink it, and stop, missing that B raises the highest-scoring benchmark (6-5) and so raises the ceiling. A second form: treating the 49 cells as probabilities. Both are worked in full under Anchor 2 and Step 5 below.") }),

  new Paragraph({ heading: "Heading1", children: [new TextRun("Five Socratic Questions")] }),
  ...[
    "\"Punishes it for which teams, in which tournaments? Does it only change 1982?\" (Anchor 2: the goals-first fix)",
    "\"If we get a percent for 1-0 and a percent for 6-5, how do we decide which one the committee should care about, before we see the numbers?\" (Anchor 3)",
    "\"Why 0-6 goals? What if it were 0-3 or 0-9?\" (Anchor 4: have them actually try it)",
    "\"If B takes 1-0 off the table, why does the ceiling go up?\" (Thread 1)",
    "\"Option A is what FIFA actually did. Does that make it the better rule, or only the one history picked?\" (Thread 2)",
  ].map((t, k) => new Paragraph({ spacing: { after: 80 }, indent: { left: 360, hanging: 360 }, children: [new TextRun({ text: (k + 1) + ".\t" }), ...inlineRuns(t)], tabStops: [{ type: "left", position: 360 }] })),

  new Paragraph({ heading: "Heading1", children: [new TextRun("What a Strong Defense Sounds Like")] }),
  new Paragraph({ spacing: { after: 120 }, children: inlineRuns("This is not an answer key; the case has no single right answer. A weak defense picks a rule and a number and stops. A strong defense does five things: it states which number it is optimising (the ceiling, the average, or the 1-0 share) and why; it says out loud that the 49 cells are a counting device and not probabilities; it explains why coasting was individually rational under the 1982 rules without anyone breaking a rule; it names what its own rule costs (for B: it raises the 6-5 share, rewrites Group 6 and would have sent Algeria, not Austria, through in 1982, and changes every future group; for A: it leaves the 1-0 deal at about four cells in five); and it names the one assumption or number that would change its mind (the goal window, the choice of benchmark scorelines, or which summary the committee adopts). After the twist, a strong defense says what changed and what did not, rather than defending the old ranking by reflex.") }),

  new Paragraph({ heading: "Heading1", children: [new TextRun("Full Guide Notes")] }),
  ...mdToChildren(bodyMd),

];

const doc = new Document({
  numbering, styles,
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1000, bottom: 1000, left: 1100, right: 1100 } } },
    footers: { default: footer("The Gijon Rule — Facilitator Guide — FACILITATOR ONLY") },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  const out = path.join(__dirname, "published", "The Gijon Rule - Facilitator Guide.docx");
  fs.writeFileSync(out, buf);
  console.log("wrote", out, buf.length, "bytes");
});
