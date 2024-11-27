n, m = map(int, input().split())
ans = [
    [0] * m for i in range(n)
]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
d_num = 0

col, row = 0, 0
ans[col][row] = 1

for i in range(2, n * m + 1):
    
    nx = row + dx[d_num]
    ny = col + dy[d_num]

    if not (0 <= ny < n and 0 <= nx < m) or ans[ny][nx] != 0:
        d_num = (d_num + 1) % 4
    
    col = col + dy[d_num]
    row = row + dx[d_num]

    ans[col][row] = i

for i in ans:
    print(' '.join([str(j) for j in i]))