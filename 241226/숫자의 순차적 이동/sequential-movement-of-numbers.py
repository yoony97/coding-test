dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n, m = map(int, input().split())
arr = []

def find_idx(arr, target):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == target:
                return (i, j)

for _ in range(n):
    arr.append(list(map(int, input().split())))


for _ in range(m):
    for target_num in range(1, n*n+1):
        x, y = find_idx(arr, target_num)
        max_value = 0
        rx = -1
        ry = -1
        
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if max_value < arr[nx][ny]:
                    rx = nx
                    ry = ny
                    max_value = arr[nx][ny]
        
        #print(rx, ry, x, y, arr[x][y], arr[rx][ry])
        if rx >= 0 and ry >= 0:
            temp = arr[x][y]
            arr[x][y] = arr[rx][ry]
            arr[rx][ry] = temp
            #arr[rx][ry], arr[x][y] = arr[x][y], arr[rx][ry]
            

for i in range(n):
    for j in range(n):
        print(arr[i][j], end =' ')
    print()    

        
