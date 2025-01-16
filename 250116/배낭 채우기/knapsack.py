N, M = map(int, input().split())
dia = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0]*(M+1) #dp[i]: 무게 i 일 때 최대 보석 가치  합
#하나씩 골라야함

# Write your code here!
for j in range(N):
    for i in range(M, -1, -1):
        nw, nv = dia[j]
        if i - nw >= 0:   
            dp[i] = max(dp[i-nw] + nv, dp[i])
3print([i for i in range(M+1)])
print(dp[M])