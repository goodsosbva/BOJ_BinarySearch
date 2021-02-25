import sys

n, m = map(int, sys.stdin.readline().split())

trees = list(map(int, input().split()))


start, end = 1, max(trees)

while start <= end:
    #print("----")
    mid = (start + end) // 2
    tree = 0
    #print("start, mid, end:",start, mid, end)
    for i in trees:
        if i >= mid:
            tree += (i - mid)
    #print("tree:", tree)
    if tree >= m:
        #print("1")
        start = mid + 1
    else:
        #print("2")
        end = mid - 1

print(end)