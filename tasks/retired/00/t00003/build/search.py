"""Search line arrangements that are adversarial but unambiguous.

Wanted: one quadruple point, several triple points, and near-miss triangles that
are small relative to the figure yet comfortably resolvable by a human reviewer.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import math, random

def norm(a, b, c):
    g = math.gcd(math.gcd(abs(a), abs(b)), abs(c)) or 1
    a, b, c = a//g, b//g, c//g
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return (a, b, c)

def through(pt, a, b):
    return norm(a, b, a*pt[0] + b*pt[1])

def meet(p, q):
    a1,b1,c1 = p; a2,b2,c2 = q
    det = a1*b2 - a2*b1
    if det == 0: return None
    return (F(c1*b2 - c2*b1, det), F(a1*c2 - a2*c1, det))

def analyse(lines):
    pts = {}
    for i, j in combinations(range(len(lines)), 2):
        m = meet(lines[i], lines[j])
        if m is None: return None
        pts.setdefault(m, set()).update({i, j})
    return pts

DIRS = [(0,1),(1,0),(1,-1),(1,1),(1,-2),(2,1),(1,-3),(3,1),(2,-1),(1,2),
        (3,-1),(1,3),(3,-2),(2,3),(1,-4),(4,1),(3,2),(2,-3),(4,-1),(1,4)]

def attempt(rng):
    Q = (rng.randint(-2,2), rng.randint(-2,2))
    ds = rng.sample(DIRS, 4)
    lines = [through(Q, a, b) for a, b in ds]
    # T1 on line 0, T2 on line 1
    out = []
    for base in (0, 1):
        a, b, c = lines[base]
        for _ in range(40):
            t = rng.randint(-5, 5)
            pt = (t, F(c - a*t, b)) if b else (F(c - b*t, a), t)
            if any(x != int(x) for x in pt): continue
            pt = (int(pt[0]), int(pt[1]))
            if pt == Q: continue
            out.append(pt); break
        else:
            return None
    T1, T2 = out
    used = set(ds)
    for T in (T1, T2):
        picks = [d for d in DIRS if d not in used]
        rng.shuffle(picks)
        for a, b in picks[:2]:
            lines.append(through(T, a, b)); used.add((a, b))
    picks = [d for d in DIRS if d not in used]
    a, b = rng.choice(picks)
    lines.append(norm(a, b, rng.randint(-6, 6)))
    if len(set(lines)) != 9: return None
    return lines

def score(lines):
    pts = analyse(lines)
    if pts is None: return None
    mult = {p: len(s) for p, s in pts.items()}
    prof = Counter(mult.values())
    if prof.get(4, 0) < 1 or prof.get(3, 0) < 2: return None
    if max(mult.values()) > 4: return None
    xy = [(float(p[0]), float(p[1])) for p in pts]
    if max(abs(x) for x, _ in xy) > 6.5 or max(abs(y) for _, y in xy) > 6.5: return None
    dmin = min(math.dist(a, b) for a, b in combinations(xy, 2))
    if dmin < 0.34: return None
    # near-miss triangles: three lines whose three pairwise points are all close
    tri = []
    for i, j, k in combinations(range(9), 3):
        ps = [meet(lines[i], lines[j]), meet(lines[i], lines[k]), meet(lines[j], lines[k])]
        if len(set(ps)) != 3: continue
        f = [(float(p[0]), float(p[1])) for p in ps]
        diam = max(math.dist(a, b) for a, b in combinations(f, 2))
        if diam <= 1.15: tri.append((diam, (i, j, k)))
    if len(tri) < 2: return None
    b2 = sum(m - 1 for m in mult.values())
    return dict(lines=lines, pts=pts, mult=mult, prof=dict(sorted(prof.items())),
                dmin=dmin, tri=sorted(tri)[:5], b2=b2)

if __name__ == '__main__':
    rng = random.Random(2024)
    best = []
    for _ in range(400000):
        L = attempt(rng)
        if not L: continue
        s = score(L)
        if s: best.append(s)
    best.sort(key=lambda s: (-s["dmin"], -len(s["tri"])))
    print(f"{len(best)} configurations found\n")
    for s in best[:4]:
        print("lines:", s["lines"])
        print(f"   profile {s['prof']}   b_2 = {s['b2']}   min point separation {s['dmin']:.3f}")
        print(f"   near-miss triangles: " +
              ", ".join(f"{d:.3f} on {t}" for d, t in s["tri"][:4]))
        print()
