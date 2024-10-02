import sys

data = sys.stdin.read().strip().split('\n')
N = int(data[0].strip())
data = data[1:]
graph = []
for idx, i in enumerate(data):
    lines = list(map(int,  i.split(" ")))
    graph.append(lines)
# 플로이드-워셜 알고리즘 적용
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

# 결과 출력
for row in graph:
    print(' '.join(map(str, row)))