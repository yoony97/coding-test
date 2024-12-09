dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

#R: direct -=1
#L: direct +=1

N, T = map(int, input().split())
ops = list(map(str, input()))
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))
total = maps[N//2][N//2]
current = (N//2, N//2)
direct = 0
#print(current)
for i in ops:
    #print(direct)
    if i == 'L':
        direct = (direct + 1)%4
    elif i == 'R':
        direct = (direct - 1+4)%4
    elif i == 'F':
        x, y = current 
        nx = x + dx[direct]
        ny = y + dy[direct]
        if 0 <= nx < N and 0<= ny < N:
            #print(nx, ny, maps[nx][ny])
            current = (nx, ny)
            total += maps[nx][ny]

print(total)