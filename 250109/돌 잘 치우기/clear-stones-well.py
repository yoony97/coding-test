from collections import deque
dxs = [0, 0, -1, 1]
dys = [1, -1, 0, 0]
n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
answer = 0
r = []
c = []
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)

# Write your code here!
# 1이 돌이야

def backtrack(cur_num, m):
    if cur_num == m:
        bfs()
        return
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                grid[i][j] = 0
                backtrack(cur_num+1, m)
                grid[i][j] = 1

def bfs():
    global answer
    visited = [[False]*n for i in range(n)]
    cnt = 0
    for i in range(k):
        cx, cy = r[i]-1, c[i]-1
        if not visited[cx][cy]:
            visited[cx][cy] =  True
            queue = deque([(cx,cy)])
            cnt += 1
        while queue:
            cx, cy = queue.popleft()
            for i in range(4):
                nx = cx + dxs[i]
                ny = cy + dys[i]
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and not visited[nx][ny] :
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    cnt+=1
    answer = max(cnt, answer)

backtrack(0, m)
print(answer-1)