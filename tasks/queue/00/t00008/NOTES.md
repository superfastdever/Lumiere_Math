# t00008, in progress: hardened plumbing graph

Driven by the first real test data in this project. The star-shaped plumbing graph was
solved correctly by both frontier models, so it fails Stage 1 and is not submittable.

## Why the star-shaped example lost 0-2

Verified, not inferred from the model transcripts:

| branch, read hub outward | continued fraction |
| --- | --- |
| [7] | 7/1 |
| [4,2] | 7/2 |
| [3,2,2] | 7/3 |
| [2,4] | 7/4 |
| [2,2,3] | 7/5 |
| [2,2,2,2,2,2] | 7/6 |

Every branch has the same numerator 7 and the denominators run 1 through 6. That is
designed, and it is what gave the problem away: the hub relation becomes v0 = 7*x_j for
every j, so a single substitution y_j = x_j - x_1 collapses five generators at once, and
sum(q_j/d_j) = 21/7 = 3 exactly, making det = 7^6 * (5-3) = 2*7^6 fall out with no work.

The second reason is that the figure has no extraction difficulty at all: 18 vertices, a
tree, radial layout, no edge crossings, large well-separated labels. The one genuine trap,
that order along a branch matters so [4,2] = 7/2 but [2,4] = 7/4, was handled correctly by
both models.

**Conclusion that overturns the earlier approach: depth is not the lever. Zero extraction
difficulty beats any amount of depth, because once the graph is read the rest is a textbook
algorithm.**

## Negative result: a cycle is the wrong fix

First attempt was to break the star shape with a 4-cycle carrying hanging chains, on the
reasoning that the Seifert continued-fraction machinery then does not apply. Over 106519
negative-definite configurations, the cokernel was almost always cyclic:

    nontrivial invariant factors:  1 -> 1000 cases,  2 -> 88 cases,  3 or more -> none

A cyclic answer is weak for this project, because the responder only needs the determinant
and can guess the structure. The rich (7,7,7,7,98) structure of the original came from the
high-valence hub, not from the absence of a shortcut. Recorded so this is not retried.

## Current direction

Two branch nodes joined by a chain, each carrying three or four chains, with branch
continued fractions deliberately mismatched. No single-star formula applies, the multiple
invariant factors survive because two high-valence nodes remain, and the uniform collapse
cannot happen.

`build/fast.py` holds exact integer Bareiss determinant and Smith normal form, written
because sympy was far too slow inside a search loop (two searches were killed on time).
