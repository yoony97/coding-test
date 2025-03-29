#M개의 병원을 고른다 -> 백트레킹
#상하좌우 백신 배포
from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def simulate(hist):
    doctors = deque([h for h in hist])
    traced =[]
    visited = [[False]*N for _ in range(N)]
    max_time = 0
    while doctors:
        x, y, t = doctors.popleft()
        visited[x][y] = True
        max_time = max(max_time, t)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if arr[nx][ny] == 0: #
                    doctors.append((nx,ny, t+1))
                    arr[nx][ny] = -1
                    traced.append((nx,ny))
    #다 진행 후에, 0이 남아있나 확인해야함
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                #불가능 하다.
                return float('inf'), traced



    return max_time, traced

def recovery(traced):
    for nx, ny in traced:
        arr[nx][ny] = 0
    
answer = float('inf')
def btk(cur_num, start, hist):
    global answer
    if cur_num == M:
        max_time, traced = simulate(hist)
        answer= min(max_time, answer)
        recovery(traced)
        return

    for i in range(start, len(total)):
        hist.append(total[i])
        btk(cur_num+1, i, hist)
        hist.pop()

N, M = map(int, input().split())
arr = [ ]
total = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 2:
            total.append((i,j,0))
    arr.append(row)

btk(0, 0, [])
if answer == float('inf'):
    answer = -1

print(answer)