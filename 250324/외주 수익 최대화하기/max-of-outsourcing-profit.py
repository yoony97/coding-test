n = int(input())
job = []
for i in range(n):
    t, p = map(int, input().split())
    job.append((t, p))

dp = [0]*(n+5)
#dp[i] : i 번째 날에 벌 수 있는 최대 수익
#dp[i] = max(dp[i-t-1]+p, p)
for i in range(n-1, -1, -1):
    t, p = job[i]
    dp[i] = max(p + dp[i+t], dp[i+1])
    
print(dp[0])
