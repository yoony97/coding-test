N = int(input())
x, y = 0, 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
d_num = 0
ans = 0
find = False
for i in range(N):
    #print(x, y)
    d, c = input().split()
    c = int(c)
    if d == 'W':
        d_num = 2
    elif d == 'S':
        d_num = 1
    elif d == 'E':
        d_num = 0
    else:
        d_num = 3
    for k in range(c):
        x += dx[d_num]
        y += dy[d_num]
        ans += 1
        if x == 0 and y == 0:
            find = True
            break
    if find:
        break
if find:
    print(ans)
else:
    print(-1)
