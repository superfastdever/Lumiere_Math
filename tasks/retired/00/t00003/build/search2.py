from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import math, random, sys
sys.path.insert(0, "/home/user/Lumiere_Math/tasks/queue/00/t00003/build")
from search import norm, through, meet, analyse, DIRS

def attempt10(rng):
    Q = (rng.randint(-3,3), rng.randint(-3,3))
    ds = rng.sample(DIRS, 4)
    lines = [through(Q, a, b) for a, b in ds]
    used = set(ds); Ts = []
    for base in (0, 1, 2):
        a, b, c = lines[base]
        for _ in range(60):
            t = rng.randint(-6, 6)
            if b and (c - a*t) % b == 0: pt = (t, (c - a*t)//b)
            elif a and (c - b*t) % a == 0: pt = ((c - b*t)//a, t)
            else: continue
            if pt == Q: continue
            Ts.append(pt); break
        else: return None
    for T in Ts:
        picks = [d for d in DIRS if d not in used]
        if len(picks) < 2: return None
        rng.shuffle(picks)
        for a, b in picks[:2]:
            lines.append(through(T, a, b)); used.add((a, b))
    return lines if len(set(lines)) == 10 else None

def score10(lines):
    pts = analyse(lines)
    if pts is None: return None
    mult = {p: len(s) for p, s in pts.items()}
    prof = Counter(mult.values())
    if prof.get(4, 0) < 1 or prof.get(3, 0) < 3 or max(mult.values()) > 4: return None
    xy = [(float(p[0]), float(p[1])) for p in pts]
    spread = max(max(x for x,_ in xy) - min(x for x,_ in xy),
                 max(y for _,y in xy) - min(y for _,y in xy))
    if not (8.0 <= spread <= 15.0): return None
    dmin = min(math.dist(a, b) for a, b in combinations(xy, 2))
    if dmin < 0.40: return None
    tri = []
    for i, j, k in combinations(range(len(lines)), 3):
        ps = [meet(lines[i],lines[j]), meet(lines[i],lines[k]), meet(lines[j],lines[k])]
        if len(set(ps)) != 3: continue
        f = [(float(p[0]), float(p[1])) for p in ps]
        d = max(math.dist(a,b) for a,b in combinations(f,2))
        if d <= 0.11*spread: tri.append((d, (i,j,k)))
    if len(tri) < 3: return None
    b2 = sum(m-1 for m in mult.values())
    return dict(lines=lines, prof=dict(sorted(prof.items())), b2=b2, dmin=dmin,
                spread=spread, tri=sorted(tri), n=len(lines), npts=len(pts))

rng = random.Random(77)
out = []
for _ in range(500000):
    L = attempt10(rng)
    if not L: continue
    s = score10(L)
    if s: out.append(s)
out.sort(key=lambda s: (-len(s["tri"]), -s["dmin"]))
print(f"{len(out)} configurations\n")
for s in out[:3]:
    print("lines:", s["lines"])
    print(f"   {s['n']} lines, {s['npts']} points, profile {s['prof']}, b_2 = {s['b2']}")
    print(f"   spread {s['spread']:.2f}, min separation {s['dmin']:.3f} "
          f"({100*s['dmin']/s['spread']:.1f}% of spread)")
    print(f"   {len(s['tri'])} near-miss triangles, smallest "
          f"{', '.join(f'{d:.3f}' for d,_ in s['tri'][:4])}")
    print()
