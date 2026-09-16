"""Line arrangement: exact intersection lattice and the Betti numbers of the
complexified complement M = C^2 minus the union of the complexified lines.

Orlik-Solomon / Arnold: for a rank-2 arrangement of n lines,
    Poincare polynomial = 1 + n t + (sum over points p of (m_p - 1)) t^2
so b_0 = 1, b_1 = n, b_2 = sum_p (m_p - 1).
"""
from fractions import Fraction as F
from itertools import combinations
import math

# a*x + b*y = c
LINES = [
    ("L1", 0, 1,  0),
    ("L2", 1, 0,  0),
    ("L3", 1, -1, 0),
    ("L4", 2, 1,  0),
    ("L5", 1, -3, 4),
    ("L6", 1, 1,  4),
    ("L7", 2, -1, -3),
    ("L8", 1, 2,  6),
    ("L9", 3, -1, -4),
]
N = len(LINES)

def meet(p, q):
    _, a1, b1, c1 = p
    _, a2, b2, c2 = q
    det = a1*b2 - a2*b1
    if det == 0:
        return None                      # parallel
    return (F(c1*b2 - c2*b1, det), F(a1*c2 - a2*c1, det))

# every pair
pts = {}
parallel = []
for p, q in combinations(LINES, 2):
    m = meet(p, q)
    if m is None:
        parallel.append((p[0], q[0])); continue
    pts.setdefault(m, set()).update({p[0], q[0]})

print("lines:", N, " parallel pairs:", parallel)
print("distinct intersection points:", len(pts))

mult = {pt: len(ls) for pt, ls in pts.items()}
from collections import Counter
print("multiplicity profile:", dict(sorted(Counter(mult.values()).items())))

b2 = sum(m - 1 for m in mult.values())
print(f"\nb_0 = 1")
print(f"b_1 = n = {N}")
print(f"b_2 = sum (m_p - 1) = {b2}")

# independent cross-check: b_2 = C(n,2) - sum over points of (C(m,2) - (m-1))
pairs = N*(N-1)//2
correction = sum(m*(m-1)//2 - (m-1) for m in mult.values())
print(f"cross-check: C({N},2) - corrections = {pairs} - {correction} = {pairs - correction}")
assert pairs - correction == b2

# third check: Zaslavsky, regions of the real arrangement = |chi(-1)|, chi(t)=t^2-n t+b_2
regions = 1 + N + b2
bounded = 1 - N + b2
print(f"Zaslavsky: regions = {regions}, bounded regions = {bounded}")

print("\nspecial points (multiplicity 3 or more):")
for pt, ls in sorted(pts.items(), key=lambda kv: (-len(kv[1]), str(kv[0]))):
    if len(ls) >= 3:
        print(f"   {(str(pt[0]), str(pt[1]))}  m={len(ls)}  {sorted(ls)}")

xs = [float(p[0]) for p in pts]; ys = [float(p[1]) for p in pts]
print(f"\nbounding box of all points: x in [{min(xs):.3f}, {max(xs):.3f}], "
      f"y in [{min(ys):.3f}, {max(ys):.3f}]")

dmin, pair = 1e9, None
for a, b in combinations(pts, 2):
    d = math.dist((float(a[0]), float(a[1])), (float(b[0]), float(b[1])))
    if d < dmin:
        dmin, pair = d, (a, b)
print(f"closest distinct points: {dmin:.4f} at "
      f"{(str(pair[0][0]),str(pair[0][1]))} and {(str(pair[1][0]),str(pair[1][1]))}")

near = sorted(
    (math.dist((float(a[0]),float(a[1])),(float(b[0]),float(b[1]))), a, b)
    for a, b in combinations(pts, 2))[:6]
print("\nsix closest pairs (candidate near-miss triangles):")
for d, a, b in near:
    print(f"   {d:.4f}   {(str(a[0]),str(a[1]))} <-> {(str(b[0]),str(b[1]))}")
