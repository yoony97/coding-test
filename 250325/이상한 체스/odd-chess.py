#방향에 따라 결정됨
#방향에 영향을 받는거1,2,3,4번 말

n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]
man = []

# 0:북, 1: 동, 2: 남, 3:서
directs = [
    #1번말에 대한 방향
    {0: [(-1, 0)],
     1: [(0, 1)],
     2: [(1, 0)],
     3: [(0, -1)]}, 
    #2번말에 대한 방향
    {
        0:[(0,1),(0,-1)],
        1:[(1,0),(-1,0)],
        2:[(0,1),(0,-1)],
        3:[(1,0),(-1,0)]
    },
    #3번말에 대한 방향
    {
        0:[(-1,0),(0,1)],
        1:[(0,1),(1,0)],
        2:[(1,0),(0,-1)],
        3:[(-1,0),(0,-1)]
    },
    {
        0:[(-1,0),(0,1),(0,-1)],
        1:[(-1,0),(1,0),(0,1)],
        2:[(1,0),(0,1),(0,-1)],
        3:[(0,-1),(1,0),(-1,0)]
    },
    {
        0:[(-1,0),(0,1),(0,-1), (1,0)],
        1:[(-1,0),(0,1),(0,-1), (1,0)],
        2:[(-1,0),(0,1),(0,-1), (1,0)],
        3:[(-1,0),(0,1),(0,-1), (1,0)]
    }
]
    



for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        arr[i][j] = row[j]
        if 1 <= row[j] <= 5:
            man.append((row[j], i, j))
            visited[i][j] = 1


def move_inplace(ma, d, visited, trace):
    c, x, y = ma
    for direct in directs[c-1][d]:
        cx, cy = x, y
        while True:
            nx = cx + direct[0]
            ny = cy + direct[1]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 6:
                    break
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    trace.append((nx, ny))
                cx, cy = nx, ny
            else:
                break

answer = float('inf')
def btk(idx):
    global answer
    if idx == len(man):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and arr[i][j] != 6:
                    cnt += 1    
        

        answer = min(answer, cnt)
        return

    for d in range(4):
        trace = []
        move_inplace(man[idx], d, visited, trace)
        btk(idx + 1)
        for x, y in trace:  # 원복
            visited[x][y] = 0
btk(0)
print(answer)



