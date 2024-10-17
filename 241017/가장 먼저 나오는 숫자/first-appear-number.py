def lower_bound(target, arr, n):
    left = 0
    right = n-1
    min_idx = n
    while left <= right:
        mid = (left+right)//2
        if arr1[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    return min_idx

def check(target, arr, n):
    left = 0
    right = n-1
    min_idx = n
    while left <= right:
        mid = (left+right)//2
        if arr1[mid] > target:
            #min_idx = min(min_idx, mid)
            right = mid - 1
        elif arr1[mid] < target:
            left = mid + 1
        elif arr1[mid] == target:
            return True

    return False




N, M = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for i in arr2:
    if check(i, arr1, N):
        print(lower_bound(i, arr1, N)+1)
    else:
        print(-1)