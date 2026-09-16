import sys
sys.path.insert(0, "/home/user/Lumiere_Math/tasks/t01")
from build import N, EDGES, laplacian, det_bareiss

lab = lambda i: f"v{i+1}"
adj = {i: sorted(j for u, v in EDGES for i2, j in ((u, v), (v, u)) if i2 == i) for i in range(N)}
print("adjacency:")
for i in range(N):
    print(f"  {lab(i)} (deg {len(adj[i])}): " + ", ".join(lab(j) for j in adj[i]))

L = laplacian()
print("\nLaplacian L (rows v1..v8):")
for r in L:
    print("  [" + " ".join(f"{x:3d}" for x in r) + "]")

M = [[L[i][j] for j in range(N-1)] for i in range(N-1)]   # delete row/col v8
print("\nMinor M = L with row/col v8 deleted (7x7):")
for r in M:
    print("  [" + " ".join(f"{x:3d}" for x in r) + "]")

# Bareiss with a printed trace
A = [row[:] for row in M]; n = len(A); prev = 1
for k in range(n-1):
    for i in range(k+1, n):
        for j in range(k+1, n):
            A[i][j] = (A[i][j]*A[k][k] - A[i][k]*A[k][j]) // prev
    prev = A[k][k]
    print(f"\nafter step {k+1} (pivot {A[k][k]}), trailing block:")
    for r in A[k+1:]:
        print("   [" + " ".join(f"{x:6d}" for x in r[k+1:]) + "]")
print("\ndet(M) =", A[n-1][n-1], " | check:", det_bareiss(M))

v = det_bareiss(M)
print("factorisation check: 1248 = 2^5 * 3 * 13 ->", 2**5 * 3 * 13 == v)
