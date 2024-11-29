N, H, T = map(int,input().split())
maps =  list(map(int,input().split()))

min_cost = float('inf')
for i in range(N-T+1):
    cost = 0
    for j in range(i, i+T):
        cost += abs(H - maps[j])
    
    min_cost = min(min_cost, cost)

print(min_cost)