"""Braid closures: walk the diagram, extract arcs, compute the knot determinant.

Convention: generator +i means the strand arriving at height i passes OVER the
strand arriving at height i+1; -i means it passes UNDER. Heights are 1..n.
"""
import itertools
from fractions import Fraction

def walk(word, n):
    """Walk the closure. Returns the cyclic list of passages (crossing_index, is_over)
    and the number of components."""
    # component detection first
    perm = list(range(n))
    for g in word:
        i = abs(g) - 1
        perm[i], perm[i+1] = perm[i+1], perm[i]
    seen, comps = set(), 0
    for s in range(n):
        if s in seen:
            continue
        comps += 1
        c = s
        while c not in seen:
            seen.add(c)
            c = perm[c]
    if comps != 1:
        return None, comps

    passages = []
    h, start = 0, 0          # height index 0-based, start of the walk
    steps = 0
    while True:
        for k, g in enumerate(word):
            i = abs(g) - 1
            if h == i:
                passages.append((k, g > 0))     # from height i: over iff g>0
                h = i + 1
            elif h == i + 1:
                passages.append((k, g < 0))     # from height i+1: over iff g<0
                h = i
        steps += 1
        if h == start:
            break
        if steps > 4 * n:
            raise RuntimeError("walk did not close")
    return passages, 1

def arcs_and_matrix(word, n):
    """Fox colouring matrix: each crossing gives 2*over - under_in - under_out = 0."""
    passages, comps = walk(word, n)
    if passages is None:
        return None
    m = len(passages)
    assert m == 2 * len(word), (m, len(word))

    # arc id for each passage position: arcs are maximal runs between UNDER passages.
    # the arc entering passage p is arc[p]; a new arc starts after each under-passage.
    under_pos = [p for p, (_, ov) in enumerate(passages) if not ov]
    assert len(under_pos) == len(word), "each crossing must be passed under once"
    arc_of_pos = [None] * m
    aid = 0
    first = under_pos[0]
    for step in range(m):
        p = (first + 1 + step) % m
        arc_of_pos[p] = aid
        if not passages[p][1]:          # this passage goes under -> arc ends here
            aid = (aid + 1) % len(word)
    nar = len(word)

    rows = []
    for k in range(len(word)):
        over_arc = under_in = under_out = None
        for p, (ck, ov) in enumerate(passages):
            if ck != k:
                continue
            if ov:
                over_arc = arc_of_pos[p]
            else:
                under_in = arc_of_pos[p]
                under_out = arc_of_pos[(p + 1) % m]
        row = [0] * nar
        row[over_arc] += 2
        row[under_in] -= 1
        row[under_out] -= 1
        rows.append(row)
    return rows, nar

def det_bareiss(M):
    M = [r[:] for r in M]; n = len(M)
    if n == 0: return 1
    sign, prev = 1, 1
    for k in range(n-1):
        if M[k][k] == 0:
            for i in range(k+1, n):
                if M[i][k] != 0:
                    M[k], M[i] = M[i], M[k]; sign = -sign; break
            else: return 0
        for i in range(k+1, n):
            for j in range(k+1, n):
                num = M[i][j]*M[k][k] - M[i][k]*M[k][j]
                assert num % prev == 0
                M[i][j] = num // prev
        prev = M[k][k]
    return sign * M[n-1][n-1]

def determinant(word, n):
    out = arcs_and_matrix(word, n)
    if out is None: return None
    rows, nar = out
    minor = [r[:-1] for r in rows[:-1]]
    return abs(det_bareiss(minor))

def count_colourings(word, n, p):
    """Brute force: number of Fox p-colourings. Should equal p * gcd-ish structure;
    p divides det(K) iff a non-trivial colouring exists."""
    out = arcs_and_matrix(word, n)
    rows, nar = out
    total = 0
    for assign in itertools.product(range(p), repeat=nar):
        if all(sum(c * a for c, a in zip(row, assign)) % p == 0 for row in rows):
            total += 1
    return total

KNOWN = {
    "trefoil 3_1":      ([1,1,1], 2, 3),
    "figure-eight 4_1": ([1,-2,1,-2], 3, 5),
    "5_1":              ([1,1,1,1,1], 2, 5),
    "5_2":              ([1,1,1,2,-1,2], 3, 7),
    "6_1":              ([1,1,-2,1,-2,-2], 3, 9),
    "6_2":              ([1,1,1,-2,1,-2], 3, 11),
    "6_3":              ([1,1,-2,1,-2,-2], 3, 9),
}
if __name__ == "__main__":
    print("validation against known determinants")
    for name, (w, n, expected) in KNOWN.items():
        d = determinant(w, n)
        comps = walk(w, n)[1]
        flag = "ok" if d == expected else f"MISMATCH (expected {expected})"
        print(f"  {name:18s} braid={w} n={n} comps={comps} det={d}  {flag}")
