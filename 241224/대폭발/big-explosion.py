n, m, r, c = map(int, input().split())
arr = [[0]*n for i in range(n)]

r -= 1
c -= 1

arr[r][c] = 1

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for t in range(1, m+1):    
    rnge = 2**(t-1)
    copy  = [[arr[i][j] for j in range(n)] for i in range(n)]
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 1:
                for i in range(4):
                    nr = r + rnge*(dx[i])
                    nc = c + rnge*(dy[i])
                    if 0 <= nr < n and 0 <= nc < n:
                        copy[nr][nc] = 1
    arr = copy


cnt = 0
for i in range(n):
    for j in range(n):
        #print(arr[i][j], end ="  ")
        if arr[i][j] == 1:
            cnt += 1
    #print()

print(cnt)