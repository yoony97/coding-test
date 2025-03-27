"""
시작 시간 14:05
nxn 에 먼지가 존재
청소기는 1번 열에 설치 크기는 2칸
1초동안
 1. 먼지가 인접한 4방향의 상하좌우로 해당 칸의 먼지량//5 확산됨(청소기가 있으면 x)
    - 원래 칸의 먼지는 확산된 량 만큼 제거
    - 확산 뒤, 확산된 만큼 해당칸에 먼지량 더해짐
 2. 청소기 운행
    1. 윗칸에서는 반시계 방향, 아래칸에서는 시계 방향
    2. 먼지가 바람의 방향대로 한칸씩 이동
    3. 돌풍으로 들어간 먼지는 삭제


"""

n, m, t = map(int, input().split())
arr = [[0]*m for _ in range(n)]
wind = [-1, -1]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        arr[i][j] = row[j]
        if row[j] == -1  and wind[0] == -1:
            wind[0], wind[1] = i, j
    
        
def spread():
    spread_arr = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if arr[x][y] != -1:
                temp = arr[x][y]//5
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != -1:
                        spread_arr[nx][ny] += temp
                        arr[x][y] -= temp

    for x in range(n):
        for y in range(m):
            arr[x][y] += spread_arr[x][y]
def rotated_up():    
    up_x, up_y = wind
    down_x, down_y = wind[0]+1, wind[1]
    arr[up_x][up_y] = 0
    arr[down_x][down_y] = 0
    #반시계 방향
    #1. up_x, up_y -> up_x, m 까지 한칸식 밀기
    #즉, arr[up_x][i] = arr[up_x][i-1]
    up_temp = arr[up_x][-1]
    for i in range(m-1, up_y, -1):
        arr[up_x][i] = arr[up_x][i-1]
    
    #2. up_x-1, m-1 부터 0, m-1 까지 위로 밀어야함
    # arr[i][m-1] = arr[i+1][m-1]
    up_temp2 = arr[0][m-1]
    for i in range(0, up_x-1):
        arr[i][m-1] = arr[i+1][m-1]
    arr[up_x-1][m-1] = up_temp    

    #3. 0, m-2부터  0, 0까지 좌측으로 밀어야함
    up_temp3 = arr[0][0]
    for i in range(m-1):
        arr[0][i] = arr[0][i+1]
    arr[0][m-2] = up_temp2
    #4. 1,0 부터 up_x, 0 까지 밑으로 밀어야함
    for i in range(up_x, 0, -1):
        arr[i][0] = arr[i-1][0]
    
    arr[1][0] = up_temp3
    arr[up_x][up_y] = 0
    
def rotated_down():
    up_x, up_y = wind
    down_x, down_y = wind[0]+1, wind[1]
    arr[up_x][up_y] = 0
    arr[down_x][down_y] = 0
    #시계 방향
    #1. down_x, down_y -> down_x, m 까지 한칸식 밀기
    #즉, arr[down_x][i] = arr[down_x][i-1]
    down_temp = arr[down_x][-1]
    for i in range(m-1, down_y, -1):
        arr[down_x][i] = arr[down_x][i-1]

    #2. down_x, m-1 부터 n-1, m-1 까지 아래로 밀어야함
    # arr[i][m-1] = arr[i+1][m-1]
    down_temp2 = arr[n-1][m-1]
    for i in range(n-1, down_x+1, -1):
        arr[i][m-1] = arr[i-1][m-1]
    
    arr[down_x+1][m-1] = down_temp    


    #3. n, m-2부터  0, 0까지 좌측으로 밀어야함
    down_temp3 = arr[n-1][0]
    for i in range(m-1):
        arr[n-1][i] = arr[n-1][i+1]
    arr[n-1][m-2] = down_temp2

    ##4. n-2,0 부터 down_x, 0 까지 밑으로 밀어야함
    for i in range(down_x, n-2):
        arr[i][0] = arr[i+1][0]
    
    arr[n-2][0] = down_temp3

    arr[down_x][down_y] = 0

def clean():    
    rotated_up()
    rotated_down()    
    up_x, up_y = wind
    down_x, down_y = wind[0]+1, wind[1]
    arr[up_x][up_y] = -1
    arr[down_x][down_y] = -1

        



for i in range(t):
    spread()
    #rotated_up()
    clean()
    # if i == 0:
    #     for j in range(n):
    #         print(arr[j])

up_x, up_y = wind
down_x, down_y = wind[0]+1, wind[1]
arr[up_x][up_y] = 0
arr[down_x][down_y] = 0

answer = 0
for i in range(n):
    answer += sum(arr[i])

print(answer)
