import itertools, math, sys
sys.path.insert(0, "/home/user/Lumiere_Math/tasks/t01")
from build import N, EDGES, det_bareiss, evaluate, seg_point_dist
from render import POS
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def count(edges, n=N):
    L = [[0]*n for _ in range(n)]
    for u, v in edges:
        L[u][u] += 1; L[v][v] += 1; L[u][v] -= 1; L[v][u] -= 1
    return det_bareiss([[L[i][j] for j in range(1, n)] for i in range(1, n)])

# ---- label placement: pick the angle furthest from incident edges & neighbours
def label_offset(i):
    best, bestang = -1, 90
    for ang in range(0, 360, 5):
        r = math.radians(ang)
        p = (POS[i][0] + 0.75*math.cos(r), POS[i][1] + 0.75*math.sin(r))
        d = min([seg_point_dist(p, POS[u], POS[v]) for u, v in EDGES]
                + [math.dist(p, POS[w]) for w in range(N) if w != i])
        if d > best:
            best, bestang = d, ang
    return bestang, best

fig, ax = plt.subplots(figsize=(7.2, 7.2), dpi=240)
for u, v in EDGES:
    ax.plot([POS[u][0], POS[v][0]], [POS[u][1], POS[v][1]],
            color="#2f4a6d", lw=2.1, zorder=1, solid_capstyle="round")
for i, (x, y) in enumerate(POS):
    ax.scatter([x], [y], s=200, color="#111111", zorder=3)
    ang, clr = label_offset(i)
    r = math.radians(ang)
    ax.annotate(f"$v_{{{i+1}}}$", (x + 0.62*math.cos(r), y + 0.62*math.sin(r)),
                ha="center", va="center", fontsize=16, zorder=4)
    print(f"  v{i+1}: label angle {ang:3d} deg, clearance {clr:.2f}")
ax.set_xlim(-1.0, 11.0); ax.set_ylim(-1.0, 11.0)
ax.set_aspect("equal"); ax.axis("off")
fig.patch.set_facecolor("white")
fig.savefig("/home/user/Lumiere_Math/tasks/t01/figure.png",
            facecolor="white", bbox_inches="tight", pad_inches=0.3)
print("\nfigure re-rendered")

c, s, nx = evaluate(POS)
print(f"edge clearance {c:.3f} | crossing sep {s:.3f} | crossings {nx}")
print("true spanning trees:", count(EDGES))

print("\n-- counts for graphs a model might substitute by prior --")
C8 = [(i, (i+1) % 8) for i in range(8)]
print("  Wagner V8 (C8 + 4 diameters):", count(C8 + [(0,4),(1,5),(2,6),(3,7)]))
print("  cube Q3                     :",
      count([(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]))
print("  K_{4,4}                     :",
      count([(i, j) for i in range(4) for j in range(4, 8)]))
print("  C8 + 0-2,4-6 only (misses 4 long chords):", count(C8 + [(0,2),(4,6)]))
