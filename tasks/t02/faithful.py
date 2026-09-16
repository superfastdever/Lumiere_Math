"""Recover the braid word from the DRAWN geometry and compare with the intended word."""
import sys, math
sys.path.insert(0, "/home/user/Lumiere_Math/tasks/t02")
from draw import paths, over_at, under_at, CENTER, HW, R, W, NC
from knot import determinant

def level_before(sidx, k):
    th, rr, _ = paths[sidx]
    target = CENTER[k] - HW - 1e-9
    best = min(range(len(th)), key=lambda j: abs(th[j]-target))
    return min(range(3), key=lambda L: abs(R[L]-rr[best]))

recovered = []
for k in range(NC):
    lo_over = level_before(over_at[k], k)
    lo_under = level_before(under_at[k], k)
    i = min(lo_over, lo_under)
    assert abs(lo_over - lo_under) == 1, (k, lo_over, lo_under)
    # generator is +(i+1) when the strand arriving at the LOWER level passes over
    sign = 1 if lo_over == i else -1
    recovered.append(sign * (i+1))

print("intended braid word :", W)
print("recovered from geometry:", recovered)
print("match:", recovered == W)
print("determinant of the recovered word:", determinant(recovered, 3))

# crossing geometry quality
def sample(sidx, k):
    th, rr, _ = paths[sidx]
    lo, hi = CENTER[k]-0.02, CENTER[k]+0.02
    pts = [(r*math.cos(t), r*math.sin(t)) for t, r in zip(th, rr) if lo <= t <= hi]
    return pts

print("\ncrossing angles (degrees between the two strands) and separation from neighbours:")
centers = []
for k in range(NC):
    a, b = sample(over_at[k], k), sample(under_at[k], k)
    va = (a[-1][0]-a[0][0], a[-1][1]-a[0][1])
    vb = (b[-1][0]-b[0][0], b[-1][1]-b[0][1])
    cosang = (va[0]*vb[0]+va[1]*vb[1])/(math.hypot(*va)*math.hypot(*vb))
    ang = math.degrees(math.acos(max(-1, min(1, cosang))))
    mid = ((a[len(a)//2][0]+b[len(b)//2][0])/2, (a[len(a)//2][1]+b[len(b)//2][1])/2)
    centers.append(mid)
    print(f"   crossing {k}: {min(ang, 180-ang):5.1f} deg")
print("\nminimum distance between two crossing points:",
      round(min(math.dist(centers[i], centers[j])
                for i in range(NC) for j in range(i+1, NC)), 3))
