n = int(input())
ans = [
    [0] * n for i in range(n)
]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
d_num = 0

col, row = n-1, n-1
ans[col][row] = n*n

num = n*n

for i in range(2, n * n + 1):
    
    nx = row + dx[d_num]
    ny = col + dy[d_num]

    if not (0 <= ny < n and 0 <= nx < n) or ans[ny][nx] != 0:
        d_num = (d_num + 1) % 4
    
    col = col + dy[d_num]
    row = row + dx[d_num]
    num = num - 1
    ans[col][row] = num

for i in ans:
    print(' '.join([str(j) for j in i]))