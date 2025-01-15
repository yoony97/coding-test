n, m = map(int, input().split())
A = list(map(int, input().split()))
dp = [-1]*(m+1)
dp[0] = 1 #아무것도 안고르면 0


# Write your code here!
for j in range(n):
    for i in range(m, -1, -1):
        if i >= A[j] and dp[i-A[j]] != -1:
            dp[i] = max(dp[i-A[j]]+1, dp[i])

if dp[m] != -1:
    print('Yes')
else:
    print("No")
#print(dp)