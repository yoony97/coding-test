n, t = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 1
ans = 1


for i in range(n):
    if nums[i] > t:
        cnt += 1
    else:
        cnt = 1
        ans = max(ans, cnt)
ans = max(ans, cnt)
print(ans)