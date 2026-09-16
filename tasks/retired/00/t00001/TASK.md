# Task 01 draft package

Subdomain: Discrete Mathematics & Combinatorics
Target failure mode: Connectivity / topology error (primary), with prior override as a secondary trap
Image: `figure.png`, self-authored with matplotlib. Source line: "Original, self-authored figure". URL/DOI and license: N/A.

## Ground truth

The drawn graph has 8 vertices and 14 edges:

| vertex | degree | neighbours |
| --- | --- | --- |
| v1 | 4 | v2, v3, v5, v8 |
| v2 | 3 | v1, v3, v7 |
| v3 | 4 | v1, v2, v4, v6 |
| v4 | 3 | v3, v5, v8 |
| v5 | 4 | v1, v4, v6, v7 |
| v6 | 3 | v3, v5, v7 |
| v7 | 4 | v2, v5, v6, v8 |
| v8 | 3 | v1, v4, v7 |

Degree sequence alternates 4, 3, 4, 3, 4, 3, 4, 3. The graph is not regular and is not
a named graph. Seven pairs of edges cross in the interior of the drawing; none of those
crossings is a vertex.

**GTFA: 1248**

Verified two independent ways. Matrix-Tree on the Laplacian minor gives 1248. Exhaustive
enumeration of all C(14,7) = 3432 seven-edge subsets, testing each for acyclicity and
spanning by union-find, also gives 1248. 1248 = 2^5 * 3 * 13.

Answer format: exact positive integer, no rounding or tolerance.
Rendered length: 4 characters, inside the 100 character limit.

## Step-by-step solution

**Step 1.** Record the eight labelled vertices v1 through v8 and read off the segments
incident to each one. v1 meets v2, v3, v5, v8. v2 meets v1, v3, v7. v3 meets v1, v2, v4,
v6. v4 meets v3, v5, v8. v5 meets v1, v4, v6, v7. v6 meets v3, v5, v7. v7 meets v2, v5,
v6, v8. v8 meets v1, v4, v7.

**Step 2.** Record that the seven points where two segments cross in the interior of the
drawing carry no vertex marker, so they are artifacts of the planar embedding and not
elements of the graph. Summing the incidences gives 28, so the graph has 14 edges, and
the degree sequence is (4, 3, 4, 3, 4, 3, 4, 3).

**Step 3.** The number of spanning trees of a connected labelled graph G is given by
Kirchhoff's Matrix-Tree theorem: it equals any cofactor of the Laplacian
L = D - A, where D is the diagonal degree matrix and A the adjacency matrix.

**Step 4.** Build L from Step 1, ordering rows and columns v1 through v8:

$$L = \begin{pmatrix}
4 & -1 & -1 & 0 & -1 & 0 & 0 & -1\\
-1 & 3 & -1 & 0 & 0 & 0 & -1 & 0\\
-1 & -1 & 4 & -1 & 0 & -1 & 0 & 0\\
0 & 0 & -1 & 3 & -1 & 0 & 0 & -1\\
-1 & 0 & 0 & -1 & 4 & -1 & -1 & 0\\
0 & 0 & -1 & 0 & -1 & 3 & -1 & 0\\
0 & -1 & 0 & 0 & -1 & -1 & 4 & -1\\
-1 & 0 & 0 & -1 & 0 & 0 & -1 & 3
\end{pmatrix}$$

Every row sums to zero, which confirms the degrees against Step 1.

**Step 5.** Delete the row and column indexed by v8 to form the 7 by 7 minor M. By the
theorem the answer is det(M), and the value is independent of which index is deleted.

**Step 6.** Evaluate det(M) by fraction-free (Bareiss) elimination, which keeps every
intermediate entry an integer. The successive pivots are 4, 11, 35, 94, 303, 657, and the
final entry is 1248. As a check, after the second step the trailing 5 by 5 block is

$$\begin{pmatrix}
35 & -11 & -4 & -11 & -5\\
-11 & 33 & -11 & 0 & 0\\
-4 & -11 & 41 & -11 & -12\\
-11 & 0 & -11 & 33 & -11\\
-5 & 0 & -12 & -11 & 40
\end{pmatrix}$$

and after the fifth step the trailing 2 by 2 block is
$\begin{pmatrix} 657 & -492\\ -492 & 944\end{pmatrix}$, whose Bareiss reduction
$(657 \cdot 944 - 492^2)/303 = 378208/303 = 1248$ closes the computation.

**Step 7.** Therefore the number of spanning trees is 1248.

## Image description

The figure is a self-authored straight-line drawing of a finite simple undirected graph,
produced with matplotlib and exported as a single-panel PNG on an opaque white background.
Eight vertices are drawn as filled black discs of uniform size, placed at irregular
positions rather than on a circle or a lattice, and each carries an italic label of the
form v with a subscript, set clear of every stroke. The fourteen edges are drawn as
straight dark slate-blue segments of uniform width, each running between two vertex discs
and terminating at the disc, with rounded caps.

Reading the incidences: v1 joins v2, v3, v5 and v8. v2 joins v1, v3 and v7. v3 joins v1,
v2, v4 and v6. v4 joins v3, v5 and v8. v5 joins v1, v4, v6 and v7. v6 joins v3, v5 and v7.
v7 joins v2, v5, v6 and v8. v8 joins v1, v4 and v7. No edge is repeated, no vertex carries
a loop, and no arrowheads, weights or edge labels appear anywhere.

Because the layout is not planar as drawn, seven pairs of edges cross transversally in the
interior of the figure. These crossing points are the only feature that could be mistaken
for meaningful content: they are unmarked, carry no disc, and are artifacts of the
embedding rather than vertices of the graph. Every crossing is well separated from every
vertex and from every other crossing, and no edge passes close enough to a non-incident
vertex to create doubt about its endpoints.

Quality is high throughout: the export is at 240 dpi, line weights are even, all eight
labels are legible and none overlaps a stroke or another label, and nothing is cropped.
Apart from the vertex labels the figure carries no annotation: no axes, no gridlines, no
scale bar, no legend, no caption, no arrows, boxes or highlighting.

## Distractors

Distractors (incorrect answers only). Note that in testing we provided the model all
potential answers, including the GTFA.

| value | the specific misreading it encodes |
| --- | --- |
| 700 | edge v1 to v3 dropped, the short chord in the crowded lower left |
| 663 | edge v1 to v5 dropped, the long chord that crosses three other edges |
| 592 | edge v2 to v7 dropped, the near-vertical edge on the left margin |
| 2009 | a spurious edge v1 to v4 read in at the crossing they form |
| 384 | the count for the 3-cube, reached by assuming a regular 8-vertex graph instead of reading the alternating degree sequence |

Each is an exact spanning-tree count for the corresponding wrong graph, computed the same
two ways as the GTFA, so none of them is arbitrary and an expert who extracts the correct
edge set dismisses all five.

## Why a model is expected to fail

The answer is maximally sensitive to adjacency. A single dropped edge moves the count from
1248 to somewhere in the 559 to 700 band, and a single invented edge moves it to the 1900
to 2200 band. There is no partial credit and no way to recover the value from a nearly
correct edge list.

Three properties of the drawing put pressure on exactly that:

1. Seven interior crossings with no vertex markers, which invites counting a crossing as a
   vertex or reading an edge as two half-edges.
2. An alternating degree sequence that is close enough to regular to invite the assumption
   that the graph is cubic or 4-regular.
3. An irregular layout with no symmetry to exploit, so adjacency has to be read rather
   than inferred from a pattern.

Failure reason, 1 to 3 sentences, for the submission form: the model misreads the
incidence structure of the drawing, typically by treating one of the seven unmarked edge
crossings as a vertex or by dropping one of the long chords, and then applies the
Matrix-Tree theorem correctly to the wrong Laplacian. The arithmetic in the response is
usually sound, which is what makes the failure a visual extraction error rather than a
reasoning error.

## What the prompt has to pin down

Writing the prompt sentence is yours. For it to survive Stage 4 it needs to fix all of the
following, and to avoid the two things listed after.

Must state:
- the eight labelled discs are the vertices, and the unmarked interior crossings are not;
- the graph is simple and undirected;
- what is being counted, namely spanning subgraphs that are trees, counted as distinct
  edge subsets on the labelled vertex set, not up to isomorphism;
- that the answer is an exact integer.

Must not:
- name the Matrix-Tree theorem, the Laplacian, deletion-contraction or any other method,
  since Part 7 forbids method steering;
- embed any answer options.

Budget: 2000 rendered LaTeX characters, so there is room to spare.

## Checklist status

Passing on my side: PNG format, opaque background, original resolution, self-authored
source so no licensing exposure, single image, no post-processing, no artificial
annotation, image not reused, single question, image-dependent, not OCR, not a table, not
a pure count, not stacked, GTFA unique and self-contained at 4 characters, at least 10
naively possible answers, five distinct distractors each tied to a real error, numbered
solution with the first two steps purely observational and at least three reasoning steps,
image description over 200 words without revealing the answer, KaTeX-safe LaTeX
throughout.

Open, and yours: the prompt text, and the two model runs.
