import math
import sys

input = sys.stdin.readline

Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, input().split())

# getDistance 부분은 비율을 생각해보시면 좋다. 길이 T 에 t만큼 나누면 왼쪽은 t 비율이 나오고 오른쪽은 T-t 즉, t:(T - t)가 될 것.
# t초 뒤에 민호의 위치 = (a, b), 강호의 위치 = (c,d), 둘 사이의 거리는 math.sqrt((a-c)**2+(b-d)**2)
def getDistance(t, T):
    a = (Bx * t + Ax * (T - t)) / T
    b = (By * t + Ay * (T - t)) / T
    c = (Dx * t + Cx * (T - t)) / T
    d = (Dy * t + Cy * (T - t)) / T
    distance = math.sqrt((a - c) ** 2 + (b - d) ** 2)
    return distance


T = 1e11
p1 = 0
p2 = T
minDistaince = getDistance(0, T)
for i in range(100):
    a = (2 * p1 + p2) // 3
    b = (p1 + 2 * p2) // 3
    if getDistance(a, T) > getDistance(b, T):
        p1 = a
    else:
        p2 = b
print(f'{getDistance((p1 + p2) // 2, T):.10f}')
