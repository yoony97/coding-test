import sys
from queue import deque
input = sys.stdin.read

data = input().strip().split('\n')
N = int(data[0])
element = data[1:]
points = deque([])
arr = []
visited = [[False]*N for _ in range(N)]
history = []
for idx, i in enumerate(element):
    row = []
    for j in range(len(i)):
        temp = int(i[j])
        row.append(temp)
        if temp == 1:
            points.append([idx, j])
        
    arr.append(row)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

while points:
    current = points.popleft()
    if not visited[current[0]][current[1]]:
        stage = deque([current])
        visited[current[0]][current[1]] = True
        h = []
        while stage:
            current = stage.popleft()
            h.append(current)
            for i in range(4):
                nx = current[0] + dx[i]
                ny = current[1] + dy[i]
                if 0 <= nx < N and 0 <=ny < N and arr[nx][ny] == 1 and not visited[nx][ny]:
                    stage.append([nx,ny])
                    visited[nx][ny] = True
        history.append(h)

count = len(history)
nums = sorted([len(i) for i in history])

print(count)
for i in nums:
    print(i)
