import math
m = int(input())
a, b = map(int, input().split())

def explore(target):
    cnt = 0
    left = 0
    right = m
    while left <= right:
        mid = (left + right+1)//2
        cnt += 1

        if mid > target:
            right = mid-1
        elif mid == target:
            return cnt
        else:
            left = mid+1
        
    return -1

minimum = float('inf')
maximum = 0
for i in range(a, b+1):
    cnt = explore(i)
    maximum = max(maximum, cnt)
    minimum = min(minimum, cnt)

print(minimum,maximum)