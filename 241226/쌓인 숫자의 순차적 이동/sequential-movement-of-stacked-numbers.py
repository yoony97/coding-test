n, m = map(int, input().split())
arr = []


def find_idx(arr, target):
    for i in range(n):
        for j in range(n):
            for l in range(len(arr[i][j])):
                if arr[i][j][l] == target:
                    return (i, j, l)


for _ in range(n):
    temp = list(map(int, input().split()))
    temps = []
    for i in temp:
        temps.append([i])
    arr.append(temps)


target = list(map(int, input().split()))

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in target:
    x, y, h = find_idx(arr, i)
    max_value = -1
    rx = -1
    ry = -1
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            for j in range(len(arr[nx][ny])):
                if max_value < arr[nx][ny][j]:
                    max_value = arr[nx][ny][j]
                    rx = nx
                    ry = ny
    #위치는 찾았어
    if rx >= 0 and ry >= 0:
        temp = arr[x][y][h:]
        arr[rx][ry].extend(temp)
        arr[x][y] = arr[x][y][:h]

for i in range(n):
    for j in range(n):
        if len(arr[i][j]) == 0:
            print("None")
        else:
            for l in range(len(arr[i][j])-1, -1, -1):
                print(arr[i][j][l], end =' ')
            print()  
                
