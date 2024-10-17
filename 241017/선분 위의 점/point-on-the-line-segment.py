N, M = map(int, input().split())
points = list(map(int, input().split()))

for i in range(M):
    left, right = list(map(int, input().split()))
    right += 1
    left -= 1
    cnt = 0
    for p in points:
        if left <= p <= right:
            cnt +=1
    print(cnt)