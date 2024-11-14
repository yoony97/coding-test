n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, n-1):
    if arr[i-1] == 0:
        arr[i-1] = not arr[i-1]
        arr[i+1] = not arr[i+1]
        arr[i] = not arr[i]
        cnt += 1
    
if arr[-1] == 0:
    cnt = -1

print(cnt)