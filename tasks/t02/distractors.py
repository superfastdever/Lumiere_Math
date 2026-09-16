import sys, itertools
sys.path.insert(0, "/home/user/Lumiere_Math/tasks/t02")
from knot import determinant, walk, arcs_and_matrix

W, N = [-2,-1,2,-1,-1,-2,1,-2,-2,1], 3
print("GTFA:", determinant(W, N))
print("\nper-crossing single switch (crossing index counted along the drawing):")
for k in range(len(W)):
    v = W[:]; v[k] = -v[k]
    print(f"   switch crossing {k}: det = {determinant(v, N)}")

def alternating(w, n):
    p, _ = walk(w, n)
    if p is None: return None
    ov = [o for _, o in p]
    return all(ov[i] != ov[(i+1) % len(ov)] for i in range(len(ov)))

print("\nnearest alternating readings (what a model gets if it assumes the diagram alternates):")
found = []
for k in range(1, 6):
    for flips in itertools.combinations(range(len(W)), k):
        v = W[:]
        for i in flips: v[i] = -v[i]
        if alternating(v, N):
            found.append((k, flips, determinant(v, N)))
    if found: break
for k, flips, d in found:
    print(f"   flip {k} crossings at {flips}: det = {d}")

rows, nar = arcs_and_matrix(W, N)
print("\narc incidence per crossing (over | under-in, under-out):")
for k, r in enumerate(rows):
    over = [i for i, x in enumerate(r) if x == 2]
    und = [i for i, x in enumerate(r) if x == -1]
    print(f"   crossing {k}: a{over[0]+1} over  |  a{und[0]+1}, a{und[1]+1} under")
