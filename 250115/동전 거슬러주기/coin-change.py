N, M = map(int, input().split())
coin = list(map(int, input().split()))
dp = [float('inf')]*(M+1)
for i in coin:
    dp[i] = 1

# Write your code here!
for i in range(M+1):
    for j in range(N):
        if i - coin[j] > 0:
            dp[i] = min(dp[i-coin[j]]+1, dp[i])

print(dp[-1])