# t00005, work in progress

Plane sextic carrying five singularities of four distinct types. Not yet finished:
the curve has not been selected or fully verified, so there is no GTFA here yet.

## Design

| point | type | delta |
| --- | --- | --- |
| (0, 0) | ordinary triple point | 3 |
| (-3, 1) | node | 1 |
| (2, -2) | node | 1 |
| (1, 3) | cusp, horizontal tangent | 1 |
| (-2, -3) | tacnode, horizontal tangent | 2 |

Every condition is linear in the 28 coefficients of a sextic, which is what makes the
family computable: a node is f = f_x = f_y = 0; a cusp with horizontal tangent adds
f_xx = f_xy = 0; a tacnode adds the vanishing of the u^3 coefficient; an ordinary triple
point is the vanishing of f and all first and second partials. That is 23 conditions,
leaving a 5-dimensional solution space.

If the curve is irreducible with no further singularities and is smooth at infinity, the
geometric genus is (6-1)(6-2)/2 - sum(delta) = 10 - 8 = 2.

## Why the first attempt was structurally dead

The first choice of points put the triple point and both nodes on one line. A line through
a triple point and two nodes meets a sextic with multiplicity at least 3 + 2 + 2 = 7, which
exceeds 6, so by Bezout the line must be a component of the curve. Every member of that
family was therefore reducible, by necessity rather than bad luck: 0 of 60 sampled members
were irreducible. Moving the points into general position fixed it at once, 40 of 40
sampled members irreducible and 37 of those smooth at infinity.

This is recorded because it is a reusable constraint, not a one-off: imposed singular
points must be in sufficiently general position that no low-degree curve through them is
forced to split off by Bezout.

## Files

- `build/construct.py` builds the linear system and saves a basis of the solution space
- `build/pick.py` fast exact test that the singular locus is exactly the designed points,
  by resultants and gcd rather than Groebner bases, which were far too slow
- `build/refine.py` searches for a member with small integer coefficients and classifies
  each singularity from its local jets

## Still to do

Select the curve, confirm each singularity is the designed type rather than merely a
singular point, confirm no further singularities anywhere including at infinity, render
the real picture, and only then write the package.

## Status: the mathematics verifies, the first curve failed visual QC

A member of the family was found whose singular locus is provably exactly the five
designed points. Exact verification, all over Q with no floating point:

- irreducible over Q
- leading form has nonzero discriminant, so the projective curve is smooth at infinity
- gcd of the two resultants factors as x^6 (x-1)^3 (x+2)^4 (x+3)^2 (x-2)^2, all linear,
  so every singular point is rational; solving at each x gives exactly
  (0,0), (1,3), (-2,-3), (-3,1), (2,-2) and nothing else, all real
- local jets confirm each designed type: multiplicity 3 with a cubic form of nonzero
  discriminant at (0,0) so an ordinary triple point; nonzero 2-jet discriminant at
  (-3,1) and (2,-2) so nodes; degenerate 2-jet with nonzero u^3 coefficient at (1,3)
  so an A2 cusp; degenerate 2-jet, vanishing u^3 and nonzero u^4 at (-2,-3) so an
  A3 tacnode

Hence sum(delta) = 3+1+1+1+2 = 8 and the geometric genus is 10 - 8 = 2.

### Two rendering problems found, one fatal

**Contouring is the wrong renderer.** matplotlib's contour at level zero leaves a visible
gap at the cusp and the tacnode, because the function is very flat near a degenerate
singularity. A gap in a curve is exactly the sort of artifact that gets a task returned.
Replaced by root finding: for each x solve the degree-6 polynomial in y and keep the real
roots, then repeat with the roles swapped and overlay. Nothing is interpolated across a
singular point, so degenerate singularities close properly.

**The curve had a false cusp.** A curvature scan over 80897 sampled points found a smooth
point at about (0.91, 2.97), a tenth of a unit from the genuine cusp at (1,3), whose
radius of curvature is 0.5 px at the figure's scale of 224 px per unit. Zooming to a
half-width of 0.008 resolves it into a smooth rounded turn, so it is not a singularity,
but at any sane viewing scale it renders as a corner indistinguishable from the real cusp.
A reader would count six singularities and compute the wrong genus. That is an ambiguity
and a major error, so this curve is rejected.

Away from the singularities the rest of the curve is fine: excluding a radius of 0.2, the
sharpest smooth point has a radius of curvature of 82 px.

### Selection criterion now being applied

Among the members with exactly the designed singular locus, choose one maximising the
minimum radius of curvature over all smooth points at distance more than 0.15 from any
singularity. `build/select.py` does this. A curve only ships if no smooth point can be
mistaken for a singularity.
