N, Q = map(int, input().split())
arr = [int(input()) for _ in range(N)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]
prefix_sum = [[0]*(N+1) for i in range(3)]

for i in range(1, N+1):
    if arr[i-1] == 1:
        prefix_sum[arr[i-1]-1][i] = prefix_sum[arr[i-1]-1][i-1] + 1
        prefix_sum[1][i] = prefix_sum[1][i-1]
        prefix_sum[2][i] = prefix_sum[2][i-1]
    elif arr[i-1] == 2:
        prefix_sum[arr[i-1]-1][i] = prefix_sum[arr[i-1]-1][i-1] + 1
        prefix_sum[0][i] = prefix_sum[0][i-1]
        prefix_sum[2][i] = prefix_sum[2][i-1]
    
    else:
        prefix_sum[arr[i-1]-1][i] = prefix_sum[arr[i-1]-1][i-1] + 1
        prefix_sum[0][i] = prefix_sum[0][i-1]
        prefix_sum[1][i] = prefix_sum[1][i-1]


for query in queries:
    s, e = query
    print(prefix_sum[0][e] - prefix_sum[0][s-1], end=" ")
    print(prefix_sum[1][e] - prefix_sum[1][s-1], end=" ")
    print(prefix_sum[2][e] - prefix_sum[2][s-1], end=" ")
    print('')