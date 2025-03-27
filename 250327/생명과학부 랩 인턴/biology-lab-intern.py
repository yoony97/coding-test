"""
6
15:19
15:26
53분
  시작 시간: 15:26
  끝난 시간: 16:19
  소요 시간: 54분
  수행시간 : 994ms
  메모리 : 59MB
  2D-deque를 써서 메모리가 많이 들고, 딥카피할 때 수행 시간이 오래걸림
  어떻게 해결할까?
  

- 곰팡이 크기, 속력
i =  0
1. 곰팡이 채취
    - i 열부터 위에서 아래로 탐색
    - 곰팡이 발견시 - 채취(빈칸이 됨)
2. 곰팡이 이동 (벽에 부딪히면 방향 바꿈/시간 소요X)
3. 한칸에 곰팡이가 두마리 이상이면 크기가 큰 곰팡이가 다른 큰 곰팡이를 모두 먹음
i+= 1 
"""
from collections import deque

n, m, k = map(int, input().split())
#arr = [[deque([])]*m for _ in range(n)] #얕은 복사가 됨
arr = [[deque() for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0] #위, #아래, 오른쪽, 왼쪽
dy = [0, 0, 1, -1]
change_d = {0:1, 1:0, 2:3, 3:2}

for _ in range(k):
    x, y, v, d, size = map(int, input().split())
    arr[x-1][y-1].append((v,d-1,size))


def move_target():
    new_arr = [[deque() for _ in range(m)] for _ in range(n)]

    for x in range(n):
        for y in range(m):
            while arr[x][y]:  # ← 한 칸에 여러 개 있을 수 있으니까 while로!
                v, d, size = arr[x][y].popleft()
                cx, cy = x, y
                for _ in range(v):
                    nx = cx + dx[d]
                    ny = cy + dy[d]
                    if not (0 <= nx < n and 0 <= ny < m):
                        d = change_d[d]
                        nx = cx + dx[d]
                        ny = cy + dy[d]
                    cx, cy = nx, ny
                new_arr[cx][cy].append((v, d, size))
    
    return new_arr

def eat():
    for x in range(n):
        for y in range(m):
            if len(arr[x][y]) >= 2:
                target = (-1, -1, -1)
                while arr[x][y]:
                    v, d, size  = arr[x][y].popleft()
                    if target[2] < size:
                        target = (v, d, size)
                #다 제거 하고 타겟만 넣음
                arr[x][y].append(target)


answer = 0

for y in range(m):
    for x in range(n):
        if arr[x][y]: #만약 곰팡이가 있다면 제거
            v, d, size = arr[x][y].popleft()
            answer += size
            break
    arr = move_target()
    eat()

print(answer)
#print(arr)
