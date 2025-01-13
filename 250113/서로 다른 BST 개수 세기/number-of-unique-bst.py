n = int(input())
dp = [0]*(20)
dp[1] = 1
dp[2] = 2
dp[3] = 5
for i in range(4, n+1):
    temp = 0
    for j in range(i):
        temp += dp[j]
    dp[i] = temp + j*2
# Write your code here!

print(dp[n])
"""
n = 1 1
n = 2 2
n = 3 5
n = 4 14, 
"""

