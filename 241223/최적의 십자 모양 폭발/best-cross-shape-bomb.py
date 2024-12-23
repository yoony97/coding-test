n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def boom(i,j, arr):
    rnge = arr[i][j]-1
    #print(rnge, i, j)
    for k in range(i-rnge, i+rnge+1):
        if 0 <= k < n:
            arr[k][j] = 0
    for k in range(j-rnge, j+rnge+1):
        if 0 <= k < n:
            arr[i][k] = 0
    return arr

def drop(arr):
    for i in range(n):
        temp =  []
        cnt = 0
        for j in range(n):
            if arr[j][i] != 0:
                temp.append(arr[j][i])
                arr[j][i] = 0
            else:
                cnt += 1
        idx = 0
        for k in range(cnt,n):
            arr[k][i] = temp[idx]
            idx += 1
    return arr

def check(arr):
    result = []
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(n):
        for j in range(n):
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < len(arr) and 0 <= ny < len(arr):
                    if arr[i][j] == arr[nx][ny]:
                        if [(i, j), (nx, ny)] not in result and [(nx, ny), (i,j)] not in result:
                            result.append([(i, j), (nx, ny)])
    
    return result

answer = 0

for i in range(n):
    for j in range(n):
        copy = [[arr[i][j] for j in range(n)] for i in range(n)]
        copy = boom(i,j, copy)
        copy = drop(copy)
        result = check(copy)
        answer = max(len(result), answer)
        
        
print(answer//2)