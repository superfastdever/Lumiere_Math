"""Task 01: adjacency extraction from a crossing-rich straight-line drawing.

Builds the figure, then computes the spanning-tree count two independent ways.
"""
import itertools, math, random
from fractions import Fraction

# ---------------------------------------------------------------- graph
# 8 vertices, 14 edges, alternating degree sequence (4,3,4,3,4,3,4,3).
# Not vertex-transitive, not a named graph: a model that assumes regularity
# or pattern-matches a textbook cubic graph gets the wrong Laplacian.
N = 8
EDGES = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 0),
    (0, 4), (1, 6), (2, 5), (3, 7), (0, 2), (4, 6),
]
assert len(set(map(frozenset, EDGES))) == len(EDGES), "duplicate edge"

def degrees():
    d = [0] * N
    for u, v in EDGES:
        d[u] += 1
        d[v] += 1
    return d

# ------------------------------------------------- spanning trees, method 1
def laplacian():
    L = [[0] * N for _ in range(N)]
    for u, v in EDGES:
        L[u][u] += 1
        L[v][v] += 1
        L[u][v] -= 1
        L[v][u] -= 1
    return L

def det_bareiss(M):
    """Fraction-free Gaussian elimination. Exact integer determinant."""
    M = [row[:] for row in M]
    n = len(M)
    sign, prev = 1, 1
    for k in range(n - 1):
        if M[k][k] == 0:
            for i in range(k + 1, n):
                if M[i][k] != 0:
                    M[k], M[i] = M[i], M[k]
                    sign = -sign
                    break
            else:
                return 0
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = M[i][j] * M[k][k] - M[i][k] * M[k][j]
                assert num % prev == 0, "Bareiss division not exact"
                M[i][j] = num // prev
        prev = M[k][k]
    return sign * M[n - 1][n - 1]

def spanning_trees_matrix_tree():
    L = laplacian()
    minor = [[L[i][j] for j in range(1, N)] for i in range(1, N)]
    return det_bareiss(minor)

# ------------------------------------------------- spanning trees, method 2
def spanning_trees_bruteforce():
    count = 0
    for subset in itertools.combinations(EDGES, N - 1):
        parent = list(range(N))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        ok = True
        for u, v in subset:
            ru, rv = find(u), find(v)
            if ru == rv:
                ok = False
                break
            parent[ru] = rv
        if ok:
            count += 1
    return count

# ------------------------------------------------------------- layout search
def seg_point_dist(p, a, b):
    ax, ay = a; bx, by = b; px, py = p
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    t = 0.0 if L2 == 0 else max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / L2))
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy))

def seg_seg_cross(a, b, c, d):
    """True only for a proper interior crossing."""
    def o(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    o1, o2, o3, o4 = o(a, b, c), o(a, b, d), o(c, d, a), o(c, d, b)
    return (o1 * o2 < 0) and (o3 * o4 < 0)

def evaluate(pos):
    """Return (min clearance, min crossing separation, crossing count)."""
    clear = min(
        seg_point_dist(pos[w], pos[u], pos[v])
        for u, v in EDGES for w in range(N) if w not in (u, v)
    )
    pts = []
    for (a, b), (c, d) in itertools.combinations(EDGES, 2):
        if len({a, b, c, d}) < 4:
            continue
        if seg_seg_cross(pos[a], pos[b], pos[c], pos[d]):
            # intersection point of the two lines
            x1, y1 = pos[a]; x2, y2 = pos[b]; x3, y3 = pos[c]; x4, y4 = pos[d]
            den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
            pts.append((x1 + t * (x2 - x1), y1 + t * (y2 - y1)))
    sep = min(
        [math.dist(p, pos[w]) for p in pts for w in range(N)]
        + [math.dist(p, q) for p, q in itertools.combinations(pts, 2)]
        or [9.9]
    )
    return clear, sep, len(pts)

def search(seed=0, iters=240000):
    rng = random.Random(seed)
    best, best_pos = None, None
    for _ in range(iters):
        pos = [(rng.uniform(0, 10), rng.uniform(0, 10)) for _ in range(N)]
        if min(math.dist(pos[i], pos[j]) for i, j in itertools.combinations(range(N), 2)) < 2.0:
            continue
        clear, sep, nx = evaluate(pos)
        if nx < 7 or clear < 0.55 or sep < 0.45:
            continue
        score = min(clear, sep) + 0.03 * nx
        if best is None or score > best:
            best, best_pos = score, pos
    return best, best_pos

if __name__ == "__main__":
    mt = spanning_trees_matrix_tree()
    bf = spanning_trees_bruteforce()
    print("degrees        :", degrees())
    print("edges          :", len(EDGES))
    print("matrix-tree    :", mt)
    print("brute force    :", bf)
    print("agree          :", mt == bf)
    score, pos = search()
    print("layout score   :", score)
    print("layout metrics :", evaluate(pos) if pos else None)
    print("positions      :", [(round(x, 3), round(y, 3)) for x, y in pos] if pos else None)
