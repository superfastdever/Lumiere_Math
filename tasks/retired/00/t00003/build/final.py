"""Exact analysis and render for the chosen arrangement."""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import math
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

LINES = [(0,1,-1), (1,2,-4), (2,-3,-1), (3,1,-7), (1,0,-4),
         (1,-2,-2), (1,4,-10), (1,1,-1), (3,2,-5)]
N = len(LINES)

def meet(p, q):
    a1,b1,c1 = p; a2,b2,c2 = q
    d = a1*b2 - a2*b1
    return None if d == 0 else (F(c1*b2 - c2*b1, d), F(a1*c2 - a2*c1, d))

pts = {}
for i, j in combinations(range(N), 2):
    m = meet(LINES[i], LINES[j])
    assert m is not None, f"lines {i},{j} are parallel"
    pts.setdefault(m, set()).update({i, j})
mult = {p: len(s) for p, s in pts.items()}
prof = Counter(mult.values())

b2 = sum(m-1 for m in mult.values())
pairs = N*(N-1)//2
corr = sum(m*(m-1)//2 - (m-1) for m in mult.values())
if __name__ == '__main__':
    print(f"lines {N} | distinct points {len(pts)} | profile {dict(sorted(prof.items()))}")
    print(f"b_0 = 1, b_1 = {N}, b_2 = {b2}")
    print(f"cross-check C({N},2) - corrections = {pairs} - {corr} = {pairs-corr}")
    assert pairs - corr == b2
    print(f"Zaslavsky consistency: regions {1+N+b2}, bounded {1-N+b2}")
    
    print("\npoints of multiplicity >= 3:")
    for p, s in sorted(pts.items(), key=lambda kv: -len(kv[1])):
        if len(s) >= 3:
            print(f"   ({p[0]}, {p[1]})  m={len(s)}  lines {sorted(x+1 for x in s)}")
    
    xy = [(float(p[0]), float(p[1])) for p in pts]
    xlo, xhi = min(x for x,_ in xy), max(x for x,_ in xy)
    ylo, yhi = min(y for _,y in xy), max(y for _,y in xy)
    spread = max(xhi-xlo, yhi-ylo)
    dmin = min(math.dist(a,b) for a,b in combinations(xy,2))
    print(f"\npoint bounding box x[{xlo:.2f},{xhi:.2f}] y[{ylo:.2f},{yhi:.2f}] spread {spread:.2f}")
    print(f"closest distinct points {dmin:.3f} ({100*dmin/spread:.1f}% of spread)")
    
    tri = []
    for i,j,k in combinations(range(N),3):
        ps = [meet(LINES[i],LINES[j]), meet(LINES[i],LINES[k]), meet(LINES[j],LINES[k])]
        if len(set(ps)) != 3: continue
        f = [(float(a[0]), float(a[1])) for a in ps]
        d = max(math.dist(a,b) for a,b in combinations(f,2))
        tri.append((d,(i+1,j+1,k+1)))
    tri.sort()
    print("\nsmallest non-concurrent triples (the near-miss traps):")
    for d,t in tri[:5]:
        print(f"   lines {t}: triangle diameter {d:.3f}")
    
    # ---------------------------------------------------------------- distractors
    def b2_from(profile):
        return sum((m-1)*c for m, c in profile.items())
    base = dict(prof)
    print("\ndistractor values from specific misreadings:")
    print(f"   all points read as simple          : {pairs}")
    q = base.copy(); q[4] -= 1; q[2] = q.get(2,0) + 6
    print(f"   quadruple missed, seen as 6 doubles: {b2_from(q)}")
    q2 = base.copy(); q2[4] -= 1; q2[3] = q2.get(3,0)+1; q2[2] = q2.get(2,0)+3
    print(f"   quadruple seen as a triple only    : {b2_from(q2)}")
    t1 = base.copy(); t1[3] -= 1; t1[2] = t1.get(2,0)+3
    print(f"   one triple missed                  : {b2_from(t1)}")
    n1 = base.copy(); n1[2] -= 3; n1[3] = n1.get(3,0)+1
    print(f"   one near-miss read as concurrent   : {b2_from(n1)}")

if __name__ == '__main__':
    # -------------------------------------------------------------------- render
    PAD = 0.9
    XL, XH = xlo-PAD, xhi+PAD
    YL, YH = ylo-PAD, yhi+PAD
    fig, ax = plt.subplots(figsize=(8.6, 8.6), dpi=280)
    for a,b,c in LINES:
        if b != 0:
            xs = [XL, XH]; ys = [(c-a*x)/b for x in xs]
        else:
            ys = [YL, YH]; xs = [c/a, c/a]
        ax.plot(xs, ys, color="#1f3b57", lw=1.9, solid_capstyle="round")
    ax.set_xlim(XL, XH); ax.set_ylim(YL, YH)
    ax.set_aspect("equal"); ax.axis("off")
    fig.patch.set_facecolor("white")
    fig.savefig("figure.png", facecolor="white", bbox_inches="tight", pad_inches=0.08)
    
    from PIL import Image
    im = Image.open("figure.png")
    bg = Image.new("RGB", im.size, (255,255,255))
    bg.paste(im, mask=im.split()[-1] if im.mode=="RGBA" else None)
    bg.save("figure.png", "PNG", optimize=True)
    out = Image.open("figure.png")
    px_per_unit = out.size[0] / (XH-XL)
    print(f"\nrendered {out.mode} {out.size}, {px_per_unit:.0f} px per unit")
    print(f"closest distinct points = {dmin*px_per_unit:.0f} px apart")
    print(f"smallest near-miss triangle = {tri[0][0]*px_per_unit:.0f} px across")
