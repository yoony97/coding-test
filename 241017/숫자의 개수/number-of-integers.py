import sys

data = sys.stdin.read().strip().split("\n")
N, M = map(int, data[0].split())
arr1 = list(map(int, data[1].split()))
arr2 = list(map(int, data[2:]))

def lower_bound(target):
    left = 0
    right = N-1
    min_idx = N
    while left <= right:
        mid = (left+right)//2
        if arr1[mid] >= target:
            min_idx = min(mid, min_idx)
            right = mid-1
        else:
            left = mid +1
    return min_idx

def upper_bound(target):
    left = 0
    right = N-1
    min_idx = N
    while left <= right:
        mid = (left+right)//2
        if arr1[mid] > target:
            min_idx = min(mid, min_idx)
            right = mid -1
        else:
            left = mid+1
    
    return min_idx

def check(target):
    left = 0
    right = N-1
    while left <= right:
        mid = (left+right)//2
        if arr1[mid] < target:
            left = mid+1
        elif arr1[mid] > target:
            right = mid -1
        else:
            return True
    return False

for i in arr2:
    if check(i):
        print(upper_bound(i) -lower_bound(i))
        
    else:
        print(0)