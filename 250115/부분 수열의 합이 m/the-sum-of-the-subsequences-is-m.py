n, m = map(int, input().split())
A = list(map(int, input().split()))
dp = [float('inf')]*(m+1)
dp[0] = 0
# Write your code here!
#A.sort()
for i in range(n):
    for j in range(m, -1, -1):
        if j >= A[i]:
            if dp[j - A[i]] == float('inf'):
                continue
            dp[j] = min(dp[j-A[i]]+1, dp[j])
if dp[m] == float('inf'):
    print(-1)
else:
    print(dp[m])