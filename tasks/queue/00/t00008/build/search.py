"""Hardened plumbing graph: a cycle with trees hanging off it.

Design targets, taken from the failure of the star-shaped example:
  * NOT star-shaped and not even a tree, so the Hirzebruch-Jung / Seifert
    continued-fraction shortcut does not apply at all;
  * branch continued fractions with DIFFERENT numerators, so no uniform collapse;
  * still negative definite, checked by leading principal minors;
  * an invariant factor structure that is not a single obvious prime power.
"""
import sympy as sp, random, itertools
from sympy.matrices.normalforms import smith_normal_form

def matrix(W, E):
    n = len(W)
    M = sp.zeros(n, n)
    for i, w in enumerate(W): M[i, i] = w
    for a, b in E: M[a, b] += 1; M[b, a] += 1
    return M

def negdef(M):
    n = M.shape[0]
    return all((-M)[:k, :k].det() > 0 for k in range(1, n + 1))

def analyse(W, E):
    M = matrix(W, E)
    if not negdef(M): return None
    S = smith_normal_form(sp.Matrix(M))
    d = [abs(S[i, i]) for i in range(M.shape[0])]
    nt = [x for x in d if x != 1]
    return dict(M=M, det=abs(M.det()), inv=nt)

# cycle C0-C1-C2-C3-C0, with a chain hanging off each cycle node
def build(cyc_w, chains):
    W = list(cyc_w); E = [(0,1),(1,2),(2,3),(3,0)]
    for node, ws in chains:
        prev = node
        for w in ws:
            W.append(w); idx = len(W)-1; E.append((prev, idx)); prev = idx
    return W, E

def hj(ws):
    from fractions import Fraction as F
    x = F(-ws[-1])
    for b in reversed(ws[:-1]):
        x = (-b) - 1/x
    return x

rng = random.Random(4)
best = []
for _ in range(4000):
    cyc = [rng.choice([-3,-3,-4,-5,-2]) for _ in range(4)]
    chains = []
    for node in range(4):
        L = rng.choice([2,3,4])
        chains.append((node, [rng.choice([-2,-2,-2,-3,-4]) for _ in range(L)]))
    W, E = build(cyc, chains)
    r = analyse(W, E)
    if not r: continue
    nums = [hj([w for w in ws]).numerator for _, ws in chains]
    if len(set(nums)) < 4: continue          # demand DIFFERENT branch numerators
    if len(r["inv"]) < 2: continue           # demand a non-cyclic group
    if r["det"] > 200000: continue
    best.append((len(r["inv"]), r, W, E, nums, cyc, chains))

best.sort(key=lambda t: (-t[0], t[1]["det"]))
print(f"{len(best)} candidates\n")
for k, r, W, E, nums, cyc, chains in best[:5]:
    print(f"  vertices {len(W)}  det {r['det']} = {sp.factorint(r['det'])}")
    print(f"     invariant factors {r['inv']}")
    print(f"     cycle weights {cyc}, branch numerators {nums}")
    print(f"     chains {[ws for _, ws in chains]}")
    print()
