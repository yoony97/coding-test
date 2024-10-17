N, M = map(int, input().split())
points = list(map(int, input().split()))

for i in range(M):
    left, right = list(map(int, input().split()))
    right += 1
    left -= 1
    cnt = 0
    for p in points:
        if left <= p <= right:
            while left <= right:
                mid = (left+right)//2
                if mid > p:
                    right = mid -1
                elif mid < p:
                    left = mid + 1
                elif mid == p:
                    cnt +=1
                    break
    print(cnt)