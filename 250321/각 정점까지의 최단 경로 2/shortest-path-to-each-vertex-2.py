n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graphs = [[float('inf')]*n for i in range(n)]

for i in range(n):
    graphs[i][i] = 0 

for s, e, v in edges:
    #graphs[s-1][e-1] = v
    graphs[s-1][e-1] = min(graphs[s-1][e-1], v)  # 여러 간선이 있을 경우 최소값 선택

for k in range(n):
    for i in range(n):
        for j in range(n):
            graphs[i][j] = min(graphs[i][j], graphs[i][k]+ graphs[k][j])



for graph in graphs:
    for i in graph:
        if i == float('inf'):
            i = -1
        print(i, end=' ')
    print()
    

# Please write your code here.
