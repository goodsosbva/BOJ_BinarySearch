import sys
import math

input = sys.stdin.readline

x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())


# 비율에 따른 거리
def minho(p):
    return [x1 + (x2 - x1) * (p / 100), y1 + (y2 - y1) * (p / 100)]


def kangho(p):
    return [x3 + (x4 - x3) * (p / 100), y3 + (y4 - y3) * (p / 100)]


fp = 0
lp = 100
length = math.sqrt(pow(10000, 2) + pow(10000, 2))

while lp - fp >= 1e-7:
    p1 = (fp * 2 + lp) / 3
    p2 = (fp + lp * 2) / 3

    minhoP1 = minho(p1)
    minhoP2 = minho(p2)
    kanghoK1 = kangho(p1)
    kanghoK2 = kangho(p2)

    distanceP1 = math.sqrt(pow(minhoP1[0] - kanghoK1[0], 2) + pow(minhoP1[1] - kanghoK1[1], 2))
    distanceP2 = math.sqrt(pow(minhoP2[0] - kanghoK2[0], 2) + pow(minhoP2[1] - kanghoK2[1], 2))

    length = min(length, min(distanceP1, distanceP2))

    if distanceP1 >= distanceP2:
        fp = p1
    else:
        lp = p2

print('%.10f' % length)
