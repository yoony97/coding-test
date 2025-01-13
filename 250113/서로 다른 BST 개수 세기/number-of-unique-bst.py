n = int(input())
dp = [0]*(20)
dp[1] = 0
dp[2] = 2
dp[3] = 5
dp[4] = 14
for i in range(5, n+1):
    temp = 0
    for j in range(i):
        dp[i] += dp[j]*2
    dp[i] += n
# Write your code here!

print(dp[n])
"""
n = 1 1
n = 2 2
n = 3 5
n = 4 14, 
n = 5 42
n = 6 132
"""



84 + 28 + 10 + 4
126 + 6


