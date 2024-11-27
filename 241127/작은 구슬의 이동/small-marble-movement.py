n, t = map(int, input().split())
x, y, d = input().split()

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

for i in range(t):
    x, y = current
    cx = x + dx[dn]
    cy = y + dy[dn]
    
    if not (0 <= cx < n and 0 <= cy < n):
        dn = 3 - dn
    
    current = (x+ dx[dn], y+dy[dn])

print(current[0], current[1])