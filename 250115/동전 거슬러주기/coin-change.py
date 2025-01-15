N, M = map(int, input().split())
coin = list(map(int, input().split()))
dp = [float('inf')]*(10001)
for i in coin:
    dp[i] = 1

# Write your code here!
for i in range(M+1):
    for j in range(N):
        if i - coin[j] > 0:
            dp[i] = min(dp[i-coin[j]]+1, dp[i])

if dp[M] == float('inf'):
    print(-1)
else:
    print(dp[M])