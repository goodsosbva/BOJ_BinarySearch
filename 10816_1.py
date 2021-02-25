from sys import stdin

n = stdin.readline()
sanCards = sorted(map(int, stdin.readline().split()))
m = stdin.readline()
checkCards = map(int, stdin.readline().split())


def binary(num, sangCards, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if num == sangCards[mid]:
        return sangCards[start:end + 1].count(num)
    elif num < sangCards[mid]:
        return binary(num, sangCards, start, mid - 1)
    else:
        return binary(num, sangCards, mid + 1, end)


sanCardsDic = {}
for num in sanCards:
    start = 0
    end = len(sanCards) - 1
    if num not in sanCardsDic:
        sanCardsDic[num] = binary(num, sanCards, start, end)
# print(n_dic)
print(' '.join(str(sanCardsDic[x]) if x in sanCardsDic else '0' for x in checkCards))
