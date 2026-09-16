from fractions import Fraction as F
from itertools import combinations
import math
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from final import LINES, N, meet, pts, mult

xy = {p: (float(p[0]), float(p[1])) for p in pts}
xs = [v[0] for v in xy.values()]; ys = [v[1] for v in xy.values()]
PAD = 0.55
XL, XH = min(xs)-PAD, max(xs)+PAD
YL, YH = min(ys)-PAD, max(ys)+PAD
print(f"window x[{XL:.2f},{XH:.2f}] y[{YL:.2f},{YH:.2f}]  ({XH-XL:.2f} x {YH-YL:.2f})")

edge = min(min(v[0]-XL, XH-v[0], v[1]-YL, YH-v[1]) for v in xy.values())
print(f"closest any intersection comes to the frame edge: {edge:.3f} units")

def draw(path, mark):
    fig, ax = plt.subplots(figsize=(9.0, 9.0*(YH-YL)/(XH-XL)), dpi=290)
    for a,b,c in LINES:
        if b: xsл = [XL, XH]; ysл = [(c-a*x)/b for x in xsл]
        else: ysл = [YL, YH]; xsл = [c/a, c/a]
        ax.plot(xsл, ysл, color="#1f3b57", lw=2.0, solid_capstyle="round")
    if mark:
        for p, m in mult.items():
            if m >= 3:
                ax.scatter(*xy[p], s=260, facecolors="none",
                           edgecolors="crimson" if m == 3 else "darkorange", lw=2.4, zorder=5)
        for i,j,k in combinations(range(N),3):
            ps = [meet(LINES[i],LINES[j]), meet(LINES[i],LINES[k]), meet(LINES[j],LINES[k])]
            if len(set(ps)) != 3: continue
            f = [xy[p] for p in ps]
            d = max(math.dist(a,b) for a,b in combinations(f,2))
            if d <= 0.80:
                cx = sum(a[0] for a in f)/3; cy = sum(a[1] for a in f)/3
                ax.scatter([cx],[cy], s=520, facecolors="none", edgecolors="seagreen",
                           lw=2.2, ls=":", zorder=5)
    ax.set_xlim(XL,XH); ax.set_ylim(YL,YH); ax.set_aspect("equal"); ax.axis("off")
    fig.patch.set_facecolor("white")
    fig.savefig(path, facecolor="white", bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)

draw("figure.png", False)
draw("build/qc_overlay.png", True)

from PIL import Image
for p in ("figure.png",):
    im = Image.open(p); bg = Image.new("RGB", im.size, (255,255,255))
    bg.paste(im, mask=im.split()[-1] if im.mode=="RGBA" else None)
    bg.save(p, "PNG", optimize=True)
    o = Image.open(p)
    ppu = o.size[0]/(XH-XL)
    dmin = min(math.dist(a,b) for a,b in combinations(xy.values(),2))
    print(f"{p}: {o.mode} {o.size}, {ppu:.0f} px/unit, "
          f"closest points {dmin*ppu:.0f} px, edge margin {edge*ppu:.0f} px")
