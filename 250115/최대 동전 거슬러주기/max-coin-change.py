N, M = map(int, input().split())
coin = list(map(int, input().split()))
coin.sort()
dp = [-1]*(M+1)

dp[0] = 0

for i in range(M+1):
    for j in range(N):
        if i - coin[j] >= 0 and dp[i-coin[j]] != -1:
            dp[i] = max(dp[i-coin[j]]+1, dp[i])

if dp[M] == 0:
    print(-1)
else:
    print(dp[M])