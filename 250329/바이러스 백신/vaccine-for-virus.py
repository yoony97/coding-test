#M개의 병원을 고른다 -> 백트레킹
#상하좌우 백신 배포
from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
arr = [ ]
total = []
isexist = False
answer = float('inf')

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 0:
            isexist = True
        if row[j] == 2:
            total.append((i,j,0))
    arr.append(row)


def simulate(hist):
    doctor = deque([i for i in hist])
    new_arr = [[arr[i][j] for j in range(N)] for i in range(N)]
    visited = [[False]*N for _ in range(N)]
    max_time = 0

    while doctor:
        x, y, t = doctor.popleft()
        visited[x][y] = True
        if arr[x][y] == 0: #바이러스 칸에서 정화 했을 경우
            max_time = max(max_time, t)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if new_arr[nx][ny] == 0:
                    doctor.append((nx, ny, t+1))
                    new_arr[nx][ny] = -1
                elif new_arr[nx][ny] == 2:
                    doctor.append((nx, ny, t))
                
    

    for i in range(N):
        for j in range(N):
            if new_arr[i][j] == 0:
                return float('inf')
    return max_time


def btk(start, hist):
    global answer 
    if len(hist) == M:
        max_time = simulate(hist)    
        answer = min(answer, max_time)
        return
    
    for i in range(start, len(total)):
        hist.append(total[i])
        btk(i+1, hist)
        hist.pop()

btk(0, [])
if answer == float('inf'):
    answer = -1

print(answer)
                

    
