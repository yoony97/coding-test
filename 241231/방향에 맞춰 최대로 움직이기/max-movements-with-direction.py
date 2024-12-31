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

r, c = map(int, input().split())
start = (r-1,c-1)

def ispossible(point, visited):
    cr, cc = point
    current = maps[cr][cc]
    dx, dy = d2d[directs[cr][cc]]
    for step in range(1, 2 * N + 1):
        nr = cr + dx * step
        nc = cc + dy * step
        if 0 <= nr < N and 0 <= nc < N:
            if current < maps[nr][nc] and not visited[nr][nc]:
                return True
        else:
            break 
    return False

def solve(cnt, point, visited):
    global answer
    answer = max(answer, cnt)
    if not ispossible(point, visited):
        return
    
    cr, cc = point
    current = maps[cr][cc]
    dx, dy = d2d[directs[cr][cc]]
    
    for step in range(1, 2 * N + 1):
        nr = cr + dx * step
        nc = cc + dy * step
        if 0 <= nr < N and 0 <= nc < N:
            if maps[cr][cc] < maps[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = True
                solve(cnt + 1, (nr, nc), visited)
                visited[nr][nc] = False
        else:
            break  
                


visited = [[False]*N for _ in range(N)]
visited[start[0]][start[1]] = True
solve(0, start, visited)
print(answer)