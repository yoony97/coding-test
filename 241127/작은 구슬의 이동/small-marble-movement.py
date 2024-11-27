n, t = map(int, input().split())
y, x, d = input().split()

x, y = int(x), int(y)
current = (x, y)
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
if d == "U":
    dn = 0
if d == "D":
    dn = 3
if d == "R":
    dn = 1
if d == "L":
    dn = 2

for i in range(t+1):
    
    x, y = current
    cx = x + dx[dn]
    cy = y + dy[dn]
    
    if not (1 <= cx < n and 1 <= cy < n):
        dn = 3 - dn
    else:
        current = (cx, cy)
    #print(current)

print(current[1], current[0])