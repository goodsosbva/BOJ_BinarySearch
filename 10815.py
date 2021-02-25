n = int(input())
sangCards = list(map(int, input().split()))

m = int(input())
checkCards = list(map(int, input().split()))

sangCards.sort()


for i in range(m):
    start = 0
    end = n - 1
    # target = checkCards[i]

    while start <= end:
        mid = (start + end) // 2

        if sangCards[mid] < checkCards[i]:
            start = mid + 1

        elif sangCards[mid] == checkCards[i]:
            print(1, end=" ")
            break

        elif sangCards[mid] > checkCards[i]:
            end = mid - 1

        if start > end:
            print(0, end=" ")
            break






