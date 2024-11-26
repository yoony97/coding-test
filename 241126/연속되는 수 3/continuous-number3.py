import sys
inputs = list(map(int, sys.stdin.read().strip().split("\n")))
n = inputs[0]
nums = inputs[1:]
cnt = 1
ans = 1
for i in range(1, n):
    if (nums[i-1] > 0 and nums[i] > 0) or (nums[i-1] < 0 and nums[i] < 0):
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1

ans = max(cnt, ans)
print(ans)