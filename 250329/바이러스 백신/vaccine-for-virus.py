from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

virus_positions = []
empty_count = 0
answer = float('inf')

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus_positions.append((i, j))
        elif arr[i][j] == 0:
            empty_count += 1

def simulate(selected):
    visited = [[False]*N for _ in range(N)]
    q = deque()
    time = 0
    spread = 0

    for x, y in selected:
        q.append((x, y, 0))
        visited[x][y] = True

    while q:
        x, y, t = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and arr[nx][ny] != 1:
                    visited[nx][ny] = True
                    if arr[nx][ny] == 0:
                        spread += 1
                        time = t + 1
                    q.append((nx, ny, t + 1))

    return time if spread == empty_count else float('inf')

def backtrack(start, selected):
    global answer
    if len(selected) == M:
        answer = min(answer, simulate(selected))
        return

    for i in range(start, len(virus_positions)):
        selected.append(virus_positions[i])
        backtrack(i + 1, selected)
        selected.pop()

backtrack(0, [])
print(-1 if answer == float('inf') else answer)
