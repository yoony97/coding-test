n = int(input())
arr = list(map(int, input().split()))
dp = [-float('inf')]*n
dp[0] = 0

# Write your code here!

for i in range(n):
    for j in range(i):
        if j+arr[j] >= i:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))