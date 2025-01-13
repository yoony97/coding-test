n = int(input())
dp = [0]*(n+1)

for i in range(1,n+1):
    if i <= 2:
        dp[i] = i
    else:
        dp[i] = dp[i-1] + dp[i-2]
# Write your code here!
"""
n = 1 1
n = 2 2
n = 3 3
n = 4 5
n = 5 8
n = 6 13
"""
print(dp[n]%10007)


