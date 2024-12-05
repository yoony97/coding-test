import sys
from collections import deque
inputs = sys.stdin.read().strip().split("\n")
L = (0,0)
R = (0,0)
B = (0,0)
for i in range(10):
    for j in range(10):
        if inputs[i][j] == 'L':
            L = (i, j)
        if inputs[i][j] == 'R':
            R = (i, j)
        if inputs[i][j] == 'B':
            B = (i, j)


candidate = deque([(L[0], L[1], 0)])
visited = [[False for _ in range(10)] for i in range(10)]
visited[L[0]][L[1]] = True
dx = [1, -1, 0, 0]
dy = [0, 0, -1,  1 ]

def dist(current, B):
    return abs(current[0] - B[0]) + abs(current[1] - B[1])


while True:
    cx, cy, c= candidate.popleft()
    current_dist = dist((cx,cy), B)
    if (cx, cy) == B:
        print(c-1)
        break
        
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nx < 10 and 0 <= ny < 10 and (nx, ny) != R and visited[nx][ny] == False:
            new_dist = dist((nx, ny), B)
            if new_dist <= current_dist:
                candidate.append((nx,ny, c+1))
                visited[nx][ny] = True



