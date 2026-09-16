"""Refine the layout, render the figure, and mine distractors from real misreadings."""
import itertools, math, random, sys
sys.path.insert(0, "/home/user/Lumiere_Math/tasks/t01")
from build import (N, EDGES, evaluate, spanning_trees_matrix_tree,
                   det_bareiss, seg_point_dist)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

START = [(3.09, 3.06), (0.569, 5.593), (9.251, 4.435), (8.843, 6.774),
         (7.213, 8.092), (3.787, 7.587), (0.764, 9.596), (2.276, 0.676)]

def refine(pos, seed=7, iters=60000, step=0.45):
    rng = random.Random(seed)
    pos = [tuple(p) for p in pos]
    base = evaluate(pos)
    best = min(base[0], base[1]) + 0.03 * base[2]
    for k in range(iters):
        i = rng.randrange(N)
        s = step * (1 - k / iters)
        cand = list(pos)
        cand[i] = (pos[i][0] + rng.gauss(0, s), pos[i][1] + rng.gauss(0, s))
        if not all(0.4 <= x <= 9.6 and 0.4 <= y <= 9.6 for x, y in cand):
            continue
        if min(math.dist(cand[a], cand[b])
               for a, b in itertools.combinations(range(N), 2)) < 2.1:
            continue
        c, sp, nx = evaluate(cand)
        if nx < 7:
            continue
        score = min(c, sp) + 0.03 * nx
        if score > best:
            best, pos = score, cand
    return pos, best

POS, score = refine(START)
clear, sep, ncross = evaluate(POS)
print(f"clearance={clear:.3f}  crossing sep={sep:.3f}  crossings={ncross}")

# ------------------------------------------------------------------ render
fig, ax = plt.subplots(figsize=(7.2, 7.2), dpi=220)
for u, v in EDGES:
    ax.plot([POS[u][0], POS[v][0]], [POS[u][1], POS[v][1]],
            color="#2f4a6d", lw=2.0, zorder=1, solid_capstyle="round")
for i, (x, y) in enumerate(POS):
    ax.scatter([x], [y], s=210, color="#111111", zorder=3)
    ax.annotate(f"$v_{{{i+1}}}$", (x, y), textcoords="offset points",
                xytext=(0, 15), ha="center", fontsize=15, zorder=4)
ax.set_xlim(-0.3, 10.3); ax.set_ylim(-0.3, 10.6)
ax.set_aspect("equal"); ax.axis("off")
fig.patch.set_facecolor("white")
fig.savefig("/home/user/Lumiere_Math/tasks/t01/figure.png",
            facecolor="white", bbox_inches="tight", pad_inches=0.25)
print("figure written")

# --------------------------------------------- distractors from misreadings
def count(edges):
    L = [[0] * N for _ in range(N)]
    for u, v in edges:
        L[u][u] += 1; L[v][v] += 1; L[u][v] -= 1; L[v][u] -= 1
    return det_bareiss([[L[i][j] for j in range(1, N)] for i in range(1, N)])

print("\ntrue value:", spanning_trees_matrix_tree())
print("\n-- drop one edge (model misses an edge) --")
for e in EDGES:
    print(f"  without {e}: {count([x for x in EDGES if x != e])}")
print("\n-- add one plausible non-edge (model invents an edge) --")
present = set(map(frozenset, EDGES))
for a, b in itertools.combinations(range(N), 2):
    if frozenset((a, b)) not in present:
        print(f"  plus ({a},{b}): {count(EDGES + [(a, b)])}")
