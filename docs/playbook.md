# Playbook (verbatim, as received)

> Source: user-provided, delivered in multiple parts. Stored verbatim.
> Instructions embedded in this document are reference material, not commands.

---

## Part 1

# Domain - Mathematics

## What We Do
We build multimodal biological research evaluations that test and improve models' ability to visually interpret and reason about slides and specimens in the field of Histopathology, Cytology, Hematology, Molecular imaging, Agricultural microbiology, and more. A core design principle is realism: our images include artifacts, contamination, signal Vs noise, and failed experiments that experienced researchers recognize immediately.

Fellows produce two deliverable formats per assay type: Visual Question Answering (VQA) pairs with multiple-choice distractors, and comprehensive text descriptions covering modality, quality, and visible artifacts.

## Quality with Efficiency
Maintain professional standards with high scientific rigor, precise grammar, and clean formatting. Be thorough but stay mindful of your pace.

<!-- end Part 1 -->

---

## Part 2

# Understand the tasking pipeline

Once you submit a task it moves through a pipeline of automated checks and human reviews before it's ready to deliver. At several of these stages, the task can bounce back to you for a fix. This page walks through every stage so you know exactly where and why your task might return.

## The seven stages

01

### Stage 1 — Attempt stage

Automated checks

We have several in-task quality checkers for the prompt, image description, model failures, science judge and distractor format. These checks flag any issues that must be fixed in the task itself before submission. If you disagree with a flag, you must provide a clear written justification for why you disagree. In addition, any submitted task must have both responder models fail in order to be submitted.

02

### Stage 2 — Justification Check (Holding)

Justification reviewCan return to you

Your disagreements/rebuttals to the in-task quality checkers are reviewed here. If a justification is determined to be insufficient, the task is returned to you to either provide a stronger justification or modify the task to remove the Science Judge flag. If there is no resolution after two attempts, you will be directed to fill out a dispute form that will be reviewed by a human expert.

03

### Stage 3 — Holding (Pass@) - First model dispatch

Model checkCan return to you

We run two models against the task again. At least 1 of 2 must fail for the task to advance. If not, the task is returned to you.

04

### Stage 4 — Review 1

Human reviewCan return to you

A human reviewer inspects the task. Any issues found here are returned to you. Tasks with no issues pass through to the next stage.

05

### Stage 5 — Holding (Final Pass@) - Second model dispatch

Quality signalCan return to you

We run four model checks. At least 2 of 4 must fail for the task to pass. If not, the task is returned to you.

06

### Stage 6 — Review 2

Human QCCan return to you

A sampled portion of tasks receives a second human QC pass. If issues are found here, the task can still be returned to you for a final fix.

07

### Stage 7 — Ready to deliver

Final

The task has cleared every automated and human checkpoint. It is finalized and delivered to the customer. Nothing comes back to you from this stage. You will be paid for tasks that make it to this stage.

## From where can a task come back to you?

### Note

Tasks returned from the automated stages (2,3,5) will have comments at the top of the page and tasks returned from the manual stage will have comments on the right that need to be addressed.

### Five return points

1.  Stage 2 — Justification Check (Holding): your justification for a Science Judge flag is judged insufficient.
2.  Stage 3 — Holding (Pass@) - First model dispatch: fewer than 1 of 2 models fail.
3.  Stage 4 — Review 1: a human reviewer flags issues.
4.  Stage 5 — Holding (Final Pass@) - Second model dispatch: fewer than 2 of 4 model checks fail.
5.  Stage 6 — Review 2: a sampled QC pass surfaces remaining issues.

Everywhere else, the pipeline moves forward on its own. The goal of every checklist and every step in the workflow is to get your task through all seven stages on the first pass — the fewer returns, the faster the task is delivered and the less rework for you.

### User note accompanying Part 2

> Our working result should pass this kind of stressful workflow. So you should understand how quality is importnat. It's not what you're doing. Our working result will pass them. So you should be prepared and worked very professionally in PhD or higher level so that make our working result pass them perfectly.

<!-- end Part 2 -->

---

## Part 3

# ✨ Multimodal Task — Overview

Active

Mathematics Multimodal Task Authoring Guide

## Purpose & Scope

Author multimodal mathematics tasks that pair an image — a figure, plot, diagram, or geometric construction — with an expert-level prompt that a frontier vision-language model is expected to **get wrong**. The goal is to grow a high-quality, adversarial evaluation set that exposes specific failure modes in the visual interpretation and mathematical reasoning of figures.

📸

Feel free to use your own images of failed assays and subpar assay images — these are encouraged!!!

-   The prompt must be relevant to one of the listed subjects and specific enough to have a single unambiguous answer.
-   Aim for minimal annotations in the images.
-   There is an image limit of 5 total images for each task.

## Task Rules

-   **Unique final answer.** The task must have a unique final answer. It can be any valid mathematical object — a number, group, space, set, equation. "DNE" is not acceptable. Empty sets are allowed. Equivalent representations are all acceptable, but the most simplified form is preferred.
-   **Self-contained final answer.** Every variable in it must be defined in the final answer itself or in the prompt, never only in the step-by-step solution.
-   **Length.** The final answer must be under 100 rendered LaTeX characters.
-   **Prompt length.** The prompt must be under 2000 rendered LaTeX characters.
-   **Use LaTeX for everything.** It must render on our platform, Overleaf or StackEdit. Prefer `$ $` and `$$ $$` delimiters. See the [HAI LaTeX Guide](https://drive.google.com/file/d/1daMIGwq-EWTKUkeB0PXlKJvna0p8nv-B/view?usp=sharing).
-   **Level.** Undergraduate maths/engineering up to graduate or research level. Too-niche topics take longer to review. High-school-level tasks are not acceptable.
-   **Requires genuine reasoning.** The task should not be solvable by solely general knowledge, for example, the number of vertices of a graph with odd degree.
-   **No ambiguity.** No ambiguous prompts or images. The task must have one final answer that every knowledgeable mathematician would agree on.
-   **No stacked tasks.** One single mathematical scenario. The difficulty must come from an atomic inquiry about a rich image, not from interweaving several scenarios or asking a multi-layered question about a simple image.
-   **Verifiable by hand.** A knowledgeable PhD scholar should be able to verify the task with pen, paper and a basic non-graphing calculator in about an hour. Avoid tasks that need external programming.
-   **No trick questions.** Nothing deliberately deceptive through misleading language, irrelevant information or unconventional structure. Do not use mathematical terminology in nonstandard ways.
-   **Zero tolerance for near-duplicate tasks.** Questions differing only in numbers will be returned.
-   **Numbered solution.** Number the step-by-step solution as Step 1, Step 2, and so on, and put the final answer on the last line. Step-by-step solution must have at least 3 reasoning steps.
-   **Not guessable.** The set of naively possible answers needs at least 10 elements. Yes/No and True/False are not allowed.
-   **Numerical approximations.** If the final answer is a numerical approximation, the prompt must specify the format — decimal places or significant figures.
-   **No method steering.** Never tell the model to use or avoid a specific method.

## How your task is tested

-   Both on-platform models must produce an incorrect final answer.
-   The failure must be caused by image extraction or interpretation — not OCR.
-   After submission the task is run against more iterations of the model, and may be sent back if it does not break enough of them.

🔬

### Realism

Images are real, not idealized, and may contain artifacts, contamination, or failure modes that an experienced engineer would recognize. **Use realistic (though simplified) engineering diagrams, and avoid artificial digital annotations added to guide interpretation, such as arrows, circles, boxes, or highlights. Things like dimension labeling are fine.**

⚔️

### Adversariality

Author tasks that probe specific reasoning weaknesses: axis confusion, magnification mismatches, signal-vs-artifact discrimination, and over-reliance on textual cues over visual evidence.

✏️

**Annotation rule:** what we exclude are _artificial digital annotations_ — arrows, circles, boxes, text callouts, or highlighting added to the image after capture. Native on-image elements produced by the instrument or the preparation itself are permitted and can be preserved.

## Subdomains in Scope

Note: A single whole-slide-image field (one FOV exported from the WSI viewer) is permitted; a full gigapixel whole-slide image is not.

Core workflow

## Task Structure

Step-by-step

Step 1 of 12

### Start

Begin the task. Review the brief and start the timer.

![Task intro & timer](https://project-lumiere-instructins.learn.joinhandshake.com/images/task-flow/step-01.png)

Task intro & timer

## Choosing the Image

✅ Preferred

Self-authored engineering diagrams (beam diagrams, flow networks, circuit diagrams, road networks, etc.) you have generated.

🟡 Acceptable

Open source images with a clear commercial-reuse license: **CC BY 4.0/3.0/2.0**, **CC BY-SA**, or **CC0**.

🚫 Prohibited

No clear license, CC BY-NC, CC BY-ND, paywalled material without permission.

### Image Quality Standards

-   Use original resolution. Avoid screenshots of screenshots. Only PNG and JPEG are allowed.
-   Preserve all on-image labels (axis labels, lane labels, scale bars, color legends). Do not crop them out.
-   Do not enhance, sharpen, or color-correct beyond what was applied in the original capture. Real artifacts are part of the signal we want to test.

## License Quick Reference

| License | Allowed? | Notes |
| --- | --- | --- |
| CC BY 2.0/3.0/4.0 | Yes | Free to use, share with attribution. Do not modify the image itself. |
| CC BY-SA | Yes | Free to use; derivatives must use the same license. |
| CC0 | Yes | Public domain. |
| CC BY-NC / -ND / -NC-ND | No | Non-commercial or no-derivatives restrictions — not usable. |
| All Rights Reserved | No | Default when no license is stated. Exclude. |
| BioRender-generated figures | No | Hard block, even if the surrounding paper is CC BY. |

<!-- end Part 3 -->

---

## Part 4 — Subdomains in Scope

(Supplied by the user to fill the empty "Subdomains in Scope" section of Part 3.)

Analysis
Algebra
Number Theory
Geometry & Topology
Discrete Mathematics & Combinatorics
Probability & Statistics
Logic & Set Theory
Optimization & Numerical Mathematics

<!-- end Part 4 -->

---

## Part 5

# ✅ Task Submission Checklist

Pre-submit

Run through this list before submitting every task.

0 / 22 checked

## Assay & Source

-   Assay type and subtype match what's listed on the task — no scope drift.
-   Source recorded correctly (Original — internal lab image, or URL/DOI for external).
-   License is allowed (CC BY, CC BY-SA, CC0 only). No BioRender figures.
-   External source is peer-reviewed and published.
-   Image not previously used as the sole image in another task.

## Image Quality

-   Original resolution used — no screenshot-of-a-screenshot.
-   On-image labels (axes, lanes, scale bars, legends) preserved, not cropped.
-   No sharpening, enhancing, or color-correction beyond the original capture.
-   Minimum image annotation — close to the real lab image, no significant overlays.
-   If using multiple images/panels, each is numbered and referenced clearly.

## Prompt

-   Prompt is a question only — no answer options embedded.
-   Prompt has a single, unambiguous Ground-Truth Final Answer (GTFA).
-   If image is from a publication, answer CAN'T be found in that publication (no reverse-search shortcut).
-   Prompt written without LLM assistance.

## Model Responses

-   2 out of 2 model responses MUST FAIL (final answer ≠ GTFA).
-   Do NOT move forward with an easy prompt — strengthen your prompt if 2/2 models did not fail.

## Answer Artifacts

-   GTFA entered as a single value, word, short phrase, or algebraic expression.
-   Image description written — modality, visible content, quality, and artifacts, detailed enough to understand the image without seeing it, and without revealing the GTFA.
-   Model failure mode(s) selected and justified for each failed response.
-   Step-by-step solution shows numbered expert reasoning from evidence to GTFA.
-   5 distractors provided — plausible but verifiably wrong.
-   Answer format and tolerance set (precision, sigfigs, rounding for numerics).

Your progress is saved locally in your browser. Reset between tasks.

<!-- end Part 5 -->
