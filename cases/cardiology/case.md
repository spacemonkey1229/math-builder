# Case Study: Cardiology

MS | Math | Case Study | 2026-27 | Heroes Academy

---

## Overview

"Your afternoon appointment is here," pages Wendy. "Thank you, I'll come out and meet them," replies Dr. Zeke Hotchkiss. He walks to the lobby and greets Cindy and Paul. "It's good to see you this morning, thank you for coming in." "Good to see you too," Paul responds. "Let's head down to my office so we can chat."

Dr. Hotchkiss leads the couple to his office, where they sit down around a coffee table. "We have your lab results, and we're here to discuss treatment options for your coronary artery disease, Paul," the doctor starts. "There are essentially two therapy options we could pursue. I'll share the pros and cons of each and give you my recommendation."

Paul nods slowly. He's been dreading this appointment for weeks, ever since the angiogram, ever since the words "coronary artery disease" first came up in a hallway conversation he wasn't ready for. Cindy reaches for his hand under the table, the way she always does before hard news.

"I want you to understand both paths clearly before you decide anything," Dr. Hotchkiss continues. "One is medication, managed carefully, for as long as it keeps working. The other adds surgery on top of that medication. Neither one is automatically right for every patient who walks through that door — but for you specifically, the numbers point somewhere. Let's walk through them together."

Whatever Dr. Hotchkiss recommends today, Paul is the one who has to live with it — literally. Cindy squeezes his hand once, and the room goes quiet as the doctor reaches for the folder on his desk.

---

## Background

Dr. Zeke Hotchkiss has worked as a cardiologist for over a decade at the Denver Health Medical Center, consulting with over 1,700 patients over his career. He has participated in several research studies on cardiovascular disease and treatment, including a recently-completed landmark study run by Duke University comparing two therapies for patients with coronary artery disease (CAD) — **SEE APPENDIX A**.

The study compared two therapies: **medication only (MT)**, and **medication plus coronary artery bypass graft surgery (CABG)**. Both treat CAD — specifically, congestive heart failure caused by a prior heart attack.

One detail Paul and Cindy don't know: the medication used in MT is made by a pharmaceutical company that has an affiliate agreement with Dr. Hotchkiss's office, paying it 0.97% of every sale of the medication his office prescribes. The CABG surgery is performed through a different office, from which Dr. Hotchkiss's office receives no referral benefit, and the follow-up medication used after CABG surgery is a different drug, unaffected by the agreement. This is disclosed here as real background, not a number the case's math turns on — it's the kind of fact a careful advisor discloses to a patient regardless of whether it changes the recommendation.

**Paul Cadenson** is a 57-year-old with no previous cardiovascular treatment. His history includes pre-diabetes, Class I obesity, a family history of premature CAD, and daily tobacco use. An angiogram showed 98% occlusion of his left coronary artery. His full lab profile is in **APPENDIX B**.

Exactly how to compute Paul's Ejection Fraction, and how each therapy's costs are modeled year over year, are fixed in **APPENDIX D** — use those conventions, or your numbers won't match anyone else's.

The vocabulary and the "how to…" skills this case will ask of you are listed in **Appendix E** — that is where Challenge 1 sends you.

---

## Dilemma

You are Dr. Hotchkiss.

Do you:

**A.)** Recommend the medical treatment only (MT) therapy **OR**

**B.)** Recommend the medical treatment + CABG therapy

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — Paul's 5-year survival rate for each therapy**, from the real trial results (Appendix A), and how much higher CABG's survival rate is than MT's, in percentage points.
- **D2 — Paul's Ejection Fraction**, computed from his own stroke volume and end-diastolic volume (Appendix B), expressed as a percent.
- **D3 — Paul's total expected expenses for each therapy**, after Year 1, Year 2, Year 3, Year 4, and Year 5 (Appendix C).
- **D4 — The slope and y-intercept of each therapy's 5-year cost line** from your Year 1-5 totals, and what each one means for Paul in plain English.
- **D5 — A recommendation** weighing survival rate, Ejection Fraction, and total cost.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A: The STICH Trial — Real Outcomes at ~5 and ~10 Years

**Study:** Comparison of Surgical and Medical Treatment for Congestive Heart Failure and Coronary Artery Disease (ClinicalTrials.gov Identifier: **NCT00023595**). **Sponsor:** Duke University. **Collaborator:** National Heart, Lung, and Blood Institute.

The study randomized patients with CAD, reduced heart function, and congestive heart failure to medical therapy only (MT) or medical therapy plus bypass surgery (CABG), and tracked all-cause mortality over time. The trial's own design only compared MT and CABG — it did not include a stenting (angioplasty) arm, because it specifically enrolled patients whose disease pattern made them candidates for bypass surgery. This case follows the trial's own real comparison and does not introduce a third option the trial itself never tested.

| Follow-up | MT mortality | CABG mortality |
|---|---|---|
| ~5 years (primary report, median follow-up 56 months) | 41% | 36% |
| ~10 years (extended follow-up, median 9.8 years) | 66.1% | 58.9% |

---

## Appendix B: Paul Cadenson — Patient Profile

57-year-old male. Pre-diabetes (HgA1C 6.4). Class I obesity (BMI 31). Family history of premature CAD. Daily tobacco smoker (1/2 pack/day for 35 years). Blood pressure 145/60 at his last two visits. Angiogram showed 98% occlusion of the left coronary artery. E/A ratio at his last two lab visits: 2.47 and 2.468.

**Stroke Volume (SV): 72.5 mL. End-Diastolic Volume (EDV): 228.6 mL.**

---

## Appendix C: Treatment Cost Figures

The original case materials did not include cost data, so the figures below are a disclosed, stated modeling convention, not sourced from the original trial.

**Medication Only (MT):** $450 per month, every month, for as long as Paul is on the therapy.

**Medication + CABG:** a one-time surgery cost of $85,000 in Year 1, plus $150 per month in follow-up medication starting immediately.

---

## Appendix D: Modeling Assumptions

**Assumption 1 — Ejection Fraction.** Ejection Fraction is calculated as Paul's stroke volume divided by his end-diastolic volume (Appendix B), expressed as a percent: EF = SV / EDV.

**Assumption 2 — Cost figures.** Appendix C's cost figures are a disclosed modeling convention (see Appendix C), not data from the original trial. Treat MT as a flat $450/month with no cost in Year 0. Treat CABG as a one-time $85,000 charge that lands entirely in Year 1, plus $150/month in follow-up medication starting in Year 1 and continuing every year after.

**Assumption 3 — Cumulative cost as a line.** Each therapy's cumulative cost, plotted against the year number (1 through 5), forms a straight line: cost = (yearly rate) x (year) + (fixed cost, if any). The yearly rate is the line's slope; the fixed cost that doesn't depend on the year is its y-intercept.

---

## Appendix E: "How To…" Math Questions To Research

**Vocabulary**

Percent · Ratio · Slope

**How to…**

- How to convert numbers to percents
- How to multiply decimal numbers
- How to add decimal numbers
- How to identify the slope of a line given a set of data, or a graph of a line of a set of data, or its linear equation
- How to compare two or more values
