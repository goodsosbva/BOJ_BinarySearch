import sys

n, c = map(int, sys.stdin.readline().split())

router = []

for j in range(n):
    j = int(input())
    router.append(j)

router.sort()
# print(router)
start = 1
end = router[-1] - router[0]
result = 0
while start <= end:
    # print("=====")
    gap_mid = (start + end) // 2  # mid 는 gap 을 의미 (간격 최소 예쌍값)
    # print("mid: ", mid)
    value = router[0]
    routerCount = 1
    for i in range(1, n):
        # print("router[i]:", router[i])
        if router[i] >= value + gap_mid:  # 간격 최소 예쌍값보다 작으면 안된다 -> 문제 조건에서 간격은 항상 최대로...때문에
            # print("router[i]:", router[i])
            value = router[i]
            routerCount += 1

    if routerCount >= c:  # c 개 이상의 공유기를 설치할 수 있는 경우
        start = gap_mid + 1
        result = gap_mid

    elif routerCount < c:
        # c 개 이상의 공유기를 설치할 수 없는 경우 -> 간격을 최대로 하고 찾다보면 공유기를 다 설치하지 못하는 경우 발생
        # print("count: ", count)
        end = gap_mid - 1  # 최대 간격을 줄여주자!
        # print("end:", end)

print(result)
