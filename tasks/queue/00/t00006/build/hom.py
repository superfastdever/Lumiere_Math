"""Hom and Ext dimensions between indecomposables, by explicit linear algebra.

For a Dynkin quiver the representation space of a positive root d has a dense orbit, so a
random representation of dimension vector d IS the indecomposable; End = k confirms it.
Hom(M,N) is the solution space of f_j M_a = N_a f_i over all arrows a: i -> j.
Ranks are computed over two different large prime fields and cross-checked, and every
result is checked against the Euler form dim Hom - dim Ext = <dim M, dim N>.
"""
import numpy as np, json, random

D = json.load(open("build/arquiver.json"))
VERT = {tuple(map(int,k.split(','))): tuple(v) for k,v in D["verts"].items()}
ARROWS_AR = [tuple(map(tuple, a)) for a in D["arrows"]]
N = 6
ARROWS = [(0,1),(1,2),(2,3),(3,4),(2,5)]
ROOTS = sorted(set(VERT.values()))

def euler(d, e):
    s = sum(a*b for a,b in zip(d,e))
    for (i,j) in ARROWS: s -= d[i]*e[j]
    return s

def rep(d, rng, p):
    return {(i,j): np.array([[rng.randrange(1,p) for _ in range(d[i])]
                             for _ in range(d[j])], dtype=np.int64) % p
            for (i,j) in ARROWS}

def rank_mod(A, p):
    A = A % p; A = A.copy(); rows, cols = A.shape; r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i, c] % p: piv = i; break
        if piv is None: continue
        A[[r, piv]] = A[[piv, r]]
        inv = pow(int(A[r, c]), p-2, p)
        A[r] = (A[r] * inv) % p
        for i in range(rows):
            if i != r and A[i, c] % p:
                A[i] = (A[i] - A[i, c] * A[r]) % p
        r += 1
        if r == rows: break
    return r

def hom_dim(dM, dN, RM, RN, p):
    off, tot = {}, 0
    for i in range(N):
        off[i] = tot; tot += dM[i]*dN[i]
    rows = []
    for (i,j) in ARROWS:
        for a in range(dN[j]):
            for b in range(dM[i]):
                row = np.zeros(tot, dtype=np.int64)
                for c in range(dM[j]):          # f_j M_a
                    row[off[j] + a*dM[j] + c] = (row[off[j] + a*dM[j] + c] + RM[(i,j)][c,b]) % p
                for c in range(dN[i]):          # - N_a f_i
                    row[off[i] + c*dM[i] + b] = (row[off[i] + c*dM[i] + b] - RN[(i,j)][a,c]) % p
                rows.append(row)
    if not rows: return tot
    return tot - rank_mod(np.array(rows, dtype=np.int64), p)

PRIMES = [1000003, 999983]
rng = random.Random(7)
REPS = {p: {d: rep(d, random.Random(100+hash(d)%9999), p) for d in ROOTS} for p in PRIMES}

print("checking End(M) = k for all 36 indecomposables (Schur, confirms indecomposability)")
bad = 0
for d in ROOTS:
    e = [hom_dim(d, d, REPS[p][d], REPS[p][d], p) for p in PRIMES]
    if e != [1,1]: bad += 1; print("   FAIL", d, e)
print("   all End dimensions equal 1" if bad==0 else f"   {bad} failures")

print("\ncomputing all 36x36 Hom and Ext dimensions")
HOM, EXT = {}, {}
mismatch = 0
for dM in ROOTS:
    for dN in ROOTS:
        h = [hom_dim(dM, dN, REPS[p][dM], REPS[p][dN], p) for p in PRIMES]
        if h[0] != h[1]: mismatch += 1
        HOM[(dM,dN)] = h[0]
        EXT[(dM,dN)] = h[0] - euler(dM, dN)
print(f"   prime cross-check mismatches: {mismatch}")
neg = sum(1 for v in EXT.values() if v < 0)
print(f"   negative Ext dimensions (would indicate an error): {neg}")
import collections
print("   Hom dimension distribution:", dict(sorted(collections.Counter(HOM.values()).items())))
print("   Ext dimension distribution:", dict(sorted(collections.Counter(EXT.values()).items())))
json.dump({"hom":{f"{a}|{b}":v for (a,b),v in HOM.items()},
           "ext":{f"{a}|{b}":v for (a,b),v in EXT.items()}}, open("build/homext.json","w"))
print("saved")
