n = int(input())
dp = [0]*(n+1)
dp[2] = 1
if n >= 3:
    dp[3] = 1

for i in range(4, n+1):
    dp[i] = dp[i-2] + dp[i-3]

#print(dp)
print(dp[n]%10007)

# Write your code here!

"""
n = 1 0
n = 2 1
n = 3 1 
n = 4 1
n = 5 2
"""