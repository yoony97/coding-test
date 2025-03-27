"""

    n*n
    m개의 몬스터 
    1개의 전투로봇 (레벨 2, 1초에 상하좌우 한칸)
    - 전투로봇 레벨 < 몬스터 레벨  = 못지나감
    - 전투로봇 레벨 > 몬스터 레벨  = 처치 가능
    - 전투로봇 레벨 == 몬스터 레벨  = 지나가기만 가능

    레벨 업 기준: 본인의 레벨과 같은 수의 몬스터를 제거시 레벨 상승    
    룰
      1. 없앨 수 있는 몬스터가 있으면 없애러감
      2. 1개 이상 일 경우, 가장 가까운 몬스터 없애러 감
        2 -1. 우선순위는 가장 위 -> 가장 왼쪽
      3. 없으면 일 끝냄

"""
from collections import deque
#init
arr = []
n = int(input())
arr = [[0]*n for _ in range(n)]
start = None
current_level = 2
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] != 9:
            arr[i][j] = row[j]
        else:
            start = (i, j, 0)

#없앨 수 있는 적 찾기
def find_enemy(start):
    #못지나갈 수 있으니까 dfs로 해야함
    q = deque([start])
    visited = [[False]*n for _ in range(n)]
    visited[start[0]][start[1]] = True
    dist = [float('inf'), float('inf'), float('inf')] #x, y, t
    while q:
        x, y, t= q.popleft()
        if arr[x][y] < current_level and arr[x][y] != 0:
            if dist[-1] > t:
                dist[0], dist[1], dist[2] = x, y, t
            elif dist[-1] == t:
                #시간이 같으면 x,y가 작은 게 우선순위
                if dist[0] > x:
                    dist[0], dist[1], dist[2] = x, y, t
                elif dist[0] == x:
                    if dist[1] > y:
                        dist[0], dist[1], dist[2] = x, y, t
                    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if arr[nx][ny] <= current_level:
                    q.append((nx,ny,t+1))
                    visited[nx][ny] = True
                
    return dist

killed = 0
while True:
    enemy = find_enemy(start)
    if enemy[0] != float('inf'):
        start = tuple(enemy)
        arr[enemy[0]][enemy[1]] = 0
        killed += 1
        if killed >= current_level:
            current_level += 1
            killed = 0
    else:
        break

print(start[2])
    
