N = int(input())
current = (0, 0)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(N):
    d, x = input().split()
    x = int(x)
    if d == 'N':
        cx, cy = current
        cx += dx[3]*x
        cy += dy[3]*x
    
    if d == 'E':
        cx, cy = current
        cx += dx[1]*x
        cy += dy[1]*x

    if d == 'S':
        cx, cy = current
        cx += dx[2]*x
        cy += dy[2]*x
    
    if d == 'W':
        cx, cy = current
        cx += dx[0]*x
        cy += dy[0]*x
    
    current = (cx,cy)
print(current[0], current[1])    
            