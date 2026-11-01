// Facilitator Guide .docx for The Hundredth: FACILITATOR.md + publish-time run-of-show
// (case-publish SKILL 1c). The teacher-facing sensitivity note is boxed at the top.
const fs = require("fs");
const path = require("path");
const { Document, Packer, Paragraph, TextRun, AlignmentType } = require("docx");
const { mdToChildren, boxedNote, numbering, NAVY } = require("./docx_lib");

const cj = JSON.parse(fs.readFileSync(path.join(__dirname, "case.json"), "utf8"));
let fac = fs.readFileSync(path.join(__dirname, "FACILITATOR.md"), "utf8");

// Pull the sensitivity note out of FACILITATOR.md so it is boxed at the top and not duplicated at the bottom.
const m = fac.match(/\n---\s*\n\s*## Facilitator note — sensitivity\s*\n([\s\S]*)$/);
if (!m) throw new Error("sensitivity note section not found in FACILITATOR.md");
const noteBody = m[1].trim().replace(/^\*\*Teacher-facing sensitivity note\.\*\*\s*/, "");
fac = fac.slice(0, m.index);
const noteParas = noteBody.split(/\s(?=\(\d\)\s)/).map((x) => x.trim()).filter(Boolean);

const bal = cj.balance;
const strongDefense = "There is no single right ruling here, so a strong defense is judged on the quality of its reasoning, not its conclusion. " +
  "It names the metric (the probability the ruling instrument orders a close finish correctly) rather than arguing from \"the video shows it\" or \"the pad measures to a thousandth\". " +
  "It treats a lag common to both lanes as cancelling, and compares the differential lag to the actual reported gap, not to zero. " +
  "It gives video a band made of both the frame period and a human reading band, and says which frame rates can actually separate a hundredth. " +
  "It states its own range for the differential lag, defends it using Ekumbo's and Bertaud's statements as attributed claims, and admits that no source measured it. " +
  "It names which single number the ruling depends on and what measurement would settle it, and it holds up when the twist drops, either by changing the ruling with a reason or by keeping it with a reason. " +
  "A defense that speaks of motive, or of who deserved the medal, has left the instrument question.";

const extra = [
  "## Publish-time run-of-show",
  "### The two arguments and the margin",
  `**Argument for A (Pad Ranks).** ${bal.argument_a}`,
  `**Argument for B (Contact Ranks).** ${bal.argument_b}`,
  `**Margin.** ${bal.margin_basis} Contact Ranks wins by ${bal.margin_pct}% on the scenario values (about 0.8 percentage points). This is a knife-edge by design. ${bal.twist_effect}`,
  "### Five Socratic questions",
  "- Three named sources say three slightly different things. Which of them is a measurement, and which is a claim?",
  "- A video of what? A frame is a snapshot every so often, and who decides which frame is first contact?",
  "- Does the pad measure the touch, or the touch plus a delay? Does the rulebook even let the third digit count?",
  "- Which single number does your ruling depend on most, and what would you measure to settle it?",
  "- Were you wrong when the twist dropped, or were you just missing information?",
  "### What a strong defense sounds like",
  strongDefense,
].join("\n\n").replace(/\n\n- /g, "\n- ");

const doc = new Document({
  numbering,
  styles: {
    default: { document: { run: { font: "Calibri", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 30, bold: true, color: NAVY, font: "Calibri" } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 26, bold: true, color: NAVY, font: "Calibri" } },
    ],
  },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1300, bottom: 1300, left: 1440, right: 1440 } } },
    children: [
      new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: "Facilitator Guide: The Hundredth", bold: true, size: 40, color: NAVY })] }),
      new Paragraph({ spacing: { after: 160 }, children: [new TextRun({ text: "FACILITATOR ONLY. Contains the balance argument, the margin, the twist and the trap. Do not distribute to Heroes.", bold: true, color: "a3312a" })] }),
      boxedNote("Teacher-facing sensitivity note: read before you run this room", noteParas),
      new Paragraph({ spacing: { after: 160 }, children: [] }),
      ...mdToChildren(fac.replace(/^# Guide Notes: The Hundredth\s*/, ""), { svgPrefix: "fac_diag" }),
      ...mdToChildren(extra, { svgPrefix: "fac_diag2" }),
    ],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  const out = path.join(__dirname, "published", "The Hundredth - Facilitator Guide.docx");
  fs.mkdirSync(path.dirname(out), { recursive: true });
  fs.writeFileSync(out, buf);
  console.log("wrote", out, buf.length, "bytes");
});
