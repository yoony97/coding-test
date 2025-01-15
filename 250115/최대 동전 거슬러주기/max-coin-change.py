N, M = map(int, input().split())
coin = list(map(int, input().split()))
dp = [0]*(M+1)

dp[0] = 0 

for i in range(M+1):
    for j in range(N):
        if i >= coin[j]:
            dp[i] = max(dp[i-coin[j]]+1, dp[i])

print(dp[M])