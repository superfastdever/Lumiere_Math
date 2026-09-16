import sys, itertools, collections
sys.path.insert(0, "/home/user/Lumiere_Math/tasks/t02")
from knot import determinant

for L in (8, 9):
    stats = collections.Counter()
    best = []
    for word in itertools.product([1,-1,2,-2], repeat=L):
        w = list(word)
        if not (any(abs(g)==1 for g in w) and any(abs(g)==2 for g in w)): continue
        if not (any(g>0 for g in w) and any(g<0 for g in w)): continue
        if any(w[i] == -w[i+1] for i in range(L-1)) or w[0] == -w[-1]: continue
        d = determinant(w, 3)
        if d is None:
            stats['not a knot'] += 1; continue
        stats['knot'] += 1
        stats[f'det={d}'] += 1
        if d >= 12:
            sw = []
            for i in range(L):
                v = w[:]; v[i] = -v[i]
                sw.append(determinant(v, 3))
            nd = len({s for s in sw if s is not None})
            best.append((nd, d, w, sw, sum(1 for s in sw if s == d)))
    print(f"=== length {L} ===")
    print("  ", dict(list(stats.most_common(12))))
    best.sort(key=lambda t: (-t[0], -t[1]))
    print(f"   {len(best)} words with det >= 12")
    for nd, d, w, sw, same in best[:6]:
        print(f"     {w}  det={d}  distinct_switches={nd}  switches_equal_to_det={same}")
        print(f"        switch values: {sw}")
