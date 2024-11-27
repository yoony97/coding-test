x, y = 0, 0
dx = [0, 1, 0 , -1]
dy = [1, 0, -1, 0]
d_num = 2
ans = 0
ops = [i for i in input()]
find = False
for op in ops:
    #print(x, y)
    ans += 1
    if op == 'L':
        d_num = (d_num - 1 + 4)%4
    elif op == 'R':
        d_num = (d_num + 1)%4
    elif op == 'F':
        x += dx[d_num]
        y += dy[d_num]

        if x == 0 and y == 0:
            find = True
            break

if x == 0 and y == 0:
    find = True

if find:
    print(ans)
else:
    print(-1)