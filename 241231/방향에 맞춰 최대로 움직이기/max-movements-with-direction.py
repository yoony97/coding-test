N = int(input())
maps = []
directs = []
answer = 0
#, , →, , ↓, ↙, ←, ↖
d2d = {
    1:(-1, 0), #↑
    2:(-1, 1), #↗
    3:(0, 1),  #→
    4:(1, 1),  #↘
    5:(1, 0),  #↓
    6:(1, -1), #↙
    7:(0, -1), #←
    8:(-1, -1), #↖
}
for _ in range(N):
    maps.append(list(map(int, input().split())))


for _ in range(N):
    directs.append(list(map(int, input().split())))

def ispossible(point):
    cr, cc = point
    current = maps[cr][cc]
    dx, dy = d2d[directs[cr][cc]]
    for i in range(N):
        nr = cr + dx
        nc = cc + dy
        if 0 <= nr < N  and 0 <= nc < N:
            if current <= maps[nr][nc]:
                return True
    return False

def solve(cnt, point, visited):
    global answer
    if not ispossible(point):
        answer = max(answer, cnt)
        return
    
    cr, cc = point
    current = maps[cr][cc]
    dx, dy = d2d[directs[cr][cc]]
    
    for i in range(N):
        nr = cr + dx
        nc = cc + dy
        if 0 <= nr < N and 0 <= nc < N and current < maps[nc][nr]:
            visited[nr][nc] = True
            solve(cnt+1, (nr, nc), visited)
            visited[nr][nc] = False
    
                

def simulate():
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            visited[i][j] = True
            solve(1, (i,j), visited)
            visited[i][j] = False

simulate()

print(answer)