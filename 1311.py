N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[float('inf')] * (1 << N) for _ in range(N)]

# 초기화: 각 사람이 첫 번째 일을 맡을 때의 비용
for i in range(N):
    dp[i][1 << i] = cost[i][0]

# 모든 가능한 할당 상태에 대해
for mask in range(1 << N):
    for i in range(N):
        if mask & (1 << i):
            for j in range(N):
                if not (mask & (1 << j)):
                    new_mask = mask | (1 << j)
                    dp[j][new_mask] = min(dp[j][new_mask], dp[i][mask] + cost[j][bin(mask).count('1')])

# 최종 비용 계산
final_mask = (1 << N) - 1
min_cost = min(dp[i][final_mask] for i in range(N))

print(min_cost)
