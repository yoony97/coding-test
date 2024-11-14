n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, n-1):
    if arr[i-1] == 0:
        arr[i-1] = int(not arr[i-1])
        arr[i+1] = int(not arr[i+1])
        arr[i] = int(not arr[i])
        cnt += 1

if arr[n-1] == 0:
    arr[n-2] = int(not arr[n-2])
    arr[n-1] = int(not arr[n-1])
    cnt += 1


if sum(arr) != n:
    cnt = -1

print(cnt)