import math

m = int(input())
a, b = map(int, input().split())

def explore(target):
    cnt = 0
    left = 0
    right = m

    while left <= right:
        mid = (left + right+1) // 2  # 정수 나눗셈으로 mid 계산
        cnt += 1

        if mid > target:
            right = mid - 1
        elif mid < target:
            left = mid + 1
        else:
            return cnt  # 찾으면 탐색 횟수 반환

    return -1  # (실제로 이 경우는 발생하지 않음)

minimum = float('inf')
maximum = 0

# 모든 i에 대해 이진 탐색 수행
for i in range(a, b + 1):
    cnt = explore(i)
    minimum = min(minimum, cnt)
    maximum = max(maximum, cnt)

print(minimum, maximum)