#L 흰, R 검
current = 0
OFFSET = 100000
maps = [0]*(2*OFFSET + 1)
li = []
n = int(input())
current = OFFSET
for _ in range(n):
    x, d = input().split()
    x = int(x)
    if d == 'L':
        right = current
        left = current - x
        current -= x
        value = -1
    else:
        right = current + x
        left = current
        value = 1
        current += x
    li.append((right, left, value))

for (right, left, value) in li:
    for i in range(left, right):
        maps[i] = value
    
white, black = 0, 0
for i in range(2*OFFSET + 1):
    if maps[i] == 1:
        white += 1
    elif maps[i] == -1:
        black += 1 

print(black, white)