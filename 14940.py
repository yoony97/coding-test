import sys
from queue import deque

input = sys.stdin.read

data = input().strip().split('\n')
N,M = map(int, data[0].split(" "))
element = data[1:]

target = (0,0)
arr = []
score = [[-1]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]
for i in range(N):
    row = list(map(int, element[i].split(" ")))
    for j in range(M):
        if row[j] == 2:
            target = (i, j)
            score[i][j] = 0
            visited[i][j] = True
        elif row[j] == 0:
            score[i][j] = 0
    
    arr.append(row)


points = deque([target])
dx = [1,-1, 0, 0]
dy = [0, 0, -1, 1]

while points:
    y, x = points.popleft()
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 1 and not visited[ny][nx]:
            score[ny][nx] = score[y][x] + 1
            points.append((ny,nx))
            visited[ny][nx] = True

for i in score:
    print(' '.join([str(j) for j in i]))