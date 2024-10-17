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



N, M = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for i in arr2:
    answer = lower_bound(i, arr1, N)
    if answer == N:
        print(-1)
    else:
        print(answer+1)