n = int(input())
dp = [0]*1001
dp[1] = 2
dp[2] = 7
dp[3] = 22
dp[4] = 71
dp[5] = 228
cnt = 0
for i in range(6, n+1):
    dp[i] = dp[i-1]*2 + dp[i-2] - dp[i-3]


# Write your code here!

"""
n == 1 2
n == 2 7
n == 3 22
n == 4 71
"""



print(dp[n]%1000000007)