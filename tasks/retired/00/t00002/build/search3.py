import sys, itertools, random
sys.path.insert(0, "/home/user/Lumiere_Math/tasks/t02")
from knot import determinant, walk

def is_knot(w, n):
    perm = list(range(n))
    for g in w:
        i = abs(g)-1
        perm[i], perm[i+1] = perm[i+1], perm[i]
    seen, comps = set(), 0
    for s in range(n):
        if s in seen: continue
        comps += 1; c = s
        while c not in seen:
            seen.add(c); c = perm[c]
    return comps == 1

def alternating(w, n):
    """A diagram alternates iff over/under alternate along the whole walk."""
    passages, _ = walk(w, n)
    if passages is None: return None
    ov = [o for _, o in passages]
    return all(ov[i] != ov[(i+1) % len(ov)] for i in range(len(ov)))

def nearest_alternating(w, n):
    """Fewest crossing switches that make the diagram alternate; return its det."""
    L = len(w)
    for k in range(1, L+1):
        for flips in itertools.combinations(range(L), k):
            v = w[:]
            for i in flips: v[i] = -v[i]
            if alternating(v, n):
                return k, determinant(v, n), flips
    return None, None, None

random.seed(11)
L, n = 10, 3
pool = []
tried = 0
while tried < 90000 and len(pool) < 400:
    tried += 1
    w = [random.choice([1,-1,2,-2]) for _ in range(L)]
    if not (any(abs(g)==1 for g in w) and any(abs(g)==2 for g in w)): continue
    if not (any(g>0 for g in w) and any(g<0 for g in w)): continue
    if any(w[i] == -w[i+1] for i in range(L-1)) or w[0] == -w[-1]: continue
    if not is_knot(w, n): continue
    if alternating(w, n): continue              # we want NON-alternating
    d = determinant(w, n)
    if d is None or d < 30 or d > 300: continue
    sw = []
    for i in range(L):
        v = w[:]; v[i] = -v[i]
        sw.append(determinant(v, n))
    if any(s == d for s in sw): continue
    pool.append((len({s for s in sw if s}), d, w, sw))

pool.sort(key=lambda t: (-t[0], -t[1]))
print(f"tried {tried} words, kept {len(pool)}\n")
for nd, d, w, sw in pool[:5]:
    k, ad, flips = nearest_alternating(w, n)
    print(f"word {w}")
    print(f"   det = {d}   non-alternating")
    print(f"   distinct single-switch dets = {nd}: {sorted(set(s for s in sw if s))}")
    print(f"   nearest alternating diagram: {k} switch(es) at {flips}, det = {ad}")
    print()
