import sys
data  = sys.stdin.read().strip().split("\n")
N, M = map(int, data[0].split())
arr1 = list(map(int, data[1].split()))
arr2 = list(map(int, data[2:]))

for i in arr2:
    left, right = 0, N-1
    isfind = False
    while left <= right:
        m = (left+right)//2
        if arr1[m] > i:
            right = m-1
        elif arr1[m] < i:
            left = m+1
        elif arr1[m] == i:
            print(m+1)
            isfind = True
            break
    if not isfind:
        print(-1)