import sys, itertools, collections
sys.path.insert(0, "/home/user/Lumiere_Math/tasks/t02")
from knot import determinant, walk

def canon(w):
    return tuple(w)

cands = []
L = 9
for word in itertools.product([1,-1,2,-2], repeat=L):
    w = list(word)
    # need both generators present and mixed signs (non-positive, so not obviously alternating)
    if not (any(abs(g)==1 for g in w) and any(abs(g)==2 for g in w)): continue
    if not (any(g>0 for g in w) and any(g<0 for g in w)): continue
    # no immediate cancellation s_i s_i^{-1}
    if any(w[i] == -w[i+1] for i in range(L-1)): continue
    if w[0] == -w[-1]: continue
    d = determinant(w, 3)
    if d is None or d < 12 or d > 400: continue
    # sensitivity: switching any single crossing must change the determinant
    switched = []
    for i in range(L):
        v = w[:]; v[i] = -v[i]
        dv = determinant(v, 3)
        switched.append(dv)
    if any(s == d for s in switched): continue
    distinct = len({s for s in switched if s is not None})
    if distinct < 5: continue
    cands.append((distinct, d, w, switched))

cands.sort(key=lambda t: (-t[0], -t[1]))
print(f"{len(cands)} candidate words of length {L}\n")
seen = set()
for distinct, d, w, sw in cands[:14]:
    key = (d, tuple(sorted(x for x in sw if x)))
    if key in seen: continue
    seen.add(key)
    print(f"  word {w}")
    print(f"     det = {d}   single-switch values = {sw}")
    print(f"     distinct switch values = {distinct}")
