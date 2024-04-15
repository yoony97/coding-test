def tsp(N, cost):
    dp = [[float('inf')] * (1 << N) for _ in range(N)]
    dp[0][1] = 0  # 시작 도시에서 출발

    for mask in range(1 << N):
        for i in range(N):
            if mask & (1 << i):
                for j in range(N):
                    if not mask & (1 << j) and cost[i][j] != 0:
                        new_mask = mask | (1 << j)
                        dp[j][new_mask] = min(dp[j][new_mask], dp[i][mask] + cost[i][j])
    final_mask = (1 << N) - 1
    min_cost = float('inf')
    for i in range(1, N):
        if dp[i][final_mask] < float('inf') and cost[i][0] != 0:
            min_cost = min(min_cost, dp[i][final_mask] + cost[i][0])

    return min_cost

N = int(input())
cost = [[0]*N for _ in range(N)]
for i in range(N):
    s = [int(i) for i in input().split(" ")]
    for j in range(N):
        cost[i][j] = s[j]

print(tsp(N,cost))

