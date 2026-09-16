# Task t00006 draft package

Subdomain: Algebra
Target failure modes: connectivity / topology error (primary), label-element mis-binding (secondary)
Image: `figure.png`, self-authored with matplotlib, opaque RGB PNG, 2882 x 1265.
Source line: "Original, self-authored figure". URL/DOI and license: N/A.

## What the figure is

The Auslander-Reiten quiver of the path algebra $kQ$ for $Q$ an orientation of the Dynkin
diagram $E_6$. Thirty-six vertices, one for each indecomposable module, labelled by
dimension vectors written as six-digit strings. Solid arrows are irreducible morphisms.
Dashed horizontal lines join $X$ to $\tau X$, the Auslander-Reiten translate.

## Ground truth

Let $T = M_1 \oplus M_2 \oplus M_3 \oplus M_4 \oplus M_5$ where the summands are the
indecomposables with dimension vectors

$$000110,\quad 001111,\quad 012101,\quad 111000,\quad 122101 .$$

**GTFA: 19**

That is $\dim_k \operatorname{End}_{kQ}(T) = \sum_{i,j} \dim_k \operatorname{Hom}(M_i, M_j)$,
with the matrix of Hom dimensions (rows indexing the source, in the order listed)

$$\begin{pmatrix}
1&1&1&0&1\\ 0&1&2&1&2\\ 0&0&1&2&2\\ 0&0&0&1&0\\ 0&0&0&2&1
\end{pmatrix},
\qquad \text{row sums } 4,\,6,\,5,\,1,\,3,\ \text{total } 19 .$$

### Why the obvious shortcut fails, which is the point of the task

For a hereditary algebra the Euler form gives
$\dim \operatorname{Hom}(M,N) - \dim \operatorname{Ext}^1(M,N) = \langle \underline{\dim} M,
\underline{\dim} N\rangle$, so the total dimension vector alone yields
$\langle d_T, d_T \rangle = 3$. Here $\dim \operatorname{Ext}^1(T,T) = 16$, so the Euler
form is short of the answer by 16. $T$ is deliberately **not** rigid: had it been a tilting
module the Ext term would vanish and the answer would be computable from the dimension
vectors without ever consulting the diagram. As it stands the Hom dimensions must be read
out of the arrow structure, which is what makes the figure load-bearing.

### Verification

Everything below is computed, not asserted.

1. **The diagram is correct.** The 36 knitted vertices reproduce the 36 positive roots of
   $E_6$ exactly. The arrow set was then checked against every mesh relation: for each
   non-projective $N$, $\underline{\dim}\,\tau N + \underline{\dim}\,N =
   \sum_{M \to N} \underline{\dim}\,M$. All 30 meshes hold. A knitting rule that failed
   this test was rejected.
2. **The modules are the right ones.** For each of the 36 positive roots a representation
   of that dimension vector was constructed and $\dim \operatorname{End} = 1$ verified,
   which by Schur's lemma confirms indecomposability and hence identifies it.
3. **The Hom dimensions are correct.** $\operatorname{Hom}(M,N)$ was computed as the
   solution space of $f_j M_a = N_a f_i$ over all arrows, by rank computation over two
   different large prime fields; all $36^2$ pairs agreed across both primes.
4. **Consistency.** $\dim \operatorname{Ext}^1$ was obtained as
   $\dim \operatorname{Hom} - \langle \cdot,\cdot\rangle$ and came out non-negative for all
   $36^2$ pairs, which it need not have done had anything been wrong.

Answer format: exact positive integer. Rendered length: 2 characters.

## Step-by-step solution

**Step 1.** Locate the five summands in the diagram by their dimension-vector labels:
$000110$, $001111$, $012101$, $111000$ and $122101$. Record their positions relative to the
dashed $\tau$-lines and the solid arrows leaving and entering each.

**Step 2.** Record the arrow structure around them. The diagram has 36 vertices and 55
solid arrows; the dashed lines identify each non-projective with its translate. No arrow
label, multiplicity or orientation marker appears, so direction must be read from the
arrowheads alone.

**Step 3.** For a hereditary algebra $\dim \operatorname{Hom}(X,Y)$ is the number of paths
from $X$ to $Y$ in the Auslander-Reiten quiver counted modulo the mesh relations: for each
non-projective $Z$, the sum of the composites through the middle terms of the almost split
sequence ending at $Z$ is zero. Compute $\operatorname{Hom}(M_i, M_j)$ for all
twenty-five ordered pairs this way. Each $\operatorname{End}(M_i)$ is one dimensional by
Schur's lemma, giving the five diagonal entries.

**Step 4.** Assemble the matrix of Hom dimensions given above. Note that three entries are
$2$, so any argument that assumes the Hom spaces are at most one dimensional is already
wrong at this step.

**Step 5.** Check the result against the Euler form. With
$d_T = \sum_i \underline{\dim} M_i$ one finds $\langle d_T, d_T\rangle = 3$, while the
matrix sums to $19$. The difference $16$ must equal $\dim \operatorname{Ext}^1(T,T)$, and
computing that independently from the diagram confirms it. The agreement is the check that
no Hom dimension has been miscounted.

**Step 6.** Summing the matrix, $4 + 6 + 5 + 1 + 3 = 19$.

**Step 7.** Therefore $\dim_k \operatorname{End}(T) = 19$.

## Image description

The figure is a self-authored diagram of an Auslander-Reiten quiver, produced with
matplotlib and exported as a single-panel opaque PNG. It occupies a wide landscape frame on
a plain white background and contains thirty-six vertices arranged in six horizontal rows
across fifteen columns, in the staggered lattice characteristic of such diagrams.

Each vertex is drawn as a short string of six digits inside a thin rounded rectangle with a
white fill, so the boxes sit above the connecting lines and remain legible where lines pass
behind them. Every digit is $0$, $1$, $2$ or $3$. The strings are all distinct and no two
boxes overlap.

Two kinds of connection appear and they are visually distinct. Solid dark lines carry a
filled arrowhead at one end and run diagonally between boxes in neighbouring rows, never
horizontally; there are fifty-five of these. Forty-three of them join adjacent rows and
twelve span two rows, and none crosses the diagram at a shallow angle, so each arrowhead
can be traced unambiguously to its target. Dashed pale grey lines run strictly
horizontally, joining boxes in the same row to their immediate neighbour on the left; these
carry no arrowhead and are visually lighter in both colour and weight than the solid
arrows. Confusing the two families, or reading a solid arrow in the wrong direction, is the
principal hazard in the figure.

The arrangement is not a rectangular grid: rows begin and end at different columns, the
leftmost column contains a single box in the top row and another lower down, and the
rightmost column likewise tapers. There are no axes, no coordinate frame, no shading, no
colour coding, no captions, no legend, no title, and no annotation identifying any
particular vertex. Nothing in the figure names the algebra, the underlying quiver or its
orientation; both must be inferred from the diagram itself.

## Distractors

Distractors (incorrect answers only). Note that in testing we provided the model all
potential answers, including the GTFA.

| value | the specific error it encodes |
| --- | --- |
| 3 | the Euler form $\langle d_T, d_T\rangle$ taken as the answer, ignoring that $T$ is not rigid |
| 16 | $\dim \operatorname{Ext}^1(T,T)$ reported in place of $\dim \operatorname{End}(T)$ |
| 35 | the Hom and Ext totals added instead of the Hom total alone |
| 14 | every nonzero Hom space assumed one dimensional, missing the three entries equal to 2 |
| 20 | one summand misread as a neighbouring vertex in the diagram |

Each value is the exact result of the corresponding error, computed with the same verified
machinery as the GTFA.

## Why a model is expected to fail

Two independent things must both go right.

The reading. Thirty-six near-identical digit strings, fifty-five arrows and thirty-five
dashed translation lines, laid out in a staggered lattice where every box has neighbours
above, below and to both sides. Solid arrows and dashed $\tau$-lines are different objects
carrying different meaning, and a single arrow read backwards changes the path count and
therefore the answer.

The mathematics. The Euler form gives 3 and is the natural thing to reach for, since it is
the standard tool for exactly this kind of question and needs no diagram at all. It is
wrong here by 16 because $T$ is not rigid. Recovering the true value requires counting
paths modulo mesh relations, which cannot be shortcut and which three times produces a
two-dimensional Hom space where a multiplicity-free habit would give one.

Failure reason, 1 to 3 sentences, for the submission form: the model either misreads the
arrow structure of the Auslander-Reiten quiver, most often by treating a dashed translation
line as an irreducible map or by reversing an arrow, or it applies the Euler form to the
total dimension vector and returns 3, which is correct only for a rigid module. In both
cases the computation that follows is internally consistent, so nothing in the response
flags the error.

## What the prompt has to pin down

Writing the prompt sentence is yours. It needs to fix the following.

Must state:
- that the figure is the Auslander-Reiten quiver of a finite dimensional path algebra
  $kQ$ over an algebraically closed field, that vertices are labelled by dimension vectors,
  that solid arrows are irreducible morphisms and dashed lines are the translation $\tau$;
- the five dimension vectors defining $T$, and that $T$ is their direct sum;
- that the quantity wanted is $\dim_k \operatorname{End}_{kQ}(T)$, the dimension of the
  endomorphism algebra as a vector space over $k$;
- that the answer is an exact positive integer.

Must not:
- say whether $T$ is rigid or tilting, or mention $\operatorname{Ext}$, the Euler form,
  mesh relations or path counting, since Part 7 forbids method steering;
- state the underlying quiver or its orientation, which would make the figure skippable;
- embed any answer options.

## Checklist status

Passing: PNG, opaque, high resolution, self-authored, single image, no post-processing,
single question, image-dependent, not OCR since the content is the arrow structure rather
than the labels, not a table, not a pure count, not stacked, GTFA unique and self-contained
at 2 characters, five distinct distractors each tied to a real error, numbered solution
with the first two steps observational and seven steps in total, image description over 300
words without revealing the answer, KaTeX-safe LaTeX.

Answer space: $\dim \operatorname{End}$ of a five-summand module over this algebra ranges
over at least 5 to 30 in sampling, so the naive answer set comfortably exceeds ten.

Hand verification: twenty-five Hom dimensions by path counting modulo meshes, five of which
are immediate by Schur. The Euler form cross-check at Step 5 catches an arithmetic slip.
Inside an hour for someone who knows the technique.

Open, and yours: the prompt text, and the two model runs.
