def dozenSearch(left, right, cnt, searchNum):
    mid = (left + right) // 2
    if left > right:
        return cnt
    else:
        if sangCards[mid] > searchNum:
            res = dozenSearch(left, mid - 1, cnt, searchNum)

        elif sangCards[mid] < searchNum:
            res = dozenSearch(mid + 1, right, cnt, searchNum)

        else:

            res = dozenSearch(left, mid - 1, cnt, searchNum)
            res += dozenSearch(mid + 1, right, cnt, searchNum)
            res += 1

        return res


from sys import stdin
_ = stdin.readline()
sangCards = sorted(map(int, stdin.readline().split()))
_ = stdin.readline()
checkCards = map(int, stdin.readline().split())

# sangCards.sort()

for i in checkCards:
    start = 0
    cnt = 0
    end = len(sangCards) - 1
    searchNum = i

    print(dozenSearch(start, end, 0, searchNum), end=" ")
