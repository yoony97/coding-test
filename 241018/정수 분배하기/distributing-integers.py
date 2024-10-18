import sys
data = sys.stdin.read().strip().split("\n")
n, m = map(int, data[0].split())
arr = list(map(int, data[1:]))

left = 1
right = max(arr)

def check(target):
    result = 0
    for i in arr:
        result += i//target
    
    return result >= m

maximum = 0
while left <= right:
    mid = (left+right)//2
    if check(mid):
        left = mid+1
        maximum = max(maximum, mid)
    else:
        right = mid - 1    


print(maximum)