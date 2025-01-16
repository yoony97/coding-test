N, M = map(int, input().split())
dia = [tuple(map(int, input().split())) for _ in range(N)]
#w, v = list(w), list(v)
# 여러개 고를수 있어
dp = [0]*(M+1)
# Write your code here!

for j in range(N):
    for i in range(M+1):
        if i-dia[j][0] >= 0:
            dp[i] = max(dp[i-dia[j][0]] + dia[j][1], dp[i])

print(dp[M])