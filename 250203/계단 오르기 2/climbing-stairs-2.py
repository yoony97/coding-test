n = int(input())
coin = [0] + list(map(int, input().split()))
def max_coins(coins):
    n = len(coins)
    dp = [[0] * 3 for _ in range(n+1)]
    dp[1][0] = coins[0]
    dp[1][1] = coins[0]

    for i in range(2, n+1):
        dp[i][0] = dp[i-2][0] + coins[i-1]
        for j in range(1, min(i, 3)):
            dp[i][j] = max(dp[i-1][j-1] + coins[i-1], dp[i-2][j] + coins[i-1])
    
    #print(dp[n])
    return max(dp[n])

print(max_coins(coin))
