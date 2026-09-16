import sys, math
sys.path.insert(0, "/home/user/Lumiere_Math/tasks/t02")
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

W, N = [-2,-1,2,-1,-1,-2,1,-2,-2,1], 3
R = [1.00, 1.46, 1.92]
NC = len(W)
SPACING = 2*math.pi/NC
HW = 0.36*SPACING                      # angular half-width of a crossing swap
CENTER = [SPACING*(k+0.5) for k in range(NC)]

def smooth(t): return 3*t*t - 2*t*t*t

def strand_path(level0, steps=26):
    """Follow one strand around; return (thetas, radii, level_before_each_crossing)."""
    th, rr, lv = [], [], []
    level, cur = level0, 0.0
    for k, g in enumerate(W):
        i = abs(g) - 1
        a, b = CENTER[k]-HW, CENTER[k]+HW
        for s in range(steps):                    # constant-radius run
            t = cur + (a-cur)*s/steps
            th.append(t); rr.append(R[level])
        lv.append(level)
        if level in (i, i+1):
            nxt = i+1 if level == i else i
            for s in range(steps+1):
                t = s/steps
                th.append(a + (b-a)*t)
                rr.append(R[level] + (R[nxt]-R[level])*smooth(t))
            level = nxt
        else:
            for s in range(steps+1):
                th.append(a + (b-a)*s/steps); rr.append(R[level])
        cur = b
    for s in range(steps+1):
        th.append(cur + (2*math.pi-cur)*s/steps); rr.append(R[level])
    return th, rr, lv

paths = [strand_path(p) for p in range(3)]

# which strand is over at each crossing
over_at, under_at = {}, {}
for k, g in enumerate(W):
    i = abs(g) - 1
    for sidx, (_, _, lv) in enumerate(paths):
        if lv[k] == i:
            (over_at if g > 0 else under_at)[k] = sidx
        elif lv[k] == i+1:
            (under_at if g > 0 else over_at)[k] = sidx
assert len(over_at) == len(under_at) == NC

def xy(th, rr):
    return [r*math.cos(t) for t, r in zip(th, rr)], [r*math.sin(t) for t, r in zip(th, rr)]

def window(sidx, k, half):
    th, rr, _ = paths[sidx]
    lo, hi = CENTER[k]-half, CENTER[k]+half
    pts = [(t, r) for t, r in zip(th, rr) if lo <= t <= hi]
    return xy([p[0] for p in pts], [p[1] for p in pts])

INK, LW = "#16324f", 3.4
fig, ax = plt.subplots(figsize=(8, 8), dpi=240)
for th, rr, _ in paths:
    x, y = xy(th, rr)
    ax.plot(x, y, color=INK, lw=LW, solid_capstyle="round", zorder=2)
for k in range(NC):
    x, y = window(under_at[k], k, 0.052)
    ax.plot(x, y, color="white", lw=LW+7.5, solid_capstyle="butt", zorder=3)
    x, y = window(over_at[k], k, 0.075)
    ax.plot(x, y, color=INK, lw=LW, solid_capstyle="round", zorder=4)
ax.set_aspect("equal"); ax.axis("off")
ax.set_xlim(-2.15, 2.15); ax.set_ylim(-2.15, 2.15)
fig.patch.set_facecolor("white")
fig.savefig("/home/user/Lumiere_Math/tasks/t02/figure.png", facecolor="white",
            bbox_inches="tight", pad_inches=0.15)

from PIL import Image
im = Image.open("/home/user/Lumiere_Math/tasks/t02/figure.png")
bg = Image.new("RGB", im.size, (255,255,255))
bg.paste(im, mask=im.split()[-1] if im.mode == "RGBA" else None)
bg.save("/home/user/Lumiere_Math/tasks/t02/figure.png", "PNG", optimize=True)
out = Image.open("/home/user/Lumiere_Math/tasks/t02/figure.png")
print("mode", out.mode, "size", out.size, "alpha", out.mode in ("RGBA","LA"))
print("over strand per crossing :", [over_at[k] for k in range(NC)])
print("under strand per crossing:", [under_at[k] for k in range(NC)])
