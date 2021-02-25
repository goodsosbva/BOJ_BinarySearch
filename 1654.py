import sys

k, n = map(int, sys.stdin.readline().split())

kLan = []

for i in range(k):
    i = int(input())
    kLan.append(i)

# print(kLan)

start, end = 1, max(kLan)

while start <= end:
    mid = (start + end) // 2
    Lan = 0
    # print(mid)
    for i in kLan:
        Lan += i // mid
    # print("lan", Lan)
    if Lan >= n:
        # print("1")
        start = mid + 1
    else:
        # print("2")
        end = mid - 1

print(end)