N, T = map(int, input().split())
ops = [i for i in input()]
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

x = N//2 
y = N//2
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
d_num = 0
ans = maps[y][x]

for d in ops:
    #print(y, x)
    if d == "L":
        d_num = (d_num - 1 + 4)%4

    if d == "R":
        d_num = (d_num + 1 )%4

    if d == "F":
        nx = x + dx[d_num]
        ny = y + dy[d_num]

        if 0 <= nx < N and 0 <= ny < N:
            
            x += dx[d_num]
            y += dy[d_num]
            ans += maps[y][x]

print(ans)