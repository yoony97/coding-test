from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
# Write your code here!
#빙하 1, 물 0
#빙하로 둘러쌓일 경우 물이 빙하를 못녹임
#물과 빙하가 붙어있으면 물이 빙하를 녹임

#일단, 둘러쌓는가? 확인해야함
#1에 대한 그룹을 구하고 둘러쌓는지 확인
#둘러쌀 경우 effect = false 로 변경,
#if effect라면, 주변에 빙하를 녹임

def check(a):
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                return False
    return True




def effect(iseffect):
    new_a  =  [[a[i][j] for j in range(m)] for i in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if iseffect[i][j]:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and new_a[nx][ny] == 1:
                        new_a[nx][ny] = 0
                        cnt += 1
    return new_a, cnt


def simulate(a):
    visited = [[False]*m for i in range(n)]
    queue = deque()
    iseffect = [[True]*m for i in range(n)]
    # 1️⃣ 테두리에 있는 0을 찾아 BFS 탐색 시작
    for i in range(n):
        for j in range(m):
            if (i == 0 or j == 0 or i == n - 1 or j == m - 1) and a[i][j] == 0:
                queue.append((i, j))
                visited[i][j] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0 and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                iseffect[i][j] = False
    #print(iseffect)
    return effect(iseffect)

time = 0
while not check(a):    
    time += 1
    a, cnt = simulate(a)
    
print(time, cnt)
