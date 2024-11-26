import sys
inputs = list(map(int, sys.stdin.read().strip().split("\n")))
n = inputs[0]
nums = inputs[1:]

cnt = 1
ans = 1 

for i in range(n):
    if nums[i-1] < nums[i]:
        cnt += 1
    else:
        ans = max(cnt, ans)
        cnt = 1

ans = max(cnt, ans)
print(ans)
