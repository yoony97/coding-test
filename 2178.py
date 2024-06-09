import sys
from queue import deque
input = sys.stdin.read

data = input().strip().split("\n")
N, M = map(int, data[0].split(" "))
arr = [list(map(int, list(line))) for line in data[1:]]

distance = [[float('inf')] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
distance[0][0] = 1
visited[0][0] = True

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque([(0, 0)])

while queue:
    y, x = queue.popleft()
    if y == N-1 and x == M-1:
        print(distance[y][x])
        break
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 1 and not visited[ny][nx]:
            visited[ny][nx] = True
            distance[ny][nx] = distance[y][x] + 1
            queue.append((ny, nx))
