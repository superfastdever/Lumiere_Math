import sys, math
sys.path.insert(0, "/home/user/Lumiere_Math/tasks/queue/00/t00004/build")
from toric import det, normal_form, hj, exceptional_hull
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

RAYS = [(1,0),(4,7),(-1,2),(-5,-3),(1,-3)]
N = len(RAYS)

def total(rays):
    t = 0
    for i in range(len(rays)):
        u, v = rays[i], rays[(i+1) % len(rays)]
        d = det(u, v)
        if d <= 0: return None
        if d == 1: continue
        dd, q = normal_form(u, v)
        t += len(hj(dd, q))
    return t

def ordinary_cf(d, q):
    out = []
    while q:
        out.append(d // q); d, q = q, d % q
    return out

GT = total(RAYS)
print("GTFA (exceptional divisors) =", GT)
print("rays of the resolution fan   =", N + GT)

print("\ndistractors from specific errors")
t = 0
for i in range(N):
    u, v = RAYS[i], RAYS[(i+1) % N]
    dd, q = normal_form(u, v)
    t += len(ordinary_cf(dd, q))
print(f"   ordinary continued fractions instead of Hirzebruch-Jung : {t}")
print(f"   counting rays of the resolution fan, not the divisors    : {N + GT}")
print(f"   the wrap-around cone <{RAYS[-1]},{RAYS[0]}> overlooked    : "
      f"{GT - len(hj(*normal_form(RAYS[-1], RAYS[0])))}")
t2 = 0
for i in range(N):
    u, v = RAYS[i], RAYS[(i+1) % N]
    dd, q = normal_form(u, v)
    qq = (dd - q) % dd
    t2 += len(hj(dd, qq)) if qq else 0
print(f"   q replaced by d-q, a convention slip                     : {t2}")
from math import gcd
print("\n   single-ray misreadings (primitive neighbours only):")
seen = {}
for idx, r in enumerate(RAYS):
    for dx in (-1,0,1):
        for dy in (-1,0,1):
            cand = list(RAYS)
            nb = (r[0]+dx, r[1]+dy)
            if nb == r or nb == (0,0): continue
            if gcd(abs(nb[0]), abs(nb[1])) != 1: continue
            cand[idx] = nb
            t = total(cand)
            if t is None or t == GT: continue
            seen.setdefault(t, []).append(f"ray {r} read as {nb}")
for t in sorted(seen):
    print(f"      total {t:3d}  e.g. {seen[t][0]}   ({len(seen[t])} such misreads)")

# ---------------------------------------------------------------- figure
XL, XH, YL, YH = -7.6, 7.6, -6.6, 8.6
fig, ax = plt.subplots(figsize=(8.4, 8.4*(YH-YL)/(XH-XL)), dpi=300)
for x in range(int(XL)+1, int(XH)+1):
    for y in range(int(YL)+1, int(YH)+1):
        ax.plot([x], [y], marker="o", ms=3.4, color="#8f9bab", zorder=6)
def boundary(v):
    t = min(((XH if v[0] > 0 else XL)/v[0]) if v[0] else 1e18,
            ((YH if v[1] > 0 else YL)/v[1]) if v[1] else 1e18)
    return (v[0]*t, v[1]*t)
for v in RAYS:
    e = boundary(v)
    ax.plot([0, e[0]], [0, e[1]], color="#16324f", lw=2.6, solid_capstyle="round", zorder=3)
ax.plot([0], [0], marker="o", ms=8.0, color="#16324f", zorder=7)
ax.set_xlim(XL, XH); ax.set_ylim(YL, YH)
ax.set_aspect("equal"); ax.axis("off")
fig.patch.set_facecolor("white")
fig.savefig("../t00004/figure.png", facecolor="white", bbox_inches="tight", pad_inches=0.12)
from PIL import Image
im = Image.open("figure.png"); bg = Image.new("RGB", im.size, (255,255,255))
bg.paste(im, mask=im.split()[-1] if im.mode=="RGBA" else None)
bg.save("figure.png", "PNG", optimize=True)
o = Image.open("figure.png")
print(f"\nfigure {o.mode} {o.size}, {o.size[0]/(XH-XL):.0f} px per lattice unit")
