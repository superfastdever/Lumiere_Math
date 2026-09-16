import sys, math
sys.path.insert(0, "/home/user/Lumiere_Math/tasks/queue/00/t00004/build")
from toric import det, normal_form, hj, primitive
from fractions import Fraction as Fr

def ordinary_cf(d, q):
    out = []
    while q:
        out.append(d // q)
        d, q = q, d % q
    return out

def report(RAYS, name=""):
    n = len(RAYS)
    ang = [math.degrees(math.atan2(y, x)) % 360 for x, y in RAYS]
    ok = all(0 < (ang[(i+1) % n] - ang[i]) % 360 < 180 for i in range(n))
    total = sum((ang[(i+1) % n] - ang[i]) % 360 for i in range(n))
    print(f"--- {name} rays {RAYS}")
    print(f"    angles {[round(a,1) for a in ang]}  complete={ok and abs(total-360)<1e-6}")
    tot = 0
    for i in range(n):
        u, v = RAYS[i], RAYS[(i+1) % n]
        d = det(u, v)
        if d <= 0:
            print("    NOT CONVEX/CCW at", u, v); return None
        if d == 1:
            print(f"    cone <{u},{v}>: d=1 smooth, 0 divisors")
            continue
        dd, q = normal_form(u, v)
        f = hj(dd, q)
        o = ordinary_cf(dd, q)
        tot += len(f)
        trap = "TRAP: ordinary CF length differs" if len(o) != len(f) else "(same length as ordinary CF)"
        print(f"    cone <{u},{v}>: d={dd} q={q}  HJ {dd}/{q} = {f} -> {len(f)} divisors   "
              f"ordinary CF {o}   {trap}")
    print(f"    TOTAL exceptional divisors = {tot}\n")
    return tot

report([(1,0),(2,5),(-1,3),(-3,-2),(2,-3)], "candidate A")
report([(1,0),(3,4),(-2,5),(-3,-1),(1,-2)], "candidate B")
report([(1,0),(1,3),(-2,3),(-4,-3),(3,-4)], "candidate C")
report([(1,0),(4,7),(-1,2),(-5,-3),(1,-3)], "candidate D")
