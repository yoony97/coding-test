n = int(input())
dp = [0]*(20)
dp[1] = 1
dp[2] = 2
dp[3] = 5
for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[i-2] + i-1 + i
# Write your code here!

print(dp[n])
"""
n = 1 1
n = 2 2
n = 3 5
n = 4 14, 
"""

