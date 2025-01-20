n = int(input())
coin = [0] + list(map(int, input().split()))
def max_coins(coins):
    n = len(coins)
    dp = [[-float('inf')] * 4 for _ in range(n)]
    dp[0][0] = 0
    dp[1][0] = coins[0]

    for i in range(2, n):
        dp[i][0] = dp[i-2][0] + coins[i-2]
        for j in range(1, min(i+1, 4)):
            dp[i][j] = max(dp[i-1][j-1] + coins[i], dp[i-2][j] + coins[i])

    return max(dp[n-1])

print(max_coins(coin))