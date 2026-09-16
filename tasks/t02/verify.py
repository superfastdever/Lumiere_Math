import sys, itertools
sys.path.insert(0, "/home/user/Lumiere_Math/tasks/t02")
from knot import determinant, walk, arcs_and_matrix, det_bareiss

W, N = [-2,-1,2,-1,-1,-2,1,-2,-2,1], 3
print("braid word:", W, " strands:", N)
passages, comps = walk(W, N)
print("components:", comps, "(1 = knot)")
ov = [o for _, o in passages]
print("over/under sequence along the knot:", "".join("O" if o else "U" for o in ov))
print("alternates:", all(ov[i] != ov[(i+1) % len(ov)] for i in range(len(ov))))

rows, nar = arcs_and_matrix(W, N)
print("\narcs:", nar, " crossings:", len(W))
print("Fox colouring matrix (rows = crossings, +2 on the over-arc, -1 on each under-arc):")
for r in rows:
    print("   [" + " ".join(f"{x:2d}" for x in r) + "]")

minor = [r[:-1] for r in rows[:-1]]
d = abs(det_bareiss(minor))
print("\n|det of 9x9 minor| =", d)

def rank_mod(rows, p, ncols):
    M = [[x % p for x in r] for r in rows]
    rk, row = 0, 0
    for col in range(ncols):
        piv = next((i for i in range(row, len(M)) if M[i][col] % p), None)
        if piv is None: continue
        M[row], M[piv] = M[piv], M[row]
        inv = pow(M[row][col], p-2, p)
        M[row] = [(x*inv) % p for x in M[row]]
        for i in range(len(M)):
            if i != row and M[i][col] % p:
                f = M[i][col]
                M[i] = [(a - f*b) % p for a, b in zip(M[i], M[row])]
        row += 1; rk += 1
    return rk

print("\nindependent check by Gaussian elimination mod p (no determinant involved).")
print("rank deficiency > 1 means non-trivial p-colourings exist, i.e. p divides det(K).")
for p in [3,5,7,11,13,17,19,23,29,31,37,41,43]:
    rk = rank_mod(rows, p, nar)
    nontrivial = rk < nar - 1
    mark = "  <-- p | det" if nontrivial else ""
    assert nontrivial == (d % p == 0), f"disagreement at p={p}"
    print(f"   p={p:3d}: rank {rk} of {nar} arcs{mark}")
print("\nboth methods agree on every prime tested.")
print("determinant of the knot =", d)
