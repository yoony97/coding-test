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

#백트레킹 어떻게 할래?
#방향별로 다 돌아보긴 할꺼잖아.
#

def move(ma, d, visited):
    new_visited = [[ visited[i][j] for j in range(m)] for i in range(n)]
    c, x, y = ma
    for direct in directs[c-1][d]:
        cx = x
        cy = y
        while True:
            nx = cx + direct[0]
            ny = cy + direct[1]
            if 0 <= nx < n and 0 <= ny < m:
                if 0 <= arr[nx][ny] <= 5:
                    new_visited[nx][ny] = 1
                    cx = nx
                    cy = ny
                else:
                    new_visited[nx][ny] = 1
                    break
            else:
                break
    return new_visited



answer = float('inf')

def btk(idx, visited):
    global answer
    if idx == len(man):
        temp = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and arr[i][j] != 6:
                    temp += 1
        if answer > temp:
            #print(visited)
            answer = min(answer, temp)
        return
    
    for d in range(4):
        new_visited = move(man[idx], d, visited)
        btk(idx+1, new_visited)

btk(0, visited)
print(answer)



[0, 0, 0, 1, 0], 
[0, 0, 1, 1, 1], 
[0, 1, 1, 1, 1], 
[1, 1, 1, 0, 0], 
[1, 0, 1, 0, 0], 
[1, 0, 1, 0, 0], 
[1, 1, 1, 0, 0]

