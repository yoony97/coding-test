n = int(input())
dp = [0]*1001
dp[1] = 2
dp[2] = 7
cnt = 0
for i in range(3, n+1):
    dp[i] = dp[i-1]*2 + dp[i-2]*4 - cnt
    cnt += 1
    
# Write your code here!

"""
n == 1 2
n == 2 7
n == 3 22
n == 4 71
"""



print(dp[n]%1000000007)