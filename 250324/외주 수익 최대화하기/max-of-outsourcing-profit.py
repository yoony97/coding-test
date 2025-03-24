n = int(input())
job = []
for i in range(n):
    t, p = map(int, input().split())
    job.append((t, p))

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    t, p = job[i]
    if i + t <= n:
        dp[i] = max(p + dp[i + t], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])