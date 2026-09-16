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

---

## Part 6

# 🖼️ Images to Use

What makes a good image for the Multimodal Task

The image is the foundation of every task. A great prompt with a weak image fails; a good image makes adversarial, expert-grade questions possible. Use this page to decide whether an image is worth building a task around.

-   The maximum number of images that can be used per task is 5.
-   When adding multiple images, the numbering/naming scheme of the images MUST match how you refer to them in the prompt.
-   Images must be JPEG or PNG format.
-   Make sure that the image is at a resolution that allows a HUMAN reviewer to obtain the correct answer. Do not use screenshots when you are in Dark Mode making text difficult to read (particularly colored text).

## Image Requirements

-   **Mathematical images only.** Images must be mathematical images of the kind that appear in maths literature, not general images: graphs, Hasse diagrams, Kripke structures, curves, surfaces, manifolds, knots and links, statistical plots. Common tools: Desmos, GeoGebra, Graphviz.
-   **High quality only.** No blurry photos, poor screenshots, low-resolution copies, or bad hand-drawn images.
-   **Crop tightly.** Use only the part of the figure you need, not a whole paper or chapter.
-   **Format.** Only jpg and png are allowed.
-   **No transparency.** A png must not have a transparent background. Convert to jpg if it does.
-   **One task per image.** Each image may be used in only one task. Cropping, resizing, recolouring, relabelling or redrawing the same underlying figure does not make it a new image. You can attach up to 5 images to a prompt.
-   **Not OCR.** The model failure must come from the rich visual content of the image, not from OCR. Do not use an image that is only a text block, formula, matrix or simple table.

## Examples of invalid prompts

![Four invalid math multimodal prompt examples](https://project-lumiere-instructins.learn.joinhandshake.com/images/math-invalid-examples.png)

Four failure reasons illustrated here: the image is OCR-only, the image is just a table of data, the image is blurry, and the image is not necessary to answer the prompt.

## Where the image should come from

★ Top priority

✅

### Strongly preferred: figures you create yourself

**Figures you build yourself** — plots, diagrams, graphs, and geometric constructions made for a problem you designed — are the single best source. They're original, license-clean, and rich with adversarial potential. Record as _"Original — self-authored figure"_ and type N/A for URL/DOI and license.

✏️

**Annotation rule:** what we exclude are _artificial digital annotations_ — arrows, circles, boxes, text callouts, or highlighting added to the image after capture. Native on-image elements produced by the instrument or the preparation itself are permitted and can be preserved.

🟡 Acceptable

Open scientific sources with a clear commercial-reuse license: **CC BY 4.0/3.0/2.0**, **CC BY-SA**, or **CC0**. Source must be peer-reviewed and published.

🚫 Prohibited

No clear license, CC BY-NC, CC BY-ND, paywalled material without permission, and **any BioRender figure** (hard block).

### Image quality standards

-   Use original resolution. Avoid screenshots of screenshots. Only PNG and JPEG are allowed.
-   Preserve all on-image labels (axis labels, lane labels, scale bars, color legends). Do not crop them out.
-   Do not enhance, sharpen, or color-correct beyond what was applied in the original capture. Real artifacts are part of the signal we want to test.
-   Avoid images with transparent backgrounds.New

## License quick reference

| Source / License | Allowed? | Notes |
| --- | --- | --- |
| Original — self-authored figure | Yes | Strongly preferred. Figures, plots, and constructions you made yourself are ideal. |
| CC BY 2.0/3.0/4.0 | Yes | Free to use, share with attribution. Do not modify the image itself. |
| CC BY-SA | Yes | Free to use; derivatives must use the same license. |
| CC0 | Yes | Public domain. |
| CC BY-NC / -ND / -NC-ND | No | Non-commercial or no-derivatives restrictions — not usable. |
| All Rights Reserved | No | Default when no license is stated. Exclude. |
| BioRender-generated figures | No | Hard block, even if the surrounding paper is CC BY. |

**Note:** You may use images that you personally created for a research paper. In these instances, the image is classified as original and is approved for prompt creation.

### Transcription of the attached "Examples of invalid prompts" figure

(My reading of the image supplied with Part 6. Four panels, each an image +
prompt + reason it is invalid. Flagged as a transcription, not source text.)

| # | Image content | Prompt | Invalid because |
| --- | --- | --- | --- |
| 1 | The typeset equation $x^4 - 2x^2 + 1 = 0$, nothing else | "Find the real roots of the equation in the attached image." | OCR |
| 2 | Two-row table — $x$: 0, 1, 2, 3 and $f(x)$: 1, 2, 4, 8 | "Calculate the value of $f(4)$ based on the table in the attached image." | Table of data |
| 3 | A low-resolution red parabola on a grey grid, vertex near $(0,-2)$ | "Find the equation of the red parabola in the attached image." | Blurry image |
| 4 | Right triangle $ABC$, right angle at $A$, drawn unlabelled apart from vertex letters | "The image shows a right triangle $ABC$ such that $\angle A = 90^\circ$, $AB = 3$ and $BC = 5$. What is the area of the triangle?" | Image is not necessary |

The second attached screenshot shows the same figure inside its "Examples of
invalid prompts" panel on the source page; it carries no additional content.

<!-- end Part 6 -->

---

## Part 7

# ✍️ Writing the Prompt

A good prompt is a question that an expert can answer confidently from the image and that a strong vision-language model gets wrong, with a clear chain of reasoning available to the human grader.

-   **Image-dependent.** The question must require reading the image. If it can be answered from the text of the prompt alone, it is not appropriate.
-   **Specific and unambiguous.** Spell out conventions (e.g. "state the answer to 3 significant figures", "count only items fully inside the marked region"). For prompts that require reading/estimating values off of a graph, you must specify the rounding convention (e.g. "for values read off of the graph, round up to the nearest tick mark")
-   **Expert-grade.** Require mathematical domain knowledge at undergraduate level or above.
-   **Single canonical answer.** The prompt should have a single verifiable answer that any expert in the field would be able to arrive to. Avoid open-ended questions.

When choosing what to ask, deliberately target reasoning patterns models struggle with:

The first five below are the most common in Maths.

Connectivity / topology errorMost common in Maths

Misreads what connects to what, or how elements are configured: wrong vertex adjacency in a graph, misread order relations in a Hasse diagram, how a curve wraps around a surface.

Geometric relation errorMost common in Maths

Misreads configuration in figures: parallelism, perpendicularity, tangency, collinearity, inside vs outside a region, occluded edges in 3D projections.

Data extraction errorMost common in Maths

Wrong information pulled from a chart: wrong series mapped to the legend, bar height misjudged, wrong interpolation between gridlines. Reports the blue curve's peak when asked about the dashed one.

Figure-based quantitative estimation errorMost common in Maths

Errors counting or measuring off the image: grid squares, lattice points, spectral peaks; also treating a "not to scale" schematic as measurable.

Label-element or axis mis-bindingMost common in Maths

Reads every label correctly but attaches it to the wrong object.

Scale and unit misread

Misinterprets the plot frame: log vs linear, tick spacing, non-zero origin, secondary y-axis, axis units, scale bar.

Direction and sign-convention error

Misreads arrows and orientation: force or field direction, coordinate handedness, clockwise vs counterclockwise, slope field direction.

Unextracted given / prior override

The figure carries a value or condition available nowhere else and the model omits it, substitutes a plausible number, or answers about a canonical textbook figure it assumed instead of the one shown.

Prompt length is limited to 2000 characters.

The model's knowledge cutoff is December 31st 2025. Do not submit prompts that require knowledge past this date.

A prompt that depends on information published after this date will fail because the model has not seen it, not because it misread the image/makes a reasoning error — which is not the failure mode this project collects.

The step-by-step is the bridge between the image and the GTFA. A grader should be able to follow it without re-deriving the mathematics from scratch.

-   **Number steps.** Use _Step 1, Step 2, …_ (or 1), 2), …) — be consistent within a task.
-   **Start from the image.** The first one or two steps should anchor the answer in concrete visual evidence ("Note which vertices are joined by an edge, and which rows the labels sit in", "Read the coordinates of the marked points off the gridlines").
-   **Bring in the mathematics explicitly.** Name the theorem, definition or convention the step depends on.
-   **Show the working.** Write out the substitutions and intermediate values, not just the result.
-   **Close with the answer.** The final step should resolve to the GTFA verbatim.

Write the answer as it should appear if the model produced a verbatim correct response. An acceptable GTFA is a number, word, short phrase, or ordered/unordered list. **GTFA should never be a long sentence that can be written in multiple ways** — this is a sign of an open ended question.

Examples

-   A short ordered list of values

The description must be at least 200 words and carry enough detail that a reader could derive the final answer from the prompt and the description alone, without seeing the image. Describe what is there — do not state the final answer itself.

-   **Modality.** State what the figure is and how it was produced — for example a plotted function, a Hasse diagram, a knot projection, a 3D surface render — plus the panel layout where relevant.
-   **Content.** Describe what is visible in the field: structures, shapes, arrangement, and how panels relate to each other.
-   **Quality.** Comment on resolution, line weight, label legibility, and whether anything in the figure is cropped or obscured.
-   **Artifacts.** Note anything that could be mistaken for meaningful content — rendering artefacts, overlapping labels, aliasing on curves, or gridlines that could be read as data.
-   **Annotations.** State explicitly whether labels, arrows, numbers, scale bars, or captions are present.
-   **Do not give away the answer.** The description must not state or imply the GTFA.

-   Provide **five distractors**.
-   None of the distractors can be the GTFA.
-   Each distractor must be unique (i.e. do not duplicate any of the distractors).
-   Every distractor should be **plausible to a non-expert and dismissable by an expert**. Distractors that are obviously wrong waste a slot and lower the difficulty.
-   Lean on common reasoning errors: axis flips, miscounts off by one bin, plausible-sounding alternative explanations that fail on a specific detail.
-   Anchor distractors to errors models tend to make. If you've already seen a model fail in a related task, mine that failure for distractor ideas.

⚠️ Required note above the distractor list

"Distractors (incorrect answers only). Note that in testing we provided the model all potential answers, including the GTFA."

Please note that the official cut-off date for published references is **December 31, 2025**. If any references are utilized within the golden solution, they must be cited in two places: the designated reference box and at the end of the golden solution itself.

<!-- end Part 7 -->

---

## Part 8

# ⚠️ Quality Bar & Common Pitfalls

## 🎯 Hold the Bar — every task must satisfy:

-   A peer in your field can answer the question from the image without seeing your solution.
-   The step-by-step solution, read alone, justifies the GTFA from the image plus assay knowledge.
-   Each distractor maps to a specific plausible error.
-   The model fails, and you can name the failure mode in one sentence.

## Common Pitfalls

1

### Writing the prompt as an explicit multiple-choice question

Explicit multiple-choice prompts are disallowed. Do not present the responder with a list of terms, or a set of labelled images/panels, and ask them to pick one option. The prompt must ask for the answer directly, with a single canonical answer the responder has to derive from the image.

2

### Asking a stacked question

A prompt must test one analysis. Do not bundle two different types of analysis into a single question — whether they are performed on the same image or across several images. If two distinct analyses are needed, split them into separate tasks.

3

### Writing a pure counting question

Counting can be part of a task, but it cannot be the whole task. A prompt whose only demand is "how many X are visible" is disallowed — the count must feed a further judgement, classification, or quantitative conclusion the responder has to derive from the image.

4

### Mixing observation and interpretation in the early solution steps

The opening steps should record what is visible. Keep interpretive claims out of them and place the reasoning in the later steps of the step-by-step solution.

5

### Prompts that can be answered from the image or figure type alone

If a reader can answer your question without ever looking at the image, the prompt isn't image-dependent and isn't testing what we care about.

6

### Distractors an undergraduate would dismiss in five seconds

Raise the floor on plausibility. Every distractor must be plausible to a non-expert and dismissable only by an expert. Anchor them to specific reasoning errors models actually make.

7

### Skipping the arithmetic in the step-by-step on quantitative tasks

Show the dilution math, the per-corner average, the unit conversion. Reviewers and graders need to follow your numbers end-to-end.

8

### Delivering a task the model got right

We are building an adversarial set; passing tasks are not the deliverable. If you cannot make it fail, redesign the prompt to target a tighter failure mode, swap in a harder image, or retire the task.

9

### External images that turn out to be license-restricted

Licensing is the single most common reason a delivered task is rejected. Verify rights before authoring the task around the image. If you cannot find clear license info, treat it as All Rights Reserved and exclude.

10

### Using BioRender (or similar) figures

Any figure created with BioRender — even inside a CC BY paper — is a hard reject. The same applies to other non-commercially licensed creation tools.

11

### Assuming open access means free to reuse

Free reading access does not imply commercial reuse rights. Always verify the specific Creative Commons designation. Image license can also differ from paper license — check the figure caption.

12

### Cropping out on-image critical annotations

Preserve all axis labels, lane labels, scale bars, color legends, and MW ladder markings. These are part of the visual reasoning the task tests.

<!-- end Part 8 -->

---

## Part 9

> **NOTE ON FIDELITY:** this part arrived with inline mathematics stripped out.
> Element names, point labels, relation lists and the quantities being asked for
> are missing (they appear as empty gaps before punctuation). The referenced
> images were not attached. Recorded below exactly as received; see the
> "Known gaps" subsection at the end for the specific losses.

# 🥇 Golden Examples

Two complete golden example tasks for the mathematics domain, paired with their images.

1

## Golden Example 1: Order Theory — Hasse diagram

### Image

![Hasse diagram of a partially ordered set](https://project-lumiere-instructins.learn.joinhandshake.com/images/math-golden-1-hasse.png)

The image represents the Hasse diagram of a partially ordered set. What is the width of the poset, namely, the maximum cardinality of its antichains?

The image represents the Hasse diagram of a poset, which has distinct elements , , , , , and . The letters label the rows from bottom to top, and subscripts increase from left to right. The strict order on the poset is the transitive closure of the relations below. A set on either side of a comparison means that the comparison holds for each member of that set. In particular, and are isolated.

2

## Golden Example 2: Topology — curve on a surface

### Image

![Hourglass-shaped surface S with a closed red curve C drawn on it](https://project-lumiere-instructins.learn.joinhandshake.com/images/math-golden-2-surface.jpg)

Consider the surface and the red curve on the surface given in the image attached. If is the complement of in , what is the rank of the zeroth homology group of ?

The image shows a smooth, light-blue, hollow, hourglass-shaped surface , with wide circular rims at the top and bottom and a narrower waist. It consists only of the tube's lateral wall, with neither end capped; topologically, it is an annulus. A vertical axis labeled passes through its center but is not part of the surface or curve. A single closed red curve lies on , away from both rims. Solid arcs lie on the visible front, and dashed arcs lie on the hidden back; the dashes do not represent gaps. The curve has exactly two genuine transverse self-intersections: an upper solid-solid crossing on the front, denoted here by , and a lower dashed-dashed crossing on the back, denoted by . Neither crossing represents an overpass or underpass. The arrangement can be described precisely as a connected graph with vertices and four edges. One edge forms a loop based at : it rises along the front, passes around the back along the upper dashed arc, and returns to . Another forms a loop based at : it descends along the back, passes around the front along the lowest solid arc, and returns to . Each loop winds once around the tube. The remaining two edges connect to , passing around the left and right sides, respectively. All four edge interiors are mutually disjoint, and each vertex has four incident branches. There are no additional crossings or red components. The complement removes every solid and dashed red arc, including both intersection points; the surface's rims remain.

## A bad example and how to fix it

Bad

![Unlabelled red curve through points A, B and C](https://project-lumiere-instructins.learn.joinhandshake.com/images/math-bad-example.png)

Prompt: Let be the graph of the red curve in the image that passes through the points . What is ?

Good

![Labelled red parabola with axes and integer-coordinate points A, B and C](https://project-lumiere-instructins.learn.joinhandshake.com/images/math-good-example.png)

Prompt: Let be the graph of the red parabola in the image that passes through the points . The coordinates of these points are integers. What is ?

The fix: the good version names the curve type and pins the points to integer coordinates, so the answer is unique.

### Known gaps in Part 9 (to be filled from the source)

Golden Example 1 (Hasse diagram):
-   Names of the seven distinct elements (stripped: "distinct elements , , , , , and").
-   The entire list of order relations whose transitive closure defines the poset
    ("the transitive closure of the relations below" — no relations followed).
-   Which two elements are isolated ("In particular, and are isolated").
-   The GTFA (the width) is not stated.
-   The image itself was not attached.

Golden Example 2 (curve on a surface):
-   Symbols for the surface, the curve, the complement and the axis.
-   The number of vertices ("a connected graph with vertices and four edges").
-   Names of the two crossing points (context suggests two labels used as
    "based at ..." throughout).
-   The GTFA (rank of the zeroth homology group) is not stated.
-   The image itself was not attached.

Bad / good example pair:
-   The name of the graph/curve and the point labels ("passes through the points .").
-   The quantity being asked for ("What is ?").
-   Both images were not attached.

<!-- end Part 9 -->

---

## Part 9 (addendum) — images received, gaps partially closed

Three of the four Part 9 images were attached directly to the conversation
(the network egress proxy blocks the source host, so they could not be
fetched). Recorded below is what could be read off them.

### Bad / good example pair — GAPS NOW CLOSED

Both prompts are fully legible in the attached screenshot:

-   **Bad:** "Let $y = f(x)$ be the graph of the red curve in the image that
    passes through the points $A, B, C$. What is $f(4)$?"
    Figure: a red upward-opening curve on a plain grid. No axis labels, no tick
    marks, no marked origin. Points $A$ (upper left, on the curve), $B$ (at the
    minimum) and $C$ (upper right, on the curve) are lettered but not drawn as
    dots, and their coordinates are not pinned down.
-   **Good:** "Let $y = f(x)$ be the graph of the red parabola in the image that
    passes through the points $A, B, C$. The coordinates of these points are
    integers. What is $f(4)$?"
    Same curve, but the axes are labelled $x$ and $y$, the origin is labelled
    $O$, unit tick marks labelled $1$ appear on both axes, and $A$, $B$, $C$ are
    drawn as filled dots on the curve.
-   Caption: "The fix: the good version names the curve type and pins the points
    to integer coordinates, so the answer is unique."

### Golden Example 2 (hourglass surface) — PARTIALLY CLOSED

Legible from the image: the surface is labelled $S$ (upper right), the closed
red curve is labelled $C$ (lower front), and the vertical axis is labelled $z$
(arrowhead at top, drawn through the interior and protruding below). The
surface is a light-blue hyperboloid-like hourglass, uncapped at both ends — the
inner wall is visible through the top rim. Solid red arcs run on the visible
front, dashed red arcs on the hidden back. Two transverse self-intersections are
visible: an upper solid-solid crossing on the front, and a lower dashed-dashed
crossing on the back. This matches the prose description, which also fixes the
stripped vertex count: the curve is a connected graph with **2 vertices** and
four edges (the two crossing points, each with four incident branches).

Still missing: the two symbols used for the crossing points, and the GTFA.

### Golden Example 1 (Hasse diagram) — STILL OPEN

The image carries **no labels at all**: it is bare black vertices joined by blue
segments. The element names described in the prose ("the letters label the rows
from bottom to top, and subscripts increase from left to right") are assigned by
the description, not drawn on the figure. The relation list therefore cannot be
recovered from the image — it was prose, and it is gone.

Structural read of the figure, offered with explicit low confidence on the
counts: roughly six horizontal levels, on the order of forty vertices, densely
connected, with edges that frequently cross between levels. One vertex on the
bottom level has a conspicuous fan of several edges running up and to the right.
At the bottom right there are **exactly two vertices with no incident edges** —
this corroborates the prose sentence "In particular, and are isolated."

Reading the exact adjacency of this figure by eye is not reliable, and no
adjacency list is asserted here. That difficulty is the point of the example:
it targets the connectivity/topology failure mode listed first in Part 7.

Still missing: the element naming scheme, the full relation list, and the GTFA
(the width of the poset).

<!-- end Part 9 addendum -->

---

## Part 9 (addendum 2) — third-party image analysis, assessed

The user supplied an external analysis of the three Part 9 images (produced by
another model). Assessed claim by claim below. Recorded because one gap is
closed by it and because two of its claims should NOT be carried forward.

### Bad / good pair — accepted, GTFA recovered

Coordinates read as $A(-2, 1)$, $B(0, -1)$, $C(2, 1)$. These are mutually
consistent (symmetric about the $y$-axis, vertex on the axis) and agree with the
figure as far as it can be read. Deriving:

Vertex at $B(0,-1)$ gives $f(x) = ax^2 - 1$. Substituting $C(2,1)$:
$1 = 4a - 1 \implies a = \tfrac{1}{2}$, so $f(x) = \tfrac{1}{2}x^2 - 1$ and
$f(4) = \tfrac{1}{2}(16) - 1 = 7$.

**GTFA for the "good" example: $f(4) = 7$.** Arithmetic verified. Caveat: this
rests on coordinates read off the plot, not on source text.

### Golden Example 2 — REJECTED as a description of this task

The external analysis frames the figure as "a geodesic on a surface of
revolution" and develops Clairaut's relation $r(z)\sin\alpha(z) = $ const,
turning points and caustics, concluding the curve "oscillates indefinitely
between two parallel latitudes." Three problems:

1.  **It misses a self-intersection.** It reports the curve "intersecting itself
    on the front face" — one crossing. The playbook prose states there are
    exactly two genuine transverse self-intersections: an upper solid-solid
    crossing on the front AND a lower dashed-dashed crossing on the back. The
    second is what makes the curve a graph with 2 vertices and 4 edges.
2.  **"Oscillates indefinitely" contradicts the source.** The prose says "a
    single closed red curve." A closed curve does not oscillate indefinitely.
3.  **The geodesic framing is imported, not observed.** Nothing in the task
    concerns geodesics. The question asks for the rank of $H_0$ of the
    complement $S \setminus C$ — a question about how many pieces the curve cuts
    the annulus into. Clairaut's relation has no bearing on it.

This is an instance of the "unextracted given / prior override" failure mode
catalogued in Part 7: the figure resembles a standard textbook geodesic
illustration, and the analysis answered about the remembered figure rather than
the one shown. Useful as a specimen; not usable as a description.

### Golden Example 1 — unresolved disagreement on the vertex count

The external analysis states 35 vertices across roughly six tiers. An
independent read of the same figure gave roughly forty. Neither count is
verified, and they disagree. **No vertex count should be relied on** until it is
confirmed from the source text.

Agreed points: roughly six tiers; no horizontal intra-level edges; a bottom-tier
vertex emitting a fan (external analysis says four edges) up and to the right;
exactly two isolated degree-zero vertices at the bottom right.

The analysis additionally frames the figure as a causal set from discrete
spacetime physics. This is speculation: the playbook identifies it as a Hasse
diagram of a poset, and the task asks for the width (maximum antichain
cardinality). The causet reading adds nothing and should not be carried forward.

<!-- end Part 9 addendum 2 -->

---

## Part 9 (addendum 3) — second external analysis, both answers fail verification

A follow-up external analysis supplied a vertex census and edge list for Golden
Example 1 (claiming width $= 16$) and an answer for Golden Example 2 (claiming
$\operatorname{rank} H_0(S \setminus C) = 3$). Both were checked. Both fail.

### Golden Example 2: the claim $\operatorname{rank} H_0 = 3$ is inconsistent

Compactly supported Euler characteristic is additive:
$\chi_c(S) = \chi_c(C) + \chi_c(S \setminus C)$.

$S$ is a compact annulus (the prose states the rims remain), so $\chi_c(S) = 0$.
$C$ is a graph with $V = 2$, $E = 4$, so $\chi_c(C) = -2$. Hence

$$\chi_c(S \setminus C) = 0 - (-2) = 2.$$

The claimed decomposition is a top cap, a bottom cap and a bounded central
ribbon. The two caps are half-open annuli, each with $\chi_c = 0$; a ribbon is
an annulus ($\chi_c = 0$) or a disk ($\chi_c = 1$). The largest total those three
can reach is $1$, not $2$. **Three components is impossible.**

Reading the regions off the stated edge structure instead: the loop based at $p$
and the loop based at $q$ each wind once around the tube, so each is essential
and each separates. The two remaining edges run from $p$ to $q$ around the left
and right sides, cutting the band between the two loops into two pieces. That
gives

1.  the region above the $p$-loop (half-open annulus, $\chi_c = 0$),
2.  the region below the $q$-loop (half-open annulus, $\chi_c = 0$),
3.  and 4. two open disks between them ($\chi_c = 1$ each).

Total $\chi_c = 0 + 0 + 1 + 1 = 2$, matching. **Rank $H_0 = 4$**, derived from
the prose description rather than from the source, so still to be confirmed.

### Golden Example 1: the claim width $= 16$ contradicts its own edge list

Collecting every element that appears on the left of some relation $u \prec v$
in the supplied edge list gives 25 non-maximal elements:

$B_1..B_5, B_{\text{hub}}, L_1, L_3, L_4, L_5, L_6, K_2, K_3, K_5, K_7, K_8,
N_{3,1}, N_{3,2}, N_{3,3}, N_{3,4}, N_{3,5}, N_{3,7}, J_1, J_2, J_3$

With 42 vertices that leaves **17 maximal elements**, not the 15 claimed. The
two omissions are:

-   $K_1$ — receives $B_1 \prec K_1$ and $B_2 \prec K_1$, and never appears on
    the left of any relation.
-   $L_2$ — receives $B_3 \prec L_2$ and $B_4 \prec L_2$, and never appears on
    the left. The analysis's own prose calls it a "zigzag peak," which is
    precisely a maximal element.

Applying the analysis's own expansion step (replace $A_0$ with its two lower
covers $N_{3,5}, N_{3,7}$, which are below nothing else in the set) gives an
antichain of size $17 - 1 + 2 = 18$, verified pairwise incomparable. So on the
supplied data the width is **at least 18**, and 16 is wrong regardless of
whether the edge list itself is accurate.

Separately, the closing appeal is circular: "By Dilworth's theorem, 16 disjoint
chains cover the 42 vertices, confirming the width is strictly 16." Dilworth's
theorem *states* that the minimum chain cover equals the width; invoking it
without exhibiting the chain cover proves nothing. An explicit cover by $k$
chains would bound the width above by $k$; none was given.

### On the vertex count itself

The count moved from 35 to "exactly 42" only after an independent read here
described the figure as having "roughly forty" vertices. That is consistent with
anchoring to the stated estimate rather than with a recount, so the agreement is
not independent corroboration. **No vertex count, edge list or width should be
treated as established** until confirmed from the source text.

<!-- end Part 9 addendum 3 -->

---

## Part 10

# 📚 Helpful Resources

Last updated: Sep 2, 2026 · External references for sourcing images and authoring tasks

These are optional aids, not a substitute for the playbook. Your own lab images remain the strongly preferred source — use the links below when you need a license-clean external image or a quick refresher on nomenclature, grading criteria, or occupation codes.

## Open image repositories

Searchable sources of license-clean laboratory and clinical imagery.

-   [BioImage Archive (EMBL-EBI)](https://beta.bioimagearchive.org/bioimage-archive/)

    Deposited biological imaging datasets; check each study's license.

-   [Figshare](https://figshare.com/)

    General research data repository; filter for CC BY / CC0 items.

-   [Harvard Dataverse](https://dataverse.harvard.edu/)

    Datasets with per-deposit licensing; confirm terms before use.

-   [Image Data Resource (IDR)](https://idr.openmicroscopy.org/)

    Published microscopy screens and imaging studies.

-   [PIDAR datasets (HPC4AI, Torino)](https://pidar.hpc4ai.unito.it/Datasets/Index)

    Pathology image datasets index.

-   [Kaggle: chromosome image dataset (karyotype)](https://www.kaggle.com/datasets/aliabedimadiseh/chromosome-image-dataset-karyotype)

    Karyotype images for cytogenetics tasks; verify the dataset license.

-   [NIH Open-i](https://openi.nlm.nih.gov/)

    Biomedical figures from PubMed Central; filter by license.

-   [PubMed Central (Open Access subset)](https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/)

    Peer-reviewed articles with CC BY / CC0 figures.

-   [Wikimedia Commons](https://commons.wikimedia.org/)

    Check the per-file license — many are CC BY-SA or CC0.

-   [The Cancer Imaging Archive (TCIA)](https://www.cancerimagingarchive.net/)

    De-identified pathology and radiology collections.

## Open Access Journals

Figures from open-access articles — always check the per-article license before use.

-   [PLoS](https://plos.org/)

    Most content is CC BY.

-   [Frontiers](https://www.frontiersin.org/)

    Open-access articles across life sciences.

-   [MDPI](https://www.mdpi.com/)

    Open-access journals; confirm the license line on each article.

-   [eLife](https://elifesciences.org/)

    Life-science research, typically CC BY.

-   [Nature (open access)](https://www.nature.com/openresearch/publishing-with-npj/)

    Only the open-access articles; subscription content is not usable.

## Licensing references

Use these to confirm an image is usable before building a task around it.

-   [Creative Commons license chooser & summaries](https://creativecommons.org/share-your-work/cclicenses/)

    What each CC license permits. NC and ND are not usable.

-   [CC0 public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/)

    Always acceptable; still record the source URL.

## Domain background

Refreshers for the subject areas in scope.

-   [O\*NET OnLine occupation search](https://www.onetonline.org/)

    Look up the exact occupation title and SOC code for the Profession field.

-   [ISCN karyotype nomenclature overview](https://en.wikipedia.org/wiki/International_System_for_Human_Cytogenomic_Nomenclature)

    Standard notation for cytogenetics answers.

-   [WHO / CAP grading & staging criteria](https://www.cap.org/protocols-and-guidelines)

    Use published criteria when a prompt asks for a graded call.

Reminder: BioRender figures are a hard block, and CC BY-NC / CC BY-ND material is never usable — regardless of where you found it.

<!-- end Part 10 -->

---

## Part 11

# 🧮 LaTeX & KaTeX Resources

External references for writing and checking LaTeX in your tasks

## KaTeX supported functions

Use this reference to check which LaTeX commands are supported by KaTeX.

[katex.org/docs/support\_table](https://katex.org/docs/support_table)

## Verify LaTeX rendering

Use this to write and verify your LaTeX renders correctly before submitting.

[stackedit.io](http://stackedit.io/)

## Handshake LaTeX master guide

This training document covers LaTeX formatting conventions for Handshake maths projects — inline and display math modes, fractions, matrices, align environments, spacing, punctuation, and more.

[Open the LaTeX master guide](https://drive.google.com/file/d/1daMIGwq-EWTKUkeB0PXlKJvna0p8nv-B/view?usp=sharing)

<!-- end Part 11 -->

---

## Part 12

# 🔍 Reviewing Guidelines

As a reviewer, you are responsible for maintaining the quality of the tasks that move through the pipeline. Use the knowledge you have as an expert and proficient tasker to identify issues in tasks and provide constructive feedback to fix them.

## 📋 Claiming Reviews

There is no reviewer claim sheet in this project. You can go to the Handshake AI dashboard → Project Lumiere → Available Tasks → set Stage to "Awaiting Review (Review 1)". This will show the tasks in the R1 layer that you can claim to review.

## 📝 How to Give Feedback

1.  Read through the task, then select the Add feedback icon on the relevant section and choose Major Issue, Minor Issue, Praise, or General Feedback.
2.  Write constructive feedback — copy the relevant error from the Error Classifications below, point to where it occurs in the task, and suggest how to correct it.
3.  If a minor error can be fixed in under 25 minutes and you're confident in the area, fix it yourself. Otherwise, send it back with feedback. When you fix a minor error to pass the task, leave a general comment noting what was corrected.
4.  Provide praise on good tasks.
5.  Select an appropriate quality score (1–5) for the task (see the rubric below).
6.  To approve, the task must have no major or minor errors.

![Feedback panel showing Major Issue, Minor Issue, Praise, and General Feedback options](https://project-lumiere-instructins.learn.joinhandshake.com/images/feedback-process.png)

Selecting a feedback type on a task.

## ⭐ Quality Score Rubric

Every reviewed task receives a quality score from 1 to 5. A score of 3 or above is passing.

Score

Verdict

Criteria

5

Pass — Excellent

No major errors and no minor errors. Task is delivery-ready with no fixes required.

4

Pass — Good

No major errors and 1–2 minor errors. Small corrections needed but the task is fundamentally sound.

3

Pass — Acceptable

No major errors and 3–4 minor errors. Passing threshold; requires fixes before delivery.

2

Fail

Contains a major error, OR more than 4 minor errors. Cannot pass — send back with feedback.

1

Fail — Flag

No effort or 3+ major errors. Very rare — flag immediately to a team lead.

## ⚠️ Error Classifications

Click on the error tag to copy it and paste on the feedback.

🚫

### Major Errors

-   Prompt has multiple correct answers
-   Prompt is incorrect or not suitable (asking for something impossible or not valid)
-   No or invalid image source for images extracted from online
-   Incorrect final answer
-   Final answer is not a single unambiguous answer
-   Final answer is a long sentence
-   Unclear image
-   Incorrect image format (not PNG or JPEG)
-   Heavily post-processed image (obvious color saturation due to editing or photographic manipulation)
-   Invalid license type - This only applies for images obtained from online - DO NOT MARK MAJOR ERROR for user's own images.
-   Invalid model failure
-   Incorrect task subtype
-   Not enough model failures
-   Other

⚠️

### Minor Errors

-   Model failure justification is incorrect or missing - Both general justification of multiple model failures or justification of a single model failure is accepted.
-   Step-by-step solution has partial or incorrect steps
-   Distractors are mismatched and do not align with the guidelines
-   Answer format (integer, decimal, etc.) or the number of decimal places selected is inaccurate
-   Poor grammar, spelling, or typos
-   Other

### 📌 Special Cases

-   Typos and grammatical errors in the prompt — Only send back tasks for this issue if the errors alter the meaning of the prompt and can lead to incorrect answers, or if there are a significant number of typos and grammatical errors that make the prompt look very poor quality.
-   Stacked questions — If a prompt asks multiple questions that require compounded answers, it is considered a stacked question and is not allowed (e.g., _"What is the antibiotic-resistant organism in the left plate, and what is the gram-positive bacterium in the middle plate?"_). A prompt must ask a single question with a single unambiguous answer. When in doubt, ask in the #lumiere-reviewer channel.

## ✅ Submission Checklist

0 / 18 checked

Image is consistent with the assigned task Supertype and Subtype.

Image is a PNG or a JPEG and not another image format.

All images embedded at original resolution and labeled "Image 1:", "Image 2:", …

On-image labels (axes, lanes, scale bars, ladders, legends) are preserved — not cropped.

"License:" row is filled in for every external image with license type, source URL/DOI, and any required attribution.

Original lab images marked as "Original — internal lab image".

License is one of CC BY 4.0/3.0/2.0, CC BY-SA, or CC0. No CC BY-NC, CC BY-ND, CC BY-NC-ND, or All Rights Reserved.

No BioRender figures (or other non-commercial creation tools).

Source article is peer-reviewed and meets the current project date cutoff.

Image has not been reused as the sole image in another task; if reused, it is combined with previously unused figures.

Prompt is image-dependent — cannot be answered from the experiment type alone.

Prompt is specific and unambiguous; conventions and options are spelled out.

Step-by-step solution is numbered, anchored in visual evidence, names the biology, shows arithmetic, and closes with the GTFA.

GTFA is written verbatim (not just a letter) and unambiguous in isolation.

Five distractors, each plausible to a non-expert but dismissible by an expert.

Both models failed.

"Failure reason:" is filled in with a 1–3 sentence diagnosis of the model error.

If the model got the task right on the first attempt: redesign, swap the image, or retire — do not deliver as-is.

<!-- end Part 12 -->
